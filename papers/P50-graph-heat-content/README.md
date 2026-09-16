# Heat-content maximization on compact metric graphs at every time

**Henry Zweiman**. September 15, 2026. AI-assisted research preprint; not independently verified or peer reviewed.

The proposed theorem answers the all-times question in Bifulco-Täufer's final EJP article, Remark 2.9. For every finite compact metric graph with the stated Dirichlet-Kirchhoff conditions, the equal-length Dirichlet-Neumann interval maximizes heat content at each positive time. Equality at one time characterizes the interval. A stronger concentration theorem covers arbitrary nonnegative L2 initial data.

- [Complete Markdown manuscript](manuscript.md)
- [Ten-page PDF](manuscript.pdf)
- [Portable LaTeX](manuscript.tex)
- [Priority and significance assessment](ASSESSMENT.md)
- [Internal proof audit](REVIEW.md)
- [Source comparison](source-audit.json) and [search scope](search-summary.json)
- [Artifact checks](artifact-check.json), [Markdown math validation](markdown-math-check.json), and [hash manifest](SHA256SUMS.txt)

The method uses classical graph rearrangement and implicit-time concentration comparison, credited to Friedlander and Vazquez. The one-time equality proof combines concentration with a half-time energy identity. No quantitative stability, arbitrary vertex-coupling result or heat-trace inequality is claimed. The source record includes unsuccessful follow-up searches; publication is not a novelty or correctness certificate.

`manuscript.md` is authoritative. To rebuild, install Pandoc and Tectonic and run `python3 build.py`. The script also recognizes the research workspace's bundled tool paths. No heuristic conversion of mathematical notation is used.
