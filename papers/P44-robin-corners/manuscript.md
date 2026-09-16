# Robin ground states on convex polyhedra: concavity and vanishing spectral gaps

Henry Zweiman

September 15, 2026

## Abstract

We disprove the universal positive-Robin fundamental-gap conjecture: in every dimension at least four, for each fixed positive Robin parameter and each fixed diameter, the infimum of the gap over bounded convex polyhedra is zero. An explicit four-dimensional family has three-dimensional cross-sections whose surface-area-to-volume ratio is larger in the middle than at the ends. Elementary variational estimates force the ground-state mass toward the two ends; an odd ground-state multiple and nested cutoffs give an exponentially small gap. A concrete member disproves both the convex-domain Robin gap monotonicity conjecture and Laugesen's spectral-ratio monotonicity conjecture. An asymmetric modification also disproves his conjecture that the second Robin eigenvalue is concave in the positive parameter: a fully proved limit to two half-line operators gives a strict midpoint violation on a fixed convex polyhedron. For the latter, we prove that the Robin ratio lies strictly below the Dirichlet ratio on the same fixed domain, using the established Dirichlet fundamental-gap theorem. Independently, we prove that the positive parameters with a log-concave ground state form a locally finite set on every convex polygon that is neither tangential nor rectangular, disproving the general eventual log-concavity conjecture of Andrews, Clutterbuck and Hauer. We also prove their full small-parameter polyhedral quasiconcavity conjecture by a global Hessian-norm rigidity argument for the Neumann first variation. The gap proof is independent of the corner regularity arguments and leaves dimensions two and three open.

**Keywords:** Robin eigenfunction; log-concavity; polygonal domain; corner singularity; analytic perturbation; quasiconcavity; fundamental gap; eigenvalue ratio; spectral geometry.

**2020 Mathematics Subject Classification:** 35P15, 35J25, 35B65, 35P05, 47A55.

## 1. Introduction

For a bounded convex polygon $P\subset\mathbb R^2$ with nonempty interior, let $u_\alpha$ be the positive first Robin eigenfunction:

$$
-\Delta u_\alpha=\lambda_\alpha u_\alpha\quad\text{in }P,
\qquad \partial_\nu u_\alpha+\alpha u_\alpha=0
\quad\text{on }\partial P.
\tag{1.1}
$$

The boundary condition is understood weakly; on the interior of an edge it is classical. We fix the normalization

$$
\int_P u_\alpha^2\,dx=|P|.
\tag{1.2}
$$

In particular, $u_0=1$ and $\lambda_0=0$. Log-concavity means concavity of $\log u_\alpha$ in the open convex set $P$.

Andrews, Clutterbuck and Hauer [ACH] proved failure of log-concavity for sufficiently small positive Robin parameters on convex polyhedra outside a geometrically distinguished class. Their final Section 10, Conjecture 1, asks whether every fixed bounded convex domain has a threshold above which its Robin ground state is log-concave. Crasta and Fragalà [CF] established eventual log-concavity on sufficiently smooth uniformly convex domains. Ye and Zhang [YZ] recently reduced the boundary assumption to $C^{3,1}$ in every dimension. These theorems leave open the conjecture on convex domains with corners.

A polygon is *tangential* if it contains a disk tangent to every edge. This is the planar instance of a circumsolid in [ACH]. In dimension two, products of circumsolids are precisely tangential polygons and rectangles. We take polygonal descriptions with no redundant collinear vertices, so every interior angle belongs to $(0,\pi)$.

**Theorem 1.1.** Let $P$ be a bounded convex polygon that is neither tangential nor a rectangle. There exist an obtuse vertex $v_*$ and a real-analytic function $c:\mathbb R\to\mathbb R$ with

$$
c(0)=0,\qquad c'(0)\ne0,
\tag{1.3}
$$

such that, whenever $\alpha>0$ and $c(\alpha)\ne0$, neither $u_\alpha$ nor $\log u_\alpha$ is semiconcave on any sufficiently small neighborhood $P\cap B_r(v_*)$. Consequently

$$
\{\alpha>0:u_\alpha\text{ is log-concave in }P\}
\subseteq\{\alpha>0:c(\alpha)=0\}.
\tag{1.4}
$$

The set on the left is locally finite, and it is empty for all sufficiently small positive parameters. In particular, for every $A>0$ there is an $\alpha>A$ for which $u_\alpha$ is not log-concave.

Here semiconcavity on a convex set means that $f(x)-M|x|^2/2$ is concave for some finite constant $M$. The assertion near $v_*$ refers to each sufficiently small radius, with no uniformity in $\alpha$ required. In fact, the exceptional zero set is finite on every bounded parameter interval, including intervals meeting zero.

**Corollary 1.2.** The polygon with consecutive vertices

$$
(0,0),\quad(2,0),\quad(3,1),\quad(1,1)
\tag{1.5}
$$

does not have an eventual log-concavity threshold. There are bounded convex polyhedral counterexamples in every dimension $d\ge2$.

The new point is the continuation of a regularity obstruction through the entire finite Robin parameter axis. The first-variation classification in [ACH] supplies the initial nonzero corner mode. We extract its continuation by a bounded functional on a fixed Sobolev space, then use the identity theorem for real-analytic functions. Thus the argument does not extrapolate a small-parameter asymptotic estimate to large parameters.

We do not determine whether log-concavity occurs at any of the exceptional parameters. Nor do we prove a classification for tangential polygons. Section 6 gives nonconvex superlevel sets on fixed prisms in every dimension at least three for all parameters outside the same discrete set. Section 8 proves the full small-parameter result in [ACH, Section 10, Conjecture 2]:

**Theorem 1.3 (polyhedral quasiconcavity conjecture).** On every bounded convex polyhedron $\Omega\subset\mathbb R^d$, $d\ge3$, which is not a product of circumsolids, the first Robin eigenfunction has a nonconvex superlevel set for every sufficiently small positive Robin parameter.

A product of circumsolids is an orthogonal Cartesian product of polyhedra each circumscribed about a ball. Theorem 1.3 follows from a new global rigidity statement for the Neumann first variation, proved as Theorems 8.1--8.2. Its proof uses the spherical spectral lower bound and inconsistent-normal obstruction of [ACH], but does not assume their proposed higher-dimensional transverse-cone lemma. Section 7 gives an independent restricted result on that local question. Section 9 resolves the separate universal fundamental-gap conjecture from the same final section of [ACH]:

**Theorem 1.4 (positive Robin gaps).** For each $d\ge4$, $D>0$ and $\alpha>0$, the infimum of $E_1(G;\alpha)-E_0(G;\alpha)$ over bounded open convex polyhedra $G\subset\mathbb R^d$ of diameter $D$ is zero. Here $E_0<E_1$ are the first two Robin eigenvalues with zero potential.

Theorem 9.1 proves this assertion with an explicit thin-polyhedron construction. Corollary 9.3 gives a domain described by rational inequalities whose gap at parameter one is less than $1/100$, while the comparison interval's gap is greater than one. Corollary 9.4 also disproves the positive-parameter gap monotonicity conjecture recorded in [L, Conjecture A]. These results use elementary form estimates and symmetry, independently of Sections 2--8. The universal conjectures fail already in dimension four; their restrictions to dimensions two and three remain open here.

Section 10 strengthens the localization estimate to an exponential upper bound and answers a different conjecture from the same survey:

**Theorem 1.5 (failure of ratio monotonicity).** For each $d\ge4$, $D>0$ and $\alpha_*>0$, there is a bounded open convex polyhedron $G\subset\mathbb R^d$ of diameter $D$ whose ratio $E_1(G;\alpha_*)/E_0(G;\alpha_*)$ is strictly smaller than its Dirichlet eigenvalue ratio. Consequently the Robin ratio increases between some two positive parameters on that fixed domain, disproving [L, Conjecture B].

The proof compares an exponentially small Robin relative gap with the Dirichlet relative gap, using the established theorem of Andrews and Clutterbuck [AC]. Proposition 10.4 gives an entirely explicit instance with rational bounds. The recent ball monotonicity theorem of Dai and Sun [DS] remains consistent with these polyhedral counterexamples. The different second-eigenvalue concavity conjecture [L, Conjecture C] is answered in Section 11:

**Theorem 1.6 (failure of second-eigenvalue concavity).** In every dimension $d\ge4$ and at every prescribed diameter, there is a bounded open convex polyhedron on which the second Robin eigenvalue is not concave in the positive parameter.

We replace the two symmetric end regions by asymmetric regions whose limiting ground energies exchange order. A complete variational convergence proof, including the Robin end caps and the ordering of low eigenvalues, produces a strict concavity violation at three positive parameters on a single domain. Theorem 11.1 gives the precise statement. The first eigenvalue remains concave.

## 2. Analytic dependence and local regularity

We first record precisely the regularity needed for the coefficient construction. Write

$$
\Gamma_\omega=\{(r\cos\theta,r\sin\theta):r>0,\ 0<\theta<\omega\},
\qquad S_R=\Gamma_\omega\cap B_R(0),
\qquad \beta=\frac\pi\omega>1.
\tag{2.1}
$$

**Lemma 2.1 (sector regularity).** Suppose $z\in H^1(\Gamma_\omega)$ is supported in a fixed closed ball, has homogeneous weak Neumann data on the rays, and $\Delta z\in L^p(\Gamma_\omega)$, where $2\le p<\infty$. If

$$
2-\frac2p<\beta,
\tag{2.2}
$$

then $z\in W^{2,p}(\Gamma_\omega)$. For a fixed support radius the inclusion is continuous for the graph norm $\|z\|_{H^1}+\|\Delta z\|_{L^p}$.

*Proof.* This is a direct planar consequence of Dauge's wedge theorem [D, Theorem 8.1], which applies to compactly supported weak Neumann solutions on $\mathbb R\times\Gamma_\omega$ when $0<2-2/p<\pi/\omega$. To check the reduction, choose a nonzero $\eta\in C_c^\infty(\mathbb R)$ and set $Z(t,x)=\eta(t)z(x)$. Then $Z\in H^1$ has compact support and

$$
\Delta_{t,x}Z=\eta\Delta_xz+\eta''z\in L^p.
\tag{2.3}
$$

Here $z\in L^p$ follows from the planar $H^1$ embedding on a bounded sector containing its support. The boundary data of $Z$ are homogeneous Neumann. The cited theorem gives $Z\in W^{2,p}$, hence $z\in W^{2,p}$, for example by integration against a smooth function $\xi(t)$ with $\int\xi\eta=1$.

For continuity, consider the pairs $(z,f)\in H^1\times L^p$ with the fixed support restriction and

$$
\int_{\Gamma_\omega}\nabla z\cdot\nabla\varphi
=-\int_{\Gamma_\omega}f\varphi
\quad\text{for all }\varphi\in C_c^\infty(\overline{\Gamma_\omega}).
\tag{2.4}
$$

They form a closed subspace of $H^1\times L^p$. The map $(z,f)\mapsto z$ into $W^{2,p}$ has closed graph, since both limits agree as distributions. The closed graph theorem proves the estimate. ∎

**Lemma 2.2 (analytic eigenpair).** With normalization (1.2), the maps $\alpha\mapsto\lambda_\alpha$ and $\alpha\mapsto u_\alpha$ are real analytic on $\mathbb R$, the latter with values in $H^1(P)$.

*Proof.* The Robin form

$$
a_\alpha(f,g)=\int_P\nabla f\cdot\nabla g
+\alpha\int_{\partial P}fg
\tag{2.5}
$$

has fixed domain $H^1(P)$. The trace map is bounded, and a sufficiently large scalar shift makes the form coercive locally uniformly in $\alpha$. The first eigenvalue is simple and its eigenfunction can be chosen positive; see [ACH, Proposition 3.1].

For completeness, analytic dependence follows from the analytic implicit function theorem applied to

$$
(\alpha,u,\lambda)\longmapsto
\left(a_\alpha(u,\cdot)-\lambda(u,\cdot)_{L^2(P)},
\ (u,u)_{L^2(P)}-|P|\right)
\tag{2.6}
$$

with values in $(H^1(P))^*\times\mathbb R$. Its derivative in $(u,\lambda)$ sends $(h,s)$ to

$$
\left(B_\alpha h-s(u_\alpha,\cdot)_{L^2(P)},
\ 2(u_\alpha,h)_{L^2(P)}\right),
\quad B_\alpha=a_\alpha-\lambda_\alpha(\cdot,\cdot)_{L^2(P)}.
\tag{2.7}
$$

The operator $B_\alpha:H^1\to(H^1)^*$ is Fredholm of index zero, by a coercive shift and compactness of the $L^2$ embedding. Its kernel is the span of $u_\alpha$, and its range is the annihilator of $u_\alpha$. Pairing the first component with $u_\alpha$ determines $s$, the second component determines the component of $h$ along $u_\alpha$, and $B_\alpha$ is invertible on the complementary subspace. Thus (2.7) is an isomorphism. The local analytic branches remain the first eigenpair by the spectral gap. Positivity and (1.2) make them agree on overlaps, giving the asserted real-analytic maps. ∎

At a vertex translated to the origin, let $\nu_1,\nu_2$ be the two outward unit normals. They are linearly independent. Let $\gamma$ be the unique vector satisfying

$$
\nu_1\cdot\gamma=\nu_2\cdot\gamma=-1.
\tag{2.8}
$$

Define the local gauge

$$
w_\alpha(x)=e^{-\alpha\gamma\cdot x}u_\alpha(x).
\tag{2.9}
$$

It satisfies homogeneous Neumann conditions on both rays and

$$
\Delta w_\alpha=F_\alpha,
\qquad
F_\alpha=-2\alpha\gamma\cdot\nabla w_\alpha
-(\lambda_\alpha+\alpha^2|\gamma|^2)w_\alpha.
\tag{2.10}
$$

**Lemma 2.3 (regularity of the gauge).** On a sufficiently small fixed sector, $w_\alpha$ depends real analytically on $\alpha$ in $H^2$. Consequently $F_\alpha$ is real analytic in $L^p$ for every finite $p$. For each fixed $\alpha$, $w_\alpha$ is $C^{1,\delta}$ up to the vertex for some $\delta>0$, and

$$
\nabla w_\alpha(0)=0.
\tag{2.11}
$$

*Proof.* Choose a smooth radial cutoff $\chi$ supported strictly inside the radius on which $P$ agrees with the sector, and equal to one on a smaller sector. Extend $z_\alpha=\chi w_\alpha$ by zero to $\Gamma_\omega$. Its ray normal derivative is zero. Lemma 2.2 and multiplication by the exponential show that $z_\alpha$ is analytic in $H^1$. Moreover,

$$
\Delta z_\alpha
=\chi F_\alpha+2\nabla\chi\cdot\nabla w_\alpha
+(\Delta\chi)w_\alpha
\tag{2.12}
$$

is analytic in $L^2$. The pairs $(z_\alpha,\Delta z_\alpha)$ are therefore analytic in the closed graph space in Lemma 2.1. Since $1<\beta$, that lemma with $p=2$ makes $z_\alpha$ analytic in $H^2$. Planar Sobolev embedding gives analytic dependence of $w_\alpha$ and $\nabla w_\alpha$ in every finite $L^p$ on a smaller sector, and hence the claim about $F_\alpha$.

Choose $p>2$ sufficiently close to two that (2.2) holds. A second, nested radial cutoff and (2.12), now with $L^p$ data, give $w_\alpha\in W^{2,p}$ locally. Morrey embedding gives $C^{1,\delta}$ regularity, with $0<\delta<1-2/p$. The two Neumann conditions then hold at the vertex by continuity. The independent normals force (2.11). ∎

**Lemma 2.4 (positivity at the vertex).** If $\alpha>0$, then $w_\alpha(0)>0$.

*Proof.* On a sufficiently small sector put $\rho(x)=e^{2\alpha\gamma\cdot x}$ and $k=\lambda_\alpha+\alpha^2|\gamma|^2>0$. Equation (2.10) becomes

$$
-\operatorname{div}(\rho\nabla w_\alpha)=k\rho w_\alpha.
\tag{2.13}
$$

The ground state is positive in the interior. It is also positive at every point in the relative interior of either edge: otherwise the Hopf boundary lemma at that smooth boundary point would contradict the Robin condition. Thus $w_\alpha$ has a positive minimum $m$ on the closed outer circular arc of a small sector. Regularity from Lemma 2.3 gives continuity on its closure.

Use $\varphi=(m-w_\alpha)_+$ as a test function in (2.13), with zero trace on the outer arc and no restriction on the rays. The ray fluxes vanish, and $w_\alpha\ge0$. Hence

$$
-\int_{S_R}\rho|\nabla\varphi|^2
=k\int_{S_R}\rho w_\alpha\varphi\ge0.
\tag{2.14}
$$

It follows that $\varphi=0$, since its outer-arc trace is zero. Therefore $w_\alpha\ge m$ on the whole sector, including its vertex. ∎

## 3. A bounded functional for the corner coefficient

Fix an obtuse sector, so $1<\beta<2$, and a radius $R$ lying inside the region of Lemma 2.3. Set

$$
\begin{aligned}
a_\alpha(r)&=\frac2\omega\int_0^\omega
w_\alpha(r,\theta)\cos(\beta\theta)\,d\theta,\\
b_\alpha(r)&=\frac2\omega\int_0^\omega
F_\alpha(r,\theta)\cos(\beta\theta)\,d\theta.
\end{aligned}
\tag{3.1}
$$

**Lemma 3.1 (analytic coefficient).** The limit

$$
c(\alpha)=\lim_{r\downarrow0}r^{-\beta}a_\alpha(r)
\tag{3.2}
$$

exists for every real $\alpha$ and is a real-analytic function of $\alpha$. More precisely,

$$
\begin{aligned}
c(\alpha)={}&R^{-\beta}a_\alpha(R)\\
&-\frac1{2\beta}\int_0^R
\big(s^{1-\beta}-R^{-2\beta}s^{1+\beta}\big)b_\alpha(s)\,ds.
\end{aligned}
\tag{3.3}
$$

*Proof.* Angular projection of (2.10), using the homogeneous Neumann conditions, gives

$$
a_\alpha''+\frac1r a_\alpha'-\frac{\beta^2}{r^2}a_\alpha=b_\alpha.
\tag{3.4}
$$

This equation first holds distributionally away from zero; the functions are smooth there. Choose a finite exponent $p$ so large that

$$
p>\frac2{2-\beta},\qquad \kappa:=2-\frac2p>\beta.
\tag{3.5}
$$

Lemma 2.3 permits this choice for $F_\alpha$. Variation of constants in (3.4) gives the regular particular solution

$$
A_\alpha(r)=\frac1{2\beta}\left[
r^\beta\int_0^r s^{1-\beta}b_\alpha(s)\,ds
-r^{-\beta}\int_0^r s^{1+\beta}b_\alpha(s)\,ds\right].
\tag{3.6}
$$

Hölder's inequality, with planar area measure $s\,ds\,d\theta$, gives

$$
|A_\alpha(r)|+r|A_\alpha'(r)|
\le C r^\kappa\|F_\alpha\|_{L^p(S_r)}.
\tag{3.7}
$$

For the first integral the relevant weight is $s^{-\beta}$ relative to area measure. Its $L^{p'}$ norm is finite exactly when $\beta p'<2$, which is equivalent to (3.5). The second integral is less singular. The homogeneous solutions of (3.4) are $r^\beta$ and $r^{-\beta}$. The latter is excluded by $w_\alpha\in H^1(S_R)$, since its angular projection would have infinite $H^1$ energy. Thus

$$
a_\alpha(r)=c(\alpha)r^\beta+A_\alpha(r).
\tag{3.8}
$$

Equations (3.7) and (3.5) prove (3.2). Evaluating (3.8) at $R$ proves (3.3).

The trace functional $w\mapsto a(R)$ is bounded on $H^2$ on a sector extending past $R$. The integral in (3.3) is a bounded linear functional of $F\in L^p(S_R)$ by the same weighted Hölder estimate. Lemma 2.3 therefore proves analyticity of (3.3). The value is independent of the auxiliary radius because it equals the limit (3.2). ∎

Two different exponents have been used for different purposes. An exponent just above two yields $C^1$ regularity in Lemma 2.3. A much larger exponent is allowed for the forcing $F_\alpha$ in Lemma 3.1. No $W^{2,p}$ regularity of $w_\alpha$ is asserted for that larger exponent; generally it is false when $c(\alpha)\ne0$.

**Lemma 3.2 (semiconcavity annihilates the coefficient).** For $\alpha>0$, if either $u_\alpha$ or $\log u_\alpha$ is semiconcave on a neighborhood of the vertex, then $c(\alpha)=0$.

*Proof.* By Lemmas 2.3 and 2.4, $u_\alpha$, $w_\alpha$ and their logarithms are $C^1$ on a smaller closed sector, and the positive functions are bounded away from zero there. If $u_\alpha$ is semiconcave, its interior Hessian has an upper bound, while

$$
\Delta u_\alpha=-\lambda_\alpha u_\alpha
\tag{3.9}
$$

is bounded. In two dimensions a symmetric matrix with bounded trace and eigenvalues bounded above has eigenvalues bounded below as well. Therefore $D^2u_\alpha$ is bounded in the interior of that sector. Integration along segments in the convex sector gives $u_\alpha\in C^{1,1}$ up to the vertex, and multiplication by the smooth gauge gives $w_\alpha\in C^{1,1}$.

If $\log u_\alpha$ is semiconcave, put $q=\log w_\alpha=\log u_\alpha-\alpha\gamma\cdot x$. Subtracting a linear function preserves semiconcavity. Equation (2.10) gives

$$
\Delta q=-|\nabla q|^2-2\alpha\gamma\cdot\nabla q
-(\lambda_\alpha+\alpha^2|\gamma|^2).
\tag{3.10}
$$

Its right hand side is bounded. The same Hessian argument gives $q\in C^{1,1}$ and hence $w_\alpha\in C^{1,1}$.

In either case, (2.11) yields

$$
w_\alpha(x)=w_\alpha(0)+O(|x|^2).
\tag{3.11}
$$

The angular integral of $\cos(\beta\theta)$ is zero, so (3.1) gives $a_\alpha(r)=O(r^2)$. Since $\beta<2$, (3.2) forces $c(\alpha)=0$. The same argument works on every smaller corner neighborhood. ∎

## 4. The initial nonzero mode

Let

$$
v=\left.\frac{d u_\alpha}{d\alpha}\right|_{\alpha=0},
\qquad \mu=\frac{|\partial P|}{|P|}.
\tag{4.1}
$$

Differentiation of the weak eigenvalue equation and normalization gives

$$
\Delta v=-\mu\quad\text{in }P,
\qquad \partial_\nu v=-1\quad\text{on }\partial P,
\qquad \int_Pv=0.
\tag{4.2}
$$

We use the following established rigidity result, with regularity on the closure understood: by [ACH, Corollary 8.3], a solution of (4.2) is $C^2(\overline P)$ if and only if $P$ is a product of circumsolids. Thus it is not $C^2(\overline P)$ under the hypotheses of Theorem 1.1.

**Lemma 4.1 (nonzero first variation).** If $P$ is neither tangential nor a rectangle, there is an obtuse vertex for which the coefficient in Lemma 3.1 satisfies $c(0)=0$ and $c'(0)\ne0$.

*Proof.* At any vertex, translate the vertex to zero and choose $\gamma$ as in (2.8). The function

$$
h(x)=v(x)+\frac\mu4|x|^2-\gamma\cdot x
\tag{4.3}
$$

is harmonic with homogeneous Neumann data on the two rays. Indeed, the normal derivative of $|x|^2$ vanishes on either ray. Separation of variables gives

$$
h(r,\theta)=d_0+\sum_{j\ge1}d_j r^{j\pi/\omega}
\cos\left(\frac{j\pi\theta}{\omega}\right).
\tag{4.4}
$$

This expansion also follows from [ACH, Proposition 5.5]. It can be obtained directly by expanding the trace on an inner arc in the Neumann cosine basis. The $H^1$ condition excludes negative powers and the logarithmic zero mode. On every strictly smaller sector the series and its derivatives converge away from zero. Moreover, the part with exponents strictly greater than two has second derivatives tending to zero at the vertex: square summability of the trace coefficients and the geometric factor $(r/R)^{j\pi/\omega}$ justify termwise bounds on smaller radii.

If $\omega<\pi/2$, every nonconstant exponent exceeds two. If $\omega=\pi/2$, the first term is a harmonic quadratic polynomial, and all subsequent exponents exceed two. If $\pi/2<\omega<\pi$, only the first exponent $\beta=\pi/\omega$ lies below two, and the next is $2\beta>2$. Therefore failure of $C^2$ regularity at a vertex is possible only at an obtuse vertex with $d_1\ne0$.

The solution $v$ is smooth in the interior and up to the relative interiors of edges, by reflection after subtracting a local particular solution with the given normal derivative. If every vertex had a $C^2$ expansion, these local statements would give $v\in C^2(\overline P)$, contrary to the rigidity result above. Fix an obtuse vertex with $d_1\ne0$.

At this vertex $w_0=1$, so $c(0)=0$. Differentiating (2.9) and (2.10) at zero gives

$$
\dot w_0=v-\gamma\cdot x,
\qquad \dot F_0=-\mu.
\tag{4.5}
$$

The constant forcing has zero first cosine projection. The radial quadratic term in (4.3) also has zero first cosine projection. It follows from (3.3), which may be differentiated by Lemma 3.1, and (4.4) that

$$
c'(0)=d_1\ne0.
\tag{4.6}
$$

This is the claimed vertex and coefficient. ∎

*Proof of Theorem 1.1.* Choose the vertex from Lemma 4.1 and its analytic coefficient from Lemma 3.1. Since $c'(0)\ne0$, this real-analytic function is not identically zero. Its zero set is locally finite on $\mathbb R$, by the identity theorem, and zero is an isolated simple zero. Lemma 3.2 shows that semiconcavity of either $u_\alpha$ or its logarithm on any sufficiently small corner neighborhood forces $c(\alpha)=0$. This proves the local assertion and (1.4). A locally finite subset cannot contain any interval $(A,A+1)$, so there are arbitrarily large parameters outside the exceptional set. ∎

## 5. Explicit domains and the Dirichlet limit

*Proof of Corollary 1.2.* The polygon (1.5) is a parallelogram with adjacent side lengths $2$ and $\sqrt2$, and angles $\pi/4$ and $3\pi/4$. It is not a rectangle. A tangential quadrilateral has equal sums of opposite side lengths: the two tangent segments from each vertex have equal lengths, and summing them gives the identity. A tangential parallelogram must therefore have equal adjacent side lengths. Our polygon is not tangential, so Theorem 1.1 applies. At its obtuse vertices the relevant exponent is $\beta=4/3$.

For $d>2$, use

$$
\Omega_d=P\times(0,1)^{d-2}.
\tag{5.1}
$$

The positive product of the first Robin eigenfunctions on the factors satisfies the Robin condition with the same parameter on every face. Its eigenvalue is the sum of the first eigenvalues of the factors, and positivity identifies it with the ground state. Restriction to a slice with fixed interior coordinates in the interval factors is a positive constant multiple of $u_\alpha$ on $P$. Log-concavity of the product would imply log-concavity on this slice. Thus every parameter excluded for $P$ is excluded for $\Omega_d$. ∎

The contrast with the Dirichlet limit concerns regularity at the corners. A nonzero coefficient in (3.2) is compatible with convergence in weaker norms and with arbitrarily small amplitude as $\alpha$ increases. For each fixed finite parameter with $c(\alpha)\ne0$, however, the mode $r^\beta$ with $\beta<2$ prevents $C^{1,1}$ regularity of the gauge at the vertex. Semiconcavity would force that regularity through the bounded-trace argument of Lemma 3.2. No uniform $C^2$ convergence near the polygon's corners is available from a Dirichlet limit alone.

The results of [CF] and [YZ] assume smooth uniformly convex domains. Our polygonal examples satisfy neither boundary hypothesis. Approximating a polygon by smooth domains for a fixed parameter does not produce a single smooth domain with the discrete-exception property proved here, since the approximation can depend on the parameter. The remaining smooth-boundary questions must be treated separately.

The method suggests two further problems. One is to determine the exceptional parameters, or to show their absence for particular nonsymmetric polygons. Another is to understand eventual log-concavity within the tangential class, where the first-variation singular coefficient vanishes and the present initial-mode argument gives no obstruction. These questions are distinct from the conjecture for all convex domains, which Corollary 1.2 answers negatively.

## 6. Nonconvex superlevel sets on fixed prisms

A positive function $U$ on a convex domain is *quasiconcave* if every superlevel set $\{U>t\}$ is convex. For a smooth positive function, a strictly positive Hessian in a direction tangent to a level set of $\log U$ rules out quasiconcavity. We give the elementary argument in the following lemma.

**Lemma 6.1 (interval lifting).** Let $D\subset\mathbb R^m$ be an open convex set, let $f\in C^2(D)$ have bounded gradient, and suppose $f$ is not semiconcave on $D$. Let $I$ be an open interval and $h\in C^2(I)$ satisfy $h'(t_0)\ne0$ at some $t_0\in I$. Then

$$
U(x,t)=\exp(f(x)+h(t))
\tag{6.1}
$$

has a nonconvex superlevel set in $D\times I$.

*Proof.* If $D^2 f(x)[v,v]\le M$ for every $x\in D$ and every unit vector $v$, integration along segments shows that $f-M|x|^2/2$ is concave. Therefore, failure of semiconcavity gives points $x_j\in D$ and unit vectors $v_j$ such that

$$
D^2f(x_j)[v_j,v_j]\longrightarrow+\infty.
\tag{6.2}
$$

Put $F=\log U$ and

$$
s_j=-\frac{\nabla f(x_j)\cdot v_j}{h'(t_0)},
\qquad V_j=(v_j,s_j).
\tag{6.3}
$$

The numbers $s_j$ are bounded. At $z_j=(x_j,t_0)$ we have

$$
\nabla F(z_j)\cdot V_j=0,\qquad
D^2F(z_j)[V_j,V_j]
=D^2f(x_j)[v_j,v_j]+h''(t_0)s_j^2\longrightarrow+\infty.
\tag{6.4}
$$

Fix $j$ for which the last expression is positive. Since $z_j$ is interior, Taylor's theorem gives, for sufficiently small $\varepsilon>0$,

$$
F(z_j\pm\varepsilon V_j)>F(z_j).
\tag{6.5}
$$

Choose $b$ strictly between $F(z_j)$ and the smaller endpoint value. Both endpoints belong to $\{U>e^b\}$, while their midpoint does not. This proves the assertion. ∎

**Theorem 6.2 (persistent failure of quasiconcavity on prisms).** Let $P$ satisfy the hypotheses of Theorem 1.1, and let $c$ be its analytic corner coefficient. For every integer $d\ge3$, the first Robin eigenfunction on the fixed convex polyhedron

$$
\Omega_d=P\times(0,1)^{d-2}
\tag{6.6}
$$

has a nonconvex superlevel set whenever $\alpha>0$ and $c(\alpha)\ne0$. Consequently, the parameters at which this ground state is quasiconcave form a locally finite set, and there is no eventual quasiconcavity threshold for $\Omega_d$.

*Proof.* Fix such an $\alpha$. On a sufficiently small convex corner neighborhood $D=P\cap B_r(v_*)$, the function $f=\log u_\alpha$ is smooth in the interior and has bounded gradient, by Lemmas 2.3 and 2.4. It is not semiconcave there, by Theorem 1.1.

The positive first Robin eigenfunction on $(0,1)$ can be written

$$
g_\alpha(t)=\cos(k(t-1/2)),\qquad
k\tan(k/2)=\alpha,\quad 0<k<\pi.
\tag{6.7}
$$

The equation for $k$ has a unique solution because its left side is strictly increasing from zero to infinity. Direct differentiation verifies the Robin condition at both endpoints; positivity identifies the eigenfunction as the ground state. For $h=\log g_\alpha$ and $t_0=1/4$,

$$
h'(t_0)=k\tan(k/4)>0,
\qquad h''(t_0)=-k^2\sec^2(k/4).
\tag{6.8}
$$

Lemma 6.1 shows that $u_\alpha(x)g_\alpha(t)$ has a nonconvex superlevel set already in $D\times(0,1)$. This product is the ground state on $P\times(0,1)$, by the product argument in Section 5. For $d>3$, fix the remaining interval coordinates at interior points. The resulting slice is a positive constant multiple of the same product, so the same two endpoints and midpoint witness nonconvexity. The assertions about parameters follow from the locally finite zero set of $c$. ∎

In particular, the explicit parallelogram (1.5) gives a fixed prism in each dimension $d\ge3$ with nonconvex ground-state superlevel sets for arbitrarily large Robin parameters. The small-parameter conclusion for these product domains follows already from the planar result in [ACH] and restriction to a slice. The additional conclusion here is persistence outside a discrete set over the entire positive parameter axis. No novelty is asserted for the elementary level-set criterion or separation of variables.

This extension answers the eventual-quasiconcavity question for these fixed prisms negatively. The extension is restricted to prisms; Section 8 treats the general small-parameter polyhedral conjecture. The proof uses both bounded gradient and unbounded positive Hessian near a polygonal corner; failure of log-concavity alone would not imply the interval-lifting conclusion. No single smooth uniformly convex domain with arbitrarily large bad parameters is constructed here.

## 7. A weighted obstruction on higher-dimensional cones

The unresolved local condition in [ACH, Lemma 9.5 and Remark 9.6] concerns the restriction of a homogeneous harmonic Neumann mode to a transverse affine slice. The following result verifies that condition for a geometric class of cones. It imposes no symmetry on the mode.

**Theorem 7.1 (transverse nonconcavity).** Let $\Gamma\subset\mathbb R^d$, $d\ge3$, be an open full-dimensional convex polyhedral cone with outward unit face normals $\nu_i$. Suppose a unit vector $e$ and a number $\eta>0$ satisfy

$$
e\cdot x\ge\eta|x|\quad(x\in\overline\Gamma),
\qquad 0<k_i:=-\nu_i\cdot e<\frac1{\sqrt2}
\quad\text{for every face}.
\tag{7.1}
$$

Let $\psi$ be a nonzero homogeneous weak Neumann harmonic function of degree $\beta\in(1,2)$, with $\psi\in H^1(\Gamma\cap B_R)$ for every finite $R$. Then $\psi$ is not concave on the affine slice

$$
K=\{x\in\Gamma:e\cdot x=1\}.
\tag{7.2}
$$

*Proof.* We first justify the derivatives used below. A smooth radial cutoff $\chi$ preserves the zero Neumann condition on the cone faces. On a sufficiently large convex truncation $\Gamma\cap B_R$, the function $z=\chi\psi$ vanishes near the outer sphere and has

$$
\Delta z=2\nabla\chi\cdot\nabla\psi+(\Delta\chi)\psi\in L^2.
\tag{7.3}
$$

The standard homogeneous Neumann regularity theorem on bounded convex domains gives $z\in H^2$. The theorem and its convex approximation argument are recalled in [T, Section 4, following Theorem 4.2]. Thus $\psi$ is locally $H^2$ up to the cone boundary, including its vertex. In particular, $h=\partial_e\psi$ is locally $H^1$ and harmonic in the interior. Even reflection gives smoothness up to every relative face interior.

Suppose that the restriction to $K$ is concave. The first condition in (7.1) puts every nonzero cone point at positive height, so homogeneity gives concavity on every parallel slice. Put $H=D^2\psi$. Its restriction to $e^\perp$ is negative semidefinite, and harmonicity gives

$$
q:=H[e,e]=-\operatorname{tr}(H|_{e^\perp})\ge0.
\tag{7.4}
$$

At a relative face interior, differentiation of the Neumann condition in every face-tangent direction shows that

$$
H\nu=a\nu,\qquad a=H[\nu,\nu].
\tag{7.5}
$$

Write $\nu=-ke+su$, where $s=\sqrt{1-k^2}$ and $u\perp e$ is a unit vector. Taking the $e$ and $u$ components of (7.5), and eliminating $H[e,u]$, gives

$$
(1-k^2)H[u,u]=(1-2k^2)a+k^2q.
\tag{7.6}
$$

The left side is nonpositive, while $q\ge0$ and $1-2k^2>0$. Hence $a\le0$, and therefore

$$
\partial_\nu h=H[\nu,e]=-ka\ge0
\tag{7.7}
$$

on each relative face interior.

We now pass this face inequality across the polyhedral skeleton. On each bounded set, the union of strata of codimension at least two has zero $H^1$ capacity. Here is the needed explicit approximation. For an affine subspace of codimension two, take a cutoff equal to zero at distance at most $\varepsilon^2$, equal to one at distance at least $\varepsilon$, and affine in the logarithm of distance between them. On a bounded set, its squared-gradient integral is $O(1/|\log\varepsilon|)$, while its difference from one tends to zero in $L^2$. A finite product treats all the lower-dimensional strata, each of which lies in such a subspace. Smooth approximations can be chosen with values between zero and one.

If $\varphi$ is a nonnegative smooth compactly supported test function on $\overline\Gamma$ whose support avoids the skeleton, harmonicity and (7.7) give

$$
\int_\Gamma\nabla h\cdot\nabla\varphi\ge0.
\tag{7.8}
$$

Multiplying an arbitrary such $\varphi$ by the preceding cutoffs gives nonnegative tests converging to it in $H^1$. Since $h$ is locally $H^1$, (7.8) follows for the original test as well. In particular, no unaccounted edge flux is discarded.

Use (7.8) with

$$
\varphi_R(x)=e^{-e\cdot x}\chi_0(|x|/R),
\tag{7.9}
$$

where $\chi_0$ is a smooth nonnegative cutoff equal to one on $[0,1]$ and zero on $[2,\infty)$. Homogeneity and the local $H^2$ estimate give polynomial growth of the relevant annular Sobolev norms. The first condition in (7.1) gives exponential decay of the weight. The term containing $\nabla\chi_0(|x|/R)$ therefore tends to zero by Cauchy--Schwarz. The remaining term converges, so (7.8) yields

$$
0\le-\int_\Gamma e^{-e\cdot x}\partial_e h
=-\int_\Gamma e^{-e\cdot x}q\le0.
\tag{7.10}
$$

It follows that $q=0$ in the interior. The negative-semidefinite transverse Hessian block then has zero trace and must vanish. Writing $x=te+z$, $z\perp e$, connectedness of each transverse slice and homogeneity give constants $A\in\mathbb R$ and $b\in e^\perp$ such that

$$
\psi(te+z)=At^\beta+t^{\beta-1}b\cdot z.
\tag{7.11}
$$

Harmonicity becomes

$$
0=(\beta-1)t^{\beta-3}
\big(\beta At+(\beta-2)b\cdot z\big).
\tag{7.12}
$$

Since $1<\beta<2$ and $\Gamma$ has nonempty interior, $A=0$ and $b=0$. This contradicts the nonzero mode and proves the theorem. ∎

### 7.1. Consequence for the small-parameter Robin question

For a consistent-normal cone, let $\gamma$ satisfy $\gamma\cdot\nu_i=-1$ for every face and set $e=\gamma/|\gamma|$. The second condition in (7.1) becomes $|\gamma|>\sqrt2$; the first condition is a separate strict-dual requirement.

**Corollary 7.2.** Let $\Omega\subset\mathbb R^d$, $d\ge3$, be a bounded convex polyhedron. Suppose the first Neumann variation $v$ of its normalized Robin ground state has at a boundary point $x_0$ a nonzero leading nonlinear homogeneous Neumann mode $\psi$ of degree $\beta\in(1,2)$. Suppose also that the tangent cone has consistent normals and satisfies (7.1) with $e=\gamma/|\gamma|$. Then the Robin ground state on $\Omega$ has a nonconvex superlevel set for every sufficiently small positive Robin parameter.

*Proof.* The expansion and interior derivative estimates in [ACH, Section 9] give, on each fixed compact subset of the tangent cone,

$$
\begin{aligned}
\nabla v(x_0+\rho x)&=\gamma+\rho^{\beta-1}\nabla\psi(x)
+o(\rho^{\beta-1}),\\
D^2v(x_0+\rho x)&=\rho^{\beta-2}D^2\psi(x)
+o(\rho^{\beta-2}).
\end{aligned}
\tag{7.13}
$$

The lower-order quadratic particular solution is included in the remainders. By Theorem 7.1 there are an interior point $x$ and a vector $\xi\perp e$ with $D^2\psi(x)[\xi,\xi]>0$. Correct $\xi$ to $\xi+a_\rho e$ so that it is orthogonal to $\nabla v(x_0+\rho x)$. Since $\gamma\cdot e=|\gamma|>0$, the first line of (7.13) gives $a_\rho=O(\rho^{\beta-1})$. The second line gives strictly positive second derivative in this corrected direction for small $\rho$. Taylor's theorem at one fixed such interior point produces two endpoints whose $v$ values strictly exceed that of their midpoint.

The Neumann perturbation $u_\alpha=1+\alpha v+o(\alpha)$ from [ACH, Proposition 3.1] holds uniformly on these three fixed points. Thus the strict midpoint inequality persists for $u_\alpha$ for all sufficiently small $\alpha>0$. This is the transfer mechanism of [ACH, Lemma 9.5]. ∎

The leading nonzero mode in this corollary is a hypothesis. No assertion is made that a chosen vertex necessarily has a nonzero coefficient, or that every polyhedron has a vertex satisfying (7.1).

### 7.2. Nonempty scope and the remaining angle range

Theorem 7.1 is not vacuous in its degree interval. Fix $0<k<1/\sqrt2$ and put $s=\sqrt{1-k^2}$. In coordinates $(x,y,t)$, consider the cone with three outward normals

$$
\begin{aligned}
\nu_1&=(s,0,-k),\\
\nu_2&=(-s\cos\varepsilon,s\sin\varepsilon,-k),\\
\nu_3&=(-s\cos(2\varepsilon),-s\sin(2\varepsilon),-k),
\end{aligned}
\qquad 0<\varepsilon<\pi/6.
\tag{7.14}
$$

The transverse normals positively span $\mathbb R^2$, so the section $t=1$ is a bounded triangle and $t$ is strictly positive on every nonzero direction in the closed cone. Thus (7.1) holds with $e=(0,0,1)$ and a positive $\eta$ depending on $\varepsilon$.

As $\varepsilon\downarrow0$, the spherical sections converge almost everywhere to the spherical section of $\{|x|<(k/s)t\}\times\mathbb R_y$. On this limiting section, $y$ has mean zero and Neumann eigenvalue two. Indeed, latitude integration gives $\int y^2=|A_0|/3$, while $|\nabla_{S^2}y|^2=1-y^2$. The Rayleigh quotient on the finite sections, tested with $y$ minus its mean, therefore tends to two by bounded convergence. On every finite pointed cone, [ACH, Theorem 9.1] gives $\lambda_1>2$, since equality requires a linear factor. Hence, for sufficiently small positive $\varepsilon$,

$$
2<\lambda_1<6,\qquad
1<\beta_1<2,\qquad \beta_1(\beta_1+1)=\lambda_1.
\tag{7.15}
$$

No explicit cutoff in $\varepsilon$ or eigenfunction parity is needed.

The angle condition cannot simply be deleted from the face-sign step. For example, with $e=(1,0,0)$,

$$
\nu=(-\sqrt3/2,1/2,0),\qquad
H=\begin{pmatrix}1&-\sqrt3&0\\-\sqrt3&-1&0\\0&0&0\end{pmatrix},
\tag{7.16}
$$

we have $\operatorname{tr}H=0$, $H|_{e^\perp}\preceq0$, and $H\nu=2\nu$. The normal second derivative is positive and the desired face-flux sign reverses. This matrix is an obstruction to that algebraic proof step, not a counterexample to the cone conjecture. The borderline angle, the larger-angle range, and cones without the strict-dual property require further arguments. Section 8 resolves the general polyhedral conjecture by a different, global argument.

## 8. Quasiconcavity forces quadraticity on every convex polyhedron

We now remove the geometric restrictions from the small-parameter result. A *product of circumsolids* has the meaning in [ACH]: after a rigid motion, the domain is an orthogonal Cartesian product of convex polyhedra, each of which contains a ball tangent to all its facets. Intervals are allowed as factors.

**Theorem 8.1.** Let $\Omega\subset\mathbb R^d$, $d\ge3$, be a bounded convex polyhedron with nonempty interior. If $\Omega$ is not a product of circumsolids, then there exists $\alpha_0>0$ such that its first Robin eigenfunction has a nonconvex superlevel set for every $0<\alpha<\alpha_0$.

This is [ACH, Section 10, Conjecture 2]. Its proof uses global rigidity rather than an unrestricted version of the transverse cone theorem in Section 7. The analytic statement behind it is the following.

**Theorem 8.2.** Put $\mu=|\partial\Omega|/|\Omega|$, and let $v\in H^1(\Omega)$ solve

$$
\Delta v=-\mu\quad\text{in }\Omega,
\qquad \partial_\nu v=-1\quad\text{on }\partial\Omega.
\tag{8.1}
$$

If $v$ is quasiconcave, then $v$ is a quadratic polynomial.

Here quasiconcavity means that every superlevel set in the open domain is convex. The additive constant in $v$ is immaterial. We first establish three regularity and energy facts, keeping their hypotheses separate.

### 8.1. Continuous gradients from compatible face data

At $z\in\partial\Omega$, call the incident normals *consistent* if there is a vector $\gamma_z$ with $\gamma_z\cdot\nu_i=-1$ on every incident facet. We use two standard analytic inputs. On a bounded convex domain, a weak homogeneous-Neumann solution with Laplacian in $L^2$ belongs to $H^2$ and satisfies

$$
\|D^2 f\|_{L^2}\le\|\Delta f\|_{L^2}.
\tag{8.2}
$$

The scalar approximation argument is recalled in [T, Section 4]. Maz'ya's gradient estimate [M] also gives $\|\nabla f\|_\infty\le C\|\Delta f\|_{L^q}$ for each fixed bounded convex domain and $q>d$; the additive mean of $f$ does not affect this estimate. Both facts apply on convex cones truncated by balls. Radial cutoffs have zero normal derivative on the planar cone faces and can be chosen to vanish near the spherical boundary.

**Lemma 8.3.** If all boundary points have consistent normals, the solution of (8.1) belongs to $H^2(\Omega)$ and its gradient extends continuously to $\overline\Omega$.

*Proof.* Fix $z$ and a conic neighborhood of radius $R_z$. In coordinates centered at $z$, the function

$$
h(x)=v(z+x)+\frac{\mu}{2d}|x|^2-\gamma_z\cdot x
\tag{8.3}
$$

is harmonic with homogeneous Neumann data. Applying (8.2) to a radial cutoff of $h$ proves local $H^2$ regularity. The cutoff forcing is in $L^2$ because $h\in H^1$. Finitely many such neighborhoods, together with interior neighborhoods, prove the global assertion.

We spell out why the homogeneous expansion also controls the gradient uniformly up to the cone faces. For a fixed cone $\Gamma$, set $A=\Gamma\cap\mathbb S^{d-1}$ and take an orthonormal Neumann eigenbasis $\Phi_j$ on $A$. Write

$$
\lambda_j=\beta_j(\beta_j+d-2),\qquad
\psi_j(r\theta)=r^{\beta_j}\Phi_j(\theta).
\tag{8.4}
$$

The cone expansion of a weak harmonic Neumann function contains only these nonnegative-degree terms; see [ACH, arXiv v2, Proposition 4.4]. By [ACH, Theorem 9.1], every positive degree is at least one, and every degree-one mode is linear. Discreteness gives a positive gap between one and the next degree.

For clarity, the spectral bounds used below need only have some polynomial exponent. The Sobolev inequality on the fixed Lipschitz spherical domain, tested in the eigenfunction equation with $|\Phi|^{p-2}\Phi$, gives

$$
\|\Phi\|_{p\kappa}
 \le [C p^2(1+\lambda)]^{1/p}\|\Phi\|_p
\quad(p\ge2)
\tag{8.5}
$$

for some fixed $\kappa>1$. Iterating $p=2\kappa^m$ proves an $L^\infty$ bound polynomial in $1+\lambda$. There is also a polynomial counting bound for the eigenvalues. One way to see this without a sharp Weyl law is to use an $H^1$ extension in finitely many spherical coordinate charts. The resulting map into a finite sum of cube spaces is injective, has an $L^2$ lower bound, and is bounded in $H^1$. Its restriction to the spectral subspace with eigenvalues at most $\Lambda$ has Rayleigh quotient at most $C(1+\Lambda)$. The min-max principle and the explicit Neumann spectra of cubes bound the dimension of that subspace by a polynomial in $1+\Lambda$.

Apply [M] to a radial cutoff of $\psi_j$ on $\Gamma\cap B_2$, equal to one on $B_1$ and zero near the outer sphere. Since $\partial_r\psi_j=\beta_jr^{\beta_j-1}\Phi_j$, its Laplacian involves no angular derivative of $\Phi_j$. For a sufficiently large fixed exponent $N$, the preceding bounds imply

$$
\|\Phi_j\|_\infty\le C(1+\beta_j)^N,
\qquad
\|\nabla\psi_j\|_{L^\infty(\Gamma\cap B_1)}
 \le C(1+\beta_j)^N2^{\beta_j}.
\tag{8.6}
$$

Choose an almost-everywhere reference radius at which the spherical trace of $h$ is in $L^2$, and rescale it to one. The expansion coefficients then satisfy $\sum_j|a_j|^2<\infty$. Remove the constant and linear terms and put $\delta=\min_{\beta_j>1}(\beta_j-1)>0$. Homogeneity, (8.6), and Cauchy--Schwarz give, for $0<r\le1/8$,

$$
\sup_{\Gamma\cap B_r}
 \left|\nabla\sum_{\beta_j>1}a_j\psi_j\right|
 \le C r^\delta
 \left(\sum_j|a_j|^2\right)^{1/2}.
\tag{8.7}
$$

Indeed, after factoring $r^\delta$ from each term, the remaining squared series is bounded by a polynomially weighted geometric series in $\beta_j$, with ratio controlled by $2r\le1/4$. The counting bound makes it summable uniformly in $r$. The same estimate proves convergence of the derivative series in $L^\infty$; its sum agrees with the weak derivative and with the classical interior derivative.

Thus the interior gradient has a limit at every $z$, equal to the linear coefficient in (8.3) plus $\gamma_z$. Interior regularity and this limit define a continuous gradient on the closure. Continuity along the boundary follows as well: approximate a boundary point approaching $z$ by an interior point where the gradient is arbitrarily close to that boundary limit. Compactness now gives a modulus

$$
\omega(t)=\sup_{\substack{x,y\in\overline\Omega\\|x-y|\le t}}
 |\nabla v(x)-\nabla v(y)|\longrightarrow0
 \quad(t\downarrow0).
\tag{8.8}
$$

Finally, continuity from a relative facet interior shows that $\nabla v(z)\cdot\nu_i=-1$ on every incident facet. No uniform corner exponent is needed. ∎

### 8.2. Quasiconcavity removes the open-edge singularities

Let $S$ be the union of the closed faces of codimension at least three. It has dimension at most $d-3$.

**Lemma 8.4.** If $v$ is quasiconcave, all its boundary normals are consistent, and $D^2v$ is locally bounded on $\overline\Omega\setminus S$.

*Proof.* The inconsistent-normal argument in [ACH, Section 9, inconsistent-normal case] produces a nonconvex superlevel set of $v$ whenever a boundary point has inconsistent normals. Hence Lemma 8.3 applies.

At a relative interior point of a codimension-two face, the tangent cone is $W\times\mathbb R^{d-2}$, where $W$ is a planar wedge of angle $\vartheta\in(0,\pi)$. We first classify its homogeneous harmonic Neumann modes of degree $\beta\in(1,2]$. For a direction $t$ in the linear factor, $\partial_t\psi$ is a weak harmonic Neumann function, by tangential difference quotients. It is locally $H^1$ by (8.2), and is homogeneous of degree $\beta-1$.

If $1<\beta<2$, the spectral lower bound [ACH, Theorem 9.1] forces this derivative to vanish. The mode is therefore planar. The only possible degree in this range is $\beta=\pi/\vartheta$, with $\vartheta>\pi/2$, and in bisector coordinates it is a nonzero multiple of

$$
\psi(r\cos\theta,r\sin\theta,t)
   =r^\beta\sin(\beta\theta),
\qquad -\vartheta/2<\theta<\vartheta/2.
\tag{8.9}
$$

On a line perpendicular to the inward bisector this is odd and nonaffine, so neither sign is concave. To check nonaffinity, affinity would, by oddness and homogeneity, give $c x^{\beta-1}y$ in bisector coordinates. For $c\ne0$ this is harmonic only when $\beta=1$ or $2$.

The normal-plane projection of $\gamma=\nabla v(z)$ is the inward bisector of length $1/\sin(\vartheta/2)$. Its possible component along the edge does not affect a normal-plane direction $\xi$ perpendicular to that bisector. Thus (8.9), with either sign, gives an interior cone point $x$ and such a $\xi$ with $D^2\psi(x)[\xi,\xi]>0$. We may choose $x$ with zero edge component and then scale it so that $\gamma\cdot x>0$ is fixed.

If a nonzero mode (8.9) occurred in the expansion of $v$ at $z$, it would be the leading nonlinear mode below degree two. At $z+rx$, the expansion gives $\nabla v=\gamma+o(1)$ and

$$
D^2v=r^{\beta-2}\bigl(D^2\psi(x)+o(1)\bigr),
\tag{8.10}
$$

with its nonzero coefficient absorbed into $\psi$. Replace $\xi$ by $\xi+c(r)x$, choosing $c(r)=o(1)$ so that it is exactly perpendicular to $\nabla v(z+rx)$. Its Hessian value is positive for small $r$. The two nearby points in opposite directions then have values strictly larger than the midpoint, contradicting quasiconcavity. This is the tangent correction of [ACH, Lemma 9.5]. Consequently every degree in $(1,2)$ is absent at every open edge point.

We give the local bounded-Hessian argument explicitly. Degree-two modes on $W\times\mathbb R^{d-2}$ are quadratic. Indeed, their derivatives in the linear-factor directions have degree one and hence are linear Neumann functions, whose gradients lie in that linear factor. Integrating gives

$$
\psi(y,t)=\tfrac12 t^T B t+\phi(y),\qquad
\Delta_y\phi=-\operatorname{tr}B.
\tag{8.11}
$$

Here $B$ is symmetric and $\phi$ is homogeneous of degree two with Neumann ray data. After adding $(\operatorname{tr}B)|y|^2/4$, it is a planar harmonic mode of degree two. Such a mode is either zero or, when $\vartheta=\pi/2$, a harmonic quadratic. Thus (8.11) is quadratic in all cases.

On a compact portion of an open edge, choose one fixed conic radius. The spherical $L^2$ norms of the local harmonic functions (8.3) are uniformly bounded, since $v$ and its gradient are continuous on the closure. The spectral $L^\infty$ bound in (8.6), the counting bound, absence of degrees in $(1,2)$, and the quadraticity just proved show that at every edge center $z$ there is a quadratic polynomial $Q_z$, with uniformly bounded coefficients, such that

$$
|v(z+x)-Q_z(x)|\le C|x|^{2+\delta_2}
\tag{8.12}
$$

for a fixed $\delta_2>0$. Here the polynomial includes the particular solution in (8.3); the remainder is harmonic with homogeneous Neumann data on the two faces. The estimate follows by summing the degrees strictly greater than two, exactly as for (8.7), now without differentiating. The first such degree has a positive gap above two.

For an interior point at distance $r$ from the edge, project to an edge center $z$. A ball of radius $c(\vartheta)r$ about the point meets at most one of the two faces. If it meets a face, even reflection of the harmonic remainder across that face gives the interior harmonic estimate. Using (8.12) on the original and reflected points yields

$$
|D^2v-D^2Q_z|\le Cr^{\delta_2}.
\tag{8.13}
$$

This proves local boundedness at the open edges. Relative facet interiors are smooth by even reflection after subtracting the normal affine term. These neighborhoods cover $\overline\Omega\setminus S$. In particular, no higher-dimensional regularity criterion for unspecified degree-two modes is being assumed. ∎

### 8.3. Energy near the higher-codimension faces

**Lemma 8.5.** Under the hypotheses of Lemma 8.3, with $H=D^2v$, there are constants $C$ and $\varepsilon_0>0$ such that

$$
\int_{\{\operatorname{dist}(x,S)<\varepsilon\}}|H|^2\,dx
 \le C\bigl(\varepsilon^3+
       \varepsilon\,\omega(C\varepsilon)^2\bigr)
\quad(0<\varepsilon<\varepsilon_0).
\tag{8.14}
$$

All integrals in this subsection are over $\Omega$. In particular the left side is $o(\varepsilon)$.

*Proof.* A finite union of bounded faces of dimension at most $d-3$ has an $\varepsilon$-net of at most $C\varepsilon^{-(d-3)}$ points, and its $\varepsilon$-tube has volume at most $C\varepsilon^3$. We need a uniform conic patch near each net point; a fixed cone radius at all points of $S$ would not be valid.

Write the polytope by unit facet inequalities $\nu_j\cdot x\le b_j$, $1\le j\le m$, and put $s_j(x)=b_j-\nu_j\cdot x$. For every feasible nonempty subset $J$, let $F_J$ be the nonempty face where all its inequalities are equalities. There is a constant $C_0$, independent of $J$, such that

$$
\operatorname{dist}(z,F_J)
 \le C_0\max_{j\in J}s_j(z),
\qquad z\in\overline\Omega.
\tag{8.15}
$$

To prove it, write $z$ as a convex combination of the finitely many vertices. Each vertex outside $F_J$ has a positive total $J$-slack. The minimum of these positive totals, over the finitely many choices, is positive. Thus the total weight of vertices outside $F_J$ is bounded by a constant times $\max_{j\in J}s_j(z)$. Move that weight to any vertex of $F_J$ and use the diameter bound. For infeasible $J$, compactness instead gives $\min_z\max_{j\in J}s_j(z)>0$.

Fix $z\in S$ and a small $\varepsilon$. Set $A_0=4$ and $A_{\ell+1}=10(C_0+1)A_\ell$. Among $m+2$ consecutive sets

$$
J_\ell=\{j:s_j(z)\le A_\ell\varepsilon\}
\tag{8.16}
$$

two adjacent sets coincide. Call the common set $J$. For uniformly small $\varepsilon$, it is feasible by the infeasible-set lower bounds. Choose $w\in F_J$ with $|w-z|\le C_0A_\ell\varepsilon$. The set $J$ includes the facets incident to $z$, so $w\in S$. Put $R=2(C_0+1)A_\ell\varepsilon$. Then $B_{2\varepsilon}(z)\subset B_R(w)$. For $j\notin J$, its supporting plane is farther than

$$
[10(C_0+1)-C_0]A_\ell\varepsilon>2R
\tag{8.17}
$$

from $w$. Hence inside $B_{2R}(w)$ the domain is exactly its tangent cone at $w$. There are only finitely many threshold levels, so $R$ is comparable to $\varepsilon$ with constants depending only on the fixed polytope.

Subtract the affine tangent at $w$, writing $g(x)=v(x)-v(w)-\nabla v(w)\cdot(x-w)$. It has homogeneous Neumann data on the incident facets, by Lemma 8.3. On this conic patch, convexity and (8.8) imply

$$
|\nabla g|\le\omega(C\varepsilon),\qquad
|g|\le CR\omega(C\varepsilon).
\tag{8.18}
$$

Take a radial cutoff $\rho$ equal to one on $B_R(w)$ and supported strictly inside $B_{2R}(w)$, with derivatives bounded by $C/R$ and $C/R^2$. Apply (8.2) to $\rho g$ on the cone truncated at radius $2R$. Since

$$
\Delta(\rho g)=-\mu\rho+2\nabla\rho\cdot\nabla g+g\Delta\rho,
\tag{8.19}
$$

we obtain

$$
\int_{\Omega\cap B_R(w)}|H|^2
 \le C\bigl(R^d+R^{d-2}\omega(C\varepsilon)^2\bigr).
\tag{8.20}
$$

The balls $B_{2\varepsilon}(z)$ for the net points cover the $\varepsilon$-tube of $S$. Sum (8.20) over at most $C\varepsilon^{-(d-3)}$ balls to get (8.14). Overlaps only enlarge this upper bound. ∎

### 8.4. A Hessian-norm identity and the proof of rigidity

*Proof of Theorem 8.2.* Assume $v$ is quasiconcave. Lemmas 8.3--8.5 apply. In the interior, every component of $H=D^2v$ is harmonic, since $\Delta v=-\mu$ is constant. At a relative facet interior, subtract an affine function with normal derivative $-1$ and reflect the result evenly. The Hessian transforms by orthogonal conjugation. Consequently, on that facet,

$$
H:\partial_\nu H=0,
\qquad \partial_\nu |H|=0.
\tag{8.21}
$$

In coordinates with the normal as the last axis, the mixed normal-tangential entries of $H$ vanish, while the normal derivatives of the other entries vanish. This also verifies (8.21) directly.

Since $\operatorname{tr}H=-\mu\ne0$, the Frobenius norm $q=|H|$ satisfies $q\ge\mu/\sqrt d>0$. Its interior Laplacian is

$$
D:=\Delta q=
\sum_{k=1}^d\left(
 \frac{|\partial_kH|^2}{q}
 -\frac{(H:\partial_kH)^2}{q^3}\right)\ge0.
\tag{8.22}
$$

For any Lipschitz cutoff $\chi$ vanishing on a neighborhood of $S$, integration by parts gives

$$
\int_\Omega\chi^2|\nabla H|^2
 \le4\int_\Omega|\nabla\chi|^2|H|^2,
\tag{8.23}
$$

and

$$
\int_\Omega\chi^2D
 =-2\int_\Omega\chi\nabla\chi\cdot\nabla q.
\tag{8.24}
$$

Here is the justification at the open edges. On each compact set away from $S$, Lemma 8.4 bounds $H$. Around a codimension-two affine face, a cutoff increasing logarithmically from zero at distance $\delta^2$ to one at distance $\delta$ has squared gradient integral $O(1/|\log\delta|)$. Products of finitely many such cutoffs remove the edges. First integrate the harmonic equations for $H$ against $\chi^2H$ times the square of this auxiliary cutoff. The facet boundary terms vanish by (8.21). Cauchy--Schwarz gives (8.23) with the auxiliary cutoff; boundedness of $H$ makes its cutoff-energy error tend to zero. Fatou first gives local $L^2$ control of $\nabla H$ up to those edges. One can then pass in the identity itself: all terms containing the auxiliary cutoff gradient tend to zero by Cauchy--Schwarz and its vanishing $L^2$ norm. Applying the same argument to $\Delta q=D$, with $|\nabla q|\le|\nabla H|$, proves (8.24). The integrand $D$ is locally integrable there since $q$ is bounded below and $D\le |\nabla H|^2/q$. Thus no edge measure or uncomputed boundary term is discarded.

Choose $\chi_\varepsilon$ to be zero when $\operatorname{dist}(x,S)\le\varepsilon$ and one when that distance is at least $2\varepsilon$, with $|\nabla\chi_\varepsilon|\le C/\varepsilon$. Define

$$
A_\varepsilon=\int_\Omega|\nabla\chi_\varepsilon|^2|H|^2,
\qquad B_\varepsilon=\int_\Omega|\nabla\chi_\varepsilon|^2.
\tag{8.25}
$$

The tube-volume bound and Lemma 8.5 imply

$$
A_\varepsilon\le C\left(\varepsilon+
  \frac{\omega(C\varepsilon)^2}{\varepsilon}\right),
\qquad B_\varepsilon\le C\varepsilon.
\tag{8.26}
$$

Although $A_\varepsilon$ need not tend to zero, its product with $B_\varepsilon$ does. Combining (8.23)--(8.26) yields

$$
0\le\int_\Omega\chi_\varepsilon^2D
 \le4\sqrt{A_\varepsilon B_\varepsilon}
 \le C\bigl(\varepsilon+\omega(C\varepsilon)\bigr)
 \longrightarrow0.
\tag{8.27}
$$

Fatou's lemma gives $D=0$ in the interior. Each summand in (8.22) is nonnegative, so equality in Cauchy--Schwarz gives $\partial_kH=a_kH$ pointwise for some scalar $a_k$. Taking traces gives $0=-\mu a_k$, hence $a_k=0$. Thus $H$ is constant, and $v$ is quadratic on the connected domain. This argument neither assumes global $H^3$ regularity nor infers bounded Hessians from continuity of the gradient. ∎

*Proof of Theorem 8.1.* The quadratic classification [ACH, Corollaries 8.2--8.3] says that a quadratic solution of (8.1) can exist only on a product of circumsolids. Thus Theorem 8.2 implies that $v$ is not quasiconcave when $\Omega$ is not such a product. There are interior points $x,y$, their midpoint $m$, and $a,\tau\in\mathbb R$ with $\tau>0$ such that

$$
v(x),v(y)>a+\tau,
\qquad v(m)<a-\tau.
\tag{8.28}
$$

Indeed, continuity makes midpoint quasiconcavity equivalent to quasiconcavity, by dyadic subdivision. The normalized first eigenfunction has the perturbation expansion [ACH, Proposition 3.1]

$$
u_\alpha=1+\alpha v+o(\alpha)
\quad\text{uniformly on }\overline\Omega.
\tag{8.29}
$$

For all sufficiently small positive $\alpha$, (8.28)--(8.29) put $x,y$ in $\{u_\alpha>1+\alpha a\}$ and exclude $m$. This proves the asserted nonconvexity for the entire interval $(0,\alpha_0)$. ∎

The recent work of Edelen and Li [EL] proves sharp Neumann spectral and regularity results under non-obtuse dihedral-angle hypotheses. Their Lemma 2.5 uses logarithmic cutoffs to justify a tensor energy identity when the tensor is bounded. The open-edge cutoff step above is of the same standard type. The additional estimate (8.14) and the use of the norm rather than its square allow the higher-codimension part to remain potentially unbounded, while quasiconcavity supplies the needed edge regularity even at obtuse edges. We do not use the spectral-gap theorem of [EL].

The unrestricted transverse-cone assertion suggested by [ACH, Remark 9.6] remains a separate local question. Theorem 8.1 resolves their polyhedral quasiconcavity conjecture through the global Neumann problem. It gives no assertion about large parameters on every polyhedron. The independent construction in the next section addresses the fundamental gap.


## 9. The positive-Robin fundamental gap can tend to zero

This section is independent of the corner regularity and quasiconcavity arguments above. For a bounded connected Lipschitz domain $G$, let

$$
E_0(G;\alpha)<E_1(G;\alpha)\le E_2(G;\alpha)\le\cdots,
\qquad \gamma(G;\alpha)=E_1(G;\alpha)-E_0(G;\alpha)
\tag{9.1}
$$

be the eigenvalues and fundamental gap of the quadratic form

$$
q_{G,\alpha}[u]=\int_G|\nabla u|^2+\alpha\int_{\partial G}|u|^2,
\qquad u\in H^1(G).
\tag{9.2}
$$

Thus our sign convention is $\partial_\nu u+\alpha u=0$. The first eigenfunction is simple and can be chosen positive in $G$. These standard facts also follow from compactness of the form embedding, replacement of a minimizer by its absolute value, and the interior strong maximum principle. All functions in the proof may be taken real.

The Robin fundamental-gap conjecture in [ACH, final Section 10, p.307] predicts that a convex domain of diameter $D$, with any convex potential, has gap at least that of the zero-potential interval of length $D$ at the same positive Robin parameter. The zero-potential version is [L, Conjecture F] and [K, Conjecture 1]; it also appears in [OP, Open Problem 7]. The interval case with convex potential is proved in [ACHI], and the rectangular-box case in [L, Theorem 3.8]. Kielty [K] proves gap degeneration for negative parameters on thin double cones. The following result concerns positive parameters and zero potential.

**Theorem 9.1 (failure of every positive diameter-only gap bound).** For every integer $d\ge4$, $D>0$ and $\alpha>0$,

$$
\inf\{\gamma(G;\alpha):G\subset\mathbb R^d
\text{ is a bounded open convex polyhedron of diameter }D\}=0.
\tag{9.3}
$$

In particular, the universal positive-Robin fundamental-gap conjecture is false. No convex potential is needed for a counterexample.

We prove the theorem with explicit estimates. The geometry is a convex thin domain whose three-dimensional cross-sections have a larger surface-area-to-volume ratio in the middle than at the ends. Its ground-state mass therefore concentrates near the two ends. An odd multiple of the ground state then gives a second Rayleigh quotient arbitrarily close to the first.

### 9.1. Cross-sections with an increasing surface-area-to-volume ratio

For $0\le s\le1$, set

$$
K_s=\{(X,Y,Z)\in\mathbb R^3:
 |X|+5|Y|<1,\quad |X|+|Z|<1+s\}.
\tag{9.4}
$$

These are convex polyhedra, with $K_s=K_0+[-s,s]e_Z$. Write $V(s)=|K_s|$ and $S(s)=|\partial K_s|$. The two families of facets, denoted by $Y$ and $Z$ according to their defining inequalities, have areas

$$
\begin{aligned}
V(s)&=\frac45\left(\frac23+s\right),\\
S_Y(s)&=\frac45\sqrt{26}(1+2s),\qquad
S_Z(s)=\frac45\sqrt2,\\
r(s):=\frac{S(s)}{V(s)}
&=\frac{\sqrt{26}(1+2s)+\sqrt2}{2/3+s}.
\end{aligned}
\tag{9.5}
$$

For completeness, at fixed $|X|=a<1$ the section is a rectangle with side lengths $2(1-a)/5$ and $2(1+s-a)$. Integrating its area gives
$V(s)=(8/5)\int_0^1(1-a)(1+s-a)\,da$. On each $Y$ facet the graph factor is $\sqrt{26}/5$; summing the two signs of $Y$ and the two signs of $X$ gives
$S_Y(s)=(8\sqrt{26}/5)\int_0^1(1+s-a)\,da$.
On the $Z$ facets the graph factor is $\sqrt2$, which gives
$S_Z(s)=(8\sqrt2/5)\int_0^1(1-a)\,da$. Edges have zero surface measure, also at $s=0$.

In particular,

$$
0<r'(s)=\frac{\sqrt{26}/3-\sqrt2}{(2/3+s)^2}<1,
\qquad r_0:=r(0)=\frac32(\sqrt{26}+\sqrt2).
\tag{9.6}
$$

Positivity follows from $26>18$. For the upper bound it suffices to evaluate the derivative at zero and use $\sqrt{26}<26/5$ and $\sqrt2>7/5$. The central barrier satisfies

$$
\delta:=r(1/2)-r_0
=\frac3{14}(\sqrt{26}-3\sqrt2)>\frac17.
\tag{9.7}
$$

Indeed, $\sqrt{26}>5$ and $\sqrt2<10/7$ give $\delta>15/98>1/7$.

The failure of monotonicity of volume divided by surface area under Minkowski addition in dimensions at least three is a known convex-geometric phenomenon; see [FGM] and the introduction of [FMMZ]. We do not claim that phenomenon as new. Formula (9.5) supplies the particular elementary family needed here, and its spectral consequence is proved below without an asymptotic spectral-convergence theorem.

### 9.2. A uniform transverse Robin estimate

**Lemma 9.2.** For $0\le s\le1$ and $0\le\beta\le1/4096$,

$$
E_0(K_s;\beta)\ge\beta r(s)-110000\beta^2.
\tag{9.8}
$$

*Proof.* We first give a coarse Poincaré estimate directly. If $K\subset\mathbb R^3$ is convex with diameter $L$ and $w$ has mean zero, then

$$
\begin{aligned}
\|w\|_{L^2(K)}^2
&=\frac1{2|K|}\int_K\int_K|w(x)-w(y)|^2\,dx\,dy\\
&\le\frac{L^2}{2|K|}\int_0^1\int_K\int_K
 |\nabla w((1-t)x+ty)|^2\,dx\,dy\,dt\\
&\le\frac32L^2\|\nabla w\|_{L^2(K)}^2.
\end{aligned}
\tag{9.9}
$$

To justify the last line, symmetry in $x,y$ replaces the $t$ integral by twice its integral over $[0,1/2]$. For fixed $y$, the substitution $z=(1-t)x+ty$ has Jacobian $(1-t)^3$, and convexity places its image inside $K$. Therefore that integral is at most
$2|K|\|\nabla w\|_2^2\int_0^{1/2}(1-t)^{-3}\,dt
=3|K|\|\nabla w\|_2^2$.
The preceding line follows from the fundamental theorem of calculus and Cauchy--Schwarz on each segment. Prove it first for smooth functions and then use density in $H^1(K)$.

Every $K_s$ contains $B_{1/6}(0)$ and is contained in $B_3(0)$; its volume is at least $1/2$ and its surface area is at most $16$. These assertions follow immediately from (9.4)--(9.5): the facet distances from zero are $1/\sqrt{26}$ and $(1+s)/\sqrt2$, while $|X|\le1$, $|Y|\le1/5$, $|Z|\le2$. Its diameter is at most six, so (9.9) gives, with $g=\|\nabla w\|_2$,

$$
\|w\|_2\le8g.
\tag{9.10}
$$

On almost every boundary point, $x\cdot\nu\ge1/6$. Applying the divergence theorem to $xw^2$ and using $|x|\le3$ yields

$$
\begin{aligned}
\int_{\partial K_s}w^2
&\le6\left(3\|w\|_2^2+6\|w\|_2g\right)
\le1440g^2\le1600g^2,\\
\left|\int_{\partial K_s}w\right|&\le160g.
\end{aligned}
\tag{9.11}
$$

Again smooth approximation and trace continuity justify this calculation for $H^1$ functions. Given $f\in H^1(K_s)$, write $f=m+w$, where $m$ is its mean and $w$ has mean zero. Dropping the nonnegative boundary integral of $\beta w^2$ and completing a square gives

$$
\begin{aligned}
q_{K_s,\beta}[f]
&\ge g^2+\beta S(s)m^2-320\beta|m|g\\
&\ge\tfrac12g^2+\beta S(s)m^2-51200\beta^2m^2.
\end{aligned}
\tag{9.12}
$$

Since $r(s)\le32$, (9.10) and $\beta\le1/4096$ imply
$\tfrac12g^2\ge\beta r(s)\|w\|_2^2$.
Also $\|f\|_2^2=V(s)m^2+\|w\|_2^2$ and $m^2\le2\|f\|_2^2$. Consequently
$q_{K_s,\beta}[f]\ge(\beta r(s)-102400\beta^2)\|f\|_2^2$, which proves (9.8). ∎

### 9.3. A convex domain with two end regions of low energy

For $0<\varepsilon\le1$, define the open polyhedron in $\mathbb R^4$

$$
\Omega_\varepsilon=\{(t,x,y,z):
 |t|<1,\quad |x|+5|y|<\varepsilon,\quad
 |x|+|z|+\varepsilon|t|<2\varepsilon\}.
\tag{9.13}
$$

It is bounded, convex, full dimensional, and invariant under $t\mapsto-t$. Its slice at $t$ is $\varepsilon K_{1-|t|}$. If $D_\varepsilon$ is its diameter, then

$$
2\le D_\varepsilon\le\sqrt{4+36\varepsilon^2},
\qquad D_\varepsilon\longrightarrow2.
\tag{9.14}
$$

The lower bound follows by approaching $(\pm1,0,0,0)$, and the upper bound uses $K_s\subset B_3$.

Write $s(t)=1-|t|$ and fix $\alpha>0$. Suppose $\alpha\varepsilon\le1/4096$. Scaling Lemma 9.2 gives

$$
E_0(\varepsilon K_s;\alpha)
\ge\frac{\alpha r(s)}{\varepsilon}-110000\alpha^2.
\tag{9.15}
$$

The lateral boundary element of $\Omega_\varepsilon$ dominates $dt$ times the transverse boundary element. On the $Y$ facets the factor is exactly one; on the $Z$ facets it is $\sqrt{1+\varepsilon^2/2}$. For example, on a $Z$ facet the graph of $z$ has derivative of absolute value one in $x$ and $\varepsilon$ in $t$, giving graph factor $\sqrt{2+\varepsilon^2}$ instead of the transverse $\sqrt2$. These formulas hold off the finitely many facet intersections, a set of surface measure zero. Dropping the nonnegative end-cap terms and applying (9.15) slice by slice therefore yields

$$
q_{\Omega_\varepsilon,\alpha}[u]\ge
\int_{\Omega_\varepsilon}\left\{
 |\partial_tu|^2+
 \left(\frac{\alpha r(s(t))}{\varepsilon}-110000\alpha^2\right)|u|^2
\right\}.
\tag{9.16}
$$

Here $\partial_t$ is the ambient derivative at fixed $(x,y,z)$. For smooth $u$ this is Fubini's theorem and the explicit facet calculation. Density in $H^1(\Omega_\varepsilon)$ and continuity of the trace extend it to the form domain. No boundary is inserted at the middle slice.

An upper bound on the first eigenvalue follows from the trial function

$$
\chi(t)=\left(1-\frac{1-t}{\ell}\right)_+,
\qquad \ell=\varepsilon^{1/3}.
\tag{9.17}
$$

It is supported on $1-\ell<t<1$, where $s(t)=1-t\le\ell$. Its squared norm is at least $\varepsilon^3V(0)\ell/3$. Since $V(1)/V(0)=5/2$, the gradient term divided by the squared norm is at most $(15/2)\ell^{-2}$. The part of the lateral boundary energy with factor one contributes at most
$\alpha(r_0+\ell)/\varepsilon$ by (9.6). The extra sloping-facet contribution is at most $\alpha\varepsilon$, because

$$
\sqrt{1+\varepsilon^2/2}-1\le\varepsilon^2/4,
\qquad \frac{S_Z}{4V(0)}<1.
\tag{9.18}
$$

The cap at $t=1$ contributes at most $3\alpha/\ell$; the other cap contributes zero. We obtain

$$
E_0(\Omega_\varepsilon;\alpha)
\le\frac{\alpha r_0}{\varepsilon}
 +A_\alpha\varepsilon^{-2/3},
\qquad A_\alpha=\frac{15}{2}+5\alpha.
\tag{9.19}
$$

All three lower-order terms were bounded using $\varepsilon\le1$.

Let $u_0$ be the positive ground state normalized by $\int_{\Omega_\varepsilon}u_0^2=1$. Combining (9.16) and (9.19), and then using (9.7), bounds its mass in the middle:

$$
\begin{aligned}
M_\varepsilon&:=\int_{\Omega_\varepsilon\cap\{|t|\le1/2\}}u_0^2\\
&\le\frac{A_\alpha\varepsilon^{1/3}+110000\alpha^2\varepsilon}
 {\alpha\delta}
\le C_\alpha\varepsilon^{1/3},\qquad
C_\alpha:=\frac{A_\alpha+110000\alpha^2}{\alpha\delta}.
\end{aligned}
\tag{9.20}
$$

### 9.4. The gap estimate, diameter normalization, and an explicit example

By simplicity and reflection symmetry, $u_0$ is even in $t$. Let

$$
f(t)=\begin{cases}
-1,&t\le-1/2,\\
2t,&|t|<1/2,\\
1,&t\ge1/2.
\end{cases}
\tag{9.21}
$$

Then $f$ is odd and Lipschitz, $u_0f\in H^1(\Omega_\varepsilon)$, and
$\int u_0(u_0f)=0$. Moreover, $\|u_0f\|_2^2\ge1-M_\varepsilon$.
Testing the weak ground-state equation with $u_0f^2$ gives the exact identity

$$
q_{\Omega_\varepsilon,\alpha}[u_0f]
 -E_0(\Omega_\varepsilon;\alpha)\|u_0f\|_2^2
 =\int_{\Omega_\varepsilon}u_0^2|\nabla f|^2
 \le4M_\varepsilon.
\tag{9.22}
$$

Both products are valid test functions because $f$ is bounded and Lipschitz. Expanding the gradients shows cancellation of the cross terms and of the Robin boundary term. The variational characterization on the orthogonal complement of $u_0$ now proves, whenever $C_\alpha\varepsilon^{1/3}<1$,

$$
0<\gamma(\Omega_\varepsilon;\alpha)
\le\frac{4C_\alpha\varepsilon^{1/3}}
 {1-C_\alpha\varepsilon^{1/3}}
\longrightarrow0.
\tag{9.23}
$$

The estimates are uniform when $\alpha$ ranges in a compact subinterval of $(0,\infty)$: $A_\alpha$ and $C_\alpha$ are bounded there, and $\alpha\varepsilon\le1/4096$ holds uniformly for sufficiently small $\varepsilon$.

*Proof of Theorem 9.1.* In dimension four put $a_\varepsilon=D/D_\varepsilon$. The domain $a_\varepsilon\Omega_\varepsilon$ has diameter exactly $D$, $a_\varepsilon\to D/2$, and the change of scale in (9.2) gives

$$
\gamma(a_\varepsilon\Omega_\varepsilon;\alpha)
=a_\varepsilon^{-2}
 \gamma(\Omega_\varepsilon;a_\varepsilon\alpha)\longrightarrow0
\tag{9.24}
$$

by the compact-parameter uniformity just proved. For $d>4$ start with
$G_\varepsilon=\Omega_\varepsilon\times(0,\varepsilon)^{d-4}$.
The Robin form separates on a Cartesian product: the tensor products of factor eigenfunctions form a complete eigenbasis and their eigenvalues add. Keeping every interval factor in its ground state and using the first two $\Omega_\varepsilon$ eigenfunctions therefore gives
$\gamma(G_\varepsilon;\alpha)\le\gamma(\Omega_\varepsilon;\alpha)$.
Also $\operatorname{diam}(G_\varepsilon)^2=D_\varepsilon^2+(d-4)\varepsilon^2\to4$.
The same scaling argument yields diameter exactly $D$. Every gap is positive, so its infimum is zero. ∎

**Corollary 9.3 (a concrete counterexample).** Set $\alpha=1$ and $\varepsilon=10^{-30}$ in (9.13), and let $I$ be an interval of length $D_\varepsilon$. Then

$$
\gamma(\Omega_\varepsilon;1)<\frac1{100},
\qquad \gamma(I;1)>1.
\tag{9.25}
$$

*Proof.* All smallness conditions above hold. From $\delta>1/7$ and $A_1=25/2$,

$$
M_\varepsilon\le7(110000+25/2)10^{-10}
<\frac1{1000}.
\tag{9.26}
$$

Thus (9.22) gives $\gamma(\Omega_\varepsilon;1)<4/999<1/100$.
By (9.14), $2\le D_\varepsilon\le21/10$. On $I$, positivity of the Robin boundary term and the min--max principle give
$E_1(I;1)\ge E_1(I;0)=\pi^2/D_\varepsilon^2>100/49$.
The constant trial function gives $E_0(I;1)\le2/D_\varepsilon\le1$.
Hence $\gamma(I;1)>51/49>1$. ∎

**Corollary 9.4 (failure of Robin gap monotonicity).** On the fixed four-dimensional polyhedron in Corollary 9.3, the function $\alpha\mapsto\gamma(\Omega_\varepsilon;\alpha)$ is not increasing on $(0,\infty)$. This disproves the convex-domain monotonicity conjecture attributed to Smits in [L, Conjecture A].

*Proof.* The segment argument in (9.9), now in dimension four, gives for a mean-zero $w$ on a convex set of diameter $D$ the estimate

$$
\|w\|_2^2\le D^2\left(\int_0^{1/2}(1-t)^{-4}\,dt\right)\|\nabla w\|_2^2
=\frac73D^2\|\nabla w\|_2^2.
\tag{9.27}
$$

Thus $\gamma(\Omega_\varepsilon;0)\ge3/(7D_\varepsilon^2)>1/20$, while Corollary 9.3 gives $\gamma(\Omega_\varepsilon;1)<1/100$.
The Robin eigenvalues are continuous at zero on this fixed Lipschitz domain. One can see this directly from the min--max principle: for $\alpha\ge0$ the eigenvalues are at least their Neumann values, and the span of the first $j+1$ Neumann eigenfunctions gives an upper bound $E_j(G;\alpha)\le E_j(G;0)+c_j\alpha$, since its unit sphere is finite dimensional and the trace is continuous. Therefore the gap is greater than $1/20$ for some sufficiently small positive $\alpha<1$, and cannot be increasing on $(0,\infty)$. ∎

The universal conjecture is therefore disproved by a polyhedron given entirely by explicit inequalities; no individual eigenvalue needs to be computed. Theorems 1.1 and 1.3 concern a fixed domain with varying parameter, whereas Theorem 9.1 fixes the positive parameter and varies the domain. These different orders of quantifiers matter: on every fixed domain the Robin eigenvalues still converge to their Neumann or Dirichlet limits as the parameter tends to zero or infinity. The degeneration above contradicts neither endpoint theorem. It uses a three-dimensional transverse family and leaves the positive-Robin gap conjecture in dimensions two and three unresolved.

## 10. Exponential gap bounds and failure of spectral-ratio monotonicity

The gap and the ratio of the first two eigenvalues are different functions of the Robin parameter. The failure of gap monotonicity in Corollary 9.4 does not alone imply failure of ratio monotonicity, because the first eigenvalue also changes. This section strengthens the localization estimate enough to compare the Robin ratio with the Dirichlet ratio on the same fixed domain.

Write

$$
\mathcal Q(G;\alpha)=\frac{E_1(G;\alpha)}{E_0(G;\alpha)},
\qquad
\mathcal Q_D(G)=\frac{\Lambda_1(G)}{\Lambda_0(G)},
\tag{10.1}
$$

where $\Lambda_0<\Lambda_1$ are the first two Dirichlet eigenvalues. Laugesen [L, Conjecture B] conjectures that $\mathcal Q(G;\alpha)$ decreases for $\alpha>0$ on every bounded Lipschitz domain. The question also appears in [OP, Open Problem 7]. The recent revised preprint of Dai and Sun [DS, Theorem 1.3] proves the assertion on balls. Their Theorems 1.1--1.2 concern shape-dependent upper bounds and are separate from monotonicity on an arbitrary fixed domain. Here we give convex polyhedral counterexamples.

**Theorem 10.1 (spectral-ratio counterexamples).** For every $d\ge4$, $D>0$ and $\alpha_*>0$, there is a bounded open convex polyhedron $G\subset\mathbb R^d$ of diameter $D$ such that

$$
\mathcal Q(G;\alpha_*)<\mathcal Q_D(G).
\tag{10.2}
$$

Consequently, there is a finite $\alpha_2>\alpha_*$ with
$\mathcal Q(G;\alpha_2)>\mathcal Q(G;\alpha_*)$. In particular, the spectral-ratio monotonicity conjecture is false, even within convex domains.

We first prove a localization lemma for the family $\Omega_\varepsilon$ in (9.13). In this section $u_0$ always denotes its positive ground state with unit $L^2$ norm. Put

$$
\delta_*:=r(1/4)-r_0
=\frac3{22}(\sqrt{26}-3\sqrt2)>\frac1{16},
\qquad \kappa_\alpha:=\frac{\alpha\delta_*}{2}.
\tag{10.3}
$$

The rational bounds used for (9.7) give $\delta_*>15/154>1/16$.
For each fixed $\alpha>0$, take $\varepsilon$ small enough that

$$
\alpha\varepsilon\le\frac1{4096},\qquad
A_\alpha\varepsilon^{1/3}+110000\alpha^2\varepsilon
\le\frac{\alpha\delta_*}{2}.
\tag{10.4}
$$

Equations (9.16) and (9.19) show that every form-domain function $v$ supported in $|t|\le3/4$ satisfies

$$
q_{\Omega_\varepsilon,\alpha}[v]
-E_0(\Omega_\varepsilon;\alpha)\|v\|_2^2
\ge\frac{\kappa_\alpha}{\varepsilon}\|v\|_2^2.
\tag{10.5}
$$

This uses $s(t)\ge1/4$ on that support. No boundary condition is imposed on an artificial slice.

**Lemma 10.2 (nested localization).** Define
$M(a)=\int_{\Omega_\varepsilon\cap\{|t|\le a\}}u_0^2$.
Under (10.4), for $0<a<b\le3/4$,

$$
M(a)\le\frac{\varepsilon}{\kappa_\alpha(b-a)^2}M(b).
\tag{10.6}
$$

*Proof.* Let $\eta(t)$ be one on $|t|\le a$, vanish on $|t|\ge b$, and be linear on each intervening interval. Multiplication by this bounded Lipschitz function preserves $H^1$. Testing the ground-state equation with $u_0\eta^2$, as in (9.22), gives

$$
\frac{\kappa_\alpha}{\varepsilon}\int\eta^2u_0^2
\le q_{\Omega_\varepsilon,\alpha}[u_0\eta]
-E_0(\Omega_\varepsilon;\alpha)\|u_0\eta\|_2^2
=\int u_0^2|\eta'|^2.
\tag{10.7}
$$

The first inequality is (10.5), and $|\eta'|\le(b-a)^{-1}$ with derivative supported in $|t|\le b$. This proves (10.6). All Robin boundary terms are included in the identity and cancel exactly. ∎

**Proposition 10.3 (exponentially small positive-Robin gaps).** For each fixed $\alpha>0$, there exist $c_\alpha>0$ and $\varepsilon_\alpha>0$ such that

$$
0<\gamma(\Omega_\varepsilon;\alpha)
\le128\exp\left(-\frac{c_\alpha}{\sqrt\varepsilon}\right)
\qquad(0<\varepsilon<\varepsilon_\alpha).
\tag{10.8}
$$

The constants can be chosen uniformly when $\alpha$ ranges over a compact subinterval of $(0,\infty)$.

*Proof.* Divide $[1/4,3/4]$ into $N$ equal subintervals and apply (10.6) successively. Since $M(3/4)\le1$,

$$
M(1/4)\le\left(\frac{4N^2\varepsilon}{\kappa_\alpha}\right)^N.
\tag{10.9}
$$

For sufficiently small $\varepsilon$, choose
$N=\lfloor\sqrt{\kappa_\alpha}/(4\sqrt\varepsilon)\rfloor\ge1$.
The factor in parentheses is at most $1/4$, so

$$
M(1/4)\le4^{-N}
\le4\exp\left(-\frac{(\log4)\sqrt{\kappa_\alpha}}
 {4\sqrt\varepsilon}\right),
\qquad M(1/4)\le\frac14.
\tag{10.10}
$$

Choose an odd function $f$ equal to $4t$ on $|t|\le1/4$ and to $\operatorname{sgn}(t)$ outside. It is orthogonal to the even ground state after multiplication by $u_0$. The same variational argument as in (9.22) gives

$$
\gamma(\Omega_\varepsilon;\alpha)
\le\frac{16M(1/4)}{1-M(1/4)}.
\tag{10.11}
$$

Equations (10.10)--(10.11) prove (10.8), with
$c_\alpha=(\log4)\sqrt{\kappa_\alpha}/4$, because $256/3<128$.
On a compact positive parameter interval, (10.4) holds uniformly for small $\varepsilon$, and $\kappa_\alpha$ has a positive lower bound. This proves the last assertion. ∎

Only an upper bound on the gap is asserted. The proof does not determine the exact tunneling rate or a matching exponential lower bound.

### 10.1. An explicit domain whose Robin ratio lies below its Dirichlet ratio

**Proposition 10.4.** For $\varepsilon=10^{-30}$, the polyhedron $\Omega_\varepsilon$ satisfies

$$
\mathcal Q(\Omega_\varepsilon;1)-1
\le2^{23}\varepsilon^3
<\frac{\varepsilon^2}{200}
<\mathcal Q_D(\Omega_\varepsilon)-1.
\tag{10.12}
$$

*Proof.* The stronger elementary inequality

$$
A_1\varepsilon^{1/3}+110000\varepsilon<\frac1{32}
\tag{10.13}
$$

holds at this value of $\varepsilon$, with $A_1=25/2$.
Since $\delta_*>1/16$, the proof of (10.5) permits the barrier constant $1/32$ in place of $\kappa_1$. Apply Lemma 10.2 first with $(a,b)=(1/2,3/4)$ and then with $(a,b)=(1/4,1/2)$. This gives
$M(1/4)\le(512\varepsilon)^2<1/2$.
Equation (10.11) therefore implies

$$
\gamma(\Omega_\varepsilon;1)
\le32(512\varepsilon)^2=2^{23}\varepsilon^2.
\tag{10.14}
$$

The global lower bound (9.16) gives
$E_0(\Omega_\varepsilon;1)\ge r_0/\varepsilon-110000\ge1/\varepsilon$.
For the last inequality, use $r_0>2$ and $110000\varepsilon<1$.
This proves the first inequality in (10.12).

We use the established Dirichlet fundamental-gap theorem of Andrews and Clutterbuck [AC, Corollary 1.4]:

$$
\Lambda_1(G)-\Lambda_0(G)\ge\frac{3\pi^2}{\operatorname{diam}(G)^2}
\tag{10.15}
$$

for bounded convex domains. The theorem includes nonsmooth convex domains by approximation, as explicitly stated in [AC] after its main results. It is a prior theorem, not a conclusion of the present paper.

The rectangular box

$$
B_\varepsilon=(-1/2,1/2)\times(-\varepsilon/12,\varepsilon/12)^3
\subset\Omega_\varepsilon
\tag{10.16}
$$

has first Dirichlet eigenvalue $\pi^2(1+108/\varepsilon^2)$. Domain monotonicity for Dirichlet eigenvalues consequently gives
$\Lambda_0(\Omega_\varepsilon)\le109\pi^2/\varepsilon^2$.
Also $D_\varepsilon^2\le5$ by (9.14). Dividing (10.15) by this upper bound gives

$$
\mathcal Q_D(\Omega_\varepsilon)-1
\ge\frac{3\varepsilon^2}{545}
>\frac{\varepsilon^2}{200}.
\tag{10.17}
$$

Finally $200\cdot2^{23}\varepsilon<1$, proving the strict separation in (10.12). Every numerical comparison used here is a rational inequality; no eigenvalue computation is required. ∎

### 10.2. The fixed-domain limit and proof of the ratio counterexample

We recall the Robin-to-Dirichlet limit, including the short form argument to make the order of limits explicit. On a fixed bounded Lipschitz domain $G$,

$$
E_j(G;\alpha)\uparrow\Lambda_j(G)
\qquad(\alpha\to+\infty)
\tag{10.18}
$$

for each fixed $j$. Indeed, positivity of the boundary term makes $E_j$ increasing, and Dirichlet trial spaces bound it above by $\Lambda_j$. Write its limit as $L_j\le\Lambda_j$. Along any sequence $\alpha_k\to\infty$, the first $j+1$ orthonormal Robin eigenfunctions are uniformly bounded in $H^1$, and their squared boundary norms are at most $\Lambda_j/\alpha_k$. Take a subsequence converging weakly in $H^1$ and strongly in $L^2$. The limits are orthonormal and have zero trace, hence belong to $H_0^1(G)$. For each linear combination of these limits, weak lower semicontinuity bounds its gradient energy by $L_j$ times its squared norm: apply the bound on the corresponding combination in the Robin eigenspace before passing to the limit. The Dirichlet min--max principle gives $\Lambda_j\le L_j$, proving (10.18). In particular,
$\mathcal Q(G;\alpha)\to\mathcal Q_D(G)$.

*Proof of Theorem 10.1.* First take $d=4$ without diameter normalization. By (9.16), for small $\varepsilon$,
$E_0(\Omega_\varepsilon;\alpha)\ge\alpha r_0/(2\varepsilon)$.
Together with Proposition 10.3 this implies, uniformly on compact positive parameter intervals,

$$
\mathcal Q(\Omega_\varepsilon;\alpha)-1
\le C\varepsilon e^{-c/\sqrt\varepsilon}.
\tag{10.19}
$$

On the other hand, (10.17) gives a Dirichlet relative gap bounded below by a positive constant times $\varepsilon^2$. Exponential decay is smaller than every positive power of $\varepsilon$, so the Robin ratio is strictly below the Dirichlet ratio for sufficiently small $\varepsilon$.

For $d>4$, let $G_\varepsilon=\Omega_\varepsilon\times(0,\varepsilon)^{d-4}$. Product separation gives
$\gamma(G_\varepsilon;\alpha)\le\gamma(\Omega_\varepsilon;\alpha)$ and
$E_0(G_\varepsilon;\alpha)\ge E_0(\Omega_\varepsilon;\alpha)$, since all additional factor ground eigenvalues are positive. Thus (10.19) remains an upper bound for its relative gap. Its diameter tends to two, while the inscribed product box gives
$\Lambda_0(G_\varepsilon)\le(105+d)\pi^2/\varepsilon^2$ for $\varepsilon\le1$.
Equation (10.15) again bounds the Dirichlet relative gap below by a positive dimension-dependent multiple of $\varepsilon^2$.

Finally set $a_\varepsilon=D/\operatorname{diam}(G_\varepsilon)$ and $G=a_\varepsilon G_\varepsilon$. The Robin ratio on $G$ at $\alpha_*$ equals the ratio on $G_\varepsilon$ at $a_\varepsilon\alpha_*$, and the Dirichlet ratio is invariant under scaling. Since $a_\varepsilon\to D/2$, compact-parameter uniformity proves (10.2) for small $\varepsilon$. Having fixed one such full-dimensional domain, use (10.18) to choose a finite $\alpha_2>\alpha_*$ for which the ratio exceeds its value at $\alpha_*$. The geometry is held fixed during this last limit. ∎

The conclusion refutes [L, Conjecture B] independently of the gap-monotonicity conjecture [L, Conjecture A]. It does not refute monotonicity of $\alpha\mathcal Q(G;\alpha)$, which is a theorem of [L], or the ball result of [DS]. The spectral-ratio conjecture restricted to dimensions two and three remains unresolved here. The different conjecture that the second eigenvalue itself is concave in the positive Robin parameter [L, Conjecture C] is addressed next, using asymmetric geometry.

## 11. The second Robin eigenvalue need not be concave

Laugesen [L, Conjecture C] asks whether the second Robin eigenvalue on every bounded convex domain is concave in the positive parameter. The question is also recorded in [OP, Open Problem 7] and [OW, p.2099]. The symmetric family of Section 9 does not by itself answer this question: if a second eigenfunction is odd across a symmetry plane, its eigenvalue is the ground eigenvalue of a mixed problem on one half and is therefore concave, as observed in [L]. We instead construct two asymmetric end regions whose limiting ground energies cross.

**Theorem 11.1 (failure of second-eigenvalue concavity).** For every $d\ge4$ and $D>0$, there is a bounded open convex polyhedron $G\subset\mathbb R^d$ of diameter $D$ and positive parameters $\alpha_-<\alpha_0<\alpha_+$, with $\alpha_0=(\alpha_-+\alpha_+)/2$, such that

$$
E_1(G;\alpha_0)
<\frac{E_1(G;\alpha_-)+E_1(G;\alpha_+)}2.
\tag{11.1}
$$

Thus [L, Conjecture C] is false. The proof uses convergence at three fixed parameters before diameter normalization, not differentiation of an asymptotic expansion. We provide the needed spectral convergence argument in full.

### 11.1. Geometry and the two limiting one-dimensional problems

Let $h>0$, $\varepsilon=h^3$, $a_L=1/2$ and $a_R=1$. For a fixed $b>0$, to be chosen below, define

$$
A_h(t)=1+\frac{bh(t+1)}2,
\qquad L(t)=\min\{a_L(t+1),a_R(1-t)\},
\quad -1<t<1,
\tag{11.2}
$$

and

$$
\begin{split}
\mathcal O_h=\{(t,x,y,z):\ &|t|<1,\\
&|x|+5|y|<\varepsilon A_h(t),\\
&|x|+|z|<\varepsilon[A_h(t)+L(t)]\}.
\end{split}
\tag{11.3}
$$

Every condition is an intersection of finitely many strict affine inequalities: for the last condition impose separately the two affine branches of $L$. Thus $\mathcal O_h$ is convex, bounded and full dimensional. The branches meet at $t_0=1/3$, where $L=2/3$. For small $h$, $1\le A_h\le2$, and its unscaled transverse section is

$$
K_h(t)=A_h(t)K_{s_h(t)},\qquad
s_h(t)=\frac{L(t)}{A_h(t)}\in[0,2/3].
\tag{11.4}
$$

Here $K_s$, $r(s)$ and $r_0$ are from (9.4)--(9.6). Write

$$
R_h(t)=\frac{r(s_h(t))}{A_h(t)},
\qquad k=r'(0)>0.
\tag{11.5}
$$

Cut the domain at $t=t_0$ into its left and right parts. Let $E_{q,j}^{\mathsf B}(h;\alpha)$, $q=L,R$, be the ordered eigenvalues on part $q$, with the original Robin condition on the exterior boundary and condition $\mathsf B=N$ or $D$ on the cut. Here $N$ means that the cut has no boundary term in the form and no trace restriction; $D$ means zero trace there. No Robin term is added at the cut.

The left rescaling is $t=-1+h\tau$, $0<\tau<T_L/h$, where $T_L=4/3$. The right rescaling is $t=1-h\tau$, $0<\tau<T_R/h$, where $T_R=2/3$. Taylor expansion of the explicit smooth function $r$, uniformly on compact $\tau$ intervals, gives

$$
\begin{aligned}
\frac{R_h(-1+h\tau)-r_0}{h}&\longrightarrow k a_L\tau,\\
\frac{R_h(1-h\tau)-r_0}{h}&\longrightarrow k a_R\tau-br_0.
\end{aligned}
\tag{11.6}
$$

Indeed, on the left $A_h=1+(b/2)h^2\tau$ and $L=a_Lh\tau$; on the right $A_h=1+bh-(b/2)h^2\tau$ and $L=a_Rh\tau$.

There is also a global lower bound on each rescaled half. If $m=\min_{[0,2/3]}r'>0$, then $r(s)\ge r_0+ms$, whence, using $1\le A_h\le2$,

$$
\frac{R_h(t)-r_0}{h}
\ge \frac{m L(t)}{4h}-br_0
=\frac{m a_q}4\tau-br_0.
\tag{11.7}
$$

This estimate prevents low-energy mass from escaping to large $\tau$.

Let $\mu_j$, $j=0,1,\ldots$, be the eigenvalues of the form

$$
\mathfrak a[g]=\int_0^\infty\bigl(|g'|^2+\tau|g|^2\bigr)\,d\tau,
\quad
\mathcal D(\mathfrak a)=\{g\in H^1(0,\infty):\sqrt\tau g\in L^2\}.
\tag{11.8}
$$

There is no trace restriction at zero, so the associated operator is the Neumann half-line Airy operator. Its form embedding is compact: local Rellich compactness and the bound $\int_T^\infty|g|^2\le T^{-1}\int\tau|g|^2$ give global compactness. Its eigenvalues are simple, since a solution of $-g''+\tau g=\mu g$ with $g'(0)=0$ is determined by $g(0)$; if both initial values vanish the solution is zero. Its ground energy is positive, because a zero-energy eigenfunction would have both derivative and $\sqrt\tau g$ equal to zero. In particular $0<\mu_0<\mu_1$.

**Lemma 11.2 (end-region spectral limits).** For every fixed $\alpha>0$, $j\ge0$ and $\mathsf B\in\{N,D\}$,

$$
\begin{aligned}
h^2\left(E_{L,j}^{\mathsf B}(h;\alpha)-\frac{\alpha r_0}{h^3}\right)
&\longrightarrow \mu_j(\alpha k a_L)^{2/3},\\
h^2\left(E_{R,j}^{\mathsf B}(h;\alpha)-\frac{\alpha r_0}{h^3}\right)
&\longrightarrow \mu_j(\alpha k a_R)^{2/3}-\alpha br_0.
\end{aligned}
\tag{11.9}
$$

### 11.2. Proof of the spectral limits

We prove Lemma 11.2 through matching variational bounds. All constants below may depend on the fixed $b$ and $\alpha$, but not on $h$, the cut condition, or the function being estimated.

**Retained transverse coercivity.** The proof of Lemma 9.2 yields the slightly stronger estimate

$$
q_{K_s,\beta}[f]\ge\frac14\|\nabla f\|_2^2
 +(\beta r(s)-110000\beta^2)\|f\|_2^2,
\qquad 0\le\beta\le1/8192.
\tag{11.10}
$$

To check this, in (9.12) use only one quarter of $g^2$ to dominate $\beta r(s)\|w\|_2^2$: $r(s)\le32$, $\|w\|_2^2\le64g^2$, and $\beta\le1/8192$ suffice. The remaining quarter is retained, and the same mean estimate bounds the remainder by $102400\beta^2\|f\|_2^2$. Dilation by $A\in[1,2]$ preserves the coefficient $1/4$ and the constant $110000$ in the quadratic remainder, with $r(s)$ replaced by $r(s)/A$, provided $A\beta\le1/8192$.

On either half of $\mathcal O_h$, each lateral facet is a graph with $t$ slope bounded by $C\varepsilon$; its surface measure divided by $dt$ times the fiber surface measure lies between $1$ and $1+C\varepsilon^2$. This follows directly from the affine inequalities in (11.3): the transverse facet normals have lengths $\sqrt{26}$ and $\sqrt2$, while the longitudinal components are respectively $-\varepsilon A_h'$ and $-\varepsilon(A_h'+L')$. Their intersections have surface measure zero. Positivity of $\alpha$ allows us to drop the excess surface factor and the exterior cap for a lower bound.

Use $X=(x,y,z)/\varepsilon$ and one of the endpoint coordinates $\tau$ above, and write $U(\tau,X)=u(t,\varepsilon X)$. After dividing both form and norm by the constant volume factor $h\varepsilon^3$, multiplying the form by $h^2$, and subtracting $\alpha r_0/h$ times the norm, denote the centered form by $\mathfrak q_h[U]$ and its norm by $\|U\|_h^2=\int|U|^2\,dX\,d\tau$. The moving fibers in this integral are $K_h(t(\tau))$. Scaling (11.10), with $\beta=\alpha\varepsilon$, gives

$$
\mathfrak q_h[U]\ge
\int\left\{|\partial_\tau U|^2+
 \frac1{4h^4}|\nabla_XU|^2+
 (W_h(\tau)-110000\alpha^2h^2)|U|^2\right\}\,dX\,d\tau,
\tag{11.11}
$$

where $W_h(\tau)=\alpha(R_h(t(\tau))-r_0)/h$ and $\partial_\tau$ is taken at fixed $X$. The factor $h^{-4}$ is $h^2\varepsilon^{-2}$. The estimate holds with either condition on the cut. It follows first for smooth functions by the facet formula and Fubini, then for the form domain by Sobolev density and trace continuity.

**Fixed-fiber coordinates.** We give the details needed to handle the moving sections without assuming differentiability of their edges. On $\mathbb R^3$ put

$$
p_s(X)=\max\left\{|X_1|+5|X_2|,
 \frac{|X_1|+|X_3|}{1+s}\right\}.
\tag{11.12}
$$

Then $K_s=\{p_s<1\}$. On the unit sphere the functions $p_s$ are uniformly Lipschitz in $(s,X)$ and bounded above and below by positive constants, since the sets $K_s$ contain $B_{1/6}$ and lie in $B_3$. Let

$$
f_h(\tau,\theta)=
 A_h(t(\tau))\frac{p_0(\theta)}{p_{s_h(t(\tau))}(\theta)},
\qquad
\Phi_h(\tau,Y)=f_h(\tau,Y/|Y|)Y,
\tag{11.13}
$$

with $\Phi_h(\tau,0)=0$. This map carries $K_0$ onto $K_h(t(\tau))$. The functions $f_h$ and $f_h^{-1}$ have uniform angular Lipschitz bounds and positive upper and lower bounds. The radial map and its inverse are consequently uniformly Lipschitz. For example, for $|Y|\ge|Z|>0$, bound the radial coefficient difference by its spherical Lipschitz constant times $|Y/|Y|-Z/|Z||$, and use $|Z|\,|Y/|Y|-Z/|Z||\le2|Y-Z|$. The bound at zero is immediate. Moreover $|\partial_\tau f_h|\le Ch$ almost everywhere, because the $t$ derivatives of $A_h$ and $s_h$ are bounded. Thus $|\partial_\tau\Phi_h|\le Ch$ on $K_0$.

The spatial Jacobian is

$$
J_h(\tau,Y)=\det D_Y\Phi_h=f_h(\tau,Y/|Y|)^3
\tag{11.14}
$$

almost everywhere. Indeed $D_Y(fY)=fI+Y\otimes\nabla f$ and $Y\cdot\nabla f=0$ for the homogeneous degree-zero radial coefficient; the determinant formula gives $f^3$. In particular $0<c\le J_h\le C$. On each fixed finite $\tau$ interval, $f_h\to1$ and $J_h\to1$ uniformly, on either half. The map $(\tau,Y)\mapsto(\tau,\Phi_h(\tau,Y))$ and its inverse are bi-Lipschitz, so Sobolev change of variables and the almost-everywhere chain rule apply.

Put $v(\tau,Y)=U(\tau,\Phi_h(\tau,Y))$. The chain rule gives

$$
\partial_\tau U=\partial_\tau v-B_h\cdot\nabla_Yv,
\qquad |B_h|\le Ch,
\qquad |\nabla_XU|\ge c|\nabla_Yv|,
\tag{11.15}
$$

at corresponding points. For the first formula $B_h=(D_Y\Phi_h)^{-1}\partial_\tau\Phi_h$. The inverse derivative is bounded by the bi-Lipschitz constant. Using $|a-B_h\cdot z|^2\ge(1-h)|a|^2-Ch|z|^2$ in (11.11) and absorbing the negative term into the transverse term yields, for small $h$,

$$
\mathfrak q_h[v]\ge
\int_{(0,T_q/h)\times K_0}
\left\{(1-h)|\partial_\tau v|^2+
 c h^{-4}|\nabla_Yv|^2+
 (W_h-C_\alpha h^2)|v|^2\right\}J_h\,dY\,d\tau.
\tag{11.16}
$$

We keep the same form symbol after pullback; its norm is now $\|v\|_h^2=\int|v|^2J_h$. By (11.7) there are $c_\alpha>0$ and $C_\alpha'>0$ such that $W_h\ge c_\alpha\tau-C_\alpha'$ on the whole cylinder. Consequently every sequence of bounded norm and bounded centered energy satisfies

$$
\int\left(|\partial_\tau v_h|^2+h^{-4}|\nabla_Yv_h|^2
 +\tau|v_h|^2\right)\,dY\,d\tau\le C.
\tag{11.17}
$$

**Lower-limit compactness.** On each fixed cylinder $(0,T)\times K_0$, (11.17) gives an $H^1$ bound and hence a strongly $L^2$ convergent subsequence. A diagonal extraction gives a common limit on all such cylinders. Since $\nabla_Yv_h\to0$ in $L^2$, this limit is $v(\tau,Y)=g(\tau)$: $K_0$ is connected. The tail estimate
$\int_{\tau>T}|v_h|^2J_h\le C/T$ follows from (11.17). Local convergence, $J_h\to1$ on finite cylinders and this tail bound show that norms and pairwise inner products converge globally. This statement concerns integrals over the increasing cylinders; no zero extension across a Neumann cut is asserted to lie in $H^1$.

By (11.6), $W_h$ converges locally uniformly to
$W_L(\tau)=\alpha k a_L\tau$ or
$W_R(\tau)=\alpha k a_R\tau-\alpha br_0$.
Choose a fixed $C_0$ so that $W_h+C_0\ge0$ for all small $h$. Apply (11.16) after adding $C_0\|v_h\|_h^2$, restrict its nonnegative integrands to $(0,T)\times K_0$, and pass to the lower limit. Weak lower semicontinuity of the derivative term and strong local convergence of the potential term give the limiting integral there. Let $T\to\infty$ and subtract $C_0$ times the converging norm. We obtain

$$
\liminf_{h\to0}\mathfrak q_h[v_h]
\ge |K_0|\int_0^\infty(|g'|^2+W_q|g|^2)\,d\tau.
\tag{11.18}
$$

The disappearing $C_\alpha h^2$ term in (11.16) can equivalently be moved to the left before restriction. The limit belongs to the form domain in (11.8); no condition on $g(0)$ is imposed. This proves the needed lower-limit statement for any bounded-energy sequence, not only eigenfunctions.

**Upper trial spaces.** Take $g$ smooth on $[0,\infty)$ and compactly supported, with arbitrary value at zero. On the actual moving fibers set $U(\tau,X)=g(\tau)$. For small $h$ its support avoids the cut, so it is admissible for both cut conditions. Its squared norm is $\int V_h(\tau)|g|^2$, where $V_h=|K_h(t(\tau))|\to|K_0|$ locally uniformly. The part of its lateral form with graph factor one gives exactly $\int V_h W_h|g|^2$ after centering; its longitudinal energy is $\int V_h|g'|^2$. The excess graph factor contributes at most $C\alpha h^5\int V_h|g|^2$, because $h^2\alpha\varepsilon^{-1}\varepsilon^2=\alpha h^5$ and $R_h$ is bounded. The exterior cap contributes
$\alpha h V_h(0)|g(0)|^2$, which tends to zero. Thus both the form and norm converge to

$$
|K_0|\int_0^\infty(|g'|^2+W_q|g|^2),
\qquad |K_0|\int_0^\infty|g|^2,
\tag{11.19}
$$

respectively. By polarization this convergence holds on every fixed finite-dimensional space of such trial functions. Smooth compactly supported functions on the closed half-line are dense in (11.8): truncate at large $\tau$, then reflect across zero and mollify. Approximation of each finite eigenspace followed by min--max gives the upper bound for every ordered eigenvalue of the centered form.

**Ordered eigenvalues and multiplicity.** For the lower bound on the $j$-th centered eigenvalue, take a sequence realizing its lower limit and its first $j+1$ orthonormal eigenfunctions. The upper bounds just proved and the lower coercive bound give (11.17) for all of them. After a common subsequence their limits $g_0,\ldots,g_j$ are orthonormal in $L^2(0,\infty;|K_0|\,d\tau)$. For any fixed coefficients, the corresponding linear combination has centered Rayleigh quotient at most the $j$-th centered eigenvalue. Apply (11.18) to that combination. The limiting span therefore has maximum Rayleigh quotient no greater than that lower limit. Min--max for the half-line form proves the opposite eigenvalue inequality. This handles multiplicities without assuming convergence of individual eigenfunctions to a prescribed basis.

Finally, dilation of $\tau$ in (11.8) shows that the eigenvalues with potential $c\tau$ are $c^{2/3}\mu_j$. Adding the constant $-\alpha br_0$ shifts the right-hand eigenvalues. This proves (11.9). ∎

### 11.3. A crossing of limiting ground energies gives a strict concavity violation

Let $\nu_j(\alpha)$ be the increasingly ordered union, with multiplicity, of the two spectra on the right of (11.9). The original domain lies between the two cut problems in the form sense. More precisely, restriction to the halves embeds its form domain into the direct sum with Neumann cuts, and the direct sum with Dirichlet cuts embeds by zero-trace gluing into its form domain, with the same form values. Min--max gives

$$
E_j^{N\oplus N}(h;\alpha)\le E_j(\mathcal O_h;\alpha)
\le E_j^{D\oplus D}(h;\alpha).
\tag{11.20}
$$

For each fixed $j$, the first $j+1$ entries in each half suffice to determine the first $j+1$ entries of its ordered union. Lemma 11.2 and (11.20) imply

$$
h^2\left(E_j(\mathcal O_h;\alpha)-\frac{\alpha r_0}{h^3}\right)
\longrightarrow \nu_j(\alpha).
\tag{11.21}
$$

Choose the geometry coefficient by

$$
\ell=\mu_0(k a_L)^{2/3},\qquad
r=\mu_0(k a_R)^{2/3},\qquad
C=r-\ell>0,\qquad b=C/r_0.
\tag{11.22}
$$

The two limiting ground energies are
$F_L(\alpha)=\ell\alpha^{2/3}$ and
$F_R(\alpha)=r\alpha^{2/3}-C\alpha$.
They coincide at $\alpha=1$, where each is strictly below both first excited end energies. By continuity, for all $\alpha$ in some interval about one the first two entries of the limiting union are these two ground energies. Therefore

$$
\nu_1(\alpha)=\max\{F_L(\alpha),F_R(\alpha)\}
\quad\text{near }1.
\tag{11.23}
$$

Since $F_R-F_L=C(\alpha^{2/3}-\alpha)$, the right branch is larger below one and the left branch is larger above one. For small $\eta>0$, Taylor's theorem gives

$$
\frac{\nu_1(1-\eta)+\nu_1(1+\eta)}2-\nu_1(1)
=\frac C6\eta+O(\eta^2)>0.
\tag{11.24}
$$

Fix one such $\eta<1$. Use (11.21) at the three fixed parameters $1-\eta,1,1+\eta$. The affine leading term cancels in their midpoint difference. Hence for every sufficiently small $h$,

$$
E_1(\mathcal O_h;1)
<\frac{E_1(\mathcal O_h;1-\eta)+E_1(\mathcal O_h;1+\eta)}2.
\tag{11.25}
$$

This is a strict inequality on a single fixed full-dimensional convex polyhedron once $h$ is chosen. The crossing in the proof belongs to the limiting decoupled problems; no actual crossing of the first two eigenvalues on the connected domain is asserted.

### 11.4. Higher dimensions and prescribed diameter

We include the short interval estimate needed for products. For $f=m+w$ on $(0,1)$ with $\int w=0$, the identity
$w(x)=\int_0^1(w(x)-w(y))\,dy$ gives
$|w(x)|\le\|w'\|_2$ and $\|w\|_2\le\|w'\|_2$. Dropping the nonnegative boundary quadratic term of $w$ and completing a square yields, for $g=\|w'\|_2$,

$$
q_{(0,1),\beta}[f]\ge g^2+2\beta m^2-4\beta|m|g
\ge\tfrac12g^2+2\beta m^2-8\beta^2m^2.
\tag{11.26}
$$

For $0\le\beta\le1/4$, the retained $g^2/2$ dominates $2\beta\|w\|_2^2$. A constant trial gives the upper bound, so after scaling,

$$
\frac{2\alpha}{\varepsilon}-8\alpha^2
\le E_0((0,\varepsilon);\alpha)
\le\frac{2\alpha}{\varepsilon}
\quad(\alpha\varepsilon\le1/4).
\tag{11.27}
$$

For $d>4$ put $H_h=\mathcal O_h\times(0,h^3)^{d-4}$. At each of the three fixed parameters in (11.25), (11.21) bounds the gap of $\mathcal O_h$ by $O(h^{-2})$. The interval gap is at least $\pi^2h^{-6}-2\alpha h^{-3}$ by Neumann comparison and the constant trial. Thus the first excited eigenvalue of the product is obtained by exciting only the four-dimensional factor for small $h$. Product separation and (11.27) give

$$
h^2\left(E_1(H_h;\alpha)
-\frac{\alpha[r_0+2(d-4)]}{h^3}\right)
\longrightarrow\nu_1(\alpha)
\tag{11.28}
$$

at these parameters. The same strict midpoint violation follows. For $d=4$ take $H_h=\mathcal O_h$.

Finally fix one sufficiently small $h$ and set $a=D/\operatorname{diam}(H_h)$, $G=aH_h$. Scaling gives $E_1(G;\alpha)=a^{-2}E_1(H_h;a\alpha)$. Choose $\alpha_\pm=(1\pm\eta)/a$ and $\alpha_0=1/a$ to transfer the strict midpoint inequality. This proves Theorem 11.1. ∎

The construction uses positive parameters, constant boundary coefficient and zero interior potential. Its universal counterexample starts in dimension four; dimensions two and three remain unresolved here. It gives an existence theorem for sufficiently small $h$, not an explicit numerical threshold or a smooth strictly convex example. The first eigenvalue remains concave, and the ball and rectangular-box results of [L] remain valid. Sections 9, 10 and 11 answer, respectively, the separate parameter conjectures A, B and C of [L].

## References

[ACH] B. Andrews, J. Clutterbuck and D. Hauer, *Non-concavity of the Robin ground state*, Cambridge Journal of Mathematics **8** (2020), no. 2, 243-310. [Final journal article](https://doi.org/10.4310/CJM.2020.v8.n2.a1). [arXiv:1711.02779v2](https://arxiv.org/abs/1711.02779v2).

[CF] G. Crasta and I. Fragalà, *Concavity properties of solutions to Robin problems*, Cambridge Journal of Mathematics **9** (2021), no. 1, 177-212. [Final journal article](https://doi.org/10.4310/CJM.2021.v9.n1.a3). [arXiv:2006.07192v1](https://arxiv.org/abs/2006.07192v1).

[D] M. Dauge, *Neumann and mixed problems on curvilinear polyhedra*, Integral Equations and Operator Theory **15** (1992), 227-261. [Author-posted text](https://dauge.pages.math.cnrs.fr/publis/DaugeMixed92.pdf), Theorem 8.1.

[YZ] D. Ye and D. Zhang, *Concavity Properties of Robin Solutions on $C^{3,1}$ Uniformly Convex Domains*, [arXiv:2609.06223v1](https://arxiv.org/abs/2609.06223v1), September 5, 2026.

[T] P. Tolksdorf, *The Stokes resolvent problem: optimal pressure estimates and remarks on resolvent estimates in convex domains*, Calculus of Variations and Partial Differential Equations **59** (2020), article 154. [Final journal article](https://doi.org/10.1007/s00526-020-01811-8), Section 4.

[M] V. Maz'ya, *Boundedness of the gradient of a solution to the Neumann--Laplace problem in a convex domain*, Comptes Rendus Mathematique **347** (2009), 517-520. [Final journal article](https://doi.org/10.1016/j.crma.2009.03.001). [Longer preprint, arXiv:0809.2514v2](https://arxiv.org/abs/0809.2514v2).

[EL] N. Edelen and C. Li, *Sharp Neumann eigenvalue estimates and $C^2$ elliptic regularity in non-obtuse polyhedral domains*, [arXiv:2608.17194v1](https://arxiv.org/abs/2608.17194v1), August 17, 2026.

[ACHI] B. Andrews, J. Clutterbuck and D. Hauer, *The fundamental gap for a one-dimensional Schrödinger operator with Robin boundary conditions*, Proceedings of the American Mathematical Society **149** (2021), 1481-1493. [arXiv:2002.06900](https://arxiv.org/abs/2002.06900).

[L] R. S. Laugesen, *The Robin Laplacian---spectral conjectures, rectangular theorems*, Journal of Mathematical Physics **60** (2019), 121507. [Final journal article](https://doi.org/10.1063/1.5116253). [arXiv:1905.07658v1](https://arxiv.org/abs/1905.07658v1), Conjectures A--C and F and Theorems 2.2 and 3.8.

[K] D. Kielty, *Degeneration of the spectral gap with negative Robin parameter*, Mathematische Nachrichten (2023). [Final journal article](https://doi.org/10.1002/mana.202200121). [arXiv:2105.02323v2](https://arxiv.org/abs/2105.02323v2), Conjecture 1 and Theorem 2.

[FGM] M. Fradelizi, A. Giannopoulos and M. Meyer, *Some inequalities about mixed volumes*, Israel Journal of Mathematics **135** (2003), 157-179. [Final journal article](https://doi.org/10.1007/BF02776055). [Author-posted text](https://perso.math.u-pem.fr/fradelizi.matthieu/pdf/mixedvolumes.pdf).

[FMMZ] M. Fradelizi, M. Madiman, M. Meyer and A. Zvavitch, *On the volume of the Minkowski sum of zonoids*, [arXiv:2206.02123](https://arxiv.org/abs/2206.02123). The introduction records the failure of monotonicity of volume divided by surface area under Minkowski addition in dimensions at least three.

[OP] *Open problems from the Miniconference on Sharp Eigenvalue Estimates for Partial Differential Operators*, April 2020, Open Problem 7 (proposed by Richard Laugesen). [Conference problem list](https://publish.illinois.edu/eigenvalues2020/files/2020/04/Open-problems.pdf).

[AC] B. Andrews and J. Clutterbuck, *Proof of the fundamental gap conjecture*, Journal of the American Mathematical Society **24** (2011), 899-916. [Final journal article](https://doi.org/10.1090/S0894-0347-2011-00699-1). [arXiv:1006.1686v2](https://arxiv.org/abs/1006.1686v2), Corollary 1.4 and the subsequent convex-domain approximation statement.

[DS] G. Dai and Y. Sun, *Upper bound estimation for the ratio of the first two eigenvalues of Robin Laplacian*, [arXiv:2511.20988v3](https://arxiv.org/abs/2511.20988v3), December 20, 2025, Theorem 1.3. The revised title, theorem numbering and hypotheses are those of v3.

[OW] *Geometric Spectral Theory*, Oberwolfach Reports **36/2023**, meeting August 20--25, 2023, problem section, p.2099. [Report](https://doi.org/10.4171/OWR/2023/36). [Full text](https://ems.press/content/serial-article-files/47475).
