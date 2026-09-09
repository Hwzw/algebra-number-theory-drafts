Counterexamples to Gao’s\
zero-sum invariant conjecture
=============================

Henry Zweiman

September 9, 2026

## Abstract

For every odd integer $`n\geq3`$, we prove that $`\nu(C_2^3\oplus C_{2n})=2n+2=\mathsf d(C_2^3\oplus C_{2n})`$. This disproves Gao’s conjecture that $`\nu(G)=\mathsf d(G)-1`$ for every nontrivial finite abelian group. The construction is a zero-sum-free sequence of length $`2n+1`$ with exactly six omitted nonzero subsequence sums. These sums form the product of the three nonzero elements of an elementary two-group of rank two with two adjacent cyclic residues. Their differences force every coset containing them to contain zero. We also give explicit extremal extensions and show that the index-two refinement and the associated local invariant attain their larger possible values.

## 1. The conjecture and the counterexamples

Let $`G`$ be a nontrivial finite abelian group, written additively. A sequence over $`G`$ is a finite multiset of elements, written multiplicatively. Thus $`g^k`$ denotes $`k`$ occurrences of $`g`$. For a sequence $`T=g_1\cdots g_\ell`$, put
```math
\Sigma(T)=\left\{\sum_{i\in I}g_i:\emptyset\neq I\subseteq[1,\ell]\right\},
 \qquad \Sigma^*(T)=\Sigma(T)\cup\{0\}.
```
The sequence is zero-sum free if $`0\notin\Sigma(T)`$. Its set of holes is
```math
R(T)=G\setminus\Sigma^*(T).
```
Write $`\mathsf d(G)`$ for the greatest length of a zero-sum-free sequence and $`\mathsf D(G)=\mathsf d(G)+1`$ for the Davenport constant.

The invariant $`\nu(G)`$ is the least integer $`\ell\geq0`$ such that every zero-sum-free sequence $`T`$ of length at least $`\ell`$ satisfies

<a id="label-eq-nu"></a>

```math
\tag{1}
 R(T)\subseteq\alpha+H
 \quad\text{for some }H\subsetneq G\text{ and }\alpha\in G\setminus H.
```

The exclusion of zero from the coset is part of the definition. Merely putting the holes in a proper subgroup does not establish [(1)](#label-eq-nu).

Gao conjectured that $`\nu(G)=\mathsf d(G)-1`$; equivalently, $`\mathsf D(G)=\nu(G)+2`$. The latter formulation appears in Gao and Thangadurai [\[3, Definition 3 and Conjecture 4\]](#ref-GT). Geroldinger and Yang [\[4, Introduction and Section 6\]](#ref-GY) restate it as an open conjecture. Their recent results include the family $`C_2^2\oplus C_{2n}`$ and certain groups with four elementary two-group factors. We give counterexamples with three such factors.

<a id="theorem-1"></a>

**Theorem 1.1.**

<a id="label-thm-main"></a>

Let $`n\geq3`$ be odd, and let
```math
G=\langle e_1\rangle\oplus\langle e_2\rangle\oplus\langle e_3\rangle
       \oplus\langle f\rangle,
 \qquad \operatorname{ord}(e_i)=2,\quad\operatorname{ord}(f)=2n.
```
Set
```math
q=\frac{n+1}{2},\qquad
 C=\{e_1,e_2,e_3,e_1+e_2+e_3\},\qquad
 W=\langle e_1+e_2,e_1+e_3\rangle.
```
Then the sequence

<a id="label-eq-construction"></a>

```math
\tag{2}
 T_n=f^{2n-3}\prod_{c\in C}(c+qf)
```

is zero-sum free, has length $`\mathsf d(G)-1=2n+1`$, and has exactly the six holes

<a id="label-eq-holes"></a>

```math
\tag{3}
 R(T_n)=(W\setminus\{0\})+\{(n-1)f,nf\}.
```

No coset excluding zero contains these holes. Consequently,

<a id="label-eq-value"></a>

```math
\tag{4}
 \nu(C_2^3\oplus C_{2n})=\mathsf d(C_2^3\oplus C_{2n})=2n+2.
```

<!-- end theorem-1 -->

The Davenport formula used here is classical. Baayen [\[1, p. 1\]](#ref-B) proves that every sequence of length $`2n+3`$ in this group has a nonempty zero-sum subsequence for odd $`n`$. On the other hand, $`e_1e_2e_3f^{2n-1}`$ is zero-sum free. Thus $`\mathsf d(G)=2n+2`$. The same formula is recorded in [\[4, Proposition 2.1\]](#ref-GY); it is not a new result of this paper.

## 2. A coset obstruction and the exact holes

We start with the obstruction that makes the construction effective.

<a id="lemma-1"></a>

**Lemma 2.1.**

<a id="label-lem-coset"></a>

Let $`u,v`$ be distinct nonzero elements of order two in an abelian group, let $`f`$ be any group element, and let $`b\in\mathbb Z`$. No coset $`\alpha+H`$ with $`\alpha\notin H`$ contains
```math
\{u,v,u+v\}+\{bf,(b+1)f\}.
```

<!-- end lemma-1 -->

<a id="proof-1"></a>

**Proof.**

Suppose all displayed elements lie in $`\alpha+H`$. The difference of $`u+(b+1)f`$ and $`u+bf`$ gives $`f\in H`$. The difference of $`u+bf`$ and $`v+bf`$ gives $`u-v=u+v\in H`$. Therefore $`u+v+bf\in H`$. This element also lies in $`\alpha+H`$, forcing $`\alpha\in H`$, a contradiction. $`\square`$

<!-- end proof-1 -->

<a id="proof-2"></a>

**Proof of Theorem [1.1](#label-thm-main).**

Put $`E=\langle e_1,e_2,e_3\rangle`$. The four elements of $`C`$ form a circuit in $`E`$: their sum is zero, and no proper nonempty subset has sum zero. Also,

<a id="label-eq-fourq"></a>

```math
\tag{5}
 4q=2n+2\equiv2\pmod{2n}.
```

Any zero-sum subsequence of $`T_n`$ must therefore use none or all four of the terms $`c+qf`$. In the former case it is $`f^k`$ with $`1\leq k\leq2n-3`$, and has nonzero sum. In the latter case its sum is $`(k+4q)f=(k+2)f`$ with $`0\leq k\leq2n-3`$, again nonzero. Thus $`T_n`$ is zero-sum free, and its length is $`2n+1`$.

We determine all its holes, including those that will not be needed to disprove the conjecture. Enumerate $`C=\{c_1,c_2,c_3,c_4\}`$. The map
```math
\{0,1\}^4\longrightarrow E,\qquad
 (\epsilon_i)\longmapsto\sum_i\epsilon_i c_i
```
is a surjective homomorphism of elementary two-groups with kernel consisting of the zero vector and the all-one vector. Hence each $`w\in E`$ is represented by precisely two subsets of $`C`$, which are complements. Let their sizes be $`k`$ and $`4-k`$.

Selecting either subset and between zero and $`2n-3`$ copies of $`f`$ shows that the cyclic coordinates of $`\Sigma^*(T_n)`$ above $`w`$ are
```math
\bigl(kq+[0,2n-3]\bigr)\ \cup\
 \bigl((4-k)q+[0,2n-3]\bigr)
 \quad\text{in }\mathbb Z/(2n)\mathbb Z.
```
Consequently the omitted coordinates above $`w`$ form the intersection

<a id="label-eq-intersection"></a>

```math
\begin{align}
 &\{kq-2,kq-1\}\cap\{(4-k)q-2,(4-k)q-1\}\notag\\
 &\hspace{35mm}=\{kq-2,kq-1\}\cap\{-kq,1-kq\},\tag{6}
\end{align}
```
where [(5)](#label-eq-fourq) was used.

Matching the first element of one pair with the second of the other would require $`2kq\equiv1`$ or $`3\pmod{2n}`$, which is impossible. The other two matches occur together, precisely when
```math
2kq\equiv2\pmod{2n}.
```
Since $`\gcd(q,n)=1`$ and $`2q\equiv1\pmod n`$, this is equivalent to $`k\equiv2\pmod n`$. For odd $`n\geq3`$ and $`0\leq k\leq4`$, the only possibility is $`k=2`$. The sums of pairs from $`C`$ are exactly
```math
e_1+e_2,\qquad e_1+e_3,\qquad e_2+e_3,
```
each represented by complementary pairs. When $`k=2`$, the two omitted coordinates in [(6)](#label-eq-intersection) are
```math
2q-2=n-1,\qquad 2q-1=n.
```
This proves [(3)](#label-eq-holes). Its six elements are distinct and nonzero.

Apply Lemma [2.1](#label-lem-coset) with $`u=e_1+e_2`$, $`v=e_1+e_3`$, and $`b=n-1`$. Thus $`T_n`$, of length $`\mathsf d(G)-1`$, violates [(1)](#label-eq-nu), so $`\nu(G)\geq\mathsf d(G)`$. For completeness, every zero-sum-free sequence $`S`$ of length $`\mathsf d(G)`$ has $`R(S)=\emptyset`$: if $`x\in R(S)`$, then $`(-x)S`$ would be zero-sum free of greater length. The empty set satisfies [(1)](#label-eq-nu), so $`\nu(G)\leq\mathsf d(G)`$. This proves [(4)](#label-eq-value). $`\square`$

<!-- end proof-2 -->

## 3. Extremal extensions and the parity of the construction

Geroldinger and Yang define $`\nu_p(G)`$ by requiring the subgroup in [(1)](#label-eq-nu) to have index $`p`$, for a prime divisor $`p`$ of $`|G|`$. They also define a local invariant $`\nu(S)`$ for a maximal zero-sum-free sequence $`S`$: it is the least threshold for which all subsequences of $`S`$ beyond that threshold have their holes in a coset excluding zero. Here maximal means that no additional term can be adjoined while retaining zero-sum freeness.

<a id="corollary-1"></a>

**Corollary 3.1.**

<a id="label-cor-local"></a>

For the group in Theorem [1.1](#label-thm-main), we have $`\nu_2(G)=\mathsf d(G)`$. Let $`u\in W\setminus\{0\}`$. Then
```math
S_n=T_n(u+nf)
```
is zero-sum free of length $`\mathsf d(G)`$ and satisfies $`\nu(S_n)=|S_n|`$. Moreover,
```math
U_n=T_n(u+nf)(u+(n+1)f)
```
is a minimal zero-sum sequence of length $`\mathsf D(G)`$.

<!-- end corollary-1 -->

<a id="proof-3"></a>

**Proof.**

The inequality $`\nu_2(G)\geq\nu(G)=\mathsf d(G)`$ follows from the definitions, and the reverse inequality follows from the empty-hole property at length $`\mathsf d(G)`$. Since $`u+nf`$ is a hole of $`T_n`$ and equals its negative, $`S_n`$ is zero-sum free. It has greatest possible length, hence is maximal and has no holes. Its subsequence $`T_n`$ violates the coset property, so the local threshold is exactly $`|S_n|`$.

The sum of $`T_n`$ is $`-f`$, by [(5)](#label-eq-fourq). Therefore the sum of $`S_n`$ is $`u+(n-1)f`$, whose negative is $`u+(n+1)f`$. Adjoining this term gives a zero-sum sequence. A proper zero-sum subsequence either lies in $`S_n`$, or has a nonempty zero-sum complement in $`S_n`$; both are impossible. Thus $`U_n`$ is minimal. $`\square`$

<!-- end proof-3 -->

The parity restriction in the theorem is intrinsic to this particular sparse construction, rather than an omitted even case.

<a id="proposition-1"></a>

**Proposition 3.2.**

<a id="label-prop-parity"></a>

Let $`n\geq2`$, let $`G=C_2^3\oplus\langle f\rangle`$ with $`\operatorname{ord}(f)=2n`$, and use the same circuit $`C\subseteq C_2^3`$. For $`t\in\mathbb Z`$, the sequence
```math
f^{2n-3}\prod_{c\in C}(c+tf)
```
is zero-sum free if and only if $`4t\equiv2\pmod{2n}`$. Such a $`t`$ exists if and only if $`n`$ is odd.

<!-- end proposition-1 -->

<a id="proof-4"></a>

**Proof.**

A zero-sum subsequence must use either none or all four circuit terms. The former possibility is excluded by the number of copies of $`f`$. In the latter case the available cyclic sums are $`4t+[0,2n-3]`$. This interval modulo $`2n`$ excludes zero exactly when $`4t`$ is congruent to one or two. The first possibility is impossible by parity, giving the stated criterion. The congruence is soluble exactly when $`\gcd(4,2n)`$ divides two, or equivalently when $`n`$ is odd. $`\square`$

<!-- end proof-4 -->

## 4. The smallest example and remaining questions

For $`n=3`$, the counterexample lies in a group of order $`48`$ and has the particularly simple form
```math
T_3=f^3(e_1+2f)(e_2+2f)(e_3+2f)(e_1+e_2+e_3+2f).
```
Its $`127`$ nonempty subsequences have $`41`$ distinct sums, all nonzero. The six holes are
```math
\{e_1+e_2,e_1+e_3,e_2+e_3\}+\{2f,3f\}.
```
They lie in the proper subgroup $`W\oplus\langle f\rangle`$, but in no coset that excludes zero. This distinction explains why containment in a proper subgroup would not suffice in the conjecture.

The proof above is uniform in $`n`$ and does not depend on finite computation. The accompanying verification checks the exact hole set, the difference-generated subgroup obstruction, the extremal extension, and the longest atom for every odd $`n`$ from three through $`101`$. It also separately enumerates all nonempty subsequences in the smallest example.

The theorem disproves the universal conjecture, but it does not classify all finite abelian groups with $`\nu(G)=\mathsf d(G)`$. In particular, Proposition [3.2](#label-prop-parity) only rules out this construction for even $`n`$; it does not determine $`\nu(C_2^3\oplus C_{2n})`$ in all those cases. A revised classification must distinguish the established positive families from the rank-four family exhibited here. The explicit six-hole configuration provides a local obstruction that such a classification must accommodate.

## References

<a id="ref-B"></a>

**\[1\]** P. C. Baayen, *$`(C_2\oplus C_2\oplus C_2\oplus C_{2n})!`$*, Report ZW 1969-006, Stichting Mathematisch Centrum, Amsterdam, 1969. [Institutional full text](https://ir.cwi.nl/pub/7264).

<a id="ref-G"></a>

**\[2\]** W. Gao, *On Davenport’s constant of finite abelian groups with rank three*, Discrete Mathematics **222** (2000), 111–124. [doi:10.1016/S0012-365X(00)00010-8](https://doi.org/10.1016/S0012-365X(00)00010-8).

<a id="ref-GT"></a>

**\[3\]** W. D. Gao and R. Thangadurai, *Davenport constant and non-Abelian version of Erdős–Ginzburg–Ziv theorem*, in The Riemann Zeta Function and Related Themes, Ramanujan Mathematical Society Lecture Notes Series, vol. 2, 2006, pp. 57–64. [Author-hosted version](https://www.hri.res.in/~thanga/papers/thanga.pdf).

<a id="ref-GY"></a>

**\[4\]** A. Geroldinger and W. Yang, *On a classical zero-sum invariant*, [arXiv:2608.19090v1](https://arxiv.org/abs/2608.19090v1), August 19, 2026.
