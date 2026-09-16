# Local minimality for the generalized Neumann Hénon problem

Henry Zweiman

September 15, 2026

## Abstract

We prove strict local minimality, modulo scaling, of radial minimizers for the generalized Neumann Hénon quotient when the exponent of the radial weight is large. The parameter range is determined by the first nonlinear Steklov eigenvalue. It contains a right neighborhood of the homogeneity exponent for every $2<p<n$, and the entire subcritical range when $n\ge4$ and $p>2$ is sufficiently close to $2$. This settles the local-minimality question left open after the second-variation analysis of Nazarov and Shcheglova. The proof combines a common weighted space, compact boundary traces, and a nonlinear coercivity lemma that retains the energy of concentrating perturbations. We also give an analytic proof that the admissible interval is nonempty. Above the Steklov threshold, a first angular mode yields instability; the threshold itself is not decided. We also determine the size of the local-minimum neighborhood under unit energy normalization: it is uniform up to and including the critical trace exponent, and above that exponent it shrinks at an explicitly determined sharp power of the concentration parameter.

## 1. Introduction and main result

Let $B$ be the unit ball in $\mathbb R^n$, let $\Sigma=\partial B$, and write $S=|\Sigma|$. All function spaces are real. For

$$
n\ge3,\qquad 2<p<n,\qquad p<q<p^*:=\frac{np}{n-p},
$$

consider

$$
\mathcal Q_\alpha(u)=
\frac{\displaystyle\int_B(|\nabla u|^p+|u|^p)\,dx}
{\displaystyle\left(\int_B |x|^\alpha|u|^q\,dx\right)^{p/q}},
\qquad u\in W^{1,p}(B)\setminus\{0\},\quad\alpha>0.
\tag{1}
$$

A positive critical point, after multiplication by a constant, solves

$$
-\Delta_p u+u^{p-1}=|x|^\alpha u^{q-1}\quad\text{in }B,
\qquad \partial_\nu u=0\quad\text{on }\Sigma.
\tag{2}
$$

We study positive minimizers of (1) among radial functions. Their existence and limiting profile are established in [Sh18]. The issue is whether these radial minimizers also minimize locally against arbitrary, possibly nonradial, perturbations.

Define the first nonlinear Steklov eigenvalue

$$
\lambda=\inf_{\substack{u\in W^{1,p}(B)\\ \int_\Sigma|u|^p>0}}
\frac{\int_B(|\nabla u|^p+|u|^p)}{\int_\Sigma|u|^p}.
\tag{3}
$$

Its positive eigenfunction $\phi$ is radial and unique up to scaling. We use the normalization

$$
\int_B(|\nabla\phi|^p+\phi^p)=1,
\qquad S\lambda\phi(1)^p=1.
\tag{4}
$$

Set

$$
q_c(n,p)=1+\lambda^{-p/(p-1)}\bigl(1-(n-1)\lambda\bigr).
\tag{5}
$$

**Theorem 1.1.** If $p<q<\min\{p^*,q_c(n,p)\}$, there is $\alpha_0$ such that, for every $\alpha\ge\alpha_0$, each positive radial minimizer $v_\alpha$ of (1) is a strict $W^{1,p}(B)$ local minimizer modulo its positive scalar ray. More precisely, there is a neighborhood $U$ of $v_\alpha$ such that

$$
\mathcal Q_\alpha(u)>\mathcal Q_\alpha(v_\alpha)
\quad\text{for }u\in U\setminus\{t v_\alpha:t>0\}.
\tag{6}
$$

If $q_c(n,p)<q<p^*$, every such radial minimizer has a negative nonradial second-variation direction for all sufficiently large $\alpha$.

The threshold and its angular origin already occur in [NS26, Lemma 1 and equation (25)]. The advance in the positive range is the passage from directional second-variation positivity to a local minimum in the full Sobolev topology. The negative-range assertion is the corresponding angular test, included to identify the scope of the result. We make no assertion when $q=q_c$.

**Corollary 1.2.** For every $n\ge3$ and $2<p<n$, one has $q_c(n,p)>p$. For every $n\ge4$, there exists $p_0(n)>2$ such that $q_c(n,p)>p^*$ whenever $2<p<p_0(n)$. Thus Theorem 1.1 applies to every subcritical $q>p$ in the latter range.

The local-minimum property need not be global. In the interval $p(n-1)/(n-p)<q<p^*$, the global minimizer is nonradial for large $\alpha$ [Sh18, Theorem 3.1]. In dimensions at least four and for $p$ close to two, this gives radial strict local minima coexisting with lower nonradial states.

For $p=2$, local minimality was proved by Gazzini and Serra [GS08, Proposition 3.6 and Theorem 3.8]. Nazarov and Shcheglova [NS26] obtain directional positivity for $p>2$ and explicitly leave local minimality open in the introduction. Their latest listed arXiv version on September 15, 2026 is v2, dated May 11, 2026. Our proof uses the radial convergence from [Sh18], but does not infer Sobolev coercivity from directional positivity.

Weighted completions and compact embeddings are established tools in the spectral theory of linearized $p$-Laplace operators [CES11]. The local Morse theory surveyed in [Ci13], and the critical-group estimates in [CDS24], address the substantial difference between Hilbert and Sobolev Banach spaces. The latter work treats Dirichlet problems and compactness for varying regularized solutions. Here a common space controls a degeneracy at the center and a degeneracy at the Neumann boundary. Its compact trace transfers the concentrating potential to a Steklov form. A separate convexity argument then controls perturbations whose gradients concentrate near the degenerate set. The non-degeneracy theorem of Asselle, Cingolani, and Starostka [ACS25] assumes a positive regularization parameter in its PDE application. Its abstract criterion requires a nearby directional Hessian estimate, which is not supplied by positivity at the critical point. We claim neither the introduction of weighted spectral spaces nor a general Morse theory.

## 2. From a weighted gap to a local minimum

This section isolates the nonlinear argument. For a bounded smooth domain $\Omega\subset\mathbb R^n$, use the norm

$$
\|h\|_{1,p}^p=\int_\Omega(|\nabla h|^p+|h|^p).
$$

**Lemma 2.1 (nonlinear coercivity).** Suppose $2<p<q<p^*$, $0\le b\in L^\infty(\Omega)$, and $b\not\equiv0$. Let $v\in C^1(\overline\Omega)$ be a positive critical point of

$$
\frac{pF(u)}{D(u)^{p/q}},\qquad
F(u)=\frac1p\|u\|_{1,p}^p,\qquad D(u)=\int_\Omega b|u|^q,
$$

normalized by $D(v)=1$. Assume $\inf_\Omega v>0$. Put $\Lambda=pF(v)$,

$$
\ell(h)=\int_\Omega bv^{q-1}h,
\qquad a=|\nabla v|^{p-2},
$$

and define the Hessian form

$$
A(h)=\int_\Omega\left[
 a|\nabla h|^2+(p-2)|\nabla v|^{p-4}(\nabla v\cdot\nabla h)^2
 +(p-1)v^{p-2}h^2\right].
\tag{7}
$$

The middle integrand is zero where $\nabla v=0$. Suppose that $a>0$ almost everywhere, $a^{-1}\in L^1(\Omega)$, and the completion $H$ of $C^\infty(\overline\Omega)$ in the norm $A^{1/2}$ embeds compactly into $L^2(\Omega)$. If, for some $\kappa>0$,

$$
A(h)-\Lambda(q-1)\int_\Omega bv^{q-2}h^2\ge\kappa A(h)
\quad(h\in H,\ \ell(h)=0),
\tag{8}
$$

then there exist $c,\rho>0$ such that

$$
F(v+h)-F(v)D(v+h)^{p/q}
\ge c\bigl(A(h)+\|h\|_{1,p}^p\bigr)
\tag{9}
$$

whenever $h\in W^{1,p}(\Omega)$, $\ell(h)=0$, and $\|h\|_{1,p}<\rho$.

*Proof.* Boundedness of $v$ and $\nabla v$ gives a continuous inclusion $W^{1,p}\subset H$. The reciprocal-weight assumption identifies the weighted gradients as distributional gradients: weighted Cauchy--Schwarz bounds their $L^1$ norm. The value term in (7) controls $L^2$.

Consider any sequence of nonzero tangent perturbations $h_j$ with $\varepsilon_j=\|h_j\|_{1,p}\to0$. Write $A(h,k)$ for the polarization of $A$, and set

$$
t_j^2=A(h_j)+\varepsilon_j^p,\qquad z_j=h_j/t_j.
\tag{10}
$$

Then $\varepsilon_j^{p/2}\le t_j\le C\varepsilon_j$. On a subsequence,

$$
\begin{gathered}
z_j\rightharpoonup z\text{ in }H,\qquad z_j\to z\text{ in }L^2,\qquad\ell(z)=0,\\
A(z_j)\to a_0,\qquad \varepsilon_j^p/t_j^2\to b_0,\qquad
 a_0+b_0=1,\quad A(z)\le a_0.
\end{gathered}
\tag{11}
$$

Let $\mathcal B_F(u,v)=F(u)-F(v)-F'(v)[u-v]$. We first prove

$$
\liminf_j\frac{\mathcal B_F(v+h_j,v)}{t_j^2}
\ge\frac12 A(z)+c_p(1-A(z))
\tag{12}
$$

with $c_p>0$. The second term accounts for energy lost in the weak limit.

Fix $w\in C^\infty(\overline\Omega)$ and put $k_j=h_j-t_jw$. The exact identity

$$
\begin{aligned}
\mathcal B_F(v+h_j,v)
={}&\mathcal B_F(v+t_jw,v)\\
&+(F'(v+t_jw)-F'(v))[k_j]\\
&+\mathcal B_F(v+t_jw+k_j,v+t_jw)
\end{aligned}
\tag{13}
$$

gives the appropriate expansion. Dividing by $t_j^2$, the first term tends to $A(w)/2$, and the second tends to $A(w,z-w)$. To justify the latter assertion in $H^*$, the difference quotient of $|X|^{p-2}X$ at $X=\nabla v$ in the fixed direction $\nabla w$ is bounded by $C_w(a+1)$ for $0<t\le1$. Its square divided by $a$ is bounded by

$$
C_w(a+2+a^{-1})\in L^1(\Omega).
$$

The pointwise derivative is the matrix in (7). Dominated convergence gives the derivative expansion in the weighted dual norm. The value term is simpler because $v$ is bounded away from zero.

For $f_p(X)=|X|^p/p$, uniform convexity gives

$$
f_p(X+Y)-f_p(X)-Df_p(X)Y
\ge c_p\bigl(|X|^{p-2}|Y|^2+|Y|^p\bigr).
\tag{14}
$$

For completeness, when $|Y|\le|X|/2$, the integral Hessian formula supplies the quadratic bound and absorbs $|Y|^p$. After scaling to $|Y|=1$, strict convexity and compactness supply a positive minimum when $|X|\le2$. These two regions cover all pairs. The constant depends only on $p$.

Apply (14) to both gradient and value terms in the last line of (13). Since

$$
|X|^{p-2}\le C_p\bigl(|X+tW|^{p-2}+t^{p-2}|W|^{p-2}\bigr),
$$

we may replace its shifted quadratic weights by those at $v$, at a fixed multiplicative cost and an error at most

$$
C_wt_j^{p-2}(\varepsilon_j+t_j)^2.
$$

After division by $t_j^2$, this is $o(1)$. Indeed it is bounded by $C_w\varepsilon_j^{p-2}$ if $p\ge4$, and by $C_w\varepsilon_j^{(p-2)^2/2}$ if $2<p<4$, using the two bounds following (10). The anisotropic Hessian (7) is comparable, with constants depending only on $p$, to its isotropic weighted part. Moreover,

$$
\frac{\bigl|\|k_j\|_{1,p}^p-\varepsilon_j^p\bigr|}{t_j^2}
\le C_w\left(\frac{\varepsilon_j^{p-1}}{t_j}+t_j^{p-2}\right)\longrightarrow0.
\tag{15}
$$

Consequently the lower limit of the last line of (13), divided by $t_j^2$, is at least

$$
c_p\bigl(a_0-2A(z,w)+A(w)+b_0\bigr).
$$

Combine the three terms, then let smooth $w$ converge to $z$ in $H$. This proves (12). The order of these limits is fixed: first $j\to\infty$ for each smooth $w$, then approximation in $H$.

We next expand the constraint. For any $\eta>0$, uniform positive upper and lower bounds on $v$ imply

$$
\left||v+s|^q-v^q-qv^{q-1}s-\frac{q(q-1)}2v^{q-2}s^2\right|
\le\eta s^2+C_\eta|s|^q.
\tag{16}
$$

This follows from Taylor expansion for small $s$ and the $q$-power bound away from zero. Sobolev embedding and (10) give

$$
\frac{\|h_j\|_q^q}{t_j^2}\le C\varepsilon_j^{q-p}\longrightarrow0.
$$

Integrate (16) against $b$, use the tangent constraint, and let $\eta\downarrow0$. Strong $L^2$ convergence in (11) yields

$$
D(v+h_j)=1+\frac{q(q-1)}2\int_\Omega bv^{q-2}h_j^2+o(t_j^2).
\tag{17}
$$

Criticality gives $F'(v)[h_j]=\Lambda\ell(h_j)=0$. Expanding the scalar power in (17) and using (8), (12), we obtain

$$
\begin{aligned}
\liminf_j\frac{F(v+h_j)-F(v)D(v+h_j)^{p/q}}{t_j^2}
&\ge\frac12\left(A(z)-\Lambda(q-1)\int_\Omega bv^{q-2}z^2\right)
 +c_p(1-A(z))\\
&\ge\min\{\kappa/2,c_p\}>0.
\end{aligned}
\tag{18}
$$

A sequence contradicting (9), with the ratio there tending to zero, is therefore impossible. This proves the lemma. $\square$

The tangent slice suffices for local minimality of the quotient. For $u$ sufficiently close to $v$, set $\widetilde u=u/\ell(u)$. Since $\ell(v)=1$, this factor is positive and tends to one, while $\ell(\widetilde u-v)=0$. Homogeneity preserves the quotient, and (9) gives a strict increase unless $\widetilde u=v$.

## 3. Radial profiles and a common weight

Normalize radial minimizers by $\|v_\alpha\|_{1,p}=1$. The radial convergence theorem [Sh18, Theorem 2.2] gives

$$
v_\alpha\longrightarrow\phi\quad\text{in }C(\overline B)\text{ and }W^{1,p}(B).
\tag{19}
$$

These statements apply along every choice of positive normalized radial minimizers. They are $C^1$ up to the boundary. The Euler equation and its multiplier are

$$
-\Delta_pv_\alpha+v_\alpha^{p-1}
 =c_\alpha r^\alpha v_\alpha^{q-1},\qquad
c_\alpha=\left(\int_Br^\alpha v_\alpha^q\right)^{-1}.
\tag{20}
$$

The equation holds against all Sobolev tests, by radial averaging of an arbitrary test. Uniform convergence in (19), positivity of $\phi$, and concentration of $(\alpha+n)r^{\alpha+n-1}\,dr$ at $1$ imply

$$
0<c\le v_\alpha\le C,\qquad
\frac{c_\alpha}{\alpha+n}\longrightarrow\frac1{S\phi(1)^q}.
\tag{21}
$$

No boundary expansion is needed to obtain the weight estimates below.

**Lemma 3.1.** Set $\beta=(p-2)/(p-1)\in(0,1)$. Uniformly over large $\alpha$ and normalized radial minimizers,

$$
|v_\alpha'(r)|^{p-2}\asymp
r^\beta\min\{1,\alpha(1-r)\}^\beta,
\qquad0<r<1.
\tag{22}
$$

In particular $v_\alpha'>0$ in $(0,1)$.

*Proof.* Integrating (20) from either endpoint gives the two exact formulas

$$
\begin{aligned}
 r^{n-1}|v_\alpha'|^{p-2}v_\alpha'
 &=\int_0^rs^{n-1}v_\alpha^{p-1}\,ds
  -c_\alpha\int_0^rs^{\alpha+n-1}v_\alpha^{q-1}\,ds\\
 &=c_\alpha\int_r^1s^{\alpha+n-1}v_\alpha^{q-1}\,ds
  -\int_r^1s^{n-1}v_\alpha^{p-1}\,ds.
\end{aligned}
\tag{23}
$$

For fixed small $\delta>0$ and $r\le1-\delta$, the first formula is bounded above by $Cr^n$ and below by $cr^n-Cr^{\alpha+n}$. For large $\alpha$, it is therefore comparable to $r^n$.

On $1-\delta\le r<1$, the second formula is bounded below by

$$
c(1-r^{\alpha+n})-C(1-r).
$$

Here $1-r^{\alpha+n}\asymp\min\{1,\alpha(1-r)\}$. Choose $\delta$ small and then $\alpha$ large. The negative term can be absorbed, both when $\alpha(1-r)\le1$ and when it exceeds $1$. Dropping that term gives the matching upper bound. Divide by $r^{n-1}$ and raise to the power $\beta$. The two regions yield (22). $\square$

Define

$$
\omega(r)=r^\beta(1-r)^\beta,\qquad
E(h)=\int_B\bigl(\omega|\nabla h|^2+h^2\bigr),
\tag{24}
$$

and let $H_\omega$ be the completion of $C^\infty(\overline B)$ in this norm. If $a_\alpha=|v_\alpha'|^{p-2}$, then (22) gives

$$
c\omega\le a_\alpha\le C,\qquad a_\alpha\le C_\alpha\omega.
\tag{25}
$$

The first two constants are uniform for large $\alpha$; the last may depend on $\alpha$. Also $\omega^{-1}\in L^1(B)$. Formula (23) and (19) imply convergence of $v_\alpha'$ to $\phi'$ uniformly on every closed subinterval of $(0,1)$.

## 4. Compact traces and boundary concentration

**Lemma 4.1.** The maps $H_\omega\to L^2(B)$ and $T:H_\omega\to L^2(\Sigma)$ are compact, where $T$ extends the ordinary boundary trace of smooth functions. If $h_j\rightharpoonup h$ in $H_\omega$ and $\alpha_j\to\infty$, then

$$
(\alpha_j+n)\int_B r^{\alpha_j}v_{\alpha_j}^{q-2}h_j^2
\longrightarrow\phi(1)^{q-2}\int_\Sigma(Th)^2.
\tag{26}
$$

The corresponding linear limit is

$$
(\alpha_j+n)\int_B r^{\alpha_j}v_{\alpha_j}^{q-1}h_j
\longrightarrow\phi(1)^{q-1}\int_\Sigma Th.
\tag{27}
$$

*Proof.* On every annulus separated from $0$ and $1$, the norm $E^{1/2}$ controls the ordinary $H^1$ norm. For $1/2\le r<1$, radial Cauchy--Schwarz gives

$$
\|h(1,\cdot)-h(r,\cdot)\|_{L^2(\Sigma)}^2
\le C(1-r)^{1-\beta}E(h).
\tag{28}
$$

An average over a fixed interior annulus bounds the trace itself by $CE(h)^{1/2}$, so it extends by completion. Averages over an annulus at distance $\delta$ from $\Sigma$ are compact in $L^2(\Sigma)$ by interior Rellich compactness. By (28), they approximate the trace in operator norm with error $O(\delta^{(1-\beta)/2})$. Thus $T$ is compact. The same estimate gives

$$
\int_{1-\delta<|x|<1}h^2\le C\delta E(h).
\tag{29}
$$

At the center, comparison along rays with the interior trace at $r=1/2$ uses

$$
\int_r^{1/2}\frac{ds}{s^{n-1}\omega(s)}\le Cr^{2-n-\beta}.
$$

The interior trace is bounded by $CE(h)^{1/2}$. Integrating the ray estimate therefore gives

$$
\int_{|x|<\delta}h^2\le C(\delta^n+\delta^{2-\beta})E(h).
\tag{30}
$$

Equations (29), (30), and Rellich compactness on interior annuli prove compactness in $L^2(B)$.

For (26), first replace $h_j(r,\cdot)$ by $Th_j$ on $r\ge1/2$. Both have uniformly bounded $L^2(\Sigma)$ norm there. By (28) the error in their squared norms is at most $C(1-r)^{(1-\beta)/2}$. Its integral against the probability density $(\alpha_j+n)r^{\alpha_j+n-1}$ is $O(\alpha_j^{-(1-\beta)/2})$. The contribution from $r<1/2$ is exponentially small by the interior $L^2$ bound. Uniform convergence in (19) and continuity of $\phi$ replace $v_{\alpha_j}^{q-2}$ by $\phi(1)^{q-2}$, with an error tending to zero. Finally compactness gives $Th_j\to Th$ in $L^2(\Sigma)$. This proves (26). The same argument, without squaring $h_j$, proves (27). $\square$

## 5. The limiting angular inequality and the weighted gap

For a radial profile $v_\alpha$, write its Hessian energy as

$$
A_\alpha(h)=\int_B\left[
 a_\alpha\bigl((p-1)|\partial_rh|^2+r^{-2}|\nabla_\theta h|^2\bigr)
 +(p-1)v_\alpha^{p-2}h^2\right].
\tag{31}
$$

Let $A_\infty$ denote the same expression with $\phi$ in place of $v_\alpha$. In particular $A_\alpha\ge cE$, uniformly for large $\alpha$, and $A_\alpha$ is equivalent to $E$ for every fixed such $\alpha$.

**Lemma 5.1.** If $g$ has zero spherical average at almost every radius and finite $A_\infty$ energy, then

$$
A_\infty(g)\ge L\int_\Sigma(Tg)^2,
\qquad
L=\phi(1)^{p-2}\left[\lambda^{-1/(p-1)}-(n-1)\lambda^\beta\right].
\tag{32}
$$

*Proof.* This is the angular Steklov calculation in [NS26, Lemma 1]. We give a verification in the finite-energy class needed here. The radial equation is

$$
(r^{n-1}(\phi')^{p-1})'=r^{n-1}\phi^{p-1},
\qquad \phi'(1)=\lambda^{1/(p-1)}\phi(1).
\tag{33}
$$

Set $f=\phi'>0$. Differentiation on $(0,1)$ yields

$$
-\bigl((p-1)r^{n-1}(\phi')^{p-2}f'\bigr)'
+\left[(n-1)r^{n-3}(\phi')^{p-2}
 +(p-1)r^{n-1}\phi^{p-2}\right]f=0.
\tag{34}
$$

Apply the spherical Poincaré inequality with eigenvalue $n-1$, and complete the radial square with $g/f$ on an annulus. The resulting lower bound is the radial boundary expression

$$
\left[(p-1)r^{n-1}(\phi')^{p-2}\frac{f'}f
 \|g(r,\cdot)\|_{L^2(\Sigma)}^2\right]_{r=\varepsilon}^{r=1}.
\tag{35}
$$

Indeed the discarded term is the integral of $(p-1)r^{n-1}(\phi')^{p-2}f^2|\partial_r(g/f)|^2$.

At the origin, (33) implies $\phi'(r)\sim\phi(0)(r/n)^{1/(p-1)}$ and $f'/f\sim1/((p-1)r)$. Finite angular energy gives

$$
\int_0^{1/2}r^{n-3+\beta}\|g(r,\cdot)\|_2^2\,dr<\infty.
$$

Hence the lower boundary term in (35), of order $r^{n-2+\beta}\|g(r,\cdot)\|_2^2$, tends to zero along a sequence $r\downarrow0$. At $1$, (33) makes its coefficient equal to $L$. Apply the square identity first on interior annuli, then pass to the boundary trace and to that sequence at the center. Ordinary Sobolev approximation on annuli justifies the argument for finite-energy $g$. This proves (32). $\square$

Define the tangent functional and the constrained Hessian by

$$
\begin{aligned}
\ell_\alpha(h)&=\int_Br^\alpha v_\alpha^{q-1}h,\\
Q_\alpha(h)&=A_\alpha(h)
 -(q-1)c_\alpha\int_Br^\alpha v_\alpha^{q-2}h^2.
\end{aligned}
\tag{36}
$$

Both extend continuously to $H_\omega$ for each fixed $\alpha$.

**Proposition 5.2.** If $q<q_c(n,p)$, there exist $\delta>0$ and $\alpha_0$ such that

$$
Q_\alpha(h)\ge\delta E(h)
\quad\text{whenever }\alpha\ge\alpha_0,\ h\in H_\omega,\ \ell_\alpha(h)=0.
\tag{37}
$$

The constants apply to every positive normalized radial minimizer.

*Proof.* Otherwise choose $\alpha_j\to\infty$ and tangent $h_j$ with $E(h_j)=1$ and $Q_{\alpha_j}(h_j)\le1/j$. By weak compactness and Lemma 4.1, after a subsequence $h_j\rightharpoonup h$ in $H_\omega$, with strong convergence in both $L^2$ spaces. Since $A_{\alpha_j}(h_j)\ge c>0$, (21) and (26) imply

$$
\int_\Sigma(Th)^2>0.
\tag{38}
$$

The linear limit (27) and the tangent constraint give $\int_\Sigma Th=0$.

On each interior annulus the gradient coefficients converge uniformly and are uniformly positive. Weak lower semicontinuity there, exhaustion, and strong $L^2$ convergence for the value term give

$$
\begin{aligned}
0&\ge\liminf_j Q_{\alpha_j}(h_j)\\
 &\ge A_\infty(h)
 -(q-1)\lambda\phi(1)^{p-2}\int_\Sigma(Th)^2.
\end{aligned}
\tag{39}
$$

Here we used $1/(S\phi(1)^2)=\lambda\phi(1)^{p-2}$ from (4). The energy $A_\infty(h)$ is finite; otherwise (39) is already a contradiction.

Decompose $h=h_0+g$ into its radial average and a function of zero spherical average. The energy splits orthogonally. The trace of $h_0$ is zero, so $Tg=Th$. Discard $A_\infty(h_0)\ge0$ and apply (32). The last line of (39) is at least

$$
\lambda\phi(1)^{p-2}(q_c-q)\int_\Sigma(Th)^2>0,
$$

contradicting (38)--(39). $\square$

## 6. Proof of the main theorem and the parameter range

Fix $\alpha$ as in Proposition 5.2. By (25), (31), and (37), there is $\kappa_\alpha>0$ such that $Q_\alpha\ge\kappa_\alpha A_\alpha$ on $\ker\ell_\alpha$. Multiply $v_\alpha$ by a positive constant so that $\int_Br^\alpha v_\alpha^q=1$. Both the Hessian energy and its negative potential scale by the same power $p-2$, so the gap persists. The weighted completion is still $H_\omega$, with an equivalent norm. Its embedding into $L^2$ is compact. Equation (22) gives reciprocal-gradient-weight integrability, and (21) supplies strict positivity. Thus Lemma 2.1 applies with $b=r^\alpha$. Its coercivity and the scalar retraction following the lemma prove (6).

This application alone permits the neighborhood and nonlinear coercivity constant to depend on $\alpha$. Section 7 strengthens the argument to determine precisely when a uniform $W^{1,p}$ neighborhood exists and gives its sharp decay power otherwise.

For the negative-range assertion, let $Y$ be a first spherical harmonic and set $g(r,\theta)=\phi'(r)Y(\theta)$. Equality holds in (32). This function has finite $A_\infty$ energy, since its gradient energy near zero is of order

$$
\int_0^\varepsilon r^{n-1-\beta}\,dr<\infty.
$$

Cut it off smoothly for $r<\varepsilon$, using a cutoff equal to one for $r>2\varepsilon$. The cutoff error in $A_\infty$ is $O(\varepsilon^{n-\beta})$, and its boundary trace is unchanged. This produces smooth functions $g_\varepsilon$ on $\overline B$, each with zero spherical average. If $q>q_c$, choose $\varepsilon$ so small that

$$
A_\infty(g_\varepsilon)
 -(q-1)\lambda\phi(1)^{p-2}\int_\Sigma g_\varepsilon^2<0.
\tag{40}
$$

For this fixed smooth test, (21), (25), interior convergence of the gradient coefficients, and dominated convergence give $Q_\alpha(g_\varepsilon)<0$ for large $\alpha$. The test is tangent for every radial $v_\alpha$. Since the quotient is $C^2$ on $W^{1,p}\setminus\{0\}$ for the exponents under consideration, its second derivative in this direction is a positive multiple of $Q_\alpha(g_\varepsilon)$. Local minimality is impossible. This proves Theorem 1.1.

To prove Corollary 1.2, introduce

$$
z(r)=\left(\frac{\phi'(r)}{\phi(r)}\right)^{p-1}.
$$

Equation (33) gives

$$
z'=1-\frac{n-1}{r}z-(p-1)z^{p/(p-1)},\qquad
z(r)=r/n+o(r),\quad z'(r)\to1/n.
\tag{41}
$$

Differentiating for $r>0$ yields

$$
z''+\left(\frac{n-1}{r}+p z^{1/(p-1)}\right)z'
 =\frac{n-1}{r^2}z>0.
\tag{42}
$$

An integrating factor starting at a sufficiently small positive radius shows that $z'>0$ throughout $(0,1]$. Since $z(1)=\lambda$, (41) implies

$$
1-(n-1)\lambda-(p-1)\lambda^{p/(p-1)}>0,
$$

which is exactly $q_c>p$. This provides a direct analytic proof of the positivity underlying [NS26, Lemmas 6--7].

Also, integrating (33) and using strict increase of $\phi$ gives

$$
z(r)=\frac{r^{1-n}}{\phi(r)^{p-1}}
 \int_0^r s^{n-1}\phi(s)^{p-1}\,ds<\frac rn.
$$

Thus $\lambda<1/n$, and (5) implies

$$
q_c>1+n^{1/(p-1)}.
\tag{43}
$$

For $n\ge4$, one has $1+n>2n/(n-2)$. Continuity of the explicit functions in (43) and $p^*=np/(n-p)$ shows that $1+n^{1/(p-1)}>p^*$ for $p$ in a right neighborhood of $2$. This proves Corollary 1.2. $\square$

## 7. The size of the local-minimum neighborhood

We now determine whether the neighborhood in Theorem 1.1 can be uniform, using the energy normalization $\|v_\alpha\|_{1,p}=1$. Put

$$
p_\partial=\frac{p(n-1)}{n-p},\qquad
\vartheta=\left(\frac{n-p}{p}-\frac{n-1}{q}\right)_+,
\qquad \sigma=\frac{q\vartheta}{q-p}.
\tag{7.1}
$$

Here $x_+=\max\{x,0\}$. The exponent $p_\partial$ is the critical Sobolev trace exponent. For a positive normalized radial minimizer, define

$$
R_\alpha(v_\alpha)=\inf\left\{\|u-v_\alpha\|_{1,p}:
\|u\|_{1,p}=1,\ u\ne v_\alpha,
\ \mathcal Q_\alpha(u)\le\mathcal Q_\alpha(v_\alpha)\right\}.
\tag{7.2}
$$

The competitor set is nonempty since it contains $-v_\alpha$. This radius describes the neighborhood on the unit energy sphere, so the positive scaling degeneracy is removed.

**Theorem 7.1 (uniform neighborhoods and their sharp decay rate).** Fix $n\ge3$, $2<p<n$, and $p<q<\min\{p^*,q_c(n,p)\}$. There are constants $c,C>0$ and $\alpha_0$, depending only on $n,p,q$, such that every positive normalized radial minimizer satisfies

$$
R_\alpha(v_\alpha)\ge c\alpha^{-\sigma}
\qquad(\alpha\ge\alpha_0).
\tag{7.3}
$$

If $q>p_\partial$, there are positive normalized nonradial competitors of strictly smaller quotient at distance at most $C\alpha^{-\sigma}$. Consequently

$$
c\alpha^{-\sigma}\le R_\alpha(v_\alpha)
\le C\alpha^{-\sigma}\qquad(q>p_\partial).
\tag{7.4}
$$

In particular a uniform neighborhood exists when $q\le p_\partial$, including equality, and no uniform neighborhood exists when $q>p_\partial$ within the positive Steklov range. The theorem determines the power, not a limiting leading constant. It makes no assertion at $q=q_c$.

### 7.1. A weighted Sobolev estimate at the trace scale

For $p<q<p^*$ and $\alpha\ge1$,

$$
\alpha\int_Br^\alpha|h|^q\,dx
\le C\alpha^{q\vartheta}\|h\|_{1,p}^q.
\tag{7.5}
$$

Indeed the ordinary Sobolev trace inequality on $B_r$, uniformly under dilation for $1/2\le r\le1$, gives
$\|h(r,\cdot)\|_{L^{p_\partial}(\Sigma)}\le C\|h\|_{1,p}$ for almost every such $r$. Integration in $r$ gives
$\int_Br^\alpha|h|^{p_\partial}\le C\alpha^{-1}\|h\|_{1,p}^{p_\partial}$; on the inner half-ball use $r^\alpha\le2^{-\alpha}$ and ordinary Sobolev embedding. The same bound with exponent $q\le p_\partial$ follows by Hölder's inequality for the measure $r^\alpha dx$, whose mass is $S/(\alpha+n)$. For $p_\partial<q<p^*$, interpolate the preceding trace-scale estimate with
$\int_Br^\alpha|h|^{p^*}\le C\|h\|_{1,p}^{p^*}$.
The resulting power of $\alpha$ is $q(n-p)/p-(n-1)=q\vartheta$, proving (7.5).

Let

$$
\widehat D_\alpha(u)=c_\alpha\int_Br^\alpha|u|^q,
\qquad L_\alpha(h)=c_\alpha\int_Br^\alpha v_\alpha^{q-1}h.
\tag{7.6}
$$

Then $\widehat D_\alpha(v_\alpha)=L_\alpha(v_\alpha)=1$. Equations (21) and (7.5) imply

$$
c_\alpha\int_Br^\alpha|h|^q
\le C\alpha^{q\vartheta}\|h\|_{1,p}^q,
\qquad |L_\alpha(h)|\le C\|h\|_{1,p}.
\tag{7.7}
$$

The second estimate uses the trace-scale estimate and Hölder, with the uniform bound on $v_\alpha$. Its constant has no power of $\alpha$.

### 7.2. Uniform nonlinear coercivity at the scale in (7.1)

We strengthen the use of Lemma 2.1 by retaining the dependence of its constraint remainder on $\alpha$. There are $c_0,c_1>0$ and $\alpha_0$ such that

$$
F(v_\alpha+h)-\frac1p\widehat D_\alpha(v_\alpha+h)^{p/q}
\ge c_1\bigl(A_\alpha(h)+\|h\|_{1,p}^p\bigr)
\tag{7.8}
$$

whenever $\alpha\ge\alpha_0$, $L_\alpha(h)=0$, and
$\|h\|_{1,p}<c_0\alpha^{-\sigma}$. Here $F(u)=\|u\|_{1,p}^p/p$ and $A_\alpha$ is (31).

We prove the sequential assertion that implies these uniform constants. Suppose $\alpha_j\to\infty$ and $h_j\ne0$ are tangent perturbations such that

$$
\delta_j=\|h_j\|_{1,p},\qquad
\delta_j\alpha_j^\sigma\longrightarrow0.
\tag{7.9}
$$

Set $t_j^2=A_{\alpha_j}(h_j)+\delta_j^p$ and $z_j=h_j/t_j$. Uniform boundedness of $v_\alpha$ and its gradient, from (21)--(22), gives
$\delta_j^{p/2}\le t_j\le C\delta_j$. Also $A_{\alpha_j}\ge cE$, so $z_j$ is bounded in $H_\omega$. Passing to a subsequence gives weak convergence to $z$ there, strong $L^2(B)$ and trace convergence, and

$$
A_{\alpha_j}(z_j)\to a_0,\quad
\delta_j^p/t_j^2\to b_0,\quad a_0+b_0=1,
\quad A_\infty(z)\le a_0.
\tag{7.10}
$$

The last inequality follows from interior coefficient convergence, lower semicontinuity on annuli and exhaustion. Equation (27) and tangency give $\int_\Sigma Tz=0$.

The Bregman argument of Lemma 2.1, now with varying $v_{\alpha_j}$, gives

$$
\liminf_j\frac{\mathcal B_F(v_{\alpha_j}+h_j,v_{\alpha_j})}{t_j^2}
\ge\frac12 A_\infty(z)+c_p\bigl(1-A_\infty(z)\bigr).
\tag{7.11}
$$

We verify the uniformity needed for this passage. For fixed smooth $w$, use (13) with $v=v_{\alpha_j}$ and $k_j=h_j-t_jw$. We have
$a_{\alpha_j}^{-1}\le C\omega^{-1}$ and $a_{\alpha_j}\le C$. The square of the gradient difference quotient in the weighted dual norm is therefore dominated by $C_w(1+\omega^{-1})$, an integrable function independent of $j$. At every interior point other than the center, $\nabla v_{\alpha_j}\to\nabla\phi$. Dominated convergence proves the required derivative expansion. Moreover the coefficient convergence gives
$A_{\alpha_j}(w)\to A_\infty(w)$ and
$A_{\alpha_j}(w,z_j)\to A_\infty(w,z)$: the coefficient functionals converge in $H_\omega^*$, using the same dominating function. The errors in shifting the quadratic weight and replacing $\|k_j\|_{1,p}^p$ by $\delta_j^p$ are precisely those bounded in (15) and its preceding paragraph, with constants independent of $j$. Uniform convexity (14) thus yields

$$
\liminf_j\frac{\mathcal B_F(v_{\alpha_j}+h_j,v_{\alpha_j})}{t_j^2}
\ge A_\infty(w,z)-\tfrac12A_\infty(w)
+c_p\bigl(1-2A_\infty(w,z)+A_\infty(w)\bigr).
$$

Finally approximate $z$ by smooth $w$ in $A_\infty$. This density does not require uniform equivalence with $E$. Indeed $(\phi')^{p-2}\asymp r^\beta$ near zero and is positive away from zero. First truncate $z$ in value, then remove a ball of radius $\varepsilon$ around zero. For the bounded truncation the cutoff cost is at most $CM^2\varepsilon^{n+\beta-2}\to0$. Away from zero ordinary Sobolev approximation applies up to the smooth boundary. Truncation and the finite energy in (7.10) complete the approximation. This proves (7.11).

For the constraint, Taylor's bound (16), (7.7), and $t_j^2\ge\delta_j^p$ give

$$
\frac{c_{\alpha_j}\int_Br^{\alpha_j}|h_j|^q}{t_j^2}
\le C\alpha_j^{q\vartheta}\delta_j^{q-p}
=C(\alpha_j^\sigma\delta_j)^{q-p}\longrightarrow0.
\tag{7.12}
$$

The quadratic term is controlled and converges by Lemma 4.1. Tangency removes the linear term. Hence

$$
\widehat D_{\alpha_j}(v_{\alpha_j}+h_j)
=1+\frac{q(q-1)}2c_{\alpha_j}\int_Br^{\alpha_j}v_{\alpha_j}^{q-2}h_j^2
+o(t_j^2).
\tag{7.13}
$$

Let $\mu=\lambda\phi(1)^{p-2}$. By Lemma 5.1 and the radial-average decomposition, every finite-energy $z$ with mean-zero trace satisfies

$$
A_\infty(z)\ge(q_c-1)\mu\int_\Sigma(Tz)^2.
$$

Consequently, with $\kappa=1-(q-1)/(q_c-1)>0$,

$$
A_\infty(z)-(q-1)\mu\int_\Sigma(Tz)^2
\ge\kappa A_\infty(z).
\tag{7.14}
$$

Criticality gives $F'(v_{\alpha_j})[h_j]=L_{\alpha_j}(h_j)=0$. Combine (7.11)--(7.14) and (26). The lower limit of the left side of (7.8), divided by $t_j^2$, is at least
$\min\{\kappa/2,c_p\}>0$.
If no constants in (7.8) existed, choosing successively $\alpha_j\ge j$ and $\delta_j\alpha_j^\sigma<1/j$ with a ratio below half this fixed positive lower bound would contradict the sequential conclusion. This proves (7.8), uniformly over the normalized radial minimizers.

For $u$ close to $v_\alpha$, set $\widetilde u=u/L_\alpha(u)$. By (7.7) the denominator is positive and
$\|\widetilde u-v_\alpha\|_{1,p}\le C\|u-v_\alpha\|_{1,p}$ uniformly. The perturbation is tangent, so (7.8) and homogeneity give a strictly larger quotient unless $\widetilde u=v_\alpha$. On the unit energy sphere this exception forces $u=v_\alpha$. Equation (7.3) follows.

### 7.3. Matching competitors above the trace exponent

Suppose $q>p_\partial$, so $\sigma>0$, and put $b=(p-1)/(q-p)$. Choose a nonnegative $\psi\in C_c^\infty(\mathbb R^n)$ that is nonzero on the lower half-space $H=\{y_n<0\}$, with

$$
N=\int_H|\nabla\psi|^p>0,\qquad
M=\int_H e^{y_n}\psi^q>0,\qquad d=S\phi(1)^q.
$$

For a fixed constant $A>0$ and $e=(0,\ldots,0,1)$, define

$$
w_\alpha(x)=A\alpha^b\psi(\alpha(x-e)).
\tag{7.15}
$$

No boundary condition is imposed on competitors for the quotient. Under $y=\alpha(x-e)$ the ball becomes
$2y_n+|y|^2/\alpha<0$, converging to $H$, and
$|e+y/\alpha|^\alpha\to e^{y_n}$ uniformly on the fixed support of $\psi$. Dominated convergence and the identities
$p(b+1)-n=1-n+bq=-p\sigma$ yield

$$
\begin{aligned}
\|w_\alpha\|_{1,p}^p
 &=A^pN\alpha^{-p\sigma}(1+o(1)),\\
\|v_\alpha+w_\alpha\|_{1,p}^p
 &=1+A^pN\alpha^{-p\sigma}+o(\alpha^{-p\sigma}),\\
\widehat D_\alpha(v_\alpha+w_\alpha)
 &=1+\frac{A^qM}{d}\alpha^{-p\sigma}
   +o(\alpha^{-p\sigma}).
\end{aligned}
\tag{7.16}
$$

For the second formula, $\nabla v_\alpha$ is uniformly bounded while the bump gradient has scale $\alpha^{b+1}$. After rescaling, its mixed gradient terms vanish by dominated convergence. The bump's value energy has an extra factor $\alpha^{-p}$. For the third formula, $v_\alpha$ is uniformly bounded, the bump amplitude tends to infinity, and $c_\alpha/\alpha\to d^{-1}$ by (21). Subtract the unchanged integrands outside the bump support before taking these limits. These observations justify the remainders uniformly over the radial minimizers.

It follows that

$$
\frac{\mathcal Q_\alpha(v_\alpha+w_\alpha)}{\mathcal Q_\alpha(v_\alpha)}
=1+\left(A^pN-\frac{pA^qM}{qd}\right)\alpha^{-p\sigma}
 +o(\alpha^{-p\sigma}).
\tag{7.17}
$$

Choose $A$ large enough that the coefficient is negative. Normalize $u_\alpha=(v_\alpha+w_\alpha)/\|v_\alpha+w_\alpha\|_{1,p}$. It is positive and nonradial, has strictly smaller quotient, and satisfies

$$
\|u_\alpha-v_\alpha\|_{1,p}
=A N^{1/p}\alpha^{-\sigma}(1+o(1)),
\tag{7.18}
$$

because the normalization changes the function by $O(\alpha^{-p\sigma})=o(\alpha^{-\sigma})$. This proves (7.4) and Theorem 7.1. $\square$


## 8. Scope and further questions

The equality case $q=q_c(n,p)$ remains open. The limiting quadratic form has a first-angular-mode zero direction there, so the strict gap used in both Theorems 1.1 and 7.1 is unavailable. More precise dependence on $\alpha$ or higher-order analysis is needed.

Theorem 7.1 resolves the earlier uniform-neighborhood question under unit energy normalization. It gives the exact decay power above the trace exponent but not a limiting leading coefficient for $\alpha^\sigma R_\alpha$. Identifying such a coefficient would require a sharper boundary concentration analysis and an optimal profile, rather than the fixed test bump used here.

Lemma 2.1 applies when a degenerate variational problem supplies its stated compact weighted completion and positive constrained Hessian. Section 7 does not assert that its uniform argument applies without the common weight, reciprocal integrability, coefficient convergence and compact trace verified in this problem. Pointwise positivity of second variations alone is insufficient.

## References

[ACS25] L. Asselle, S. Cingolani, and M. Starostka, *Morse homology for a class of elliptic partial differential equations*, arXiv:2504.19721v1 (2025), Theorems 1.2 and 3.7. [Author preprint](https://arxiv.org/abs/2504.19721); [related journal DOI](https://doi.org/10.1142/S0219199726500082).

[CDS24] S. Cingolani, M. Degiovanni, and B. Sciunzi, *Weighted Sobolev spaces and Morse estimates for quasilinear elliptic equations*, Journal of Functional Analysis **286** (2024), no. 8, 110346. [DOI](https://doi.org/10.1016/j.jfa.2024.110346).

[CES11] D. Castorina, P. Esposito, and B. Sciunzi, *Spectral theory for linearized p-Laplace equations*, Nonlinear Analysis **74** (2011), 3606--3613. [DOI](https://doi.org/10.1016/j.na.2011.03.009).

[Ci13] S. Cingolani, *On local Morse theory for p-area functionals, p > 2*, Journal of Fixed Point Theory and Applications **14** (2013), 355--373; published online April 7, 2014. [DOI](https://doi.org/10.1007/s11784-014-0163-6).

[GS08] M. Gazzini and E. Serra, *The Neumann problem for the Hénon equation, trace inequalities and Steklov eigenvalues*, Annales de l'Institut Henri Poincaré C, Analyse non linéaire **25** (2008), 281--302. [DOI](https://doi.org/10.1016/j.anihpc.2006.09.003).

[NS26] A. I. Nazarov and A. P. Shcheglova, *The Neumann problem for the generalized Hénon equation. Local analysis*, arXiv:2604.26286v2, May 11, 2026. [Author preprint](https://arxiv.org/abs/2604.26286).

[Sh18] A. P. Shcheglova, *The Neumann problem for the generalized Hénon equation*, Journal of Mathematical Sciences **235** (2018), no. 3, 360--373. [DOI](https://doi.org/10.1007/s10958-018-4078-4).
