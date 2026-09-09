# Symbolic defect and normalization of whiskered cover ideals

Henry Zweiman

September 8, 2026

## Abstract

Let $`J`$ be the cover ideal of the full whiskering of a graph $`G`$ on $`n`$ vertices. We express its symbolic defect and integral symbolic defect as differences between the Ehrhart functions of the fractional and ordinary stable-set polytopes and the Hilbert function of the stable-set semigroup. For every nonbipartite core graph the two defects are asymptotic, with common leading term $`(\operatorname{vol}(\operatorname{FRAC}(G))-\operatorname{vol}(\operatorname{STAB}(G)))m^n`$ and positive coefficient. Their difference is eventually polynomial of degree at most $`n-1`$, without any normality hypothesis. This bound is sharp: when the complement of $`G`$ is a disjoint union of two odd cycles of lengths at least five, we determine the difference in every degree by a single binomial coefficient, and give a composition formula for any number of odd-cycle components. We also give closed formulas for the full symbolic defect of whiskered complete graphs.

## 1. Introduction and statements

For a homogeneous ideal $`I`$ in a polynomial ring, the symbolic defect $`\operatorname{sdef}(I,m)=\mu(I^{(m)}/I^m)`$ measures the number of generators needed to account for the difference between symbolic and ordinary powers. The integral symbolic defect introduced by Oltsik [\[7, Definition 4.1\]](#ref-Oltsik) is
```math
\operatorname{isdef}(I,m)=\mu\bigl(\overline{I^{(m)}}/\overline{I^m}\bigr).
```
Here a bar denotes integral closure and $`\mu`$ the minimal number of module generators. These two counts need not agree. Oltsik asks about their growth comparison and the degrees and coefficients of their eventual quasipolynomials [\[7, Section 7\]](#ref-Oltsik). We obtain an exact description for cover ideals of fully whiskered graphs, including graphs whose stable-set semigroup rings are not normal.

We write $`\mathbb N=\mathbb Z_{\geq0}`$. Throughout, $`G`$ is a finite simple graph with specified vertex set $`[n]`$, where $`n\geq1`$. Isolated vertices are allowed. Its full whiskering $`w(G)`$ has vertices $`x_1,\ldots,x_n,y_1,\ldots,y_n`$, the core edges $`x_ix_j`$ for $`ij\in E(G)`$, and the pendant edges $`x_iy_i`$. Over an arbitrary field $`\Bbbk`$, put
```math
R=\Bbbk[x_1,\ldots,x_n,y_1,\ldots,y_n],\qquad
J=J(w(G))=\bigcap_{uv\in E(w(G))}(u,v).
```
Write $`s_m=\operatorname{sdef}(J,m)`$ and $`i_m=\operatorname{isdef}(J,m)`$.

Let $`\mathcal I(G)`$ be the independent sets of $`G`$, including the empty set. We use the polytopes and finite sets
```math
\begin{align*}
P=\operatorname{FRAC}(G)&=\{b\in[0,1]^n:b_i+b_j\leq1\text{ for }ij\in E(G)\},\\
Q=\operatorname{STAB}(G)&=\operatorname{conv}\{\mathbf 1_A:A\in\mathcal I(G)\},\\
B_m&=\{\mathbf 1_{A_1}+\cdots+\mathbf 1_{A_m}:A_j\in\mathcal I(G)\}.
\end{align*}
```
The upper coordinate bounds in $`P`$ include isolated vertices. Define
```math
E_P(m)=|mP\cap\mathbb Z^n|,\quad E_Q(m)=|mQ\cap\mathbb Z^n|,
\quad H_G(m)=|B_m|.
```
All volumes below are Euclidean $`n`$-dimensional volumes, with unit cube volume one. Thus the Ehrhart leading coefficient is $`\operatorname{vol}(P)`$, rather than $`n!\operatorname{vol}(P)`$.

<a id="theorem-1"></a>

**Theorem 1.1.**

<a id="label-thm-main"></a>

For every graph $`G`$ as above and every $`m\geq1`$,

<a id="label-eq-dictionary"></a>

```math
\tag{1}
s_m=E_P(m)-H_G(m),\qquad i_m=E_P(m)-E_Q(m).
```

The difference $`s_m-i_m`$ is nonnegative, eventually polynomial, and $`O(m^{n-1})`$. It vanishes for every $`m`$ if and only if $`Q`$ has the integer decomposition property.

Both defects are eventually quasipolynomial with period dividing two. If $`G`$ is bipartite, both vanish identically. If $`G`$ is nonbipartite, then

<a id="label-eq-asymptotic"></a>

```math
\tag{2}
s_m=c_Gm^n+O(m^{n-1}),\qquad
i_m=c_Gm^n+O(m^{n-1}),\qquad
c_G=\operatorname{vol}(P)-\operatorname{vol}(Q)>0.
```

In particular both parity branches have degree $`n`$ and leading coefficient $`c_G`$, and $`s_m/i_m\longrightarrow1`$.

<!-- end theorem-1 -->

The next result gives an exact correction in a nonnormal family. For a graph $`G`$, its complement is denoted by $`\overline G`$; this notation is distinct from integral closure of ideals.

<a id="theorem-2"></a>

**Theorem 1.2.**

<a id="label-thm-correction"></a>

Suppose $`\overline G=C_r\sqcup C_s`$, where $`r,s\geq5`$ are odd, and put $`n=r+s`$. Then

<a id="label-eq-correction"></a>

```math
\tag{3}
s_m-i_m=
\begin{cases}
0,&m<n/2,\\[2pt]
\displaystyle\binom{m+n/2-1}{n-1},&m\geq n/2.
\end{cases}
```

Consequently the exponent $`n-1`$ in Theorem [1.1](#label-thm-main) is sharp. The correction first occurs in degree $`n/2`$ and has leading coefficient $`1/(n-1)!`$.

<!-- end theorem-2 -->

For complete cores, the normalization correction is zero and the full defect has a direct closed form.

<a id="theorem-3"></a>

**Theorem 1.3.**

<a id="label-thm-complete"></a>

For $`G=K_n`$ one has $`s_m=i_m`$ for all $`m`$. For $`q\geq0`$,

<a id="label-eq-even"></a>

<a id="label-eq-odd"></a>

```math
\begin{align}
s_{2q}&=(q+1)^n+n\sum_{k=1}^q k^{n-1}-\binom{2q+n}{n},\tag{4}\\
s_{2q+1}&=(q+1)^n+n\sum_{k=1}^{q+1}k^{n-1}
-\binom{2q+1+n}{n}.\tag{5}
\end{align}
```
In [(4)](#label-eq-even), $`s_0`$ is interpreted as zero. For $`n\geq3`$, the leading coefficient as a function of $`m`$ is $`2^{1-n}-1/n!>0`$. For $`n=1,2`$, all defects are zero.

<!-- end theorem-3 -->

### Relation to previous work

The ordinary generators of whiskered cover ideals, their independent-set parametrization, and their analytic spread $`n+1`$ occur in Drabkin–Guerrieri [\[3, Proposition 5.7 and Theorem 5.8\]](#ref-DGFreiman). The additional observation used here is that every symbolic power is also generated in a single degree, and that ordinary products and integral closure can be compared inside the same affine slice.

Eventual quasipolynomiality with period dividing two for graph cover ideals is already known [\[2, Corollary 4.3\]](#ref-DG). The conditional recursion in [\[2, Theorem 5.5\]](#ref-DG) does not apply to all whiskered graphs: [\[2, Remark 5.3\]](#ref-DG) exhibits the whiskered triangle as a failure of its indecomposability hypothesis. Theorem [1.3](#label-thm-complete) includes that example and concerns whiskered complete graphs, whereas [\[2, Theorem 5.7\]](#ref-DG) treats unwhiskered complete graphs.

The polyhedral facts about fractional stable-set polytopes used below are established [\[4\]](#ref-HHO). Conditional comparisons with integral closure appear in [\[7, Proposition 4.5\]](#ref-Oltsik) and, more recently, [\[1, Theorem 4.1\]](#ref-BHL); the latter paper also gives coefficient constancy results under filtration and module hypotheses [\[1, Theorem 4.2\]](#ref-BHL). Our conclusions are the explicit volume difference, unconditional ratio one for this whiskered class, and exact correction [(3)](#label-eq-correction). They do not resolve the unrestricted growth questions for monomial ideals.

Nonnormality in Theorem [1.2](#label-thm-correction) is already implied by [\[6, Theorem 1\]](#ref-MOS). Preservation of multiplicity under semigroup normalization is standard; see also [\[5, Proposition 3.1\]](#ref-Higashitani). Moreover, [\[5, Proposition 4.2\]](#ref-Higashitani) computes a translated free-face hole monoid and its Hilbert-series correction for a different connected edge-ring family built around two triangles. Our exact correction is a specific stable-set and symbolic-defect calculation with that conceptual precedent. We give elementary proofs, including the exclusion of holes away from the relevant facet.

## 2. The common degree slice

Since $`J`$ is squarefree with minimal primes indexed by the edges,
```math
J^{(m)}=\bigcap_{uv\in E(w(G))}(u,v)^m.
```
Thus $`x^ay^b\in J^{(m)}`$ if and only if

<a id="label-eq-covers"></a>

```math
\tag{6}
a_i+b_i\geq m\quad(1\leq i\leq n),\qquad
a_i+a_j\geq m\quad(ij\in E(G)).
```

<a id="lemma-1"></a>

**Lemma 2.1.**

<a id="label-lem-generators"></a>

The minimal monomial generators of $`J^{(m)}`$ are precisely
```math
u_b=\prod_{i=1}^n x_i^{m-b_i}y_i^{b_i},
\qquad b\in mP\cap\mathbb Z^n.
```
In particular, every such generator has degree $`nm`$.

<!-- end lemma-1 -->

<a id="proof-1"></a>

**Proof.**

In a minimal generator, no $`a_i`$ can exceed $`m`$, because replacing it by $`m`$ preserves every inequality in [(6)](#label-eq-covers). Once $`a_i\leq m`$, a strict inequality $`a_i+b_i>m`$ permits decreasing the positive exponent $`b_i`$. Hence minimality requires $`a_i+b_i=m`$ for every $`i`$. Conversely, these equalities prevent decreasing any positive exponent: its pendant inequality would fail. Substituting $`a_i=m-b_i`$ in the core inequalities gives $`b_i+b_j\leq m`$, exactly the asserted lattice set. $`\square`$

<!-- end proof-1 -->

<a id="proposition-1"></a>

**Proposition 2.2.**

<a id="label-prop-dictionary"></a>

The identities [(1)](#label-eq-dictionary) hold for every $`m\geq1`$.

<!-- end proposition-1 -->

<a id="proof-2"></a>

**Proof.**

At $`m=1`$, the lattice vectors in Lemma [2.1](#label-lem-generators) are precisely the independent-set indicators. A product of $`m`$ such generators is $`u_b`$ with $`b\in B_m`$, and every element of $`B_m`$ occurs. These products all have degree $`nm`$, so distinct products are identified only when their exponent vectors are equal.

Let $`\mathfrak m`$ be the homogeneous maximal ideal of $`R`$. If a monomial ideal $`A`$ is generated in one degree $`d`$ and $`D\subseteq A`$ is a monomial ideal, the minimal generators of $`A/D`$ are exactly the degree-$`d`$ generators of $`A`$ absent from $`D`$. Their nonzero classes form a basis modulo $`\mathfrak m(A/D)`$: the latter has no degree-$`d`$ part, and the monomials present in the quotient are linearly independent. Applying this to $`A=J^{(m)}`$, $`D=J^m`$ gives $`s_m=E_P(m)-H_G(m)`$.

For a monomial ideal, a monomial belongs to its integral closure precisely when its exponent lies in its Newton polyhedron. This criterion can also be expressed by requiring a positive power of the monomial to belong to the same power of the ideal; see [\[7, Proposition 2.13\]](#ref-Oltsik). The Newton polyhedron of $`J^m`$ is the convex hull of its generating exponent vectors plus $`\mathbb R_{\geq0}^{2n}`$. Its intersection with the total-degree hyperplane $`nm`$ is exactly the affine image of $`mQ`$ under

<a id="label-eq-affine"></a>

```math
\tag{7}
b\longmapsto(m\mathbf 1-b,b).
```

Indeed the convex hull of all sums of $`m`$ independent-set indicators is $`mQ`$. All these exponent vectors already have total degree $`nm`$, and a nonzero nonnegative addition would increase that degree. It follows that
```math
u_b\in\overline{J^m}\quad\Longleftrightarrow\quad b\in mQ.
```
Each coordinate-prime power $`(u,v)^m`$ is integrally closed, as is their intersection. Thus $`J^{(m)}`$ is integrally closed and $`\overline{J^m}\subseteq J^{(m)}`$. Applying the same degree-$`nm`$ quotient argument gives $`i_m=E_P(m)-E_Q(m)`$. This argument does not assume that the entire ideal $`\overline{J^m}`$ is generated in degree $`nm`$. $`\square`$

<!-- end proof-2 -->

## 3. Normalization and asymptotic comparison

We include the semigroup estimate to make clear that no normality assumption on the stable-set ring is needed.

<a id="lemma-2"></a>

**Lemma 3.1.**

<a id="label-lem-conductor"></a>

Let $`S\subseteq\mathbb Z^{n+1}`$ be generated by $`(\mathbf 1_A,1)`$ for $`A\in\mathcal I(G)`$, and let $`\overline S=\mathbb R_{\geq0}S\cap\mathbb Z^{n+1}`$. Then
```math
0\leq E_Q(m)-H_G(m)=O(m^{n-1}).
```
The difference is eventually a polynomial.

<!-- end lemma-2 -->

<a id="proof-3"></a>

**Proof.**

The group generated by $`S`$ is all of $`\mathbb Z^{n+1}`$: it contains $`(0,1)`$ and $`(e_i,1)`$, and their differences give $`(e_i,0)`$. The degree-$`m`$ elements of $`\overline S`$ are exactly $`\{(b,m):b\in mQ\cap\mathbb Z^n\}`$.

There exists a conductor element $`c\in S`$ with $`c+\overline S\subseteq S`$. Here is a direct construction. If $`a_1,\ldots,a_t`$ generate $`S`$, subtract the floors of the coefficients in a nonnegative real expression $`u=\sum_j\lambda_ja_j`$ for $`u\in\overline S`$. The remainder is a lattice point in the bounded set $`\{\sum_j\theta_ja_j:0\leq\theta_j<1\}`$. Its finitely many possible values $`r_1,\ldots,r_v`$ belong to $`\overline S`$, and $`\overline S\subseteq\bigcup_j(r_j+S)`$. Fullness of the generated group allows us to write $`r_j=p_j-q_j`$ with $`p_j,q_j\in S`$. Taking $`c=\sum_jq_j`$ ensures $`c+r_j\in S`$ for every $`j`$, as required.

Write $`c=(c',d)`$. Translation by $`c`$ injects $`\overline S_{m-d}`$ into $`S_m`$ for $`m\geq d`$, and hence
```math
0\leq E_Q(m)-H_G(m)\leq E_Q(m)-E_Q(m-d)=O(m^{n-1}).
```
The last assertion uses Ehrhart’s theorem: $`Q`$ is an integral, full-dimensional polytope, containing $`0,e_1,\ldots,e_n`$, so $`E_Q`$ is a polynomial of degree $`n`$. Finally $`H_G`$ is the Hilbert function of the standard graded affine semigroup algebra $`\Bbbk[S]`$, and is therefore eventually polynomial by the Hilbert–Serre theorem. Their difference is eventually polynomial as well. $`\square`$

<!-- end proof-3 -->

<a id="lemma-3"></a>

**Lemma 3.2.**

<a id="label-lem-half"></a>

Every vertex of $`P`$ has coordinates in $`\{0,1/2,1\}`$.

<!-- end lemma-3 -->

<a id="proof-4"></a>

**Proof.**

Let $`b`$ be a vertex. Consider the graph on coordinates with $`0<b_i<1`$, retaining the edges on which $`b_i+b_j=1`$. A tight edge cannot join a fractional coordinate to a coordinate equal to zero or one. If a connected component of this tight graph is bipartite, add $`\varepsilon`$ on one side and subtract it on the other. For sufficiently small positive and negative $`\varepsilon`$, every nontight inequality and every coordinate bound remains satisfied. This contradicts extremality. Every component therefore has an odd cycle. The tight equations around that cycle force all its coordinates to be $`1/2`$, and the same equations propagate this value throughout the component. $`\square`$

<!-- end proof-4 -->

<a id="proof-5"></a>

**Proof of Theorem [1.1](#label-thm-main).**

Proposition [2.2](#label-prop-dictionary) and Lemma [3.1](#label-lem-conductor) give the identities and correction estimate. Since $`Q\subseteq[0,1]^n`$ satisfies the edge inequalities, its lattice points are exactly the independent-set indicators. Thus $`E_Q(m)=H_G(m)`$ for every $`m`$ is precisely the integer decomposition property of $`Q`$.

By Lemma [3.2](#label-lem-half) and Ehrhart’s theorem, $`E_P`$ is a quasipolynomial of period dividing two, with both branches having leading term $`\operatorname{vol}(P)m^n`$. Also
```math
E_Q(m)=\operatorname{vol}(Q)m^n+O(m^{n-1}),\qquad
H_G(m)=\operatorname{vol}(Q)m^n+O(m^{n-1}).
```
The asserted eventual quasipolynomiality and asymptotic expansions follow.

Suppose first that $`G`$ is bipartite with parts $`U,V`$. For $`b\in mP\cap\mathbb Z^n`$, assign vertex $`i\in U`$ the first $`b_i`$ colors from $`[m]`$, and vertex $`j\in V`$ the last $`b_j`$ colors. Adjacent vertices receive disjoint color sets because $`b_i+b_j\leq m`$. Each color class is therefore independent, giving a representation of $`b`$ in $`B_m`$. Isolated vertices can be placed in either part. Hence $`B_m=mP\cap\mathbb Z^n`$ and both defects vanish.

If $`G`$ is not bipartite, choose an odd cycle with $`2r+1`$ vertices. On its vertex set the coordinate sum of any point of $`Q`$ is at most $`r`$. The point $`(1/2,\ldots,1/2)`$ belongs to $`P`$ and violates that inequality, so $`Q\subsetneq P`$. Both polytopes are full-dimensional. Their strict containment gives $`\operatorname{vol}(Q)<\operatorname{vol}(P)`$: moving a point of $`P\setminus Q`$ slightly toward an interior point of $`P`$ produces a small open ball in $`P`$ disjoint from the closed set $`Q`$. Thus $`c_G>0`$. It follows that both parity branches have degree exactly $`n`$, and that $`i_m>0`$ eventually. Dividing the two asymptotic expansions proves the ratio limit. $`\square`$

<!-- end proof-5 -->

## 4. An exact correction from two odd cycles

Let $`C`$ be an odd cycle and $`b`$ a nonnegative integral demand vector on its vertices. Put $`T=\sum_i b_i`$ and define
```math
\begin{align*}
\nu^*(b)&=\max\left\{\sum_{e\in E(C)}\lambda_e:
\lambda_e\geq0,\ \sum_{e\ni i}\lambda_e\leq b_i\right\},\\
\nu(b)&=\max\left\{\sum_{e\in E(C)}\lambda_e:
\lambda_e\in\mathbb N,\ \sum_{e\ni i}\lambda_e\leq b_i\right\}.
\end{align*}
```
Repeated use of an edge is allowed in this capacitated matching problem.

<a id="lemma-4"></a>

**Lemma 4.1.**

<a id="label-lem-cycle"></a>

One has $`\nu(b)=\lfloor\nu^*(b)\rfloor`$. A noninteger value of $`\nu^*(b)`$ occurs exactly when the full saturation equations $`\lambda_{i-1}+\lambda_i=b_i`$ have a nonnegative, nonintegral solution. In that case the solution is unique, every edge weight is a positive halfinteger, $`T`$ is odd, and $`\nu^*(b)=T/2`$.

<!-- end lemma-4 -->

<a id="proof-6"></a>

**Proof.**

Choose an optimal vertex of the bounded fractional matching polytope. If an edge coordinate is zero, its positive support is a disjoint union of paths. The vertex-edge incidence matrix of a bipartite graph is totally unimodular: changing signs on the rows of one bipartition gives an oriented incidence matrix, whose square subdeterminants are $`0,1,-1`$. Thus the resulting active system with integral right-hand side has an integral vertex.

If every edge coordinate is positive, extremality requires every vertex inequality to be tight; otherwise there are fewer active constraints than edge variables. The incidence matrix of an odd cycle is nonsingular, as its homogeneous equations alternate signs and the odd closing condition forces zero. Solving successively shows that its saturated solution is either integral or has every coordinate in $`\mathbb Z+1/2`$. In the latter case all coordinates are at least $`1/2`$, and $`T`$ is odd. Round consecutive edge coordinates alternately down, up, down, up, ending down. All vertex sums remain unchanged except the one between the first and last edges, where the sum decreases by one. The resulting integral matching has weight $`(T-1)/2`$.

This proves the floor identity. Conversely, any feasible nonintegral saturated solution attains the universal upper bound $`T/2`$, and its uniform halfintegrality on an odd number of edges makes $`T`$ odd. $`\square`$

<!-- end proof-6 -->

<a id="proof-7"></a>

**Proof of Theorem [1.2](#label-thm-correction).**

Set $`F=\overline G=C_r\sqcup C_s`$. Because both cycles have length at least five, the independent sets of $`G`$ are exactly the empty set, singletons, and edges of $`F`$. For $`b\in\mathbb N^n`$, put $`T=\sum_i b_i`$, and let $`\nu_j^*,\nu_j`$ be the two matching numbers on component $`j`$. Then

<a id="label-eq-fractional-test"></a>

<a id="label-eq-integer-test"></a>

```math
\begin{align}
b\in mQ&\quad\Longleftrightarrow\quad
T-\nu_1^*(b)-\nu_2^*(b)\leq m,\tag{8}\\
b\in B_m&\quad\Longleftrightarrow\quad
T-\nu_1(b)-\nu_2(b)\leq m.\tag{9}
\end{align}
```
Indeed a choice of edge weights leaves nonnegative residual demands filled by singleton weights. The total coefficient mass is $`T-\sum_e\lambda_e`$; empty-set weights fill any remaining mass up to $`m`$. This argument works over the nonnegative reals for [(8)](#label-eq-fractional-test) and over the nonnegative integers for [(9)](#label-eq-integer-test).

If both fractional optima are integral, the two tests coincide. If just one is a halfinteger, rounding the fractional threshold up to the integer $`m`$ again gives the ordinary threshold. Thus a hole $`b\in(mQ\cap\mathbb Z^n)\setminus B_m`$ can occur only when both fractional optima are halfintegers. By Lemma [4.1](#label-lem-cycle), each component is then fully saturated by its unique positive halfintegral edge vector, and its demand total is odd. The fractional threshold is $`T/2`$, an integer, whereas the ordinary threshold is $`T/2+1`$. Consequently a hole occurs exactly when $`T=2m`$ and both saturation solutions are positive halfintegral. This also excludes holes away from the face $`\sum_i b_i=2m`$.

Write these edge weights as $`\lambda_e=k_e+1/2`$, with $`k_e\in\mathbb N`$. The block incidence matrix of the two odd cycles is nonsingular, so edge weights determine demands injectively. Conversely every such edge vector gives integral nonnegative demands, odd component totals, and the hole condition at degree $`m=\sum_e\lambda_e`$. We have obtained a bijection between degree-$`m`$ holes and
```math
\left\{(k_e)_{e\in E(F)}\in\mathbb N^n:
\sum_e k_e=m-\frac n2\right\}.
```
Stars and bars gives [(3)](#label-eq-correction), by Theorem [1.1](#label-thm-main). Its first degree and leading coefficient follow immediately. $`\square`$

<!-- end proof-7 -->

<a id="remark-1"></a>

**Remark 4.2.**

Equivalently, the Hilbert-series correction for this family is
```math
\sum_{m\geq0}(s_m-i_m)t^m=\frac{t^{n/2}}{(1-t)^n}.
```
The correction consists of a translate of the free monoid on the $`n`$ edge vectors of $`C_r\sqcup C_s`$. For $`r=s=5`$, its first values are $`0,0,0,0,1,10,55`$ in degrees $`1`$ through $`7`$.

<!-- end remark-1 -->

The same threshold argument gives a composition formula with any number of odd-cycle components. The factors below are the Hilbert series of single-component stable-set rings, so the formula uses ordinary Hilbert data to recover the entire normalization correction of their graph join.

<a id="proposition-2"></a>

**Proposition 4.3.**

<a id="label-prop-composition"></a>

Suppose $`\overline G=\bigsqcup_{a=1}^t C_{r_a}`$, with every $`r_a\geq5`$ odd. Let
```math
\begin{align*}
\mathcal H_a(z)&=\sum_{m\geq0}H_{\overline{C_{r_a}}}(m)z^m,
&V_a(z)&=\frac{z^{(r_a+1)/2}}{(1-z)^{r_a}},\\
U_a(z)&=(1-z)\mathcal H_a(z)-V_a(z).
\end{align*}
```
Then

<a id="label-eq-composition"></a>

```math
\tag{10}
\sum_{m\geq0}(s_m-i_m)z^m
=\sum_{\substack{F\subseteq[t]\\ |F|\geq2}}
\left(\sum_{j=1}^{\lfloor|F|/2\rfloor}z^{-j}\right)
\prod_{a\in F}V_a(z)\prod_{a\notin F}U_a(z).
```

The right-hand side is a formal power series with nonnegative exponents. For $`t=2`$ it equals
```math
\frac{z^{(r_1+r_2)/2}}{(1-z)^{r_1+r_2}}.
```

<!-- end proposition-2 -->

<a id="proof-8"></a>

**Proof.**

For a demand vector on component $`a`$, let $`c_a=T_a-\nu_a`$ be its minimum ordinary coefficient mass, and mark the component if $`\nu_a^*`$ is a halfinteger. By Lemma [4.1](#label-lem-cycle), the minimum fractional mass is $`c_a`$ on an unmarked component and $`c_a-1/2`$ on a marked one. In particular the single-component polytope has the integer decomposition property: for an integer degree, its fractional and ordinary feasibility thresholds agree.

The series counting all component demands by their minimum ordinary mass is $`(1-z)\mathcal H_a(z)`$, since the Hilbert function counts demands whose minimum mass is at most the given degree. A marked component has unique edge weights $`k_e+1/2`$ and
```math
c_a=\sum_e k_e+\frac{r_a+1}{2}.
```
Thus $`V_a`$ counts the marked demands by $`c_a`$, and $`U_a`$ counts the unmarked demands. All coefficients are nonnegative and each coefficient is finite, because total demand is at most twice the minimum mass.

For a demand on all components, put $`C=\sum_a c_a`$ and let $`F`$ be the set of marked components. Independent sets of $`G`$ lie within a single component of its complement, so the ordinary minimum mass is $`C`$ and the fractional minimum mass is $`C-|F|/2`$. Its missing degrees are exactly $`C-j`$, for $`1\leq j\leq\lfloor|F|/2\rfloor`$. Multiplying the component demand series and recording those degrees gives [(10)](#label-eq-composition). Each factor $`V_a`$ starts in degree at least three, so the displayed negative powers cannot create negative exponents. The specialization $`t=2`$ follows directly. $`\square`$

<!-- end proof-8 -->

## 5. Complete cores

<a id="proof-9"></a>

**Proof of Theorem [1.3](#label-thm-complete).**

For $`K_n`$, independent sets are empty or singletons. Hence
```math
B_m=\{b\in\mathbb N^n:\textstyle\sum_i b_i\leq m\},\qquad
H_G(m)=E_Q(m)=\binom{m+n}{n}.
```
It remains to count integral $`b`$ with $`0\leq b_i\leq m`$ and $`b_i+b_j\leq m`$ for distinct $`i,j`$. Put $`q=\lfloor m/2\rfloor`$. If every coordinate is at most $`q`$, there are $`(q+1)^n`$ choices. Otherwise exactly one coordinate exceeds $`q`$. If that coordinate is $`a`$, every other coordinate ranges independently from $`0`$ to $`m-a`$; their mutual pair constraints are automatic. The additional count is
```math
n\sum_{a=q+1}^m(m-a+1)^{n-1}.
```
Separating even and odd $`m`$ and subtracting $`\binom{m+n}{n}`$ proves [(4)](#label-eq-even)–[(5)](#label-eq-odd). The same partition works for $`n=1`$, where the coordinate bound is retained even though there are no edges. For $`n=1,2`$ the graph is bipartite, so the defect vanishes. Finally, for $`n\geq3`$ the power-sum estimate $`\sum_{k=1}^q k^{n-1}=q^n/n+O(q^{n-1})`$ gives leading coefficient $`2^{1-n}-1/n!`$. It is positive because $`n!>2^{n-1}`$ for $`n\geq3`$. $`\square`$

<!-- end proof-9 -->

In particular the whiskered triangle has $`s_2=1`$ and $`s_3=3`$. The calculation includes the obstruction in [\[2, Remark 5.3\]](#ref-DG) without using the indecomposability recursion.

### Verification and scope

The proofs above are independent of computation. Ancillary scripts check direct minimality of symbolic exponent vectors on all core graphs with at most three vertices and powers at most three; ordinary and symbolic counting on all $`1099`$ labeled graphs with at most five vertices in powers one through three; and the complete-core formulas for $`n,m\leq6`$. A separate check compares fractional matching vertex enumeration with exact integer matching dynamic programming on $`11628`$ demand vectors on $`C_5`$, and verifies the two-component correction through degree seven. All checks pass. The fractional vertex calculation uses numerical linear algebra with a checked halfinteger tolerance; Lemma [4.1](#label-lem-cycle) supplies the exact argument.

The results concern the fully whiskered cover-ideal class. They neither classify normal stable-set polytopes nor determine the minimal quasiperiod for arbitrary cores. The complete-core formula and the nonnormal correction family are parts of the same comparison theorem.

## References

<a id="ref-BHL"></a>

**\[1\]** A. Banerjee, T. H. Hà, and V. B. Lama, *Defect Functions Between Filtrations of Ideals*, preprint (2025), [arXiv:2512.14573](https://arxiv.org/abs/2512.14573).

<a id="ref-DG"></a>

**\[2\]** B. Drabkin and L. Guerrieri, *Asymptotic invariants of ideals with Noetherian symbolic Rees algebra and applications to cover ideals*, J. Pure Appl. Algebra **224** (2020), 300–319. [doi:10.1016/j.jpaa.2019.05.008](https://doi.org/10.1016/j.jpaa.2019.05.008).

<a id="ref-DGFreiman"></a>

**\[3\]** B. Drabkin and L. Guerrieri, *On quasi-equigenerated and Freiman cover ideals of graphs*, Comm. Algebra **48** (2020), no. 10, 4413–4435. [doi:10.1080/00927872.2020.1762890](https://doi.org/10.1080/00927872.2020.1762890).

<a id="ref-HHO"></a>

**\[4\]** G. Hamano, T. Hibi, and H. Ohsugi, *Ehrhart series of fractional stable set polytopes of finite graphs*, Ann. Comb. **22** (2018), 563–573. [doi:10.1007/s00026-018-0392-2](https://doi.org/10.1007/s00026-018-0392-2).

<a id="ref-Higashitani"></a>

**\[5\]** A. Higashitani, *Difference of Hilbert series of homogeneous monoid algebras and their normalizations*, Semigroup Forum **108** (2024), 101–114. [doi:10.1007/s00233-024-10414-0](https://doi.org/10.1007/s00233-024-10414-0).

<a id="ref-MOS"></a>

**\[6\]** K. Matsuda, H. Ohsugi, and K. Shibata, *Toric Rings and Ideals of Stable Set Polytopes*, Mathematics **7** (2019), no. 7, article 613. [doi:10.3390/math7070613](https://doi.org/10.3390/math7070613).

<a id="ref-Oltsik"></a>

**\[7\]** B. R. Oltsik, *Symbolic Defect of Monomial Ideals*, Comm. Algebra **52** (2024), no. 9, 3996–4012; [arXiv:2310.12280](https://arxiv.org/abs/2310.12280).
