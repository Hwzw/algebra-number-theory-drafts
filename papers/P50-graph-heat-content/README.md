# Heat-content maximization on compact metric graphs at every time

**Henry Zweiman**. Revision 1.1, September 16, 2026. AI-assisted research preprint; not independently verified or peer reviewed.

The original theorem answers the all-times question in Bifulco-Täufer's final EJP article, Remark 2.9: the equal-length Dirichlet-Neumann interval maximizes heat content at each positive time, and equality at one time characterizes the interval. A stronger concentration theorem covers arbitrary nonnegative L2 initial data.

**New in revision 1.1:** Theorem 7.1 treats finite nonnegative killing measures of fixed positive total mass on graphs of fixed length. The unique heat-content maximizer is the interval with all killing at one endpoint. The result includes delta-vertex interactions, nonnegative integrable potentials and singular measures, with general-data concentration comparison and one-time rigidity. Its atomic torsion corollary is prior work of Özcan-Täufer and is expressly credited.

- [Complete Markdown manuscript](manuscript.md)
- [PDF manuscript](manuscript.pdf)
- [Portable LaTeX](manuscript.tex)
- [Priority and significance assessment](ASSESSMENT.md)
- [Internal proof audit](REVIEW.md)
- [Source comparison](source-audit.json) and [search scope](search-summary.json)
- [Artifact checks](artifact-check.json), [Markdown math validation](markdown-math-check.json), and [hash manifest](SHA256SUMS.txt)

Classical graph rearrangement and implicit-time concentration comparison are credited to Friedlander and Vazquez. The extension uses a Robin boundary inequality for cumulative resolvents and a separate equality argument for singular measures. Quantitative stability, arbitrary vertex couplings, signed potentials, heat-trace bounds and a sharp Kohler-Jobin product inequality remain outside the claims. This is one revised manuscript; its source comparison and internal proof audit are documented in the accompanying files.

`manuscript.md` is authoritative. To rebuild, install Pandoc and Tectonic and run `python3 build.py`. The script also recognizes the research workspace's bundled tool paths. No heuristic conversion of mathematical notation is used.
