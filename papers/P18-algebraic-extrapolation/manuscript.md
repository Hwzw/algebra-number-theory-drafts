# Integer-polynomial lifting and the classification of algebraic extrapolation sets

Henry Zweiman

September 9, 2026

## Abstract

For a complex parameter $`\lambda`$, let $`Q_\lambda`$ be the closure of $`\{0,1\}`$ under the operation $`(a,b)\mapsto(1-\lambda)a+\lambda b`$, without taking topological closure. We characterize $`Q_\lambda`$ for every algebraic integer $`\lambda\ne0,1`$ by inequalities at its conjugates in $`(0,1)`$ and two endpoint congruences. The proof lifts polynomial residue classes to integer polynomials strictly between zero and one on $`(0,1)`$, using classical integer-coefficient approximation with control at the endpoints. Together with the algebraic-integrality theorem of Fenner, Green, and Homer, the characterization proves that $`Q_\lambda`$ is discrete exactly when $`\lambda`$ is a strong PV number. Every nondegenerate discrete $`Q_\lambda`$ is a Meyer set, and equality with the unrestricted internal-cube model set is determined by the two integers $`|m_\lambda(0)|`$ and $`|m_\lambda(1)|`$. We also prove finite generation of the entire cube model set, with a seed of size at most $`|m_\lambda(0)m_\lambda(1)|+2`$. These results resolve the corresponding extrapolation questions in all degrees.

## 1. Introduction and results

For $`\lambda\in\mathbb C`$ and $`S\subseteq\mathbb C`$, let $`Q_\lambda(S)`$ be the least superset of $`S`$ closed under
```math
a\star_\lambda b=(1-\lambda)a+\lambda b,
 \qquad Q_\lambda=Q_\lambda(\{0,1\}).
```
Only finite expressions are allowed in $`Q_\lambda(S)`$. Its topological closure is a different object.

A *strong PV number* is an algebraic integer whose conjugates other than itself and its complex conjugate all belong to $`(0,1)`$. This includes every rational integer and every nonreal quadratic integer. Fenner, Green, and Homer [\[1\]](#ref-FGH2026) relate extrapolation sets to aperiodic order and prove discreteness for strong PV parameters. Their Section 11 asks for the converse, relative density, equality with the natural model set, and finite generation of that model set. Earlier versions of these questions appear in [\[3,2\]](#ref-FGH2018).

Our main tool is an exact lifting result for integer polynomials modulo a prescribed polynomial. Its arithmetic consequence is the following theorem.

<a id="theorem-1"></a>

**Theorem 1.**

<a id="label-thm-arithmetic"></a>

Let $`\lambda\ne0,1`$ be an algebraic integer, let $`m\in\mathbb Z[X]`$ be its monic minimal polynomial, and put $`\mathcal O=\mathbb Z[\lambda]`$. Let $`\mu_1,\ldots,\mu_k`$ be all the conjugates of $`\lambda`$ in $`(0,1)`$, and let $`\sigma_i:\mathbb Q(\lambda)\to\mathbb R`$ send $`\lambda`$ to $`\mu_i`$. Then

<a id="label-eq-criterion"></a>

```math
\tag{1}
\begin{split}
 Q_\lambda=\{0,1\}\ \cup\ \{a\in\mathcal O:\;&0<\sigma_i(a)<1\quad(1\le i\le k),\\
 &a\bmod\lambda\mathcal O\in\{0,1\},\\
 &a\bmod(1-\lambda)\mathcal O\in\{0,1\}\}.
\end{split}
```

Here $`\{0,1\}`$ in a quotient means the images of those integers, which may coincide. If $`k=0`$, the inequalities impose no restriction. If $`\lambda\in(0,1)`$, its identity embedding is among the $`\sigma_i`$.

<!-- end theorem-1 -->

The two quotient rings are particularly simple:

<a id="label-eq-endpoints"></a>

```math
\tag{2}
 \mathcal O/\lambda\mathcal O\cong\mathbb Z/m(0)\mathbb Z,\qquad
 \mathcal O/(1-\lambda)\mathcal O\cong\mathbb Z/m(1)\mathbb Z.
```

They record evaluation at $`0`$ and $`1`$ of a polynomial representative. No maximal-order hypothesis is imposed on $`\mathcal O`$.

<a id="theorem-2"></a>

**Theorem 2.**

<a id="label-thm-discrete"></a>

For every $`\lambda\in\mathbb C`$, the set $`Q_\lambda`$ is discrete if and only if $`\lambda`$ is a strong PV number.

<!-- end theorem-2 -->

For the remaining results, take a strong PV number $`\lambda\ne0,1`$ and retain the notation of Theorem [1](#label-thm-arithmetic). Put
```math
a^*=(\sigma_1(a),\ldots,\sigma_k(a)),\qquad
 M_\lambda=\{a\in\mathcal O:a^*\in[0,1]^k\},\qquad
 I=\lambda(1-\lambda)\mathcal O.
```
When $`k=0`$, set $`M_\lambda=\mathcal O`$. The physical space $`F`$ is $`\mathbb R`$ for real $`\lambda`$ and $`\mathbb C\cong\mathbb R^2`$ for nonreal $`\lambda`$. A set is *relatively dense* if every point of the physical space is within a fixed distance of it. It is a *Meyer set* if it is relatively dense and its difference set is uniformly discrete.

<a id="theorem-3"></a>

**Theorem 3.**

<a id="label-thm-model"></a>

For every strong PV number $`\lambda\ne0,1`$, the set $`Q_\lambda`$ is a model set with internal group
```math
\mathbb R^k\times(\mathcal O/I),
```
and it is a Meyer set in $`F`$. Moreover,

<a id="label-eq-equality"></a>

```math
\tag{3}
 Q_\lambda=M_\lambda
 \quad\Longleftrightarrow\quad
 |m(0)|\le2\ \hbox{ and }\ |m(1)|\le2.
```

For a nonreal quadratic integer $`\lambda`$, the set $`Q_\lambda`$ is a finite union of cosets of the lattice $`I`$ and is therefore periodic.

<!-- end theorem-3 -->

<a id="theorem-4"></a>

**Theorem 4.**

<a id="label-thm-finite"></a>

For every strong PV number $`\lambda\ne0,1`$, there is a finite set $`Y\subseteq M_\lambda`$ such that
```math
Q_\lambda(Y)=M_\lambda,\qquad
 |Y|\le |m(0)m(1)|+2.
```
One may take representatives in $`M_\lambda`$ of all residue classes modulo $`I`$, together with $`0`$ and $`1`$.

<!-- end theorem-4 -->

<a id="corollary-1"></a>

**Corollary 5.**

<a id="label-cor-relative"></a>

The set $`Q_\lambda`$ is relatively dense in $`\mathbb R`$ for every $`\lambda\in\mathbb R\setminus[0,1]`$, and in $`\mathbb C`$ for every $`\lambda\in\mathbb C\setminus\mathbb R`$.

<!-- end corollary-1 -->

Theorem [2](#label-thm-discrete) proves [\[1, Conjecture 11.1\]](#ref-FGH2026). Theorem [3](#label-thm-model) answers Question 11.2 and the quadratic Question 11.6; Corollary [5](#label-cor-relative) answers Question 11.3. Theorem [4](#label-thm-finite) proves the finite-generation assertions of Conjectures 11.4–11.5 for nondegenerate parameters. If the phrase “any strong PV number” in Conjecture 11.5 is read literally to include $`0`$ and $`1`$, these are exceptions: $`Q_0(Y)=Q_1(Y)=Y`$, whereas $`M_0=M_1=\mathbb Z`$ under the empty-window convention. Throughout our finite-generation statements they are explicitly excluded.

The quadratic cases of [(3)](#label-eq-equality) recover the four families already classified in [\[1, Theorem 6.9\]](#ref-FGH2026). The contribution is the exact arithmetic description and its consequences in arbitrary degree. These consequences use one common argument, rather than separate classifications by dimension.

## 2. Integer approximation and finite extrapolation trees

We first record two classical approximation facts in a form that makes integrality explicit. The first is the integer-approximation theorem of Chlodovsky and Kantorovich; see [\[4\]](#ref-GL) for its history and quantitative refinements.

<a id="lemma-1"></a>

**Lemma 6.**

<a id="label-lem-approx"></a>

If $`h:[0,1]\to\mathbb R`$ is continuous and $`h(0),h(1)\in\mathbb Z`$, then for every $`\varepsilon>0`$ there is $`H\in\mathbb Z[X]`$ with $`\|H-h\|_\infty<\varepsilon`$.

<!-- end lemma-1 -->

<a id="proof-1"></a>

**Proof.**

The ordinary Bernstein polynomial is
```math
B_nh(X)=\sum_{j=0}^n\binom nj h(j/n)X^j(1-X)^{n-j}.
```
Round each coefficient $`\binom njh(j/n)`$ to the nearest integer. The coefficients for $`j=0,n`$ are already integral. Since $`\binom nj\ge n`$ for $`1\le j\le n-1`$, the resulting integer polynomial $`H_n`$ satisfies
```math
|H_n(t)-B_nh(t)|
 \le\frac12\sum_{j=1}^{n-1}t^j(1-t)^{n-j}
 \le\frac1{2n}\qquad(0\le t\le1).
```
Bernstein’s uniform approximation theorem now gives $`H_n\to h`$ uniformly. $`\square`$

<!-- end proof-1 -->

<a id="lemma-2"></a>

**Lemma 7.**

<a id="label-lem-positive"></a>

Let $`p\in\mathbb R[X]`$ be strictly positive on $`(0,1)`$ and nonnegative at both endpoints. For every sufficiently large $`n`$, its coefficients in the basis
```math
X^j(1-X)^{n-j},\qquad 0\le j\le n,
```
are nonnegative. If $`p\in\mathbb Z[X]`$, those coefficients are integers.

<!-- end lemma-2 -->

<a id="proof-2"></a>

**Proof.**

Factor $`p=X^a(1-X)^b h`$, where $`a,b\ge0`$ and $`h>0`$ on $`[0,1]`$. For a fixed polynomial $`h(X)=\sum_{s=0}^d h_sX^s`$, its normalized Bernstein coefficients of degree $`n\ge d`$ are
```math
\beta_{j,n}=\sum_{s=0}^d h_s\frac{(j)_s}{(n)_s},
```
where $`(j)_s=j(j-1)\cdots(j-s+1)`$ and $`(j)_0=1`$. For each fixed $`s`$, the quotient $`(j)_s/(n)_s`$ differs from $`(j/n)^s`$ by $`O_s(1/n)`$ uniformly in $`0\le j\le n`$. Thus $`\beta_{j,n}-h(j/n)\to0`$ uniformly. The positive minimum of $`h`$ gives positivity of all $`\beta_{j,n}`$ for large $`n`$. Multiplication by $`X^a(1-X)^b`$ preserves nonnegativity in the unnormalized basis.

For integrality, use
```math
X^s=\sum_{j=s}^n\binom{n-s}{j-s}X^j(1-X)^{n-j}.
```
Every integer polynomial of degree at most $`n`$ consequently has integer coefficients in this basis. $`\square`$

<!-- end proof-2 -->

<a id="lemma-3"></a>

**Lemma 8.**

<a id="label-lem-tree"></a>

Suppose $`p_1,\ldots,p_l\in\mathbb Z[X]`$ sum to $`1`$, and each is either zero or strictly positive on $`(0,1)`$ and nonnegative at the endpoints. For arbitrary $`y_1,\ldots,y_l\in\mathbb C`$ and $`\lambda\in\mathbb C`$,
```math
\sum_{i=1}^l p_i(\lambda)y_i\in Q_\lambda(\{y_1,\ldots,y_l\}).
```

<!-- end lemma-3 -->

<a id="proof-3"></a>

**Proof.**

Choose one large degree $`n`$ for all the polynomials in Lemma [7](#label-lem-positive). Write their unnormalized coefficients as $`c_{i,j}\in\mathbb Z_{\ge0}`$. The partition identity gives
```math
\sum_{i=1}^l c_{i,j}=\binom nj.
```
A complete binary extrapolation tree of depth $`n`$ has exactly $`\binom nj`$ leaves with $`j`$ right branches. Each such leaf has weight $`\lambda^j(1-\lambda)^{n-j}`$. Label exactly $`c_{i,j}`$ of them by $`y_i`$. The tree evaluates to the desired sum. $`\square`$

<!-- end proof-3 -->

<a id="corollary-2"></a>

**Corollary 9.**

<a id="label-cor-polynomials"></a>

An integer polynomial is generated from $`0,1`$ by $`(p,q)\mapsto(1-X)p+Xq`$ if and only if it is $`0`$, $`1`$, or strictly between $`0`$ and $`1`$ on $`(0,1)`$.

<!-- end corollary-2 -->

<a id="proof-4"></a>

**Proof.**

Finite trees give the necessity: at an interior argument all leaf weights are positive, so a tree using both labels has value strictly between zero and one. Conversely, a polynomial $`p`$ strictly between zero and one has endpoint values in $`\{0,1\}`$, and Lemma [8](#label-lem-tree) applied to $`1-p,p`$ constructs the required tree. $`\square`$

<!-- end proof-4 -->

This is the characterization of [\[1, Theorem 3.6\]](#ref-FGH2026). We have included a proof to make the finite-tree step, also needed with more than two leaf labels, self-contained.

## 3. Lifting with endpoint control

<a id="lemma-4"></a>

**Lemma 10.**

<a id="label-lem-weighted"></a>

Let $`m,R,w\in\mathbb Z[X]`$ satisfy $`m(0)m(1)\ne0`$ and $`w(t)>0`$ on $`(0,1)`$. Suppose there are integers $`h_0,h_1`$ such that, on putting
```math
H_0=(1-X)h_0+Xh_1,\qquad F_0=R+mX(1-X)H_0,
```
the following conditions hold:

1.  $`0<R(\mu)<w(\mu)`$ at every real zero $`\mu`$ of $`m`$ in $`(0,1)`$;

2.  near each endpoint, $`0<F_0(t)<w(t)`$ and both $`F_0(t)`$ and $`w(t)-F_0(t)`$ are at least a positive constant times $`t(1-t)`$.

Then some $`H\in\mathbb Z[X]`$ makes
```math
P=R+mX(1-X)H
```
satisfy $`0<P(t)<w(t)`$ for every $`0<t<1`$.

<!-- end lemma-4 -->

<a id="proof-5"></a>

**Proof.**

Let $`W=mX(1-X)`$. By the first condition and continuity, $`0<F_0<w`$ also holds in neighborhoods of the interior real zeros of $`m`$. Choose a continuous function $`\chi:[0,1]\to[0,1]`$ that vanishes on smaller neighborhoods of all these zeros and the endpoints, equals one outside slightly larger neighborhoods, and transitions only where $`0<F_0<w`$. Such a function can be chosen piecewise linear. Define
```math
h=H_0+\chi\frac{w/2-F_0}{W},
```
where the second term is extended by zero near the zeros of $`W`$. Then $`h`$ is continuous and its endpoint values are the integers $`h_0,h_1`$. Also
```math
F:=R+Wh=(1-\chi)F_0+\chi w/2
```
lies strictly between zero and $`w`$ throughout $`(0,1)`$. It agrees with $`F_0`$ near the endpoints. The endpoint lower bounds and compactness of the remaining interval give $`\eta>0`$ such that
```math
\min(F(t),w(t)-F(t))\ge\eta t(1-t)\qquad(0\le t\le1).
```
By Lemma [6](#label-lem-approx), choose $`H\in\mathbb Z[X]`$ with
```math
\|H-h\|_\infty<\frac{\eta}{\max_{[0,1]}|m|}.
```
Then $`|P(t)-F(t)|<\eta t(1-t)`$ on $`(0,1)`$, proving the assertion. $`\square`$

<!-- end proof-5 -->

<a id="theorem-5"></a>

**Theorem 11.**

<a id="label-thm-lift"></a>

Let $`m,p\in\mathbb Z[X]`$ with $`m(0)m(1)\ne0`$. There is $`P\in p+m\mathbb Z[X]`$ satisfying $`0<P(t)<1`$ for all $`0<t<1`$ if and only if

<a id="label-eq-liftconditions"></a>

```math
\tag{4}
\begin{gathered}
 0<p(\mu)<1\quad\hbox{at every real zero $\mu$ of $m$ in $(0,1)$},\\
 p(0)\bmod m(0)\in\{0,1\},\qquad
 p(1)\bmod m(1)\in\{0,1\}.
\end{gathered}
```

<!-- end theorem-5 -->

<a id="proof-6"></a>

**Proof.**

Necessity follows by evaluation, including continuity and integrality at the endpoints. Conversely, choose $`e_0,e_1\in\{0,1\}`$ in the specified residue classes. There is an integer linear polynomial $`q_0`$ with
```math
q_0(0)=\frac{e_0-p(0)}{m(0)},\qquad
 q_0(1)=\frac{e_1-p(1)}{m(1)}.
```
Set $`R=p+mq_0`$, so $`R(0)=e_0`$ and $`R(1)=e_1`$. Adding $`mX(1-X)H_0`$ changes its endpoint derivatives to
```math
R'(0)+m(0)h_0,\qquad R'(1)-m(1)h_1.
```
Choose integers $`h_0,h_1`$ to make these derivatives strictly inward: at zero the sign is positive if $`e_0=0`$ and negative if $`e_0=1`$; at one the sign is negative if $`e_1=0`$ and positive if $`e_1=1`$. This is possible because $`m(0),m(1)`$ are nonzero. The resulting function and its complement have the required positive linear lower bounds near the endpoints. Apply Lemma [10](#label-lem-weighted) with $`w=1`$. The resulting $`P`$ still belongs to $`p+m\mathbb Z[X]`$. $`\square`$

<!-- end proof-6 -->

<a id="proof-7"></a>

**Proof of Theorem [1](#label-thm-arithmetic).**

Every element of $`Q_\lambda`$ is $`p(\lambda)`$ for a polynomial generated by a finite tree. Corollary [9](#label-cor-polynomials) gives its strict inequalities at the internal conjugates, unless it is $`0`$ or $`1`$, and its endpoint values give the two congruences.

Conversely, take $`a=p(\lambda)`$ satisfying [(1)](#label-eq-criterion). The kernel of evaluation $`\mathbb Z[X]\to\mathcal O`$ is $`m\mathbb Z[X]`$, since $`m`$ is monic. Reducing further modulo $`\lambda`$ or $`1-\lambda`$ gives [(2)](#label-eq-endpoints). Thus $`p`$ satisfies [(4)](#label-eq-liftconditions). Theorem [11](#label-thm-lift) gives a representative $`P`$ strictly between zero and one, and Corollary [9](#label-cor-polynomials) yields $`a=P(\lambda)\in Q_\lambda`$. $`\square`$

<!-- end proof-7 -->

## 4. Discreteness

We use the full Minkowski embedding of the number field $`K=\mathbb Q(\lambda)`$ into $`\mathbb R^r\times\mathbb C^s`$, treated as a real space of dimension $`[K:\mathbb Q]`$. The image of a nonzero ideal of the order $`\mathcal O`$ is a full lattice.

<a id="proof-8"></a>

**Proof of Theorem [2](#label-thm-discrete).**

If $`Q_\lambda`$ is discrete, then $`\lambda`$ is an algebraic integer by [\[2, Theorem 8.2\]](#ref-FGH2020); this theorem applies to arbitrary complex parameters. The values $`0,1`$ are strong PV and have $`Q_\lambda=\{0,1\}`$. For $`0<\lambda<1`$, iterated subdivision of $`[0,1]`$ at ratio $`\lambda`$ gives points in $`Q_\lambda`$ with largest gap at most $`\max(\lambda,1-\lambda)^n`$. Hence $`Q_\lambda`$ is dense in $`[0,1]`$, so this case is not discrete.

Suppose now that $`\lambda\notin[0,1]`$ is an algebraic integer that is not strong PV. In the Minkowski embedding distinguish the physical coordinate of $`\lambda`$ (a real coordinate or a complete complex pair) and the $`k`$ real internal coordinates in $`(0,1)`$. Since $`\lambda`$ is not strong PV, at least one real dimension is left over.

Put $`a_0=\lambda(1-\lambda)`$. Every internal value $`\mu_i(1-\mu_i)`$ lies strictly between zero and one. Fix $`\eta>0`$ smaller than its distance to each boundary; if $`k=0`$, choose any $`\eta>0`$. For each $`\varepsilon>0`$, consider the symmetric box in the Minkowski space that bounds each physical real coordinate by $`\varepsilon`$, each internal coordinate by $`\eta`$, and all remaining coordinates by $`T`$. Its volume tends to infinity with $`T`$. Minkowski’s convex body theorem therefore gives a nonzero $`\delta\in I`$ satisfying the physical and internal bounds for sufficiently large $`T`$.

Both $`a_0`$ and $`\delta`$ lie in $`I`$, and every internal value of $`a_0+\delta`$ lies in $`(0,1)`$. Theorem [1](#label-thm-arithmetic) implies $`a_0+\delta\in Q_\lambda`$. Letting $`\varepsilon\to0`$ gives nonzero physical values $`\delta\to0`$, because an embedding of a field is injective. Thus $`a_0`$ is an accumulation point of $`Q_\lambda`$, contradicting discreteness.

For the converse, let $`\lambda`$ be strong PV. It cannot belong to $`(0,1)`$, since then the product of all its conjugates would be a nonzero integer of absolute value less than one. The exceptional parameters $`0,1`$ were handled above. Otherwise the full Minkowski space consists exactly of the physical and internal coordinates. Formula [(1)](#label-eq-criterion) places $`Q_\lambda`$ inside $`M_\lambda`$. Differences of its points have internal coordinates in $`[-1,1]^k`$. A compact physical neighborhood times this internal cube meets the order lattice in finitely many points. The nonzero physical norms among them have a positive minimum, so $`Q_\lambda`$ is uniformly discrete. $`\square`$

<!-- end proof-8 -->

## 5. Arithmetic model sets

We give the needed density statement with proof to avoid assumptions about the order or its ideals.

<a id="lemma-5"></a>

**Lemma 12.**

<a id="label-lem-projection"></a>

Let $`J`$ be a full $`\mathbb Z`$-lattice in a number field $`K`$. Its projection onto any proper collection of real embeddings and complete complex pairs is dense in the corresponding real vector space.

<!-- end lemma-5 -->

<a id="proof-9"></a>

**Proof.**

On the full Minkowski space use the nondegenerate real bilinear form
```math
B(v,w)=\sum_{i=1}^r v_iw_i+2\operatorname{Re}\sum_{j=1}^s v_jw_j.
```
For field elements this is $`\operatorname{Tr}_{K/\mathbb Q}(ab)`$. The lattice dual to the image of $`J`$ for $`B`$ is the image of
```math
J^\vee=\{b\in K:\operatorname{Tr}_{K/\mathbb Q}(bJ)\subseteq\mathbb Z\}.
```
Indeed the trace-dual basis of a $`\mathbb Z`$-basis of $`J`$ lies in $`K`$, by nondegeneracy of the rational trace pairing.

If the projected subgroup were not dense, its closure would be a proper closed subgroup of a real vector space. The decomposition of such a subgroup into a vector space and a lattice gives a nonzero real linear functional taking integer values on it. Extend this functional by zero on the omitted coordinates. Its representing vector for $`B`$ belongs to the dual lattice and has zero in every omitted coordinate. Thus it is the image of some $`b\in K`$ with one embedding equal to zero. This forces $`b=0`$, contrary to the choice of the functional. $`\square`$

<!-- end proof-9 -->

Let $`C=\mathcal O/I`$. The two endpoint ideals are comaximal since $`\lambda+(1-\lambda)=1`$, so

<a id="label-eq-crt"></a>

```math
\tag{5}
 C\cong\mathbb Z/m(0)\mathbb Z\times\mathbb Z/m(1)\mathbb Z,
 \qquad |C|=|m(0)m(1)|.
```

Write $`E\subseteq C`$ for the pairs with each coordinate in $`\{0,1\}`$. For a strong PV parameter $`\lambda\ne0,1`$, define
```math
\mathcal L=\{(a,a^*,a\bmod I):a\in\mathcal O\}
 \subseteq F\times\mathbb R^k\times C.
```
This is a discrete cocompact subgroup. Discreteness follows from the Minkowski lattice; cocompactness follows by reducing the Minkowski coordinate into a compact fundamental region, leaving only the finite coordinate in $`C`$. Projection to the physical space is injective. Projection to the internal group $`\mathbb R^k\times C`$ is dense: in each residue class the real internal values are a translate of $`I^*`$, which is dense by Lemma [12](#label-lem-projection). When $`k=0`$, this says simply that the projection onto $`C`$ is surjective.

A *model set* for this scheme is obtained by retaining the physical coordinates of lattice points whose internal coordinates lie in a relatively compact window with nonempty interior. Set
```math
W=[0,1]^k\times E.
```
Any internal value of a field element equal to $`0`$ or $`1`$ forces the element itself to be $`0`$ or $`1`$. Thus Theorem [1](#label-thm-arithmetic) gives exactly

<a id="label-eq-model"></a>

```math
\tag{6}
 Q_\lambda=\{a\in\mathcal O:(a^*,a\bmod I)\in W\}.
```

The closed window makes no extraneous boundary points.

<a id="lemma-6"></a>

**Lemma 13.**

<a id="label-lem-meyer"></a>

The set in [(6)](#label-eq-model) is relatively dense and its difference set is uniformly discrete.

<!-- end lemma-6 -->

<a id="proof-10"></a>

**Proof.**

Choose a compact set $`K_0`$ with $`\mathcal L+K_0=F\times\mathbb R^k\times C`$. For a physical point $`x`$, write $`(x,0)=l+u`$ with $`l\in\mathcal L`$ and $`u\in K_0`$. The internal coordinate of $`l`$ belongs to a fixed compact set. For each possible internal value $`t`$, density of the internal projection gives $`l'\in\mathcal L`$ with $`t+l'_{\rm int}\in W^\circ`$. The same $`l'`$ works in a neighborhood of $`t`$, and compactness leaves only finitely many necessary choices of $`l'`$. Consequently $`l+l'`$ is a selected lattice point at uniformly bounded physical distance from $`x`$. This proves relative density.

A difference of two selected points has internal coordinate in $`W-W`$. A difference of two such differences has internal coordinate in $`W-W-W+W`$, a compact set. Discreteness of $`\mathcal L`$ implies that only finitely many lattice points have this internal constraint and physical norm at most one. Every nonzero such point has a nonzero physical coordinate by injectivity. Taking the minimum of their nonzero norms and one gives a positive separation bound for the difference set. $`\square`$

<!-- end proof-10 -->

<a id="proof-11"></a>

**Proof of Theorem [3](#label-thm-model).**

The model-set and Meyer assertions follow from [(6)](#label-eq-model) and Lemma [13](#label-lem-meyer). Every class modulo $`I`$ meets $`M_\lambda`$: for $`k>0`$ apply Lemma [12](#label-lem-projection) to $`I`$ and the open cube; for $`k=0`$ there is no internal restriction. Hence $`Q_\lambda=M_\lambda`$ holds exactly when $`E=C`$. By [(5)](#label-eq-crt), this is equivalent to each endpoint quotient having at most two elements, which is [(3)](#label-eq-equality). For a nonreal quadratic integer, $`k=0`$ and $`\mathcal O`$ is a lattice in $`\mathbb C`$; [(6)](#label-eq-model) is precisely a union of the cosets of $`I`$ indexed by $`E`$. $`\square`$

<!-- end proof-11 -->

<a id="proof-12"></a>

**Proof of Corollary [5](#label-cor-relative).**

Strong PV parameters in the indicated ranges are covered by Theorem [3](#label-thm-model). For every other parameter in these ranges, Theorem [2](#label-thm-discrete) gives nondiscreteness. By [\[2, Corollary 3.5 and Theorem 2.19\]](#ref-FGH2020), the topological closure is then $`\mathbb R`$ or $`\mathbb C`$, respectively. A dense subset of either space is relatively dense. $`\square`$

<!-- end proof-12 -->

## 6. Finite generation of the full cube

<a id="proof-13"></a>

**Proof of Theorem [4](#label-thm-finite).**

By Lemma [12](#label-lem-projection), every class in $`C`$ has a representative in $`M_\lambda`$. Choose such representatives and add $`0,1`$, obtaining $`Y`$ with the stated size bound. The set $`M_\lambda`$ is $`\lambda`$-convex because each internal operation is interpolation with parameter $`\mu_i\in(0,1)`$. Thus $`Q_\lambda(Y)\subseteq M_\lambda`$.

For the reverse inclusion, fix $`a\in M_\lambda\setminus\{0,1\}`$. Every internal coordinate of $`a`$ is strictly between zero and one. Choose $`y_L,y_R\in Y`$ such that
```math
a\equiv y_L\pmod{\lambda\mathcal O},\qquad
 a\equiv y_R\pmod{(1-\lambda)\mathcal O}.
```
Let $`r,u,v\in\mathbb Z[X]`$ represent $`a,y_L,y_R`$, respectively. For an integer $`N\ge2`$, put
```math
b_L=(1-X)^N,\qquad b_R=X^N,\qquad
 w=1-b_L-b_R,\qquad f=r-u b_L-v b_R.
```
As $`N\to\infty`$, the values $`b_L(\mu_i),b_R(\mu_i)`$ tend to zero. Choose $`N`$ large enough that

<a id="label-eq-finiteconditions"></a>

```math
\tag{7}
 0<f(\mu_i)<w(\mu_i)\quad(1\le i\le k),\qquad
 N>\max(|m(0)|,|m(1)|).
```

This is possible since $`0<\sigma_i(a)<1`$ and the internal seed values lie in $`[0,1]`$. If $`k=0`$, only the last inequality is needed.

The chosen residues give $`m(0)\mid f(0)`$ and $`m(1)\mid f(1)`$. Choose an integer linear polynomial $`q_0`$ so that $`R=f+mq_0`$ has both endpoint values zero. The derivatives after adding $`mX(1-X)H_0`$ are
```math
R'(0)+m(0)h_0,\qquad R'(1)-m(1)h_1.
```
Each runs through an integer residue class with modulus $`|m(0)|`$ or $`|m(1)|`$. An open interval of length $`N`$ larger than that modulus contains a member of every such class. Choose integers $`h_0,h_1`$ so that
```math
0<R'(0)+m(0)h_0<N,\qquad
 -N<R'(1)-m(1)h_1<0.
```
Since $`w'(0)=N`$ and $`w'(1)=-N`$, these inequalities ensure that both $`F_0`$ and $`w-F_0`$ have positive linear lower bounds near the endpoints. The internal inequalities in [(7)](#label-eq-finiteconditions) supply the other hypothesis of Lemma [10](#label-lem-weighted). We obtain an integer polynomial
```math
p_1\in f+m\mathbb Z[X],\qquad 0<p_1(t)<w(t)\quad(0<t<1),
```
with $`p_1(0)=p_1(1)=0`$. Set $`p_0=w-p_1`$. Then $`p_0,p_1,b_L,b_R`$ are integer polynomials, each positive on $`(0,1)`$ and nonnegative at both endpoints, and
```math
p_0+p_1+b_L+b_R=1.
```
Evaluation at $`\lambda`$ gives
```math
p_0(\lambda)\,0+p_1(\lambda)\,1+b_L(\lambda)y_L+b_R(\lambda)y_R=a.
```
By Lemma [8](#label-lem-tree), the right-hand side belongs to $`Q_\lambda(Y)`$. The elements $`0,1`$ were already in $`Y`$, completing the proof. $`\square`$

<!-- end proof-13 -->

The degree of the tree in this proof depends on the target point, including how close its internal coordinates are to the cube boundary. The theorem bounds the size of the seed, not the degree or the number of extrapolation steps uniformly over all points.

## 7. Examples and further directions

For an integer parameter $`q\ne0,1`$, the criterion reduces to
```math
Q_q=\{a\in\mathbb Z:a\bmod q\in\{0,1\},\quad
 a\bmod(1-q)\in\{0,1\}\}.
```
This recovers the integer classification in [\[2\]](#ref-FGH2020); it is not a new special case. For $`\lambda=2i`$, the order is $`\mathbb Z[2i]`$ and the minimal polynomial is $`X^2+4`$. Writing an element as $`a+2bi`$ gives the explicit periodic description
```math
Q_{2i}=\{a+2bi:a,b\in\mathbb Z,\quad
 a\bmod4\in\{0,1\},\quad(a+b)\bmod5\in\{0,1\}\}.
```
It consists of four cosets of the index-twenty lattice $`(4+2i)\mathbb Z[2i]`$.

As a higher-degree example, let $`\lambda`$ be the largest root of
```math
m(X)=X^3-6X^2+5X-1.
```
There is one root in each of $`(0,1/3)`$, $`(1/3,1)`$, and $`(5,6)`$, by sign changes; the rational-root test proves irreducibility. Thus $`\lambda`$ is strong PV. Since $`m(0)=m(1)=-1`$, Theorem [3](#label-thm-model) gives $`Q_\lambda=M_\lambda`$. By contrast, a strong PV minimal polynomial with $`|m(0)|>2`$ or $`|m(1)|>2`$ has a proper congruence restriction even though its extrapolation set is still Meyer and its full cube is finitely generated.

The lifting proof suggests quantitative questions about the smallest possible seed and the shortest extrapolation trees. Explicit degree bounds in terms of the internal distance to the boundary, the coefficients of $`m`$, and the chosen residue representatives would make the construction more effective. The present results establish exact membership, discreteness, and finite generation; they do not claim optimal seed size or optimal computational complexity.

## Preparation and verification

This manuscript was prepared with OpenAI Codex assistance in problem selection, proof development, literature checking, and writing. The originating agent performed the internal proof audit; no separate-agent or human referee review is claimed. The accompanying source assessment records the literature-search scope and the exact statements used from the extended source. Historical priority remains subject to scholarly review. The proofs above are general arguments; optional finite consistency checks supplied with the manuscript do not replace them.

## References

<a id="ref-FGH2026"></a>

**\[1\]** S. Fenner, F. Green, and S. Homer, *Fixed-Parameter Extrapolation and Aperiodic Order*, Discrete & Computational Geometry **76** (2026), 1–74. [doi:10.1007/s00454-025-00816-4](https://doi.org/10.1007/s00454-025-00816-4).

<a id="ref-FGH2020"></a>

**\[2\]** S. Fenner, F. Green, and S. Homer, *Fixed-Parameter Extrapolation and Aperiodic Order*, extended version, arXiv:1212.2889v6 (2020). [arXiv:1212.2889v6](https://arxiv.org/abs/1212.2889v6).

<a id="ref-FGH2018"></a>

**\[3\]** S. Fenner, F. Green, and S. Homer, *Fixed-Parameter Extrapolation and Aperiodic Order: Open Problems*, ACM SIGACT News **49**(3) (2018), 35–47. [doi:10.1145/3289137.3289145](https://doi.org/10.1145/3289137.3289145).

<a id="ref-GL"></a>

**\[4\]** C. S. Güntürk and W. Li, *Uniform Approximation by Polynomials with Integer Coefficients via the Bernstein Lattice*, arXiv:2311.10901v1 (2023). [arXiv:2311.10901v1](https://arxiv.org/abs/2311.10901v1).
