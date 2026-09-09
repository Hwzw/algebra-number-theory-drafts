# Lefschetz properties of fully whiskered simplicial complexes

Henry Zweiman

September 8, 2026

## Abstract

Let $`\Delta`$ be a simplicial complex on $`n`$ vertices, and form the Artinian monomial algebra obtained by adjoining one square-zero variable $`y_i`$ to each square-zero vertex variable $`x_i`$, with $`x_i y_i=0`$. In characteristic zero we classify the weak Lefschetz property: it holds precisely when the maximum face cardinality is at most one, or when $`n`$ is odd and that cardinality is at most two. The strong Lefschetz property holds precisely when the maximum face cardinality is at most one. An embedded squarefree complete intersection provides a universal multiplication kernel. Combining it with a differentiation cokernel yields the negative directions without Hilbert-function estimates. For independence complexes, this proves the conjecture of Holleben and Nicklasson concerning independence number at least three. The negative assertions hold over arbitrary fields.

## 1. Introduction and statements

Throughout, $`\Delta`$ is a finite simplicial complex with vertex set $`[n]`$, $`n\geq1`$, and $`r=\max\{|S|:S\in\Delta\}`$. In particular every singleton is a face. Let $`I_\Delta\subseteq\mathbb{k}[x_1,\ldots,x_n]`$ be its Stanley–Reisner ideal and set
```math
{A_{\Delta}}=\frac{\mathbb{k}[x_1,\ldots,x_n,y_1,\ldots,y_n]}{I_\Delta+(x_i^2,y_i^2,x_i y_i:1\leq i\leq n)}.
```
This construction will be called full whiskering followed by square-zero Artinian reduction. Its definition here fixes the precise meaning of whiskering; no hypothesis on flagness or purity of $`\Delta`$ is imposed.

A standard graded Artinian algebra $`A`$ has the weak Lefschetz property (WLP) if some linear form $`L`$ induces maps $`A_d\to A_{d+1}`$ of maximal rank in every degree. It has the strong Lefschetz property (SLP) if every map $`L^s:A_d\to A_{d+s}`$ has maximal rank for that same form and all $`s\geq1`$.

<a id="theorem-1"></a>

**Theorem 1.1.**

<a id="label-thm-main"></a>

Suppose $`\operatorname{char}\mathbb{k}=0`$. Then $`{A_{\Delta}}`$ has the WLP if and only if
```math
r\leq1\quad\text{or}\quad (n\text{ is odd and }r\leq2).
```
More precisely, if $`n`$ is even and $`r\geq2`$, or $`n`$ is odd and $`r\geq3`$, the map induced by the sum of the variables from degree $`\lceil n/2\rceil`$ to degree $`\lceil n/2\rceil+1`$ is neither injective nor surjective. These negative assertions, and failure of WLP in those cases, hold over every field.

<!-- end theorem-1 -->

<a id="theorem-2"></a>

**Theorem 1.2.**

<a id="label-thm-slp"></a>

In characteristic zero, $`{A_{\Delta}}`$ has the SLP if and only if $`r\leq1`$. If $`r\geq2`$, it fails SLP over every field. Consequently, in characteristic zero $`A(w(G))`$ has the SLP if and only if $`G`$ is complete.

<!-- end theorem-2 -->

For a graph $`G`$ on $`[n]`$, take $`\Delta=\operatorname{Ind}(G)`$. Then $`I_\Delta`$ is its edge ideal, $`r=\alpha(G)`$, and $`{A_{\Delta}}=A(w(G))`$ is the Artinian algebra of the graph obtained by attaching a pendant vertex to each vertex of $`G`$.

<a id="corollary-1"></a>

**Corollary 1.3.**

<a id="label-cor-graph"></a>

Over a field of characteristic zero, $`A(w(G))`$ has the WLP if and only if $`G`$ is complete, or $`n`$ is odd and $`\alpha(G)\leq2`$. In particular, $`\alpha(G)\geq3`$ implies failure of WLP.

<!-- end corollary-1 -->

The final assertion is the statement of Holleben–Nicklasson [\[2, Conjectures 1.3 and 3.15\]](#ref-HN). The positive graph cases were established in [\[2, Propositions 3.2 and 3.5\]](#ref-HN). Their Theorem 3.10 supplies a cokernel associated to an independent set, but obtaining maximal-rank failure through Hilbert-function estimates leaves a range of cases unresolved. We use their differentiation witness together with a universal multiplication kernel. The latter avoids any comparison of consecutive Hilbert-function values. Earlier work [\[1\]](#ref-CFHNV) establishes several degreewise Lefschetz results for whiskered graphs; a recent computation [\[3\]](#ref-Zeng) treats graphs on eight vertices. The contribution here is the uniform kernel argument, the resulting classification, and its extension to arbitrary simplicial complexes. The cokernel construction itself is credited to [\[2\]](#ref-HN).

## 2. Two elementary linear-algebra observations

The surviving monomials in $`{A_{\Delta}}`$ are exactly
```math
x_Sy_T=\prod_{i\in S}x_i\prod_{j\in T}y_j,
\qquad S\in\Delta,\quad T\subseteq[n]\setminus S.
```
They form a basis. Put $`L=\sum_{i=1}^n(x_i+y_i)`$.

<a id="lemma-1"></a>

**Lemma 2.1.**

<a id="label-lem-general"></a>

For an Artinian monomial quotient over any field, WLP (respectively SLP) holds if and only if the sum of its variables is a weak (respectively strong) Lefschetz element.

<!-- end lemma-1 -->

<a id="proof-1"></a>

**Proof.**

First work over an infinite field. Diagonal changes of variables preserve a monomial ideal, so all linear forms with nonzero coefficients have the same multiplication ranks as the sum of the variables. The simultaneous maximal-rank conditions define a Zariski-open subset of the space of linear forms: there are only finitely many maps to consider, and each condition is the nonvanishing of some maximal minor. If this set is nonempty, it intersects the coefficient torus, giving the claim. For a finite field, pass to its algebraic closure. Matrix ranks are unchanged by extension of scalars; a Lefschetz element over the original field would remain one after extension. Conversely the sum of the variables is itself defined over the original field. $`\square`$

<!-- end proof-1 -->

<a id="lemma-2"></a>

**Lemma 2.2.**

<a id="label-lem-propagate"></a>

If $`A`$ is standard graded and $`L\in A_1`$, nonsurjectivity of $`L:A_{t-1}\to A_t`$ implies nonsurjectivity of $`L:A_{s-1}\to A_s`$ for $`1\leq s\leq t`$.

<!-- end lemma-2 -->

<a id="proof-2"></a>

**Proof.**

The quotient $`A/(L)`$ is standard graded. If its degree-$`s`$ component vanishes, so do all higher-degree components. $`\square`$

<!-- end proof-2 -->

## 3. A universal kernel and a face-dependent cokernel

<a id="lemma-3"></a>

**Lemma 3.1.**

<a id="label-lem-kernel"></a>

For every $`\Delta`$ and every field, multiplication by $`L`$ on $`{A_{\Delta}}`$ has a nonzero kernel in degree $`d=\lceil n/2\rceil`$.

<!-- end lemma-3 -->

<a id="proof-3"></a>

**Proof.**

Set $`z_i=x_i+y_i`$. The relations imply $`z_i^2=0`$. The homomorphism
```math
B_n=\mathbb{k}[z_1,\ldots,z_n]/(z_1^2,\ldots,z_n^2)\longrightarrow{A_{\Delta}}
```
is injective: the pure-$`y`$ component of $`z_S`$ is $`y_S`$, and these surviving monomials are linearly independent. This also identifies the image of $`\sum z_i`$ with $`L`$.

If $`n=2m`$, set $`f=\prod_{j=1}^m(z_{2j-1}-z_{2j})`$. Each summand $`z_{2j-1}+z_{2j}`$ of $`L`$ kills the corresponding factor, so $`Lf=0`$. The coefficient of $`y_1y_3\cdots y_{2m-1}`$ is one, proving $`f\ne0`$.

If $`n=2m+1`$, use $`f=z_{2m+1}\prod_{j=1}^m(z_{2j-1}-z_{2j})`$. The same pairwise cancellations apply, and the remaining term gives $`z_{2m+1}^2=0`$. Again the pure-$`y`$ part proves nonvanishing. The degrees are respectively $`m`$ and $`m+1`$. $`\square`$

<!-- end proof-3 -->

<a id="lemma-4"></a>

**Lemma 3.2.**

<a id="label-lem-cokernel"></a>

Let $`C\in\Delta`$ have cardinality $`c`$. Multiplication by $`L`$ into degree $`t=\lfloor(n+c)/2\rfloor`$ is nonsurjective.

<!-- end lemma-4 -->

<a id="proof-4"></a>

**Proof.**

This is the construction of [\[2, Theorem 3.10\]](#ref-HN), which uses only the face condition and therefore applies here. Relabel $`C=\{q+1,\ldots,n\}`$ with $`q=n-c`$, and consider
```math
g=\prod_{j=1}^{\lfloor q/2\rfloor}(y_{2j-1}-y_{2j})
  \prod_{i=q+1}^n(x_i-y_i).
```
Its monomials all survive: their $`x`$-support is a subset of $`C`$, and their $`x`$- and $`y`$-supports are disjoint. It is nonzero and has degree $`t`$.

On the vector space spanned by surviving squarefree monomials, let $`D=\sum_i(\partial_{x_i}+\partial_{y_i})`$. Differentiation removes one variable, so it preserves this vector space. In its monomial bases, $`D:{A_{\Delta}}_t\to{A_{\Delta}}_{t-1}`$ is the transpose of $`L:{A_{\Delta}}_{t-1}\to{A_{\Delta}}_t`$. Ordinary differentiation of the displayed polynomial gives $`Dg=0`$, since the sum of the coefficients in every linear factor is zero. Hence $`D`$ has nonzero kernel and $`L`$ is nonsurjective. This use of differentiation is a vector-space construction; it does not assert that ordinary differentiation descends as a derivation of the quotient algebra. $`\square`$

<!-- end proof-4 -->

<a id="proof-5"></a>

**Proof of the negative assertions in Theorem [1.1](#label-thm-main).**

Let $`d=\lceil n/2\rceil`$ and choose a face of cardinality $`r`$. If $`n=2m`$ and $`r\geq2`$, then $`\lfloor(n+r)/2\rfloor\geq m+1=d+1`$. If $`n=2m+1`$ and $`r\geq3`$, then $`\lfloor(n+r)/2\rfloor\geq m+2=d+1`$. Lemmas [3.2](#label-lem-cokernel) and [2.2](#label-lem-propagate) give nonsurjectivity from degree $`d`$ to $`d+1`$, and Lemma [3.1](#label-lem-kernel) gives noninjectivity of the same map. Lemma [2.1](#label-lem-general) completes the argument over any field. $`\square`$

<!-- end proof-5 -->

## 4. The positive cases

We include a direct proof to make the WLP classification self-contained.

<a id="lemma-5"></a>

**Lemma 4.1.**

<a id="label-lem-boolean"></a>

In characteristic zero, multiplication by $`U=z_1+\cdots+z_a`$ on $`B_a=\mathbb{k}[z_1,\ldots,z_a]/(z_i^2)`$ from degree $`q`$ to $`q+1`$ is injective if $`q<a/2`$ and surjective if $`q\geq(a-1)/2`$.

<!-- end lemma-5 -->

<a id="proof-6"></a>

**Proof.**

The matrices have integer entries, so it suffices to prove their ranks over $`\mathbb R`$. Give the squarefree monomial basis the orthonormal inner product and let $`D=U^{\mathsf T}`$ be the operator that removes one variable. On degree $`q`$, the commutator satisfies $`DU-UD=(a-2q)\mathrm{id}`$. If $`Uv=0`$ and $`q<a/2`$, then
```math
(a-2q)\lVert v\rVert^2=-\lVert Dv\rVert^2,
```
forcing $`v=0`$. Complementation of subsets identifies the transpose of the degree-$`q`$ raising map with the degree-$`(a-q-1)`$ raising map; the injectivity just proved gives the stated surjectivity. The cases involving zero graded components are immediate. $`\square`$

<!-- end proof-6 -->

<a id="proof-7"></a>

**Proof of the positive assertions in Theorem [1.1](#label-thm-main).**

Order the monomial bases by their $`x`$-support cardinality. The $`y`$ part of $`L`$ preserves the support $`S`$, and the $`x`$ part increases its cardinality by one. Thus the multiplication matrix is block triangular, with diagonal blocks indexed by faces $`S\in\Delta`$. For $`s=|S|`$, that block is the Boolean raising map in $`n-s`$ variables, from degree $`i-s`$ to degree $`i+1-s`$. A finite block triangular map is injective, or surjective, if all its diagonal blocks have the corresponding property.

If $`r\leq1`$, only $`s=0,1`$ occur. For $`n=2m`$ these diagonal blocks are all injective when $`i\leq m-1`$ and all surjective when $`i\geq m`$. For $`n=2m+1`$ they are all injective when $`i\leq m`$ and all surjective when $`i\geq m+1`$, by Lemma [4.1](#label-lem-boolean).

Finally suppose $`n=2m+1`$ and $`r\leq2`$. The additional $`s=2`$ blocks are Boolean raising maps in $`2m-1`$ variables with a degree shift of two. They too are injective for $`i\leq m`$ and surjective for $`i\geq m+1`$; at $`i=m+1`$ the underlying Boolean map is bijective. Thus all maps have maximal rank in precisely the stated positive cases. $`\square`$

<!-- end proof-7 -->

## 5. Strong Lefschetz classification

We first recall the all-powers version of Lemma [4.1](#label-lem-boolean), including a proof.

<a id="lemma-6"></a>

**Lemma 5.1.**

<a id="label-lem-booleanpowers"></a>

In characteristic zero, $`U^k:(B_a)_q\to(B_a)_{q+k}`$ is injective if $`2q+k\leq a`$ and surjective if $`2q+k\geq a`$.

<!-- end lemma-6 -->

<a id="proof-8"></a>

**Proof.**

As before it suffices to work over $`\mathbb R`$. If $`Dv=0`$ and $`v`$ has degree $`b\leq a/2`$, the commutator identity gives
```math
D U^jv=j(a-2b-j+1)U^{j-1}v.
```
Taking inner products shows that $`U^jv\ne0`$ for $`0\leq j\leq a-2b`$ when $`v\ne0`$, and that $`U^{a-2b+1}v=0`$. For $`b\leq a/2`$, decompose $`(B_a)_b`$ orthogonally as $`U(B_a)_{b-1}\oplus\ker D`$. Choose an orthogonal basis for each such primitive space. Its iterated images form strings supported on the symmetric interval $`[b,a-b]`$. The commutator identity and adjointness show that different strings are orthogonal wherever they coexist: move powers of $`U`$ to the other side as powers of $`D`$, and use either primitive orthogonality or $`Dv=0`$. These strings span degree by degree, using the orthogonal decomposition in the lower half and surjectivity from Lemma [4.1](#label-lem-boolean) in the upper half. On each string $`U`$ advances one position. Since all strings have center $`a/2`$, the asserted injectivity and surjectivity for $`U^k`$ follow. $`\square`$

<!-- end proof-8 -->

<a id="proof-9"></a>

**Proof of Theorem [1.2](#label-thm-slp).**

Suppose first that $`r\leq1`$. Apply the support filtration from the WLP proof to $`L^k:{A_{\Delta}}_i\to{A_{\Delta}}_{i+k}`$. The diagonal block for $`s=0`$ is injective when $`2i+k\leq n`$ and surjective when $`2i+k\geq n`$. For $`s=1`$, the corresponding conditions are $`2i+k\leq n+1`$ and $`2i+k\geq n+1`$. The integer $`2i+k`$ is either at most $`n`$ or at least $`n+1`$, so all blocks have the same required rank property. This proves SLP; the graph case also follows from [\[2, Proposition 3.2\]](#ref-HN).

The negative WLP cases already imply failure of SLP. It remains to treat $`n=2m+1`$ with $`r=2`$, so $`m\geq1`$. In $`{A_{\Delta}}_m`$, the nonzero element
```math
f=\prod_{j=1}^{m}(z_{2j-1}-z_{2j})
```
satisfies $`Lf=z_n f`$ and $`L^2f=0`$. Thus $`L^2:{A_{\Delta}}_m\to{A_{\Delta}}_{m+2}`$ is noninjective.

Choose a two-element face $`C`$. Pair $`2m-2`$ of the vertices outside $`C`$, leaving one vertex $`v`$ unpaired. Let $`g`$ be the polynomial in the proof of Lemma [3.2](#label-lem-cokernel) for this pairing and face. It has degree $`m+1`$, satisfies $`Dg=0`$, and involves neither $`x_v`$ nor $`y_v`$. Hence $`h=y_vg`$ is a nonzero sum of surviving monomials of degree $`m+2`$ and
```math
D^2h=D^2(y_vg)=2Dg+y_vD^2g=0.
```
The transpose of $`L^2`$ in monomial bases is $`D^2`$, because this holds for each consecutive multiplication map. Therefore $`L^2:{A_{\Delta}}_m\to{A_{\Delta}}_{m+2}`$ is also nonsurjective. The witnesses work in every characteristic. Lemma [2.1](#label-lem-general) completes the proof. $`\square`$

<!-- end proof-9 -->

## 6. Verification and scope

The proofs use no finite classification or computation. The accompanying script `verify.py` checks the multiplication and differentiation witnesses with exact integer arithmetic and verifies rational matrix ranks for all labelled graphs on at most four vertices. It also checks selected larger graphs, including complete graphs with a triangle removed. The results and fixed random seed are recorded in `verification.json`. These calculations are ancillary checks rather than a component of the proof.

The theorem concerns the specified square-zero Artinian reductions. It does not claim a classification for arbitrary monomial powers, arbitrary Artinian reductions, or all very well-covered graphs. The latter class is strictly broader than fully whiskered graphs, and the independent-set criterion can fail there; see [\[2, Example 3.18\]](#ref-HN).

## References

<a id="ref-CFHNV"></a>

**\[1\]** S. M. Cooper, S. Faridi, T. Holleben, L. Nicklasson and A. Van Tuyl, *The weak Lefschetz property of whiskered graphs*, in *Lefschetz Properties: Current and New Directions*, Springer INdAM Series **59** (2024), 97–110. [doi:10.1007/978-981-97-3886-1_5](https://doi.org/10.1007/978-981-97-3886-1_5); [arXiv:2306.04393](https://arxiv.org/abs/2306.04393).

<a id="ref-HN"></a>

**\[2\]** T. Holleben and L. Nicklasson, *Roller Coaster Gorenstein algebras and Koszul algebras failing the weak Lefschetz property*, Journal of Pure and Applied Algebra **230** (2026), article 108238. [doi:10.1016/j.jpaa.2026.108238](https://doi.org/10.1016/j.jpaa.2026.108238); [arXiv:2502.00155](https://arxiv.org/abs/2502.00155).

<a id="ref-Zeng"></a>

**\[3\]** Z. Zeng, *The Whiskered-Graph Weak Lefschetz Conjecture for Graphs on Eight Vertices*, SSRN preprint, posted September 3, 2026. [doi:10.2139/ssrn.7385138](https://doi.org/10.2139/ssrn.7385138).
