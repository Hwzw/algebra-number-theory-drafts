# Critical-scale growth bounds for congruence-preserving functions over finite fields

Henry Zweiman

September 9, 2026

## Abstract

Let $`R=\mathbb F_q[t]`$. We prove that a function $`f:R\to R`$ preserving congruences modulo every irreducible polynomial is a polynomial map if $`\deg f(A)\le q^{\deg A}/(256q^2)`$ for every input of sufficiently large degree. This replaces the factor $`q^n/n`$ in the growth hypothesis of Bell and Nguyen by a positive constant times $`q^n`$. The proof uses integer-valued Carlitz digit polynomials, multiplied by a squarefree primorial, in the auxiliary-polynomial method. The rationality step is Bell and Nguyen’s linear-growth theorem. For $`\mathbb F_q`$-linear functions we prove the sharp threshold $`q/(q-1)`$ for $`\limsup_n\deg f(t^n)/q^n`$, and give a nonpolynomial example attaining it. We also give a Newton-coefficient formulation of the remaining sharp problem and an obstruction to a coefficient estimate using growth alone.

## 1. Results and their scope

Throughout, $`q`$ is a prime power, $`R=\mathbb F_q[t]`$, and $`K=\mathbb F_q(t)`$. We set $`\deg 0=-\infty`$. Write $`V_n=\{A\in R:\deg A<n\}`$, including zero, and let $`\mathcal P`$ be the set of monic irreducible polynomials in $`R`$. We say that $`f:R\to R`$ preserves prime congruences if

<a id="label-eq-cp"></a>

```math
\tag{1}
 P\mid A-B\quad\Longrightarrow\quad P\mid f(A)-f(B)
 \qquad(A,B\in R,\ P\in\mathcal P).
```

A polynomial map is the evaluation of one polynomial in $`K[X]`$ on $`R`$. Its coefficients need not belong to $`R`$.

Bell and Nguyen [\[1, Theorem 1.4\]](#ref-BN) proved polynomiality under $`\deg f(A)<q^n/(27qn)`$ for all sufficiently large $`n=\deg A`$. Their Section 4 asks whether the growth function $`q^n/n`$ can be enlarged; Question 4.1 proposes every fixed constant below the primorial threshold. Our first theorem addresses the enlargement of the growth scale.

<a id="theorem-1"></a>

**Theorem 1.1.**

<a id="label-thm-general"></a>

Let $`\ell`$ be the least positive integer such that $`q^\ell\ge16`$, and set
```math
c_q=\frac1{16q^{\ell+1}}.
```
If $`f:R\to R`$ satisfies [(1)](#label-eq-cp) and

<a id="label-eq-growth"></a>

```math
\tag{2}
 \deg f(A)\le c_q q^{\deg A}
```

for every input of sufficiently large degree, then $`f`$ is a polynomial map. In particular, the bound $`q^{\deg A}/(256q^2)`$ suffices.

<!-- end theorem-1 -->

<a id="corollary-1"></a>

**Corollary 1.2.**

<a id="label-cor-littleo"></a>

If $`f`$ satisfies [(1)](#label-eq-cp) and $`\max_{\deg A=n}\deg f(A)=o(q^n)`$, then $`f`$ is a polynomial map.

<!-- end corollary-1 -->

The constant in Theorem [1.1](#label-thm-general) is chosen for a transparent proof, rather than optimized. For $`q=2,3,4,9`$ the stated $`c_q`$ is, respectively, $`1/512,1/1296,1/1024,1/11664`$. Put

<a id="label-eq-primorial"></a>

```math
\tag{3}
 \Pi_n=\prod_{\substack{P\in\mathcal P\\\deg P\le n}}P,
 \qquad d_n=\deg\Pi_n,\qquad \Pi_0=1.
```

Then $`d_n/q^n\to q/(q-1)`$. The proposed sharp condition in [\[1, Question 4.1\]](#ref-BN) is $`\deg f(A)\le(1-\varepsilon)d_n`$ on every sufficiently large degree-$`n`$ shell, for some $`\varepsilon>0`$. Theorem [1.1](#label-thm-general) does not prove that full assertion.

<a id="theorem-2"></a>

**Theorem 1.3.**

<a id="label-thm-additive"></a>

Suppose $`f:R\to R`$ is $`\mathbb F_q`$-linear and satisfies [(1)](#label-eq-cp). If $`f`$ is not a polynomial map, then
```math
\limsup_{n\to\infty}\frac{\deg f(t^n)}{q^n}\ge\frac q{q-1}.
```
This constant is sharp, even with the maximum over all inputs of degree $`n`$ in the numerator. Thus Bell–Nguyen Question 4.1 holds for $`\mathbb F_q`$-linear functions.

<!-- end theorem-2 -->

The interpolation polynomials below are classical. Wagner’s work [\[3,4\]](#ref-W74) describes related coefficient divisibility for functions preserving all polynomial moduli, including prime powers. Here only [(1)](#label-eq-cp) is assumed, and the squarefree factor $`\Pi_n`$ replaces the least common multiple with prime powers. Li and Sha [\[2\]](#ref-LS) study congruence-preserving maps between finite residue rings. We use the classical interpolation tools to obtain a growth theorem for arbitrary maps on the infinite ring $`R`$.

## 2. Integral interpolation polynomials

Define

<a id="label-eq-carlitz"></a>

```math
\tag{4}
 e_i(X)=\prod_{B\in V_i}(X-B),\qquad
 H_i=e_i(t^i),\qquad E_i(X)=\frac{e_i(X)}{H_i}.
```

In particular $`e_0(X)=E_0(X)=X`$ and $`H_0=1`$. These are the normalized linear Carlitz polynomials; see also [\[3, Section 2\]](#ref-W74). We give the needed elementary properties.

<a id="lemma-1"></a>

**Lemma 2.1.**

<a id="label-lem-carlitz"></a>

The polynomial $`E_i`$ is $`\mathbb F_q`$-linear, has $`X`$-degree $`q^i`$, and takes values in $`R`$ on $`R`$. Moreover,

<a id="label-eq-Hdegree"></a>

<a id="label-eq-Hvaluation"></a>

<a id="label-eq-triangular"></a>

<a id="label-eq-Edegree"></a>

```math
\begin{align}
 \deg H_i&=iq^i,\tag{5}\\
 v_P(H_i)&=\sum_{\substack{k\ge1\\k\deg P\le i}}q^{i-k\deg P},
       \tag{6}\\
 E_i(t^j)&=0\ (j<i),\qquad E_i(t^i)=1,\tag{7}\\
 \deg E_i(A)&=(\deg A-i)q^i\quad(\deg A\ge i).
       \tag{8}
\end{align}
```

<!-- end lemma-1 -->

<a id="proof-1"></a>

**Proof.**

The decomposition $`V_{i+1}=V_i+\mathbb F_qt^i`$ gives inductively
```math
e_{i+1}(X)=e_i(X)^q-H_i^{q-1}e_i(X).
```
This proves linearity and the asserted $`X`$-degree. The factors of $`H_i`$ are exactly all monic degree-$`i`$ polynomials, proving [(5)](#label-eq-Hdegree). For $`P`$ of degree $`d`$, the number of those polynomials divisible by $`P^k`$ is $`q^{i-kd}`$ if $`kd\le i`$ and zero otherwise. This proves [(6)](#label-eq-Hvaluation).

For arbitrary $`A`$, if $`e_i(A)=0`$ there is nothing to prove. Otherwise, for every $`k`$ with $`kd\le i`$, the map $`V_i\to R/(P^k)`$ is onto and has fibers of size $`q^{i-kd}`$. Therefore $`v_P(e_i(A))\ge v_P(H_i)`$. This holds at every prime, so $`E_i(A)\in R`$. The triangular assertions follow from the definitions. If $`\deg A\ge i`$, every factor $`A-B`$, $`B\in V_i`$, has degree $`\deg A`$, proving [(8)](#label-eq-Edegree). $`\square`$

<!-- end proof-1 -->

<a id="lemma-2"></a>

**Lemma 2.2.**

<a id="label-lem-primecount"></a>

For $`n\ge1`$,
```math
q^n\le d_n<\frac q{q-1}q^n,
 \qquad
 d_n=\frac{q(q^n-1)}{q-1}+O_q(q^{n/2}).
```

<!-- end lemma-2 -->

<a id="proof-2"></a>

**Proof.**

The squarefree polynomial $`t^{q^n}-t`$ divides $`\Pi_n`$, proving the lower bound. If $`I_j`$ counts monic irreducibles of degree $`j`$, then $`jI_j\le q^j`$, whence $`d_n\le\sum_{j=1}^nq^j<q^{n+1}/(q-1)`$. From $`jI_j=\sum_{a\mid j}\mu(a)q^{j/a}`$, the error in replacing $`jI_j`$ by $`q^j`$ is at most $`\sum_{r\le j/2}q^r=O_q(q^{j/2})`$. Summing gives the final assertion. $`\square`$

<!-- end proof-2 -->

For $`0\le j<q^s`$, write $`j=\sum_{i=0}^{s-1}j_iq^i`$ with $`0\le j_i<q`$. Set

<a id="label-eq-digit"></a>

```math
\tag{9}
 F_j(X)=\prod_{i=0}^{s-1}E_i(X)^{j_i},\qquad
 G_{s,j}(X)=\Pi_{s-1}F_j(X).
```

The first expression is independent of appended zero digits; $`F_0=1`$.

<a id="lemma-3"></a>

**Lemma 2.3.**

<a id="label-lem-digit"></a>

The polynomials $`G_{s,j}`$, $`0\le j<q^s`$, are $`R`$-valued and preserve prime congruences. Their $`X`$-degrees are $`j`$, so they are linearly independent over $`K`$. Put $`\kappa=(q+1)/(q-1)`$. For $`D\ge s-1`$,

<a id="label-eq-digitheight"></a>

```math
\tag{10}
 \deg G_{s,j}(A)<(D-s+\kappa)q^s
 \qquad(A\in V_{D+1}).
```

<!-- end lemma-3 -->

<a id="proof-3"></a>

**Proof.**

Integrality follows from Lemma [2.1](#label-lem-carlitz). If $`\deg P\le s-1`$, every value of $`G_{s,j}`$ is divisible by $`P`$. If $`\deg P>s-1`$, all the $`H_i`$ in [(9)](#label-eq-digit) are $`P`$-units. Thus $`G_{s,j}\in R_{(P)}[X]`$ and preserves congruences modulo $`P`$. Also $`\deg_X F_j=j`$.

If a factor with $`i>\deg A`$ has positive exponent, the value is zero. In every other case, Lemmas [2.1](#label-lem-carlitz) and [2.2](#label-lem-primecount) give, with $`C=q/(q-1)`$,
```math
\begin{align*}
 \deg G_{s,j}(A)
 &\le d_{s-1}+\sum_{i=0}^{s-1}(q-1)(D-i)q^i\\
 &<\frac{q^s}{q-1}+(D-s+C)q^s-D-C
 <(D-s+\kappa)q^s.
\end{align*}
```
Here the same strict bound for $`d_0=0`$ applies when $`s=1`$. $`\square`$

<!-- end proof-3 -->

## 3. The general growth theorem

We first recall the elementary vanishing principle underlying the Bell–Nguyen polynomial method [\[1, Lemma 2.1\]](#ref-BN).

<a id="lemma-4"></a>

**Lemma 3.1.**

<a id="label-lem-vanishing"></a>

Suppose $`g:R\to R`$ satisfies [(1)](#label-eq-cp), vanishes on $`V_{M+1}`$, and $`\deg g(A)<d_{\deg A}`$ whenever $`\deg A>M`$. Then $`g=0`$.

<!-- end lemma-4 -->

<a id="proof-4"></a>

**Proof.**

If not, choose $`A`$ of least degree $`D`$ with $`g(A)\ne0`$. Then $`D>M`$. For each prime $`P`$ of degree at most $`D`$, the remainder of $`A`$ modulo $`P`$ has degree less than $`D`$ and hence has zero image. Condition [(1)](#label-eq-cp) gives $`\Pi_D\mid g(A)`$, contradicting its degree bound. $`\square`$

<!-- end proof-4 -->

<a id="proposition-1"></a>

**Proposition 3.2.**

<a id="label-prop-curve"></a>

Under the hypotheses of Theorem [1.1](#label-thm-general), there is a nonzero $`Q\in K[X,Y]`$ such that $`Q(A,f(A))=0`$ for every $`A\in R`$.

<!-- end proposition-1 -->

<a id="proof-5"></a>

**Proof.**

Take $`M`$ sufficiently large and put
```math
s=M-\ell\ge1,\qquad T=\lfloor q^M/4\rfloor,
 \qquad J=4q^{\ell+1}.
```
We may require $`\deg f(A)\le c_qq^M`$ for every $`A\in V_{M+1}`$: the finitely many exceptions to [(2)](#label-eq-growth) have bounded image degrees. Choose unknowns $`u_{h,j,k}\in\mathbb F_q`$ and form

<a id="label-eq-auxiliary"></a>

```math
\tag{11}
 Q(X,Y)=\sum_{h=0}^T\sum_{j=0}^{q^s-1}\sum_{k=0}^J
       u_{h,j,k}t^hG_{s,j}(X)Y^k.
```

Then $`g(A)=Q(A,f(A))`$ is $`R`$-valued and preserves prime congruences. Since $`\ell\le4`$, $`\kappa\le3`$, $`q^\ell\ge16`$, and $`Jc_q=1/4`$, Lemma [2.3](#label-lem-digit) gives

<a id="label-eq-ballheight"></a>

```math
\tag{12}
 \deg g(A)<\frac{q^M}{4}+(\ell+\kappa)q^{M-\ell}
                       +\frac{q^M}{4}
 \le\frac{15}{16}q^M<q^M
 \quad(A\in V_{M+1}).
```

Thus requiring $`g(A)=0`$ for these $`q^{M+1}`$ inputs imposes at most $`q^{2M+1}`$ homogeneous linear equations over $`\mathbb F_q`$. The number of unknowns is strictly larger:
```math
(T+1)q^{M-\ell}(J+1)
 >\frac{q^M}{4}q^{M-\ell}4q^{\ell+1}=q^{2M+1}.
```
A nonzero solution exists. It represents a nonzero polynomial $`Q`$: for each power of $`Y`$, the $`G_{s,j}`$ have distinct $`X`$-degrees, and $`1,t,\ldots,t^T`$ are independent over $`\mathbb F_q`$.

For an input of degree $`D=M+r`$, $`r\ge0`$, the same calculation gives

<a id="label-eq-outerheight"></a>

```math
\tag{13}
 \frac{\deg g(A)}{q^D}
 <\frac{q^{-r}}4+(r+\ell+\kappa)q^{-\ell-r}+\frac14
 \le\frac{15}{16}.
```

The two $`r`$-dependent summands are nonincreasing: for $`a\ge1`$, $`(r+a+1)/q\le r+a`$. By Lemma [2.2](#label-lem-primecount) we have $`q^D\le d_D`$. Lemma [3.1](#label-lem-vanishing) therefore gives $`g=0`$. $`\square`$

<!-- end proof-5 -->

<a id="proof-6"></a>

**Proof of Theorem [1.1](#label-thm-general).**

Clear denominators in the relation from Proposition [3.2](#label-prop-curve), and write
```math
Q=\sum_{k=0}^vP_k(X)Y^k,\qquad P_k\in R[X],\quad P_v\ne0.
```
Necessarily $`v>0`$, since a nonzero polynomial in $`X`$ cannot vanish on all of $`R`$. There are constants $`a,b\ge0`$ such that
```math
\deg P_k(A)\le a\deg A+b
```
for every nonzero $`A`$ and every $`k`$. If $`P_v(A)\ne0`$ and $`\deg f(A)>a\deg A+b`$, the term $`P_v(A)f(A)^v`$ has strictly larger degree than every other term of $`Q(A,f(A))`$, a contradiction. Enlarge $`b`$ to cover the finitely many roots of $`P_v`$ and obtain $`\deg f(t^n)=O(n)`$ for $`n\ge0`$.

Bell and Nguyen [\[1, Theorem 3.1\]](#ref-BN) prove that a function satisfying [(1)](#label-eq-cp) is a polynomial map if $`\deg f(U^n)=O(n)`$ for some $`U\in R`$ with $`U'\ne0`$. Apply that theorem with $`U=t`$. Finally, minimality of $`\ell`$ gives $`q^\ell<16q`$, and hence $`c_q>1/(256q^2)`$. $`\square`$

<!-- end proof-6 -->

The gain comes from [(10)](#label-eq-digitheight): $`q^{M-\ell}`$ independent polynomials have value degrees $`O(q^M)`$ on $`V_{M+1}`$. Ordinary monomials of comparable $`X`$-degree have value degrees of order $`Mq^M`$. The rational denominators of the digit polynomials do not enter the value-height estimate, while the factor $`\Pi_{s-1}`$ ensures the exact congruences needed for vanishing.

## 4. The sharp linear case

Every $`\mathbb F_q`$-linear $`f:R\to R`$ has a unique locally finite expansion

<a id="label-eq-linearseries"></a>

```math
\tag{14}
 f(A)=\sum_{i\ge0}a_iE_i(A),\qquad a_i\in R.
```

Indeed, recursively set $`a_n=f(t^n)-\sum_{i<n}a_iE_i(t^n)`$. Lemma [2.1](#label-lem-carlitz) makes the coefficients integral. The resulting map agrees with $`f`$ on the basis $`1,t,t^2,\ldots`$, and $`E_i(A)=0`$ for $`i>\deg A`$.

<a id="proposition-2"></a>

**Proposition 4.1.**

<a id="label-prop-linearcriterion"></a>

The function [(14)](#label-eq-linearseries) preserves prime congruences if and only if $`\Pi_i\mid a_i`$ for every $`i\ge0`$.

<!-- end proposition-2 -->

<a id="proof-7"></a>

**Proof.**

Fix $`P`$ of degree $`d`$. For $`i<d`$, $`H_i`$ is a $`P`$-unit, so $`E_i`$ is a polynomial over $`R_{(P)}`$. If $`P\mid a_i`$ for every $`i\ge d`$, all higher terms vanish modulo $`P`$, proving sufficiency.

Conversely, subtract $`\sum_{i<d}a_iE_i`$ from $`f`$. The result modulo $`P`$ is a linear function on $`R/(P)`$ vanishing at the basis $`1,t,\ldots,t^{d-1}`$, and hence vanishing everywhere. Evaluating successively at $`t^d,t^{d+1},\ldots`$ and using $`E_i(t^i)=1`$ proves $`P\mid a_i`$ for every $`i\ge d`$. Apply this at all primes. $`\square`$

<!-- end proof-7 -->

<a id="lemma-5"></a>

**Lemma 4.2.**

<a id="label-lem-transform"></a>

Write $`\alpha_n=\deg a_n`$, $`\beta_n=\deg f(t^n)`$, and $`S_n=(q^n-1)/(q-1)`$. Then

<a id="label-eq-transform"></a>

```math
\tag{15}
 \alpha_n\le S_n+\max_{0\le j\le n}(\beta_j-S_j).
```

Consequently,

<a id="label-eq-limsup"></a>

```math
\tag{16}
 \limsup_n\frac{\alpha_n}{q^n}
 \le\max\left\{\frac1{q-1},\limsup_n\frac{\beta_n}{q^n}\right\}.
```

<!-- end lemma-5 -->

<a id="proof-8"></a>

**Proof.**

The recursion and [(8)](#label-eq-Edegree) give $`\alpha_n\le\max\{\beta_n,\max_{i<n}(\alpha_i+(n-i)q^i)\}`$. Since $`(n-i)q^i\le S_n-S_i`$, induction proves [(15)](#label-eq-transform). For the limiting assertion it suffices to consider a finite right side. Choose $`c`$ strictly larger than it, and then choose $`c_0<c`$ with $`c_0>1/(q-1)`$ such that eventually $`\beta_j\le c_0q^j`$. The finitely many earlier $`\beta_j-S_j`$ have an upper bound $`B`$. Equation [(15)](#label-eq-transform) gives
```math
\alpha_n\le\max\{S_n+B,c_0q^n\}
```
for all large $`n`$. Divide by $`q^n`$ and let $`c`$ decrease to the asserted bound. The identically zero map causes no exception with the convention $`\deg0=-\infty`$. $`\square`$

<!-- end proof-8 -->

<a id="proof-9"></a>

**Proof of Theorem [1.3](#label-thm-additive).**

If $`\limsup\beta_n/q^n<q/(q-1)`$, Lemmas [2.2](#label-lem-primecount) and [4.2](#label-lem-transform) give $`\deg a_n<d_n`$ for all large $`n`$. Proposition [4.1](#label-prop-linearcriterion) forces $`a_n=0`$ there. Thus [(14)](#label-eq-linearseries) is a finite polynomial.

For sharpness define

<a id="label-eq-boundary"></a>

```math
\tag{17}
 f_*(A)=\sum_{i\ge0}\Pi_iE_i(A).
```

This map is well-defined, $`\mathbb F_q`$-linear, and preserves prime congruences. Put $`C=q/(q-1)`$. For $`\deg A=n`$,
```math
\deg f_*(A)\le\max_{0\le i\le n}\{d_i+(n-i)q^i\}\le Cq^n,
```
because $`d_i<Cq^i`$ and $`C+k\le Cq^k`$ for $`k\ge0`$. For $`i<n`$ the same bound is at most $`(C+1)q^{n-1}`$: the sequence $`(C+k)/q^k`$ decreases for $`k\ge1`$. At $`A=t^n`$ the term with $`i=n`$ has degree $`d_n`$, and $`d_n/q^n\to C>(C+1)/q`$. Eventually it strictly dominates all other terms. Therefore $`\deg f_*(t^n)=d_n`$ for all sufficiently large $`n`$. This gives the asserted sharp limit and proves nonpolynomiality, since a fixed polynomial map has value degrees $`O(n)`$ at $`t^n`$. $`\square`$

<!-- end proof-9 -->

Wagner’s characterization [\[3, Theorem 3.2\]](#ref-W74) for the stronger all-moduli condition uses
```math
L_i=\prod_{r=1}^i(t^{q^r}-t)
```
in place of $`\Pi_i`$. Proposition [4.1](#label-prop-linearcriterion) is the squarefree counterpart. The boundary construction above and the degree estimate address the prime-congruence growth condition of [\[1\]](#ref-BN).

## 5. Newton coefficients and the remaining threshold

Fix an ordering $`\alpha_0=0,\alpha_1=1,\ldots,\alpha_{q-1}`$ of $`\mathbb F_q`$. For the base-$`q`$ expansion $`j=\sum_i j_iq^i`$, put $`A_j=\sum_i\alpha_{j_i}t^i`$. The first $`q^m`$ entries form $`V_m`$ and $`A_{q^m}=t^m`$. Define

<a id="label-eq-newton"></a>

```math
\tag{18}
 B_0(X)=1,\qquad
 B_n(X)=\frac{\prod_{j<n}(X-A_j)}{\prod_{j<n}(A_n-A_j)}\quad(n\ge1).
```

<a id="proposition-3"></a>

**Proposition 5.1.**

<a id="label-prop-newton"></a>

Every function $`f:R\to R`$ has a unique locally finite expansion
```math
f(A)=\sum_{n\ge0}b_nB_n(A),\qquad b_n\in R.
```
It preserves prime congruences if and only if

<a id="label-eq-newtoncriterion"></a>

```math
\tag{19}
 \Pi_{\lfloor\log_qn\rfloor}\mid b_n\qquad(n\ge1).
```

There is no restriction on $`b_0`$.

<!-- end proposition-3 -->

<a id="proof-10"></a>

**Proof.**

For $`P`$ of degree $`d`$, the denominator in [(18)](#label-eq-newton) has valuation
```math
\sum_{k\ge1}\left\lfloor\frac n{q^{kd}}\right\rfloor.
```
Indeed, each aligned block of $`q^{kd}`$ consecutive entries runs through every residue modulo $`P^k`$. In the final incomplete block preceding $`A_n`$, none has its residue: their differences from $`A_n`$ are nonzero and have degree less than $`kd`$. The numerator at any input has at least the same valuation. Thus all $`B_n`$ are $`R`$-valued. Since $`B_n(A_n)=1`$ and $`B_n(A_i)=0`$ for $`i<n`$, integral triangular recursion gives the expansion and uniqueness.

Fix $`P`$ of degree $`d`$. Terms with $`n<q^d`$ have $`P`$-unit denominators. If $`P\mid b_n`$ for $`n\ge q^d`$, the other terms vanish pointwise modulo $`P`$, proving sufficiency. Conversely, subtract the initial sum with $`n<q^d`$. The resulting congruence-preserving function vanishes on the complete residue system $`A_0,\ldots,A_{q^d-1}`$, hence everywhere modulo $`P`$. Successive evaluation at the remaining $`A_n`$ gives $`P\mid b_n`$ for $`n\ge q^d`$. Taking all primes proves [(19)](#label-eq-newtoncriterion). $`\square`$

<!-- end proof-10 -->

This statement concerns first powers of primes. It makes no assertion that the same ordering characterizes preservation of all prime powers; compare the local constructions in [\[2, Theorem 1.11\]](#ref-LS).

The sharp general question is consequently a truncation problem: does [(19)](#label-eq-newtoncriterion), together with the strict subcritical bound $`(1-\varepsilon)d_n`$ on degree-$`n`$ inputs, force $`b_n=0`$ eventually? A finite expansion is equivalent to a polynomial map. The next example shows why value growth by itself cannot supply the needed coefficient margin.

<a id="proposition-4"></a>

**Proposition 5.2.**

<a id="label-prop-obstruction"></a>

Let $`\delta(A)`$ be $`1`$ at $`A=0`$ and $`0`$ elsewhere. Its coefficients in [(18)](#label-eq-newton) satisfy, for $`m\ge1`$,
```math
\deg b_{q^m}=\frac{q^{m+1}-q}{q-1}-m,
 \qquad \frac{\deg b_{q^m}}{d_m}\longrightarrow1.
```

<!-- end proposition-4 -->

<a id="proof-11"></a>

**Proof.**

The leading coefficient of interpolation at $`A_0,\ldots,A_n`$ gives
```math
b_n=\frac{\prod_{j<n}(A_n-A_j)}{\prod_{j=1}^n(-A_j)}.
```
For $`n=q^m`$, the numerator has degree $`mq^m`$. The denominator has degree $`m+\sum_{r=0}^{m-1}r(q-1)q^r`$. Subtraction gives the formula; Lemma [2.2](#label-lem-primecount) gives the limit. $`\square`$

<!-- end proof-11 -->

The function $`\delta`$ fails [(1)](#label-eq-cp), since $`\delta(0)=1`$ and $`\delta(P)=0`$. It is an obstruction to an estimate using growth alone, not a counterexample to the sharp question. A proof at every constant below $`q/(q-1)`$ must use the congruences and the general coefficient transform together, or supply a different rigidity argument.

## 6. Verification and further directions

The proofs hold for every prime power and do not depend on finite computations. The accompanying exact-arithmetic checker tests both prime and extension fields. The digit-basis audit covers 8,570 literal values over $`\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_9`$, including integrality, degrees, and congruences. It also checks 56,320 instances of the height and propagation inequalities and 2,816 dimension inequalities. A separate audit covers the additive criterion, its boundary example, and the general Newton criterion with positive and negative examples.

The main remaining problem is the sharp arbitrary-function threshold. The integer-valued auxiliary family suggests optimizing its value-height profile and replacing the rectangular set of indices in [(11)](#label-eq-auxiliary) by a weighted set. Those changes do not by themselves prove the sharp constant. Theorems [1.1](#label-thm-general) and [1.3](#label-thm-additive), and their coefficient formulations, constitute one growth-rigidity result rather than separate solutions to the full question.

## References

<a id="ref-BN"></a>

**\[1\]** J. P. Bell and K. D. Nguyen, *An analogue of Ruzsa’s conjecture for polynomials over finite fields*, J. Combin. Theory Ser. A **178** (2021), 105337. [doi:10.1016/j.jcta.2020.105337](https://doi.org/10.1016/j.jcta.2020.105337). Theorem and question numbering here refers to [arXiv:1910.08255v1](https://arxiv.org/abs/1910.08255v1) (2019).

<a id="ref-LS"></a>

**\[2\]** X. Li and M. Sha, *Congruence preserving functions in the residue class rings of polynomials over finite fields*, Finite Fields Appl. **61** (2020), 101604. [doi:10.1016/j.ffa.2019.101604](https://doi.org/10.1016/j.ffa.2019.101604); [arXiv:1807.02379v2](https://arxiv.org/abs/1807.02379v2).

<a id="ref-W74"></a>

**\[3\]** C. G. Wagner, *Linear pseudo-polynomials over $`\operatorname{GF}[q,x]`$*, Arch. Math. **25** (1974), 385–390. [Author’s copy](https://web.math.utk.edu/~cwagner/papers/pseudo.pdf).

<a id="ref-W76"></a>

**\[4\]** C. G. Wagner, *Polynomials over $`\operatorname{GF}(q,x)`$ with integral-valued differences*, Arch. Math. **27** (1976), 495–501. [Author’s copy](https://web.math.utk.edu/~cwagner/papers/gfqx.pdf).
