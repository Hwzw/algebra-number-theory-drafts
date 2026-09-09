# Failure of the length-set structure theorem for weakly C-monoids

**Henry Zweiman - September 9, 2026**

[Complete Markdown](manuscript.md) · [PDF](manuscript.pdf) · [LaTeX](manuscript.tex)

This six-page paper gives an internally checked proposed negative answer to Geroldinger-Kim-Loper, arXiv:2502.21020v3, Problem 20. It constructs a weakly C-monoid with factorial complete integral closure, a conductor principal in that closure, and distance set exactly `{1,2}`, whose length sets fail the Structure Theorem for Sets of Lengths.

The proof includes the Mori property, all factorization-length formulas, and a quantitative obstruction valid for every AAMP difference. It depends on hand arguments; finite computation supplies additional checks. The theorem concerns weakly C-monoids under the exact definition cited in the problem. No counterexample under an additional local-tameness assumption or the stronger condition (C) is asserted.

- [Literature and scope assessment](ASSESSMENT.md)
- [Internal proof review](REVIEW.md)
- [Reproducible checks](check.py) and [results](check-results.json)
- [Artifact quality record](artifact-qa.json) and [file manifest](manifest.json)

Run `python3 check.py`; no external Python packages are needed. This is one consolidated manuscript. The originating agent performed the proof review; no separate-agent or human review is claimed. Historical priority and scholarly significance remain provisional.
