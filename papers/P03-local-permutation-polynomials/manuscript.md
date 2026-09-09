# Maximum-degree local permutation polynomials over the prime field

Henry Zweiman

September 8, 2026

## Abstract

For every prime power $`q=p^r>3`$ and every positive integer $`n`$, we prove the existence of a local permutation polynomial over $`\mathbb F_q`$ with coefficients in $`\mathbb F_p`$ and total degree $`n(q-2)`$. The proof uses a subfield patch that preserves the extremal coefficient, together with an analysis of a recursive family formed from inversion and a transposition. For every nonprime odd field, we compute the extremal coefficient of that family in every arity $`n\geq2`$ by a first-order recurrence over $`\mathbb F_p`$. In particular, over every $`\mathbb F_{5^r}`$ with $`r\geq2`$, the family fails to have maximum degree among arities $`n\geq2`$ precisely when $`n`$ is congruent to $`6`$ or $`7`$ modulo $`10`$. This gives infinite families of counterexamples to the proposed maximum-degree conjecture for this recursion, while the ternary case supplies the missing construction for the uniform existence result.

## 1. Introduction and main results

A *local permutation polynomial* (LPP) over a finite field $`E=\mathbb F_q`$ is a polynomial function $`F:E^n\to E`$ that is a permutation in each variable when the other variables are fixed. We identify polynomial functions with their unique reduced representatives, whose degree in each variable is less than $`q`$. For $`q>2`$, an LPP has degree at most $`q-2`$ in each variable, and hence total degree at most $`n(q-2)`$. We call this total degree *maximum degree*.

Gutiérrez and Jiménez Urroz established unrestricted-coefficient existence and several prime-coefficient cases in [\[2,3\]](#ref-GJU-afr). Their remaining prime-coefficient existence question is answered by the following theorem.

<a id="theorem-1"></a>

**Theorem 1.**

<a id="label-thm-exist"></a>

For every prime power $`q=p^r>3`$ and every integer $`n\geq1`$, there is an LPP in $`\mathbb F_p[X_1,\ldots,X_n]`$ over $`\mathbb F_q`$ of reduced total degree $`n(q-2)`$.

<!-- end theorem-1 -->

The characteristic-two case is already known [\[2, Theorem 4\]](#ref-GJU-afr). For $`p\geq5`$, we extend prime-field examples by a patching construction that preserves the extremal coefficient. The case $`p=3`$ follows from the next result, which also describes the failure of a proposed general construction.

Let $`q>3`$, put $`I(z)=z^{q-2}`$, and let
```math
t(z)=z+\sum_{j=0}^{q-2}z^j.
```
As functions, $`I`$ inverts nonzero elements and fixes zero, while $`t`$ interchanges zero and one and fixes all other elements. Define reduced polynomial functions

<a id="label-eq-family"></a>

```math
\tag{1}
 f_1=X_1,\qquad
 f_n=t\bigl(I(f_{n-1})+I(X_n)\bigr)\quad(n\geq2).
```

Every $`f_n`$ is an LPP defined over $`\mathbb F_p`$. The assertion that this recursion always has maximum degree in odd characteristic is Conjecture 1 of both [\[2, Section 6\]](#ref-GJU-afr) and [\[3, Section 4\]](#ref-GJU-mal).

For a reduced polynomial $`F`$ in $`n`$ variables, write
```math
\operatorname{top}_q(F)=[X_1^{q-2}\cdots X_n^{q-2}]F.
```
For an LPP, maximum degree is equivalent to $`\operatorname{top}_q(F)\ne0`$.

<a id="theorem-2"></a>

**Theorem 2.**

<a id="label-thm-recurrence"></a>

Let $`q=p^r`$ with $`p`$ odd and $`r\geq2`$. Set $`C_n=\operatorname{top}_q(f_n)`$ for the family [(1)](#label-eq-family). Define $`E_k\in\mathbb F_p`$ by

<a id="label-eq-Ek"></a>

```math
\tag{2}
 E_1=2,\qquad E_{k+1}=-4E_k+4.
```

Then, for every $`k\geq1`$,

<a id="label-eq-Cn"></a>

```math
\tag{3}
 C_{2k}=E_k,\qquad C_{2k+1}=-2E_k.
```

In particular, $`f_{2k}`$ and $`f_{2k+1}`$ have maximum degree if and only if $`E_k\ne0`$. Explicitly,

<a id="label-eq-closed"></a>

```math
\tag{4}
 E_k=\begin{cases}
 \bigl(6(-4)^{k-1}+4\bigr)/5,&p\ne5,\\
 4k-2,&p=5,
 \end{cases}
```

where all quantities are interpreted in $`\mathbb F_p`$.

<!-- end theorem-2 -->

<a id="corollary-1"></a>

**Corollary 3.**

<a id="label-cor-failure"></a>

For the recursion [(1)](#label-eq-family) over $`\mathbb F_{p^r}`$, $`r\geq2`$, the following hold.

1.  If $`p=3`$, then $`C_n=2`$ for every $`n\geq2`$.

2.  If $`p=5`$, then $`f_n`$ fails to have maximum degree precisely when $`n\equiv6`$ or $`7\pmod {10}`$, for $`n\geq2`$.

3.  If $`p\geq7`$, then the failures in the paired arities $`2k,2k+1`$ occur precisely when $`(-4)^{k-1}=-2/3`$ in $`\mathbb F_p`$. Either there are no failures or the corresponding $`k`$ form one residue class modulo the multiplicative order of $`-4`$ in $`\mathbb F_p^\times`$.

<!-- end corollary-1 -->

In particular, $`q=25`$ and $`n=6`$ give a counterexample to the recursive conjecture with degree strictly smaller than $`138`$. Theorem [2](#label-thm-recurrence) classifies maximum-degree arities, rather than the precise degree when the extremal coefficient vanishes. Its hypothesis $`r\geq2`$ is essential to the coefficient-counting argument below; no classification over prime fields is asserted here. Also, $`f_1=X_1`$ is not of maximum degree for $`q>3`$, so our statements about the recursion start at arity two.

## 2. Extremal coefficients and subfield patching

We first record the coefficient functional used throughout the paper. In two variables, replacing an embedded subsquare is a form of Latin trade; see [\[1, Section 1\]](#ref-CF) for the trade viewpoint. The feature needed here is the exact preservation of a polynomial coefficient across different fields, together with Frobenius equivariance.

<a id="lemma-1"></a>

**Lemma 4.**

<a id="label-lem-coefficient"></a>

Let $`q>2`$. For every reduced polynomial function $`P:\mathbb F_q^n\to\mathbb F_q`$,

<a id="label-eq-moment"></a>

```math
\tag{5}
 \operatorname{top}_q(P)=(-1)^n\sum_{a\in\mathbb F_q^n}
 \left(\prod_{i=1}^n a_i\right)P(a).
```

If $`P`$ is an LPP, then its degree in each variable is at most $`q-2`$.

<!-- end lemma-1 -->

<a id="proof-1"></a>

**Proof.**

For a reduced univariate polynomial $`h`$, the sums of powers in $`\mathbb F_q`$ give
```math
\sum_{a\in\mathbb F_q}a h(a)=-[X^{q-2}]h.
```
Indeed, for $`0\leq j\leq q-1`$, the sum of $`a^{j+1}`$ is nonzero only for $`j=q-2`$, when it equals $`-1`$. Applying this identity one variable at a time proves [(5)](#label-eq-moment).

On a coordinate line, an LPP takes each field value once. Its sum of values is therefore zero, as $`q>2`$. For a reduced univariate polynomial this sum equals minus the coefficient of $`X^{q-1}`$. Consequently the coefficient polynomial of $`X_i^{q-1}`$ in $`P`$ vanishes on every choice of the remaining coordinates. It is reduced in those coordinates and hence is the zero polynomial. $`\square`$

<!-- end proof-1 -->

<a id="lemma-2"></a>

**Lemma 5 (Subfield patch).**

<a id="label-lem-patch"></a>

Let $`k=\mathbb F_s\subseteq E=\mathbb F_q`$ with $`s>3`$, and let $`h:k^n\to k`$ be an LPP of maximum degree. Define

<a id="label-eq-patch"></a>

```math
\tag{6}
 F(x_1,\ldots,x_n)=\begin{cases}
 h(x_1,\ldots,x_n),&(x_1,\ldots,x_n)\in k^n,\\
 x_1+\cdots+x_n,&(x_1,\ldots,x_n)\notin k^n.
 \end{cases}
```

Then $`F`$ is an LPP of maximum degree over $`E`$, and

<a id="label-eq-patchcoefficient"></a>

```math
\tag{7}
 \operatorname{top}_q(F)=\operatorname{top}_s(h).
```

If $`h`$ is equivariant under the prime-field Frobenius automorphism, then so is $`F`$, and its reduced polynomial has coefficients in the prime field.

<!-- end lemma-2 -->

<a id="proof-2"></a>

**Proof.**

Fix all coordinates except $`x_i`$. If a fixed coordinate lies outside $`k`$, the coordinate map is translation by a constant of $`E`$. Otherwise all fixed coordinates lie in $`k`$. On $`k`$ the coordinate map is a permutation of $`k`$, because $`h`$ is an LPP. On $`E\setminus k`$ it is translation by a constant in $`k`$, which permutes $`E\setminus k`$. These two parts have disjoint images, so the coordinate map permutes $`E`$.

Put $`A(x)=x_1+\cdots+x_n`$. Since $`s>3`$ and $`q\geq s`$, both $`\operatorname{top}_s(A)`$ and $`\operatorname{top}_q(A)`$ vanish: the relevant total degree is greater than one. The function $`F-A`$ is supported on $`k^n`$. Lemma [4](#label-lem-coefficient) therefore gives
```math
\operatorname{top}_q(F)=(-1)^n\sum_{a\in k^n}\left(\prod_i a_i\right)(h(a)-A(a))
 =\operatorname{top}_s(h)\ne0.
```
The degree bound in that lemma proves maximality.

Finally $`k`$ is stable under the prime-field Frobenius, and addition commutes with Frobenius. Thus [(6)](#label-eq-patch) is equivariant whenever $`h`$ is. To see that equivariance is equivalent to prime-field coefficients, write the reduced representative as $`P=\sum_\alpha c_\alpha X^\alpha`$. Its coefficientwise Frobenius conjugate is $`P^\sigma=\sum_\alpha c_\alpha^pX^\alpha`$. Equivariance and the bijectivity of Frobenius imply that $`P`$ and $`P^\sigma`$ agree at every point of $`E^n`$. Uniqueness of reduced interpolation yields $`c_\alpha^p=c_\alpha`$ for all $`\alpha`$. $`\square`$

<!-- end proof-2 -->

The patch has a direct polynomial representative. If $`h`$ denotes its reduced polynomial over $`k`$, then

<a id="label-eq-explicitpatch"></a>

```math
\tag{8}
 F=\operatorname{red}_q\left(
 A+\prod_{i=1}^n\bigl(1-(X_i^s-X_i)^{q-1}\bigr)(h-A)
 \right).
```

Here $`\operatorname{red}_q`$ means reduction modulo $`(X_1^q-X_1,\ldots,X_n^q-X_n)`$. Each bracket is the indicator function of $`k`$. In particular, when $`s=p`$, formula [(8)](#label-eq-explicitpatch) visibly has coefficients in $`\mathbb F_p`$.

## 3. A transfer operator for the recursion

Let $`E=\mathbb F_q`$ with $`q>3`$. On the space of reduced univariate polynomial functions $`h:E\to E`$, define the linear operator

<a id="label-eq-T"></a>

```math
\tag{9}
 (Th)(z)=\sum_{x\in E}x\,h\bigl(t(I(z)+I(x))\bigr).
```

For $`n\geq1`$ put
```math
S_n(h)=\sum_{x\in E^n}\left(\prod_{i=1}^n x_i\right)h(f_n(x)).
```
Summing in the last coordinate of [(1)](#label-eq-family) shows that $`S_n(h)=S_{n-1}(Th)`$. Since $`S_1(h)=\sum_z zh(z)=-[X^{q-2}]h`$, we obtain

<a id="label-eq-transfercoefficient"></a>

```math
\tag{10}
 C_n=(-1)^{n+1}[X^{q-2}]T^{n-1}X.
```

<a id="lemma-3"></a>

**Lemma 6.**

<a id="label-lem-T"></a>

Let $`h=\sum_{j=0}^{q-1}h_jX^j`$, and put $`\Delta=h(1)-h(0)=\sum_{j=1}^{q-1}h_j`$. The coefficients of $`Th`$ satisfy

<a id="label-eq-Tend"></a>

<a id="label-eq-Tmiddle"></a>

```math
\begin{align}
 (Th)_0&=-h_1-\Delta, & (Th)_1&=h_{q-1},\tag{11}\\
 (Th)_i&=i(h_{q-i}+\Delta)\quad(2\leq i\leq q-2),
 & (Th)_{q-1}&=0.\tag{12}
\end{align}
```
The integer $`i`$ in [(12)](#label-eq-Tmiddle) is interpreted as an element of $`E`$.

<!-- end lemma-3 -->

<a id="proof-3"></a>

**Proof.**

Let $`g`$ be the reduced representative of $`h\circ t`$. Since $`t`$ swaps zero and one, the difference between $`g`$ and $`h`$ is represented by
```math
g(X)=h(X)+\Delta\sum_{j=0}^{q-2}X^j.
```
Indeed the sum on the right is $`1`$ at zero, $`-1`$ at one, and zero elsewhere. In [(9)](#label-eq-T), substitute $`u=I(x)`$ and write $`v=I(z)`$. Expansion of $`g(v+u)`$ gives
```math
(Th)(z)=\sum_{u\in E}I(u)g(v+u)=-g'(v).
```
For clarity, the coefficient of $`u^j`$ in that expansion is multiplied by $`\sum_{u\ne0}u^{j-1}`$. Among $`0\leq j\leq q-1`$, this sum vanishes except at $`j=1`$, where it is $`-1`$. The surviving coefficient is precisely $`g'(v)`$.

Thus $`Th=-g'\circ I`$. Its constant coefficient is $`-g_1=-h_1-\Delta`$. For $`2\leq j\leq q-1`$, the monomial $`-j g_jI(X)^{j-1}`$ reduces to $`-j g_jX^{q-j}`$. When $`j=q-1`$ this gives coefficient $`h_{q-1}`$ at $`X`$; the other cases give [(12)](#label-eq-Tmiddle). No term of degree $`q-1`$ occurs. $`\square`$

<!-- end proof-3 -->

## 4. The extremal coefficient over nonprime odd fields

We now prove Theorem [2](#label-thm-recurrence). Assume $`q=p^r`$ with $`p`$ odd and $`r\geq2`$, and put $`H_j=T^jX`$ for $`j\geq1`$. Lemma [6](#label-lem-T) shows that the coefficients of $`H_j`$ at indices $`1`$ and $`q-1`$ are zero. Its remaining positive-degree coefficients have the form

<a id="label-eq-profile"></a>

```math
\tag{13}
 [X^i]H_j=P_j(i\bmod p)\quad(2\leq i\leq q-2),
```

where $`P_j:\mathbb F_p\to\mathbb F_p`$ and $`P_j(0)=0`$. For $`j=1`$ we may take $`P_1(a)=a`$; the profile property then follows inductively from [(12)](#label-eq-Tmiddle).

Write $`\Delta_j=H_j(1)-H_j(0)`$. In the complete index interval $`0,\ldots,q-1`$, each residue modulo $`p`$ occurs $`p^{r-1}`$ times. This multiplicity is zero in $`\mathbb F_p`$. Removing indices $`0,1,q-1`$ and using $`P_j(0)=0`$ gives

<a id="label-eq-Deltaj"></a>

```math
\tag{14}
 \Delta_j=-P_j(1)-P_j(-1).
```

By Lemma [6](#label-lem-T) we can therefore choose the profiles recursively as

<a id="label-eq-Pupdate"></a>

```math
\tag{15}
 P_{j+1}(a)=a\bigl(P_j(-a)+\Delta_j\bigr).
```

Evaluating at $`a=1`$ and $`a=-1`$ yields
```math
P_{j+1}(1)=-P_j(1),\qquad P_{j+1}(-1)=P_j(-1).
```
Since $`P_1(1)=1`$ and $`P_1(-1)=-1`$, we conclude that

<a id="label-eq-Deltaalternates"></a>

```math
\tag{16}
 P_j(1)=(-1)^{j-1},\qquad P_j(-1)=-1,\qquad
 \Delta_j=1-(-1)^{j-1}.
```

Put $`a_j=P_j(-2)`$ and $`b_j=P_j(2)`$. Equation [(15)](#label-eq-Pupdate) gives
```math
a_{j+1}=-2(b_j+\Delta_j),\qquad
 b_{j+1}=2(a_j+\Delta_j).
```
Combining the two identities and substituting [(16)](#label-eq-Deltaalternates),

<a id="label-eq-aj"></a>

```math
\tag{17}
 a_{j+2}=-4a_j-4\Delta_j-2\Delta_{j+1}
 =-4a_j-6+2(-1)^{j-1}.
```

These evaluations remain valid when $`p=3`$, where some of the named residues coincide: they are values of the same functions, not coordinates required to be distinct.

The residue of $`q-2`$ modulo $`p`$ is $`-2`$, so [(10)](#label-eq-transfercoefficient) becomes $`C_n=(-1)^{n+1}a_{n-1}`$ for $`n\geq2`$. Consequently [(17)](#label-eq-aj) gives

<a id="label-eq-Crec"></a>

```math
\tag{18}
 C_{n+2}=-4C_n+6(-1)^n-2\quad(n\geq2).
```

The initial values are $`C_2=2`$ and $`C_3=-4`$, obtained from $`P_1(a)=a`$ and $`P_2(a)=-a^2`$. Thus the even subsequence is the sequence $`E_k`$ in [(2)](#label-eq-Ek). The odd subsequence starts at $`-2E_1`$ and obeys $`C_{2k+3}=-4C_{2k+1}-8`$, which proves $`C_{2k+1}=-2E_k`$ by induction. Solving [(2)](#label-eq-Ek) proves [(4)](#label-eq-closed). Lemma [4](#label-lem-coefficient) then proves the maximum-degree criterion, completing Theorem [2](#label-thm-recurrence). Corollary [3](#label-cor-failure) follows immediately.

## 5. Uniform existence over the prime field

We complete the proof of Theorem [1](#label-thm-exist) and give formulas for its constructions. For $`n=1`$, the polynomial $`X^{q-2}`$ works in every field under consideration. It remains to treat $`n\geq2`$.

If $`p=2`$, the known construction [\[2, Theorem 4\]](#ref-GJU-afr) is

<a id="label-eq-binary"></a>

```math
\tag{19}
 B_{q,n}(X_1,\ldots,X_n)
 =\prod_{i=1}^n\left(\sum_{j=1}^{q-2}X_i^j\right)+\sum_{i=1}^nX_i.
```

It is an LPP of degree $`n(q-2)`$, with coefficients in $`\mathbb F_2`$.

Suppose $`p\geq5`$. Theorem 5 of [\[2\]](#ref-GJU-afr), applied over $`\mathbb F_p`$ with $`b=p-2`$, provides a maximum-degree LPP $`h`$ in every arity: the required conditions are $`1<b<p-1`$ and $`\gcd(b,p-1)=1`$. For $`q=p`$ this is the desired polynomial. For any larger extension, apply Lemma [5](#label-lem-patch) with $`s=p`$. Formula [(8)](#label-eq-explicitpatch) gives the resulting polynomial over $`\mathbb F_p`$ and [(7)](#label-eq-patchcoefficient) proves its maximum degree.

For completeness, the prime-field seed can be chosen by a finite explicit procedure from that construction. Set $`G_0(Y)=Y`$. Form $`G_{d+1}`$ by taking $`b`$ disjoint copies of $`G_d`$, adding them, and raising the sum to the $`b`$th power. Choose $`d`$ with $`N=b^d\geq n`$, and form
```math
H=\operatorname{red}_p G_d(Y_1^{p-2},\ldots,Y_N^{p-2}).
```
The seed construction proves that $`H`$ has nonzero coefficient at $`\prod_{i=1}^N Y_i^{p-2}`$. Specialize the last $`N-n`$ variables to a tuple in $`\mathbb F_p^{N-n}`$ for which the coefficient of $`\prod_{i=1}^nY_i^{p-2}`$ remains nonzero. Such a tuple exists because that coefficient is a nonzero reduced polynomial in the last variables. Choosing the lexicographically first such tuple, with field elements represented by $`0,1,\ldots,p-1`$, makes this a deterministic procedure. Specialization preserves the local permutation property.

Finally, suppose $`p=3`$. Since $`q>3`$, its extension degree satisfies $`r\geq2`$. Use the recursion [(1)](#label-eq-family). Corollary [3](#label-cor-failure) shows that $`\operatorname{top}_q(f_n)=2\ne0`$ for every $`n\geq2`$, and every operation in the recursion has coefficients in $`\mathbb F_3`$. This proves Theorem [1](#label-thm-exist).

## 6. Scope and further questions

The subfield patch separates coefficient descent from the original construction of an LPP. Its extremal coefficient is preserved exactly, rather than merely shown to remain nonzero. The ternary recursion supplies the case where the prime subfield itself is too small for the patching lemma.

The transfer identity $`Th=-(h\circ t)'\circ I`$, where the derivative is taken after reducing $`h\circ t`$, also applies when $`q`$ is prime. The simplification [(14)](#label-eq-Deltaj) does not: residue classes then occur only once. Determining the maximum-degree arities in that case is a separate problem. For nonprime odd fields, another question is to determine the exact reduced degree at the arities where Theorem [2](#label-thm-recurrence) gives $`C_n=0`$.

## References

<a id="ref-CF"></a>

**\[1\]** N. J. Cavenagh and R. M. Falcón, *Latin bitrades derived from quasigroup autoparatopisms*, arXiv:2308.14987v1 (2023). <https://arxiv.org/abs/2308.14987>.

<a id="ref-GJU-afr"></a>

**\[2\]** J. Gutierrez and J. Jiménez Urroz, *Permutation and local permutation polynomials of maximum degree*, Afrika Matematika **36** (2025), article 45. [doi:10.1007/s13370-025-01247-3](https://doi.org/10.1007/s13370-025-01247-3).

<a id="ref-GJU-mal"></a>

**\[3\]** J. Gutierrez and J. Jiménez Urroz, *Local permutation polynomials of maximum degree over prime finite fields*, Bulletin of the Malaysian Mathematical Sciences Society **48** (2025), article 40. [doi:10.1007/s40840-025-01825-5](https://doi.org/10.1007/s40840-025-01825-5).
