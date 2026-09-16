# Heat-content maximization on compact metric graphs at every time

Henry Zweiman

September 15, 2026

## Abstract

Among finite compact connected metric graphs of prescribed total length with a nonempty Dirichlet vertex set and standard conditions elsewhere, the interval with one Dirichlet and one Neumann endpoint maximizes heat content at every positive time. Equality at a single positive time characterizes this interval, up to subdivision. This answers the all-times question of Bifulco and Täufer. We prove the stronger statement that heat evolution on any such graph is dominated in cumulative decreasing rearrangement by mixed-boundary interval evolution of the rearranged initial datum. The argument combines the classical metric-graph level-set inequality with the zero-order elliptic concentration comparison and implicit-time iteration of parabolic symmetrization. The rigidity proof uses the half-time energy identity and strict edgewise concavity of the heat evolution of the constant function. No arithmetic condition on the edge lengths is imposed.

**Keywords:** metric graph; heat content; rearrangement; concentration comparison; Faber-Krahn inequality; rigidity.

**Mathematics Subject Classification (2020):** 35K05, 34B45, 49Q10.

## 1. Introduction and main results

Let $\Gamma$ be a finite compact connected metric graph, with positive edge lengths and total length $L>0$. Let $D$ be a nonempty subset of its vertices. We assume that $\Gamma\setminus D$ is connected. The Laplacian has Dirichlet conditions at $D$ and standard continuity and Kirchhoff conditions at every other vertex. A standard condition at a vertex of degree one is a Neumann condition. Loops and multiple edges are permitted; degrees and Kirchhoff sums count edge incidences, so a loop contributes twice.

Write $A_\Gamma$ for the nonnegative realization of $-d^2/dx^2$ and $S_\Gamma(t)=e^{-tA_\Gamma}$. Its heat content is

$$
Q_\Gamma(t)=\int_\Gamma S_\Gamma(t)1\,dx.
\tag{1}
$$

We compare $\Gamma$ to $I_L=(0,L)$, with Neumann condition at $0$ and Dirichlet condition at $L$. Denote the corresponding operator, semigroup and heat content by $A_I$, $S_I(t)$ and $Q_I(t)$.

**Theorem 1.1 (heat-content maximization and rigidity).** For every graph described above and every $t>0$,

$$
Q_\Gamma(t)\le Q_I(t).
\tag{2}
$$

Equality for one positive time holds if and only if $\Gamma$ is a path of length $L$, $D$ consists of one endpoint, and all other vertices have standard conditions. Equivalently, after suppressing vertices of degree two, the graph is the Dirichlet-Neumann interval. In particular, for every other admissible graph the inequality is strict at every positive time.

For a nonnegative measurable function $f$ on a space of length $L$, let $f^*$ be its decreasing rearrangement on $(0,L)$, and set

$$
\mathcal C_f(s)=\int_0^s f^*(r)\,dr,
\qquad 0\le s\le L.
\tag{3}
$$

We write $f\preccurlyeq g$ if $\mathcal C_f(s)\le\mathcal C_g(s)$ for all $s$. Equality of total integrals is not part of this definition. Thus the order is weak submajorization, also called concentration order in the parabolic comparison literature.

**Theorem 1.2 (concentration comparison).** Let $0\le f\in L^2(\Gamma)$ and let $0\le g\in L^2(0,L)$ be nonincreasing. If

$$
\mathcal C_f(s)\le\int_0^s g(r)\,dr
\quad\text{for every }s\in[0,L],
\tag{4}
$$

then, for every $t>0$,

$$
\mathcal C_{S_\Gamma(t)f}(s)
\le\int_0^s S_I(t)g(r)\,dr
\quad\text{for every }s\in[0,L].
\tag{5}
$$

The interval function on the right is nonnegative and nonincreasing. In particular, one may take $g=f^*$.

Taking $f=g=1$ and $s=L$ proves the inequality in Theorem 1.1. Its one-time equality assertion needs an additional argument and is proved in Section 5.

### 1.1. Relation to earlier work

Bifulco and Täufer [BT, Theorem 2.6] prove the interval comparison for sufficiently large times, and for sufficiently small times when the edge lengths are rationally dependent. Their final Remark 2.9 leaves the comparison at every positive time open. Theorem 1.1 resolves that question without a restriction on edge lengths or on the time. The graph, vertex conditions and total-length normalization here agree with their Definitions 2.1 and 2.2. Their comparison interval is written with its Dirichlet endpoint at $0$; reflection gives our convention.

Bifulco and Mugnolo [BM] derive a heat-content formula, short-time asymptotics and surgery principles for compact quantum graphs. Their Section 6 includes comparisons under imposing Dirichlet conditions, taking subgraphs and attaching pendant graphs, as well as heat-content-preserving constructions. These are a different set of comparisons from (5), which rearranges arbitrary initial data and compares graphs of the same total length. We use the ordinary Kirchhoff heat semigroup studied in that work.

The geometric rearrangement input is classical. In the proof of [F, Lemma 3], Friedlander uses the number of points in a regular level set to compare the graph Dirichlet energy to the energy of a monotone rearrangement on an interval. That proof also explains how equality in level multiplicity excludes branching. We give the relevant calculation because the zero-order term of the resolvent equation must be retained.

The passage from elliptic concentration comparison to parabolic comparison by implicit-time discretization is likewise classical. Vázquez [V, Sections 5 and 7] develops precisely this strategy for Euclidean equations; see in particular the zero-order comparison and the parabolic iteration in the author's available text. We adapt that mechanism to the mixed-boundary graph problem. Neither the level-set Cauchy-Schwarz inequality nor implicit Euler iteration is asserted to be new. The contribution is the all-times graph comparison (5), its answer to [BT, Remark 2.9], and the one-time rigidity theorem. The elementary consequences in Section 6 are included as applications of the same result.

## 2. Graph forms and rearrangement preliminaries

The measure on $\Gamma$ is the sum of Lebesgue measures on the edges; vertices have measure zero. The closed quadratic form of $A_\Gamma$ is

$$
\mathfrak a_\Gamma[u]=\sum_{e}\int_0^{\ell_e}|u_e'(x)|^2\,dx,
\qquad
\mathcal D(\mathfrak a_\Gamma)
=\{u\in H^1(\Gamma):u|_D=0\}.
\tag{6}
$$

Here $H^1(\Gamma)$ consists of edgewise $H^1$ functions continuous at the vertices. The operator domain consists of edgewise $H^2$ functions in the form domain satisfying the Kirchhoff sum at each vertex outside $D$. The same construction on $I_L$, with form domain $\{v\in H^1(0,L):v(L)=0\}$, gives $A_I$.

Both operators are nonnegative and self-adjoint, with compact resolvent. They are strictly positive: if $p\in D$, integration along a simple path from $p$ to any point gives

$$
|u(x)|^2\le L\,\mathfrak a_\Gamma[u],
\qquad
\|u\|_2^2\le L^2\mathfrak a_\Gamma[u].
\tag{7}
$$

The truncations $u\mapsto u_+$ and $u\mapsto\min\{1,\max\{u,0\}\}$ preserve the form domain and do not increase its energy. The resolvents and semigroups are therefore positivity preserving and sub-Markovian. In particular,

$$
0\le S_\Gamma(t)1\le1,
\qquad
0\le S_I(t)1\le1.
\tag{8}
$$

We recall two elementary rearrangement facts. For nonnegative $f\in L^1$ on a nonatomic space of length $L$,

$$
\mathcal C_f(s)=\sup_{|E|=s}\int_E f,
\qquad
\sup_{0\le s\le L}|\mathcal C_f(s)-\mathcal C_h(s)|
\le\|f-h\|_1.
\tag{9}
$$

The supremum formula follows by filling a superlevel set of $f$ and, if necessary, part of one level set. The second assertion follows by comparing the integrals on each candidate set. Also,

$$
\|f^*-h^*\|_{L^2(0,L)}\le\|f-h\|_{L^2(\Gamma)}
\tag{10}
$$

for nonnegative $f,h$. Indeed, Hardy-Littlewood gives $\int_\Gamma fh\le\int_0^L f^*h^*$, while rearrangement preserves the two squared norms. Expanding the squared distances proves (10).

**Lemma 2.1 (a Lipschitz rearrangement).** Suppose $u\ge0$ is continuous on $\Gamma$, vanishes at $D$, and is Lipschitz on every edge, with maximum edge Lipschitz constant $K$. Then $u^*$ has a Lipschitz representative on $[0,L]$ with Lipschitz constant at most $K$, and $u^*(L)=0$.

**Proof.** The case $K=0$ is immediate. Choose a maximum point and a simple path from it to $D$. For $0\le c_1<c_2\le\max u$, this path contains a subarc along which $u$ passes from $c_2$ to $c_1$ while remaining between those values. The length of that subarc is at least $(c_2-c_1)/K$. The path is simple, so its length is counted without multiplicity in the graph measure. Consequently

$$
|\{c_1<u<c_2\}|\ge\frac{c_2-c_1}{K}.
\tag{11}
$$

This inverse-distribution estimate gives the Lipschitz assertion; jumps of the distribution due to plateaus correspond to constant portions of the rearrangement and cause no difficulty. Finally, continuity at a Dirichlet vertex shows that the essential infimum is zero. Hence the representative has $u^*(L)=0$. $\square$

## 3. Resolvent concentration comparison

For $h>0$, put

$$
R_h=(1+hA_\Gamma)^{-1},
\qquad B_h=(1+hA_I)^{-1}.
\tag{12}
$$

**Lemma 3.1 (the interval resolvent).** If $g\ge0$ is nonincreasing and belongs to $L^2(0,L)$, then $v=B_hg$ is nonnegative and nonincreasing. With $V(s)=\int_0^s v$ and $G(s)=\int_0^s g$,

$$
-hV''+V=G,
\qquad V(0)=0,\qquad V'(L)=0.
\tag{13}
$$

If $g_1,g_2$ are two such functions and $\int_0^s g_1\le\int_0^s g_2$ for all $s$, then $\int_0^s B_hg_1\le\int_0^s B_hg_2$ for all $s$.

**Proof.** First let $g$ be smooth on $[0,L]$. The equation is $-hv''+v=g$, with $v'(0)=0$ and $v(L)=0$. Positivity of the resolvent gives $v\ge0$, hence $v'(L)\le0$. Its derivative $q=v'$ satisfies

$$
-hq''+q=g'\le0,\qquad q(0)=0,\quad q(L)\le0.
\tag{14}
$$

Testing against $q_+$ gives $q\le0$. Every nonnegative nonincreasing $L^2$ function can be approximated in $L^2$ by smooth nonnegative nonincreasing functions: first truncate, then extend by constant endpoint values and mollify. Boundedness of $B_h$ on $L^2$ passes the conclusion to the limit; the cone of nonincreasing functions is closed in $L^2$.

Integration of the resolvent equation from $0$ to $s$, using $v'(0)=0$, proves (13). This remains valid for $L^2$ data because $v\in H^2$. For the last assertion, the difference $W=V_1-V_2$ satisfies $-hW''+W\le0$, $W(0)=0$ and $W'(L)=0$. Thus

$$
h\int_0^L|(W_+)'|^2+\int_0^L|W_+|^2\le0,
\tag{15}
$$

and $W\le0$. $\square$

**Lemma 3.2 (graph resolvent comparison).** For every $0\le f\in L^2(\Gamma)$,

$$
\mathcal C_{R_hf}(s)\le\int_0^s B_h(f^*)(r)\,dr
\quad(0\le s\le L).
\tag{16}
$$

Consequently, if $g$ satisfies the hypotheses and concentration bound of Theorem 1.2, then

$$
\mathcal C_{R_hf}(s)\le\int_0^s B_hg(r)\,dr.
\tag{17}
$$

**Proof.** We first suppose that on every closed edge the load $f$ is a strictly positive nonconstant polynomial. Loads need not be continuous across vertices. The solution $u=R_hf$ satisfies

$$
-hu_e''+u_e=f_e
\tag{18}
$$

on each edge, so it extends analytically past both endpoints as an edgewise function. It is strictly positive outside $D$. For completeness, a zero interior minimum contradicts (18) and $f_e>0$. At a non-Dirichlet vertex with value zero, all outgoing derivatives would be nonnegative, and their Kirchhoff sum would make them all zero. Equation (18) would then give a negative second derivative into each incident edge at that endpoint, contradicting nonnegativity. This proves the positivity assertion.

The function $u$ cannot be constant on an edge, because (18) would force $f$ to be constant there. Each edge therefore has only finitely many critical points: its derivative is analytic on a neighborhood of the closed edge and is not identically zero. Exclude their values and all vertex values. For every remaining $c\in(0,\max u)$, write

$$
E_c=\{u>c\},\quad \mu(c)=|E_c|,\quad
N(c)=\#\{u=c\},
\quad a(c)=\sum_{u=c}|u'|,\quad
b(c)=\sum_{u=c}\frac1{|u'|}.
\tag{19}
$$

All sums run over interior edge points. Continuity along a path from a maximum to $D$ gives $N(c)\ge1$. Define $U=\mathcal C_u$ and $F=\mathcal C_f$. Integration of (18) over $E_c$ gives

$$
ha(c)+U(\mu(c))=\int_{E_c}f\le F(\mu(c)).
\tag{20}
$$

To check the sign and vertex terms, the derivative pointing out of a superlevel interval is $-|u'|$ at a regular boundary point. At a vertex contained in $E_c$, continuity puts all incident edge germs in $E_c$, and their fluxes cancel by Kirchhoff. No Dirichlet vertex belongs to $E_c$. These observations give exactly the positive flux term on the left of (20).

The one-dimensional coarea formula and inverse differentiation give

$$
-\mu'(c)=b(c),\qquad
U''(\mu(c))=(u^*)'(\mu(c))=-\frac1{b(c)}.
\tag{21}
$$

Cauchy-Schwarz, in the form already used for graph rearrangement in [F], yields

$$
a(c)b(c)\ge N(c)^2\ge1.
\tag{22}
$$

Combining (20)-(22), we obtain

$$
-hU''+U\le F.
\tag{23}
$$

There is no omitted singular part in (23). The function $u^*$ is Lipschitz by Lemma 2.1, so $U\in W^{2,\infty}(0,L)$. There are no plateaus of $u$, and hence the finitely many exceptional levels yield only finitely many exceptional ranks $\mu(c)$. Thus the displayed inequality holds almost everywhere and in the weak sense. Its boundary data are

$$
U(0)=0,\qquad U'(L)=0.
\tag{24}
$$

By Lemma 3.1, the cumulative integral $V$ of $B_h(f^*)$ satisfies the equality in (23), with the same boundary data. The positive-part test (15) proves $U\le V$.

To remove the polynomial assumption, approximate an arbitrary nonnegative $L^2$ load by strictly positive nonconstant polynomials on every closed edge. Such loads are dense: separately on each edge, approximate first by a nonnegative continuous function, then uniformly by a polynomial, adding a vanishing positive constant to ensure strict positivity. A vanishing linear perturbation makes a constant polynomial nonconstant while preserving positivity. There are only finitely many edges.

For an approximating sequence $f_n\to f$ in $L^2$, resolvent boundedness and (10) give

$$
R_hf_n\to R_hf,\qquad
B_h(f_n^*)\to B_h(f^*)
\quad\text{in }L^2.
\tag{25}
$$

Finite total length converts these to $L^1$ convergences, and (9) passes the cumulative inequality to the limit. This proves (16). Finally apply Lemma 3.1 to the decreasing interval data $f^*$ and $g$ to obtain (17). $\square$

The comparison retains the zero-order term in (18). Dropping that term would give a Poisson comparison, which does not by itself iterate to the required heat inequality.

## 4. Passage to the heat semigroup

**Proof of Theorem 1.2.** Fix $h>0$ and define

$$
u_0=f,\quad u_j=R_hu_{j-1},\qquad
v_0=g,\quad v_j=B_hv_{j-1}.
\tag{26}
$$

All these functions are nonnegative, and every $v_j$ is nonincreasing by Lemma 3.1. The hypothesis at $j=0$ and (17) give inductively

$$
\mathcal C_{u_j}(s)\le\int_0^s v_j(r)\,dr
\quad(0\le s\le L,\ j\ge0).
\tag{27}
$$

For a fixed $t>0$, take $h=t/n$ and $j=n$. The spectral theorem gives

$$
\left(1+\frac tn A_\Gamma\right)^{-n}f\longrightarrow S_\Gamma(t)f,
\qquad
\left(1+\frac tn A_I\right)^{-n}g\longrightarrow S_I(t)g
\quad\text{in }L^2.
\tag{28}
$$

Indeed, $(1+t\lambda/n)^{-n}\to e^{-t\lambda}$ for every $\lambda\ge0$, and both multipliers are bounded by one. Dominated convergence in the spectral measure proves (28). Passing to the limit in (27) by (9) proves (5), uniformly in $s$. Closedness of the cone of nonincreasing functions gives the remaining monotonicity assertion. $\square$

This is the classical implicit-time strategy of [V], with the graph resolvent inequality supplied by Section 3. In particular, no differentiability of a time-dependent rearrangement and no assumption about regular heat levels are needed to prove the inequality.

## 5. Equality at a single time

The proof of rigidity uses the constant initial datum. Put

$$
w(t)=S_\Gamma(t)1,\qquad z(t)=S_I(t)1.
\tag{29}
$$

We first record a strict regularity property of this particular heat evolution.

**Lemma 5.1 (strict edgewise concavity).** For every $t>0$, the function $w(t)$ is smooth on the closure of each individual edge, positive outside $D$, and

$$
-w_e''(t,x)=A_\Gamma w(t,x)>0
\quad(0<x<\ell_e).
\tag{30}
$$

Consequently, each open edge has at most one critical point of $w(t)$ and has no constant subinterval.

**Proof.** Spectral smoothing gives $w(t)\in\mathcal D(A_\Gamma^m)$ for every integer $m\ge1$. Repeated use of the edge equation for the operator gives edgewise $H^{2m}$ regularity, and hence smoothness up to each endpoint. On a graph connected outside its Dirichlet set, the Kirchhoff heat semigroup is positivity improving on $\Gamma\setminus D$.

Here is a maximum-principle justification of the positivity statement used in this proof. For nonzero nonnegative initial data, positivity preservation and injectivity of $S_\Gamma(t)$ give a nonzero nonnegative profile at positive times. An interior zero at a positive time forces the solution to vanish backwards on that edge by the parabolic strong maximum principle. At a standard vertex where the nonnegative solution has value zero, all outgoing derivatives are nonnegative. Their sum is zero, so every one vanishes; the parabolic boundary point lemma excludes a positive incident edge with zero outgoing derivative. Thus positivity propagates across each standard vertex. Connectivity of $\Gamma\setminus D$ gives positivity throughout the open edges and at its standard vertices. This is the usual strict-positivity property of the connected graph heat kernel; see also the discussion in [BM, Section 1].

Sub-Markovianity and positivity give

$$
w(t+h)=S_\Gamma(t)S_\Gamma(h)1\le S_\Gamma(t)1=w(t)
\quad(h>0).
\tag{31}
$$

Differentiation at positive time in $L^2$ implies $A_\Gamma w(t)=-\partial_t w(t)\ge0$. It is not the zero function: otherwise (7) would give $w(t)=0$, which contradicts positivity. Commutation through the semigroup yields

$$
A_\Gamma w(t)=S_\Gamma(t/2)A_\Gamma w(t/2).
\tag{32}
$$

Positivity improvement applied to the nonzero nonnegative datum on the right proves (30). The final assertion follows because $w_e'$ is strictly decreasing. $\square$

**Lemma 5.2 (equal norms under concentration).** Suppose $a,b\ge0$ belong to $L^2$ on spaces of the same finite measure, $a\preccurlyeq b$, and $\|a\|_2=\|b\|_2$. Then $a^*=b^*$ almost everywhere.

**Proof.** For $c\ge0$ define

$$
H_a(c)=\int(a-c)_+
=\sup_{0\le s\le L}\{\mathcal C_a(s)-cs\}.
\tag{33}
$$

The same formula holds for $b$, so $H_a\le H_b$. Tonelli gives

$$
\|a\|_2^2=2\int_0^\infty H_a(c)\,dc,
\qquad
\|b\|_2^2=2\int_0^\infty H_b(c)\,dc.
\tag{34}
$$

Equality of the norms makes $H_a=H_b$ almost everywhere, and then everywhere by continuity. Their right derivatives are $-|\{a>c\}|$ and $-|\{b>c\}|$, respectively. Thus the distributions agree and so do the rearrangements. $\square$

**Proof of the rigidity assertion in Theorem 1.1.** Self-adjointness and the semigroup law give the half-time identities

$$
Q_\Gamma(t)=\|w(t/2)\|_2^2,
\qquad
Q_\Gamma'(t)=-\mathfrak a_\Gamma[w(t/2)].
\tag{35}
$$

The identical formulas hold on the interval. Suppose $Q_\Gamma(T)=Q_I(T)$ for some $T>0$. Theorem 1.2 at time $T/2$ gives $w(T/2)\preccurlyeq z(T/2)$. Lemma 5.2 and (35) imply

$$
w(T/2)^*=z(T/2)
\quad\text{almost everywhere on }(0,L).
\tag{36}
$$

The differentiable nonnegative function $Q_I(t)-Q_\Gamma(t)$ attains its minimum zero at the interior point $T$, so its derivative vanishes there. Thus (35) gives

$$
\mathfrak a_\Gamma[w(T/2)]
=\mathfrak a_I[z(T/2)]
=\int_0^L|(w(T/2)^*)'|^2.
\tag{37}
$$

Set $u=w(T/2)$ and $M=\max u$. By Lemma 5.1, only finitely many critical or vertex values need be excluded. At all other levels $c\in(0,M)$ use the notation $a(c),b(c),N(c)$ from (19). Lemma 2.1 and one-dimensional coarea yield

$$
\mathfrak a_\Gamma[u]=\int_0^M a(c)\,dc,
\qquad
\int_0^L|(u^*)'|^2=\int_0^M\frac1{b(c)}\,dc.
\tag{38}
$$

The second formula follows from $s=\mu(c)$, $ds=-b(c)dc$ and $(u^*)'(\mu(c))=-1/b(c)$ on every interval between exceptional values. The Lipschitz representative ensures that these identities lose no singular energy. By (22),

$$
a(c)-\frac1{b(c)}\ge\frac{N(c)^2-1}{b(c)}\ge0.
\tag{39}
$$

Equations (37)-(39) force $N(c)=1$ for almost every regular $c$.

Every edge incidence at a Dirichlet vertex has strictly positive derivative into its edge. Indeed, the function is positive inside that edge, zero at its endpoint, and strictly concave; the endpoint derivative is at least any positive chord slope. Therefore, for all sufficiently small positive regular levels,

$$
N(c)\ge\sum_{p\in D}\deg(p).
\tag{40}
$$

The small incident edge neighborhoods can be chosen disjoint, including the two incidences of a loop. It follows that $D$ consists of one vertex and that this vertex has degree one.

Next consider a standard vertex $p$ of degree $d\ge3$. Write $c=u(p)>0$ and let $d_i$ be the derivatives along its outgoing incidences. Kirchhoff gives $\sum_i d_i=0$. Each incidence with $d_i>0$ gives increasing values immediately away from $p$; each incidence with $d_i<0$ gives decreasing values. If $d_i=0$, strict edgewise concavity also gives decreasing values. Thus every incidence is assigned to one of two classes. Since $d\ge3$, one class contains at least two incidences. On the corresponding side of $c$, all sufficiently close regular levels have at least two distinct preimages. This contradicts $N=1$ almost everywhere. No standard vertex can have degree at least three.

A connected finite graph whose degrees are at most two and which has a vertex of degree one is a path. Its unique Dirichlet vertex is an endpoint; its other endpoint is standard and hence Neumann. Suppressing standard degree-two vertices changes neither the metric space nor its Laplacian. This proves necessity. Sufficiency follows by reflection and subdivision invariance of the interval problem. $\square$

The equality argument does not infer strictness from strict resolvent inequalities followed by a limit. Such a limit could erase a positive defect. Instead, equality at the specified time produces the exact energy equality (37).

## 6. Consequences and limits

**Corollary 6.1 (convex temperature functionals).** Under the hypotheses of Theorem 1.2, for every convex nondecreasing function $\Phi:[0,\infty)\to[0,\infty)$ with $\Phi(0)=0$,

$$
\int_\Gamma\Phi(S_\Gamma(t)f)\,dx
\le\int_0^L\Phi(S_I(t)g)\,dx.
\tag{41}
$$

In particular, all $L^p$ norms, $1\le p\le\infty$, are bounded by those of the comparison evolution.

**Proof.** Concentration order implies the stop-loss comparison (33) and the comparison of first moments. Every such convex $\Phi$ is a nonnegative linear function plus an integral of $(r-c)_+$ against its distributional second derivative; approximation applies if necessary. Integrating that representation proves (41). Choosing $\Phi(r)=r^p$ gives finite $p$; passage to the limit gives $p=\infty$. At positive time the profiles are bounded by spectral smoothing and the edge Sobolev embedding. $\square$

The interval bound has the explicit expansion

$$
Q_I(t)=\frac{8L}{\pi^2}\sum_{k=0}^{\infty}
\frac{\exp\!\left(-\frac{(2k+1)^2\pi^2t}{4L^2}\right)}{(2k+1)^2}.
\tag{42}
$$

Indeed, the normalized eigenfunctions are $\sqrt{2/L}\cos((2k+1)\pi x/(2L))$. Their squared integrals are $8L/(\pi^2(2k+1)^2)$, giving (42) by the spectral representation of (1).

**Corollary 6.2 (positive time weights).** Let $\rho:(0,\infty)\to[0,\infty)$ be measurable. Whenever the interval integral is finite,

$$
\int_0^\infty\rho(t)Q_\Gamma(t)\,dt
\le\int_0^\infty\rho(t)Q_I(t)\,dt.
\tag{43}
$$

If $\rho$ is positive on a set of positive measure, equality characterizes the same interval. In particular, choosing $\rho=1$ recovers the sharp torsional-rigidity bound $\int_0^\infty Q_\Gamma(t)dt\le L^3/3$.

**Proof.** Integrate Theorem 1.1 and use its strictness. For the last constant, the interval torsion function solves $-v''=1$, $v'(0)=v(L)=0$, hence $v(x)=(L^2-x^2)/2$ and $\int_0^L v=L^3/3$. $\square$

The torsional comparison itself is prior work; it is discussed in [BT, Remark 2.3] and is not a separate novelty claim here. Similarly, with the diffusion convention that the generator is $d^2/dx^2$ on each edge, $Q_\Gamma(t)/L$ is the survival probability at time $t$ for the killed graph diffusion started from uniform length measure. Theorem 1.1 therefore also says that its lifetime is stochastically dominated by the lifetime on the mixed interval. This is the direct probabilistic interpretation of the heat-content bound, using the Feynman-Kac representation in [BT, Proposition 3.2].

Our conclusions concern unweighted finite metric graphs with the stated Dirichlet and Kirchhoff conditions. They do not provide a heat-trace bound, pointwise heat-kernel domination, or a theorem for arbitrary vertex couplings. We prove no quantitative stability estimate. A useful next problem is to quantify the loss in (2) in terms of geometric distance from a path, with explicit control of the time scale and of edges whose lengths tend to zero. Such a statement requires additional work beyond the qualitative rigidity proved here.

## References

**[BT]** P. Bifulco and M. Täufer, *Faber-Krahn inequality for the heat content on quantum graphs via random walk expansion*, Electronic Journal of Probability **30** (2025), paper no. 158, 1-19. [DOI: 10.1214/25-EJP1414](https://doi.org/10.1214/25-EJP1414). [Preprint arXiv:2501.09693](https://arxiv.org/abs/2501.09693). The final Theorem 2.6 and Remark 2.9 specify the prior result and the all-times question.

**[BM]** P. Bifulco and D. Mugnolo, *On the Heat Content of Compact Quantum Graphs*, Annales Henri Poincaré (2026), published online September 9, 2026. [DOI: 10.1007/s00023-026-01755-3](https://doi.org/10.1007/s00023-026-01755-3). [Preprint arXiv:2502.09461](https://arxiv.org/abs/2502.09461).

**[F]** L. Friedlander, *Extremal properties of eigenvalues for a metric graph*, Annales de l'Institut Fourier **55** (2005), no. 1, 199-211. [DOI: 10.5802/aif.2095](https://doi.org/10.5802/aif.2095). Lemma 3 and its proof contain the energy rearrangement and level-multiplicity argument used here.

**[V]** J. L. Vázquez, *Symmetrization and Mass Comparison for Degenerate Nonlinear Parabolic and Related Elliptic Equations*, Advanced Nonlinear Studies **5** (2005), no. 1, 87-131. [DOI: 10.1515/ans-2005-0107](https://doi.org/10.1515/ans-2005-0107). [Author manuscript, November 25, 2004](https://verso.mat.uam.es/~juanluis.vazquez/SymmJANS04.pdf), Sections 5.2 and 7, especially Theorems 5.2 and 7.3.

## Research transparency

This is an AI-assisted research preprint prepared under Henry Zweiman's name at his request. The proof and the primary-source comparison were audited internally by the originating assistant; no independent expert review or journal acceptance is claimed. The accompanying assessment and source records state the search scope, the source passages inspected and the remaining priority limitations. The mathematical statements above are supported by the displayed arguments, rather than by finite computations or artifact checks.
