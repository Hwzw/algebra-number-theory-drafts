# P09 final manuscript transfer review

Reviewer: internal agent `arithmetic`. Date: 2026-09-08.

**Verdict: PASS. No mathematical correction requested.**

The actual frozen source was read completely:

`research_program/selected_papers/P09-unique-addition/manuscript.tex`

SHA-256, independently recomputed:

`2c304a0ff786141c14f8355c7fe82c56c4b5cf8e4633ec76ddde922cbc6d3890`

This report is bound to those source bytes. No manuscript file was edited. It certifies an internal proof/source transfer review, not external refereeing, exhaustive priority clearance, or PDF visual quality. Parent handles the separate PDF and Markdown checks.

## Main theorem and transfer

The final statement correctly requires a commutative unital coefficient ring, finite length of the underlying source module, centerlessness, and an abelian derived algebra. The target is an arbitrary Lie ring, with no presumed scalar structure. The definition uses an alternating bracket, including characteristic two. The clarification that the module-generated derived algebra equals the additive derived Lie subring is valid because r[x,y]=[rx,y].

The generalized Fitting-image lemma in the final source is stronger in presentation than the original vector-space lemma but uses exactly sufficient hypotheses: positive N, im(d^(N+1))=im(d^N), and ker(d^(2N))=ker(d^N). These imply bijectivity on the image and trivial image/kernel intersection without finiteness of the target. Its bracket-closed kernel proof uses the integer-coefficient iterated derivation identity, valid in all characteristics. Target images and kernels are additive subgroups because the target adjoint is additive; no addition of alpha is used to obtain this fact. The B_v bracket calculation and injectivity step are transferred correctly.

The common power-kernel lemma is correctly stated for general abelian groups. A finite list of commuting nilpotent restrictions has a nonzero common kernel on any nonzero invariant subgroup; no dimension, field, or division is used.

The finite-length proof correctly supplies uniform stabilization and a finite list of module generators. Adjoint restrictions commute on C_L([L,L]), not on all of L. Source bilinearity makes the generators detect the center. The derived-algebra addition defect has a preimage in this centralizer and is killed by every adjoint power. This proves additivity on the derived algebra, after which centerlessness removes every remaining defect. Surjectivity is used explicitly and legitimately. The zero-algebra and positive-N conventions are correct.

The field and finite-Lie-ring corollaries follow with exactly their stated scope. Finite abelian groups have finite length over Z. No arbitrary finitely generated module or infinite-dimensional extension is asserted.

## Supplementary results checked independently

**Finite-field family L_q.** The weight action is faithful, has zero common fixed space, and has derived algebra precisely V. There are q+1 weights, so the total dimension is q+3. Every acting vector annihilates one weight and hence has singular restriction to V. Translation does not change that restriction. The source correctly avoids claiming failure of the two-centralizer condition.

**Exact common-centralizer number.** In L_(r,s), the subspace of candidate centralizing elements (0,N,v,0) is naturally Hom(W plus K,U). An h-tuple imposes annihilation of the span of h vectors (w_i,a_i), giving the stated dimension r(s+1-rank), and therefore a nonzero centralizer for h<=s. Commuting with the identity-action element removes every translation component; commuting with a basis of W then removes the scalar and Hom(W,U) components. Thus c(L_(r,s))=s+1 over every field. The metabelian and centerless assertions, the block-matrix representation, and the r=s=2 identification are correct.

**Direct sums.** The direct-sum derived algebra is the direct sum of the derived algebras. The singular restriction in the first factor guarantees singularity of every total restricted adjoint. The second factor supplies a nonzero common centralizer for every s-tuple by placing its witness in that factor. The claimed simultaneous obstruction is valid; no general inheritance of unique addition under direct sums is assumed, since the main theorem applies to the resulting algebra directly.

**Reconstruction consequences.** Additive bracket-preserving bijections are precisely Lie-ring isomorphisms. Additivity implies scalar linearity over a common prime field, including Q by uniqueness of division. The explicit limits concerning other scalar fields, semilinearity, and algorithmic complexity are correct.

**Separate faithful-action theorem.** This proof works for arbitrary abelian V and an arbitrary Lie subring A of End_Z(V). A central acting element t need only be bijective; its inverse need not be in A. The target image of its adjoint is alpha(V), and its kernel is alpha(A), both additive subgroups before alpha is known additive. The mixed-sum discrepancy lies in alpha(A); comparison of its action on every alpha(w) identifies it by faithfulness. The subtraction calculation recovers addition on V. Kernel closure then allows addition on A to be recovered by testing all w. The proof is valid even for nonabelian A and does not assume finite length. The case V=0 is trivial because End_Z(0)=0 and hence A=0.

## Reference and overlap claims

I rechecked the final Arzhantsev primary PDF and the locally retained complete Ferreira–Guzzo primary text, including Theorem 4.1, Lemma 3.1, and Lemmas 4.2–4.6. The source comparison is substantively accurate. Arzhantsev's infinite-field two-centralizer theorem and its specific solvable example do not state the finite-length metabelian result. The relevant matrix classification in Sosnov's June 2026 paper is a different scope, as already checked in the independent extension review.

The claimed triangular overlap is correct, with the standard unital-module meaning of an associative algebra acting on V. The map (a,v,b) to ((a-bI,v),b) identifies the triangular Lie ring with (A semidirect V) plus central K. The extended bijection preserves brackets and centers. In the n=2 specialization, Ferreira–Guzzo's target calculations use only the additive group, brackets, and centrality; associative multiplication is needed on the source for its triangular decomposition, not on the arbitrary target. Hence adaptation to a Lie-ring target is legitimate. Centerlessness of the affine factor makes the residual central defect have only its extra K-coordinate, and that coordinate is identically zero. This supports the paper's prominent concession that the associative-unital affine application is accessible by the older method.

Primary sources used for this comparison:

- [Arzhantsev, published paper](https://www.mathos.unios.hr/mc/index.php/mc/article/download/5110/1595).
- [Ferreira–Guzzo, institutional primary PDF](https://repositorio.usp.br/directbitstream/0349dfbc-0e9b-4e54-9b61-9081fba14522/2952053.pdf).
- [Sosnov, June 2026 primary preprint](https://arxiv.org/html/2606.08201v1).

The bibliography's Arzhantsev volume/pages/DOI and Ferreira–Guzzo volume/issue/pages/DOI agree with their primary title pages. Qi–Hou's title, authors, journal, year, volume, and pages agree with Ferreira–Guzzo's reference and reproduced theorem. The DOI resolver did not return readable Qi–Hou content in this pass, so this is not represented as a fresh full-text audit of the 2011 original.

## Final scope assessment

The final source faithfully consolidates the complete finite-length proof, all-field and finite-ring consequences, independently valid examples, and the separate faithful-action theorem. It clearly states the older triangular overlap and does not claim the entire centerless-Lie-ring problem, arbitrary injections, or unsupported semilinearity. No inflation into several papers occurs. Mathematical transfer is approved for the exact hash above. Absolute novelty and editorial significance remain judgments beyond what an internal audit can certify.
