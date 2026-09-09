# P09: an all-field extension via Fitting images

Date: September 8, 2026. Author of this extension: internal agent `review_rational_power`. Status: **complete proposed proof, awaiting fresh independent review**. This file does not modify the admitted manuscript or represent external validation.

## Theorem

Let K be **any field**, and let L be a finite-dimensional centerless metabelian Lie algebra over K. Then every bracket-preserving bijection from L onto an arbitrary Lie ring is additive.

No scalar extension of L, scalar structure on the target, or UA inheritance by subalgebras is used. In particular, this includes every finite field, even when every individual adjoint action on the derived algebra is singular.

## 1. Fitting-image addition lemma

Let L be a finite-dimensional Lie algebra, e an element of L, and d=ad_e. Fix N at least max(1,dim L), and put

\[
 U=\operatorname{im}d^N,\qquad W=\ker d^N.
\]

Assume U is abelian. Let alpha:L→S be a bracket-preserving bijection onto a Lie ring. Then alpha is additive on U.

**Proof.** First alpha(0)=0 by alternation. Set E=alpha(e) and D=ad_E on S. Bracket preservation gives D^j alpha(x)=alpha(d^j x) for every nonnegative j. Consequently

\[
 U'=\alpha(U)=\operatorname{im}D^N,\qquad
 W'=\alpha(W)=\ker D^N.
\]

These are additive subgroups of S. Fitting stabilization in L implies that d restricts bijectively to U and that U∩W=0. The same set-conjugacy shows that D restricts bijectively to U' and U'∩W'={0}. These assertions do not presume alpha is additive.

The subspace W is a Lie subalgebra. Indeed, for a,b∈ker d^N, the derivation formula for d^{2N}[a,b] has each term zero, since one of the two exponents is at least N. Thus [a,b]∈ker d^{2N}=ker d^N. Therefore W' is a Lie subring: its addition is inherited as a kernel, and bracket closure is inherited via alpha. Likewise U' is abelian, since U is abelian and U' is an additive subgroup.

For each v∈U, d^N(e+v)=d^N v, so

\[
 B_v:=\alpha(e+v)-\alpha(v)\in W'.
\]

For any w∈U, bilinearity in S and [U,U]=0 give

\[
 [B_v,\alpha(w)]
 =[\alpha(e+v),\alpha(w)]-[\alpha(v),\alpha(w)]
 =\alpha([e,w])=D\alpha(w).
\]

For v,w∈U, expand the bracket of alpha(e+v) and alpha(e+w):

\[
 \alpha(d(w-v))=[B_v,B_w]+D(\alpha(w)-\alpha(v)).
\]

The left side and the final term lie in U', while [B_v,B_w] lies in W'. The trivial intersection gives [B_v,B_w]=0. Hence

\[
 D\alpha(w-v)=D(\alpha(w)-\alpha(v)).
\]

Both arguments lie in U', and D is injective there. Thus alpha(w−v)=alpha(w)−alpha(v), which implies additivity on U. This includes U=0. QED.

## 2. A joint-kernel observation

Suppose T_1,...,T_m are commuting endomorphisms of a finite-dimensional vector space C and have zero common kernel. For every positive N,

\[
 \bigcap_i\ker T_i^N=0.
\]

**Proof.** Their common power-kernel Q is invariant under every T_i. Each T_i is nilpotent on Q. If Q were nonzero, successive restriction to kernels would produce a nonzero vector killed by all the T_i: at each step, the next nilpotent acts on a nonzero invariant subspace and has nonzero kernel. This contradicts the zero common kernel. QED.

This fact is valid over every field and does not require an invertible linear combination of the T_i.

## 3. Proof of the theorem

Put V=[L,L], which is abelian, and C=C_L(V). The subspace C is an ideal. For x∈L, c∈C and v∈V, the Jacobi identity gives [[x,c],v]=0, since [c,v]=0 and [x,v]∈V. Thus [x,c]∈C.

Fix a K-basis x_1,...,x_m of L and N at least max(1,dim L). On C the operators

\[
 T_i=\operatorname{ad}_{x_i}|_C
\]

commute: their commutator is ad_[x_i,x_j], which annihilates C because [x_i,x_j]∈V. Their common kernel is C∩Z(L)=0. The joint-kernel observation therefore gives

\[
 C\cap\bigcap_i\ker(\operatorname{ad}_{x_i})^N=0. \tag{1}
\]

Let alpha:L→S be a bracket-preserving bijection. For any e∈L, the Fitting image U_e=im(ad_e)^N lies in V, hence is abelian. The Fitting-image lemma proves alpha additive on every U_e separately.

We next prove additivity on V. For v,w∈V, form the defect in the already-given target additive group:

\[
 \delta=\alpha(v+w)-\alpha(v)-\alpha(w).
\]

Since every element of V commutes with v,w,v+w, delta centralizes alpha(V). Surjectivity supplies an element a∈L with alpha(a)=delta. Bracket preservation and injectivity show that a centralizes V, so a∈C.

For each i, put D_i=ad_alpha(x_i). Since all three source arguments below lie in U_{x_i}, where alpha is additive,

\[
 \begin{aligned}
 D_i^N\delta
 &=\alpha((\operatorname{ad}_{x_i})^N(v+w))
   -\alpha((\operatorname{ad}_{x_i})^Nv)
   -\alpha((\operatorname{ad}_{x_i})^Nw)\\
 &=0.
 \end{aligned}
\]

The same intertwining identity implies (ad_{x_i})^N a=0. By (1), a=0. Hence delta=0, proving additivity of alpha on V.

Finally let x,y∈L be arbitrary. For every z∈L, all three brackets [x+y,z], [x,z], [y,z] belong to V. The established additivity on V yields

\[
 [\alpha(x+y)-\alpha(x)-\alpha(y),\alpha(z)]=0.
\]

The center of S is zero: a bracket-preserving bijection carries centers to centers as sets. Surjectivity now forces alpha(x+y)=alpha(x)+alpha(y). QED.

## 4. Finite-field family requiring the extension

Let K=F_q, A=K^2, and choose one nonzero linear form lambda in A* from each one-dimensional subspace of A*. There are q+1 such forms. Let

\[
 V=\bigoplus_{\lambda}K v_\lambda,
 \qquad a(v_\lambda)=\lambda(a)v_\lambda,
 \qquad L_q=A\ltimes V.
\]

The action of A is faithful, its common fixed space in V is zero, and its acting operators commute. Therefore L_q is centerless and metabelian. Its dimension is q+3. Every v_lambda belongs to [A,V] because lambda takes a nonzero value, so [L_q,L_q]=V.

For every a∈A, some lambda has lambda(a)=0: this is immediate for a=0, and for nonzero a its annihilator is a one-dimensional subspace of A*. Thus **every** ad_a on V is singular. Translating a by an element of V does not alter its action on V. Consequently L_q has no element acting invertibly on its derived algebra.

The new theorem nevertheless proves L_q is a UA-Lie ring. These examples show why choosing one global regular element cannot establish the all-field theorem. At q=2 this is an explicit five-dimensional example.

## 5. Finite Lie rings beyond fields

**Corollary.** Every finite centerless metabelian Lie ring is a UA-Lie ring.

**Proof.** The proof above only needs two finite-dimensional facts, both of which hold for finite abelian groups. An endomorphism d of a finite abelian group has stabilized kernels and images; once both stabilize at N, it acts bijectively on U=im d^N and U∩ker d^N=0. For completeness, d maps U onto itself by image stabilization and is therefore bijective by finiteness; if u∈U and d^N u=0, bijectivity on U gives u=0. The Fitting-image addition lemma uses precisely these properties and the iterated derivation identity, all valid for Lie rings.

The joint-kernel observation also holds for commuting endomorphisms of an abelian group whenever their common power-kernel is nonzero: finitely many commuting nilpotent endomorphisms on a nonzero abelian group have a nonzero common kernel by the same successive-kernel argument. A nilpotent endomorphism cannot be injective on a nonzero group, since then its zero power would be injective.

For a finite Lie ring take the finite list x_1,...,x_m of all its elements and choose N large enough for the kernel/image chains of every ad_x to stabilize. The restrictions to C_L([L,L]) commute, and their common kernel is the center. The proof in Section 3 now applies verbatim, with additive groups replacing vector spaces. QED.

This includes Lie rings whose additive groups have exponent p^a with a>1; they need not be Lie algebras over a field. No assertion about every infinite centerless metabelian Lie ring follows.

## 6. Boundaries and remaining work

The proof reconstructs addition on each Fitting image and then eliminates a global defect using commuting operators on C_L([L,L]). It does not assume that alpha preserves a direct-sum decomposition, preserves scalar multiplication, or commutes with an additive sum of adjoint operators before additivity is proved.

The centralizer ideal is essential to the gluing proof: adjoint operators need not commute on all of L, but they do commute on C_L([L,L]). No assertion C_L([L,L])=[L,L] is needed.

For nonmetabelian L, Fitting images need not be abelian and the local lemma is unavailable. For general infinite-dimensional metabelian L, kernel/image stabilization and the finite joint-kernel argument need not hold. Neither wider question is solved here.

This completes the mathematical extension as proposed. Independent adversarial review, a fresh scope/priority audit, and integration into a coherent Markdown manuscript remain required before promotion under the stricter goal.

## 7. Unified finite-length statement

The parent identified the following natural common formulation of the two results above; its Fitting and generating-set details have been verified here.

**Theorem (finite length).** Let R be a commutative unital ring and L a Lie algebra over R whose underlying R-module has finite length. If L is centerless and metabelian, then L is a UA-Lie ring.

**Proof.** Write ell for the length of L as an R-module and choose N≥max(1,ell). For every e∈L, d=ad_e is R-linear. Both chains ker d^j and im d^j stabilize by j=N: each strict inclusion changes length by at least one, and a repeated term forces all subsequent terms to repeat. Hence im d^N=im d^{N+1} and ker d^N=ker d^{2N}. For U=im d^N and W=ker d^N, d maps U onto U. If u=d^N x belongs to U∩W, then d^{2N}x=0, whence d^Nx=0 and u=0. Thus d acts injectively, and therefore bijectively, on U. The derivation formula proves W closed under brackets exactly as before. These are all the source properties used in the Fitting-image addition lemma, so that lemma holds in this setting.

A finite-length R-module is finitely generated: this follows by induction along a composition series, since each simple factor is cyclic. Choose R-module generators x_1,...,x_m of L. The centralizer C=C_L([L,L]) is an R-submodule and an ideal. Its adjoint restrictions T_i commute, and their common kernel is Z(L)=0. Indeed, commuting with all the generators is equivalent, by R-bilinearity of the bracket, to commuting with every element of L. The joint-kernel observation is a statement about commuting endomorphisms of abelian groups and remains valid for these T_i.

Apply the proof of Section 3: recover addition on U_e for every e, place the defect on [L,L] inside alpha(C), kill it by the common power-kernel condition, then use centerlessness to eliminate the defect on all of L. All target calculations take place solely in its given Lie-ring operations. This proves the theorem. QED.

Taking R to be a field gives the all-field theorem. Taking R=Z gives all finite Lie rings, since every finite abelian group has finite length as a Z-module. Finite length is a genuine input; this proof does not claim that an arbitrary finitely generated module over an arbitrary ring has stabilized adjoint kernels and images.
