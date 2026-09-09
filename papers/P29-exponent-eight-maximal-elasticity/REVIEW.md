# Internal proof review

September 9, 2026. Review by the originating agent; no separate-agent or human review.

## Universal arguments checked

1. The minimum positive factorization-length difference is the generator of the group of all such differences. Products and reversal justify both subgroup operations. The signed-atom relation supplies the stated divisibilities and ensures non-half-factoriality.
2. The chosen order-eight and order-four projection matrices are invertible over the respective local residue rings. Their lifted subgroups are graphs over the chosen summands, and the specified complements exist. Each order-filtration relation uses the least positive multiple entering the previous subgroup, which is essential for atom minimality.
3. In the order-eight lift of an order-four quotient term, the two relation differences are t-1 and t+2. Their gcd divides three. In the order-four lift of an order-two quotient term, the differences are t-1 and t, forcing one. The one-coordinate case has lengths two and three. The remaining case satisfies all hypotheses of the cited 2018 lemma.
4. A short signed word has no zero-sum subsequence because each independent order-four coordinate occurs fewer than four times with one sign, and the order-eight coordinate occurs fewer than eight times with one sign. This is used to prove minimality, not merely zero sum, of every constructed witness.
5. For an order-eight term outside K, the E projection forces the witness subword to contain zero or two copies of the distinguished term. Switching residue representatives creates a length change of four in all cases, which excludes the term.
6. Inside K, the permitted order-eight residues are 0,1,4,7. A representative switch by four leaves only 0,4. A single switch forces absolute order-four coefficient one; two switches then change length by four. This proves the stated support classification. The zero-coefficient case and b=0 are included.
7. For an extremal zero-sum-free sequence, the group-algebra product is nonzero because the identity coefficient is one. Its degree equals the top degree, so only linear terms survive. Dependent E projections of order-two terms make their product zero. Removing an order-eight term preserves every order-two term, so the lemma applies to all such terms of U. Their total projection is zero, giving the required contradiction.
8. The atom-length bound eight for the residual signed support handles opposite pairs, pure atoms, two order-four blocks, one block with four copies of f, and the no-block case. The noncyclic hypothesis gives D(G)>8.
9. The arithmetic corollary uses the exact external support-to-invariant criterion and the established uniform-end theorem. It does not assert that every maximal-elasticity length set is an exact interval with no exceptional ends.

## Finite diagnostics

Run `python3 check.py` in this folder. The script uses coordinate addition and a subset-sum dynamic program independent of the proof's minimality argument. It tests every representative choice for every excluded order-eight element in C4^b+C8 and every outside-K order-eight element in C2+C4^b+C8, for b=0,1,2,3.

All 4,756 sequences are zero-sum atoms. For each of the 660 tested excluded elements, at least one constructed atom has length not congruent to two modulo three. Minimality is checked by verifying that the full sum is zero and that deleting one designated term leaves no nonempty zero-sum subsequence; a proper zero-sum subsequence containing that term would have a zero-sum complement in the deletion.

The group-algebra argument, arbitrary rank, and infinite-family conclusions are hand proofs. The finite computation is only a diagnostic of the explicit signed-word construction.

## Source and artifact checks

The original 2018 Lemma 3.10 and Corollary 3.3, the 2021 known-case theorem and Corollary 2.3, the February 2026 standing conjecture, and the August 2026 relevant group-algebra results were checked. See ASSESSMENT.md for scope and historical limitations. Artifact hashes, Markdown conversion, equation checks, and final PDF visual inspection are recorded in the adjacent JSON files.
