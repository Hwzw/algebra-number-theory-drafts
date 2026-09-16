# Uniform weak-field and small-flux asymptotics for exterior magnetic Steklov operators

Henry Zweiman

September 16, 2026

**Research manuscript for review.** AI-assisted development; no independent mathematical review or journal acceptance is claimed.

## Abstract

Let a fixed smooth compact obstacle in the plane have connected exterior. We study its magnetic Dirichlet-to-Neumann operator as a constant magnetic field and a nonnegative scalar potential vanish jointly. We obtain a uniform rank-one expansion in the norm of bounded differences on boundary $L^2$. The coefficient is an explicit digamma expression involving logarithmic capacity, and the remainder is $O(\sqrt{b+p})$, uniformly over all ratios of the two parameters. Consequently one effective rank-one operator approximates all ordered eigenvalues with the same error and determines every inverse-logarithmic order on each fixed spectral cluster. For a smooth simply connected obstacle, we compute the second-order gap from the equal-perimeter disk. The gap is strictly positive for every fixed nondisk at sufficiently small field, without symmetry or convexity assumptions. We also obtain an operator approximation uniform across integral Aharonov--Bohm flux, with an explicit coefficient regular at zero flux. This yields a universal lowest-eigenvalue crossover and a third-order signed-flux asymmetry that distinguishes magnetic from scalar regularization. A second-order expansion identifies the geometric terms throughout this transition and proves strict equal-perimeter disk maximization on an entire small-field, small-flux parameter neighborhood, with an explicit limiting gap. The scalar expansion, fixed-flux disk limit and compact-cylinder hyperbolic formulas are established prior results; the contribution considered here is the quantitative general-obstacle transition and its consequences.

## 1. Introduction and main theorem

The planar exterior Steklov problem has a zero eigenvalue represented by a constant harmonic function, which is not square-integrable in the exterior. Adding either a positive scalar potential or a constant magnetic field selects square-integrable extensions. Removing these regularizations is a singular perturbation, with logarithmic rather than ordinary power-series behavior.

Christiansen and Datchev [CD], Theorem 4, established the nonmagnetic shifted-logarithmic Dirichlet-to-Neumann expansion for planar obstacles. Their final Proposition 4.2 gives a lowest-eigenvalue consequence. Grebenkov and Chaigneau [GC] analyzed scalar exterior Steklov asymptotics and identified capacity and harmonic values at infinity in the coefficients. We do not claim these scalar mechanisms as new.

Helffer and Nicoleau [HN] proved the exterior disk magnetic weak-field limit and obtained disk asymptotics. Their inspected author preprint, Section 6, raises the general-domain weak-field question. Bundrock, Girouard, Grebenkov, Levitin and Polterovich [BGGLP], Remark 1.6, subsequently expected general-domain magnetic convergence and pointed to a diamagnetic compactness argument. Qualitative convergence is therefore already suggested by the literature. Our aim is a quantitative general-obstacle expansion, uniform in the simultaneous scalar and magnetic parameters.

Kachmar and Lotoreichik [KL] proved a magnetic exterior disk comparison in a specified field range under additional geometric and symmetry hypotheses. The consequence here has different scope: all smooth simply connected planar obstacles are allowed, with no symmetry or convexity condition, throughout an obstacle-dependent neighborhood of zero field, zero scalar mass and integral flux. We do not establish a field interval uniform over that class. Colbois, Provenzano and Savo [CPS] proved the classical Aharonov--Bohm Weinstock inequality using conformal energy covariance. We use that covariance as a classical input and prove the transition estimate separately.

The proof separates a single angular mode at an enclosing circle. A uniform special-function estimate gives its logarithmic coefficient. An elementary variational argument bounds every other angular mode at once. A classical bounded-region Dirichlet-to-Neumann estimate and a Schur complement transfer this information to the obstacle. Exact harmonic identities remove the enclosing radius and identify the capacity shift.

The small-flux extension is developed in Section 10. The fixed nonzero-flux disk estimate in [HN], Theorem 5.1, has an error of order $b^{|\nu|}$ and does not control the regime $\nu\asymp1/|\log b|$. Our effective operator retains the bounded-region flux dependence and isolates the singular scalar coefficient. The hyperbolic form itself has classical compact-cylinder antecedents: see [PS], Theorem 11, and [CS], Examples 2.2--2.3. Neither those formulas nor the Kummer connection identity [DLMF] is claimed as new.

### 1.1. Notation and statement

Let $K$ be the closure of a nonempty bounded smooth planar obstacle, with finitely many boundary components and connected exterior $E=\mathbb R^2\setminus K$. Put $\Gamma=\partial K$ and $L=|\Gamma|$. Fix the symmetric potential $A(x)=(-x_2,x_1)$, so that $\operatorname{curl}(bA)=2b$. No fixed Aharonov–Bohm flux is included. For $b,p\geq0$, $b+p>0$, define the exterior DtN operator $\Lambda_{b,p}$ by minimizing

$$q_{b,p}(u)=\int_E\bigl(|(\nabla-ibA)u|^2+p|u|^2\bigr)\,dx$$

with prescribed boundary trace and the finite magnetic-energy, square-integrable condition at infinity. Its conormal is $\partial_\nu-ibA\cdot\nu$, with $\nu$ pointing out of $E$ into $K$. At $(b,p)=(0,0)$ use the bounded harmonic extension, and denote its DtN operator by $\Lambda_0$. Its kernel consists of the constants and its other eigenvalues are positive.

Let $G$ be the exterior Green function with pole at infinity, normalized by

$$G|_\Gamma=0,\qquad G(x)=\log|x|-\log c+O(|x|^{-1}),$$

where $c=\operatorname{cap}(K)$ is logarithmic capacity. Define

$$\omega=-\frac1{2\pi}\partial_\nu G\big|_\Gamma,\qquad \int_\Gamma\omega\,ds=1.$$

Thus $\omega$ is the harmonic-measure density at infinity. Use the inner product $\langle f,g\rangle=\int_\Gamma\overline f g\,ds$ and $(\omega\otimes\omega)f=\omega\langle\omega,f\rangle$.

For $b>0$, put

$$\mathcal D_c(b,p)=\log(1/b)-\psi\!\left(\frac12+\frac{p}{4b}\right)-2\gamma-2\log c,$$

where $\psi$ is the digamma function and $\gamma$ is Euler's constant. On the scalar axis set

$$\mathcal D_c(0,p)=\log(4/p)-2\gamma-2\log c.$$

Write $\rho=b+p$. **Theorem 1.1 (uniform threshold expansion).** There are constants $C_K>0$ and $\rho_K>0$ such that for $0<\rho=b+p<\rho_K$, the following difference, initially defined on $H^1(\Gamma)$, extends to a bounded operator on $L^2(\Gamma)$:

$$\Lambda_{b,p}=\Lambda_0+\frac{4\pi}{\mathcal D_c(b,p)}\omega\otimes\omega+\mathcal R_{b,p},\qquad
\|\mathcal R_{b,p}\|_{L^2(\Gamma)\to L^2(\Gamma)}\leq C_K\sqrt\rho.\tag{1}$$

The estimate is uniform as $\rho\downarrow0$, including $p/b\to0$, finite positive ratios, and $p/b\to\infty$. Fixed units of length are understood; a simultaneous rescaling replaces $b,p$ by their inverse-square scalings and $c$ by its length scaling, leaving the denominator invariant.

At $p=0$ the denominator is $\log(1/b)+\log4-\gamma-2\log c$. The scalar axis is already covered by Christiansen–Datchev's stronger nonmagnetic expansion. The result here concerns the magnetic extension, the uniform transition, and its consequences. The obstacle is fixed throughout; constants may depend on its geometry.

Only the bounded difference in (1) has an $L^2$ operator norm. The individual Dirichlet-to-Neumann maps are unbounded self-adjoint operators with common domain $H^1(\Gamma)$. The theorem includes finitely many obstacle components. It assumes a constant magnetic field and no fixed Aharonov--Bohm flux; it makes no claim for arbitrary variable fields or higher dimensions.

**Corollary 1.2 (all eigenvalues and sharp norm).** Set $\tau=4\pi/\mathcal D_c(b,p)$ and $H(\tau)=\Lambda_0+\tau\omega\otimes\omega$. If eigenvalues are indexed from zero, repeated according to multiplicity, then

$$\sup_{j\geq0}|\lambda_j(\Lambda_{b,p})-\lambda_j(H(\tau))|\leq C_K\sqrt\rho,$$

and

$$\left|\|\Lambda_{b,p}-\Lambda_0\|_{L^2\to L^2}-\tau\|\omega\|_{L^2}^2\right|\leq C_K\sqrt\rho.$$

Theorem 1.1 is proved in Sections 2--6. Corollary 1.2 and the fixed-cluster and lowest-eigenvalue expansions are proved in Section 7. Section 8 gives the disk comparison.

**Theorem 1.3 (geometric comparison across the flux transition).** Suppose additionally that $K$ is simply connected, is not a disk and contains zero in its interior. For the potential $bA+\nu(-x_2,x_1)/|x|^2$, let $\lambda_0(b,p,\nu;K)$ be the lowest exterior DtN eigenvalue, and let $D$ be the disk centered at zero with perimeter $L$. There are constants $C_K,\rho_K,\nu_K>0$ such that

$$\lambda_0(b,p,\nu;D)-\lambda_0(b,p,\nu;K)
\geq C_K\left(|\nu|+\frac1{\log(1/(b+p))}\right)^2$$

for every $b,p\geq0$ with $0<b+p<\rho_K$ and every $|\nu|<\nu_K$. There is no restriction on the product $\nu\log(1/(b+p))$. The constants may depend on the obstacle. Section 11 proves this statement and computes the second-order limiting gap; Section 10 supplies the uniform operator approximation on which it rests.



## 2. The exterior realization

Let $D_b=\nabla-ibA$ and

$$X_b(E)=\{u\in L^2(E):D_bu\in L^2(E)\}.$$

This is a Hilbert space with its graph norm. On every bounded collar of the boundary it is contained continuously in $H^1$, because $A$ is bounded there. Thus its trace is defined. Every $f\in H^{1/2}(\Gamma)$ has a compactly supported $H^1$ extension belonging to $X_b(E)$.

For a zero-trace $v\in X_b(E)$, extend by zero into the obstacle. The full-plane magnetic identity, first for compactly supported smooth functions and then by density, gives

$$\|D_bv\|_{L^2(E)}^2\geq2b\|v\|_{L^2(E)}^2.$$

This is the lowest Landau-level inequality, also obtainable by completing the square in the two covariant derivatives. For $b=0$, the added scalar term supplies the lower bound $p\|v\|^2$. Consequently, whenever $b+p>0$, the form $q_{b,p}$ defined in Section 1 is coercive on the zero-trace space in its graph norm. Lax–Milgram applied after subtracting a compactly supported extension produces a unique energy-minimizing extension of each boundary datum. Coercivity need not be uniform as $b+p\to0$ for this existence statement.

The boundary form has domain exactly $H^{1/2}(\Gamma)$ and is closed. Here is a useful verification that does not assume global control of the unweighted gradient. On a fixed connected collar region $U=B_R\setminus K$, the anchored Poincaré inequality gives

$$\||u|\|_{L^2(U)}\leq C\bigl(\|\nabla|u|\|_{L^2(U)}+\|u|_\Gamma\|_{L^2(\Gamma)}\bigr).$$

The diamagnetic inequality bounds its gradient term by $\|D_bu\|$. Since $A$ is bounded on $U$, the local $H^1$ norm of $u$ is controlled by $q_{b,p}(u)^{1/2}+\|f\|_{L^2(\Gamma)}$, uniformly for bounded small $b$. The trace theorem then bounds $\|f\|_{H^{1/2}}$ by the same quantity. In the other direction a compactly supported extension bounds the minimum energy by $C\|f\|_{H^{1/2}}^2$. Thus the boundary-form norm is equivalent to $H^{1/2}$, and the representation theorem yields a nonnegative self-adjoint operator with compact resolvent.

At zero field and zero scalar parameter, inversion about a point inside $K$ changes the exterior into a bounded smooth domain with one interior point removed. Filling that point and solving the ordinary Dirichlet problem gives the harmonic extension bounded near infinity. In two dimensions the Dirichlet integral is conformally invariant. The solution is unique: a harmonic function of finite energy has no logarithmic or negative-power singular part at the filled point, and a zero-trace difference is zero by the bounded-domain uniqueness theorem. This constructs the zero-parameter form and gives its one-dimensional constant kernel. It also works when the obstacle has several components.

For smooth data, Green's formula gives precisely the conormal $\partial_\nu-ibA\cdot\nu$. The two outward conormals at the enclosing circle have opposite orientations, so their sum vanishes when two solutions are glued. The matching equation in Section 5 therefore uses the sum of the two Dirichlet-to-Neumann maps. Conversely, the matching equation makes the glued solution weakly harmonic and finite-energy, so uniqueness identifies it with the minimizing extension. Density extends this identity to the trace form domain.

## 3. The uniform radial logarithm

First take an enclosing circle of radius $R$, and assume $b>0$. The zero angular mode of the exterior equation is

$$-u''-r^{-1}u'+(b^2r^2+p)u=0.$$

Set $z=br^2$ and $a=\tfrac12+p/(4b)$. Direct substitution gives the decaying solution

$$u(r)=e^{-z/2}U(a,1,z),$$

up to a positive constant. Only the integral representation is needed:

$$I(a,z):=\Gamma(a)U(a,1,z)=\int_0^\infty e^{-zt}\left(\frac{t}{1+t}\right)^a\frac{dt}{t}.$$

**Lemma 3.1 (the radial mode).** The expansion (6) below holds uniformly for $b,p\geq0$, $0<b+p\ll1$.

*Proof.* We establish estimates uniform for $a\geq1/2$ and $\eta=az\downarrow0$. Let $w_a(t)=(t/(1+t))^a$. The identity

$$\int_0^\infty\left(w_a(t)-\boldsymbol1_{[a,\infty)}(t)\right)\frac{dt}{t}=\log a-\psi(a)-\gamma\tag{2}$$

follows by substituting $s=t/(1+t)$ in the truncated integral and using the digamma integral

$$\psi(a)+\gamma=\int_0^1\frac{1-s^{a-1}}{1-s}\,ds.$$

Indeed, the truncated integral of $w_a(t)/t$, minus $\log M$, tends to $-\psi(a)-\gamma$ as $M\to\infty$; subtracting the reference step beginning at $a$ adds $\log a$.

For $t\geq a$, $0\leq1-w_a(t)\leq a/t$, since $1-e^{-a\log(1+1/t)}\leq a/t$. On $(0,a)$ simply use $0\leq w_a\leq1$. Therefore

$$\int_0^\infty |e^{-zt}-1|\left|w_a(t)-\boldsymbol1_{[a,\infty)}(t)\right|\frac{dt}{t}
\leq C\eta(1+|\log\eta|).\tag{3}$$

To check the bound, integrate $z$ on $(0,a)$, $za/t$ on $(a,1/z)$, and $a/t^2$ on $(1/z,\infty)$. All constants are independent of $a$. The exponential integral satisfies $E_1(\eta)=-\log\eta-\gamma+O(\eta)$. Combining this with (2)–(3),

$$I(a,z)=D(a,z)+O\bigl(\eta(1+|\log\eta|)\bigr),\qquad
D(a,z)=-\log z-\psi(a)-2\gamma.\tag{4}$$

Also, with differentiation at fixed $a$,

$$J(a,z):=-z\partial_z I(a,z)=\int_0^\infty z e^{-zt}w_a(t)\,dt
=1+O\bigl(\eta(1+|\log\eta|)\bigr).\tag{5}$$

For (5), subtract the integral of $ze^{-zt}$ and split at $a$; the error is at most $\eta+\eta E_1(\eta)$. Since $\psi(a)-\log a$ is bounded for $a\geq1/2$, $D=\log(1/\eta)+O(1)$ uniformly. In particular the denominator is positive for sufficiently small $\eta$.

At $r=R$, $\eta=R^2(b/2+p/4)$ is comparable to $\rho$. The radial DtN eigenvalue is

$$t_{b,p}(R)=-\frac{u'(R)}{u(R)}=\frac{z}{R}+\frac{2J(a,z)}{RI(a,z)}
=\frac{2}{R\mathcal D_R(b,p)}+O_R(\rho).\tag{6}$$

The error is $O(\rho)$, not merely a fixed-$a$ expansion: divide the errors in (4)–(5) by $D$ or $D^2$ and use $D\asymp\log(1/\rho)$. This is the step that permits an unbounded ratio $p/b$.

On $b=0$, the decaying radial solution is $K_0(\sqrt p\,r)$; its elementary small-argument expansion gives exactly (6), with the scalar definition of $\mathcal D_R$. It can also be obtained from the integral above by $a\to\infty$, $az\to pR^2/4$. No limit through fixed $a$ is being used.

This proves the radial-mode estimate. $\square$

## 4. A bound for all nonconstant circle modes

Rescale to $R=1$ for this paragraph. The rescaled parameters are $bR^2,pR^2$, and DtN eigenvalues scale by $R^{-1}$. For an integer $n\ne0$, put $k=|n|$ and let $\mu_n(b,p)$ be the infimum, with $v(1)=1$, of

$$\int_1^\infty\left(|v'|^2+\left(\frac n r-br\right)^2|v|^2+p|v|^2\right)r\,dr.$$

**Lemma 4.1 (nonconstant modes).**

$$\sup_{n\ne0}|\mu_n(b,p)-|n||\leq C\sqrt\rho.\tag{7}$$

*Proof.* Choose $T=\rho^{-1/4}\geq2$. On $[1,T]$,

$$\left(\frac n r-br\right)^2+p\geq\left(1-\frac{2bT^2}{k}\right)\frac{k^2}{r^2}.$$

The coefficient is positive for sufficiently small $\rho$ and at most one. Discarding the nonnegative exterior energy and using the free-end minimum on $[1,T]$ yields

$$\mu_n(b,p)\geq\left(1-\frac{2bT^2}{k}\right)k\tanh(k\log T)
\geq k-2kT^{-2k}-2bT^2\geq k-C\sqrt\rho.$$

The free-end minimizer used here is $(r^{-k}+T^{-2k}r^k)/(1+T^{-2k})$; its energy is the boundary derivative $-v'(1)$, namely $k(1-T^{-2k})/(1+T^{-2k})$. This argument includes both signs of $n$; it bounds the unfavorable sign of the cross term by its absolute value.

For the upper bound, take $v=\chi(r/T)r^{-k}$, where $\chi$ is one up to $1$ and zero beyond $2$. Integration by parts against the harmonic function $r^{-k}$ gives

$$\int_1^\infty\left(|v'|^2+\frac{k^2}{r^2}|v|^2\right)r\,dr
=k+\int_T^{2T}|\partial_r\chi(r/T)|^2r^{1-2k}\,dr\leq k+CT^{-2k}.$$

The absolute cross term is bounded by $2bk\int_1^{2T}r^{1-2k}dr$, which is at most $Cb\log(2T)$ uniformly over $k\geq1$. The mass term is at most $Cp\log(2T)$, and the quadratic magnetic term is at most $Cb^2T^2$. Hence

$$\mu_n(b,p)\leq k+C\{T^{-2}+\rho\log(2T)+b^2T^2\}\leq k+C\sqrt\rho.$$

This proves (7). It is weaker than the one-parameter disk estimate in [HN], but uniform in the joint limit and proved without differentiating a large-order special-function remainder. $\square$

Let $T_{b,p}$ denote the outer-circle DtN operator, $T_0=|D_\theta|/R$, and $\Pi=e\otimes e$ with $e=(2\pi R)^{-1/2}$. Equations (6)–(7) give

$$T_{b,p}=T_0+t\Pi+F_{b,p},\qquad t=\frac2{R\mathcal D_R(b,p)},\qquad
\|F_{b,p}\|_{L^2\to L^2}\leq C_R\sqrt\rho.\tag{8}$$

Only the difference is bounded; each DtN operator itself has order one.

## 5. Bounded-region perturbation and matching

**Lemma 5.1 (bounded-region perturbation).** Let $V$ be a fixed smooth bounded domain with finitely many boundary components, and let $M_{b,p}$ be its magnetic/Helmholtz DtN operator for the same smooth potential. For parameters in a neighborhood of zero small enough that the Dirichlet realization remains invertible,

$$M_{b,p}-M_{0,0}\in\Psi^0(\partial V),\qquad
\|M_{b,p}-M_{0,0}\|_{L^2(\partial V)\to L^2(\partial V)}\leq C_V(|b|+|p|).\tag{9}$$

*Proof.* Here $\Psi^0$ is the usual class of pseudodifferential operators of order zero. This is a classical parameter consequence, not a new microlocal theorem.

We record the parameter dependence explicitly. Smooth-boundary elliptic theory constructs the Poisson operator and the DtN operator, whose degree-one symbol is $|\xi|$ in the induced boundary metric. The magnetic and scalar coefficients occur only in the lower-degree symbols. The factorization and recursive formulas in [LT], Propositions 3.1–3.2 and equations (3.3)–(3.11), show this directly. Their convention is $(-i\nabla+A)^2$; set their potential equal to $-bA$ and their electric potential equal to $p$.

Every finite stage of this construction depends smoothly on $(b,p)$ with bounds in the relevant symbol seminorms. The same assertion holds for the exact smoothing correction: the Dirichlet inverse on the fixed space $H^2(V)\cap H_0^1(V)$ is a smooth family, by the resolvent identity and a Neumann series around the invertible Dirichlet Laplacian. Composing it with the smooth parametrix error gives a smooth family of smooth kernels. One may use a finite-order parametrix of sufficiently negative remainder order to bound the finitely many seminorms needed below; no uniform convergence of a formal full-symbol series is assumed.

Differentiate along the segment $(tb,tp)$, $0\leq t\leq1$. The degree-one symbol is independent of $t$, so the derivative is order zero. Its required symbol seminorms and smoothing-kernel bounds are at most $C(|b|+|p|)$. The $L^2$ boundedness theorem for order-zero operators and the fundamental theorem of calculus give (9). Merely observing that each individual difference is order zero, without this parameter argument, would not justify the rate.

For any fixed region with an inner boundary $\Gamma$ and a disjoint outer boundary $\Sigma$, the off-diagonal block $B_{b,p}$ is smoothing: its two arguments lie on disjoint boundary components, away from the diagonal singularity of the DtN kernel. Its adjoint is smoothing as well, and both are uniformly bounded on $L^2$. Their differences satisfy (9). $\square$

[Gr], Theorems 11.11, 11.14 and 11.16, with (11.55) and (11.65a), supply the smooth-boundary Dirichlet realization, Poisson mappings and ellipticity used here. Only the elliptic realization, symbol construction and Poisson calculus are used here; no heat-coefficient formula is needed.

### Matching on an enclosing circle

Choose $R$ so that $K$ is strictly inside $B_R$, and set $U=B_R\setminus K$, $\Sigma=\partial B_R$. Write the bounded-region magnetic/Helmholtz DtN operator in blocks,

$$M_{b,p}=\begin{pmatrix} A_{b,p}&B_{b,p}\\ B_{b,p}^*&C_{b,p}\end{pmatrix},$$

where the first boundary is $\Gamma$, the second is $\Sigma$, and all normals are outward from $U$. The notation $A_{b,p}$ in this block matrix does not denote the vector potential. Conservation of conormal derivatives at $\Sigma$ gives the exact Schur formula

$$\Lambda_{b,p}=A_{b,p}-B_{b,p}(C_{b,p}+T_{b,p})^{-1}B_{b,p}^*.\tag{10}$$

For smooth data the outer trace $g$ solves $(C_{b,p}+T_{b,p})g=-B_{b,p}^*f$. The finite-energy realization in Section 2 and elliptic regularity justify gluing and extension to the form domain. The energy formulation fixes the sign of $T_{b,p}$ in the sum.

Put $K_0=C_0+T_0$ and retain $t=2/(R\mathcal D_R)$, $\Pi=e\otimes e$ from (8). The operator $K_0$ is self-adjoint elliptic of order one, with principal symbol $2|\xi|$. It is nonnegative and has no kernel: zero energy would force the annular extension, with zero data on $\Gamma$, to be constant and hence zero. Compactness of the boundary and elliptic regularity give a positive lower spectral bound and a bounded inverse $L^2(\Sigma)\to H^1(\Sigma)$.

By (8) and Lemma 5.1,

$$C_{b,p}+T_{b,p}=K_0+t\Pi+E_{b,p},\qquad
\|E_{b,p}\|_{L^2\to L^2}\leq C\sqrt\rho.\tag{11}$$

For sufficiently small $\rho$, $t>0$. Thus $(K_0+t\Pi)^{-1}$ is uniformly bounded on $L^2$. The inverse identity, or a Neumann series after multiplication by this inverse, gives

$$\|(C_{b,p}+T_{b,p})^{-1}-(K_0+t\Pi)^{-1}\|_{L^2\to L^2}
\leq C\sqrt\rho.$$

Apply Lemma 5.1 to the diagonal block $A_{b,p}$ and the smoothing blocks $B_{b,p},B_{b,p}^*$. Substitution in (10) and the rank-one inverse formula yield

$$\Lambda_{b,p}=\Lambda_0+\frac{t}{1+t\kappa}v\otimes v
+O_{L^2\to L^2}(\sqrt\rho),\tag{12}$$

where $\kappa=\langle e,K_0^{-1}e\rangle$ and $v=B_0K_0^{-1}e$. The sign of the rank-one term is positive because the inverse appears with a minus sign in (10).

The diagonal block $A_{b,p}$ has elliptic order one. The Schur correction in (10) is smoothing on $\Gamma$: for every $m>0$, its right off-diagonal block maps $H^{-m}(\Gamma)$ to $L^2(\Sigma)$, the middle inverse is bounded on $L^2(\Sigma)$, and its left off-diagonal block maps $L^2(\Sigma)$ to $H^m(\Gamma)$. Therefore the form realization in Section 2 has domain $H^1(\Gamma)$. All operator differences above can first be taken on that common domain and then extended to $L^2$.


## 6. Capacity and cancellation of the enclosing radius

Let $g=G|_\Sigma$. The exterior harmonic expansion of $G$ is its logarithm plus decaying modes, so

$$\partial_rG|_\Sigma=R^{-1}-T_0g.$$

The annular solution with boundary data $(0,g)$ is $G|_U$, whence $C_0g=R^{-1}-T_0g$, or $K_0g=R^{-1}$. It follows that

$$K_0^{-1}e=\sqrt{\frac R{2\pi}}g,\qquad
\kappa=R\log(R/c),\qquad
v=-\sqrt{2\pi R}\,\omega.\tag{13}$$

For the middle identity use the mean of $G$ on $\Sigma$, which is exactly $\log(R/c)$. For the last identity use the inner conormal of $G$ and the definition of $\omega$. These formulas hold also for several obstacle components.

Substitution into (12) yields

$$\frac{t}{1+t\kappa}v\otimes v
=\frac{4\pi}{\mathcal D_R(b,p)+2\log(R/c)}\omega\otimes\omega
=\frac{4\pi}{\mathcal D_c(b,p)}\omega\otimes\omega.$$

This proves Theorem 1.1. In particular the artificial radius cancels exactly, including the constant inside the logarithm.

## 7. Spectral consequences

*Proof of Corollary 1.2.* Both operators have common domain $H^1$ and their difference is self-adjoint and bounded by $C_K\sqrt\rho$. The min--max principle gives the all-index eigenvalue bound. The norm of the rank-one operator $\tau\omega\otimes\omega$ is $\tau\|\omega\|^2$; the reverse triangle inequality gives the stated norm estimate. $\square$

The same bounded-difference estimate and the resolvent identity give

$$\|(\Lambda_{b,p}+1)^{-1}-(H(\tau)+1)^{-1}\|_{L^2\to L^2}\leq C_K\sqrt\rho.\tag{14}$$

Both resolvents have norm at most one. Thus the convergence is in norm resolvent as well as in the stronger norm of bounded differences after the effective correction.

For every isolated finite spectral cluster of $\Lambda_0$, the self-adjoint analytic family $H(\tau)$ has real-analytic eigenvalue branches near $\tau=0$. One may obtain this by the Riesz projection onto the cluster and analytic identification of its finite-dimensional range with the unperturbed eigenspace, followed by analytic diagonalization of a one-real-parameter Hermitian matrix. Every fixed cluster therefore has a convergent power series in $\tau$. The comparison error is smaller than every inverse-logarithmic order, since $\mathcal D_c=\log(1/\rho)+O_K(1)$ uniformly and $\sqrt\rho=o(|\log\rho|^{-N})$ for every fixed $N$.

At a multiple eigenvalue the first correction is the compression of $\omega\otimes\omega$ to the entire eigenspace. It is not given by arbitrary basiswise diagonal entries. The all-index estimate in Corollary 1.2 does not assert a radius of convergence uniform across clusters.

**Proposition 7.1 (second-order ground state).** Write $e_0=L^{-1/2}$, $\eta_0=\omega-L^{-1}$ and

$$S_K=\langle\eta_0,(\Lambda_0|_{e_0^\perp})^{-1}\eta_0\rangle\geq0.$$

Then, uniformly as $b+p\to0$,

$$\lambda_0(b,p;K)=\frac{\tau}{L}-\frac{\tau^2 S_K}{L}+O_K(\tau^3)+O_K(\sqrt\rho).\tag{15}$$

*Proof.* The zero eigenvalue of $\Lambda_0$ is simple. Normalize its analytic eigenvector branch $u(\tau)$ by $\langle e_0,u(\tau)\rangle=1$. With $V=\omega\otimes\omega$, the first derivative of $H(\tau)u(\tau)=\lambda(\tau)u(\tau)$ at zero gives

$$\lambda'(0)=\langle e_0,Ve_0\rangle=L^{-1},\qquad
u_1:=u'(0)=-L^{-1/2}(\Lambda_0|_{e_0^\perp})^{-1}\eta_0.$$

The coefficient of $\tau^2$ in the eigenvalue is $\langle e_0,Vu_1\rangle=-S_K/L$. Analyticity controls the third-order remainder for this fixed obstacle, and Corollary 1.2 transfers the expansion to $\Lambda_{b,p}$. $\square$


## 8. A disk comparison without symmetry assumptions

**Theorem 8.1 (eventual disk comparison).** Let $K=\overline\Omega$, where $\Omega$ is smooth, bounded and simply connected. Let $D$ be a disk of the same perimeter $L$, with radius $r_*=L/(2\pi)$. Set $\ell=\log(1/(b+p))$. Then

$$\lim_{\substack{b,p\geq0\\b+p\downarrow0}}
\ell^2\bigl(\lambda_0(b,p;D)-\lambda_0(b,p;K)\bigr)
=\frac{8\pi}{L}\log\frac{r_*}{c}+\frac{16\pi^2}{L}S_K.\tag{16}$$

The limit is uniform in the ratio of the parameters. Its right side is strictly positive unless $\Omega$ is a disk. In particular, for every fixed nondisk there is $\rho_\Omega>0$ such that the disk has strictly larger lowest eigenvalue whenever $b,p\geq0$ and $0<b+p<\rho_\Omega$.

*Proof.* The classical strict capacity--perimeter inequality is

$$c\leq r_*,\qquad c=r_*\ \Longleftrightarrow\ \Omega\text{ is a disk}.\tag{17}$$

Here is a proof including equality. The exterior conformal map has expansion $F(z)=cz+a_0+\sum_{n\geq1}a_nz^{-n}$ with $c>0$. Smoothness gives its boundary derivative and

$$L=\int_0^{2\pi}|F'(e^{i\theta})|\,d\theta\geq\left|\int_0^{2\pi}F'(e^{i\theta})\,d\theta\right|=2\pi c.$$

Equality forces $F'$ to be nonnegative real on the boundary. Its imaginary part is harmonic in the compactified exterior and vanishes on the boundary, so it vanishes everywhere. A holomorphic real-valued function is constant. Therefore $F'=c$ and the obstacle is a disk.

For a disk of radius $r_*$, $\omega=L^{-1}$, hence $S_D=0$. The denominators for the two obstacles satisfy the exact relation

$$\mathcal D_c(b,p)=\mathcal D_{r_*}(b,p)+2\log(r_*/c).$$

The proof of Lemma 3.1 gives $\mathcal D_c=\ell+O_K(1)$ uniformly, because $az$ is comparable to $b+p$ and $\psi(a)-\log a$ is bounded for $a\geq1/2$. The scalar axis has the same property directly. In particular $\ell^2/\mathcal D_c^2\to1$ and $\ell^2/(\mathcal D_c\mathcal D_{r_*})\to1$ uniformly.

Apply Proposition 7.1 to the two obstacles and use the exact denominator difference. Their leading-term difference is

$$\frac{4\pi}{L}\left(\frac1{\mathcal D_{r_*}}-\frac1{\mathcal D_c}\right)
=\frac{8\pi\log(r_*/c)}{L\mathcal D_{r_*}\mathcal D_c}.$$

The second-order term contributes $16\pi^2S_K/(L\mathcal D_c^2)$. Both the cubic inverse-logarithmic remainder and $\sqrt\rho$ disappear after multiplication by $\ell^2$. This proves (16). Strict positivity follows from (17) and $S_K\geq0$. $\square$

Taking $p=0$ gives the magnetic geometric consequence. No convexity, central symmetry, two-axis symmetry or outer-parallel-curve condition is imposed. This is a shape-dependent eventual comparison, not a uniform field-range result for all smooth obstacles. The magnetic-field parameter in [KL] corresponds to $2b$ here. The theorem does not extend the perimeter conclusion to disconnected obstacles: their capacity can grow with separation at fixed total perimeter.


## 9. Scope and further questions

The uniform transition isolates how the scalar mass and the constant field select the same harmonic-measure direction, with different logarithmic constants. The scalar axis belongs to the established theory [CD, GC], and the disk magnetic specialization is consistent with [HN]. In the magnetic case $p=0$, the denominator is $\log(1/b)+\log4-\gamma-2\log c$. For a disk of radius $c$, the effective ground-state value $2/(c\mathcal D_c)$ agrees with the small-field expansion of the exact radial eigenvalue $bcK_1(bc^2/2)/K_0(bc^2/2)$.

The argument is deliberately insensitive to the sharper algebraic remainders of individual circle modes. Improving the remainder while retaining uniformity over both parameters and angular indices, obtaining quantitative stability with a field interval uniform over a geometric class, and allowing several independently varying circulations remain separate questions. The next section treats one flux pole, including the transition near integral flux. The qualitative magnetic equivalence in arbitrary dimensions and for general fields, anticipated in [BGGLP], is not settled by the planar constant-field theorem here.

## 10. Uniform transition across integral flux

Let $K$ be a smooth compact planar obstacle with connected exterior $E$, and assume $0\in\operatorname{int}K$. There may be several components; the flux pole is in the component containing zero. On $E$ put

$$A(x)=(-x_2,x_1),\qquad a_0(x)=\frac{(-x_2,x_1)}{|x|^2},\qquad
\mathcal A_{b,\nu}=bA+\nu a_0.$$

The field in $E$ is $2b$, and the additional circulation about the pole is $2\pi\nu$. In this section we consider $b,p\geq0$, $\rho=b+p>0$, and $|\nu|\leq1/4$. The exterior DtN operator for $|\nabla-i\mathcal A_{b,\nu}|^2+p$ is denoted $\Lambda_{b,p,\nu}$. It uses square-integrable finite magnetic-energy extensions for $\rho>0$.



### 10.1. The radial coefficient and its uniform remainder

Fix an enclosing circle $\Sigma=\partial B_R$. For $b>0$ put

$$a=\frac12+\frac{p}{4b},\qquad z=bR^2,\qquad \eta=az=R^2\left(\frac b2+\frac p4\right).$$

For $\nu\neq0$, define

$$d_\nu(a,z)=-\log z-
\frac{\log\Gamma(1-\nu)-\log\Gamma(1+\nu)+\log\Gamma(a+\nu)-\log\Gamma(a)}{\nu}.\tag{F1}$$

All gamma arguments in the logarithms are positive. The continuous definition at $\nu=0$ is

$$d_0(a,z)=-\log z-2\gamma-\psi(a).$$

For $b=0,p>0$, use

$$d_\nu(0,p;R)=\log\frac4{pR^2}
-\frac{\log\Gamma(1-\nu)-\log\Gamma(1+\nu)}{\nu},\tag{F2}$$

again continuously at zero. Denote these expressions collectively by $d_\nu(b,p;R)$. Then

$$d_\nu(b,p;R)=\log(1/\rho)+O_R(1)\tag{F3}$$

uniformly for $|\nu|\leq1/4$, including all $p/b$ ratios. To see this on $b>0$, write the last gamma quotient as $\int_0^1\psi(a+t\nu)dt$. Since $a\geq1/2$, $a+t\nu\geq a/2$ and $\psi(a+t\nu)-\log a$ is uniformly bounded. The quotient involving $1\pm\nu$ is bounded on the fixed flux interval. Thus $d_\nu=-\log(az)+O(1)$, and $az\asymp_R\rho$.

For sufficiently small $\rho$, $d_\nu>0$. Define

$$\sigma_{b,p,\nu}(R)=\frac{\nu}{R}\coth\!\left(\frac{\nu d_\nu(b,p;R)}2\right),\qquad
\sigma_{b,p,0}(R)=\frac2{R d_0(b,p;R)}.\tag{F4}$$

This expression is positive even when $\nu<0$. Its dependence on the signed flux is not exactly even, because $d_\nu$ need not equal $d_{-\nu}$ when $b>0$.

**Lemma 10.1 (uniform radial coefficient).** The zero-angular-mode DtN eigenvalue satisfies

$$\mu_0(b,p,\nu;R)=\sigma_{b,p,\nu}(R)+O_R(\rho),\tag{F5}$$

uniformly for $|\nu|\leq1/4$ and all nonnegative parameter ratios.

#### Positive field

The decaying radial solution is

$$u(r)=r^{-\nu}e^{-br^2/2}U(a,1-\nu,br^2).$$

This follows by substituting into

$$-u''-r^{-1}u'+\left(\left(br+\frac\nu r\right)^2+p\right)u=0.$$

For $\nu\neq0$, the classical Kummer connection identity, [DLMF 13.2.42](https://dlmf.nist.gov/13.2.E42), gives exactly

$$U(a,1-\nu,z)=\frac{\Gamma(\nu)}{\Gamma(a+\nu)}\{P_\nu(z)-qQ_\nu(z)\},\tag{F6}$$

where

$$P_\nu=M(a,1-\nu,z),\quad Q_\nu=M(a+\nu,1+\nu,z),\quad
q=\frac{\Gamma(1-\nu)\Gamma(a+\nu)}{\Gamma(1+\nu)\Gamma(a)}z^\nu
=e^{-\nu d_\nu}.$$

The identity itself is prior special-function theory. Uniform control of the cancellation at $\nu=0$ is essential here.

For $a\geq1/2$, $|\nu|\leq1/4$, $\eta=az\leq\eta_0$, the defining power series of $M$ imply

$$|P_\nu-1|+|Q_\nu-1|+|z\partial_zP_\nu|+|z\partial_zQ_\nu|\leq C\eta,\tag{F7}$$

and

$$|P_\nu-Q_\nu|+|z\partial_z(P_\nu-Q_\nu)|\leq C|\nu|\eta.\tag{F8}$$

Here are explicit uniform bounds for this use of the series. Its coefficients are $(\alpha)_jz^j/((c)_j j!)$. Along the required parameter segments $\alpha=a+\theta\nu\geq a/2$, $c\geq3/4$, and

$$\frac{(a+\theta\nu)_j}{a^j(3/4)_j}\leq2^j.$$

Indeed $1+\theta\nu/a+k/a\leq3/2+2k=2(k+3/4)$ termwise. The same bound applies with $\alpha=a$. Differentiating a coefficient with respect to $\nu$ adds sums of reciprocals of $\alpha+k$ or $c+k$, bounded by $Cj$ since $\alpha\geq1/4$ and $c\geq3/4$. Applying $z\partial_z$ adds a factor $j$. The series with these polynomial factors are bounded by $C\eta$ for $j\geq1$. At zero flux $P_0=Q_0$, so integration of the parameter derivative proves (F8). No large-a asymptotic is differentiated without a bound.

Factor the braces in (F6) as

$$P_\nu-qQ_\nu=(1-q)(1+\delta),\qquad
\delta=P_\nu-1+\frac q{1-q}(P_\nu-Q_\nu).$$

The elementary inequalities

$$\frac{|\nu|q}{|1-q|}\leq|\nu|+\frac1{d_\nu},\qquad
\frac{\nu^2q}{(1-q)^2}=\frac{\nu^2}{4\sinh^2(\nu d_\nu/2)}\leq\frac1{d_\nu^2}\tag{F9}$$

control both signs of flux. Differentiate at fixed $a,\nu$; then $z\partial_zq=\nu q$. Equations (F7)–(F9) give

$$|\delta|+|z\partial_z\delta|\leq C\eta.\tag{F10}$$

For the differentiated second term in $\delta$, use (F8) and the second bound of (F9); this avoids an apparent $1/\nu$ singularity. Taking the logarithmic derivative in (F6),

$$-z\frac{\partial_zU}{U}=\frac{\nu q}{1-q}+O(\eta).$$

The constant factor in (F6) and $1-q$ can both be negative when $\nu<0$, but their product is positive; the displayed identity is a real logarithmic derivative of that positive product and does not require a complex logarithm. Therefore

$$-\frac{u'(R)}{u(R)}=\frac\nu R+\frac zR+
\frac{2\nu q}{R(1-q)}+O_R(\eta)
=\frac\nu R\coth\left(\frac{\nu d_\nu}2\right)+O_R(\rho).$$

At $\nu=0$ use continuity of the positive defining integral of $U$ and its derivative for fixed $a,z$. All constants just established are uniform in punctured flux neighborhoods, so (F5) passes to zero flux. This recovers the previous digamma coefficient without a loss in the remainder.

#### Scalar axis

For fixed $p>0$, let $b\downarrow0$. The minimum radial energy converges to the scalar/flux radial energy. A compactly supported radial trial function gives the upper bound, approximating the scalar minimizer by cutoffs. For the lower bound, restrict minimizers to each finite interval. Their energies control local H1 norms and, through the positive p term, global weighted L2 norms. Weak compactness, trace continuity at R and lower semicontinuity on successive finite intervals give an admissible scalar limit with no larger energy. The uniqueness of the scalar minimum identifies the limit. The pointwise potentials are nonnegative, so discarding the exterior interval in this argument is legitimate.

Also $\log\Gamma(a+\nu)-\log\Gamma(a)=\nu\log a+O(|\nu|/a)$ uniformly in the fixed flux interval, with the quotient at zero understood by the digamma integral. As $b\to0$, $az\to pR^2/4$, so (F1) tends to (F2). Passing to the limit in the uniform estimate (F5) gives its scalar-axis version. This agrees with the solution $K_{|\nu|}(\sqrt p\,r)$ and does not assume a uniformity that was proved only at fixed nonzero flux.

### 10.2. The other circle modes

For $n\neq0$, put $k=|n-\nu|\geq3/4$. Rescale to $R=1$ and choose $T=\rho^{-1/4}$. The radial energy is

$$\int_1^\infty\left(|v'|^2+\left(\frac{n-\nu}r-br\right)^2|v|^2+p|v|^2\right)r\,dr.$$

The free-end argument of Section 4 works with the real exponent k:

$$\mu_n\geq k-2kT^{-2k}-2bT^2\geq k-C\rho^{3/8}.$$

For the upper bound use $v=\chi(r/T)r^{-k}$. Its unperturbed energy is $k+O(T^{-2k})$. The cross and mass terms are bounded uniformly by $C\rho T^{1/2}\log(2T)$; for $k\geq1$ this is a deliberately loose bound, and for $3/4\leq k\leq1$ it follows by bounding the integral of $r^{1-2k}$. The quadratic magnetic term is at most $Cb^2T^{5/2}$. Each is $O(\rho^{3/8})$. Thus

$$\sup_{n\neq0}\left|\mu_n(b,p,\nu;R)-\frac{|n-\nu|}{R}\right|\leq C_R\rho^{3/8}.\tag{F11}$$

Define $S_\nu$ on the circle to have Fourier eigenvalue $|n-\nu|/R$ for $n\neq0$ and zero for $n=0$. Unlike the complete $|D_\theta-\nu|/R$, this family is analytic at $\nu=0$: its nonzero eigenvalues are $(|n|-\nu\operatorname{sgn}n)/R$. With $e=(2\pi R)^{-1/2}$ and $\Pi=e\otimes e$, (F5) and (F11) imply

$$T_{b,p,\nu}=S_\nu+\sigma_{b,p,\nu}(R)\Pi+F_{b,p,\nu},\qquad
\|F_{b,p,\nu}\|_{L^2\to L^2}\leq C_R\rho^{3/8}.\tag{F12}$$

The exponent $3/8$ is a convenient uniform bound on the chosen flux interval. It is not claimed sharp.

### 10.3. The general-obstacle effective operator

Use the fixed bounded region $U=B_R\setminus K$ and let

$$M_\nu=\begin{pmatrix}A_\nu&B_\nu\\B_\nu^*&C_\nu\end{pmatrix}$$

be its DtN map for the flat potential $\nu a_0$, with no constant field or scalar mass. This notation for the blocks does not denote the vector potential. The singular pole lies outside the closure of U, so all coefficients on U are smooth. Lemma 5.1 gives

$$\|M_{b,p,\nu}-M_\nu\|_{L^2\to L^2}\leq C\rho\tag{F13}$$

uniformly for $|\nu|\leq1/4$. The principal symbol is independent of all three parameters. The family $M_\nu-M_0$ is real analytic as a bounded operator on $L^2$, and the off-diagonal blocks are smoothing. For this parameter claim, the differential expression is polynomial in $\nu$ on a fixed Dirichlet domain. Its inverse extends holomorphically to a complex neighborhood of each real invertible parameter by a Neumann series. The finite symbol construction in Lemma 5.1 is holomorphic there, with parameter-independent principal symbol. The exact remainder is obtained from that Dirichlet inverse and has the same holomorphic dependence in the finitely many operator norms needed for the $L^2$ bound. This proves the asserted bounded-operator analyticity without assuming convergence of an infinite symbol expansion.

Put

$$K_\nu=C_\nu+S_\nu,\quad
H_\nu=A_\nu-B_\nu K_\nu^{-1}B_\nu^*,\quad
v_\nu=B_\nu K_\nu^{-1}e,\quad
\kappa_\nu=\langle e,K_\nu^{-1}e\rangle.$$

The operator $K_\nu$ is uniformly positive and invertible over the compact flux interval. Its energy is the sum of the bounded-region magnetic energy with zero data on $\Gamma$ and the nonnegative outer form of $S_\nu$. If its energy vanishes, the bounded-region function is covariantly constant and has zero trace on $\Gamma$, hence is zero. Ellipticity, compact resolvent, and continuity in the parameter give the uniform positive lower bound.

For $t\geq0$, define the auxiliary effective operator

$$\mathcal H(\nu,t)=H_\nu+\frac{t}{1+t\kappa_\nu}v_\nu\otimes v_\nu
=A_\nu-B_\nu(K_\nu+t\Pi)^{-1}B_\nu^*.\tag{F14}$$

It is nonnegative, self-adjoint, has common domain $H^1(\Gamma)$ and compact resolvent. Its bounded difference from $\Lambda_0$ is real analytic in $(\nu,t)$ near $(0,0)$. The form interpretation minimizes the bounded-region energy plus the nonnegative form $S_\nu+t\Pi$. Notice that $H_\nu$ must be retained: replacing it by $\Lambda_0$ discards terms of order $\nu$, which matter in the transition regime.

**Theorem 10.3 (uniform flux normal form).** For some $C_K,\rho_K>0$, uniformly for $|\nu|\leq1/4$ and $0<\rho<\rho_K$,

$$\left\|\Lambda_{b,p,\nu}-\mathcal H\bigl(\nu,\sigma_{b,p,\nu}(R)\bigr)\right\|_{L^2\to L^2}
\leq C_K\rho^{3/8}.\tag{F15}$$

*Proof.* The exterior realization for positive $\rho$ is constructed as in Section 2. On zero-trace functions, the lower bound $2b+p$ follows by completing the covariant-derivative square on smooth functions compactly supported in E, where the curl is exactly $2b$, and passing by density. It is not necessary to extend the singular Aharonov–Bohm potential through the pole. Local trace/form estimates use that the potential is bounded on U, uniformly in the chosen parameter window.

The exact conormal matching gives

$$\Lambda_{b,p,\nu}=A_{b,p,\nu}-B_{b,p,\nu}
(C_{b,p,\nu}+T_{b,p,\nu})^{-1}B_{b,p,\nu}^*.$$

By (F12)–(F13), the middle denominator equals $K_\nu+\sigma\Pi+O_{L^2}(\rho^{3/8})$. Since $\sigma>0$, its unperturbed inverse is uniformly bounded. The inverse identity, smoothing off-diagonal bounds and (F13) then give (F15), exactly as in the zero-flux proof. The bounded difference is taken initially on the common $H^1$ domain. This proves the theorem using Lemma 5.1. $\square$

In particular, the error in every ordered eigenvalue is bounded by the same $C_K\rho^{3/8}$. The estimate is uniform through integral flux after the usual integer gauge conjugation. It concerns one specified flux pole, not an arbitrary independently varying vector of circulations about several components.

At zero flux $H_0=\Lambda_0$, $v_0=-\sqrt{2\pi R}\omega$ and $\kappa_0=R\log(R/c)$. Formula (F14) therefore reduces to Theorem 1.1. At a fixed nonzero flux, $\sigma\to|\nu|/R$, and (F14) tends to the DtN operator obtained by matching the exterior decaying flat-flux modes $r^{-|n-\nu|}$. This recovers the appropriate exterior Aharonov–Bohm limit. The algebraic convergence exponent in (F15) concerns approximation by the parameter-dependent effective operator, not convergence to this fixed-flux limit; the latter still contains the slower $\rho^{|\nu|}$ transition through $\sigma$.

A two-parameter real-analytic operator family need not have jointly analytic individual eigenvalues at a multiple eigenvalue. Only its finite-dimensional analytic spectral-cluster matrix, and its simple eigenvalue branches, are asserted analytic. The all-index min–max bound needs no such assertion.

### 10.4. The leading lowest-eigenvalue crossover

Let $L=|\Gamma|$, $\ell=\log(1/\rho)$, and now also let $\nu\to0$. Complex conjugation sends $M_\nu$ to $M_{-\nu}$ and $S_\nu$ to $S_{-\nu}$. The vector e is real. Thus

$$\overline{\mathcal H(\nu,t)}=\mathcal H(-\nu,t),$$

and its simple lowest eigenvalue $h(\nu,t)$ is even in $\nu$ near zero. The first derivatives are

$$\partial_\nu h(0,0)=0,\qquad
\partial_t h(0,0)=|\langle v_0,L^{-1/2}\rangle|^2=\frac{2\pi R}{L}.$$

Analytic perturbation at the isolated simple zero eigenvalue gives

$$h(\nu,t)=\frac{2\pi R}{L}t+O_K((|\nu|+|t|)^2).$$

Since $\sigma=O_R(|\nu|+\ell^{-1})$, the normal form yields

$$\lambda_0(b,p,\nu;K)=\frac{2\pi}{L}\nu\coth\left(\frac{\nu\ell}{2}\right)
+O_K\bigl((|\nu|+\ell^{-1})^2\bigr)+O_K(\rho^{3/8}).\tag{F16}$$

To replace $d_\nu$ by $\ell$, differentiate $\nu\coth(\nu d/2)$ in d. Its derivative has absolute value

$$\frac{\nu^2}{2\sinh^2(\nu d/2)}\leq\frac2{d^2}.$$

Equation (F3) therefore incurs only $O(\ell^{-2})$, uniformly over signed flux. All functions at $\nu=0$ have their continuous values.

**Corollary 10.4 (crossover).** If $\nu\ell\to s\in\mathbb R$, then

$$\ell\lambda_0(b,p,\nu;K)\longrightarrow
\frac{2\pi}{L}s\coth(s/2),\qquad s\coth(s/2)|_{s=0}=2.\tag{F17}$$

The limit is independent of the ratio $p/b$ and of the obstacle except for perimeter. If instead $\nu\to0$ with $|\nu|\ell\to\infty$, (F16) gives $\lambda_0\sim2\pi|\nu|/L$. Thus the logarithmic zero-flux regime and the small-flux Aharonov–Bohm regime are joined by one uniform law. This is not a claim that the full effective operator is independent of shape or that its linear flux correction vanishes.

### 10.5. Signed-flux asymmetry

**Corollary 10.5 (signed-flux asymmetry).** Suppose $b>0$, $\rho\to0$, $\nu\ell\to s\in\mathbb R$, and $p/b\to r\in[0,\infty]$. Write

$$\Psi_r=\psi'\left(\frac12+\frac r4\right)\quad(r<\infty),\qquad\Psi_\infty=0.$$

Then

$$\ell^3\bigl(\lambda_0(b,p,\nu;K)-\lambda_0(b,p,-\nu;K)\bigr)
\longrightarrow \frac{\pi}{L}s^3\operatorname{csch}^2(s/2)\,\Psi_r,\tag{F18}$$

where the continuous value of $s^3\operatorname{csch}^2(s/2)$ at zero is zero. For a pure constant-field regularization, $r=0$ and $\Psi_0=\pi^2/2$. The scalar-dominated limit gives zero at this scale.

*Proof.* The quotient involving $\Gamma(1\pm\nu)$ in (F1) is even in $\nu$. Taylor's theorem applied to the digamma integral gives, uniformly for $a\geq1/2$,

$$d_\nu-d_{-\nu}=-\nu\psi'(a)+O(\nu^3).$$

The bound on the remainder follows from bounded polygamma derivatives on $[1/4,\infty)$. The mean-value theorem in the d argument of (F4) then gives, for some intermediate $d_*=\ell+O(1)$,

$$\sigma_{b,p,\nu}-\sigma_{b,p,-\nu}
=\frac{\nu^3\psi'(a)}{2R}\operatorname{csch}^2(\nu d_*/2)
+O_R\left(\frac{|\nu|^5}{\sinh^2(\nu d_*/2)}\right).\tag{F19}$$

The expression is interpreted continuously at zero. Uniformly when $|\nu|\ell$ is bounded, the last term is $O(|\nu|^3/\ell^2)$, and hence is $o(\ell^{-3})$. Also the leading term in (F19), multiplied by $\ell^3$, tends to $s^3\Psi_r\operatorname{csch}^2(s/2)/(2R)$; continuity at s=0 follows from $x/\sinh x\to1$.

Because $h(\nu,t)=h(-\nu,t)$, the difference of its evaluations at the two actual radial coefficients is

$$h(\nu,\sigma_\nu)-h(-\nu,\sigma_{-\nu})
=\left(\frac{2\pi R}{L}+o(1)\right)(\sigma_\nu-\sigma_{-\nu}).$$

Finally $\ell^3\rho^{3/8}\to0$, so (F15) transfers this relation to the actual lowest eigenvalues and proves (F18). No derivative of the unknown operator remainder is taken. Differentiating a uniform real-parameter error estimate without derivative control would not justify a flux-derivative theorem; the finite signed difference avoids that pitfall. $\square$

The asymmetry is sensitive to how mass and magnetic field vanish, even though the leading crossover (F17) is not.

## 11. The second-order geometric gap across the transition

### 11.1. The flat-flux coefficient and harmonic measure

Assume $K$ is the closure of a smooth bounded simply connected domain containing zero. Set $E=\mathbb R^2\setminus K$, $\Gamma=\partial K$, $L=|\Gamma|$, and $c=\operatorname{cap}(K)$. Let $F:\{|w|>1\}\to E$ be the exterior conformal map normalized by $F(w)=cw+O(1)$ at infinity. Put $m(\theta)=|F'(e^{i\theta})|$. Thus $ds=m(\theta)d\theta$ and $L=\int_0^{2\pi}m(\theta)d\theta$.

The function $F(w)/w$ has a nonvanishing analytic logarithm on the exterior disk, tending to $\log c$ at infinity. Indeed it is nonzero and its winding number on a large circle is zero. Write $\chi=\operatorname{Im}\log(F(w)/w)$. Pulling back the one-form $a_0=d\arg z$ gives $d\theta+d\chi$. Multiplication by $e^{i\nu\chi}$ removes the exact summand, and conformal invariance of two-dimensional magnetic energy gives the exterior flat-flux boundary operator, in $L^2(m\,d\theta)$, as

$$m^{-1}|D_\theta-\nu|.\tag{G1}$$

For nonzero flux, the finite-energy solution uses radial modes $r^{-|n-\nu|}$, not an $L^2$ requirement at infinity. This is precisely the flat limit constructed by circle matching in Section 10. At zero flux its constant mode is the bounded harmonic extension. Thus the use of a conformal map does not change the realization.

Let $P_0$ project onto constants in $L^2(d\theta)$ and put $J e^{in\theta}=\operatorname{sgn}(n)e^{in\theta}$, with $J1=0$. For $0\leq\nu<1/2$,

$$|D_\theta-\nu|=|D_\theta|+\nu(P_0-J).$$

This is an exact affine family, with common domain, self-adjoint in the weighted boundary space after multiplication by $m^{-1}$. Its perturbation is bounded because $m$ is smooth and bounded above and below. The simple zero eigenvalue at $\nu=0$ therefore has an analytic branch from the right.

Recall $\omega=-\partial_{n_E}G/(2\pi)$ and

$$\eta_0=\omega-L^{-1},\qquad S_K=\langle\eta_0,(\Lambda_0|_{1^\perp})^{-1}\eta_0\rangle\geq0.$$

Conformal invariance of harmonic measure gives $\omega(F(e^{i\theta}))=(2\pi m(\theta))^{-1}$. With the normalized constant $e_0=L^{-1/2}$ and $V=m^{-1}(P_0-J)$, one has

$$Ve_0=2\pi L^{-1/2}\omega,\qquad
\langle e_0,Ve_0\rangle=\frac{2\pi}{L},\qquad
(I-e_0\otimes e_0)Ve_0=2\pi L^{-1/2}\eta_0.$$

Differentiate the simple eigenvalue equation with eigenvector normalized by its scalar product with $e_0$. The first eigenvector derivative is $-2\pi L^{-1/2}(\Lambda_0|_{1^\perp})^{-1}\eta_0$. Since the operator family is affine, the quadratic eigenvalue coefficient is the scalar product of this vector with $Ve_0$, namely $-4\pi^2S_K/L$. Consequently

$$\lambda_0^{\mathrm{flat}}(\nu;K)=\frac{2\pi}{L}|\nu|-\frac{4\pi^2}{L}S_K\nu^2+O_K(|\nu|^3).\tag{G2}$$

Conjugation supplies the negative side. The flat-flux calculation is an auxiliary perturbation argument, not a separate novelty claim. Aharonov--Bohm Weinstock inequalities and conformal energy covariance are prior results; see [CPS], Theorem 16 and Appendix C. The exterior formula here also follows directly from the displayed conformal gauge and radial modes.

For an explicit geometric formula, use Fourier coefficients $m_n=(2\pi)^{-1}\int m(\theta)e^{-in\theta}d\theta$. The equation $\Lambda_0g=\eta_0$ becomes

$$|D_\theta|g=\frac1{2\pi}-\frac mL.$$

The nonconstant coefficients of $g$ are $-m_n/(L|n|)$. Choosing the constant coefficient so that $\int gm\,d\theta=0$ and then evaluating $S_K=\int \eta_0g\,ds$ yields

$$S_K=\frac{2\pi}{L^2}\sum_{n\neq0}\frac{|m_n|^2}{|n|}.\tag{G3}$$

The sum converges for smooth $m$. Therefore $S_K=0$ exactly when $m$ is constant. In that case $\log|F'|$ is bounded harmonic on the exterior, has constant boundary value and a removable value at infinity; it is constant. A holomorphic function of constant modulus is constant, so $F'$ is constant and $K$ is a disk. In particular, $S_K>0$ for every nondisk.

### 11.2. Identifying the two-parameter Hessian

Fix an enclosing radius $R$ and write $q=\log(R/c)>0$. The auxiliary analytic ground branch $h(\nu,t)$ of Section 10 is even in $\nu$, so

$$h(\nu,t)=\alpha t+\beta t^2+\gamma\nu^2+O_K((|\nu|+|t|)^3).\tag{G4}$$

At zero flux, the exact capacity identity gives $\tau=2\pi Rt/(1+Rq t)$ and $h(0,t)=\tau/L-\tau^2S_K/L+O(t^3)$. Hence

$$\alpha=\frac{2\pi R}{L},\qquad
\beta=-\frac{2\pi R^2}{L}q-\frac{4\pi^2R^2}{L}S_K.$$

On the positive flat-flux curve $t=\nu/R$, the auxiliary operator is exactly the flat-flux DtN operator. Comparing (G4) to (G2) determines the remaining coefficient:

$$\gamma=\frac{2\pi}{L}q.\tag{G5}$$

No extrapolation from finite diagnostics is involved. The exact flat-flux curve determines a Taylor coefficient of the two-variable analytic family.

### 11.3. Capacity-normalized second-order expansion

For $\rho=b+p>0$, let $\ell=\log(1/\rho)$ and let $d_\nu(b,p;R)$ be the radial denominator of Section 10. Define

$$d_\nu^c=d_\nu(b,p;R)+2\log(R/c),\qquad
X_c=\nu\coth(\nu d_\nu^c/2),\quad X_c|_{\nu=0}=2/d_0^c.\tag{G6}$$

The first expression is independent of $R$, directly from its logarithmic dependence on radius. Write $\varepsilon=|\nu|+\ell^{-1}$. Uniformly over all nonnegative parameter ratios and sufficiently small $\rho$, $d_\nu^c=\ell+O_K(1)$ and $X_c\asymp_K\varepsilon$.

**Theorem 11.1 (second-order transition).** For a fixed smooth simply connected obstacle,

$$\lambda_0(b,p,\nu;K)=\frac{2\pi}{L}X_c-\frac{4\pi^2}{L}S_KX_c^2
+O_K(\varepsilon^3)+O_K(\rho^{3/8}),\tag{G7}$$

uniformly as $\rho\downarrow0$ and $\nu\to0$, without a relation between the two rates.

*Proof.* Put $X_R=\nu\coth(\nu d_\nu(b,p;R)/2)$, so $t=X_R/R$. Substitution in (G4)--(G5) gives

$$h(\nu,X_R/R)=\frac{2\pi}{L}\{X_R+q(\nu^2-X_R^2)\}
-\frac{4\pi^2}{L}S_KX_R^2+O_K(\varepsilon^3).$$

For $f_\nu(d)=\nu\coth(\nu d/2)$ one has

$$f_\nu'(d)=-\frac12\nu^2\operatorname{csch}^2(\nu d/2),\qquad
f_\nu''(d)=\frac12\nu^3\operatorname{csch}^2(\nu d/2)\coth(\nu d/2).$$

On the relevant interval of bounded shifts from $\ell$, $|f_\nu'|\leq C\varepsilon^2$ and $|f_\nu''|\leq C\varepsilon^3$, including their continuous values at zero. Indeed $|\nu\coth(\nu d/2)|\leq |\nu|+2/d$ and $\nu^2\operatorname{csch}^2(\nu d/2)\leq4/d^2$.

Taylor's theorem across the fixed shift $2q$ therefore gives

$$X_c=X_R+q(\nu^2-X_R^2)+O_K(\varepsilon^3),\qquad
X_c^2=X_R^2+O_K(\varepsilon^3).$$

The existing uniform operator theorem supplies the remaining $O_K(\rho^{3/8})$ difference to the actual lowest eigenvalue. This proves (G7). $\square$

### 11.4. Uniform disk comparison

**Theorem 11.2 (uniform eventual disk comparison).** Let $K$ be a fixed nondisk satisfying the assumptions of this section. There are positive constants $\nu_K,\rho_K,C_K$ for which (G9) holds throughout the indicated parameter neighborhood. Furthermore, the distinguished-limit gap is (G10).

*Proof.* Let $D$ be the disk of perimeter $L$, centered at the flux pole, and write $r_*=L/(2\pi)$ and $\delta=\log(r_*/c)$. Capacity--perimeter gives $\delta\geq0$, strictly for a nondisk. The radial denominators satisfy exactly

$$d_\nu^c=d_\nu^{r_*}+2\delta.$$

Since $f_\nu$ is decreasing, $X_{r_*}\geq X_c$ for either sign of flux. For a disk $S_D=0$. Applying (G7) to the two obstacles gives

$$\lambda_0(b,p,\nu;D)-\lambda_0(b,p,\nu;K)
=\frac{2\pi}{L}(X_{r_*}-X_c)+\frac{4\pi^2}{L}S_KX_c^2
+O_K(\varepsilon^3)+O_K(\rho^{3/8}).\tag{G8}$$

If $K$ is not a disk, $S_K>0$ by (G3). Because $X_c\asymp_K\varepsilon$ and $\rho^{3/8}\ell^2\to0$, the right side is bounded below by a positive constant times $\varepsilon^2$ after first restricting $|\nu|$ and then $\rho$ sufficiently. Thus there exist $\nu_K,\rho_K,C_K>0$ such that

$$\lambda_0(b,p,\nu;D)-\lambda_0(b,p,\nu;K)
\geq C_K\left(|\nu|+\frac1{\log(1/(b+p))}\right)^2>0\tag{G9}$$

whenever $b,p\geq0$, $0<b+p<\rho_K$ and $|\nu|<\nu_K$. This is one rectangular parameter neighborhood; no bound on $\nu\log(1/\rho)$ is required. The constants depend on the obstacle, and no uniform threshold over all shapes is claimed.

In the distinguished regime $\nu\ell\to s\in\mathbb R$, the exact leading gap is

$$\ell^2\bigl(\lambda_0(b,p,\nu;D)-\lambda_0(b,p,\nu;K)\bigr)
\longrightarrow \frac{2\pi}{L}\delta\,s^2\operatorname{csch}^2(s/2)
+\frac{4\pi^2}{L}S_Ks^2\coth^2(s/2).\tag{G10}$$

Both squared hyperbolic expressions have continuous value $4$ at zero. The mean-value theorem in (G6) gives the first term, and (G8) gives the second. The $O(\varepsilon^3)$ remainder becomes negligible because $\varepsilon=O(\ell^{-1})$ in this regime. The formula recovers Theorem 8.1 at $s=0$ and is uniform in the magnetic/scalar ratio. $\square$

The comparison removes symmetry and convexity assumptions at an obstacle-dependent parameter threshold. It does not provide a field interval uniform over all shapes, and it does not settle the entire specified field range of [KL]. The flux neighborhood is likewise allowed to depend on $K$.

**Development and review.** This manuscript was developed with AI assistance. Floating-point radial checks supplement the analytic proof. The companion review records source versions, access limitations and the scope of the priority and significance assessment. Internal checks are not independent expert review.

## References

**[BGGLP]** L. Bundrock, A. Girouard, D. S. Grebenkov, M. Levitin and I. Polterovich, *The exterior Steklov problem for Euclidean domains*, arXiv:2511.09490v3, June 23, 2026. [Inspected version](https://arxiv.org/html/2511.09490v3).

**[CD]** T. J. Christiansen and K. Datchev, *Low energy scattering asymptotics for planar obstacles*, Pure and Applied Analysis **5** (2023), 767--794. [Final article](https://doi.org/10.2140/paa.2023.5.767).

**[GC]** D. S. Grebenkov and A. Chaigneau, *The Steklov problem for exterior domains: asymptotic behavior and applications*, Journal of Mathematical Physics **66** (2025), 061502. [DOI](https://doi.org/10.1063/5.0228529); [inspected arXiv version](https://arxiv.org/abs/2407.09864v3).

**[Gr]** G. Grubb, *Pseudodifferential methods for boundary value problems*, Chapter 11, author's chapter PDF, especially Theorems 11.11, 11.14 and 11.16. [Author copy](https://web.math.ku.dk/~grubb/dist11.pdf).

**[HN]** B. Helffer and F. Nicoleau, *On the magnetic Dirichlet to Neumann operator on the exterior of the disk -- diamagnetism, weak-magnetic field limit and flux effects*, Journal de Mathematiques Pures et Appliquees **205** (2026), 103799. [DOI](https://doi.org/10.1016/j.matpur.2025.103799); [inspected author preprint, March 25, 2025](https://arxiv.org/abs/2503.14008v2).

**[KL]** A. Kachmar and V. Lotoreichik, *Isoperimetric inequalities for the lowest magnetic Steklov eigenvalue*, arXiv:2602.17416v1, February 19, 2026. [Inspected version](https://arxiv.org/html/2602.17416v1).

**[LT]** G. Liu and X. Tan, *Spectral invariants of the magnetic Dirichlet-to-Neumann map on Riemannian manifolds*, arXiv:2108.07611v1, August 17, 2021, Propositions 3.1--3.2 and equations (3.3)--(3.11). [Inspected version](https://arxiv.org/html/2108.07611v1).

**[CPS]** B. Colbois, L. Provenzano and A. Savo, *Isoperimetric inequalities for the magnetic Neumann and Steklov problems with Aharonov--Bohm magnetic potential*, Journal of Geometric Analysis **32** (2022), 285. [Final article](https://doi.org/10.1007/s12220-022-01001-2).

**[CS]** M. Cekic and A. Siffert, *Magnetic Steklov problem on surfaces*, Journal of Functional Analysis **289** (2025), 111159. [Final article](https://doi.org/10.1016/j.jfa.2025.111159).

**[DLMF]** NIST Digital Library of Mathematical Functions, Section 13.2, especially the Kummer connection formula (13.2.42). [Formula](https://dlmf.nist.gov/13.2.E42).

**[PS]** L. Provenzano and A. Savo, *Geometry of the magnetic Steklov problem on Riemannian annuli*, arXiv:2310.08203v1, October 12, 2023. [Inspected version](https://arxiv.org/html/2310.08203v1); journal publication in Communications in Contemporary Mathematics, [DOI](https://doi.org/10.1142/S0219199725500014).
