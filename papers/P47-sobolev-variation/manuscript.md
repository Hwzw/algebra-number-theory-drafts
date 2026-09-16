# Sharp total variation bounds from spherical rearrangement

Henry Zweiman

September 16, 2026

## Abstract

We study the sharp control of total variation by a higher derivative under homogeneous endpoint conditions. For every integer $n\ge2$, we prove that the norm of $u\mapsto u'$ from $W_0^{n,2}(0,1)$ to $L^1(0,1)$ is twice the norm of point evaluation into $L^\infty(0,1)$. The extremizers of the two embeddings coincide and are symmetric about the midpoint. This proves the Hilbert-space case of a conjecture of Nazarov and Shcheglova. The main step is a rearrangement principle for a clamped Green operator after projection onto the zero-mean subspace. A Jacobi-polynomial representation identifies its quadratic form with a positive mixture of Poisson interactions on a sphere, where rearrangement reduces the optimization to a cap. We also prove the constant identity and coincidence of maximizing sets at the measure endpoint $p=1$, using the geometry of extreme moment measures and unimodal splines. For each fixed derivative order, we further prove the full variation identity and midpoint-symmetric equality classification on an open interval of exponents around two. A dual optimality equation gives compactness through the highest derivative; polynomial sublevel bounds control the point-evaluation profile on both sides of the Hilbert exponent. At the measure endpoint in derivative order four, we also determine the exact sharp constant and unique symmetric extremizer by a cubic alternation argument and an explicit algebraic exclusion of asymmetric maximizers. An all-order contact-motion argument then proves strict midpoint maximization and the unique symmetric measure extremizer in every order, completing the measure-endpoint conjecture. A weighted zero-count extension proves strict midpoint point-evaluation maximization and unique symmetric height extremizers for every finite exponent. This completes the function-height case of the broader symmetry conjecture when combined with the endpoint results. Finally, compactness of arbitrary variation maximizers at the unique measure endpoint proves the full variation statement on an order-dependent interval immediately above one. We also prove that every finite-exponent variation maximizer has finitely many nondegenerate critical points and simple dual-residual zeros, and derive its switching Hessian. A translation cancellation then excludes every two-switch variation maximizer, without a symmetry assumption. Affine dilation also excludes midpoint-symmetric three-switch maximizers and restricts the geometry of remaining three-switch candidates. An explicit rational certificate shows that the analogous identity fails for arbitrary positive derivative weights, even for smooth weights in order three; this rules out an unrestricted weighted Hilbert shortcut. The full all-exponent variation conjecture remains open.

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

The radius is allowed to depend on $n$ and is not estimated here. The theorem does not reach all $1<p<\infty$, give an interval uniform in $n$, or settle the full all-exponent variation conjecture.

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

This argument does not prove that the set of valid exponents is closed. At a hypothetical first exponent where the result ceases to hold, compactness of the old single-peak branch does not exclude a different multiple-peak global maximizer with the same value. Theorem 10 below resolves the separate point-evaluation symmetry question at every finite exponent. The possible coexistence of multiple-peak variation maximizers remains a substantive global obstacle.

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


## 9. Point symmetry at every finite exponent

The preceding cancellation also has a finite-exponent form. Instead of following finitely many contacts, we integrate an auxiliary spline against a positive weight and count its zeros. Throughout this section $q=p/(p-1)$ is the dual exponent; it is not the target exponent in [NS, Conjecture 4.3].

**Theorem 10 (finite-exponent point symmetry).** Let $n\ge2$ and $1<p<\infty$. The point-evaluation norm

$$
A_{n,p}(a)=\sup\{u(a):u\in W_0^{n,p}(0,1),\ \|u^{(n)}\|_p\le1\}
\tag{9.1}
$$

is strictly increasing on $(0,1/2)$ and strictly decreasing on $(1/2,1)$. The nonzero extremizers for the height inequality in (2) are precisely the scalar multiples of the unique positive norm-one midpoint normer. That normer is symmetric, positive in the interior, and has a unique nondegenerate maximum.

The order-two statement and order-three midpoint symmetry are prior results [W, Theorem 1.1 and Lemma 1.3], recorded also in [NS, Theorem 4.5]. Watanabe et al. explicitly note in [W, Remark 1.4] that their symmetrization proof does not extend to orders at least four. The theorem above gives the all-order comparison. Together with Theorem 9 and the credited $p=\infty$ theorem [NS, Theorem 4.12], it establishes the $k=0$, target-$L^\infty$ case of [NS, Conjecture 4.3] for every $n\ge2$ and $1\le p\le\infty$. It does not establish the remaining variation identity in Conjecture 4.14.

### 9.1. Simple residual zeros and a single peak

We prove the theorem for $n\ge3$ and write $m=n-1$. As in Section 6, let $P_a$ be the unique best $L^q$ polynomial approximant of degree at most $m$ to $K_a(t)=(a-t)_+^m/m!$. Set

$$
R_a=K_a-P_a,\qquad f_a=|R_a|^{q-2}R_a,\qquad
u_a(t)=\int_0^t\frac{(t-z)^{n-1}}{(n-1)!}f_a(z)\,dz.
\tag{9.2}
$$

The normal equations (6.5) make $u_a$ clamped at both endpoints and give

$$
u_a(a)=\int_0^1|R_a|^q>0,\qquad
v_a=\frac{u_a}{\|R_a\|_q^{q-1}}.
\tag{9.3}
$$

Here $v_a$ is the unique positive-evaluation normer. This follows from the dual formula and equality in Hölder's inequality, as in Section 6; the best-approximation formula itself is credited to [GS, Theorem 2 and Corollary 1].

The residual has at least $n$ sign changes. Otherwise the polynomial having its sign-change points as roots, with a suitable sign, has degree at most $n-1$ and gives a strictly positive integral against $f_a$, contradicting (6.5). Neither polynomial piece of $R_a$ vanishes identically: smooth matching would make the other a nonzero multiple of $(t-a)^m$, of constant sign on its side, contradicting the constant moment. The one-knot zero count of Section 8.1 bounds the total number of zeros, with multiplicity, by $n$. Its exceptional two-monomial case has only one distinct zero and is excluded. Thus $R_a$ has exactly $n$ simple interior zeros, and its endpoint values are nonzero.

Repeated Rolle counting shows that $u_a$ has no interior zero and $u_a'$ has exactly one simple interior zero. Indeed, $u_a\in C^n$ has endpoint zeros of multiplicity $n$. An additional interior zero would force at least $n+1$ distinct zeros of $f_a$ after $n$ differentiations. Applied to $u_a'$, whose endpoint multiplicities are $n-1$, the same count excludes either two distinct interior zeros or a degenerate zero. Consequently $u_a>0$ in $(0,1)$ and its unique peak $s(a)$ satisfies

$$
u_a''(s(a))<0,\qquad
f_a(0)>0,\qquad (-1)^nf_a(1)>0.
\tag{9.4}
$$

The last two signs follow from the endpoint Taylor expansions.

### 9.2. Differentiation through the residual zeros

The preceding simple-root result removes the restriction to exponents near two in the regularity argument. Fix $q>1$ and $a\in(0,1)$. The residual is $C^1$ in $t$, since $m\ge2$. Its roots are transverse even if one equals the kernel knot. In a small neighborhood of the minimizing polynomial coefficients and evaluation point, there remain exactly $n$ simple roots with inverse slopes uniformly bounded. For $1<q<2$, this gives the locally uniform estimate

$$
\int_{\{|R|<h\}}|R|^{q-2}\,dt\le C h^{q-1}.
\tag{9.5}
$$

It follows by changing variables from $t$ to $R(t)$ in disjoint monotone neighborhoods of the roots; outside them $|R|$ is bounded below. For $q\ge2$ the weight has no singularity. Differentiating the normal equations in $a$ and the polynomial coefficients is therefore justified by the same sublevel splitting as in Section 6.3. The coefficient Jacobian is

$$
-(q-1)\left[\int_0^1|R_a|^{q-2}t^{i+j}\,dt\right]_{i,j=0}^{n-1},
\tag{9.6}
$$

a negative definite Gram matrix. The implicit function theorem and uniqueness give a $C^1$ minimizing coefficient map for every fixed $q>1$.

The same estimate shows that $a\mapsto f_a$ is continuously differentiable as a map into $L^1$. Its derivative is $(q-1)|R_a|^{q-2}\dot R_a$. As a function of $t$, $f_a$ is absolutely continuous, with derivative $(q-1)|R_a|^{q-2}R_a'$. Integration gives continuous differentiability of $a\mapsto u_a$ into $C^{n-1}$, as well as $u_a\in W^{n+1,1}$. The nondegenerate peak in (9.4) therefore depends continuously differentiably on $a$. In what follows, a dot denotes the $a$ derivative and a prime the $t$ derivative.

### 9.3. A weighted comparison for peak motion

Fix $a$ and abbreviate $u=u_a$, $R=R_a$, $f=f_a$, and $s=s(a)$. Define

$$
\ell=\frac{\dot u(s)}{u(s)},\qquad
W=\dot u+u'-\ell u,\qquad H=\dot R+R'.
\tag{9.7}
$$

The identity $\partial_aK_a+\partial_tK_a=0$ makes $H$ a polynomial of degree at most $n-1$. Almost everywhere,

$$
D^nW=|R|^{q-2}T,\qquad T=(q-1)H-\ell R.
\tag{9.8}
$$

The function $T$ is a degree-at-most-$n-1$ spline with one simple knot. If both pieces are nonzero, Section 8.1 bounds its isolated zeros by $n$, with the two-monomial exception having only one distinct zero. The weight in (9.8) is positive almost everywhere and integrable.

The function $W\in W^{n,1}\subset C^{n-1}$ satisfies

$$
\begin{aligned}
W^{(j)}(0)&=W^{(j)}(1)=0 &&(0\le j\le n-2),\\
W^{(n-1)}(0)&=f(0)>0,\qquad W^{(n-1)}(1)=f(1),\\
W(s)&=0.
\end{aligned}
\tag{9.9}
$$

In particular, $W$ is positive near zero and negative near one. We claim

$$
W'(s)<0.
\tag{9.10}
$$

Here is a zero-count proof that includes the possible singularities of the weight. If $W'(s)>0$, the opposite endpoint signs force another root on each side of $s$. If $W'(s)=0$ and $W''(s)\ne0$, there is a double root and another root. If $W'(s)=W''(s)=0$, there is a root of multiplicity at least three. These derivatives exist because $n\ge3$. Thus failure of (9.10) supplies interior zeros of total multiplicity at least three, besides the two endpoint zeros of multiplicity $n-1$.

Apply ordinary Rolle's theorem $n-1$ times. It yields at least $n+2$ distinct zeros of $W^{(n-1)}$: the initial count is at least $2n+1$, and all retained multiplicities are exhausted by this stage. On each of the $n+1$ intervening disjoint intervals, the integral of $|R|^{q-2}T$ is zero. If both pieces of $T$ are nonzero, it is not identically zero on any interval. Positivity of the weight then forces a sign change of $T$ on each interval, contradicting its zero bound.

If one piece of $T$ vanishes identically, smooth matching makes the other a constant multiple of $(t-a)^{n-1}$. Then $W^{(n-1)}$ is the nonzero constant $f(0)$ or $f(1)$ on the zero side and is strictly monotone on the other side. It has at most one zero, again a contradiction. If both pieces vanish, it is constant nonzero and has none. This proves (9.10).

Differentiate $u_a'(s(a))=0$. Equations (9.7) and (9.10) give

$$
W'(s)=u_a''(s)\{1-s'(a)\}<0.
\tag{9.11}
$$

Since $u_a''(s)<0$, we obtain $s'(a)<1$ for every $a\in(0,1)$.

### 9.4. Strict midpoint maximization and the remaining gap

Reflection and uniqueness give $s(1/2)=1/2$. Thus $s(a)-a$ is strictly decreasing, positive before the midpoint and negative after it. The envelope identity is

$$
A_{n,p}'(a)=\frac{u_a'(a)}{\|R_a\|_q^{q-1}}.
\tag{9.12}
$$

The strict single-peak signs of $u_a$ prove the stated monotonicity. Any height extremizer must attain its absolute maximum at $1/2$; uniqueness of the midpoint normer gives all equality cases, and reflection gives its symmetry. This proves Theorem 10. $\square$

Two useful boundary identities follow from the same cancellation. With $J(a)=\int_0^1|R_a|^q$, integration by parts and the normal equations give

$$
\begin{aligned}
J'(a)&=|R_a(0)|^q-|R_a(1)|^q,\\
((n-1)q+1)J(a)&=a|R_a(0)|^q+(1-a)|R_a(1)|^q.
\end{aligned}
\tag{9.13}
$$

For the second identity use $(a-t)R_a'=-mR_a$ plus a polynomial of degree at most $m$. The theorem therefore also proves the strict ordering of the endpoint residual magnitudes on either side of the midpoint.

This argument classifies height extremizers for every finite exponent. It does not imply that every variation maximizer has a single peak. Its dual residual in (6.6) comes from $H_g$, which may have many changes of polynomial piece when $g=\operatorname{sign}(u')$. The one-knot bound in (9.8) is then unavailable. This is the remaining obstruction to the full variation conjecture.

## 10. Variation continuation from the measure endpoint

The unique endpoint measure also controls arbitrary variation maximizers as the input exponent decreases to one. Two issues require care: ordinary highest derivatives develop concentration, and in order three weak measure convergence does not directly give uniform second-derivative convergence.

**Theorem 11 (continuation above one).** For every $n\ge3$ there exists $\eta_n>0$ such that, for $1<p<1+\eta_n$,

$$
V_{n,p}=2C_{n,p}.
\tag{10.1}
$$

The nonzero extremizers in the two inequalities are exactly the scalar multiples of the unique positive norm-one midpoint normer. They are symmetric and strictly unimodal up to sign. The interval width is not estimated, and overlap with the interval in Theorem 5 is not asserted. The case $n=2$ is already known for all $p$ by [NS, Remark 4.15].

### 10.1. Compactness of arbitrary endpoint sequences

Fix $n\ge3$. Let $p_j>1$ tend to one and let $u_j$ be any norm-one variation maximizers, whose existence was proved in Section 6. Write $f_j=u_j^{(n)}$ and $\mu_j=f_j\,dt$. Since the interval has length one,

$$
\|\mu_j\|_{\mathrm{TV}}=\|f_j\|_1\le\|f_j\|_{p_j}=1.
$$

A subsequence converges weak-star to some $\mu\in\mathcal M_n$. For $n\ge3$ the potential kernel and its first derivative are jointly continuous on the square. Their integrals over the unit measure ball are uniformly equicontinuous. Pointwise weak-star convergence and this equicontinuity therefore give $u_j\to U_\mu$ in $C^1[0,1]$.

The constants satisfy $V_{n,p_j}\le V_{n,1}$. Conversely, given $\delta>0$, the recovery argument in Theorem 4 supplies one nonzero smooth clamped function $v$ with

$$
\frac{\|v'\|_1}{\|v^{(n)}\|_1}>V_{n,1}-\delta.
$$

Its highest-derivative $L^{p_j}$ norm tends to its $L^1$ norm. Testing this fixed function and then letting $\delta$ decrease to zero proves $V_{n,p_j}\to V_{n,1}$. Thus $U_\mu$ maximizes endpoint variation. Theorems 4 and 9 identify $\mu$ with $\mu_n$ or $-\mu_n$. After choosing the common sign along the subsequence, we have

$$
\mu_j\stackrel{*}{\rightharpoonup}\mu_n,\qquad
u_j\longrightarrow U_{\mu_n}\quad\hbox{in }C^1,
\qquad \|\mu_j\|_{\mathrm{TV}}\longrightarrow1.
\tag{10.2}
$$

The last limit follows from lower semicontinuity and the upper bound one.

We also need convergence of the absolute measures:

$$
|\mu_j|\stackrel{*}{\rightharpoonup}|\mu_n|.
\tag{10.3}
$$

Indeed, any weak-star limit $\nu$ of a subsequence of $|\mu_j|$ dominates $|\mu_n|$. To see this, for nonnegative continuous $h$ and continuous $\phi$ with $|\phi|\le h$, pass to the limit in
$|\int\phi\,d\mu_j|\le\int h\,d|\mu_j|$ and use the dual description of variation. Both $\nu$ and $|\mu_n|$ have mass one by (10.2), so they agree. Every subsequence has this same limit, proving (10.3).

### 10.2. The limiting dual residual fixes the endpoint signs

Put $U=U_{\mu_n}$ and let $g_j=\operatorname{sign}(u_j')$, with any choice in $[-1,1]$ where $u_j'=0$. The strict signs of $U'$ imply pointwise convergence except at $0,1/2,1$ to the midpoint sign function $g_*$, which is positive before $1/2$ and negative after it. Dominated convergence gives $g_j\to g_*$ in $L^1$. Hence $H_j=H_{g_j}$ converges uniformly to

$$
H_*(t)=2K_{1/2}(t)-\frac{(1-t)^{n-1}}{(n-1)!}.
\tag{10.4}
$$

Let $P_j$ minimize $\|H_j-P\|_{q_j}$ over polynomials of degree at most $n-1$, where $q_j=p_j/(p_j-1)\to\infty$. The bound
$\|P_j\|_1\le\|P_j\|_{q_j}\le2\|H_j\|_\infty$
and finite-dimensional norm equivalence give bounded polynomial coefficients. Take any subsequential coefficient limit $P_\infty$. For each fixed finite $r$, each polynomial $P$ in the same space, and all sufficiently large $j$,

$$
\|H_j-P_j\|_r\le\|H_j-P_j\|_{q_j}
\le\|H_j-P\|_{q_j}\le\|H_j-P\|_\infty.
\tag{10.5}
$$

First let $j$ tend to infinity, using uniform convergence, and then let $r$ tend to infinity. Thus $P_\infty$ is a best uniform approximant to $H_*$. Uniqueness of best uniform polynomial approximation and (10.4) identify

$$
R_j:=H_j-P_j\longrightarrow2R_{1/2}\quad\hbox{uniformly},
\qquad
f_j=\operatorname{sign}(R_j)
\left|\frac{R_j}{V_{n,p_j}}\right|^{q_j-1}.
\tag{10.6}
$$

Here $R_{1/2}$ is the truncated-power residual in Section 8; every subsequence has the same limit. The second identity is the dual optimality equation (6.6).

The endpoint residual values in (8.2) are nonzero, positive at zero and of sign $(-1)^n$ at one. Uniform convergence therefore fixes these signs for $R_j$ on small endpoint neighborhoods, independently of $j$ once it is large. Equation (10.6) fixes the same strict signs for $f_j$, although its magnitude need not remain bounded. Integration from the clamped endpoints gives $u_j'>0$ near zero and $u_j'<0$ near one. On compact sets separated from the endpoints and midpoint, uniform convergence of $u_j'$ to $U'$ preserves the required signs as well.

### 10.3. Curvature at the midpoint and completion

For $n\ge4$, the twice-differentiated potential kernel is jointly continuous. The compactness argument above then gives $u_j''\to U''$ uniformly. The B-spline peak is nondegenerate, as used in Section 8 and [F, Proposition 6]. Thus $u_j''<0$ on a fixed central interval for all sufficiently large $j$.

For $n=3$, the unique symmetric measure has four distinct knots $0,a,1-a,1$, with $a<1/2$. The midpoint lies in a knot-free interval, where $U''$ is a strictly negative constant. Choose a closed central subinterval $I=[c,d]$ entirely inside this gap. Equation (10.3) and $|\mu_n|(I)=0$ imply $|\mu_j|(I)\to0$. Also $\mu_j([0,c])\to\mu_n([0,c])$: continuous approximation of the interval indicator, together with (10.3), justifies this passage because its relative boundary $\{c\}$ has zero limiting variation mass. The endpoint atom at zero is included on both sides. Since $u_j''(x)=\mu_j([0,x])$, we obtain

$$
\begin{split}
\sup_{x\in I}|u_j''(x)-U''(x)|
&\le |\mu_j([0,c])-\mu_n([0,c])|+|\mu_j|(I)\\
&\longrightarrow0.
\end{split}
\tag{10.7}
$$

Hence the middle curvature is strictly negative in order three too.

Combine this curvature with the derivative signs already proved near the endpoints and on the intervening compact intervals. Each $u_j$ has exactly one critical point for large $j$, with positive derivative before it and negative derivative after it. Because the original sequence consisted of arbitrary variation maximizers, a contradiction-sequence argument supplies $\eta_n>0$ for which every normalized maximizer has this geometry, up to sign, whenever $1<p<1+\eta_n$.

Such a maximizer has variation twice its height, so $V_{n,p}\le2C_{n,p}$. The reverse bound always holds. A variation maximizer is therefore a height maximizer, and a height maximizer is a variation maximizer. Theorem 10 gives the midpoint symmetry and unique equality class. This proves Theorem 11. $\square$

## 11. Finite switches and the stability matrix

The remaining variation problem can be reduced to finite, regular switching configurations without assuming this regularity in advance.

**Theorem 12 (regularity of variation maximizers).** Fix $n\ge3$ and $1<p<\infty$, and put $q=p/(p-1)$. Every norm-one variation maximizer $u$ has finitely many interior critical points, all nondegenerate. If their number is $r$, then $r\ge1$ and its dual residual $R=H_{\operatorname{sign}(u')}-P$ has exactly $n+r-1$ simple interior zeros. Moreover,

$$
|u^{(n)}(0)|^p=|u^{(n)}(1)|^p=(n-1)q+1.
\tag{11.1}
$$

The number $r$ is uniformly bounded when $p$ ranges over a compact subinterval of $(1,\infty)$, with $n$ fixed. No explicit bound or assertion $r=1$ is made.

### 11.1. Endpoint identities without a switching assumption

Write $m=n-1$, $V=V_{n,p}$, $f=u^{(n)}$ and $g=\operatorname{sign}(u')$. By Section 6,

$$
\|R\|_q=V,\qquad f=\frac{|R|^{q-2}R}{V^{q-1}},\qquad
\int_0^1Rf=V.
\tag{11.2}
$$

In particular $R\in W^{m,\infty}$, $f$ is continuous and $u\in C^n$. For some constant $c$, differentiation of the load gives

$$
g-c=(-1)^mR^{(m)}\quad\hbox{almost everywhere}.
\tag{11.3}
$$

The chain rule for $|u'|$ is valid regardless of its zero set. It gives

$$
\int_0^1(g-c)u''=0,\qquad
\int_0^1t(g-c)u''=-V.
$$

Integrate by parts $m-1$ times. All boundary terms vanish by the clamped conditions. In the second identity use
$D^{m-1}(tu'')=tf+(m-1)u^{(m)}$
and $\int R'u^{(m)}=-\int Rf=-V$. The result is

$$
\int_0^1R'f=0,\qquad \int_0^1tR'f=mV.
\tag{11.4}
$$

The absolutely continuous function $|R|^q$ has derivative $qV^{q-1}fR'$. Therefore

$$
|R(0)|^q=|R(1)|^q=(mq+1)V^q.
\tag{11.5}
$$

Equation (11.1) follows from (11.2), since $(q-1)p=q$. In particular $f$ is bounded away from zero on endpoint neighborhoods. No derivative of the sign function $g$ was taken.

### 11.2. A degenerate critical point is unstable

Suppose $u'(a)=u''(a)=0$ at an interior point. By (11.1), choose open intervals $E_-$ to its left and $E_+$ to its right on which $|f|$ has a positive lower bound. There exists $\phi\in C_c^\infty(E_-\cup E_+)$ such that

$$
\int_0^1t^j\phi(t)\,dt=0\quad(0\le j<n),\qquad
\int_0^1\frac{(a-t)_+^{n-2}}{(n-2)!}\phi(t)\,dt\ne0.
\tag{11.6}
$$

Indeed, if the last functional vanished on the common kernel of the moment functionals, finite-dimensional linear algebra would express it as their linear combination. Testing smooth functions supported in the two intervals would make its kernel a polynomial of degree at most $n-1$ there. That polynomial vanishes on $E_+$ and hence identically, but the kernel is nonzero on $E_-$, a contradiction.

Let $h=I^n\phi$. The moment conditions make it a smooth clamped function, and $h'(a)\ne0$. Since $h^{(n)}$ is supported where $|f|$ is bounded below, the map $\varepsilon\mapsto\|f+\varepsilon\phi\|_p$ is twice continuously differentiable near zero, including when $p<2$. Applying the sharp variation inequality to $u+\varepsilon h$ and $u-\varepsilon h$ and averaging gives

$$
\frac{\|(u+\varepsilon h)'\|_1+\|(u-\varepsilon h)'\|_1}{2}
-\|u'\|_1\le C\varepsilon^2.
\tag{11.7}
$$

The scalar identity
$(|y+z|+|y-z|)/2-|y|=(|z|-|y|)_+$
identifies the left side with $\int(\varepsilon|h'|-|u'|)_+$ for $\varepsilon>0$. But $u'(t)=o(|t-a|)$ and $|h'|$ is bounded below near $a$. For every fixed $M>0$, integration over $|t-a|<M\varepsilon$ gives a lower bound $c_0M\varepsilon^2$ for all sufficiently small $\varepsilon$, where $c_0>0$ is independent of $M$. Choosing $M$ arbitrarily large contradicts (11.7). Thus $u''(a)\ne0$ at every interior zero of $u'$.

All these zeros are isolated. The clamped Taylor expansions and nonzero endpoint values of $f$ fix a nonzero sign of $u'$ near each endpoint. An infinite set of zeros in the remaining compact interval would have an accumulation point, necessarily with $u'=u''=0$. Hence there are finitely many zeros. Each is a sign switch, and at least one occurs because $\int_0^1u'=0$ and $u$ is nonzero.

### 11.3. The residual zeros are also simple

Let the critical points be $\tau_1<\cdots<\tau_r$. The moment equations force at least $n$ sign changes of $R$. Repeated mean-value arguments then force $R^{(m)}$ to take both positive and negative values on sets of positive measure. Equation (11.3), with $g$ taking only the values $\pm1$ almost everywhere, implies $-1<c<1$.

Consequently $R$ has degree exactly $m$ on each of the $r+1$ knot intervals. Its derivative $R^{(m-1)}$ is continuous piecewise affine, with a nonzero slope on each interval, and has at most $r+1$ distinct zeros. The $r$ interior zeros of $u'$, together with its endpoint zeros of exact multiplicity $m$, force at least $m+r$ distinct zeros of $f$ after $m$ applications of Rolle's theorem. These are also zeros of $R$.

Conversely, applying Rolle $m-1$ times to $R$ bounds its distinct zeros by $m+r$. A multiple root would add another zero in this count and force at least $r+2$ distinct zeros of $R^{(m-1)}$, which is impossible. This argument uses only a double root and continuity of $R'$, including at a switching knot when $m=2$. Thus the residual has exactly $n+r-1$ simple interior zeros.

For the uniform bound, suppose $p_j$ stays in a compact subinterval of $(1,\infty)$ and the corresponding maximizing functions have unbounded critical-point counts. After a subsequence $p_j\to p_0$, the compactness argument in Section 6.5 gives convergence in $C^n$ to a normalized maximizer at $p_0$. Its endpoint highest derivatives are nonzero and all its interior critical points are nondegenerate. Hence the endpoint signs persist, each interior critical point has exactly one nearby critical point for large $j$, and the intervening compact sets contain none. The critical-point counts are eventually equal to that of the limit, a contradiction. This completes the proof of Theorem 12. $\square$

### 11.4. A justified second-variation condition

Let $\sigma_i$ be the sign of $u'$ just before $\tau_i$, so the load jumps there by $-2\sigma_i$. Nearby ordered switching points define nearby sign loads. Modulo a polynomial of degree at most $n-1$, their dual load is

$$
H_{\boldsymbol\tau}=2\sum_{i=1}^r\sigma_iK_{\tau_i}.
$$

Put $J(\boldsymbol\tau)=\min_P\int|H_{\boldsymbol\tau}-P|^q$. At the maximizing configuration set

$$
w=|R|^{q-2},\qquad
L_i(t)=\frac{(\tau_i-t)_+^{n-2}}{(n-2)!},\qquad
B_i=L_i-\Pi_w L_i,
\tag{11.8}
$$

where $\Pi_w$ is orthogonal projection onto $\mathcal P_{n-1}$ in the weighted inner product $\langle v,z\rangle_w=\int wvz$. The weight is positive almost everywhere and integrable. By Theorem 12 all residual roots are simple, so the transverse-root estimates of Section 9 justify continuously differentiating the normal equations in the switching parameters. Their coefficient Gram matrix is positive definite. The same sublevel argument and the envelope formula make $J$ twice continuously differentiable near this configuration.

With the unnormalized potential $U=I^n(|R|^{q-2}R)$, differentiation gives

$$
\begin{aligned}
J_i&=2q\sigma_iU'(\tau_i)=0,\\
J_{ij}&=4q(q-1)\sigma_i\sigma_j\langle B_i,B_j\rangle_w
+2q\sigma_i\delta_{ij}U''(\tau_i).
\end{aligned}
\tag{11.9}
$$

For $n=3$, the second derivative of a moving kernel is an indicator. Its contribution is still justified by dominated convergence against the bounded signed residual power; no boundary term is introduced. The weighted term is controlled by the integrable transverse-root estimates.

Define $D_i=-\sigma_iU''(\tau_i)>0$ and $G_{ij}=\sigma_i\sigma_j\langle B_i,B_j\rangle_w$. Every nearby sign load has dual norm at most $V$, so the Hessian in (11.9) must be negative semidefinite. Equivalently,

$$
2(q-1)G\preceq\operatorname{diag}(D_1,\ldots,D_r),
\tag{11.10}
$$

where $\preceq$ denotes comparison of quadratic forms. This is a necessary condition for every finite-exponent variation maximizer. Theorem 12 justifies its finite, nondegenerate setting; Theorem 13 below excludes $r=2$. It remains to exclude every configuration with $r\ge3$ satisfying it, or prove that such a configuration has a smaller value than the midpoint load. No such general exclusion is asserted here.

## 12. Two switches are unstable

The translation direction in the Hessian has a stronger consequence than the finite Hilbert diagnostic: it excludes a two-switch maximizer at every finite exponent, without a symmetry assumption.

**Theorem 13 (two-switch exclusion).** Let $n\ge3$ and $1<p<\infty$. A nonzero global variation maximizer cannot have exactly two interior critical points. Consequently its critical-point count is either one or at least three.

### 12.1. A polynomial cancellation under translation

Suppose otherwise, and write the critical points as $a<b$. Choose the sign so that $u'>0$ near zero. Put $m=n-1$, $q=p/(p-1)$, $F=|R|^{q-2}R$ and $U=I^nF$, so $U$ is a positive multiple of $u$. By Theorem 12, the sign load is $+1,-1,+1$ on the three successive intervals, all residual roots are simple, and

$$
F(0)>0,\qquad F(1)=(-1)^{n+1}F(0).
\tag{12.1}
$$

The signs follow from the $n+1$ residual roots, and equality of the endpoint magnitudes follows from (11.5).

Translate both switches to $a+s,b+s$. Modulo $\mathcal P_m$, the load is $H_s=2K_{a+s}-2K_{b+s}$. Let $R_s=H_s-P_s$ be its best $L^q$ residual and $U_s=I^n(|R_s|^{q-2}R_s)$. A dot denotes differentiation in $s$ at zero. Since differentiation in $s$ cancels differentiation in the integration variable for each translated kernel,

$$
T=\dot R+R'=-\dot P-P'\in\mathcal P_m.
\tag{12.2}
$$

Define

$$
W=\dot U+U',\qquad W^{(n)}=(q-1)|R|^{q-2}T.
\tag{12.3}
$$

The simple-root estimates used in Section 11 justify differentiation of the signed residual power in $L^1$, even when $1<q<2$. They also give $F'=(q-1)|R|^{q-2}R'\in L^1$. Thus $W\in W^{n,1}(0,1)\subset C^{n-1}[0,1]$, and (12.3) is an almost-everywhere identity with a positive almost-everywhere integrable weight.

The moment equations make every $U_s$ clamped. Their differentiated equations make $\dot U$ clamped as well. Therefore

$$
\begin{aligned}
W^{(j)}(0)&=W^{(j)}(1)=0 &&(0\le j\le n-2),\\
W^{(n-1)}(0)&=F(0),&\qquad W^{(n-1)}(1)&=F(1).
\end{aligned}
\tag{12.4}
$$

### 12.2. The auxiliary function has a single peak

Put $z=W'$. Its endpoint zeros have exact multiplicity $n-2$. Equations (12.1) and (12.4) show that $z>0$ just after zero and $z<0$ just before one. We claim that $z$ has exactly one interior zero.

Here is the required weighted Rolle count. If selected interior zeros of $z$ have total multiplicity $N$, counting a zero with $z'=0$ twice, repeated Rolle arguments through $n-2$ derivatives give at least $n-2+N$ distinct zeros of $W^{(n-1)}$. Between consecutive zeros the integral of $|R|^{q-2}T$ vanishes. Positivity of the weight forces a root of the polynomial $T$ in every such open interval. The polynomial is nonzero: otherwise $W$ would be a polynomial of degree at most $n-1$ with endpoint zeros of multiplicity $n-1$ at both ends, contradicting $F(0)>0$. Hence

$$
n-3+N\le\deg T\le n-1,\qquad N\le2.
\tag{12.5}
$$

This reasoning uses an integral between zeros of the absolutely continuous function $W^{(n-1)}$; it does not differentiate the weight or assign a finite value to it at a residual zero.

There must be a sign-changing zero of $z$ because its endpoint signs are opposite. Two distinct sign-changing zeros would require a third to give these endpoint signs. Any additional tangency contributes multiplicity at least two and, together with the sign-changing zero, also violates (12.5). An infinite zero set is excluded by selecting three distinct zeros. Thus $z$ has exactly one interior zero $c$, and

$$
W'>0\quad(0,c),\qquad W'<0\quad(c,1).
\tag{12.6}
$$

In particular $W$ is strictly unimodal and positive in the interior.

### 12.3. Orthogonality gives a positive second variation

Since $T\in\mathcal P_m$, the moment equations give $\int FT=0$, and (12.3) gives $\int RW^{(n)}=0$. Integrating by parts $n-1$ times, the only possible boundary term is
$[RW^{(n-1)}]_0^1=[RF]_0^1=0$ by (11.5). Using (11.3) and $W(0)=W(1)=0$, we obtain

$$
0=\int_0^1RW^{(n)}
=\int_0^1gW'=2\{W(a)-W(b)\}.
\tag{12.7}
$$

Strict unimodality and $a<b$ now imply $a<c<b$. Let $J(s)=\int|R_s|^q$. The envelope identity near zero and its derivative at zero give

$$
\begin{aligned}
J'(s)&=2q\{U_s'(a+s)-U_s'(b+s)\},\\
J''(0)&=2q\{W'(a)-W'(b)\}>0.
\end{aligned}
\tag{12.8}
$$

Every nearby translated sign load has dual norm at most the sharp variation norm attained at $s=0$. The strict positivity in (12.8) contradicts this local maximum, proving Theorem 13. $\square$

For three or more switches, the same translation cancellation gives an alternating sum in (12.7). It no longer equates the values at just two points, so the sign conclusion in (12.8) does not follow. No exclusion of all such configurations is asserted.

## 13. Affine motion and the three-switch obstruction

The dilation direction complements common translation. It excludes a midpoint-symmetric three-switch maximizer and imposes a further necessary geometric condition on every remaining three-switch candidate.

**Theorem 14 (three-switch dilation test).** Let $n\ge3$ and $1<p<\infty$. A global variation maximizer that is symmetric about the midpoint cannot have exactly three interior critical points. More generally, if a global maximizer has exactly three critical points $a<b<c$, the unique minimum of the auxiliary function for dilation about $b$, defined below, must lie outside the closed interval $[a,c]$.

### 13.1. The general affine cancellation

Use the notation of Section 11, put $m=n-1$, $d=mq+1$, and set $F=|R|^{q-2}R$, $U=I^nF$. Fix an affine velocity $v(t)=A+Bt$ and move the switches along $\tau_i(s)=\tau_i+s v(\tau_i)$. A dot denotes differentiation at zero. The kernel identity

$$
v(\tau)\partial_\tau K_\tau(t)+v(t)\partial_tK_\tau(t)=mB K_\tau(t)
$$

shows that

$$
T_v=\dot R+vR'-mBR\in\mathcal P_m.
\tag{13.1}
$$

Define

$$
W_v=\dot U+vU'-BdU,\qquad
W_v^{(n)}=(q-1)|R|^{q-2}T_v.
\tag{13.2}
$$

As in Section 12, simple residual roots justify parameter and spatial differentiation of the signed residual power in $L^1$. Thus $W_v\in W^{n,1}$, its endpoint derivatives through order $n-2$ vanish, and

$$
W_v^{(n-1)}(0)=v(0)F(0),\qquad
W_v^{(n-1)}(1)=v(1)F(1).
\tag{13.3}
$$

Polynomial orthogonality gives $\int RW_v^{(n)}=0$. After $n-1$ integrations by parts, the surviving boundary term is $[vRF]_0^1=B|R(0)|^q$. Hence

$$
2\sum_i\sigma_i W_v(\tau_i)=-B|R(0)|^q.
\tag{13.4}
$$

Let $\mathcal H$ be the Hessian in (11.9), and let $\mathbf v=(v(\tau_i))_i$. Since $U'(\tau_i)=0$, differentiating the envelope formula gives

$$
(\mathcal H\mathbf v)_i=2q\sigma_iW_v'(\tau_i),\qquad
\mathbf v^T\mathcal H\mathbf v
=2q\sum_i\sigma_i v(\tau_i)W_v'(\tau_i).
\tag{13.5}
$$

Indeed $W_v'=\dot U'+vU''+B(1-d)U'$, and the last term vanishes at the switches. The switch path is affine in $s$, so there is no acceleration term.

### 13.2. Dilation about the middle switch

Suppose there are exactly three switches $a<b<c$, and choose the sign so that $F(0)>0$. Their signs are $+,-,+$. The $n+2$ simple residual zeros and equal endpoint magnitudes give $F(1)=(-1)^nF(0)$. Take $v(t)=t-b$. Equation (13.3) implies that $W_v'<0$ near zero and $W_v'>0$ near one, with endpoint zeros of exact multiplicity $n-2$.

The weighted Rolle argument in (12.5) applies verbatim to (13.2): $W_v'$ has at most two interior zeros counted with the same multiplicity convention. Its opposite endpoint signs exclude a second zero or tangency. Consequently there is a unique interior point $z$ such that

$$
W_v'<0\quad(0,z),\qquad W_v'>0\quad(z,1).
\tag{13.6}
$$

The auxiliary function is negative in the interior and has its unique minimum at $z$. If $a\le z\le c$, the middle switch has zero velocity and (13.5) becomes

$$
\mathbf v^T\mathcal H\mathbf v
=2q\{(a-b)W_v'(a)+(c-b)W_v'(c)\}>0.
\tag{13.7}
$$

Both summands are positive when $a<z<c$. At either endpoint of $[a,c]$, one vanishes and the other remains positive. This contradicts maximality. Any remaining three-switch global maximizer therefore requires $z<a$ or $z>c$.

### 13.3. Midpoint symmetry excludes three switches

If $u(1-t)=u(t)$, its three simple critical points are $a,1/2,1-a$, with $a<1/2$. Dilation about $1/2$ preserves this symmetry of the switch set. Every moved sign load is antisymmetric. Reflection and uniqueness of best $L^q$ polynomial approximation give $R_s(1-t)=(-1)^nR_s(t)$; the clamped potentials $U_s$ are consequently symmetric. Thus $\dot U$, $(t-1/2)U'$ and $W_v$ are symmetric as well.

The unique minimum in (13.6) is therefore at $z=1/2$, between the outer switches. In particular,

$$
\mathbf v^T\mathcal H\mathbf v
=4q(1/2-a)W_v'(1-a)>0,
\tag{13.8}
$$

contradicting maximality and completing the proof of Theorem 14. $\square$

The theorem does not establish symmetry of arbitrary variation maximizers. For a nonsymmetric three-switch candidate, it remains to exclude the response-minimum locations $z<a$ and $z>c$, or find another positive Hessian direction. Configurations with at least four switches also remain open.

## 14. A limitation of weighted Hilbert reduction

The constant derivative weight in Theorem 1 cannot be replaced by an arbitrary positive weight. This matters for a possible reduction of the remaining finite-exponent problem. For a positive bounded weight $a$ bounded away from zero, put

$$
C(a)=\sup_{u\ne0}\frac{\|u\|_\infty}{E_a(u)^{1/2}},\qquad
V(a)=\sup_{u\ne0}\frac{\|u'\|_1}{E_a(u)^{1/2}},\qquad
E_a(u)=\int_0^1a(t)|u'''(t)|^2\,dt,
\tag{14.1}
$$

where the suprema run over $W_0^{3,2}(0,1)$.

**Theorem 15 (failure of the arbitrary-weight extension).** There exists a positive bounded piecewise-constant weight $a$, bounded away from zero, such that

$$
V(a)^2>\frac{967}{10^6},\qquad
4C(a)^2<\frac{900}{10^6}.
\tag{14.2}
$$

Such weights also exist in $C^\infty([0,1])$. In particular, the arbitrary-weight version of $V=2C$ and the assertion that every weighted variation maximizer is single-peaked are false. This is a weighted counterexample; it does not disprove [NS, Conjecture 4.14].

### 14.1. Dual formulas and an explicit weight

Write $\rho=1/a$ and $\langle f,h\rangle_\rho=\int_0^1\rho fh$. Let $P_\rho$ be the orthogonal projection onto $\mathcal P_2$ in this inner product. The endpoint conditions on $u$ are equivalent to the three moments $\int_0^1t^j u'''(t)\,dt=0$, $0\le j\le2$. Weighted Hilbert duality therefore gives

$$
4C(a)^2=\max_{0\le x\le1}D(x),\qquad
D(x)=\|(I-P_\rho)h_x\|_\rho^2,\qquad h_x(t)=(x-t)_+^2.
\tag{14.3}
$$

For a sign load with switches $b<c$ and successive signs $+,-,+$, integration of the load against the derivative kernel gives $h_b-h_c$ modulo $\mathcal P_2$. Hence

$$
V(a)^2\ge J,\qquad J=\|(I-P_\rho)(h_b-h_c)\|_\rho^2.
\tag{14.4}
$$

These formulas have no numerical approximation. For example, if $R=(I-P_\rho)(h_b-h_c)$ and $u'''=\rho R$ with zero initial derivatives, the moment equations give the right endpoint conditions, $E_a(u)=J$, and $\int gu'=J$. Thus $\|u'\|_1/E_a(u)^{1/2}\ge\sqrt J$.

Take $b=3/7$, $c=6/7$ and

$$
\rho(t)=\frac1{100}+\sum_{j=1}^6\frac{m_j}{2\varepsilon}
\mathbf1_{[c_j-\varepsilon,c_j+\varepsilon]}(t),\qquad
\varepsilon=\frac1{1000},
\tag{14.5}
$$

with

$$
(c_1,\ldots,c_6)=\frac1{100}(3,6,13,85,87,97),\qquad
(m_1,\ldots,m_6)=(1,1,1,1000,3000,5).
\tag{14.6}
$$

In particular $1/100\le\rho\le1500000+1/100$, so $a=1/\rho$ satisfies all the hypotheses in (14.1).

### 14.2. A rational certificate on the entire evaluation interval

Here the explicit counterexample is proved by finite exact polynomial arithmetic, not by testing finitely many evaluation points. We give the formulas and a positive Bernstein certificate covering every $x\in[0,1]$.

Let $A_{ij}=\int_0^1\rho(t)t^{i+j}\,dt$, $0\le i,j\le2$, and let $B_i(x)=\int_0^1\rho(t)t^i h_x(t)\,dt$. Then

$$
D(x)=\int_0^1\rho(t)h_x(t)^2\,dt-B(x)^T A^{-1}B(x).
\tag{14.7}
$$

The matrix $A$ is positive definite. All its entries and the required polynomial coefficients are rational. For full reproducibility, define

$$
F_{k,r}(x,z)=\sum_{j=0}^r(-1)^j\binom rj
\frac{x^{r-j}z^{k+j+1}}{k+j+1}.
\tag{14.8}
$$

On a constant-weight interval $[l,s]$ lying to the left of $x$, its contribution to $\int\rho t^k(x-t)_+^r\,dt$ is $\rho\{F_{k,r}(x,s)-F_{k,r}(x,l)\}$. On the interval containing $x$, replace $s$ by $x$. Intervals to the right contribute zero. Use $(k,r)=(0,2),(1,2),(2,2),(0,4)$ in (14.7). On each of the thirteen constant-weight intervals, $D$ is thus a polynomial of degree at most ten.

For $Q(x)=9/10000-D(x)$, write on a subinterval $[l,s]$

$$
Q(l+(s-l)y)=\sum_{k=0}^{10}q_k y^k
=\sum_{i=0}^{10}\beta_i\binom{10}{i}y^i(1-y)^{10-i},\qquad
\beta_i=\sum_{k=0}^i q_k\frac{\binom ik}{\binom{10}k}.
\tag{14.9}
$$

A polynomial of lower degree is padded by zero coefficients. The following table gives rational lower bounds: on each row every $\beta_i$ is at least the displayed integer divided by $10^9$. The only added subdivision of a constant-weight interval is at $49/100$.

| $1000l$ | $1000s$ | Lower bound numerator |
| ---: | ---: | ---: |
| 0 | 29 | 899999 |
| 29 | 31 | 899999 |
| 31 | 59 | 899579 |
| 59 | 61 | 899452 |
| 61 | 129 | 863685 |
| 129 | 131 | 860777 |
| 131 | 490 | 96932 |
| 490 | 849 | 88748 |
| 849 | 851 | 339729 |
| 851 | 869 | 337888 |
| 869 | 871 | 480234 |
| 871 | 969 | 511776 |
| 969 | 971 | 899999 |
| 971 | 1000 | 899999 |

The Bernstein basis is nonnegative and sums to one on $[0,1]$. Every entry is positive, so the table proves $D(x)<9/10000$ on the entire closed interval. Exact integration and the same moment projection give

$$
J=\frac{8182370250764298579352352052564188484681}
{8455630511289484805583272519708405000000000}
>\frac{967}{10^6}.
\tag{14.10}
$$

Equations (14.3)--(14.4) now prove (14.2). The accompanying [certificate generator](certify_counterexample.py) computes the piecewise polynomials and their exact Bernstein coefficients. A separate [interpolation checker](check_certificate_independent.py) evaluates the integrals at eleven rational points per interval, reconstructs the degree-at-most-ten polynomial, and verifies every printed bound and the exact fraction (14.10). Interpolation is exact here because the degree bound is already proved. Both programs use rational arithmetic for all decisive comparisons. The initial floating-point search is not part of this proof.

### 14.3. Smooth weights and the limit of freezing

Extend $\rho$ by $1/100$ outside $[0,1]$ and convolve with nonnegative smooth approximate identities. The resulting $\rho_\delta$ are smooth, obey the same positive lower and upper bounds, and converge to $\rho$ in $L^1(0,1)$. The moment matrices converge to $A$, so their inverses converge. The kernels $h_x$ are uniformly bounded for $0\le x,t\le1$; therefore all moments in (14.7), and hence $D_\delta(x)$, converge uniformly in $x$. The fixed two-switch energy $J_\delta$ also converges to $J$. The strict gaps in (14.2) persist for sufficiently small $\delta$. Taking $a_\delta=1/\rho_\delta$ proves the smooth assertion. Weighted variation maximizers exist by the compact embedding of the equivalent Hilbert norm into $C^1[0,1]$. A single-peaked function vanishing at both endpoints has variation twice its height, so none can maximize when $V(a)>2C(a)$. $\square$

The counterexample closes one tempting route to the original problem. If $1<p<2$ and $u$ is a norm-one global maximizer with $f=u^{(n)}$, define $a=|f|^{p-2}$ away from its finite zero set. For every clamped $h$ with finite weighted energy, Holder's inequality gives

$$
\int_0^1|h^{(n)}|^p
\le\left(\int_0^1a|h^{(n)}|^2\right)^{p/2}
\left(\int_0^1|f|^p\right)^{(2-p)/2}
=\left(\int_0^1a|h^{(n)}|^2\right)^{p/2}.
\tag{14.11}
$$

Thus $u$ also maximizes variation in this weighted Hilbert problem. However, a general weighted single-peak theorem is false by Theorem 15. Any successful use of (14.11) must exploit the special relation between the weight and the original maximizer. Our example is not shown to have this relation. The corresponding transfer for $p>2$ is not established by (14.11).

The recent weighted result of Hindov and Lokharu [HL, Theorem 1] places a weight on the function's $L^1$ norm and leaves the derivative energy unweighted. It has no additional mean constraint of the kind obtained by setting $v=u'$. It therefore supplies neither the arbitrary derivative-weight assertion disproved here nor the missing constrained variation theorem.

## 15. Remaining questions

The full all-exponent form of [NS, Conjecture 4.14] remains unresolved. Theorem 9 completes its measure endpoint, and Theorems 5 and 11 give exponent intervals around two and immediately above one. Their widths and overlap are not established. Theorem 10 proves height symmetry and uniqueness at every finite exponent. Theorem 12 now proves that every finite-exponent variation maximizer has finitely many nondegenerate critical points and simple dual-residual zeros, so the stability matrix (11.10) applies without a regularity assumption. Theorem 13 excludes every two-switch maximizer. Theorem 14 excludes midpoint-symmetric three-switch maximizers and imposes a response-minimum condition on any remaining three-switch candidate. The remaining finite-exponent task is to exclude nonsymmetric three-switch maximizers and configurations with at least four switches. The endpoint p=infinity also remains to be addressed for the full variation statement. Theorem 15 rules out a reduction that assumes the same identity for arbitrary derivative weights. The special weights generated by an actual maximizer remain a possible restricted route. A necessary matrix condition and finite examples are not a universal exclusion theorem. The stronger centroid and knot-reflection inequalities in the research notes remain unproved and are not needed for the results above.

## References

[ABR] S. Axler, P. Bourdon and W. Ramey, *Harmonic Function Theory*, second edition, Springer, 2001 (author PDF revision July 17, 2020). [Author text](https://axler.net/HFT.pdf), formula (1.15), Theorem 1.17 and Chapter 5.

[BH] A. Burchard and H. Hajaiej, *Rearrangement inequalities for functionals with monotone integrands*, Journal of Functional Analysis **233** (2006), 561--582. [DOI](https://doi.org/10.1016/j.jfa.2005.08.010). [Final revised author version](https://arxiv.org/abs/math/0506336).

[dB] C. de Boor, *Divided Differences*, Surveys in Approximation Theory **1** (2005), 46--69. [Author text](https://arxiv.org/abs/math/0502036), formulas (47)--(48) and (52).

[dB03] C. de Boor, *Math/CS 887 course notes*, Spring 2003, TeX version November 21, 2009. [Author notes](https://pages.cs.wisc.edu/~deboor/887/notes.pdf), p. 74, centered cubic Chebyshev-spline example.

[F] S. Foucart, *Interlacing property for B-splines*, Journal of Approximation Theory **135** (2005), no. 1, 1--21. [DOI](https://doi.org/10.1016/j.jat.2005.03.001). [Author preprint, February 24, 2005](https://foucart.github.io/publi/tbsm2.pdf), Lemma 3, Formulae 5 and Proposition 6.

[GHW] R. J. Gardner, D. Hug and W. Weil, *The Orlicz-Brunn-Minkowski theory: A general framework, additions, and inequalities*, Journal of Differential Geometry **97** (2014), no. 3. [DOI](https://doi.org/10.4310/jdg/1406033976). [Author text](https://arxiv.org/abs/1301.5267).

[GS] T. A. Garmanova and I. A. Sheipak, *Sharp Estimates of High-Order Derivatives in Sobolev Spaces*, Moscow University Mathematics Bulletin **79** (2024), 1--10. [DOI](https://doi.org/10.3103/S0027132224700013).

[HL] R. Hindov and E. Lokharu, *On a class of sharp Sobolev type estimates with weights*, arXiv:2605.25637v1 (2026). [Author preprint](https://arxiv.org/abs/2605.25637), Theorem 1.

[HNOR] R. Hindov, S. Nitzan, J.-F. Olsen and E. Rydhe, *A sharp higher order Sobolev embedding*, Mathematika **71** (2025), e70012. [DOI](https://doi.org/10.1112/mtk.70012). [Author preprint](https://arxiv.org/abs/2411.10201).

[K] G. A. Kalyabin, *Sharp Estimates for Derivatives of Functions in the Sobolev Classes $W_2^r(-1,1)$*, Proceedings of the Steklov Institute of Mathematics **269** (2010), 137--142. [DOI](https://doi.org/10.1134/S0081543810020112).

[NS] A. I. Nazarov and A. P. Shcheglova, *A Survey of Results on 1D Steklov Type Inequalities*, Proceedings of the Steklov Institute of Mathematics **331** (2025), 134--147; published online March 19, 2026. [DOI](https://doi.org/10.1134/S0081543825601509). [Latest author preprint](https://arxiv.org/abs/2101.10752).

[W] K. Watanabe, Y. Kametaka, A. Nagai, H. Yamagishi and K. Takemura, *Symmetrization of Functions and the Best Constant of 1-DIM $L^p$ Sobolev Inequality*, Journal of Inequalities and Applications **2009**, Article 874631, 12 pp. [DOI](https://doi.org/10.1155/2009/874631), Theorem 1.1, Lemma 1.3 and Remark 1.4.
