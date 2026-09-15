# Boundary selection for low-temperature logarithmic Sobolev constants

Henry Zweiman. September 15, 2026.

A 13-page research preprint giving a proposed sharp first-order low-temperature logarithmic Sobolev expansion for convex quadratic confinement around a smooth bounded convex domain. It includes nonlinear extremizers, the spectral branch at equality, and a smooth strictly convex example requiring the nonlinear branch.

- [Complete Markdown manuscript](manuscript.md)
- [PDF](manuscript.pdf)
- [LaTeX source](manuscript.tex)
- [Priority and significance assessment](ASSESSMENT.md)
- [Proof and artifact review](REVIEW.md)
- [Dated source audit](source-audit.json)
- [Artifact hashes and checks](artifact-check.json)

Prepared with OpenAI Codex. The internal assessment supports proceeding as a substantial preprint, but does not certify correctness, historical priority, journal suitability or future citations. No independent human verification or journal acceptance is claimed.

The spectral coefficient and interval result are credited to Ben Nejma's 2026 paper. The proposed contribution is the higher-dimensional sharp entropy expansion and selection over nonlinear and spectral limiting regimes. Other normal exponents, degenerate stiffness and classification of the extremizers are not settled. All consequences here belong to this one paper.

Build with `python3 build.py` after installing Pandoc and Tectonic, or compile `manuscript.tex` directly. The source uses portable standard LaTeX packages. Run `python3 check_triangle.py` with SymPy for the exact auxiliary example checks. The authoritative Markdown contains 413 successfully parsed mathematical expressions; all 13 final PDF pages were visually inspected.
