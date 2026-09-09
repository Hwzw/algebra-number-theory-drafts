# Effective joint Fourier decay at independent Pisot and Salem scales

Henry Zweiman

September 9, 2026

## Abstract

Let $`\theta,\phi>1`$ be multiplicatively independent real algebraic integers, each with all its other conjugates in the closed unit disk. For positive algebraic $`s,t`$, we prove an effective upper bound $`\exp(-c\log\log u/\log\log\log u)`$ for the product of the two Bernoulli Fourier products at arguments $`su`$ and $`tu`$. The result applies to Pisot–Pisot, Pisot–Salem, and Salem–Salem pairs. The proof gives a quantitative lower bound on the combined number of large fractional parts at the two scales. Its ingredients are a uniform algebraic projection on a near-integer interval, a height bound that excludes exact resonance, and the theorem on linear forms in logarithms. We also obtain the same decay rate for convolutions of homogeneous self-similar measures with algebraic translations.

## 1. Statement and context

All logarithms are natural. Write $`\left\|x\right\|`$ for distance to the nearest integer, and, for $`\theta>1`$, put
```math
F_\theta(u)=\prod_{n=0}^{\infty}\cos(\pi u\theta^{-n}).
```
The product converges: its tail factors differ from one by a summable sequence. A Pisot number is a real algebraic integer greater than one whose other conjugates have modulus less than one. Allowing conjugates on the unit circle also includes Salem numbers. Independence means $`\theta^m\phi^n=1`$, with $`m,n\in\mathbb Z`$, only when $`m=n=0`$.

<a id="theorem-1"></a>

**Theorem 1.**

<a id="label-thm-main"></a>

Let $`\theta,\phi>1`$ be multiplicatively independent real algebraic integers. Suppose all other conjugates of each have modulus at most one. Let $`s,t>0`$ be algebraic. There are effectively computable constants $`c>0`$ and $`U>\exp(\exp(e))`$, depending only on these four numbers, such that

<a id="label-eq-main"></a>

```math
\tag{1}
 |F_\theta(su)F_\phi(tu)|
 \leq \exp\left(-c\frac{\log\log u}{\log\log\log u}\right)
 \qquad(u\geq U).
```

<!-- end theorem-1 -->

The qualitative Pisot product problem has a classical solution in the nonexceptional parameter range: Senge and Straus [\[4\]](#ref-SS), Theorem 2, give its multiplicative-independence criterion. The case $`\theta=2`$ has the elementary identity $`F_2(u)=\sin(2\pi u)/(2\pi u)`$ and must be excluded from an “if and only if” formulation; it causes no problem for the sufficient condition in Theorem [1](#label-thm-main). Stewart [\[5\]](#ref-Stewart) gives effective joint digit estimates in integer bases. The present question is quantitative joint decay with arbitrary nonrational Pisot and Salem parameters and algebraic rescalings.

Nguyen [\[3\]](#ref-Nguyen), Theorem 1.6, proves qualitative decay for Pisot products with arguments having algebraic main terms. His Section 3 extracts algebraic approximants from long intervals of small fractional parts. We use a uniform projection version of this mechanism and make the interval ratio grow with the frequency. This permits an effective logarithm estimate despite the changing approximants.

For a single Salem parameter, Marshall-Maldonado and Solomyak [\[2\]](#ref-MMS), Corollary B.1, obtain an upper bound of the form $`A\exp(-C\log^*u)`$. Our result concerns a product with independent parameters and does not improve their single-factor assertion. Varjú and Yu [\[6\]](#ref-VY), Theorem 1.10, give a stronger joint fractional-part bound for one fixed base at two arguments whose ratio is not Liouville over the field of that base. Here the bases differ; the ratio of arguments may be one. No assertion of power Fourier decay, absolute continuity, or optimality of [(1)](#label-eq-main) is made.

## 2. Two height estimates

Use the absolute logarithmic Weil height $`h`$, with $`h(0)=0`$. For a number field $`K`$, normalize its absolute values so that the product formula holds and
```math
h(z)=\sum_v\log\max(1,|z|_v)
      =\tfrac12\sum_v|\log|z|_v|\quad(z\in K^*).
```
We use $`h(xy)\leq h(x)+h(y)`$, $`h(x^{-1})=h(x)`$, and $`h(x+y)\leq h(x)+h(y)+\log2`$.

<a id="lemma-1"></a>

**Lemma 2.**

<a id="label-lem-height"></a>

For fixed independent positive algebraic numbers $`\theta,\phi`$, an effectively computable $`b>0`$ satisfies

<a id="label-eq-height"></a>

```math
\tag{2}
 h(\theta^m\phi^n)\geq b(|m|+|n|)\qquad(m,n\in\mathbb Z).
```

<!-- end lemma-1 -->

<a id="proof-1"></a>

**Proof.**

Take a field containing the two numbers and let $`S`$ consist of its archimedean places and the finite places where either number is not a unit. Their logarithm vectors $`v,w\in\mathbb R^S`$ are linearly independent over $`\mathbb R`$. Indeed, a rational dependence would make a nontrivial $`\theta^m\phi^n`$ have height zero; this is a positive real root of unity, hence one. An irrational dependence would, by rational approximation, give infinitely many distinct such products with logarithm vectors bounded (in fact tending to zero). They have bounded degree and height, contrary to Northcott’s finiteness theorem.

Choose a nonzero two-by-two minor of the matrix with columns $`v,w`$. The inverse matrix bounds $`|m|+|n|`$ by a constant times $`\|mv+nw\|_1=2h(\theta^m\phi^n)`$, proving the estimate. This also proves effectivity. The set $`S`$ and its logarithms are computable from algebraic data. Certified approximations will eventually identify and bound away from zero some nonzero minor, since one exists. An upper bound for the inverse norm then gives a positive lower bound for $`b`$. No effective version of Northcott finiteness is required. $`\square`$

<!-- end proof-1 -->

<a id="lemma-2"></a>

**Lemma 3.**

<a id="label-lem-logs"></a>

Fix positive algebraic $`\theta,\phi`$ and a number field $`K\subset\mathbb R`$ containing them. There is an effective $`B>0`$ such that, for positive $`\gamma\in K`$, $`m,n\in\mathbb Z`$, and $`E\geq2`$ with $`\max(|m|,|n|)\leq E`$, one has

<a id="label-eq-logs"></a>

```math
\tag{3}
 \gamma\theta^m\phi^n\ne1\quad\Longrightarrow\quad
 \log|\gamma\theta^m\phi^n-1|
 >-B(1+h(\gamma))\log(E+2).
```

<!-- end lemma-2 -->

<a id="proof-2"></a>

**Proof.**

Apply the multiplicative form of Matveev’s estimate, as stated in Bugeaud–Mignotte–Siksek [\[1\]](#ref-BMS), Theorem 9.4. For $`r`$ logarithms, the real-field bound is
```math
\log|\alpha_1^{b_1}\cdots\alpha_r^{b_r}-1|
 >-1.4\,30^{r+3}r^{4.5}D^2(1+\log D)(1+\log B_0)
       \prod_{i=1}^r A_i,
```
where $`D=[K:\mathbb Q]`$, $`B_0\geq\max_i|b_i|`$, and $`A_i\geq\max\{Dh(\alpha_i),|\log\alpha_i|,0.16\}`$. Take the numbers $`\gamma,\theta,\phi`$ and exponents $`1,m,n`$, omitting any term equal to one or having exponent zero. The parameters for $`\theta,\phi`$ are fixed. Since $`|\log\gamma|\leq Dh(\gamma)`$, the remaining parameter is at most a fixed multiple of $`1+h(\gamma)`$. This gives [(3)](#label-eq-logs); when only one term remains, the same estimate or the elementary height inequality suffices. $`\square`$

<!-- end proof-2 -->

## 3. Projection from a near-integer interval

<a id="lemma-3"></a>

**Lemma 4.**

<a id="label-lem-projection"></a>

Fix a real algebraic integer $`\theta>1`$ of degree $`d`$, all of whose other conjugates have modulus at most one. There are effective $`\eta_\theta\in(0,1/2)`$ and $`C_\theta\geq1`$ with the following property. If $`1\leq a<\theta`$, $`k\geq0`$, $`L\geq k+d-1`$, and
```math
\left\|a\theta^j\right\|<\eta_\theta\quad(k\leq j\leq L),
```
there is $`\alpha\in\mathbb Q(\theta)`$ such that

<a id="label-eq-projection"></a>

```math
\tag{4}
 h(\alpha)\leq C_\theta(k+1),\qquad
 |a-\alpha|\leq C_\theta\theta^{k-L}.
```

<!-- end lemma-3 -->

<a id="proof-3"></a>

**Proof.**

Write $`P(X)=\sum_{i=0}^d c_iX^i`$ for the monic minimal polynomial. Choose $`\eta_\theta<(2\sum_i|c_i|)^{-1}`$ and let $`A_j`$ be the nearest integer to $`a\theta^j`$. For $`k\leq j\leq L-d`$, the integer $`\sum_i c_iA_{j+i}`$ has absolute value less than one, hence is zero.

Let $`t_1=\theta,t_2,\ldots,t_d`$ be the distinct roots of $`P`$. The initial $`d`$ values and the recurrence give unique coefficients $`b_i`$ with

<a id="label-eq-binet"></a>

```math
\tag{5}
 A_{k+r}=\sum_{i=1}^d b_it_i^r\qquad(0\leq r\leq L-k).
```

The inverse of the fixed Vandermonde matrix $`(t_i^r)_{0\leq r<d,1\leq i\leq d}`$ has bounded entries. Since $`|A_{k+r}|\leq2\theta^{k+d}`$ in this initial range, $`|b_i|\leq C\theta^k`$, with effective $`C`$.

Write
```math
\frac{P(X)}{(X-\theta)P'(\theta)}=\sum_{r=0}^{d-1}v_rX^r.
```
This polynomial is one at $`t_1`$ and zero at the other roots, so $`b_1=\sum_rv_rA_{k+r}\in\mathbb Q(\theta)`$. Set $`\alpha=\theta^{-k}b_1`$. The height inequalities, with the $`v_r`$ fixed and $`h(A_{k+r})\leq(k+d)\log\theta+\log2`$, give the first bound in [(4)](#label-eq-projection). At the last index, [(5)](#label-eq-binet) gives
```math
|a-\alpha|
 \leq\theta^{-L}\left(\eta_\theta+
              \sum_{i=2}^d |b_i|\,|t_i|^{L-k}\right)
 \leq C_\theta\theta^{k-L}.
```
This uses only $`|t_i|\leq1`$, so it includes the Salem case. All constructions also apply when $`d=1`$, with an empty final sum. $`\square`$

<!-- end proof-3 -->

## 4. Independent scales force large fractional parts

For $`x\geq1`$, define the finite count
```math
D_\theta(x;\eta)=\#\{0\leq n\leq\lfloor\log_\theta x\rfloor:
                           \left\|x\theta^{-n}\right\|\geq\eta\}.
```

<a id="theorem-2"></a>

**Theorem 5.**

<a id="label-thm-count"></a>

Under the hypotheses of Theorem [1](#label-thm-main), there are effective $`\eta,c_1>0`$ and $`U_1`$ such that

<a id="label-eq-count"></a>

```math
\tag{6}
 D_\theta(su;\eta)+D_\phi(tu;\eta)
 \geq c_1\frac{\log\log u}{\log\log\log u}\qquad(u\geq U_1).
```

<!-- end theorem-2 -->

<a id="proof-4"></a>

**Proof.**

Write $`su=a\theta^e`$ and $`tu=b\phi^f`$, with $`1\leq a<\theta`$, $`1\leq b<\phi`$, and set $`E=\max(e,f)`$. For effectively large $`u`$, both exponents are positive, $`E`$ is comparable to $`\log u`$, and $`e/f`$ is bounded above and below by positive constants. All constants below depend only on the fixed data. Take $`\eta`$ smaller than the two thresholds in Lemma [4](#label-lem-projection) and take a fixed integer $`k_0\geq\max(1,\deg\theta,\deg\phi)`$.

Choose
```math
R=\lceil H\log(E+2)\rceil,
```
where the effective constant $`H`$ will be fixed sufficiently large. For an integer $`j\geq2`$, put $`k=\lfloor e/R^j\rfloor`$, $`l=\lfloor f/R^j\rfloor`$. Consider only indices for which $`\min(e,f)/R^j\geq2k_0`$. Then $`k,l\geq k_0`$ and

<a id="label-eq-compare"></a>

```math
\tag{7}
 \frac{e}{2f}\leq\frac{k}{l}\leq\frac{2e}{f},\qquad
 k+l\leq\frac{e+f}{R^2}.
```

We claim that at least one distance is at least $`\eta`$ on the paired intervals $`[k,Rk-1]`$ and $`[l,Rl-1]`$ for the sequences $`a\theta^i`$ and $`b\phi^i`$, respectively. Suppose otherwise. Lemma [4](#label-lem-projection) gives $`\alpha\in\mathbb Q(\theta)`$, $`\beta\in\mathbb Q(\phi)`$ with
```math
h(\alpha)+h(\beta)\leq C(k+l),\quad
 |a-\alpha|\leq C\theta^{1-(R-1)k},\quad
 |b-\beta|\leq C\phi^{1-(R-1)l}.
```
For sufficiently large $`R`$ these errors are less than $`1/2`$, so $`\alpha,\beta`$ are positive and uniformly bounded above and away from zero. Set
```math
\gamma=\frac{t\alpha}{s\beta},\qquad
 Z=\gamma\theta^e\phi^{-f}.
```
Since $`(t/s)\theta^e\phi^{-f}=b/a`$, the preceding estimates and [(7)](#label-eq-compare) imply, with fixed effective constants $`C_2,c_2>0`$,

<a id="label-eq-Z"></a>

```math
\tag{8}
 h(\gamma)\leq C_2(k+l),\qquad
 |Z-1|\leq\exp(-c_2R(k+l)).
```

Here fixed prefactors are absorbed by increasing the lower bound on $`R`$; comparability of $`k,l`$ is uniform in $`j`$.

If $`Z=1`$, Lemma [2](#label-lem-height) gives
```math
b_0(e+f)\leq h(\theta^e\phi^{-f})=h(\gamma)
 \leq C_2(k+l)\leq C_2(e+f)/R^2,
```
which is impossible for large $`R`$. If $`Z\ne1`$, apply Lemma [3](#label-lem-logs) in the fixed field $`\mathbb Q(s,t,\theta,\phi)`$. It gives $`\log|Z-1|>-C_3(k+l)\log(E+2)`$, contradicting [(8)](#label-eq-Z) once $`H>C_3/c_2`$. This proves the claim.

There are sufficiently many disjoint pairs of intervals. Precisely, put
```math
J=\left\lfloor\frac{\log(\min(e,f)/(2k_0))}{\log R}\right\rfloor.
```
All $`2\leq j\leq J`$ are allowed. For effectively large $`E`$, $`J-1\geq c_3\log E/\log\log E`$. For each base the intervals are disjoint, because $`R\lfloor e/R^j\rfloor\leq\lfloor e/R^{j-1}\rfloor`$, and similarly for $`f`$. Their indices lie between zero and $`e`$ or $`f`$, since $`j\geq2`$. Reversing indices, $`a\theta^i=su\theta^{-(e-i)}`$, shows that every large distance supplied by the claim is counted in [(6)](#label-eq-count). Distinct pairs give distinct counted factors. Finally $`E\asymp\log u`$ converts the lower bound for $`J-1`$ into [(6)](#label-eq-count). All thresholds used are effective. $`\square`$

<!-- end proof-4 -->

<a id="proof-5"></a>

**Proof of Theorem [1](#label-thm-main).**

At each factor counted in Theorem [5](#label-thm-count), $`|\cos(\pi x)|\leq\rho:=\cos(\pi\eta)<1`$. Every remaining factor has modulus at most one. Thus the product is bounded by $`\rho^{D_\theta(su;\eta)+D_\phi(tu;\eta)}`$, proving the theorem. $`\square`$

<!-- end proof-5 -->

## 5. Homogeneous self-similar measures

Use the Fourier convention $`\widehat\mu(u)=\int e^{2\pi iux}\,d\mu(x)`$. A homogeneous self-similar probability measure with contraction $`\theta^{-1}`$ and translations $`a_1,\ldots,a_r`$ satisfies
```math
\widehat\mu(u)=\prod_{n\geq0}
       \left(\sum_{i=1}^r p_i e^{2\pi i a_i u\theta^{-n}}\right),
 \qquad p_i>0,\quad\sum_i p_i=1.
```

<a id="corollary-1"></a>

**Corollary 6.**

<a id="label-cor-measures"></a>

Let $`\theta,\phi`$ satisfy Theorem [1](#label-thm-main). Let $`\mu,\nu`$ be homogeneous self-similar probability measures with these reciprocal contractions, positive probability vectors, and algebraic translations. Suppose each translation set has at least two distinct elements. Then $`|\widehat{\mu*\nu}(u)|`$ satisfies the bound [(1)](#label-eq-main) with suitable $`c,U`$. The constants are effective when the probabilities are also given as algebraic numbers.

<!-- end corollary-1 -->

<a id="proof-6"></a>

**Proof.**

Choose distinct translations $`a_1,a_2`$ for $`\mu`$ and $`b_1,b_2`$ for $`\nu`$, and put $`s=|a_1-a_2|`$, $`t=|b_1-b_2|`$. For a factor of the first Fourier product,
```math
\left|\sum_i p_i e^{2\pi i a_i x}\right|^2
 =1-4\sum_{i<j}p_ip_j\sin^2(\pi(a_i-a_j)x)
 \leq1-4p_1p_2\sin^2(\pi sx).
```
The analogous inequality holds for the second measure. Each distance counted in Theorem [5](#label-thm-count) therefore supplies a factor bounded by a fixed number strictly less than one. Multiplication gives the assertion, since $`\widehat{\mu*\nu}=\widehat\mu\widehat\nu`$. For arbitrary positive probabilities one can choose positive rational lower bounds for the selected weights to obtain existence of constants; algebraic input makes this choice algorithmic. $`\square`$

<!-- end proof-6 -->

For a concrete mixed pair take $`\theta=(1+\sqrt5)/2`$ and let $`\phi>1`$ be the largest root of $`X^4-3X^3+3X^2-3X+1`$. Indeed, $`y=\phi+\phi^{-1}=(3+\sqrt5)/2>2`$; its other conjugate lies in $`(-2,2)`$, giving two unit-circle roots. The polynomial is irreducible: $`y^2-4`$ has a negative conjugate in the real quadratic field, so is not a square there. Thus $`\phi`$ has degree four and is Salem. These parameters are independent. More generally, a number satisfying our conjugate assumption obeys $`\mathbb Q(\theta^m)=\mathbb Q(\theta)`$ for every $`m\geq1`$: an embedding fixing $`\theta^m`$ must send $`\theta`$ to a conjugate of modulus $`\theta`$, and there is only one. Hence two such numbers of different degrees cannot have a common positive power.

The loss of $`\log\log\log u`$ comes from intervals with ratio $`R\asymp\log\log u`$: the logarithm estimate charges a factor $`\log E`$ for exponents of size $`E\asymp\log u`$. Improving this rate requires additional input beyond the estimates used here. The theorem supplies no comparable assertion for a single Salem factor or for two multiplicatively dependent nonexceptional Pisot bases.

## References

<a id="ref-BMS"></a>

**\[1\]** Y. Bugeaud, M. Mignotte, and S. Siksek, Classical and modular approaches to exponential Diophantine equations I. Fibonacci and Lucas perfect powers, *Ann. of Math.* (2) **163** (2006), 969–1018. [Authoritative full text](https://annals.math.princeton.edu/wp-content/uploads/annals-v163-n3-p05.pdf).

<a id="ref-MMS"></a>

**\[2\]** J. Marshall-Maldonado and B. Solomyak, Quantitative weak mixing for typical Salem substitution suspension flows, [arXiv:2601.15035v1](https://arxiv.org/abs/2601.15035v1) (2026).

<a id="ref-Nguyen"></a>

**\[3\]** K. D. Nguyen, Algebraic numbers and Fourier analysis: Salem’s third problem, [arXiv:2604.18875v1](https://arxiv.org/abs/2604.18875v1) (2026).

<a id="ref-SS"></a>

**\[4\]** H. G. Senge and E. G. Straus, PV-numbers and sets of multiplicity, *Period. Math. Hungar.* **3** (1973), 93–100. [doi:10.1007/BF02018464](https://doi.org/10.1007/BF02018464).

<a id="ref-Stewart"></a>

**\[5\]** C. L. Stewart, On the representation of an integer in two different bases, *J. Reine Angew. Math.* **319** (1980), 63–72. [Author’s copy](https://uwaterloo.ca/pure-mathematics/sites/default/files/uploads/documents/j-reine-ange-math-1980.pdf).

<a id="ref-VY"></a>

**\[6\]** P. P. Varjú and H. Yu, Fourier decay of self-similar measures and self-similar sets of uniqueness, [arXiv:2004.09358v2](https://arxiv.org/abs/2004.09358v2) (2021).
