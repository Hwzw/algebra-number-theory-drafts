# Sharp total variation bounds from spherical rearrangement

**Henry Zweiman. September 15, 2026.**

This preprint proves the all-order Hilbert-space case of the Nazarov-Shcheglova variation conjecture, including the exact constant and all extremizers. A Jacobi expansion turns the constrained Green form into a positive mixture of spherical Poisson interactions. A complementary measure argument proves the constant identity and coincidence of maximizing sets at p=1.

- [Full Markdown manuscript](manuscript.md)
- [Typeset PDF](manuscript.pdf) and [LaTeX source](manuscript.tex)
- [Priority and significance assessment](ASSESSMENT.md)
- [Internal proof review](REVIEW.md)
- [Source audit](source-audit.json) and [download provenance](source-downloads.json)
- [Artifact checks](artifact-check.json), [MathJax checks](markdown-math-check.json), and [hashes](SHA256SUMS.txt)
- [Exact normalization diagnostic](check_jacobi.py) and [recorded results](jacobi-exact-check.json)

The full all-p conjecture and p=1 midpoint symmetry remain unresolved. The point-evaluation constant, spherical rearrangement theorem and spline identities are credited prior work. All results here form one paper.

Prepared with OpenAI Codex. This is an internally audited, unreviewed preprint; no independent human verification, absolute priority certification or journal acceptance is claimed.

## Rebuild

Run `python3 build.py` with Pandoc and Tectonic on PATH. The Markdown is authoritative. The package does not redistribute third-party PDFs. The rational diagnostic uses only Python's standard library; it does not prove the general theorem.
