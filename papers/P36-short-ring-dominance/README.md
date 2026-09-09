# Dominance and common deformations of short local rings

**Henry Zweiman** · September 9, 2026 · P36

A six-page, internally checked proposed solution to both clauses of Kobayashi–Takahashi Question 7.1. Not peer reviewed; historical priority and significance remain provisional.

The structural theorem constructs a common one-dimensional deformation for every Artinian local ring with maximal-ideal cube zero and its associated graded ring. Both quotient parameters are regular and outside the maximal-ideal square. This transfers dominance and uniform dominance in either direction, including rings without a coefficient field. Combined with Kimura's essential equicharacteristic theorem and known flat descent, it gives dominance for all non-complete-intersection Gorenstein rings with maximal-ideal cube zero or multiplicity at most embedding codimension plus two.

- [Full Markdown manuscript](manuscript.md)
- [PDF manuscript](manuscript.pdf)
- [LaTeX source](manuscript.tex)
- [Problem, priority, and significance assessment](ASSESSMENT.md)
- [Internal proof review](REVIEW.md)
- [Exact check program](check.py) and [recorded results](check-results.json)

Run `python3 check.py` with Python 3.8 or later; no third-party packages are needed. The tests cover 258 finite quotients, including 172 non-Gorenstein examples, and are diagnostics rather than a substitute for the universal proof.

This is one manuscript. It does not prove uniform dominance of all short Gorenstein rings, does not claim dominance for all non-Gorenstein short rings, and does not claim the first non-complete-intersection Gorenstein dominant examples: Kimura already constructed those. The paper was developed with AI assistance and has not received independent expert review.
