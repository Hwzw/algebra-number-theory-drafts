# Complete splitting of planar Robin eigenvalues by a single shrinking hole

**Henry Zweiman** · September 16, 2026 · P52 · Version 1.0

AI-assisted research preprint. Internally checked by the originating assistant; not independently verified by human experts or peer reviewed.

For a prescribed point in a bounded connected planar Lipschitz domain and a fixed nonzero real Robin parameter, the paper constructs one analytic, strictly convex, area-preserving hole shape near a disk that completely splits every fixed eigenvalue cluster when the hole is sufficiently small. The same shape works across all finite spectral windows. The size threshold depends on the window. The proof includes arbitrary-hole coefficients at every nodal order, signed nonnodal separation and quantitative correctors.

- [Complete Markdown manuscript](manuscript.md)
- [Typeset PDF](manuscript.pdf) and [portable LaTeX](manuscript.tex)
- [Proof review](REVIEW.md) and [priority and significance assessment](ASSESSMENT.md)
- [Source audit](source-audit.json) and [local retrieval inventory](source-downloads.json)
- [Artifact checks](artifact-check.json), [formula syntax check](markdown-math-check.json) and [file hashes](SHA256SUMS.txt)
- [Supplementary diagnostics](diagnostics/) and [citation metadata](CITATION.cff)

The spectral projection method, corrected Schur-complement mechanism, shape differentiation of polarization tensors and standard functional estimates are credited prior work. Some older full texts remain incompletely compared. No common positive size threshold for the entire infinite spectrum is proved. The mixed nonnodal Neumann problem is outside the theorem.

The Markdown is authoritative. With Pandoc and Tectonic on PATH, run `python3 build.py` in this directory to regenerate the LaTeX and PDF. The two diagnostic scripts require Python and mpmath; each writes its JSON results beside itself. They check finite circular sectors or synthetic matrices, and are not used to prove the PDE theorems. Third-party article PDFs are not redistributed.
