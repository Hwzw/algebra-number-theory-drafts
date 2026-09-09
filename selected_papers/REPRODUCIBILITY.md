# Reproduction and verification

Each paper has matching TeX, PDF, and complete GitHub Markdown. All main mathematical results are hand-proved. The finite checks are diagnostics, not assumptions of the infinite theorems. The recorded proof reviews are internal AI reviews.

## Build

The local builds used Tectonic 0.17.0. From the repository root, compile a paper with:

```sh
tools/tectonic/tectonic --keep-logs selected_papers/P01-lefschetz-classification/manuscript.tex
```

Repeat with another paper folder as needed. A system installation of Tectonic can replace the first executable path. A new build may change PDF metadata and therefore its hash even when the mathematics is unchanged.

## Markdown

`tools/convert_manuscripts.py` uses Pandoc and an AUX-only Tectonic compilation in a temporary directory. It preserves full theorem and proof content, expands custom math macros, resolves numbering and references, and checks a semantic Markdown round trip. `tools/check_markdown_math.cjs` checks every formula with MathJax 3.2.2, with undefined-command errors enabled. The tools and exact runtime provenance are retained locally; installed executable binaries and node_modules are not part of a paper.

For one folder:

```sh
python3 tools/convert_manuscripts.py selected_papers/P01-lefschetz-classification --manifest /tmp/P01-markdown-manifest.json
node tools/check_markdown_math.cjs selected_papers/P01-lefschetz-classification/manuscript.md
```

The first command assumes Pandoc and Tectonic in `tools/pandoc/pandoc` and `tools/tectonic/tectonic`. The MathJax checker uses dependencies installed under `tools/markdown-math-check/` according to its package lock. The per-paper conversion report records exact TeX/PDF/Markdown hashes; the combined manifest contains all five records. GitHub's live visual renderer was not inspected during local conversion.

## Artifact audit

```sh
python3 tools/verify_selected.py
```

This checks that each current TeX/PDF/Markdown triple matches its conversion records, final source review and all-page PDF visual record. It checks that no unresolved references or build errors were recorded and regenerates `selected_papers/manifest.json`. It does not prove the mathematics or certify novelty.

PDF page images and contact sheets are in each local `qa/` directory. The `visually_reviewed` flag was set only after the root actually inspected all rendered pages. A new source/PDF build requires an updated matching record and fresh inspection.

## Supplementary mathematics

- P01 `check_extension.py`: direct multiplication matrices in the original x/y basis compared with the formula over finite fields. An independently written second checker and its hand review are in `reassessment/`.
- P02 `P02-extension-check.py`: exact local congruences and sharp witnesses for the cubic example. The inherited Lucas checks are separate diagnostics.
- P06 `P06-independent-check.py`: independent inclusion–exclusion modulo p times k factorial before exact integer division, checking the digit formula. `check_digits.py` is an earlier independent diagnostic.
- P09 and P13: complete hand proofs and fresh independent source-transfer reviews; the new structural theorems do not rely on a computation.

Running an ancillary checker may regenerate its JSON report. No finite range should be interpreted as proving an unresolved general conjecture.
