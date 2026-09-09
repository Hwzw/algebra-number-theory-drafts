# A complete classification of a primitive cubic family

Henry Zweiman

September 9, 2026

## Abstract

We prove that a primitive polynomial $`X^3+X^2+X+\lambda`$ over $`\mathbb F_{q^2}`$, with $`\lambda`$ primitive in $`\mathbb F_{q^2}`$, exists if and only if the characteristic is not three. This determines all surviving cases of a conjecture of Awasthi and Sharma, whose case $`q=3`$ was recently disproved. A Kummer parametrization retains the coefficient conditions exactly and gives uniform character-sum estimates, with different main terms in odd and even characteristic. A sieve proves existence for every $`q\ge1511`$, and independently verified finite-field certificates cover the remaining 261 prime powers. The proof uses the incomplete-character-sum theorem of Fu and Wan and includes an explicit accounting of its geometric hypotheses.

## 1. Introduction and statement

A monic polynomial of degree $`m`$ over $`\mathbb F_Q`$ is primitive if its roots generate the multiplicative group $`\mathbb F_{Q^m}^*`$. Awasthi and Sharma [\[1, Conjecture 9.1\]](#ref-AS) asked whether there always exists a primitive polynomial

<a id="label-eq-family"></a>

```math
\tag{1}
 h_\lambda(X)=X^3+X^2+X+\lambda\in\mathbb F_{q^2}[X]
```

with $`\lambda`$ primitive in $`\mathbb F_{q^2}`$. Their surrounding discussion takes $`q`$ prime. Sharma [\[3, Section 4\]](#ref-S) disproved the case $`q=3`$ and considered the broader prime-power setting. We give the complete classification in that setting.

<a id="theorem-1"></a>

**Theorem 1.1.**

<a id="label-thm-main"></a>

Let $`q`$ be any prime power. There exists a primitive element $`\lambda\in\mathbb F_{q^2}`$ for which [(1)](#label-eq-family) is primitive if and only if $`\operatorname{char}(\mathbb F_q)\ne3`$.

<!-- end theorem-1 -->

The positive direction is partly computer assisted: a uniform argument reduces it to a specified finite interval, and 261 explicit certificates cover that entire interval. The files `witnesses.json` and `check.py` provide the certificates and a verifier using only exact integer and polynomial arithmetic. The proof does not infer the infinite conclusion from a sample.

We also obtain a counting result. Write $`P(q)`$ for the number of constants in Theorem [1.1](#label-thm-main), and put
```math
Q=q^2,\qquad N=Q^3-1=q^6-1,\qquad
 \theta(e)=\frac{\varphi(e)}e,\qquad W(e)=2^{\omega(e)},
```
where $`\omega(e)`$ is the number of distinct prime divisors of $`e`$.

<a id="theorem-2"></a>

**Theorem 1.2.**

<a id="label-thm-count"></a>

If $`q`$ has odd characteristic different from three, then
```math
\left|\frac{3P(q)}{\theta(N)}-(q^2-1)\right|
 \le 6q\bigl(W(N)-1\bigr).
```
If $`q`$ is even, then
```math
\left|\frac{3P(q)}{\theta(N)}-2q^2\right|
 \le 4q\bigl(W(N)-1\bigr).
```
In characteristic three, $`P(q)=0`$.

<!-- end theorem-2 -->

Thus the even-characteristic family has twice the leading density. Since $`W(n)=n^{o(1)}`$, both estimates have a relative error tending to zero as $`q`$ tends to infinity in the respective regime.

The character estimates come from Fu and Wan [\[2, Proposition 2.1 and Theorem 4.2\]](#ref-FW). The Kummer parametrization below enforces both prescribed coefficients before applying those estimates. This is essential: multiplicative freeness in an extension field does not enforce membership in a smaller field. We discuss the distinction from the sufficient condition in [\[3\]](#ref-S) at the end.

## 2. The obstruction and a parametrization

<a id="lemma-1"></a>

**Lemma 2.1.**

<a id="label-lem-obstruction"></a>

In characteristic three, no polynomial [(1)](#label-eq-family) can be both irreducible and have primitive constant term.

<!-- end lemma-1 -->

<a id="proof-1"></a>

**Proof.**

The discriminant of $`X^3+X^2+X+\lambda`$ in characteristic three is $`-\lambda`$. An irreducible cubic over an odd finite field has nonzero square discriminant: Frobenius permutes its roots as a three-cycle and therefore fixes their Vandermonde product. Since $`Q=q^2`$ is an odd square, $`-1`$ is a square in $`\mathbb F_Q`$. Consequently $`\lambda`$ must be a square. A generator of the even-order cyclic group $`\mathbb F_Q^*`$ is not a square. $`\square`$

<!-- end proof-1 -->

From now on the characteristic $`p`$ differs from three. Then $`Q\equiv1\pmod3`$. Choose a noncube $`a\in\mathbb F_Q^*`$ and a root $`\alpha`$ of $`X^3-a`$. This cubic is irreducible, since a reducible cubic has a root. Hence
```math
K=\mathbb F_Q(\alpha)=\mathbb F_{Q^3}.
```
The element $`\zeta=\alpha^{Q-1}`$ is a primitive cube root of unity in $`\mathbb F_Q`$, and the three conjugates of $`\alpha`$ are $`\alpha,\zeta\alpha,\zeta^2\alpha`$.

For $`\beta\in K`$, define its subtrace by
```math
\operatorname{St}(\beta)=\beta^{1+Q}+\beta^{1+Q^2}+\beta^{Q+Q^2}.
```
Every $`\beta\in K`$ has a unique expression $`c+u\alpha+v\alpha^2`$ with $`c,u,v\in\mathbb F_Q`$. Direct expansion of the three conjugates gives

<a id="label-eq-trace"></a>

```math
\tag{2}
 \operatorname{Tr}_{K/\mathbb F_Q}(\beta)=3c,\qquad
 \operatorname{St}(\beta)=3c^2-3auv.
```

<a id="lemma-2"></a>

**Lemma 2.2.**

<a id="label-lem-param"></a>

If $`p\ge5`$, the elements of $`K`$ having trace $`-1`$ and subtrace $`1`$ are exactly

<a id="label-eq-oddparam"></a>

```math
\tag{3}
 b(t)=-\frac13+\alpha t-\frac{2\alpha^2}{9at},\qquad t\in\mathbb F_Q^*,
```

each occurring once. If $`p=2`$, they form the union of the two lines

<a id="label-eq-evenparam"></a>

```math
\tag{4}
 b_1(t)=1+\alpha t,\qquad b_2(t)=1+\alpha^2t,
 \qquad t\in\mathbb F_Q,
```

whose only common element is $`1`$.

<!-- end lemma-2 -->

<a id="proof-2"></a>

**Proof.**

For $`p\ge5`$, equations [(2)](#label-eq-trace) give $`c=-1/3`$ and $`uv=-2/(9a)\ne0`$. Take $`u=t`$ and solve for $`v`$. In characteristic two they give $`c=1`$ and $`uv=0`$. Uniqueness of the basis expansion proves both the parametrizations and the intersection assertion. $`\square`$

<!-- end proof-2 -->

A primitive $`\beta\in K`$ has degree three over $`\mathbb F_Q`$. Its minimal polynomial is
```math
X^3-\operatorname{Tr}(\beta)X^2+\operatorname{St}(\beta)X-\operatorname{N}_{K/\mathbb F_Q}(\beta).
```
Moreover, the norm of a generator of $`K^*`$ generates $`\mathbb F_Q^*`$. Negation preserves generators of $`\mathbb F_Q^*`$ when $`Q`$ is even or $`Q\equiv1\pmod4`$. In the latter case, if $`z`$ generates the group and $`\gcd(j,Q-1)=1`$, then $`j+(Q-1)/2`$ remains coprime to $`Q-1`$: it remains odd and is unchanged modulo every odd prime divisor. Since $`Q=q^2`$, one of these two cases always applies.

It follows that every primitive element in Lemma [2.2](#label-lem-param) gives a polynomial counted by $`P(q)`$, and every such polynomial has exactly three counted roots. In characteristic two we may count the two lines with multiplicity at $`1`$, since $`1`$ is not primitive in $`K`$.

## 3. Incomplete character sums

We record the precise specialization of the external character-sum theorem that we use. Let $`f\in K(t)^*`$, and let $`U`$ be an open subset of $`\mathbb P^1_{\mathbb F_Q}`$ obtained by removing the zeros and poles of all three coefficient conjugates of $`f`$. For a nontrivial multiplicative character $`\chi`$ of $`K^*`$, the Kummer sheaf of $`(\chi,f)`$ has rank one, weight zero, and only tame ramification. Fu–Wan tensor induction produces a rank-one sheaf on $`U`$ whose trace at $`t\in U(\mathbb F_Q)`$ is $`\chi(f(t))`$. After base change, its three Kummer factors have character weights $`1,Q,Q^2`$ on the coefficient conjugates; see [\[2, Proposition 2.1\]](#ref-FW).

If some zero belongs to exactly one conjugate and is simple, its inertia exponent in this tensor product is one of $`1,Q,Q^2`$. These integers are coprime to the order of $`\chi`$, which divides $`Q^3-1`$. The induced sheaf is therefore geometrically nonconstant. If the removed set has $`s`$ geometric points, [\[2, Theorem 4.2\]](#ref-FW), with genus zero and zero Swan conductors, gives

<a id="label-eq-fw"></a>

```math
\tag{5}
 \left|\sum_{t\in U(\mathbb F_Q)}\chi(f(t))\right|\le(s-2)\sqrt Q.
```

The puncture count in [(5)](#label-eq-fw) is the actual union of the three supports. This is sharper here than counting their degrees separately. These observations check the geometric nonconstancy hypothesis; the mere nontriviality of $`\chi`$ would not suffice.

<a id="lemma-3"></a>

**Lemma 3.1.**

<a id="label-lem-chars"></a>

For every nontrivial multiplicative character $`\chi`$ of $`K^*`$, we have
```math
\left|\sum_{t\in\mathbb F_Q^*}\chi(b(t))\right|\le6\sqrt Q\quad(p\ge5),
```
and
```math
\left|\sum_{t\in\mathbb F_Q}\chi(b_i(t))\right|\le2\sqrt Q
 \quad(p=2,\ i=1,2).
```

<!-- end lemma-3 -->

<a id="proof-3"></a>

**Proof.**

The two zeros of [(3)](#label-eq-oddparam) are
```math
\frac{2}{3\alpha},\qquad -\frac{1}{3\alpha}.
```
Each has a Frobenius orbit of size three. The orbits could meet only if $`-2`$ were a cube root of unity. That would imply $`-8=1`$, impossible for $`p\ge5`$. Thus the three conjugate functions have six disjoint simple zeros. Their poles are $`0`$ and $`\infty`$, both simple, and there are eight punctures in total. No zero lies in $`\mathbb F_Q`$, so $`U(\mathbb F_Q)=\mathbb F_Q^*`$. Apply [(5)](#label-eq-fw).

For either line in [(4)](#label-eq-evenparam), its zero and the two coefficient-conjugate zeros are distinct and lie outside $`\mathbb F_Q`$. The pole is $`\infty`$. Hence there are four punctures and $`U(\mathbb F_Q)=\mathbb F_Q`$. The same nonconstancy check and [(5)](#label-eq-fw) prove the second bound. $`\square`$

<!-- end proof-3 -->

For a divisor $`e\mid N`$, call $`x\in K^*`$ *$`e`$-free* if it is not an $`\ell`$-th power for any prime $`\ell\mid e`$. Let $`A(e)`$ count $`e`$-free values in the parameter multiset of Lemma [2.2](#label-lem-param), counting the common point of the two lines twice in characteristic two. Every value is nonzero. The standard indicator is

<a id="label-eq-indicator"></a>

```math
\tag{6}
 \rho_e(x)=\theta(e)\sum_{d\mid e}\frac{\mu(d)}{\varphi(d)}
               \sum_{\operatorname{ord}(\chi)=d}\chi(x).
```

This follows by multiplying the prime-divisor indicators in the cyclic group $`K^*`$.

Set

<a id="label-eq-CB"></a>

```math
\tag{7}
 (C,B)=
 \begin{cases}
 (Q-1,6\sqrt Q),&p\ge5,\\
 (2Q,4\sqrt Q),&p=2.
 \end{cases}
```

The trivial character contributes $`C`$. Lemma [3.1](#label-lem-chars) and [(6)](#label-eq-indicator) imply

<a id="label-eq-freebound"></a>

```math
\tag{8}
 \left|\frac{A(e)}{\theta(e)}-C\right|\le\bigl(W(e)-1\bigr)B.
```

Since $`A(N)=3P(q)`$, this proves Theorem [1.2](#label-thm-count), including the obstruction from Lemma [2.1](#label-lem-obstruction).

## 4. A sieve and a finite cutoff

<a id="lemma-4"></a>

**Lemma 4.1.**

<a id="label-lem-sieve"></a>

Write $`\operatorname{rad}(N)=k\ell_1\cdots\ell_s`$, where $`k`$ is squarefree and the $`\ell_i`$ are distinct primes not dividing $`k`$. Suppose $`s\ge1`$ and
```math
\delta=1-\sum_{i=1}^s\frac1{\ell_i}>0.
```
Then $`A(N)>0`$ whenever

<a id="label-eq-sievecondition"></a>

```math
\tag{9}
 \frac CB>W(k)\left(\frac{s-1}{\delta}+2\right)-1.
```

For $`s=0`$, the sufficient condition is $`C/B>W(N)-1`$.

<!-- end lemma-4 -->

<a id="proof-4"></a>

**Proof.**

Pointwise on any multiset of elements of $`K^*`$, the $`e`$-free indicators give
```math
A(N)\ge\sum_{i=1}^s A(k\ell_i)-(s-1)A(k).
```
Indeed, an element which is not $`k`$-free contributes zero on the right; a $`k`$-free element missing at least one further prime condition contributes at most zero, and an $`N`$-free element contributes one.

Subtracting the character expansions for $`A(k\ell_i)`$ and $`\theta(\ell_i)A(k)`$ leaves the squarefree character orders divisible by $`\ell_i`$. There are $`W(k)`$ such orders, with normalized total weight one for each. Therefore
```math
\left|A(k\ell_i)-\theta(\ell_i)A(k)\right|
 \le\theta(k\ell_i)W(k)B.
```
Since $`\sum_i\theta(\ell_i)=s-1+\delta`$, inequality [(8)](#label-eq-freebound) yields
```math
\begin{align*}
 A(N)&\ge\delta A(k)-\theta(k)W(k)B(s-1+\delta)\\
 &\ge\theta(k)\bigl[\delta(C+B)-W(k)B(s-1+2\delta)\bigr].
\end{align*}
```
This is positive under [(9)](#label-eq-sievecondition). The case $`s=0`$ follows directly from [(8)](#label-eq-freebound). $`\square`$

<!-- end proof-4 -->

<a id="proposition-1"></a>

**Proposition 4.2.**

<a id="label-prop-cutoff"></a>

If $`q\ge1511`$ and $`p\ne3`$, then $`A(N)>0`$.

<!-- end proposition-1 -->

<a id="proof-5"></a>

**Proof.**

In both cases of [(7)](#label-eq-CB),

<a id="label-eq-uniform"></a>

```math
\tag{10}
 \frac CB\ge\frac{q-1/q}{6}.
```

Let $`t=\omega(N)`$, and write $`p_1<p_2<\cdots`$ for the ordinary primes. Take $`k`$ to contain the $`j`$ smallest prime divisors of $`N`$. For $`j<t`$, put
```math
d_{t,j}=1-\sum_{i=j+1}^t\frac1{p_i},\qquad
 R_{t,j}=2^j\left(\frac{t-j-1}{d_{t,j}}+2\right)-1,
```
using only choices with $`d_{t,j}>0`$. For $`j=t`$, put $`R_{t,t}=2^t-1`$. The actual $`\delta`$ is at least $`d_{t,j}`$, so Lemma [4.1](#label-lem-sieve) applies if $`q-1/q>6R_{t,j}`$.

For $`1\le t\le15`$, choose respectively
```math
j=0,1,2,2,2,2,2,2,2,2,2,2,3,3,3.
```
Exact rational calculation gives $`6R_{t,j}<1511-1/1511`$ in every case. For $`16\le t\le56`$, Table [1](#label-tab-sieve) gives $`j`$ and an integer $`T`$ satisfying

<a id="label-eq-finitecert"></a>

```math
\tag{11}
 \prod_{i=1}^t p_i>T^6,\qquad T-1/T>6R_{t,j}.
```

Since $`N=q^6-1`$ has $`t`$ distinct prime factors, the first inequality implies $`q>T`$, and the second proves the desired sieve condition.

For the infinite tail, the exact base inequality is
```math
\prod_{i=1}^{57}p_i>(6\cdot2^{57})^6.
```
The next prime is $`271>64`$, as are all subsequent primes. Induction therefore proves $`\prod_{i=1}^t p_i>(6\cdot2^t)^6`$ for every $`t\ge57`$. Hence $`q>6\cdot2^t`$, which implies $`q-1/q>6(2^t-1)`$. The direct case $`j=t`$ suffices.

All finite rational inequalities, prime products, and the tail base inequality are checked by the supplied verifier. This completes the cutoff proof. $`\square`$

<!-- end proof-5 -->

<a id="label-tab-sieve"></a>

**Table 1.** Exact finite sieve certificates for [(11)](#label-eq-finitecert).

| $`t`$ | $`j`$ | $`T`$ | $`t`$ | $`j`$ | $`T`$ | $`t`$ | $`j`$ | $`T`$ |
|------:|------:|------:|------:|------:|------:|------:|------:|------:|
|    16 |     3 |  1724 |    30 |     3 |  6891 |    44 |     4 | 15968 |
|    17 |     3 |  1949 |    31 |     3 |  7469 |    45 |     4 | 16726 |
|    18 |     3 |  2195 |    32 |     3 |  8090 |    46 |     4 | 17515 |
|    19 |     3 |  2456 |    33 |     3 |  8752 |    47 |     4 | 18316 |
|    20 |     3 |  2736 |    34 |     3 |  9470 |    48 |     4 | 19129 |
|    21 |     3 |  3040 |    35 |     4 | 10129 |    49 |     4 | 19969 |
|    22 |     3 |  3363 |    36 |     4 | 10701 |    50 |     4 | 20841 |
|    23 |     3 |  3710 |    37 |     4 | 11290 |    51 |     4 | 21743 |
|    24 |     3 |  4078 |    38 |     4 | 11897 |    52 |     4 | 22671 |
|    25 |     3 |  4464 |    39 |     4 | 12525 |    53 |     4 | 23634 |
|    26 |     3 |  4878 |    40 |     4 | 13171 |    54 |     4 | 24617 |
|    27 |     3 |  5326 |    41 |     4 | 13837 |    55 |     4 | 25630 |
|    28 |     3 |  5807 |    42 |     4 | 14529 |    56 |     4 | 26673 |
|    29 |     3 |  6329 |    43 |     4 | 15235 |       |       |       |

## 5. Finite certificates and completion of the proof

For each of the 261 prime powers $`q=p^r<1511`$ with $`p\ne3`$, the file `witnesses.json` supplies a monic polynomial $`M(Z)`$ of degree $`2r`$ over $`\mathbb F_p`$ and an exponent $`v`$. If $`z`$ denotes the residue class of $`Z`$, the certificate verifies that $`z`$ has exact order $`Q-1`$ in $`\mathbb F_p[Z]/(M)`$. This proves that the quotient is a field: the cyclic subgroup generated by $`z`$ already contains all $`Q-1`$ nonzero residue classes. It is therefore a specified model of $`\mathbb F_Q`$.

The exponent satisfies $`\gcd(v,Q-1)=1`$, and $`\lambda=z^v`$. In the quotient by $`h_\lambda`$, the residue class $`x`$ of $`X`$ is checked to satisfy

<a id="label-eq-ordercert"></a>

```math
\tag{12}
 x^N=1,\qquad x^{N/\ell}\ne1\quad\text{for every prime }\ell\mid N.
```

Thus its order is exactly $`N`$. Independently, the verifier checks
```math
\gcd(X^Q-X,h_\lambda)=1.
```
A cubic with no root in $`\mathbb F_Q`$ is irreducible, so this also verifies the field property of the cubic quotient directly. Consequently each certificate gives a primitive polynomial of the required form.

There is no unverified factorization in [(12)](#label-eq-ordercert). The full prime support of $`N`$ is obtained by factoring the four integers in
```math
q^6-1=(q-1)(q+1)(q^2+q+1)(q^2-q+1).
```
For this finite interval, each factor is less than $`1511^2+1511+1`$. Trial division is enough, and the verifier removes all resulting prime powers from $`N`$ and checks that the residual factor is one. It likewise verifies the complete set of prime powers below the cutoff, rather than merely reading a claimed count.

The witness generator uses C++ integer encodings of finite-field elements. The separate Python verifier uses coefficient tuples and independent polynomial arithmetic. It verifies the base-field generator, the primitive constant, cubic irreducibility, all root-order tests, the 261-case coverage, and every finite inequality in Proposition [4.2](#label-prop-cutoff). Neither implementation uses floating-point arithmetic for a mathematical decision.

<a id="proof-6"></a>

**Proof of Theorem [1.1](#label-thm-main).**

Lemma [2.1](#label-lem-obstruction) excludes characteristic three. In all other characteristics, Proposition [4.2](#label-prop-cutoff) proves existence when $`q\ge1511`$. The finite certificates prove existence for every remaining prime power $`q`$. The norm argument after Lemma [2.2](#label-lem-param) ensures that all counted constants are primitive. These cases exhaust the theorem. $`\square`$

<!-- end proof-6 -->

## 6. Relation to earlier claims and further questions

The case $`q=3`$ was already disproved in [\[3\]](#ref-S); we do not claim priority for that counterexample. The new conclusion is the complete classification of the surviving cases, together with the two uniform counting estimates. The general degree-$`m`$ existence problem for polynomials $`g(X)+\lambda`$, with nonconstant coefficients in a subfield, remains outside the theorem.

The sufficient-condition argument in [\[3, Section 5\]](#ref-S) counts pairs in which $`-g(\beta)`$ is $`(q^n-1)`$-free in $`\mathbb F_{q^{mn}}^*`$. That condition does not require $`-g(\beta)`$ to lie in $`\mathbb F_{q^n}`$, so it is not equivalent to the stated primitive-constant condition. Its general conclusion also conflicts with a norm obstruction: if $`m`$ is odd and $`q^n\equiv3\pmod4`$, the norm of a primitive root would be $`-\lambda`$, while a primitive $`\lambda`$ has nonprimitive negative. Taking $`m=n=3`$ and arbitrarily large $`q=7^{2r+1}`$ meets the characteristic hypothesis of its Theorem 5.1 and exhibits this incompatibility. Our proof for the cubic family uses no such equivalence.

The parametrization gives a more general route for prescribed-coefficient questions: impose the trace equations first, then check that the induced multiplicative characters are geometrically nonconstant on the resulting curve. The characteristic-three obstruction here shows that this last condition cannot be omitted. Extending the classification to other pairs of prescribed cubic coefficients, or to higher-degree subfield families, requires a new analysis of those curves and their exceptional characters.

## References

<a id="ref-AS"></a>

**\[1\]** A. Awasthi and R. K. Sharma, *Primitive transformation shift registers over finite fields*, Journal of Algebra and Its Applications **18** (2019), 1950171. [doi:10.1142/S0219498819501718](https://doi.org/10.1142/S0219498819501718). Author revision dated August 18, 2018; earlier version [arXiv:1612.05367](https://arxiv.org/abs/1612.05367).

<a id="ref-FW"></a>

**\[2\]** L. Fu and D. Wan, *A class of incomplete character sums*, Quarterly Journal of Mathematics **65** (2014), 1195–1211. [doi:10.1093/qmath/hau012](https://doi.org/10.1093/qmath/hau012). We use the corrected [arXiv:1303.3650v3](https://arxiv.org/abs/1303.3650v3), January 6, 2025.

<a id="ref-S"></a>

**\[3\]** A. K. Sharma, *On the existence of primitive polynomials $`f(x)=g(x)+\lambda`$ over finite fields*, [arXiv:2608.07262v1](https://arxiv.org/abs/2608.07262v1), August 7, 2026.
