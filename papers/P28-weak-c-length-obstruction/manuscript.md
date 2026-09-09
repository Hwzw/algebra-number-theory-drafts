Failure of the length-set structure theorem\
for weakly C-monoids
============================================

Henry Zweiman

September 9, 2026

## Abstract

We construct a reduced weakly C-monoid with factorial complete integral closure, nonempty conductor, and distance set exactly $`\{1,2\}`$ which does not satisfy the Structure Theorem for Sets of Lengths. The monoid is the union of a free rank-two boundary and a principal conductor ideal in a free abelian monoid of rank four. We prove its Mori property by a six-element colon witness and determine all of its length sets. An explicit sequence of elements has length sets consisting of two residue classes modulo three and one additional endpoint. Every almost arithmetical multiprogression representation of the $`N`$th set, with difference $`d`$ and bound $`M`$, satisfies $`2M\geq3N-d-3`$. This gives a negative answer to Problem 20 of Geroldinger, Kim, and Loper for weakly C-monoids in Kainrath’s stated sense.

## 1. Introduction and main result

The Structure Theorem for Sets of Lengths describes all length sets of a monoid by almost arithmetical multiprogressions with a common bound and differences from a finite set. It holds for C-monoids and for tame monoids; the latter result is due to Geroldinger and Kainrath [\[2\]](#ref-GK). Geroldinger, Kim, and Loper ask whether it holds for every weakly C-monoid in the sense of Kainrath [\[3, Problem 20\]](#ref-GKL). We give a counterexample.

All monoids below are commutative and cancellative, with identity. The notation $`\mathcal F(S)`$ denotes the free abelian monoid on $`S`$. Put

<a id="label-eq-construction"></a>

```math
\tag{1}
 F=\mathcal F(x,a,b,c),\qquad P=a^2b,\qquad Q=a^5c,\qquad
 B=\langle P,Q\rangle,\qquad H=B\cup x^2F.
```

<a id="theorem-1"></a>

**Theorem 1.1.**

<a id="label-thm-main"></a>

The monoid $`H`$ in [(1)](#label-eq-construction) is a reduced Mori weakly C-monoid with
```math
\widehat H=F,\qquad (H:\widehat H)=x^2F,\qquad \Delta(H)=\{1,2\}.
```
It does not satisfy the Structure Theorem for Sets of Lengths. More precisely, for every $`N\geq1`$ the element
```math
z_N=x^2a^{10N+2}b^{5N}c^{2N}
```
has length set

<a id="label-eq-ray"></a>

```math
\tag{2}
 \mathsf L_H(z_N)=(2N+2)+T_N,\qquad
 T_N=\bigl(\{0,1\}+3[0,N-1]\bigr)\cup\{3N-1\}.
```

If $`T_N`$ is an almost arithmetical multiprogression with difference $`d`$ and bound $`M`$, then

<a id="label-eq-lower-bound"></a>

```math
\tag{3}
 2M\geq3N-d-3.
```

<!-- end theorem-1 -->

Intervals in this paper contain integers only. The counterexample concerns the full definition of weakly C-monoid in [\[4, Definition 5.1\]](#ref-K). That definition does not require local tameness or the stronger condition (C) introduced in the same chapter. We make no assertion that a version restricted by either additional hypothesis fails.

## 2. Definitions and the Mori verification

For $`E\subseteq H`$, write
```math
(H:E)=\{z\in\mathsf q(H):zE\subseteq H\},\qquad E_v=(H:(H:E)),
```
where $`\mathsf q(H)`$ is the quotient group. An integral divisorial ideal is an ideal $`I\subseteq H`$ with $`I=I_v`$. The monoid is Mori, or $`v`$-Noetherian, if these ideals satisfy the ascending chain condition. Its complete integral closure is
```math
\widehat H=\{z\in\mathsf q(H):\text{some }h\in H\text{ satisfies }hz^n\in H
                 \text{ for every }n\geq1\}.
```

We recall the part of the weak-C definition that must be checked. For a factorial monoid $`F=F^\times\times\mathcal F(S)`$, two elements $`y,y'\in F`$ are $`H`$-equivalent if $`yz\in H`$ exactly when $`y'z\in H`$ for every $`z\in F`$; write $`[y]^F_H`$ for the equivalence class. A submonoid $`H\subseteq F`$ is weakly C in [\[4, Definition 5.1\]](#ref-K) if:

1.  $`H`$ is Mori, $`(H:\widehat H)\neq\emptyset`$, and $`\widehat H\subseteq F`$ is saturated and cofinal;

2.  there are an equivalence relation $`\sim`$ on $`S`$ with finitely many classes and an integer $`\lambda\geq1`$ such that, whenever all $`p_1,p'_1,\ldots,p_\lambda,p'_\lambda`$ lie in one class, some $`\varepsilon\in F^\times`$ satisfies
    ```math
    [p_1\cdots p_\lambda]^F_H=[\varepsilon p'_1\cdots p'_\lambda]^F_H.
    ```

In particular, the second condition is automatic for a finite ambient prime set: take equality for $`\sim`$ and $`\lambda=1`$.

The boundary in [(1)](#label-eq-construction) has the useful description

<a id="label-eq-boundary"></a>

```math
\tag{4}
 B=\{a^ub^vc^w:u,v,w\in\mathbb N_0,\ u=2v+5w\}.
```

Define the weight of $`a^ub^vc^w`$ to be $`-u+2v+5w`$, also for integral exponents in the quotient group.

<a id="lemma-1"></a>

**Lemma 2.1.**

<a id="label-lem-mori"></a>

For every nonempty $`E\subseteq H`$, there is $`E'\subseteq E`$ with $`|E'|\leq6`$ and $`(H:E')=(H:E)`$. Consequently $`H`$ is Mori.

<!-- end lemma-1 -->

<a id="proof-1"></a>

**Proof.**

Choose at most four elements attaining the minimum of each of the four ambient prime valuations on $`E`$. Write $`j=\min v_x(E)`$ and choose one of these witnesses, $`e_0`$, with $`v_x(e_0)=j`$. If $`E`$ contains an element with $`x`$-valuation $`j+1`$, add one. If the weights of the $`a,b,c`$ parts of the elements at $`x`$-valuation $`j`$ are not all equal, add one whose weight differs from that of $`e_0`$. Call the resulting set $`E'`$.

Suppose $`zE'\subseteq H`$. The valuation minima imply $`zE\subseteq F`$. Put $`h=v_x(z)+j\geq0`$. If $`h\geq2`$, every product belongs to $`x^2F`$. The case $`h=1`$ is impossible, since $`ze_0\notin H`$ then.

Suppose $`h=0`$. The witness at valuation $`j+1`$, if present, would give a product of $`x`$-valuation one. Thus there are no such elements. At valuation $`j`$, membership requires the sum of the two $`a,b,c`$ weights to be zero. The weight witness either makes this impossible or ensures that the same equation holds for all elements of $`E`$ at this valuation. It already holds for $`e_0`$. All other elements give products of $`x`$-valuation at least two. Hence $`zE\subseteq H`$, as required.

Thus $`E_v=E'_v`$ for a finite subset of each nonempty $`E`$. To see ACC directly, take the union of an ascending chain of integral divisorial ideals. Its finite witness lies in one member of the chain, whose divisorial closure therefore contains the union. The chain stabilizes. $`\square`$

<!-- end proof-1 -->

<a id="proposition-1"></a>

**Proposition 2.2.**

<a id="label-prop-weak-c"></a>

The monoid $`H`$ is reduced and weakly C, with $`\mathsf q(H)=\mathsf q(F)`$, $`\widehat H=F`$, and conductor $`x^2F`$.

<!-- end proposition-1 -->

<a id="proof-2"></a>

**Proof.**

The set in [(1)](#label-eq-construction) is a submonoid, and its only unit is $`1`$. The elements $`x^2,x^3,x^2a,x^2b,x^2c`$ show that its quotient group contains all four ambient primes. Every element $`z\in F`$ is almost integral over $`H`$, since $`x^2z^n\in H`$ for all $`n\geq1`$. An element of $`\mathsf q(F)`$ with a negative ambient valuation cannot be almost integral over $`H\subseteq F`$. This proves $`\widehat H=F`$.

The ideal $`x^2F`$ is in the conductor. No boundary element is in the conductor, since multiplying it by $`x`$ leaves $`H`$. Thus the conductor is exactly $`x^2F`$. The closure embedding is the identity on $`F`$, hence saturated and cofinal. Lemma [2.1](#label-lem-mori) and the equality partition of the four primes now verify both weak-C conditions. $`\square`$

<!-- end proof-2 -->

## 3. All factorization lengths

For an atomic monoid $`H`$ and $`z\in H`$, let $`\mathsf L_H(z)`$ be the set of numbers of atoms in factorizations of $`z`$, with $`\mathsf L_H(1)=\{0\}`$. In our monoid these sets are nonempty and finite: the sum of the four coordinates decreases in any proper factorization and bounds every factorization length. For a finite set $`L`$, its distances are the differences between successive elements in increasing order; $`\Delta(H)`$ is their union over $`z\in H`$.

Call a monomial in $`\mathcal F(a,b,c)`$ boundary-free if it has no nonunit divisor from $`B`$ in the ambient monoid.

<a id="lemma-2"></a>

**Lemma 3.1.**

<a id="label-lem-atoms"></a>

The atoms of $`H`$ are $`P,Q`$ and precisely the elements
```math
x^ea^ub^vc^w,\qquad e\in\{2,3\},\qquad
 (u<2\text{ or }v=0),\quad (u<5\text{ or }w=0).
```

<!-- end lemma-2 -->

<a id="proof-3"></a>

**Proof.**

The boundary $`B`$ is free abelian on $`P,Q`$ by [(4)](#label-eq-boundary), and a boundary factorization cannot use positive $`x`$-degrees. At $`x`$-degree two or three, a proper factorization must remove a boundary atom. The displayed conditions exclude exactly these divisors. At $`x`$-degree at least four, split off $`x^2`$ to obtain two nonunits in $`x^2F`$. $`\square`$

<!-- end proof-3 -->

For $`u,v,w\in\mathbb N_0`$, define

<a id="label-eq-cutoffs"></a>

<a id="label-eq-f"></a>

```math
\begin{align}
 g_0&=\min\left(w,\max\left(0,\left\lfloor\frac{u-2v}{5}\right\rfloor\right)\right),
 &g_1&=\min\left(w,\left\lfloor\frac u5\right\rfloor\right),\tag{5}\\
 f(j)&=j+\min\left(v,\left\lfloor\frac{u-5j}{2}\right\rfloor\right)
 &&(g_0\leq j\leq g_1).\tag{6}
\end{align}
```
Notice that $`g_0\leq g_1`$.

<a id="proposition-2"></a>

**Proposition 3.2.**

<a id="label-prop-lengths"></a>

The length sets of $`H`$ are given by the following formulas.

1.  If $`u=2v+5w`$, then $`\mathsf L_H(a^ub^vc^w)=\{v+w\}`$.

2.  If $`e=2`$ or $`3`$, then

    <a id="label-eq-first-layer"></a>

    ```math
    \tag{7}
     \mathsf L_H(x^ea^ub^vc^w)=1+\{f(j):g_0\leq j\leq g_1\}.
    ```

3.  If $`n\geq4`$, then

    <a id="label-eq-high-layers"></a>

    ```math
    \tag{8}
     \mathsf L_H(x^na^ub^vc^w)
     =\left[\left\lceil\frac n3\right\rceil,
             \left\lfloor\frac n2\right\rfloor+f(g_0)\right].
    ```

Moreover $`\Delta(H)=\{1,2\}`$.

<!-- end proposition-2 -->

<a id="proof-4"></a>

**Proof.**

The first assertion follows from the freeness of $`B`$. A factorization at $`x`$-degree two or three uses exactly one positive-$`x`$ atom. If it contains $`i`$ copies of $`P`$ and $`j`$ copies of $`Q`$, its remaining $`a,b,c`$ exponents are
```math
(u-2i-5j,\ v-i,\ w-j).
```
They must be nonnegative and boundary-free. After $`j`$ copies of $`Q`$, maximality with respect to $`P`$ forces
```math
i=\min\left(v,\left\lfloor\frac{u-5j}{2}\right\rfloor\right).
```
If $`i<v`$, the residual $`a`$-exponent is less than two, so maximality with respect to $`Q`$ follows. If $`i=v`$, it requires either $`j=w`$ or $`u-2v-5j<5`$. Together with feasibility these conditions give exactly the range in [(5)](#label-eq-cutoffs). This proves [(7)](#label-eq-first-layer).

For $`j>g_0`$, the capacity $`i\leq v`$ no longer binds and
```math
f(j)=\left\lfloor\frac{u-3j}{2}\right\rfloor.
```
These values decrease successively by one or two. If the first value is capacity-limited and there is a next value, write $`u-2v=5g_0+r`$ with $`0\leq r\leq4`$. The first difference is
```math
f(g_0+1)-f(g_0)=1+\left\lfloor\frac{r-5}{2}\right\rfloor\in\{-2,-1,0\}.
```
Otherwise the same floor formula applies from the beginning. Thus $`f`$ is nonincreasing and the maximum number of boundary atoms whose product divides $`a^ub^vc^w`$ is $`f(g_0)`$. A maximum packing is maximal, and every smaller packing size is obtained by taking a subset of one of maximum size.

Now fix $`n\geq4`$. If a factorization uses $`k`$ positive-$`x`$ atoms, then
```math
\left\lceil n/3\right\rceil\leq k\leq\left\lfloor n/2\right\rfloor,
 \qquad k\geq2.
```
Every such $`k`$ is possible, since $`n`$ is a sum of $`k`$ integers each equal to two or three. For any packing of $`s`$ boundary atoms, split its remaining monomial into its $`a`$-part and its $`b,c`$-part. Both are boundary-free. Adjoin $`k-2`$ factors equal to $`1`$, and assign the $`x`$-degrees just described. This gives every length in $`[k,k+f(g_0)]`$. The reverse inclusion follows because the boundary factors are a packing. Taking the union over consecutive $`k`$ gives [(8)](#label-eq-high-layers).

The first-layer sets have distances at most two, the higher-layer sets are intervals, and boundary length sets are singletons. Finally, [(7)](#label-eq-first-layer) at $`(u,v,w)=(22,10,4)`$ gives $`\{6,7,9,10,11\}`$, exhibiting both distances. $`\square`$

<!-- end proof-4 -->

## 4. An endpoint that prevents uniform structure

We use the standard AAMP definition from [\[2, Section 5\]](#ref-GK). A nonempty finite set $`L\subseteq\mathbb Z`$ is an almost arithmetical multiprogression of difference $`d\geq1`$, period $`\{0,d\}\subseteq\mathcal D\subseteq[0,d]`$, and bound $`M\geq0`$ if

<a id="label-eq-aamp"></a>

```math
\tag{9}
 L=y+(L^-\cup L^*\cup L^+)\subseteq y+\mathcal D+d\mathbb Z,
```

where $`\min L^*=0`$, $`L^*=(\mathcal D+d\mathbb Z)\cap[0,\max L^*]`$, $`L^-\subseteq[-M,-1]`$, and $`L^+\subseteq\max L^*+[1,M]`$. Equivalently there is a core interval $`[s,t]`$ with endpoints in $`L`$, with both tails of width at most $`M`$, on which the permitted periodic residue pattern is complete. The whole of $`L`$ lies in that same periodic pattern. This last containment, including the tails, is essential.

The Structure Theorem requires a single bound $`M`$ and a finite nonempty set of permitted differences for all length sets. Bounds and differences are unchanged by translating a finite set.

<a id="lemma-3"></a>

**Lemma 4.1.**

<a id="label-lem-obstruction"></a>

For $`N\geq1`$, let $`T_N`$ be the set in [(2)](#label-eq-ray). Every AAMP representation of $`T_N`$ with difference $`d`$ and bound $`M`$ satisfies [(3)](#label-eq-lower-bound).

<!-- end lemma-3 -->

<a id="proof-5"></a>

**Proof.**

Let $`I=[s,t]`$ be its core interval. Since $`\min T_N=0`$ and $`\max T_N=3N-1`$, we have
```math
s\leq M,\qquad 3N-1-t\leq M.
```
Put $`J=I\cap[0,3N-2]`$. Suppose that $`J`$ contains at least $`d+3`$ consecutive integers. On $`J`$, membership in $`T_N`$ is the pattern accepting residues zero and one modulo three. It is also invariant under translation by $`d`$ whenever both points lie in the core. Comparing three consecutive pairs $`k,k+d`$ in $`J`$ proves $`3\mid d`$: a nonzero translation modulo three does not preserve the subset $`\{0,1\}`$.

The endpoint $`3N-1`$ belongs to $`T_N`$. By the containment in [(9)](#label-eq-aamp), its residue modulo $`d`$ is permitted throughout the core. Since $`J`$ contains at least $`d`$ consecutive integers, it contains an integer in that residue class. This integer is two modulo three, hence is missing from $`T_N`$. This is a contradiction.

Therefore $`|J|\leq d+2`$. At most the endpoint lies in $`I\setminus J`$, giving $`t-s\leq d+2`$. We conclude that
```math
3N-1\leq M+(t-s)+M\leq2M+d+2,
```
as asserted. $`\square`$

<!-- end proof-5 -->

<a id="proof-6"></a>

**Completion of the proof of Theorem [1.1](#label-thm-main).**

The structural assertions follow from Proposition [2.2](#label-prop-weak-c), and the distance set from Proposition [3.2](#label-prop-lengths). At $`(u,v,w)=(10N+2,5N,2N)`$, the cutoffs are $`g_0=0`$, $`g_1=2N`$. The first packing length is $`f(0)=5N`$; all others are
```math
f(j)=\left\lfloor\frac{10N+2-3j}{2}\right\rfloor,
 \qquad 1\leq j\leq2N.
```
Separating odd and even $`j`$ gives [(2)](#label-eq-ray). Lemma [4.1](#label-lem-obstruction) proves [(3)](#label-eq-lower-bound). If the Structure Theorem held with common bound $`M`$ and differences bounded by $`D`$, then [(3)](#label-eq-lower-bound) would give $`3N\leq2M+D+3`$ for every $`N`$, which is impossible. $`\square`$

<!-- end proof-6 -->

## 5. Scope and further questions

The example separates finite distances from uniform length structure inside the class of weakly C-monoids, even with factorial complete integral closure and a conductor principal in that closure. Its boundary is itself factorial, and every length set at $`x`$-degree at least four is an interval. Thus the obstruction is confined to the first conductor layers and to the requirement that the AAMP tails respect the period of the core.

The union of a lattice boundary and a conductor ideal is related to the non-locally-tame example of Geroldinger and Hassler [\[1, Example 6.11\]](#ref-GH). The particular two-generator boundary in [(1)](#label-eq-construction) permits an explicit incompatible endpoint. The result does not contradict the theorem for tame monoids [\[2\]](#ref-GK). Nor does it settle the length-structure problem under the stronger condition (C) discussed by Kainrath [\[4\]](#ref-K). Identifying additional algebraic hypotheses that eliminate these endpoint obstructions remains a natural next question.

The accompanying standard-library Python script checks the atom characterization by direct decompositions, compares the full length formulas with independent factorizations in a finite box, and checks the ray formula and obstruction inequality in finite ranges. The proofs above, including the Mori property and the unbounded obstruction, do not depend on computation.

## References

<a id="ref-GH"></a>

**\[1\]** A. Geroldinger and W. Hassler, *Arithmetic of Mori domains and monoids*, Journal of Algebra **319** (2008), 3419–3463. [doi:10.1016/j.jalgebra.2007.11.025](https://doi.org/10.1016/j.jalgebra.2007.11.025).

<a id="ref-GK"></a>

**\[2\]** A. Geroldinger and F. Kainrath, *On the arithmetic of tame monoids with applications to Krull monoids and Mori domains*, Journal of Pure and Applied Algebra **214** (2010), 2199–2218. [doi:10.1016/j.jpaa.2010.02.023](https://doi.org/10.1016/j.jpaa.2010.02.023).

<a id="ref-GKL"></a>

**\[3\]** A. Geroldinger, H. Kim, and K. A. Loper, *On Long-Term Problems in Multiplicative Ideal Theory and Factorization Theory*, [arXiv:2502.21020v3](https://arxiv.org/abs/2502.21020), February 28, 2026.

<a id="ref-K"></a>

**\[4\]** F. Kainrath, *Arithmetic of Mori domains and monoids: the global case*, in S. T. Chapman, M. Fontana, A. Geroldinger, and B. Olberding (eds.), *Multiplicative Ideal Theory and Factorization Theory*, Springer Proceedings in Mathematics & Statistics **170**, Springer, 2016, 183–218. [doi:10.1007/978-3-319-38855-7_8](https://doi.org/10.1007/978-3-319-38855-7_8).
