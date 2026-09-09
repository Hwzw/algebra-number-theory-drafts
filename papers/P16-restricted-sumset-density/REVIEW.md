# Internal proof and artifact audit

Henry Zweiman manuscript P16. September 9, 2026. Review by the originating OpenAI Codex agent; no independent human or separate-agent review.

## Mathematical checks

1. **Nonempty sets and small cases.** Both main theorems require nonempty A,B. The b=1,2 bound follows from one column; the b=3 contradiction uses Cauchy--Davenport on S-B with the original boundary guaranteeing a+1<p. The interval/inverse proof starts at b=4, not b=5.
2. **Exact transfer.** For each fixed b, the map d -> (d-b,b) is an injection from the new forbidden column into the original forbidden column. Allowed differences d-b avoid A by definition. The transformed upper bound equals the desired counterexample threshold with the transformed cardinality. No matching hypothesis or bound at the other summand is inserted.
3. **Ordering.** Before an exchange, d=p-a-b+4>=b+4. If a>d and the sets are exchanged, the new a is the old d and is at least b; the new d is larger and still at least b+4. The new a+d identity and all representation counts persist after reflection. The complement is of an enlarged allowed set, which is legitimate for every containment argument used.
4. **Qualitative deduction.** At b>=4, the normalized a+b is at most p/2+b. With b<=p/16 it is less than 3p/4. Ouyang's Corollary 1.8(i) has no further large-p hypothesis. Empty forbidden columns may be filled because A is nonempty; this decreases the surviving sums.
5. **Pollard.** Level 2 is valid because a,d>=b>=4. The total a+d-2=p-b+2 is below p. Since the truncated sum equals 2p-2z-u, its lower bound gives 2z+u<=2b-4 with the direction used in the proof. Together with z+u>=b it gives u>=4 and z<=b-4.
6. **Deletion.** Only distinct D-endpoints of unique differences are removed, so k<=u. Each such difference loses its sole representation and no absent difference is restored. Thus the complementary difference set has at least z+u elements. The identity r'<=b-4+k-z-u follows by subtracting a+d-k=p-b+4-k. Cauchy--Davenport gives r'>=-1; its minimum is not saturated at p because the difference set is proper and the summand total is at most p.
7. **Inverse hypotheses.** In the unbalanced case, d>=a>=102b and u<=2b-4 give |D'|>=100b+4. Both summands have size at least 100(r'+3), and the complement has size at least b>=r'+3. These are exactly sufficient for Grynkiewicz Theorem 1.4, after reordering D' and -A. The book's separate logarithmic inverse theorem is not an input. The sign on A only reflects its progression.
8. **Progression and normalization.** Dilation by a nonzero common difference inverse, and translations of the other coordinates, preserve all incidences. The progression length is m=a+h with h<=b-3-z. It is less than p, as also follows from the later positive bound for p-m.
9. **Boundary signs.** At a missing zero, D is the complement of A minus delta points; at a unique zero it is that complement minus delta+1 points plus one point of A. In the latter case the extra overlap contribution is nonnegative, so the upper bound on the A-boundary follows in the stated direction. Removing h holes from I reduces its directed boundary by at most h, not 2h.
10. **No modular wrap ambiguity.** The interval identity forces B into [-L,L] only after proving both m>L and p-m>2L. The entire integer sumset then has an enclosing interval with m+2L<p elements. Reduction is injective on the entire sumset, including all allowed sums, rather than merely on each coordinate.
11. **Comparable-set doubling.** At most b forbidden pairs create at most b additional unrestricted sums. The estimates for 2A and 2B use a nonempty minimizing subset in Petridis' theorem, not an unjustified assertion about all translates. The expression for the union doubling ratio is t+6+10/t+4/t^2. Its second derivative is 20/t^3+24/t^4>0; the maximum on [1,102] is below 110.
12. **Rectification threshold.** Green--Ruzsa Theorem 1.3 uses the actual doubling ratio; the threshold decreases with that ratio for K>=1. Using the upper bound 110 is therefore safe. The chosen c gives density strictly below half the threshold. Freiman isomorphisms preserve all sum equalities in both directions, so arbitrary restrictions and overlaps between A,B are preserved. Lev's original theorem uses the ceiling logarithm; its definition and proof convention were checked.
13. **Scope.** Corollary 2 follows because C=1/c>2. This proves existence of an absolute coefficient, not all positive coefficients and not C=2. No step assumes Ouyang's full conjecture. The logarithmic result is one additional bound in this paper, not a new paper.

## Auxiliary exact checks

The included Python script checks all 86,367 ordered pairs of nonempty subsets in cyclic groups of orders 2 through 8. Their maximal admissible column sets give 252,967 instances of degrees 0 through 3. Exact reflection, containment, degree, and cardinality identities pass. It also checks 74,100 interval-boundary instances in moduli through 13 with up to four holes.

These are checks of auxiliary identities, including composite moduli because the transfer is a finite-group fact. They neither enumerate the enormous prime range of the main theorem nor establish novelty. The proof is a hand argument using the cited theorems, not a computer-assisted finite exhaustion theorem.

## Artifact checks

The six-page PDF compiled without undefined references, overfull boxes, underfull boxes, or warnings in the saved build log. All six rendered pages were visually inspected for equation clipping, page breaks, author identification, and reference layout. The full Markdown conversion preserved all 223 source math expressions and all seven proofs, with AUX-derived theorem/equation/reference numbering. Its 230 rendered math expressions passed syntax checking with zero errors. A content round trip and artifact hashes are recorded in the accompanying manifests.

No proof gap was identified in this internal review. This is a record of the checks actually performed, not external mathematical certification.
