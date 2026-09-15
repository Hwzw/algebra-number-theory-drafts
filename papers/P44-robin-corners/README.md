# P44: Corner singularities obstruct eventual log-concavity of Robin ground states

Henry Zweiman. September 15, 2026.

**AI-assisted research preprint. Not peer reviewed or independently verified.**

For every bounded convex polygon that is neither tangential nor a rectangle, the manuscript proves that the positive Robin parameters with a log-concave ground state form a locally finite set. A fixed parallelogram therefore disproves eventual log-concavity on general bounded convex domains. The proof continues a first-variation corner singularity through an explicitly extracted analytic coefficient.

- [Full Markdown manuscript](manuscript.md)
- [Ten-page revised PDF](manuscript.pdf)
- [Portable LaTeX](manuscript.tex)
- [Priority and significance assessment](ASSESSMENT.md)
- [Internal proof review](REVIEW.md)
- [Source audit](source-audit.json), [download metadata](source-downloads.json), [artifact checks](artifact-check.json), and [checksums](SHA256SUMS.txt)

The initial singular mode and geometric classification are credited to Andrews, Clutterbuck and Hauer. Sector regularity uses Dauge's theorem. The new contribution is analytic persistence across the finite parameter axis and its geometric consequence. The September 2026 Ye--Zhang theorem for smooth uniformly convex domains is compatible with this polygonal result. Section 6 now proves failure of quasiconcavity on fixed prisms in every dimension at least three outside the same discrete parameter set. Exceptional parameters, tangential polygons, the full higher-dimensional small-parameter conjecture, and the sharp fundamental gap remain unresolved. This is a revision of P44, not an additional paper.

To rebuild, install Pandoc and Tectonic on PATH and run `python3 build.py`. The authoritative source is manuscript.md. Formula parsing and PDF inspection establish artifact integrity, not proof correctness or historical priority. The assessment and source audit disclose the scope and limits of the literature check.
