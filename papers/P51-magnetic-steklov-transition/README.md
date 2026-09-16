# Uniform weak-field and small-flux asymptotics for exterior magnetic Steklov operators

**Henry Zweiman** · September 16, 2026 · P51 · Version 1.0

AI-assisted research preprint. Internally checked by the originating assistant; not independently verified by human experts or peer reviewed.

The paper gives a uniform operator expansion for planar exterior magnetic Steklov problems as field and scalar mass vanish, including the transition across integral Aharonov–Bohm flux. It derives a universal ground-state crossover, a signed-flux asymmetry and a second-order geometric gap. Every fixed smooth simply connected nondisk is strictly below the equal-perimeter disk in an obstacle-dependent small-parameter neighborhood, without symmetry or convexity assumptions.

- [Complete Markdown manuscript](manuscript.md)
- [21-page PDF](manuscript.pdf)
- [Portable LaTeX](manuscript.tex)
- [Proof and source review](REVIEW.md)
- [Priority, significance and scope assessment](ASSESSMENT.md)
- [Source audit](source-audit.json) and [download records](source-downloads.json)
- [Artifact checks](artifact-check.json), [math parsing check](markdown-math-check.json), and [SHA-256 hashes](SHA256SUMS.txt)
- [Supplementary numerical diagnostics](diagnostics/)
- [Citation metadata](CITATION.cff)

The scalar capacity expansion, classical circle spectra, Kummer identity, conformal covariance and boundary calculus are credited prior work. Thresholds depend on the obstacle; no full-field-range theorem or independent flux-vector theorem is claimed. Exact source-access limits are disclosed in the assessment.

The Markdown file is authoritative. With Pandoc and Tectonic on PATH, run `python3 build.py` to regenerate LaTeX and PDF; the LaTeX is also standalone. Diagnostic scripts require Python and NumPy, and should be run from their own directory so their sibling imports resolve. They are floating-point consistency checks only and are not needed for the proof. Third-party article PDFs are not included in this bundle.
