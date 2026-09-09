# Unique addition in centerless metabelian Lie algebras

Henry Zweiman

September 8, 2026

## Abstract

A Lie ring has unique addition if every bracket-preserving bijection from it onto an arbitrary Lie ring is additive. We prove that every finite-dimensional centerless metabelian Lie algebra over an infinite field has unique addition, with no restriction on the characteristic. The underlying criterion applies to a faithful semidirect product $`A\ltimes V`$, where $`V`$ is an arbitrary abelian group and the acting Lie ring contains a central element acting invertibly on $`V`$. Applications include the nine-dimensional algebra in a question of Arzhantsev and families for which the least number of elements with zero common centralizer is arbitrarily large. We explain the relation with earlier additivity results for triangular associative algebras.

## 1. Introduction

A *unique-addition Lie ring*, or a *UA-Lie ring*, is a Lie ring $`L`$ such that, for every Lie ring $`S`$, each bijection $`\alpha:L\to S`$ satisfying
```math
\alpha([x,y])=[\alpha(x),\alpha(y)]\qquad(x,y\in L)
```
is additive. Neither additivity nor linearity is included in the hypothesis on $`\alpha`$. In particular, when $`L`$ is a Lie algebra over a field, the target need not be a Lie algebra over that field.

Arzhantsev’s recent account [\[1\]](#ref-Arz) develops structural criteria for this property and poses several open questions. An important sufficient condition, over an infinite field, is the existence of two elements whose common centralizer is zero. His Example 2 is a nine-dimensional centerless solvable Lie algebra for which this condition fails; Problem 4 asks whether that algebra nevertheless has unique addition. Our main result concerns a full class of centerless solvable Lie algebras.

<a id="theorem-1"></a>

**Theorem 1.**

<a id="label-thm-main"></a>

Every finite-dimensional centerless metabelian Lie algebra over an infinite field is a UA-Lie ring.

<!-- end theorem-1 -->

Here metabelian means that the derived algebra is abelian. The characteristic in Theorem [1](#label-thm-main) is arbitrary. The proof combines a faithful-action criterion with an elementary fact about commuting linear operators. Its first ingredient is valid without a field or a finiteness assumption.

<a id="theorem-2"></a>

**Theorem 2.**

<a id="label-thm-affine"></a>

Let $`V`$ be an abelian group, and let $`A`$ be a Lie subring of $`\mathop{\mathrm{End}}_{\mathbb Z}(V)`$, with the commutator bracket. Suppose that there is $`t\in A`$ which commutes with every element of $`A`$ and is bijective on $`V`$. Then
```math
L=A\ltimes V,\qquad
 [(a,v),(b,w)]=([a,b],a(w)-b(v)),
```
is a UA-Lie ring.

<!-- end theorem-2 -->

In particular, it is enough that $`A`$ contain the identity endomorphism. The ring $`A`$ is not required to be closed under associative multiplication; its inclusion in $`\mathop{\mathrm{End}}_{\mathbb Z}(V)`$ expresses faithfulness of the action. The inverse of $`t`$ need not belong to $`A`$.

There is a relevant earlier approach. Qi and Hou [\[3\]](#ref-QH) proved additivity modulo a central error for Lie-multiplicative bijections from triangular associative algebras. Their theorem is reproduced in [\[2, Theorem 1.1\]](#ref-FG), which also extends it. The target calculations in the proof of [\[2, Theorem 4.1, $`n=2`$\]](#ref-FG) use addition and brackets and adapt to arbitrary Lie-ring targets. Consequently the associative unital special case of Theorem [2](#label-thm-affine), including Arzhantsev’s particular matrix example, is obtainable by a central-extension argument from that earlier method. We give the argument in Section [5](#label-sec-comparison). The results here are formulated for arbitrary acting Lie subrings and yield Theorem [1](#label-thm-main) without an associative-closure assumption.

For comparison, Sosnov [\[4\]](#ref-Sos) recently classifies the UA property for $`\mathfrak{gl}_n(K)`$ and $`\mathfrak{sl}_n(K)`$ over fields and settles another question from [\[1\]](#ref-Arz). Those results concern the full matrix Lie rings and their special linear subrings. The present argument concerns faithful affine actions and metabelian Lie algebras.

## 2. Recovering addition from a faithful action

<a id="proof-1"></a>

**Proof of Theorem [2](#label-thm-affine).**

Fix a bracket-preserving bijection $`\alpha:L\to S`$. We identify $`A`$ and $`V`$ with their summands in $`L`$. Since $`\alpha([0,0])=[\alpha(0),\alpha(0)]`$, we have $`\alpha(0)=0`$. Set
```math
e=(t,0),\qquad E=\alpha(e),\qquad D=\mathop{\mathrm{ad}}_E:S\to S.
```
The map $`D`$ is an additive endomorphism of the given additive group of $`S`$. On $`L`$ we have
```math
[e,(a,v)]=(0,t(v)).
```
Centrality of $`t`$ in $`A`$ and bijectivity of $`t`$ on $`V`$ therefore give

<a id="label-eq-images"></a>

```math
\tag{1}
 \mathop{\mathrm{im}}D=\alpha(V)=:V',\qquad \ker D=\alpha(A)=:A'.
```

Thus $`A'`$ and $`V'`$ are additive subgroups of $`S`$. The subgroup $`V'`$ has zero bracket, and $`D|_{V'}`$ is bijective, since it is conjugate as a set map to $`t:V\to V`$.

We first prove

<a id="label-eq-mixed"></a>

```math
\tag{2}
 \alpha(a+v)=\alpha(a)+\alpha(v)\qquad(a\in A,\ v\in V).
```

Indeed, $`[e,a+v]=[e,v]`$, so $`\alpha(a+v)-\alpha(v)`$ lies in $`\ker D=\alpha(A)`$. Write this difference as $`\alpha(b)`$ with $`b\in A`$. For every $`w\in V`$, we have
```math
\begin{align*}
 \alpha(b(w))
 &=[\alpha(b),\alpha(w)]\\
 &=[\alpha(a+v)-\alpha(v),\alpha(w)]\\
 &=\alpha(a(w)).
\end{align*}
```
The last equality uses $`[V,V]=0`$. Injectivity implies $`b(w)=a(w)`$ for all $`w`$, and faithfulness gives $`b=a`$. This proves [(2)](#label-eq-mixed).

For $`v,w\in V`$, the identity
```math
[e+v,e+w]=t(w-v)
```
and [(2)](#label-eq-mixed) give
```math
\begin{align*}
 D\bigl(\alpha(w-v)\bigr)
 &=\alpha(t(w-v))\\
 &=[E+\alpha(v),E+\alpha(w)]\\
 &=D\bigl(\alpha(w)-\alpha(v)\bigr).
\end{align*}
```
Both arguments of $`D`$ belong to the additive subgroup $`V'`$. Its restriction to $`V'`$ is injective, whence
```math
\alpha(w-v)=\alpha(w)-\alpha(v).
```
It follows that $`\alpha|_V`$ is additive.

Now take $`a,b\in A`$. Since $`A'`$ is an additive subgroup, write
```math
\alpha(a)+\alpha(b)=\alpha(c),\qquad c\in A.
```
For every $`w\in V`$, additivity on $`V`$ yields
```math
\begin{align*}
 \alpha(c(w))
 &=[\alpha(a)+\alpha(b),\alpha(w)]\\
 &=\alpha(a(w))+\alpha(b(w))
 =\alpha((a+b)(w)).
\end{align*}
```
Again injectivity and faithfulness give $`c=a+b`$. Thus $`\alpha|_A`$ is additive. Equation [(2)](#label-eq-mixed) now proves additivity on $`L=A\oplus V`$. $`\square`$

<!-- end proof-1 -->

<a id="corollary-1"></a>

**Corollary 3.**

<a id="label-cor-intrinsic"></a>

Let $`L`$ be a Lie ring with an abelian ideal $`V`$ satisfying $`C_L(V)=V`$. Suppose that some $`e\in L`$ satisfies $`[e,L]\subseteq V`$ and that $`\mathop{\mathrm{ad}}_e|_V`$ is bijective. Then $`L`$ is a UA-Lie ring.

<!-- end corollary-1 -->

<a id="proof-2"></a>

**Proof.**

Put $`A=C_L(e)`$. For $`x\in L`$, choose the unique $`v\in V`$ with $`[e,v]=[e,x]`$. Then $`x-v\in A`$. Also $`A\cap V=0`$, so $`L=A\ltimes V`$. The action of $`A`$ on $`V`$ is faithful because
```math
C_A(V)\subseteq A\cap C_L(V)=A\cap V=0.
```
The element $`e`$ is central in $`A`$ and acts bijectively on $`V`$. Apply Theorem [2](#label-thm-affine). $`\square`$

<!-- end proof-2 -->

<a id="remark-1"></a>

**Remark 4.**

Surjectivity of $`\alpha`$ is used in [(1)](#label-eq-images): it identifies its images of the two source summands with an image and a kernel in the target additive group. Theorem [2](#label-thm-affine) makes no assertion about arbitrary bracket-preserving injections. All subtractions in its proof occur in the already-given Lie ring $`S`$; no transported addition is assumed in advance.

<!-- end remark-1 -->

## 3. Centerless metabelian Lie algebras

<a id="lemma-1"></a>

**Lemma 5.**

<a id="label-lem-commuting"></a>

Let $`T_1,\ldots,T_m`$ be commuting endomorphisms of a nonzero finite-dimensional vector space $`V`$ over an infinite field $`K`$. If
```math
\bigcap_{i=1}^m\ker T_i=0,
```
then some $`K`$-linear combination of the $`T_i`$ is invertible.

<!-- end lemma-1 -->

<a id="proof-3"></a>

**Proof.**

Extend scalars to an algebraic closure $`F`$ of $`K`$. The common kernel stays zero, since it is the kernel of the scalar extension of the map $`v\mapsto(T_1v,\ldots,T_mv)`$.

Successive decompositions into generalized eigenspaces give a direct-sum decomposition of $`V_F`$ into nonzero simultaneous generalized eigenspaces $`V_\lambda`$. Commutativity ensures invariance at each step. On $`V_\lambda`$ we have
```math
T_i=\lambda_i I+N_i,
```
where the $`N_i`$ commute and are nilpotent. The tuple $`\lambda`$ cannot be zero. Otherwise the commuting nilpotents would have a nonzero common kernel: successively take kernels, each time restricting the next nilpotent to the nonzero invariant subspace already obtained.

Choose $`c_1,\ldots,c_m\in F`$ so that $`\sum_i c_i\lambda_i\ne0`$ for every one of the finitely many nonzero weight tuples. This is possible over the infinite field $`F`$. The operator $`\sum_i c_iT_i`$ is invertible on every $`V_\lambda`$, since a sum of commuting nilpotents is nilpotent. For the latter fact, expand a sufficiently high power; each monomial contains a power at least the nilpotence exponent of one of the operators.

It follows that
```math
\det(X_1T_1+\cdots+X_mT_m)\in K[X_1,\ldots,X_m]
```
is a nonzero polynomial. Over the infinite field $`K`$ it has a nonzero value at some $`K`$-rational tuple, as required. $`\square`$

<!-- end proof-3 -->

<a id="proof-4"></a>

**Proof of Theorem [1](#label-thm-main).**

Let $`L`$ be centerless and metabelian, and set $`V=[L,L]`$. If $`V=0`$, then centerlessness forces $`L=0`$, and the conclusion is immediate. Otherwise the endomorphisms of $`V`$ induced by the adjoint action of $`L`$ commute, because $`V`$ is abelian. Their common kernel is
```math
V\cap Z(L)=0.
```
Apply Lemma [5](#label-lem-commuting) to a basis of the space of acting endomorphisms. There is $`e\in L`$ such that $`\mathop{\mathrm{ad}}_e|_V`$ is invertible.

Set $`A=C_L(e)`$. Since $`[e,L]\subseteq V`$, for every $`x\in L`$ there is a unique $`v\in V`$ with $`[e,v]=[e,x]`$. Thus $`L=A\oplus V`$ as vector spaces. For $`a,b\in A`$, the bracket $`[a,b]`$ belongs to $`V`$ and commutes with $`e`$, so it is zero. Therefore $`A`$ is abelian. If an element of $`A`$ annihilates $`V`$, it commutes with both $`A`$ and $`V`$ and hence is central in $`L`$. The action of $`A`$ on $`V`$ is consequently faithful.

We have expressed $`L`$ as $`A\ltimes V`$, with $`e`$ central in $`A`$ and invertible on $`V`$. Theorem [2](#label-thm-affine) applies. $`\square`$

<!-- end proof-4 -->

<a id="remark-2"></a>

**Remark 6.**

The infinite-field assumption enters only when choosing a rational point at which the determinant polynomial is nonzero. The affine criterion itself applies over finite fields. The preceding argument does not assert that every centerless metabelian Lie algebra over a finite field contains an element acting invertibly on its derived algebra.

<!-- end remark-2 -->

## 4. Common centralizers and the matrix example

For a finite-dimensional centerless Lie algebra $`L`$, denote by $`c(L)`$ the least size of a tuple with zero common centralizer. Thus the C-condition of [\[1\]](#ref-Arz) is $`c(L)\le2`$. We use this notation only to quantify the following separation.

Let $`K`$ be any field, $`U=K^r`$, $`W=K^s`$, and $`V=U\oplus W`$, where $`r,s\ge1`$. Extend each element of $`\mathop{\mathrm{Hom}}_K(W,U)`$ by zero on $`U`$, and put
```math
A=K I_V\oplus\mathop{\mathrm{Hom}}_K(W,U),\qquad L_{r,s}=A\ltimes V.
```
Two elements of $`\mathop{\mathrm{Hom}}_K(W,U)`$ have zero product, so $`A`$ is an abelian Lie algebra. In block form,

<a id="label-eq-block"></a>

```math
\tag{3}
 L_{r,s}=\left\{
 \begin{pmatrix}
  aI_r&M&u\\
  0&aI_s&w\\
  0&0&0
 \end{pmatrix}
 :a\in K,\ M\in\mathop{\mathrm{Hom}}_K(W,U),\ u\in U,\ w\in W
 \right\}.
```

<a id="proposition-1"></a>

**Proposition 7.**

<a id="label-prop-centralizers"></a>

Over every field, $`L_{r,s}`$ is a centerless UA-Lie ring and
```math
c(L_{r,s})=s+1.
```

<!-- end proposition-1 -->

<a id="proof-5"></a>

**Proof.**

The UA assertion follows from Theorem [2](#label-thm-affine). Take any $`\ell`$ elements, and write
```math
x_i=(a_i,M_i,u_i,w_i).
```
An element $`z=(0,N,v,0)`$ centralizes all of them precisely when
```math
N(w_i)-a_iv=0\qquad(1\le i\le\ell).
```
The pairs $`(N,v)`$ identify with maps $`F:W\oplus K\to U`$ by $`F(w,a)=N(w)-av`$. Thus their solution space has dimension
```math
r\bigl(s+1-\dim\langle(w_i,a_i):1\le i\le\ell\rangle\bigr)
 \ge r(s+1-\ell).
```
For $`\ell\le s`$ this is positive.

Conversely, let $`w_1,\ldots,w_s`$ be a basis of $`W`$. The common centralizer of $`e=(I_V,0)`$ and the $`s`$ translation vectors $`w_1,\ldots,w_s`$ is zero. Commuting with $`e`$ removes the translation component. An element $`aI_V+M`$ annihilating every $`w_j`$ has $`a=0`$ by its $`W`$-component and then $`M=0`$. This proves the upper bound and also centerlessness. $`\square`$

<!-- end proof-5 -->

For $`r=s=2`$, formula [(3)](#label-eq-block) is exactly the algebra in [\[1, Example 2, Problem 4, p. 184\]](#ref-Arz). Proposition [7](#label-prop-centralizers) gives an affirmative answer to that question. The family also shows that there is no universal bound on $`c(L)`$ among UA-Lie algebras.

The same phenomenon occurs when the acting Lie algebra is not closed under associative multiplication. Let $`T=K^3`$, let $`N`$ be a nilpotent Jordan block of size three on $`T`$, and extend it by zero on $`U\oplus W`$. On $`\widetilde V=T\oplus U\oplus W`$, set
```math
\widetilde A=K I_{\widetilde V}\oplus K N\oplus\mathop{\mathrm{Hom}}_K(W,U).
```
The operators in $`\widetilde A`$ commute, but $`N^2\notin\widetilde A`$. Theorem [2](#label-thm-affine) applies to $`\widetilde L=\widetilde A\ltimes\widetilde V`$.

Moreover $`c(\widetilde L)=s+1`$. The lower-bound calculation above is unchanged, since $`N`$ acts trivially on $`U\oplus W`$. For the upper bound, choose a Jordan basis $`t_1,t_2,t_3`$ with $`N(t_3)=t_2`$, and use $`e`$ and the translation vectors
```math
w_1+t_3,\ w_2,\ldots,w_s.
```
An element $`aI+bN+M`$ annihilating these vectors has successively $`a=0`$, $`b=0`$, and $`M=0`$. Thus these examples simultaneously lack associative closure of the acting algebra and, when $`s\ge2`$, fail the two-centralizer condition.

## 5. Relation with triangular associative algebras

<a id="label-sec-comparison"></a>

Suppose for this paragraph that $`A`$ is an associative unital $`K`$-algebra acting faithfully on $`V`$. The Lie algebra underlying $`\mathop{\mathrm{Tri}}(A,V,K)`$ is isomorphic to
```math
(A\ltimes V)\oplus K,
```
where the last summand is central: the isomorphism sends a triangular block $`(a,v,b)`$ to $`((a-bI,v),b)`$.

Given a bracket-preserving bijection $`\alpha:A\ltimes V\to S`$, extend it by the identity on the central copy of $`K`$. The target is the Lie ring $`S\oplus K`$. The argument for triangular algebras in [\[3\]](#ref-QH), reproduced and extended in [\[2\]](#ref-FG), yields additivity modulo the center after adapting its bracket calculations to this target. Since $`A\ltimes V`$ is centerless, so is $`S`$. Comparing the extra $`K`$-coordinates eliminates the remaining central error. This recovers the associative unital affine case.

Accordingly, the particular matrix answer should be understood together with this prior proof-level route. The proof in Section 2 is a direct structural argument requiring only a faithful Lie action and a central invertible acting element. It permits acting Lie subrings without associative closure, arbitrary abelian translation groups, and the metabelian consequence of Section 3. No inheritance of the UA property by arbitrary Lie subalgebras is used or asserted.

## References

<a id="ref-Arz"></a>

**\[1\]** I. Arzhantsev, *Uniqueness of addition in Lie algebras revisited*, Math. Commun. **30** (2025), 179–189. [doi:10.64785/mc.30.2.3](https://doi.org/10.64785/mc.30.2.3).

<a id="ref-FG"></a>

**\[2\]** B. L. M. Ferreira and H. Guzzo Jr., *Lie $`n`$-multiplicative mappings on triangular $`n`$-matrix rings*, Rev. Un. Mat. Argentina **60** (2019), no. 1, 9–20. [doi:10.33044/revuma.v60n1a02](https://doi.org/10.33044/revuma.v60n1a02).

<a id="ref-QH"></a>

**\[3\]** X. Qi and J. Hou, *Additivity of Lie multiplicative maps on triangular algebras*, Linear Multilinear Algebra **59** (2011), no. 4, 391–397. [doi:10.1080/03081080903582094](https://doi.org/10.1080/03081080903582094).

<a id="ref-Sos"></a>

**\[4\]** G. Sosnov, *Uniqueness of addition in Lie rings $`\mathfrak{gl}_n(K)`$ and $`\mathfrak{sl}_n(K)`$*, preprint (2026). [arXiv:2606.08201v1](https://arxiv.org/abs/2606.08201).
