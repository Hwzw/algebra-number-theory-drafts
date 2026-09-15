# Counterexamples to a nullity criterion for matrix power maps

Henry Zweiman

September 15, 2026

## Abstract

For every integer $`k\ge5`$ and every field $`\mathbb F`$, we construct a diagonal idempotent $`B\in M_{k+1}(\mathbb F)`$ of nullity two for which the map $`(X,Y)\mapsto X^k+BY^k`$ is not surjective. An explicit omitted value is the direct sum of three nilpotent Jordan blocks of size two, transposed, and $`k-5`$ zero blocks. Since $`k+1>k(\dim\ker B-1)`$, this gives a negative answer to the sufficiency question posed by Saini and Singh. The first example concerns fifth powers of $`6\times6`$ matrices. The proof uses two elementary facts: in dimension $`k+1`$, a $`k`$-th power with a nontrivial zero chain has rank one, and a one-dimensional perturbation of a square-zero map of rank two forces such a chain. Over algebraically closed fields of characteristic zero, the image is dense but not closed under addition.

## 1. Introduction and main result

Polynomial maps with nonscalar matrix coefficients extend matrix Waring problems. The behavior of a singular coefficient can differ substantially from that of a scalar coefficient, even if another coefficient is invertible. Saini and Singh [\[1\]](#ref-SS) study the maps
```math
(X,Y)\longmapsto A_1X^k+A_2Y^k
```
over algebraically closed fields of characteristic zero, with $`A_1`$ invertible. For $`B=A_1^{-1}A_2`$, they prove that surjectivity requires

<a id="label-eq-criterion"></a>

```math
\tag{1}
 n>k(\dim\ker B-1),
```

and establish sufficiency when $`n\le4`$ and, in every dimension, when $`\dim\ker B\le1`$. Their Question 6.1 asks whether [(1)](#label-eq-criterion) is sufficient in general. Related questions about surjectivity and image linearity over division algebras are considered by Gangwal, Mandal and Verma [\[2\]](#ref-GMV), particularly in dimension two.

We give counterexamples to the proposed sufficiency criterion. They use diagonal idempotent coefficients, so nontrivial nilpotent Jordan blocks in the coefficient are not needed. The argument works over every field.

Let
```math
J=\begin{pmatrix}0&1\\0&0\end{pmatrix}.
```
We use $`0_s`$ for the zero matrix of size $`s`$, with a zero-size summand omitted.

<a id="theorem-1"></a>

**Theorem 1.1.**

<a id="label-thm-main"></a>

Let $`\mathbb F`$ be any field and $`k\ge5`$. Set $`n=k+1`$ and

<a id="label-eq-matrices"></a>

```math
\tag{2}
 B_k=0_2\oplus I_{k-1},\qquad
 C_k=J^{\mathsf T}\oplus J^{\mathsf T}\oplus J^{\mathsf T}\oplus0_{k-5}.
```

There are no $`X,Y\in M_n(\mathbb F)`$ satisfying

<a id="label-eq-impossible"></a>

```math
\tag{3}
 X^k+B_kY^k=C_k.
```

In particular, the map $`(X,Y)\mapsto X^k+B_kY^k`$ is not surjective although $`B_k^2=B_k`$, $`\dim\ker B_k=2`$, and
```math
n=k+1>k(\dim\ker B_k-1).
```

<!-- end theorem-1 -->

Thus Question 6.1 of [\[1\]](#ref-SS) has a negative answer. This does not affect the necessity of [(1)](#label-eq-criterion) or the positive results in the regimes proved there. Our first example has size six; we do not claim that six is the smallest possible size for a counterexample.

## 2. Two linear-algebra lemmas

The first lemma isolates the special role of the dimension $`k+1`$. It can be read from Jordan form, but a cyclic-vector argument avoids assumptions on the field.

<a id="lemma-1"></a>

**Lemma 2.1.**

<a id="label-lem-rigid"></a>

Let $`V`$ have dimension $`k+1`$ over a field $`\mathbb F`$, and let $`A\in\operatorname{End}(V)`$. If
```math
\operatorname{im}(A^k)\cap\ker(A^k)\ne0,
```
then $`A`$ is cyclic nilpotent and $`\operatorname{rank}(A^k)=1`$.

<!-- end lemma-1 -->

<a id="proof-1"></a>

**Proof.**

Choose $`v\in V`$ with $`A^kv\ne0`$ and $`A^{2k}v=0`$, and let $`s`$ be the least positive integer such that $`A^sv=0`$. Then $`s\ge k+1`$. The vectors
```math
v,Av,\ldots,A^{s-1}v
```
are linearly independent. Indeed, if a nonzero relation has its first nonzero coefficient at $`A^jv`$, applying $`A^{s-1-j}`$ gives a nonzero scalar multiple of $`A^{s-1}v`$ equal to zero. Hence $`s\le\dim V=k+1`$, so $`s=k+1`$ and these vectors form a basis of $`V`$. In this basis $`A`$ is a single nilpotent Jordan block. Its $`k`$-th power has rank one. $`\square`$

<!-- end proof-1 -->

The next lemma concerns an arbitrary extension of a prescribed map. There is no assumption on its action outside the indicated subspace.

<a id="lemma-2"></a>

**Lemma 2.2.**

<a id="label-lem-chain"></a>

Let $`W\subseteq V`$ be vector spaces over a field $`\mathbb F`$, let $`u\in V\setminus W`$, and let $`N\in\operatorname{End}(W)`$ satisfy $`N^2=0`$ and $`\operatorname{rank}N\ge2`$. Suppose that $`Z\in\operatorname{End}(V)`$ satisfies

<a id="label-eq-restriction"></a>

```math
\tag{4}
 Zw=Nw+\phi(w)u\qquad(w\in W)
```

for a linear functional $`\phi`$ on $`W`$. Then
```math
\operatorname{im}Z\cap\ker Z\ne0.
```

<!-- end lemma-2 -->

<a id="proof-2"></a>

**Proof.**

Put $`R=\operatorname{im}N`$ and $`K=\ker N`$. Since $`N^2=0`$, one has $`R\subseteq K`$, and $`\dim R\ge2`$.

First suppose that $`\phi|_K\ne0`$. Choose a nonzero $`r\in R\cap\ker\phi`$; a single linear functional cannot be injective on a space of dimension at least two. Choose $`w_0\in W`$ with $`Nw_0=r`$. Since $`\phi|_K`$ is a nonzero functional, there is $`a\in K`$ such that $`\phi(w_0+a)=0`$. With $`w=w_0+a`$, equation [(4)](#label-eq-restriction) gives $`Zw=r`$. Also $`Nr=0`$ and $`\phi(r)=0`$, so $`Zr=0`$.

Now suppose that $`\phi|_K=0`$. There is a well-defined linear functional $`\ell:R\to\mathbb F`$ such that $`\ell(Nw)=\phi(w)`$ for every $`w\in W`$. Choose a nonzero $`r\in\ker\ell`$, possible because $`\dim R\ge2`$, and choose $`w\in W`$ with $`Nw=r`$. Then $`\phi(w)=0`$, so $`Zw=r`$. Since $`r\in R\subseteq K`$ and $`\phi`$ vanishes on $`K`$, one also has $`Zr=0`$.

In either case, the nonzero vector $`r`$ belongs to $`\operatorname{im}Z\cap\ker Z`$. $`\square`$

<!-- end proof-2 -->

<a id="remark-1"></a>

**Remark 2.3.**

The rank hypothesis in Lemma [2.2](#label-lem-chain) cannot be replaced by $`\operatorname{rank}N\ge1`$. For example, on a space with basis $`u,a,b`$, put $`Na=0`$, $`Nb=a`$ on $`W=\langle a,b\rangle`$, and define
```math
Zu=b,\qquad Za=u,\qquad Zb=a.
```
Then [(4)](#label-eq-restriction) holds with $`\phi(a)=1`$ and $`\phi(b)=0`$, but $`Z`$ is invertible. This explains why two square-zero blocks are used on the complementary subspace in our construction.

<!-- end remark-1 -->

## 3. Proof and the first explicit example

<a id="proof-3"></a>

**Proof of Theorem [1.1](#label-thm-main).**

Suppose [(3)](#label-eq-impossible) holds. Transposing, and writing $`A=X^{\mathsf T}`$ and $`D=Y^{\mathsf T}`$, gives

<a id="label-eq-transposed"></a>

```math
\tag{5}
 M=A^k+D^kB_k,\qquad
 M=J\oplus J\oplus J\oplus0_{k-5}.
```

Let $`e_1,\ldots,e_n`$ be the standard basis and set
```math
U=\langle e_1,e_2\rangle,\qquad
 W=\langle e_3,\ldots,e_n\rangle.
```
The coefficient $`B_k`$ vanishes on $`U`$ and is the identity on $`W`$. Put $`T=A^k`$ and $`Z=D^k`$. Restricting [(5)](#label-eq-transposed) to $`U`$ gives
```math
Te_2=e_1,\qquad Te_1=0.
```
Thus $`e_1\in\operatorname{im}T\cap\ker T`$, and Lemma [2.1](#label-lem-rigid) gives $`\operatorname{rank}T=1`$. Since its image contains $`e_1`$, there is a linear functional $`\lambda`$ on $`V`$ such that $`Tv=\lambda(v)e_1`$ for all $`v\in V`$.

On $`W`$, equation [(5)](#label-eq-transposed) now becomes
```math
Zw=Nw-\lambda(w)e_1,
\qquad
 N=J\oplus J\oplus0_{k-5}\in\operatorname{End}(W).
```
Here $`N^2=0`$, $`\operatorname{rank}N=2`$, and $`e_1\notin W`$. Lemma [2.2](#label-lem-chain) shows that $`\operatorname{im}Z\cap\ker Z\ne0`$. Applying Lemma [2.1](#label-lem-rigid) to $`D`$ therefore gives $`\operatorname{rank}Z=1`$.

However, let $`\pi_W:V\to W`$ be the projection along $`U`$. The last displayed identity gives
```math
\pi_W\circ Z|_W=N,
```
so $`\operatorname{rank}Z\ge\operatorname{rank}N=2`$. This contradiction proves the theorem. $`\square`$

<!-- end proof-3 -->

For $`k=5`$, the omitted target and its coefficient are the following matrices over any field:
```math
B_5=\begin{pmatrix}
 0&0&0&0&0&0\\0&0&0&0&0&0\\0&0&1&0&0&0\\
 0&0&0&1&0&0\\0&0&0&0&1&0\\0&0&0&0&0&1
 \end{pmatrix},\qquad
 C_5=\begin{pmatrix}
 0&0&0&0&0&0\\1&0&0&0&0&0\\0&0&0&0&0&0\\
 0&0&1&0&0&0\\0&0&0&0&0&0\\0&0&0&0&1&0
 \end{pmatrix}.
```
They satisfy $`\operatorname{rank}B_5=4`$, $`\operatorname{rank}C_5=3`$, and $`6>5(2-1)`$, but $`C_5\ne X^5+B_5Y^5`$ for all $`X,Y\in M_6(\mathbb F)`$.

## 4. Image geometry and the remaining classification

<a id="corollary-1"></a>

**Corollary 4.1.**

<a id="label-cor-image"></a>

Let $`\mathbb F`$ be algebraically closed of characteristic zero, and let $`k\ge5`$. The image of
```math
\Psi_k:M_{k+1}(\mathbb F)^2\longrightarrow M_{k+1}(\mathbb F),
 \qquad \Psi_k(X,Y)=X^k+B_kY^k,
```
is Zariski dense and is not closed under addition. In particular, it is not a vector subspace.

<!-- end corollary-1 -->

<a id="proof-4"></a>

**Proof.**

Every invertible matrix has a $`k`$-th root over $`\mathbb F`$, so setting $`Y=0`$ shows that $`\operatorname{im}\Psi_k`$ contains $`\mathrm{GL}_{k+1}(\mathbb F)`$, a dense open subset. For completeness, the root assertion follows blockwise: on an invertible Jordan block $`\alpha I+Q`$, choose $`a^k=\alpha`$ and use the truncated binomial polynomial $`a(I+\alpha^{-1}Q)^{1/k}`$. It is a finite polynomial because $`Q`$ is nilpotent.

Nonadditivity can also be witnessed explicitly. The matrices $`I`$ and $`C_k-I`$ belong to the image, whereas their sum $`C_k`$ does not by Theorem [1.1](#label-thm-main). Indeed, $`I=\Psi_k(I,0)`$; and since $`C_k^2=0`$, a scalar $`a`$ with $`a^k=-1`$ gives
```math
\bigl(a(I-k^{-1}C_k)\bigr)^k
 =-(I-C_k)=C_k-I.
```
$`\square`$

<!-- end proof-4 -->

The image statement is a consequence of the counterexample and the familiar existence of roots of invertible matrices; it is not a separate classification theorem. The theorem itself does not need algebraic closure or characteristic zero, while this explicit additive witness uses both the scalar root and $`k^{-1}`$.

The examples lie immediately above the proposed numerical boundary: $`n=k+1`$ and $`\dim\ker B_k=2`$. They show that this inequality alone cannot characterize surjectivity, even for idempotent coefficients. The mechanism constrains both summands. A nontrivial nilpotent chain on the kernel of the coefficient forces the first power to have rank one; the remaining two square-zero blocks then force the second power into the same rank-one regime, which is impossible. A construction of only the first power, satisfying the rows or columns prescribed by the kernel of the coefficient, would miss this second obstruction.

A complete criterion for surjectivity remains open beyond the cases in [\[1\]](#ref-SS). In particular, the present construction gives no classification for fixed small exponents, does not decide all five-dimensional cases, and does not determine the entire image for the coefficients $`B_k`$. It also does not address the classical multilinear Kaplansky–L’vov conjecture: the maps here involve powers and fixed matrix coefficients.

## References

<a id="ref-SS"></a>

**\[1\]** P. Saini and A. Singh, *Polynomial Maps with Constants on Matrix Algebra*, arXiv:2604.27592v1 (2026), especially Theorems 1.2 and 1.3, Proposition 4.2, and Question 6.1. <https://arxiv.org/abs/2604.27592>.

<a id="ref-GMV"></a>

**\[2\]** A. Gangwal, A. Mandal and S. Verma, *Polynomial Maps with Constants over Division Algebras and the Generalized Kaplansky–L’vov Conjecture*, arXiv:2607.27226v1 (2026), Question 1.1 and Theorem 1.4. <https://arxiv.org/abs/2607.27226>.
