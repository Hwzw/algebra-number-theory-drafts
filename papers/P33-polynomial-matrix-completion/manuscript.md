# Sharp completion bounds for polynomial values of matrices

September 9, 2026

## Abstract

Let $`\mathbb F`$ be an algebraically closed field of characteristic zero and $`f\in\mathbb F[t]`$ a nonconstant polynomial. For each $`\lambda`$, take the smallest multiplicity of a root of $`f(t)-\lambda`$, and let $`E(f)`$ be the largest of these numbers. We prove that every prescription of $`r`$ rows of an $`n\times n`$ matrix can be completed to a value $`f(X)`$ if and only if $`n>E(f)(r-1)`$. Equivalently, for every rank-$`r`$ matrix $`A`$, the image of $`X\mapsto Af(X)`$ is the right ideal $`AM_n(\mathbb F)`$ exactly under this inequality. We deduce necessary and sufficient conditions for surjectivity and image linearity of sums $`\sum_i A_i f_i(X_i)`$ when the coefficient column spaces form a direct sum. For complementary coefficients and powers, these conditions are sharp in every dimension. The proof combines the chain decomposition of a partial linear operator with a dimension estimate for Jordan blocks under polynomial evaluation.

## 1. Introduction

Polynomial maps with matrix coefficients extend the usual matrix Waring problem. Panja, Saini and Singh [\[1\]](#ref-PSS) determined the images of $`AX^k+BY^\ell`$ on $`2\times2`$ matrices over an algebraically closed field. Gangwal, Mandal and Verma [\[3, Question 1.1\]](#ref-GMV) ask for surjectivity and image linearity in arbitrary dimension over infinite division algebras, and treat real and quaternion matrices of size two. Saini and Singh [\[2\]](#ref-SS) study the distinct regime in which one coefficient is invertible. For $`X^k+BY^k`$, they prove the necessary condition
```math
n>k(\dim\ker B-1),
```
and prove sufficiency in dimensions at most four. Their Question 6.1 asks whether sufficiency holds in all dimensions.

We study the regime in which the coefficient column spaces form a direct sum. In particular, both coefficients of a two-term map may be singular and have complementary column spaces. We obtain a complete classification in this regime, with arbitrary scalar polynomials in place of powers. The underlying result is a sharp uniform completion theorem. The decomposition of partial operators used in its proof is classical Kronecker theory; the contribution is the polynomial completion bound and its application to maps with coefficients.

Throughout, $`\mathbb F`$ is algebraically closed of characteristic zero, $`n\ge1`$, and $`f\in\mathbb F[t]`$ is nonconstant. Define

<a id="label-eq-ef"></a>

```math
\tag{1}
 e_f(\lambda)=\min_{\alpha:\,f(\alpha)=\lambda}
       \operatorname{ord}_{t=\alpha}(f(t)-\lambda),
 \qquad E(f)=\max_{\lambda\in\mathbb F} e_f(\lambda).
```

The minimum exists because $`\mathbb F`$ is algebraically closed. The maximum is finite, lies between $`1`$ and $`\deg f`$, and equals $`1`$ unless some fiber of $`f`$ has no simple point. For $`f(t)=t^k`$, one has $`E(f)=k`$.

<a id="theorem-1"></a>

**Theorem 1.1.**

<a id="label-thm-main"></a>

Let $`A\in M_n(\mathbb F)`$ have rank $`r`$. Then

<a id="label-eq-main"></a>

```math
\tag{2}
 \{Af(X):X\in M_n(\mathbb F)\}=AM_n(\mathbb F)
 \quad\Longleftrightarrow\quad n>E(f)(r-1).
```

Equivalently, for an $`r`$-dimensional subspace $`U`$ of an $`n`$-dimensional space $`V`$, every linear map $`L:U\to V`$ is the restriction of $`f(X)`$ for some $`X\in\operatorname{End}(V)`$ if and only if this inequality holds.

<!-- end theorem-1 -->

The equivalence with prescribed rows follows by transposition. The theorem concerns a uniform assertion over every prescription. An individual prescription can have a completion even when the inequality fails.

<a id="theorem-2"></a>

**Theorem 1.2.**

<a id="label-thm-sum"></a>

Let $`A_1,\ldots,A_m\in M_n(\mathbb F)`$, let $`f_1,\ldots,f_m\in\mathbb F[t]`$ be nonconstant, and suppose that the column spaces $`W_i=\operatorname{im}A_i`$ form a direct sum $`W=\bigoplus_i W_i`$. Set $`r_i=\operatorname{rank}A_i`$ and
```math
\Phi(X_1,\ldots,X_m)=\sum_{i=1}^m A_i f_i(X_i).
```
Then the following are equivalent:

1.  The image of $`\Phi`$ is a vector subspace of $`M_n(\mathbb F)`$.

2.  The image of $`\Phi`$ is $`\operatorname{Hom}(\mathbb F^n,W)`$.

3.  For every $`i`$, one has $`n>E(f_i)(r_i-1)`$.

Consequently, $`\Phi`$ is surjective on $`M_n(\mathbb F)`$ if and only if $`W=\mathbb F^n`$ and these inequalities all hold.

<!-- end theorem-2 -->

Neither theorem assumes that a coefficient is an idempotent or that different coefficients commute. The direct-sum hypothesis is on their images as linear maps. It is essential to the proof of Theorem [1.2](#label-thm-sum). We do not settle the case of overlapping column spaces or Question 6.1 of [\[2\]](#ref-SS).

## 2. Polynomial evaluation on Jordan blocks

Write $`J_d(\lambda)`$ for a Jordan block of size $`d`$ and eigenvalue $`\lambda`$. A block of size zero is omitted from a direct sum.

<a id="lemma-1"></a>

**Lemma 2.1.**

<a id="label-lem-jordan"></a>

Suppose $`f(\alpha)=\lambda`$ and $`e=\operatorname{ord}_{t=\alpha}(f(t)-\lambda)`$. The Jordan type of $`f(J_s(\alpha))-\lambda I`$ is the Jordan type of $`J_s(0)^e`$. In particular, for $`d\ge1`$ and $`s=e(d-1)+1`$,

<a id="label-eq-packet"></a>

```math
\tag{3}
 f(J_s(\alpha))\sim J_d(\lambda)\oplus
                  J_{d-1}(\lambda)^{\oplus(e-1)}.
```

Every matrix whose eigenvalues $`\lambda`$ satisfy $`e_f(\lambda)=1`$ is a value of $`f`$ on a matrix of the same size.

<!-- end lemma-1 -->

<a id="proof-1"></a>

**Proof.**

Put $`N=J_s(0)`$. Taylor expansion gives
```math
f(\alpha I+N)-\lambda I=N^e g(N),\qquad g(0)\ne0.
```
The matrix $`g(N)`$ is invertible and commutes with $`N`$. Thus, for every $`j\ge1`$, the nullity of $`(N^e g(N))^j`$ is the nullity of $`N^{ej}`$. The nullities of all powers determine a nilpotent Jordan type.

The chains of $`N^e`$ are the residue classes of the indices $`1,\ldots,s`$ modulo $`e`$. When $`s=e(d-1)+1`$, one chain has length $`d`$ and the other $`e-1`$ chains have length $`d-1`$. This proves [(3)](#label-eq-packet). When $`e=1`$, polynomial evaluation preserves the size of the Jordan block. Choose a simple preimage of each eigenvalue, apply this observation to every block, and conjugate the resulting direct sum. $`\square`$

<!-- end proof-1 -->

<a id="lemma-2"></a>

**Lemma 2.2.**

<a id="label-lem-exception"></a>

There is at most one $`\lambda\in\mathbb F`$ for which $`e_f(\lambda)>1`$.

<!-- end lemma-2 -->

<a id="proof-2"></a>

**Proof.**

Let $`d=\deg f`$. If all roots of $`f(t)-\lambda`$ have multiplicity at least two, this polynomial has at most $`\lfloor d/2\rfloor`$ distinct roots. The total multiplicity of these roots as zeros of $`f'`$ is therefore at least $`d-\lfloor d/2\rfloor`$. Two different fibers are disjoint and would contribute at least $`d`$ zeros to $`f'`$, counted with multiplicity. This contradicts $`\deg f'=d-1`$. $`\square`$

<!-- end proof-2 -->

The proof of Theorem [1.1](#label-thm-main) needs only finiteness of the exceptional set. Lemma [2.2](#label-lem-exception) also makes the parameter $`E(f)`$ easy to interpret. For example, $`f(t)=t^2(t-1)^3`$ has $`E(f)=2`$, although its degree is five: its zero fiber has minimum multiplicity two, and no other fiber is exceptional.

## 3. Decomposing a partial operator

We give the special case of the Kronecker decomposition needed below, including an elementary proof. For the general matrix-pencil decomposition, see Verdier [\[4, Section 8\]](#ref-V).

<a id="lemma-3"></a>

**Lemma 3.1.**

<a id="label-lem-chains"></a>

Let $`U\subseteq V`$ be finite-dimensional vector spaces and $`L:U\to V`$ linear. There is a basis of $`V`$ adapted to $`U`$ consisting of:

1.  a basis of an $`L`$-invariant space $`U_\infty\subseteq U`$;

2.  open chains
    ```math
    v_{i,1},\ldots,v_{i,\ell_i},v_{i,\ell_i+1},
     \qquad L(v_{i,j})=v_{i,j+1}\quad(1\le j\le\ell_i),
    ```
    where $`\ell_i\ge1`$, and precisely the first $`\ell_i`$ vectors belong to the adapted basis of $`U`$;

3.  additional vectors outside $`U`$.

If $`a=\dim U_\infty`$, $`r=\dim U`$, $`n=\dim V`$, $`c`$ is the number of chains and $`z`$ the number of additional vectors, then

<a id="label-eq-dimensions"></a>

```math
\tag{4}
 \sum_i\ell_i=r-a,\qquad c+z=n-r,\qquad c\le r-a.
```

<!-- end lemma-3 -->

<a id="proof-3"></a>

**Proof.**

Set $`U_{-1}=V`$, $`U_0=U`$, and
```math
U_{j+1}=\{u\in U:L(u)\in U_j\}\qquad(j\ge0).
```
These spaces form a descending chain. If $`U_d=U_{d+1}`$, then $`U_d`$ is $`L`$-invariant and all subsequent spaces equal it. Set $`U_\infty=U_d`$. For $`0\le j<d`$, the map $`L`$ induces an injection

<a id="label-eq-graded"></a>

```math
\tag{5}
 U_j/U_{j+1}\longrightarrow U_{j-1}/U_j.
```

Indeed, $`L(U_j)\subseteq U_{j-1}`$, and $`L(u)\in U_j`$ for $`u\in U_j`$ is equivalent to $`u\in U_{j+1}`$.

Starting at $`j=d-1`$ and proceeding downwards to $`j=0`$, choose representatives for a basis of $`U_j/U_{j+1}`$. At each stage retain the images under $`L`$ of the representatives already chosen one level higher, and extend them to a quotient basis. This is possible by [(5)](#label-eq-graded). Every newly added representative at level $`j`$ starts an actual chain of successive $`L`$-images with $`j+1`$ vectors in $`U`$ and one final vector outside $`U`$. Representatives propagated from higher levels continue an existing chain.

At each level the vectors of these chains give a basis of $`U_j/U_{j+1}`$. Together with a basis of $`U_\infty`$, all chain vectors lying in $`U`$ therefore form a basis of $`U`$. By the injection at $`j=0`$, the final vectors of the chains are linearly independent modulo $`U`$. Thus the basis remains independent after these final vectors are adjoined. Complete it to a basis of $`V`$. All chain equations are exact, since the representatives were propagated by the actual map $`L`$. The dimension formulas follow by counting basis vectors. $`\square`$

<!-- end proof-3 -->

## 4. The sharp completion bound

<a id="proof-4"></a>

**Proof of the extension assertion in Theorem [1.1](#label-thm-main).**

The case $`r=0`$ is immediate. Put $`E=E(f)`$. If $`E=1`$, extend $`L`$ arbitrarily to an endomorphism $`T`$ of $`V`$ and apply Lemma [2.1](#label-lem-jordan) to obtain $`T=f(X)`$. The required inequality is automatic since $`r\le n`$.

Suppose $`E\ge2`$ and

<a id="label-eq-budget"></a>

```math
\tag{6}
 n\ge E(r-1)+1.
```

Apply Lemma [3.1](#label-lem-chains). On each open chain, choose the image of its final vector so that the completed block is a companion matrix with distinct eigenvalues avoiding the critical values of $`f`$. Such a companion matrix exists: choose any required number of distinct elements outside this finite set and use their monic product as the characteristic polynomial. The completed block has an $`f`$-preimage in the same dimension, by Lemma [2.1](#label-lem-jordan).

It remains to handle $`R=L|_{U_\infty}`$. Split $`R`$ into Jordan blocks. For a block $`J_d(\lambda)`$, choose a preimage $`\alpha`$ of $`\lambda`$ with multiplicity $`e=e_f(\lambda)`$. Lemma [2.1](#label-lem-jordan) shows that this block, together with $`(e-1)(d-1)`$ additional dimensions, is a value of $`f`$: put $`e-1`$ blocks of size $`d-1`$ and eigenvalue $`\lambda`$ on those dimensions. The resulting direct sum is similar to $`f(J_{e(d-1)+1}(\alpha))`$. Transporting the preimage by this similarity gives the specified action of $`R`$ on the original block.

If no block requires additional dimensions, we are done. Otherwise $`a\ge2`$. If $`D`$ is the total number of additional dimensions required, then

<a id="label-eq-cost"></a>

```math
\tag{7}
 D=\sum_{\text{blocks }J_d(\lambda)}
        (e_f(\lambda)-1)(d-1)\le(E-1)(a-1).
```

For this estimate, retain only blocks with $`d\ge2`$ and $`e_f(\lambda)\ge2`$. Their total size is at most $`a`$, and their number is at least one.

There are $`z=n-r-c`$ unused basis vectors after completing the open chains. Equations [(4)](#label-eq-dimensions) and [(6)](#label-eq-budget) give
```math
\begin{align*}
 z&\ge(E-1)(r-1)-c\\
  &\ge(E-1)(a-1)+(E-2)(r-a)\\
  &\ge D.
\end{align*}
```
We may therefore use these vectors for all the required Jordan blocks. On any remaining vectors use scalar blocks, which are values of $`f`$. The direct sum of these constructions is an endomorphism $`T=f(X)`$ extending $`L`$.

For necessity, choose $`\lambda`$ with $`e_f(\lambda)=E`$ and prescribe $`L=J_r(\lambda)`$ on $`U`$. If $`T=f(X)`$ extends $`L`$, then $`U`$ is $`T`$-invariant and the minimal polynomial of $`T`$ is divisible by $`(t-\lambda)^r`$. Hence $`T`$ has a $`\lambda`$-Jordan block of length at least $`r`$. For each Jordan block $`J_s(\alpha)`$ of $`X`$ with $`f(\alpha)=\lambda`$, Lemma [2.1](#label-lem-jordan) bounds the largest resulting block by
```math
\left\lceil\frac{s}{\operatorname{ord}_{\alpha}(f-\lambda)}\right\rceil
 \le\left\lceil\frac nE\right\rceil.
```
Thus $`r\le\lceil n/E\rceil`$, which is equivalent to $`n>E(r-1)`$. $`\square`$

<!-- end proof-4 -->

<a id="proof-5"></a>

**Passage to the coefficient formulation.**

The space $`AM_n(\mathbb F)`$ consists of the matrices $`D`$ with $`\operatorname{im}D\subseteq\operatorname{im}A`$. For such a $`D`$, put $`U=\operatorname{im}A^{\mathsf T}`$ and define
```math
L(A^{\mathsf T}v)=D^{\mathsf T}v.
```
This is well defined because $`\ker A^{\mathsf T}\subseteq\ker D^{\mathsf T}`$. Every linear map $`U\to\mathbb F^n`$ is obtained this way. Moreover,
```math
Af(X)=D\quad\Longleftrightarrow\quad
 f(X^{\mathsf T})|_U=L.
```
The extension assertion proves [(2)](#label-eq-main). $`\square`$

<!-- end proof-5 -->

The necessity argument is the same Jordan-size obstruction that appears in [\[2, Proposition 4.2\]](#ref-SS) for power maps with one invertible coefficient. The sufficient completion argument supplies the other direction for the one-sided image problem.

## 5. Sums with independent coefficient images

<a id="proof-6"></a>

**Proof of Theorem [1.2](#label-thm-sum).**

Write $`V=\mathbb F^n`$ and $`\mathcal H_i=\operatorname{Hom}(V,W_i)`$. The direct-sum hypothesis gives a linear isomorphism
```math
\bigoplus_i\mathcal H_i\longrightarrow\operatorname{Hom}(V,W),
 \qquad(D_i)_i\longmapsto\sum_iD_i.
```
Under this isomorphism, $`\operatorname{im}\Phi`$ is the product of the individual images $`A_i f_i(M_n(\mathbb F))`$. Equality with $`\operatorname{Hom}(V,W)`$ is therefore equivalent to equality with $`\mathcal H_i`$ in every component. Theorem [1.1](#label-thm-main) proves the equivalence of assertions 2 and 3.

For assertion 1, let $`\Omega_i`$ be the set of matrices whose eigenvalues avoid the finitely many critical values of $`f_i`$. This is a nonempty Zariski open set, and Lemma [2.1](#label-lem-jordan) gives $`\Omega_i\subseteq f_i(M_n(\mathbb F))`$. Its image under the surjective linear map $`T\mapsto A_iT`$ is Zariski dense in $`\mathcal H_i`$. For instance, any polynomial vanishing on that image pulls back to a polynomial vanishing on the dense set $`\Omega_i`$, and hence vanishes identically. Thus each individual image is dense in $`\mathcal H_i`$, and $`\operatorname{im}\Phi`$ is dense in $`\operatorname{Hom}(V,W)`$. A vector subspace of a finite-dimensional vector space is Zariski closed. Consequently assertion 1 implies assertion 2; the reverse implication is immediate. The surjectivity statement follows. $`\square`$

<!-- end proof-6 -->

<a id="corollary-1"></a>

**Corollary 5.1.**

<a id="label-cor-powers"></a>

Suppose $`\operatorname{im}A\oplus\operatorname{im}B=\mathbb F^n`$, with ranks $`r`$ and $`s`$, and let $`k,\ell\ge1`$. Then $`AX^k+BY^\ell`$ is surjective if and only if
```math
n>k(r-1)\qquad\text{and}\qquad n>\ell(s-1).
```
Whenever either inequality fails, its image is Zariski dense in $`M_n(\mathbb F)`$ but is not a vector space. For $`k=\ell=2`$, surjectivity is equivalent to $`|r-s|\le1`$.

<!-- end corollary-1 -->

<a id="proof-7"></a>

**Proof.**

Apply Theorem [1.2](#label-thm-sum) with $`E(t^k)=k`$, $`E(t^\ell)=\ell`$, and use $`r+s=n`$. In the square case the two strict inequalities are equivalent to $`r-s<2`$ and $`s-r<2`$. $`\square`$

<!-- end proof-7 -->

For a small illustration, let $`n=3`$, $`A=\operatorname{diag}(1,1,0)`$ and $`B=\operatorname{diag}(0,0,1)`$. The map $`AX^2+BY^2`$ is surjective, whereas $`AX^3+BY^3`$ is not. Indeed, the latter misses $`C=\operatorname{diag}(J_2(0),0)`$: the first two rows of $`X^3`$ would have to be those of $`C`$, so $`X^3`$ would have a nilpotent Jordan block of length at least two. No cube of a $`3\times3`$ matrix can have such a block at zero. The same obstruction is already implicit in the general necessary condition of [\[2\]](#ref-SS); the example illustrates the classification rather than claiming priority for failure of the older surjectivity conjecture.

As a higher-degree example, replacing either square by $`f(X)=X^2(X-I)^3`$ leaves its threshold unchanged. More generally the degree of a scalar polynomial is replaced by the minimum multiplicity in its exceptional fiber, if that fiber exists.

## 6. Checks and remaining questions

The proof above is independent of computation. The accompanying exact-arithmetic script checks the partial-operator decomposition for all $`729`$ maps $`\mathbb F_3^2\to\mathbb F_3^3`$ and for $`924`$ additional maps over $`\mathbb F_7`$. It classifies all $`19683`$ matrices in $`M_3(\mathbb F_3)`$ by whether they have square or fourth roots over the algebraic closure, using nilpotent Jordan partitions. All $`729`$ prescriptions of two rows admit a square completion; $`721`$ admit a fourth-power completion, and the displayed nilpotent prescription is among the eight exceptions. The script also checks the dimension estimate and the balanced Jordan-block formula over explicit finite ranges. These checks are diagnostics for the universal proof, not substitutes for it.

Theorem [1.1](#label-thm-main) also gives a sharp criterion for the relaxed map $`X^k+BY`$, where the second variable enters linearly: it is surjective precisely when $`n>k(\dim\ker B-1)`$. Indeed, after quotienting the target by $`\operatorname{im}B`$, the problem is exactly a prescription on the dual subspace annihilating $`\operatorname{im}B`$. Requiring $`Y`$ itself to be a $`k`$-th power is an additional condition. Establishing that additional step would be necessary to resolve [\[2, Question 6.1\]](#ref-SS); our completion theorem does not establish it.

For general coefficient families with intersecting column spaces, a target no longer has unique components. Determining which decompositions admit polynomial preimages remains a natural next problem. Over non-algebraically-closed fields, arithmetic conditions on scalar preimages also enter, so the present rank criteria are not asserted there.

**Research disclosure.**

This manuscript was prepared with OpenAI Codex assistance in problem selection, proof development, literature search, computation and writing. It has not undergone independent expert review or journal peer review. The accompanying assessment separates the proved manuscript claims from unresolved questions and historical-priority limitations.

## References

<a id="ref-PSS"></a>

**\[1\]** S. Panja, P. Saini and A. Singh, *Images of polynomial maps with constants*, Mathematika **71** (2025), no. 3, e70031. Preprint: [arXiv:2312.13865](https://arxiv.org/abs/2312.13865).

<a id="ref-SS"></a>

**\[2\]** P. Saini and A. Singh, *Polynomial maps with constants on matrix algebra*, preprint (2026), [arXiv:2604.27592v1](https://arxiv.org/abs/2604.27592v1).

<a id="ref-GMV"></a>

**\[3\]** A. Gangwal, A. Mandal and S. Verma, *Polynomial maps with constants over division algebras and the generalized Kaplansky–L’vov conjecture*, preprint (2026), [arXiv:2607.27226v1](https://arxiv.org/abs/2607.27226v1).

<a id="ref-V"></a>

**\[4\]** O. Verdier, *Reduction and normal forms of matrix pencils*, preprint (2012), [arXiv:1205.1138](https://arxiv.org/abs/1205.1138), Section 8.
