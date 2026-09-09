# Independent adversarial review of the P09 extension

Reviewer: internal agent `arithmetic`. Date: 2026-09-08.

Reviewed: `research_program/reassessment/P09-extension.md`, Sections 1–7, including the newly appended finite-length theorem. The manuscript was not edited. This is an internal mathematical and source audit, not external refereeing or a guarantee of priority.

Reviewed proof-file SHA-256 after the positive-N editorial correction: `5bd720065a5535f4f9c23cb10b31cfdf94f4c58efcc01bcd1a3a28ca4ee8f1ab`.

**Verdict: PASS.** The finite-length theorem has a complete proof. In particular, the infinite-field hypothesis can be removed from the proposed centerless metabelian theorem. Neither the Fitting-image step nor the gluing step assumes that the bracket-preserving bijection is additive, linear, or compatible with an underlying scalar action on its target.

## Exact statement approved

Let R be a commutative unital ring, and let L be a Lie R-algebra whose underlying R-module has finite length. Suppose that Z(L)=0 and that V=[L,L] is abelian. Then every bracket-preserving bijection from L onto an arbitrary Lie ring S is additive.

Here Lie rings have an abelian additive group, an alternating biadditive bracket, and the Jacobi identity. No R-module structure on S is assumed. Thus the result includes finite-dimensional centerless metabelian Lie algebras over every field and finite centerless metabelian Lie rings, by taking R=Z in the latter case.

## Audit of the local Fitting-image argument

Fix e in L, set d=ad_e, and choose N at least max(1,length_R L). The ascending kernel and descending image chains stabilize by N. Once two consecutive kernels or images agree, all later members agree, so the bounds on the number of strict length changes suffice. Put U=im(d^N) and W=ker(d^N).

The map d is onto U by image stabilization. If u=d^N x lies in U and d(u)=0, then d^(2N)x=0 because N is positive, and kernel stabilization implies d^N x=0. Thus d is also one-to-one on U. Similarly U intersect W is zero. This uses only source-module finite length.

Let alpha be a bracket-preserving bijection and D=ad_alpha(e). Alternation gives alpha(0)=0. The identity D^j alpha(x)=alpha(d^j x) is a composition identity between maps of sets; it does not use additivity of alpha. Surjectivity and injectivity therefore give

    alpha(U)=im(D^N),    alpha(W)=ker(D^N).

Because D is an endomorphism of the already-given additive group of S, these two image sets are additive subgroups. They have zero intersection, and D acts bijectively on alpha(U), by the same set conjugacy. There is no invocation of a Fitting theorem for the possibly infinite, non-linear target S.

The derivation formula for d^(2N)[a,b], with a,b in W, has every summand zero: at least one of the two differentiation exponents is at least N. Kernel stabilization then places [a,b] in W. This works in arbitrary characteristic; no binomial coefficient is divided out. Hence alpha(W) is bracket-closed as well as an additive subgroup.

Assuming U abelian, alpha(U) is likewise an abelian Lie subring. Define B_v=alpha(e+v)-alpha(v) for v in U. The equality d^N(e+v)=d^N(v) uses N>=1 and gives B_v in alpha(W). For w in U, bracket preservation and target biadditivity give [B_v,alpha(w)]=D alpha(w). Consequently

    alpha(d(w-v)) = [B_v,B_w] + D(alpha(w)-alpha(v)).

The first and last expressions are in alpha(U), whereas the middle commutator is in alpha(W). Their zero intersection kills the commutator. Both arguments of D in the resulting equality lie in alpha(U), so injectivity of its restriction yields alpha(w-v)=alpha(w)-alpha(v). Taking w=a+b and v=b proves addition on U.

All subtractions in this argument occur in the supplied additive group of S. In particular, alpha(U) being additive is proved by its image-of-D description before any subtraction is asserted to remain there. The bracket signs are valid also in characteristic two, since alternation implies anticommutativity without division by two.

## Audit of the gluing argument

For V=[L,L], the centralizer C=C_L(V) is an R-submodule and a Lie ideal by Jacobi and the ideal property of V. Choose finitely many R-module generators x_1,...,x_m of L, which exist because finite length implies finite generation. On C, the operators T_i=ad_(x_i)|_C commute: their commutator is ad_[x_i,x_j], and this vanishes on C since [x_i,x_j] belongs to V. An element of C killed by every T_i commutes with the R-module generators and hence, using source R-bilinearity, with all of L. Its common kernel is therefore zero.

The common power-kernel assertion requires no vector space. For commuting endomorphisms T_i of an abelian group, Q=intersection ker(T_i^N) is invariant under all T_i. If Q is nonzero, successively taking kernels of their restrictions leaves nonzero invariant subgroups: a nilpotent endomorphism of a nonzero group cannot be injective. After finitely many steps this supplies a nonzero common kernel, a contradiction. Thus intersection ker(T_i^N)=0 on C.

For every e, the image of (ad_e)^N lies in V and is abelian, so the local lemma proves additivity of alpha on that image. For v,w in V, set delta=alpha(v+w)-alpha(v)-alpha(w). Biadditivity of the target bracket shows that delta centralizes alpha(V). Its unique preimage a under alpha lies in C, by bracket preservation and injectivity. For each i, applying D_i^N to delta gives zero, since all three source arguments lie in a Fitting image on which alpha is already additive. Intertwining gives T_i^N(a)=0 for all i. The common power-kernel argument now gives a=0 and delta=0. This proves addition on V.

Finally, the addition defect of any pair x,y centralizes every alpha(z), because [x,z], [y,z], and [x+y,z] belong to V, where addition has been established. A bracket-preserving bijection preserves the center as a set. Since the source center is zero, the target center is zero, and the final defect vanishes.

No assertion that C=V, that all adjoints on L commute, or that alpha preserves a source direct sum occurs. Commutation is needed only on C. The two uses of surjectivity, to represent a target defect by a source element and to eliminate a target central element, are essential to the stated proof; no result for arbitrary bracket-preserving injections is certified.

## Finite-field example and scope

The family L_q in Section 4 is valid. The q+1 projective classes of nonzero forms on F_q^2 give a faithful diagonal action on V, with zero common fixed space. Each weight vector belongs to the derived algebra, and every acting element lies in the kernel of at least one weight. Therefore L_q is centerless and metabelian of dimension q+3, while every adjoint restricted to V is singular. Translating an element by V does not change this restriction. This is a genuine obstruction to the earlier strategy of selecting one invertible derived adjoint.

The example should not be advertised as failing the C-condition. In fact it satisfies it. To see this, choose independent a,b in A and v,w in V so that lambda(b)v_lambda-lambda(a)w_lambda is nonzero for every weight lambda; each coordinate choice is possible. If (c,u) centralizes both (a,v) and (b,w), the two coordinate equations imply lambda(c)=0 for every lambda, hence c=0. Those same equations then give u=0. Thus those two centralizers have zero intersection. The current extension file makes only the correct claim about singular adjoints.

The zero module/ring is harmless. The author corrected the local lemma during this review to specify N>=max(1,dim L), avoiding a formally exceptional N=0 case in the identity involving e+v; Section 7 already had the positive-length-bound convention. No unresolved correction remains. Finite generation alone, infinite-dimensional Lie algebras, and nonmetabelian algebras are not established by this argument.

## Fresh primary-source comparison

Arzhantsev's *Uniqueness of addition in Lie algebras revisited*, Theorem 2, assumes an infinite field and the C-condition. Its proof uses nonempty intersections of Zariski-open sets. Lemma 2 is an earlier centralizer test for addition of a pair; Example 2 and Problem 4 concern a specific centerless solvable example outside the C-condition. Those statements do not supply this finite-length metabelian theorem. [Primary text, 2401.06241v2](https://arxiv.org/html/2401.06241v2), [published version](https://www.mathos.unios.hr/mc/index.php/mc/article/download/5110/1595).

Sosnov's June 2026 *Uniqueness of addition in Lie rings gl_n(K) and sl_n(K)* treats matrix families over arbitrary fields in Theorems A–C. Its Lemma 2.2 records preservation of centers; Lemmas 2.4 and 2.7 give centralizer and adjoint identities for addition defects. These general ingredients are prior art and should not be claimed as new. No metabelian or finite-length theorem is stated there. [Primary text, 2606.08201v1](https://arxiv.org/html/2606.08201v1).

Fresh targeted searches for unique addition with metabelian, centerless, and finite-length terms did not locate the exact theorem. This is bounded evidence, not an exhaustive priority certificate. The prior P09 audit of triangular almost-additivity remains relevant: arbitrary Lie-ring targets alone do not establish novelty. The substantive new argument here is recovering addition separately on Fitting images and then gluing by commuting adjoints on the centralizer of the derived algebra. It removes the global regular-element requirement and proves one uniform theorem over finite-length coefficient modules. This strengthens the same coherent P09 paper; it should not be counted as a second paper.

## Recommendation

Integrate the finite-length statement and its full proof into P09, retaining explicit source attribution for the older centralizer/defect techniques and the limits above. Mathematical admission of this extension is supported. Final manuscript transfer and exact bibliographic/priority assessment remain separate checks.
