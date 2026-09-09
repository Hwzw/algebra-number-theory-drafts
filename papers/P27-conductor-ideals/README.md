# Conductor ideals of C-monoids with prescribed Krull closure

**Henry Zweiman — September 9, 2026**

[Complete Markdown](manuscript.md) · [PDF](manuscript.pdf) · [LaTeX](manuscript.tex)

This paper gives an internally checked proposed characterization answering Geroldinger--Kim--Loper, arXiv:2502.21020v3, Problem 19. Extend an ideal of a Krull monoid to its free divisor monoid. Except for one unit obstruction, the ideal is realizable as a C-monoid conductor exactly when dividing that extension by individual primes gives only finitely many distinct colon ideals. Equivalently, finitely many bounded sums of prime valuations determine membership.

The proof covers infinite divisor rank and arbitrary unit groups. It constructs a realization whenever one exists, permits a prescribed subgroup of normalization units, and bounds the reduced class semigroup. Examples show why finite generation is unnecessary and why trivial divisor class group alone is insufficient.

- [Literature and scope assessment](ASSESSMENT.md)
- [Internal proof review](REVIEW.md)
- [Exact checks](check.py) and [results](check-results.json)
- [Artifact quality record](artifact-qa.json) and [file manifest](manifest.json)

Run `python3 check.py`. The checks compare exact finite monomial ideals and exhaust complete finite quotient monoids; the universal theorem is established by the written proof, including its infinite-rank argument.

The work is one consolidated manuscript. It is not a characterization of ring conductors or all intermediate Mori monoids. Review was performed by the originating agent; no separate-agent or human review is claimed. Historical priority and scholarly significance remain provisional.
