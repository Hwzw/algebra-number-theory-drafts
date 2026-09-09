# Uniform dominance of short Gorenstein algebras

**Henry Zweiman**

September 9, 2026

## Abstract

Let $`R`$ be a commutative graded Artinian Gorenstein algebra over an arbitrary field, with Hilbert function $`(1,e,1)`$ and $`e\ge3`$. We prove that its dominant index is exactly one: the residue field belongs to level two from every nonzero object of the stable module category. The proof combines Ringel’s eventual bristle-generation theorem for Kronecker representations with an explicit identity between normalized syzygies and kernel reflections. Distant cosyzygies map onto every bristle, producing a single exact sequence between sums of shifts of the original module whose kernel has a simple summand after a shift. Every nonzero stable object consequently has generation time at most three. The common deformation of a short local ring and its associated graded ring also gives dominant index at most seven without a coefficient-field assumption. These results establish uniform dominance for this class; they do not decide whether every dominant local ring is uniformly dominant.

## 1. Introduction and statements

Let $`(R,\mathfrak m,k)`$ be an Artinian Gorenstein local ring. Its stable category $`\mathcal C=\underline{\mathrm{mod}}\,R`$ has finitely generated modules as objects and homomorphisms modulo those factoring through free modules as morphisms. It is triangulated, with suspension $`\Omega^{-1}`$, and agrees with the singularity category. For an object $`M`$, let $`\langle M\rangle_1`$ consist of finite direct sums and direct summands of shifts of $`M`$. Inductively, $`\langle M\rangle_{r+1}`$ is obtained by taking summands of extensions of objects in $`\langle M\rangle_r`$ by objects in $`\langle M\rangle_1`$.

Following Takahashi [\[5\]](#ref-T), the dominant index $`\operatorname{dx}(R)`$ is the least integer $`r`$ such that $`k\in\langle M\rangle_{r+1}`$ for every nonzero $`M\in\mathcal C`$. Finiteness of this invariant is *uniform dominance*. Dominance alone asks only that $`k`$ belong to the thick closure of each nonzero object, with no uniform bound on the number of extensions.

Kobayashi and Takahashi study uniform dominance for several classes of local rings and ask about dominance of non-complete-intersection short Gorenstein rings [\[2, Question 7.1\]](#ref-KT). Kimura proves dominance in the coefficient-field case through a classification of thick subcategories over weakly symmetric algebras [\[1, Theorem 7.3\]](#ref-K). That qualitative result is already known and is not claimed as new here. The present paper establishes a sharp uniform bound for the commutative short graded case.

<a id="theorem-1"></a>

**Theorem 1.1.**

<a id="label-thm-main"></a>

Let $`k`$ be any field and let $`R=R_0\oplus R_1\oplus R_2`$ be a commutative graded Artinian Gorenstein $`k`$-algebra, generated in degree one, with
```math
R_0=k,\qquad \dim_kR_1=e\ge3,\qquad \dim_kR_2=1.
```
Then $`\operatorname{dx}(R)=1`$. More precisely, for every nonzero $`M\in\underline{\mathrm{mod}}\,R`$,
```math
k\in\langle M\rangle_2,
 \qquad \underline{\mathrm{mod}}\,R=\langle M\rangle_4.
```
The first bound is sharp for every such algebra.

<!-- end theorem-1 -->

The essential existing input is Ringel’s theorem that sufficiently high kernel reflections of a matrix pencil have enough eigenvectors to span the source space [\[4, Section 5, Theorem 2\]](#ref-RP). This is the matrix formulation of his eventual bristle-generation theorem [\[3, Main Theorem 1.3\]](#ref-RB). We show that even normalized syzygies realize these reflections. We then use bristles only as intermediate factors of a map between shifts of the original module. They need not themselves have been constructed in its thick closure.

<a id="corollary-1"></a>

**Corollary 1.2.**

<a id="label-cor-arbitrary"></a>

Let $`(R,\mathfrak m,k)`$ be an Artinian Gorenstein local ring with $`\mathfrak m^3=0`$ and $`\operatorname{edim}R\ge3`$. If $`R`$ contains a field, then $`\operatorname{dx}(R)=1`$. In general, $`R`$ is uniformly dominant and $`\operatorname{dx}(R)\le7`$.

<!-- end corollary-1 -->

The second assertion uses the common-deformation construction in [\[6\]](#ref-Z); its role and proof are recalled in Section [5](#label-sec-transfer). Theorem [1.1](#label-thm-main) is independent of that construction. The global question whether a dominant local ring can fail to be uniformly dominant [\[5, Question 6.12\]](#ref-T) remains open beyond the classes treated here.

## 2. Two-layer modules and normalized syzygies

Throughout Sections 2–5 let $`R`$ satisfy Theorem [1.1](#label-thm-main). Choose $`z\ne0`$ in $`R_2`$ and a basis $`x_1,\ldots,x_e`$ of $`R_1`$. There is an invertible symmetric matrix $`Q=(Q_{ij})`$ with

<a id="label-eq-ring"></a>

```math
\tag{1}
 x_ix_j=Q_{ij}z,\qquad x_iz=z^2=0.
```

Indeed the multiplication pairing on $`R_1`$ is nondegenerate because the socle of $`R`$ is $`R_2`$. Symmetry follows from commutativity. No diagonalization of this pairing will be used.

<a id="lemma-1"></a>

**Lemma 2.1.**

<a id="label-lem-layers"></a>

Every finite $`R`$-module with no free summand is annihilated by $`\mathfrak m^2`$ and admits a grading concentrated in degrees zero and one. If it also has no simple summand, then its radical and socle coincide.

<!-- end lemma-1 -->

<a id="proof-1"></a>

**Proof.**

If $`zv\ne0`$, the map $`R\to M`$ sending $`r`$ to $`rv`$ is injective: every nonzero ideal contains the one-dimensional socle, whereas its kernel does not. Since $`R`$ is self-injective, this injection splits. This contradicts the absence of free summands. Thus $`\mathfrak m^2M=0`$. Choose a $`k`$-linear complement $`M_0`$ to $`M_1=\mathfrak mM`$. Multiplication by $`R_1`$ sends $`M_0`$ into $`M_1`$ and kills $`M_1`$, giving the grading.

Finally, any vector-space complement to $`\mathfrak mM`$ in $`\operatorname{Soc}M`$ splits off as a semisimple module: choose the complement to $`\mathfrak mM`$ in $`M`$ to contain it, and split the corresponding top vector subspace. Thus absence of simple summands implies $`\operatorname{Soc}M=\mathfrak mM`$. $`\square`$

<!-- end proof-1 -->

Call a nonzero module with no free summands *persistent* if none of its minimal syzygies or cosyzygies, indexed by all integers, has a simple summand. This terminology is used only within this paper. If $`M`$ is not persistent, then $`k\in\langle M\rangle_1`$, so such modules already satisfy the theorem.

A two-layer module is specified by vector spaces $`A=M_0`$, $`B=M_1`$ and arrows $`T_i:A\to B`$, giving an $`e`$-Kronecker representation. For a persistent module the arrows jointly span $`B`$ and their kernels have zero intersection. Normalize every syzygy to degrees zero and one, and denote the resulting operation by $`\overline\Omega`$.

<a id="lemma-2"></a>

**Lemma 2.2.**

<a id="label-lem-omega"></a>

Let $`M`$ be persistent, with $`\dim_kM_0=a`$ and $`\dim_kM_1=b`$. Put
```math
K=\ker\bigl([T_1\ \cdots\ T_e]:A^e\longrightarrow B\bigr).
```
Then $`\overline\Omega M`$ has degree-zero space $`K`$, degree-one space $`A`$, and arrows

<a id="label-eq-omegamaps"></a>

```math
\tag{2}
 U_i=\left.\sum_{j=1}^eQ_{ij}\pi_j\right|_K,
```

where $`\pi_j:A^e\to A`$ is the $`j`$th projection. In particular,

<a id="label-eq-recurrence"></a>

```math
\tag{3}
 \dim\overline\Omega M=(ea-b,a),\qquad
 \dim\overline\Omega^{-1}M=(b,eb-a).
```

Moreover, normalized syzygy is exact on any short exact sequence of persistent two-layer modules, and on all its iterates.

<!-- end lemma-2 -->

<a id="proof-2"></a>

**Proof.**

The natural minimal cover $`R\otimes_k A\to M`$ is an isomorphism in degree zero. Its kernel has degree-one part $`K`$ and degree-two part $`kz\otimes_kA\cong A`$. Multiplication in the cover gives [(2)](#label-eq-omegamaps). After shifting degrees, persistence and Lemma [2.1](#label-lem-layers) ensure that the degree-one component is the radical. This proves the first dimension formula. A graded injective envelope embeds $`M`$ into $`R(1)^b`$, since the socle of $`M`$ is $`B`$; the quotient, after normalization, has dimensions $`(b,eb-a)`$.

For exactness, take degree-zero components of a graded short exact sequence and tensor them over $`k`$ with $`R`$. These give an exact sequence of the natural covers. The snake lemma gives an exact sequence of their kernels. Normalize the degrees. Persistence supplies the same hypotheses at the next step, so the argument iterates. This is also the exactness construction appearing in [\[1, Lemma 3.11\]](#ref-K); the local argument given here requires no ambient proper thick subcategory. $`\square`$

<!-- end proof-2 -->

<a id="lemma-3"></a>

**Lemma 2.3.**

<a id="label-lem-growth"></a>

Put $`\lambda=(e+\sqrt{e^2-4})/2`$. For a persistent module $`M`$, write $`\dim\overline\Omega^{-n}M=(u_n,v_n)`$. Then
```math
u_n\longrightarrow\infty,\qquad v_n/u_n\longrightarrow\lambda>e-1.
```
Also $`\dim_k\overline\Omega^nM\to\infty`$ as $`n\to\infty`$.

<!-- end lemma-3 -->

<a id="proof-3"></a>

**Proof.**

The matrix for cosyzygy in [(3)](#label-eq-recurrence) has eigenvectors $`(1,\lambda)`$ and $`(1,\lambda^{-1})`$, with eigenvalues $`\lambda`$ and $`\lambda^{-1}`$ respectively. Write the initial vector as their linear combination. Since the dimension vector remains strictly positive for all positive and negative iterates, both coefficients are nonnegative. Neither coefficient can be zero, because $`u_0,v_0`$ are positive integers and the slopes are irrational. Irrationality follows from $`(e-1)^2<e^2-4<e^2`$ for $`e\ge3`$. Both coefficients are therefore positive. The conclusions follow by taking positive and negative iterates. Finally, $`\lambda+\lambda^{-1}=e`$ and $`\lambda>1`$, so $`\lambda>e-1`$. $`\square`$

<!-- end proof-3 -->

## 3. Kernel reflections and bristles

For a pencil $`P=(A,B;T_1,\ldots,T_e)`$, let $`\sigma P`$ have source $`K=\ker[T_1\ \cdots\ T_e]`$, target $`A`$, and arrows $`\pi_j|_K`$. This is precisely the kernel reflection used in [\[4, Section 5\]](#ref-RP). For $`g\in\mathrm{GL}_e(k)`$ let $`\mathcal T_g`$ replace the column of arrows by $`g`$ times that column.

<a id="lemma-4"></a>

**Lemma 3.1.**

<a id="label-lem-reflection"></a>

On persistent modules there are natural identifications

<a id="label-eq-reflection"></a>

```math
\tag{4}
 \overline\Omega=\mathcal T_Q\sigma,
 \qquad \overline\Omega^2\cong\sigma^2.
```

Consequently $`\overline\Omega^{2t}M\cong\sigma^{2t}M`$ for every nonnegative integer $`t`$.

<!-- end lemma-4 -->

<a id="proof-4"></a>

**Proof.**

The first identity is [(2)](#label-eq-omegamaps). The row map of the changed pencil $`\mathcal T_gP`$ is $`[T_1\ \cdots\ T_e](g^{\mathsf T}\otimes1_A)`$. Its kernel is $`(g^{-\mathsf T}\otimes1_A)K`$. Under this identification, its projection arrows are $`g^{-\mathsf T}`$ times the old projections. Hence
```math
\sigma\mathcal T_g\cong\mathcal T_{g^{-\mathsf T}}\sigma.
```
It follows that $`\overline\Omega^2\cong\mathcal T_{Q Q^{-\mathsf T}}\sigma^2=\sigma^2`$, since $`Q`$ is symmetric. These are identifications of the arrow maps, not just the dimensions. Iteration is legitimate by persistence. $`\square`$

<!-- end proof-4 -->

A *bristle* is the pencil $`B(c)=(k,k;c_1,\ldots,c_e)`$, where $`c\ne0`$. It is also a cyclic $`R`$-module of length two. We use the following consequence of Ringel’s theorem.

<a id="theorem-2"></a>

**Theorem 3.2 (Ringel).**

<a id="label-thm-ringel"></a>

For $`e\ge3`$ and any pencil $`P`$, the source of $`\sigma^tP`$ is spanned by vectors whose arrow images span a one-dimensional space, for all sufficiently large $`t`$.

<!-- end theorem-2 -->

This is [\[4, Section 5, Theorem 2\]](#ref-RP), deduced there from [\[3\]](#ref-RB). It applies over an arbitrary field. In particular, if $`\sigma^tP`$ is generated by its source space, a basis chosen from these vectors gives a surjection from a direct sum of bristles onto $`\sigma^tP`$.

<a id="lemma-5"></a>

**Lemma 3.3.**

<a id="label-lem-bristlequotient"></a>

For every persistent $`M`$, there is an integer $`n_0`$ such that $`\overline\Omega^{-n}M`$ maps onto every bristle whenever $`n\ge n_0`$.

<!-- end lemma-5 -->

<a id="proof-5"></a>

**Proof.**

Let $`Y=(U,W;T_i)`$ be generated in degree zero, with dimensions $`(u,v)`$. A map $`Y\to B(c)`$ is a pair of functionals $`f_0:U\to k`$ and $`f_1:W\to k`$ satisfying
```math
f_1T_i=c_i f_0\qquad(1\le i\le e).
```
These are at most $`eu`$ linear equations on $`u+v`$ unknowns. Thus the space of maps has dimension at least $`v-(e-1)u`$. If a map is nonzero, then $`f_0\ne0`$, since $`W=\sum_iT_i(U)`$. Its top map is consequently surjective, and the images of the arrows then give surjectivity on the target degree as well. Lemma [2.3](#label-lem-growth) makes the displayed lower bound positive for $`Y=\overline\Omega^{-n}M`$ and all sufficiently large $`n`$, independently of $`c`$. $`\square`$

<!-- end proof-5 -->

## 4. The uniform bound and its sharpness

<a id="proof-6"></a>

**Proof of Theorem [1.1](#label-thm-main).**

Remove free summands from a representative of $`M`$. If it is not persistent, then $`k\in\langle M\rangle_1`$. Otherwise choose $`t`$ large enough that Theorem [3.2](#label-thm-ringel) applies to the even reflection $`\sigma^{2t}M`$. By Lemma [3.1](#label-lem-reflection), the normalized module
```math
X=\overline\Omega^{2t}M
```
is generated by bristles. Put $`h=\dim_kX_0`$. A basis of eigenvectors in $`X_0`$ gives a fixed epimorphism

<a id="label-eq-bristlepresentation"></a>

```math
\tag{5}
 B_1\oplus\cdots\oplus B_h\longrightarrow X.
```

For every sufficiently large $`n`$, Lemma [3.3](#label-lem-bristlequotient) supplies epimorphisms $`Y_n=\overline\Omega^{-n}M\to B_j`$ for all $`j`$. Compose their direct sum with [(5)](#label-eq-bristlepresentation) to obtain

<a id="label-eq-cone"></a>

```math
\tag{6}
 0\longrightarrow K_n\longrightarrow Y_n^{\oplus h}\longrightarrow X\longrightarrow0.
```

Both the middle and right modules belong to $`\langle M\rangle_1`$, so $`K_n\in\langle M\rangle_2`$. Choose $`n`$ still larger, if necessary, so that

<a id="label-eq-dimensioncontradiction"></a>

```math
\tag{7}
 \dim_k\overline\Omega^nX>h\dim_kM.
```

Here $`h`$ and $`X`$ have already been fixed, and Lemma [2.3](#label-lem-growth) guarantees such $`n`$.

The kernel has no free summand, since it is annihilated by $`\mathfrak m^2`$. If it were persistent, applying normalized syzygy $`n`$ times to [(6)](#label-eq-cone), using Lemma [2.2](#label-lem-omega), would give an epimorphism
```math
M^{\oplus h}\longrightarrow\overline\Omega^nX.
```
This contradicts [(7)](#label-eq-dimensioncontradiction). A zero kernel gives the same contradiction. Thus some stable shift of $`K_n`$ has $`k`$ as a summand. Consequently $`k\in\langle M\rangle_2`$.

To prove sharpness, take a bristle $`B(c)`$ as an $`R`$-module. It is indecomposable and nonprojective. Minimal stable syzygies and cosyzygies preserve nonprojective indecomposability, since $`R`$ is self-injective and its stable category is Krull–Schmidt. The two dimension transformations in [(3)](#label-eq-recurrence) preserve
```math
q(a,b)=a^2+b^2-eab.
```
Starting from $`(1,1)`$ gives $`q=2-e<0`$. Suppose a simple module first occurs in either direction. Up to that step the preceding modules are nonsimple indecomposables, so the minimal-cover or injective-envelope calculation in Lemma [2.2](#label-lem-omega) gives the same dimension transformation at that step. A one-dimensional graded module has vector $`(1,0)`$ or $`(0,1)`$ and hence $`q=1`$, a contradiction. Thus every shift of $`B(c)`$ is nonsimple. Krull–Schmidt and cancellation of free summands imply that $`k`$ is not a summand of a finite sum of those shifts. Hence $`k\notin\langle B(c)\rangle_1`$, proving $`\operatorname{dx}(R)=1`$.

Finally Lemma [2.1](#label-lem-layers) shows that every nonfree module is an extension of two semisimple modules. Therefore $`\mathcal C=\langle k\rangle_2`$. The usual composition rule for levels gives $`\mathcal C=\langle M\rangle_4`$ for every nonzero $`M`$. $`\square`$

<!-- end proof-6 -->

<a id="remark-1"></a>

**Remark 4.1.**

The proof does not bound the shift $`t`$ in Ringel’s theorem or the number $`h`$ of bristle generators. Such bounds are unnecessary: shifts and finite sums are level-one operations. The crucial order is to fix $`X`$ and $`h`$ first, and only then choose $`n`$ in [(7)](#label-eq-dimensioncontradiction). Allowing $`h`$ to grow with $`n`$ would not give the stated contradiction.

<!-- end remark-1 -->

## 5. Consequences, transfer, and an example

<a id="label-sec-transfer"></a>

The generation time of an object is the least $`r`$ for which the whole category is its level $`r+1`$. Thus Theorem [1.1](#label-thm-main) gives an upper bound of three for the generation time of every nonzero object, and in particular for the ultimate dimension of $`\mathcal C`$. This does not assert that every integer up to three occurs in its Orlov spectrum.

For completeness, we recall the specific deformation input used to remove the coefficient-field assumption. The construction below is the short Gorenstein case of [\[6, Theorems 1.1 and 1.2\]](#ref-Z).

<a id="proposition-1"></a>

**Proposition 5.1.**

<a id="label-prop-transfer"></a>

If $`(R,\mathfrak m,k)`$ is an Artinian Gorenstein local ring with $`\mathfrak m^3=0`$ and $`e=\operatorname{edim}R\ge3`$, and $`G=\operatorname{gr}_{\mathfrak m}R`$, then
```math
\operatorname{dx}(R)\le4\operatorname{dx}(G)+3.
```

<!-- end proposition-1 -->

<a id="proof-7"></a>

**Proof.**

The socle is $`\mathfrak m^2\cong k`$, and the multiplication pairing on $`\mathfrak m/\mathfrak m^2`$ is nondegenerate. If $`R`$ has a coefficient field, a complement to $`\mathfrak m^2`$ in $`\mathfrak m`$ identifies $`R`$ with $`G`$.

Otherwise its residue characteristic $`p`$ is nonzero in $`R`$. Choose a complete Cohen discrete valuation ring $`V`$, with uniformizer $`p`$ and residue field $`k`$, mapping to $`R`$. Such a map need not be injective. Choose lifts $`x_i`$ of a basis of $`\mathfrak m/\mathfrak m^2`$ and a socle generator $`z`$. Lift their symmetric multiplication coefficients arbitrarily to $`V`$, and define
```math
T=V\,1\oplus\bigoplus_{i=1}^eV X_i\oplus V Z,
 \quad X_iX_j=\widetilde Q_{ij}Z,\quad X_iZ=Z^2=0.
```
This associative commutative ring is finite free over $`V`$, complete local of dimension one, and Cohen–Macaulay. The assignment $`X_i\mapsto x_i`$, $`Z\mapsto z`$ is a surjection $`T\to R`$, as can be checked on the three layers of the maximal-ideal filtration.

If $`p\notin\mathfrak m^2`$, choose $`x_1=p`$ and set $`a=X_1`$. If $`0\ne p\in\mathfrak m^2`$, choose $`z=p`$ and set $`a=Z`$. Then $`a^3=0`$ and $`p-a`$ lies in the kernel. Multiplication by $`p-a`$ on the free $`V`$-module $`T`$ has determinant $`p^{e+2}`$, so it is injective and its cokernel has $`V`$-length $`e+2`$. The surjection $`T/(p-a)\to R`$ is therefore an isomorphism, since $`R`$ has the same length. Also $`T/pT\cong G`$.

If $`\mathfrak n`$ is the maximal ideal of $`T`$, the augmentation $`T\to V`$ sends $`\mathfrak n^2`$ into $`p^2V`$, whereas it sends $`p`$ and $`p-a`$ to $`p`$. Thus both regular elements belong to $`\mathfrak n\setminus\mathfrak n^2`$. Takahashi’s regular-element inequalities [\[5, Theorem 6.2\]](#ref-T) give
```math
\operatorname{dx}(T)\le2\operatorname{dx}(G)+1,
 \qquad \operatorname{dx}(R)\le2\operatorname{dx}(T)+1.
```
Combining them proves the result. $`\square`$

<!-- end proof-7 -->

<a id="proof-8"></a>

**Proof of Corollary [1.2](#label-cor-arbitrary).**

The associated graded ring satisfies Theorem [1.1](#label-thm-main). If $`R`$ contains a field, its completeness supplies a coefficient field and $`R\cong G`$. Otherwise apply Proposition [5.1](#label-prop-transfer) and $`\operatorname{dx}(G)=1`$. $`\square`$

<!-- end proof-8 -->

Here is an explicit instance of [(6)](#label-eq-cone). Over $`k=\mathbb F_2`$, take $`e=3`$, $`Q=I_3`$, and $`M=B(1,0,0)`$. Then
```math
\dim X=\dim\overline\Omega^2M=(5,2),\qquad
 \dim Y=\dim\overline\Omega^{-2}M=(2,5).
```
The accompanying exact computation selects five bristle generators of $`X`$, factors each through $`Y`$, and obtains an epimorphism $`Y^5\to X`$. Its kernel has graded dimensions $`(5,23)`$ and radical dimension $`15`$. A complement to its radical in the degree-one space therefore gives eight simple direct summands. This is a concrete one-cone witness for $`k\in\langle M\rangle_2`$.

The file `check.py` also verifies the reflection identity on 288 finite-field matrix examples and on 24 additional alternating pairings in characteristic two. These computations check the matrix identifications and the displayed example; the general theorem rests on the proof and Ringel’s cited result, not on finite verification.

## 6. Further questions

The exact Orlov spectrum of the stable category in Theorem [1.1](#label-thm-main) is not determined here. The bound seven in Proposition [5.1](#label-prop-transfer) is likewise not asserted to be sharp. A direct mixed-characteristic construction could improve it. More generally, the one-cone argument suggests looking for generation theorems by uniformly small intermediate modules over other algebras. Such a theorem would have to be established for the relevant module category; the present Kronecker result cannot simply be assumed outside the short case.

## References

<a id="ref-K"></a>

**\[1\]** K. Kimura, *Thick subcategories over weakly symmetric algebras with radical cube zero*, preprint, 2026, [arXiv:2609.05781v1](https://arxiv.org/abs/2609.05781v1).

<a id="ref-KT"></a>

**\[2\]** T. Kobayashi and R. Takahashi, *On the ubiquity of uniformly dominant local rings*, preprint, 2026, [arXiv:2603.10810v1](https://arxiv.org/abs/2603.10810v1).

<a id="ref-RB"></a>

**\[3\]** C. M. Ringel, *Kronecker modules generated by modules of length 2*, Representations of Algebras, Contemporary Mathematics **705** (2018), 189–214; [arXiv:1612.07679](https://arxiv.org/abs/1612.07679); [doi:10.1090/conm/705/14194](https://doi.org/10.1090/conm/705/14194).

<a id="ref-RP"></a>

**\[4\]** C. M. Ringel, *The eigenvector variety of a matrix pencil*, 2017, [arXiv:1703.04097v2](https://arxiv.org/abs/1703.04097v2), especially Section 5, Theorem 2.

<a id="ref-T"></a>

**\[5\]** R. Takahashi, *Uniformly dominant local rings and Orlov spectra of singularity categories*, [arXiv:2412.00669](https://arxiv.org/abs/2412.00669); author version [udim8.pdf](https://www.math.nagoya-u.ac.jp/~takahashi/udim8.pdf), Theorem 6.2 and Question 6.12.

<a id="ref-Z"></a>

**\[6\]** H. Zweiman, *Dominance and common deformations of short local rings*, 2026, [public manuscript P36](https://github.com/Hwzw/algebra-number-theory-drafts/tree/96274cfe30f7844b4dfd4917cb6b8dd1106bb954/papers/P36-short-ring-dominance), Theorems 1.1 and 1.2.
