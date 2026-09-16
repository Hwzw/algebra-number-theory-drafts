# Ground-state uniqueness on convex domains and sharp logarithmic concavity on balls

**Henry Zweiman. September 16, 2026. Revision 1.2.**

The new theorem proves uniqueness of the positive logarithmic Schrodinger ground state on every bounded convex domain, in every dimension and without boundary smoothness assumptions. Every positive log-concave solution is that ground state. A Gaussian-strength logarithmic Hessian bound and a sharp energy inequality with a complete equality case answer the ground-state questions in Gallo-Mosconi-Squassina, Remark 1.6 (2026).

The manuscript retains the positive radial series, sharp normalized square-root-log concavity and positive power concavity on balls. Its convex-deformation counterexamples are now identified as ground states.

- [Complete Markdown manuscript](manuscript.md), [typeset PDF](manuscript.pdf), and [LaTeX](manuscript.tex).
- [Contribution and scope](ASSESSMENT.md) and [internal proof review](REVIEW.md).
- [Ground-state source audit](ground-state-source-audit.json), [deformation source audit](deformation-source-audit.json), [original source audit](source-audit.json), and [download provenance](source-downloads.json).
- [Artifact checks](artifact-check.json), [MathJax checks](markdown-math-check.json), and [hashes](SHA256SUMS.txt).

Uniqueness among all positive solutions remains open: the proof does not exclude positive solutions of greater energy. The optimal ball power exponent remains implicit. The deformation result concerns normalization by the maximum and does not disprove the weaker small-rescaling half-log-concavity property.

This is one internally audited, AI-assisted, unreviewed preprint. It is a revision, not another distinct paper. No independent expert verification, exhaustive priority certification or journal acceptance is claimed. The proofs are by hand.

## Rebuild

Run `python3 build.py` with Pandoc and Tectonic on PATH. Markdown is authoritative. No third-party source PDFs are redistributed.
