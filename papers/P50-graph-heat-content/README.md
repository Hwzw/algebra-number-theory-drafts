# Heat-content maximization on compact metric graphs at every time

**Henry Zweiman**. Revision 1.4, September 16, 2026. AI-assisted research preprint; not independently verified or peer reviewed.

The original theorem answers the all-times question in Bifulco-Täufer's final EJP article, Remark 2.9: the equal-length Dirichlet-Neumann interval maximizes heat content at each positive time, and equality at one time characterizes the interval. A stronger concentration theorem covers arbitrary nonnegative L2 initial data.

**Revision 1.1:** Theorem 7.1 treats finite nonnegative killing measures of fixed positive total mass on graphs of fixed length. The unique heat-content maximizer is the interval with all killing at one endpoint. The result includes delta-vertex interactions, nonnegative integrable potentials and singular measures, with general-data concentration comparison and one-time rigidity. Its atomic torsion corollary is prior work of Özcan-Täufer and is expressly credited.

**Revision 1.3:** Theorems 8.1-8.2 settle both joint comparisons for arbitrary finite nonnegative killing measures. The endpoint-killed interval uniquely minimizes the torsion-eigenvalue product at fixed length and total killing, and the first eigenvalue at fixed torsion and total killing. Proposition 8.3 proves a ground-state distribution bound using a weak-equation test that absorbs every killing term, followed by a cosine comparison. This replaces the one-point proof of revision 1.2.

**New in revision 1.4:** Theorem 9.1 extends both joint comparisons to the nonlinear p-Laplacian for every 1 < p < infinity and every finite nonnegative killing measure. The proof distinguishes torsion mass from homogeneous torsional rigidity, retains the finite Robin strength, and proves the same unique endpoint-interval equality case. Section 9 contains the variational construction, scalar normalization, measure limit and rigidity proof. Özcan's nonlinear Dirichlet theorem and modified-torsion construction are explicitly credited.

- [Complete Markdown manuscript](manuscript.md)
- [PDF manuscript](manuscript.pdf)
- [Portable LaTeX](manuscript.tex)
- [Priority and significance assessment](ASSESSMENT.md)
- [Internal proof audit](REVIEW.md)
- [Source comparison](source-audit.json) and [search scope](search-summary.json)
- [Artifact checks](artifact-check.json), [Markdown math validation](markdown-math-check.json), and [hash manifest](SHA256SUMS.txt)

Classical graph rearrangement and implicit-time concentration comparison are credited to Friedlander and Vazquez. The extension uses a Robin boundary inequality for cumulative resolvents and a separate equality argument for singular measures. Quantitative stability, arbitrary vertex couplings, signed potentials, weighted edge forms and heat-trace bounds remain outside the claims. This is one revised manuscript; its source comparison and internal proof audit are documented in the accompanying files.

`manuscript.md` is authoritative. To rebuild, install Pandoc and Tectonic and run `python3 build.py`. The script also recognizes the research workspace's bundled tool paths. No heuristic conversion of mathematical notation is used.
