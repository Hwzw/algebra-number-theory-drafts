# The average number of unit-circle zeros in Stanley’s reciprocal polynomial family

Henry Zweiman

September 9, 2026

## Abstract

For a finite set $`S`$ of positive integers, put $`N_S(x)=1-(1-x)\sum_{j\in S}x^j`$. We determine the asymptotic average number of unit-circle zeros when $`S`$ is chosen uniformly subject to $`\max S=2b+1`$ and reciprocity of $`N_S`$. The average is $`(2b+2)/\sqrt3+o(b)`$, with zeros counted with multiplicity. More generally, the mean unit-circle zero measure, normalized by the degree, converges to $`1/\sqrt3`$ times uniform angular measure. This answers the average-count question posed by Stanley. The proof parametrizes the family by independent signs, preserves its zero-set law while randomizing a fixed boundary term, and applies the general real universality theorem of Nguyen and Vu. A Gaussian density computation gives the bulk limit, and the Erdős–Turán discrepancy theorem controls the endpoints.

## 1. Introduction and statement

For a nonempty finite set $`S\subset\mathbb Z_{>0}`$ define

<a id="label-eq-NS"></a>

```math
\tag{1}
 N_S(x)=1-(1-x)\sum_{j\in S}x^j.
```

If $`d=\max S`$, this is a monic integer polynomial of degree $`d+1`$ and constant coefficient one. Let
```math
\mathcal S_b=\{S\subset\{1,\ldots,2b+1\}:\max S=2b+1,
 \ x^{2b+2}N_S(1/x)=N_S(x)\}.
```
There are $`2^b`$ such sets. Throughout the paper $`S`$ is uniform on $`\mathcal S_b`$, and every zero is counted with its algebraic multiplicity. Write $`U_b(S)`$ for the number of zeros of $`N_S`$ on the unit circle.

Stanley introduced these polynomials in connection with enumerative identities and cyclotomic sets [\[5\]](#ref-StanleyECA). His question [\[6, Addendum 2\]](#ref-StanleyMO) asks for an analytic estimate of the number of unit-circle zeros of
```math
F_{2b+1}(x)=\prod_{S\in\mathcal S_b}N_S(x),
```
or, equivalently, for the average of $`U_b(S)`$. The same unit-circle phenomenon is noted in the aside on page 9 of [\[5\]](#ref-StanleyECA).

<a id="theorem-1"></a>

**Theorem 1.**

<a id="label-thm-main"></a>

For every continuous function $`h`$ on the unit circle,

<a id="label-eq-measure"></a>

```math
\tag{2}
 \lim_{b\to\infty}\frac{1}{2b+2}
 \mathbb E\sum_{\substack{N_S(\alpha)=0\\|\alpha|=1}}h(\alpha)
 =\frac{1}{2\pi\sqrt3}\int_0^{2\pi}h(e^{i\theta})\,d\theta.
```

In particular,

<a id="label-eq-mean"></a>

```math
\tag{3}
 \mathbb EU_b=\frac{2b+2}{\sqrt3}+o(b).
```

<!-- end theorem-1 -->

<a id="corollary-1"></a>

**Corollary 2.**

<a id="label-cor-product"></a>

If $`g(2b+1)`$ denotes the number of unit-circle zeros of $`F_{2b+1}`$, then
```math
g(2b+1)=2^b\left(\frac{2b+2}{\sqrt3}+o(b)\right).
```
For every fixed arc $`I`$ of angular length $`|I|`$, the average number of unit-circle zeros of $`N_S`$ on $`I`$ is
```math
\frac{(2b+2)|I|}{2\pi\sqrt3}+o(b).
```

<!-- end corollary-1 -->

The constant $`1/\sqrt3`$ is classical for independent Gaussian cosine polynomials; see the discussion in [\[1\]](#ref-CFI). General Gaussian zero-density formulas are developed in [\[2\]](#ref-EK). The coefficients of [(1)](#label-eq-NS), however, are differences of constrained indicators and are not independent. We establish the exact reduction needed for this family, including its fixed endpoint coefficients. The probabilistic input is the existing general universality theorem [\[3, Theorem 2.6\]](#ref-NV), whose hypotheses we verify below. We do not assert a new universality theorem. Nor does the average-count result classify those $`S`$ for which all zeros are roots of unity, the broader problem in [\[5\]](#ref-StanleyECA).

## 2. Independent signs and exact preservation of zeros

Put $`d=2b+1`$ and $`m=b+1`$. Let $`a_j`$ be the indicator of $`j\in S`$ for $`1\le j\le d`$, and put $`a_0=0`$. Reciprocity of [(1)](#label-eq-NS) is equivalent to
```math
\sum_{j=0}^d a_jx^j+\sum_{j=0}^d a_jx^{d-j}
 =1+x+\cdots+x^d.
```
Indeed, multiplication of this identity by $`1-x`$ gives the reciprocity identity, and the implication reverses because $`1-x`$ is nonzero. Consequently

<a id="label-eq-complement"></a>

```math
\tag{4}
 a_j+a_{d-j}=1\quad(0\le j\le d).
```

The $`b`$ pairs besides $`\{0,d\}`$ may be chosen independently, proving $`|\mathcal S_b|=2^b`$.

Set $`\delta_j=2a_j-1`$. Thus $`\delta_0=-1`$, $`\delta_d=1`$, and $`\delta_{d-j}=-\delta_j`$. Under uniform choice of $`S`$, the variables
```math
\epsilon_k=\delta_{b+1+k},\qquad 0\le k<b,
```
are independent Rademacher variables, each taking $`-1`$ and $`1`$ with probability $`1/2`$. Pairing the terms indexed by $`j,d-j`$ gives

<a id="label-eq-T"></a>

```math
\begin{align}
 T_b(\theta)&:=e^{-im\theta}N_S(e^{i\theta})\notag\\
 &=\cos(m\theta)-2\sin(\theta/2)
 \left(\sin((b+\tfrac12)\theta)
   +\sum_{k=0}^{b-1}\epsilon_k\sin((k+\tfrac12)\theta)\right).
 \tag{5}
\end{align}
```
For completeness, substituting $`a_j=(1+\delta_j)/2`$ first gives
```math
N_S(x)=\tfrac12(1+x^{d+1})-\tfrac12(1-x)\sum_{j=0}^d\delta_jx^j.
```
Using $`1-e^{i\theta}=-2ie^{i\theta/2}\sin(\theta/2)`$ in this last expression proves [(5)](#label-eq-T), including its sign.

Make the change of variable $`\theta=\pi-2t`$. The signs $`\eta_k=(-1)^k\epsilon_k`$ are again independent Rademacher variables. Define, on $`0<t<\pi/2`$,

<a id="label-eq-RD"></a>

```math
\tag{6}
 R_b(t)=\sum_{k=0}^{b-1}\eta_k\cos((2k+1)t),\qquad
 D_b(t)=(-1)^b\left(\cos((2b+1)t)+\frac{\cos((2b+2)t)}{2\cos t}\right).
```

Equation [(5)](#label-eq-T) becomes

<a id="label-eq-change"></a>

```math
\tag{7}
 T_b(\pi-2t)=-2\cos t\,(R_b(t)+D_b(t)).
```

There are no missing endpoint zeros: $`N_S(1)=1`$ and $`N_S(-1)=1-2\sum_{j\in S}(-1)^j`$ is odd and nonzero. Complex conjugation pairs the zeros in the two open semicircles. The maps and nonvanishing factors in [(7)](#label-eq-change) preserve multiplicity. Hence $`U_b`$ is twice the number of zeros of $`R_b+D_b`$ in $`(0,\pi/2)`$.

<a id="lemma-1"></a>

**Lemma 3.**

<a id="label-lem-symmetrize"></a>

Let $`R`$ be a random analytic function with $`R`$ and $`-R`$ equal in law, and let $`D`$ be deterministic and analytic on the same domain. Assume $`R+D`$ is almost surely not identically zero. If $`\eta_*`$ is an independent Rademacher variable, then $`R+D`$ and $`R+\eta_*D`$ have the same zero-multiset distribution.

<!-- end lemma-1 -->

<a id="proof-1"></a>

**Proof.**

The functions $`R-D`$ and $`-R-D=-(R+D)`$ have the same distribution of zeros, since $`R`$ and $`-R`$ have the same law and multiplication by $`-1`$ does not change a zero or its multiplicity. The two choices of $`\eta_*`$ therefore give identical zero-multiset laws. $`\square`$

<!-- end proof-1 -->

To work with entire functions, define

<a id="label-eq-H"></a>

```math
\tag{8}\begin{aligned}
 H_b(t)&=\sum_{k=0}^{b-1}\eta_k\cos t\cos((2k+1)t)
       +\eta_*\Psi_b(t),\\
 \Psi_b(t)&=(-1)^b\left(\cos t\cos((2b+1)t)
                    +\tfrac12\cos((2b+2)t)\right).
\end{aligned}
```

This is a real trigonometric polynomial of degree $`2b+2`$. By Lemma [3](#label-lem-symmetrize), its zeros in $`(0,\pi/2)`$ have the same law as the transformed zeros of $`N_S`$ in the upper semicircle. Let $`\widetilde H_b`$ be obtained by replacing all $`b+1`$ signs in [(8)](#label-eq-H) by independent standard real Gaussians $`Z_k,Z_*`$. On this interval its zeros are those of

<a id="label-eq-G"></a>

```math
\tag{9}
 G_b(t)=\sum_{k=0}^{b-1}Z_k\cos((2k+1)t)+Z_*D_b(t).
```

## 3. Universality on compact subintervals

For a real analytic function $`f`$, write $`\mathcal Z_f(v)=\sum_{f(t)=0,\,t\in\mathbb R}v(t)`$ when $`v`$ has compact support in a domain of analyticity. Multiplicities are included.

<a id="proposition-1"></a>

**Proposition 4.**

<a id="label-prop-universality"></a>

For every $`v\in C_c^\infty((0,\pi/2))`$ there is $`c>0`$ such that

<a id="label-eq-univ"></a>

```math
\tag{10}
 \left|\mathbb E\mathcal Z_{H_b}(v)-\mathbb E\mathcal Z_{\widetilde H_b}(v)\right|
 =O_v(b^{1-c}).
```

<!-- end proposition-1 -->

<a id="proof-2"></a>

**Proof.**

We verify Conditions C1 and C2 of [\[3\]](#ref-NV) for Theorem 2.6, using its case $`k=1,l=0`$. Fix $`0<a<\pi/4`$ such that the support of $`v`$ lies in the interior of $`[a,\pi/2-a]`$. Rescale by $`z=bt`$ and use the real center set
```math
\mathcal D_b=[ab,(\pi/2-a)b],\qquad \delta=1/b.
```
There are $`n=b+1`$ random terms. Their deterministic basis functions are
```math
\phi_k(z)=\cos(z/b)\cos((2k+1)z/b)\quad(0\le k<b),
 \qquad \phi_*(z)=\Psi_b(z/b).
```
These are entire and real on the real axis. The random coefficients in both ensembles have mean zero, variance one, and uniformly bounded $`5/2`$ moments. Thus C1 holds with $`\epsilon=1/2`$ and matching moments. Take $`C_1=2`$ and $`\alpha_1=1/2`$ in C2. The remaining parameters $`A,c_1>0`$ are those prescribed by Theorem 2.6; the estimates below hold for every fixed $`A,c_1>0`$.

**Local zero counts.**

Both ensembles are trigonometric polynomials of degree at most $`2b+2`$. Their coefficient of $`\cos((2b+2)t)`$ is $`(-1)^b\eta_*`$ or $`(-1)^bZ_*`$, respectively, and is nonzero surely or almost surely. For $`w=e^{it}`$, multiplying either polynomial by $`w^{2b+2}`$ produces an algebraic polynomial of degree at most $`4b+4`$. On any disk of radius $`1/b`$ in the $`t`$ plane the exponential map is injective for large $`b`$. The number $`N`$ of zeros in a unit disk in the $`z`$ plane is therefore at most $`4b+4`$, including multiplicity. In particular $`N<b^2=\delta^{-C_1}`$ for sufficiently large $`b`$. The truncated moment in C2(1) is then zero.

**Size, delocalization, and derivatives.**

On complex distance two neighborhoods of $`\mathcal D_b`$ the basis functions and their first two $`z`$ derivatives are bounded by a constant independent of $`b,k`$. Indeed, the rescaled frequencies are at most $`2+2/b`$ and the imaginary parts of their arguments are bounded. For real $`t`$ in a compact subinterval of $`(0,\pi/2)`$, the geometric sum gives

<a id="label-eq-variance0"></a>

```math
\tag{11}
 \sum_{k=0}^{b-1}\cos^2((2k+1)t)=\frac b2+O_a(1).
```

To see uniformity, the oscillatory part is half the real part of $`e^{2it}(1-e^{4ibt})/(1-e^{4it})`$; its denominator is bounded away from zero on this subinterval. For $`t=x+iy`$, the identity
```math
|\cos(jt)|^2=\cos^2(jx)+\sinh^2(jy)
```
shows that the same lower bound applies to the sum of squared moduli. Also $`|\cos t|`$ is bounded below here. It follows, uniformly for $`z\in\mathcal D_b+B(0,1)`$, that

<a id="label-eq-delo"></a>

```math
\tag{12}
 \sum_j|\phi_j(z)|^2\ge c_a b,\qquad
 \frac{\max_j|\phi_j(z)|}{(\sum_j|\phi_j(z)|^2)^{1/2}}
 \le C_a b^{-1/2}.
```

This proves C2(4). The sums of squared first derivatives, and of the squared suprema of second derivatives on unit disks, are $`O_a(b)`$. Together with [(12)](#label-eq-delo), this proves C2(5), even without its allowed factor $`\delta^{-c_1}`$. Its mean-dependent term is zero.

For the Rademacher ensemble the function itself is bounded by $`C_a b`$ on the relevant disks. For the Gaussian ensemble the event that every coefficient has absolute value at most $`b`$ has complement of probability at most $`C b e^{-b^2/2}`$; on that event the function is bounded by $`C_a b^2`$. For any fixed $`A,c_1>0`$, these bounds imply C2(3), whose size threshold is $`\exp(b^{c_1})`$ and exceptional probability is $`O(b^{-A})`$.

**Anti-concentration.**

Fix $`z_0\in\mathcal D_b`$ and put $`t_0=z_0/b`$. We use [\[3, Lemma 9.2\]](#ref-NV) for the index set
```math
E_b=\{1,3,\ldots,2b-1\}
```
of size $`b`$, with all deterministic coefficients equal to one. Choose a fixed parameter $`L>\max\{2,2A\}`$. In an interval of length $`1/(200b)`$ centered at $`t_0`$, the lemma supplies a deterministic point $`x`$ such that, for the appropriate Rademacher or Gaussian variables $`\xi_k`$,

<a id="label-eq-smallball"></a>

```math
\tag{13}
 \sup_{u\in\mathbb R}\mathbb P\left\{
 \left|\sum_{k=0}^{b-1}\xi_k\cos((2k+1)x)-u\right|
 \le b^{-16L^2}\right\}=O_L(b^{-L/2}).
```

The interval-length hypothesis holds for all sufficiently large $`b`$. The lemma explicitly permits arbitrary index sets of the given size; it does not require consecutive frequencies. Condition on the distinguished coefficient $`\xi_*`$. At $`x`$, division of the function in [(8)](#label-eq-H) by $`\cos x`$ leaves the sum in [(13)](#label-eq-smallball) plus $`\xi_*D_b(x)`$. The uniformity in $`u`$ makes the estimate independent of this conditioning. Since $`|\cos x|\ge c_a>0`$, eventually
```math
\frac{\exp(-b^{c_1})}{|\cos x|}<b^{-16L^2}.
```
Thus the probability that the rescaled function at $`z'=bx`$ is smaller than $`\exp(-b^{c_1})`$ is $`O(b^{-A})`$. Moreover $`|z'-z_0|\le1/400<1/100`$. This is precisely the nearby-point condition C2(2), for each ensemble.

All constants can be chosen uniformly over $`z_0\in\mathcal D_b`$. Theorem 2.6 of [\[3\]](#ref-NV) therefore compares smooth real-zero statistics on intervals of radius $`1/100`$ in the $`z`$ variable with error $`O(b^{-c})`$. Its tests have derivatives through order six bounded by one; by linearity the same conclusion holds with any fixed derivative bound. Take a smooth partition of unity in $`z`$ with mesh $`1/400`$, pieces supported in intervals of radius less than $`1/100`$, and uniformly bounded derivatives. Multiply the pieces by $`v(z/b)`$. Only $`O_v(b)`$ pieces occur, their derivatives through order six stay bounded independently of $`b`$, and their centers lie in $`\mathcal D_b`$ for large $`b`$. Summing the local estimates proves [(10)](#label-eq-univ). $`\square`$

<!-- end proof-2 -->

## 4. The Gaussian density

<a id="proposition-2"></a>

**Proposition 5.**

<a id="label-prop-gaussian"></a>

Uniformly on $`[a,\pi/2-a]`$, the mean real-zero density of $`G_b`$ is

<a id="label-eq-density"></a>

```math
\tag{14}
 \rho_b(t)=\frac{2b}{\pi\sqrt3}+O_a(1).
```

Consequently, for every $`v\in C_c^\infty((0,\pi/2))`$,

<a id="label-eq-bulk"></a>

```math
\tag{15}
 \lim_{b\to\infty}\frac1b\mathbb E\mathcal Z_{H_b}(v)
 =\frac{2}{\pi\sqrt3}\int_0^{\pi/2}v(t)\,dt.
```

<!-- end proposition-2 -->

<a id="proof-3"></a>

**Proof.**

Write $`q_k=2k+1`$, and let
```math
\begin{align*}
 A_b(t)&=\operatorname{Var}G_b(t)=\sum_{k=0}^{b-1}\cos^2(q_kt)+D_b(t)^2,\\
 B_b(t)&=\operatorname{Cov}(G_b(t),G_b'(t))
       =-\tfrac12\sum_{k=0}^{b-1}q_k\sin(2q_kt)+D_b(t)D_b'(t),\\
 C_b(t)&=\operatorname{Var}G_b'(t)=\sum_{k=0}^{b-1}q_k^2\sin^2(q_kt)+D_b'(t)^2.
\end{align*}
```
On the chosen interval $`D_b=O_a(1)`$ and $`D_b'=O_a(b)`$. For $`r=0,1,2`$, summation by parts applied to the bounded partial sums of $`e^{4ikt}`$ gives
```math
\sum_{k=0}^{b-1}q_k^r e^{2iq_kt}=O_a(b^r).
```
The constants are uniform because $`|1-e^{4it}|`$ is bounded below. Using [(11)](#label-eq-variance0) and $`\sum_{k=0}^{b-1}q_k^2=b(4b^2-1)/3`$ yields

<a id="label-eq-ABC"></a>

```math
\tag{16}
 A_b=\frac b2+O_a(1),\qquad B_b=O_a(b),\qquad
 C_b=\frac23b^3+O_a(b^2).
```

In particular $`A_bC_b-B_b^2>0`$ for large $`b`$. The Gaussian real-zero formula [\[2, Theorem 3.1\]](#ref-EK) gives
```math
\rho_b(t)=\frac1\pi
 \sqrt{\frac{C_b(t)}{A_b(t)}-\left(\frac{B_b(t)}{A_b(t)}\right)^2}.
```
Equivalently, this follows by conditioning $`G_b'`$ on $`G_b=0`$ in the Kac–Rice formula: the conditional derivative variance is $`C_b-B_b^2/A_b`$. The covariance determinant is positive, so the formula applies on the interval and multiple Gaussian zeros have probability zero. Substituting [(16)](#label-eq-ABC) gives [(14)](#label-eq-density). On the support of $`v`$, the zeros of $`G_b`$ and $`\widetilde H_b`$ agree. Integrating their common density and applying Proposition [4](#label-prop-universality) proves [(15)](#label-eq-bulk). $`\square`$

<!-- end proof-3 -->

## 5. Endpoint control and completion of the proof

We need control near $`t=0,\pi/2`$ only for the original integer-polynomial ensemble. A deterministic estimate supplies it.

<a id="lemma-2"></a>

**Lemma 6.**

<a id="label-lem-endpoints"></a>

Let $`J`$ be an arc of angular length $`|J|`$. For every $`S\in\mathcal S_b`$,

<a id="label-eq-ET"></a>

```math
\tag{17}
 \#\{\alpha:N_S(\alpha)=0,\ \arg\alpha\in J\}
 \le\frac{(2b+2)|J|}{2\pi}
       +\frac8\pi\sqrt{(2b+2)\log(2b+3)}.
```

The same upper bound holds when only unit-circle zeros are counted.

<!-- end lemma-2 -->

<a id="proof-4"></a>

**Proof.**

Every coefficient of $`N_S`$ lies in $`\{-1,0,1\}`$, and its leading and constant coefficients are one. Therefore $`\max_{|z|=1}|N_S(z)|\le2b+3`$. The Erdős–Turán discrepancy inequality in the form [\[4, Theorem 2\]](#ref-Sound) bounds the angular discrepancy by $`(8/\pi)\sqrt{n h(P)}`$ for a monic degree-$`n`$ polynomial $`P`$ with constant coefficient one, where
```math
h(P)=\frac1{2\pi}\int_0^{2\pi}\log^+|P(e^{it})|\,dt.
```
Here $`h(N_S)\le\log(2b+3)`$, giving [(17)](#label-eq-ET). Restricting to unit-circle zeros can only decrease the count. Endpoint conventions for arcs may be handled by enlarging the arc and taking a limit; multiplicities are included in the discrepancy theorem. $`\square`$

<!-- end proof-4 -->

<a id="proof-5"></a>

**Proof of Theorem [1](#label-thm-main).**

Let $`\nu_b`$ be $`1/b`$ times the expected zero-counting measure of $`H_b`$ on $`(0,\pi/2)`$; we consider $`b\ge1`$. By the exact zero-law reduction, its total mass is at most $`(b+1)/b`$. Proposition [5](#label-prop-gaussian) says that its integral against each smooth compactly supported test converges to the integral against
```math
\frac{2}{\pi\sqrt3}\,dt.
```
For $`0<a<\pi/4`$, the two $`t`$ intervals $`(0,a)`$ and $`(\pi/2-a,\pi/2)`$ correspond to two angular arcs, each of length $`2a`$, near $`\theta=\pi`$ and $`\theta=0`$ in the upper semicircle. Lemma [6](#label-lem-endpoints) and the zero-law identity imply

<a id="label-eq-tight"></a>

```math
\tag{18}
 \nu_b\big((0,a)\cup(\pi/2-a,\pi/2)\big)
 =O(a)+O\left(\sqrt{\frac{\log b}{b}}\right),
```

with absolute implied constants for large $`b`$. By first inserting a smooth interior cutoff, then approximating a continuous test uniformly on the interior, and finally letting $`a`$ decrease to zero in [(18)](#label-eq-tight), we obtain, for every continuous $`v`$ on $`[0,\pi/2]`$,

<a id="label-eq-fullt"></a>

```math
\tag{19}
 \lim_{b\to\infty}\int v\,d\nu_b
 =\frac{2}{\pi\sqrt3}\int_0^{\pi/2}v(t)\,dt.
```

All approximations are uniform in $`b`$ because the total masses are bounded.

For a continuous $`h`$ on the unit circle put
```math
v(t)=h(e^{i(\pi-2t)})+h(e^{-i(\pi-2t)}).
```
Conjugation and the change of variables in [(7)](#label-eq-change) identify the left side of [(2)](#label-eq-measure) with $`[b/(2b+2)]\int v\,d\nu_b`$. Also
```math
\int_0^{\pi/2}v(t)\,dt
 =\frac12\int_0^{2\pi}h(e^{i\theta})\,d\theta.
```
Taking limits proves [(2)](#label-eq-measure). Setting $`h=1`$ proves [(3)](#label-eq-mean). $`\square`$

<!-- end proof-5 -->

<a id="proof-6"></a>

**Proof of Corollary [2](#label-cor-product).**

Multiplicities add under products, so $`g(2b+1)=2^b\mathbb EU_b`$. For arcs, approximate their indicators from above and below by continuous functions. The limiting angular measure has no atoms, and Theorem [1](#label-thm-main) then gives the asserted limit. $`\square`$

<!-- end proof-6 -->

## 6. Exact checks and further questions

The accompanying script uses rational arithmetic to verify the reciprocity parametrization and to count unit-circle roots without a numerical tolerance. For each reciprocal degree-$`2m`$ polynomial it forms the integer polynomial $`Q`$ defined by
```math
x^{-m}N_S(x)=Q(x+x^{-1}).
```
The recurrence $`C_0(y)=2`$, $`C_1(y)=y`$, $`C_{j+1}(y)=yC_j(y)-C_{j-1}(y)`$ represents $`x^j+x^{-j}`$. Squarefree factorization of $`Q`$, followed by Sturm counts in $`(-2,2)`$ weighted by the factor multiplicities, gives half the unit-circle count. There are no roots at $`\pm2`$, because $`N_S(\pm1)\ne0`$. For $`0\le b\le9`$, this checks all $`1{,}023`$ polynomials and reproduces
```math
(g(1),g(3),\ldots,g(19))
 =(2,8,22,54,126,308,660,1538,3350,7368).
```
These are consistency checks against the initial data in [\[6\]](#ref-StanleyMO); the asymptotic proof does not depend on finite computation. In converting counts to fractions, the degree is $`2b+2`$, one more than $`\max S`$.

The theorem determines an average, with no claimed concentration rate or second-order expansion. Natural next questions are fluctuations of $`U_b`$, a quantitative error term uniform up to the endpoint regions, and the interaction between the noncyclotomic unit-circle zeros and irreducibility. The number of entirely cyclotomic members of $`\mathcal S_b`$ is a separate arithmetic enumeration problem. The reductions above identify a tractable random-function representation without settling that classification.

## References

<a id="ref-CFI"></a>

**\[1\]** J. B. Conrey, D. W. Farmer, and Ö. İmamoğlu, *Palindromic random trigonometric polynomials*, Proc. Amer. Math. Soc. 137 (2009), 1835–1839. [arXiv:0812.1752](https://arxiv.org/abs/0812.1752).

<a id="ref-EK"></a>

**\[2\]** A. Edelman and E. Kostlan, *How many zeros of a random polynomial are real?*, Bull. Amer. Math. Soc. 32 (1995), 1–37. [arXiv:math/9501224](https://arxiv.org/abs/math/9501224).

<a id="ref-NV"></a>

**\[3\]** O. Nguyen and V. Vu, *Roots of random functions: A framework for local universality*, Amer. J. Math. 144 (2022), 1–74. [arXiv:1711.03615](https://arxiv.org/abs/1711.03615).

<a id="ref-Sound"></a>

**\[4\]** K. Soundararajan, *Equidistribution of zeros of polynomials*, Amer. Math. Monthly 126 (2019), 226–236. [doi:10.1080/00029890.2019.1546078](https://doi.org/10.1080/00029890.2019.1546078).

<a id="ref-StanleyECA"></a>

**\[5\]** R. P. Stanley, *Some enumerative applications of cyclotomic polynomials*, Enumer. Comb. Appl. 6:1 (2026), Article S2R4. [doi:10.54550/ECA2026V6S1R4](https://doi.org/10.54550/ECA2026V6S1R4).

<a id="ref-StanleyMO"></a>

**\[6\]** R. Stanley, *Polynomials with many zeros of absolute value 1*, MathOverflow question 461829, January 8, 2024; Addendum 2, January 29, 2024. [mathoverflow.net/questions/461829](https://mathoverflow.net/questions/461829/).
