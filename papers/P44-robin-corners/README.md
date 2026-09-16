# P44: Robin ground states on convex polyhedra: concavity and vanishing spectral gaps

Henry Zweiman. September 15, 2026. Revision 4.1.

**AI-assisted research preprint. Not peer reviewed or independently verified.**

Section 9 disproves the universal positive-Robin fundamental-gap conjecture. For every dimension at least four, fixed diameter D, and fixed Robin parameter alpha > 0, the infimum of the first-to-second eigenvalue gap over bounded convex polyhedra is zero. Section 9 supplies a complete elementary variational proof and an explicit polytope with gap below 1/100 while the comparison interval has gap above one. The same fixed domain disproves the positive-parameter gap monotonicity conjecture attributed to Smits in Laugesen's survey.

Revision 3.1 adds a distinct counterexample to Laugesen's spectral-ratio monotonicity conjecture. Section 10 derives an exponential gap bound, places the Robin ratio below the Dirichlet ratio on the same convex polyhedron, and then uses the fixed-domain Robin-to-Dirichlet limit. The Dirichlet fundamental-gap theorem is an explicitly credited prior input. An explicit member works without numerical eigenvalue computation.

Revision 4.0 adds a counterexample to the second-eigenvalue concavity conjecture, Laugesen C. A convex asymmetric thin domain has two end regions with limiting ground energies that exchange order. Section 11 proves the required spectral convergence by forms, compactness and min--max, then obtains a strict midpoint violation on one fixed domain. This completes the manuscript's answers to the separate positive-parameter conjectures A, B and C in dimensions at least four.

Revision 4.1 adds a planar first-eigenvalue result for the parameter divided by perimeter. On area-one triangles of increasing aspect ratio the positive-parameter value tends to alpha/2, while the disk has a larger value for 0 < alpha <= 4 pi. An explicit triangle at alpha=1 has value below 123/175, while the disk exceeds 12/13. For each negative alpha the functional is unbounded below even among convex triangles. Section 12 disproves the exact Conjecture D formulation in Laugesen's arXiv v1. The final journal wording was not accessible and historical priority remains qualified explicitly.

The manuscript also retains its discrete-exception disproof of eventual polygonal log-concavity and full proof of the ACH small-parameter polyhedral quasiconcavity conjecture. The new gap proof is independent of those regularity arguments.

- [Full Markdown manuscript](manuscript.md)
- [Thirty-eight-page revised PDF](manuscript.pdf)
- [Portable LaTeX](manuscript.tex)
- [Priority and significance assessment](ASSESSMENT.md)
- [Internal proof review](REVIEW.md)
- [Source audit](source-audit.json), [download metadata](source-downloads.json), [artifact checks](artifact-check.json), and [checksums](SHA256SUMS.txt)

The gap proof derives uniform transverse estimates, includes the exact lateral-facet factors and end caps, bounds the ground-state mass in the middle, and uses an odd ground-state multiple to estimate the gap. Diameter normalization is exact. No numerical eigenvalues are used. Known Minkowski volume/surface phenomena, negative-Robin gap degeneration, interval and rectangular-box results are credited.

The positive-gap, gap-monotonicity and ratio-monotonicity conjectures in dimensions two and three remain unresolved here. Second-eigenvalue concavity in dimensions two and three, exceptional polygonal parameters and the unrestricted local transverse-cone question are also open here. This is a revision of P44, not a new paper. The assessment explains the significance judgment and the limits of internal review.

To rebuild, install Pandoc and Tectonic on PATH and run `python3 build.py`. The authoritative source is manuscript.md. Formula parsing and PDF inspection establish artifact integrity, not proof correctness or historical priority.
