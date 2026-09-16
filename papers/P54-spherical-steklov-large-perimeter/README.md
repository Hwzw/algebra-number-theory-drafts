# A spherical Weinstock inequality at large perimeter

**Henry Zweiman** · September 16, 2026 · P54 · Version 1.0

AI-assisted research preprint. Internally checked by the originating assistant; not independently verified by human experts or peer reviewed.

For every dimension at least three, the manuscript gives a proposed proof that balls maximize the first nonzero Steklov eigenvalue among smooth geodesically convex domains of fixed boundary measure sufficiently close to equatorial area. Equality holds only for balls. The interval is uniform over all such shapes. The argument includes a harmonic boundary center, quantitative hemispherical stability, a strict lune comparison, and treatment of collapsed convex limits.

- [Complete Markdown manuscript](manuscript.md)
- [Typeset PDF](manuscript.pdf) and [portable LaTeX](manuscript.tex)
- [Proof review](REVIEW.md) and [priority/significance assessment](ASSESSMENT.md)
- [Source/read-scope audit](source-audit.json)
- [Artifact checks](artifact-check.json), [formula check](markdown-math-check.json), and [file hashes](SHA256SUMS.txt)
- [Supplementary diagnostics](diagnostics/) and [citation metadata](CITATION.cff)

The full spherical fixed-perimeter conjecture remains open in this work. The interval size is nonexplicit. Standard harmonic separation, Euclidean local-stability methods, spherical centroid precedents, and Crofton theory are credited. Some final journal full-text comparisons remain incomplete, as recorded in the source audit.

The work was prepared with OpenAI Codex, including problem selection, proof development, literature searches, diagnostics, and drafting, under the requested Henry Zweiman byline. That byline and GitHub hosting do not establish human verification.

The Markdown is authoritative. With Pandoc and Tectonic on PATH, run `python3 build.py` in this folder to regenerate LaTeX and PDF. The diagnostic scripts require Python, NumPy and SymPy; run `verify_harmonic_center.py`, `verify_hemisphere_profiles.py`, and `verify_lune_comparison.py` inside `diagnostics/`. They write JSON beside themselves. Their finite checks do not prove the universal theorem or novelty. Third-party article PDFs are not redistributed.
