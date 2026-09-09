# Finite parameter tests for partition congruences and the surviving classes of an elongated partition conjecture

Henry Zweiman

September 8, 2026

## Abstract

We prove the seven remaining congruence families in a conjecture of Guadalupe on elongated plane partitions, and determine exactly when its final pair of congruences holds. The two progressions conjectured to vanish modulo $`3125`$ vanish identically precisely for parameter classes $`c\equiv0,2\pmod5`$; they vanish modulo $`625`$ for every $`c`$. The obstruction at the initial coefficients was identified by Patel. We prove the converse and the other families using a finite parameter principle and explicit Radu certificates. The principle reduces a parameter family modulo $`p^s`$ to $`\lceil s/v\rceil`$ initial parameter values when its normalized parameter ratio is $`1`$ modulo $`p^v`$. We give the complete certificate data and exact arithmetic verifiers.

## 1. Introduction and results

For $`j\ge1`$, write $`f_j(q)=\prod_{n\ge1}(1-q^{jn})`$. The elongated plane partition functions considered by Andrews and Paule, and subsequently by several authors, have generating functions

<a id="label-eq-gf"></a>

```math
\tag{1}
D_k(q)=\sum_{n\ge0}d_k(n)q^n=\frac{f_2(q)^k}{f_1(q)^{3k+1}}
=\frac{H(q)^k}{f_1(q)},\qquad H(q)=\frac{f_2(q)}{f_1(q)^3}.
```

Guadalupe [\[1\]](#ref-Guadalupe) proved numerous congruences modulo small powers of $`5`$ and stated eight further families in Conjecture 7.1. A generic transfer theorem quoted there changes $`k`$ by a substantially larger power of $`5`$ than the step $`125`$ appearing in the conjecture. Controlling this smaller parameter step is therefore essential.

The last family of that conjecture is false. Patel’s posted counterexample [\[2\]](#ref-Patel) proves

<a id="label-eq-obstructions"></a>

```math
\tag{2}
\begin{split}
d_{125c+58}(66)&\equiv625c(c-2)\pmod{3125},\\
d_{125c+58}(116)&\equiv-625c(c-2)\pmod{3125}.
\end{split}
```

These formulas rule out three parameter classes. Our main result proves that the two remaining classes work for every coefficient, and establishes the other seven families. We include an independently checked proof of [(2)](#label-eq-obstructions) for completeness; we make no priority claim for that obstruction.

<a id="theorem-1"></a>

**Theorem 1.**

<a id="label-thm-main"></a>

For every $`c,n\ge0`$, the congruences in Table [1](#label-tab-results) hold. A list of residues means that the assertion holds separately at each listed residue.

<a id="label-tab-results"></a>

**Table 1.** Uniform congruences.

| Parameter $`k`$ | Argument of $`d_k`$   | Dividing modulus |
|:----------------|:----------------------|:-----------------|
| $`125c+58`$     | $`25n+16`$            | $`125`$          |
| $`125c+83`$     | $`125n+41,91`$        | $`125`$          |
| $`125c+100`$    | $`125n+124`$          | $`125`$          |
| $`125c+5`$      | $`125n+69,119`$       | $`125`$          |
| $`125c+30`$     | $`125n+69`$           | $`125`$          |
| $`125c+60`$     | $`125n+14,64,89,114`$ | $`125`$          |
| $`125c+58`$     | $`125n+91`$           | $`625`$          |
| $`125c+58`$     | $`125n+66,116`$       | $`625`$          |

Moreover, for a fixed $`c\ge0`$, each of the following assertions is equivalent to $`c\equiv0`$ or $`2\pmod5`$:

<a id="label-eq-66"></a>

<a id="label-eq-116"></a>

```math
\begin{align}
 d_{125c+58}(125n+66)&\equiv0\pmod{3125}\quad\text{for every }n\ge0,\tag{3}\\
 d_{125c+58}(125n+116)&\equiv0\pmod{3125}\quad\text{for every }n\ge0.\tag{4}
\end{align}
```

<!-- end theorem-1 -->

The result uses a standard modular finite coefficient criterion, with explicitly bounded exact computations. It does not use numerical evidence as a substitute for an infinite argument. All infinite parameter dependence is handled by the following elementary principle.

## 2. A finite parameter principle

For $`m\ge1`$ and $`0\le r<m`$, let $`\mathcal I_{m,r}(p^s)`$ denote the additive subgroup of $`\mathbb Z[[q]]`$ consisting of series whose coefficients in degrees congruent to $`r`$ modulo $`m`$ are divisible by $`p^s`$. Multiplication by any series in $`\mathbb Z[[q^m]]`$ preserves this subgroup.

<a id="lemma-1"></a>

**Lemma 2.**

<a id="label-lem-parameter"></a>

Let $`p`$ be prime, let $`s,v\ge1`$, and let $`F,A\in\mathbb Z[[q]]`$. Suppose that $`B\in1+q^m\mathbb Z[[q^m]]`$ and
```math
A/B\in1+p^v\mathbb Z[[q]].
```
Put $`L=\lceil s/v\rceil`$. If $`FA^j\in\mathcal I_{m,r}(p^s)`$ for $`0\le j<L`$, then $`FA^c\in\mathcal I_{m,r}(p^s)`$ for every $`c\ge0`$.

<!-- end lemma-1 -->

<a id="proof-1"></a>

**Proof.**

The inverse $`B^{-1}`$ also belongs to $`\mathbb Z[[q^m]]`$. Thus the hypotheses imply $`F(A/B)^j\in\mathcal I_{m,r}(p^s)`$ for $`j<L`$. The integer binomial identity gives
```math
F(A/B-1)^j=\sum_{i=0}^j(-1)^{j-i}\binom ji F(A/B)^i\in\mathcal I_{m,r}(p^s)
```
for $`j<L`$. For $`j\ge L`$, the entire left side is divisible by $`p^s`$. Expanding $`F(A/B)^c`$ in powers of $`A/B-1`$ proves that it belongs to the subgroup. Multiplication by $`B^c`$ completes the proof. $`\square`$

<!-- end proof-1 -->

For any integer unit series $`H`$, reduction modulo $`p`$ gives $`H(q)^{p^a}=H(q^{p^a})`$. This identity holds for infinite formal series because each coefficient depends on only finitely many factors and terms.

<a id="corollary-1"></a>

**Corollary 3.**

<a id="label-cor-transfer"></a>

Fix $`a\ge0`$. For $`m\in\{25,125\}`$, to prove
```math
d_{a+125c}(mn+r)\equiv0\pmod{5^s}\qquad(c,n\ge0),
```
it is enough to prove the assertion for every $`n\ge0`$ at $`c=0,\ldots,s-1`$. For $`m=125`$, to prove
```math
d_{a+625c}(125n+r)\equiv0\pmod{3125}\qquad(c,n\ge0),
```
it is enough to prove the assertion for every $`n\ge0`$ at $`c=0,1,2`$.

<!-- end corollary-1 -->

<a id="proof-2"></a>

**Proof.**

In the first case use $`F=D_a`$, $`A=H^{125}`$ and $`B=H(q^{125})`$ in Lemma [2](#label-lem-parameter), with $`p=5,v=1`$. In the second case use $`A=H^{625}`$ and $`B=H(q^{125})^5`$. If $`H^{125}/H(q^{125})=1+5C`$, then $`A/B=(1+5C)^5\equiv1\pmod{25}`$. Hence $`v=2`$ and $`L=3`$. $`\square`$

<!-- end proof-2 -->

## 3. A modular certificate with explicit cusp bounds

We recall the finite criterion of Radu in the formulation of Wang [\[3, Definition 4.1 and Lemmas 4.2–4.3\]](#ref-Wang); see also Tang [\[4, Lemma 7\]](#ref-Tang). For an exponent vector $`\rho=(\rho_\delta)_{\delta\mid M}`$, define $`c_\rho(n)`$ by
```math
\prod_{\delta\mid M}f_\delta(q)^{\rho_\delta}=\sum_{n\ge0}c_\rho(n)q^n.
```
Write $`\kappa=\gcd(m^2-1,24)`$ and $`\sigma(\rho)=\sum_{\delta\mid M}\delta\rho_\delta`$. The orbit $`P_{m,\rho}(t)`$ consists of the least nonnegative residues

<a id="label-eq-orbit"></a>

```math
\tag{5}
 ts+\frac{s-1}{24}\sigma(\rho)\pmod m,
 \qquad s\in(\mathbb Z/24m\mathbb Z)^{\times2}.
```

Unit squares modulo $`24m`$ are $`1`$ modulo $`24`$, so this is integral.

The admissibility conditions for $`(m,M,N,t,\rho)`$ are the following: every prime divisor of $`m`$ divides $`N`$; every $`\delta>1`$ with $`\rho_\delta\ne0`$ divides $`mN`$; and
```math
\begin{align*}
 \kappa N\sum_{\delta\mid M}\rho_\delta\frac{mN}{\delta}&\equiv0\pmod{24},\\
 \kappa N\sum_{\delta\mid M}\rho_\delta&\equiv0\pmod8,\\
 \frac{24m}{\gcd(\kappa(-24t-\sigma(\rho)),24m)}&\mid N.
\end{align*}
```
There is an additional condition for even $`m`$, irrelevant here. We use only odd $`m`$.

For $`\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)`$ and an integer vector $`\alpha=(\alpha_\delta)_{\delta\mid N}`$, put
```math
\begin{align*}
 p_{m,\rho}(\gamma)&=\min_{0\le\lambda<m}\frac1{24}
 \sum_{\delta\mid M}\rho_\delta\frac{\gcd(\delta(a+\kappa\lambda c),mc)^2}{\delta m},\\
 p^*_{\alpha}(\gamma)&=\frac1{24}\sum_{\delta\mid N}\alpha_\delta\frac{\gcd(\delta,c)^2}{\delta}.
\end{align*}
```
If the tuple is admissible and $`p_{m,\rho}(\gamma)+p^*_{\alpha}(\gamma)\ge0`$ for a complete set of cusp representatives, the criterion states that the congruences
```math
c_\rho(mn+t')\equiv0\pmod u\qquad(t'\in P_{m,\rho}(t))
```
hold for every $`n\ge0`$ provided they hold for $`0\le n\le\lfloor\nu\rfloor`$, where

<a id="label-eq-nu"></a>

```math
\tag{6}
 \nu=\frac{(\sum\rho_\delta+\sum\alpha_\delta)[\mathrm{SL}_2(\mathbb Z):\Gamma_0(N)]
 -\sum\delta\alpha_\delta}{24}
 -\frac{\sigma(\rho)}{24m}-\frac{\min P_{m,\rho}(t)}m.
```

Here $`u`$ is any positive integer. In particular this criterion applies directly to $`125,625,3125`$.

<a id="proposition-1"></a>

**Proposition 4.**

<a id="label-prop-certificate"></a>

Let $`k\ge1`$, $`m\in\{25,125\}`$, $`s\ge1`$, $`u=5^s`$, and $`0\le t<m`$. Suppose $`25\mid24t-k-1`$. Set

<a id="label-eq-params"></a>

```math
\tag{7}
 J=\left\lceil\frac{3k+1}{u}\right\rceil,
 \quad\rho=(uJ-3k-1,k,-uJ/5,0),
 \quad A=\left\lceil\frac{m(5k+2)}{50}\right\rceil,
```

where the coordinates are indexed by $`1,2,5,10`$. Define $`P=P_{m,\rho}(t)`$ and

<a id="label-eq-bound"></a>

```math
\tag{8}
 \nu=\frac{18(4uJ/5-2k-1+A)-A}{24}
       +\frac{k+1}{24m}-\frac{\min P}{m}.
```

If $`d_k(mn+t')\equiv0\pmod u`$ for every $`t'\in P`$ and $`0\le n\le\lfloor\nu\rfloor`$, then these congruences hold for all $`n\ge0`$.

<!-- end proposition-1 -->

<a id="proof-3"></a>

**Proof.**

The binomial congruence $`f_1^{5^s}\equiv f_5^{5^{s-1}}\pmod{5^s}`$ shows that $`c_\rho(n)\equiv d_k(n)\pmod u`$. It follows, for example, by induction from $`(1-X)^5\equiv1-X^5\pmod5`$, then multiplication of formal series. Inverting a unit series preserves a coefficientwise congruence.

Take $`M=N=10`$. The index is $`18`$ and $`\kappa=24`$. Also $`\sigma(\rho)=-k-1`$. The first four admissibility conditions are immediate. The last follows because $`m/\gcd(24t-k-1,m)`$ is either $`1`$ or $`5`$ and hence divides $`10`$.

Since $`10`$ is squarefree, the four matrices $`\gamma_c=\left(\begin{smallmatrix}1&0\\c&1\end{smallmatrix}\right)`$, $`c=1,2,5,10`$, represent the cusps. Directly from the definition,

<a id="label-eq-cusps"></a>

```math
\tag{9}
 24p_{m,\rho}(\gamma_c)=
 \begin{cases}
 -m(5k+2)/50,&c=1,\\
 -m(k+1)/25,&c=2,\\
 -(5k+2)/(2m),&c=5,\\
 -(k+1)/m,&c=10.
 \end{cases}
```

We justify these equalities to make the cusp bounds explicit. For $`c=1`$, put $`g=\gcd(1+24\lambda,m)`$. If $`g<m`$, the scaled sum is $`-g^2(5k+2)/(2m)`$, minimized at $`g=m/5`$. If $`g=m`$, it is
```math
m\bigl((24/25)uJ-(5k+2)/2\bigr)>0,
```
since $`uJ\ge3k+1`$ and $`k\ge1`$. At $`c=2`$, the integer $`1+48\lambda`$ is odd; the corresponding expressions are $`-g^2(k+1)/m`$ for $`g<m`$ and a positive expression for $`g=m`$. Both extremizing gcd values occur. At $`c=5,10`$, the integer $`1+24\lambda c`$ is coprime to $`5`$, giving the last two values in [(9)](#label-eq-cusps).

The most negative entry is the first. Thus $`\alpha=(A,0,0,0)`$ has $`p^*_{\alpha}=A/24`$ and satisfies every cusp inequality. Substitution into [(6)](#label-eq-nu) gives [(8)](#label-eq-bound), proving the proposition. $`\square`$

<!-- end proof-3 -->

## 4. Base cases and sufficiency

Table [2](#label-tab-certs) gives every base case used. In each row, $`u=5^s`$, $`J,A,\rho`$ are given by [(7)](#label-eq-params), and the final column is $`\lfloor\nu\rfloor`$. Formula [(5)](#label-eq-orbit) gives exactly the displayed set $`P`$. All rows satisfy $`25\mid24t-k-1`$ for $`t=\min P`$.

The supplied exact arithmetic verification checks all $`182\,706`$ coefficients required by the table. The largest index is $`1\,901\,366`$. Every tested residue is zero modulo the stated modulus. Proposition [4](#label-prop-certificate) therefore proves each base congruence for all $`n\ge0`$.

<a id="label-tab-certs"></a>

**Table 2.** Complete base certificates.

| $`k`$ | $`m`$ | $`s`$ | $`\lfloor\nu\rfloor`$ | $`P`$          |
|------:|------:|------:|----------------------:|:---------------|
|    58 |    25 |     3 |                   165 | $`\{16\}`$     |
|   183 |    25 |     3 |                   424 | $`\{16\}`$     |
|   308 |    25 |     3 |                   683 | $`\{16\}`$     |
|    83 |   125 |     3 |                   763 | $`\{41,91\}`$  |
|   208 |   125 |     3 |                  1907 | $`\{41,91\}`$  |
|   333 |   125 |     3 |                  3051 | $`\{41,91\}`$  |
|   100 |   125 |     3 |                   962 | $`\{124\}`$    |
|   225 |   125 |     3 |                  2106 | $`\{124\}`$    |
|   350 |   125 |     3 |                  3250 | $`\{124\}`$    |
|     5 |   125 |     3 |                   114 | $`\{69,119\}`$ |
|   130 |   125 |     3 |                  1258 | $`\{69,119\}`$ |
|   255 |   125 |     3 |                  2402 | $`\{69,119\}`$ |
|    30 |   125 |     3 |                   297 | $`\{69\}`$     |
|   155 |   125 |     3 |                  1442 | $`\{69\}`$     |
|   280 |   125 |     3 |                  2586 | $`\{69\}`$     |
|    60 |   125 |     3 |                   593 | $`\{14,64\}`$  |
|    60 |   125 |     3 |                   593 | $`\{89,114\}`$ |
|   185 |   125 |     3 |                  1738 | $`\{14,64\}`$  |
|   185 |   125 |     3 |                  1738 | $`\{89,114\}`$ |
|   310 |   125 |     3 |                  2882 | $`\{14,64\}`$  |
|   310 |   125 |     3 |                  2881 | $`\{89,114\}`$ |
|    58 |   125 |     4 |                   803 | $`\{91\}`$     |
|    58 |   125 |     4 |                   803 | $`\{66,116\}`$ |
|   183 |   125 |     4 |                  1723 | $`\{91\}`$     |
|   183 |   125 |     4 |                  1723 | $`\{66,116\}`$ |
|   308 |   125 |     4 |                  3017 | $`\{91\}`$     |
|   308 |   125 |     4 |                  3017 | $`\{66,116\}`$ |
|   433 |   125 |     4 |                  4311 | $`\{91\}`$     |
|   433 |   125 |     4 |                  4312 | $`\{66,116\}`$ |
|    58 |   125 |     5 |                  2303 | $`\{66,116\}`$ |
|   683 |   125 |     5 |                  6900 | $`\{66,116\}`$ |
|  1308 |   125 |     5 |                 13371 | $`\{66,116\}`$ |
|   308 |   125 |     5 |                  4142 | $`\{66,116\}`$ |
|   933 |   125 |     5 |                  8739 | $`\{66,116\}`$ |
|  1558 |   125 |     5 |                 15210 | $`\{66,116\}`$ |

For the first six rows of Table [1](#label-tab-results), the certificate table supplies $`k=a,a+125,a+250`$. Corollary [3](#label-cor-transfer) proves the desired congruences for every $`c\ge0`$. For the two rows modulo $`625`$, it supplies $`k=58,183,308,433`$, so the same corollary again applies.

For the stronger congruences, the table supplies
```math
k=58,683,1308\quad\text{and}\quad k=308,933,1558.
```
The second part of Corollary [3](#label-cor-transfer) yields both progressions modulo $`3125`$ for $`k=58+625c`$ and $`k=308+625c`$. These are exactly the parameter classes $`c\equiv0,2\pmod5`$ in Theorem [1](#label-thm-main). This proves sufficiency.

## 5. The obstruction and necessity

We record Patel’s initial-coefficient argument [\[2\]](#ref-Patel), with an independent integer verification. Put $`V=H(q)^{125}/H(q^{125})`$. Then $`V\equiv1\pmod5`$. Below degree $`125`$, the factor $`H(q^{125})^c`$ is $`1`$. Consequently each of
```math
a(c)=d_{125c+58}(66),\qquad b(c)=d_{125c+58}(116)
```
is, modulo $`3125`$, an integer linear combination of $`\binom cj`$ for $`0\le j\le4`$. Indeed, expand $`D_{58}V^c`$ and discard $`(V-1)^j`$ for $`j\ge5`$.

The five exact initial evaluations are
```math
\begin{array}{c|rrrrr}
c&0&1&2&3&4\\\hline
a(c)\bmod3125&0&2500&0&1875&1875\\
b(c)\bmod3125&0&625&0&1250&1250.
\end{array}
```
The evaluation matrix $`\bigl(\binom ij\bigr)_{0\le i,j\le4}`$ is unit lower triangular over $`\mathbb Z/3125\mathbb Z`$. These values therefore establish [(2)](#label-eq-obstructions) for every $`c\ge0`$, since $`c(c-2)=2\binom c2-\binom c1`$. No division by a nonunit is involved.

For reproducibility, the evaluations can be made using only integers:

<a id="label-eq-recurrence"></a>

```math
\tag{10}
 n d_k(n)=\sum_{j=1}^n\left((3k+1)\sigma_1(j)
 -2k\mathbf1_{2\mid j}\sigma_1(j/2)\right)d_k(n-j),
 \qquad d_k(0)=1.
```

This follows by formal logarithmic differentiation of [(1)](#label-eq-gf). The supplied independent verifier uses exact division in $`\mathbb Z`$ and checks its divisibility at every step. Either of [(3)](#label-eq-66) and [(4)](#label-eq-116), at $`n=0`$, forces $`c(c-2)\equiv0\pmod5`$. Together with the sufficiency already proved, this completes Theorem [1](#label-thm-main).

## 6. Verification and reproducibility

The supplementary files contain one authoritative manifest of the $`35`$ base cases, the complete rational certificates, and two coefficient algorithms. The certificate generator computes every orbit and cusp minimum with integers and rational numbers, and also checks the closed formulas [(9)](#label-eq-cusps). Its record includes $`k,m,s,\rho,A,P,\nu`$, the largest coefficient index and the number of zero checks.

The main verifier forms Euler’s pentagonal series in $`(\mathbb Z/5^s\mathbb Z)[q]/(q^L)`$, inverts its constant coefficient $`1`$, and computes $`f_1^{-1}(f_2f_1^{-3})^k`$ in that ring. Truncated multiplication, inversion and exponentiation give precisely the first $`L`$ coefficients of the infinite formal series. The implementation uses Python with python-flint 0.9.0; its mathematical arithmetic is exact. The separate integer verifier evaluates [(10)](#label-eq-recurrence) through degree $`116`$.

The mathematical dependence on computation is limited and explicit: the finite modular zero checks in Table [2](#label-tab-certs) and the five initial evaluations. The finite criterion, its cusp hypotheses, the parameter extension, and the necessity argument are proved or cited above. The supplementary code and machine-readable records are part of the manuscript’s reproducibility package.

## References

<a id="ref-Guadalupe"></a>

**\[1\]** R. Guadalupe, *The $`k`$-elongated plane partition function modulo small powers of $`5`$*, arXiv:2504.08627v2 (2025), [arXiv record](https://arxiv.org/abs/2504.08627).

<a id="ref-Patel"></a>

**\[2\]** S. Patel, *Counterexample*, solution posted to “Conjectural congruences for the $`k`$-elongated plane partition function modulo powers of $`5`$,” MathDB, accessed September 8, 2026, [online solution](https://mathdb.com/p/382381/conjectural-congruences-for-the-k-elongated-plane-partition).

<a id="ref-Wang"></a>

**\[3\]** L. Wang, *Arithmetic properties of $`(k,\ell)`$-regular bipartitions*, Bull. Aust. Math. Soc. **95** (2017), 353–364, [doi:10.1017/S0004972716000964](https://doi.org/10.1017/S0004972716000964).

<a id="ref-Tang"></a>

**\[4\]** D. Tang, *New congruences for broken $`k`$-diamond partitions*, J. Integer Seq. **21** (2018), Article 18.5.8, [publisher PDF](https://cs.uwaterloo.ca/journals/JIS/VOL21/Tang/tang13.pdf).

<a id="ref-Radu"></a>

**\[5\]** S. Radu, *An algorithmic approach to Ramanujan’s congruences*, Ramanujan J. **20** (2009), 215–251.
