# P42: Euclidean persistence and sharp stability for anisotropic eigenvalue-torsion products

Henry Zweiman. September 15, 2026.

**AI-assisted research preprint. Not peer reviewed or independently verified.** The complete proof, primary-source comparison and internal audit are available for examination and correction.

The proposed theorem identifies the Euclidean norm as the unique optimizer of the first eigenvalue times a power of torsional rigidity on a fixed ball: a maximizer for sufficiently small positive product exponents, and a minimizer for sufficiently large ones. It covers all normalized symmetric seminorms, every dimension n>=2 and every energy exponent p>1. The product deficit is equivalent to an angular average and controls the uniform distance with the optimal power (n+1)/2.

- [Full Markdown manuscript](manuscript.md)
- [Ten-page PDF](manuscript.pdf)
- [Portable LaTeX source](manuscript.tex)
- [Primary-source and significance assessment](ASSESSMENT.md)
- [Internal proof review](REVIEW.md)
- [Source audit](source-audit.json), [download metadata](source-downloads.json), [artifact checks](artifact-check.json), and [checksums](SHA256SUMS.txt)

This addresses the ball cases of the Euclidean-optimality questions in Buttazzo and Fernandes Horta, Section 6. Their quadratic-seminorm ball result and classical convex symmetrization are credited. General fixed domains, asymmetric anisotropies, optimal product-exponent thresholds and endpoint-uniform p estimates remain outside the theorem. Both regimes and the nonlinear extension form one paper.

To rebuild, install Pandoc and Tectonic on PATH and run `python3 build.py`. The authoritative source is manuscript.md. Local MathJax parsing and PDF rendering do not certify mathematical correctness or reproduce GitHub's live renderer. No numerical experiments enter the proof.
