# A spherical Weinstock inequality at large perimeter

Henry Zweiman

September 16, 2026

## Abstract

For each dimension at least three, we prove that geodesic balls maximize the first nonzero Steklov eigenvalue among smooth geodesically convex domains in the unit sphere with prescribed boundary measure sufficiently close to the area of an equator. Equality holds only for balls. The perimeter hypothesis requires no prior closeness to a ball. We first construct a unique harmonic boundary center whose centered hemisphere contains the entire convex domain. In cotangent radial coordinates about this center, we prove a quantitative comparison uniform at the hemispherical endpoint. A cut-and-join construction gives a strict spectral comparison for spherical lunes. Crofton estimates then classify the noncollapsed limits of maximal-perimeter sequences, while coordinate trials control collapsed limits. These ingredients establish a uniform interval of perimeters. The full spherical comparison at arbitrary perimeter remains open in this work.

## 1. Introduction

Let $\Omega$ be a smooth domain in the unit sphere $\mathbb S^n$. Its first positive Steklov eigenvalue is

$$
\sigma_1(\Omega)=
\inf_{\substack{u\in H^1(\Omega),\ \int_{\partial\Omega}u\,dS=0\\
\int_{\partial\Omega}u^2\,dS>0}}
\frac{\int_\Omega|\nabla u|^2\,dV}
{\int_{\partial\Omega}u^2\,dS}.
\tag{1.1}
$$

Write $P(\Omega)=\mathcal H^{n-1}(\partial\Omega)$ and $\omega_j=|\mathbb S^j|$. Throughout the paper, a proper spherical convex domain means a geodesically convex domain whose closure lies in an open hemisphere. Convexity of a smooth boundary permits zero principal curvatures; positive curvature is not an assumption of the main theorem.

The higher-dimensional Euclidean Weinstock inequality was proved for convex domains by Bucur, Ferone, Nitsch, and Trombetti [BFNT]. The spherical and hyperbolic analogues are asked for in Open Question 4.27 of Colbois, Girouard, Gordon, and Sher [CGGS]. Recent hyperbolic results, including [GWW], do not directly transfer to the sphere. In positive curvature, a convex domain can approach a hemisphere or a lune as its boundary measure approaches the equatorial value. A perimeter condition near that value therefore does not force the domain to be nearly spherical.

**Theorem 1.1.** For every $n\geq3$ there exists $\varepsilon_n>0$ such that, for every smooth proper spherical convex domain $\Omega\subset\mathbb S^n$ with

$$
\omega_{n-1}-\varepsilon_n<P(\Omega)<\omega_{n-1},
\tag{1.2}
$$

one has

$$
\sigma_1(\Omega)\leq\sigma_1(B_R),\qquad
P(B_R)=P(\Omega),\quad 0<R<\frac{\pi}{2}.
\tag{1.3}
$$

Equality holds if and only if $\Omega$ is a geodesic ball.

The interval in this theorem is uniform over the entire smooth convex class. Its size is not explicit. The result addresses the large-perimeter part of the spherical question, and does not assert the comparison for all perimeters.

The first ingredient is a weighted boundary-center theorem. For the harmonic weight needed in (1.1), the center is unique inside the domain and lies in the domain's open positive polar. Thus centering the trial functions and placing the domain in a centered hemisphere are compatible. Ordinary spherical volume centroids have a related centered-hemisphere property in dimension two [BHLL]; the boundary weight here depends on the unknown center, and the proof uses a weighted hypersurface integration identity.

The second ingredient is uniform endpoint stability. If $\rho$ is the radial boundary about the harmonic center, put $u=\cot\rho$, $m=\langle u\rangle$, and $v=u-m$, where brackets denote normalized averages on $\mathbb S^{n-1}$. For $m$ sufficiently small, we prove

$$
\sigma_1(B_R)-\sigma_1(\Omega)
\geq \frac{c_n}{m}
\left\langle v^2+|\nabla v|^2\right\rangle.
\tag{1.4}
$$

The use of low spherical harmonics and moment estimates has a close Euclidean precedent in [GLMPT]. The uniform factor $1/m$ here arises from the degenerating perimeter derivative at the hemisphere and the positive endpoint slope of the ball eigenvalue. Convexity controls the cotangent graph by its mean, allowing the estimate to hold for varying shapes.

The third ingredient treats the other noncollapsed maximal-perimeter limits. A spherical lune has the same boundary measure as a hemisphere, independently of its opening angle. We construct a trial function by cutting an angular strip out of a hemisphere eigenfunction and joining the remaining pieces. Its boundary norm is unchanged and its energy is strictly reduced. Finally, a Crofton argument classifies positive-volume maximal-perimeter limits, and a local cap-area bound prevents concentration of boundary measure in the collapsed case.

The weighted geometric inequalities of Kwong and Wei [KW] are relevant to the broader problem, but the proof below uses neither their spherical flow argument at an unspecified center nor a radial volume rearrangement. Fixed-volume comparisons and their possible failure on the sphere [CR] are distinct from the perimeter-constrained question considered here.

## 2. Harmonic coordinates on spherical balls

Set $L=n-1$, $a(r)=\sin^Lr$, and

$$
I(r)=\int_0^r\sin^Lt\,dt,\qquad f(r)=\frac{I(r)}{\sin^Lr}.
\tag{2.1}
$$

Differentiation gives

$$
f'+L\cot r\,f=1,\qquad
f''+L\cot r\,f'-L\csc^2r\,f=0.
\tag{2.2}
$$

Since $f(r)=r/n+O(r^3)$ at zero, the functions $f(r)\theta_i$ extend smoothly and harmonically through the center.

**Lemma 2.1.** For $0<R\leq\pi/2$,

$$
\sigma_1(B_R)=z(R),\qquad z(r)=\frac{f'(r)}{f(r)}.
\tag{2.3}
$$

**Proof.** Degree-$\ell$ spherical harmonics have angular eigenvalue $\mu_\ell=\ell(\ell+n-2)$. Their regular harmonic radial factor minimizes

$$
\int_0^R\left(v'^2+\mu_\ell\csc^2r\,v^2\right)a(r)\,dr
\tag{2.4}
$$

in the finite-energy class with $v(R)=1$. Integration by parts identifies the minimum divided by $a(R)$ with the corresponding Steklov eigenvalue. Increasing the positive angular eigenvalue strictly increases this minimum: evaluate the smaller-angular-potential functional at the larger one's minimizer. The angular-potential integral is positive. Degree zero gives constants; the spherical harmonic decomposition exhausts the boundary space. The degree-one radial factor is $f(r)/f(R)$, proving the claim. This standard separation argument is also discussed in [CR]. $\square$

**Lemma 2.2.** If $n\geq3$, then

$$
z'(\pi/2)=L-A^{-2}>0,\qquad
A=I(\pi/2).
\tag{2.5}
$$

**Proof.** Positivity of $f$ is immediate. Also $(af')'=Laf/\sin^2r>0$, with $af'$ tending to zero at the origin, so $f'>0$. Put $x=\sin r\,f'/f$. Equation (2.2) gives

$$
x'=\frac{L-x^2-(L-1)\cos r\,x}{\sin r},
\qquad x(0)=1.
\tag{2.6}
$$

Since $L>1$, a first upward contact with $\sqrt L$ before $\pi/2$ is impossible: the right side is strictly negative there. Thus $0<x<\sqrt L$ in that interval. To obtain a strict endpoint inequality, let $y=\sqrt L-x$ and fix $r_0>0$. On $[r_0,\pi/2]$,

$$
y'+\frac{\sqrt L+x}{\sin r}y=(L-1)\cot r\,x\geq0.
\tag{2.7}
$$

The integrating factor and $y(r_0)>0$ give $y(\pi/2)>0$. At the endpoint $f=A$ and $f'=1$, so $A^{-1}<\sqrt L$. The Riccati equation for $z$ now gives (2.5). $\square$

For later use, summing the degree-one harmonic energies gives

$$
E(r)=f'(r)^2+L\frac{f(r)^2}{\sin^2r},
\qquad (aff')'=aE.
\tag{2.8}
$$

This identity converts the volume energy of a centered radial domain into a boundary radial integral.


## 3. A weighted center in the positive polar

### Statement and conventions

Let $\Omega\subset\mathbb S^n$, $n\geq2$, be a domain whose closure is contained in an open hemisphere. Assume that $\Omega$ is geodesically convex and its boundary $\Sigma$ is smooth with nonnegative principal curvatures for the outward unit normal $\nu$. Put $L=n-1$ and $H=\kappa_1+\cdots+\kappa_L\geq0$. Thus our sign convention is

$$
\Delta_\Sigma X=-LX-H\nu.
\tag{3.1}
$$

Define the **open positive polar**

$$
\Omega^+=\{p\in\mathbb S^n:p\cdot q>0\text{ for every }q\in\overline\Omega\}.
\tag{3.2}
$$

The word “positive” matters: the spherical polar is also conventionally defined using the opposite inequality.

Let $w:(-1,1]\to(0,\infty)$ be continuously differentiable, with a continuously differentiable extension at $1$, and suppose $w'(t)<0$ for $-1<t<1$. No boundedness near $-1$ is assumed. Set

$$
M(p)=\int_\Sigma w(p\cdot X)X\,dS_X,\qquad
F(p)=(I-p\otimes p)M(p).
\tag{3.3}
$$

**Theorem 3.1 (weighted boundary center).** There is a unique $p\in\Omega$ for which $F(p)=0$. This point belongs to $\Omega^+$; in particular,

$$
\max_{q\in\overline\Omega}d(p,q)<\frac{\pi}{2}.
\tag{3.4}
$$

Uniqueness here concerns centers inside $\Omega$. We make no assertion about critical points elsewhere on the sphere.

### Existence of an interior center

Write

$$
W(t)=\int_t^1w(s)\,ds,\qquad
U(p)=\int_\Sigma W(p\cdot X)\,dS_X.
\tag{3.5}
$$

Because $\overline\Omega$ is compact in an open hemisphere, no two of its points are antipodal. Consequently $p\cdot X$ stays in a compact subinterval of $(-1,1]$ for $p,X\in\overline\Omega$. The function $U$ is continuous on $\overline\Omega$ and twice continuously differentiable in a neighborhood of it. Direct differentiation on the sphere gives

$$
\nabla_{\mathbb S^n}U(p)=-F(p).
\tag{3.6}
$$

It attains a minimum on $\overline\Omega$. If a minimum were at $p\in\Sigma$, the supporting greatsphere at $p$ would give $X\cdot\nu(p)\leq0$ for all $X\in\overline\Omega$, with strict inequality on an open part of $\Sigma$. Since $p\cdot\nu(p)=0$ and $w>0$,

$$
dU_p[-\nu(p)]
=F(p)\cdot\nu(p)
=\int_\Sigma w(p\cdot X)X\cdot\nu(p)\,dS_X<0.
\tag{3.7}
$$

The inward normal initially enters $\Omega$, so this contradicts minimality. The minimum is interior and satisfies $F(p)=0$.

At any such point, $M(p)=\lambda p$. Choose a hemisphere vector $e$ with $e\cdot X>0$ throughout $\overline\Omega$. Then

$$
\lambda(e\cdot p)=e\cdot M(p)
=\int_\Sigma w(p\cdot X)e\cdot X\,dS_X>0.
\tag{3.8}
$$

As $e\cdot p>0$, we have $\lambda>0$.

### A boundary integration identity

Define

$$
b(t)=\int_0^1s^{L-1}w(ts)\,ds.
\tag{3.9}
$$

This definition is regular at $t=0$ and applies to negative $t$ as well. It gives

$$
b>0,\qquad b'<0,\qquad Lb(t)+tb'(t)=w(t).
\tag{3.10}
$$

For the last identity, integrate the derivative of $s^Lw(ts)$ from $0$ to $1$. The lower boundary term is zero because $L\geq1$.

Fix $p,q\in\mathbb S^n$ and write $t=p\cdot X$, $u=q\cdot X$, $p_\nu=p\cdot\nu(X)$, and $q_\nu=q\cdot\nu(X)$ on $\Sigma$. From (3.1) and orthogonal projection onto $T_X\Sigma$,

$$
\Delta_\Sigma u=-Lu-Hq_\nu,\qquad
\nabla_\Sigma t\cdot\nabla_\Sigma u=p\cdot q-tu-p_\nu q_\nu.
\tag{3.11}
$$

Integrating $\operatorname{div}_\Sigma(b(t)\nabla_\Sigma u)$ over the closed hypersurface and using (3.10) yields the exact identity

$$
\int_\Sigma w(t)u\,dS
=(p\cdot q)\int_\Sigma b'(t)\,dS
-\int_\Sigma\bigl(b(t)H+b'(t)p_\nu\bigr)q_\nu\,dS.
\tag{3.12}
$$

The term involving $b'p_\nu q_\nu$ must be retained.

### Positivity against the whole domain

Suppose $p\in\Omega$ is balanced. Let

$$
A=\int_\Sigma b'(p\cdot X)\,dS,\qquad
B(X)=b(p\cdot X)H+b'(p\cdot X)\,p\cdot\nu(X).
\tag{3.13}
$$

Convexity gives $p\cdot\nu(X)<0$, while (3.10) and $H\geq0$ give $A<0$ and $B(X)>0$, since $b'<0$ and $p\cdot\nu(X)<0$. For every $q\in\overline\Omega$, the support inequality is $q\cdot\nu(X)\leq0$. It is strict on a nonempty open part of $\Sigma$. Indeed, maximize distance from $q$ on the boundary. At a farthest point $X$, the distance lies strictly between zero and $\pi$, and tangential differentiation shows that $q$ lies in the span of $X,\nu(X)$. Its normal component has nonzero magnitude $\sin d(q,X)$, and the support inequality fixes its negative sign. Continuity gives the required open patch.

The left side of (3.12) equals $q\cdot M(p)=\lambda p\cdot q$. Hence

$$
(\lambda-A)p\cdot q
=-\int_\Sigma B(X)\,q\cdot\nu(X)\,dS>0.
\tag{3.14}
$$

Since $\lambda>0$ and $A\leq0$, this proves $p\cdot q>0$. Compactness of $\overline\Omega$ now gives (3.4). This argument applies to every balanced point in $\Omega$, not just to the particular minimum constructed above.

### Uniqueness

For $p\in\Omega^+$ and $v\in T_p\mathbb S^n$, differentiating (3.5) along a spherical geodesic gives

$$
\operatorname{Hess}_{\mathbb S^n}U(p)[v,v]
=\int_\Sigma
\left[-w'(p\cdot X)(v\cdot X)^2
+w(p\cdot X)(p\cdot X)|v|^2\right]dS_X.
\tag{3.15}
$$

This is positive when $v\ne0$. The set $\Omega\cap\Omega^+$ is geodesically convex: it is the intersection of a convex domain with open hemispheres, and any two of its points have a unique short geodesic between them. If two distinct balanced points existed in $\Omega$, (3.14) would place them both in this intersection. Along the joining geodesic, (3.15) would make the derivative of $U$ strictly increasing, although it vanishes at both endpoints. This is impossible.

### Corollary 3.2: harmonic centering

Use the degree-one harmonic radial function from Section 2:

$$
I(r)=\int_0^r\sin^Ls\,ds,\qquad
f(r)=\frac{I(r)}{\sin^Lr},\qquad 0<r<\pi.
\tag{3.16}
$$

Set

$$
w(\cos r)=\frac{f(r)}{\sin r}
=\frac{I(r)}{\sin^{L+1}r}.
\tag{3.17}
$$

The apparent singularity at $r=0$ is removable, with $w(1)=1/(L+1)$. Smoothness in $t=\cos r$ near $1$ follows, for example, from the convergent series $w(\cos r)=\sum_{j\geq0}\binom{2j}{j}\sin^{2j}r/[4^j(n+2j)]$ near $r=0$.

To check monotonicity on the entire interval, rather than assuming the hemisphere conclusion in advance, define

$$
J(r)=\sin^{L+1}r-(L+1)\cos r\,I(r).
\tag{3.18}
$$

Then

$$
\frac{d}{dr}\left(\frac{I(r)}{\sin^{L+1}r}\right)
=\frac{J(r)}{\sin^{L+2}r},\qquad
J'(r)=(L+1)\sin r\,I(r)>0,\qquad J(0)=0.
\tag{3.19}
$$

Thus $w'(\cos r)<0$ for every $0<r<\pi$. All the lemma's hypotheses hold. For $X=\cos r\,p+\sin r\,\theta_p(X)$, equation (3.3) becomes

$$
F(p)=\int_\Sigma f(d(p,X))\,\theta_p(X)\,dS_X.
\tag{3.20}
$$

There is therefore a unique interior harmonic center. Every degree-one trial function about this center has zero boundary mean, and the complete domain lies strictly inside its centered hemisphere. The harmonic Rayleigh trials are therefore admissible at this same center.



## 4. Uniform quantitative stability at the hemisphere

### Statement

**Theorem 4.1 (uniform endpoint stability).** Fix $n\geq3$ and put $L=n-1$. There are constants $m_n,c_n^*>0$ depending only on dimension with the following property. Let $\Omega\subset\mathbb S^n$ be smooth and geodesically convex, and have closure in an open hemisphere. Use its unique harmonic center $p$ from Section 3. Write its radial boundary as $r=\rho(\theta)<\pi/2$ and set

$$
u(\theta)=\cot\rho(\theta)>0,\qquad
m=\langle u\rangle,\qquad
v=u-m,\qquad
T=\langle v^2+|\nabla v|^2\rangle.
\tag{4.1}
$$

Averages and derivatives are on the unit $\mathbb S^L$. If $m<m_n$, and $R<\pi/2$ is the radius of the ball with the same boundary measure, then

$$
\sigma_1(B_R)-\sigma_1(\Omega)
\geq \frac{c_n^*}{m}\,T.
\tag{4.2}
$$

In particular, a zero eigenvalue deficit implies that $\Omega$ is a ball centered at $p$.

The smallness condition is expressed at the harmonic center. It is stronger than requiring perimeter close to that of an equator. In particular, this proposition does not cover convex domains approaching a lune. Constants are not claimed to be explicit or optimal.

### Convexity controls the graph by its mean

In gnomonic coordinates about $p$, the domain has radial function $1/u$. Convexity implies that $u$ is the support function of its Euclidean polar body $K$. The body $K$ contains the origin in its interior; its support function is smooth and

$$
\nabla^2u+u\,g\geq0.
\tag{4.3}
$$

These claims can be seen directly from the homogeneous extension $\widehat u$: it is the gauge of the convex gnomonic image, hence is convex, and its sublevel set is that image. Convexity gives the nonnegative tangential Hessian in (4.3).

Let $M=\max u=\max_{x\in K}|x|$. Choose $x_0\in K$ of length $M$. Because $0\in K$, for every direction $\theta$,

$$
u(\theta)\geq\max(0,x_0\cdot\theta).
\tag{4.4}
$$

Therefore

$$
m\geq \kappa_n M,\qquad
\kappa_n=\langle\max(0,\theta_1)\rangle>0.
\tag{4.5}
$$

The usual support parametrization can also be verified by differentiating the support plane: $x(\theta)=u(\theta)\theta+\nabla u(\theta)\in K$. It follows that $|\nabla u|\leq M$. Consequently

$$
\|u\|_{C^1}+\|v\|_{C^1}\leq C_n m,\qquad
T\leq C_n m^2.
\tag{4.6}
$$

This bound is the point where convexity makes the endpoint argument uniform over varying shapes.

### Exact centering removes the first harmonic

For a radial graph, define

$$
I(r)=\int_0^r\sin^Ls\,ds,\qquad
\mathcal G(u,\xi)=I(\operatorname{arccot}u)
\sqrt{1+\frac{|\xi|^2}{1+u^2}}.
\tag{4.7}
$$

The harmonic mean-zero equation is exactly

$$
\langle\mathcal G(u,\nabla u)\theta\rangle=0.
\tag{4.8}
$$

Indeed, $f(\rho)=I(\rho)/\sin^L\rho$, and multiplying by the radial area density cancels $\sin^L\rho$.

On a fixed neighborhood of $(u,\xi)=(0,0)$, $\mathcal G$ has bounded second derivatives, and

$$
\mathcal G_u(m,0)=-(1+m^2)^{-(L+2)/2},\qquad
\mathcal G_\xi(m,0)=0.
\tag{4.9}
$$

Taylor expansion at $(m,0)$, followed by integration in (4.8), yields

$$
|\langle v\theta\rangle|\leq C_nT.
\tag{4.10}
$$

Here $m$ is sufficiently small that the first derivative in (4.9) is bounded away from zero. The constant term integrates to zero against $\theta$.

Let $v_1$ denote the degree-one projection of $v$. Since $\langle v\rangle=0$, orthogonality and $\langle\theta_i\theta_j\rangle=\delta_{ij}/n$ give

$$
\langle v_1^2\rangle\leq C_nT^2\leq C_nm^2T.
\tag{4.11}
$$

For all degrees at least two, the angular eigenvalue is at least $2n$. Thus, with

$$
S=\langle|\nabla v|^2-Lv^2\rangle,
\tag{4.12}
$$

the spherical harmonic expansion implies

$$
S\geq \frac{L+2}{2L+3}\,T-C_n\langle v_1^2\rangle
\geq c_nT
\tag{4.13}
$$

for some $c_n>0$ after decreasing the permitted bound on $m$. All constants in this proof denoted by $C_n$ or $c_n$ may change from line to line.

### Perimeter comparison at the mean cotangent

The normalized area density in cotangent coordinates is

$$
\mathcal J(u,\xi)
=(1+u^2)^{-L/2}\sqrt{1+\frac{|\xi|^2}{1+u^2}}.
\tag{4.14}
$$

It is smooth near zero and invariant under $(u,\xi)\mapsto(-u,-\xi)$. Its Hessian at zero is diagonal, with $u$ entry $-L$ and the $\xi$ block equal to the identity. Since its third derivatives vanish at zero, its Hessian differs from this constant matrix by $O_n(|u|^2+|\xi|^2)$. Taylor expansion at $(m,0)$, using (4.6) and $\langle v\rangle=0$, therefore gives

$$
\frac{P(\Omega)}{\omega_L}-(1+m^2)^{-L/2}
=\frac12S+O_n(m^2T)\geq c_nT,
\tag{4.15}
$$

where $\omega_L=|\mathbb S^L|$. No bound on second derivatives of the graph is needed in this Taylor estimate.

We also need $P(\Omega)<\omega_L$. To see this without an unstated branch choice, use the convex family with cotangent graph $tu$, $0<t\leq1$. Its gnomonic images are dilations of a fixed smooth convex body. They remain geodesically convex. Their radial derivative in $t$ is

$$
\partial_t\rho_t=-\frac{u}{1+t^2u^2}<0.
\tag{4.16}
$$

The outward normal component of this velocity is negative, and the mean curvature is nonnegative and not identically zero. Otherwise the smooth closed convex hypersurface would be totally geodesic, contradicting containment in an open hemisphere. The first variation of area, with the convention $H>0$ for outward convex spheres, consequently gives $dP(\Omega_t)/dt<0$. As $t\downarrow0$ its graph converges smoothly to the equator, whose area is $\omega_L$. This proves the strict upper bound on perimeter.

Set $r_m=\operatorname{arccot}m$. There is a unique equal-perimeter $R\in(0,\pi/2)$, and (4.15) shows $R\geq r_m$. For $r\in[r_m,\pi/2]$,

$$
\frac{d}{dr}\sin^Lr=L\sin^{L-1}r\cos r\leq Lm.
\tag{4.17}
$$

Integrating this inequality and applying (4.15) gives

$$
R-r_m\geq \frac{c_n}{m}\,T.
\tag{4.18}
$$

If $T=0$ all these comparisons are equalities at $R=r_m$.

### The trial quotient loses only a quadratic error

Write $a(r)=\sin^Lr$, $f(r)=I(r)/a(r)$, and $z(r)=f'(r)/f(r)$. The exact harmonic trial quotient at the chosen center is

$$
Q=\frac{N}{D},\quad
N=\langle a(\rho)f(\rho)f'(\rho)\rangle,\quad
D=\left\langle a(\rho)f(\rho)^2
\sqrt{1+\frac{|\nabla u|^2}{1+u^2}}\right\rangle.
\tag{4.19}
$$

It satisfies $\sigma_1(\Omega)\leq Q$. Define the numerator integrand as a smooth function $\mathcal N(u)$, and the denominator integrand as a smooth function $\mathcal D(u,\xi)$. Near zero, all relevant derivatives are bounded and $D$ is bounded below by a positive dimensional constant.

For fixed $m$, the function

$$
\mathcal K_m(u,\xi)=\mathcal N(u)-z(r_m)\mathcal D(u,\xi)
\tag{4.20}
$$

vanishes at $(m,0)$. Its $\xi$ derivative there is zero, while its $u$ derivative multiplies $v$, which has zero mean. Bounded second derivatives and (4.6) give

$$
|N-z(r_m)D|\leq C_nT,\qquad
Q\leq z(r_m)+C_nT.
\tag{4.21}
$$

The constants are uniform for small $m$.

### Positive endpoint slope completes the estimate

The first ball eigenvalue is $z(R)$. By Lemma 2.2,

$$
z'(\pi/2)=L-I(\pi/2)^{-2}>0\qquad(n\geq3).
\tag{4.22}
$$

Continuity gives $z'\geq\gamma_n>0$ on a fixed interval just below $\pi/2$. Since $r_m$ belongs to that interval for sufficiently small $m$, (4.18) and (4.21) imply

$$
\begin{aligned}
\sigma_1(B_R)-\sigma_1(\Omega)
&\geq z(R)-Q\\
&\geq \gamma_n(R-r_m)-C_nT\\
&\geq \left(\frac{c_n}{m}-C_n\right)T.
\end{aligned}
\tag{4.23}
$$

Finally decrease $m_n$ once more to absorb the last term. This proves (4.2). A zero deficit forces $T=0$, hence $u$ is constant and the domain is a centered ball.



## 5. A strict comparison for lunes

### Lunes and the comparison value

Let $n\geq3$, $0<\alpha<\pi$, and write points of the unit sphere as

$$
X=(\sin\eta\cos\phi,\sin\eta\sin\phi,\cos\eta\,y),
\quad 0<\eta<\frac{\pi}{2},\quad y\in\mathbb S^{n-2}.
\tag{5.1}
$$

Let $\Lambda_\alpha$ be the spherical lune given by $|\phi|<\alpha/2$. Its edge is the great $\mathbb S^{n-2}$ at $\eta=0$. The two faces are hemispheres of great $\mathbb S^{n-1}$'s, and hence

$$
P(\Lambda_\alpha)=\omega_{n-1},\qquad
\omega_j=|\mathbb S^j|.
\tag{5.2}
$$

The hemisphere is the limiting case $\alpha=\pi$. Put

$$
A=\int_0^{\pi/2}\sin^{n-1}r\,dr,\qquad
\sigma_H=A^{-1}.
\tag{5.3}
$$

Lemma 2.1 identifies $\sigma_H$ as the first positive Steklov eigenvalue of a hemisphere. The Rayleigh variational principle applies to the bounded Lipschitz lune.

**Proposition 5.1 (lune comparison).** For every $0<\alpha<\pi$,

$$
\sigma_1(\Lambda_\alpha)
\leq \sigma_H-d_n(\pi-\alpha)<\sigma_H,
\qquad
d_n=\frac{\omega_{n-2}(n-2)}
{n(n-1)^2A^2\omega_{n-1}}>0.
\tag{5.4}
$$

The explicit constant is a convenient lower bound on removed energy, not an optimal estimate.

### A hemisphere eigenfunction

For $0\leq t\leq1$, define

$$
w(t)=
\frac{\displaystyle\int_0^{\arccos t}\sin^{n-1}s\,ds}
{(1-t^2)^{n/2}},
\qquad w(1)=\frac1n.
\tag{5.5}
$$

It is smooth up to $1$, positive, and decreasing; these properties were proved on the larger interval in Section 3. In particular $w(t)\geq1/n$. On the hemisphere $H=\{X_0>0\}$, choose

$$
U_H(X)=w(X_0)X_2
=w(\sin\eta\cos\phi)\cos\eta\,y_1.
\tag{5.6}
$$

This is a harmonic first Steklov eigenfunction. It is even in $\phi$, and its boundary trace is $AX_2$. Therefore

$$
D_H=\int_{\partial H}U_H^2\,dS
=\frac{A^2\omega_{n-1}}n,\qquad
\int_H|\nabla U_H|^2\,dV=\sigma_HD_H.
\tag{5.7}
$$

The boundary mean vanishes by reflection of $X_2$.

### Removing an angular strip

Set $b=(\pi-\alpha)/2$. On the positive half of the lune use the rotated restriction of $U_H$ with angular coordinate $\psi=\phi+b$; on the negative half use $\psi=\phi-b$. Equivalently, define the explicit function

$$
U_\alpha(X)=w\bigl(\cos b\,X_0-\sin b\,|X_1|\bigr)X_2.
\tag{5.8}
$$

The argument of $w$ lies in $[0,1]$ on the closed lune. The two expressions coincide on $\phi=0$. Thus $U_\alpha$ is Lipschitz and is an admissible $H^1$ trial function, although its normal derivative may jump at the joining hypersurface. No equation is asserted at that seam.

On either face, the argument of $w$ is zero. Hence $U_\alpha=AX_2$ on the boundary, its boundary mean is zero, and

$$
\int_{\partial\Lambda_\alpha}U_\alpha^2\,dS=D_H.
\tag{5.9}
$$

Each half of the construction is an isometry to an outer angular strip of $H$, preserving $\eta,y$. Consequently

$$
\int_{\Lambda_\alpha}|\nabla U_\alpha|^2\,dV
=\int_{H\cap\{|\psi|>b\}}|\nabla U_H|^2\,dV
=\sigma_HD_H-E_b,
\tag{5.10}
$$

where

$$
E_b=\int_{H\cap\{|\psi|<b\}}|\nabla U_H|^2\,dV.
\tag{5.11}
$$

The seam has zero volume, and matching traces justify the piecewise energy identity.

### A dimensional lower bound on the removed energy

The metric and volume form in (5.1) are

$$
g=d\eta^2+\sin^2\eta\,d\psi^2+\cos^2\eta\,g_{\mathbb S^{n-2}},
\qquad
dV=\sin\eta\cos^{n-2}\eta\,d\eta\,d\psi\,dS_y.
\tag{5.12}
$$

The component of the gradient in the $y$ directions contributes

$$
w(\sin\eta\cos\psi)^2(1-y_1^2)
\geq \frac{1-y_1^2}{n^2}
\tag{5.13}
$$

to its squared norm. Since

$$
\int_0^{\pi/2}\sin\eta\cos^{n-2}\eta\,d\eta=\frac1{n-1},
\qquad
\int_{\mathbb S^{n-2}}(1-y_1^2)\,dS
=\omega_{n-2}\frac{n-2}{n-1},
\tag{5.14}
$$

we obtain

$$
E_b\geq
(\pi-\alpha)\frac{\omega_{n-2}(n-2)}{n^2(n-1)^2}.
\tag{5.15}
$$

Combining (5.7), (5.9), (5.10), and the Rayleigh principle gives (5.4).

### A fixed ambient trial for passing to nearby domains

For each fixed $\alpha$, choose a smooth extension of $w$ from $[0,1]$ to a bounded smooth function on $[-1,1]$. Such an extension exists because its derivatives are regular at both endpoints of $[0,1]$. Using this extension in (5.8) gives a globally Lipschitz function on $\mathbb S^n$ that agrees with the trial function on $\Lambda_\alpha$. Its gradient is bounded almost everywhere.

This observation will allow a fixed trial function to be used on convex domains converging to the lune. On those domains one subtracts the boundary mean; one does not assume that the exact lune symmetry persists.



## 6. Crofton estimates and maximal-perimeter compactness

### Crofton normalization and a local area bound

Let $\mu$ be probability Haar measure on the Grassmannian $G(2,n+1)$. A plane $E$ determines a great circle $C_E=E\cap\mathbb S^n$. For a rectifiable hypersurface portion $S$, spherical Crofton gives

$$
\mathcal H^{n-1}(S)
=\frac{\omega_{n-1}}2\int_{G(2,n+1)}
\#(S\cap C_E)\,d\mu(E).
\tag{6.1}
$$

The normalization follows by taking $S$ to be a great $\mathbb S^{n-1}$, which has two intersections with almost every great circle. More generally, the incidence coarea formula identifies the right side with a constant times local hypersurface area: rotations make the tangential angular factor independent of the point and tangent hyperplane. Calibration at the great sphere determines that constant. The same coarea formula extends the identity from smooth patches to rectifiable patches by partition and approximation. Tangencies and exceptional circles have zero measure.

The spherical Crofton/quermassintegral convention is recorded, for example, in [CRS, Section 2], with reference to the standard incidence theory. Here the local incidence formula is normalized directly by the equator.

For the smooth boundary $\Sigma$ of a proper geodesically convex domain, almost every circle meets $\Sigma$ at most twice. Thus

$$
P(\Omega)\leq\omega_{n-1}.
\tag{6.2}
$$

For a cap $B(p,r)$, $r<\pi/2$, a random great circle meets the cap precisely when $|\operatorname{proj}_E p|\geq\cos r$. Rotational invariance gives the squared projection the beta distribution with parameters $1$ and $(n-1)/2$. This can be derived by expressing a uniform point on $\mathbb S^n$ as a normalized Gaussian vector and grouping its first two squared coordinates. Hence

$$
\mu\{E:C_E\cap B(p,r)\ne\varnothing\}=\sin^{n-1}r.
\tag{6.3}
$$

Applying (6.1) to $\Sigma\cap B(p,r)$ gives the uniform bound

$$
\mathcal H^{n-1}(\Sigma\cap B(p,r))
\leq\omega_{n-1}\sin^{n-1}r.
\tag{6.4}
$$

No curvature bound is needed for this estimate.

### Collapsed volume forces small first Steklov eigenvalue

Assume $n\geq3$ and $P=P(\Omega)\geq\omega_{n-1}/2$. Write

$$
c=\frac1P\int_\Sigma X\,dS,\qquad
\delta_0=1-\left(\frac{2+\sqrt3}{4}\right)^2>0.
\tag{6.5}
$$

For $r=\pi/6$, (6.4) bounds the area in every cap by $\omega_{n-1}/4\leq P/2$. If $c\ne0$, take $p=c/|c|$. At least half the boundary measure is outside this cap, so

$$
|c|=\frac1P\int_\Sigma p\cdot X\,dS
\leq\frac{1+\cos(\pi/6)}2=\frac{2+\sqrt3}{4}.
\tag{6.6}
$$

The same bound is immediate when $c=0$. Subtracting the boundary means from all $n+1$ ambient coordinate functions, then summing their Rayleigh inequalities, yields

$$
\sigma_1(\Omega)
\leq\frac{n|\Omega|}{P(1-|c|^2)}
\leq\frac{n|\Omega|}{\delta_0P}.
\tag{6.7}
$$

Here $\sum_i|\nabla_{\mathbb S^n}X_i|^2=n$ and $\sum_i(X_i-c_i)^2$ integrates to $P(1-|c|^2)$. Consequently any such sequence with volume tending to zero has $\sigma_1$ tending to zero. This rules out spectral concentration on a collapsed maximal-perimeter sequence without asserting convergence of its boundary to the boundary of a lower-dimensional set.

### Full-dimensional limits at maximal perimeter are lunes or hemispheres

Let $\overline\Omega_j$ be smooth proper convex spherical bodies with $P(\Omega_j)\to\omega_{n-1}$. By compactness of the space of nonempty compact subsets of the sphere, pass to a Hausdorff limit $K$. Convexity persists: normalized positive combinations of non-antipodal points are obtained by taking limits of the corresponding combinations. The cone

$$
C=\{tX:t\geq0,\ X\in K\}
\tag{6.8}
$$

is therefore a closed convex cone. Each $K_j$ is contained in a closed hemisphere; passing to a subsequence of the hemisphere centers shows the same for $K$. In particular $C$ is not all of $\mathbb R^{n+1}$.

Suppose $K$ has nonempty spherical interior. Then $C$ is full dimensional. Its positive dual

$$
D=\{a\in\mathbb R^{n+1}:a\cdot x\geq0\text{ for all }x\in C\}
\tag{6.9}
$$

is nonzero and pointed: a line in $D$ would force $C$ into a hyperplane.

If $\dim\operatorname{span}D\geq3$, choose three linearly independent vectors $a_1,a_2,a_3\in D$. Set

$$
h=a_1+a_2+a_3,\qquad
E=\operatorname{span}\{a_1,a_2,a_3\}\cap h^\perp.
\tag{6.10}
$$

The space $E$ is a two-plane. If $x\in E\cap C$, then each $a_i\cdot x\geq0$ while their sum is $h\cdot x=0$. Thus all three inner products vanish, forcing $x=0$. It follows that $C_E$ misses $K$.

The disjoint compact sets $C_E$ and $K$ have positive distance. A whole open neighborhood of $E$ in the Grassmannian therefore misses $K$; after taking a smaller neighborhood with compact closure, it also misses every $K_j$ for large $j$. Let its positive Haar measure be $\eta$. Equation (6.1) then gives

$$
P(\Omega_j)\leq(1-\eta)\omega_{n-1},
\tag{6.11}
$$

a contradiction.

Thus $D$ spans at most two dimensions. A nonzero closed pointed cone in one dimension is a ray; its dual is a halfspace, so $K$ is a hemisphere. In two dimensions, $D$ is a sector with opening $\beta\in(0,\pi)$. The bipolar theorem, which here follows directly from separating a point from a closed convex cone, says that $C$ is its positive dual. Therefore $K$ is a lune with opening $\alpha=\pi-\beta\in(0,\pi)$. This proves the required classification for full-dimensional limits. It neither classifies collapsed limits nor needs to do so, in view of (6.7).

### Boundary integrals at a nondegenerate lune limit

If $K_j\to\overline\Lambda_\alpha$ with fixed $0<\alpha<\pi$, then for every continuous function $g$ on the sphere,

$$
\int_{\partial\Omega_j}g\,dS\longrightarrow
\int_{\partial\Lambda_\alpha}g\,dS.
\tag{6.12}
$$

Here is a direct justification adapted to this limit. Away from the edge, cover each face by finitely many compact patches in gnomonic charts. Convexity turns the boundaries into graphs of convex functions over the limiting flat face, with the domain consistently on one side. Hausdorff convergence gives uniform convergence of the graph functions to zero on slightly larger patches. Convex difference-quotient bounds then give convergence of their gradients to zero on the smaller patches. The spherical metric is smooth in each chart, so the graph area densities converge uniformly there.

The edge is a compact smooth $\mathbb S^{n-2}$. Its $r$-neighborhood can be covered by $O_n(r^{-(n-2)})$ caps of radius $O(r)$. Applying (6.4) in each cap bounds the boundary area of that neighborhood, uniformly in $j$, by $O_n(r)$. Its contribution against bounded $g$ therefore tends to zero as $r\downarrow0$. Combining the patch convergence and this bound proves (6.12). The same argument gives ordinary boundary-area convergence near a hemispherical limit, without an edge term.

Volume integrals of a fixed bounded measurable function also converge for a full-dimensional convex limit, provided it is defined almost everywhere: the characteristic functions converge almost everywhere off the limit boundary, which has zero spherical volume. Interior convergence follows, for example, by covering compact subsets of the interior by small geodesic simplices whose vertices persist under Hausdorff convergence; exterior convergence is immediate. Dominated convergence applies.

As a consequence, for every globally Lipschitz $U$ whose limiting boundary variance is positive,

$$
\limsup_j\sigma_1(\Omega_j)
\leq
\frac{\int_{\Lambda_\alpha}|\nabla U|^2\,dV}
{\displaystyle\int_{\partial\Lambda_\alpha}
\left(U-\frac1{\omega_{n-1}}\int_{\partial\Lambda_\alpha}U\,dS\right)^2dS}.
\tag{6.13}
$$

One subtracts the boundary mean separately on each $\Omega_j$. This is a fixed-trial upper bound, not an assertion of full spectral convergence.



## 7. Proof of Theorem 1.1

### Contradiction sequence

Suppose no $\varepsilon_n$ has the stated property. There is then a sequence of nonball domains $\Omega_j$ satisfying all the geometric hypotheses, with

$$
P(\Omega_j)\longrightarrow\omega_{n-1},
\qquad
\sigma_1(\Omega_j)\geq\sigma_1(B_{R_j}),
\qquad
P(B_{R_j})=P(\Omega_j).
\tag{7.1}
$$

This formulation includes both violations of the inequality and nonball equality cases. The comparison radii obey $R_j\to\pi/2$. With

$$
A=\int_0^{\pi/2}\sin^{n-1}r\,dr,\qquad
\sigma_H=A^{-1}>0,
\tag{7.2}
$$

the ball eigenvalue formula gives

$$
\sigma_1(B_{R_j})\longrightarrow\sigma_H.
\tag{7.3}
$$

Pass to a Hausdorff limit $K$ of the closed domains.

### Collapsed limit

If $K$ has empty spherical interior, convexity places it in a lower-dimensional great subsphere, so its spherical volume is zero. More explicitly, the cone over $K$ is convex; if that cone spanned $\mathbb R^{n+1}$, it would have nonempty interior and its spherical section would also have interior. Thus its span is proper.

Hausdorff convergence implies $|\Omega_j|\to0$. For large $j$, $P(\Omega_j)\geq\omega_{n-1}/2$. The coordinate estimate (6.7) therefore implies

$$
\sigma_1(\Omega_j)\leq
\frac{n|\Omega_j|}{\delta_0P(\Omega_j)}
\longrightarrow0,
\tag{7.4}
$$

contradicting (7.1) and (7.3).

### Proper lune limit

Suppose $K$ has nonempty interior. The dual-cone/Crofton argument in Section 6 shows that $K$ is either a hemisphere or a lune. If $K=\overline\Lambda_\alpha$ with $0<\alpha<\pi$, use the fixed globally Lipschitz trial $U_\alpha$ from Section 5.

Its limiting boundary mean is zero and its boundary norm is positive. Boundary-integral convergence and volume dominated convergence, as proved in Section 6, imply

$$
\limsup_j\sigma_1(\Omega_j)
\leq
\frac{\int_{\Lambda_\alpha}|\nabla U_\alpha|^2\,dV}
{\int_{\partial\Lambda_\alpha}U_\alpha^2\,dS}
\leq\sigma_H-d_n(\pi-\alpha)<\sigma_H.
\tag{7.5}
$$

This again contradicts (7.1) and (7.3). The fixed trial is recentered by subtracting its boundary mean on each approximating domain; no residual symmetry of $\Omega_j$ is assumed.

### Hemispherical limit

The remaining possibility is $K=\overline H_o=\{X:o\cdot X\geq0\}$. Let $p_j$ be the harmonic center of $\Omega_j$. By Corollary 3.2,

$$
p_j\cdot X>0\qquad\text{for every }X\in\overline\Omega_j.
\tag{7.6}
$$

Every subsequential limit $p$ thus satisfies $p\cdot X\geq0$ for all $X\in\overline H_o$. Taking both signs of each equatorial direction forces $p$ to be parallel to $o$, and taking $X=o$ fixes the positive sign. Hence

$$
p_j\longrightarrow o.
\tag{7.7}
$$

Convex Hausdorff convergence to a full-dimensional convex body gives inner convergence on compact subsets of the interior. In this case, for every fixed $\delta>0$ and large $j$,

$$
B(o,\pi/2-\delta)\subset\Omega_j.
\tag{7.8}
$$

For completeness, this inner-convergence fact follows by covering a compact subset of the hemisphere by finitely many small geodesic simplices whose vertices lie in the interior; vertices can be perturbed into $\Omega_j$ by Hausdorff convergence, and their convex hulls continue to cover the compact subset after using slightly larger simplices.

Equations (7.7) and (7.8) imply

$$
B(p_j,\pi/2-2\delta)\subset\Omega_j
\tag{7.9}
$$

for large $j$. The radial boundary $\rho_j$ about $p_j$ also satisfies $\rho_j<\pi/2$ by (7.6). Therefore

$$
0<\cot\rho_j(\theta)\leq\tan(2\delta),
\qquad
m_j=\langle\cot\rho_j\rangle\longrightarrow0.
\tag{7.10}
$$

Apply Theorem 4.1 for large $j$. Since $\Omega_j$ is a nonball, its squared centered graph deviation $T_j$ is positive. The uniform estimate gives

$$
\sigma_1(B_{R_j})-\sigma_1(\Omega_j)
\geq\frac{c_n^*}{m_j}T_j>0,
\tag{7.11}
$$

contradicting (7.1).

All cases are excluded, proving the theorem.



## 8. Scope and further questions

The proof establishes a uniform interval adjacent to maximal boundary measure. The central unresolved question is whether the same ball comparison holds for every perimeter in $(0,\omega_{n-1})$. The present compactness argument does not address counterexample sequences whose perimeters stay in a compact subinterval of that range.

The weighted boundary-center theorem may be useful for other spherical variational problems in which centering and a centered-hemisphere condition must hold simultaneously. The quantitative estimate in Section 4 also records the scale of the deficit near the hemispherical endpoint. Neither observation provides a monotonicity principle for the full Steklov problem.

The argument was written for smooth initial domains. It uses nonsmooth lunes only as limiting domains and fixed trial functions. An extension of the main theorem to nonsmooth initial convex bodies would require an appropriate trace approximation argument.

AI assistance was used in developing and checking the arguments, searching the literature, and preparing this manuscript. Supplementary finite numerical checks are not used as proofs.

## References

[BFNT] D. Bucur, V. Ferone, C. Nitsch, and C. Trombetti, *Weinstock inequality in higher dimensions*, Journal of Differential Geometry 118 (2021), 1-21.

[BHLL] B. Basit, S. Hoehner, Z. Lángi, and J. Ledford, *Steiner symmetrization on the sphere*, [arXiv:2406.10614v3](https://arxiv.org/abs/2406.10614), 2025. Lemma 4.4.

[CGGS] B. Colbois, A. Girouard, C. Gordon, and D. Sher, *Some recent developments on the Steklov eigenvalue problem*, Revista Matemática Complutense 37 (2024), 1-161, [DOI:10.1007/s13163-023-00480-3](https://doi.org/10.1007/s13163-023-00480-3). Open Question 4.27.

[CR] P. Castillon and B. Ruffini, *A spectral characterization of geodesic balls in non-compact rank one symmetric spaces*, Annali della Scuola Normale Superiore di Pisa, Classe di Scienze (5) 19 (2019), 1359-1388.

[CRS] E. Cabezas-Rivas and J. Scheuer, *The quermassintegral-preserving mean curvature flow in the sphere*, Analysis & PDE 17 (2024), 3589-3621, [DOI:10.2140/apde.2024.17.3589](https://doi.org/10.2140/apde.2024.17.3589). Section 2.

[GLMPT] N. Gavitone, D. A. La Manna, G. Paoli, and L. Trani, *A quantitative Weinstock inequality for convex sets*, Calculus of Variations and Partial Differential Equations 59 (2020), article 2, [DOI:10.1007/s00526-019-1642-9](https://doi.org/10.1007/s00526-019-1642-9).

[GWW] C. Gao, Y. Wei, and R. Zhou, *Weinstock inequalities for outward-minimizing domains*, [arXiv:2608.11841v1](https://arxiv.org/abs/2608.11841), 2026.

[KW] K.-K. Kwong and Y. Wei, *Geometric inequalities involving three quantities in warped product manifolds*, Advances in Mathematics 430 (2023), 109213, [DOI:10.1016/j.aim.2023.109213](https://doi.org/10.1016/j.aim.2023.109213).
