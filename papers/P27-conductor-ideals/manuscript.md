# Conductor ideals of C-monoids with prescribed Krull closure

Henry Zweiman

September 9, 2026

## Abstract

Let $`H`$ be a commutative Krull monoid with finite divisor class group. We characterize the ideals of $`H`$ that occur as conductors of C-monoids with complete integral closure $`H`$. For a nonempty proper ideal $`\mathfrak f`$, extend its image under a divisor theory to a monomial ideal $`J`$ in the free divisor monoid. Apart from one elementary unit obstruction, the required condition is finiteness of the family $`(J:p)`$ as $`p`$ ranges over the prime divisors. Equivalently, membership in $`J`$ is determined by finitely many truncated sums of prime valuations. Whenever the condition holds, $`\mathfrak f\cup\{1\}`$ is already a realization. More generally, its unit group can be prescribed as any subgroup of $`H^\times`$ compatible with properness. We give an explicit bound for the reduced class semigroup and examples separating the criterion from finite generation. This answers Problem 19 of Geroldinger, Kim, and Loper.

## 1. Introduction and main result

All monoids are commutative and cancellative, with identity. An ideal of $`H`$ means an $`s`$-ideal: a subset $`I\subseteq H`$ satisfying $`IH=I`$. For a submonoid $`M\subseteq H`$ with the same quotient group, its conductor is
```math
(M:H)=\{x\in\mathsf q(H):xH\subseteq M\}.
```
Since $`1\in H`$, this set is contained in $`M`$. Its complete integral closure is
```math
\widehat M=\{x\in\mathsf q(M):\text{some }c\in M\text{ satisfies }cx^n\in M
                         \text{ for every }n\ge1\}.
```
The notation $`H^\times`$ denotes the unit group.

Geroldinger, Kim, and Loper ask which ideals of a Krull monoid with finite class group can occur as conductors of C-monoids having that complete integral closure [\[2, Problem 19\]](#ref-GKL). Their formulation is purely multiplicative. It differs from the ring-conductor problem with a prescribed subring, studied by Reinhart [\[4\]](#ref-Reinhart): the monoids constructed below need not be closed under addition.

Fix a divisor theory $`\varphi:H\to D=\mathcal F(P)`$. Thus $`D`$ is free abelian on its prime set $`P`$, the map $`\varphi`$ reflects divisibility, and every prime of $`D`$ is the gcd of a finite subset of $`\varphi(H)`$. The image $`K=\varphi(H)`$ is isomorphic to $`H/H^\times`$ and satisfies

<a id="label-eq-saturated"></a>

```math
\tag{1}
 K=\mathsf q(K)\cap D.
```

The divisor class group is $`G=\mathsf q(D)/\mathsf q(K)`$. For an ideal $`\mathfrak f\subseteq H`$, put
```math
J=\varphi(\mathfrak f)D,\qquad (J:p)=\{x\in D:xp\in J\}\quad(p\in P).
```
The criterion below is independent of the chosen divisor theory, since divisor theories are unique up to an isomorphism of their free monoids.

<a id="theorem-1"></a>

**Theorem 1.1.**

<a id="label-thm-main"></a>

Let $`H`$ be a Krull monoid with finite divisor class group, and let $`\mathfrak f`$ be a nonempty proper ideal of $`H`$. The following are equivalent.

1.  There is a C-monoid $`M\subseteq H`$ such that $`\widehat M=H`$ and $`(M:H)=\mathfrak f`$.

2.  The family $`\{(J:p):p\in P\}`$ is finite and $`\mathfrak f\cup\{1\}\ne H`$.

3.  There are a finite partition $`P=P_1\sqcup\cdots\sqcup P_r`$, an integer $`N\ge1`$, and an upward-closed set $`W\subseteq\{0,\ldots,N\}^r`$ such that

    <a id="label-eq-threshold"></a>

    ```math
    \tag{2}
     J=\{a\in D:\tau(a)\in W\},\qquad
     \tau_i(a)=\min\left\{N,\sum_{p\in P_i}v_p(a)\right\},
    ```

    and $`\mathfrak f\cup\{1\}\ne H`$.

Whenever these conditions hold, $`M=\mathfrak f\cup\{1\}`$ is a realization in (1).

<!-- end theorem-1 -->

Every sum in [(2)](#label-eq-threshold) is finite, even when $`P_i`$ is infinite. The unit obstruction is exactly the case where $`H`$ is reduced and $`\mathfrak f=H\setminus\{1\}`$. The whole ideal $`H`$ is realized by $`H`$ itself, and the empty ideal cannot be the conductor of a C-monoid. These statements also cover groups, whose only nonempty ideal is the whole group.

The criterion involves colon ideals for individual primes, not residuals for all monomials. It allows infinite divisor rank and ideals that are not finitely generated. The proof combines the classical dense embedding theorem for C-monoids with an exchange argument on prime factors and Dickson’s lemma. The dense embedding theorem, rather than any seminormality assumption, is the structural input.

## 2. Finite prime profiles of a monomial ideal

For a subset $`X\subseteq D`$, call $`X`$ recognizable if there is a homomorphism $`\eta:D\to S`$ to a finite monoid such that membership in $`X`$ depends only on $`\eta(a)`$. We use this terminology only to connect the ideal criterion with the finite class semigroups below; the proofs are given directly.

<a id="lemma-1"></a>

**Lemma 2.1.**

<a id="label-lem-profiles"></a>

Let $`J`$ be a nonempty proper ideal of $`D=\mathcal F(P)`$. The following are equivalent:

1.  the family $`\{(J:p):p\in P\}`$ is finite;

2.  $`J`$ has a presentation [(2)](#label-eq-threshold);

3.  $`J`$ is recognizable.

<!-- end lemma-1 -->

<a id="proof-1"></a>

**Proof.**

Suppose (1) holds. Define $`p\sim q`$ when $`(J:p)=(J:q)`$, and let $`P_1,\ldots,P_r`$ be the equivalence classes. For every $`x\in D`$,

<a id="label-eq-exchange"></a>

```math
\tag{3}
 xp\in J\quad\Longleftrightarrow\quad xq\in J\qquad(p\sim q).
```

Two monomials with the same number of factors from each $`P_i`$, counted with multiplicity, can be connected by finitely many such replacements. Membership in $`J`$ therefore depends only on the vector
```math
\lambda(a)=\left(\sum_{p\in P_i}v_p(a)\right)_{i=1}^r\in\mathbb N_0^r.
```
This map is surjective. The set $`V=\lambda(J)`$ is upward closed because $`J`$ is an ideal. By Dickson’s lemma, its set $`B`$ of coordinatewise minimal elements is finite. Choose $`N\ge1`$ at least as large as every coordinate of every member of $`B`$. A vector dominates a member of $`B`$ exactly when its coordinatewise truncation at $`N`$ does. Taking $`W=V\cap\{0,\ldots,N\}^r`$ proves (2).

For (2) implies (3), give $`\{0,\ldots,N\}^r`$ coordinatewise truncated addition, $`s\oplus t=(\min\{N,s_i+t_i\})_i`$. The map $`\tau`$ is a monoid homomorphism and recognizes $`J`$.

Finally, if $`\eta:D\to S`$ recognizes $`J`$, then $`\eta(p)=\eta(q)`$ implies $`xp\in J`$ exactly when $`xq\in J`$. There are at most $`|S|`$ prime colon ideals, proving (1). $`\square`$

<!-- end proof-1 -->

The upward-closed hypothesis is essential to the truncation conclusion. Arbitrary recognizable subsets of a free monoid can have periodic conditions. For ideals, increasing exponents cannot destroy membership, and finite prime profiles yield the finite threshold description.

<a id="lemma-2"></a>

**Lemma 2.2.**

<a id="label-lem-upward"></a>

Let $`X\subseteq D`$ be recognized by a finite congruence $`\sim`$, and put $`J=XD`$. If primes $`p,q`$ satisfy $`p\sim q`$, then $`(J:p)=(J:q)`$. In particular, $`J`$ has finitely many prime profiles.

<!-- end lemma-2 -->

<a id="proof-2"></a>

**Proof.**

Suppose $`xp\in J`$, and choose $`a\in X`$ dividing $`xp`$. If $`a`$ divides $`x`$, then $`a`$ also divides $`xq`$, so $`xq\in J`$. Otherwise the distinguished extra occurrence of $`p`$ in $`xp`$ belongs to $`a`$. Write $`a=pb`$ with $`b\mid_D x`$. The monomial $`qb`$ is congruent to $`pb`$, hence lies in $`X`$, and divides $`xq`$. This proves $`xp\in J\Rightarrow xq\in J`$. Interchanging $`p`$ and $`q`$ proves the reverse implication. $`\square`$

<!-- end proof-2 -->

## 3. Necessity from an arbitrary realization

Let $`M\subseteq F=F^\times\times\mathcal F(P)`$ be a submonoid with $`M^\times=M\cap F^\times`$. For $`a,b\in F`$, write $`a\sim_M b`$ if
```math
ax\in M\quad\Longleftrightarrow\quad bx\in M\qquad\text{for every }x\in F.
```
This is a congruence. Its classes represented by $`(F\setminus F^\times)\cup\{1\}`$ form the reduced class semigroup $`\mathcal C^*(M,F)`$. By definition, $`M`$ is a C-monoid if such an embedding exists with $`\mathcal C^*(M,F)`$ finite. The full class semigroup may be infinite because of units.

We use the following classical dense embedding theorem. A C-monoid has a factorial embedding in which it remains a C-monoid and the projection of $`\widehat M`$ to the free factor is a divisor theory. It also has nonempty conductor, and $`\widehat M`$ is Krull with finite class group. These facts are summarized in [\[3, Section 2, equation (2.4)\]](#ref-GZ), from [\[1, Theorems 2.9.11–2.9.12\]](#ref-GHK). They apply to arbitrary C-monoids; seminormality is not a hypothesis.

<a id="proposition-1"></a>

**Proposition 3.1.**

<a id="label-prop-necessary"></a>

Suppose $`M`$ is a C-monoid with $`\widehat M=H`$, and put $`\mathfrak f=(M:H)`$. For every divisor theory $`\varphi:H\to D`$, the set $`\varphi(\mathfrak f)`$ is recognizable in $`D`$. Consequently $`J=\varphi(\mathfrak f)D`$ has finitely many prime profiles.

<!-- end proposition-1 -->

<a id="proof-3"></a>

**Proof.**

Choose a dense factorial embedding $`M\subseteq F=E\times\mathcal F(P')`$ as above. Its extension to the complete integral closure identifies $`H`$ with a submonoid of $`F`$. The projection $`\partial:H\to\mathcal F(P')`$ is a divisor theory. Uniqueness of divisor theories permits us to identify $`\mathcal F(P')`$ with $`D`$ and $`\partial`$ with $`\varphi`$.

Regard elements of $`D`$ as pure monomials in $`F`$. The restriction of $`\sim_M`$ to $`D`$ has finitely many classes: a pure monomial is either $`1`$ or a nonunit of $`F`$, and hence its class lies in $`\mathcal C^*(M,F)`$.

Suppose $`a,b\in D`$ are equivalent under this restriction. For each $`\varepsilon\in E`$ and every $`h\in H`$, equivalence in $`F`$ gives
```math
\varepsilon ah\in M\quad\Longleftrightarrow\quad\varepsilon bh\in M.
```
It follows that $`\varepsilon a\in\mathfrak f`$ if and only if $`\varepsilon b\in\mathfrak f`$. Indeed, the condition for all $`h`$, including $`h=1`$, both places the element in $`M\subseteq\mathsf q(M)`$ and is precisely the conductor condition. Taking the existence of such an $`\varepsilon`$ shows
```math
a\in\varphi(\mathfrak f)\quad\Longleftrightarrow\quad b\in\varphi(\mathfrak f).
```
Thus the finite restricted congruence recognizes $`\varphi(\mathfrak f)`$. Lemma [2.2](#label-lem-upward) proves the last assertion. $`\square`$

<!-- end proof-3 -->

This proof never requires $`E/M^\times`$ to be finite. Keeping the finite congruence on pure monomials separate from the full class semigroup is necessary when the normalization has many units.

## 4. Construction, units, and the class bound

We first record the contraction identity used in the construction.

<a id="lemma-3"></a>

**Lemma 4.1.**

<a id="label-lem-contraction"></a>

For every ideal $`\mathfrak f`$ of $`H`$, with $`K=\varphi(H)`$ and $`J=\varphi(\mathfrak f)D`$, one has
```math
\varphi(\mathfrak f)=J\cap K,\qquad \mathfrak f=\varphi^{-1}(J).
```

<!-- end lemma-3 -->

<a id="proof-4"></a>

**Proof.**

Only $`J\cap K\subseteq\varphi(\mathfrak f)`$ needs proof. If $`\varphi(h)=\varphi(a)d`$ with $`a\in\mathfrak f`$ and $`d\in D`$, divisor reflection gives $`a\mid_H h`$. The ideal property implies $`h\in\mathfrak f`$. The second equality also uses invariance of every ideal under multiplication by $`H^\times`$. $`\square`$

<!-- end proof-4 -->

<a id="proposition-2"></a>

**Proposition 4.2.**

<a id="label-prop-construction"></a>

Suppose $`\mathfrak f`$ is a nonempty proper ideal of $`H`$ and $`J`$ has a presentation [(2)](#label-eq-threshold). Let $`U=H^\times`$, and let $`V\le U`$ be any subgroup such that $`M_V=\mathfrak f\cup V\ne H`$. Then $`M_V`$ is a C-monoid with
```math
M_V^\times=V,\qquad \widehat{M_V}=H,\qquad (M_V:H)=\mathfrak f.
```
In a factorial embedding whose free part is the chosen divisor theory,

<a id="label-eq-bound"></a>

```math
\tag{4}
 |\mathcal C^*(M_V,F)|\le 1+|G|(N+1)^r.
```

There is no restriction on the index $`(U:V)`$.

<!-- end proposition-2 -->

<a id="proof-5"></a>

**Proof.**

A proper ideal contains no unit of $`H`$. Its ideal property shows that $`M_V`$ is a monoid with unit group $`V`$. Fix $`c\in\mathfrak f`$. For every $`h\in H`$, both $`c`$ and $`ch`$ lie in $`M_V`$. Hence $`\mathsf q(M_V)=\mathsf q(H)`$. Also $`ch^n\in\mathfrak f`$ for all $`n\ge1`$, so $`H\subseteq\widehat{M_V}`$. The reverse inclusion follows from $`M_V\subseteq H=\widehat H`$.

Every element of $`\mathfrak f`$ belongs to $`(M_V:H)`$. Conversely a conductor element lies in $`M_V`$. If it were a unit $`v\in V`$, then $`vH=H\subseteq M_V`$, contradicting properness. Thus the conductor is exactly $`\mathfrak f`$.

We may identify $`H`$ with $`U\times K`$, and embed it in $`F=U\times D`$. For completeness, the splitting follows because $`\mathsf q(K)`$ is a subgroup of the free abelian group $`\mathsf q(D)`$ and is therefore free abelian. The quotient-group map $`\mathsf q(H)\to\mathsf q(K)`$ has kernel $`U`$ and splits. The section sends $`K`$ into $`H`$: any lift of a member of $`K`$ differs from a representative in $`H`$ by a unit. This gives the stated product decomposition.

Let $`x=(\varepsilon,a)\in F\setminus F^\times`$, so $`a\ne1`$. For every $`y=(\eta,b)\in F`$, the product $`xy`$ is a nonunit of $`F`$ and cannot belong to $`V`$. By Lemma [4.1](#label-lem-contraction) and [(1)](#label-eq-saturated),
```math
\begin{align*}
 xy\in M_V
 &\Longleftrightarrow ab\in K\cap J\\
 &\Longleftrightarrow [a]+[b]=0\text{ in }G
       \quad\text{and}\quad \tau(a)\oplus\tau(b)\in W.
\end{align*}
```
Consequently the pair $`([a],\tau(a))`$ determines the class of every nonunit $`x`$. It takes at most $`|G|(N+1)^r`$ values, independently of $`\varepsilon`$. Including the class represented by $`1`$ proves [(4)](#label-eq-bound). Finally, $`M_V\cap F^\times=V=M_V^\times`$, so the finite reduced class semigroup proves that $`M_V`$ is C. $`\square`$

<!-- end proof-5 -->

<a id="proof-6"></a>

**Proof of Theorem [1.1](#label-thm-main).**

If (1) holds, Proposition [3.1](#label-prop-necessary) proves the finiteness assertion in (2). Every realization contains $`\mathfrak f`$ and $`1`$. If $`\mathfrak f\cup\{1\}=H`$, the realization must be $`H`$, whose conductor in itself is $`H`$, a contradiction. This proves (2). The equivalence of (2) and (3) follows from Lemma [2.1](#label-lem-profiles). Proposition [4.2](#label-prop-construction), with $`V=\{1\}`$, proves (3) implies (1).

For the boundary cases, the classical C-monoid theorem gives a nonempty conductor, and a Krull monoid with finite class group is C. Hence the empty ideal is excluded and the whole ideal is realized by $`H`$. If a proper ideal satisfies $`\mathfrak f\cup\{1\}=H`$, it must contain every element other than $`1`$. It cannot contain a unit, so $`H^\times=\{1\}`$ and $`\mathfrak f=H\setminus\{1\}`$. The converse is immediate. $`\square`$

<!-- end proof-6 -->

In particular, allowing a more complicated intermediate monoid cannot rescue a proper ideal with infinitely many prime profiles. When a realization exists at all, the smallest possible submonoid containing its conductor, $`\mathfrak f\cup\{1\}`$, is already C.

## 5. Consequences and examples

<a id="corollary-1"></a>

**Corollary 5.1.**

<a id="label-cor-finite"></a>

Every nonempty finitely generated ideal of $`H`$ is realizable unless it is the excluded proper ideal $`H\setminus\{1\}`$ in a reduced monoid. The same conclusion holds for every nonempty ideal if the divisor monoid has finite rank.

<!-- end corollary-1 -->

<a id="proof-7"></a>

**Proof.**

If $`\mathfrak f=a_1H\cup\cdots\cup a_tH`$, then $`J=\varphi(a_1)D\cup\cdots\cup\varphi(a_t)D`$. Only finitely many primes occur in these generators. Membership in $`J`$ is determined by their individual exponents truncated above the largest required exponent; all other primes may be placed in a single irrelevant part of the partition. If $`P`$ is finite, any monomial ideal has finitely many prime profiles, simply because there are finitely many primes. Apply Theorem [1.1](#label-thm-main), treating the whole ideal separately. $`\square`$

<!-- end proof-7 -->

<a id="example-1"></a>

**Example 5.2.**

<a id="label-ex-degree"></a>

Let $`P`$ be infinite, let $`H=D=\mathcal F(P)`$, and fix $`d\ge2`$. The ideal
```math
\mathfrak f_d=\{a\in D:|a|\ge d\},\qquad |a|=\sum_{p\in P}v_p(a),
```
has a single prime profile and is described by one threshold $`d`$. It is not finitely generated: every monomial of degree $`d`$ is divisibility-minimal, and there are infinitely many of them. Nevertheless $`M_d=\{1\}\cup\mathfrak f_d`$ realizes it.

In fact $`|\mathcal C^*(M_d,D)|=d+1`$. For a monomial of degree $`k`$ with $`1\le k<d`$, its residual is the set of monomials of degree at least $`d-k`$; for $`k\ge d`$ its residual is all of $`D`$. The residual at $`1`$ is $`M_d`$. These $`d+1`$ residuals are distinct. This also shows that a bound independent of the threshold is impossible.

<!-- end example-1 -->

<a id="example-2"></a>

**Example 5.3.**

<a id="label-ex-matching"></a>

Let $`H=D=\mathcal F(\{p_i,q_i:i\ge1\})`$, with all displayed primes distinct, and set
```math
\mathfrak f=\bigcup_{i\ge1}p_iq_iD.
```
For $`i\ne j`$, the monomial $`q_i`$ belongs to $`(\mathfrak f:p_i)`$ but not to $`(\mathfrak f:p_j)`$. Thus $`\mathfrak f`$ has infinitely many prime profiles. It is not the conductor of any C-monoid with complete integral closure $`D`$, even though $`D`$ has trivial class group.

The monoid $`\{1\}\cup\mathfrak f`$ does have conductor $`\mathfrak f`$ and complete integral closure $`D`$, by the conductor and closure argument in Proposition [4.2](#label-prop-construction), which does not use finiteness. The obstruction is specifically the C-monoid requirement, not existence of an unrestricted monoid realization.

<!-- end example-2 -->

<a id="example-3"></a>

**Example 5.4.**

<a id="label-ex-units"></a>

Let $`U`$ be any nontrivial abelian group and $`D=\mathcal F(P)`$ with $`P\ne\emptyset`$. Put $`H=U\times D`$ and $`\mathfrak f=H\setminus H^\times`$. This is a proper ideal with one prime profile. Although $`\mathfrak f\cup H^\times=H`$, the monoid $`\mathfrak f\cup\{1\}`$ is proper and realizes $`\mathfrak f`$. The quotient $`H^\times/M^\times\cong U`$ can be infinite, while the reduced class semigroup of $`M`$ has two elements: the class of $`1`$ and the common class of all ambient nonunits. This explains why replacing “reduced class semigroup” by “full class semigroup” would give a false necessity condition.

<!-- end example-3 -->

The theorem characterizes possible conductors with a prescribed Krull closure. It does not characterize every intermediate Mori monoid having such a conductor, which is the different recognition problem in [\[2, Problem 18\]](#ref-GKL). Nor does it characterize conductors of subrings or orders: the minimal monoid construction imposes no additive closure.

## References

<a id="ref-GHK"></a>

**\[1\]** A. Geroldinger and F. Halter-Koch, *Non-Unique Factorizations: Algebraic, Combinatorial and Analytic Theory*, Pure and Applied Mathematics 278, Chapman & Hall/CRC, Boca Raton, 2006.

<a id="ref-GKL"></a>

**\[2\]** A. Geroldinger, H. Kim, and K. A. Loper, On long-term problems in multiplicative ideal theory and factorization theory, [arXiv:2502.21020v3](https://arxiv.org/abs/2502.21020v3), 2026.

<a id="ref-GZ"></a>

**\[3\]** A. Geroldinger and Q. Zhong, A characterization of seminormal C-monoids, *Boll. Unione Mat. Ital.* **12** (2019), 583–597. [doi:10.1007/s40574-019-00194-9](https://doi.org/10.1007/s40574-019-00194-9).

<a id="ref-Reinhart"></a>

**\[4\]** A. Reinhart, A note on conductor ideals, [arXiv:1508.04260](https://arxiv.org/abs/1508.04260), 2015.
