# Quasipolynomiality and eventual growth at fixed ordinarization number

September 9, 2026

## Abstract

Let $`n_{g,r}`$ count numerical semigroups of genus $`g`$ and ordinarization number $`r`$. For every fixed positive integer $`r`$, we prove that $`n_{g,r}`$ is a quasipolynomial for all positive integers $`g`$, answering a question of Cyrusian and Kaplan. Its leading coefficient is $`1/(2(2r)!)+1/(2\cdot4^r(r!)^2)`$. We determine the oscillation of the next coefficient: its exact period is two, and its even value is smaller than its odd value by $`1/(4^r r!(r-1)!)`$. This gives explicit positive leading terms for $`n_{g+1,r}-n_{g,r}`$ in both parities and proves eventual strict monotonicity for every fixed $`r`$. The proof separates a binomial-sum bulk from exceptional additive relations. Those relations lie in linear hyperplanes through the origin, which prevents them from introducing periodicity in the next coefficient.

## 1. Introduction and main results

A numerical semigroup is an additive submonoid $`S`$ of $`\mathbb Z_{\ge0}`$ with finite complement. Its genus $`g(S)`$ is the number of gaps, and its Frobenius number $`F(S)`$ is the largest gap when $`g(S)>0`$. The ordinary semigroup of genus $`g`$ is $`\{0,g+1,g+2,\ldots\}`$. Repeatedly removing the smallest positive nongap and inserting the largest gap leads to this ordinary semigroup. The number of steps is the ordinarization number $`r(S)`$.

The ordinarization number equals the number of positive elements of $`S`$ at most $`g(S)`$; see [\[2, Proposition 1.4\]](#ref-CK). We write
```math
n_{g,r}=\#\{S:g(S)=g,\ r(S)=r\}.
```
Cyrusian and Kaplan proved eventual quasipolynomiality of degree $`2r`$ for fixed $`r`$ [\[2, Theorem 3.4\]](#ref-CK). They asked whether the quasipolynomial holds for every positive genus [\[2, Remark 3.7\]](#ref-CK). They also discuss the conjecture $`n_{g+1,r}\ge n_{g,r}`$ for every $`g,r`$ [\[2, Conjecture 1.5\]](#ref-CK), and prove it for $`r=2`$. We answer their quasipolynomiality question and prove the eventual strict version of this conjecture for every fixed positive $`r`$.

Recall that a quasipolynomial on the positive integers is an expression $`\sum_{j=0}^d c_j(g)g^j`$ with rational-valued periodic functions $`c_j`$. Equivalently, one polynomial applies in each residue class modulo some positive integer. The degree is the largest $`j`$ for which $`c_j`$ is not identically zero. All asymptotic estimates below keep $`r`$ fixed.

<a id="theorem-1"></a>

**Theorem 1.1.**

<a id="label-thm-main"></a>

For every positive integer $`r`$, the function $`g\mapsto n_{g,r}`$ is a quasipolynomial of degree $`2r`$ on all positive integers. Put

<a id="label-eq-constants"></a>

```math
\tag{1}
 A_r=\frac{1}{2(2r)!}+\frac{1}{2\cdot4^r(r!)^2},
 \qquad C_r=\frac{1}{4^r r!(r-1)!}.
```

There is a rational number $`\beta_r`$ such that

<a id="label-eq-main"></a>

```math
\tag{2}
 n_{g,r}=A_r g^{2r}
   +\left(\beta_r-\frac{C_r}{2}(-1)^g\right)g^{2r-1}
   +O_r(g^{2r-2}).
```

Consequently, the leading coefficient is constant and the coefficient of $`g^{2r-1}`$ has exact period two.

<!-- end theorem-1 -->

<a id="corollary-1"></a>

**Corollary 1.2.**

<a id="label-cor-growth"></a>

For fixed $`r\ge1`$,

<a id="label-eq-increment"></a>

```math
\tag{3}
 n_{g+1,r}-n_{g,r}=
 \begin{cases}
 \displaystyle\left(\frac{r}{(2r)!}+2C_r\right)g^{2r-1}
                  +O_r(g^{2r-2}),&g\text{ even},\\[4pt]
 \displaystyle\frac{r}{(2r)!}g^{2r-1}
                  +O_r(g^{2r-2}),&g\text{ odd}.
 \end{cases}
```

In particular, $`n_{g+1,r}>n_{g,r}`$ for every sufficiently large $`g`$.

<!-- end corollary-1 -->

The conclusion is pointwise in $`r`$: no threshold uniform in a growing ordinarization number is asserted. We do not settle monotonicity at every genus, nor monotonicity of the total number of numerical semigroups. A positive constant leading coefficient alone would not prove Corollary [1.2](#label-cor-growth), because a periodic next coefficient can contribute at the same order to successive differences. Determining that coefficient’s oscillation is the essential additional step.

## 2. An exact homogeneous description

Fix positive integers $`g,r`$. Consider integer tuples satisfying

<a id="label-eq-ambient"></a>

```math
\tag{4}
 0<b_1<\cdots<b_r\le g<a_1<\cdots<a_r\le2g.
```

Write $`B=\{b_1,\ldots,b_r\}`$ and $`A=\{a_1,\ldots,a_r\}`$, and associate the set

<a id="label-eq-S"></a>

```math
\tag{5}
 S(A,B)=\{0\}\cup B\cup\bigl(\{g+1,g+2,\ldots\}\setminus A\bigr).
```

It has precisely $`g`$ gaps. We use $`2g`$ as the upper bound in [(4)](#label-eq-ambient); closure under addition will automatically exclude a gap at $`2g`$.

<a id="lemma-1"></a>

**Lemma 2.1.**

<a id="label-lem-closure"></a>

The set [(5)](#label-eq-S) is a numerical semigroup if and only if both of the following conditions hold:

<a id="label-eq-BB"></a>

<a id="label-eq-AB"></a>

```math
\begin{align}
 &(b_i+b_j>g\ \text{or}\ b_i+b_j\in B)
       \quad\text{and}\quad b_i+b_j\notin A
       &&(1\le i\le j\le r),\tag{6}\\
 &a_h-b_i\le g\ \text{or}\ a_h-b_i\in A
       &&(1\le h,i\le r).\tag{7}
\end{align}
```
Every numerical semigroup of genus $`g`$ and ordinarization number $`r`$ arises from exactly one such tuple.

<!-- end lemma-1 -->

<a id="proof-1"></a>

**Proof.**

Condition [(6)](#label-eq-BB) says exactly that sums of two elements of $`B`$ lie in $`S(A,B)`$. For a mixed sum $`b_i+x`$ with $`x\in S(A,B)`$ and $`x>g`$, the only possible failure is $`b_i+x=a_h`$ for some $`h`$. Such a failure occurs precisely when $`a_h-b_i>g`$ and $`a_h-b_i\notin A`$. This is excluded exactly by [(7)](#label-eq-AB). Two summands greater than $`g`$ have sum greater than $`2g`$, and zero causes no obstruction. This proves the equivalence.

For completeness, if $`S`$ has genus $`g>0`$ and Frobenius number $`F`$, the map $`s\mapsto F-s`$ injects $`S\cap[0,F]`$ into the gaps: otherwise $`F`$ would be a sum of two elements of $`S`$. Hence $`F+1-g\le g`$, so $`F\le2g-1`$. There are $`r`$ positive nongaps at most $`g`$, leaving $`g-r`$ gaps there and therefore $`r`$ gaps above $`g`$. These two sets give $`B`$ and $`A`$ uniquely, and the Frobenius bound places $`A`$ in the required interval. $`\square`$

<!-- end proof-1 -->

We recall the particular lattice-counting facts needed here. A rational polyhedral Boolean set means a set specified by a finite Boolean combination of rational linear equalities and strict or weak inequalities.

<a id="lemma-2"></a>

**Lemma 2.2.**

<a id="label-lem-ehrhart"></a>

Let $`D\subset\mathbb R^d`$ be a bounded rational polyhedral Boolean set. Then
```math
t\longmapsto\#(tD\cap\mathbb Z^d)
```
is a quasipolynomial for all positive integers $`t`$. If $`D`$ is contained in a finite union of rational linear hyperplanes through the origin, then there is a rational constant $`\kappa`$ such that

<a id="label-eq-hyperasymp"></a>

```math
\tag{8}
 \#(tD\cap\mathbb Z^d)=\kappa t^{d-1}+O_D(t^{d-2})
```

when $`d\ge2`$. The same conclusion holds for a finite signed sum of such counts.

<!-- end lemma-2 -->

<a id="proof-2"></a>

**Proof.**

Take the arrangement of all hyperplanes appearing in a description of $`D`$, together with a rational bounding box. Its cells that belong to $`D`$ are relative interiors of bounded rational polytopes, and they form a finite disjoint partition. Ehrhart’s theorem gives quasipolynomial lattice counts for closed rational polytopes [\[1, Theorem 3.23\]](#ref-BR). Removing the boundary by inclusion-exclusion over proper faces gives the same conclusion for relative interiors and therefore for $`D`$. This argument holds at every positive dilation, including for lower-dimensional polytopes whose affine hulls may meet the lattice only at some dilations.

For the second assertion, refine the arrangement to include the stated hyperplanes. Every selected cell has dimension at most $`d-1`$. A cell of dimension $`d-1`$ lies in some hyperplane $`H`$, and its affine hull equals $`H`$. The lattice $`\Lambda=H\cap\mathbb Z^d`$ has full rank in $`H`$. After choosing a lattice basis of $`\Lambda`$, the closure $`P`$ of this cell becomes a full-dimensional rational polytope in $`\mathbb R^{d-1}`$. Its lattice count is
```math
\#(t\operatorname{relint}P\cap\Lambda)
   =\operatorname{vol}_{\Lambda}(P)t^{d-1}+O_P(t^{d-2}),
```
where volume is normalized so that a fundamental parallelepiped of $`\Lambda`$ has volume one. One can see this directly by tiling $`H`$ by such parallelepipeds: only those meeting the boundary contribute to the discrepancy, and their number is $`O_P(t^{d-2})`$. Boundary removal has the same error bound. The normalized volume is rational and does not depend on a residue class of $`t`$.

Cells of dimension at most $`d-2`$ contribute $`O_D(t^{d-2})`$, by their Ehrhart quasipolynomials. Summing proves [(8)](#label-eq-hyperasymp); signed sums follow by linearity. The requirement that the containing hyperplanes pass through the origin ensures that the full lattice in each top-dimensional affine hull is present at every dilation. $`\square`$

<!-- end proof-2 -->

<a id="proposition-1"></a>

**Proposition 2.3.**

<a id="label-prop-quasi"></a>

For fixed positive $`r`$, the function $`n_{g,r}`$ is a quasipolynomial on all positive integers $`g`$, of degree at most $`2r`$.

<!-- end proposition-1 -->

<a id="proof-3"></a>

**Proof.**

Apply Lemma [2.1](#label-lem-closure). Membership in a finite set such as $`B`$ is a finite disjunction of linear equalities, and nonmembership is a conjunction of their negations. All conditions in [(4)](#label-eq-ambient), [(6)](#label-eq-BB), and [(7)](#label-eq-AB) are homogeneous in the variables $`(a_1,\ldots,a_r,b_1,\ldots,b_r,g)`$. In particular, strict inequalities are retained as strict inequalities, without introducing an additive constant.

Let $`D_r\subset\mathbb R^{2r}`$ be the set obtained by putting $`g=1`$ in these conditions. It is bounded and rational polyhedral Boolean. Homogeneity gives
```math
n_{g,r}=\#(gD_r\cap\mathbb Z^{2r})\qquad(g\ge1).
```
Lemma [2.2](#label-lem-ehrhart) gives the desired quasipolynomial, with degree at most the ambient dimension. $`\square`$

<!-- end proof-3 -->

## 3. The bulk and its exceptional hyperplanes

Let $`\mathcal N_r(g)`$ be the set of tuples counted by $`n_{g,r}`$. Define the bulk $`\mathcal M_r(g)`$ to consist of the integer tuples in [(4)](#label-eq-ambient) satisfying

<a id="label-eq-bulk"></a>

```math
\tag{9}
 2b_1>g,\qquad a_r\le g+b_1.
```

These conditions do not themselves impose closure. Put $`M_r(g)=\#\mathcal M_r(g)`$.

<a id="lemma-3"></a>

**Lemma 3.1.**

<a id="label-lem-bulk"></a>

For all positive integers $`g,r`$,

<a id="label-eq-M"></a>

```math
\tag{10}
 M_r(g)=\sum_{m=\lfloor g/2\rfloor+1}^{g}
                \binom{g-m}{r-1}\binom{m}{r},
```

where a binomial coefficient is zero if its lower index exceeds its nonnegative upper index. Moreover, there is $`\kappa_r\in\mathbb Q`$ such that

<a id="label-eq-correction"></a>

```math
\tag{11}
 n_{g,r}-M_r(g)=\kappa_r g^{2r-1}+O_r(g^{2r-2}).
```

<!-- end lemma-3 -->

<a id="proof-4"></a>

**Proof.**

Choose $`m=b_1`$. The remaining $`r-1`$ elements of $`B`$ are chosen from $`m+1,\ldots,g`$. The $`r`$ elements of $`A`$ are chosen from $`g+1,\ldots,g+m`$. This proves [(10)](#label-eq-M).

We claim that the symmetric difference of $`\mathcal N_r(g)`$ and $`\mathcal M_r(g)`$ lies in the union of the proper linear hyperplanes

<a id="label-eq-H1"></a>

<a id="label-eq-H2"></a>

<a id="label-eq-H3"></a>

```math
\begin{align}
 2b_1&=b_i &&(1\le i\le r),\tag{12}\\
 a_r-b_1&=a_h &&(1\le h\le r),\tag{13}\\
 b_i+b_j&=a_h &&(1\le i\le j\le r,\ 1\le h\le r).\tag{14}
\end{align}
```
Indeed, if a tuple is valid but $`2b_1\le g`$, condition [(6)](#label-eq-BB) forces $`2b_1\in B`$. If it is valid but $`a_r>g+b_1`$, condition [(7)](#label-eq-AB) forces $`a_r-b_1\in A`$. These are [(12)](#label-eq-H1) and [(13)](#label-eq-H2).

Conversely, suppose a tuple belongs to the bulk. Every sum of two elements of $`B`$ is greater than $`g`$. Also $`a_h-b_i\le a_r-b_1\le g`$ for all $`h,i`$, so the mixed-sum condition is automatic. The only remaining failures of closure are therefore the equalities in [(14)](#label-eq-H3). This proves the claim. The argument also holds for the real tuples defined by the same Boolean conditions, because it uses only those conditions and the ordering.

Set $`g=1`$ in the real valid and bulk sets. Their two set differences are bounded rational polyhedral Boolean sets in the union of [(12)](#label-eq-H1)–[(14)](#label-eq-H3). These hyperplanes involve no $`g`$ and pass through the origin in $`\mathbb R^{2r}`$. Apply the signed version of Lemma [2.2](#label-lem-ehrhart) with $`d=2r`$ to obtain [(11)](#label-eq-correction). $`\square`$

<!-- end proof-4 -->

<a id="remark-1"></a>

**Remark 3.2.**

<a id="label-rem-constant"></a>

The constancy of $`\kappa_r`$ is crucial. The weaker estimate $`n_{g,r}-M_r(g)=O_r(g^{2r-1})`$ would permit a correction of the same size as the main term in a successive difference. In contrast, [(11)](#label-eq-correction) implies
```math
(n_{g+1,r}-M_r(g+1))-(n_{g,r}-M_r(g))=O_r(g^{2r-2}).
```
No differentiation of an unspecified error term is used: subtracting two quantities individually of order $`g^{2r-2}`$ remains of that order.

<!-- end remark-1 -->

## 4. Two leading coefficients of the bulk

<a id="lemma-4"></a>

**Lemma 4.1.**

<a id="label-lem-asymp"></a>

There is a rational number $`\gamma_r`$ such that

<a id="label-eq-bulkexp"></a>

```math
\tag{15}
 M_r(g)=A_r g^{2r}
       +\left(\gamma_r-\frac{C_r}{2}(-1)^g\right)g^{2r-1}
       +O_r(g^{2r-2}),
```

with $`A_r,C_r`$ as in [(1)](#label-eq-constants).

<!-- end lemma-4 -->

<a id="proof-5"></a>

**Proof.**

First suppose $`r\ge2`$. Expanding the two binomial polynomials gives, uniformly for $`g/2\le m\le g`$,

<a id="label-eq-summand"></a>

```math
\tag{16}
 \binom{g-m}{r-1}\binom{m}{r}
 =g^{2r-1}f_r(m/g)+g^{2r-2}h_r(m/g)+O_r(g^{2r-3}),
```

where $`h_r\in\mathbb Q[x]`$ is a polynomial and
```math
f_r(x)=\frac{x^r(1-x)^{r-1}}{r!(r-1)!}.
```
The polynomial interpretation of the binomial coefficients is valid even when a nonnegative upper index is smaller than the lower index, since the product defining the polynomial then vanishes. There is no endpoint exception in [(16)](#label-eq-summand).

Write $`\delta=1`$ for even $`g`$ and $`\delta=1/2`$ for odd $`g`$. The first summation point in [(10)](#label-eq-M) is $`m=g/2+\delta`$. For any fixed polynomial $`f`$, the trapezoidal summation formula gives

<a id="label-eq-EM"></a>

```math
\tag{17}
 \sum_{m=\lfloor g/2\rfloor+1}^{g}f(m/g)
 =g\int_{1/2}^1f(x)\,dx+\frac{f(1)}2
       +\left(\frac12-\delta\right)f(1/2)+O_f(g^{-1}).
```

To verify the endpoint term, apply the trapezoidal formula on the mesh from $`1/2+\delta/g`$ to $`1`$. Extending the integral to $`1/2`$ subtracts $`\delta f(1/2)`$, whereas the lower endpoint contributes $`f(1/2)/2`$, up to $`O_f(g^{-1})`$.

The $`h_r`$ sum equals $`g\int_{1/2}^1 h_r(x)\,dx+O_r(1)`$. Substitution into [(16)](#label-eq-summand) shows that the coefficient of $`g^{2r}`$ is $`\int_{1/2}^1 f_r`$, and that the only parity dependence in the next coefficient comes from
```math
\left(\frac12-\delta\right)f_r(1/2).
```
Since $`f_r(1/2)=2C_r`$, the even second coefficient is smaller than the odd second coefficient by $`C_r`$. Their average is rational.

It remains to evaluate the integral. Put $`q(x)=x^{r-1}(1-x)^{r-1}`$. Then
```math
xq(x)=\frac12q(x)+\frac12(2x-1)q(x),
 \qquad
 \frac{d}{dx}\bigl(x^r(1-x)^r\bigr)=-r(2x-1)q(x).
```
Symmetry of $`q`$ and the beta integral therefore give
```math
\begin{align*}
 \int_{1/2}^1x^r(1-x)^{r-1}\,dx
 &=\frac14\int_0^1x^{r-1}(1-x)^{r-1}\,dx+\frac{1}{2r4^r}\\
 &=\frac{((r-1)!)^2}{4(2r-1)!}+\frac{1}{2r4^r}.
\end{align*}
```
Dividing by $`r!(r-1)!`$ gives $`A_r`$.

For $`r=1`$ the summand in [(10)](#label-eq-M) is exactly $`m`$. Direct summation yields
```math
M_1(g)=\begin{cases}
 3g^2/8+g/4,&g\text{ even},\\
 3g^2/8+g/2+1/8,&g\text{ odd}.
 \end{cases}
```
This has $`A_1=3/8`$, $`C_1=1/4`$, and $`\gamma_1=3/8`$, as required. $`\square`$

<!-- end proof-5 -->

<a id="proof-6"></a>

**Proof of Theorem [1.1](#label-thm-main) and Corollary [1.2](#label-cor-growth).**

Proposition [2.3](#label-prop-quasi) gives exact quasipolynomiality for positive $`g`$. Combine Lemmas [3.1](#label-lem-bulk) and [4.1](#label-lem-asymp), and set $`\beta_r=\gamma_r+\kappa_r`$. This proves [(2)](#label-eq-main). Because $`A_r>0`$, the degree is $`2r`$. On each residue class of a common period, a polynomial that is $`O(g^{2r-2})`$ has zero coefficients in degrees $`2r`$ and $`2r-1`$. Thus [(2)](#label-eq-main) identifies those coefficients of the exact quasipolynomial. Since $`C_r>0`$, the second coefficient has exact period two.

Subtract [(2)](#label-eq-main) at consecutive genera. The leading term contributes $`2rA_rg^{2r-1}+O_r(g^{2r-2})`$, the constant part $`\beta_rg^{2r-1}`$ contributes only $`O_r(g^{2r-2})`$, and the alternating contribution is
```math
C_r(-1)^gg^{2r-1}+O_r(g^{2r-2}).
```
Using $`2rA_r=r/(2r)!+C_r`$ gives [(3)](#label-eq-increment). Both parity constants are strictly positive, so the error is eventually smaller than the leading term in each parity. $`\square`$

<!-- end proof-6 -->

## 5. Consequences, checks, and remaining questions

The first three leading coefficients are $`A_1=3/8`$, $`A_2=11/384`$, and $`A_3=7/7680`$. The first two agree with the exact formulas of [\[2, Proposition 2.1 and Theorem 3.5\]](#ref-CK). These small values illustrate the general coefficient formula; our contribution concerns arbitrary fixed $`r`$.

The homogeneous description is also effective in principle. For a specified $`r`$, form the finite arrangement in the proof of Proposition [2.3](#label-prop-quasi), enumerate its rational cells, and compute their Ehrhart quasipolynomials. A common multiple of the vertex denominators bounds a period. The argument gives no efficient bound for this enumeration. Once the finitely many constituents are obtained, eventual positivity of [(3)](#label-eq-increment) reduces the full monotonicity question for that particular $`r`$ to finitely many genera.

The accompanying Python script compares literal closure with Lemma [2.1](#label-lem-closure) on all $`66\,187`$ tuples through genus $`9`$, checking all $`584`$ exceptional tuples. Independently generated semigroup trees through genus $`16`$ contain $`11\,770`$ semigroups in total; their counts agree with the tuple counts and the known $`r=1,2`$ formulas on the overlapping ranges. Exact rational interpolation tests the bulk’s two leading coefficients for $`1\le r\le12`$, with $`936`$ additional evaluations beyond the interpolation data. These finite diagnostics do not replace the general proofs.

Several questions remain. One can seek an explicit formula for the constant $`\beta_r`$ by evaluating the top-dimensional exceptional cells, determine the full period of $`n_{g,r}`$, and find bounds for the onset of strict growth. The stronger conjecture asks for monotonicity at every genus and every ordinarization number. The present argument controls the top two coefficients for fixed $`r`$ and leaves those further questions open.

## References

<a id="ref-BR"></a>

**\[1\]** M. Beck and S. Robins, *Computing the Continuous Discretely: Integer-Point Enumeration in Polyhedra*, 2nd ed., Undergraduate Texts in Mathematics, Springer, 2015. [doi:10.1007/978-1-4939-2969-6](https://doi.org/10.1007/978-1-4939-2969-6).

<a id="ref-CK"></a>

**\[2\]** S. Cyrusian and N. Kaplan, Ordinarization numbers of numerical semigroups, *Communications in Algebra* (2026), 1–24. [doi:10.1080/00927872.2026.2615092](https://doi.org/10.1080/00927872.2026.2615092). Also [arXiv:2506.10222v2](https://arxiv.org/abs/2506.10222v2); theorem numbering follows this version.
