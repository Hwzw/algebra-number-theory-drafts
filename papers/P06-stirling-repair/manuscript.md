# Prime support and growth of Stirling repair factors

Henry Zweiman

September 8, 2026

## Abstract

For fixed $`k\geq1`$, let $`F_k`$ be the least positive integer such that $`(F_k S(n+k-1,k))_{n\geq1}`$ counts the periodic points of a map, where $`S(N,k)`$ is a Stirling number of the second kind. We prove
```math
\mathop{\mathrm{rad}}((k-1)!)\mid F_k\mid\mathop{\mathrm{lcm}}(1,\ldots,k-1).
```
Thus the prime divisors of $`F_k`$ are exactly the primes below $`k`$, and the previous factorial bound can be replaced by a least common multiple. We also prove $`v_p(F_k)=1`$ whenever $`p<k\leq p^2`$, and $`v_p(F_{p^j+1})=j`$ for every prime $`p`$ and $`j\geq1`$. A formula for prime-power values in terms of the base-$`p`$ digits of $`k-1`$ also yields $`\log(F_k/\mathop{\mathrm{rad}}((k-1)!))\sim\sqrt{k}`$. These results establish Conjectures 1, 2, 3, and 4(d) of Miska and Ward. The upper bound follows from a Frobenius congruence for an integral recurrence; the prime-support obstruction comes from the repeated poles of its generating function modulo $`p`$.

## 1. Introduction

An integer sequence $`(a_n)_{n\geq1}`$ satisfies the *Dold condition* if

<a id="label-eq-dold"></a>

```math
\tag{1}
 n\mid\sum_{d\mid n}\mu(n/d)a_d\qquad(n\geq1).
```

For a nonnegative integer sequence, realizability as the numbers of fixed points of the iterates of a map is equivalent to [(1)](#label-eq-dold) together with nonnegativity of the sums in [(1)](#label-eq-dold). Indeed, their quotients by $`n`$ are precisely the required numbers of orbits of length $`n`$. A disjoint union of those finite cycles supplies a realizing map.

Miska and Ward introduced the least positive multiplier $`\mathop{\mathrm{Fail}}(a)`$ making a sequence realizable and studied it for Stirling sequences [\[3\]](#ref-MW). Throughout this paper,
```math
a_n^{(k)}=S(n+k-1,k),\qquad
 F_k=\mathop{\mathrm{Fail}}\bigl((a_n^{(k)})_{n\geq1}\bigr).
```
They proved that $`F_k`$ is finite and divides $`(k-1)!`$ [\[3, Theorem 7\]](#ref-MW). Their Conjectures 1 and 2 predict, respectively, that every prime below $`k`$ divides $`F_k`$, and that primes in $`[\sqrt{k},k)`$ have valuation exactly one. Their Conjecture 4(d) predicts $`v_p(F_{p^j+1})=j`$. Their Conjecture 3 predicts that $`F_k/\mathop{\mathrm{rad}}((k-1)!)`$ tends to infinity. We prove all four assertions, improve the factorial upper bound, and determine the logarithmic growth of that ratio.

<a id="theorem-1"></a>

**Theorem 1.**

<a id="label-thm-main"></a>

For every integer $`k\geq1`$,

<a id="label-eq-bounds"></a>

```math
\tag{2}
 \mathop{\mathrm{rad}}((k-1)!)\mid F_k\mid L_{k-1},
 \qquad L_{k-1}=\mathop{\mathrm{lcm}}(1,\ldots,k-1),
```

where $`L_0=1`$. More precisely, for every prime $`p<k`$,
```math
1\leq v_p(F_k)\leq\lfloor\log_p(k-1)\rfloor.
```
In addition:

1.  if $`p<k\leq p^2`$, then $`v_p(F_k)=1`$;

2.  if $`k=p^j+1`$ with $`j\geq1`$, then $`v_p(F_k)=j`$.

<!-- end theorem-1 -->

<a id="theorem-2"></a>

**Theorem 2.**

<a id="label-thm-growth"></a>

Let $`\vartheta(x)=\sum_{p\leq x}\log p`$, where the sum is over primes. As $`k\to\infty`$, with $`K=k-1`$,

<a id="label-eq-theta-growth"></a>

```math
\tag{3}
 \log\frac{F_k}{\mathop{\mathrm{rad}}(K!)}
 =\vartheta(\sqrt K)+O\bigl(K^{1/3}(\log K)^2\bigr).
```

Consequently,

<a id="label-eq-growth"></a>

```math
\tag{4}
 \log\frac{F_k}{\mathop{\mathrm{rad}}((k-1)!)}\sim\sqrt{k}.
```

<!-- end theorem-2 -->

The estimate [(3)](#label-eq-theta-growth) is elementary. Only the passage to [(4)](#label-eq-growth) uses the prime number theorem.

The upper bound is sharp at the prime $`p`$ whenever $`k=p^j+1`$. The argument for prime support applies to the entire sequence and does not require locating an individual prime-power witness. In particular, our result does not establish the proposed finite cutoff for computing $`F_k`$ described in [\[1, Section 4.5\]](#ref-BGW).

## 2. Local congruences and the integral recurrence

For a sequence $`a`$ write $`D_n(a)=\sum_{d\mid n}\mu(n/d)a_d`$. The following standard local form of the Dold condition will be useful; we include the proof to fix the indexing.

<a id="lemma-1"></a>

**Lemma 3.**

<a id="label-lem-local"></a>

An integer sequence $`a`$ satisfies the Dold condition if and only if

<a id="label-eq-local"></a>

```math
\tag{5}
 a_{mp^r}\equiv a_{mp^{r-1}}\pmod {p^r}
```

for every prime $`p`$, every $`r\geq1`$, and every $`m\geq1`$ with $`p\nmid m`$.

<!-- end lemma-1 -->

<a id="proof-1"></a>

**Proof.**

Möbius inversion gives $`a_n=\sum_{d\mid n}D_d(a)`$. Thus
```math
a_{mp^r}-a_{mp^{r-1}}=\sum_{d\mid m}D_{dp^r}(a),
```
which proves one implication. Conversely,
```math
D_{mp^r}(a)=\sum_{d\mid m}\mu(m/d)
       \bigl(a_{dp^r}-a_{dp^{r-1}}\bigr).
```
The congruences imply $`p^r\mid D_{mp^r}(a)`$. Applying this at each prime factor of an arbitrary index gives [(1)](#label-eq-dold). $`\square`$

<!-- end proof-1 -->

<a id="lemma-2"></a>

**Lemma 4.**

<a id="label-lem-sign"></a>

For every $`k\geq1`$, the sequence $`a^{(k)}`$ satisfies $`D_n(a^{(k)})\geq0`$ for all $`n\geq1`$. Consequently, $`F_k`$ is its least positive Dold multiplier.

<!-- end lemma-2 -->

<a id="proof-2"></a>

**Proof.**

For $`k=1`$ the sequence is constant equal to one, so the assertion is immediate. For $`k\geq2`$, the Stirling recurrence gives
```math
a_{n+1}^{(k)}=k a_n^{(k)}+S(n+k-1,k-1)\geq2a_n^{(k)}.
```
As $`a_1^{(k)}=1`$, for $`n\geq2`$ we have
```math
\sum_{d=1}^{n-1}a_d^{(k)}
 \leq a_n^{(k)}\sum_{d=1}^{n-1}2^{d-n}<a_n^{(k)}.
```
Therefore $`D_n(a^{(k)})\geq a_n^{(k)}-\sum_{d<n}a_d^{(k)}>0`$. Positive multiplication preserves this sign condition. $`\square`$

<!-- end proof-2 -->

Fix $`k\geq2`$, and suppress the superscript on $`a_n`$. Define
```math
P_k(z)=\prod_{j=1}^k(1-jz),\qquad
 G_k(X)=\prod_{j=1}^k(X-j).
```
The usual generating identity for Stirling numbers is

<a id="label-eq-gf"></a>

```math
\tag{6}
 H_k(z):=\sum_{n\geq1}a_nz^{n-1}=\frac1{P_k(z)}.
```

It follows directly, for example, by applying the Stirling recurrence to $`\sum_{t\geq0}S(k+t,k)z^t`$: this series is the corresponding series for $`k-1`$, divided by $`1-kz`$, and the initial series for $`k=1`$ is $`(1-z)^{-1}`$.

<a id="lemma-3"></a>

**Lemma 5.**

<a id="label-lem-companion"></a>

Set $`a_0=S(k-1,k)=0`$. There are an integer $`k\times k`$ matrix $`T`$, a vector $`v\in\mathbb Z^k`$, and an integer linear functional $`\lambda`$ such that
```math
G_k(T)=0,\qquad a_n=\lambda(T^n v)\quad(n\geq0).
```

<!-- end lemma-3 -->

<a id="proof-3"></a>

**Proof.**

Write $`G_k(X)=X^k+c_1X^{k-1}+\cdots+c_k`$. Multiplying [(6)](#label-eq-gf) by $`P_k(z)=1+c_1z+\cdots+c_kz^k`$ shows
```math
a_{n+k}+c_1a_{n+k-1}+\cdots+c_ka_n=0\qquad(n\geq0).
```
For $`n=0`$ this uses the coefficient of $`z^{k-1}`$, which is zero since $`k\geq2`$, and the fact that $`a_0=0`$. For $`n\geq1`$ it uses the coefficient of $`z^{n+k-1}`$. Take the companion transition matrix for the states $`(a_n,a_{n+1},\ldots,a_{n+k-1})^{\mathsf T}`$, take the initial state as $`v`$, and let $`\lambda`$ extract its first coordinate. The companion identity $`G_k(T)=0`$ gives the result. $`\square`$

<!-- end proof-3 -->

The integral initialization at zero is useful: the matrix powers represent $`a_n`$ itself, without a shift in the exponent.

## 3. The least-common-multiple upper bound

<a id="lemma-4"></a>

**Lemma 6.**

<a id="label-lem-lift"></a>

Let $`X,Y`$ be commuting integer matrices. If $`X\equiv Y\pmod {p^a}`$, where $`p`$ is prime and $`a\geq1`$, then
```math
X^{p^t}\equiv Y^{p^t}\pmod {p^{a+t}}\qquad(t\geq0).
```

<!-- end lemma-4 -->

<a id="proof-4"></a>

**Proof.**

Write $`X=Y+p^aC`$; then $`C`$ commutes with $`Y`$. In the binomial expansion of $`X^p-Y^p`$, the terms of degree $`i`$ in $`C`$, for $`1\leq i<p`$, are divisible by $`p^{ai+1}`$, hence by $`p^{a+1}`$. The last term is divisible by $`p^{ap}`$, and $`ap\geq a+1`$. Iteration proves the assertion, including $`p=2`$. $`\square`$

<!-- end proof-4 -->

<a id="lemma-5"></a>

**Lemma 7.**

<a id="label-lem-frob"></a>

Fix a prime $`p`$ and put
```math
m=\lceil k/p\rceil,\qquad h=\lceil\log_p m\rceil.
```
For the matrix $`T`$ of Lemma [5](#label-lem-companion),
```math
T^{p^{h+1}}\equiv T^{p^h}\pmod p.
```

<!-- end lemma-5 -->

<a id="proof-5"></a>

**Proof.**

Every residue class modulo $`p`$ occurs among $`1,\ldots,k`$ at most $`m`$ times. Over $`\mathbb F_p`$ this implies $`G_k(X)\mid(X^p-X)^m`$, so $`(T^p-T)^m=0`$ modulo $`p`$. Since $`p^h\geq m`$, raising $`T^p-T`$ to the power $`p^h`$ gives zero. The characteristic-$`p`$ binomial identity for commuting matrices gives $`T^{p^{h+1}}-T^{p^h}=0`$ modulo $`p`$. $`\square`$

<!-- end proof-5 -->

<a id="proof-6"></a>

**Proof of the upper bound in Theorem [1](#label-thm-main).**

The case $`k=1`$ is immediate. For $`k\geq2`$, fix a prime $`p`$ and use the notation of Lemma [7](#label-lem-frob). For $`r\geq h+1`$, Lemma [6](#label-lem-lift) gives
```math
T^{p^r}\equiv T^{p^{r-1}}\pmod {p^{r-h}}.
```
Taking arbitrary positive powers preserves the congruence. Applying $`\lambda(\,\cdot\,v)`$ therefore gives
```math
a_{tp^r}\equiv a_{tp^{r-1}}\pmod {p^{r-h}}
 \qquad(t\geq1,\ r\geq h+1).
```
Multiplication by $`p^h`$ supplies the required local modulus $`p^r`$. For $`1\leq r\leq h`$ the same conclusion is automatic after multiplication by $`p^h`$.

If $`p\geq k`$, then $`m=1`$ and $`h=0`$. If $`p<k`$, then

<a id="label-eq-h"></a>

```math
\tag{7}
 h=\lfloor\log_p(k-1)\rfloor.
```

Indeed, for the integer on the right, $`p^h<k\leq p^{h+1}`$, and hence $`p^{h-1}<\lceil k/p\rceil\leq p^h`$. The product of these local multipliers is
```math
\prod_{p<k}p^{\lfloor\log_p(k-1)\rfloor}=L_{k-1}.
```
Lemmas [3](#label-lem-local) and [4](#label-lem-sign) show that this is a realizability multiplier. The least multiplier divides every multiplier: it is the least common multiple of the denominators of the rational numbers $`D_n(a)/n`$ in lowest terms. Consequently $`F_k\mid L_{k-1}`$. $`\square`$

<!-- end proof-6 -->

## 4. Every prime below $`k`$ is necessary

<a id="proof-7"></a>

**Proof of the lower bound in Theorem [1](#label-thm-main).**

Let $`p<k`$, and suppose that $`p\nmid F_k`$. The local congruences for $`F_ka`$, reduced modulo $`p`$, imply

<a id="label-eq-cartier"></a>

```math
\tag{8}
 a_{pn}=a_n\quad\text{in }\mathbb F_p\qquad(n\geq1).
```

Here one writes $`n=tp^r`$ with $`p\nmid t`$ and applies the local congruence at level $`r+1`$, cancelling the nonzero scalar $`F_k`$ modulo $`p`$. Iteration gives $`a_{p^h n}=a_n`$ for every $`h\geq0`$.

Choose $`h`$ as in Lemma [7](#label-lem-frob) and set $`B=T^{p^h}`$ modulo $`p`$. Then $`B^p=B`$, whence $`B^{n+p-1}=B^n`$ for every $`n\geq1`$. The matrix representation and [(8)](#label-eq-cartier) imply
```math
a_{n+p-1}=a_n\quad\text{in }\mathbb F_p\qquad(n\geq1).
```
Thus the generating series $`H_k(z)`$ modulo $`p`$ has period $`p-1`$, and $`(1-z^{p-1})H_k(z)`$ is a polynomial. By [(6)](#label-eq-gf), this forces
```math
P_k(z)\mid1-z^{p-1}\quad\text{in }\mathbb F_p[z].
```
There is no numerator cancellation because the numerator in [(6)](#label-eq-gf) is the constant one. But $`k>p`$ means that the factors with $`j=1`$ and $`j=p+1`$ both occur, so $`(1-z)^2\mid P_k(z)`$ modulo $`p`$. The polynomial $`1-z^{p-1}`$ is squarefree: its derivative in characteristic $`p`$ is $`z^{p-2}`$, which has no common root with it. This is a contradiction, also when $`p=2`$. Hence $`p\mid F_k`$ for every $`p<k`$. $`\square`$

<!-- end proof-7 -->

## 5. Prime-power values and exact valuations

The next formula extends the first-level congruence $`S(p+k-1,k)\equiv\lceil k/p\rceil\pmod p`$ of Miska and Ward [\[3, Lemma 10\]](#ref-MW).

<a id="lemma-6"></a>

**Lemma 8.**

<a id="label-lem-digits"></a>

Let $`p`$ be prime, $`k\geq1`$, and $`r\geq0`$. Write
```math
k-1=\sum_{i\geq0}d_i p^i,\qquad 0\leq d_i<p.
```
Then

<a id="label-eq-digits"></a>

```math
\tag{9}
 S(p^r+k-1,k)\equiv\prod_{i=1}^r(d_i+1)\pmod p,
```

where the empty product is one.

<!-- end lemma-6 -->

<a id="proof-8"></a>

**Proof.**

Write $`k=qp+c`$, with $`0\leq c<p`$, and put $`R=(p^r-1)/(p-1)`$. Over $`\mathbb F_p`$ we have
```math
P_k(z)=(1-z^{p-1})^qP_c(z),\qquad P_0(z)=1.
```
If $`1\leq c<p`$, every coefficient of $`1/P_c(z)`$ at a nonnegative degree $`e`$ divisible by $`p-1`$ equals one modulo $`p`$. Indeed, the coefficient is $`S(e+c,c)`$, and inclusion–exclusion gives
```math
S(e+c,c)=\frac1{c!}\sum_{j=1}^c(-1)^{c-j}\binom cj j^{e+c}
 \equiv S(c,c)=1\pmod p.
```
Here $`c!`$ is invertible modulo $`p`$ and Fermat’s congruence applies to each $`j\in\{1,\ldots,c\}`$. Thus, when $`c>0`$ and $`q\geq1`$, the coefficient of $`z^{(p-1)R}`$ in $`1/P_k(z)`$ is
```math
\sum_{t=0}^R\binom{q+t-1}{t}=\binom{q+R}{R}\pmod p.
```
When $`c>0`$ and $`q=0`$, this coefficient is one, which agrees with the final binomial expression. If $`c=0`$, only the degree-zero coefficient of $`1/P_0(z)`$ contributes, and the answer is $`\binom{q+R-1}{R}`$. Putting $`J=\lceil k/p\rceil-1=\lfloor(k-1)/p\rfloor`$ combines both cases into

<a id="label-eq-binomial"></a>

```math
\tag{10}
 a_{p^r}^{(k)}\equiv\binom{J+R}{R}\pmod p.
```

The base-$`p`$ digits of $`J`$ are $`d_1,d_2,\ldots`$, and those of $`R`$ are one in positions $`0,\ldots,r-1`$ and zero thereafter. If all $`d_1,\ldots,d_r`$ are at most $`p-2`$, adding $`J`$ and $`R`$ produces no carry. Lucas’s coefficient formula therefore evaluates [(10)](#label-eq-binomial) as $`\prod_{i=1}^r(d_i+1)`$. If one of these digits is $`p-1`$, take the first such digit. There was no earlier carry, and the corresponding digit of $`J+R`$ is zero. Its Lucas factor is $`\binom01=0`$, and the proposed product is zero as well. For completeness, the coefficient formula used here follows by comparing coefficients in
```math
(1+x)^N=\prod_{i\geq0}(1+x^{p^i})^{N_i}\quad\text{in }\mathbb F_p[x],
```
where $`N_i`$ are the base-$`p`$ digits of $`N`$. $`\square`$

<!-- end proof-8 -->

<a id="corollary-1"></a>

**Corollary 9.**

<a id="label-cor-sharp-digits"></a>

Let $`p<k`$, put $`h=\lfloor\log_p(k-1)\rfloor`$, and use the digits in Lemma [8](#label-lem-digits). If $`1\leq r\leq h`$, $`d_r\ne0`$, and $`d_i\ne p-1`$ for every $`1\leq i<r`$, then $`v_p(F_k)\geq r`$. In particular, if $`d_i\ne p-1`$ for every $`1\leq i<h`$, then
```math
v_p(F_k)=h.
```

<!-- end corollary-1 -->

<a id="proof-9"></a>

**Proof.**

Subtracting successive formulas in [(9)](#label-eq-digits) gives
```math
a_{p^r}^{(k)}-a_{p^{r-1}}^{(k)}
 \equiv d_r\prod_{i=1}^{r-1}(d_i+1)\pmod p.
```
Under the stated conditions this is nonzero. The local Dold congruence at level $`r`$ forces $`p^r\mid F_k`$. At $`r=h`$, the highest digit $`d_h`$ is nonzero, and the upper bound in Theorem [1](#label-thm-main) gives equality. $`\square`$

<!-- end proof-9 -->

<a id="remark-1"></a>

**Remark 10.**

Lemma [8](#label-lem-digits) also supplies an explicit witness for full prime support. For $`p<k`$, let $`s\geq1`$ be the first position with $`d_s\ne0`$. Then $`a_{p^s}^{(k)}-a_{p^{s-1}}^{(k)}\not\equiv0\pmod p`$, with $`p^s<k`$. This proves the prime-support assertion by a second method and locates one necessary prime-power factor below $`k`$. It does not locate the maximum possible valuation of the repair factor.

<!-- end remark-1 -->

<a id="proof-10"></a>

**Proof of Theorem [1](#label-thm-main)(1) and (2).**

When $`p<k\leq p^2`$, we have $`h=1`$, so the digit restrictions in Corollary [9](#label-cor-sharp-digits) are empty and $`v_p(F_k)=1`$. When $`k=p^j+1`$, the digits of $`k-1=p^j`$ are zero below position $`j`$ and one at position $`j`$. The same corollary gives $`v_p(F_k)=j`$. In particular, for $`p=2`$ the corollary also gives $`v_2(F_k)=h`$ at both $`k=2^h+1`$ and $`k=2^h+2`$, for every $`h\geq1`$. $`\square`$

<!-- end proof-10 -->

## 6. Growth beyond the squarefree factor

<a id="proof-11"></a>

**Proof of Theorem [2](#label-thm-growth).**

Put $`K=k-1`$ and $`E_k=\log(F_k/\mathop{\mathrm{rad}}(K!))`$. By Theorem [1](#label-thm-main),
```math
\begin{align*}
 0\leq E_k
 &\leq\sum_{j=2}^{\lfloor\log_2 K\rfloor}\vartheta(K^{1/j})\\
 &=\vartheta(\sqrt K)+O\bigl(K^{1/3}(\log K)^2\bigr).
\end{align*}
```
For the error estimate, there are $`O(\log K)`$ terms with $`j\geq3`$, and each is at most $`K^{1/3}\log K`$, by the elementary inequality $`\vartheta(x)\leq x\log x`$.

For the lower bound, consider primes
```math
K^{1/3}<p\leq\sqrt K.
```
For each such prime, $`h=\lfloor\log_p K\rfloor=2`$. Corollary [9](#label-cor-sharp-digits) gives $`v_p(F_k)=2`$ unless the digit $`d_1`$ in $`K=d_2p^2+d_1p+d_0`$ is $`p-1`$. In that exceptional case, $`t=d_2+1`$ satisfies

<a id="label-eq-exception"></a>

```math
\tag{11}
 tp^2-p\leq K<tp^2,\qquad 2\leq t\leq K^{1/3}+1.
```

For a fixed $`t\geq2`$, at most one positive integer $`p`$ can satisfy [(11)](#label-eq-exception). Indeed, the lower endpoint for $`p+1`$ exceeds the upper endpoint for $`p`$, since
```math
t(p+1)^2-(p+1)-tp^2=2tp+t-p-1>0.
```
The intervals increase with $`p`$, so they are pairwise disjoint. Consequently, at most $`\lfloor K^{1/3}\rfloor+1`$ primes in the specified range are exceptional.

Every nonexceptional prime contributes at least $`\log p`$ to $`E_k`$. It follows that
```math
\begin{align*}
 E_k&\geq\vartheta(\sqrt K)-\vartheta(K^{1/3})
       -(\lfloor K^{1/3}\rfloor+1)\log\sqrt K\\
    &=\vartheta(\sqrt K)-O(K^{1/3}\log K).
\end{align*}
```
This proves [(3)](#label-eq-theta-growth). The classical prime number theorem $`\vartheta(x)\sim x`$ [\[2\]](#ref-Hadamard), together with $`K^{1/3}(\log K)^2=o(\sqrt K)`$, proves [(4)](#label-eq-growth). In particular, $`F_k/\mathop{\mathrm{rad}}((k-1)!)\to\infty`$. $`\square`$

<!-- end proof-11 -->

## 7. Remaining questions

The exact value of $`F_k`$ for general $`k`$ is still not determined by these arguments. In particular, the finite-cutoff assertion discussed in [\[1, Section 4.5\]](#ref-BGW) would compute $`F_k`$ from the denominators of $`D_n(a^{(k)})/n`$ only for indices $`n`$ at most the largest prime power strictly below $`k`$. Our upper bound controls all prime-power valuations, but does not show that their maxima occur within that finite range.

The results above leave open parts (a)–(c) of Conjecture 4 in [\[3\]](#ref-MW). In particular, the assertion $`v_p(F_{p^j})=1`$ for $`j>1`$ requires a sharper upper bound than the one proved here. Distinguishing those special cancellations from the general Frobenius bound appears necessary for an exact formula.

## References

<a id="ref-BGW"></a>

**\[1\]** J. Byszewski, G. Graff, and T. Ward, *Dold sequences, periodic points, and dynamics*, Bull. London Math. Soc. **53** (2021), 1263–1298. [doi:10.1112/blms.12531](https://doi.org/10.1112/blms.12531).

<a id="ref-Hadamard"></a>

**\[2\]** J. Hadamard, *Sur la distribution des zéros de la fonction $`\zeta(s)`$ et ses conséquences arithmétiques*, Bull. Soc. Math. France **24** (1896), 199–220. [doi:10.24033/bsmf.545](https://doi.org/10.24033/bsmf.545).

<a id="ref-MW"></a>

**\[3\]** P. Miska and T. Ward, *Stirling numbers and periodic points*, Acta Arith. **201** (2021), 421–435. [doi:10.4064/aa210309-9-8](https://doi.org/10.4064/aa210309-9-8). Author preprint: [arXiv:2102.07561](https://arxiv.org/abs/2102.07561).
