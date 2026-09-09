# Integral Lefschetz decompositions of fully whiskered simplicial complexes

September 8, 2026

## Abstract

The square-zero Artinian algebra of a fully whiskered simplicial complex admits an exact integral decomposition, as a module over its Lefschetz operator, into shifted squarefree complete intersections indexed by the faces. This gives an integral diagonal form for every multiplication power through Wilson’s classical inclusion-matrix theorem. We obtain all multiplication ranks and graded Jordan types in every characteristic, and an exact description of every failing degree and power in characteristic zero. In particular, if the complex has $`n`$ vertices and maximum face cardinality $`r`$, the weak Lefschetz property holds precisely when $`r\leq1`$, or $`n`$ is odd and $`r\leq2`$, with the additional condition $`p>\lceil n/2\rceil`$ in positive characteristic. The strong Lefschetz property holds precisely when $`r\leq1`$, with $`p>n`$ additionally required. For independence complexes this settles the conjecture of Holleben and Nicklasson. The decomposition also produces a larger family of G-quadratic Gorenstein idealizations failing the weak Lefschetz property.

## 1. Introduction

Let $`\Delta`$ be a simplicial complex with vertex set $`[n]`$, where $`n\geq1`$ and every singleton is a face. Let $`I_\Delta`$ be its Stanley–Reisner ideal. We study

<a id="label-eq-algebra"></a>

```math
\tag{1}
 A_{\Delta,\mathbb K}=
 \frac{\mathbb K[x_1,\ldots,x_n,y_1,\ldots,y_n]}
 {I_\Delta(x)+(x_i^2,y_i^2,x_i y_i:1\leq i\leq n)}
```

over an arbitrary field $`\mathbb K`$. The corresponding integral algebra is denoted $`A_{\Delta,\mathbb Z}`$. Put
```math
L=\sum_{i=1}^n(x_i+y_i),\qquad
 f_s=|\{S\in\Delta:|S|=s\}|,\qquad
 r=\max\{|S|:S\in\Delta\}.
```
Our face numbers are indexed by cardinality: $`f_0=1`$ and $`f_1=n`$. Binomial coefficients with lower index outside $`[0,a]`$ are interpreted as zero.

A standard graded Artinian algebra has the weak Lefschetz property (WLP) if multiplication by some linear form has maximal rank in every consecutive degree. It has the strong Lefschetz property (SLP) if all positive powers of the same form have maximal rank between every pair of degrees. For a monomial algebra, these properties can be tested using the sum of the variables.

If $`\Delta=\operatorname{Ind}(G)`$ is the independence complex of a graph $`G`$, then [(1)](#label-eq-algebra) is the square-zero Artinian algebra of the fully whiskered graph $`w(G)`$. Holleben and Nicklasson conjectured that this algebra fails WLP whenever $`\alpha(G)\geq3`$ [\[4, Conjectures 1.3 and 3.15\]](#ref-HN). Positive cases for complete graphs and for odd-order graphs of independence number at most two were already known [\[4, Propositions 3.2 and 3.5\]](#ref-HN). Earlier work gives endpoint ranks and lower-half injectivity [\[1, Theorem 1.2\]](#ref-CFHNV). A recent preprint verifies the eight-vertex case by exact kernel certificates [\[6\]](#ref-Zeng).

The main observation is an exact operator decomposition. For
```math
B_{a,\mathbb Z}=\mathbb Z[z_1,\ldots,z_a]/(z_1^2,\ldots,z_a^2),
 \qquad U=z_1+\cdots+z_a,
```
with $`B_{0,\mathbb Z}=\mathbb Z`$, it takes the form

<a id="label-eq-main-splitting"></a>

```math
\tag{2}
 (A_{\Delta,\mathbb Z},L)\cong
 \bigoplus_{S\in\Delta}(B_{n-|S|,\mathbb Z},U)(-|S|).
```

This is a graded $`\mathbb Z[t]`$-module isomorphism, with $`t`$ acting as the displayed operators. The shift $`(-s)`$ places degree zero in degree $`s`$. In particular, [(2)](#label-eq-main-splitting) is simultaneous for every power and survives reduction modulo every prime.

Combining this decomposition with Wilson’s diagonal form for Boolean inclusion matrices [\[5,3\]](#ref-Wilson) gives every multiplication rank and its integral torsion data. In characteristic zero, we obtain the particularly simple criterion

<a id="label-eq-locus-intro"></a>

```math
\tag{3}
 L^e:(A_\Delta)_i\longrightarrow(A_\Delta)_{i+e}
 \text{ has maximal rank}
 \quad\Longleftrightarrow\quad
 2i+e\leq n\ \text{or}\ 2i+e\geq n+r
```

for $`0\leq i<i+e\leq n`$. All ranks depend only on the face numbers, while the maximal-rank locus in characteristic zero depends only on $`n`$ and $`r`$. We also prove sharp positive-characteristic WLP and SLP criteria and recover the face numbers from ordinary Jordan type in characteristic zero.

The classical inclusion-matrix theorem is not a new ingredient. The contribution is the exact splitting [(2)](#label-eq-main-splitting) and the operator description it gives for the whole whiskered family. The block-triangular argument in [\[4, Lemma 3.1\]](#ref-HN) treats complete graphs and more general monomial powers. Its square-zero specialization does not state the simultaneous splitting used here. The differentiation cokernel in [\[4, Theorem 3.10\]](#ref-HN) was a precursor to the classification, but the present proof determines all ranks directly. Section [7](#label-sec-idealization) applies the resulting cokernel range to Gorenstein idealizations, extending [\[4, Theorem 4.6\]](#ref-HN).

## 2. The integral splitting

<a id="theorem-1"></a>

**Theorem 2.1.**

<a id="label-thm-splitting"></a>

There is an isomorphism [(2)](#label-eq-main-splitting) of graded $`\mathbb Z[t]`$-modules. In particular, this is a direct sum decomposition over every field, and the summand associated with a face $`S`$ is a squarefree complete intersection on its complementary indices, shifted by $`|S|`$.

<!-- end theorem-1 -->

<a id="proof-1"></a>

**Proof.**

Set $`z_i=x_i+y_i`$, so $`y_i=z_i-x_i`$. This is an invertible integral linear change of variables. The identities
```math
\begin{align*}
 x_i z_i&=x_i^2+x_i y_i,&
 z_i^2&=x_i^2+2x_i y_i+y_i^2,\\
 x_i y_i&=x_i z_i-x_i^2,&
 y_i^2&=z_i^2-2x_i z_i+x_i^2
\end{align*}
```
show equality of the local defining ideals after substitution. The ideal $`I_\Delta(x)`$ is unchanged. Thus
```math
A_{\Delta,\mathbb Z}=
 \frac{\mathbb Z[x_1,\ldots,x_n,z_1,\ldots,z_n]}
 {I_\Delta(x)+(x_i^2,z_i^2,x_i z_i:1\leq i\leq n)},
 \qquad L=\sum_i z_i.
```
Its integral monomial basis is
```math
\{x_S z_T:S\in\Delta,\ T\subseteq[n]\setminus S\}.
```
For fixed $`S`$, the span of these monomials is stable under every $`z_i`$. It is $`x_S`$ times the squarefree complete intersection on $`[n]\setminus S`$. The basis is a disjoint union over $`S`$, proving the theorem. $`\square`$

<!-- end proof-1 -->

<a id="remark-1"></a>

**Remark 2.2.**

The decomposition is a decomposition of modules with an operator, not an algebra direct product. It is also stronger than a Hilbert-series identity or a filtration: the multiplication matrices have no off-diagonal blocks in this basis.

<!-- end remark-1 -->

The decomposition immediately gives

<a id="label-eq-hilbert"></a>

```math
\tag{4}
 h_i:=\dim_\mathbb K(A_{\Delta,\mathbb K})_i
 =\sum_{s=0}^r f_s\binom{n-s}{i-s},\qquad
 H_{A_\Delta}(t)=\sum_{s=0}^r f_s t^s(1+t)^{n-s}.
```

The algebra is concentrated in degrees $`0,\ldots,n`$, with nonzero components in each of these degrees.

## 3. Integral diagonal forms and ranks in every characteristic

We recall precisely the classical matrix result used below. Let $`W_{t,k}(a)`$ be the matrix with rows indexed by $`t`$-subsets of $`[a]`$, columns indexed by $`k`$-subsets, and entry one exactly for containment.

<a id="theorem-2"></a>

**Theorem 3.1 (Wilson).**

<a id="label-thm-wilson"></a>

If $`0\leq t\leq k\leq a-t`$, then $`W_{t,k}(a)`$ is equivalent under unimodular integer row and column operations to a rectangular diagonal matrix with entries
```math
\binom{k-j}{t-j}
 \quad\text{with multiplicity}\quad
 \binom aj-\binom a{j-1},\qquad 0\leq j\leq t.
```

<!-- end theorem-2 -->

This is Wilson’s theorem [\[5\]](#ref-Wilson); an accessible primary proof, also crediting Bier’s approach, is [\[3, Corollary 3\]](#ref-GKKM). The entries need not occur in divisibility order, so this is a diagonal form rather than necessarily the Smith normal form in its standard order.

<a id="theorem-3"></a>

**Theorem 3.2.**

<a id="label-thm-diagonal"></a>

Fix $`i\geq0`$ and $`e\geq1`$. For each $`s`$ such that $`f_s\ne0`$ and
```math
0\leq q_s:=i-s\leq q_s+e\leq a_s:=n-s,
 \qquad t_s=\min(q_s,a_s-q_s-e),
```
the multiplication map
```math
L^e:(A_{\Delta,\mathbb Z})_i\longrightarrow(A_{\Delta,\mathbb Z})_{i+e}
```
has a nonzero integral diagonal entry

<a id="label-eq-diagentries"></a>

```math
\tag{5}
 e!\binom{t_s+e-j}{e}
 \quad\text{with multiplicity}\quad
 f_s\left(\binom{a_s}{j}-\binom{a_s}{j-1}\right),
 \qquad 0\leq j\leq t_s.
```

Collecting these entries over $`s`$, together with the remaining zero rows and columns, gives a diagonal form of the entire map.

<!-- end theorem-3 -->

<a id="proof-2"></a>

**Proof.**

In $`B_a`$, multiplication by $`U^e`$ takes a squarefree monomial $`z_T`$ of degree $`q`$ to
```math
U^e z_T=e!\sum_{\substack{V\supseteq T\\|V|=q+e}}z_V.
```
Each choice of $`e`$ new indices occurs in $`e!`$ orders; choices with a repeated index vanish. Thus the matrix is $`e!W_{q,q+e}(a)^{\mathsf T}`$.

If $`2q+e\leq a`$, apply Theorem [3.1](#label-thm-wilson) with $`t=q`$. Otherwise complementing subsets and transposing reduces the matrix to the inclusion matrix with $`t=a-q-e`$ and $`k=a-q`$. In both cases $`k=t+e`$ and $`t\leq k\leq a-t`$. Multiplying the matrix by $`e!`$ multiplies each diagonal entry by $`e!`$, using the same unimodular operations. Theorem [2.1](#label-thm-splitting) supplies the direct sum and the factors $`f_s`$. Blocks with zero source or target contribute only zero columns or rows. $`\square`$

<!-- end proof-2 -->

For a prime $`p`$ define, when $`0\leq q\leq q+e\leq a`$ and $`t=\min(q,a-q-e)`$,

<a id="label-eq-rho"></a>

```math
\tag{6}
 \rho_p(a,q,e)=
 \sum_{j=0}^t\left(\binom aj-\binom a{j-1}\right)
 \mathbf1_{\,p\nmid e!\binom{t+e-j}{e}}.
```

In characteristic zero put
```math
\rho_0(a,q,e)=\min\left\{\binom aq,\binom a{q+e}\right\}.
```
For invalid Boolean degrees set $`\rho_p(a,q,e)=0`$, including $`p=0`$.

<a id="corollary-1"></a>

**Corollary 3.3.**

<a id="label-cor-ranks"></a>

Over a field of characteristic $`p`$, with $`p=0`$ allowed,

<a id="label-eq-rankformula"></a>

```math
\tag{7}
 \operatorname{rank}\bigl(L^e:(A_\Delta)_i\to(A_\Delta)_{i+e}\bigr)
 =\sum_{s=0}^r f_s\rho_p(n-s,i-s,e).
```

In positive characteristic $`L^e=0`$ whenever $`e\geq p`$. Every rank depends only on the face numbers.

<!-- end corollary-1 -->

<a id="proof-3"></a>

**Proof.**

Reduce the integral diagonal form modulo $`p`$. In characteristic zero all its displayed entries are nonzero, and the multiplicities telescope to $`\binom at`$, the smaller Boolean dimension. If $`e\geq p`$, every diagonal entry is divisible by $`p`$; equivalently $`L^p=0`$ by Frobenius. $`\square`$

<!-- end proof-3 -->

Theorem [3.2](#label-thm-diagonal) also determines the abelian-group cokernel. Each positive diagonal entry $`d`$ contributes a cyclic group $`\mathbb Z/d\mathbb Z`$, and the excess target rank contributes a free summand. This integral statement distinguishes the primes causing rank failure without computing any minors of the full whiskered multiplication matrix.

## 4. Every maximal-rank degree and power in characteristic zero

<a id="theorem-4"></a>

**Theorem 4.1.**

<a id="label-thm-locus"></a>

Suppose $`\operatorname{char}\mathbb K=0`$ and $`0\leq i<i+e\leq n`$. Then $`L^e:(A_\Delta)_i\to(A_\Delta)_{i+e}`$ has maximal rank if and only if
```math
2i+e\leq n\qquad\text{or}\qquad 2i+e\geq n+r.
```
It is injective in the first range and surjective in the second. In the intervening range $`n<2i+e<n+r`$, it has both a nonzero kernel and a nonzero cokernel. The last assertion holds over every field.

<!-- end theorem-4 -->

<a id="proof-4"></a>

**Proof.**

A Boolean block shifted by $`s`$ has source and target dimensions
```math
\binom{n-s}{i-s}\quad\text{and}\quad\binom{n-s}{i+e-s}.
```
Its characteristic-zero rank is the smaller dimension. Comparison of symmetric binomial coefficients shows injectivity when $`2i+e\leq n+s`$ and surjectivity when $`2i+e\geq n+s`$. The same conclusions hold if one of the graded components is zero. If $`2i+e\leq n`$, all blocks are injective; if $`2i+e\geq n+r`$, all blocks are surjective.

Suppose now that $`n<2i+e<n+r`$. The empty-face block has strictly larger source than target dimension, so it has a kernel over every field. Put $`h=2i+e-n`$, so $`0<h<r`$. Since $`i+e\leq n`$, we have $`h\leq i`$. Downward closure gives a face of cardinality $`s=h+1\leq i+1`$. If $`s=i+1`$, its block has zero source and nonzero target. Otherwise its source and target degrees are both valid, and $`2i+e=n+h<n+s`$ makes the target dimension strictly larger. Hence this block has a cokernel over every field. The direct sum gives both defects for the whole map. $`\square`$

<!-- end proof-4 -->

<a id="corollary-2"></a>

**Corollary 4.2.**

<a id="label-cor-degrees"></a>

In characteristic zero, the consecutive maps that fail maximal rank are exactly
```math
i\longrightarrow i+1,
 \qquad \left\lceil\frac n2\right\rceil
 \leq i\leq\left\lfloor\frac{n+r}{2}\right\rfloor-1.
```
An empty interval means that the WLP holds.

<!-- end corollary-2 -->

## 5. Weak and strong Lefschetz properties in every characteristic

We first record the usual reduction from arbitrary linear forms to $`L`$.

<a id="lemma-1"></a>

**Lemma 5.1.**

<a id="label-lem-generic"></a>

For an Artinian monomial quotient over any field, the sum of the variables tests WLP and SLP. Over an infinite field its ranks are the generic ranks for every multiplication power.

<!-- end lemma-1 -->

<a id="proof-5"></a>

**Proof.**

Diagonal automorphisms preserve the monomial ideal, so forms with all coefficients nonzero have the same ranks as the sum of the variables. The maximal-rank conditions are Zariski open, with only finitely many relevant degrees and powers. Over an infinite field a nonempty such open set meets the coefficient torus. For a finite field extend scalars to its algebraic closure: ranks of the fixed sum are unchanged, a Lefschetz element would remain one after extension, and the sum itself is defined over the original field. $`\square`$

<!-- end proof-5 -->

<a id="theorem-5"></a>

**Theorem 5.2.**

<a id="label-thm-classification"></a>

Over any field, $`A_{\Delta,\mathbb K}`$ has WLP if and only if

<a id="label-eq-wlpcondition"></a>

```math
\tag{8}
 r\leq1\quad\text{or}\quad(n\text{ odd and }r\leq2),
```

and, in positive characteristic $`p`$, additionally $`p>\lceil n/2\rceil`$. It has SLP if and only if $`r\leq1`$ and, in positive characteristic, additionally $`p>n`$.

<!-- end theorem-5 -->

<a id="proof-6"></a>

**Proof.**

Theorem [4.1](#label-thm-locus) and Lemma [5.1](#label-lem-generic) prove the characteristic-zero assertions. They also exclude [(8)](#label-eq-wlpcondition)’s negative cases over every field: use $`i=\lceil n/2\rceil`$, $`e=1`$ in the mixed range. For SLP this excludes $`r\geq2`$ when $`n`$ is even, and $`r\geq3`$ when $`n`$ is odd. If $`n=2m+1`$ and $`r=2`$, take $`i=m,e=2`$, again in the mixed range. Thus $`r\geq2`$ always excludes SLP.

Suppose $`p\leq\lceil n/2\rceil`$ and put $`i=p-1`$. Frobenius gives $`L^p=0`$, but $`L^{p-1}\ne0`$: in the empty-face block its squarefree coefficients are $`(p-1)!`$, nonzero modulo $`p`$. Thus multiplication by $`L`$ has a nonzero kernel in degree $`i`$.

In this degree $`h_i<h_{i+1}`$. Indeed $`i\leq\lceil n/2\rceil-1`$, so every difference
```math
\binom{n-s}{i+1-s}-\binom{n-s}{i-s}
```
is nonnegative. For even $`n=2m`$, the empty-face difference is strictly positive for $`i\leq m-1`$. For odd $`n=2m+1`$ it is strictly positive for $`i\leq m-1`$. In the remaining case $`i=m`$, the singleton difference is
```math
\binom{2m}{m}-\binom{2m}{m-1}>0.
```
Here $`m\geq1`$, because $`p\geq2`$, and $`f_1=n>0`$. Equation [(4)](#label-eq-hilbert) proves the strict inequality. The nonzero kernel therefore violates maximal rank, establishing necessity of the WLP characteristic condition.

Conversely, suppose [(8)](#label-eq-wlpcondition) holds and $`p>\lceil n/2\rceil`$. For $`e=1`$, every nonzero diagonal entry in a Boolean block is $`t+1-j`$. In $`a\leq n`$ variables, $`t+1\leq\lceil a/2\rceil\leq\lceil n/2\rceil`$. Every entry is consequently nonzero modulo $`p`$. All consecutive ranks equal their characteristic-zero ranks, and WLP follows.

For SLP, if $`p\leq n`$, then $`L^p:A_0\to A_p`$ is zero with both spaces nonzero. If $`p>n`$, each diagonal entry in [(5)](#label-eq-diagentries) is a product
```math
e!\binom{t+e-j}{e}
 =(t+e-j)(t+e-j-1)\cdots(t-j+1)
```
of positive integers at most $`n`$. Thus all powers retain their characteristic-zero ranks. When $`r\leq1`$, this gives SLP. $`\square`$

<!-- end proof-6 -->

<a id="corollary-3"></a>

**Corollary 5.3.**

<a id="label-cor-graph"></a>

For a graph $`G`$ on $`n`$ vertices, $`A(w(G))`$ has WLP precisely when $`G`$ is complete, or $`n`$ is odd and $`\alpha(G)\leq2`$, subject to $`p>\lceil n/2\rceil`$ in positive characteristic. It has SLP precisely when $`G`$ is complete, subject to $`p>n`$ in positive characteristic.

<!-- end corollary-3 -->

This proves the graph WLP conjecture of Holleben and Nicklasson. The positive graph cases in characteristic zero and the SLP sufficient condition $`p>n`$ for complete graphs were already established in [\[4\]](#ref-HN). Frobenius gives the necessity of the latter threshold. These known positive cases are recovered by the full operator formula.

## 6. Jordan type and recovery of face numbers

Write $`R_e=\operatorname{rank}(L^e:A_\Delta\to A_\Delta)`$, summing over degrees, with $`R_0=\dim A_\Delta`$. Put $`R_e=0`$ for $`e>n`$.

<a id="proposition-1"></a>

**Proposition 6.1.**

<a id="label-prop-jordan"></a>

Over every field, the number of Jordan blocks of length $`\ell`$ is
```math
R_{\ell-1}-2R_\ell+R_{\ell+1}.
```
For $`0\leq a\leq b\leq n`$, put
```math
r_{a,b}=\operatorname{rank}(L^{b-a}:(A_\Delta)_a\to(A_\Delta)_b),
 \qquad r_{a,a}=h_a,
```
and interpret indices $`a<0`$ or $`b>n`$ as zero. The multiplicity of graded Jordan strings supported on $`[a,b]`$ is

<a id="label-eq-gradedjordan"></a>

```math
\tag{9}
 r_{a,b}-r_{a-1,b}-r_{a,b+1}+r_{a-1,b+1}.
```

Consequently [(7)](#label-eq-rankformula) determines ordinary and graded Jordan type from the face numbers in every characteristic.

<!-- end proposition-1 -->

<a id="proof-7"></a>

**Proof.**

The elementary structure theorem for finite graded torsion $`\mathbb K[t]`$-modules gives a direct sum of shifted modules $`\mathbb K[t]/(t^\ell)`$, or homogeneous Jordan strings. A length-$`\ell`$ string contributes $`\max(\ell-e,0)`$ to $`R_e`$; the second difference isolates its length. A string $`[u,v]`$ contributes one to $`r_{a,b}`$ exactly when $`u\leq a`$ and $`v\geq b`$. The two-variable difference in [(9)](#label-eq-gradedjordan) isolates $`u=a,v=b`$. $`\square`$

<!-- end proof-7 -->

In characteristic zero the answer has a closed form.

<a id="theorem-6"></a>

**Theorem 6.2.**

<a id="label-thm-charzerojordan"></a>

If $`\operatorname{char}\mathbb K=0`$, then as a graded $`\mathbb K[t]`$-module,

<a id="label-eq-strings"></a>

```math
\tag{10}
 A_\Delta\cong
 \bigoplus_{s=0}^r\ \bigoplus_{b=0}^{\lfloor(n-s)/2\rfloor}
 \left(\frac{\mathbb K[t]}{(t^{n-s-2b+1})}(-s-b)\right)^
 {f_s\left(\binom{n-s}{b}-\binom{n-s}{b-1}\right)},
```

where $`t`$ acts by $`L`$. The string indexed by $`s,b`$ is supported on $`[s+b,n-b]`$.

<!-- end theorem-6 -->

<a id="proof-8"></a>

**Proof.**

The Boolean power ranks are the smaller binomial dimensions by Theorem [3.1](#label-thm-wilson). Applying [(9)](#label-eq-gradedjordan) to these ranks yields strings $`[b,a-b]`$ with multiplicity $`\binom ab-\binom a{b-1}`$ in $`B_a`$. Theorem [2.1](#label-thm-splitting) shifts these strings by $`s`$ and repeats them $`f_s`$ times. $`\square`$

<!-- end proof-8 -->

<a id="corollary-4"></a>

**Corollary 6.3.**

<a id="label-cor-recover"></a>

In characteristic zero, the ordinary Jordan type of $`L`$ determines the face numbers of $`\Delta`$. Conversely, the face numbers determine the graded Jordan type in every characteristic.

<!-- end corollary-4 -->

<a id="proof-9"></a>

**Proof.**

The largest block in [(10)](#label-eq-strings) has length $`n+1`$ and multiplicity one, recovering $`n`$. Let $`J_\ell`$ denote the multiplicity of blocks of length $`\ell`$. For $`0\leq s\leq n`$,
```math
J_{n-s+1}=f_s+
 \sum_{\substack{0\leq h<s\\s-h\text{ even}}}
 f_h\left(\binom{n-h}{(s-h)/2}-\binom{n-h}{(s-h)/2-1}\right).
```
This triangular system has coefficient one on $`f_s`$ and recovers the face numbers successively. The converse follows from Proposition [6.1](#label-prop-jordan) and Corollary [3.3](#label-cor-ranks). $`\square`$

<!-- end proof-9 -->

The characteristic-zero strings in [(10)](#label-eq-strings) are not asserted to give an integral Jordan decomposition. Reduction modulo a prime can change the string structure, which is why the integral diagonal forms and rank differences are used for arbitrary characteristic.

## 7. A Gorenstein idealization application

<a id="label-sec-idealization"></a>

Let $`A^\vee`$ be the graded $`\mathbb K`$-dual of $`A=A_{\Delta,\mathbb K}`$, and form
```math
T=A\ltimes A^\vee(-n-1),\qquad
 T_i=A_i\oplus(A_{n+1-i})^\vee.
```
The product is $`(a,\varphi)(b,\psi)=(ab,a\psi+b\varphi)`$, with the natural dual module action. This is the standard canonical-module idealization of $`A`$ with socle degree $`n+1`$.

<a id="proposition-2"></a>

**Proposition 7.1.**

<a id="label-prop-idealization"></a>

In characteristic zero, $`T`$ is standard graded Artinian Gorenstein and fails WLP whenever $`n`$ is even and $`r\geq2`$, or $`n`$ is odd and $`r\geq3`$. For $`\Delta=\operatorname{Ind}(G)`$, these are G-quadratic Gorenstein algebras.

<!-- end proposition-2 -->

<a id="proof-10"></a>

**Proof.**

Every maximal surviving monomial of $`A`$ has degree $`n`$: a monomial $`x_Sy_T`$ of smaller degree can be multiplied by $`y_j`$ for an index outside $`S\cup T`$. Thus $`A`$ is level of socle degree $`n`$, its shifted dual is generated in degree one, and $`T`$ is standard graded. Evaluation gives a perfect pairing between its complementary degrees and a one-dimensional degree-$`(n+1)`$ socle, proving the Gorenstein assertion.

Put $`d=\lceil n/2\rceil`$. In the stated cases Theorem [4.1](#label-thm-locus) gives a cokernel for $`L:A_d\to A_{d+1}`$. In fact every $`u\in A_1`$ is nonsurjective in this degree: if a surjective form existed, its nonempty rank-open set would meet the coefficient torus, contradicting Lemma [5.1](#label-lem-generic).

Suppose $`T`$ had WLP with a linear form $`\ell`$. Its Hilbert function would be unimodal: once a multiplication map is surjective, the standard graded quotient by $`\ell`$ vanishes in that and all higher degrees, so all subsequent maps are surjective. Its Hilbert function is also symmetric about $`(n+1)/2`$. Therefore $`\ell:T_d\to T_{d+1}`$ must be surjective. For even $`n`$ the two middle dimensions are equal; for odd $`n`$ the source is the middle degree and is at least the next dimension. Surjectivity descends under the quotient $`T\to A`$ to multiplication by the image $`u`$ of $`\ell`$, a contradiction.

For the graph assertion, $`\operatorname{Ind}(w(G))`$ is flag and shellable [\[4, Theorem 2.1\]](#ref-HN). Its facets correspond to independent sets $`S`$ of $`G`$, with monomials $`m_S=x_Sy_{[n]\setminus S}`$. Since $`r\geq2`$, some $`\{u,v\}`$ is independent and
```math
m_{\{u,v\}}m_{\varnothing}=m_{\{u\}}m_{\{v\}}.
```
The distinct facet monomials are thus linearly independent and algebraically dependent, making the associated simplicial form a Perazzo form. By [\[4, Lemma 4.5\]](#ref-HN), its apolar algebra is $`T`$. Shellability supplies a quadratic Gröbner basis by [\[4, Theorem 4.4\]](#ref-HN), which invokes the results of D’Alì and Venturello [\[2, Corollary 8.2 and Proposition 8.3\]](#ref-DV). $`\square`$

<!-- end proof-10 -->

The high-degree quotient obstruction for idealizations is already used in [\[4, Theorem 4.6\]](#ref-HN). That theorem assumes $`\alpha(G)\geq n/3+2`$; Proposition [7.1](#label-prop-idealization) applies throughout the broader parity-dependent ranges above. We do not claim a classification of WLP for these idealizations or for all Perazzo algebras.

## 8. Scope

The results concern the precise square-zero reductions [(1)](#label-eq-algebra). The integral coordinate change uses all three local quadratic relations and does not establish an analogous decomposition for arbitrary monomial powers. The class of very well-covered graphs is broader than fully whiskered graphs, and the present classification is not asserted for that broader class.

All main formulas follow from the integral splitting and the classical inclusion-matrix theorem. Exact computations in the original $`x/y`$ monomial bases provide ancillary checks of the modular rank formulas and characteristic thresholds; they are not premises of the proofs.

## References

<a id="ref-CFHNV"></a>

**\[1\]** S. M. Cooper, S. Faridi, T. Holleben, L. Nicklasson and A. Van Tuyl, *The weak Lefschetz property of whiskered graphs*, in *Lefschetz Properties: Current and New Directions*, Springer INdAM Series **59** (2024), 97–110. [doi:10.1007/978-981-97-3886-1_5](https://doi.org/10.1007/978-981-97-3886-1_5); [arXiv:2306.04393](https://arxiv.org/abs/2306.04393).

<a id="ref-DV"></a>

**\[2\]** A. D’Alì and L. Venturello, *Koszul Gorenstein algebras from Cohen–Macaulay simplicial complexes*, International Mathematics Research Notices **2023** (2023), no. 6, 4998–5045. [doi:10.1093/imrn/rnac003](https://doi.org/10.1093/imrn/rnac003); [arXiv:2106.05051v2](https://arxiv.org/abs/2106.05051v2).

<a id="ref-GKKM"></a>

**\[3\]** E. Ghorbani, G. B. Khosrovshahi, Ch. Maysoori and M. Mohammad-Noori, *Inclusion matrices and chains*, Journal of Combinatorial Theory, Series A **115** (2008), no. 5, 878–887. [doi:10.1016/j.jcta.2007.09.002](https://doi.org/10.1016/j.jcta.2007.09.002); [arXiv:0709.3144](https://arxiv.org/abs/0709.3144).

<a id="ref-HN"></a>

**\[4\]** T. Holleben and L. Nicklasson, *Roller Coaster Gorenstein algebras and Koszul algebras failing the weak Lefschetz property*, Journal of Pure and Applied Algebra **230** (2026), no. 4, article 108238. [doi:10.1016/j.jpaa.2026.108238](https://doi.org/10.1016/j.jpaa.2026.108238); [arXiv:2502.00155v2](https://arxiv.org/abs/2502.00155v2).

<a id="ref-Wilson"></a>

**\[5\]** R. M. Wilson, *A diagonal form for the incidence matrices of $`t`$-subsets vs. $`k`$-subsets*, European Journal of Combinatorics **11** (1990), no. 6, 609–615. [doi:10.1016/S0195-6698(13)80046-7](https://doi.org/10.1016/S0195-6698(13)80046-7).

<a id="ref-Zeng"></a>

**\[6\]** Z. Zeng, *The Whiskered-Graph Weak Lefschetz Conjecture for Graphs on Eight Vertices*, SSRN preprint, posted September 3, 2026. [doi:10.2139/ssrn.7385138](https://doi.org/10.2139/ssrn.7385138).
