# Source and contribution assessment

Henry Zweiman. September 9, 2026. Internal assessment.

## Target and status

The target is an effective uniform decay bound for a product at two fixed
multiplicatively independent Pisot or Salem parameters, including
nonrational parameters and algebraic rescalings. The proposed result is
`exp(-c log log u / log log log u)`, with computable positive constants.

This quantitative target was formulated in the research program. The
audit did not locate an explicit published open question with precisely
these hypotheses and this rate. It is therefore presented as a proposed
quantitative contribution, not as a certified solution to a named open
problem. The absence of a matching search result does not prove novelty.

## Primary sources checked

- [Senge–Straus (1973), full primary paper](https://doi.org/10.1007/BF02018464), eight pages, Theorem 2 on p. 96: the qualitative Pisot Fourier-product criterion is already present. The complete paper was read. Its base-two degeneracy requires care in an iff formulation. Our theorem only gives a sufficient condition and includes base two harmlessly. The classical theorem is not counted as a new solution.
- [Stewart (1980), author's PDF](https://uwaterloo.ca/pure-mathematics/sites/default/files/uploads/documents/j-reine-ange-math-1980.pdf), pp. 63–64 visually inspected: effective simultaneous digit bounds in two integer bases and digit bounds for dominant-root recurrence values. These are earlier quantitative results; the manuscript does not claim new integer-base digit bounds. The rest of the ten-page paper was not needed to establish the scope of these theorem statements and was not represented as fully read.
- [Nguyen, arXiv:2604.18875v1](https://arxiv.org/abs/2604.18875v1), introduction and Section 3 read: Theorem 1.6 already gives qualitative Pisot decay with algebraic main terms. Theorem 1.2 cannot be used to establish that the qualitative question was still open in 2026, in view of Senge–Straus. Its approximation method is explicitly credited. The present projection proof keeps the height and error estimates uniform as the interval ratio grows.
- [Marshall-Maldonado–Solomyak, arXiv:2601.15035v1](https://arxiv.org/abs/2601.15035v1), Appendix B read: Corollary B.1 gives `A exp(-C log* u)` for one Salem Bernoulli convolution. Our theorem is for a pair of independent parameters. It neither supersedes that single-factor theorem nor proves a better single-factor rate.
- [Varjú–Yu, arXiv:2004.09358v2](https://arxiv.org/abs/2004.09358v2), introduction and Theorem 1.10 read: a `log log x` lower bound for digit changes in one base at two arguments requires their ratio outside the base field and not Liouville over it. It does not directly cover two different bases at the same argument. Their Corollary 1.6 excludes Pisot and Salem parameters. Their self-similar results with differing contractions concern a different measure equation from the convolution here.
- [Bugeaud–Mignotte–Siksek (2006), Annals full text](https://annals.math.princeton.edu/wp-content/uploads/annals-v163-n3-p05.pdf), Section 9.1, pp. 988–989: Theorem 9.4 gives the exact multiplicative Matveev bound used. The number field and two parameter heights are fixed, leaving one varying algebraic height. The original Matveev paper was not directly read; this primary research paper's formulation is the stated dependency.
- [Solomyak (2022), journal PDF](https://ems.press/content/serial-article-files/37359), Section 1, especially Theorems 1.2–1.3: power Fourier decay outside a measure-zero set of diagonal parameter vectors. Those generic theorems do not establish the assertion for the specified exceptional algebraic parameters considered here. The text also explains why the cited nonhomogeneous self-affine criteria do not hold for a homogeneous self-affine system.

An earlier Nazarov–Peres–Shmerkin paper also attributes the qualitative
Pisot product result to Senge–Straus. This provided a discovery route;
the attribution was then checked against the full 1973 source itself.
Downloaded sources and SHA-256 values are preserved in the private
research notes; third-party PDFs are not republished in this folder.

## Contribution and decision

The proposed contribution is a uniform effective joint fractional-part
obstruction. Every pair of geometric index intervals contains a large
distance. Taking their ratio proportional to the logarithm of the
exponent absorbs the varying-height cost in Matveev's theorem. Exact
resonance is excluded separately by an effective height norm on the
rank-two multiplicative group. This yields many disjoint contracting
factors and works with unit-circle conjugates as well as strictly
contracting conjugates.

Searches on September 9, 2026 covered the exact classical title,
Senge–Straus with effective/Fourier/Pisot keywords, quantitative products,
independent Pisot–Salem parameters, digit changes, linear forms in
logarithms, and homogeneous self-affine decay. No matching uniform
two-parameter theorem was located in the sources inspected. This is
bounded literature evidence, not an exhaustive priority certificate.

The proof and comparison justify release as a proposed research
preprint. They do not justify adding one to a certified count of
significant solved open problems. The underlying arithmetic estimate
may be useful in studying arithmetic convolutions at fixed parameters;
no citation count or future impact is predicted.

The weaker qualitative statements, the measure corollary, and the example
belong to this one manuscript. Power decay, sharp rates, single-Salem
improvements, and absolute continuity remain outside its conclusions.
