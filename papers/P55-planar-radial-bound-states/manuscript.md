# A planar comparison argument for radial bound states

Research draft prepared for Henry Zweiman

September 17, 2026

**Working proof reconstruction; independent mathematical review pending.** This manuscript reconstructs the planar comparison method of Cortázar, García-Huidobro, and Yarur, with explicit treatment of the origin and the infinite endpoint. Zhang and Zhang [ZZ26, Section 6] also explicitly claim the full planar extension in a June 2026 preprint. This manuscript is not presented as a first proof or an independently reviewed resolution of an open problem.

## Abstract

We give a planar shooting argument for uniqueness of radial bound states of $\Delta u-u+|u|^{p-1}u=0$, for each $p>1$ and each prescribed number of zeros. The argument uses the inverse-branch comparison functionals introduced by Cortázar, García-Huidobro, and Yarur. In dimension two the auxiliary term used to initialize their induction is constant. We instead initialize at a common solution level. At the infinite endpoint we retain a positive gap between weighted energy quantities, rather than pass a strict radius inequality to a limit. The comparison is transferred through each successive extremum and yields a one-sided shooting separation near every bound state. An elementary interval argument gives uniqueness. Existence is taken from the established prescribed-node existence theorem. Energy estimates then complete the classification of all positive-central shots. The whole-plane conclusion is already stated in the 2011 theorem and is also covered by the planar extension claimed by Zhang and Zhang in 2026; this reconstruction makes no first-proof claim.

## 1. Statement and relation to earlier work

Fix a real number $p>1$. Write

$$
f(s)=|s|^{p-1}s-s,\qquad
F(s)=\frac{|s|^{p+1}}{p+1}-\frac{s^2}{2},\qquad
\beta=\left(\frac{p+1}{2}\right)^{1/(p-1)}.
$$

Thus $\beta>1$, $F(\pm\beta)=0$, $F<0$ on $(-\beta,\beta)\setminus\{0\}$, and $F>0$ outside $[-\beta,\beta]$. Let $u(r,\alpha)$ solve

$$
u''+\frac1r u'+f(u)=0,\qquad u(0,\alpha)=\alpha>0,
\qquad u'(0,\alpha)=0. \tag{1.1}
$$

A bound state is a nonzero solution tending to zero as $r\to\infty$. A node means a zero in $(0,\infty)$, and the central value is normalized to be positive.

**Theorem 1.1 (the conclusion addressed by this draft).** For every $p>1$ and every integer $k\geq0$, there is exactly one $\alpha_k>0$ for which $u(\cdot,\alpha_k)$ is a bound state with exactly $k$ nodes. Moreover,

$$\beta<\alpha_0<\alpha_1<\alpha_2<\cdots,$$

and, for every $k\geq0$, the shot $u(\cdot,\alpha)$ has at least $k+1$ nodes if and only if $\alpha>\alpha_k$.

**Corollary 1.2 (classification of the remaining shots).** The sequence in Theorem 1.1 satisfies $\alpha_k\to\infty$. If $0<\alpha<\alpha_0$ and $\alpha\ne1$, the shot is positive, is bounded away from zero, and oscillates about $1$. If $\alpha=1$, it is identically $1$. If $\alpha\in(\alpha_k,\alpha_{k+1})$, it has exactly $k+1$ nodes and, after its last zero, oscillates about $(-1)^{k+1}$ and stays bounded away from zero in absolute value. Each bound state satisfies $u'/u\to-1$ on its final tail and $|u(r)|=O(e^{-\mu r})$ for every $0<\mu<1$.

This is a whole-plane statement. No uniqueness theorem for a prescribed finite disk and no nondegeneracy theorem is asserted here.

Theorem 1.1 of Cortázar, García-Huidobro, and Yarur [CGY11] already states uniqueness for every node count in the planar power case. Their example following that theorem explicitly includes $f(s)=s^p-s^q$ on the positive half-line, $p>q>0$, in dimension two. Tang [T] proves a substantially stronger collection of conclusions in dimensions $n\geq3$ and conjectures a planar extension. These source statements must be distinguished: the present work does not establish that the whole-plane uniqueness statement was previously open.

Our functionals $Q$ and $W$ and the extremum-by-extremum organization come from [CGY11, Section 4]. Two endpoint details motivate the reconstruction. First, the strict inequality involving $H$ in [CGY11, p. 614, Proposition 4.3] becomes an equality when $n=2$. Second, strict finite-level comparisons require additional justification at a decaying endpoint. We give a common-level initialization and a quantitative tail argument. We do not identify either issue with any previously reported correction; no such mathematical correction has been verified in this audit.

Zhang and Zhang [ZZ26, Section 6] explicitly claim that Tang's Theorems 1 and 2 extend to $n=2$, $p>1$, using a different comparison of Tang's variation-dependent quantities. We checked both versions of their preprint: the planar section remains text-identical in v1 and v2, even though its announcement was removed from the v2 abstract. Thus the latest version retains that claim. This source was overlooked in the initial audit of the present draft and is now explicitly credited. The present proof is a reconstruction of [CGY11], not a verification of every dependency of [ZZ26].

## 2. Elementary shooting facts

The integral form of (1.1) is

$$
u(r)=\alpha-\int_0^r t\log(r/t)f(u(t))\,dt. \tag{2.1}
$$

Since $f\in C^1(\mathbb R)$, contraction on a sufficiently small interval gives the regular solution and its $C^1$ dependence on $\alpha$. The kernel has integral $r^2/4$. In particular,

$$u(r)=\alpha-\frac{f(\alpha)}4r^2+o(r^2).$$

Continuation away from zero is the usual ODE continuation. The energy

$$E(r)=\frac12u'(r)^2+F(u(r))$$

satisfies

$$E'(r)=-\frac{u'(r)^2}{r}. \tag{2.2}$$

As $F$ is bounded below and tends to infinity with $|s|$, both $u$ and $u'$ are bounded. Thus every shot exists for all $r\geq0$. Every zero at positive radius is simple: a double zero would imply the identically zero solution by ODE uniqueness.

If $E(R)<0$ at a finite radius, the solution has no subsequent zero. We call this a finite negative-energy witness. If $0<\alpha\leq\beta$, energy becomes negative at a positive radius unless the shot is the constant $1$, whose energy is already negative. Therefore all bound states and all shots with a node have $\alpha>\beta$.

**Lemma 2.1 (the last lobe).** Suppose that a shot has no zero after some radius. Either it has a finite negative-energy witness, or it is a bound state. In the latter case $u$, $u'$, and $u''$ decay exponentially. A bound state has only finitely many nodes, its energy is strictly positive at every finite radius, and each of its nonzero-radius critical points is nondegenerate with $|u|>\beta$.

*Proof.* By reflection suppose the solution is positive after its last zero. Assume that $E(r)\geq0$ there. At a critical point one has $F(u)\geq0$, so $u\geq\beta$, $f(u)>0$, and $u''=-f(u)<0$. Every such critical point is a strict maximum; consequently there is at most one. The solution is eventually monotone and has a limit $\ell\geq0$.

Boundedness of $u''$ away from the origin makes $u'$ uniformly continuous. Monotonicity and boundedness of $u$ imply integrability of $|u'|$, hence $u'\to0$. The equation then shows that $f(\ell)=0$: otherwise $u''$ would tend to a nonzero constant. Since the limiting energy is nonnegative, $\ell=1$ is impossible. Thus $\ell=0$ and the solution is eventually decreasing.

For completeness, choose $R$ so that $0<u(r)<1$ for $r\geq R$ and $1-u(r)^{p-1}\geq\lambda^2>0$. For $0<\mu<\lambda$, comparison for

$$L=\frac{d^2}{dr^2}+\frac1r\frac d{dr}-\lambda^2$$

with $u(R)e^{-\mu(r-R)}$ gives $u(r)\leq u(R)e^{-\mu(r-R)}$. Indeed, $Lu\geq0$, the comparison function has strictly negative $L$-image, and a positive interior maximum of their difference is impossible; the difference tends to zero at infinity. Also $(ru')'=r(u-u^p)>0$ on this tail. Its increasing negative value has limit zero, since a negative limit would force a logarithmically divergent decrease of $u$. Therefore

$$-ru'(r)=\int_r^\infty t(u(t)-u(t)^p)\,dt,$$

which gives exponential decay of $u'$; the equation gives the same for $u''$.

For any solution tending to zero, $u'\to0$ by the same boundedness and uniform-continuity argument, and hence $E\to0$. Equation (2.2) makes $E(r)>0$ at every finite radius. Eventually $|u|<1$. Two consecutive zeros in that region would enclose a positive maximum or a negative minimum, contradicting $u''=-f(u)$ at that extremum. Thus there are only finitely many zeros. Positivity of energy at a critical point gives $|u|>\beta$, and $f(u)\ne0$ gives nondegeneracy. $\square$

A $k$-node bound state has precisely $k$ critical points at positive radius. To see this, on a positive lobe every critical point is a strict maximum and on a negative lobe every critical point is a strict minimum. Rolle's theorem and decay supply the required extrema, and there cannot be two on the same lobe. Write their radii as

$$0=c_0<c_1<\cdots<c_k.$$

The solution is strictly monotone on each $(c_i,c_{i+1})$ and on $(c_k,\infty)$. All finite extrema and nodes persist continuously under sufficiently small changes of $\alpha$; on a fixed compact interval around them energy stays positive.

## 3. Intersections near a bound state

Let $u_*(r)=u(r,\alpha_*)$ be a bound state and put

$$v(r)=\partial_\alpha u(r,\alpha_*) .$$

Differentiating (2.1) and then the ODE gives

$$v''+\frac1r v'+f'(u_*)v=0,\qquad v(0)=1,\quad v'(0)=0. \tag{3.1}$$

Every zero of $v$ at positive radius is simple.

**Lemma 3.1 (intersections on each monotone part).** The variation $v$ has a zero in each $(c_i,c_{i+1})$ and in $(c_k,\infty)$. Consequently there is a neighborhood $J$ of $\alpha_*$ such that, for every two distinct parameters $\alpha_1,\alpha_2\in J$, their shots intersect on each pair of corresponding monotone parts, including the final positive-amplitude tail after reflection.

*Proof.* On a monotone part let $w$ equal $u_*'$ or $-u_*'$ so that $w>0$. Differentiating (1.1) gives

$$w''+\frac1r w'+\left(f'(u_*)-\frac1{r^2}\right)w=0.$$

If $v$ had no interior zero, change its sign so that $v>0$ there. Then

$$J(r)=r(w'v-wv'),\qquad J'(r)=\frac{wv}{r}>0. \tag{3.2}$$

On a finite part, $w$ vanishes at both endpoints, $w'$ is positive at the first and negative at the second. Thus $J$ is nonnegative at the first endpoint and nonpositive at the second, a contradiction. At $c_0=0$ use $w=O(r)$, bounded $v,v'$, and $J(0)=0$.

On the last part the same identity gives $J(r)\geq d>0$ after any fixed interior radius. Once $|u_*|<1$, reflection makes the tail positive and decreasing, and $w=-u_*'>0$ satisfies $w'<0$ and $(rw)'=rf(u_*)<0$. In particular $rw$ is bounded above. If $v$ stayed positive, (3.2) would imply

$$v'=\frac{w'}w v-\frac{J}{rw}\leq-\frac d{rw}\leq-d_1<0,$$

which is impossible for a positive function on the entire tail.

Around a simple zero of $v$ in each part choose fixed radii $a_i<b_i$ with opposite signs of $v$. Uniform continuous dependence of $\partial_\alpha u$ preserves those signs for all parameters in one sufficiently small neighborhood. For $\alpha_1<\alpha_2$,

$$u(r,\alpha_2)-u(r,\alpha_1)=\int_{\alpha_1}^{\alpha_2}\partial_\alpha u(r,a)\,da$$

has opposite signs at $a_i,b_i$. These radii remain inside both corresponding monotone parts. This proves the intersection claim. For the final part choose $a_k,b_k$ finite and after the last extremum, where the reflected reference solution is positive. $\square$

## 4. Planar comparison identities

On a decreasing monotone branch use $s=u(r)$ as the independent variable and write

$$r=r(s),\qquad t(s)=-u'(r(s))>0,\qquad q(s)=r(s)t(s)>0.$$

Then

$$r_s=-\frac rq=-\frac1t,\qquad q_s=-\frac{r^2f(s)}q. \tag{4.1}$$

On either of the outer intervals $|s|\geq\beta$, put $R(s)=F(s)/f(s)$ and define

$$Q(s)=4R(s)q(s)-q(s)^2-2r(s)^2F(s). \tag{4.2}$$

At a finite extremum take the continuous value $Q=-2r^2F(s)$. Direct differentiation gives

$$Q_s=4R'(s)q(s). \tag{4.3}$$

In particular $Q_s>0$ on the interior of either outer interval. To check this for every $p>1$, let $x=s^{p-1}$ for $s\geq\beta$ and $y=x-(p+1)/2\geq0$. Then

$$R'(s)=\frac{2y^2+p(p-1)y+(p-1)^2(p+1)/2}{2(p+1)(x-1)^2}>0. \tag{4.4}$$

Oddness of $R$ makes $R'$ even. Notice that $Q$ is used only on the outer intervals; no division by $f$ at $s=0$ or $s=\pm1$ is required.

Where energy is positive, also define

$$W(s)=r(s)\sqrt{t(s)^2+2F(s)}=\sqrt{q(s)^2+2r(s)^2F(s)}.$$

Here the inverse-branch identities give

$$W_s=\frac{-2F(s)}{t(s)\sqrt{t(s)^2+2F(s)}}. \tag{4.5}$$

**Lemma 4.1 (comparison across the inner interval).** Suppose two decreasing branches have positive energy, $F\leq0$ between levels $L\leq U$, and

$$r_1(U)\geq r_2(U),\qquad W_2(U)-W_1(U)=\delta>0.$$

Throughout their common continuation from $U$ down to $L$ while both have positive energy,

$$r_1(s)>r_2(s),\qquad t_1(s)<t_2(s),\qquad W_2(s)-W_1(s)\geq\delta \quad(s<U). \tag{4.6}$$

*Proof.* The hypotheses imply $W_1/r_1<W_2/r_2$, hence $t_1<t_2$. At a fixed $s$, writing $a=-2F(s)\geq0$, the function

$$h(t)=\frac{a}{t\sqrt{t^2-a}},\qquad t>\sqrt a,$$

is nonincreasing; for $a>0$ its derivative is

$$h'(t)=-\frac{a(2t^2-a)}{t^2(t^2-a)^{3/2}}<0.$$

Thus $(W_2-W_1)_s=h(t_2)-h(t_1)\leq0$, and $(r_1-r_2)_s=-1/t_1+1/t_2<0$. Since $s$ is decreasing along the continuation, the energy gap does not decrease and the radius gap increases. A first failure of the inequalities is therefore impossible. The relation between $W/r$ and $t$ keeps the slope inequality strict. $\square$

The constant $\delta$ is essential: the conclusion at an infinite-radius endpoint will follow from this bound, not from continuity of a strict radius inequality.

## 5. Transfer from one extremum to the next

Fix a bound state. Shrink its parameter neighborhood so that all the finite extrema, positive energies, and intersections of Lemma 3.1 persist. Consider corresponding decreasing parts of two nearby shots, with starting maxima $M_1<M_2$ and next minima $m_1,m_2<-\beta$. Their starting maxima exceed $\beta$.

For an interior starting maximum we will assume

$$Q_1(M_1)>Q_2(M_2). \tag{5.1}$$

For the first part, starting at radius zero, the central values satisfy $M_j=\alpha_j$, and both $Q_j(M_j)$ are zero. This first part is treated separately in the initialization below.

**Lemma 5.1 (extremum transfer).** In either the interior case (5.1) or the origin case $\alpha_1<\alpha_2$, one has

$$m_1>m_2,\qquad Q_1(m_1)>Q_2(m_2). \tag{5.2}$$

*Proof.* We first establish the common-level initial conditions

$$r_1(M_1)<r_2(M_1),\qquad Q_1(M_1)>Q_2(M_1). \tag{5.3}$$

In the interior case, (4.3) and (5.1) give the second inequality. By shrinking the neighborhood, uniformly for the nearby pair we have

$$0<q_2(M_1)<4R(M_1).$$

Indeed, both maxima approach the same nondegenerate reference maximum, so $q_2(M_1)\to0$ while $R(M_1)$ tends to a positive number. At $s=M_1$, $q_1=0$ and

$$Q_1-Q_2=q_2(q_2-4R)+2F(M_1)(r_2^2-r_1^2).$$

Its positivity forces $r_2>r_1$.

At the origin, $r_1(M_1)=0<r_2(M_1)$. Equation (4.3), applied along the second shot between $M_1$ and $M_2$, gives

$$Q_2(M_1)<Q_2(M_2)=0=Q_1(M_1). \tag{5.4}$$

This supplies (5.3) without any strict comparison at the two distinct central levels.

Let $s_I$ be the first inverse-radius intersection encountered while decreasing $s$ from $M_1$. Such an intersection exists by Lemma 3.1. Before it, $r_1<r_2$; at it, $r_1=r_2>0$ and $q_1<q_2$. To justify the strict slope order, the first-contact derivative gives $q_1\leq q_2$, and equality would give identical values and derivatives at the same radius, contradicting distinct central parameters.

We next find a level $U\leq-\beta$ at which

$$r_1(U)\geq r_2(U),\qquad q_1(U)<q_2(U),\qquad Q_1(U)>Q_2(U). \tag{5.5}$$

There are three cases.

**Case 1: $s_I\geq\beta$.** From just below $M_1$ until the first intersection, $q_1<q_2$. Otherwise, at its first equality while $r_1<r_2$, (4.1) gives

$$ (q_1-q_2)_s=\frac{f(s)(r_2^2-r_1^2)}q>0.$$

At a first zero reached from negative values as $s$ decreases, the derivative must be nonpositive, a contradiction. Therefore (4.3) shows that $Q_1-Q_2$ increases as $s$ descends to $s_I$ and remains strictly positive there.

After the intersection, the inequalities $r_1>r_2$ and $q_1<q_2$ continue down to $\beta$. As long as they hold, $(r_1-r_2)_s<0$ and $(Q_1-Q_2)_s<0$. At a hypothetical first equality of $q_1,q_2$ at $s>\beta$, one would have

$$Q_1-Q_2=-2F(s)(r_1^2-r_2^2)<0,$$

contrary to the positive gap. Equality at $s=\beta$ would give $Q_1-Q_2=0$ and is also impossible. At $\beta$, $W_j=q_j$, so Lemma 4.1 carries $r_1>r_2$ and $W_1<W_2$ down to $-\beta$. At that level $Q_j=-q_j^2$ and $W_j=q_j$, which proves (5.5) with $U=-\beta$.

**Case 2: $-\beta\leq s_I\leq\beta$.** At the intersection, equal radii and $q_1<q_2$ give $W_1<W_2$. Lemma 4.1 takes this directly to $-\beta$, again giving (5.5). If $s_I=-\beta$, no propagation is needed.

**Case 3: $s_I<-\beta$.** Take $U=s_I$. At equal radii,

$$Q_1-Q_2=(q_1-q_2)(4R-q_1-q_2)>0,$$

because $R<0$ and $q_1<q_2$. Thus (5.5) holds.

For $s<U$, continue until one of the two minima is reached. On this outer negative interval, $F>0$ and $R'>0$. Starting from (5.5), the inequalities $r_1>r_2$ and $q_1<q_2$ persist: the radius difference increases as $s$ decreases, the $Q$ difference is bounded below by its positive value at $U$, and equality of the $q$'s would give the same contradiction $Q_1-Q_2=-2F(r_1^2-r_2^2)<0$.

The first endpoint must therefore be the first shot's minimum, with $m_1>m_2$ and $q_2(m_1)>0$. In detail, if the second shot reached its minimum first, the limiting slope order would force both $q$'s to vanish there. If the minima had equal levels the same would occur. In either case the positive $Q$ gap would contradict its extremal value $-2F(r_1^2-r_2^2)\leq0$.

Finally $Q_1(m_1)>Q_2(m_1)$, while $Q_2(m_1)>Q_2(m_2)$ by (4.3). This proves (5.2). $\square$

Reflection preserves the comparison quantity: under $u\mapsto-u$, $F$ is unchanged and both $F/f$ and $u'$ change sign in the expression $-4(F/f)ru'-r^2u'^2-2r^2F$. Thus (5.2), after reflection, is precisely (5.1) for the next decreasing part, with starting maxima $-m_1<-m_2$.

**Corollary 5.2 (ordered finite extrema).** Near any $k$-node bound state, for every pair $\alpha_1<\alpha_2$ the absolute amplitudes of corresponding extrema satisfy

$$|u(c_i(\alpha_1),\alpha_1)|<|u(c_i(\alpha_2),\alpha_2)|\quad(0\leq i\leq k).$$

For $i\geq1$ the corresponding extremal $Q$ values satisfy the strict order needed in (5.1) after reflection.

*Proof.* Use the origin case of Lemma 5.1 for the first part and its interior case after each reflection. Only finitely many neighborhoods are involved; take their common intersection. $\square$

## 6. The infinite endpoint

Consider the final parts of two shots near a $k$-node bound state. Reflect both if necessary so their corresponding final extrema are positive maxima. Corollary 5.2 gives $M_1<M_2$ and the appropriate $Q$ order. For $k=0$ use (5.4). The same initialization as in Lemma 5.1 gives (5.3).

By Lemma 3.1 the two final decreasing parts intersect at a positive level. At their first inverse-radius intersection $s_I>0$, the order is $q_1<q_2$. If $s_I>\beta$, Case 1 of Lemma 5.1, stopped at $\beta$, gives a strict $W$ order there. If $s_I\leq\beta$, it gives the $W$ order at $s_I$ itself. Consequently there is a level $U\in(0,\beta]$ for which

$$r_1(U)\geq r_2(U),\qquad W_2(U)-W_1(U)=\delta>0. \tag{6.1}$$

The intervening branches have positive energy. If the intersection exceeds $\beta$, the branches cannot stop before $\beta$: energy cannot vanish where $F>0$, a decreasing positive solution cannot have a first minimum where $f>0$, and a monotone asymptote above $\beta$ is impossible since $f$ has no zero there. The positive energy at the remaining finite part is ensured by the chosen neighborhood of the reference bound state.

For $0<s<U$, Lemma 4.1 now gives

$$W_2(s)-W_1(s)\geq\delta \tag{6.2}$$

on the common positive-energy continuation. For any bound-state endpoint Lemma 2.1 yields

$$W(s)=r(s)\sqrt{u'(r(s))^2+2F(s)}\longrightarrow0\qquad(s\downarrow0). \tag{6.3}$$

Indeed $0<W^2=2r^2E\leq r^2u'^2$ once $F\leq0$, and $ru'\to0$ exponentially.

**Proposition 6.1 (local shooting separation).** If $u(\cdot,\alpha_*)$ is a $k$-node bound state, there is $\varepsilon>0$ such that:

- $\alpha_*<\alpha<\alpha_*+\varepsilon$ implies at least $k+1$ nodes;
- $\alpha_*-\varepsilon<\alpha<\alpha_*$ implies exactly $k$ nodes and a finite negative-energy witness.

*Proof.* All nearby shots retain the first $k$ nodes and their next extremum. Compare $\alpha_1=\alpha_*$ with $\alpha_2>\alpha_*$. The first shot's final branch exists with positive energy at every level $s\in(0,U]$. The second shot cannot be the first to lose positive energy: at a positive level this would give $W_2=0$ while (6.2) gives $W_2\geq\delta$. Nor can it turn before this happens, because a first positive minimum has negative energy. An infinite monotone endpoint at a positive level would have to be the equilibrium $1$, with negative limiting energy, and hence would also have an earlier negative-energy witness. Thus the second branch reaches zero, either at finite radius or as a bound state. The latter is excluded by (6.2)-(6.3). It crosses zero at finite radius, giving the next node.

Now compare $\alpha_1<\alpha_*$ with $\alpha_2=\alpha_*$. If the first shot continued with positive energy at every level down to zero, (6.2) and $W_1\geq0$ would contradict $W_2\to0$. A positive monotone asymptote without earlier energy loss is impossible as above. Hence the first shot reaches zero energy at a positive level and finite radius. Immediately afterwards its energy is negative by (2.2). It cannot acquire another node, so it has exactly $k$. $\square$

## 7. The interval argument and existence

Set $N_0=(\beta,\infty)$ and, for $j\geq1$, let $N_j$ be the set of central values whose shots have at least $j$ nodes. Define $G_k$ to be the set giving a $k$-node bound state and $P_k$ to be the set of $\alpha\in N_k$ giving exactly $k$ nodes together with a finite negative-energy witness. Lemma 2.1 gives the disjoint partition

$$N_k=N_{k+1}\;\dot\cup\;G_k\;\dot\cup\;P_k. \tag{7.1}$$

The set $N_j$ is open because its defining finitely many simple zeros persist. The set $P_k$ is open because both its $k$ zeros and a subsequent finite negative-energy witness persist; after that witness there can be no further zero. Proposition 6.1 says that every point of $G_k$ has a left neighborhood in $P_k$ and a right neighborhood in $N_{k+1}$.

We use the following elementary fact. Suppose an interval $I$ is partitioned into $P\dot\cup G\dot\cup N$, with $P,N$ open in $I$, and every $g\in G$ has a left neighborhood in $P$ and a right neighborhood in $N$. If $g\in G$, then

$$P=I\cap(-\infty,g),\qquad N=I\cap(g,\infty),\qquad G=\{g\}. \tag{7.2}$$

To prove it, take the component of $N$ immediately to the right of $g$. If it ended at a point $b\in I$, that point could belong neither to $N$ nor to the open set $P$. It would belong to $G$, but would have $N$ immediately to its left, contradicting its required left neighborhood in $P$. Hence the component extends to the right endpoint of $I$. The analogous argument for the component of $P$ to the left of $g$ proves (7.2).

For existence with prescribed positive node count, apply [CGY13, Theorem 1.1] with $N=m=2$. Its hypotheses are verified as follows. The function $f$ is continuous and locally Lipschitz, $\beta^\pm=\pm\beta$, and $\gamma^\pm=\pm\infty$. The two limits of $F$ at infinity are both infinite. The quantity called $Q$ in that existence theorem (different from (4.2)) is $Q_{\rm ex}(s)=4F(s)$. Fix $\theta\in(0,1)$. For all sufficiently large $s>0$, uniformly for $s_1,s_2\in[\theta s,s]$,

$$4F(s_2)\frac{s}{f(s_1)}\geq c s^{p+1}\frac{s}{s^p}=cs^2\longrightarrow\infty.$$

The corresponding negative-side condition follows by oddness of $f$ and evenness of $F$. The finite-$\gamma$ conditions are vacuous. Thus for every $k\geq1$ the existence theorem supplies a $k$-node state, and reflection makes its central value positive.

In particular $N_1$ is nonempty. At $\alpha=\beta$ the nonconstant shot has negative energy at any sufficiently small positive radius, and by continuity an interval immediately to the right of $\beta$ lies in $P_0$. Since the interval $N_0$ cannot be partitioned into the two nonempty disjoint open sets $P_0$ and $N_1$, (7.1) gives $G_0\ne\varnothing$. Applying (7.2) on $N_0$ gives a unique $\alpha_0\in G_0$ and $N_1=(\alpha_0,\infty)$.

Inductively suppose $N_k=(\alpha_{k-1},\infty)$. Existence gives $G_k\ne\varnothing$; applying (7.2) to (7.1) gives $G_k=\{\alpha_k\}$ and $N_{k+1}=(\alpha_k,\infty)$. Since $G_k\subset N_k$, one has $\alpha_k>\alpha_{k-1}$. This proves Theorem 1.1. $\square$

## 8. Completion of the shooting classification

We give the energy details needed for Corollary 1.2. The finite-zero argument is the planar specialization of the weighted-energy method in [T, Proposition 2.4]; it is included to make the classification independent of an unstated global nodal assumption.

**Lemma 8.1 (finitely many nodes for every shot).** Every solution of (1.1) has only finitely many zeros.

*Proof.* Suppose otherwise. All zeros are simple and do not accumulate at a finite radius, so they can be listed as $z_i\to\infty$. The decreasing energy has a limit $E_\infty\geq0$, since $E(z_i)=u'(z_i)^2/2>0$. In particular $E(r)>0$ for every finite $r$. Between consecutive zeros there is exactly one critical point, with amplitude greater than $\beta$, as in Section 2.

Fix a positive bound $D$ for $|u'|$ and write $c=f(\beta)>0$. The function $f$ is increasing on $[\beta,\infty)$, and so $|f(u)|\geq c$ when $|u|\geq\beta$. For sufficiently large $r$, the damping term has absolute value at most $c/2$. On each such outer arc, $u''$ has sign opposite to $u$ and absolute value at least $c/2$. Each arc between an extremum and the level $|u|=\beta$ therefore has length at most $2D/c$.

First suppose $E_\infty>0$. Between the two outer arcs joining consecutive extrema, the solution traverses from $\beta$ to $-\beta$, or conversely. On that inner portion, $F\leq0$ and $|u'|\geq\sqrt{2E_\infty}$. Its length is at most $2\beta/\sqrt{2E_\infty}$. Thus consecutive extrema are separated by at most

$$C=\frac{4D}{c}+\frac{2\beta}{\sqrt{2E_\infty}}.$$

After indexing these late parts by $i$, their right endpoints are at most $C_0+iC$. The energy loss on each inner portion is at least

$$\int\frac{|u'|^2}{r}\,dr\geq\frac{\sqrt{2E_\infty}}{C_0+iC}\int |u'|\,dr
=\frac{2\beta\sqrt{2E_\infty}}{C_0+iC}.$$

Summation contradicts the bounded total energy loss.

Now suppose $E_\infty=0$. Set $H(r)=r^2E(r)$, so that

$$H'(r)=2rF(u(r)). \tag{8.1}$$

Consider a sufficiently late complete lobe $(z_i,z_{i+1})$, with extremum at $a_i$. The portion where $F>0$ has length at most $C_1=4D/c$, and $F(u)\leq F(u(a_i))=E(a_i)$. On the decreasing-amplitude side choose $d_i<e_i$ at which $|u(d_i)|=1$ and $|u(e_i)|=1/2$. Then $e_i-d_i\geq1/(2D)$, and $F(u)\leq F(1/2)<0$ throughout $[d_i,e_i]$. The positive-$F$ portion is entirely to the left of $d_i$. All other contributions in (8.1) are nonpositive. Consequently,

$$\frac{H(z_{i+1})-H(z_i)}2
\leq d_i\left(C_1E(a_i)+\frac{F(1/2)}{2D}\right).$$

For all sufficiently large $i$, $C_1E(a_i)\leq-F(1/2)/(4D)$. Hence

$$H(z_{i+1})-H(z_i)\leq\frac{d_iF(1/2)}{2D}<0.$$

Since $d_i\to\infty$, these losses are eventually bounded above by a fixed negative constant. This forces $H(z_i)<0$ for some $i$, contrary to $H(z_i)>0$. Both cases are impossible. $\square$

**Lemma 8.2 (oscillation on a trapped tail).** If a nonconstant shot has negative energy at a finite radius, then on its subsequent fixed-sign tail it is bounded away from zero and oscillates about the equilibrium of that sign.

*Proof.* Reflect so that $u>0$ after a radius $R$ with $E(R)<0$. From $F(u(r))\leq E(r)\leq E(R)<0$, its values lie in a compact interval $[a,b]\subset(0,\beta)$. Define the positive continuous function

$$A(s)=\begin{cases}f(s)/(s-1),&s\ne1,\\p-1,&s=1.\end{cases}$$

It has a positive lower bound on $[a,b]$. The substitution $y(r)=\sqrt r\,(u(r)-1)$ gives

$$y''+\left(A(u(r))+\frac1{4r^2}\right)y=0. \tag{8.2}$$

The function $y$ cannot have a fixed nonzero sign on any final interval. For if $y>0$ there, then $y''\leq-a_0y$ for a constant $a_0>0$. Once $y'<0$, concavity forces a zero in finite time. If $y'$ stayed nonnegative, $y$ would have a positive lower bound, forcing $y''$ to be bounded above by a negative constant and eventually making $y'<0$. Reflection treats $y<0$. Thus $u$ crosses $1$ infinitely often. These crossings are simple, since $u=1$, $u'=0$ would give the constant solution. Between consecutive crossings there is exactly one extremum: above $1$ all critical points are strict maxima, and below $1$ all are strict minima. The reflected assertion follows. $\square$

*Proof of Corollary 1.2.* If the increasing sequence $\alpha_k$ were bounded above by a finite $L$, any $\alpha>L$ would belong to every $N_j$, by Theorem 1.1. This would give infinitely many nodes, contrary to Lemma 8.1. Thus $\alpha_k\to\infty$.

For $\alpha\in(\alpha_k,\alpha_{k+1})$, Theorem 1.1 gives membership in $N_{k+1}$ and exclusion from $N_{k+2}$. There are exactly $k+1$ nodes. The shot is not a bound state, since the unique state with that count is at $\alpha_{k+1}$. Lemmas 2.1 and 8.2 now give the asserted oscillatory tail. The same argument gives a positive oscillatory shot when $\beta<\alpha<\alpha_0$; the initial energy argument in Section 2 treats $0<\alpha\leq\beta$, excluding the constant solution. Positivity on the initial compact interval and the trapped-tail lower bound give $\inf_{r\geq0}u(r)>0$ in this case.

Finally, reflect a bound state's last tail to be positive and put $\eta=-u'/u>0$. It obeys

$$\eta'=\eta^2-\frac\eta r-1+u^{p-1}. \tag{8.3}$$

For $r\geq2$, if $\eta$ ever reached $2$, it would thereafter satisfy $\eta'\geq\eta^2/2$ and blow up in finite time, impossible since $u>0$ on the whole tail. Thus eventually $0<\eta<2$, and (8.3) becomes $\eta'=\eta^2-1+o(1)$. For any fixed $\delta\in(0,1)$ and sufficiently large $r$, reaching $1+\delta$ would force continued increase and a subsequent value $2$; reaching $1-\delta$ from above, or starting below it, would force continued decrease and a subsequent value $0$. Both are impossible. Hence $\eta\to1$. The exponential estimates for any $0<\mu<1$ follow from Lemma 2.1 by taking $R$ sufficiently large that $1-u^{p-1}>\mu^2$. $\square$

## 9. Audit and scope

The proof uses the existence theorem [CGY13], standard local ODE theory, and the elementary arguments written above. It does not invoke the uniqueness conclusion of [CGY11] or the higher-dimensional uniqueness theorem of [T]. Its comparison quantities and organizing strategy are nevertheless those of [CGY11].

The two explicit additions are (5.4), replacing a planar initialization that is not strict at distinct central levels, and (6.2), retaining a positive gap before taking a decaying limit. The proposed proof requires independent mathematical checking, especially of Lemma 5.1 and Proposition 6.1. The accompanying computation checks seven algebraic identities in the comparison and classification arguments. It does not verify the ODE comparison or the theorem.

No inference about spectral nondegeneracy, stability, soliton resolution, or finite-disk uniqueness is drawn from Theorem 1.1. Those require additional arguments. The exact overlap with [CGY11] and the retained planar-extension claim in [ZZ26] preclude presenting the statement here as a first announced solution. Whether a distinct proof or a precise correction warrants publication is a separate assessment from mathematical correctness.

## References

[CGY11] C. Cortázar, M. García-Huidobro, and C. S. Yarur, *On the uniqueness of sign changing bound state solutions of a semilinear equation*, Annales de l'Institut Henri Poincaré C, Analyse non linéaire **28** (2011), 599-621. [DOI: 10.1016/j.anihpc.2011.04.002](https://doi.org/10.1016/j.anihpc.2011.04.002).

[CGY13] C. Cortázar, M. García-Huidobro, and C. S. Yarur, *On the existence of sign changing bound state solutions of a quasilinear equation*, [arXiv:1208.0017v2](https://arxiv.org/abs/1208.0017v2), Theorem 1.1. The version cited is the explicit primary source used for the hypotheses checked in Section 7.

[T] M. Tang, *Uniqueness of bound states to $\Delta u-u+|u|^{p-1}u=0$ in $\mathbb R^n$, $n\geq3$*, Inventiones mathematicae **243** (2026), 245-291. [DOI: 10.1007/s00222-025-01379-0](https://doi.org/10.1007/s00222-025-01379-0).

[ZZ26] C. Zhang and X. Zhang, *Uniqueness of bound states for sublinear elliptic equations*, [arXiv:2606.17840v2](https://arxiv.org/abs/2606.17840v2), June 27, 2026, Section 6. The planar section was compared with v1, submitted June 16, 2026, and remains unchanged.

## Preparation note

This working manuscript was drafted with OpenAI Codex as part of Henry Zweiman's research investigation. Its status is an unreviewed proof reconstruction. It has not received external peer review and has not been admitted as a new paper in the research program's publication ledger.
