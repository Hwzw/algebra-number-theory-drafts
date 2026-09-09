# Full Markdown manuscripts and conversion checks

Every paper directory contains a complete **manuscript.md**, generated from its frozen **manuscript.tex**. These are full papers, including abstracts, theorem statements, proofs, displays, tables, and bibliographies. They are not the overview summaries.

The converter is [convert_manuscripts.py](../tools/convert_manuscripts.py). The collection records are [markdown-conversion-manifest.json](markdown-conversion-manifest.json) and [markdown-math-check-manifest.json](markdown-math-check-manifest.json); each paper has matching individual records.

## Manuscripts

| Paper | Full Markdown |
|---|---|
| P01 | [Lefschetz properties of fully whiskered simplicial complexes](P01-lefschetz-classification/manuscript.md) |
| P02 | [Squarefree repair factors and optimal exponents for linear recurrences](P02-recurrence-repair/manuscript.md) |
| P03 | [Maximum-degree local permutation polynomials over the prime field](P03-local-permutation-polynomials/manuscript.md) |
| P04 | [Divisors and unique factorizations of Carlitz binomial polynomials](P04-carlitz-factorization/manuscript.md) |
| P05 | [Symbolic defect and normalization of whiskered cover ideals](P05-symbolic-defect/manuscript.md) |
| P06 | [Prime support and growth of Stirling repair factors](P06-stirling-repair/manuscript.md) |
| P07 | [Irreducible compositions in an exceptional unicritical family](P07-irreducible-compositions/manuscript.md) |
| P08 | [Componentwise polymatroidality is not preserved by homological shifts](P08-homological-shift-counterexamples/manuscript.md) |
| P09 | [Unique addition in centerless metabelian Lie algebras](P09-unique-addition/manuscript.md) |
| P10 | [Counterexamples to a conjecture on one-sided restricted sumsets](P10-restricted-sumsets/manuscript.md) |
| P11 | [Finite parameter tests for partition congruences and the surviving classes of an elongated partition conjecture](P11-partition-congruences/manuscript.md) |
| P12 | [Sharp orders of arithmetical critical groups  via canonical lattice simplices](P12-arithmetical-critical-groups/manuscript.md) |
| P13 | [Nilperiod rings and additive periods of power maps](P13-nilperiod-rings/manuscript.md) |

## Reproduction

The conversion requires Python 3.9 or later, Pandoc 3.9.0.2, and Tectonic. The local binaries live under tools/. The isolated Pandoc binary is downloaded from the official release and checked against a pinned SHA-256; its archive provenance is in [provenance.json](../tools/pandoc/provenance.json). The executable and Node dependencies are local tools, not manuscript content.

From the repository root, on macOS arm64:

    python3 tools/pandoc/install.py
    python3 tools/convert_manuscripts.py

On another platform, install the same official Pandoc version and Tectonic, then set the PANDOC and TECTONIC environment variables to their executable paths. The converter performs AUX-only LaTeX compilations in temporary directories. It neither regenerates nor edits the admitted PDFs or TeX files.

To convert a separate frozen collection, pass its individual directories and a separate manifest destination. For example:

    python3 tools/convert_manuscripts.py \
      --manifest selected_papers/markdown-conversion-manifest.json \
      selected_papers/P02-recurrence-repair

The default output name is manuscript.md; the option --output-name full.md selects another Markdown filename without changing the source. Always rerun after the author freezes revised TeX, and compare the recorded source hash. Do not treat a conversion record as certifying a subsequently edited source.

The optional independent math check uses local MathJax 3.2.2:

    npm ci --prefix tools/markdown-math-check --ignore-scripts
    node tools/check_markdown_math.cjs

Pass Markdown filenames to check a different collection. The --html option also writes local SVG-based HTML previews under each paper's markdown-qa/ directory; these previews are not the authoritative manuscripts. The package lock fixes dependency versions. The validator requires Node.js and uses the adjacent Pandoc executable.

## What the checks establish

- Authoritative LaTeX AUX labels supply equation, theorem, table, and citation numbers. Section-based theorem counters are reconstructed and compared against source labels; a plain Pandoc conversion would number them incorrectly.
- Every theorem, lemma, proposition, corollary, remark, example, and proof environment has explicit start/end coverage markers. No such body is shortened.
- The entire original expanded math sequence is compared before and after structural conversion. Custom manuscript macros are expanded into ordinary MathJax-compatible commands.
- An ordered text/math/code content fingerprint is compared between the prepared document and the Markdown read back through Pandoc. Differences fail the build, rather than being silently accepted.
- Every generated citation and cross-reference link has an existing local anchor. Bibliography entries and their original numbers are retained.
- The complete P11 certificate table retains all 35 data rows. Its eight-row result table is also retained.
- Source TeX and PDF hashes are checked before and after each conversion.
- Every Markdown formula is separately processed by local MathJax with undefined commands treated as errors. The original 13 papers contain 3,175 formulas including explicit proof-end squares; all pass.

## Deliberate presentation differences and limits

TeX pagination, running headers, font sizing, floats, manual vertical spacing, and line/page-break control are not reproduced. Theorem bodies use normal paragraph typography, with bold numbered headings. Sections retain their numbers. Proof-end squares are explicit inline math.

Numbered equations receive explicit tags. Cross-references and citations are clickable links with the same numbers as the PDF. Custom macros are expanded; mathematical meaning and source formula order are preserved. A LaTeX page-break suppression command in P10 is removed because MathJax does not implement it. Accented styled symbols receive explicit argument braces when MathJax requires them.

The P11 longtable's repeated page header appears once, and captions precede the Markdown tables. This removes only repeated pagination furniture, not a certificate row or a mathematical assertion.

GitHub's documented inline-math and fenced-math syntax is used. Local MathJax validation is not a test of GitHub's deployed configuration. Local SVG previews were generated, but a browser was unavailable for visual inspection; no live GitHub rendering or full-page visual check is claimed. The Markdown source, resolved references, and certificate table were inspected. No GitHub publication or update was performed by these utilities.

These checks certify conversion fidelity, not mathematical correctness, novelty, or publication suitability. The mathematical reviews remain separate documents.

## Tool documentation

- [Official Pandoc 3.9.0.2 release](https://github.com/jgm/pandoc/releases/tag/3.9.0.2).
- [GitHub's mathematical-expression syntax and MathJax renderer](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).
