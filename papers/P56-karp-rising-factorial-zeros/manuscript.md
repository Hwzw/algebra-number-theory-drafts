# Negative real zeros of a rising-factorial transform

Henry Zweiman

September 22, 2026

Research preprint, version 1.0. Prepared with OpenAI Codex; not peer reviewed. No independent human verification or priority determination is claimed.

## Abstract

We prove that a palindromic polynomial with positive constant term and only negative real zeros is carried, by a particular difference of rising-factorial transforms, either to zero or to a polynomial of degree two less with only negative real zeros. The proof factors the reciprocal root pairs, differentiates the resulting gamma polynomial, and applies an elementary interlacing lemma for a factorial basis. This yields the coefficient-pairing assertion for every polynomial of degree greater than two with only negative real roots. An additional Hadamard product with a binomial polynomial yields the positive-endpoint formulation of Karp's 2012 Conjecture 3. If zero endpoints are allowed in a finite Polya frequency sequence, the corresponding limit statement has nonpositive zeros, and we give an explicit example showing why strict negativity requires qualification.

## 1. Statements and scope

Throughout, $(x)_0=1$ and

$$
(x)_k=x(x+1)\cdots(x+k-1)\qquad(k\ge1)
$$

are rising factorials. A nonzero constant polynomial is regarded as having no zeros. The zero polynomial is treated separately. All polynomials below have real coefficients, and zeros are counted with multiplicity.

**Theorem 1 (coefficient pairing).** Let $n\ge3$ and let

$$
p(z)=\sum_{k=0}^n a_kz^k
$$

have degree $n$ and only strictly negative real zeros. Then

$$
P_n(x)=\sum_{k=0}^n a_ka_{n-k}
\bigl[(x)_k(x)_{n-k}-(x+1)_k(x-1)_{n-k}\bigr]
\tag{1}
$$

has degree $n-2$ and only strictly negative real zeros.

Karp [K12, Conjecture 3 and equation (7)] considers

$$
\begin{aligned}
\mathcal K_n[f](x)&:=Q_n^{1,1}(x-1)\\
&=\sum_{k=0}^n\binom nk f_kf_{n-k}
\bigl[(x)_k(x)_{n-k}-(x+1)_k(x-1)_{n-k}\bigr].
\end{aligned}
\tag{2}
$$

A finite sequence is $PF_\infty$ when its associated Toeplitz matrix has all minors nonnegative. By the Aissen--Schoenberg--Whitney theorem [ASW52], this is equivalent to its nonzero generating polynomial having nonnegative coefficients and only real nonpositive zeros.

**Theorem 2 (positive-endpoint form of Karp's Conjecture 3).** Let $n\ge3$ and let $(f_0,\ldots,f_n)$ be $PF_\infty$ with $f_0f_n>0$. Then $\mathcal K_n[f]$ has degree $n-2$ and only strictly negative real zeros.

The condition $f_0f_n>0$ makes the scope explicit: the input has degree exactly $n$ and no zero at the origin. Section 6 treats sequences with zero endpoints. No assertion of historical priority is needed for either theorem; the implication for Karp's formulation is proved in Section 5.

## 2. A factorial-transform lemma

For $d\ge0$, $\alpha>0$, and $h(t)=\sum_{r=0}^d h_rt^r$, define

$$
T_{d,\alpha}h(x)=\sum_{r=0}^d h_r(x)_r(x+r+\alpha)_{d-r}.
\tag{3}
$$

**Lemma 3.** Suppose $h$ is nonzero, has nonnegative coefficients, $h_0>0$, and has only strictly negative real zeros, with $\deg h\le d$. Then $T_{d,\alpha}h$ has degree $d$ and only strictly negative real zeros. Its consecutive zeros are separated by at least one.

**Proof.** Normalize $h_0=1$; this changes neither set of zeros. Factor

$$
h(t)=\prod_{j=1}^d(1+\mu_jt),\qquad \mu_j\ge0,
$$

padding with zero values of $\mu_j$ if $\deg h<d$. Put $h_i(t)=\prod_{j=1}^i(1+\mu_jt)$ and $Q_i=T_{i,\alpha}h_i$. Then $Q_0=1$ and

$$
Q_i(x)=(x+\alpha+i-1)Q_{i-1}(x)
       +\mu_i xQ_{i-1}(x+1).
\tag{4}
$$

Indeed, for the basis elements $B_{d,r}(x)=(x)_r(x+r+\alpha)_{d-r}$,

$$
B_{d+1,r}(x)=(x+\alpha+d)B_{d,r}(x),\qquad
B_{d+1,r+1}(x)=xB_{d,r}(x+1),
$$

which gives (4) by multiplying $h_{i-1}$ by $1+\mu_it$.

Assume first that all $\mu_j>0$. We prove by induction that $Q_i$ has $i$ simple zeros in $(-\alpha-i+1,0)$, with consecutive zeros separated by more than one. For $i=1$,

$$
Q_1(x)=(1+\mu_1)x+\alpha,
$$

so the assertion holds. Suppose it holds for $i-1$, with zeros $r_1<\cdots<r_{i-1}$. The two polynomials

$$
A(x)=(x+\alpha+i-1)Q_{i-1}(x),\qquad
B(x)=xQ_{i-1}(x+1)
$$

have positive leading coefficients, and their zeros alternate as follows:

$$
-\alpha-i+1<r_1-1<r_1<r_2-1<\cdots
<r_{i-1}-1<r_{i-1}<0.
\tag{5}
$$

The first inequality follows from $r_1>-\alpha-i+2$; the others follow from the induction hypothesis. Write $\xi_1=-\alpha-i+1$, $\xi_j=r_{j-1}$ for $2\le j\le i$, $\eta_j=r_j-1$ for $1\le j<i$, and $\eta_i=0$. Thus $\xi_1<\eta_1<\cdots<\xi_i<\eta_i$, where the $\xi_j$ are the roots of $A$ and the $\eta_j$ the roots of $B$.

At $\xi_j$, the sign of $A+\mu_iB$ is $(-1)^{i-j+1}$, because $i-j+1$ roots of $B$ lie to its right. At $\eta_j$, its sign is $(-1)^{i-j}$, because $i-j$ roots of $A$ lie to its right. Consequently $Q_i=A+\mu_iB$ has a root in each of the $i$ intervals $(\xi_j,\eta_j)$. Its degree is $i$, so these are all its roots. If they are $s_1<\cdots<s_i$, then

$$
s_j<r_j-1<r_j<s_{j+1}\qquad(1\le j<i).
$$

Hence $s_{j+1}-s_j>1$, and the induction is complete.

For general $\mu_j\ge0$, replace them by $\mu_j+\delta$ and let $\delta\downarrow0$. The leading coefficient of (3) is $\sum_r h_r=h(1)>0$, so the degree remains $d$ in the limit. Continuity of roots gives real nonpositive zeros and spacing at least one. Finally,

$$
T_{d,\alpha}h(0)=h_0(\alpha)_d>0,
$$

so none of those zeros is zero. This proves the lemma. $\square$

## 3. Palindromic polynomials and the difference transform

For a coefficient vector $c=(c_0,\ldots,c_n)$ define

$$
\mathcal D_n[c](x)=\sum_{k=0}^n c_k
\bigl[(x)_k(x)_{n-k}-(x+1)_k(x-1)_{n-k}\bigr].
\tag{6}
$$

**Theorem 4.** Let $n\ge2$ and let $C(z)=\sum_{k=0}^n c_kz^k$ have degree $n$, positive constant term, only strictly negative real zeros, and $c_k=c_{n-k}$. If $C(z)=c_0(1+z)^n$, then $\mathcal D_n[c]\equiv0$. Otherwise $\mathcal D_n[c]$ has degree $n-2$ and only strictly negative real zeros.

**Proof.** Write $n=2m+\varepsilon$, where $\varepsilon\in\{0,1\}$. Reciprocal symmetry pairs every root with its reciprocal. A pair $-r,-r^{-1}$, $r>0$, contributes

$$
(z+r)(z+r^{-1})=(1+z)^2+\lambda z,
\qquad \lambda=r+r^{-1}-2\ge0.
$$

Any roots at $-1$ can be paired except for one when $n$ is odd. It follows that

$$
\begin{aligned}
C(z)&=c_0(1+z)^\varepsilon
\prod_{i=1}^m\bigl((1+z)^2+\lambda_i z\bigr)\\
&=c_0\sum_{j=0}^m\gamma_jz^j(1+z)^{n-2j},
\end{aligned}
\tag{7}
$$

where

$$
\Gamma(t):=\sum_{j=0}^m\gamma_jt^j
=\prod_{i=1}^m(1+\lambda_it).
\tag{8}
$$

Define $F_C(x,y)=\sum_{k=0}^n c_k(x)_k(y)_{n-k}$. For each summand in (7), the rising-factorial Vandermonde identity gives

$$
\begin{aligned}
&\sum_{\ell=0}^{n-2j}\binom{n-2j}{\ell}
(x)_{j+\ell}(y)_{n-j-\ell}\\
&\quad=(x)_j(y)_j
\sum_{\ell=0}^{n-2j}\binom{n-2j}{\ell}
(x+j)_\ell(y+j)_{n-2j-\ell}\\
&\quad=(x)_j(y)_j(x+y+2j)_{n-2j}.
\end{aligned}
$$

Therefore

$$
F_C(x,y)=c_0\sum_{j=0}^m\gamma_j
(x)_j(y)_j(x+y+2j)_{n-2j}.
\tag{9}
$$

For $j\ge1$ we have the polynomial identity

$$
\begin{aligned}
&(x)_j^2-(x+1)_j(x-1)_j\\
&\quad=(x)_{j-1}(x+1)_{j-1}
\bigl[x(x+j-1)-(x-1)(x+j)\bigr]\\
&\quad=j(x)_{j-1}(x+1)_{j-1}.
\end{aligned}
\tag{10}
$$

Taking $F_C(x,x)-F_C(x+1,x-1)$ in (9) cancels the $j=0$ term and yields

$$
\mathcal D_n[c](x)=c_0\sum_{j=1}^m
j\gamma_j(x)_{j-1}(x+1)_{j-1}(2x+2j)_{n-2j}.
\tag{11}
$$

Now split the last factor using

$$
(2u)_{2v}=4^v(u)_v(u+\tfrac12)_v,
\qquad
(2u)_{2v+1}=2\cdot4^v(u)_{v+1}(u+\tfrac12)_v.
$$

Since

$$
(x+1)_{j-1}(x+j)_{m-j+\varepsilon}
=(x+1)_{m-1+\varepsilon},
$$

we obtain

$$
\mathcal D_n[c](x)=2^\varepsilon c_0
(x+1)_{m-1+\varepsilon}R(x),
\tag{12}
$$

where

$$
R(x)=\sum_{r=0}^{m-1}(r+1)\gamma_{r+1}4^{m-1-r}
(x)_r(x+r+\tfrac32)_{m-1-r}.
\tag{13}
$$

If all $\lambda_i=0$, then $\Gamma=1$ and (11) vanishes. Otherwise $\Gamma$ is nonconstant, $\Gamma'(0)=\sum_i\lambda_i>0$, and Rolle's theorem implies that $\Gamma'$ has only strictly negative real zeros (or is a positive constant). Set

$$
h(t)=4^{m-1}\Gamma'(t/4).
\tag{14}
$$

This polynomial has nonnegative coefficients, positive constant term, and degree at most $m-1$. Equation (13) is exactly

$$
R=T_{m-1,\,3/2}h.
$$

Lemma 3 shows that $R$ has degree $m-1$ and only strictly negative real zeros. The factor $(x+1)_{m-1+\varepsilon}$ has the same zero property. Their degrees add to $2m-2+\varepsilon=n-2$, proving the theorem. $\square$

In particular, (12) displays the fixed negative integer roots. The remaining factor has simple negative zeros separated by at least one. This does not assert that all roots of the full product are distinct: a root of $R$ may coincide with one of the fixed integer roots.

## 4. Proof of the coefficient-pairing theorem

We use the classical Hadamard-product theorem: if two real polynomials have nonnegative coefficients and only real nonpositive zeros, then their nonzero coefficientwise product also has only real nonpositive zeros. This is the consequence of Malo's theorem recalled in [GW96, p. 798]; see also [GW96, Theorem 4(a)]. A positive constant term excludes a zero at the origin.

Replace $p$ by $-p$ if necessary so that its coefficients are positive. Its reciprocal

$$
p^*(z)=z^np(1/z)=\sum_{k=0}^n a_{n-k}z^k
$$

also has only negative real zeros. Thus

$$
C(z)=p\odot p^*(z)=\sum_{k=0}^n a_ka_{n-k}z^k
$$

has only negative real zeros and is palindromic, where $\odot$ means coefficientwise product.

It remains to exclude $C=c_0(1+z)^n$. Write $p(z)=a_n\prod_{i=1}^n(z+s_i)$ with $s_i>0$. Cauchy--Schwarz gives

$$
\frac{c_1}{c_0}
=\frac{a_1a_{n-1}}{a_0a_n}
=\left(\sum_{i=1}^n s_i\right)
 \left(\sum_{i=1}^n s_i^{-1}\right)
\ge n^2>n.
\tag{15}
$$

But the corresponding ratio for $c_0(1+z)^n$ is $n$. The nonzero case of Theorem 4 applies, proving Theorem 1. $\square$

For completeness, the formula gives $P_0=P_1=0$ and $P_2=a_1^2-2a_0a_2>0$. The assertion for $n\ge3$ therefore concerns a nonconstant polynomial throughout.

## 5. The binomial factor in Karp's conjecture

Let $F(z)=\sum_{k=0}^n f_kz^k$ satisfy the hypotheses of Theorem 2. By [ASW52], $F$ has only strictly negative real zeros. Define

$$
C_K(z)=\sum_{k=0}^n\binom nk f_kf_{n-k}z^k.
$$

The extra binomial factor is handled by a third polynomial in the Hadamard product:

$$
C_K=F\odot\bigl(z^nF(1/z)\bigr)\odot(1+z)^n.
\tag{16}
$$

Applying the Hadamard-product theorem twice proves that $C_K$ has only strictly negative real zeros. It is palindromic, has degree $n$, and has constant term $f_0f_n>0$. Applying (15) to $F$ gives

$$
\frac{[z]C_K(z)}{C_K(0)}
=n\frac{f_1f_{n-1}}{f_0f_n}\ge n^3>n.
$$

Hence $C_K\ne C_K(0)(1+z)^n$. Theorem 4, applied to the coefficients of $C_K$, proves that (2) has degree $n-2$ and only strictly negative real zeros. This proves Theorem 2. $\square$

Equation (16) is essential to the comparison: the original coefficient-pairing formula (1) and Karp's formula (2) differ by $\binom nk$. No identification of their coefficient sequences without this extra step is being made. The result establishes the conjectured conclusion when both endpoints are positive; the distinction between negative and nonpositive roots at zero endpoints is addressed next.

## 6. Zero endpoints

**Proposition 5.** Let $n\ge3$. If $(f_0,\ldots,f_n)$ is a nonzero finite $PF_\infty$ sequence, allowing zero endpoints, then $\mathcal K_n[f]$ is either zero or has only real nonpositive zeros.

**Proof.** Factor its generating polynomial as

$$
F(z)=A z^s\prod_{i=1}^{D-s}(z+u_i),
\qquad A>0,\quad u_i>0,\quad D\le n.
$$

For $\delta>0$ set

$$
F_\delta(z)=A(z+\delta)^s
\prod_{i=1}^{D-s}(z+u_i)(1+\delta z)^{n-D}.
$$

Each $F_\delta$ has degree $n$, positive endpoints, and only strictly negative real zeros. Its coefficients converge to those of $F$, padded through degree $n$. Theorem 2 applies to $\mathcal K_n[F_\delta]$, whose coefficients converge to those of $\mathcal K_n[f]$. A nonzero coefficientwise limit of polynomials of bounded degree with all zeros in $(-\infty,0]$ again has all zeros in that closed set. This follows, for example, by continuity of zeros near any finite zero of the nonzero limit. The proposition follows. $\square$

Strict negativity need not survive. Take $n=4$ and

$$
(f_0,f_1,f_2,f_3,f_4)=(1,2,1,0,0),
\qquad F(z)=(1+z)^2.
$$

This is a $PF_\infty$ sequence, but only $k=2$ contributes to (2), so

$$
\mathcal K_4[f](x)
=6\bigl[(x)_2^2-(x+1)_2(x-1)_2\bigr]
=12x(x+1).
$$

If degree exactly $n$ is required but a zero constant coefficient is allowed, $(0,0,1,2,1)$ gives the same example. Thus the positive-endpoint hypothesis in Theorem 2 is substantive for the stated strict conclusion. Karp's use of finite $PF_\infty$ sequences should be read with its endpoint convention made explicit; no counterexample to the positive-endpoint form is asserted here.

## 7. Verification and provenance

The proof uses the classical Hadamard-product theorem and, for the $PF_\infty$ formulation, the Aissen--Schoenberg--Whitney characterization. The factorial-transform lemma, reciprocal-pair reduction, and algebraic identities are proved in this manuscript. The supplementary SymPy script checks the identities, transform recurrence, sample outputs with exact real-root counts, and the zero-endpoint example. Those finite checks are supporting evidence and do not replace the proof for arbitrary degree.

This manuscript was prepared with OpenAI Codex from the author's problem statement and publication instructions. The drafting assistant also performed the algebraic audit. An off-by-one endpoint in an earlier conversational version of the interlacing argument has been corrected: the leftmost root in (5) is exactly $-\alpha-i+1$. No independent human review, journal acceptance, or exhaustive literature determination is claimed.

## References

[ASW52] M. Aissen, I. J. Schoenberg, and A. M. Whitney. On the generating functions of totally positive sequences I. *Journal d'Analyse Mathematique* **2** (1952), 93-103.

[GW96] J. Garloff and D. G. Wagner. Hadamard products of stable polynomials are stable. *Journal of Mathematical Analysis and Applications* **202** (1996), 797-809. The classical real-rooted Hadamard-product result is recalled on p. 798 and strengthened in Theorem 4(a). [Author-hosted article](https://www-home.htwg-konstanz.de/~garloff/Garloff_Wagner_Hadamard_Products.pdf).

[K12] D. Karp. Positivity of Toeplitz determinants formed by rising factorial series and properties of related polynomials. *Zap. Nauchn. Sem. POMI* **404** (2012), 184-198; English translation, *Journal of Mathematical Sciences* **193** (2013), 106-114. [arXiv:1203.1482](https://arxiv.org/abs/1203.1482), Conjecture 3 and equation (7). [Journal DOI](https://doi.org/10.1007/s10958-013-1438-y).
