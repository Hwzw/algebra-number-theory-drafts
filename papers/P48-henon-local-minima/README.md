# Local minimality for the generalized Neumann Hénon problem

**Henry Zweiman. September 15, 2026. Revision 1.1.**

This preprint proves strict Sobolev local minimality, modulo scaling, for radial minimizers below the known limiting Steklov threshold. The result covers q near p for every 2<p<n, and every subcritical q when n>=4 and p>2 is close to two. A common weighted space and a nonlinear convexity argument control perturbations near the degenerate gradient set.

- [Full Markdown manuscript](manuscript.md)
- [Fourteen-page typeset PDF](manuscript.pdf) and [LaTeX source](manuscript.tex)
- [Priority and significance assessment](ASSESSMENT.md)
- [Internal proof review](REVIEW.md)
- [Source audit](source-audit.json), [download provenance](source-downloads.json), and [search summary](search-summary.json)
- [Artifact checks](artifact-check.json), [MathJax checks](markdown-math-check.json), and [hashes](SHA256SUMS.txt)

The threshold formula and p=2 theorem are prior work. The equality case at the Steklov threshold remains unresolved. Revision 1.1 determines uniformity and the sharp decay power of the neighborhood. All results form one paper.

Prepared with OpenAI Codex. This is an internally audited, unreviewed preprint; no independent human verification, absolute priority certification or journal acceptance is claimed. No finite computation is used as proof.

## Rebuild

Run `python3 build.py` with Pandoc and Tectonic on PATH. The Markdown is authoritative. Third-party PDFs are not redistributed.

## Revision 1.1: size of the local-minimum neighborhood

Under unit energy normalization, Section 7 proves a uniform neighborhood up to and including the critical trace exponent. Above it, throughout the positive Steklov range, the neighborhood radius is bounded above and below by constant multiples of alpha^(-sigma), where sigma = [q(n-p)-p(n-1)]/[p(q-p)]. The lower bound retains nonlinear energy under varying-alpha weighted compactness; the upper bound uses positive localized boundary competitors. The Steklov equality case and the leading radius constant remain open.
