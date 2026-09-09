# Counterexamples to a conjecture on one-sided restricted sumsets

September 8, 2026

## Abstract

For finite integer sets $`A,B`$ and a forbidden relation $`R\subseteq A\times B`$, let $`A\mathbin{+_{R}}B`$ be the set of sums represented by pairs outside $`R`$. Ouyang conjectured that, when $`|B|\leq |A|`$ and every vertex of $`B`$ has forbidden degree at most $`\Delta`$, one has $`|A\mathbin{+_{R}}B|\geq |A|+|B|-1-\lfloor 5\Delta/2\rfloor`$. We give explicit counterexamples for every $`\Delta=3k`$, $`k\geq1`$. For every $`N\geq14k`$, our sets have cardinality $`N`$ and restricted sumset cardinality $`2N-8k-1`$, falling below the conjectured bound by $`\lceil k/2\rceil`$. Consequently a universal linear loss coefficient must be at least $`8/3`$. For $`\Delta=3`$ and equal summand sizes $`N\geq14`$, the construction attains the known lower bound $`2N-9`$, and hence determines the exact minimum.

## 1. Introduction

Let $`A,B\subseteq\mathbb Z`$ be finite, nonempty sets and let $`R\subseteq A\times B`$. The restricted sumset associated with the forbidden relation $`R`$ is
```math
A\mathbin{+_{R}}B=\{a+b:a\in A,\ b\in B,\ (a,b)\notin R\}.
```
For $`b\in B`$, put $`d_R(b)=|\{a\in A:(a,b)\in R\}|`$. We consider the one-sided condition $`d_R(b)\leq\Delta`$ for all $`b\in B`$. Degrees on $`A`$ are unrestricted.

Ouyang proved that, if $`|B|\leq|A|`$ and the one-sided degree condition holds, then

<a id="label-eq-known"></a>

```math
\tag{1}
 |A\mathbin{+_{R}}B|\geq |A|+|B|-3\Delta
```

[\[1, Theorem 1.5(i)\]](#ref-Ouyang). Motivated by a construction in [\[1, Theorem 1.9\]](#ref-Ouyang), Ouyang proposed the stronger inequality

<a id="label-eq-conjecture"></a>

```math
\tag{2}
 |A\mathbin{+_{R}}B|\geq |A|+|B|-1-\left\lfloor\frac{5\Delta}{2}\right\rfloor
```

[\[1, Conjecture 1.10\]](#ref-Ouyang). All numbered references to that paper refer to its September 4, 2025 author version, arXiv:2503.09121v3.

We disprove [(2)](#label-eq-conjecture) by a family whose forbidden degree is unbounded. The construction uses an interval with three holes as $`A`$, an interval as $`B`$, and four intervals of deleted sums. The holes near the endpoints of $`A`$ control the degree when both interior intervals of deleted sums meet the same translate of $`A`$. Exact intersection counts show that the resulting degree is at most $`3k`$, while the loss from $`|A|+|B|-1`$ is $`8k`$.

Throughout, $`[x,y]`$ denotes the integer interval $`\{x,x+1,\ldots,y\}`$ for integers $`x\leq y`$.

<a id="theorem-1"></a>

**Theorem 1.**

<a id="label-thm-construction"></a>

Let $`k,N,U`$ be integers satisfying

<a id="label-eq-parameters"></a>

```math
\tag{3}
 k\geq1,\qquad N\geq14k,\qquad 8k\leq U\leq N-6k.
```

Define
```math
\begin{align*}
 A={}&[0,N+4k-1]\setminus\bigl([k,2k-1]\cup[U,U+2k-1]\\[-2pt]
 &\hspace{43mm}\cup[N+2k,N+3k-1]\bigr),\\
 B={}&[0,N-1],
\end{align*}
```
and put
```math
\begin{align*}
 D_0&=[0,4k-1],& D_1&=[U,U+2k-1],\\
 D_2&=[U+N-1,U+N+2k-2],&
 D_3&=[2N-1,2N+4k-2].
\end{align*}
```
Let $`D=D_0\cup D_1\cup D_2\cup D_3`$ and
```math
R=\{(a,b)\in A\times B:a+b\in D\}.
```
Then
```math
\begin{gather*}
 |A|=|B|=N,\qquad \max_{b\in B}d_R(b)=3k,\\
 A\mathbin{+_{R}}B=[0,2N+4k-2]\setminus D,\qquad
 |A\mathbin{+_{R}}B|=2N-8k-1.
\end{gather*}
```

<!-- end theorem-1 -->

<a id="corollary-1"></a>

**Corollary 2.**

<a id="label-cor-failure"></a>

Conjecture 1.10 of [\[1\]](#ref-Ouyang) is false. For each $`k\geq1`$, Theorem [1](#label-thm-construction) gives examples with $`\Delta=3k`$ whose restricted sumset has $`\lceil k/2\rceil`$ fewer elements than the proposed lower bound.

<!-- end corollary-1 -->

<a id="proof-1"></a>

**Proof.**

The proposed lower bound is $`2N-1-\lfloor15k/2\rfloor`$, whereas the actual cardinality is $`2N-8k-1`$. Their difference is
```math
8k-\left\lfloor\frac{15k}{2}\right\rfloor
 =\left\lceil\frac{k}{2}\right\rceil>0.
```
$`\square`$

<!-- end proof-1 -->

<a id="corollary-2"></a>

**Corollary 3.**

<a id="label-cor-coefficient"></a>

Suppose real constants $`c,K`$, independent of $`A,B,\Delta`$, satisfy
```math
|A\mathbin{+_{R}}B|\geq |A|+|B|-1-c\Delta-K
```
for all finite, nonempty $`A,B\subseteq\mathbb Z`$ with $`|B|\leq|A|`$ and all relations of degree at most $`\Delta`$ on $`B`$. Then $`c\geq8/3`$.

<!-- end corollary-2 -->

<a id="proof-2"></a>

**Proof.**

Apply Theorem [1](#label-thm-construction) with $`N=14k`$ and $`U=8k`$. The claimed universal bound implies $`8k\leq3ck+K`$. Divide by $`k`$ and let $`k`$ tend to infinity. $`\square`$

<!-- end proof-2 -->

## 2. Proof of the construction

<a id="proof-3"></a>

**Proof of Theorem [1](#label-thm-construction).**

The three holes in $`A`$ are disjoint and have total cardinality $`4k`$. Hence $`|A|=N`$, and clearly $`|B|=N`$. Both endpoints $`0`$ and $`N+4k-1`$ belong to $`A`$. The largest difference between consecutive elements of $`A`$ is $`2k+1\leq N`$. Thus the intervals $`a+B=[a,a+N-1]`$, as $`a`$ runs through $`A`$ in increasing order, overlap or are adjacent. It follows that

<a id="label-eq-full"></a>

```math
\tag{4}
 A+B=[0,2N+4k-2].
```

The parameter inequalities imply that $`D_0,D_1,D_2,D_3`$ are disjoint, lie in this interval, and have lengths $`4k,2k,2k,4k`$, respectively. Consequently $`|D|=12k`$.

It remains to prove the degree assertion. For $`b\in B`$, define
```math
d_i(b)=|(A+b)\cap D_i|\quad(0\leq i\leq3),\qquad
 d(b)=\sum_{i=0}^3d_i(b)=d_R(b).
```
The interval $`D_0`$ can contribute only when $`0\leq b\leq4k-1`$, and $`D_3`$ can contribute only when $`N-4k\leq b\leq N-1`$. The two interior intervals can both contribute only when
```math
U-4k\leq b\leq U+2k-1.
```
Indeed, meeting $`D_2`$ requires $`N+4k-1+b\geq U+N-1`$, while meeting $`D_1`$ requires $`b\leq U+2k-1`$. The three ranges

<a id="label-eq-ranges"></a>

```math
\tag{5}
 [0,4k-1],\qquad [U-4k,U+2k-1],\qquad [N-4k,N-1]
```

are pairwise disjoint: $`U-4k\geq4k`$ and $`U+2k-1\leq N-4k-1`$. Outside their union, neither endpoint interval contributes and at most one interior interval contributes. Its length is $`2k`$, so $`d(b)\leq2k`$ there.

*The left endpoint range.* Suppose $`0\leq b\leq4k-1`$. Only $`D_0`$ and $`D_1`$ contribute. The first count is the number of elements in $`[0,4k-1-b]`$ after removing $`[k,2k-1]`$. The second is the number of elements of $`A`$ in $`[U-b,U+2k-1-b]`$. This interval can meet the central hole $`[U,U+2k-1]`$ but no other hole. Direct counting gives

<a id="label-eq-lefttable"></a>

```math
\tag{6}
\begin{array}{c|c|c|c}
 \text{range of }b&d_0(b)&d_1(b)&d(b)\\\hline
 0\leq b\leq2k-1&3k-b&b&3k\\
 2k\leq b\leq3k-1&k&2k&3k\\
 3k\leq b\leq4k-1&4k-b&2k&6k-b
\end{array}
```

Every entry in the last column is at most $`3k`$.

*The middle range.* Write $`b=U-4k+t`$ with $`0\leq t\leq6k-1`$. Only $`D_1`$ and $`D_2`$ contribute. To compute $`d_1(b)`$, intersect $`A`$ with
```math
D_1-b=[4k-t,6k-1-t].
```
This interval meets only the left endpoint of $`A`$ and the hole $`[k,2k-1]`$; its upper endpoint is less than $`U`$. For the second count,
```math
D_2-b=[N+4k-1-t,N+6k-2-t].
```
Set $`L=N+4k-1`$. Reflection $`x\mapsto L-x`$ takes this interval to $`[t-2k+1,t]`$. The reflected set $`L-A`$ has the endpoint hole $`[k,2k-1]`$ and its central hole begins at $`N+2k-U\geq8k`$. Since $`t\leq6k-1`$, no other hole contributes to this count. The exact intersection sizes are therefore

<a id="label-eq-middletable"></a>

```math
\tag{7}
\begin{array}{c|c|c|c}
 \text{range of }t&d_1(b)&d_2(b)&d(b)\\\hline
 0\leq t\leq k-1&2k&t+1&2k+t+1\\
 k\leq t\leq2k-1&2k&k&3k\\
 2k\leq t\leq3k-1&4k-t&k&5k-t\\
 3k\leq t\leq4k-1&k&t-2k+1&t-k+1\\
 4k\leq t\leq5k-1&k&2k&3k\\
 5k\leq t\leq6k-1&6k-t&2k&8k-t
\end{array}
```

Again every entry in the last column is at most $`3k`$.

*The right endpoint range.* The left endpoint calculation also handles this range by reflection. To make the parameter change explicit, write $`A_U,D_U`$ for the constructed sets. With
```math
U'=N+2k-U,\qquad M=2N+4k-2,
```
we have
```math
L-A_U=A_{U'},\qquad M-D_U=D_{U'},\qquad (N-1)-B=B.
```
Moreover, $`8k\leq U'\leq N-6k`$. The map
```math
(a,b)\longmapsto(L-a,N-1-b)
```
therefore carries the forbidden relation for $`U`$ to the forbidden relation for $`U'`$. For $`b\in[N-4k,N-1]`$, the new coordinate $`N-1-b`$ lies in $`[0,4k-1]`$, where [(6)](#label-eq-lefttable) applies. This proves $`d(b)\leq3k`$ in the right endpoint range.

Together these calculations establish $`d_R(b)\leq3k`$ for every $`b\in B`$. Equality holds at $`b=0`$ by [(6)](#label-eq-lefttable). Finally, by the definition of $`R`$, every representation of a sum in $`D`$ is forbidden and every representation of a sum outside $`D`$ is permitted. Using [(4)](#label-eq-full), we obtain
```math
A\mathbin{+_{R}}B=(A+B)\setminus D=[0,2N+4k-2]\setminus D.
```
Its cardinality is $`(2N+4k-1)-12k=2N-8k-1`$, as required. $`\square`$

<!-- end proof-3 -->

## 3. Exact sharpness at degree three

For completeness, we recall the elementary lower-bound argument underlying [(1)](#label-eq-known). This is the argument of [\[1, Theorem 1.5(i)\]](#ref-Ouyang).

<a id="proposition-1"></a>

**Proposition 4 (Ouyang).**

<a id="label-prop-known"></a>

Let $`A,B\subseteq\mathbb Z`$ be finite, nonempty sets, with $`|B|\leq|A|`$, and let $`\Delta\geq1`$ be an integer. If $`R\subseteq A\times B`$ has degree at most $`\Delta`$ on $`B`$, then $`|A\mathbin{+_{R}}B|\geq |A|+|B|-3\Delta`$.

<!-- end proposition-1 -->

<a id="proof-4"></a>

**Proof.**

Write $`A=\{a_1<\cdots<a_m\}`$ and $`B=\{b_1<\cdots<b_n\}`$. If $`a_1`$ has forbidden degree at most $`\Delta`$, the strictly increasing chain of sums along
```math
(a_1,b_1),\ldots,(a_1,b_n),(a_2,b_n),\ldots,(a_m,b_n)
```
has $`m+n-1`$ elements and at most $`2\Delta`$ forbidden pairs. It supplies at least $`m+n-1-2\Delta\geq m+n-3\Delta`$ permitted sums.

Otherwise, $`a_1`$ has degree at least $`\Delta+1`$. Since
```math
\sum_{a\in A}d_R(a)=\sum_{b\in B}d_R(b)\leq n\Delta\leq m\Delta,
```
there is some $`a_j`$ with $`j\geq2`$ whose degree is at most $`\Delta-1`$. Consider the chain along the first column up to $`a_j`$, then along the row of $`a_j`$, then along the last column:
```math
(a_1,b_1),\ldots,(a_j,b_1),
 (a_j,b_2),\ldots,(a_j,b_n),
 (a_{j+1},b_n),\ldots,(a_m,b_n).
```
It contains $`m+n-1`$ strictly increasing sums. The number of forbidden pairs is at most $`\Delta+(\Delta-1)+\Delta=3\Delta-1`$, since the two columns have degree at most $`\Delta`$. Thus at least $`m+n-3\Delta`$ sums remain. $`\square`$

<!-- end proof-4 -->

<a id="corollary-3"></a>

**Corollary 5.**

<a id="label-cor-exact"></a>

For every integer $`N\geq14`$,
```math
\min |A\mathbin{+_{R}}B|=2N-9,
```
where the minimum is over finite integer sets $`A,B`$ of cardinality $`N`$ and relations $`R\subseteq A\times B`$ of degree at most three on $`B`$.

<!-- end corollary-3 -->

<a id="proof-5"></a>

**Proof.**

Proposition [4](#label-prop-known) gives the lower bound. Theorem [1](#label-thm-construction), with $`k=1`$ and any $`8\leq U\leq N-6`$, attains it. $`\square`$

<!-- end proof-5 -->

For example, take $`k=1`$, $`N=20`$, and $`U=14`$. Then
```math
\begin{align*}
 A&=\{0\}\cup[2,13]\cup[16,21]\cup\{23\},\\
 B&=[0,19],\\
 D&=\{0,1,2,3,14,15,33,34,39,40,41,42\}.
\end{align*}
```
The degree sequence on $`B`$, in increasing order, is
```math
(3,3,3,3,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3).
```
The restricted sumset has $`31`$ elements, whereas [(2)](#label-eq-conjecture) requires $`32`$.

The construction leaves a gap in the possible universal leading coefficient: Corollary [3](#label-cor-coefficient) requires at least $`8/3`$, while [(1)](#label-eq-known) supplies $`3`$. We do not determine that coefficient, classify the equality cases at degree three, or assert a corresponding counterexample under a degree restriction on both sides.

## References

<a id="ref-Ouyang"></a>

**\[1\]** Minghui Ouyang, *On restricted sumsets with bounded degree relations*, Mathematika **71** (2025), no. 4, e70045. [doi:10.1112/mtk.70045](https://doi.org/10.1112/mtk.70045). Author version: [arXiv:2503.09121v3](https://arxiv.org/abs/2503.09121v3), September 4, 2025.
