# Sharp stability of the annulus for physical torsion

Henry Zweiman

September 15, 2026

## Abstract

For the physical torsional rigidity of a planar domain with holes, the concentric annulus maximizes torsion when the outer area and the total hole area are fixed. We prove that the deficit controls the square of the distance of the outer domain and the union of holes from two disks with a common center. The constant depends only on the ratio of the prescribed areas. When the holes occupy at most two-thirds of the outer area, we also obtain a universal constant for the sum of the squared individual Fraenkel asymmetries, weighted by the squares of their areas. Both exponents are optimal. These results answer the optimal-exponent questions posed by Amato and Barbato. The proof combines the global quantitative calibration theorem of Hensel and Laux with a level-set transport argument inspired by Guerra, Machado and Ramos. An exact decomposition isolates the displacement of the positive-measure plateaus corresponding to the holes. A smooth compactly supported calibration then propagates proximity to disks with one fixed center, without a diameter bound or a bound on the number of holes.

## 1. Introduction and main results

Let $G\subset\mathbb R^2$ be a bounded Lipschitz domain. Let $S_1,\ldots,S_m$ be nonempty bounded connected Lipschitz domains with pairwise disjoint closures compactly contained in $G$, and write

$$
S=\bigcup_{i=1}^m\overline{S_i},\qquad \Omega=G\setminus S,
\qquad A=|G|,\quad B=|S|,\quad 0<B<A.
\tag{1}
$$

Lebesgue measure is denoted by $|\cdot|$. Boundaries of Lipschitz sets have measure zero, so closures do not affect area formulas. The physical torsional rigidity is

$$
T(\Omega)=\sup_{0\ne v\in V_S}
\frac{\left(\int_Gv\right)^2}{\int_G|\nabla v|^2},\qquad
V_S=\{v\in H_0^1(G):v\text{ is constant a.e. on each }S_i\}.
\tag{2}
$$

The load in (2) is integrated over the filled outer domain $G$. The constants on different holes are free and need not agree. Thus (2) is different from the all-Dirichlet torsion functional on $\Omega$.

Set

$$
R=\sqrt{A/\pi},\qquad r=\sqrt{B/\pi},\qquad
\mathcal A_{A,B}=B_R\setminus\overline{B_r},\qquad
\delta=T(\mathcal A_{A,B})-T(\Omega).
\tag{3}
$$

The Pólya-Weinstein inequality states that $\delta\ge0$ [PW]. Amato and Barbato established rigidity and quantitative stability [AB]. Their first quantitative theorem gives cubic individual asymmetries when $B\le2A/3$; their second gives an unspecified positive exponent for an annular asymmetry. Section 7 of their final article asks for the optimal exponents.

For a measurable set $E$ of positive finite area, let

$$
\alpha(E)=\inf_z\frac{|E\triangle B_{\sqrt{|E|/\pi}}(z)|}{|E|}.
$$

To state center alignment without ambiguity, define

$$
\begin{aligned}
\mathfrak a(G,S)&=\inf_z\bigl(|G\triangle B_R(z)|+|S\triangle B_r(z)|\bigr),\\
\beta(\Omega)&=\inf_z|\Omega\triangle(B_R(z)\setminus\overline{B_r(z)})|.
\end{aligned}
\tag{4}
$$

The centers of the two comparison disks in (4) are the same.

**Theorem 1.1.** There is a positive function $c:(1,\infty)\to(0,\infty)$ such that every configuration (1) satisfies

$$
\delta\ge c(A/B)\,\mathfrak a(G,S)^2
\ge c(A/B)\,\beta(\Omega)^2.
\tag{5}
$$

The constants are independent of the diameter, the number of holes, and the Lipschitz constants of the boundaries. If $B\le2A/3$, there is an absolute constant $c_0>0$ such that

$$
\delta\ge c_0\bigl(A^2\alpha(G)^2+B^2\alpha(S)^2\bigr).
\tag{6}
$$

The exponent two in (5) and (6) cannot be replaced by any smaller positive exponent, even for smooth domains with one hole and fixed $A,B$.

The second inequality in (5) follows from the inclusion of the symmetric difference of set differences in the union of the two symmetric differences. The powers of area in (6) and the dependence on $A/B$ in (5) agree with the scaling $T(t\Omega)=t^4T(\Omega)$.

Sharp stability for Dirichlet torsion was proved by Brasco, De Philippis and Velichkov [BDPV]. Guerra, Machado and Ramos recently developed a different route, using simultaneous control of the isoperimetric deficit and the oscillation of the gradient along torsion levels [GMR]. We use their transport viewpoint. Two additional issues arise in (2): the value distribution has atoms on the holes, and separately selected centers do not establish concentricity. We resolve the first by a quantitative accounting of the plateau ranks, and the second by transporting relative to a fixed center with a smooth compactly supported calibration. The essential geometric input is the global theorem of Hensel and Laux [HL]. We do not claim an effective numerical value of the constants: their global theorem is used as an existence result.

## 2. The torsion function and its levels

The space $V_S$ is closed for the Dirichlet norm: restriction of the weak gradient to each connected hole is continuous, and its kernel consists of constants there. Riesz representation gives a unique $u\in V_S$ satisfying

$$
\int_G\nabla u\cdot\nabla v=\int_Gv\qquad(v\in V_S).
\tag{7}
$$

It follows that

$$
T(\Omega)=\int_Gu=\int_G|\nabla u|^2.
\tag{8}
$$

We use the representative extended constantly through each hole, with values $c_i$.

**Lemma 2.1.** The function $u$ is positive in $\Omega$ and on every hole, bounded and continuous on $\overline G$, and smooth in $\Omega$. For every positive regular value distinct from the $c_i$, the boundary of $\{u>t\}$ is a compact smooth curve, possibly with several components, contained in $\Omega$.

**Proof.** Testing (7) with the negative part gives $u\ge0$. To obtain positivity on the holes, let $H$ be harmonic in $\Omega$, with zero outer trace and trace one on all holes, extended as one through $S$. For $v\in V_S$, write $v_i$ for its constant on $S_i$. Harmonicity and fixed $H^1$ lifts of the hole traces give finite numbers $C_i$ such that

$$
\int_\Omega\nabla H\cdot\nabla v=\sum_i C_iv_i.
$$

Indeed subtraction of the corresponding lifts leaves a function in $H_0^1(\Omega)$. Choose $\varepsilon>0$ with $\varepsilon C_i\le|S_i|$ for all $i$. For nonnegative $v\in V_S$, the weak pairing of $u-\varepsilon H$ with $v$ is

$$
\int_\Omega v+\sum_i(|S_i|-\varepsilon C_i)v_i\ge0.
$$

Its negative part is an admissible test, so $u\ge\varepsilon H$. In particular $c_i\ge\varepsilon$. Interior positivity follows from the strong maximum principle and $-\Delta u=1$ in $\Omega$.

The constants $c_i$ are finite. Weak comparison with a containing-ball quadratic plus $\max_i c_i$ bounds $u$ from above. On $\Omega$, the function $u+|x|^2/4$ is harmonic, and its trace is continuous on each boundary component. The exterior-cone property of a Lipschitz boundary gives continuity up to the boundary. In the planar setting this can be seen directly: at a boundary point choose a slightly narrower exterior cone. On its complementary wedge, of angle $\omega<2\pi$, the function $\rho^{\pi/\omega}\sin(\pi\theta/\omega)$ is a positive harmonic barrier. The cone can be chosen narrow enough that $\pi/\omega<1$, and with its edges separated from the domain. After subtracting the locally constant boundary value, add a quadratic particular solution. A multiple of the barrier dominates both the quadratic remainder on the physical boundary and the bounded data on the local circular boundary. Weak comparison proves continuity at the vertex. Positive levels different from all boundary constants therefore stay a positive distance from every boundary component. Interior regularity and the implicit function theorem prove the last assertion. $\square$

For regular levels define

$$
E_t=\{u>t\},\quad m(t)=|E_t|,\quad
p(t)=\mathcal H^1(\partial E_t),\quad
\ell(t)=\int_{\partial E_t}\frac1{|\nabla u|}.
\tag{9}
$$

Truncations of $u$ remain in $V_S$. Testing with a linear approximation to the indicator of $E_t$, or differentiating (7) tested with $(u-t)_+$, yields

$$
\int_{\partial E_t}|\nabla u|=m(t).
\tag{10}
$$

The critical set of $u$ in $\Omega$ has area zero. One proof uses the fact that weak derivatives vanish almost everywhere on a level set: if $\nabla u=0$ on a set of positive measure, all entries of $D^2u$ vanish almost everywhere there, contradicting $\Delta u=-1$. Coarea, first on compact subsets and then by exhaustion, consequently gives the value distribution in the form

$$
-dm=\ell(t)\,dt+\sum_j b_j\delta_{d_j}.
\tag{11}
$$

Here $d_j$ are the distinct hole values, and $b_j$ is the combined area of the holes with value $d_j$. Thus there is no additional singular-continuous part. In particular $m$ is absolutely continuous between the finitely many $d_j$, and $-m'=\ell$ there. Sard's theorem and this absolute continuity imply that nonregular values occupy zero mass rank, apart from the hole plateaus.

Introduce two nonnegative deficits,

$$
D_H(t)=\ell(t)m(t)-p(t)^2,\qquad
D_I(t)=p(t)^2-4\pi m(t).
\tag{12}
$$

Their nonnegativity follows respectively from Cauchy-Schwarz using (10), and from the planar isoperimetric inequality.

## 3. The plateau deficit

Let $M=\max u$. At each hole value set

$$
h_j=m(d_j-),\qquad a_j=m(d_j),\qquad
I=\bigcup_j(a_j,h_j).
\tag{13}
$$

These intervals are disjoint and $|I|=B$. A jump at $M$ is included, with lower endpoint zero. Positivity gives $m(0+)=A$. Integrating the absolutely continuous part of the derivative of $m^2$, and telescoping across the jumps, gives

$$
\int_0^M m(t)\ell(t)\,dt
=\frac{A^2}{2}-\frac12\sum_j(h_j^2-a_j^2).
\tag{14}
$$

The torsion function of the concentric annulus, extended through its hole, equals $(R^2-|x|^2)/4$ on the annulus and $(R^2-r^2)/4$ on the hole. Its weak equation follows by integration by parts, including the constant hole test value. Hence

$$
T(\mathcal A_{A,B})=\frac{A^2-B^2}{8\pi}.
$$

Layer cake, (12) and (14) now give the exact identity

$$
\delta=J+K,\qquad
J=\frac1{4\pi}\int_0^M(D_H+D_I)\,dt,\qquad
K=\frac1{4\pi}\left(\int_I s\,ds-\frac{B^2}{2}\right).
\tag{15}
$$

This separates the level-set deficit from the displacement of plateau ranks. It is consistent with the plateau bookkeeping in [AB, proof of Theorem 2.6].

**Lemma 3.1.** Both terms in (15) are nonnegative, and

$$
|I\triangle(0,B)|\le4\sqrt{\pi\delta},\qquad
|I\setminus(0,B)|\le2\sqrt{\pi\delta}.
\tag{16}
$$

**Proof.** Set $a=|I\setminus(0,B)|=|(0,B)\setminus I|$. For fixed length $a$, the first moment outside $(0,B)$ is minimized on $(B,B+a)$, and the removed first moment is maximized on $(B-a,B)$. Therefore

$$
\int_I s\,ds-\frac{B^2}{2}\ge a^2.
$$

Use $K\le\delta$ and $|I\triangle(0,B)|=2a$. $\square$

Choose a nested family $F_s$, $0\le s\le A$, consisting of the points with the highest values of $u$ and satisfying $|F_s|=s$. At plateau values resolve ties by any nested measurable ordering within the corresponding hole union. Such an ordering exists because Lebesgue measure is atomless; for example, cut each plateau by a coordinate whose distribution has no atoms. Then $F_A=G$ up to null sets, and

$$
|S\triangle F_B|=|I\triangle(0,B)|\le4\sqrt{\pi\delta}.
\tag{17}
$$

Indeed each plateau occupies exactly its interval in (13) in the rank parameter. Equation (17) is a measure identity and asserts no regularity of an artificial cut through a plateau.

## 4. A smooth calibration with a movable center

The next lemma is the only quantitative geometric input beyond the isoperimetric inequality.

**Lemma 4.1.** Fix $0<r_0<r_1<\infty$. There is a smooth compactly supported field $X:\mathbb R^2\to\mathbb R^2$, with $|X|\le1$ and $X(x)=x$ on $\partial B_1$, with the following properties. Write

$$
X_{\rho,z}(x)=X((x-z)/\rho),\qquad
\mathcal E_z(E)=\int_{\partial^*E}(1-X_{\rho,z}\cdot\nu_E),
$$

where $|E|=\pi\rho^2$, $r_0\le\rho\le r_1$, and $\nu_E$ is the outer normal. Put $d_I=P(E)^2-4\pi^2\rho^2$. There is a center $y$ such that

$$
\mathcal E_y(E)+|E\triangle B_\rho(y)|^2\le C d_I.
\tag{18}
$$

Moreover, there are positive $q_*,\eta_*$ such that, if $q_z=|E\triangle B_\rho(z)|\le q_*$ and $d_I\le\eta_*$, then

$$
\mathcal E_z(E)\le C(d_I+q_z^2).
\tag{19}
$$

All constants depend only on $r_0,r_1$.

**Proof.** Hensel and Laux [HL, Theorem 1 and Lemma 3] prove (18), after scaling, for their Lipschitz calibration

$$
X^0(x)=g(|x|)\frac{x}{|x|},\qquad g(s)=[1-(1-s)^2]_+.
$$

We have changed their inward-normal convention to outward normals. Their global theorem applies to every finite-perimeter set of prescribed measure; no confinement or barycenter hypothesis is imposed. To obtain the required smoothness, let

$$
f(s)=\begin{cases}
\exp\!\left(-\dfrac{(s-1)^2}{s(2-s)}\right),&0<s<2,\\
0,&s=0\text{ or }s\ge2,
\end{cases}
\qquad X(x)=f(|x|)\frac{x}{|x|},\quad X(0)=0.
\tag{20}
$$

The field is smooth at the origin and at its support boundary. We have $f(1)=1$, $f'(1)=0$, and $1-f\le C(1-g)$. The last inequality follows from Taylor expansion near one and compactness away from one. For $a\in[-1,1]$ it implies $1-fa\le C(1-ga)$: for $a\ge0$ split off $1-a$, and for $a<0$ use the bounds one and two. Thus smoothing preserves domination of the relative energy at the center supplied by [HL], proving (18). Approximate minimizing centers suffice if necessary; when $d_I=0$, isoperimetric rigidity gives a disk.

The lens estimate for equal-radius disks gives, for sufficiently small $q_*,\eta_*$,

$$
|z-y|\le C\bigl(q_z+\sqrt{d_I}\bigr).
\tag{21}
$$

To verify its use, the triangle inequality bounds the disk-to-disk symmetric difference by $q_z+C\sqrt{d_I}$. Below a fixed fraction of $\pi r_0^2$, that difference is bounded below by a positive constant times the distance between centers, uniformly over the radius interval.

Gauss-Green gives $\mathcal E_z(E)=P(E)-\int_E\operatorname{div}X_{\rho,z}$. Since $\mathcal E_y(B_\rho(y))=0$,

$$
\begin{aligned}
\mathcal E_z(E)-\mathcal E_y(E)
={}&\mathcal E_z(B_\rho(y))\\
&+\int(\chi_E-\chi_{B_\rho(y)})
\operatorname{div}(X_{\rho,y}-X_{\rho,z}).
\end{aligned}
\tag{22}
$$

Let $d=|z-y|$. The first term is $O(d^2)$. On the reference sphere its integrand and first center derivative vanish: the radial derivative of $f$ is zero at one, and the derivative of the radial unit direction is tangential. The bounded second derivatives give a uniform Taylor estimate. The bulk term is bounded by $Cd|E\triangle B_\rho(y)|$, because the divergence has a uniformly bounded spatial derivative. Equations (18), (21) and (22) prove (19). $\square$

The smoothing step matters here: translating the divergence of the original merely Lipschitz calibration would not justify the same uniform first-order bulk estimate.

## 5. Transport over a prescribed interval of areas

We prove a window statement that will also supply the universal constant in (6).

**Proposition 5.1.** If $B\le a<b\le A$, there is a center $z$ such that

$$
\sup_{s\in[a,b]}|F_s\triangle B_{\sqrt{s/\pi}}(z)|
\le C(b/a)\sqrt\delta.
\tag{23}
$$

**Proof.** Set $r_0=\sqrt{a/\pi}$, $r_1=\sqrt{b/\pi}$ and $E_\rho=F_{\pi\rho^2}$. Outside the plateau ranks, $E_\rho=\{u>t(\rho)\}$. At regular radii let $w=-t'(\rho)$. Equations (9)-(12) give

$$
0<w\le\rho/2,\qquad \ell w=2\pi\rho,\qquad m=\pi\rho^2.
\tag{24}
$$

By changing variables in $J$, we obtain

$$
J=\frac1{4\pi}\int_{\mathrm{act}}(D_H+D_I)w\,d\rho
=\int_{\mathrm{act}}\pi\rho^2(\rho/2-w)\,d\rho\le\delta.
\tag{25}
$$

Here $\mathrm{act}$ denotes all nonplateau radii in $(0,R)$. The plateau intervals are excluded in both integrals; they are already accounted for by $K$.

Within $[r_0,r_1]$ the plateau set $\mathcal P$ has length at most $C\sqrt\delta$, by (16) and $a\ge B$. Call an active radius bad if either $w<r_0/4$, or $w\ge r_0/4$ and $D_I>\eta_*$, with $\eta_*$ from Lemma 4.1. The second expression in (25) bounds the measure of the first bad set by $C\delta$; the first expression bounds that of the second by $C\delta$. On the remaining good set $\mathcal G$,

$$
|\mathcal P|\le C\sqrt\delta,\qquad
|\mathcal B|\le C\delta,\qquad
\int_{\mathcal G}(D_H+D_I)\,d\rho\le C\delta.
\tag{26}
$$

Nonregular nonplateau radii form a null set, as discussed after (11).

Fix temporarily a center $z$, and let $q(\rho)=|E_\rho\triangle B_\rho(z)|$. Nestedness gives

$$
|q(\rho)-q(\sigma)|\le2\pi|\rho^2-\sigma^2|
\le4\pi r_1|\rho-\sigma|.
\tag{27}
$$

This unconditional Lipschitz bound applies also inside the artificially ordered plateaus.

At a regular active radius the outward normal velocity is $V=w/|\nabla u|$. Compare the changing level with the flow of the frozen field $X_{\rho,z}$. On the comparison disk the field has normal component one, so its flow agrees with radial expansion to first order. Along the compact regular level, tubular coordinates and the implicit function theorem give

$$
|E_{\rho+h}\triangle\Phi_h(E_\rho)|
=|h|\int_{\partial E_\rho}|V-X_{\rho,z}\cdot\nu|+o(|h|).
$$

The Jacobian of $\Phi_h$ differs from one by $O(|h|)$ globally. Comparing both sets after the same flow and using the reverse triangle inequality for their symmetric-difference distances proves, at differentiability radii,

$$
|q'(\rho)|\le Cq(\rho)+
\int_{\partial E_\rho}|V-X_{\rho,z}\cdot\nu|.
\tag{28}
$$

The argument works for both signs of $h$ and differentiates no intersection of boundaries. It is a bounded-field version of the level-set comparison underlying [GMR, Lemma 3.2].

Let $P=P(E_\rho)$ and $\overline V=2\pi\rho/P\le1$. A direct expansion, using $\int V=2\pi\rho$ and $\int|\nabla u|=\pi\rho^2$, gives

$$
\int\frac{(V-\overline V)^2}{V}
=\frac{2\pi\rho}{P^2}D_H,
\qquad
\int|V-\overline V|\le\frac{2\pi\rho}{P}\sqrt{D_H}\le\sqrt{D_H}.
\tag{29}
$$

This is the velocity-oscillation estimate used in [GMR]. Since $X_{\rho,z}\cdot\nu\le1$, Lemma 4.1 gives on good radii, as long as $q\le q_*$,

$$
\begin{aligned}
\int|V-X_{\rho,z}\cdot\nu|
&\le\sqrt{D_H}+(P-2\pi\rho)+\mathcal E_z(E_\rho)\\
&\le\sqrt{D_H}+CD_I+Cq^2.
\end{aligned}
$$

Therefore

$$
|q'|\le Cq+\sqrt{D_H}+CD_I
\quad\text{on }\mathcal G\text{ while }q\le q_*.
\tag{30}
$$

For sufficiently small $\delta$, the good set has length at least $(r_1-r_0)/2$. Equation (26) supplies a good radius $\rho_0$ with $D_I(\rho_0)\le C\delta$. Choose the center from (18) at this radius, so that $q(\rho_0)\le C\sqrt\delta$. Keep this center fixed.

Integrate (30) in both directions from $\rho_0$. Cauchy-Schwarz and (26) bound its inhomogeneous term by $C(\sqrt\delta+\delta)$. On the bad and plateau sets use (27); their total contribution has the same bound. Gronwall's inequality consequently yields

$$
\sup_{[r_0,r_1]}q\le C\sqrt\delta.
\tag{31}
$$

To justify the smallness assumption in (30), first work on the component containing $\rho_0$ of the set $\{q<q_*\}$. Choose the deficit threshold so that the right side of (31) is below $q_*/2$. Continuity excludes an interior endpoint of that component. If $\delta=0$, the same argument starts at a zero-deficit regular level and has zero forcing. For deficits above the threshold, use $q\le2b$ and enlarge the constant.

Finally rescale $x$ by $\sqrt{\pi/a}$. The lower radius becomes one, the upper radius becomes $\sqrt{b/a}$, symmetric differences scale quadratically, and $\sqrt\delta$ scales in the same way. Thus the constant depends only on $b/a$. $\square$

## 6. Proof of the stability inequalities

Apply Proposition 5.1 to $[B,A]$. At its upper endpoint $F_A=G$, while (17) identifies $F_B$ with the hole union up to $4\sqrt{\pi\delta}$. The triangle inequality proves

$$
\mathfrak a(G,S)\le C(A/B)\sqrt\delta,
$$

which is (5).

For (6), assume $B\le2A/3$. Apply Proposition 5.1 separately to $[2A/3,A]$ and $[B,3B/2]$. Both windows have ratio $3/2$. The first gives $A\alpha(G)\le C\sqrt\delta$. The second, combined with (17), gives $B\alpha(S)\le C\sqrt\delta$. These two applications may use different centers, exactly as permitted by the individual Fraenkel asymmetries. Squaring and adding proves (6) with an absolute constant.

## 7. Optimality of the exponent

Fix $0<r<R$, and for small real $\varepsilon$ define a smooth star-shaped hole by

$$
S_\varepsilon=\{te_\theta:0\le t<\sqrt{r^2+2r\varepsilon\cos(2\theta)}\},
\qquad \Omega_\varepsilon=B_R\setminus\overline{S_\varepsilon}.
\tag{32}
$$

Its area is exactly $\pi r^2$.

We compute the deficit to second order by an energy identity. For physical torsion on a smooth single-hole domain, put $h=u+|x|^2/4$ on $\Omega$ and $I(E)=\int_E|x|^2$. Extending $u$ constantly through the hole and integrating by parts gives

$$
\int_\Omega|\nabla h|^2=\frac14I(\Omega)-T(\Omega).
\tag{33}
$$

The function $h$ minimizes the Dirichlet integral among functions with outer trace $|x|^2/4$ and inner trace $|x|^2/4+d$, where $d$ is free. Indeed, for a variation with zero outer trace and constant inner trace, (7) cancels its pairing with $x/2$.

Subtract $R^2/4$ from $h$. In (32) its outer trace is zero and its inner trace is $r\varepsilon\cos(2\theta)/2+d$. A radial map from the fixed annulus to $\Omega_\varepsilon$, linear in the radial coordinate between the two boundaries and preserving the angle, has derivative $\mathrm{Id}+O(|\varepsilon|)$. The pulled-back Dirichlet matrices are consequently bounded between $(1-C|\varepsilon|)\mathrm{Id}$ and $(1+C|\varepsilon|)\mathrm{Id}$. Taking infima over the same traces and the free constant shows that the perturbed minimum differs from the fixed-annulus minimum by a relative $O(|\varepsilon|)$.

Write $L=\log(R/r)$. In logarithmic polar coordinates $s\in[0,L]$, the harmonic mode with inner value $G\cos(k\theta)$ and zero outer value is

$$
G\frac{\sinh(k(L-s))}{\sinh(kL)}\cos(k\theta).
$$

Its energy is $\pi k\coth(kL)G^2$, by integration of the boundary term $[HH']_0^L$. The constant inner mode is orthogonal to it and is minimized at zero. With $k=2$ and $G=r\varepsilon/2$, the minimum is $\pi r^2\varepsilon^2\coth(2L)/2$. Direct polar integration also gives $I(S_\varepsilon)-I(B_r)=\pi r^2\varepsilon^2$. Equation (33) therefore yields

$$
\delta_\varepsilon=
\frac{\pi r^2}{4}\bigl(2\coth(2L)+1\bigr)\varepsilon^2
+O(|\varepsilon|^3).
\tag{34}
$$

For clarity, the lower bound on asymmetry is also checked. We have $|S_\varepsilon\triangle B_r|=4r|\varepsilon|$. Any disk center giving an error of this order must satisfy $|z|=O(|\varepsilon|)$, by the triangle inequality and the lens lower bound. Its translated radial boundary is $r+z\cdot e_\theta+O(|z|^2)$, uniformly in angle. Hence

$$
|S_\varepsilon\triangle B_r(z)|
=r\int_0^{2\pi}|\varepsilon\cos(2\theta)-z\cdot e_\theta|\,d\theta
+O(\varepsilon^2).
\tag{35}
$$

Testing the integrand against $\cos(2\theta)$ bounds the integral below by $\pi|\varepsilon|$, because first and second harmonics are orthogonal. Thus $\alpha(S_\varepsilon)$ is bounded above and below by positive multiples of $|\varepsilon|$.

For the annular asymmetry, a minimizing common center tends to zero: translated fixed annuli escaping to infinity have a fixed positive discrepancy, and the limiting concentric annulus has a unique center. For centers near zero, the inner and outer boundary collars are disjoint, so the annular symmetric difference is the sum of the discrepancies at the two boundaries. The outer disk term forces $|z|=O(|\varepsilon|)$ for any center giving an $O(|\varepsilon|)$ error. Equation (35) then gives the same lower bound for $\beta(\Omega_\varepsilon)$. This also works if the two comparison disk centers are allowed to vary separately, since their boundary collars remain disjoint near a minimizing configuration.

Together with (34), these estimates exclude every power less than two. For (6) choose any fixed ratio satisfying $B\le2A/3$. This completes the proof of Theorem 1.1. $\square$

## 8. Further questions

The proof gives constants uniform in the number of holes and in the geometry of the outer domain. It does not determine the best constants. Nor does it give a joint-center constant uniform as the prescribed ratio tends to either endpoint. Such limiting regimes require additional analysis.

The argument also suggests stability questions for nonlinear physical torsion and for nonconstant loads. The simple first-moment penalty for plateau ranks in (15) and the velocity normalization in (24) use the planar linear equation. Extending the transport estimate alone does not establish either nonlinear or higher-dimensional analogues.

## References

[AB] V. Amato and L. Barbato, *On the stability of the annulus for the torsion of multiply connected domains*, Calculus of Variations and Partial Differential Equations **65** (2026), article 199. DOI: [10.1007/s00526-026-03362-w](https://doi.org/10.1007/s00526-026-03362-w). Final article, published June 10, 2026; related preprint arXiv:2506.07592v2.

[BDPV] L. Brasco, G. De Philippis and B. Velichkov, *Faber-Krahn inequalities in sharp quantitative form*, Duke Mathematical Journal **164** (2015), 1777-1831. DOI: [10.1215/00127094-3120167](https://doi.org/10.1215/00127094-3120167). Author final version available from [CVGMT](https://cvgmt.sns.it/paper/2161/).

[GMR] A. Guerra, J. M. Machado and J. P. G. Ramos, *On the effective sharp stability of the Faber-Krahn inequality*, [arXiv:2609.07772v1](https://arxiv.org/abs/2609.07772v1), September 7, 2026.

[HL] S. Hensel and T. Laux, *The quantitative isoperimetric inequality: A calibration argument*, [arXiv:2606.17172v1](https://arxiv.org/abs/2606.17172v1), June 15, 2026.

[PW] G. Pólya and A. Weinstein, *On the torsional rigidity of multiply connected cross-sections*, Annals of Mathematics **52** (1950), 154-163. Historical attribution as cited in [AB]; the qualitative inequality also follows from (15).
