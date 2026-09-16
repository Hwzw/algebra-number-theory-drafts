# Sharp total variation bounds from spherical rearrangement

Henry Zweiman

September 16, 2026

## Abstract

We study the sharp control of total variation by a higher derivative under homogeneous endpoint conditions. For every integer $n\ge2$, we prove that the norm of $u\mapsto u'$ from $W_0^{n,2}(0,1)$ to $L^1(0,1)$ is twice the norm of point evaluation into $L^\infty(0,1)$. The extremizers of the two embeddings coincide and are symmetric about the midpoint. This proves the Hilbert-space case of a conjecture of Nazarov and Shcheglova. The main step is a rearrangement principle for a clamped Green operator after projection onto the zero-mean subspace. A Jacobi-polynomial representation identifies its quadratic form with a positive mixture of Poisson interactions on a sphere, where rearrangement reduces the optimization to a cap. We also prove the constant identity and coincidence of maximizing sets at the measure endpoint $p=1$, using the geometry of extreme moment measures and unimodal splines. For each fixed derivative order, we further prove the full variation identity and midpoint-symmetric equality classification on an open interval of exponents around two. A dual optimality equation gives compactness through the highest derivative; polynomial sublevel bounds control the point-evaluation profile on both sides of the Hilbert exponent. At the measure endpoint in derivative order four, we also determine the exact sharp constant and unique symmetric extremizer by a cubic alternation argument and an explicit algebraic exclusion of asymmetric maximizers. An all-order contact-motion argument then proves strict midpoint maximization and the unique symmetric measure extremizer in every order, completing the measure-endpoint conjecture. The full all-exponent conjecture remains open.

## 1. The sharp inequality

All functions and measures in this paper are real. For $1\le p\le\infty$, we use the homogeneous norm $\|u^{(n)}\|_p$ on $W_0^{n,p}(0,1)$. The endpoint conditions are

$$
u^{(j)}(0)=u^{(j)}(1)=0,\qquad 0\le j<n.
\tag{1}
$$

Let $C_{n,p}$ and $V_{n,p}$ denote the sharp constants in

$$
\|u\|_\infty\le C_{n,p}\|u^{(n)}\|_p,
\qquad
\|u'\|_1\le V_{n,p}\|u^{(n)}\|_p.
\tag{2}
$$

The inequality $V_{n,p}\ge2C_{n,p}$ follows from the variation of a function that vanishes at both endpoints. Nazarov and Shcheglova [NS, Conjecture 4.14] conjecture equality for all $n\ge2$ and $1\le p\le\infty$, together with coincidence and midpoint symmetry of the extremizers. Their Remark 4.15 records the previously known case $n=2$.

**Theorem 1.** For every integer $n\ge2$,

$$
V_{n,2}=2C_{n,2}
=\frac{1}{2^{2n-2}(n-1)!\sqrt{2n-1}}.
\tag{3}
$$

The nonzero extremizers are precisely the scalar multiples of the Riesz representer $R_n(\cdot,1/2)$ of evaluation at $1/2$ in $W_0^{n,2}(0,1)$. In particular, the maximizing sets in (2) coincide, and their elements are even about $1/2$.

The point-evaluation formula used here is prior work. Kalyabin [K, Theorem 2] gives, after affine rescaling,

$$
\|\operatorname{ev}_a\|^2
=\frac{[a(1-a)]^{2n-1}}{(2n-1)((n-1)!)^2}.
\tag{4}
$$

Our contribution is the upper bound for the variation norm and its equality classification, obtained through the rearrangement principle in Section 3. Best polynomial approximation already occurs in this embedding problem [GS]. The sharp $W_0^{m,2}$ to $L^1$ embedding of the function itself was proved by Hindov, Nitzan, Olsen and Rydhe [HNOR]; their theorem does not include the additional zero-mean constraint on a derivative that appears below.

## 2. A Jacobi representation of the clamped Green form

Fix $m\ge1$, and set

$$
w(x)=x^m(1-x)^m,\qquad
M=\int_0^1w(x)\,dx=\frac{(m!)^2}{(2m+1)!},
\qquad d\pi(x)=M^{-1}w(x)\,dx.
\tag{5}
$$

Let $h_k$ be the orthonormal polynomials for $\pi$, with positive leading coefficients. These are normalized shifted Jacobi polynomials with parameters $(m,m)$; in particular $h_0=1$. Put

$$
v_k=wh_k,\qquad \lambda_k=\frac{(k+2m)!}{k!}.
\tag{6}
$$

**Lemma 2.** The functions $v_k/\sqrt{M\lambda_k}$ form an orthonormal basis of $H=W_0^{m,2}(0,1)$ in its energy inner product. Moreover,

$$
(-1)^m v_k^{(2m)}=\lambda_k h_k.
\tag{7}
$$

*Proof.* The left side of (7) has degree $k$. If $q$ is a polynomial of degree less than $k$, integration by parts $2m$ times yields

$$
\int_0^1 (wh_k)^{(2m)}wq
=\int_0^1 wh_k(wq)^{(2m)}=0.
\tag{8}
$$

Every boundary term vanishes because one of its two factors has fewer than $m$ derivatives and retains an endpoint zero. Orthogonality therefore shows that the left side of (7) is proportional to $h_k$. Comparing leading coefficients proves (7). A further integration by parts gives

$$
\langle v_k,v_\ell\rangle_H=M\lambda_k\delta_{k\ell}.
\tag{9}
$$

If $y\in H$ is orthogonal to every $v_k$, weak integration by parts gives $\int_0^1 yh_k=0$ for every $k$. The $h_k$ span the polynomials, which are dense in $C[0,1]$, so $y=0$. This proves completeness. $\square$

The mean functional $y\mapsto\int_0^1y$ has Riesz representer $v_0/\lambda_0=w/(2m)!$. Therefore

$$
H_*:=\left\{y\in H:\int_0^1y=0\right\}
\tag{10}
$$

is obtained by removing the zeroth basis vector. For a bounded real load $g$, Parseval gives the squared dual norm of $y\mapsto\int gy$ on $H_*$:

$$
Q_m(g)
=M\sum_{k\ge1}\frac{\left|\int_0^1gh_k\,d\pi\right|^2}{\lambda_k}.
\tag{11}
$$

Equivalently, if $G_m$ is the clamped Green kernel and $w_m=w/(2m)!$, then

$$
Q_m(g)=\iint g(x)G_m(x,t)g(t)\,dx\,dt
-\frac{\left(\int gw_m\right)^2}{\int w_m}.
\tag{12}
$$

Formula (11) is sufficient for the proof and avoids any pointwise convergence issue for a Green series.

## 3. Spherical rearrangement of the load

Set $d=2m+2$ and let $\sigma$ be normalized surface measure on $S^d$. The coordinate $x=(1+\xi_{d+1})/2$ has law $\pi$. Thus

$$
F(\xi)=g\!\left(\frac{1+\xi_{d+1}}2\right)
\tag{13}
$$

identifies $L^2(\pi)$ with the zonal subspace of $L^2(S^d)$. Under this identification, $h_k$ is the normalized zonal harmonic of degree $k$. This follows from the orthogonal decomposition of polynomials into spherical harmonics: a zonal polynomial of degree $k$ orthogonal to all lower zonal degrees has only its degree-$k$ component.

The spherical Poisson operator $P_r$, $0<r<1$, has eigenvalue $r^k$ on degree-$k$ harmonics and kernel

$$
K_r(\xi\cdot\eta)
=\frac{1-r^2}{(1-2r\xi\cdot\eta+r^2)^{(d+1)/2}}.
\tag{14}
$$

We use normalized surface measure, as in [ABR, (1.15)]. The eigenvalue follows by harmonic extension of a homogeneous harmonic polynomial. The beta integral gives

$$
\frac1{\lambda_k}
=\frac1{(2m-1)!}\int_0^1r^k(1-r)^{2m-1}\,dr.
\tag{15}
$$

Tonelli's theorem applied to the nonnegative spectral terms in (11) therefore gives

$$
Q_m(g)=\frac{M}{(2m-1)!}\int_0^1(1-r)^{2m-1}
\left(\langle F,P_rF\rangle-\left(\int F\,d\sigma\right)^2\right)dr.
\tag{16}
$$

The deletion of the constant harmonic is exactly the mean subtraction needed in (12).

**Theorem 3.** If $A\subset(0,1)$ is measurable and $a\in[0,1]$ satisfies $\pi(A)=\pi([0,a])$, then

$$
Q_m(\mathbf1_A)\le Q_m(\mathbf1_{[0,a]}).
\tag{17}
$$

If $0<\pi(A)<1$, equality holds only when $A$ agrees, up to null sets, with an interval abutting one endpoint and having that $\pi$-measure.

*Proof.* Lift $A$ to the zonal subset $E\subset S^d$ using (13). For fixed $r$, $K_r$ is positive, bounded and strictly decreasing in geodesic distance. Spherical rearrangement [BH, Theorem 2] maximizes the self-interaction of $\mathbf1_E$ at fixed surface measure by a cap. Choose that cap about the negative coordinate axis. It corresponds to $[0,a]$. The mean term in (16) is unchanged, and integration proves (17).

For clarity, the equality hypotheses in [BH] are satisfied with two functions and integrand $(s,t)\mapsto st$. Its mixed finite difference is strictly positive; the kernel is positive and strictly decreasing; and the nontrivial indicators are nonconstant with finite interaction. Hence equality at fixed $r$ forces $E$ to be a cap up to rotation. If equality holds in (17), the nonnegative rearrangement deficit has zero integral in (16), so equality holds for almost every $r$, and in particular for one $r\in(0,1)$. Thus $E$ is a cap.

Its axis must be the original coordinate axis up to reversal. Indeed, zonal invariance makes the centroid of $E$ parallel to that axis. A nontrivial cap has a nonzero centroid parallel to its own axis. Consequently $A$ is an endpoint interval, as claimed. $\square$

The same argument proves a broader load rearrangement statement. For a bounded real $g$, let $g^\downarrow$ be its nonincreasing equimeasurable rearrangement relative to $\pi$. Adding a constant makes $g$ nonnegative without changing $Q_m$. Applying [BH] in (16) gives

$$
Q_m(g)\le Q_m(g^\downarrow).
\tag{18}
$$

This is rearrangement of a load in a Green quadratic form. It does not assert that ordinary rearrangement preserves a higher derivative norm.

## 4. Proof of Theorem 1

Put $m=n-1$. The map $u\mapsto y=u'$ is an isometric bijection from $W_0^{n,2}$ to $H_*$: integrating $y$ recovers $u$, and the zero-mean condition supplies $u(1)=0$.

Duality gives

$$
V_{n,2}^2=\sup_{|g|\le1}Q_m(g)
=4\sup_A Q_m(\mathbf1_A).
\tag{19}
$$

To justify the second equality, write a bounded $g$ with $|g|\le1$ as the average of $\operatorname{sign}(g-s)$ over uniform $s\in[-1,1]$. Convexity of the squared Hilbert dual norm bounds its value by the supremum over sign functions. Constants are annihilated in (11), giving $Q_m(2\mathbf1_A-1)=4Q_m(\mathbf1_A)$.

For an endpoint interval,

$$
\int_0^a y(x)\,dx=u(a),
\qquad Q_m(\mathbf1_{[0,a]})=\|\operatorname{ev}_a\|^2.
\tag{20}
$$

Theorem 3, (4), and (19) now prove (3). In particular, the maximizing interval is a half-interval.

Suppose that $u\ne0$ attains equality, and take $g=\operatorname{sign}(u')$, choosing either sign where $u'=0$. Both signs occur on sets of positive measure. Equality in the Hilbert dual bound and in Theorem 3 forces $g$ to be a half-interval sign function, up to its global sign and null sets. Its functional on $H_*$ is $\pm2u(1/2)$. Equality in Cauchy--Schwarz therefore makes $u$ a scalar multiple of $R_n(\cdot,1/2)$.

Conversely, this representer maximizes point evaluation. Its variation is at least twice its maximum and at most the bound just proved, so it also maximizes variation. Formula (4) has its unique maximum at $a=1/2$, and uniqueness of a Hilbert-space Riesz representer gives precisely the same classification for the point-norm extremizers. Finally, reflection preserves the energy inner product and fixes evaluation at $1/2$, so uniqueness makes $R_n(\cdot,1/2)$ reflection invariant. $\square$

## 5. The measure endpoint

Let $\mathcal M_n$ consist of real finite signed measures $\mu$ on $[0,1]$ such that

$$
\|\mu\|_{\mathrm{TV}}\le1,
\qquad \int_0^1t^j\,d\mu(t)=0\quad(0\le j<n).
\tag{21}
$$

Their compactly supported potentials are

$$
U_\mu(x)=\int_0^1\frac{(x-t)_+^{n-1}}{(n-1)!}\,d\mu(t).
\tag{22}
$$

The moments make $U_\mu$ vanish off $[0,1]$, and $D^nU_\mu=\mu$. For $n\ge2$, $U_\mu$ is continuous and absolutely continuous, with integrable first derivative. Endpoint atoms are allowed in this relaxed formulation.

**Theorem 4.** For every $n\ge2$,

$$
\sup_{\mu\in\mathcal M_n}\|U_\mu'\|_1
=2\sup_{\mu\in\mathcal M_n}\|U_\mu\|_\infty.
\tag{23}
$$

The maximizing measures for the two quantities coincide. The relaxed constants equal $V_{n,1}$ and $C_{n,1}$, respectively. No symmetry assertion at $p=1$ is included.

*Proof of the constant identity.* Every extreme point of $\mathcal M_n$ has norm one and exactly $n+1$ support points. To prove the support bound, suppose $\mu$ has norm one and at least $n+2$ disjoint Borel sets of positive $|\mu|$-measure. A nonzero function $h$ constant on those sets can satisfy the $n$ equations $\int t^jh\,d\mu=0$ and the extra equation $\int h\,d|\mu|=0$. Then $(1\pm\varepsilon h)\mu$ are distinct norm-one admissible measures for small $\varepsilon$. Such a $\mu$ is not extreme. A nonzero measure of norm less than one is excluded by scalar perturbation. Zero is the midpoint of opposite nonzero moment measures, which exist on any $n+1$ distinct nodes, and is not extreme either. A nonzero measure on at most $n$ points is excluded by the Vandermonde determinant.

On nodes $t_0<\cdots<t_n$, the moment nullspace is one-dimensional, with weights

$$
b_i=\prod_{j\ne i}(t_i-t_j)^{-1}.
\tag{24}
$$

Thus every extreme measure is a normalized signed multiple of $\sum_i b_i\delta_{t_i}$. Its potential is a B-spline, up to scale and sign. More explicitly, the Genocchi--Hermite identity [dB, (52)] identifies

$$
\rho(x)=n\sum_{i=0}^n b_i(t_i-x)_+^{n-1}
=(-1)^n n!\,U_{\sum b_i\delta_{t_i}}(x)
\tag{25}
$$

with the density of $\sum_i t_iX_i$, where $X$ is uniform on the standard $n$-simplex. After parallel sections of the simplex are identified by translation, their Minkowski interpolation is contained in the section at the interpolated coordinate. The classical Brunn--Minkowski inequality [GHW, (3), $p=1$] therefore makes their volumes to the power $1/(n-1)$ concave. The coarea factor relating section volume to $\rho$ is constant, so $\rho^{1/(n-1)}$ is concave and $\rho$ is unimodal. It is positive between its end knots, continuous, and zero at those knots. Every extreme potential therefore satisfies

$$
\|U_\mu'\|_1=2\|U_\mu\|_\infty.
\tag{26}
$$

Write $C=\sup_{\mathcal M_n}\|U_\mu\|_\infty$. The set $\mathcal M_n$ is weak-star compact. Moreover, $\mu\mapsto\|U_\mu'\|_1$ is weak-star lower semicontinuous: it is the supremum of the continuous linear functionals $\int H_g\,d\mu$, where $|g|\le1$ and

$$
H_g(t)=\int_t^1\frac{(x-t)^{n-2}}{(n-2)!}g(x)\,dx.
\tag{27}
$$

Its sublevel set at $2C$ is closed and convex and contains all extreme points by (26). Krein--Milman therefore gives the upper bound in (23). The elementary variation lower bound gives the reverse inequality. The height supremum is attained: on the bounded measure set, joint continuity of the kernels in (22) makes the potential map weak-star to uniform continuous. Consequently the variation supremum is attained as well.

*Coincidence.* Let $\mu$ maximize variation, choose $g=\operatorname{sign}(U_\mu')$, and let $\mathcal F$ be the compact exposed face on which $\int H_g\,d\nu=2C$. Its extreme points are extreme in $\mathcal M_n$. For each such point $e$,

$$
2C=\int gU_e'\le\|U_e'\|_1=2\|U_e\|_\infty\le2C.
\tag{28}
$$

Thus $g$ agrees with the sign of $U_e'$ wherever the latter is nonzero, and every $U_e$ maximizes height. Its end knots must be $0$ and $1$: a potential supported on a shorter interval of length $L$ can be stretched to $[0,1]$, keeping its derivative-measure norm one and multiplying its height by $L^{1-n}>1$.

All $U_e$ have the same global sign, since opposite signs give opposite nonzero derivatives on a common interval near zero, contradicting their agreement with $g$. Change that common sign to positive. Concavity of $U_e^{1/(n-1)}$ makes its maximum set a closed interval, with strictly positive derivative almost everywhere before it and strictly negative derivative almost everywhere after it. Two disjoint maximum intervals would again force contradictory signs for $g$. The maximum intervals therefore intersect pairwise, and hence have a common point $a_*$. All $U_e(a_*)=C$. Evaluation is weak-star continuous, so Krein--Milman applied to $\mathcal F$ gives $U_\mu(a_*)=C$. Conversely, a height maximizer is a variation maximizer by the already proved constant identity.

*Recovery of the ordinary constants.* For an ordinary admissible $u$, the measure $u^{(n)}dx$ satisfies (21). Conversely, mollify the zero extension of $U_\mu$ with a nonnegative mollifier supported in $[-\varepsilon,\varepsilon]$, obtaining $U_\varepsilon$. With $a=1+2\varepsilon$, set

$$
u_\varepsilon(x)=a^{1-n}U_\varepsilon(ax-\varepsilon).
\tag{29}
$$

It is smooth, supported on $[0,1]$, satisfies all endpoint conditions, and has $\|u_\varepsilon^{(n)}\|_1\le1$. Its maximum and variation converge to those of $U_\mu$, by uniform convergence of the potential mollification and $L^1$ convergence of its first derivative. This proves equality of the relaxed and ordinary sharp constants. The proof classifies coincidence of relaxed maximizers and does not assert attainment in the ordinary $W_0^{n,1}$ class. $\square$

## 6. An open interval of exponents

The Hilbert theorem also yields a neighborhood of exponents for each fixed derivative order. The interval is not asserted to be uniform in the order. In this section write $X_{n,p}=W_0^{n,p}(0,1)$ for the clamped space defined by (1), with norm $\|u^{(n)}\|_p$.

**Theorem 5 (local continuation in the exponent).** For every fixed integer $n\ge3$, there exists $0<\varepsilon_n<1$ such that, if $|p-2|<\varepsilon_n$, then

$$
V_{n,p}=2C_{n,p}.
\tag{6.1}
$$

All nonzero extremizers in the two inequalities are the scalar multiples of the unique positive norm-one extremizer for evaluation at $1/2$. They are symmetric about the midpoint and, after a choice of global sign, have strictly positive derivative on $(0,1/2)$ and strictly negative derivative on $(1/2,1)$.

The radius is allowed to depend on $n$ and is not estimated here. The theorem does not reach all $1<p<\infty$, give an interval uniform in $n$, or settle the remaining endpoint symmetry questions.

### 6.1. Dual representation and compactness of variation maximizers

Let $\mathcal P_{n-1}$ denote the polynomials of degree at most $n-1$. Integration from the left endpoint identifies $X_{n,p}$ isometrically with

$$
Z_{n,p}=\{f\in L^p(0,1):\int_0^1t^jf(t)\,dt=0,\ 0\le j<n\}.
\tag{6.2}
$$

Indeed $u(x)=\int_0^x(x-t)^{n-1}f(t)/(n-1)!\,dt$; the right endpoint conditions are equivalent to the displayed moments. For bounded $g$, put

$$
H_g(t)=\int_t^1\frac{(x-t)^{n-2}}{(n-2)!}g(x)\,dx.
\tag{6.3}
$$

Fubini gives $\int gu'=\int H_gf$. If $q=p/(p-1)$, the norm of this functional on $Z_{n,p}$ equals

$$
\min_{P\in\mathcal P_{n-1}}\|H_g-P\|_q.
\tag{6.4}
$$

Here is a direct justification without a quotient-duality assumption. A minimizing polynomial exists by finite-dimensional coercivity and is unique for $q>1$. Its residual $R=H_g-P$ satisfies

$$
\int_0^1 |R|^{q-2}R\,Q=0\qquad(Q\in\mathcal P_{n-1}).
\tag{6.5}
$$

If $R\ne0$, the function $f=\operatorname{sign}(R)|R/\|R\|_q|^{q-1}$ has $L^p$ norm one and belongs to (6.2). It realizes the bound in Hölder's inequality. The zero-residual case is immediate. This proves (6.4).

For every fixed $p>1$, the variation supremum is attained. A norm-bounded sequence is bounded in $W^{n,p}$ by successive integration, and its derivatives through order $n-1$ are uniformly bounded and equicontinuous, using Hölder's inequality for the highest integral. A subsequence converges uniformly through order $n-1$, and the highest derivatives have a weakly convergent subsequence in $L^p$. The limit satisfies all endpoint conditions, has norm at most one, and retains the limiting variation. The supremum is positive, so a maximizer must have norm exactly one by scaling.

For a norm-one variation maximizer $u$, choose $g=\operatorname{sign}(u')$, with any value in $[-1,1]$ on the zero set. The functional in (6.4) is at most $V_{n,p}$, since $\int gv'\le\|v'\|_1$. On $u$ it equals $V_{n,p}$. Thus its residual satisfies $\|R\|_q=V_{n,p}$, and equality in Hölder gives

$$
u^{(n)}(t)=\operatorname{sign}R(t)
\left|\frac{R(t)}{V_{n,p}}\right|^{q-1}.
\tag{6.6}
$$

This formula gives more compactness than the original Sobolev bound.

**Lemma 6 (compactness of maximizers).** Suppose $p_j\to2$ and $u_j$ is any sequence of norm-one variation maximizers in $X_{n,p_j}$. Then, after a subsequence and a choice of global signs, $u_j$ converges in $C^n[0,1]$ to the positive norm-one Hilbert maximizer $u_*$.

*Proof.* Restrict to $3/2\le p_j\le5/2$, so $5/3\le q_j\le3$. The functions $H_{g_j}$, with $|g_j|\le1$, are uniformly bounded and Lipschitz. For $n=2$, this follows directly from $H_g'=-g$; for $n\ge3$, differentiate (6.3) once and bound its remaining integral.

The minimizing polynomials satisfy
$\|P_j\|_{q_j}\le2\|H_{g_j}\|_{q_j}$.
Their coefficients are uniformly bounded. To verify the needed uniform norm equivalence, a contrary sequence of polynomials can be normalized to have coefficient norm one and $L^{q_j}$ norm tending to zero. A coefficient-convergent subsequence would give a nonzero polynomial vanishing almost everywhere, a contradiction. Consequently both $P_j$ and their derivatives are uniformly bounded, and the residuals $R_j$ are uniformly bounded and Lipschitz.

The quantities $V_{n,p_j}$ are bounded above by (6.4) with the zero polynomial. They are bounded away from zero by testing the one fixed nonzero function $u_*$, whose highest derivative is bounded. Formula (6.6) now makes $u_j^{(n)}$ uniformly bounded and equicontinuous. For example, signed power maps with exponent in $[2/3,2]$ on a fixed bounded interval have a common Hölder modulus with exponent $2/3$, after enlarging the constant. Arzelà--Ascoli supplies a uniformly convergent subsequence of the highest derivatives. Integration and the left endpoint conditions give convergence in $C^n$ to some $u$.

Uniform boundedness and $p_j\to2$ imply
$\int |u^{(n)}|^2=\lim_j\int|u_j^{(n)}|^{p_j}=1$.
All right endpoint conditions pass to the limit. Also
$\|u'\|_1=\lim_jV_{n,p_j}$.
Testing $u_*/\|u_*^{(n)}\|_{p_j}$ gives
$\liminf_j V_{n,p_j}\ge V_{n,2}$, while the Hilbert inequality applied to the limit gives the reverse bound. Thus $u$ is a Hilbert maximizer. Theorem 1 identifies it with $u_*$ or $-u_*$, proving the lemma. $\square$

### 6.2. Persistence of a single peak

We give the details that weak or uniform convergence alone would miss. The Hilbert midpoint representer, up to a positive factor, can be written

$$
U(x)=F(|1-2x|),\qquad
F(z)=\int_z^1(t^2-z^2)^{n-1}\,dt,
\quad 0\le z\le1.
\tag{6.7}
$$

To check this representation, expand the integrand. The resulting expression for $F$ is an even polynomial of degree at most $2n-2$, plus a multiple of $z^{2n-1}$. Thus (6.7) is polynomial of degree at most $2n-1$ on each half-interval and has matching derivatives through order $2n-2$ at the midpoint. Near $z=1$, writing $t=z+(1-z)s$ shows that $F(z)$ is a positive constant times $(1-z)^n$, to leading order. Therefore all endpoint derivatives below order $n$ vanish. The jump of the derivative of order $2n-1$ is nonzero. The weak derivative $(-1)^nD^{2n}U$ is a scalar multiple of the midpoint delta. Testing against $U$ shows this scalar is positive because $\int|U^{(n)}|^2>0$ and $U(1/2)>0$. Uniqueness of the Riesz representer proves the claim up to positive normalization.

For $n\ge2$, differentiation gives

$$
F'(z)=-2(n-1)z\int_z^1(t^2-z^2)^{n-2}\,dt<0
\qquad(0<z<1).
\tag{6.8}
$$

Also $F''(0)=-2(n-1)/(2n-3)<0$. Hence
$u_*'>0$ on $(0,1/2)$, $u_*'<0$ on $(1/2,1)$, and $u_*''(1/2)<0$. The endpoint expansion gives
$u_*^{(n)}(0)>0$ and $(-1)^nu_*^{(n)}(1)>0$.

These properties imply that every sufficiently close $C^n$ perturbation satisfying the same clamped endpoint conditions has exactly one interior critical point, a strict maximum. Indeed, near zero its highest derivative remains positive and

$$
u'(x)=\int_0^x\frac{(x-t)^{n-2}}{(n-2)!}u^{(n)}(t)\,dt>0.
\tag{6.9}
$$

The reflected argument gives negativity near one. On compact intervals away from the endpoints and midpoint the strict derivative signs persist. On a small interval about the midpoint, the second derivative stays negative, so there is precisely one zero of the first derivative, bracketed by its signs on either side.

Lemma 6 therefore implies that for all $p$ sufficiently close to two, every norm-one variation maximizer is, up to sign, positive and strictly unimodal. Such a maximizer has variation exactly twice its height. Since every admissible function has variation at least twice its height, this proves (6.1). It also proves coincidence of maximizing sets: a variation maximizer has height $C_{n,p}$, and every height maximizer has variation between $2C_{n,p}$ and $V_{n,p}$.

The only conclusion still needed for the local theorem is midpoint symmetry. Single-peak geometry by itself does not supply it.

### 6.3. Smoothness of the point-evaluation profile near two

Let $m=n-1\ge2$, and define

$$
K_a(t)=\frac{(a-t)_+^m}{m!},\qquad
J(q,a)=\min_{P\in\mathcal P_m}\int_0^1|K_a-P|^q\,dt.
\tag{6.10}
$$

By the same moment argument as (6.4), the evaluation norm is $J(q,a)^{1/q}$. We need uniform continuity on the whole interval in $a$, and twice continuous differentiability in $a$ near $(q,a)=(2,1/2)$.

First, minimizing polynomials have coefficients bounded uniformly for $q$ in a compact subset of $(1,\infty)$ and $a\in[0,1]$, by the argument used above. On this bounded coefficient set the integrands in (6.10) vary continuously with $(q,a,P)$, uniformly in $t$. Minimizing over that compact set proves continuity of $J$, including uniform convergence $J(q,\cdot)\to J(2,\cdot)$ as $q\to2$. Strict convexity gives a unique minimizing polynomial; compactness and uniqueness prove continuous dependence of its coefficients.

The following elementary sublevel estimate handles exponents just below two. If $P$ is a polynomial of degree at most $m$ on an interval $I$ of length bounded above and below, and $\|P\|_{L^\infty(I)}\ge b>0$, then

$$
|\{t\in I:|P(t)|\le h\}|\le C(m,b,I)h^{1/m}
\qquad(0<h<1).
\tag{6.11}
$$

The constant is uniform for intervals in the stated length range. To prove this, let the sublevel set have length $\ell>0$. Divide its mass into sufficiently many equal portions and choose $m+1$ points from alternate portions. They can be chosen in the sublevel set with consecutive separations bounded below by a fixed multiple of $\ell/(m+1)$: coordinate separation is at least the measure of the intervening portion. Lagrange interpolation at these points gives $\|P\|_\infty\le C_m h\ell^{-m}$, with the interval-length factor absorbed into the constant. Rearrangement gives (6.11); approximation of the chosen points handles essential rather than attained sublevel membership.

Consequently, for $0<s<1/m$, integration of distribution functions gives

$$
\int_{\{|P|<h\}}|P|^{-s}\,dt\le C h^{1/m-s}.
\tag{6.12}
$$

For example, split the region into dyadic bands $2^{-k-1}h\le|P|<2^{-k}h$, apply (6.11) to each, and sum the convergent geometric series. The estimates also show uniform integrability of these inverse powers.

At $(q,a)=(2,1/2)$, the minimizing residual in (6.10) is a nonzero polynomial on each of the two half-intervals. If it were identically zero on one half, its orthogonality to constants would fail on the other: the remaining residual would be a nonzero constant multiple of the nonnegative truncated power. Continuity of the coefficients therefore supplies a uniform positive lower bound for the sup norm of each polynomial piece on its own interval when $(q,a)$ and the polynomial coefficients are sufficiently close to this point. The intervals' lengths also stay bounded away from zero. Thus (6.11)--(6.12) apply uniformly to both pieces.

Write $P_c(t)=\sum_{j=0}^mc_jt^j$ and $R=K_a-P_c$. The normal equations are

$$
\mathcal N_j(q,a,c)=\int_0^1|R|^{q-2}R\,t^j\,dt=0,
\qquad 0\le j\le m.
\tag{6.13}
$$

Take a small open neighborhood with $q>2-1/(2m)$. The equations are continuously differentiable in $(q,a,c)$ there. Their derivatives in $(a,c)$ are obtained by multiplying the variation of $R$ by $(q-1)|R|^{q-2}$, and the derivative in $q$ has integrand $|R|^{q-2}R\log|R|\,t^j$, with value zero at $R=0$. These assertions follow first away from a small sublevel set of $R$, by ordinary differentiation. The uniform bound (6.12) makes the omitted derivatives uniformly integrable and arbitrarily small as the sublevel threshold tends to zero. The logarithmic derivative is bounded by a constant times a small positive power of $|R|$ near zero. This also proves continuity of the derivatives by splitting into the same two regions. The moving interface $t=a$ causes no additional term, since $K_a$ and its first $a$-derivative are continuous there for $m\ge2$.

At the base point, the coefficient derivative of (6.13) is the negative definite Gram matrix $-[\int_0^1t^{i+j}\,dt]_{i,j=0}^m$. The finite-dimensional implicit function theorem yields a continuously differentiable coefficient map $c(q,a)$. It is the minimizing polynomial map by strict convexity and continuity already established.

The envelope derivative and its second derivative are

$$
\begin{aligned}
J_a&=q\int |R|^{q-2}R K_a^{[1]},\\
J_{aa}&=q(q-1)\int |R|^{q-2}
\bigl(K_a^{[1]}-P_{c_a}\bigr)K_a^{[1]}
+q\int |R|^{q-2}R K_a^{[2]},
\end{aligned}
\tag{6.14}
$$

where
$K_a^{[1]}=(a-t)_+^{m-1}/(m-1)!$ and
$K_a^{[2]}=(a-t)_+^{m-2}/(m-2)!$.
For $m=2$, the last expression is the indicator of $t<a$, with its value at $t=a$ immaterial. The coefficient term in the first derivative vanishes by (6.13). The second derivative exists and is continuous by (6.12), boundedness of these kernels, and dominated convergence away from the moving interface. In particular no claim that all residual roots are simple is needed.

At $q=2$, the credited point-evaluation formula (4) gives

$$
J(2,a)=\frac{[a(1-a)]^{2n-1}}{(2n-1)((n-1)!)^2}.
\tag{6.15}
$$

It has a unique maximum at $a=1/2$, with strictly negative second derivative there. By continuity of (6.14), it follows that $J(q,\cdot)$ is strictly concave on one fixed neighborhood of $1/2$, for all $q$ close enough to two. Uniform convergence on $[0,1]$ forces every global maximum into that neighborhood. Reflection of the original evaluation problem gives $J(q,a)=J(q,1-a)$. Strict concavity and this symmetry show that $1/2$ is the unique global maximizing point.

### 6.4. Completion of the proof

Shrink $\varepsilon_n$ so that both the variation-maximizer argument and the evaluation-profile argument apply. We have established the constant identity and coincidence of maximizing sets. Every height maximizer must realize evaluation at its absolute maximum, and Section 6.3 forces that point to be $1/2$. The norm-one positive evaluation extremizer is unique by equality in Hölder in (6.4), or by strict convexity of the unit ball of $L^p$. Reflection preserves the norm and evaluation at $1/2$, so uniqueness makes this function midpoint symmetric. Section 6.2 already gives its strict derivative signs and its unique peak. This proves Theorem 5. $\square$

### 6.5. The unresolved global step

**Compactness away from the endpoints of the exponent range.** The argument in Lemma 6 gives the following more general statement. If $p_j\to p_0\in(1,\infty)$ and $u_j$ are norm-one variation maximizers, a subsequence converges in $C^n$ to a norm-one variation maximizer at $p_0$, and $V_{n,p_j}\to V_{n,p_0}$. To see this, keep $p_j$ in any fixed compact subinterval of $(1,\infty)$; the exponents $q_j-1$ then have a positive lower bound, so (6.6) still gives a common Hölder modulus. The limit has norm one at $p_0$. For the lower bound on the limiting optimal value, test a maximizer at $p_0$; (6.6) makes its highest derivative bounded, so it is admissible at all nearby exponents and its varying norms converge. The upper bound follows by applying the $p_0$ inequality to the limit. This proves the statement without assuming uniqueness or symmetry at $p_0$.

Thus a local continuation criterion at another exponent is available: if all its normalized variation maximizers are scalar-sign copies of one single-peak function with nonzero endpoint highest derivatives and a nondegenerate peak, and its point-evaluation profile has a unique midpoint maximum with a continuously persisting negative second derivative, the same argument proves the conjecture in a neighborhood of that exponent. These hypotheses must be established there; they cannot be imported from the case $p=2$.

The strongest compactness assertion here is $C^n$ convergence of *variation maximizers*, established from their dual optimality equation. It is not asserted for arbitrary normalized Sobolev sequences. This distinction is necessary to preserve the derivative signs near the clamped endpoints.

The point-profile calculation uses finite-dimensional best approximation only after proving uniform control of possible multiple zeros in its polynomial residual. Omitting (6.11)--(6.12) would leave the two-sided neighborhood in $p$ unjustified, since $q<2$ creates negative powers at residual zeros.

This argument does not prove that the set of valid exponents is closed. At a hypothetical first exponent where the result ceases to hold, compactness of the old single-peak branch does not exclude a different multiple-peak global maximizer with the same value. Nor does local strict concavity of the point-evaluation profile exclude a remote competing maximum at other exponents. These are substantive global obstacles, not consequences of the implicit function theorem.

The remaining task is to exclude such competing branches or to find a counterexample. Theorem 5 supplies a local result, not the full conjecture. No numerical experiment is used in its proof.


## 7. Complete symmetry at the fourth-order measure endpoint

We first settle the endpoint symmetry problem explicitly in order four by a finite alternation argument. The theorem below concerns the measure class (21); its constants also apply to the ordinary clamped Sobolev space by Theorem 4.

**Theorem 8 (fourth-order endpoint).** One has

$$
C_{4,1}=\frac1{1296},\qquad V_{4,1}=\frac1{648}.
\tag{7.1}
$$

The norm-one relaxed extremizers for height and variation are exactly $\mu_*$ and $-\mu_*$, where

$$
\mu_* =\frac19(\delta_0+\delta_1)
-\frac14(\delta_{1/6}+\delta_{5/6})
+\frac5{18}\delta_{1/2}.
\tag{7.2}
$$

Their potentials are even about $1/2$. No nonzero extremizer exists in the ordinary $W_0^{4,1}$ class. Thus the full constant, coincidence and symmetry assertions in [NS, Conjecture 4.14] hold for $n=4$, $p=1$, with the endpoint understood in the measure sense.

The all-order symmetry assertion is proved separately in Section 8. The point estimates for orders two and three are already included in [NS, Theorem 4.5]; those cases are not new here.

### 7.1. Extreme measures and a dual cubic

Let $C$ be the maximal relaxed height. It is positive and attained by Section 5. Choose a maximizing point and sign. The corresponding evaluation functional exposes a nonempty compact face of $\mathcal M_4$. An extreme point of that face is extreme in $\mathcal M_4$ and still maximizes height. By the moment-circuit argument in Theorem 4, after choosing its positive potential it has nodes

$$
\begin{gathered}
0<a<b<c<1,\qquad (t_0,t_1,t_2,t_3,t_4)=(0,a,b,c,1),\\
\mu=\frac1D\sum_{i=0}^4\beta_i\delta_{t_i},\qquad
\beta_i=\prod_{j\ne i}(t_i-t_j)^{-1},\qquad D=\sum_i|\beta_i|.
\end{gathered}
\tag{7.3}
$$

The end nodes are $0$ and $1$ because stretching a shorter support, with derivative-measure norm fixed, multiplies height by the inverse cube of its length. The signs of the weights in (7.3) are $+,-,+,-,+$.

Write $U$ for this positive potential and let $x$ maximize it. Before $a$ it is a positive multiple of $x^3$; after $c$ it is a positive multiple of $(1-x)^3$. Its derivatives at $a$ and $c$ have strict opposite signs. Hence $a<x<c$. Reflecting if necessary, assume

$$
a<x\le b<c<1.
\tag{7.4}
$$

Put $K_x(t)=(x-t)_+^3/6$. There is a polynomial $P$ of degree at most three such that

$$
R(t)=K_x(t)-P(t),\qquad
\|R\|_\infty=C,\qquad
(R(0),R(a),R(b),R(c),R(1))=(C,-C,C,-C,C).
\tag{7.5}
$$

Here are the duality details. The dual of $C[0,1]/\mathcal P_3$ is the space of finite measures annihilating $\mathcal P_3$, with total-variation norm. Hahn-Banach and the Riesz representation theorem therefore identify the distance of $K_x$ to $\mathcal P_3$ with the norm of its evaluation functional on $\mathcal M_4$. That norm equals $C$, because the chosen measure attains the global height. A best polynomial exists by finite-dimensional coercivity. Equality in $\int R\,d\mu\le\|R\|_\infty\|\mu\|_{\mathrm{TV}}$ forces the five values in (7.5). Since $R$ is continuously differentiable, its derivative vanishes at $a,b,c$.

Let $R_+=-P$, so that $R=R_+$ on $[x,1]$. The cubic $R_+$ has a maximum at $b$ and a minimum at $c$. Consequently, for some $k>0$,

$$
R_+'(t)=k(t-b)(t-c).
\tag{7.6}
$$

Equality of its values at $b$ and $1$ gives, on putting $h=c-b$,

$$
1-b=\frac32h,\qquad
b=1-\frac32h,\qquad c=1-\frac12h.
\tag{7.7}
$$

Indeed $\int_b^1(t-b)(t-c)dt=(1-b)^2((1-b)/3-h/2)=0$.

### 7.2. The remaining algebraic constraints

On the left of $x$, $R(t)=R_+(t)+(x-t)^3/6$. The equations $R'(a)=0$ and $R(a)=R(c)$ yield

$$
(x-a)^2=2k(b-a)(c-a),\qquad
(x-a)^3=k(c-a)^2(2(c-a)-3h).
\tag{7.8}
$$

Set $v=(c-a)/h>1$. Dividing the two equations, and using $0<x-a\le b-a$, gives

$$
\frac32<v\le2,\qquad
 a=1-h\left(v+\frac12\right),\qquad
 x=1-\frac{h(2v-1)}{2(v-1)}.
\tag{7.9}
$$

For clarity, $(x-a)/h=v(2v-3)/(2(v-1))$. Its positivity gives $v>3/2$, and its upper bound $v-1$ gives $v\le2$.

The potential itself is stationary at $x$. Only the nodes $0,a$ contribute to its first derivative under (7.4), so $U'(x)=0$ reads

$$
(x-a)^2=x^2\frac{(b-a)(c-a)(1-a)}{bc}.
\tag{7.10}
$$

Combining this with (7.8) gives $k=x^2(1-a)/(2bc)$. Also $R(0)=R(1)$ implies

$$
\frac{x^3}{6}
=k\int_0^1(t-b)(t-c)dt
=\frac{k b^2}{3},\qquad
x=\frac{b(1-a)}c.
\tag{7.11}
$$

The integral equals $b^2/3$ by (7.7). All divided quantities are positive.

Substitute (7.7) and (7.9) into (7.10)-(7.11). The resulting two quadratic equations in $h$ are

$$
A h^2+B h+C_0=0,\qquad D_0h^2+E h+F=0,
\tag{7.12}
$$

where

$$
\begin{aligned}
A&=6v^2-v-4,& B&=-4v^2-4v+6,\\
C_0&=4v-4,& D_0&=2(v-1)(2v-1)^2,\\
E&=-16v^3+42v^2-31v+4,\qquad& F&=2v(2v-3)^2.
\end{aligned}
\tag{7.13}
$$

One can check the second equation without elimination software: after substitution, the difference between the two sides of (7.10), multiplied by $bc$, is

$$
(x-a)^2bc-x^2(b-a)(c-a)(1-a)
=\frac{a h^2v}{8(v-1)^2}(D_0h^2+Eh+F).
\tag{7.14}
$$

The first equation is $4(v-1)(xc-b(1-a))=0$. These identities justify (7.12) with no loss from a vanishing factor.

Two quadratics in (7.12) with a common root must satisfy

$$
0=(AF-C_0D_0)^2-(AE-BD_0)(BF-C_0E)
=16(v-2)^2(v-1)(2v+1)\Pi(v),
\tag{7.15}
$$

where direct expansion gives

$$
\Pi(v)=8v^6-24v^5-6v^4+64v^3-48v^2+9v-2.
\tag{7.16}
$$

To verify the first equality directly, put $L=AE-BD_0$, $M=AF-C_0D_0$ and $N=BF-C_0E$. Subtracting multiples of the two equations gives $Lh+M=0$ and $h(Mh+N)=0$. Since $h>0$, these imply $M^2-LN=0$. The factorization in the second equality is an ordinary polynomial identity.

There is a short sign check for its last factor. For $z=v-3/2\in[0,1/2]$,

$$
\begin{aligned}
\Pi(3/2+z)
&=8z^6+48z^5+84z^4+28z^3
 -\frac{87}{2}z^2-27z-2\\
&\le -2z^2-27z-2<0.
\end{aligned}
\tag{7.17}
$$

Indeed the four positive terms are at most $(1/2+6+21+14)z^2=(83/2)z^2$. Since $v>3/2$, equation (7.15) forces $v=2$. Both equations in (7.12) then reduce to $2(3h-2)(3h-1)=0$. The root $h=2/3$ makes $a<0$ and is inadmissible. The other gives

$$
(a,b,c,x)=\left(\frac16,\frac12,\frac56,\frac12\right).
\tag{7.18}
$$

Thus every globally maximizing extreme measure has precisely these nodes. This conclusion concerns maximizers directly; it does not require a knot-reflection inequality for every configuration.

### 7.3. Constants and all equality cases

The symmetric dual cubic, after normalization, is the centered cubic Chebyshev spline already described in [dB03, p. 74]. The new issue in this section is unrestricted global optimality and its equality classification. The weights in (7.3), normalized to total variation one at (7.18), are exactly (7.2). Their potential is

$$
U_*(x)=\frac16\left[
\frac{x_+^3+(x-1)_+^3}{9}
-\frac{(x-1/6)_+^3+(x-5/6)_+^3}{4}
+\frac5{18}(x-1/2)_+^3\right].
\tag{7.19}
$$

It is symmetric and unimodal by Section 5. Substitution at $x=1/2$ gives $U_*(1/2)=1/1296$. The extreme maximizing measure exists, and (7.18) identifies it, so this value is the unrestricted sharp height, not merely the maximum within symmetric configurations. Theorem 4 then gives the variation constant $1/648$.

For an arbitrary norm-one height maximizer, expose a face by evaluation at one of its maximum-height points, with the appropriate sign. Every extreme point of that face is a height-maximizing extreme measure and therefore equals $\mu_*$ or $-\mu_*$. Only one of these two signs can belong to the chosen face, because the exposed value is positive. Krein-Milman makes the face a singleton. This proves the stated equality classification, and Theorem 4 transfers it to variation. An ordinary Sobolev extremizer would have an absolutely continuous fourth derivative, whereas (7.2) is atomic. Hence ordinary attainment is impossible. The approximation argument in Theorem 4 still recovers both sharp constants. $\square$


## 8. Symmetry in every order at the measure endpoint

The fourth-order calculation can be replaced by an all-order comparison. The key is to follow the contacts of the best uniform polynomial approximation as the evaluation point moves. Their velocities are strictly less than one. The monotonicity of B-spline peaks then compares the evaluation point with the peak of its own optimizing potential.

**Theorem 9 (all-order measure endpoint).** For every $n\ge2$, the point-evaluation norm

$$
A_n(x)=\sup_{\mu\in\mathcal M_n}U_\mu(x)
$$

is strictly increasing on $(0,1/2)$ and strictly decreasing on $(1/2,1)$. There is a unique measure $\mu_n$ of total variation one attaining positive evaluation at $1/2$. Its potential is positive in $(0,1)$, symmetric about $1/2$, and has exactly one peak. The normalized relaxed height and variation extremizers are precisely $\mu_n$ and $-\mu_n$. In particular, all assertions of [NS, Conjecture 4.14] hold at $p=1$ for every order, with the endpoint interpreted in the measure sense. The sharp constants in the ordinary clamped Sobolev class agree with the relaxed constants, but no nonzero ordinary extremizer exists.

The full conjecture at the other exponents is not asserted here. The B-spline peak monotonicity used below is credited to Foucart [F]; the endpoint dependence needed here is supplied explicitly.

### 8.1. A zero count and regular contacts

We first record an elementary zero-count fact. Suppose $f$ is polynomial of degree at most $d$ on each side of a single knot $x$ and belongs to $C^{d-1}$, with neither polynomial piece identically zero. Then the number of isolated zeros, counted with polynomial multiplicity away from $x$ and the order of the first nonzero common derivative at $x$, is at most $d+1$. The only case where no common derivative through order $d-1$ is nonzero at a knot zero is

$$
f(t)=a_-(t-x)^d\quad(t<x),\qquad
f(t)=a_+(t-x)^d\quad(t>x),
$$

with $a_-a_+\ne0$; this case has just one distinct zero.

Here is a proof of the count, including missing coefficients. Write the common Taylor coefficients through degree $d-1$ as $a_0,\ldots,a_{d-1}$ and the two top coefficients as $a_d^-,a_d^+$. If the first nonzero common coefficient has index $r$, factor $(t-x)^r$. Descartes' rule of signs bounds the zeros on the right and left by the sign variations in the remaining coefficient list and the list with signs alternating according to degree. For successive nonzero common coefficients whose degrees differ by $h$, the sum of the two variation contributions is at most $h$: it is one for odd $h$, and zero or two for even $h$. Their total is at most $d-r-1$. The two independently chosen top coefficients add at most two. Adding the knot multiplicity $r$ gives $d+1$. If all common coefficients vanish, the displayed monomial case applies. Endpoint zeros of the interval under consideration are among the roots counted by this argument.

Fix $n\ge3$, put $m=n-1$, and write

$$
K_x(t)=\frac{(x-t)_+^m}{m!},\qquad
R_x(t)=K_x(t)-P_x(t),\qquad
A=A_n(x)=\|R_x\|_\infty,
\tag{8.1}
$$

where $P_x$ is a best uniform polynomial of degree at most $m$. The moment duality in Section 7 applies in every order. A maximizing evaluation face has an extreme measure supported on $n+1$ distinct nodes, and the signed weights force $n+1$ alternating contacts of $R_x$.

Neither piece of $R_x$ can be constant: smooth matching at $x$ would make the other a constant plus a multiple of $(t-x)^m$, yielding at most two alternating contacts. Thus the contact set is finite. Every interior contact is a strict local extremum. Applying the zero count to $R_x'$ with $d=n-2$ shows that it has at most $n-1$ zeros counting multiplicity. Since there are already at least $n-1$ interior contacts, the contact set is exactly

$$
0=t_0(x)<t_1(x)<\cdots<t_{n-1}(x)<t_n(x)=1,
\qquad R_x(t_i)=(-1)^iA.
\tag{8.2}
$$

All interior critical points are simple, and the endpoint derivatives are nonzero. For $n=3$, a contact cannot equal $x$: the two linear pieces of $R_x'$ would otherwise have their common zero at $x$, and a second critical point would force one piece to vanish identically. For $n\ge4$, a multiple critical point at $x$ also violates the same zero count. Consequently, in every case,

$$
\operatorname{sgn}R_x''(t_i)=(-1)^{i+1}\quad(1\le i<n),
\qquad R_x'(0)<0,\qquad
\operatorname{sgn}R_x'(1)=(-1)^n.
\tag{8.3}
$$

Every measure maximizing positive evaluation at $x$ is supported on this contact set, by equality in the dual norm inequality. Vandermonde rank gives a one-dimensional nullspace for the $n$ moment conditions on $n+1$ nodes. Positive evaluation and total variation one fix its sign and magnitude. Denote this unique measure by $\mu_x$. Its potential is the positive normalized B-spline on these nodes.

The contacts, polynomial coefficients and $A_n$ are $C^1$ functions of $x$. Indeed, differentiate the $n+1$ contact-value equations and $n-1$ critical-point equations. The contact-value block in the polynomial coefficients and $A$ is invertible: a nonzero polynomial of degree at most $n-1$ cannot take nonzero alternating values at $n+1$ ordered points. The remaining diagonal block consists of the nonzero numbers $R_x''(t_i)$. The implicit function theorem applies. Its equations are $C^1$ even when $x$ equals a contact for $n\ge4$; the case $n=3$ was excluded above. To identify this local branch with the actual optimizer, use uniqueness and compactness: best polynomial coefficients are locally bounded and their subsequential limits are best approximants; the norming measures converge to the unique norming measure, whose $n+1$ nonzero atoms prevent contact coalescence.

### 8.2. Every contact moves more slowly than evaluation

A dot denotes differentiation with respect to $x$; a prime denotes differentiation with respect to $t$. Put $\ell=A_n'(x)/A_n(x)$ and define

$$
V(t)=\dot R_x(t)+R_x'(t)-\ell R_x(t).
\tag{8.4}
$$

The identity $\partial_xK_x+\partial_tK_x=0$ shows that $V$ is again a degree-at-most-$m$ spline with one simple knot: it is a polynomial minus $\ell K_x$. Differentiating (8.2) and using $R_x'(t_i)=0$ at interior contacts gives

$$
V(t_i)=0\quad(1\le i<n),\qquad
V(0)=R_x'(0)<0,\qquad V(1)=R_x'(1).
\tag{8.5}
$$

Neither piece of $V$ vanishes identically, since its endpoint values are nonzero. The zero count gives at most $n$ zeros counting multiplicity. The $n-1$ prescribed interior zeros must therefore all be simple and there can be no additional zero. To see the parity step explicitly, the endpoint signs in (8.5) require the parity of the number of crossings to be $n-1$. An additional simple zero or one double prescribed zero would reverse this parity; restoring it costs another zero and exceeds the bound $n$. A prescribed zero of multiplicity at least three already exceeds that bound. At a knot zero where the first $m$ common coefficients vanish, both pieces would be monomials and there would be only one distinct zero, contrary to the $n-1\ge2$ prescribed zeros. Thus this exception does not interfere with the parity argument.

It follows that $V'(t_i)$ has sign $(-1)^{i+1}$, the same as $R_x''(t_i)$. Differentiating the critical-point equation yields

$$
\dot R_x'(t_i)+R_x''(t_i)t_i'(x)=0,
\qquad
V'(t_i)=R_x''(t_i)\{1-t_i'(x)\}.
$$

Hence

$$
t_i'(x)<1\qquad(1\le i<n).
\tag{8.6}
$$

No lower bound on these velocities is needed.

### 8.3. The dependence of a B-spline peak on all its knots

Let $B_{\mathbf t}$ be the conventional positive B-spline of degree $m\ge2$ on $m+2$ simple knots and let $s(\mathbf t)$ be its unique peak. Foucart [F, Proposition 6] proves

$$
\frac{\partial s}{\partial t_j}>0
\quad\text{for every interior knot }t_j.
\tag{8.7}
$$

The peak is nondegenerate and depends differentiably on the knots. We need the same inequality for the two support endpoints. We prove this extension using the same divided-difference identities, keeping its scope separate from the cited statement.

By affine scaling take the support to be $[0,1]$, and let $B_j$ be the degree-$m+1$ B-spline obtained by repeating the endpoint $t_j$. The knot-insertion identity in [F, Lemma 3 and Formulae 5] gives

$$
B_j(y)=\frac{y-t_j}{m+1}B_j'(y)+B_{\mathbf t}(y).
\tag{8.8}
$$

At $s=s(\mathbf t)$, differentiating once and eliminating $B_j'(s)$ yields

$$
(s-t_j)^2B_j''(s)
=m(m+1)\{B_j(s)-B_{\mathbf t}(s)\}.
\tag{8.9}
$$

For the left endpoint $t_j=0$, integrating (8.8) with $B_j(1)=0$ gives

$$
B_j(s)=(m+1)s^{m+1}\int_s^1B_{\mathbf t}(y)y^{-m-2}\,dy
\le B_{\mathbf t}(s)(1-s^{m+1})<B_{\mathbf t}(s).
\tag{8.10}
$$

For the right endpoint, the reflected formula gives the same strict inequality. Thus $B_j''(s)<0$. Differentiation of the divided difference defining $B_{\mathbf t}$ with respect to an endpoint gives

$$
\partial_{t_j}B_{\mathbf t}'(s)=-\frac1{m+1}B_j''(s)>0.
\tag{8.11}
$$

The derivative of the support-length normalization contributes a multiple of $B_{\mathbf t}'(s)=0$, so it contributes nothing to (8.11). Since $B_{\mathbf t}''(s)<0$, implicit differentiation of $B_{\mathbf t}'(s)=0$ proves (8.7) for the endpoints too.

Translation equivariance now gives

$$
\sum_{j=0}^{m+1}\frac{\partial s}{\partial t_j}=1,
\qquad \frac{\partial s}{\partial t_j}>0\quad\text{for every }j.
\tag{8.12}
$$

### 8.4. Strict midpoint comparison and equality

Let $s(x)=s(t_0(x),\ldots,t_n(x))$ be the peak of $U_{\mu_x}$. The normalizing factor of this potential does not affect its peak. Equations (8.6) and (8.12), together with $t_0'=t_n'=0$, show that

$$
s'(x)=\sum_{i=1}^{n-1}\frac{\partial s}{\partial t_i}t_i'(x)
<\sum_{i=1}^{n-1}\frac{\partial s}{\partial t_i}<1.
\tag{8.13}
$$

Reflection and uniqueness of the positive-evaluation norming measure at $1/2$ give $s(1/2)=1/2$. Therefore $s(x)-x$ is strictly decreasing and

$$
s(x)>x\quad(x<1/2),\qquad s(x)<x\quad(x>1/2).
\tag{8.14}
$$

Finally, uniqueness and weak-star continuity of $\mu_x$, together with joint continuity of $\partial_xK_x$ for $n\ge3$, give the envelope identity

$$
A_n'(x)=U_{\mu_x}'(x).
\tag{8.15}
$$

It follows directly by testing the optimizer at each of two neighboring points in the other evaluation problem and taking the two difference quotients. The B-spline potential is strictly increasing before its unique peak and strictly decreasing after it. Equation (8.14) therefore proves the asserted strict monotonicity of $A_n$.

Every global height maximizer must consequently attain its absolute height at $1/2$. The unique norming measure there, up to the sign of evaluation, is $\mu_n$. Its potential is symmetric by reflection and positive by the moment-circuit formula. Theorem 4 transfers the complete classification to variation. The ordinary constants agree by the recovery argument there; an ordinary extremizer would have an absolutely continuous highest derivative, whereas the unique relaxed one is a nonzero atomic circuit. This rules out ordinary attainment.

For $n=2$, the direct formula $A_2(x)=x(1-x)/2$ and its unique three-point norming measure give the same conclusions. This completes the proof. $\square$


## 9. Remaining questions

The full all-exponent form of [NS, Conjecture 4.14] remains unresolved. Theorem 9 completes the measure endpoint in every order, including strict midpoint maximization, unique symmetric extremizers and ordinary nonattainment. Theorem 5 proves an order-dependent open interval about two. Extending the identity and symmetry through the remaining exponents requires a new global argument: compactness alone does not exclude competing variation maximizers. The contact-motion proof uses uniform approximation and atomic moment circuits and does not automatically extend to a finite dual exponent. The stronger centroid and knot-reflection inequalities explored in the research notes are not required or proved by Theorem 9.

## References

[ABR] S. Axler, P. Bourdon and W. Ramey, *Harmonic Function Theory*, second edition, Springer, 2001 (author PDF revision July 17, 2020). [Author text](https://axler.net/HFT.pdf), formula (1.15), Theorem 1.17 and Chapter 5.

[BH] A. Burchard and H. Hajaiej, *Rearrangement inequalities for functionals with monotone integrands*, Journal of Functional Analysis **233** (2006), 561--582. [DOI](https://doi.org/10.1016/j.jfa.2005.08.010). [Final revised author version](https://arxiv.org/abs/math/0506336).

[dB] C. de Boor, *Divided Differences*, Surveys in Approximation Theory **1** (2005), 46--69. [Author text](https://arxiv.org/abs/math/0502036), formulas (47)--(48) and (52).

[dB03] C. de Boor, *Math/CS 887 course notes*, Spring 2003, TeX version November 21, 2009. [Author notes](https://pages.cs.wisc.edu/~deboor/887/notes.pdf), p. 74, centered cubic Chebyshev-spline example.

[F] S. Foucart, *Interlacing property for B-splines*, Journal of Approximation Theory **135** (2005), no. 1, 1--21. [DOI](https://doi.org/10.1016/j.jat.2005.03.001). [Author preprint, February 24, 2005](https://foucart.github.io/publi/tbsm2.pdf), Lemma 3, Formulae 5 and Proposition 6.

[GHW] R. J. Gardner, D. Hug and W. Weil, *The Orlicz-Brunn-Minkowski theory: A general framework, additions, and inequalities*, Journal of Differential Geometry **97** (2014), no. 3. [DOI](https://doi.org/10.4310/jdg/1406033976). [Author text](https://arxiv.org/abs/1301.5267).

[GS] T. A. Garmanova and I. A. Sheipak, *Sharp Estimates of High-Order Derivatives in Sobolev Spaces*, Moscow University Mathematics Bulletin **79** (2024), 1--10. [DOI](https://doi.org/10.3103/S0027132224700013).

[HNOR] R. Hindov, S. Nitzan, J.-F. Olsen and E. Rydhe, *A sharp higher order Sobolev embedding*, Mathematika **71** (2025), e70012. [DOI](https://doi.org/10.1112/mtk.70012). [Author preprint](https://arxiv.org/abs/2411.10201).

[K] G. A. Kalyabin, *Sharp Estimates for Derivatives of Functions in the Sobolev Classes $W_2^r(-1,1)$*, Proceedings of the Steklov Institute of Mathematics **269** (2010), 137--142. [DOI](https://doi.org/10.1134/S0081543810020112).

[NS] A. I. Nazarov and A. P. Shcheglova, *A Survey of Results on 1D Steklov Type Inequalities*, Proceedings of the Steklov Institute of Mathematics **331** (2025), 134--147; published online March 19, 2026. [DOI](https://doi.org/10.1134/S0081543825601509). [Latest author preprint](https://arxiv.org/abs/2101.10752).
