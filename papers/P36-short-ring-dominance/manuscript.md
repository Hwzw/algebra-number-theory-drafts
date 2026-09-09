# Dominance and common deformations of short local rings

**Henry Zweiman**

September 9, 2026

## Abstract

Let $`(R,\mathfrak m,k)`$ be a commutative Artinian local ring with $`\mathfrak m^3=0`$. We construct a one-dimensional complete Cohen–Macaulay local ring whose quotients by two regular elements outside the square of its maximal ideal are $`R`$ and $`\operatorname{gr}_{\mathfrak m}R`$. Consequently, dominance and uniform dominance are each equivalent for $`R`$ and its associated graded ring. Their dominant indices differ by at most the bounds $`\operatorname{dx}(R)\le4\operatorname{dx}(\operatorname{gr}_{\mathfrak m}R)+3`$ and the reverse inequality when finite. Combining this construction with Kimura’s equicharacteristic dominance theorem and known deformation and flat-descent results, we prove that every non-complete-intersection Gorenstein local ring satisfying either $`\mathfrak m^3=0`$ or $`e(R)\le\operatorname{codim}R+2`$ is dominant. This answers both clauses of Kobayashi–Takahashi Question 7.1 without restrictions on characteristic or residue-field cardinality.

## 1. Introduction

All rings in this paper are commutative, Noetherian, and have identity. A local ring $`(R,\mathfrak m,k)`$ is *dominant* if
```math
k\in\operatorname{thick}_{\mathsf D_{\mathrm{sg}}(R)}(X)\qquad\text{for every nonzero }X\in\mathsf D_{\mathrm{sg}}(R).
```
Here $`\mathsf D_{\mathrm{sg}}(R)`$ is the quotient of the bounded derived category of finitely generated modules by the perfect complexes. A thick subcategory is closed under shifts, cones, and direct summands. Dominance was introduced by Takahashi in connection with subcategory classification [\[6\]](#ref-T). For an Artinian ring, $`k`$ generates $`\mathsf D_{\mathrm{sg}}(R)`$, so dominance says that this category has no nonzero proper thick subcategory.

Short local rings, here meaning those with $`\mathfrak m^3=0`$, have long provided examples and tests for homological conjectures; see Avramov–Iyengar–Şega [\[1\]](#ref-AIS). In the Gorenstein case, Kobayashi and Takahashi ask whether every non-complete-intersection ring with $`\mathfrak m^3=0`$, or more generally with $`e(R)\le\operatorname{codim}R+2`$, is dominant [\[3, Question 7.1\]](#ref-KT). The multiplicity is Hilbert–Samuel multiplicity, and $`\operatorname{codim}R=\operatorname{edim}R-\dim R`$.

Kimura recently proved the short case when $`R`$ contains a field, and the higher-dimensional case in equal characteristic with infinite residue field [\[2, Theorem 7.3\]](#ref-K). His theorem supplies the essential representation-theoretic input here. In particular, the first non-complete-intersection Gorenstein dominant examples already belong to that work. Our contribution is a common deformation that transfers dominance from the associated graded ring to an arbitrary short local ring, including rings without a coefficient field. The construction does not require the Gorenstein hypothesis.

<a id="theorem-1"></a>

**Theorem 1.1.**

<a id="label-thm-deform"></a>

Let $`(R,\mathfrak m,k)`$ be an Artinian local ring with $`\mathfrak m^3=0`$, and put $`G=\operatorname{gr}_{\mathfrak m}R`$. There exist a one-dimensional complete Cohen–Macaulay local ring $`(T,\mathfrak n,k)`$ and $`T`$-regular elements $`u,v\in\mathfrak n\setminus\mathfrak n^2`$ such that

<a id="label-eq-quotients"></a>

```math
\tag{1}
 T/(u)\cong G,\qquad T/(v)\cong R.
```

If $`R`$ has residue characteristic $`p>0`$ and $`p\ne0`$ in $`R`$, one can take $`T`$ finite free of rank $`\ell_R(R)`$ over a complete Cohen discrete valuation ring $`V`$ with uniformizer $`p`$, with $`u=p`$ and $`v=p-a`$ for an element $`a`$ satisfying $`a^3=0`$.

<!-- end theorem-1 -->

The elements $`u`$ and $`v`$ need not be distinct. The condition that both lie outside $`\mathfrak n^2`$ is essential for the categorical application: dominance need not descend through a regular element in $`\mathfrak n^2`$; see [\[6, Corollary 6.12\]](#ref-T).

<a id="theorem-2"></a>

**Theorem 1.2.**

<a id="label-thm-transfer"></a>

With $`R`$ and $`G`$ as above, $`R`$ is dominant if and only if $`G`$ is dominant. Also, $`R`$ is uniformly dominant if and only if $`G`$ is uniformly dominant. If their dominant indices are finite, then

<a id="label-eq-indices"></a>

```math
\tag{2}
 \operatorname{dx}(R)\le4\operatorname{dx}(G)+3,\qquad \operatorname{dx}(G)\le4\operatorname{dx}(R)+3.
```

<!-- end theorem-2 -->

<a id="theorem-3"></a>

**Theorem 1.3.**

<a id="label-thm-gorenstein"></a>

Let $`(R,\mathfrak m,k)`$ be a Gorenstein local ring that is not a complete intersection. If either $`\mathfrak m^3=0`$ or $`e(R)\le\operatorname{codim}R+2`$, then $`R`$ is dominant.

<!-- end theorem-3 -->

Thus Theorem [1.3](#label-thm-gorenstein) answers Question 7.1 of [\[3\]](#ref-KT). The removal of the characteristic restriction uses Theorem [1.1](#label-thm-deform); the removal of the finite-residue-field obstruction in positive dimension uses Liu’s flat descent [\[4\]](#ref-L). We make no assertion that the rings in Theorem [1.3](#label-thm-gorenstein) are uniformly dominant. Theorem [1.2](#label-thm-transfer) transfers that stronger question to their graded Artinian counterparts without answering it.

## 2. The common deformation

Write
```math
e=\dim_k(\mathfrak m/\mathfrak m^2),\qquad f=\dim_k\mathfrak m^2,\qquad N=1+e+f=\ell_R(R).
```
Since $`\mathfrak m^3=0`$, multiplication gives a well-defined symmetric bilinear map

<a id="label-eq-tensor"></a>

```math
\tag{3}
 b:(\mathfrak m/\mathfrak m^2)\times(\mathfrak m/\mathfrak m^2)\longrightarrow\mathfrak m^2.
```

Its values span $`\mathfrak m^2`$. The graded ring $`G`$ is precisely the vector space $`k\oplus k^e\oplus k^f`$ with multiplication given by $`b`$ in positive degree and all products of total degree at least three zero.

<a id="lemma-1"></a>

**Lemma 2.1.**

<a id="label-lem-field"></a>

If $`R`$ contains a field, then $`R\cong G`$ as local rings.

<!-- end lemma-1 -->

<a id="proof-1"></a>

**Proof.**

The Artinian ring $`R`$ is complete, so the equicharacteristic Cohen structure theorem gives a coefficient field identified with $`k`$; see [\[5, Tag 032A\]](#ref-Stacks). Choose a $`k`$-linear complement $`E`$ of $`\mathfrak m^2`$ in $`\mathfrak m`$. The decomposition $`R=k\oplus E\oplus\mathfrak m^2`$ has exactly the multiplication described in [(3)](#label-eq-tensor), because $`E\mathfrak m^2=(\mathfrak m^2)^2=0`$. Identifying $`E`$ with $`\mathfrak m/\mathfrak m^2`$ gives the desired isomorphism. $`\square`$

<!-- end proof-1 -->

We now treat rings that do not contain a field. Their residue field has characteristic $`p>0`$, with $`p\ne0`$ in $`R`$. By the Cohen structure theorem there is a complete discrete valuation ring $`V`$ of characteristic zero, with maximal ideal $`pV`$ and residue field $`k`$, and a local homomorphism

<a id="label-eq-cohen"></a>

```math
\tag{4}
 V\longrightarrow R
```

inducing the chosen residue-field isomorphism [\[5, Tag 032A and its proof\]](#ref-Stacks). This statement holds for imperfect $`k`$ as well. The map [(4)](#label-eq-cohen) is not asserted to be injective. All uses of scalars from $`V`$ in $`R`$ are through this map.

Choose elements $`x_1,\ldots,x_e\in\mathfrak m`$ whose classes are a basis of $`\mathfrak m/\mathfrak m^2`$, and a $`k`$-basis $`z_1,\ldots,z_f`$ of $`\mathfrak m^2`$. Define $`b_{ij}^t\in k`$ by
```math
x_ix_j=\sum_{t=1}^f b_{ij}^t z_t.
```
This equality uses the canonical $`k`$-module structure on $`\mathfrak m^2`$, annihilated by $`\mathfrak m`$. Choose symmetric lifts $`B_{ij}^t=B_{ji}^t\in V`$ of these coefficients. Empty lists and empty sums are allowed when $`f=0`$.

Define a free $`V`$-module

<a id="label-eq-algebra"></a>

```math
\tag{5}
 T=V\cdot1\ \oplus\ \bigoplus_{i=1}^e VX_i\ \oplus\ \bigoplus_{t=1}^f VZ_t
```

with a $`V`$-bilinear multiplication, unit $`1`$, and rules

<a id="label-eq-rules"></a>

```math
\tag{6}
 X_iX_j=\sum_{t=1}^f B_{ij}^t Z_t,\qquad X_iZ_t=0,\qquad Z_sZ_t=0.
```

These rules define an associative commutative algebra: on triples of nonunit basis elements, both associated products are zero; triples containing $`1`$ satisfy associativity automatically. Put
```math
J=\bigoplus_i VX_i\oplus\bigoplus_t VZ_t.
```
Then $`J`$ is an ideal with $`J^3=0`$ and $`T/J=V`$. Therefore $`T`$ is local, with maximal ideal $`\mathfrak n=pT+J`$, and has dimension one. It is Noetherian and complete: it is finite free over $`V`$, and the $`p`$-adic and $`\mathfrak n`$-adic topologies agree since $`p^rT\subseteq\mathfrak n^r`$ and $`\mathfrak n^{r+2}\subseteq p^rT`$. Multiplication by $`p`$ is injective, so $`T`$ is Cohen–Macaulay. Reducing [(6)](#label-eq-rules) modulo $`p`$ gives

<a id="label-eq-fiber"></a>

```math
\tag{7}
 T/pT\cong G.
```

The coefficient map and the assignments $`X_i\mapsto x_i`$, $`Z_t\mapsto z_t`$ define a ring homomorphism $`\varphi:T\to R`$. Indeed, the differences between the lifted coefficients and their residues annihilate $`\mathfrak m^2`$, and all products involving $`\mathfrak m^2\mathfrak m`$ vanish. It is surjective: first represent an element of $`R`$ modulo $`\mathfrak m`$ by an element of $`V`$, then represent the remaining class modulo $`\mathfrak m^2`$ by a $`V`$-linear combination of the $`x_i`$, and finally represent the remainder by the $`z_t`$.

Adapt the bases to the nonzero element $`p\in R`$. If $`p\notin\mathfrak m^2`$, choose $`x_1=p`$ and set $`a=X_1`$. If $`p\in\mathfrak m^2`$, choose $`z_1=p`$ and set $`a=Z_1`$. In both cases $`a^3=0`$ and $`\varphi(p-a)=0`$.

<a id="lemma-2"></a>

**Lemma 2.2.**

<a id="label-lem-length"></a>

The element $`p-a`$ is $`T`$-regular, the map $`\varphi`$ induces an isomorphism $`T/(p-a)\cong R`$, and both $`p`$ and $`p-a`$ belong to $`\mathfrak n\setminus\mathfrak n^2`$.

<!-- end lemma-2 -->

<a id="proof-2"></a>

**Proof.**

Let $`K`$ be the fraction field of $`V`$. In $`T\otimes_V K`$, the element $`p-a`$ is invertible, with inverse
```math
p^{-1}\bigl(1+p^{-1}a+p^{-2}a^2\bigr).
```
Since $`T`$ is $`V`$-free, it embeds in this algebra, proving that $`p-a`$ is regular.

In the ordered basis $`(1,X_1,\ldots,X_e,Z_1,\ldots,Z_f)`$, multiplication by $`a`$ is strictly triangular. Thus multiplication by $`p-a`$ has determinant $`p^N`$. The length formula for the cokernel of a square matrix of nonzero determinant over a discrete valuation ring gives
```math
\ell_V\bigl(T/(p-a)\bigr)=v_p(p^N)=N.
```
The $`R`$-composition factors of $`R`$ are all $`k`$, which also has $`V`$-length one. Hence $`\ell_V(R)=N`$. The surjection $`T/(p-a)\to R`$ is an isomorphism by additivity of length.

Finally, the projection $`\pi:T\to V`$ with kernel $`J`$ satisfies $`\pi(\mathfrak n^2)=p^2V`$. Both $`p`$ and $`p-a`$ project to $`p\notin p^2V`$, so neither lies in $`\mathfrak n^2`$. $`\square`$

<!-- end proof-2 -->

<a id="proof-3"></a>

**Proof of Theorem [1.1](#label-thm-deform).**

When $`R`$ does not contain a field, the algebra [(5)](#label-eq-algebra) and Lemma [2.2](#label-lem-length) give the result with $`u=p`$ and $`v=p-a`$. In the remaining case, Lemma [2.1](#label-lem-field) allows $`T=R[[t]]`$ and $`u=v=t`$. This ring is complete of dimension one, $`t`$ is regular and outside its maximal-ideal square, and an Artinian ring is Cohen–Macaulay. $`\square`$

<!-- end proof-3 -->

## 3. Transfer of categorical generation

We recall the exact deformation properties needed. If $`(A,\mathfrak a,k)`$ is local and $`x\in\mathfrak a`$ is $`A`$-regular, then

<a id="label-eq-known"></a>

```math
\tag{8}
 A/(x)\text{ dominant}\ \Longrightarrow\ A\text{ dominant}.
```

The converse holds when $`x\notin\mathfrak a^2`$ [\[6, Theorem 5.6\]](#ref-T).

For quantitative generation, let $`\langle X\rangle_j`$ be the subcategory obtained from shifts, finite direct sums, and direct summands of $`X`$ using at most $`j-1`$ successive extensions, with $`\langle X\rangle_0=\{0\}`$. Takahashi’s dominant index is
```math
\operatorname{dx}(A)=\inf\{r\in\mathbb Z_{\ge-1}:k\in\langle X\rangle_{r+1}
       \text{ for every }0\ne X\in\mathsf D_{\mathrm{sg}}(A)\}.
```
A ring is *uniformly dominant* when this index is finite. A regular ring has index $`-1`$. For a regular element $`x`$, the known bounds are

<a id="label-eq-knownindices"></a>

```math
\tag{9}
 \operatorname{dx}(A)\le2\operatorname{dx}(A/(x))+1,
 \qquad
 \operatorname{dx}(A/(x))\le2\operatorname{dx}(A)+1\quad\text{if }x\notin\mathfrak a^2;
```

see [\[7, Theorem 6.2\]](#ref-U).

<a id="proof-4"></a>

**Proof of Theorem [1.2](#label-thm-transfer).**

Choose $`T,u,v`$ from Theorem [1.1](#label-thm-deform). Apply [(8)](#label-eq-known) and its converse to each of $`u,v`$. This gives
```math
G\text{ dominant}\ \Longleftrightarrow\ T\text{ dominant}
 \ \Longleftrightarrow\ R\text{ dominant}.
```
Applying [(9)](#label-eq-knownindices) twice gives
```math
\operatorname{dx}(R)\le2\operatorname{dx}(T)+1\le4\operatorname{dx}(G)+3.
```
Interchanging $`u`$ and $`v`$ gives the other inequality and the equivalence of finiteness. No uniform bound is inferred from dominance alone. $`\square`$

<!-- end proof-4 -->

## 4. Gorenstein rings of almost minimal multiplicity

We first verify the hypotheses needed to apply Kimura’s theorem to $`G`$.

<a id="lemma-3"></a>

**Lemma 4.1.**

<a id="label-lem-gorenstein"></a>

Let $`(R,\mathfrak m,k)`$ be Gorenstein, with $`\mathfrak m^3=0`$, and suppose $`R`$ is not a complete intersection. Then $`G=\operatorname{gr}_{\mathfrak m}R`$ is a Gorenstein local $`k`$-algebra, is not a complete intersection, and has embedding dimension at least three.

<!-- end lemma-3 -->

<a id="proof-5"></a>

**Proof.**

By [\[3, Lemma 7.2(1)\]](#ref-KT), $`e=\operatorname{edim}R\ge3`$ and $`\operatorname{Soc}R=\mathfrak m^2\cong k`$. Choose a generator $`z`$ of $`\mathfrak m^2`$. The multiplication pairing on $`\mathfrak m/\mathfrak m^2`$ with values in $`kz`$ is nonsingular. Indeed, a vector in its radical lifts to an element of $`\mathfrak m`$ annihilating $`\mathfrak m`$, which lies in $`\operatorname{Soc}R=\mathfrak m^2`$ and hence has zero degree-one class. Thus $`G`$ has socle $`kz`$, and is Gorenstein with Hilbert function $`(1,e,1)`$.

Write $`G=k[[Y_1,\ldots,Y_e]]/I`$ in its graded presentation. The space of quadratic relations has dimension $`\binom{e+1}{2}-1`$. As $`I`$ contains no linear form, these relations give linearly independent classes in $`I/(Y_1,\ldots,Y_e)I`$. Therefore
```math
\mu(I)\ge\binom{e+1}{2}-1>e\qquad(e\ge3).
```
An Artinian complete intersection in this regular local ring has a defining ideal minimally generated by $`e`$ elements. Hence $`G`$ is not a complete intersection. $`\square`$

<!-- end proof-5 -->

<a id="proof-6"></a>

**Proof of Theorem [1.3](#label-thm-gorenstein).**

If $`\mathfrak m^3=0`$, Lemma [4.1](#label-lem-gorenstein) makes $`G`$ a non-complete-intersection Gorenstein local ring containing a field. Kimura’s theorem [\[2, Theorem 7.3(1)\]](#ref-K) says that $`G`$ is dominant. Theorem [1.2](#label-thm-transfer) now implies that $`R`$ is dominant.

Suppose $`e(R)\le\operatorname{codim}R+2`$ and the residue field is infinite. Set $`d=\dim R`$. Choose $`x_1,\ldots,x_d\in\mathfrak m`$ whose initial linear forms give a homogeneous system of parameters for $`\operatorname{gr}_{\mathfrak m}R`$. This is possible over an infinite field. Their ideal $`Q`$ is a minimal reduction of $`\mathfrak m`$, and their classes in $`\mathfrak m/\mathfrak m^2`$ are linearly independent. Since $`R`$ is Cohen–Macaulay, this is a regular parameter sequence. The Artinian quotient $`A=R/Q`$ therefore satisfies
```math
\ell_A(A)=e(R),\qquad \operatorname{edim}A=\operatorname{edim}R-d=\operatorname{codim}R.
```
These are the usual minimal-reduction equalities, also used in [\[2, proof of Theorem 7.3(2)\]](#ref-K). The ring $`A`$ is Gorenstein and not a complete intersection: each of these properties is equivalent across quotient by a regular sequence. If $`\mathfrak a`$ is its maximal ideal, then
```math
\ell_A(\mathfrak a^2)=\ell_A(A)-1-\operatorname{edim}A\le1.
```
Thus $`\mathfrak a^2`$ is zero or a simple $`A`$-module, and $`\mathfrak a^3=0`$. The Artinian case proves that $`A`$ is dominant. Applying [(8)](#label-eq-known) successively to the parameter sequence proves dominance of $`R`$.

For a finite residue field, put $`S=R[t]_{\mathfrak mR[t]}`$. The map $`R\to S`$ is faithfully flat and local, its maximal ideal is $`\mathfrak mS`$, and its residue field is the infinite field $`k(t)`$. Flatness gives
```math
(\mathfrak mS)^j/(\mathfrak mS)^{j+1}\cong(\mathfrak m^j/\mathfrak m^{j+1})\otimes_k k(t)
 \qquad(j\ge0).
```
Consequently the Hilbert functions, embedding dimensions, dimensions, and multiplicities agree. The closed fiber is a field, so $`S`$ is Gorenstein, and $`S`$ is a complete intersection if and only if $`R`$ is; see [\[5, Tags 0BJL and 09Q7\]](#ref-Stacks). The infinite-field case applies to $`S`$. Liu’s flat-descent theorem [\[4, Theorem 3.8\]](#ref-L) then gives dominance of $`R`$. $`\square`$

<!-- end proof-6 -->

## 5. Examples, verification, and scope

The two positions of the residue characteristic in the maximal-ideal filtration both occur. Let $`V=\mathbb Z_p`$, let $`e\ge3`$, and form the algebra with basis $`1,X_1,\ldots,X_e,Z`$ and rules
```math
X_iX_j=\delta_{ij}Z,\qquad X_iZ=Z^2=0.
```
The quotients $`T/(p-Z)`$ and $`T/(p-X_1)`$ have Hilbert function $`(1,e,1)`$ and nonsingular multiplication pairing. They are Gorenstein and dominant. In the first, $`p`$ generates the socle and the characteristic is $`p^2`$. In the second, $`p`$ has nonzero degree-one class, $`p^2=Z\ne0`$, and the characteristic is $`p^3`$. Their common graded counterpart has characteristic $`p`$. These examples illustrate the transfer; the theorem covers arbitrary residue fields and arbitrary symmetric multiplication tensors.

The accompanying standard-library Python program constructs exact finite quotients using the lattice generated by the columns of multiplication by $`p-a`$. Its triangular matrix has diagonal entries $`p`$, giving unique representatives with every coordinate in $`\{0,\ldots,p-1\}`$. The program checks associativity on the integral basis, stability of the relation lattice under multiplication, the quotient cardinality, the first two maximal-ideal layers, the socle, and the position and order of $`p`$.

The recorded run covers 258 quotient rings, including 86 Gorenstein and 172 non-Gorenstein cases. It enumerates 16,860 elements and checks 31,698 basis associativity identities. The examples have characteristics $`4,8,9,27`$. These are diagnostics for the construction; the proof over an arbitrary Cohen ring is the argument of Section 2.

The construction uses $`\mathfrak m^3=0`$ at a precise point: every triple product of positive-degree basis elements vanishes, so arbitrary lifts of the multiplication coefficients remain associative. For longer local rings, lifting a multiplication table introduces additional associativity conditions. No corresponding arbitrary-length lifting theorem is asserted. Nor does Theorem [1.2](#label-thm-transfer) imply that every non-Gorenstein short ring is dominant.

The quantitative transfer leaves a focused further problem: determine whether the non-complete-intersection Gorenstein graded rings with Hilbert function $`(1,e,1)`$ are uniformly dominant, and, if so, bound their dominant indices in terms of $`e`$. Any such bound transfers immediately to short Gorenstein rings without a coefficient field by [(2)](#label-eq-indices).

**Preparation.**

This manuscript was developed with AI assistance. The proof and accompanying computations have undergone internal checks; independent expert review has not been completed.

## References

<a id="ref-AIS"></a>

**\[1\]** L. L. Avramov, S. B. Iyengar, and L. M. Şega, *Free resolutions over short local rings*, J. Lond. Math. Soc. (2) **78** (2008), 459–476. <https://arxiv.org/abs/0707.4451>.

<a id="ref-K"></a>

**\[2\]** K. Kimura, *Thick subcategories over weakly symmetric algebras with radical cube zero*, preprint, 2026, version 1. <https://arxiv.org/abs/2609.05781v1>.

<a id="ref-KT"></a>

**\[3\]** T. Kobayashi and R. Takahashi, *On the ubiquity of uniformly dominant local rings*, preprint, 2026, version 1. <https://arxiv.org/abs/2603.10810v1>.

<a id="ref-L"></a>

**\[4\]** J. Liu, *On Takahashi’s descent question about dominant local rings*, preprint, 2026, version 2. <https://arxiv.org/abs/2608.14283v2>.

<a id="ref-Stacks"></a>

**\[5\]** The Stacks Project Authors, *The Stacks Project*, Tags 032A, 09Q7, and 0BJL, accessed September 9, 2026. <https://stacks.math.columbia.edu>.

<a id="ref-T"></a>

**\[6\]** R. Takahashi, *Dominant local rings and subcategory classification*, Int. Math. Res. Not. IMRN **2023**, no. 9, 7259–7318. <https://doi.org/10.1093/imrn/rnac053>.

<a id="ref-U"></a>

**\[7\]** R. Takahashi, *Uniformly dominant local rings and Orlov spectra of singularity categories*, preprint. <https://arxiv.org/abs/2412.00669>.
