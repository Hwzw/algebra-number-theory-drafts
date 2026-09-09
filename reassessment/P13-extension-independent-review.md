# Independent audit: power-map periods and the prime radical

Date: 2026-09-08.
Reviewer: commutative-algebra agent, independent of extension author review_groups.
Reviewed artifact: `research_program/reassessment/P13-extension.md`, complete version read directly.

**Verdict: PASS.** The theorem is valid for associative rings without identity as well as unital rings. The classical bounded-index one-sided-ideal lemma applies exactly as required, without a Noetherian or characteristic hypothesis. The new extension is a substantive strengthening of the original NI conclusion and should be incorporated into the same paper. This is a mathematical/source audit of the extension note, not a signoff on a revised manuscript that has not yet been written.

## Precise result and independent reconstruction

For every associative ring R and n≥1, define

    Per_n(R) = {a in R : (x+a)^n=x^n for every x in R}.

Then Per_n(R)⊆P(R), where P(R) is the prime radical. Consequently every power map on a semiprime ring has zero additive period group, and every nilperiod ring satisfies Nil(R)=P(R).

I independently reconstructed the argument as follows.

First suppose S is semiprime and a is a nonzero element of Per_n(S). Evaluation at zero gives a^n=0. Its least nilpotency index j therefore satisfies 2≤j≤n. Set b=a^(j−1)≠0.

Let S^1 be the Dorroh unitization and r∈S^1. The element x=br belongs to S, so the original period identity can be evaluated at x. This does not require the unitization to inherit the identity. We have ax=a^j r=0.

In any word of length n in the letters x,a, an a preceding some later x produces an adjacent occurrence ax at the boundary between an a-block and an x-block. Thus all such words vanish. Each remaining word is x^(n−k)a^k, appearing with coefficient exactly one. Terms with k≥j vanish by a^j=0, including the all-a word. The period identity consequently gives

    0 = sum_{k=1}^{j−1} x^(n−k) a^k.

Since j≤n, every x exponent in this displayed sum is at least one. Right multiplication by a^(j−2)r leaves the k=1 term equal to x^(n−1)a^(j−1)r=x^n. All terms k≥2 vanish because the new a exponent is k+j−2≥j. When j=2 the multiplier is simply r; the use of a^0=1 in S^1 is a valid shorthand. Hence

    (br)^n=0 for every r in S^1.

The set bS^1=Zb+bS is an additive subgroup, is closed under right multiplication by S, and contains the nonzero element b. It is therefore a nonzero right ideal of S all of whose elements have nth power zero. The exact classical lemma below rules out this ideal in a semiprime ring. This contradiction proves Per_n(S)={0}.

For arbitrary R, pass to the semiprime quotient R/P(R). The particular period identity descends through the surjective map, so the image of a is zero by the semiprime case. Thus a∈P(R). There is no assumption here that arbitrary quotients of a nilperiod ring are nilperiod; only the one specified identity is transported.

Finally, if R is nilperiod, every nilpotent lies in some Per_n(R), whence Nil(R)⊆P(R). The prime radical is nil, giving equality. Its standard local nilpotence also proves the extension note's local-nilpotence consequence.

## Audit of the exact classical input

The required input is the bounded-index one-sided-ideal form of Levitzki's result: a ring with a nonzero nil one-sided ideal of uniformly bounded index has a nonzero nilpotent two-sided ideal. Therefore a semiprime ring has no such nonzero one-sided ideal.

This is distinct from the theorem saying that nil one-sided ideals of a Noetherian ring are nilpotent. No Noetherian premise is being imported or omitted.

I directly inspected these primary sources independently of the extension author:

1. **H. E. Bell and W. S. Martindale III, *Centralizing mappings of semiprime rings*, Canadian Mathematical Bulletin 30(1) (1987), 92–101.** [Publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C836B1E2941F763A2B4A3867B6976935/S0008439500002605a.pdf/centralizing-mappings-of-semiprime-rings.pdf), [DOI](https://doi.org/10.4153/CMB-1987-014-x). Preliminary item (V), printed p.93, states the fixed-exponent assertion for an unrestricted ring and a nonzero left ideal, and explicitly records the semiprime consequence. Opposite rings give the right-ideal form. The article introduces no identity or chain-condition assumption before this assertion. Its subsequent discussion of generated one-sided ideals also retains generator terms separately from ring multiples, consistent with nonunital rings. Reference [2] is Herstein, *Topics in Ring Theory* (1965); item (V) points to Lemma 1.1 there. I verified this reference chain in the Bell–Martindale bibliography; I did not inspect the original Herstein lemma directly.

2. **Pace P. Nielsen, *Bootstrapping the bounded nilradical*, Journal of Pure and Applied Algebra 217(9) (2013), 1711–1715.** [Author-hosted primary PDF](https://mathdept.byu.edu/~pace/BoundedNilradical_web.pdf). Section 1, author-PDF p.1, defines B(S)={b : bS is nil of bounded index} and states B(S)⊆P(S), attributing this containment to Levitzki. Author-PDF p.2 explicitly explains the related characterization for rings without identity. The same section records local nilpotence of P(S). The publication coordinates are also confirmed by [Nielsen's institutional CV](https://math.byu.edu/0000018b-b156-dec1-a9cf-b5fe482d0001/nielsencv-pdf).

Bell–Martindale gives the exact lemma in the form used in the proof; Nielsen supplies an independent radical formulation and confirms the nonunital setting. For the actual argument one only needs the vanishing consequence in semiprime rings. One need not reproduce Nielsen's surrounding proof sketch about arbitrary rings or assert that every bounded-index nil ideal is itself nilpotent.

## Edge cases and possible hidden assumptions

- n=1 admits only the zero period, directly. The nonzero-period argument automatically starts at j≥2 and n≥2.
- Characteristic plays no role: no division, linearization by scalar interpolation, or factorial argument occurs.
- Noncommutativity is fully retained: the vanishing relation is ax=0, not xa=0, and the proof only discards words containing the former ordered pair.
- The exponent n is fixed for the chosen period a and is uniform over r, so the constructed right ideal really has bounded index. No bound on the nilpotency indices of unrelated elements of S is required.
- Using bS^1, rather than merely bS, guarantees that the constructed right ideal is nonzero even before invoking any semiprime annihilator fact. It avoids an unnecessary nonunital boundary argument.
- The prime-radical quotient is semiprime by definition. The particular period identity descends through every quotient, even though the nilperiod property itself need not descend through arbitrary quotients.
- The claim is local nilpotence of the entire nilpotent ideal, not a uniform nilpotency bound or nilpotence of every principal two-sided ideal. The extension note states this distinction correctly.

No mathematical revision to the extension note is requested.

## Prior-art and significance audit

I freshly searched combinations of the exact nilperiod term, additive periods, power maps, semiprime rings, the prime radical, 2-primality, and Levitzki. I found no primary source stating this specific inclusion for power-map periods. Nearby results about multiplicativity of power maps, generalized derivations, and centralizing maps use different identities; they do not supply this statement merely by changing terminology. This remains limited search evidence and cannot certify absolute priority.

Burnette's [published 2025 paper](https://gradmath.org/wp-content/uploads/2025/07/GJM2025-Burnette.pdf), Conjecture 2.6 and Theorem 2.9, respectively asks for NI in general and proves NI for PI algebras. The extension also generalizes the vanishing result for matrix rings over division rings used in Lemma 2.8 to all semiprime rings. Burnette's discussion of periodic NI rings that fail 2-primality does not contradict the extension: those rings are not asserted to be nilperiod. The triangular-matrix counterexample remains valid for the failure of the converse 2-primal⇒nilperiod.

The new contribution is the highest-nonzero-power substitution that creates a bounded-index right ideal from a single period, followed by the classical radical theorem. The latter must be cited and must not be presented as a new result. This yields a meaningful improvement: individual periods in arbitrary rings are localized in the prime radical, and nilperiod rings are proved 2-primal with locally nilpotent nilpotent ideal. It is stronger and more coherent than an NI-only presentation, but it belongs in the same paper, not as an additional paper for the quota.

## Recommendation for manuscript transfer

Replace the NI-only leading theorem with Per_n(R)⊆P(R) and derive the nilperiod 2-primal theorem as a corollary. Cite Bell–Martindale p.93(V) for the bounded-index lemma, with the opposite-ring passage stated. The earlier elementary NI proof may remain as an optional self-contained alternative if its added length serves the paper, but the stronger proof uses a classical external theorem and should be described accordingly. Preserve the independently reviewed finite-ring classification and Corbas correction. A revised manuscript requires a new exact transfer review and new artifact hashes.
