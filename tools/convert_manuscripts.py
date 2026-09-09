#!/usr/bin/env python3
"""Complete TeX to GitHub Markdown conversion with authoritative AUX numbering.

Requires tools/pandoc/pandoc and tools/tectonic/tectonic.
Writes only Markdown files and conversion records in papers/.
"""
from __future__ import annotations
import argparse
import collections
import copy
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PANDOC = Path(os.environ.get("PANDOC", ROOT / "tools/pandoc/pandoc"))
TECTONIC = Path(os.environ.get("TECTONIC", ROOT / "tools/tectonic/tectonic"))
THEOREMS = {"theorem", "lemma", "proposition", "corollary", "remark", "example", "definition"}
MARK = "ZZCONVERSIONMARK"


def sha(data):
    return hashlib.sha256(data if isinstance(data, bytes) else data.encode()).hexdigest()


def run(args, text=None):
    p = subprocess.run([str(x) for x in args], input=text, text=True, capture_output=True)
    if p.returncode:
        raise RuntimeError(p.stderr)
    return p.stdout, p.stderr.strip()


def read_latex(text):
    out, warnings = run([PANDOC, "-f", "latex", "-t", "json"], text)
    if warnings:
        raise RuntimeError("Pandoc reader warning: " + warnings)
    return json.loads(out)


def nodes(obj, kind=None):
    if isinstance(obj, dict):
        if "t" in obj and (kind is None or obj["t"] == kind):
            yield obj
        for value in obj.values():
            yield from nodes(value, kind)
    elif isinstance(obj, list):
        for value in obj:
            yield from nodes(value, kind)


def braced(text, start):
    assert text[start] == "{", (text[start:start + 40], start)
    depth = 1
    i = start + 1
    while i < len(text):
        if text[i] == "\\":
            i += 2
            continue
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if not depth:
                return text[start + 1:i], i + 1
        i += 1
    raise ValueError("Unclosed brace")


def command_arg(text, command):
    m = re.search(r"\\" + command + r"\s*(?=\{)", text)
    return braced(text, m.end())[0] if m else None


def no_comments(text):
    return re.sub(r"(?<!\\)%[^\n]*", "", text)


def anchor(key):
    return "label-" + re.sub(r"[^a-zA-Z0-9-]", "-", key)


def get_aux(source):
    with tempfile.TemporaryDirectory(prefix="manuscript-aux-") as tmp:
        run([TECTONIC, "-X", "compile", source, "--outfmt", "aux",
             "--keep-intermediates", "--outdir", tmp])
        aux = (Path(tmp) / "manuscript.aux").read_text()
    labels, cites = {}, {}
    for m in re.finditer(r"\\newlabel\{([^}]+)\}\s*(?=\{)", aux):
        fields, _ = braced(aux, m.end())
        labels[m[1]] = braced(fields, 0)[0]
    for m in re.finditer(r"\\bibcite\{([^}]+)\}\{([^}]+)\}", aux):
        cites[m[1]] = m[2]
    return labels, cites


def normalized_math(tex):
    tex = no_comments(tex)
    tex = re.sub(r"\\label\{[^}]+\}|\\tag\*?\{[^}]+\}", "", tex)
    tex = re.sub(r"\\(?:begin|end)\{equation\*?\}", "", tex)
    return re.sub(r"\s+", "", tex)


def math_sequence(ast):
    return [normalized_math(x["c"][1]) for x in nodes(ast, "Math")]


def semantic_sequence(ast):
    """Order-preserving text/math/code content, ignoring presentation wrappers."""
    out = []
    def visit(obj):
        if isinstance(obj, dict):
            t = obj.get("t")
            if t == "Str":
                out.extend(("text", x) for x in re.findall(r"\w+|[^\w\s]", obj["c"]))
                return
            if t == "Quoted":
                kind, contents = obj["c"]
                left, right = ("‘", "’") if kind["t"] == "SingleQuote" else ("“", "”")
                out.append(("text", left))
                visit(contents)
                out.append(("text", right))
                return
            if t == "Math":
                out.append(("math", obj["c"][1].strip()))
                return
            if t == "Code":
                out.append(("code", obj["c"][1]))
                return
            if t == "CodeBlock":
                attr, body = obj["c"]
                out.append(("math" if "math" in attr[1] else "codeblock", body.strip()))
                return
            if t in {"RawBlock", "RawInline"}:
                return
            if t in {"Link", "Image"}:
                visit(obj["c"][1])
                return
            if t in {"Header", "Div", "Span"}:
                visit(obj["c"][-1])
                return
            for val in obj.values():
                visit(val)
        elif isinstance(obj, list):
            for val in obj:
                visit(val)
    visit(ast["blocks"])
    return out


def prepare(source, labels, cites):
    source = no_comments(source)
    preamble, body = source.split(r"\begin{document}", 1)
    body = body.rsplit(r"\end{document}", 1)[0]
    title = command_arg(preamble, "title")
    if not title:
        m = re.search(r"\\begin\{center\}([\s\S]*?)\\end\{center\}", body)
        if not m:
            raise ValueError("No title")
        title = re.sub(r"\\(?:par|vspace\{[^}]*\}|Large|large|bfseries)", " ", m[1])
        title = re.sub(r"September 2026", "", title).strip()
        title = re.sub(r"\s+", " ", title)
    date = command_arg(preamble, "date") or ("September 2026" if "September 2026" in body[:400] else "")
    body = re.sub(r"\\begin\{center\}[\s\S]*?\\end\{center\}", "", body, count=1)
    body = body.replace(r"\maketitle", "")
    body = re.sub(r"\\vspace\*?\{[^}]+\}", "", body)
    body = body.replace(r"\begin{abstract}", r"\section*{Abstract}").replace(r"\end{abstract}", "")
    markers = {}
    def marker(kind, key):
        token = MARK + str(len(markers) + 1).zfill(5)
        markers[token] = (kind, key)
        return "\n\n" + token + "\n\n"
    body = re.sub(r"\\begin\{thebibliography\}\{[^}]+\}", r"\\section*{References}", body)
    body = body.replace(r"\end{thebibliography}", "")
    bib_order = []
    def bib(m):
        key = m[1]
        bib_order.append(key)
        return marker("anchor", "ref-" + key) + r"\noindent\textbf{[" + cites[key] + "]}" + " "
    body = re.sub(r"\\bibitem\{([^}]+)\}", bib, body)
    cited = []
    def cite(m):
        note, keys = m[1], [x.strip() for x in m[2].split(",")]
        cited.extend(keys)
        nums = ",".join(cites[key] for key in keys)
        text = "[" + nums + (", " + note if note else "") + "]"
        return r"\href{#ref-" + keys[0] + "}{" + text + "}"
    body = re.sub(r"\\cite(?:\[([^\]]*)\])?\{([^}]+)\}", cite, body)
    ref_count = 0
    def ref(m):
        nonlocal ref_count
        ref_count += 1
        value = labels[m[2]]
        if m[1] == "eqref":
            value = "(" + value + ")"
        return r"\href{#" + anchor(m[2]) + "}{" + value + "}"
    body = re.sub(r"\\(eqref|ref)\{([^}]+)\}", ref, body)
    displays = []
    def display(m):
        env, content = m[1], m[2]
        keys = re.findall(r"\\label\{([^}]+)\}", content)
        if not keys:
            raise ValueError("Numbered equation without a label")
        displays.extend(keys)
        content = re.sub(r"\\label\{([^}]+)\}",
                         lambda x: r"\tag{" + labels[x[1]] + "}", content)
        prefix = "".join(marker("anchor", anchor(key)) for key in keys)
        if env == "equation":
            return prefix + "\\[\n" + content + "\n\\]\n"
        return prefix + r"\begin{" + env + "}" + content + r"\end{" + env + "}"
    body = re.sub(r"\\begin\{(equation|align|gather)\}([\s\S]*?)\\end\{\1\}", display, body)
    # A label embedded after a longtable caption must not become a table cell.
    def table_labels(m):
        env, content = m[1], m[2]
        keys = re.findall(r"\\label\{([^}]+)\}", content)
        content = re.sub(r"\\label\{[^}]+\}", "", content)
        prefix = "".join(marker("anchor", anchor(key)) for key in keys)
        return prefix + r"\begin{" + env + "}" + content + r"\end{" + env + "}"
    body = re.sub(r"\\begin\{(table|longtable)\}([\s\S]*?)\\end\{\1\}", table_labels, body)
    within_section = bool(re.search(r"\\newtheorem\{theorem\}\{[^}]+\}\[section\]", preamble))
    counts = collections.Counter()
    env_records = []
    section = 0
    theorem = 0
    begin_re = re.compile(r"\\section(\*)?\s*\{|\\begin\{(" +
                          "|".join(sorted(THEOREMS | {"proof"})) +
                          r")\}(?:\[([^\]]*)\])?")
    def env_begin(m):
        nonlocal section, theorem
        if m[0].startswith(r"\section"):
            if not m[1]:
                section += 1
                if within_section:
                    theorem = 0
                return m[0] + str(section) + ". "
            return m[0]
        env, optional = m[2], m[3]
        counts[env] += 1
        ident = env + "-" + str(counts[env])
        if env == "proof":
            heading = optional or "Proof"
        else:
            theorem += 1
            number = f"{section}.{theorem}" if within_section else str(theorem)
            heading = env.title() + " " + number
            if optional:
                heading += " (" + optional + ")"
            label_match = re.match(r"\s*\\label\{([^}]+)\}", body[m.end():])
            label_key = label_match[1] if label_match else None
            if label_key:
                assert labels[label_key] == number, (label_key, labels[label_key], number)
            env_records.append(dict(environment=env, ordinal=counts[env], number=number,
                                    id=ident, source_label=label_key))
        return marker("begin", ident) + r"\paragraph*{" + heading + ".}"
    body = begin_re.sub(env_begin, body)
    end_counts = collections.Counter()
    def env_end(m):
        env = m[1]
        end_counts[env] += 1
        return (r"\hfill$\square$" if env == "proof" else "") + marker("end", env + "-" + str(end_counts[env]))
    body = re.sub(r"\\end\{(" + "|".join(sorted(THEOREMS | {"proof"})) + r")\}", env_end, body)
    assert counts == end_counts
    body = re.sub(r"\\label\{([^}]+)\}", lambda m: marker("anchor", anchor(m[1])), body)
    prepared = preamble + r"\begin{document}" + r"\section*{" + title + "}\n"
    if date:
        prepared += date + "\n\n"
    prepared += body + r"\end{document}"
    return prepared, markers, dict(environments=dict(counts), environment_records=env_records,
                                   references=ref_count, citations=len(cited),
                                   cited_keys=sorted(set(cited)), bibliography_keys=bib_order,
                                   equation_labels=displays, label_numbers=labels,
                                   bibliography_numbers=cites)


def convert(source, output_name="manuscript.md"):
    before_hash = sha(source.read_bytes())
    pdf = source.with_suffix(".pdf")
    pdf_hash = sha(pdf.read_bytes())
    text = source.read_text()
    labels, cites = get_aux(source)
    prepared, markers, audit = prepare(text, labels, cites)
    ast = read_latex(prepared)
    # Preserve an explicitly requested Markdown byline independently of the TeX.
    previous_report = source.parent / "markdown-conversion.json"
    if previous_report.exists():
        author = json.loads(previous_report.read_text()).get("markdown_author")
        if author:
            ast["blocks"].insert(1, {"t": "Para", "c": [{"t": "Str", "c": author}]})
            audit["markdown_author"] = author
    raw = [x for x in nodes(ast) if x["t"] in {"RawInline", "RawBlock"}]
    if raw:
        raise ValueError(f"{source.parent.name}: unconverted raw nodes {raw[:3]}")
    original_ast = read_latex(text)
    original_math = [normalized_math(x["c"][1]) for x in nodes(original_ast["meta"], "Math")]
    original_math += [normalized_math(x["c"][1]) for x in nodes(original_ast["blocks"], "Math")]
    converted_math = math_sequence(ast)
    math_without_qed = [x for x in converted_math if x != r"\square"]
    if original_math != math_without_qed:
        import difflib
        diff = list(difflib.unified_diff(original_math, math_without_qed))
        raise ValueError(f"{source.parent.name}: math coverage mismatch\n" + "\n".join(diff[:40]))
    # GFM has no table-caption element. Emit captions immediately before tables.
    # Repeated longtable page headers are presentation, not additional data rows.
    rebuilt = []
    table_records = []
    for block in ast["blocks"]:
        if block["t"] == "Table":
            block = copy.deepcopy(block)
            attr, caption, cols, head, bodies, foot = block["c"]
            caption_blocks = caption[1]
            if caption_blocks:
                caption_blocks[0]["c"] = [
                    {"t": "Strong", "c": [{"t": "Str", "c": f"Table {len(table_records)+1}."}]},
                    {"t": "Space"}] + caption_blocks[0]["c"]
                for cap in caption_blocks:
                    cap["t"] = "Para"
                rebuilt.extend(caption_blocks)
            block["c"][1] = [None, []]
            repeated = 0
            for tbody in bodies:
                if head[1] and tbody[3] and head[1][-1] == tbody[3][0]:
                    tbody[3].pop(0)
                    repeated += 1
            table_records.append(dict(columns=len(cols), body_rows=sum(len(x[3]) for x in bodies),
                                      repeated_page_headers_removed=repeated))
        rebuilt.append(block)
    ast["blocks"] = rebuilt
    audit["tables"] = table_records
    found = collections.Counter()
    layout_commands_removed = collections.Counter()
    def transform(obj):
        if isinstance(obj, list):
            return [transform(x) for x in obj]
        if not isinstance(obj, dict):
            return obj
        if obj.get("t") == "Math":
            obj = copy.deepcopy(obj)
            # Pandoc expands LaTeX's starred row break to \nobreak, which
            # MathJax does not implement. It only controls page breaking.
            layout_commands_removed["nobreak"] += len(re.findall(r"\\nobreak(?![A-Za-z])", obj["c"][1]))
            obj["c"][1] = re.sub(r"\\nobreak(?![A-Za-z])", "", obj["c"][1])
            # MathJax needs an explicit group around styled accent arguments.
            accent = r"\\(overline|widehat|hat|bar|widetilde|tilde)\\(mathbb|mathcal|mathrm|mathbf|mathfrak)\s*([A-Za-z])"
            obj["c"][1], count = re.subn(accent, lambda m: "\\" + m[1] + "{\\" + m[2] + "{" + m[3] + "}}", obj["c"][1])
            layout_commands_removed["accent_argument_groups_added"] += count
        if obj.get("t") in {"Para", "Plain"}:
            inlines = obj["c"]
            if len(inlines) == 1 and inlines[0].get("t") == "Str" and inlines[0]["c"] in markers:
                token = inlines[0]["c"]
                found[token] += 1
                kind, key = markers[token]
                html = f"<!-- end {key} -->" if kind == "end" else f'<a id="{key}"></a>'
                return {"t": "RawBlock", "c": ["html", html]}
        if obj.get("t") == "Header":
            level, attr, inlines = obj["c"]
            if level >= 4:
                return {"t": "Para", "c": [{"t": "Strong", "c": transform(inlines)}]}
            obj = copy.deepcopy(obj)
            obj["c"][0] = level + 1
        return {key: transform(val) for key, val in obj.items()}
    ast = transform(ast)
    ast["blocks"][0]["c"][0] = 1
    missing_markers = [key for key in markers if found[key] != 1]
    if missing_markers:
        raise ValueError(f"{source.parent.name}: markers not standalone: {missing_markers}")
    custom = re.findall(r"\\(?:newcommand|renewcommand|DeclareMathOperator)\*?\{\\([A-Za-z]+)\}", text)
    survivors = sorted({macro for macro in custom for m in nodes(ast, "Math")
                        if re.search(r"\\" + re.escape(macro) + r"(?![A-Za-z])", m["c"][1])})
    if survivors:
        raise ValueError(f"Unexpanded macros: {survivors}")
    md, warnings = run([PANDOC, "-f", "json", "-t", "gfm", "--wrap=none"], json.dumps(ast))
    if warnings:
        raise ValueError(warnings)
    fence = chr(96) * 3
    md = md.replace(fence + " math", fence + "math")
    if MARK in md or re.search(r"\\(?:cite|ref|eqref|label)\{", md):
        raise ValueError("Unresolved conversion marker/reference")
    roundtrip, warnings = run([PANDOC, "-f", "gfm", "-t", "json"], md)
    if warnings:
        raise ValueError(warnings)
    reread = json.loads(roundtrip)
    seq1, seq2 = semantic_sequence(ast), semantic_sequence(reread)
    if seq1 != seq2:
        import difflib
        diff = list(difflib.unified_diff([str(x) for x in seq1], [str(x) for x in seq2]))
        raise ValueError(f"{source.parent.name}: roundtrip content mismatch\n" + "\n".join(diff[:60]))
    ids = set(re.findall(r'<a id="([^"]+)"></a>', md))
    links = re.findall(r"\]\(#([^)]+)\)", md)
    missing = sorted(set(links) - ids)
    if missing:
        raise ValueError("Missing link targets: " + str(missing))
    assert sha(source.read_bytes()) == before_hash
    assert sha(pdf.read_bytes()) == pdf_hash
    target = source.with_name(output_name)
    target.write_text(md)
    audit.update(source_tex_sha256=before_hash, source_pdf_sha256=pdf_hash,
                 markdown_sha256=sha(md), markdown_bytes=len(md.encode()),
                 source_math_expressions_verified=len(original_math),
                 markdown_math_expressions=len(list(nodes(ast, "Math"))),
                 custom_macros_expanded=custom, output_name=output_name,
                 source_environment_markers_verified=len(markers),
                 semantic_roundtrip_sha256=sha(json.dumps(seq1)), roundtrip_content_equal=True,
                 standalone_anchor_targets=len(ids), warnings=[], github_live_render_inspected=False)
    audit["math_layout_normalizations"] = {k:v for k,v in layout_commands_removed.items() if v}
    (source.parent / "markdown-conversion.json").write_text(json.dumps(audit, indent=2) + "\n")
    print(source.parent.name, "PASS", len(md.encode()), "bytes,", len(original_math), "math expressions")
    return dict(paper=source.parent.name, **audit)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folders", nargs="*", type=Path)
    ap.add_argument("--output-name", default="manuscript.md")
    ap.add_argument("--manifest", type=Path)
    args = ap.parse_args()
    folders = args.folders or sorted((ROOT / "papers").glob("P[0-9][0-9]-*"))
    if Path(args.output_name).name != args.output_name or not args.output_name.endswith(".md"):
        ap.error("--output-name must be a Markdown filename, not a path")
    result = [convert(folder / "manuscript.tex", args.output_name) for folder in folders]
    manifest = dict(converter="tools/convert_manuscripts.py", converter_sha256=sha(Path(__file__).read_bytes()),
                    pandoc_version=run([PANDOC, "--version"])[0].splitlines()[0],
                    numbering_source="Tectonic AUX-only compilation in temporary directories",
                    paper_count=len(result), papers=result)
    target = args.manifest or ROOT / "papers/markdown-conversion-manifest.json"
    target.write_text(json.dumps(manifest, indent=2) + "\n")


if __name__ == "__main__":
    main()
