# Sharp logarithmic concavity on balls and its instability under convex deformation

**Henry Zweiman. September 16, 2026. Revision 1.1.**

The positive radial series proves sharp normalized square-root-log concavity and positive power concavity on every ball. The new theorem shows that the normalized square-root-log property fails under arbitrarily small smooth uniformly convex deformations near every ball in dimensions at least two. An explicit degree-three boundary deformation gives positive solutions that remain strictly log-concave but fail the stronger property arbitrarily close to their unique maximum.

- [Complete Markdown manuscript](manuscript.md), [typeset PDF](manuscript.pdf), and [LaTeX](manuscript.tex).
- [Priority and scope assessment](ASSESSMENT.md) and [internal proof review](REVIEW.md).
- [Original source audit](source-audit.json), [deformation source comparison](deformation-source-audit.json), and [download provenance](source-downloads.json).
- [Artifact checks](artifact-check.json), [MathJax checks](markdown-math-check.json), and [hashes](SHA256SUMS.txt).

The new result concerns the factor 1/maximum(u). It does not disprove the weaker half-log-concavity notion that permits sufficiently small rescaling. Ball uniqueness, the Gaussian threshold and shooting order remain credited prior work. The optimal positive-power exponent and its radius dependence in higher dimensions remain open. The implicit-function theorem gives a nearby solution branch, not a classification of all solutions on general domains.

This is one internally audited, unreviewed preprint. No independent expert verification, exhaustive priority certification or journal acceptance is claimed. The proof is by hand; no numerical PDE calculation is used as proof.

## Rebuild

Run `python3 build.py` with Pandoc and Tectonic on PATH. Markdown is authoritative. No third-party source PDFs are redistributed.
