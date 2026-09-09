# Reconstruction of Krull monoids from conductor submonoids

Henry Zweiman

September 9, 2026

## Abstract

Let $`\varphi:H\to F`$ be a divisor theory of a commutative Krull monoid, and let $`M_\varphi=\{1\}\cup\varphi(H\setminus H^\times)F`$. We show that $`M_\varphi`$ determines the reduced monoid of $`H`$, together with its divisor theory. The reconstruction takes the complete integral closure and then generates a submonoid from its divisibility-minimal nonunits. Consequently two such conductor monoids are isomorphic exactly when the original reduced Krull monoids are isomorphic, answering an isomorphism question of Geroldinger, Yan, and Zhong. We also describe the automorphism group in terms of the characteristic and give an intrinsic recognition criterion for conductor monoids that arise in this way.

## 1. The isomorphism question

All monoids in this note are commutative and cancellative, with identity. Write $`H^\times`$ for the group of units, $`H_{\mathrm{red}}=H/H^\times`$, and $`\mathsf q(H)`$ for the quotient group. A reduced free abelian monoid $`F=\mathcal F(P)`$ consists of the finite products of primes from $`P`$. A homomorphism $`\varphi:H\to F`$ is a divisor homomorphism if divisibility of $`\varphi(a)`$ by $`\varphi(b)`$ implies divisibility of $`a`$ by $`b`$. It is a divisor theory if, in addition, every element of $`F`$ is the gcd of a finite nonempty subset of $`\varphi(H)`$. It suffices to impose this condition on the primes of $`F`$. A monoid is Krull precisely when it admits a divisor theory.

Geroldinger, Yan, and Zhong associate to a divisor theory the conductor submonoid

<a id="label-eq-construction"></a>

```math
\tag{1}
 M_\varphi=\{1\}\cup\varphi(H\setminus H^\times)F.
```

Immediately after Proposition 4.3 of [\[2\]](#ref-GYZ), they ask when the monoids associated to two Krull monoids are isomorphic. Their notation is $`F_\varphi`$. We use $`M_\varphi`$ to distinguish it from the ambient free monoid.

<a id="theorem-1"></a>

**Theorem 1.1.**

<a id="label-thm-main"></a>

For $`i=1,2`$, let $`\varphi_i:H_i\to F_i`$ be divisor theories of Krull monoids. There is a natural bijection
```math
\operatorname{Iso}(M_{\varphi_1},M_{\varphi_2})
 \longleftrightarrow
 \operatorname{Iso}((H_1)_{\mathrm{red}},(H_2)_{\mathrm{red}}).
```
It respects identities and composition. In particular, the two conductor monoids are isomorphic if and only if the two reduced Krull monoids are isomorphic.

<!-- end theorem-1 -->

The complete integral closure of a conductor monoid is already identified in [\[2, Lemmas 3.1–3.2\]](#ref-GYZ). The additional observation needed here is that minimal nonunits in that closure recover the atoms of the original Krull monoid. Thus the proof uses standard divisor theory and is short. The automorphism and recognition statements below are consequences of the same reconstruction, rather than separate isomorphism problems.

## 2. Intrinsic recovery of the original monoid

For a monoid $`M`$, its complete integral closure is
```math
\widehat M=\{x\in\mathsf q(M):\text{some }c\in M\text{ satisfies }cx^n\in M
                 \text{ for every }n\ge1\}.
```
An isomorphism extends uniquely to quotient groups and carries complete integral closures onto one another.

<a id="lemma-1"></a>

**Lemma 2.1.**

<a id="label-lem-closure"></a>

Let $`F`$ be free abelian, and let $`I\subset F`$ be a nonempty ideal with $`1\notin I`$. For $`M=\{1\}\cup I`$, one has $`\mathsf q(M)=\mathsf q(F)`$ and $`\widehat M=F`$.

<!-- end lemma-1 -->

<a id="proof-1"></a>

**Proof.**

Fix $`c\in I`$. For every $`f\in F`$, both $`c`$ and $`cf`$ belong to $`M`$, so $`f=(cf)/c\in\mathsf q(M)`$. This proves equality of quotient groups. Also $`cf^n\in I`$ for all $`n\ge1`$, proving $`F\subset\widehat M`$. If $`x\in\mathsf q(F)\setminus F`$, some prime valuation $`v_p(x)`$ is negative. For every fixed $`b\in M`$, the integer $`v_p(bx^n)`$ is eventually negative. Hence $`bx^n`$ cannot belong to $`M\subset F`$ for all $`n`$, and $`x\notin\widehat M`$. $`\square`$

<!-- end proof-1 -->

Whenever $`\widehat M`$ is free abelian and $`M`$ is reduced, define
```math
B(M)=\{a\in M\setminus\{1\}: b\in M\setminus\{1\},\ b\mid_{\widehat M}a
                       \ \Longrightarrow\ b=a\}.
```
This definition is intrinsic to $`M`$. It uses divisibility in the recovered closure, not divisibility inside $`M`$.

<a id="lemma-2"></a>

**Lemma 2.2.**

<a id="label-lem-atoms"></a>

Let $`\varphi:H\to F`$ be a divisor theory of a nontrivial reduced Krull monoid. Then
```math
B(M_\varphi)=\varphi(\mathcal A(H)),\qquad
 \langle B(M_\varphi)\rangle=\varphi(H).
```

<!-- end lemma-2 -->

<a id="proof-2"></a>

**Proof.**

The divisor homomorphism $`\varphi`$ is injective because $`H`$ is reduced. The nonunits of $`M_\varphi`$ form the nonempty ideal $`\varphi(H\setminus\{1\})F`$, and Lemma [2.1](#label-lem-closure) identifies the closure with $`F`$.

Take $`a\in B(M_\varphi)`$. Some $`h\in H\setminus\{1\}`$ satisfies $`\varphi(h)\mid_F a`$. The Krull monoid $`H`$ is atomic, so an atom $`u`$ divides $`h`$. Since $`\varphi(u)`$ is a nonunit of $`M_\varphi`$ dividing $`a`$ in $`F`$, minimality gives $`a=\varphi(u)`$.

Conversely, let $`u\in\mathcal A(H)`$ and suppose that $`b\in M_\varphi\setminus\{1\}`$ divides $`\varphi(u)`$ in $`F`$. Choose $`h\ne1`$ such that $`\varphi(h)\mid_F b`$. The divisor homomorphism property gives $`h\mid_H u`$. Thus $`h=u`$, and
```math
\varphi(u)=\varphi(h)\mid_F b\mid_F\varphi(u)
```
forces $`b=\varphi(u)`$. This proves the first equality. Atomicity proves the second. $`\square`$

<!-- end proof-2 -->

<a id="proof-3"></a>

**Proof of Theorem [1.1](#label-thm-main).**

A divisor theory factors through $`H_{\mathrm{red}}`$, so we may suppose both original monoids reduced. If $`H_i=\{1\}`$, the gcd condition forces $`F_i=\{1\}`$; this case is immediate.

An isomorphism $`f:M_{\varphi_1}\to M_{\varphi_2}`$ extends uniquely to quotient groups. By Lemma [2.1](#label-lem-closure) it restricts to an isomorphism $`\widehat f:F_1\to F_2`$. This extension preserves divisibility and maps $`B(M_{\varphi_1})`$ onto $`B(M_{\varphi_2})`$. Lemma [2.2](#label-lem-atoms) therefore gives a restricted isomorphism of $`\varphi_1(H_1)`$ with $`\varphi_2(H_2)`$, and hence one of $`H_1`$ with $`H_2`$.

Conversely, an isomorphism $`h:H_1\to H_2`$ identifies two divisor theories of $`H_1`$. The uniqueness theorem for divisor theories [\[1, Theorem 2.4.7\]](#ref-GHK) supplies a unique isomorphism $`\widetilde h:F_1\to F_2`$ with $`\widetilde h\varphi_1=\varphi_2h`$. Equation [(1)](#label-eq-construction) shows that its restriction maps $`M_{\varphi_1}`$ onto $`M_{\varphi_2}`$. Uniqueness makes the two constructions inverse and ensures compatibility with composition. $`\square`$

<!-- end proof-3 -->

## 3. Characteristic and automorphisms

Identify a reduced Krull monoid $`H`$ with its image in a divisor theory $`H\subset F=\mathcal F(P)`$. Set
```math
G=\mathsf q(F)/\mathsf q(H),\qquad P_g=\{p\in P:[p]=g\},\qquad m(g)=|P_g|.
```
The group and prime multiplicities are the characteristic. The familiar classification of reduced Krull monoids by this data is [\[1, Theorem 2.5.4\]](#ref-GHK). We record explicitly how it answers the conductor question.

<a id="corollary-1"></a>

**Corollary 3.1.**

<a id="label-cor-characteristic"></a>

Two conductor monoids in Theorem [1.1](#label-thm-main) are isomorphic exactly when there is a group isomorphism $`\alpha:G_1\to G_2`$ with $`m_1(g)=m_2(\alpha(g))`$ for every $`g\in G_1`$.

<!-- end corollary-1 -->

<a id="proof-4"></a>

**Proof.**

An isomorphism of conductor monoids extends to the free monoids and preserves the recovered submonoids, so it induces the required isomorphism on quotient groups and bijections of prime fibers. Conversely, choose such fiber bijections. The resulting isomorphism of free monoids carries $`\mathsf q(H_1)`$ onto $`\mathsf q(H_2)`$. Since a divisor homomorphism identifies

<a id="label-eq-saturation"></a>

```math
\tag{2}
 H_i=\mathsf q(H_i)\cap F_i,
```

it carries $`H_1`$ onto $`H_2`$, and therefore also the conductor monoids. $`\square`$

<!-- end proof-4 -->

<a id="corollary-2"></a>

**Corollary 3.2.**

<a id="label-cor-automorphisms"></a>

Let $`\Gamma=\{\alpha\in\operatorname{Aut}(G):m(\alpha(g))=m(g)\text{ for all }g\in G\}`$. There is a split exact sequence
```math
1\longrightarrow\prod_{g\in G}\operatorname{Sym}(P_g)
 \longrightarrow\operatorname{Aut}(M_\varphi)\longrightarrow\Gamma\longrightarrow1.
```
Thus, after choices of labels on the prime fibers,
```math
\operatorname{Aut}(M_\varphi)\cong
 \left(\prod_{g\in G}\operatorname{Sym}(P_g)\right)\rtimes\Gamma.
```
The product is unrestricted, including when $`P`$ is infinite.

<!-- end corollary-2 -->

<a id="proof-5"></a>

**Proof.**

Theorem [1.1](#label-thm-main) identifies automorphisms with prime permutations preserving $`H`$, equivalently its quotient-group kernel. The kernel of their action on $`G`$ consists exactly of the independent permutations within the fibers $`P_g`$. Every member of $`\Gamma`$ lifts by choosing fiber bijections, as in Corollary [3.1](#label-cor-characteristic).

For a splitting, choose, for each cardinal $`\kappa`$ occurring among the multiplicities, a fixed set $`X_\kappa`$ and bijections $`P_g\to\{g\}\times X_{m(g)}`$. Lift $`\alpha\in\Gamma`$ by $`(g,x)\mapsto(\alpha(g),x)`$. These lifts compose and preserve the quotient-group kernel. Every permutation of an infinite prime set still acts on its free abelian monoid, since each monomial has finite support. $`\square`$

<!-- end proof-5 -->

For a Dedekind domain, the associated conductor monoid can be described as the unit ideal together with the nonzero ideals contained in a proper principal ideal [\[2, Example 4.4\]](#ref-GYZ). The reconstruction recovers the monoid of nonzero principal ideals and its divisor theory. It recovers the multiplicative monoid modulo units, not the addition law or the unit group of the domain.

## 4. Recognition and examples

The construction does not exhaust all conductor submonoids. The following criterion gives an intrinsic test.

<a id="proposition-1"></a>

**Proposition 4.1.**

<a id="label-prop-recognition"></a>

Let $`M=\{1\}\cup I\subset F`$, where $`F`$ is free abelian and $`I`$ is a nonempty proper ideal. Put $`K=\langle B(M)\rangle\subset\widehat M=F`$. Then $`M`$ is isomorphic to the conductor monoid of a divisor theory of a Krull monoid if and only if

1.  $`K=\mathsf q(K)\cap F`$;

2.  every prime of $`F`$ is the gcd of a finite nonempty subset of $`K`$.

When these conditions hold, the inclusion $`K\subset F`$ is the recovered divisor theory and $`M=\{1\}\cup(K\setminus\{1\})F`$.

<!-- end proposition-1 -->

<a id="proof-6"></a>

**Proof.**

For every $`x\in I`$, choose a divisor of $`x`$ in $`I`$ of least free-monoid length. It lies in $`B(M)`$. Hence $`I=B(M)F`$. The two stated conditions say respectively that the inclusion $`K\subset F`$ is a divisor homomorphism and that it satisfies the gcd condition. Thus they make it a divisor theory, with $`K`$ Krull. Since $`B(M)\subset K\setminus\{1\}\subset I`$, its associated conductor monoid is exactly $`M`$.

Conversely, any isomorphism with a conductor monoid of a divisor theory extends to the free closures. Lemma [2.2](#label-lem-atoms) identifies $`K`$ with the image of that Krull monoid, proving both conditions. $`\square`$

<!-- end proof-6 -->

If $`F`$ has finite rank, $`B(M)`$ is a finite antichain of exponent vectors. To check condition (2), it suffices, for each prime $`p`$, to take the gcd of
```math
B_p=\{a\in B(M):p\mid_F a\}
```
and require it to be $`p`$. Indeed, if $`p`$ divides a product of elements of $`B(M)`$, it divides at least one factor. The gcd of all $`p`$-divisible elements of $`K`$ therefore equals the gcd of $`B_p`$. Condition (1) is the equality of the affine monoid generated by these vectors with the intersection of their integer span and the nonnegative orthant. This formulation separates saturation from the indispensable gcd condition.

<a id="example-1"></a>

**Example 4.2.**

<a id="label-ex-threshold"></a>

In additive notation, let $`r\ge2`$, $`d\ge1`$, and
```math
M_{r,d}=\{0\}\cup\{a\in\mathbb N_0^r:a_1+\cdots+a_r\ge d\}.
```
The minimal elements are exactly the vectors of coordinate sum $`d`$. Their generated monoid is
```math
K_{r,d}=\{a\in\mathbb N_0^r:a_1+\cdots+a_r\equiv0\pmod d\}.
```
To see the equality, repeatedly remove a nonnegative subvector of sum $`d`$. Its quotient group consists of the integer vectors whose coordinate sum is divisible by $`d`$: differences of degree-$`d`$ vectors include $`e_i-e_j`$, and $`de_i`$ is present. Thus condition (1) holds. For $`d>1`$, the coordinatewise minimum of $`de_i`$ and $`e_i+(d-1)e_j`$, with $`j\ne i`$, is $`e_i`$. For $`d=1`$, $`e_i`$ itself is present. This verifies condition (2).

The recovered class group is $`\mathbb Z/d\mathbb Z`$, with all $`r`$ primes in the class of $`1`$. Its only automorphism preserving the occupied class fixes $`1`$ and is the identity. Consequently $`\operatorname{Aut}(M_{r,d})\cong\operatorname{Sym}(r)`$. The class group recovered from the conductor monoid distinguishes the parameter $`d`$, even though this automorphism group does not.

<!-- end example-1 -->

<a id="example-2"></a>

**Example 4.3.**

<a id="label-ex-rankone"></a>

For $`d>1`$, the rank-one conductor monoid $`M=\{0\}\cup\{d,d+1,\ldots\}\subset\mathbb N_0`$ has $`B(M)=\{d\}`$ and $`K=d\mathbb N_0`$. It satisfies $`K=\mathsf q(K)\cap\mathbb N_0`$, but no gcd of nonzero elements of $`K`$ is $`1`$. Proposition [4.1](#label-prop-recognition) shows that $`M`$ is not isomorphic to the conductor monoid of any divisor theory of a Krull monoid. An arbitrary divisor homomorphism cannot replace a divisor theory in Theorem [1.1](#label-thm-main).

<!-- end example-2 -->

## References

<a id="ref-GHK"></a>

**\[1\]** A. Geroldinger and F. Halter-Koch, *Non-Unique Factorizations: Algebraic, Combinatorial and Analytic Theory*, Pure and Applied Mathematics 278, Chapman & Hall/CRC, Boca Raton, 2006.

<a id="ref-GYZ"></a>

**\[2\]** A. Geroldinger, W. Yan, and Q. Zhong, On conductor submonoids of factorial monoids, *Semigroup Forum* **112** (2026), 792–819. [doi:10.1007/s00233-025-10583-6](https://doi.org/10.1007/s00233-025-10583-6).
