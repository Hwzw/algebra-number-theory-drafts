# P44: Robin ground states on convex polyhedra: concavity and vanishing spectral gaps

Henry Zweiman. September 15, 2026. Revision 3.0.

**AI-assisted research preprint. Not peer reviewed or independently verified.**

The new result disproves the universal positive-Robin fundamental-gap conjecture. For every dimension at least four, fixed diameter D, and fixed Robin parameter alpha > 0, the infimum of the first-to-second eigenvalue gap over bounded convex polyhedra is zero. Section 9 supplies a complete elementary variational proof and an explicit polytope with gap below 1/100 while the comparison interval has gap above one. The same fixed domain disproves the positive-parameter gap monotonicity conjecture attributed to Smits in Laugesen's survey.

The manuscript also retains its discrete-exception disproof of eventual polygonal log-concavity and full proof of the ACH small-parameter polyhedral quasiconcavity conjecture. The new gap proof is independent of those regularity arguments.

- [Full Markdown manuscript](manuscript.md)
- [Twenty-six-page revised PDF](manuscript.pdf)
- [Portable LaTeX](manuscript.tex)
- [Priority and significance assessment](ASSESSMENT.md)
- [Internal proof review](REVIEW.md)
- [Source audit](source-audit.json), [download metadata](source-downloads.json), [artifact checks](artifact-check.json), and [checksums](SHA256SUMS.txt)

The gap proof derives uniform transverse estimates, includes the exact lateral-facet factors and end caps, bounds the ground-state mass in the middle, and uses an odd ground-state multiple to estimate the gap. Diameter normalization is exact. No numerical eigenvalues are used. Known Minkowski volume/surface phenomena, negative-Robin gap degeneration, interval and rectangular-box results are credited.

The positive-gap and gap-monotonicity conjectures in dimensions two and three remain unresolved here, as do exceptional polygonal parameters and the unrestricted local transverse-cone question. This is a revision of P44, not a new paper. The assessment explains the significance judgment and the limits of internal review.

To rebuild, install Pandoc and Tectonic on PATH and run `python3 build.py`. The authoritative source is manuscript.md. Formula parsing and PDF inspection establish artifact integrity, not proof correctness or historical priority.
