# P44: Corner singularities and quasiconcavity rigidity for Robin ground states

Henry Zweiman. September 15, 2026. Revision 2.0.

**AI-assisted research preprint. Not peer reviewed or independently verified.**

The manuscript proves two results concerning conjectures of Andrews, Clutterbuck and Hauer:

1. On every convex polygon that is neither tangential nor rectangular, the parameters with log-concave Robin ground state form a locally finite set. This disproves their general eventual log-concavity conjecture.
2. On every convex polyhedron in dimension at least three that is not a product of circumsolids, the ground state has a nonconvex superlevel set for every sufficiently small positive parameter. This proves their polyhedral quasiconcavity conjecture.

The second result is new in revision 2.0. The proof shows that a quasiconcave solution of the Neumann first-variation problem is quadratic. It combines the known inconsistent-normal obstruction with an open-edge mode argument, continuous-gradient regularity, a uniform energy estimate near the higher-codimension faces, and a Hessian-norm identity. The earlier prism and restricted transverse-cone results remain in the same manuscript.

- [Full Markdown manuscript](manuscript.md)
- [Twenty-page revised PDF](manuscript.pdf)
- [Portable LaTeX](manuscript.tex)
- [Priority and significance assessment](ASSESSMENT.md)
- [Internal proof review](REVIEW.md)
- [Source audit](source-audit.json), [download metadata](source-downloads.json), [artifact checks](artifact-check.json), and [checksums](SHA256SUMS.txt)

The foundational Robin perturbation, spherical spectral bound, inconsistent-normal obstruction, planar mode argument, and quadratic classification are credited to Andrews, Clutterbuck and Hauer. Other inputs include Dauge's sector regularity, Maz'ya's convex Neumann gradient estimate, and the standard convex Neumann H2 estimate. The comparison includes the August 2026 Edelen--Li preprint on non-obtuse polyhedra and the September 2026 Ye--Zhang smooth-domain theorem.

The unrestricted local transverse-cone question, exceptional polygonal parameters, and the sharp Robin fundamental gap remain outside the proved results. This is a revision of P44, not a new paper. The assessment distinguishes the manuscript's theorem claims from independent review and from the broader research program's exceptional-significance threshold.

To rebuild, install Pandoc and Tectonic on PATH and run `python3 build.py`. The authoritative source is manuscript.md. Formula parsing and PDF inspection establish artifact integrity, not proof correctness or historical priority.
