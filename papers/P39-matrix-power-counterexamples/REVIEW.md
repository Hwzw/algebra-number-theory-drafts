# Internal proof and artifact review

Henry Zweiman. September 15, 2026. Review performed by the originating agent; no independent agent or human review is claimed.

## Universal proof audit

1. **Power rigidity.** A vector v with A^k v nonzero and A^(2k)v=0 has nilpotent cyclic length at least k+1. Linear independence bounds that length by dim V=k+1. This forces a full cyclic nilpotent basis and rank(A^k)=1. The argument is independent of characteristic and does not require algebraic closure.
2. **Forced chain.** For N^2=0 and rank N>=2, split according to whether phi vanishes on ker N. In the first case, adjust a preimage of a nonzero r in im N intersect ker phi. In the second, descend phi through N and choose a nonzero vector in the kernel of the descended functional. Both produce Zw=r and Zr=0 using only vectors in W; no choice of Z outside W can remove this chain.
3. **First restriction.** After transposition, the coefficient is on the right and kills e_1,e_2. Therefore T e_2=e_1 and T e_1=0. Rank T=1, and im T is exactly the span of e_1. The functional description of T is thus forced, not assumed generic.
4. **Second restriction.** On W the coefficient is identity. Hence Z=N-e_1 lambda, with N the two residual square-zero blocks. The forced chain invokes power rigidity a second time, giving rank Z=1, while projection onto W has rank two. This is a contradiction for all inputs.
5. **Parameter and orientation checks.** The padding has size k-5, so the construction is defined for every k>=5. Transposition turns the right-coefficient proof into the requested left-coefficient map. The explicit target has lower-diagonal ones in positions (2,1), (4,3), (6,5). Nullity B is two and k+1>k.
6. **Nonadditivity.** Over an algebraically closed characteristic-zero field choose a^k=-1. Since C^2=0, [a(I-C/k)]^k=C-I. Thus I and C-I are attained while C is not. Density follows separately from the standard existence of kth roots of invertible matrices. No finite-field nonadditivity claim is inferred.
7. **Rank-one boundary remark.** The three-cycle example in Remark 2.3 is invertible and restricts to a rank-one square-zero map plus one outside direction. This checks that the rank-two hypothesis in the lemma has real content; it is not a proof of dimension-minimality for the main counterexamples.

No gap was identified in these obligations. The main argument is self-contained; finite computation is not used to supply a universal quantifier.

## Exact diagnostics

`q37-counterexample-check.py` has SHA-256 `dd3c8e7d35123fdd7459b2188dedf8814ef8bd6bd109632896f951b0cffe01cb` and passed. It checks all 1,125 linear functionals in seven finite-field configurations, computing the kernel/image intersection by exact modular elimination. It also checks 10,977 zero-primary partition cases in dimensions 2 through 20, and coefficient/target ranks and the proposed inequality at k=5,...,20. The first explicit matrices are retained in the JSON output.

These are checks of the proof ingredients, not exhaustive searches over X and Y. In particular, finite-field computations do not establish characteristic-zero nonexistence. That conclusion comes from the two lemmas and their universal application.

## Artifact review

The final PDF has four pages. All four rendered pages were inspected after the final TeX edit; matrices, mathematical notation, page numbers and references are legible, without clipping or overlap. The theorem continues normally from page one to page two. Text extraction yields 8,871 characters across the four pages, with no replacement characters. The TeX log has no overfull boxes or undefined references.

The complete Markdown has the Henry Zweiman byline, preserves all theorem/proof content in a semantic round-trip check, and contains 170 parsed math expressions with zero errors. The converter verified 166 source math expressions and all labels. SHA-256 records identify the precise reviewed files. No external journal submission or human peer review is implied by this preparation.
