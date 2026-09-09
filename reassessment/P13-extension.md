# Power-map periods lie in the prime radical

Status: complete argument with a precisely identified classical external lemma; fresh independent review requested. This is a proposed strengthening of P13, not a change to its manuscript. Date: 2026-09-08.

All rings below are associative and may lack an identity. Write P(R) for the lower nilradical, equivalently the intersection of the prime ideals or the least ideal with semiprime quotient. Write

Per_n(R) = {a in R : (x+a)^n=x^n for every x in R}.

## Theorem

For every ring R and every positive integer n,

**Per_n(R) is contained in P(R).**

In particular, a semiprime ring has no nonzero additive period of any power map. Every nilperiod ring is 2-primal:

**Nil(R)=P(R).**

Its nilpotents consequently form a locally nilpotent ideal. The NI conclusion in the current manuscript is a weaker consequence.

## Exact classical input, with scope checked

The bounded-index one-sided ideal lemma says: if an associative ring S has a nonzero right ideal I and some fixed positive integer N satisfies y^N=0 for every y in I, then S has a nonzero nilpotent two-sided ideal. Consequently a semiprime ring has no such nonzero right ideal. No Noetherian condition, characteristic restriction, or identity hypothesis is needed.

This is the bounded-index lemma associated with Levitzki, **not** the differently formulated theorem about nil one-sided ideals in Noetherian rings.

Two directly inspected sources establish the intended generality:

1. H. E. Bell and W. S. Martindale III, *Centralizing mappings of semiprime rings*, Canadian Mathematical Bulletin 30 (1987), 92-101, DOI [10.4153/CMB-1987-014-x](https://doi.org/10.4153/CMB-1987-014-x). The preliminary item (V), printed page 93, states the left-ideal version for an unrestricted ring and gives the semiprime consequence. Passing to the opposite ring gives the right-ideal version. Their text cites Herstein, *Topics in Ring Theory* (1965), Lemma 1.1. [Primary publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C836B1E2941F763A2B4A3867B6976935/S0008439500002605a.pdf/centralizing-mappings-of-semiprime-rings.pdf).
2. Pace P. Nielsen, *Bootstrapping the bounded nilradical*, [author-hosted primary PDF](https://mathdept.byu.edu/~pace/BoundedNilradical_web.pdf), Section 1, pages 1-2. It defines B(S)={b : bS is nil of bounded index}, states B(S) contained in P(S), and explicitly discusses the same statements for rings without 1. It also records that P(S) is locally nilpotent and hence nil. The cited original bounded-index sources include J. Levitzki, *A theorem on polynomial identities*, Proc. AMS 1 (1950), 334-341, and A. A. Klein, *Rings of bounded index*, Comm. Algebra 12 (1984), 9-21, Lemma 5.

The proof below only uses the semiprime vanishing consequence. It does not require a bound on the nilpotency indices of all nilpotents in S; the bound is confined to one explicitly constructed principal right ideal.

## Proof of the theorem

First let S be semiprime, and suppose a in Per_n(S). Evaluation at x=0 gives a^n=0. If a is nonzero, let j be its minimal nilpotency index. Then 2<=j<=n. Put b=a^(j-1), which is nonzero.

Let S^1 be a standard unitization of S, and take any r in S^1. Set x=br; this lies in S, so the original period identity may be evaluated at x without assuming that S^1 has any period property. We have ax=a^j r=0.

In the word expansion of (x+a)^n, every word that has an a somewhere before an x vanishes because it has an adjacent a x. Therefore the only possibly nonzero words are x^(n-k)a^k. Terms with k>=j vanish because a^j=0. Subtracting x^n from the period identity gives

0 = sum_{k=1}^{j-1} x^(n-k) a^k.

Right-multiply this equation by a^(j-2)r, with a^0 interpreted as 1 in S^1 if j=2. The k=1 term becomes

x^(n-1) a^(j-1)r = x^n.

Every term with k>=2 vanishes because its power of a is k+j-2>=j. Consequently

(br)^n=0 for every r in S^1.

The nonzero principal right ideal I=bS^1=Zb+bS of S is thus nil of bounded index n. It is an actual additive subgroup and right ideal, not merely the set of arbitrary products with varying nilpotency indices. This contradicts the bounded-index lemma in the semiprime ring S. Hence a=0.

Now let R be arbitrary and a in Per_n(R). The period identity descends through every surjective ring homomorphism. In particular, the image of a in S=R/P(R) is an additive period of its nth power map. This quotient is semiprime, so the result just proved makes that image zero. Thus a lies in P(R).

If R is nilperiod, every nilpotent belongs to some Per_n(R), so Nil(R) is contained in P(R). The reverse containment follows from the standard fact that the prime radical is nil. This proves Nil(R)=P(R). Local nilpotence follows from the standard local nilpotence of the prime radical. QED.

## Genuine consequences and limits

- The conclusion is stronger than NI: the upper nilradical can properly exceed the prime radical in general. The current manuscript's proof therefore understates the radical location of periods.
- The result treats individual periods in arbitrary rings, not only rings whose every nilpotent is a period. It generalizes the matrix-over-division-ring vanishing lemma used in Burnette's PI argument to all semiprime rings, without a PI or finiteness assumption.
- Every finitely generated subring of the nilpotent ideal of a nilperiod ring is nilpotent. This uses local nilpotence, not a uniform nilpotency exponent for the whole ideal.
- No claim is made that the entire nilpotent ideal, or each ideal generated by one nilpotent, is nilpotent. These do not follow merely by replacing the upper nilradical with the prime radical.
- The converse 2-primal implies nilperiod is false. The upper triangular 2-by-2 matrices over F_2 have prime radical equal to their strictly upper triangular ideal, but E_12 cannot be a period because diag(1,0) and diag(1,0)+E_12 are distinct idempotents.

## Prior-art and significance status

Burnette's published [2025 article](https://gradmath.org/wp-content/uploads/2025/07/GJM2025-Burnette.pdf), Conjecture 2.6, asks only for NI; Theorem 2.9 proves that conclusion for PI algebras. The discussion following the conjecture distinguishes 2-primality from NI and notes that a periodic NI ring need not be 2-primal. That observation does not subsume or contradict the theorem here, because such rings need not be nilperiod.

Exact-term searches combining additive periods, power maps, semiprime rings, prime radical, Levitzki, and nilperiod did not locate a previously stated version of this stronger result. Nearby older power-map/commutativity and generalized-derivation identities are not the translation identity used here. This remains a bounded search rather than a proof of priority.

The proof is short but structurally stronger than the original NI-only note. Its genuinely new-looking step is the highest-nonzero-power substitution, after which the substantial radical fact is classical. It should be assessed as a concise general theorem resolving the named conjecture and locating all power-map periods, not as a new proof of Levitzki's theorem or a broad breakthrough in radical theory. Independent review must pass before rewriting the paper around this claim.
