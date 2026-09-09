# Squarefree repair factors and optimal exponents for linear recurrences

September 8, 2026

## Abstract

An integer sequence satisfies the Dold congruences if its Möbius transform at every positive integer $`n`$ is divisible by $`n`$. We determine the least multiplier that makes all entries of a power-indexed integer matrix sequence satisfy these congruences: under a finite-field exponent condition, it is the product of the primes at which the matrix has nonsemisimple reduction. Consequently, for a fixed separable integral recurrence polynomial $`F`$ of degree $`d`$ with nonzero constant term, the exact multiplier that works uniformly for every integral initialization indexed from $`1`$ is $`\operatorname{rad}(|F(0)\operatorname{disc}(F)|)`$ when sampling at $`n^s`$, where $`s`$ is a positive multiple of $`\operatorname{lcm}(1,\ldots,d)`$. For the fundamental Lucas sequence of nonzero discriminant $`D`$, we obtain the exact scalar repair factor $`\operatorname{rad}(|D|)`$ along every positive even power. We also show that the multiples of $`\operatorname{lcm}(1,\ldots,d)`$ are exactly the exponents admitting finite repair for every separable recurrence of order at most $`d`$ with nonzero constant term. The sufficiency proofs use Jordan decomposition over finite fields and lifting of congruences between commuting matrices; exponent necessity uses cyclic number fields and Chebotarev. These statements concern Dold divisibility; nonnegativity of orbit counts is a separate condition.

## 1. Introduction and principal results

For a sequence $`a=(a_n)_{n\geq1}`$ of integers, define
```math
b_n(a)=\sum_{e\mid n}\mu(n/e)a_e.
```
The *Dold congruences* require $`n\mid b_n(a)`$ for every $`n\geq1`$. Write $`\operatorname{Fail}_{D}(a)`$ for the least positive integer $`C`$ such that $`(Ca_n)`$ satisfies these congruences, with $`\operatorname{Fail}_{D}(a)=\infty`$ if no such integer exists. We use this notation for signed sequences as well. It is a divisibility invariant: the condition $`b_n(a)\geq0`$, required to interpret $`a_n`$ as fixed-point counts of a map, is not part of its definition.

The repair phenomenon for power subsequences is exemplified by the Fibonacci sequence. Moss and Ward [\[4\]](#ref-MW) established realizability after multiplication by $`5`$ along positive even powers and proposed a corresponding discriminant-scaled Lucas congruence. Luca and Ward [\[2\]](#ref-LW), Theorem 5, proved that conjecture. Rajs [\[5\]](#ref-Rajs) investigated repair factors for general linear recurrences and their power subsequences. Here we work with integral matrices directly, avoiding the denominators of a Binet representation.

Set $`L_d=\operatorname{lcm}(1,\ldots,d)`$. For a nonzero integer $`t`$, $`\operatorname{rad}(|t|)`$ is the product of its distinct positive prime divisors, with $`\operatorname{rad}(1)=1`$.

<a id="theorem-1"></a>

**Theorem 1 (Uniform repair for a fixed recurrence).**

<a id="label-thm-recurrence"></a>

Let
```math
F(x)=x^d+c_{d-1}x^{d-1}+\cdots+c_0\in\mathbb Z[x]
```
be monic, with $`d\geq1`$, $`c_0\neq0`$, and $`\operatorname{disc}(F)\neq0`$. Let $`s`$ be a positive multiple of $`L_d`$. Among positive integers $`C`$, the least one with the following property is
```math
C=\operatorname{rad}\bigl(|F(0)\operatorname{disc}(F)|\bigr):
```
for every choice $`u_1,\ldots,u_d\in\mathbb Z`$, the recurrence
```math
u_{n+d}+c_{d-1}u_{n+d-1}+\cdots+c_0u_n=0\quad(n\geq1)
```
has $`(C u_{n^s})_{n\geq1}`$ satisfying the Dold congruences.

<!-- end theorem-1 -->

The conclusion is uniform over initial data. A particular sequence may admit a smaller multiplier. A fundamental quadratic recurrence permits an exact scalar answer.

<a id="theorem-2"></a>

**Theorem 2 (Exact Lucas repair).**

<a id="label-thm-lucas"></a>

Let $`P,Q\in\mathbb Z`$, and define
```math
U_0=0,\qquad U_1=1,\qquad U_{n+2}=P U_{n+1}-Q U_n\quad(n\geq0).
```
If $`D=P^2-4Q\neq0`$, then for every $`k\geq1`$,
```math
\operatorname{Fail}_{D}\bigl((U_{n^{2k}})_{n\geq1}\bigr)=\operatorname{rad}(|D|).
```
If $`D=0`$, this failure invariant is infinite for every $`k\geq1`$.

<!-- end theorem-2 -->

<a id="theorem-3"></a>

**Theorem 3 (Optimal universal exponents).**

<a id="label-thm-optimal-exponent"></a>

Fix $`d\geq1`$ and $`s\geq1`$. The following are equivalent:

1.  $`L_d\mid s`$;

2.  for every integer sequence admitting a monic separable integral recurrence polynomial of degree at most $`d`$ with nonzero constant term, its subsequence $`(u_{n^s})_{n\geq1}`$ has finite Dold repair factor.

The repairing integer in the second condition may depend on the sequence.

<!-- end theorem-3 -->

These theorems do not assume that the terms are nonnegative. In particular, the conclusion applies to negative recurrence parameters and to periodic or degenerate Lucas sequences, subject to the stated discriminant distinction.

## 2. The matrix repair theorem

A sequence of integer matrices satisfies the Dold congruences if every matrix entry does so. A matrix over $`\mathbb F_p`$ is called semisimple here if it is diagonalizable over an algebraic closure of $`\mathbb F_p`$.

<a id="theorem-4"></a>

**Theorem 4 (Exact entrywise matrix repair).**

<a id="label-thm-matrix"></a>

Let $`A\in\operatorname{Mat}_N(\mathbb Z)`$ be annihilated by a monic polynomial $`F\in\mathbb Z[x]`$ of degree $`d\geq1`$ with $`\operatorname{disc}(F)\neq0`$. Suppose $`s\geq1`$ satisfies:

1.  for every prime $`p`$, the degree of every irreducible factor of $`F`$ modulo $`p`$ divides $`s`$;

2.  $`2^s\geq d`$.

Let $`\mathcal B(A)`$ be the set of primes at which $`A`$ has nonsemisimple reduction. Then $`\mathcal B(A)`$ is finite, and
```math
C(A)=\prod_{p\in\mathcal B(A)}p
```
is the least positive integer for which $`(C(A)A^{n^s})_{n\geq1}`$ satisfies the Dold congruences entrywise. In particular,
```math
C(A)\mid\operatorname{rad}(|\operatorname{disc}(F)|).
```
Both hypotheses on $`s`$ hold if $`s`$ is a positive multiple of $`L_d`$.

<!-- end theorem-4 -->

The exact factor depends on the integral matrix, not merely on a chosen annihilating polynomial. For example, a diagonal integer matrix has semisimple reduction at every prime, even if two of its eigenvalues become equal modulo some prime.

We give the local argument in detail, including the small-prime and noninvertible cases.

<a id="lemma-1"></a>

**Lemma 5 (Local Dold criterion).**

<a id="label-lem-local"></a>

Let $`M`$ be a free abelian group and let $`x_n\in M`$. Then
```math
\sum_{e\mid n}\mu(n/e)x_e\in nM\quad(n\geq1)
```
if and only if, for every prime $`p`$, every $`r\geq1`$, and every $`m\geq1`$ with $`p\nmid m`$,
```math
x_{mp^r}-x_{mp^{r-1}}\in p^r M.
```

<!-- end lemma-1 -->

<a id="proof-1"></a>

**Proof.**

Put $`b_n=\sum_{e\mid n}\mu(n/e)x_e`$. Möbius inversion gives $`x_n=\sum_{e\mid n}b_e`$. Thus
```math
x_{mp^r}-x_{mp^{r-1}}=\sum_{e\mid m}b_{ep^r},
```
which proves necessity. Conversely, pairing divisors gives
```math
b_{mp^r}=\sum_{e\mid m}\mu(m/e)
      (x_{ep^r}-x_{ep^{r-1}}).
```
The local hypothesis therefore makes $`b_n`$ divisible by the full power of every prime dividing $`n`$. Since $`M`$ is free abelian, it follows that $`b_n\in nM`$. $`\square`$

<!-- end proof-1 -->

<a id="lemma-2"></a>

**Lemma 6 (Commuting-power lifting).**

<a id="label-lem-lifting"></a>

Let $`X,Y`$ be commuting integer matrices, and let $`p`$ be prime. If $`X\equiv Y\pmod{p^a}`$ for $`a\geq1`$, then
```math
X^{p^j}\equiv Y^{p^j}\pmod{p^{a+j}}\qquad(j\geq0).
```

<!-- end lemma-2 -->

<a id="proof-2"></a>

**Proof.**

Write $`X=Y+p^aZ`$. The commutativity of $`X`$ and $`Y`$ implies that $`Z`$ and $`Y`$ commute. In the binomial expansion of $`(Y+p^aZ)^p-Y^p`$, the terms with powers $`Z^i`$ for $`1\leq i<p`$ are divisible by $`p^{ai+1}`$, and the last term is divisible by $`p^{ap}`$. All are divisible by $`p^{a+1}`$, including when $`p=2`$ and $`a=1`$. Induction proves the assertion. $`\square`$

<!-- end proof-2 -->

<a id="proof-3"></a>

**Proof of Theorem [4](#label-thm-matrix).**

Fix a prime $`p`$, and put $`h=\lceil\log_p d\rceil`$, with $`h=0`$ if $`d=1`$. Reduce $`A`$ modulo $`p`$ and pass to an algebraic closure. Since $`F(A)=0`$, every Jordan block has size at most $`d`$. Every eigenvalue $`\lambda`$ belongs to $`\mathbb F_{p^f}`$ for an irreducible factor degree $`f`$ of $`F`$ modulo $`p`$. Hence $`\lambda^{p^s}=\lambda`$.

If $`J=\lambda I+R`$ is a Jordan block, then $`R^{p^h}=0`$, and in characteristic $`p`$,
```math
J^{p^h}=\lambda^{p^h}I.
```
It follows that

<a id="label-eq-frobenius"></a>

```math
\tag{1}
 A^{p^{h+s}}\equiv A^{p^h}\pmod p.
```

The size hypothesis gives $`h\leq s`$. At a semisimple prime the same congruence holds with $`h=0`$.

For $`r\geq2`$, set $`t=s(r-1)-h\geq0`$. Applying Lemma [6](#label-lem-lifting) to the commuting matrices in [(1)](#label-eq-frobenius), and then raising both sides to $`m^s`$, gives

<a id="label-eq-localbound"></a>

```math
\tag{2}
 A^{m^s p^{sr}}\equiv A^{m^s p^{s(r-1)}}
       \pmod{p^{s(r-1)-h+1}}.
```

Since
```math
s(r-1)-h+1\geq r-1,
```
one additional factor of $`p`$ suffices at every nonsemisimple prime. The case $`r=1`$ at such a prime is automatic after multiplication by $`p`$.

At a semisimple prime take $`h=0`$. The same argument, now also for $`r=1`$, gives a modulus $`p^{s(r-1)+1}`$, which is at least $`p^r`$. Therefore no multiplier is needed there. If $`p\nmid\operatorname{disc}(F)`$, the polynomial $`F`$ modulo $`p`$ is squarefree and its annihilation of $`A`$ implies semisimplicity. Thus $`\mathcal B(A)`$ is finite and supported on the prime divisors of $`\operatorname{disc}(F)`$. Lemma [5](#label-lem-local) proves sufficiency of $`C(A)`$.

For necessity consider the Dold congruence at $`n=p`$. Over $`\mathbb F_p`$, the identity $`A^{p^s}=A`$ holds if and only if $`A`$ is semisimple: the forward direction follows because $`x^{p^s}-x`$ has derivative $`-1`$, and the reverse direction follows from the eigenvalue condition. Thus at every prime $`p\in\mathcal B(A)`$ at least one entry of $`A^{p^s}-A`$ is nonzero. Every integer repairing all entries must be divisible by $`p`$. This proves exactness.

Finally, if $`L_d\mid s`$, every irreducible factor degree divides $`s`$, and $`s\geq d`$ implies $`2^s\geq d`$. $`\square`$

<!-- end proof-3 -->

## 3. Arbitrary initialization and uniform sharpness

<a id="proof-4"></a>

**Proof of Theorem [1](#label-thm-recurrence).**

Use states
```math
v_n=(u_n,u_{n+1},\ldots,u_{n+d-1})^{\mathsf t},\qquad
 v_{n+1}=Tv_n,
```
where $`T`$ is the integer companion matrix with ones immediately above the main diagonal and last row $`(-c_0,\ldots,-c_{d-1})`$. In particular $`F(T)=0`$.

For a fixed initial vector $`v_1`$, define an integer matrix $`B`$ on $`\mathbb Z e_0\oplus\mathbb Z^d`$ by
```math
Be_0=v_1,\qquad Bw=Tw\quad(w\in\mathbb Z^d).
```
Then $`B^n e_0=T^{n-1}v_1`$ for $`n\geq1`$, so $`u_n`$ is a fixed entry of $`B^n`$. The polynomial $`xF(x)`$ annihilates $`B`$. It is separable because $`F`$ is separable and $`F(0)\neq0`$, and
```math
\operatorname{disc}(xF)=F(0)^2\operatorname{disc}(F).
```
Every irreducible factor of $`xF`$ modulo any prime has degree at most $`d`$, since the new factor $`x`$ has degree one. The exponent $`s`$ is divisible by all these degrees. Also $`2^s\geq d+1`$, including the case $`d=1`$. Theorem [4](#label-thm-matrix) therefore implies that
```math
\operatorname{rad}(|F(0)\operatorname{disc}(F)|)\,u_{n^s}
```
satisfies the Dold congruences for every initial vector.

To prove universal sharpness, fix a prime $`p\mid F(0)\operatorname{disc}(F)`$ and reduce $`T`$ modulo $`p`$. Its minimal polynomial remains $`F`$ modulo $`p`$, because a companion matrix is cyclic over every field. Put
```math
E=T^{p^s-1}-I.
```
This is zero if and only if $`F`$ modulo $`p`$ divides $`x^{p^s-1}-1`$. Every root of $`F`$ modulo $`p`$ lies in $`\mathbb F_{p^s}`$. The roots of $`x^{p^s-1}-1`$ are exactly the nonzero elements of this field, each with multiplicity one. It follows that $`E=0`$ if and only if $`F`$ modulo $`p`$ is squarefree with nonzero constant term, equivalently if and only if $`p\nmid F(0)\operatorname{disc}(F)`$. Thus $`E\neq0`$.

The first row of $`E`$ is nonzero. Otherwise, using $`ET=TE`$ and
```math
e_1^{\mathsf t}T^j=e_{j+1}^{\mathsf t}\quad(0\leq j<d),
```
all rows of $`E`$ would be zero. Choose an integral vector $`v_1`$ whose reduction has $`e_1^{\mathsf t}Ev_1\neq0`$. Its recurrence sequence satisfies
```math
u_{p^s}-u_1=e_1^{\mathsf t}Ev_1\not\equiv0\pmod p.
```
Thus every multiplier working for all initial values must be divisible by $`p`$. This holds for each prime in the proposed radical and proves minimality. $`\square`$

<!-- end proof-4 -->

<a id="example-1"></a>

**Example 7 (The constant term cannot be omitted).**

<a id="label-ex-initialization"></a>

Let $`u_n=2^{n-1}+3^{n-1}`$ for $`n\geq1`$. The recurrence polynomial is
```math
F(x)=(x-2)(x-3)=x^2-5x+6,
```
and $`\operatorname{disc}(F)=1`$. For every positive integer $`s`$, $`u_{2^s}`$ is odd while $`u_1=2`$, so the prime $`2`$ is required in every repair. Likewise, $`u_{3^s}\equiv1\pmod3`$, so $`3`$ is required. For every even $`s`$, Theorem [1](#label-thm-recurrence) gives the factor $`6`$, which is therefore exact for this particular sequence.

<!-- end example-1 -->

<a id="remark-1"></a>

**Remark 8 (Comparison with the printed general statement of Luca–Ward).**

In [\[2\]](#ref-LW), Theorem 1(i), the stated sufficient multiplier is a multiple of $`\operatorname{lcm}(\Delta(K),\Delta(F))`$, with the recurrence initialized at $`u_1,\ldots,u_d`$, and the exponent required to be at least $`[K:\mathbb Q]`$ and divisible by the Galois-group exponent. Example [7](#label-ex-initialization) has $`K=\mathbb Q`$ and both discriminants equal to $`1`$. Thus the printed statement allows multiplier $`1`$, contradicted by its prime-$`2`$ Dold congruence. This is a counterexample to that statement with its printed indexing conventions; we do not assert an official erratum or any conclusion about the other theorems of the article. The initialization argument above accounts explicitly for the extra prime support from $`F(0)`$.

<!-- end remark-1 -->

## 4. The optimal universal sampling exponent

<a id="proof-5"></a>

**Proof of Theorem [3](#label-thm-optimal-exponent).**

If $`L_d\mid s`$, then $`L_e\mid s`$ for every $`e\leq d`$. Theorem [1](#label-thm-recurrence) therefore gives a finite repair for every sequence in the stated class.

Conversely, suppose $`L_d\nmid s`$. There is an integer $`f`$, with $`2\leq f\leq d`$, such that $`f\nmid s`$. Choose a prime $`q\equiv1\pmod f`$, whose existence follows from Dirichlet’s theorem; see [\[3, Example 8.34\]](#ref-Milne). The Galois group of $`\mathbb Q(\zeta_q)/\mathbb Q`$ is cyclic of order $`q-1`$ by the standard cyclotomic description [\[3, Section 6\]](#ref-Milne). Taking the fixed field of its subgroup of index $`f`$ produces a cyclic extension $`K/\mathbb Q`$ of degree $`f`$.

Choose a nonzero integral primitive element $`\alpha`$ of $`K`$, and let $`H\in\mathbb Z[x]`$ be its monic minimal polynomial. Then $`H`$ is separable of degree $`f`$ and $`H(0)\neq0`$. Let $`A`$ be the integer matrix of multiplication by $`\alpha`$ on the order $`\mathbb Z[\alpha]`$, in its basis $`1,\alpha,\ldots,\alpha^{f-1}`$. Thus $`H(A)=0`$.

Fix a generator $`\sigma`$ of $`\operatorname{Gal}(K/\mathbb Q)`$. Chebotarev’s theorem [\[3, Theorem 8.31\]](#ref-Milne), applied to the conjugacy class $`\{\sigma\}`$ in this finite Galois extension, gives infinitely many unramified rational primes with Frobenius $`\sigma`$. Each is inert, since its residue degree is the order $`f`$ of its Frobenius. Exclude also the finitely many prime divisors of $`[\mathcal O_K:\mathbb Z[\alpha]]`$. At every remaining prime $`p`$,
```math
\mathbb Z[\alpha]/p\mathbb Z[\alpha]
       \simeq\mathcal O_K/p\mathcal O_K\simeq\mathbb F_{p^f},
```
and the reduction $`\bar\alpha`$ generates this field over $`\mathbb F_p`$. Consequently
```math
\bar\alpha^{p^s}=\bar\alpha\quad\Longleftrightarrow\quad f\mid s.
```
Indeed the Frobenius orbit of a field generator has length $`f`$. Since $`f\nmid s`$, the multiplication matrix $`A^{p^s}-A`$ is nonzero modulo each of these infinitely many primes.

There are only $`f^2`$ entries. Hence some fixed pair $`(i,j)`$ satisfies
```math
(A^{p^s}-A)_{ij}\not\equiv0\pmod p
```
for infinitely many such $`p`$. Put $`u_n=(A^n)_{ij}`$. This is an integer sequence annihilated by $`H`$, so it belongs to the specified class. The Dold congruence for a repaired subsequence at $`n=p`$ would require
```math
p\mid C(u_{p^s}-u_1).
```
Each of infinitely many distinct primes must therefore divide $`C`$, which is impossible for a positive integer $`C`$. This proves necessity. $`\square`$

<!-- end proof-5 -->

<a id="remark-2"></a>

**Remark 9.**

The nonzero-constant-term restriction in Theorem [3](#label-thm-optimal-exponent) is essential with initialization at $`n=1`$. The sequence $`u_1=1`$ and $`u_n=0`$ for $`n>1`$ is annihilated by the separable polynomial $`x`$ but has infinite repair factor along every positive power.

<!-- end remark-2 -->

## 5. The exact Lucas factor

<a id="proof-6"></a>

**Proof of Theorem [2](#label-thm-lucas).**

Set
```math
A=\begin{pmatrix}P&-Q\\1&0\end{pmatrix}.
```
Since $`A^2=PA-QI`$ and the lower-left entries of $`I,A`$ are $`0,1`$, respectively, one has $`(A^n)_{21}=U_n`$ for all $`n\geq0`$.

If $`D\neq0`$, the polynomial $`F(x)=x^2-Px+Q`$ is separable. Every positive even exponent $`s=2k`$ meets the hypotheses of Theorem [4](#label-thm-matrix). That theorem proves sufficiency of $`\operatorname{rad}(|D|)`$.

To prove necessity, fix a prime $`p\mid D`$. The characteristic polynomial of $`A`$ modulo $`p`$ has a repeated root $`a\in\mathbb F_p`$: if $`p`$ is odd, $`a=P/2`$; if $`p=2`$, $`P`$ is even and $`a=Q`$ modulo $`2`$. Write $`A=aI+R`$ modulo $`p`$. The Cayley–Hamilton identity gives $`R^2=0`$, and $`R_{21}=1`$. Hence
```math
A^{p^{2k}}=a^{p^{2k}}I\pmod p,
```
so $`U_{p^{2k}}\equiv0\pmod p`$. The difference from $`U_1=1`$ forces $`p`$ to divide every repair multiplier.

If $`D=0`$, the same argument applies to every prime, precluding any positive finite repair multiplier. It also covers $`P=Q=0`$ directly. $`\square`$

<!-- end proof-6 -->

<a id="example-2"></a>

**Example 10.**

For $`P=6,Q=5`$ the discriminant is $`16`$ and
```math
U_n=\frac{5^n-1}{4}.
```
Every positive even-power subsequence has exact Dold repair factor $`2`$. Thus repeated prime powers in the polynomial discriminant do not require repeated prime powers in the repair factor.

<!-- end example-2 -->

<a id="remark-3"></a>

**Remark 11 (A stronger quadratic congruence).**

For any $`P,Q\in\mathbb Z`$, any prime $`p`$, any $`m\geq1`$, and $`r\geq2`$, the same Jordan-and-lifting argument with a degree-two annihilator gives
```math
U_{m p^{2r}}\equiv U_{m p^{2r-2}}\pmod{p^r}.
```
Here the exponent furnished by [(2)](#label-eq-localbound) is $`2r-2\geq r`$, since one may take $`h\leq1`$. This statement does not require a nonzero discriminant. At discriminant primes the scalar obstruction is consequently already visible at the first local level.

<!-- end remark-3 -->

## 6. Relation to previous bounds and verification

Theorem [2](#label-thm-lucas) sharpens the sufficient Lucas discriminant factor in [\[4,2\]](#ref-MW) to an exact radical. The matrix theorem explains this through nonsemisimple reduction. Rajs [\[5\]](#ref-Rajs), Theorem 4 and its proof, retains a denominator-clearing factor $`N`$ in addition to a radical for quadratic square subsequences. His Theorem 9 supplies a factor $`r_d\Delta_U\operatorname{rad}(\Delta_K)`$ for exponents divisible by the splitting-field degree. The bounds here remove higher prime powers and determine the uniform recurrence factor without constructing a splitting field.

The companion and initialization constructions give a uniform statement about integral recurrence modules. No assertion is made that every individual scalar repair factor is determined by the prime-index congruence alone in arbitrary order.

The accompanying script `check.py` uses exact modular integer arithmetic. It checks $`125{,}000`$ local instances across $`P,Q\in[-12,12]`$, eight primes from $`2`$ through $`19`$, local levels $`1`$ through $`5`$, and five multiplicative indices. It checks both the congruences and the Lucas minimality witnesses. These computations support the proof and do not replace its infinite-family argument. An independent implementation using arithmetic in the quadratic quotient ring additionally checks composite-index Dold congruences.

## References

<a id="ref-BGW"></a>

**\[1\]** J. Byszewski, G. Graff, and T. Ward, *Dold sequences, periodic points, and dynamics*, Bulletin of the London Mathematical Society (2021). [doi:10.1112/blms.12531](https://doi.org/10.1112/blms.12531).

<a id="ref-LW"></a>

**\[2\]** F. Luca and T. Ward, *On (Almost) Realizable Subsequences of Linearly Recurrent Sequences*, Journal of Integer Sequences **26** (2023), Article 23.4.6. <https://cs.uwaterloo.ca/journals/JIS/VOL26/Ward/ward9.pdf>.

<a id="ref-Milne"></a>

**\[3\]** J. S. Milne, *Algebraic Number Theory*, version 3.08 (2020), Section 6, Theorem 8.31, and Example 8.34. <https://www.jmilne.org/math/CourseNotes/ANTc.pdf>.

<a id="ref-MW"></a>

**\[4\]** P. Moss and T. Ward, *Fibonacci Along Even Powers Is (Almost) Realizable*, Fibonacci Quarterly **60** (2022), 40–47. <https://www.fq.math.ca/Papers/60-1/ward01062021.pdf>.

<a id="ref-Rajs"></a>

**\[5\]** M. Rajs, *On Dold condition and fail factor of linear recurrent sequences*, arXiv:2509.09847v1 (2025). <https://arxiv.org/html/2509.09847>.
