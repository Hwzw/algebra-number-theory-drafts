# Complement transfer and density bounds for one-sided restricted sumsets

September 9, 2026

## Abstract

Let $`A,B\subseteq\mathbb F_p`$ be nonempty, with $`|B|\le |A|`$, and forbid at most one pair in each $`B`$-column of $`A\times B`$. We prove that the remaining sums number at least $`|A|+|B|-3`$ whenever $`|A|+2|B|\le p`$ and $`|B|\le cp`$, where $`c=3520^{-145200}/206`$. In particular, an absolute linear size condition $`|A|+C|B|<p`$ suffices. This gives an affirmative answer to the existence-of-a-constant question preceding Ouyang’s one-sided restricted-sumset conjecture. A complement transfer first reduces a hypothetical counterexample to one whose larger complementary set has at least half the available elements. Deleting the endpoints of unique representations then permits a high-density inverse theorem in the unbalanced case; small-doubling rectification handles the comparable case. We also obtain the bound under $`p\ge10|B|`$ and $`103|B|\le\lceil\log_2p\rceil`$. The sharp conjecture without a sparsity restriction on $`B`$ remains open.

## 1. Introduction

For nonempty finite subsets $`A,B`$ of an abelian group and a relation $`\mathcal R\subseteq A\times B`$, write
```math
A+_{\mathcal R}B=\{a+b:a\in A,\ b\in B,\ (a,b)\notin\mathcal R\}.
```
The relation is *one-sided of degree at most one* if each $`b\in B`$ belongs to at most one pair in $`\mathcal R`$. No degree bound is imposed at $`A`$. Such a relation need not be a matching.

Lev’s study of mapping restrictions [\[3\]](#ref-Lev2000) shows why the classical Erdős–Heilbronn bound does not extend to arbitrary maps without size assumptions. Ouyang [\[5\]](#ref-Ouyang) establishes the degree-one bound with hypotheses $`|A|+|B|\le(1-\varepsilon)p`$ and $`|B|\le c_\varepsilon p`$. Immediately before Conjecture 1.13, he asks for a bound under a linear size condition with an absolute coefficient on $`|B|`$. His conjecture predicts that $`|A|+2|B|\le p`$ suffices. The following theorem retains this boundary when the smaller summand has sufficiently small absolute density.

<a id="theorem-1"></a>

**Theorem 1.**

<a id="label-thm-density"></a>

Set
```math
c=\frac{3520^{-145200}}{206}.
```
Let $`p`$ be prime and let $`A,B\subseteq\mathbb F_p`$ be nonempty. Suppose
```math
b:=|B|\le a:=|A|,\qquad a+2b\le p,\qquad b\le cp.
```
For every relation $`\mathcal R\subseteq A\times B`$ of degree at most one on $`B`$,
```math
|A+_{\mathcal R}B|\ge a+b-3.
```

<!-- end theorem-1 -->

<a id="corollary-1"></a>

**Corollary 2.**

<a id="label-cor-linear"></a>

With the absolute integer $`C=206\cdot3520^{145200}`$, the conclusion of Theorem [1](#label-thm-density) holds whenever $`1\le|B|\le|A|`$ and $`|A|+C|B|<p`$.

<!-- end corollary-1 -->

<a id="proof-1"></a>

**Proof.**

Since $`C>2`$ and $`C=1/c`$, the stated conditions imply both $`a+2b\le p`$ and $`b<cp`$. $`\square`$

<!-- end proof-1 -->

The constant is very small and is not optimized. The qualitative existence of a suitable $`c`$ has a shorter proof by combining the complement transfer below with Ouyang’s existing finite-field theorem; we include that deduction to distinguish it from the quantitative argument. The explicit bound in Theorem [1](#label-thm-density) uses Grynkiewicz’s inverse theorem [\[2\]](#ref-Grynkiewicz) and Green–Ruzsa rectification [\[1\]](#ref-GR). A second consequence uses cardinality rectification instead.

<a id="theorem-2"></a>

**Theorem 3.**

<a id="label-thm-log"></a>

Let $`p,A,B,\mathcal R`$ satisfy the nonemptiness, ordering, degree, and boundary assumptions of Theorem [1](#label-thm-density). Its conclusion also holds if
```math
p\ge10b,\qquad 103b\le\lceil\log_2p\rceil.
```

<!-- end theorem-2 -->

The logarithmic bound can give a much smaller explicit threshold for a fixed number of columns. It is a quantitative companion to the positive-density theorem, not a separate asymptotic resolution. Neither theorem covers all of Ouyang’s Conjecture 1.13.

## 2. Complement transfer

<a id="lemma-1"></a>

**Lemma 4.**

<a id="label-lem-dual"></a>

Let $`G`$ be a finite abelian group of order $`N`$. Suppose $`A+_{\mathcal R}B\subseteq S\subsetneq G`$, and put $`D=G\setminus S`$. Define a relation on $`D\times(-B)`$ by
```math
\mathcal R^*=\{(d,-b):d\in D,\ b\in B,\ d-b\in A\}.
```
Its degree at $`-b`$ is at most the degree of $`\mathcal R`$ at $`b`$, and
```math
D+_{\mathcal R^*}(-B)\subseteq G\setminus A.
```
If $`|S|=|A|+|B|-q-1`$, then
```math
|G\setminus A|=|D|+|B|-q-1.
```

<!-- end lemma-1 -->

<a id="proof-2"></a>

**Proof.**

For fixed $`b`$, every $`d\in D`$ with $`d-b\in A`$ corresponds injectively to the forbidden pair $`(d-b,b)\in\mathcal R`$, since its sum is outside $`S`$. This proves the degree assertion. A pair $`(d,-b)`$ is allowed precisely when $`d-b\notin A`$, proving the inclusion. The cardinality identity follows from $`|D|=N-|S|`$. $`\square`$

<!-- end proof-2 -->

Thus a counterexample to a lower bound with loss $`q`$ transfers to one with the same loss and one-sided degree bound. In the degree-one problem, enlarge a putative counterexample to a set $`S`$ of size $`a+b-4`$. Under $`a+2b\le p`$, its complement has size $`d\ge b+4`$, while

<a id="label-eq-normalization"></a>

```math
\tag{1}
 a+d=p-b+4.
```

If necessary, apply Lemma [4](#label-lem-dual) to interchange $`A,D`$ and replace $`B`$ by $`-B`$. We may therefore assume

<a id="label-eq-ordered"></a>

```math
\tag{2}
 b\le a\le d,\qquad d\ge b+4,\qquad
 \rho(y):=|D\cap(A+y)|\le1\quad(y\in B).
```

The new relation may differ from the original relation, but it remains one-sided of degree at most one, and its allowed sumset has size at most $`a+b-4`$ with the new value of $`a`$. We use this normalization only within a contradiction argument.

<a id="proposition-1"></a>

**Proposition 5.**

<a id="label-prop-qualitative"></a>

There exists an absolute $`c_0>0`$ such that the conclusion of Theorem [1](#label-thm-density) holds for $`b\le c_0p`$.

<!-- end proposition-1 -->

<a id="proof-3"></a>

**Proof.**

Take $`c_0=\min(1/16,c_{1/4})`$, using the constant in [\[5, Corollary 1.8(i)\]](#ref-Ouyang). The cases $`b\le3`$ follow from the elementary argument below. For $`b\ge4`$, normalize a counterexample as in [(1)](#label-eq-normalization)–[(2)](#label-eq-ordered). Then
```math
a+b\le\frac{p+b+4}{2}\le\frac p2+b\le\frac{9p}{16}<\frac{3p}{4}.
```
Extend the relation to the graph of a function $`B\to A`$ by filling any empty forbidden column. This can only shrink the allowed sumset. Ouyang’s corollary, with $`\varepsilon=1/4`$, now contradicts the counterexample. $`\square`$

<!-- end proof-3 -->

For completeness, the degree-one bound when $`b=1`$ or $`2`$ follows by retaining a single column, which gives at least $`a-1`$ sums. If $`b=3`$ and the allowed sumset had size at most $`a-1`$, every column would have exactly that same set of $`a-1`$ surviving sums; call it $`S`$. Thus $`S-B\subseteq A`$. Cauchy–Davenport gives $`|S-B|\ge\min(p,a+1)=a+1`$, a contradiction. Here $`a+6\le p`$ ensures the last equality.

## 3. An inverse theorem after deleting unique representations

We use the following version of [\[2, Theorem 1.4\]](#ref-Grynkiewicz). If $`U,V\subseteq\mathbb F_p`$ are nonempty, $`U+V\ne\mathbb F_p`$, and
```math
r=|U+V|-|U|-|V|,\qquad
 \min(|U|,|V|)\ge100(r+3),\qquad
 p-|U+V|\ge r+3,
```
then both summands lie in arithmetic progressions of lengths at most their respective cardinalities plus $`r+1`$. This follows by ordering the summands in the cited theorem. Its high-density hypothesis is essential here.

<a id="lemma-2"></a>

**Lemma 6.**

<a id="label-lem-unbalanced"></a>

There is no normalized counterexample satisfying [(1)](#label-eq-normalization)–[(2)](#label-eq-ordered) with $`b\ge4`$, $`p\ge10b`$, and $`a\ge102b`$.

<!-- end lemma-2 -->

<a id="proof-4"></a>

**Proof.**

Let $`z`$ and $`u`$ be the numbers of residues $`y`$ with $`\rho(y)=0`$ and $`\rho(y)=1`$, respectively. In particular, $`z+u\ge b`$. Pollard’s theorem [\[6\]](#ref-Pollard), at level $`2`$ for $`D`$ and $`-A`$, gives
```math
2p-2z-u=\sum_y\min(2,\rho(y))
 \ge2(a+d-2)=2(p-b+2).
```
Consequently

<a id="label-eq-zu"></a>

```math
\tag{3}
 2z+u\le2b-4,\qquad z\le b-4,\qquad u\ge4.
```

Delete from $`D`$ every endpoint of a unique representation $`y=d-x`$, $`d\in D`$, $`x\in A`$. Let $`k`$ be the number of deleted elements and let $`D'`$ be the remaining set. Since there are $`u`$ unique representations, $`k\le u`$. All $`z+u`$ missing or unique differences are now absent from $`D'-A`$. If
```math
r'=|D'-A|-|D'|-a,
```
then Cauchy–Davenport and the deletion estimate give

<a id="label-eq-excess"></a>

```math
\tag{4}
 -1\le r'\le b-4+k-z-u\le b-4-z.
```

The sets to which we apply the inverse theorem are nonempty, since
```math
|D'|\ge d-u\ge a-(2b-4)\ge100b+4.
```
Thus both $`|D'|`$ and $`a`$ exceed $`100(r'+3)`$; also $`p-|D'-A|\ge z+u\ge b\ge r'+3`$. The cited inverse theorem places $`A`$ in a progression of length $`m=a+h`$ with

<a id="label-eq-holes"></a>

```math
\tag{5}
 0\le h\le r'+1\le b-3-z.
```

After dilation and translation, write $`A=I\setminus H`$, where $`I=[0,m-1]\subseteq\mathbb F_p`$ and $`|H|=h`$. Common dilation and the corresponding translations of $`D,B`$ preserve the difference counts in [(2)](#label-eq-ordered).

For a set $`X`$ and a residue $`y`$, put
```math
\partial_X(y)=|(X+y)\setminus X|.
```
Write $`\delta=b-4`$. If $`z>0`$, translate $`D`$ and $`B`$ so that a missing difference becomes zero. The sets $`D,A`$ are then disjoint, so
```math
D=\mathbb F_p\setminus(A\cup T),\qquad T\subseteq\mathbb F_p\setminus A,
 \qquad |T|=\delta.
```
For $`y\in B`$, this yields
```math
\rho(y)=\partial_A(y)-|T\cap(A+y)|\le1,
 \qquad \partial_A(y)\le\delta+1.
```
If $`z=0`$, use a unique difference instead; such a difference exists by [(3)](#label-eq-zu). After translation $`D\cap A=\{x\}`$ for some $`x`$, and
```math
D=\{x\}\cup\bigl(\mathbb F_p\setminus(A\cup T)\bigr),
 \qquad T\subseteq\mathbb F_p\setminus A,\quad |T|=\delta+1.
```
The same counting identity, with an additional nonnegative term for $`x\in A+y`$, gives $`\partial_A(y)\le\delta+2`$. In either case

<a id="label-eq-boundary"></a>

```math
\tag{6}
 \partial_A(y)\le b-2\quad(y\in B).
```

Removing $`h`$ elements from an interval can decrease this boundary by at most $`h`$: every point of $`(I+y)\setminus I`$ remains in $`(A+y)\setminus A`$ unless it belongs to $`H+y`$. Hence $`\partial_A(y)\ge\partial_I(y)-h`$. For $`0\le y<p`$, direct interval intersection gives
```math
\partial_I(y)=\min(y,p-y,m,p-m).
```
Set $`L=b-2+h\le2b-5`$. By [(6)](#label-eq-boundary), every $`y\in B`$ has $`\partial_I(y)\le L`$. We have $`m\ge a\ge102b>L`$, and
```math
p-m=d+b-4-h\ge d-1+z\ge\frac{p-b+2}{2}
 >4b-10\ge2L.
```
It follows that all elements of $`B`$ have integer representatives in $`[-L,L]`$. Use these representatives and those of $`A`$ in $`[0,m-1]`$. Their entire integer sumset is contained in $`[-L,m-1+L]`$, an interval with $`m+2L<p`$ elements. Reduction modulo $`p`$ is injective on it, and therefore preserves the size of the restricted sumset and the forbidden relation.

Ouyang’s integer theorem [\[5, Theorem 1.5(i)\]](#ref-Ouyang), at degree one, now gives at least $`a+b-3`$ allowed sums, contradicting the normalization. $`\square`$

<!-- end proof-4 -->

## 4. Rectification when the sizes are comparable

Recall that a Freiman isomorphism of order two is an injective map preserving, in both directions, equalities between two-term sums. Applied to $`A\cup B`$, it preserves the cardinality of every restricted sumset, after transferring the relation through its coordinate restrictions. Overlap between $`A`$ and $`B`$ causes no difficulty.

<a id="lemma-3"></a>

**Lemma 7.**

<a id="label-lem-doubling"></a>

Suppose $`1\le b\le a<102b`$, the degree of $`\mathcal R`$ at $`B`$ is at most one, and $`|A+_{\mathcal R}B|\le a+b-4`$. For $`T=A\cup B`$,
```math
|T|<103b,\qquad |T+T|<110|T|.
```

<!-- end lemma-3 -->

<a id="proof-5"></a>

**Proof.**

Put $`M=|A+B|`$. There are at most $`b`$ forbidden pairs. Each sum outside $`A+_{\mathcal R}B`$ is the sum of at least one such pair, so
```math
M\le a+2b-4<a+2b.
```
The Plünnecke inequality gives $`|2A|\le M^2/b`$ and $`|2B|\le M^2/a`$. More explicitly, choose a nonempty $`X\subseteq B`$ minimizing $`|X+A|/|X|`$. Petridis’ inequality, in the form of [\[2, Theorem 2.4\]](#ref-Grynkiewicz), gives
```math
|2A|\le|X+2A|\le(M/b)^2|X|\le M^2/b.
```
The other estimate follows by interchanging $`A,B`$. Since $`2T=2A\cup(A+B)\cup2B`$ and $`|T|\ge a`$, the ratio $`t=a/b\in[1,102)`$ satisfies
```math
\frac{|2T|}{|T|}
 \le\frac{M^2/b+M+M^2/a}{a}
 <t+6+\frac{10}{t}+\frac4{t^2}<110.
```
For the last inequality, the function on the right is convex on the positive real axis; its values at $`1`$ and $`102`$ are $`21`$ and $`108+10/102+4/102^2`$, both below $`110`$. Finally $`|T|\le a+b<103b`$. $`\square`$

<!-- end proof-5 -->

<a id="proof-6"></a>

**Proof of Theorem [1](#label-thm-density).**

The cases $`b\le3`$ were handled in Section 2. For $`b\ge4`$, assume a counterexample and normalize it by complement transfer. Since $`c<1/10`$, we have $`p\ge10b`$. Lemma [6](#label-lem-unbalanced) excludes $`a\ge102b`$, so Lemma [7](#label-lem-doubling) applies to the transformed pair. It gives
```math
|T+T|<110|T|,\qquad
 |T|<103b\le\frac12\,3520^{-145200}p.
```
Green and Ruzsa [\[1, Theorem 1.3\]](#ref-GR) prove that a subset of $`\mathbb F_p`$ with doubling ratio $`K`$ is Freiman-isomorphic to an integer set when its density is at most $`(32K)^{-12K^2}`$. This threshold decreases for $`K\ge1`$, and $`32\cdot110=3520`$, $`12\cdot110^2=145200`$. The theorem therefore rectifies $`T`$. Transfer the forbidden relation to the integer images of $`A,B`$ and apply [\[5, Theorem 1.5(i)\]](#ref-Ouyang). The resulting lower bound $`a+b-3`$ contradicts the assumed counterexample. $`\square`$

<!-- end proof-6 -->

<a id="proof-7"></a>

**Proof of Theorem [3](#label-thm-log).**

Normalize a counterexample with $`b\ge4`$ as before. Lemma [6](#label-lem-unbalanced) again gives $`a<102b`$, so
```math
|A\cup B|<103b\le\lceil\log_2p\rceil.
```
Lev’s rectification theorem [\[4, Theorem 1\]](#ref-Lev2008), at order two, makes $`A\cup B`$ Freiman-isomorphic to an integer set. The same integer restricted-sumset bound gives the contradiction. The cases $`b\le3`$ remain elementary. $`\square`$

<!-- end proof-7 -->

## 5. Scope and further questions

The proof isolates two operations that may be useful in sharper density questions: complement transfer preserves a one-sided degree condition exactly, and endpoint deletion converts low representation counts into small excess in an unrestricted difference set. The latter operation is particularly efficient at degree one. For larger degrees, deleting endpoints of low-multiplicity differences need not leave an excess small enough for the inverse theorem used here.

The complement lemma itself works for every fixed degree and every loss parameter $`q`$. It does not preserve a degree bound at the other summand, so it cannot automatically transfer results whose hypotheses require a matching. The quantitative proof depends on the existing inverse theorem and rectification bounds; improving those inputs or treating comparable summands at higher density could improve the absolute constant.

The remaining sharp question is whether $`a+2b\le p`$ alone suffices. The results here resolve the weaker existence-of-an-absolute-linear-coefficient question, not that full conjecture. The earlier logarithmic and the positive-density conclusions are two bounds in this single investigation.

**Preparation.**

This manuscript was prepared with OpenAI Codex assistance. Proof checking recorded with the manuscript is internal; no independent human peer review is claimed.

## References

<a id="ref-GR"></a>

**\[1\]** B. Green and I. Z. Ruzsa, *Sets with small sumset and rectification*, Bull. London Math. Soc. **38** (2006), 43–52. [doi:10.1112/S0024609305018102](https://doi.org/10.1112/S0024609305018102). Author version: [arXiv:math/0403338v2](https://arxiv.org/abs/math/0403338).

<a id="ref-Grynkiewicz"></a>

**\[2\]** D. J. Grynkiewicz, *The $`3k-4`$ Theorem modulo a Prime: High Density for $`A+B`$*, Mathematika **71** (2025), e70030. [doi:10.1112/mtk.70030](https://doi.org/10.1112/mtk.70030). Author version: [arXiv:2402.15028v1](https://arxiv.org/abs/2402.15028).

<a id="ref-Lev2000"></a>

**\[3\]** V. F. Lev, *Restricted set addition in groups, II. A generalization of the Erdős–Heilbronn conjecture*, Electron. J. Combin. **7** (2000), R4. [Journal article](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v7i1r4).

<a id="ref-Lev2008"></a>

**\[4\]** V. F. Lev, *The rectifiability threshold in abelian groups*, Combinatorica **28** (2008), 491–497. [doi:10.1007/s00493-008-2299-8](https://doi.org/10.1007/s00493-008-2299-8).

<a id="ref-Ouyang"></a>

**\[5\]** M. Ouyang, *On restricted sumsets with bounded degree relations*, Mathematika **71** (2025), e70045. [doi:10.1112/mtk.70045](https://doi.org/10.1112/mtk.70045). Revised author version: [arXiv:2503.09121v3](https://arxiv.org/abs/2503.09121v3).

<a id="ref-Pollard"></a>

**\[6\]** J. M. Pollard, *A generalisation of the theorem of Cauchy and Davenport*, J. London Math. Soc. (2) **8** (1974), 460–462. [doi:10.1112/jlms/s2-8.3.460](https://doi.org/10.1112/jlms/s2-8.3.460).
