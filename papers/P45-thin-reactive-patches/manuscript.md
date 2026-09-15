# Spectral localization and uniform reactive capacitance of thin planar patches

Henry Zweiman

September 15, 2026

## Abstract

We study the Newtonian single-layer operator on planar patches that collapse onto an embedded curve with a variable transverse width. After division by the thickness times its logarithm, the operators converge strongly to transverse averaging followed by multiplication by the local width. Every fixed eigenvalue converges to the top of this limiting spectrum, whereas the spectral measure of a constant function converges to the area-weighted distribution of widths. Consequently, when the maximum-width set has zero length, every fixed spectral weight tends to zero. This proves the proposed vanishing of the principal weight for thin ellipses and rhombi. A separate capacity estimate controls the singular perfect-reaction endpoint and yields a relative asymptotic formula uniform over all positive reactivities. The formula characterizes when the standard one-pole approximation is asymptotically exact. For constant-width Euclidean tubes we obtain bounded remainders in two conjectured logarithmic asymptotics. Finally, a separated-disk construction and a small-area perturbation argument produce a connected smooth patch whose second spectral weight exceeds its principal weight.

**Keywords:** reactive capacitance; exterior Steklov problem; thin domains; single-layer operator; spectral measure; localization.

## 1. Introduction and results

For a bounded planar patch $\Gamma\subset\mathbb R^2$, consider the operator

$$
(G_\Gamma f)(x)=\int_\Gamma\frac{f(y)}{2\pi|x-y|}\,dy.
\tag{1.1}
$$

Its reciprocal eigenvalues are the exterior Steklov eigenvalues for a reactive patch in the boundary of a reflecting half-space. The spectral representation of reactive capacitance associates to each normalized eigenfunction a weight given by its squared integral. These weights measure how the corresponding mode couples to a spatially constant input.

Grebenkov and Maurette [GM, Sections III C and IV] ask whether the principal weight tends to zero for increasingly thin ellipses and rhombi, and whether a higher weight can exceed the principal weight. Their Appendix B also proposes two logarithmic tube asymptotics, equations (B18) and (B19). We address these questions through a common operator framework. The spectral representation, the one-pole approximation, and the underlying variational principles are prior results; our contribution is their thin-shape limit and its consequences.

The distinction between spectral location and spectral weight is essential. All fixed eigenvalue indices approach the same normalized value, determined by the largest width. In contrast, the limiting response depends on the entire width distribution. Its mass can escape every fixed set of eigenvalue indices without escaping the bounded spectral interval.

### 1.1. Geometry and normalization

Let $S=[0,\ell]$, or let $S=\mathbb R/\ell\mathbb Z$ be an arclength circle. Let $\gamma:S\to\mathbb R^2$ be an embedded unit-speed $C^3$ arc or simple closed curve. In the arc case it is $C^3$ up to the endpoints. Assume the center curve has a positive tubular radius: sufficiently close points have a unique nearest point on the curve. Write $n(s)$ for a continuous unit normal and $\kappa(s)$ for the signed curvature.

Let $h:S\to[0,\infty)$ be Hölder continuous, positive in the interior of the arc, or everywhere on the circle. Define

$$
H=\max_S h>0,\qquad
D=\{(s,y):s\in S^\circ,\ |y|<h(s)\},\qquad
A=|D|=\int_S2h(s)\,ds.
\tag{1.2}
$$

For a circle, $S^\circ=S$. Endpoints have no effect on the integrals. For sufficiently small $\varepsilon>0$, put

$$
F_\varepsilon(s,y)=\gamma(s)+\varepsilon y n(s),\qquad
\Gamma_\varepsilon=F_\varepsilon(D),\qquad
L_\varepsilon=\log(1/\varepsilon).
\tag{1.3}
$$

All limits below are as $\varepsilon\downarrow0$, with the curve and $h$ fixed. The Jacobian of $F_\varepsilon$ is $\varepsilon J_\varepsilon$, where

$$
J_\varepsilon(s,y)=1-\varepsilon\kappa(s)y,
\qquad |\Gamma_\varepsilon|=\varepsilon A.
\tag{1.4}
$$

The area identity follows from symmetry in $y$. Define the unitary map and normalized operator

$$
U_\varepsilon f=\sqrt{\varepsilon J_\varepsilon}\,f\circ F_\varepsilon,
\qquad
B_\varepsilon=\frac{U_\varepsilon G_{\Gamma_\varepsilon}U_\varepsilon^*}
 {\varepsilon L_\varepsilon}.
\tag{1.5}
$$

List the eigenvalues of $G_{\Gamma_\varepsilon}$ in decreasing order, with multiplicity, as $\nu_0(\varepsilon)>\nu_1(\varepsilon)\ge\cdots>0$. Set $\mu_k=1/\nu_k$. For any real orthonormal eigenbasis $\psi_k$, define

$$
F_k(\varepsilon)=\frac{1}{|\Gamma_\varepsilon|}
 \left(\int_{\Gamma_\varepsilon}\psi_k\right)^2,
\qquad \sum_{k\ge0}F_k(\varepsilon)=1.
\tag{1.6}
$$

Individual weights in a multiple eigenspace depend on the chosen basis. Our fixed-index conclusions hold for every choice; the spectral measure below is basis independent.

### 1.2. Main theorems

**Theorem 1.1 (operator limit and localization).** Under the preceding hypotheses, $B_\varepsilon$ converges strongly on $L^2(D)$ to

$$
(Bf)(s,y)=\frac1\pi\int_{-h(s)}^{h(s)}f(s,z)\,dz
 =\frac{2h(s)}\pi(Pf)(s,y),
\tag{1.7}
$$

where $P$ is the orthogonal projection onto functions constant on each transverse section. For every fixed $k\ge0$,

$$
\frac{\nu_k(\varepsilon)}{\varepsilon L_\varepsilon}
 \longrightarrow\frac{2H}\pi,
\qquad
\varepsilon L_\varepsilon\mu_k(\varepsilon)
 \longrightarrow\frac\pi{2H}.
\tag{1.8}
$$

If $\phi_{k,\varepsilon}=U_\varepsilon\psi_k$, then

$$
\int_D (H-h(s))|\phi_{k,\varepsilon}(s,y)|^2\,ds\,dy\longrightarrow0.
\tag{1.9}
$$

If $\{s:h(s)=H\}$ has arclength measure zero, then $\phi_{k,\varepsilon}\rightharpoonup0$ and $F_k(\varepsilon)\to0$ for every fixed $k$.

**Theorem 1.2 (limiting spectral measure).** The probability measures

$$
\eta_\varepsilon=\sum_{k\ge0}F_k(\varepsilon)
 \delta_{\nu_k(\varepsilon)/(\varepsilon L_\varepsilon)}
\tag{1.10}
$$

converge weakly to the pushforward of $2h(s)\,ds/A$ under $s\mapsto2h(s)/\pi$. Equivalently, for every continuous function $g$ on a fixed compact interval containing the spectra,

$$
\int g\,d\eta_\varepsilon\longrightarrow
 \frac1A\int_S2h(s)g(2h(s)/\pi)\,ds.
\tag{1.11}
$$

For $\mu>0$, the reactive capacitance in the normalization of [GM] is

$$
C_\varepsilon(\mu)=\frac{\mu}{2\pi}
 \langle1,(I+\mu G_{\Gamma_\varepsilon})^{-1}1\rangle
 =\frac{\mu|\Gamma_\varepsilon|}{2\pi}
 \sum_{k\ge0}\frac{F_k(\varepsilon)}{1+\mu\nu_k(\varepsilon)}.
\tag{1.12}
$$

Write $C_\varepsilon(\infty)=\lim_{\mu\to\infty}C_\varepsilon(\mu)$. Define

$$
R_h(t)=\frac{t}{2\pi}\int_S\frac{2h(s)}{1+2t h(s)/\pi}\,ds,
\quad t\ge0,\qquad R_h(\infty)=\frac\ell2.
\tag{1.13}
$$

**Theorem 1.3 (uniform reactive capacitance).** One has

$$
L_\varepsilon C_\varepsilon(\infty)\longrightarrow\frac\ell2,
\qquad
\sup_{0<\mu\le\infty}
\left|\frac{L_\varepsilon C_\varepsilon(\mu)}
 {R_h(\mu\varepsilon L_\varepsilon)}-1\right|\longrightarrow0.
\tag{1.14}
$$

The ratio has continuous value one at $\mu=0$. Thus (1.14) includes the transition between reaction-limited and diffusion-limited behavior, even when $\mu$ varies arbitrarily with $\varepsilon$.

Two further results concern the same geometric questions. Theorem 5.1 proves the bounded remainders in [GM, (B18)-(B19)] for regular embedded center curves. Theorem 6.1 constructs a connected smooth patch with $F_1>F_0$.

### 1.3. Relation to other asymptotic regimes

The small-patch expansions of Grebenkov-Ward [GW1, GW2] and Lindsay-Bernoff-Grebenkov-Hoskins-Ward [LBGHW] involve patches whose diameters shrink on a three-dimensional boundary. They express global quantities through local reactive capacitances and interaction terms. Here the center curve remains fixed while only the transverse width shrinks, and we determine the local spectral measure and capacitance in this different degeneration. The local spectral representation used in those works is credited throughout; their global expansions are not needed in our proofs.

## 2. The logarithmic operator limit

We first record elementary operator facts. For every bounded measurable planar set $E$,

$$
\sup_x\int_E\frac{dy}{2\pi|x-y|}\le C|E|^{1/2}.
\tag{2.1}
$$

Indeed, splitting at radius $r$ gives a bound $r+|E|/(2\pi r)$, and one minimizes in $r$. Schur's test makes $G_E$ bounded. Deleting its kernel on $|x-y|<\delta$ changes the operator norm by at most $\delta$; the remaining kernel is square integrable. Thus $G_E$ is compact and self-adjoint. It is strictly positive as a quadratic form: extend $f$ by zero and use the Gaussian representation of $|x-y|^{-1}$, whose Fourier transform is positive. Each nonzero $f$ has strictly positive Gaussian energy. This also proves injectivity. The strictly positive kernel implies a simple positive principal eigenfunction: replacing a maximizer by its absolute value can only increase its Rayleigh quotient, strictly if both signs occur, and its image under $G_E$ is positive almost everywhere. Two orthogonal principal eigenfunctions are therefore impossible.

### 2.1. A straight strip

Suppose first that $\gamma(s)=(s,0)$, $S=[0,\ell]$. On $L^2(D)$ the operator $T_\varepsilon=L_\varepsilon B_\varepsilon$ has kernel

$$
K_\varepsilon((s,y),(t,z))=
 \frac{1}{2\pi\sqrt{(s-t)^2+\varepsilon^2(y-z)^2}}.
\tag{2.2}
$$

Let $r_\varepsilon(s,y)=\int_D K_\varepsilon((s,y),(t,z))\,dt\,dz$.

**Lemma 2.1 (row estimate).** Uniformly on $D$,

$$
r_\varepsilon(s,y)=\frac{h(s)}\pi
 \left[\log_+\frac{s}{\varepsilon}
       +\log_+\frac{\ell-s}{\varepsilon}\right]+O(1),
\qquad
r_\varepsilon(s,y)\le\frac{2h(s)}\pi L_\varepsilon+C,
\tag{2.3}
$$

where $\log_+q=\max(\log q,0)$.

*Proof.* On $|t-s|<\varepsilon$, substitute $t=s+\varepsilon u$. The integral is bounded by a constant times the integral of $(u^2+v^2)^{-1/2}$ on $[-1,1]\times[-2H,2H]$, hence uniformly bounded. On the complementary region,

$$
0\le\frac1{|s-t|}-\frac1{\sqrt{(s-t)^2+\varepsilon^2(y-z)^2}}
 \le\frac{2\varepsilon^2 H^2}{|s-t|^3}.
\tag{2.4}
$$

Its integral is $O(1)$. Consequently,

$$
r_\varepsilon(s,y)=\frac1\pi
 \int_{\substack{0<t<\ell\\|t-s|\ge\varepsilon}}
 \frac{h(t)}{|t-s|}\,dt+O(1).
\tag{2.5}
$$

If $h$ has Hölder exponent $\alpha>0$, replacing $h(t)$ by $h(s)$ costs at most a constant times $\int_0^\ell q^{\alpha-1}\,dq$. The remaining integral is explicit and gives (2.3). ∎

The one-sided endpoint logarithms in (2.3) cannot be replaced by a uniform two-sided $O(1)$ remainder when $h$ is positive at an endpoint. The uniform upper bound is sufficient for the spectral estimates; their integrability will suffice for the tube average.

**Lemma 2.2 (strong convergence).** For the straight strip, $B_\varepsilon\to B$ strongly on $L^2(D)$.

*Proof.* Let $f$ be the restriction of a continuous function on the closed rectangle $[0,\ell]\times[-H,H]$, and put

$$
a_f(t)=\int_{-h(t)}^{h(t)}f(t,z)\,dz.
\tag{2.6}
$$

This is continuous. The same near/far split as in Lemma 2.1 gives, uniformly in $(s,y)$,

$$
(T_\varepsilon f)(s,y)=\frac1{2\pi}
 \int_{|t-s|\ge\varepsilon}\frac{a_f(t)}{|t-s|}\,dt
 +O(\|f\|_\infty).
\tag{2.7}
$$

For a fixed interior $s$, the integral with $a_f(s)$ substituted for $a_f(t)$, divided by $L_\varepsilon$, tends to $2a_f(s)$. To bound the difference, first restrict to $|t-s|<\delta$, where continuity bounds it by $2\omega_{a_f}(\delta)L_\varepsilon+O(1)$; the remaining part is $O_\delta(1)$. Divide by $L_\varepsilon$, then let $\delta\downarrow0$. This proves pointwise convergence to $a_f(s)/\pi$.

Lemma 2.1 bounds $|B_\varepsilon f|$ uniformly by $C\|f\|_\infty$. Dominated convergence gives convergence in $L^2(D)$. Continuous restrictions are dense, and Schur's test gives $\sup_\varepsilon\|B_\varepsilon\|<\infty$, so the convergence extends to every $f\in L^2(D)$. ∎

### 2.2. Curvature

For a curved strip, $T_\varepsilon=L_\varepsilon B_\varepsilon$ has kernel

$$
\widetilde K_\varepsilon((s,y),(t,z))=
 \frac{\sqrt{J_\varepsilon(s,y)J_\varepsilon(t,z)}}
 {2\pi|F_\varepsilon(s,y)-F_\varepsilon(t,z)|}.
\tag{2.8}
$$

On a circle let $d_S(s,t)$ denote the shorter arclength distance. On an interval put $d_S(s,t)=|s-t|$. The straight reference kernel means (2.2) with $|s-t|$ replaced by $d_S(s,t)$.

**Lemma 2.3 (curvature comparison).** The difference between the operators with kernels (2.8) and the straight reference kernel has norm $O(1)$, uniformly in $\varepsilon$.

*Proof.* For a signed shorter displacement $d$ with $|d|<\delta$, Taylor expansion gives

$$
F_\varepsilon(s,y)-F_\varepsilon(t,z)
 =d\gamma'(t)+\varepsilon(y-z)n(t)+O(d^2+\varepsilon|d|).
\tag{2.9}
$$

Set $Q=(d^2+\varepsilon^2(y-z)^2)^{1/2}$. Since $Q\ge|d|$, for fixed sufficiently small $\delta$ and then small $\varepsilon$, the distance in (2.9) is comparable to $Q$, and

$$
\left|\widetilde K_\varepsilon-\frac1{2\pi Q}\right|
 \le C\frac{|d|+\varepsilon}{Q}.
\tag{2.10}
$$

The term $|d|/Q$ is bounded by one. The row integral of $\varepsilon/Q$ is $O(\varepsilon L_\varepsilon+\varepsilon)$ by the same near/far estimate used above. These bounds are uniform. For $d_S(s,t)\ge\delta$, compactness and embeddedness give a positive minimum chord distance between $\gamma(s)$ and $\gamma(t)$. The transverse perturbation preserves a positive lower bound for small $\varepsilon$, so this part also has bounded row integral. Symmetry and Schur's test prove the assertion. ∎

For the circular reference kernel, Lemmas 2.1 and 2.2 hold with two equal local logarithmic sides and no endpoints. In particular its row is $2h(s)L_\varepsilon/\pi+O(1)$ uniformly. Lemma 2.3 therefore proves the strong convergence assertion of Theorem 1.1 in all cases. It also gives, for every $f\in L^2(D)$,

$$
\langle B_\varepsilon f,f\rangle
 \le\int_D\frac{2h(s)}\pi|f(s,y)|^2\,ds\,dy
       +\frac{C}{L_\varepsilon}\|f\|_2^2.
\tag{2.11}
$$

For the straight reference operator this follows from $2|f(x)f(y)|\le|f(x)|^2+|f(y)|^2$ and the row estimate; Lemma 2.3 supplies the same bound for the curved operator.

The convergence is not convergence in operator norm. The limit acts as nonzero multiplication on an infinite-dimensional space of transverse constants and is not compact, whereas each $B_\varepsilon$ is compact.

## 3. Eigenvalues, localization, and spectral measures

*Proof of the remaining assertions of Theorem 1.1.* Inequality (2.11) gives the upper bound $\limsup\nu_0/(\varepsilon L_\varepsilon)\le2H/\pi$. Given $\delta>0$ and $k$, choose a $(k+1)$-dimensional space of transverse constants supported where $h>H-\delta$. This is possible even if the maximum occurs at an endpoint, by continuity and positivity in the interior. On this space $\langle Bf,f\rangle\ge2(H-\delta)\|f\|^2/\pi$. Strong convergence is uniform on its unit sphere, since the space is finite dimensional. The minimax principle gives

$$
\liminf\frac{\nu_k(\varepsilon)}{\varepsilon L_\varepsilon}
 \ge\frac{2(H-\delta)}\pi.
\tag{3.1}
$$

Letting $\delta\downarrow0$ proves (1.8). Substituting $f=\phi_{k,\varepsilon}$ into (2.11), using its unit norm and (1.8), proves (1.9).

Suppose the maximum set has measure zero. Put $E_\delta=\{(s,y)\in D:H-h(s)<\delta\}$. Its area tends to zero with $\delta$. On $D\setminus E_\delta$, (1.9) implies $\|\phi_{k,\varepsilon}\|_{L^2(D\setminus E_\delta)}\to0$ for each fixed $\delta$. For any $v\in L^2(D)$,

$$
|\langle\phi_{k,\varepsilon},v\rangle|
 \le\|v\|_{L^2(E_\delta)}
 +\|\phi_{k,\varepsilon}\|_{L^2(D\setminus E_\delta)}\|v\|_2.
\tag{3.2}
$$

First let $\varepsilon\downarrow0$, then $\delta\downarrow0$. This proves weak convergence. The normalized constant input pulls back to

$$
q_\varepsilon=U_\varepsilon\frac1{\sqrt{|\Gamma_\varepsilon|}}
 =\frac{\sqrt{J_\varepsilon}}{\sqrt A}
 \longrightarrow q=\frac1{\sqrt A}\quad\hbox{in }L^2(D).
\tag{3.3}
$$

Thus $F_k=|\langle q_\varepsilon,\phi_{k,\varepsilon}\rangle|^2\to0$. ∎

*Proof of Theorem 1.2.* Positivity and the uniform norm bound place all spectra in a common compact interval. Strong convergence implies strong convergence of every polynomial in the operators. Uniform polynomial approximation then gives $g(B_\varepsilon)\to g(B)$ strongly for every continuous $g$ on that interval. By (3.3),

$$
\int g\,d\eta_\varepsilon
 =\langle q_\varepsilon,g(B_\varepsilon)q_\varepsilon\rangle
 \longrightarrow\langle q,g(B)q\rangle.
\tag{3.4}
$$

Since $Pq=q$, the last expression is the right-hand side of (1.11). The transverse zero eigenspace of $B$ contributes no additional atom. ∎

**Corollary 3.1 (ellipses and rhombi).** On $S=[-1,1]$, take respectively $h(s)=\sqrt{1-s^2}$ or $h(s)=1-|s|$. For the resulting ellipses or rhombi,

$$
\varepsilon\log(1/\varepsilon)\mu_k(\varepsilon)\to\frac\pi2,
\qquad F_k(\varepsilon)\to0
\quad\hbox{for every fixed }k.
\tag{3.5}
$$

In particular there are bounded smooth convex patches with arbitrarily small principal weight. Uniform spatial dilation preserves the weights, so this remains true after fixing area or diameter by dilation.

*Proof.* Both profiles are Hölder continuous and have a unique maximum of value one. Ellipses have smooth convex boundaries for every positive $\varepsilon$. Under a dilation by $a$, the unitary change of variables multiplies $G$ by $a$ and preserves the normalized squared integrals in (1.6). ∎

## 4. Uniform capacitance and the one-pole approximation

### 4.1. Finite rescaled reactivity

Put $t=\mu\varepsilon L_\varepsilon$. Equations (1.12) and (3.3) give

$$
L_\varepsilon C_\varepsilon(t/(\varepsilon L_\varepsilon))
 =\frac{tA}{2\pi}
 \langle q_\varepsilon,(I+tB_\varepsilon)^{-1}q_\varepsilon\rangle.
\tag{4.1}
$$

The strong functional calculus proves convergence to $R_h(t)$ for fixed finite $t$. The resolvent identity and the uniform operator bound imply a common Lipschitz bound for the scalar expressions after division by $t$, including their continuous values at zero. A finite mesh therefore upgrades the pointwise convergence to uniform convergence after division by $t$ on every bounded $t$-interval. This also follows directly from uniform polynomial approximation of $(1+tx)^{-1}$ on a compact rectangle in $(t,x)$.

### 4.2. The perfect-reaction endpoint

Strong convergence alone does not control inverse operators at zero. We use an independent energy upper bound. If a compactly supported potential $u\in H^1(\mathbb R^3)$ equals one on a neighborhood of $\Gamma$, then

$$
C_\Gamma(\mu)\le\frac1{4\pi}\int_{\mathbb R^3}|\nabla u|^2
 \quad(0<\mu\le\infty).
\tag{4.2}
$$

This is the usual Newtonian capacity upper bound, consistent with [GM, (52) and (55)]. For completeness it also follows directly from the integral operator, even for our Hölder profiles. For $f\in L^2(\Gamma)$ let $v$ be its single-layer potential with kernel $1/(2\pi|x-y|)$ in $\mathbb R^3$. The distributional identity $-\Delta v=2f\,\delta_{\{x_3=0\}}$ gives

$$
\int|\nabla v|^2=2\langle f,G_\Gamma f\rangle,
\qquad \int\nabla u\cdot\nabla v=2\int_\Gamma f.
\tag{4.3}
$$

These identities follow first for smooth densities and then by the energy bound (2.1). Cauchy-Schwarz yields $(\int f)^2\le(\int|\nabla u|^2)\langle f,G_\Gamma f\rangle/2$. Apply this in the quadratic variational identity

$$
2\pi C_\Gamma(\mu)
 =\sup_f\left\{2\int_\Gamma f-\langle f,G_\Gamma f\rangle
                         -\mu^{-1}\|f\|_2^2\right\}.
\tag{4.4}
$$

The supremum is bounded by $\int|\nabla u|^2/2$. This proves (4.2) for finite $\mu$, and monotone convergence in (1.12) proves it for infinity.

View the center curve in $\mathbb R^3$. Choose a fixed $\delta$ smaller than its tubular radius, and set $a=2\varepsilon H<\delta$. With $d(x)$ denoting distance to the curve, take

$$
u(x)=\begin{cases}
1,&d(x)\le a,\\
\log(\delta/d(x))/\log(\delta/a),&a<d(x)<\delta,\\
0,&d(x)\ge\delta.
\end{cases}
\tag{4.5}
$$

It equals one on a neighborhood of the patch and is an admissible $H^1$ test potential. In normal polar coordinates around the interior of a planar curve, the volume Jacobian is $r(1-\kappa(s)r\cos\theta)$. Its angular integral is $2\pi r$. The shell energy along the curve is therefore $2\pi\ell/\log(\delta/a)$. An open arc also has two hemispherical endpoint shells, whose total energy is $4\pi(\delta-a)/\log(\delta/a)^2$. There are no endpoint shells for a closed curve. Thus

$$
C_\varepsilon(\infty)
 \le\frac{\ell}{2\log(\delta/a)}+O(L_\varepsilon^{-2}),
\qquad
\limsup L_\varepsilon C_\varepsilon(\infty)\le\frac\ell2.
\tag{4.6}
$$

The decomposition is valid for $\delta$ below the reach; smoothing (4.5) preserves admissibility and the energy limit if smooth test potentials are preferred.

For every finite $t$, monotonicity in $\mu$ and (4.1) give $\liminf L_\varepsilon C_\varepsilon(\infty)\ge R_h(t)$. Since $h>0$ almost everywhere on $S$, dominated convergence gives $R_h(t)\to\ell/2$ as $t\to\infty$. This proves the first assertion of (1.14).

### 4.3. Uniformity over the whole range

*Completion of the proof of Theorem 1.3.* Define $f_\varepsilon(t)$ by the left-hand side of (4.1), including its value at infinity. It is nondecreasing in $t$, converges pointwise to $R_h$ on the compactified half-line $[0,\infty]$, and the limit is continuous there. A finite partition, on each of whose intervals the oscillation of $R_h$ is small, proves uniform absolute convergence by monotonicity. This argument requires no monotonicity in $\varepsilon$.

For any fixed $T>0$, the convergence of $f_\varepsilon(t)/t$ is uniform on $[0,T]$, and

$$
\frac{R_h(t)}t\ge\frac{A}{2\pi(1+2TH/\pi)}>0
 \quad(0\le t\le T),
\tag{4.7}
$$

with continuous interpretation at zero. Hence relative convergence is uniform on $(0,T]$. On $[T,\infty]$, use uniform absolute convergence and $R_h(t)\ge R_h(T)>0$. The two bounds prove (1.14). The exact area formula (1.4) gives the claimed ratio at zero. ∎

### 4.4. When a single pole suffices

The approximation of [GM, (27)] is

$$
C_{\mathrm{app},\varepsilon}(\mu)
 =\left[C_\varepsilon(\infty)^{-1}
              +\frac{2\pi}{\mu|\Gamma_\varepsilon|}\right]^{-1}.
\tag{4.8}
$$

Let $\bar h=\ell^{-1}\int_S h(s)\,ds$, and define

$$
R_{\mathrm{app},h}(t)=\frac\ell2
       \frac{2t\bar h/\pi}{1+2t\bar h/\pi}.
\tag{4.9}
$$

**Corollary 4.1 (limiting approximation error).** For every $t>0$,

$$
\frac{C_{\mathrm{app},\varepsilon}(t/(\varepsilon L_\varepsilon))}
 {C_\varepsilon(t/(\varepsilon L_\varepsilon))}
 \longrightarrow\frac{R_{\mathrm{app},h}(t)}{R_h(t)}.
\tag{4.10}
$$

The convergence of these ratios is uniform on $0<t\le\infty$. The limiting ratio is identically one if and only if $h$ is constant. If $h$ is nonconstant, it is strictly larger than one at every finite $t>0$. In particular,

$$
\lim_{\varepsilon\downarrow0}\sup_{\mu>0}
 \left|\frac{C_{\mathrm{app},\varepsilon}(\mu)}{C_\varepsilon(\mu)}-1\right|
 =\max_{0<t<\infty}
       \left(\frac{R_{\mathrm{app},h}(t)}{R_h(t)}-1\right)>0
\tag{4.11}
$$

for nonconstant $h$. For constant $h$ the limit of the supremum is zero.

*Proof.* Use (1.4) and (1.14) in (4.8). More explicitly, replacing $L_\varepsilon C_\varepsilon(\infty)$ by $\ell/2$ in the harmonic mean changes it by a relative error no larger than a quantity tending to zero, uniformly in $t$. Theorem 1.3 then gives uniform convergence of the ratios. The function $x\mapsto (2tx/\pi)/(1+2tx/\pi)$ is strictly concave for $t>0$. Jensen's inequality with respect to $ds/\ell$ proves the comparison and its equality condition. The limiting ratio tends to one at both endpoints, and is positive and continuous throughout. This gives the attained interior maximum in (4.11). ∎

For a rhombus with $h(s)=1-|s|$ on $[-1,1]$, let $c=2t/\pi$. Direct integration gives

$$
R_h(t)=1-\frac{\log(1+c)}c,
\qquad R_{\mathrm{app},h}(t)=\frac{c}{c+2}.
\tag{4.12}
$$

At $c=2$, the limiting relative error is $1/(2-\log3)-1>0$. For a rectangle with $h=1$, both limiting responses are $c/(1+c)$. These conclusions concern the moving reaction scale $\mu\asymp1/(\varepsilon\log(1/\varepsilon))$; a fixed bounded numerical range of $\mu$ need not sample this scale for very small $\varepsilon$.

## 5. Constant-width Euclidean tubes

Here the patch is the full planar distance tube

$$
\mathcal T_\varepsilon=\{x\in\mathbb R^2:
                    \operatorname{dist}(x,\gamma(S))<\varepsilon\}.
\tag{5.1}
$$

For an arc this includes the semicircular end caps. Define its normalized average kernel energy by

$$
\mathcal A_\varepsilon=\frac1{|\mathcal T_\varepsilon|^2}
 \int_{\mathcal T_\varepsilon}\int_{\mathcal T_\varepsilon}
                       \frac{dx\,dy}{2\pi|x-y|}.
\tag{5.2}
$$

**Theorem 5.1 (bounded tube remainders).** For a fixed embedded $C^3$ arc or simple closed curve of length $\ell$ and positive reach,

$$
\frac{\nu_0(\mathcal T_\varepsilon)}\varepsilon
 =\frac2\pi L_\varepsilon+O(1),
\qquad
\mathcal A_\varepsilon
 =\frac{2L_\varepsilon}{\pi|\partial\mathcal T_\varepsilon|}+O(1).
\tag{5.3}
$$

*Proof.* Let $\Sigma_\varepsilon$ be the normal strip with $h=1$. Lemma 2.1, integrated in $(s,y)$, and Lemma 2.3 give

$$
\int_{\Sigma_\varepsilon}\int_{\Sigma_\varepsilon}
 \frac{dx\,dy}{2\pi|x-y|}
 =\frac{4\varepsilon^2\ell}\pi L_\varepsilon+O(\varepsilon^2).
\tag{5.4}
$$

To see explicitly the endpoint control, the difference between $\log_+(s/\varepsilon)$ and $L_\varepsilon$ is $\log\max(s,\varepsilon)$, whose integral on $[0,\ell]$ is bounded. In passing between the curved kernel and physical integrals, factors $J_\varepsilon=1+O(\varepsilon)$ contribute only $O(\varepsilon L_\varepsilon)=O(1)$ after division by $\varepsilon^2$.

The physical row on $\Sigma_\varepsilon$ is at most $\varepsilon(2L_\varepsilon/\pi+C)$. If the curve is closed, this is the whole tube and Schur's test and the constant Rayleigh quotient prove the first part of (5.3).

For an arc, the two caps have total area $\pi\varepsilon^2$. Their contribution to any row is $O(\varepsilon)$ by (2.1). For a point $x$ in the cap at $s=0$, the strip portion $s<C\varepsilon$ also contributes $O(\varepsilon)$ by its area. On $C\varepsilon<s<\delta$, Taylor expansion about the endpoint gives, uniformly across the width,

$$
\left|\frac1{|x-F_\varepsilon(s,y)|}-\frac1s\right|
 \le C\left(1+\frac\varepsilon{s^2}\right).
\tag{5.5}
$$

Choose $C$ large and $\delta$ small so that the compared distances are uniformly comparable. Integrating (5.5) against the physical transverse measure gives a one-sided strip row $\varepsilon L_\varepsilon/\pi+O(\varepsilon)$. For $s\ge\delta$, embeddedness gives a positive distance from the endpoint, and that part is $O(\varepsilon)$. The other endpoint is identical. Thus the maximum row of the full tube is still at most $\varepsilon(2L_\varepsilon/\pi+C)$.

The constant Rayleigh quotient is bounded below by (5.4) divided by $2\varepsilon\ell+\pi\varepsilon^2$. Its leading term is $2\varepsilon L_\varepsilon/\pi$ and its error is $O(\varepsilon)$. This proves the first part of (5.3). Integrals involving caps are bounded by their area times the full row bound, hence are $O(\varepsilon^3 L_\varepsilon)=o(\varepsilon^2)$. Therefore (5.4) remains valid with the full tube in place of the strip.

Finally, integration of the planar normal-coordinate Jacobian and offset arclength gives

$$
\begin{array}{c|cc}
&|\mathcal T_\varepsilon|&|\partial\mathcal T_\varepsilon|\\ \hline
\text{closed curve}&2\varepsilon\ell&2\ell\\
\text{arc}&2\varepsilon\ell+\pi\varepsilon^2&2\ell+2\pi\varepsilon.
\end{array}
\tag{5.6}
$$

Dividing (5.4) by the squared area gives $L_\varepsilon/(\pi\ell)+O(1)$, which equals the second expression in (5.3). ∎

Since $\nu_0=1/\mu_0$, (5.3) has the normalization and the bounded remainders in [GM, (B18)-(B19)]. The statement does not include singular or self-intersecting center curves, or families in which the center curve changes with the thickness.

## 6. A higher spectral weight can exceed the principal weight

**Theorem 6.1.** There exists a bounded connected simply connected $C^\infty$ planar patch $\Omega$ for which the largest two eigenvalues of $G_\Omega$ are simple and $F_1(\Omega)>F_0(\Omega)$.

*Proof.* Let $B$ be the unit disk. Denote its largest two eigenvalues by $\lambda_0>\lambda_1$, and let $\varphi$ be its positive normalized principal eigenfunction. Set

$$
m=\int_B\varphi>0,\qquad F_B=\frac{m^2}\pi,
\qquad \max\{\lambda_1/\lambda_0,1/\sqrt2\}<r<1.
\tag{6.1}
$$

Let $\Gamma_R$ be the union of the unit disk centered at zero and two radius-$r$ disks centered at $\pm Re_1$. On a fixed direct sum of three unit-disk Hilbert spaces, translations and unitary dilations identify its operator with

$$
G_R=D+R^{-1}V+O(R^{-2}),
\qquad D=\operatorname{diag}(G_B,rG_B,rG_B),
\tag{6.2}
$$

in operator norm. Indeed, on distinct bounded component disks the kernel has a uniform inverse-distance expansion, while each diagonal block is exact. The eigenvalue $\lambda_0$ of $D$ is simple. The next eigenvalue is $r\lambda_0$, with multiplicity two, separated from the rest by (6.1).

In the orthonormal basis of the two satellite ground states, compression of $V$ to this eigenspace is

$$
\begin{pmatrix}0&b\\b&0\end{pmatrix},
\qquad b=\frac{r^2m^2}{4\pi}>0.
\tag{6.3}
$$

The numerator uses the integral $rm$ of a normalized radius-$r$ disk eigenfunction, and the denominator uses the satellite separation $2R$. Coupling with the central disk affects this isolated cluster only at second order.

For clarity, this last assertion follows by decomposing into the cluster projection $P$ and $Q=I-P$. In a fixed neighborhood of $r\lambda_0$, the $Q$-block of $G_R-\lambda I$ is uniformly invertible. Solve its eigenvector equation for the $Q$ component and substitute into the $P$ component. The resulting two-dimensional Schur complement is

$$
(r\lambda_0-\lambda)I+R^{-1}PVP+O(R^{-2}).
\tag{6.4}
$$

The two eigenvalues are consequently $r\lambda_0\pm b/R+O(R^{-2})$, and their normalized eigenvectors approach the even and odd satellite combinations. The error in these vectors inside the cluster is $O(R^{-1})$, since the first-order matrix has distinct eigenvalues. Spectral separation from all other eigenvalues persists. Thus the plus branch is the simple second eigenvalue of $G_R$, while the principal eigenfunction converges to the central disk ground state. It follows that

$$
F_0(\Gamma_R)\longrightarrow\frac{F_B}{1+2r^2},
\qquad
F_1(\Gamma_R)\longrightarrow\frac{2r^2F_B}{1+2r^2}.
\tag{6.5}
$$

Choose a sufficiently large fixed $R$. Since $2r^2>1$, the strict weight inequality holds on $\Gamma_R$.

It remains to connect the disks. Join them along the intervening horizontal segments by channels of width tending to zero, and round the finitely many junctions. This gives bounded simply connected $C^\infty$ domains $\Omega_\delta\supset\Gamma_R$, all in a fixed container, with $|\Omega_\delta\setminus\Gamma_R|\to0$. One may first enlarge the disks slightly and then smooth the junctions to preserve containment. No holes are introduced because the channels connect the three disks along a tree.

Extend all operators by zero to $L^2$ of the container and put $E_\delta=\Omega_\delta\setminus\Gamma_R$. By (2.1), the $E_\delta$ diagonal block has norm $O(|E_\delta|^{1/2})$. The two row bounds for a cross block give, by Schur's test,

$$
\|G_{\Gamma_R,E_\delta}\|
 \le C|\Gamma_R|^{1/4}|E_\delta|^{1/4}.
\tag{6.6}
$$

Hence the zero-extended operators converge in norm. Resolvents and the spectral projections of the isolated simple first two eigenvalues converge in norm, by the resolvent identity and contour integration. Choosing eigenvector signs consistently gives convergence in $L^2$. Also $1_{\Omega_\delta}\to1_{\Gamma_R}$ in $L^2$, and the areas converge. Thus both weights converge and their strict inequality persists for small $\delta$. ∎

The connected examples in Theorem 6.1 are not claimed to be convex. Smooth convex examples with arbitrarily small $F_0$ are supplied separately by Corollary 3.1.

## 7. Further questions

The leading operator limit leaves a finer spectral problem. Near an isolated maximum of $h$, the width defect competes with a logarithmic longitudinal interaction. Determining a sharp localization scale and the subleading eigenvalue expansion requires estimates beyond strong convergence. We make no claim about that expansion here.

When the maximum-width set has positive length, Theorem 1.1 still gives concentration near it, but does not determine the limiting individual weights. Even for constant-width strips, the limiting measure is a single atom while the distribution of that mass among fixed indices requires a finer operator limit. This distinction explains why a uniform capacitance formula does not by itself settle individual ground-state profiles.

The geometric hypotheses also matter. Intersections, corners in the center curve, or a separation scale that shrinks with $\varepsilon$ may alter the bounded remainder or introduce interactions absent from Lemma 2.3. These cases are outside the present theorems.

## References

[GM] Denis S. Grebenkov and Raphael Maurette, *Reactive capacitance of flat patches of arbitrary shape*, Physical Review E **113** (2026), 034112. [DOI: 10.1103/mtgh-d591](https://doi.org/10.1103/mtgh-d591). [arXiv:2510.25288v2](https://arxiv.org/abs/2510.25288v2), January 30, 2026. The cited equation numbers refer to the final journal article.

[GW1] Denis S. Grebenkov and Michael J. Ward, *The Asymptotic Analysis of Some PDE and Steklov Eigenvalue Problems with Partially Reactive Patches in 3-D*, [arXiv:2509.17394v3](https://arxiv.org/abs/2509.17394v3), August 3, 2026.

[GW2] Denis S. Grebenkov and Michael J. Ward, *The Effective Reactivity for Capturing Brownian Motion by Partially Reactive Patches on a Spherical Surface*, Multiscale Modeling & Simulation **24** (2026), no. 2, 660-692. [DOI: 10.1137/25M180562X](https://doi.org/10.1137/25M180562X).

[LBGHW] Alan E. Lindsay, Andrew J. Bernoff, Denis S. Grebenkov, Jeremy G. Hoskins, and Michael J. Ward, *Asymptotic Analysis of the Narrow Escape and Berg-Purcell problems on general three-dimensional domains with reactive boundary patches*, [arXiv:2608.08626v1](https://arxiv.org/abs/2608.08626v1), August 9, 2026.
