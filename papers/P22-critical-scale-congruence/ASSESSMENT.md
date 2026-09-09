# Source and contribution assessment

Henry Zweiman. September 9, 2026. Internal research assessment.

## Exact problem and result

Bell and Nguyen, *An analogue of Ruzsa's conjecture for polynomials over finite fields*, [arXiv:1910.08255v1](https://arxiv.org/abs/1910.08255v1), Theorem 1.4 proves polynomiality under the eventual degree bound q^n/(27qn). On page 8, the paragraph opening Section 4 explicitly asks to replace q^n/n by a larger function. Question 4.1 then proposes the full primorial threshold (1−epsilon)d_n.

The main theorem here gives c_q q^n with explicit c_q>0 for arbitrary functions satisfying the same prime-congruence condition. It settles the growth-scale enlargement problem, while establishing only a range of constants in Question 4.1. The separate sharp result assumes F_q-linearity. The source's earlier Question 1.3 was already solved there and is not claimed as the open target.

## Closest earlier work

- Bell–Nguyen's auxiliary-polynomial method and their Theorem 3.1 supply the architecture and the final rationality step. The new height-efficient family is G_(s,j)=Pi_(s−1) times a Carlitz digit polynomial. Its q^s independent elements have value degrees O(q^M) on a degree-M ball when s=M−O_q(1), avoiding the factor M incurred by ordinary monomials.
- [Wagner 1974, author's copy](https://web.math.utk.edu/~cwagner/papers/pseudo.pdf), Theorem 3.2, characterizes linear functions preserving every polynomial modulus with coefficients divisible by the corresponding least common multiple. Its Section 2 describes the classical normalized Carlitz polynomials. The present linear coefficient criterion uses the squarefree primorial for prime-only congruences; the interpolation polynomials themselves are not new.
- [Wagner 1976, author's copy](https://web.math.utk.edu/~cwagner/papers/gfqx.pdf) constructs bases for polynomials with integral-valued divided differences. Its all-moduli condition is stronger than the one here. The complete paper was read for the comparison.
- [Li–Sha, arXiv:1807.02379v2](https://arxiv.org/abs/1807.02379v2), Theorem 1.11 and Section 5, give local binomial-coefficient conditions for functions between finite residue rings. The present general Newton criterion is only for first powers of primes, not a claimed uniform prime-power characterization.

## Version and novelty audit

The journal record is J. Combin. Theory Ser. A 178 (2021), 105337, [DOI](https://doi.org/10.1016/j.jcta.2020.105337). Journal metadata and the open-archive flag were verified. The full typeset journal article could not be retrieved; the Elsevier API returned metadata, not the article body. No access restriction was bypassed.

[Nguyen's current author page](https://sites.google.com/view/khoanguyen-calgary), inspected September 9, 2026, still links arXiv:1910.08255 for this article. arXiv lists only v1. The manuscript pins all theorem and question numbering to that complete, directly inspected version. It does not represent the unread journal body as verified identical. This remains a bibliographic limitation of the proposed preprint.

Targeted searches covered the exact title, arXiv identifier, DOI, Question 4.1, finite-field congruence growth, Carlitz interpolation, Wagner's pseudo-polynomials, and later Ruzsa papers. No matching growth-scale improvement was located. Delaygue's April 2026 paper concerns the integer sequence problem with a hypothesis on singular directions; it does not supply the stated finite-field theorem. Search results alone do not certify historical priority.

The earlier internal aspiration to read the final journal text before admission could not be met. Admission as a proposed preprint instead rests on the full version still linked by the author, explicit version-specific attribution, the comparison above, and the recorded limitation. There is no claim of independently certified novelty or journal readiness.

## Significance and limits

For fixed q, the ratio of the new sufficient growth bound to the earlier one is unbounded as n grows. The interpolation family may be useful for other arithmetic polynomial-method arguments. Those are substantive reasons to investigate the result; no citation forecast is asserted. All results belong to one manuscript, and neither the sharp arbitrary-function conjecture nor the 45-paper research goal is complete.
