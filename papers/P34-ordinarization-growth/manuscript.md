# Quasipolynomiality and collision asymptotics for ordinarization counts

September 16, 2026; revised version 1.2

## Abstract

Let $`n_{g,r}`$ count numerical semigroups of genus $`g`$ and ordinarization number $`r`$. For every fixed positive integer $`r`$, we prove that $`n_{g,r}`$ is a quasipolynomial for all positive integers $`g`$, answering a question of Cyrusian and Kaplan. Its leading coefficient is $`1/(2(2r)!)+1/(2\cdot4^r(r!)^2)`$. We determine the complete next coefficient in closed form, including its constant part and its oscillation: its exact period is two, and its even value is smaller than its odd value by $`1/(4^r r!(r-1)!)`$. This gives explicit positive leading terms for $`n_{g+1,r}-n_{g,r}`$ in both parities and proves eventual strict monotonicity for every fixed $`r`$. The proof separates a binomial-sum bulk from exceptional additive relations. Those relations lie in linear hyperplanes through the origin, which prevents them from introducing periodicity in the next coefficient. For growing $`r`$ with $`r^2/g\to0`$ and $`r^3/g\to\tau`$, we prove that $`n_{g,r}/(A_rg^{2r})\to e^{-\tau/2}`$. This follows from a Poisson law for forbidden holes and bounds on all tuples outside the bulk, using closure under addition by the multiplicity. The full all-genus counting conjectures remain open.

## 1. Introduction and main results

A numerical semigroup is an additive submonoid $`S`$ of $`\mathbb Z_{\ge0}`$ with finite complement. Its genus $`g(S)`$ is the number of gaps, and its Frobenius number $`F(S)`$ is the largest gap when $`g(S)>0`$. The ordinary semigroup of genus $`g`$ is $`\{0,g+1,g+2,\ldots\}`$. Repeatedly removing the smallest positive nongap and inserting the largest gap leads to this ordinary semigroup. The number of steps is the ordinarization number $`r(S)`$.

The ordinarization number equals the number of positive elements of $`S`$ at most $`g(S)`$; see [\[2, Proposition 1.4\]](#ref-CK). We write
```math
n_{g,r}=\#\{S:g(S)=g,\ r(S)=r\}.
```
Cyrusian and Kaplan proved eventual quasipolynomiality of degree $`2r`$ for fixed $`r`$ [\[2, Theorem 3.4\]](#ref-CK). They asked whether the quasipolynomial holds for every positive genus [\[2, Remark 3.7\]](#ref-CK). They also discuss the conjecture $`n_{g+1,r}\ge n_{g,r}`$ for every $`g,r`$ [\[2, Conjecture 1.5\]](#ref-CK), and prove it for $`r=2`$. We answer their quasipolynomiality question and prove the eventual strict version of this conjecture for every fixed positive $`r`$.

Recall that a quasipolynomial on the positive integers is an expression $`\sum_{j=0}^d c_j(g)g^j`$ with rational-valued periodic functions $`c_j`$. Equivalently, one polynomial applies in each residue class modulo some positive integer. The degree is the largest $`j`$ for which $`c_j`$ is not identically zero. Sections 1–5 keep $`r`$ fixed. Section [6](#label-sec-growing) treats sequences with increasing $`r`$.

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

With the explicit rational number $`\beta_r`$ given in Theorem [5.1](#label-thm-second), we have

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

## 5. The complete second coefficient

We now evaluate the constant left implicit in the preceding argument. This also answers the question about $`\beta_r`$ in the first version of this paper.

<a id="theorem-2"></a>

**Theorem 5.1.**

<a id="label-thm-second"></a>

For every $`r\ge1`$, the constant in [(2)](#label-eq-main) is

<a id="label-eq-beta-explicit"></a>

```math
\tag{18}
\begin{split}
\beta_r={}&-\frac{r^2+7r-10}{8(2r-1)!}
-\frac{4r^2-4r+3}{2(2r-1)}C_r\\
&-\frac{3(r-1)}{(2r-1)9^r r!(r-1)!}.
\end{split}
```

In particular, $`\beta_1=-1/8`$, $`\beta_2=-1193/5184`$, and $`\beta_r<0`$ for every positive $`r`$. Moreover,

<a id="label-eq-coefficient-scale"></a>

```math
\tag{19}
\frac{\beta_r}{A_r}\sim-\frac{r^3}{2}\qquad(r\longrightarrow\infty).
```

The last statement concerns the coefficients as functions of $`r`$. It does not make the error in [(2)](#label-eq-main) uniform in $`r`$, and does not give a threshold for the counting conjecture.

<!-- end theorem-2 -->

### The three exceptional contributions

All dimensions in the next argument refer to the $`2r`$ coordinates $`(A,B)`$ at fixed real $`g>0`$. Enlarge the equality arrangement used in Section 3 to include all equations
```math
b_i+b_j=b_k,\qquad a_h-b_i=a_j,\qquad b_i+b_j=a_h.
```
Delete equations with no solutions in the strict ordering region, and identify equations defining the same hyperplane. Two distinct hyperplanes in this arrangement have an intersection of dimension at most $`2r-2`$. Their bounded integer sections consequently contribute $`O_r(g^{2r-2})`$: choose two coordinates with independent coefficients and fix the other $`2r-2`$ coordinates; at most one solution remains. We may therefore compute the coefficient of $`g^{2r-1}`$ away from such intersections. Boundary faces of each resulting region do not affect its leading lattice volume.

Suppose first that a valid tuple is outside the bulk because $`2m\le g`$, where $`m=b_1`$. Closure forces $`2m\in B`$. Away from the discarded intersections this is its only additive equality. Thus $`3m>g`$, every other element of $`B\setminus\{m,2m\}`$ exceeds $`g-m`$, and $`\max A\le g+m`$. For example, $`3m\le g`$ would force a second equality for $`m+2m`$; any other $`b\le g-m`$ would force a second equality for $`m+b`$. Conversely, these inequalities make all low sums except $`m+m`$ exceed $`g`$, and make all hole-minus-low-element differences at most $`g`$. Excluding sums in $`A`$ costs only the discarded intersections. After scaling $`g=1`$, the leading contribution is therefore

<a id="label-eq-kappa-low"></a>

```math
\tag{20}
\ell_r=\frac{1}{(r-2)!r!}\int_{1/3}^{1/2}m^{2r-2}\,dm
=\frac{2^{-(2r-1)}-3^{-(2r-1)}}{(2r-1)(r-2)!r!},
\quad r\ge2.
```

Indeed, the $`r-2`$ free low elements lie in $`(1-m,1)`$, of length $`m`$, and the $`r`$ holes lie in $`(1,1+m)`$, also of length $`m`$. The forced low element $`2m`$ is in the first interval. Dividing by the factorials counts unordered sets. Eliminating the coordinate equal to $`2m`$ preserves the integer lattice; no Euclidean surface-area factor enters this volume.

The second positive contribution comes from a valid tuple with $`2m>g`$ and $`a_r>g+m`$. Closure forces $`a_r-m=a_h`$ for some $`h<r`$. Write $`a=a_h`$. Away from multiple equalities, all the other holes are at most $`g+m`$ and all elements of $`B\setminus\{m\}`$ are at least $`a+m-g`$. These conditions are also sufficient away from the discarded intersections. At $`g=1`$, $`1/2<m<1`$ and $`1<a<2-m`$. The free holes occupy an interval of length $`m`$; the free low elements occupy an interval of length $`2-a-m`$. Hence

<a id="label-eq-kappa-high"></a>

```math
\tag{21}
\begin{split}
u_r&=\frac{1}{(r-2)!(r-1)!}
 \int_{1/2}^1\int_1^{2-m}m^{r-2}(2-a-m)^{r-1}\,da\,dm\\
&=\frac{1}{(r-2)!r!}\int_{1/2}^1m^{r-2}(1-m)^r\,dm,
\quad r\ge2.
\end{split}
```

Here the eliminated coordinate is $`a_r=a+m`$, again an integral graph. Tuples violating both bulk inequalities have two distinct equalities and are already in the discarded set.

For the negative contribution, a bulk tuple is invalid exactly when a sum $`b_i+b_j`$ is a hole. Distinct such equalities overlap only on discarded intersections, so their leading contributions add. Fix $`m\in(1/2,1)`$ and put $`L=1-m`$. For each low set $`B`$, the $`r`$ unordered pairs involving its minimum, including $`(m,m)`$, always have sum in $`(1,1+m)`$. The other low elements lie in $`(m,1)`$. Among their doubled elements, the permitted interval has half its full length. Among two distinct such elements, the permitted unordered region is a triangle of area $`L^2/4`$. Relative to the volume $`L^{r-1}/(r-1)!`$ of all choices of the free low elements, these three contributions have factors
```math
r,\qquad \frac{r-1}{2},\qquad \frac{(r-1)(r-2)}4.
```
Their sum is $`r(r+3)/4`$. Once a sum is forced to be a hole, the other $`r-1`$ holes have volume $`m^{r-1}/(r-1)!`$. Consequently the magnitude of the negative coefficient is

<a id="label-eq-kappa-negative"></a>

```math
\tag{22}
d_r=\frac{r(r+3)}{4((r-1)!)^2}
 \int_{1/2}^1m^{r-1}(1-m)^{r-1}\,dm
=\frac{r(r+3)}{8(2r-1)!}.
```

The last equality uses symmetry and the beta integral. Each sum-hole hyperplane eliminates a hole coordinate with coefficient one, so the same lattice normalization applies. We have proved, for $`r\ge2`$,

<a id="label-eq-kappa-split"></a>

```math
\tag{23}
\kappa_r=\ell_r+u_r-d_r.
```

### Evaluation and the bulk average

For $`r\ge2`$, reflection about $`1/2`$ and an elementary antiderivative give
```math
\begin{align*}
&\int_{1/2}^1\bigl(m^r(1-m)^{r-2}+m^{r-2}(1-m)^r\bigr)\,dm
 =\frac{r!(r-2)!}{(2r-1)!},\\
&\int_{1/2}^1\bigl(m^r(1-m)^{r-2}-m^{r-2}(1-m)^r\bigr)\,dm
 =\frac{1}{(r-1)4^{r-1}}.
\end{align*}
```
The second integrand is $`(2m-1)m^{r-2}(1-m)^{r-2}`$, the negative derivative of $`m^{r-1}(1-m)^{r-1}/(r-1)`$. Thus
```math
u_r=\frac{1}{2(2r-1)!}-2C_r.
```
Substituting this and [(20)](#label-eq-kappa-low) into [(23)](#label-eq-kappa-split) yields

<a id="label-eq-kappa-explicit"></a>

```math
\tag{24}
\kappa_r=-\frac{(r+4)(r-1)}{8(2r-1)!}
-\frac{2r}{2r-1}C_r
-\frac{3(r-1)}{(2r-1)9^r r!(r-1)!}.
```

We also make the polynomial $`h_r`$ in [(16)](#label-eq-summand) explicit:
```math
h_r(x)=-\frac{(r-1)(r-2)x^r(1-x)^{r-2}
 +r(r-1)x^{r-1}(1-x)^{r-1}}{2r!(r-1)!}.
```
The mean of the two lower-endpoint terms in [(17)](#label-eq-EM) is $`-f_r(1/2)/4=-C_r/2`$. Since $`f_r(1)=0`$ for $`r\ge2`$, the preceding integrals give

<a id="label-eq-gamma-explicit"></a>

```math
\tag{25}
\gamma_r=\int_{1/2}^1h_r(x)\,dx-\frac{C_r}{2}
=-\frac{2r-3}{4(2r-1)!}-\left(r-\frac32\right)C_r.
```

Adding [(24)](#label-eq-kappa-explicit) and [(25)](#label-eq-gamma-explicit) proves [(18)](#label-eq-beta-explicit) for $`r\ge2`$.

For $`r=1`$, no valid tuple is outside the bulk: either violated bulk inequality would force $`m=0`$. A bulk pair $`(a,m)`$ fails only at $`a=2m`$, so $`n_{g,1}-M_1(g)=-\lceil g/2\rceil`$. Hence $`\kappa_1=-1/2`$ and, using $`\gamma_1=3/8`$, we obtain $`\beta_1=-1/8`$. Formulas [(24)](#label-eq-kappa-explicit), [(25)](#label-eq-gamma-explicit), and [(18)](#label-eq-beta-explicit) have these same values at $`r=1`$. For $`r\ge2`$, all three summands of [(18)](#label-eq-beta-explicit) are negative, proving the asserted sign.

Finally, $`\binom{2r}{r}/4^r\sim1/\sqrt{\pi r}`$ implies
```math
A_r\sim\frac{1}{4r(2r-1)!},\qquad
\beta_r\sim-\frac{r^2}{8(2r-1)!}.
```
The remaining terms in [(18)](#label-eq-beta-explicit) are smaller by the same central-binomial estimate and the exponential factor $`(4/9)^r`$. Taking the ratio proves [(19)](#label-eq-coefficient-scale) and completes the proof of Theorem [5.1](#label-thm-second).

### Exact sums for reproducing the leading volumes

The three regions above admit convenient finite counting formulas. These count candidates, with multiplicity for the negative contribution; they are not exact formulas for the correction $`n_{g,r}-M_r(g)`$. For $`r\ge2`$, put

<a id="label-eq-low-sum"></a>

<a id="label-eq-high-sum"></a>

```math
\begin{align}
L_r(g)&=\sum_{\lfloor g/3\rfloor<m\le\lfloor g/2\rfloor}
 \binom{m-1}{r-2}\binom mr,\tag{26}\\
U_r(g)&=\sum_{\lfloor g/2\rfloor<m\le g}
 \binom{m-1}{r-2}\binom{g-m+1}{r}.\tag{27}
\end{align}
```
The first formula removes the forced element $`2m`$ from the $`m`$ possible free-low positions. For the second, sum over the lower forced hole $`a`$: the number of available other low elements is $`2g-a-m+1`$. The hockey-stick identity then sums their binomial coefficients. For every $`r\ge1`$, define

<a id="label-eq-negative-sum"></a>

```math
\tag{28}
\begin{split}
D_r(g)=\sum_{m=\lfloor g/2\rfloor+1}^{g}\binom{m-1}{r-1}
\biggl[&r\binom{g-m}{r-1}
+\left\lfloor\frac{g-m}{2}\right\rfloor\binom{g-m-1}{r-2}\\
&+\left\lfloor\frac{(g-m-1)^2}{4}\right\rfloor
 \binom{g-m-2}{r-3}\biggr].
\end{split}
```

A binomial coefficient in these formulas is zero unless its two indices are integers with $`0\le k\le n`$. The last term counts distinct unordered $`u,v\in[1,g-m]`$ with $`u+v\le g-m`$. There are $`\lfloor(g-m-1)^2/4\rfloor`$ such pairs. Set $`L_1=U_1=0`$.

The equality-arrangement argument proves

<a id="label-eq-signed-approx"></a>

```math
\tag{29}
n_{g,r}-M_r(g)=L_r(g)+U_r(g)-D_r(g)+O_r(g^{2r-2}).
```

In particular their leading coefficients are $`\ell_r,u_r,d_r`$, respectively. Formula [(29)](#label-eq-signed-approx) retains a remainder from multiple additive equalities. It must not be used as an exact identity or as a uniform estimate with $`r`$ increasing.

## 6. Growing ordinarization and a collision limit

<a id="label-sec-growing"></a>

The preceding coefficients suggest the scale $`r^3/g`$. We now establish a limit in which this parameter need not vanish. The argument counts the multiple additive coincidences directly, rather than summing a fixed-$`r`$ asymptotic expansion.

<a id="theorem-3"></a>

**Theorem 6.1.**

<a id="label-thm-uniform"></a>

Let $`g,r`$ be positive integers varying along a sequence such that
```math
r\longrightarrow\infty,\qquad \frac{r^2}{g}\longrightarrow0,
\qquad \frac{r^3}{g}\longrightarrow\tau\in[0,\infty].
```
With $`A_r`$ as in [(1)](#label-eq-constants),

<a id="label-eq-uniform-limit"></a>

```math
\tag{30}
\frac{n_{g,r}}{A_rg^{2r}}\longrightarrow e^{-\tau/2},
```

where $`e^{-\infty}=0`$. If $`\tau<\infty`$, this is the relative asymptotic $`n_{g,r}\sim e^{-\tau/2}A_rg^{2r}`$. More generally, for every sequence with $`r\to\infty`$ and $`r^2/g\to0`$,

<a id="label-eq-uniform-additive"></a>

```math
\tag{31}
\frac{n_{g,r}}{A_rg^{2r}}-\exp\left(-\frac{r^3}{2g}\right)
\longrightarrow0.
```

The error in [(31)](#label-eq-uniform-additive) is additive. When $`r^3/g`$ tends to infinity, no relative estimate with that exponential is asserted.

<!-- end theorem-3 -->

Let $`V_r(g)`$ count the valid tuples in the bulk $`\mathcal M_r(g)`$ and let $`E_r(g)=n_{g,r}-V_r(g)`$ count the valid tuples outside it. We use the following three ingredients: a uniform estimate for $`M_r(g)`$, a bound for $`E_r(g)`$ using addition by the multiplicity, and a collision law inside the bulk. Throughout this section, a bound with an absolute implicit constant is independent of $`g`$ and $`r`$.

### The bulk measure and its minimum

<a id="lemma-5"></a>

**Lemma 6.2.**

<a id="label-lem-uniform-bulk"></a>

If $`r\to\infty`$ and $`r^2/g\to0`$, then

<a id="label-eq-uniform-M"></a>

```math
\tag{32}
M_r(g)\sim A_rg^{2r}.
```

For a tuple chosen uniformly from $`\mathcal M_r(g)`$, its minimum $`m=\min B`$ satisfies $`m/g\to1/2`$ in probability.

<!-- end lemma-5 -->

<a id="proof-7"></a>

**Proof.**

Put $`p_r(x)=x^r(1-x)^{r-1}`$ and $`J_r=\int_{1/2}^1p_r(x)\,dx`$. The evaluation in Section 4 gives $`J_r/(r!(r-1)!)=A_r`$. The function $`p_r`$ is unimodal, and
```math
\frac{\max_{[1/2,1]}p_r}{J_r}=O(\sqrt r).
```
For completeness, its maximum occurs at $`r/(2r-1)`$ and is $`O(4^{-r})`$. On an interval $`[1/2,1/2+c/\sqrt r]`$ with fixed small $`c>0`$, the factor $`(x(1-x))^{r-1}`$ is bounded below by an absolute positive multiple of $`4^{-(r-1)}`$. Integrating over this interval gives $`J_r\gg4^{-r}/\sqrt r`$. The error of a mesh Riemann sum for a unimodal nonnegative function is at most an absolute multiple of its maximum. It follows that
```math
\sum_{m=\lfloor g/2\rfloor+1}^{g}p_r(m/g)
=gJ_r\left(1+O\left(\frac{\sqrt r}{g}\right)\right).
```
For each fixed $`\varepsilon\in(0,1/2)`$, the fraction of this sum on $`m/g\ge1/2+\varepsilon`$ tends to zero: on that interval, $`x(1-x)\le1/4-\varepsilon^2`$, giving an exponentially decreasing bound times a polynomial in $`r`$.

Every summand in [(10)](#label-eq-M) is at most $`g^{2r-1}p_r(m/g)/(r!(r-1)!)`$. On $`1/2<m/g\le3/4`$, both upper binomial indices are at least $`g/4`$. Their falling-factorial products differ from the corresponding powers by a relative $`O(r^2/g)`$, uniformly there. This follows from $`1-\prod_j(1-u_j)\le\sum_j u_j`$ for $`0\le u_j\le1`$; eventually all factors in question are nonnegative. The polynomial weight outside this interval is negligible by the preceding exponential bound. These upper and lower comparisons prove [(32)](#label-eq-uniform-M) and transfer the concentration of $`m/g`$ to the exact bulk weights. $`\square`$

<!-- end proof-7 -->

### Bounding all valid tuples outside the bulk

We need only the necessary closure conditions coming from addition by $`m`$. The resulting bound includes semigroups with any number of other additive equalities.

<a id="lemma-6"></a>

**Lemma 6.3.**

<a id="label-lem-outside-bulk"></a>

If $`r\to\infty`$ and $`r^2/g\to0`$, then

<a id="label-eq-outside-small"></a>

```math
\tag{33}
E_r(g)=o(M_r(g)).
```

This estimate is on the scale of $`M_r(g)`$, not necessarily on the smaller scale of $`n_{g,r}`$.

<!-- end lemma-6 -->

<a id="proof-8"></a>

**Proof.**

For a semigroup with multiplicity $`m`$, the holes $`A`$ form initial segments of the $`m`$ arithmetic-progression chains in $`[g+1,2g]`$ with step $`m`$. Indeed, $`a\in A`$ and $`a-m>g`$ imply $`a-m\in A`$. Ignoring the finite chain lengths, the number of choices of $`r`$ holes is at most

<a id="label-eq-hole-chain-bound"></a>

```math
\tag{34}
\binom{m+r-1}{r}.
```

Suppose $`2\le m\le g/2`$ and put $`q=\lfloor g/m\rfloor\ge2`$. The set $`B`$ contains the $`q`$ multiples $`m,2m,\ldots,qm`$. In each other residue class modulo $`m`$, its elements form a terminal segment of the chain in $`[m+1,g]`$, because adding $`m`$ preserves membership. If $`q>r`$ there are no such tuples. Otherwise stars and bars bounds the choices of $`B`$ by
```math
\binom{m+r-q-2}{r-q}\le\binom{m+r-4}{r-2}.
```
The inequality follows because the number of weak compositions into $`m-1`$ parts is nondecreasing with the sum. There is no positive-genus semigroup with multiplicity one. Consequently the entire low-minimum contribution is at most

<a id="label-eq-low-uniform-bound"></a>

```math
\tag{35}
\begin{split}
\sum_{m=2}^{\lfloor g/2\rfloor}
 \binom{m+r-4}{r-2}\binom{m+r-1}{r}
&\le\frac{(g/2+r+1)^{2r-1}}{(2r-1)(r-2)!r!}.
\end{split}
```

For the last inequality, bound the product by $`(m+r)^{2r-2}/((r-2)!r!)`$ and compare the increasing sum with an integral extending to $`g/2+1`$. Using $`A_r\ge1/(2(2r)!)`$ and the central-binomial estimate, the right side of [(35)](#label-eq-low-uniform-bound), divided by $`A_rg^{2r}`$, is
```math
O\left(\frac{\sqrt r}{g}
 \exp\left(O\left(\frac{r(r+1)}g\right)\right)\right)=o(1).
```

For $`m>g/2`$, the low set has exactly $`\binom{g-m}{r-1}`$ possible choices. Every subset of $`[g+1,g+m]`$ is an initial-chain hole set; there are $`\binom mr`$ such subsets. Thus the number of possible hole sets extending above $`g+m`$ is at most
```math
\binom{m+r-1}{r}-\binom mr.
```
Eventually $`r<m/2`$, uniformly in this range, and
```math
\frac{\binom{m+r-1}{r}}{\binom mr}
=\prod_{j=0}^{r-1}\frac{m+j}{m-j}
\le\exp\left(\frac{3r(r-1)}{2m}\right)
\le\exp\left(\frac{3r^2}{g}\right).
```
Here $`\log((1+x)/(1-x))\le3x`$ for $`0\le x\le1/2`$. Multiplying by the low-set count and summing over $`m`$ bounds the high contribution by $`(\exp(3r^2/g)-1)M_r(g)=o(M_r(g))`$. Together with [(35)](#label-eq-low-uniform-bound) and Lemma [6.2](#label-lem-uniform-bulk), this proves [(33)](#label-eq-outside-small). $`\square`$

<!-- end proof-8 -->

### Distinct forbidden sums

In a bulk tuple, write
```math
K(B)=\#\bigl((B+B)\cap[g+1,g+m]\bigr).
```
This counts distinct forbidden hole positions, not pairs producing them. Conditional on $`m`$ and $`B`$, the $`r`$ holes are a uniform subset of an interval of size $`m`$. Hence the exact conditional validity probability is

<a id="label-eq-avoidance"></a>

```math
\tag{36}
\frac{\binom{m-K(B)}r}{\binom mr}.
```

<a id="lemma-7"></a>

**Lemma 6.4.**

<a id="label-lem-forbidden-sums"></a>

Under the bulk distribution, if $`r\to\infty`$ and $`r^2/g\to0`$, then

<a id="label-eq-K-limit"></a>

```math
\tag{37}
\frac{K(B)}{r^2}\longrightarrow\frac14
\quad\hbox{in probability}.
```

<!-- end lemma-7 -->

<a id="proof-9"></a>

**Proof.**

By Lemma [6.2](#label-lem-uniform-bulk), it suffices to work uniformly on $`g/2<m\le3g/4`$. Put $`L=g-m\ge g/4`$. Conditional on $`m`$, the $`r-1`$ elements of $`B\setminus\{m\}`$ are a uniform subset of $`\{m+1,\ldots,g\}`$. Subtract $`m`$ and label them in random order as $`Y_1,\ldots,Y_{r-1}`$. Their law is that of independent uniform variables on $`[1,L]`$ conditioned to be distinct. The probability of a repeat in the independent sample is $`O(r^2/L)=o(1)`$, so it suffices to establish the assertions under the independent law.

Let $`H`$ count pairs $`i<j`$ with $`Y_i+Y_j\le L`$. Their corresponding low-element sums are precisely those at most $`g+m`$. Each indicator has expectation $`(L-1)/(2L)`$. Indicators on disjoint pairs are independent, and at most $`O(r^3)`$ pairs of indicators share an index. Thus $`\operatorname{Var}(H)=O(r^3)`$ and $`H/r^2\to1/4`$ in probability.

Two distinct unordered index pairs have equal sums with probability at most $`1/L`$: condition on all but a variable with coefficient $`1`$ or $`-1`$ in the equality. There are $`O(r^4)`$ pairs of such pairs. If $`K_H`$ counts distinct values among the sums counted by $`H`$, then $`H-K_H`$ is at most the number of equal-sum pairs. Therefore
```math
\mathbb E\left[\frac{H-K_H}{r^2}\right]=O(r^2/L)=o(1).
```
The sums involving the minimum and the doubled other elements add at most $`2r`$ distinct positions, so $`K_H\le K(B)\le K_H+2r`$ under the distinct-sample law. Conditioning changes the probability statements by $`o(1)`$. This proves [(37)](#label-eq-K-limit) uniformly in the stipulated range of $`m`$, and hence under the bulk distribution. $`\square`$

<!-- end proof-9 -->

### The collision law and the count

For a uniformly chosen bulk tuple, let $`Z=\#(A\cap(B+B))`$. Thus $`Z`$ is the number of distinct holes which are sums of two low nongaps, and the tuple is valid exactly when $`Z=0`$.

<a id="proposition-2"></a>

**Proposition 6.5.**

<a id="label-prop-poisson"></a>

Under the hypotheses of Theorem [6.1](#label-thm-uniform) with finite $`\tau`$, $`Z`$ converges in distribution to a Poisson variable of mean $`\tau/2`$. In particular, $`V_r(g)/M_r(g)\to e^{-\tau/2}`$.

<!-- end proposition-2 -->

<a id="proof-10"></a>

**Proof.**

Conditionally on $`m,B`$, $`Z`$ is hypergeometric. If $`(x)_k`$ denotes the falling factorial, then
```math
\mathbb E[(Z)_k\mid m,B]=\frac{(r)_k(K(B))_k}{(m)_k}.
```
Lemmas [6.2](#label-lem-uniform-bulk) and [6.4](#label-lem-forbidden-sums) give
```math
\frac{rK(B)}m
=\frac{r^3}{g}\frac{K(B)}{r^2}\frac gm
\longrightarrow\frac\tau2
\quad\hbox{in probability}.
```
For fixed $`k`$, the conditional factorial moments therefore tend to $`(\tau/2)^k`$ in probability. This also holds at $`\tau=0`$, directly by the upper bound below. Since $`K(B)\le r(r+1)/2`$ and $`m>g/2`$, there is a constant $`C_\tau`$ independent of $`k,g,r`$ along this sequence (after finitely many terms) such that, for $`0\le k\le r`$,
```math
\frac{(r)_k(K(B))_k}{(m)_k}\le
\left(\frac{rK(B)}{m-r}\right)^k\le C_\tau^k.
```
For $`k>r`$ the moment is zero. Bounded convergence gives convergence of each unconditional factorial moment. Moreover, for $`0\le z\le1`$, the finite expansion
```math
\mathbb E[(1-z)^Z]
=\sum_{k\ge0}\frac{(-z)^k}{k!}\mathbb E[(Z)_k]
\longrightarrow\exp(-\tau z/2)
```
is justified by the summable majorant $`C_\tau^k/k!`$. These are the probability generating functions of the asserted Poisson limit. Equivalently, tightness follows from the bounded first moments, and every subsequential limit has this same generating function. Taking $`z=1`$ proves the stated zero-collision probability directly. $`\square`$

<!-- end proof-10 -->

<a id="proof-11"></a>

**Proof of Theorem [6.1](#label-thm-uniform).**

For finite $`\tau`$, combine Proposition [6.5](#label-prop-poisson) with [(32)](#label-eq-uniform-M) and [(33)](#label-eq-outside-small), using $`n_{g,r}=V_r(g)+E_r(g)`$. If $`r^3/g\to\infty`$, [(36)](#label-eq-avoidance) is at most $`\exp(-rK(B)/m)`$, with the ratio interpreted as zero if fewer than $`r`$ allowable hole positions remain. The exponent tends to infinity in probability by Lemmas [6.2](#label-lem-uniform-bulk) and [6.4](#label-lem-forbidden-sums). The bounded avoidance probability therefore has expectation tending to zero. The same decomposition proves [(30)](#label-eq-uniform-limit) with $`\tau=\infty`$. Finally, any subsequence of $`r^3/g`$ has a further subsequence converging in $`[0,\infty]`$. Applying the just-proved limits on every such subsequence proves [(31)](#label-eq-uniform-additive). $`\square`$

<!-- end proof-11 -->

For finite $`\tau`$, the valid tuples outside the bulk also form an $`o(1)`$ fraction of all semigroups with these parameters, since the normalized count has a positive limit. This relative conclusion is not asserted when $`\tau=\infty`$. The theorem gives no error rate fine enough to subtract consecutive genus counts and prove their sign. It also does not reach $`r`$ proportional to $`g`$. Both distinctions are essential when comparing this result with the full Bras-Amorós counting conjectures.

## 7. Consequences, checks, and remaining questions

The first three leading coefficients are $`A_1=3/8`$, $`A_2=11/384`$, and $`A_3=7/7680`$. The first two agree with the exact formulas of [\[2, Proposition 2.1 and Theorem 3.5\]](#ref-CK). These small values illustrate the general coefficient formula; our contribution concerns arbitrary fixed $`r`$.

The homogeneous description is also effective in principle. For a specified $`r`$, form the finite arrangement in the proof of Proposition [2.3](#label-prop-quasi), enumerate its rational cells, and compute their Ehrhart quasipolynomials. A common multiple of the vertex denominators bounds a period. The argument gives no efficient bound for this enumeration. Once the finitely many constituents are obtained, eventual positivity of [(3)](#label-eq-increment) reduces the full monotonicity question for that particular $`r`$ to finitely many genera.

The accompanying Python script compares literal closure with Lemma [2.1](#label-lem-closure) on all $`66\,187`$ tuples through genus $`9`$, checking all $`584`$ exceptional tuples. Independently generated semigroup trees through genus $`16`$ contain $`11\,770`$ semigroups in total; their counts agree with the tuple counts and the known $`r=1,2`$ formulas on the overlapping ranges. Exact rational interpolation tests the bulk’s two leading coefficients for $`1\le r\le12`$, with $`936`$ additional evaluations beyond the interpolation data. For the revised second-coefficient formula, a separate script checks all $`17\,568`$ tuples through genus $`8`$, verifies that all $`223`$ nonzero signed residuals satisfy two independent additive equalities, and checks the candidate-sum formulas. Exact rational interpolation of those sums for $`1\le r\le8`$ has $`864`$ holdout evaluations; the resulting coefficients also agree with every residue of the cited exact $`r=2`$ formula. The growing-ordinarization checks additionally verify the chain conditions for all $`11\,753`$ nonordinary semigroups through genus $`16`$, compare $`1\,004`$ exact bulk fibers with tree counts, and check the outside-bulk bounds on the same range. Literal closure is checked in each bulk fiber through genus $`8`$. These finite diagnostics do not replace the general proofs.

Several questions remain. Theorem [5.1](#label-thm-second) evaluates the previously undetermined constant $`\beta_r`$. One can next determine the full period of $`n_{g,r}`$, evaluate the lower-dimensional multiple-equality contributions, and find bounds for the onset of strict growth. The stronger conjecture asks for monotonicity at every genus and every ordinarization number. The present argument now evaluates the top two coefficients completely for fixed $`r`$ and leaves those further questions open. Theorem [6.1](#label-thm-uniform) separately establishes a growing-$`r`$ limit under $`r^2/g\to0`$. It gives neither a relative exponential estimate when $`r^3/g\to\infty`$, nor an error rate that decides consecutive differences. Reaching $`r`$ proportional to $`g`$ and controlling the full Bras-Amorós Fibonacci sign remain open.

## References

<a id="ref-BR"></a>

**\[1\]** M. Beck and S. Robins, *Computing the Continuous Discretely: Integer-Point Enumeration in Polyhedra*, 2nd ed., Undergraduate Texts in Mathematics, Springer, 2015. [doi:10.1007/978-1-4939-2969-6](https://doi.org/10.1007/978-1-4939-2969-6).

<a id="ref-CK"></a>

**\[2\]** S. Cyrusian and N. Kaplan, Ordinarization numbers of numerical semigroups, *Communications in Algebra* (2026), 1–24. [doi:10.1080/00927872.2026.2615092](https://doi.org/10.1080/00927872.2026.2615092). Also [arXiv:2506.10222v2](https://arxiv.org/abs/2506.10222v2); theorem numbering follows this version.
