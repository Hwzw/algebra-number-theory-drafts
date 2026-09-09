# Rational points on connected curves cut out by quadrics

**Henry Zweiman** · September 9, 2026 · P35

[Full manuscript (Markdown)](manuscript.md) · [PDF](manuscript.pdf) · [LaTeX](manuscript.tex)

This six-page manuscript proposes a uniform point bound for reduced, geometrically connected curves set-theoretically defined by quadrics: if q >= 3 and D <= q+5, there are at most Dq+1 rational points. A sharp corollary gives 8q+1 for every complete intersection of three quadrics in projective four-space, including reducible and nonreduced intersections. This is the (d,m,k,r)=(2,4,1,3) specialization of Lin's projective largest-intersection conjecture.

The general conjecture remains unresolved. Optimality of the degree threshold is not claimed. The structural theorem, sharp corollary, and examples are one paper.

The proof and diagnostics have been internally checked by the originating AI agent. There has been no independent human or separate-agent review. Historical priority, significance, and journal readiness remain provisional; public hosting is not peer review. See the [assessment](ASSESSMENT.md) and [internal proof review](REVIEW.md).

## Reproduction

Run `python3 check.py` with standard-library Python 3. It writes `check-results.json`; runtime is machine-dependent. Compile `manuscript.tex` with Tectonic or a current LaTeX installation containing AMS packages and hyperref. The full Markdown conversion and math-validation records are included.

Checks cover exact arithmetic in seven finite fields, 32,211 projective points, transformed sharp examples, nonreduced examples, and 632,626 instances of the proof's numerical inequalities. Finite diagnostics do not establish the universal theorem. File hashes appear in [manifest.json](manifest.json).
