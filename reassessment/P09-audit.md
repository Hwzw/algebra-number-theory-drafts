# P09 fresh adversarial audit and significance reassessment

Date: September 8, 2026. Agent: `review_rational_power`.

## Decision

The current manuscript is mathematically sound. Its original infinite-field theorem is a useful structural result, but the older triangular-additivity method substantially reduces the novelty and difficulty of its flagship matrix application. I would not automatically carry its earlier internal admission into the user's stricter five-paper goal.

During this audit I developed a stronger complete proof, recorded separately in [P09-extension.md](P09-extension.md): **every centerless metabelian Lie algebra over a commutative unital ring whose underlying module has finite length is a UA-Lie ring.** This covers all finite-dimensional Lie algebras over all fields and all finite Lie rings. The parent independently reconstructed the all-field proof and proposed its natural finite-length formulation, whose module details have been checked here. A fresh reviewer is inspecting it; my own authorship of the extension is not independent proof validation.

The extension supplies a substantially better basis for reconsideration: it removes the global invertible-adjoint hypothesis by a local Fitting-image argument and works where every adjoint action on the derived algebra is singular. Nevertheless, neither internal agreement nor a negative search establishes editorial importance or absolute priority. The appropriate status is **stronger candidate pending independent extension review, source comparison, and final Markdown integration**, rather than an automatic significant-paper count.

## 1. Current source reconstructed

Read all of `research_program/papers/P09-unique-addition/manuscript.tex`, SHA256 `cb1d0e82004dfa70becc367dba38b2d585bc9c7ce06cb542f3c9b075a716cd77`. No manuscript edit was made.

The affine criterion is correct. If t acts bijectively and centrally, the bracket-preserving bijection identifies the translation summand and acting summand with the image and kernel of an additive adjoint map in the target. The mixed-sum identity uses faithfulness, then the bracket of e+v and e+w recovers translation subtraction. Faithfulness again recovers addition on the acting summand. The argument neither presumes target linearity nor transports addition covertly. It also works in characteristic two.

The commuting-operator lemma is valid over an infinite field: zero common kernel eliminates the zero joint generalized weight, and the determinant polynomial has a nonzero rational value. Applied to the action on the abelian derived algebra, it produces a splitting and a faithful abelian complement. The resulting centerless-metabelian theorem follows. The family with common-centralizer number s+1 and its nonassociatively closed variant have the stated bounds: the lower bound is a dimension count on maps W⊕K→U, and the proposed upper-bound tuples force every remaining component to vanish.

No mathematical defect was found in the existing result. In particular, its explicit warning that the infinite-field determinant argument does not cover every finite field is accurate.

## 2. Primary-source comparison

The following sources were inspected afresh rather than accepted on the strength of earlier AI review files.

**Arzhantsev.** [Uniqueness of addition in Lie algebras revisited](https://arxiv.org/html/2401.06241v2), Math. Commun. 30 (2025), 179–189; the [arXiv record](https://arxiv.org/abs/2401.06241) still lists v2 as latest. Theorem 2 is the two-centralizer criterion over infinite fields. Example 2 and Problem 4 ask about the specific matrix example. Section 8 treats admissible radicals in characteristic zero by proving that same centralizer condition. It does not state the full metabelian theorem. The source's broader centerless-Lie-ring question remains strictly wider than the proposed extension. The current paper's unbounded common-centralizer examples give a concrete separation from these criteria. These comparisons concern precise scope, not a claim that an explicit question's continued appearance rules out an older implicit solution.

**Qi–Hou and Ferreira–Guzzo.** The complete 2019 primary paper was downloaded from the [University of São Paulo repository](https://repositorio.usp.br/directbitstream/0349dfbc-0e9b-4e54-9b61-9081fba14522/2952053.pdf) and its proof read, including Theorem 1.1, Lemmas 3.1 and 4.2–4.6, Theorem 4.1 and Corollary 5.2. Local PDF/text are retained alongside this audit. Theorem 1.1 reproduces Qi–Hou's 2011 triangular-algebra theorem. Its n=2 target calculations require only additive Lie-ring operations. For associative unital acting algebras, the central extension Tri(A,V,K)=(A⋉V)⊕K therefore recovers the original affine result by adapting that proof; centerlessness kills the residual central error. This is real proof-level subsumption of the matrix application, not merely superficial similarity. The published source hypotheses still require associative diagonal rings and bimodules. They do not directly give an arbitrary finite-length metabelian Lie algebra; UA inheritance under subalgebras, quotients, or scalar descent cannot be assumed.

**Sosnov.** [Uniqueness of addition in Lie rings gl_n(K) and sl_n(K)](https://arxiv.org/html/2606.08201v1), June 2026; the [current record](https://arxiv.org/abs/2606.08201) lists only v1. The inspected statements and proof concern matrix Lie rings and special-linear injections. They neither state nor immediately imply the metabelian class result. Its use of defects and commutator tests is relevant methodological background, not evidence of a finite-length Fitting-image theorem.

Searches combined “unique addition,” “metabelian,” “centerless,” “finite field,” “Fitting,” “bracket-preserving,” and “Lie multiplicative,” and checked the recent source records. They did not locate an exact full-class result. Most broad hits were irrelevant; those negative results carry little priority weight. No reliance was placed on aggregator claims of open/solved status.

## 3. Why the current version is not automatically a hard-paper success

The original infinite-field criterion has three attractive features: it is intrinsic, permits an arbitrary target Lie ring, and handles a whole solvable class outside the two-centralizer condition. The proof is clean and short, which is a virtue, not a defect.

But a short proof cannot be relabeled difficult merely because an application appears in a recent problem list. Its associative-unital case follows from an older proof, and passing from an invertible central action to a centerless metabelian algebra over an infinite field uses familiar commuting linear algebra. The nonassociative acting examples are genuine scope extensions, but their presence alone does not demonstrate a major conceptual advance. Under the new user standard, the original P09 is best viewed as a plausible concise specialist paper whose exceptional significance has not been established.

The all-field/finite-length extension is different in a concrete way: no single regular adjoint need exist, so one must recover partial addition on many intrinsic images and prove that their information determines global addition. The local argument permits residual errors in a Fitting kernel, then removes them by separating kernel and image. The global argument locates the remaining defect in the derived-algebra centralizer, where finitely many adjoints commute and the joint power-kernel is zero. That is a new proof mechanism relative to the old manuscript's single global splitting.

## 4. Extension mechanism and checks

The full proof is in the extension file; its essential points are:

1. For d=ad_e and stabilized exponent N, U=im d^N and W=ker d^N map under a bracket-preserving bijection to an additive image and an additive kernel in the target. No target scalar structure is used.
2. If U is abelian, put B_v=alpha(e+v)−alpha(v). Although B_v need not equal alpha(e), it lies in the target Fitting kernel and acts on alpha(U) exactly as ad_alpha(e). Expanding a bracket separates its kernel error from its image component and proves additivity on U.
3. In a metabelian algebra every U is contained in the abelian derived algebra. A defect on that derived algebra lies in alpha(C_L([L,L])). Adjoint restrictions commute on this centralizer, even though adjoints do not commute on all of L.
4. A nonzero common power-kernel of finitely many commuting nilpotents would contain a nonzero common kernel. Centerlessness excludes it. This kills the defect on the derived algebra; testing brackets then kills every defect.
5. Finite-length modules have stabilized adjoint chains and a finite module generating set. Those generators detect the full center by bilinearity. These replace the vector-space inputs without assuming that the target is an R-module.

The delicate steps are expressly justified in the extension: W is bracket closed by the iterated derivation identity; image/kernel intersection is zero from stabilized power kernels; the target image is an additive subgroup because the target adjoint is additive; and the final common-kernel argument is applied on the correct centralizer ideal. Scalar-extension descent of UA, arbitrary-subalgebra inheritance, and preservation of sums of adjoint maps are all avoided.

## 5. Concrete additional scope and downstream consequences

For each finite field F_q, let A=F_q^2 and let V contain one one-dimensional weight space for each projective nonzero linear form on A. The algebra L_q=A⋉V is centerless, metabelian, and has dimension q+3. Every element acts singularly on V, because one of the chosen weights annihilates its A-component. The extension proves L_q is UA nonetheless. Thus its extra finite-field scope is witnessed by an infinite family, including a five-dimensional example over F_2.

Combining L_q with the old L_{r,s} by direct sum gives examples that simultaneously have no globally invertible action on the derived algebra and require at least s+1 elements to obtain zero common centralizer. Both conclusions follow directly from the corresponding factors. These examples make the two separate limitations of the earlier criteria visible in one family.

The reconstruction consequence is precise: an abstract bracket-preserving bijection out of any algebra in the new class is automatically a Lie-ring isomorphism. Over a prime field this also forces linearity; therefore bracket-magma isomorphism and Lie-algebra isomorphism coincide there. Over a nonprime field the theorem only gives the underlying additive/Lie-ring structure, not field-linearity or a common semilinear scalar automorphism. It also identifies bracket-preserving self-bijections with ordinary Lie-ring automorphisms. These are immediate downstream consequences, not additional papers or an efficient reconstruction algorithm.

The finite-ring corollary includes additive groups of exponent p^a with a>1, which are not vector spaces over a field. The general theorem hence has useful scope beyond removing a finite-field technicality.

## 6. Exact remaining gap

There is no currently identified mathematical gap in the proposed finite-length proof, but it was developed in this audit and requires fresh independent adversarial validation before promotion. The stronger statement also needs its own final source comparison and complete manuscript integration; the current six-page TeX still states only the infinite-field result. Root is handling Markdown integration, and no theorem in the admitted source has been silently changed.

The broader open boundaries remain substantive: arbitrary infinite-dimensional centerless metabelian Lie rings need not have stabilized Fitting images or finite centralizer detectors; nonmetabelian algebras need not have abelian Fitting images. Neither problem is solved by this argument. Establishing every centerless Lie ring to be UA, a claim of algorithmic reconstruction efficiency, or field-semilinear rigidity would require further proofs.

**Recommendation:** reassess P09 as one stronger finite-length reconstruction paper if the new proof and priority review pass. Do not count the original theorem, finite-field extension, finite-ring corollary, examples, and automorphism observation separately. Do not certify that it meets the user's unusually high significance threshold solely from this internal audit.
