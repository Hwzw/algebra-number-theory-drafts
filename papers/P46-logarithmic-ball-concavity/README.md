# Positive radial series and sharp logarithmic concavity on balls

**Henry Zweiman. September 15, 2026.**

This research preprint proposes a positive-series representation throughout every ball for positive Dirichlet solutions of the logarithmic Schrodinger equation. It proves the stronger square-root-log concavity asked about in Gallo--Mosconi--Squassina's final 2026 paper, with a sharp transform exponent, and positive power concavity on each ball.

- [Full Markdown manuscript](manuscript.md)
- [Typeset PDF](manuscript.pdf)
- [LaTeX source](manuscript.tex)
- [Priority and significance assessment](ASSESSMENT.md)
- [Internal proof review](REVIEW.md)
- [Source audit](source-audit.json) and [download provenance](source-downloads.json)
- [Artifact checks](artifact-check.json), [MathJax checks](markdown-math-check.json), and [file hashes](SHA256SUMS.txt)

Ball uniqueness, the Gaussian amplitude threshold and shooting order are credited to prior work. The novelty claim concerns the global positive-series structure and its stronger concavity consequences. No arbitrary-convex-domain theorem or explicit optimal positive-power exponent is asserted.

Prepared with OpenAI Codex. This is an internally audited, unreviewed preprint; no independent human verification, absolute priority certification or journal acceptance is claimed. All consequences form one paper.

## Rebuild

Run `python3 build.py` with Pandoc and Tectonic installed on PATH. The complete Markdown is authoritative; the build creates LaTeX and PDF. No third-party source PDFs are redistributed in this package.
