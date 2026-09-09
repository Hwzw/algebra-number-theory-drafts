# Exact Dold repair for matrix powers and integral recurrences

Henry Zweiman

September 8, 2026\
Research draft; AI-generated and not externally peer reviewed

## Abstract

We classify the integral matrices $`A`$ and positive exponents $`s`$ for which a fixed positive integer makes every entry of $`(A^{n^s})_{n\geq1}`$ satisfy the Dold congruences. Such an integer exists exactly when $`A`$ is semisimple over $`\mathbb Q`$ and the exponent of the Galois group of its minimal polynomial divides $`s`$. In that case the least multiplier is $`\prod_p p^{\lceil\log_{p^s}\nu_p(A)\rceil}`$, where $`\nu_p(A)`$ is the largest Jordan-block size modulo $`p`$. For a fixed monic recurrence polynomial $`F`$, initialized at $`u_1,\ldots,u_d`$, we obtain an analogous complete classification and an exact uniform multiplier from the largest root multiplicities of $`xF`$ modulo $`p`$. One integral initialization attains this uniform multiplier. The prime exponents are forced at an explicit critical local level. Consequences include the optimal universal sampling exponent $`\operatorname{lcm}(1,\ldots,d)`$ and the exact radical repair factor for fundamental Lucas sequences along even powers. The results concern Dold divisibility, without a nonnegativity assumption.

## 1. Introduction and statements

For an integer sequence $`a=(a_n)_{n\geq1}`$ put
```math
b_n(a)=\sum_{e\mid n}\mu(n/e)a_e.
```
The *Dold congruences* require $`n\mid b_n(a)`$ for every positive integer $`n`$. We write $`\operatorname{Fail}_{D}(a)`$ for the least positive integer $`C`$ for which $`(Ca_n)`$ satisfies these congruences, and set $`\operatorname{Fail}_{D}(a)=\infty`$ when no such integer exists. The condition $`b_n(a)\geq0`$, needed for an interpretation as orbit counts, is separate and is not imposed here. For matrix sequences, the same multiplier must repair every entry.

Power subsequences of linear recurrences have been studied in connection with realizability and its divisibility obstruction. Moss and Ward [\[5\]](#ref-MW) treated the Fibonacci sequence along even powers, and Luca and Ward [\[2\]](#ref-LW) proved sufficient general recurrence and Lucas results. The sufficient use of the Galois-group exponent is already explicit in [\[2, Theorem 1\]](#ref-LW). Rajs [\[6\]](#ref-Rajs) gives further scalar criteria and bounds. At exponent $`s=1`$, Minton’s classification identifies the scalar recurrence sequences admitting finite repair as trace sequences; see [\[4, Theorem 2.15 and Remark 2.16\]](#ref-Minton) and its formulation in [\[1, Theorem 2.4\]](#ref-BGW). Our classification concerns all matrix entries simultaneously, or all initializations for a fixed recurrence. It does not replace that scalar classification.

The main result determines both the allowable sampling exponents and the exact multiplier. Semisimple over $`\mathbb Q`$ will mean diagonalizable over $`\overline{\mathbb{Q}}`$, equivalently having a squarefree minimal polynomial. For a prime $`p`$, let $`\nu_p(A)`$ be the largest Jordan-block size of the reduction of $`A`$ over $`\overline{\mathbb{F}}_p`$. Define the integer threshold

<a id="label-eq-threshold"></a>

```math
\tag{1}
 \rho_{p,s}(t)=\min\{r\geq0:p^{sr}\geq t\}
             =\left\lceil\log_{p^s}t\right\rceil\qquad(t\geq1).
```

In particular, $`\rho_{p,s}(1)=0`$.

<a id="theorem-1"></a>

**Theorem 1 (Complete matrix classification).**

<a id="label-thm-matrix"></a>

Let $`A\in\operatorname{Mat}_N(\mathbb Z)`$, $`N\geq1`$, let $`m_A\in\mathbb Z[x]`$ be its monic minimal polynomial over $`\mathbb Q`$, and let $`G_A`$ be the Galois group of the splitting field of $`m_A`$. Fix $`s\geq1`$. A positive integer $`C`$ repairs $`(A^{n^s})_{n\geq1}`$ entrywise if and only if

1.  $`A`$ is semisimple over $`\mathbb Q`$;

2.  $`\exp(G_A)\mid s`$; and

3.  $`C_s(A)\mid C`$, where

    <a id="label-eq-matrixfactor"></a>

    ```math
    \tag{2}
     C_s(A)=\prod_p p^{\rho_{p,s}(\nu_p(A))}.
    ```

Under the first two conditions the product is finite. Its prime support is exactly the set of nonsemisimple reductions of $`A`$.

<!-- end theorem-1 -->

The precise group is the splitting-field group of the minimal polynomial, rather than of an arbitrarily chosen annihilator. The multiplier depends on the integral matrix: collisions between eigenvalues of a diagonal integral matrix do not create Jordan blocks, and such a matrix has multiplier $`1`$ for every $`s`$.

For recurrences, initialization at index $`1`$ affects the answer. Let

<a id="label-eq-recurrence"></a>

```math
\tag{3}
 F(x)=x^d+c_{d-1}x^{d-1}+\cdots+c_0\in\mathbb Z[x],\qquad
 u_{n+d}+\sum_{j=0}^{d-1}c_j u_{n+j}=0\quad(n\geq1),
```

where $`d\geq1`$. Let $`G_F`$ be the Galois group of the splitting field of $`F`$. For any monic polynomial $`H`$ of positive degree, let $`\nu_p(H)`$ be the greatest multiplicity of a root of its reduction over $`\overline{\mathbb{F}}_p`$. Equivalently, it is the greatest exponent in the factorization of $`H`$ into irreducibles over $`\mathbb F_p`$.

<a id="theorem-2"></a>

**Theorem 2 (Complete uniform recurrence classification).**

<a id="label-thm-recurrence"></a>

For $`F`$ as in [(3)](#label-eq-recurrence) and $`s\geq1`$, the following are equivalent:

1.  every integral initialization $`u_1,\ldots,u_d`$ has $`\operatorname{Fail}_{D}((u_{n^s}))<\infty`$;

2.  one positive integer repairs $`(u_{n^s})`$ for all integral initializations;

3.  $`F`$ is separable, $`F(0)\neq0`$, and $`\exp(G_F)\mid s`$.

Under these conditions the least uniform multiplier is

<a id="label-eq-recfactor"></a>

```math
\tag{4}
 C_s(F)=\prod_p p^{\rho_{p,s}(\nu_p(xF))}.
```

Its prime divisors are exactly those of $`F(0)\operatorname{disc}(F)`$. Moreover, there is one integral initialization whose scalar failure factor is exactly $`C_s(F)`$.

<!-- end theorem-2 -->

No lower bound on $`s`$ other than the necessary group-exponent condition is required. In particular, the least multiplier can have higher prime powers. Theorem [2](#label-thm-recurrence) gives a finite calculation at the primes dividing $`F(0)\operatorname{disc}(F)`$ once the sampling exponent is admissible: factor $`xF`$ modulo those primes and apply [(1)](#label-eq-threshold). The extra factor $`x`$ records the indexing convention.

The proof separates a local calculation, which determines the exact prime powers, from a global necessity argument using Chebotarev. We subsequently recover squarefree factors, optimal universal exponents, and exact Lucas factors as consequences.

## 2. Local congruences and the matrix multiplier

<a id="lemma-1"></a>

**Lemma 3 (Local Dold criterion).**

<a id="label-lem-local"></a>

Let $`M`$ be a free abelian group and let $`x_n\in M`$. Then
```math
\sum_{e\mid n}\mu(n/e)x_e\in nM\quad(n\geq1)
```
if and only if, for every prime $`p`$, $`r\geq1`$, and $`m\geq1`$ with $`p\nmid m`$,
```math
x_{mp^r}-x_{mp^{r-1}}\in p^r M.
```

<!-- end lemma-1 -->

<a id="proof-1"></a>

**Proof.**

Put $`b_n=\sum_{e\mid n}\mu(n/e)x_e`$. Möbius inversion gives
```math
x_{mp^r}-x_{mp^{r-1}}=\sum_{e\mid m}b_{ep^r},
```
which proves necessity. Conversely, pairing divisors gives
```math
b_{mp^r}=\sum_{e\mid m}\mu(m/e)(x_{ep^r}-x_{ep^{r-1}}).
```
Thus $`b_n`$ is divisible by the full power of each prime dividing $`n`$. Freeness gives $`b_n\in nM`$. $`\square`$

<!-- end proof-1 -->

<a id="lemma-2"></a>

**Lemma 4 (Commuting-power lifting).**

<a id="label-lem-lifting"></a>

Let $`X,Y`$ be commuting integer matrices. If $`X\equiv Y\pmod{p^a}`$ for a prime $`p`$ and $`a\geq1`$, then
```math
X^{p^j}\equiv Y^{p^j}\pmod{p^{a+j}}\qquad(j\geq0).
```

<!-- end lemma-2 -->

<a id="proof-2"></a>

**Proof.**

Write $`X=Y+p^a Z`$. Then $`Y`$ commutes with $`Z`$. In the binomial expansion of $`X^p-Y^p`$, the term involving $`Z^i`$ for $`1\leq i<p`$ is divisible by $`p^{ai+1}`$, and the last term by $`p^{ap}`$. Both exponents are at least $`a+1`$, including when $`p=2,a=1`$. Induction proves the assertion. No invertibility is needed. $`\square`$

<!-- end proof-2 -->

<a id="proposition-1"></a>

**Proposition 5 (Exact local exponent).**

<a id="label-prop-localexact"></a>

Fix $`p,s`$, and suppose that every eigenvalue $`\lambda`$ of $`A`$ modulo $`p`$ satisfies $`\lambda^{p^s}=\lambda`$. Set $`\nu=\nu_p(A)`$ and $`r_0=\rho_{p,s}(\nu)`$. Then all local Dold congruences at $`p`$ for the entrywise sequence $`(C A^{n^s})`$ hold if and only if $`v_p(C)\geq r_0`$.

<!-- end proposition-1 -->

<a id="proof-3"></a>

**Proof.**

Let $`h=\min\{j\geq0:p^j\geq\nu\}`$. Then $`r_0=\lceil h/s\rceil`$, so $`h\leq sr_0`$. On each Jordan block $`J=\lambda I+R`$ in characteristic $`p`$, taking the $`p^h`$-th power kills $`R`$. The eigenvalue condition implies

<a id="label-eq-frobenius"></a>

```math
\tag{5}
 A^{p^{h+s}}\equiv A^{p^h}\pmod p.
```

For $`r\geq r_0+1`$ we may apply Lemma [4](#label-lem-lifting) with $`j=s(r-1)-h\geq0`$. Raising the resulting congruence to the $`m^s`$-th power gives, for every $`m\geq1`$,

<a id="label-eq-localbound"></a>

```math
\tag{6}
 A^{m^s p^{sr}}-A^{m^s p^{s(r-1)}}
       \equiv0\pmod{p^{s(r-1)-h+1}}.
```

Multiplication by $`p^{r_0}`$ supplies the modulus $`p^r`$, because
```math
r_0+s(r-1)-h+1-r
   =(sr_0-h)+(s-1)(r-r_0-1)\geq0.
```
For $`1\leq r\leq r_0`$, the multiplier alone suffices. When $`r_0=0`$ we have $`h=0`$, and the lifting argument starts at $`r=1`$. This proves sufficiency in every case.

For sharpness suppose $`r_0\geq1`$ and take the critical level $`r=r_0`$, with $`m=1`$. Put
```math
q_0=p^{s(r_0-1)},\qquad q_1=p^{sr_0}.
```
On a block of maximum size $`\nu`$ we have $`q_0<\nu\leq q_1`$. Its contribution to the reduction of $`A^{q_1}-A^{q_0}`$ is
```math
(\lambda^{q_1}-\lambda^{q_0})I+R^{q_1}-R^{q_0}
      =-R^{q_0}\neq0.
```
The semisimple terms agree by the eigenvalue condition. Hence at least one entry of the integral matrix $`A^{q_1}-A^{q_0}`$ is a $`p`$-adic unit. The local Dold congruence at index $`p^{r_0}`$ forces $`p^{r_0}\mid C`$. This is automatic when $`r_0=0`$ and proves necessity. $`\square`$

<!-- end proof-3 -->

<a id="lemma-3"></a>

**Lemma 6 (Eigenvalues at all primes).**

<a id="label-lem-residue"></a>

Let $`A`$ be an integer matrix and let $`K`$ split its minimal polynomial. If $`\exp(\operatorname{Gal}(K/\mathbb Q))\mid s`$, then every eigenvalue of $`A`$ modulo every prime $`p`$ lies in $`\mathbb F_{p^s}`$.

<!-- end lemma-3 -->

<a id="proof-4"></a>

**Proof.**

The minimal polynomial $`m_A`$ is monic integral, since it is a monic rational factor of the integral characteristic polynomial. Its roots are therefore algebraic integers. Fix a prime $`\mathfrak P`$ of $`K`$ above $`p`$. The residue-field Galois group is the cyclic quotient
```math
D(\mathfrak P)/I(\mathfrak P)
       \simeq\operatorname{Gal}(\mathcal O_K/\mathfrak P\,/\mathbb F_p).
```
Its order $`f`$ divides the exponent of $`\operatorname{Gal}(K/\mathbb Q)`$, since the exponent of a quotient of a subgroup divides the group exponent. Hence $`f\mid s`$. Reducing the split factorization of $`m_A`$ at $`\mathfrak P`$ puts all its reduced roots in $`\mathbb F_{p^f}\subseteq\mathbb F_{p^s}`$. The reduced polynomial annihilates $`A`$ modulo $`p`$, so the assertion follows. This argument includes ramified primes; it uses the decomposition/inertia quotient rather than an unramified Frobenius element. See [\[3, Section 8\]](#ref-Milne). $`\square`$

<!-- end proof-4 -->

<a id="proof-5"></a>

**Sufficiency and exact multiplier in Theorem [1](#label-thm-matrix).**

Assume semisimplicity over $`\mathbb Q`$ and $`\exp(G_A)\mid s`$. Lemma [6](#label-lem-residue) and Proposition [5](#label-prop-localexact) give the precise exponent $`\rho_{p,s}(\nu_p(A))`$ at every prime. Since $`m_A`$ is separable, at every $`p\nmid\operatorname{disc}(m_A)`$ its reduction is a squarefree annihilator, so $`\nu_p(A)=1`$. The product [(2)](#label-eq-matrixfactor) is therefore finite. Lemma [3](#label-lem-local) proves that precisely its positive multiples repair the sequence. A prime occurs precisely when $`\nu_p(A)>1`$, equivalently when the reduction is nonsemisimple. $`\square`$

<!-- end proof-5 -->

## 3. Global obstructions and the necessary exponent

<a id="lemma-4"></a>

**Lemma 7 (Minimal-polynomial stability).**

<a id="label-lem-stability"></a>

For an integer matrix $`A`$, its minimal polynomial modulo $`p`$ equals the reduction of $`m_A`$ for all but finitely many primes $`p`$.

<!-- end lemma-4 -->

<a id="proof-6"></a>

**Proof.**

Let $`d=\deg m_A`$. The matrices $`I,A,\ldots,A^{d-1}`$ are linearly independent over $`\mathbb Q`$. Vectorizing them as columns produces an integer matrix with some nonzero $`d`$-by-$`d`$ minor $`\delta`$. For $`p\nmid\delta`$, these powers remain independent modulo $`p`$. Since the monic relation $`m_A(A)=0`$ reduces at every prime, the reduced minimal polynomial has degree exactly $`d`$ and equals the reduction of $`m_A`$. $`\square`$

<!-- end proof-6 -->

<a id="proof-7"></a>

**Necessity in Theorem [1](#label-thm-matrix).**

If $`A`$ is not semisimple over $`\mathbb Q`$, then $`m_A`$ is divisible by the square of a positive-degree monic integral polynomial. Its reduction is consequently nonsquarefree at every prime. By Lemma [7](#label-lem-stability), the minimal polynomial of $`A`$ modulo $`p`$ is nonsquarefree for all but finitely many primes. It cannot divide $`x^{p^s}-x`$, whose derivative is $`-1`$ in characteristic $`p`$. Thus

<a id="label-eq-primeobstruction"></a>

```math
\tag{7}
 A^{p^s}-A\not\equiv0\pmod p
```

for infinitely many primes. At each such prime the Dold congruence at index $`p`$ forces $`p\mid C`$, so a finite positive repair is impossible.

Now assume $`m_A`$ separable, but $`\exp(G_A)\nmid s`$. Choose $`\sigma\in G_A`$ with $`\sigma^s\neq1`$. The action of $`G_A`$ on the roots of $`m_A`$ is faithful, since those roots generate the splitting field. Therefore $`\sigma^s`$ moves a root. Chebotarev’s theorem [\[3, Theorem 8.31\]](#ref-Milne) supplies infinitely many unramified rational primes with Frobenius conjugacy class that of $`\sigma`$. Exclude the finitely many primes dividing $`\operatorname{disc}(m_A)`$ and those excluded in Lemma [7](#label-lem-stability). The reduced roots are then distinct; their Frobenius permutation has the same cycle structure as $`\sigma`$. Some root is not fixed by the $`p^s`$-power map, and every root occurs in the reduced minimal polynomial. That polynomial does not divide $`x^{p^s}-x`$, so [(7)](#label-eq-primeobstruction) again holds at infinitely many primes. No finite positive multiplier can satisfy all these prime-index congruences. This proves both necessary conditions. $`\square`$

<!-- end proof-7 -->

<a id="remark-1"></a>

**Remark 8.**

The matrix quantifier is essential. For example, the trace sequence of an integral matrix satisfies the Dold congruences even when its individual entries have infinite repair at $`s=1`$; see [\[1\]](#ref-BGW). Traces can combine conjugate eigenvalues in a way that the entrywise requirement does not allow.

<!-- end remark-1 -->

## 4. Recurrence modules and attainment of the uniform factor

Let $`T`$ be the companion matrix of [(3)](#label-eq-recurrence), with ones immediately above the main diagonal and last row $`(-c_0,\ldots,-c_{d-1})`$. For $`v=(u_1,\ldots,u_d)^{\mathsf t}`$,

<a id="label-eq-observation"></a>

```math
\tag{8}
 u_n=e_1^{\mathsf t}T^{n-1}v.
```

The matrix $`T`$ has minimal polynomial $`F`$ over every residue field. Also

<a id="label-eq-cyclicrow"></a>

```math
\tag{9}
 e_1^{\mathsf t}T^j=e_{j+1}^{\mathsf t}\qquad(0\leq j<d).
```

Consequently, if a polynomial $`E`$ satisfies $`E(T)\neq0`$ over a field, its first row is nonzero: otherwise commutativity with $`T`$ and [(9)](#label-eq-cyclicrow) would make every row zero.

<a id="proof-8"></a>

**Sufficiency in Theorem [2](#label-thm-recurrence).**

Suppose $`F`$ is separable, $`F(0)\neq0`$, and $`\exp(G_F)\mid s`$. For an initial vector $`v`$, define an integer matrix $`B_v`$ on $`\mathbb Ze_0\oplus\mathbb Z^d`$ by
```math
B_v e_0=v,\qquad B_v w=Tw\quad(w\in\mathbb Z^d).
```
Then $`B_v^n e_0=T^{n-1}v`$ for $`n\geq1`$. Thus $`u_n`$ is an entry of $`B_v^n`$, and $`xF(x)`$ annihilates $`B_v`$. The polynomial $`xF`$ is separable over $`\mathbb Q`$ and has the same splitting field as $`F`$. The minimal-polynomial splitting field of $`B_v`$ is a Galois subextension of that field, so its group exponent divides $`\exp(G_F)`$. Moreover, every Jordan block of $`B_v`$ modulo $`p`$ has size at most $`\nu_p(xF)`$. Theorem [1](#label-thm-matrix) proves that [(4)](#label-eq-recfactor) repairs all these matrices, hence all initializations.

The product is finite because
```math
\operatorname{disc}(xF)=F(0)^2\operatorname{disc}(F).
```
The inequality $`\nu_p(xF)>1`$ is equivalent to $`p\mid F(0)\operatorname{disc}(F)`$: a zero of $`F`$ increases its multiplicity in $`xF`$, while a repeated nonzero root remains repeated. This identifies the exact possible prime support; sharpness follows next. $`\square`$

<!-- end proof-8 -->

<a id="proof-9"></a>

**Sharpness and attainment in Theorem [2](#label-thm-recurrence).**

Fix a prime $`p`$ with $`\nu=\nu_p(xF)>1`$. Let $`r_0=\rho_{p,s}(\nu)`$, $`q_0=p^{s(r_0-1)}`$, and $`q_1=p^{sr_0}`$. In $`\mathbb F_p[x]`$ consider

<a id="label-eq-criticalpolynomial"></a>

```math
\tag{10}
 E(x)=x^{q_1-1}-x^{q_0-1}
     =x^{q_0-1}(x^{p^s-1}-1)^{q_0}.
```

Every nonzero root of $`F`$ modulo $`p`$ lies in $`\mathbb F_{p^s}`$ by the argument of Lemma [6](#label-lem-residue). Its multiplicity in $`E`$ is exactly $`q_0`$, because $`x^{p^s-1}-1`$ has simple nonzero roots. The multiplicity of zero in $`E`$ is $`q_0-1`$. Therefore
```math
\overline F\mid E\quad\Longleftrightarrow\quad\nu_p(xF)\leq q_0.
```
The right side is false by the definition of $`r_0`$. Since the reduced minimal polynomial of $`T`$ is $`\overline F`$, we have $`E(T)\neq0`$ modulo $`p`$. Its first row is nonzero by [(9)](#label-eq-cyclicrow). Choose $`v_p\in\mathbb Z^d`$ such that $`e_1^{\mathsf t}E(T)v_p\not\equiv0\pmod p`$. By [(8)](#label-eq-observation), its sequence has
```math
u_{q_1}-u_{q_0}\not\equiv0\pmod p.
```
The local Dold congruence at index $`p^{r_0}`$ forces $`p^{r_0}\mid C`$ for any multiplier repairing this initialization. Thus every uniform multiplier contains the full factor in [(4)](#label-eq-recfactor).

There are only finitely many relevant primes. The Chinese remainder theorem, applied coordinatewise, supplies one integral vector $`v`$ with $`v\equiv v_p\pmod p`$ for each of them. The corresponding sequence forces all the required prime powers simultaneously. Its failure factor is exactly $`C_s(F)`$, since the latter was already proved sufficient. When $`C_s(F)=1`$, any initialization, including the zero initialization, attains it. $`\square`$

<!-- end proof-9 -->

<a id="proof-10"></a>

**Necessity in Theorem [2](#label-thm-recurrence).**

If every initialization has some finite repair, take the least common multiple of repairing integers for the $`d`$ standard-basis initializations. Linearity gives one integer repairing all initializations. Thus the first two conditions are equivalent.

If $`F(0)=0`$, the initialization giving $`u_1=1`$ and $`u_n=0`$ for $`n\geq2`$ satisfies [(3)](#label-eq-recurrence). Its prime-index difference is $`-1`$ at every prime, so it has infinite repair.

If $`F`$ is not separable, it has a positive-degree monic square factor over $`\mathbb Z`$, so its reduction cannot divide the squarefree polynomial $`x^{p^s-1}-1`$. Hence $`T^{p^s-1}-I`$ is nonzero modulo every prime, and its first row is nonzero. One of the finitely many standard-basis initializations witnesses this nonvanishing for infinitely many primes. Its differences $`u_{p^s}-u_1`$ force infinitely many prime divisors in any repair.

Finally, suppose $`F`$ is separable with $`F(0)\neq0`$ but $`\exp(G_F)\nmid s`$. The Chebotarev argument used for Theorem [1](#label-thm-matrix), now excluding the primes dividing $`F(0)\operatorname{disc}(F)`$, gives infinitely many primes for which $`\overline F`$ does not divide $`x^{p^s-1}-1`$. The same nonzero-first-row and finite-pigeonhole argument gives one initialization with infinite repair. All three conditions are necessary. $`\square`$

<!-- end proof-10 -->

<a id="example-1"></a>

**Example 9 (Higher prime powers and an attaining initialization).**

<a id="label-ex-higher"></a>

For
```math
F=(x-2)(x-4)(x-6)=x^3-12x^2+44x-48,
```
the Galois group is trivial, so every $`s\geq1`$ is admissible. At $`s=1`$, the companion matrix has exact multiplier $`4`$: modulo $`2`$, its maximum block has size $`3`$, and at all other primes it is semisimple. Indeed modulo $`3`$ the roots $`2,4,6`$ are distinct. The polynomial $`xF`$ has maximum root multiplicity $`4`$ modulo $`2`$ and $`2`$ modulo $`3`$, giving the uniform recurrence multiplier $`12`$.

The initialization $`(u_1,u_2,u_3)=(0,1,1)`$ attains $`12`$. Here $`u_4=-32`$, so $`u_4-u_2=-33`$ is odd and forces $`4`$ at the index $`4`$ Dold congruence, while $`u_3-u_1=1`$ forces $`3`$. For every $`s\geq2`$, the corresponding matrix and uniform recurrence multipliers are $`2`$ and $`6`$.

<!-- end example-1 -->

<a id="example-2"></a>

**Example 10 (The constant term and indexing).**

<a id="label-ex-initialization"></a>

Let $`u_n=2^{n-1}+3^{n-1}`$ for $`n\geq1`$. Its recurrence polynomial is $`F=(x-2)(x-3)`$, with $`\operatorname{disc}(F)=1`$ and $`F(0)=6`$. For every $`s\geq1`$, Theorem [2](#label-thm-recurrence) gives uniform factor $`6`$. This sequence attains it: $`u_{2^s}`$ is odd whereas $`u_1=2`$, and $`u_{3^s}\equiv1\pmod3`$. Thus the constant-term primes cannot be removed from a uniform statement initialized at index $`1`$.

<!-- end example-2 -->

<a id="remark-2"></a>

**Remark 11 (The printed multiplier in Luca–Ward).**

<a id="label-rem-LW"></a>

Theorem 1(i) of [\[2\]](#ref-LW) states a sufficient multiplier that is a multiple of $`\operatorname{lcm}(\Delta(K),\Delta(F))`$, for initialization $`u_1,\ldots,u_d`$ and sampling exponent at least $`[K:\mathbb Q]`$ divisible by the Galois-group exponent. In Example [10](#label-ex-initialization), $`K=\mathbb Q`$ and both discriminants are $`1`$. Thus the printed statement permits multiplier $`1`$, which fails already at prime index $`2`$. This is a counterexample to that printed multiplier with its stated indexing convention; no official erratum or conclusion about the article’s other theorems is asserted. The augmentation by $`xF`$ accounts for the missing constant-term support.

<!-- end remark-2 -->

## 5. Squarefree factors and universal exponents

Put $`L_d=\operatorname{lcm}(1,\ldots,d)`$ and let $`\operatorname{rad}(|t|)`$ be the product of the distinct prime divisors of a nonzero integer $`t`$.

<a id="corollary-1"></a>

**Corollary 12 (Squarefree range).**

<a id="label-cor-squarefree"></a>

Under the spectral hypotheses of Theorem [1](#label-thm-matrix), if $`p^s\geq\nu_p(A)`$ for every prime, then
```math
C_s(A)=\prod_{\nu_p(A)>1}p.
```
For a monic separable $`F`$ of degree $`d`$ with $`F(0)\neq0`$, every positive multiple $`s`$ of $`L_d`$ satisfies
```math
C_s(F)=\operatorname{rad}\bigl(|F(0)\operatorname{disc}(F)|\bigr).
```

<!-- end corollary-1 -->

<a id="proof-11"></a>

**Proof.**

The first assertion is immediate from [(1)](#label-eq-threshold). The action of $`G_F`$ on the $`d`$ roots embeds it into the symmetric group $`S_d`$, whose exponent is $`L_d`$. Hence $`s`$ is admissible. Also $`s\geq d`$, so $`p^s\geq2^d\geq d+1\geq\nu_p(xF)`$ for every prime. Apply Theorem [2](#label-thm-recurrence) and its prime-support statement. $`\square`$

<!-- end proof-11 -->

<a id="corollary-2"></a>

**Corollary 13 (Optimal universal exponent).**

<a id="label-cor-universal"></a>

Fix $`d,s\geq1`$. Every integer sequence admitting a monic separable integral recurrence polynomial of degree at most $`d`$ with nonzero constant term has finite Dold repair along $`n^s`$ if and only if $`L_d\mid s`$.

<!-- end corollary-2 -->

<a id="proof-12"></a>

**Proof.**

Sufficiency follows from Corollary [12](#label-cor-squarefree). If $`L_d\nmid s`$, choose $`2\leq f\leq d`$ with $`f\nmid s`$. There exists a cyclic extension $`K/\mathbb Q`$ of degree $`f`$: choose a prime $`q\equiv1\pmod f`$ by Dirichlet’s theorem, and take the fixed field of the subgroup of index $`f`$ in the cyclic group $`\operatorname{Gal}(\mathbb Q(\zeta_q)/\mathbb Q)`$. See [\[3, Sections 6 and 8\]](#ref-Milne). Choose a nonzero integral primitive element of $`K`$ and let $`F`$ be its minimal polynomial. This polynomial is separable, has degree $`f`$ and nonzero constant term, and its splitting field is $`K`$, with group exponent $`f`$. The necessity in Theorem [2](#label-thm-recurrence) supplies an integral initialization with infinite repair along $`n^s`$. $`\square`$

<!-- end proof-12 -->

## 6. Exact repair for fundamental Lucas sequences

<a id="corollary-3"></a>

**Corollary 14 (Lucas factor).**

<a id="label-cor-lucas"></a>

For $`P,Q\in\mathbb Z`$, let $`U_0=0`$, $`U_1=1`$, and
```math
U_{n+2}=P U_{n+1}-Q U_n\qquad(n\geq0).
```
If $`D=P^2-4Q\neq0`$, then for every $`k\geq1`$,
```math
\operatorname{Fail}_{D}((U_{n^{2k}})_{n\geq1})=\operatorname{rad}(|D|).
```
If $`D=0`$, the failure factor along $`n^s`$ is infinite for every $`s\geq1`$.

<!-- end corollary-3 -->

<a id="proof-13"></a>

**Proof.**

Set $`A=\left(\begin{smallmatrix}P&-Q\\1&0\end{smallmatrix}\right)`$. Since $`A^2=PA-QI`$ and the lower-left entries of $`I,A`$ are $`0,1`$, we have $`(A^n)_{21}=U_n`$. If $`D\neq0`$, the polynomial $`x^2-Px+Q`$ is separable with Galois-group exponent dividing $`2`$. Every even $`s`$ is admissible, all Jordan blocks have size at most $`2`$, and nonsemisimple primes are supported on $`D`$. Theorem [1](#label-thm-matrix) gives sufficiency of $`\operatorname{rad}(|D|)`$.

For a prime $`p\mid D`$, the characteristic polynomial modulo $`p`$ has a repeated root $`a\in\mathbb F_p`$. For odd $`p`$ take $`a=P/2`$; for $`p=2`$, $`P`$ is even and $`a=Q`$ modulo $`2`$. Writing $`A=aI+R`$ modulo $`p`$, Cayley–Hamilton gives $`R^2=0`$ and $`R_{21}=1`$. Thus for every $`s\geq1`$,
```math
A^{p^s}=a^{p^s}I\pmod p,\qquad U_{p^s}\equiv0\pmod p.
```
The difference from $`U_1=1`$ forces $`p`$ in any repairing multiplier. If $`D=0`$, this applies to every prime, proving the last assertion. $`\square`$

<!-- end proof-13 -->

<a id="example-3"></a>

**Example 15.**

For $`P=6,Q=5`$, we have $`D=16`$ and $`U_n=(5^n-1)/4`$. Every positive even-power subsequence has exact repair factor $`2`$.

<!-- end example-3 -->

<a id="remark-3"></a>

**Remark 16 (A quadratic lifting consequence).**

For any $`P,Q\in\mathbb Z`$, prime $`p`$, $`m\geq1`$, and $`r\geq2`$,
```math
U_{m p^{2r}}\equiv U_{m p^{2r-2}}\pmod{p^r}.
```
Every reduced quadratic eigenvalue lies in $`\mathbb F_{p^2}`$, and in [(5)](#label-eq-frobenius) one can take $`s=2`$ and $`h=1`$. Lifting and raising to the $`m`$-th power gives divisibility by $`p^{2r-2}`$, which is at least $`p^r`$. This also holds when $`D=0`$.

<!-- end remark-3 -->

## 7. Relation to previous work and verification

The sufficient Galois-exponent condition and the residue-degree mechanism are already present in Luca–Ward [\[2\]](#ref-LW). The contribution of Theorems [1](#label-thm-matrix) and [2](#label-thm-recurrence) is the complete criterion for these simultaneous repair problems, together with the exact prime-power multiplier for every admissible $`s`$, including small $`s`$, and an initialization attaining the uniform multiplier. The matrix argument avoids Binet denominators and separates rational semisimplicity from nonsemisimple reduction. The critical-level calculation explains why a prime power can be necessary even when the first prime-index obstruction detects only that prime.

Rajs [\[6, Theorem 9\]](#ref-Rajs) gives a sufficient multiplier $`r_d\Delta_U\operatorname{rad}(\Delta_K)`$ for exponents divisible by the splitting-field degree. His Theorem 8 addresses scalar recurrence sequences without power sampling, and Theorem 4 supplies a quadratic square-subsequence bound including a denominator-clearing factor. The present exact formulas concern different simultaneous quantifiers; they do not claim a classification of the least repair factor of every individual scalar power subsequence. In particular, the established scalar trace classification at $`s=1`$ remains a distinct result.

For Lucas sequences, [\[5,2\]](#ref-MW) establish sufficient discriminant factors, and Corollary [14](#label-cor-lucas) determines the exact radical. The uniform squarefree factor and universal exponent follow from the general classification and are included as consequences of the same theorem.

The proof is independent of computation. Exact modular checks accompanying the earlier Lucas result cover $`125{,}000`$ local instances. An additional script, `P02-extension-check.py`, checks $`378`$ local instances of Example [9](#label-ex-higher), including its sharpness witnesses, for five primes, levels up to $`6`$, and sampling exponents $`1,2,3`$. The check outputs and independent proof review are retained with the research records. These checks support the transfer of the formulas; they do not establish novelty or replace the arguments above.

## References

<a id="ref-BGW"></a>

**\[1\]** J. Byszewski, G. Graff, and T. Ward, *Dold sequences, periodic points, and dynamics*, Bull. London Math. Soc. **53** (2021), 1263–1298. [doi:10.1112/blms.12531](https://doi.org/10.1112/blms.12531).

<a id="ref-LW"></a>

**\[2\]** F. Luca and T. Ward, *On (Almost) Realizable Subsequences of Linearly Recurrent Sequences*, J. Integer Seq. **26** (2023), Article 23.4.6. <https://cs.uwaterloo.ca/journals/JIS/VOL26/Ward/ward9.pdf>.

<a id="ref-Milne"></a>

**\[3\]** J. S. Milne, *Algebraic Number Theory*, course notes, Sections 6 and 8, especially Theorem 8.31. <https://www.jmilne.org/math/CourseNotes/ANT.pdf>.

<a id="ref-Minton"></a>

**\[4\]** G. T. Minton, *Linear recurrence sequences satisfying congruence conditions*, Proc. Amer. Math. Soc. **142** (2014), 2337–2352. [doi:10.1090/S0002-9939-2014-12168-X](https://doi.org/10.1090/S0002-9939-2014-12168-X).

<a id="ref-MW"></a>

**\[5\]** P. Moss and T. Ward, *Fibonacci Along Even Powers Is (Almost) Realizable*, Fibonacci Quart. **60** (2022), 40–47. <https://www.fq.math.ca/Papers/60-1/ward01062021.pdf>.

<a id="ref-Rajs"></a>

**\[6\]** M. Rajs, *On Dold condition and fail factor of linear recurrent sequences*, arXiv:2509.09847v1 (2025). <https://arxiv.org/abs/2509.09847>.
