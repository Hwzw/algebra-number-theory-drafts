# Literature, open status, and scope

Date: 2026-09-09. Author: Henry Zweiman. Status: complete internally checked proposed counterexample; historical priority and outside mathematical assessment remain provisional.

## The published question

Geroldinger, Kim, and Loper, [*On Long-Term Problems in Multiplicative Ideal Theory and Factorization Theory*, arXiv:2502.21020v3](https://arxiv.org/html/2502.21020v3), dated February 28, 2026, Problem 20, asks whether the Structure Theorem for Length Sets holds for weakly C-monoids in Kainrath's sense. The current source body and references 102 and 69 were checked on September 9, 2026. The question is explicitly stated as open in that source.

The main theorem addresses its unrestricted monoid formulation. It constructs one fixed monoid, not a sequence of unrelated examples, and proves an unbounded obstruction across its length sets.

## Definitions and closest prior results

1. Florian Kainrath, [*Arithmetic of Mori domains and monoids: the global case*](https://doi.org/10.1007/978-3-319-38855-7_8), 2016, pp. 183-218. Definition 5.1 on pp. 198-199 was read in the complete institutional PDF. It requires the Mori and conductor conditions, a saturated and cofinal complete-closure embedding, and the finite prime-partition condition. It does **not** include local tameness. Condition (C), Definition 4.2 and Section 5, is stronger. The extra hypotheses in Theorem 6.2 were checked separately. Examples 5.6, 5.7, and 6.3 were also examined for overlap.
2. Alfred Geroldinger and Wolfgang Hassler, [*Arithmetic of Mori domains and monoids*](https://doi.org/10.1016/j.jalgebra.2007.11.025), Journal of Algebra 319 (2008), 3419-3463. This introduced weakly C-monoids. Indexed primary-PDF text of Example 6.11 gives a related conductor-plus-cyclic-boundary construction that is not locally tame. The present manuscript credits that construction; novelty is claimed for the explicit obstruction using the two-generator boundary and its consequence for Problem 20, not for inventing all conductor extensions.
3. Alfred Geroldinger and Florian Kainrath, [*On the arithmetic of tame monoids with applications to Krull monoids and Mori domains*](https://doi.org/10.1016/j.jpaa.2010.02.023), Journal of Pure and Applied Algebra 214 (2010), 2199-2218. Theorem 5.1 proves STSL for tame monoids. Its Section 5 definition of an AAMP requires the whole set, including the tails, to lie in the permitted periodic residue classes. That inclusion was rechecked in the primary PDF and is decisive for Lemma 4.1 here.

Targeted searches combining the exact weak-C terminology with length sets, the structure theorem, and counterexamples did not locate a prior solution of Problem 20. Search absence is not proof of historical priority; no exhaustive database or human-expert audit is claimed.

## Contribution and significance

The example shows that the weak-C axioms, a nonempty conductor principal in the complete integral closure, factorial complete integral closure, and the very small distance set `{1,2}` do not force the standard length-set structure theorem. The algebraic verification has a uniform six-element finite-colon witness. Every length set is determined explicitly. The obstruction is quantitative for every prescribed difference, so allowing a different bounded difference for each element does not avoid it.

The result would settle the stated survey problem if the proof and scope survive outside review. It identifies an endpoint obstruction that any stronger positive theorem must exclude. This gives a specific path for subsequent work on stronger hypotheses, rather than a claim of a universal classification or a forecast of citation counts.

## Limits

- The proof is multiplicative. No domain-realization theorem is claimed.
- No failure under an additional local-tameness assumption, or under condition (C), is asserted.
- An informal version that permits arbitrary off-period end pieces is weaker than the AAMP definition used here; the obstruction specifically concerns the standard definition in the cited theorem.
- All proofs and artifact checks were reviewed by the originating agent. Separate-agent review, human review, and journal acceptance are not claimed.
- This is one manuscript. The exact length formulas, distance computation, and quantitative obstruction are parts of that paper, not additional papers toward the research target.
