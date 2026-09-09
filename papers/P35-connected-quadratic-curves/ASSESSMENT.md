# Source, novelty, and significance assessment

Date: September 9, 2026. Author: Henry Zweiman. Assessment by the originating AI agent, not an independent referee.

## Published question and exact scope

[Yuxin Lin, arXiv:2608.17771v1](https://arxiv.org/abs/2608.17771v1), Conjecture 1.5, predicts a dimension-constrained maximum for common zeros of homogeneous forms. For complete intersections of r=m-k forms of degree d, it predicts d^r q^k + pi_(k-1)(q), for q >= d+1. Theorem 1.8 proves the codimension-two case. The introduction explicitly distinguishes the general complete-intersection question from unrestricted systems of quadrics.

P35 proposes the sharp specialization (d,m,k,r)=(2,4,1,3), for all q >= 3, including nonreduced intersections. Its main theorem applies more generally to connected reduced quadratic base-locus curves in any ambient dimension when D <= q+5. The full conjecture and higher-dimensional intersections are not resolved.

The Lin introduction, relevant conjectures, main theorem, Section 7.3, and proof of Theorem 1.8 were read. Not all of its intermediate sections have been audited line by line.

## Known ingredients and credit

- [Homma, arXiv:1108.4975v1](https://arxiv.org/abs/1108.4975v1), Corollary 1.2, is the substantive external point-counting input. It allows reducible curves without rational line components; its sole exception is the planar degree-four curve over F4. The source and proof were read, including the nonabsolute and reducible cases. The quadratic base-locus hypothesis excludes the exception.
- Minimal-degree curve classification, normalization, the plane genus formula, and complete-intersection connectedness are classical. The manuscript supplies the needed arguments, including a Koszul cohomology proof of connectedness for nonreduced intersections.
- [Beelen and Montanucci, arXiv:2008.05748v1](https://arxiv.org/abs/2008.05748v1), Theorem 3.11, contains the space-quartic bound as a special case. The manuscript credits that antecedent but proves the needed quartic case directly and does not depend on the general theorem.
- [Couvreur, arXiv:1409.7544v3](https://arxiv.org/abs/1409.7544v3), especially Section 5.3, places the complete-intersection bound in the prior literature. The general projective-variety bound is background, not the proof of P35.
- The extremal binary-grid cone is a special case of the tubular constructions of [Lachaud and Rolland, arXiv:1405.3027](https://arxiv.org/abs/1405.3027). It is not claimed as new. Their abstract was inspected; attribution of the construction is also directly supported by Lin's introduction and Couvreur Section 5.3. No claim of a full independent audit of the Lachaud–Rolland paper is made.

## Candidate contribution

The proof allocates the total degree between rational lines and the nonlinear part. Homma handles nonlinear degree at least five under the stated degree budget. The remaining degrees are controlled by quadratic plane exclusion, minimal-degree curves, a space-quartic projection argument, and rational attachment of line components to an irreducible conic. This yields a general connected-curve criterion and a sharp codimension-three complete-intersection result in one manuscript.

This is a focused contribution to a published conjectural framework. It may be useful in further study of rational line components of quadratic base loci and dimension-constrained point maxima. That possible use is an assessment, not evidence of future citations or broad impact. The result should be evaluated as a specialist theorem and partial conjecture case, not a solution of the entire largest-intersection problem.

## Priority search and limitations

Searches included combinations of “three quadrics”, “8q”, “complete intersection curves”, “maximum”, “finite fields”, “connected curves”, “quadrics”, and “q+5”. Related hits included unrestricted quadratic systems, smooth genus-five curves, two-quadric bounds, and rational points over number fields. None of the inspected sources gave the stated general connected quadratic-curve theorem or the full reducible/nonreduced triple-quadric conclusion.

Search absence does not certify novelty. In particular, a result embedded in older work on quadratic systems or projective codes could supersede this case. No outside expert or author was contacted. Historical priority, correctness, significance, and suitability for a journal remain subject to independent review. This folder records one complete internally checked proposed manuscript, not one certified significant open-problem solution.
