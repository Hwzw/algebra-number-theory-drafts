Word fibres over finite chain rings\
and the Amit–Ashurst conjecture for metacyclic groups
=====================================================

Henry Zweiman

September 9, 2026

## Abstract

We prove the Amit–Ashurst conjecture for every finite metacyclic $`p`$-group, including nonsplit extensions. The proof applies more generally to cyclic extensions of finite modules over commutative chain rings, when conjugation acts as multiplication by a principal unit. In particular, it also proves the conjecture for every finite $`p`$-group with an elementary abelian normal subgroup and cyclic quotient. The main estimate concerns split extensions by abelian $`p`$-groups. After fixing the quotient coordinates of a word, its base coordinate is linear in the module variables. Finite differences control the support of a coefficient of least valuation, and the module filtration compensates for the resulting loss of support. A stronger word-dependent estimate then descends through a central cyclic kernel, removing the splitting hypothesis for cyclic quotients. All bounds hold for every word and every attained value, without a bound on the number of variables or the nilpotency class.

## 1. Introduction and principal results

For a finite group $`G`$, a word $`w\in F_k=\langle x_1,\ldots,x_k\rangle`$ induces a map $`w:G^k\to G`$. Write $`w(G)`$ for its image and
```math
P_{w,G}(g)=\frac{|\{(g_1,\ldots,g_k)\in G^k:w(g_1,\ldots,g_k)=g\}|}{|G|^k}.
```
The Amit–Ashurst conjecture asserts that, for every finite nilpotent group $`G`$,

<a id="label-eq-aa"></a>

```math
\tag{1}
 P_{w,G}(g)\ge |G|^{-1}\qquad(w\in F_k,\ g\in w(G)).
```

The formulation appears in Ashurst’s thesis [\[2, Conjecture 6.2.1\]](#ref-A) and is discussed under this name by Camina, Cocke and Thillaisundaram [\[3\]](#ref-CCT). It strengthens the Amit conjecture, which concerns only the identity fibre. We always permit arbitrary $`k\ge1`$, including words with zero exponent sums. The identity word causes no exception to [(1)](#label-eq-aa).

A group is metacyclic if it has a cyclic normal subgroup with cyclic quotient. Our first main conclusion is the following.

<a id="theorem-1"></a>

**Theorem 1.1.**

<a id="label-thm-metacyclic"></a>

Every finite nilpotent metacyclic group satisfies the Amit–Ashurst conjecture. In particular, for every finite metacyclic $`p`$-group $`G`$, every $`w\in F_k`$, and every $`g\in w(G)`$,
```math
|w^{-1}(g)|\ge |G|^{k-1}.
```
No splitting hypothesis is required.

<!-- end theorem-1 -->

Camina, Cocke and Thillaisundaram prove [(1)](#label-eq-aa) for finite $`p`$-groups with a cyclic maximal subgroup [\[3, Theorem A\]](#ref-CCT). Their Sections 2–3 already use linearization after fixing cyclic coordinates and polynomial arguments. Theorem [1.1](#label-thm-metacyclic) removes the cyclic-maximal-subgroup restriction. For example, $`C_{16}\rtimes_3 C_4`$ has class four and no cyclic maximal subgroup; a direct verification is given in Section [5](#label-sec-examples). Levy’s split-extension result [\[5, Proposition 1.3\]](#ref-L) supplies the identity-fibre bound for split metacyclic groups. Controlling every attained value requires an additional argument.

The second main conclusion concerns modules of arbitrary rank.

<a id="theorem-2"></a>

**Theorem 1.2.**

<a id="label-thm-elementary"></a>

Let $`G`$ be a finite $`p`$-group with an elementary abelian normal subgroup $`V`$ such that $`G/V`$ is cyclic. Then $`G`$ satisfies the Amit–Ashurst conjecture.

<!-- end theorem-2 -->

In particular, this applies to $`(C_p)^d\wr C_{p^e}`$ for all $`d\ge1`$ and $`e\ge0`$. Recent work of de las Heras, Toti and Vannacci [\[4\]](#ref-HTV) gives finer fibre estimates for selected Engel words in cyclic wreath products. Theorem [1.2](#label-thm-elementary) treats every word; it does not provide their finer estimates or settle their separate question about profinite sections.

Both results follow from a theorem about modules over finite chain rings. A finite commutative chain ring $`R`$ is a finite commutative ring with identity whose ideals form a chain. We write its ideals as
```math
R\supsetneq \pi R\supsetneq\cdots\supsetneq\pi^{\ell-1}R
 \supsetneq\pi^\ell R=0,
 \qquad |R/\pi R|=Q=p^f.
```
The field case has $`\ell=1`$ and $`\pi=0`$. Modules are unital and finite. A principal unit is an element of $`1+\pi R`$.

<a id="theorem-3"></a>

**Theorem 1.3.**

<a id="label-thm-extension"></a>

Suppose a finite group $`G`$ contains the additive group of a finite $`R`$-module $`M`$ as a normal subgroup, where $`R`$ is a finite commutative chain ring of residue characteristic $`p`$. Suppose $`G/M`$ is cyclic of $`p`$-power order and a lift of its generator acts on $`M`$ by multiplication by a principal unit of $`R`$. Then $`G`$ satisfies [(1)](#label-eq-aa).

<!-- end theorem-3 -->

The proof first establishes a sharper estimate for $`M\rtimes T`$, where $`T`$ is any finite abelian $`p`$-group acting by principal units. It then constructs a split cover of a cyclic extension. The extra strength in the split estimate is essential: no general assertion that [(1)](#label-eq-aa) descends to arbitrary quotients is used.

The finite-difference language is the established functional-degree framework; see Aichinger and Moosbauer [\[1\]](#ref-AM). We give the elementary support estimate needed here in full. The contribution is its use with a common coefficient ideal on each quotient fibre, followed by the cyclic-cover transfer. The argument does not require polynomial coordinates on a finite abelian group or a choice of digits in a chain ring.

## 2. Finite differences and word coefficients

For finite abelian groups $`H,A`$, a function $`f:H\to A`$, and $`h\in H`$, set
```math
\Delta_h f(x)=f(x+h)-f(x).
```
Say that $`f`$ has degree at most $`d`$ if every composition of $`d+1`$ difference operators annihilates it. This condition is meaningful without a field structure on either group.

<a id="lemma-1"></a>

**Lemma 2.1.**

<a id="label-lem-support"></a>

If $`f:H\to A`$ is nonzero and has degree at most $`d\ge0`$, then
```math
|\operatorname{supp}f|\ge 2^{-d}|H|,
 \qquad \operatorname{supp}f=\{x\in H:f(x)\ne0\}.
```

<!-- end lemma-1 -->

<a id="proof-1"></a>

**Proof.**

For $`d=0`$ the function is a nonzero constant. More generally a nonzero constant satisfies the assertion for every $`d`$. Otherwise choose $`h\in H`$ such that $`\Delta_h f\ne0`$. Since difference operators commute, $`\Delta_h f`$ has degree at most $`d-1`$. Induction and the containment
```math
\operatorname{supp}(\Delta_h f)\subseteq\operatorname{supp}f\ \cup\ (\operatorname{supp}f-h)
```
give $`2^{-(d-1)}|H|\le2|\operatorname{supp}f|`$. $`\square`$

<!-- end proof-1 -->

Now let $`R`$ be a finite commutative chain ring, let $`M`$ be a finite $`R`$-module, and let $`T`$ be a finite abelian $`p`$-group. Fix a homomorphism
```math
\rho:T\longrightarrow 1+\pi R.
```
Use additive notation for $`M,T`$, and form $`S=M\rtimes_\rho T`$ with multiplication

<a id="label-eq-product"></a>

```math
\tag{2}
 (m,t)(n,u)=(m+\rho(t)n,t+u).
```

For a word $`w`$, let $`a_i`$ be the exponent sum of $`x_i`$, and put

<a id="label-eq-alpha"></a>

```math
\tag{3}
 \alpha:T^k\to T,\qquad
 \alpha(t_1,\ldots,t_k)=\sum_{i=1}^k a_i t_i,
 \qquad D=|\operatorname{im}\alpha|.
```

<a id="lemma-2"></a>

**Lemma 2.2.**

<a id="label-lem-coefficients"></a>

There are functions $`c_i:T^k\to R`$ such that

<a id="label-eq-word"></a>

```math
\tag{4}
 w((m_1,t_1),\ldots,(m_k,t_k))
 =\left(\sum_{i=1}^k c_i(\mathbf t)m_i,\alpha(\mathbf t)\right).
```

Each $`c_i`$ is a finite signed sum of homomorphisms from the additive group $`T^k`$ to the multiplicative group $`1+\pi R`$.

<!-- end lemma-2 -->

<a id="proof-2"></a>

**Proof.**

Write $`w=x_{i_1}^{\epsilon_1}\cdots x_{i_n}^{\epsilon_n}`$, with $`\epsilon_j\in\{1,-1\}`$, and set
```math
L_j(\mathbf t)=\sum_{h<j}\epsilon_h t_{i_h}.
```
The inverse of $`(m,t)`$ is $`(-\rho(-t)m,-t)`$. Reading the product in [(2)](#label-eq-product) gives

<a id="label-eq-coefficient"></a>

```math
\tag{5}
 c_i(\mathbf t)=
 \sum_{\substack{j:i_j=i\\\epsilon_j=1}}\rho(L_j(\mathbf t))
 -\sum_{\substack{j:i_j=i\\\epsilon_j=-1}}\rho(L_j(\mathbf t)-t_i).
```

Both $`L_j`$ and $`L_j-t_i`$ are additive homomorphisms. Formula [(5)](#label-eq-coefficient) also covers the empty word, with all sums zero. $`\square`$

<!-- end proof-2 -->

For a fixed $`\mathbf t`$, the first coordinate of [(4)](#label-eq-word) is a homomorphism $`M^k\to M`$. Uniform inputs therefore give a uniform distribution on its image. The difficulty is to control how often a sufficiently large common image occurs as $`\mathbf t`$ varies in a prescribed fibre of $`\alpha`$.

## 3. The chain-ring estimate

<a id="label-sec-split"></a>

The ideal valuation on $`R`$ is defined by $`\nu(0)=\ell`$ and
```math
\nu(c)=j\quad\text{if }c\in\pi^jR\setminus\pi^{j+1}R.
```
In the following refined statement we assume $`M\ne0`$ is faithful. This entails no restriction on the ensuing bound [(8)](#label-eq-strong): for a nonzero module one may replace $`R`$ by $`R/\operatorname{Ann}_R(M)`$, again a chain ring with the same residue field. The action and group are unchanged.

<a id="theorem-4"></a>

**Theorem 3.1.**

<a id="label-thm-split"></a>

With the preceding notation, let $`M`$ be faithful. For $`r\in\operatorname{im}\alpha`$ define

<a id="label-eq-s"></a>

```math
\tag{6}
 s_r=\min_{\substack{\mathbf t\in\alpha^{-1}(r)\\1\le i\le k}}
       \nu(c_i(\mathbf t)).
```

Then the word image above $`r`$ is exactly $`\pi^{s_r}M\times\{r\}`$. If $`s_r<\ell`$, then for every $`b\in\pi^{s_r}M`$,

<a id="label-eq-refined"></a>

```math
\tag{7}
 P_{w,S}(b,r)\ge\frac{1}{D\,2^{s_r}|\pi^{s_r}M|}
 \ge\frac{(Q/2)^{s_r}}{D|M|}.
```

If $`s_r=\ell`$, the only value above $`r`$ is $`(0,r)`$, with probability $`1/D`$. Consequently, for arbitrary finite $`M`$, every attained $`y\in S`$ satisfies

<a id="label-eq-strong"></a>

```math
\tag{8}
 P_{w,S}(y)\ge\frac1{D|M|}\ge\frac1{|S|}.
```

<!-- end theorem-4 -->

<a id="proof-3"></a>

**Proof.**

Fix $`r\in\operatorname{im}\alpha`$, choose $`\mathbf t^0\in\alpha^{-1}(r)`$, and write $`H=\ker\alpha`$. The fibre of $`r`$ is $`\mathbf t^0+H`$, and its probability in $`T^k`$ is $`1/D`$. Put $`s=s_r`$. If $`s=\ell`$, all coefficients vanish on this fibre, which proves the asserted exceptional case.

Suppose $`s<\ell`$. Choose an index $`i`$ for which the minimum in [(6)](#label-eq-s) is attained. The function
```math
f:H\longrightarrow R/\pi^{s+1}R,
 \qquad f(h)=c_i(\mathbf t^0+h)\pmod{\pi^{s+1}R}
```
is nonzero and has degree at most $`s`$. To see this, a summand of [(5)](#label-eq-coefficient) restricted to the fibre has the form $`\chi(h)=\rho(L(\mathbf t^0+h))`$, with $`L:T^k\to T`$ additive. For $`u\in H`$,
```math
\Delta_u\chi(h)=\chi(h)(\rho(L(u))-1).
```
Thus
```math
\Delta_{u_1}\cdots\Delta_{u_{s+1}}\chi(h)
 =\chi(h)\prod_{j=1}^{s+1}(\rho(L(u_j))-1)
 \in\pi^{s+1}R.
```
The same assertion holds for the signed sum defining $`c_i`$. Lemma [2.1](#label-lem-support) shows that at least $`|H|/2^s`$ tuples in $`\alpha^{-1}(r)`$ have $`c_i(\mathbf t)`$ nonzero modulo $`\pi^{s+1}R`$. By minimality of $`s`$, this means $`\nu(c_i(\mathbf t))=s`$.

For every $`\mathbf t\in\alpha^{-1}(r)`$, all the coefficients in [(4)](#label-eq-word) lie in $`\pi^sR`$. Its base image is therefore contained in $`\pi^sM`$. At each of the tuples just counted, $`c_i(\mathbf t)=\pi^s v`$ for a unit $`v\in R`$, so $`c_i(\mathbf t)M=\pi^sM`$. The base map is then onto $`\pi^sM`$. In particular, the entire image above $`r`$ is exactly $`\pi^sM\times\{r\}`$.

At each such tuple the conditional probability of any prescribed $`b\in\pi^sM`$ is $`1/|\pi^sM|`$. Multiplying by the fraction of these tuples and by the top-fibre probability gives
```math
P_{w,S}(b,r)\ge\frac1D\frac1{2^s}\frac1{|\pi^sM|}.
```
It remains to compare the module sizes. For $`0\le j<\ell`$, $`\pi^jM/\pi^{j+1}M`$ is a nonzero vector space over $`R/\pi R`$. Indeed, equality $`\pi^jM=\pi^{j+1}M`$ would iterate to $`\pi^jM=0`$, contradicting $`\pi^{\ell-1}M\ne0`$, which follows from faithfulness. Consequently,

<a id="label-eq-length"></a>

```math
\tag{9}
 \frac{|M|}{|\pi^sM|}
 =\prod_{j=0}^{s-1}|\pi^jM/\pi^{j+1}M|\ge Q^s\ge2^s.
```

This proves [(7)](#label-eq-refined) and [(8)](#label-eq-strong) for nonzero $`M`$, including after the faithful reduction. For $`M=0`$, the group is $`T`$, the word map is $`\alpha`$, and its attained values all have probability $`1/D`$. $`\square`$

<!-- end proof-3 -->

<a id="remark-1"></a>

**Remark 3.2.**

The coefficient itself, with values in $`R/\pi^{s+1}R`$, is the function to which the difference lemma is applied. No assertion is needed about the functional degree of a separately chosen $`\pi`$-adic digit. Also, $`H`$ may have mixed cyclic exponents: the proof works on its actual additive group.

<!-- end remark-1 -->

The lower bound $`1/|S|`$ is sharp uniformly over words, since $`w=x_1`$ is uniformly distributed. Estimate [(7)](#label-eq-refined) records additional information when the coefficient ideal is deep. More importantly for nonsplit groups, [(8)](#label-eq-strong) retains the image size $`D`$ instead of replacing it by $`|T|`$.

## 4. Cyclic extensions and attained lifts

<a id="label-sec-transfer"></a>

We prove Theorem [1.3](#label-thm-extension). The case $`M=0`$ is abelian, so suppose $`M\ne0`$ and replace $`R`$ by $`R/\operatorname{Ann}_R(M)`$. Let $`G/M`$ have order $`q=p^e`$, and let $`b\in G`$ lift a generator. Write $`u\in1+\pi R`$ for its scalar action. Since $`b^q\in M`$ and $`M`$ is abelian, $`u^q=1`$ on $`M`$, hence in $`R`$ by faithfulness.

Regard
```math
c=b^q\in M
```
as an element of the additive module, and write $`|\langle c\rangle|=p^h`$. We have $`uc=c`$. The order of $`b`$ is $`qp^h`$: an exponent killing $`b`$ must be divisible by $`q`$, and $`b^{qj}=1`$ precisely when $`p^h`$ divides $`j`$. Form
```math
L=M\rtimes_u C_{p^{e+h}}.
```
The map

<a id="label-eq-cover"></a>

```math
\tag{10}
 \varphi:L\longrightarrow G,\qquad \varphi(m,j)=m b^j
```

is a well-defined surjective homomorphism, where $`M`$ is identified with its normal subgroup in the displayed product. Its kernel is

<a id="label-eq-kernel"></a>

```math
\tag{11}
 K=\{(-tc,tq):t\in\mathbb Z/p^h\mathbb Z\}=\langle(-c,q)\rangle.
```

This subgroup is central: $`u^q=1`$ and $`uc=c`$ show that $`(-c,q)`$ commutes with $`M`$ and with the cyclic complement. Thus $`K`$ is central cyclic of order $`p^h`$, and $`|G|=|M|p^e`$.

Fix a word $`w`$ with exponent sums $`a_1,\ldots,a_k`$. Put
```math
t=\min_i\nu_p(a_i),\qquad \nu_p(0)=\infty.
```
For $`t=\infty`$, expressions of the form $`p^{\max(v-t,0)}`$ below mean $`1`$. The image size of the exponent-sum map on the complement of $`L`$ is
```math
D=p^{\max(e+h-t,0)}.
```
By Theorem [3.1](#label-thm-split), every attained $`y\in L`$ satisfies

<a id="label-eq-coverbound"></a>

```math
\tag{12}
 P_{w,L}(y)\ge\frac1{|M|D}.
```

For central elements $`z_i\in K`$ and arbitrary $`x_i\in L`$, direct collection gives

<a id="label-eq-centralvariation"></a>

```math
\tag{13}
 w(x_1z_1,\ldots,x_kz_k)=w(x_1,\ldots,x_k)\prod_{i=1}^kz_i^{a_i}.
```

Let $`a=\gcd(a_1,\ldots,a_k)`$, with $`a=0`$ if all $`a_i=0`$, and set $`K^a=\{z^a:z\in K\}`$. The products on the right of [(13)](#label-eq-centralvariation) range over $`K^a`$. Hence, if $`y`$ is attained, every element of $`yK^a`$ is attained and projects to $`\varphi(y)`$. Since $`K`$ is cyclic,

<a id="label-eq-powerimage"></a>

```math
\tag{14}
 |K^a|=p^{\max(h-t,0)}.
```

Now take $`g\in w(G)`$. Lifting any input tuple attaining $`g`$ gives an attained $`y\in\varphi^{-1}(g)`$. Uniform inputs in $`L`$ project to uniform inputs in $`G`$, so

<a id="label-eq-pushforward"></a>

```math
\begin{align}
 P_{w,G}(g)
 &=\sum_{z\in\varphi^{-1}(g)}P_{w,L}(z)\notag\\
 &\ge\frac{|K^a|}{|M|D}
 =\frac{1}{|M|p^{\max(e+h-t,0)-\max(h-t,0)}}.
 \tag{15}
\end{align}
```
For finite $`t\le h`$ the exponent difference is $`e`$; for $`t>h`$ it is at most $`e`$. It is zero when $`t=\infty`$. Thus [(15)](#label-eq-pushforward) is at least $`1/(|M|p^e)=1/|G|`$, proving Theorem [1.3](#label-thm-extension).

<a id="remark-2"></a>

**Remark 4.1.**

The proof gives the stronger bound displayed in [(15)](#label-eq-pushforward). In particular, if every exponent sum is divisible by $`p^{e+h}`$, every attained value has probability at least $`1/|M|`$. The order $`p^{e+h}`$ here is the order of the chosen lift $`b`$. The ordinary bound $`1/|L|`$ would lose a factor $`|K|`$ and would not suffice for the argument.

<!-- end remark-2 -->

## 5. Consequences and examples

<a id="label-sec-examples"></a>

<a id="proof-4"></a>

**Proof of Theorem [1.1](#label-thm-metacyclic).**

First let $`G`$ be a finite metacyclic $`p`$-group, with normal cyclic subgroup $`M=C_{p^a}`$ and cyclic quotient. If $`M=1`$, the group is cyclic. Otherwise take $`R=\mathbb Z/p^a\mathbb Z`$ and identify $`M`$ with its additive module. Conjugation by a lift of a quotient generator is multiplication by a unit $`u`$. This automorphism has $`p`$-power order. Its reduction in $`\mathbb F_p^\times`$ is therefore trivial, since that group has order $`p-1`$. Hence $`u\in1+pR`$, including for $`p=2`$, and Theorem [1.3](#label-thm-extension) applies.

For a finite nilpotent metacyclic group $`G`$, choose a cyclic normal subgroup $`C`$ with cyclic quotient. Every Sylow subgroup $`P`$ is metacyclic: $`P\cap C`$ is cyclic and normal in $`P`$, and $`P/(P\cap C)`$ embeds in $`G/C`$. Finally, $`G`$ is the direct product of its Sylow subgroups, and word probabilities multiply across direct products. Multiplying the bounds for the Sylow components proves [(1)](#label-eq-aa). $`\square`$

<!-- end proof-4 -->

<a id="proof-5"></a>

**Proof of Theorem [1.2](#label-thm-elementary).**

Suppose $`|G/V|=p^e`$ and let $`A`$ be the linear automorphism of the $`\mathbb F_p`$-space $`V`$ induced by a lift. Since $`V`$ is abelian, $`A^{p^e}=I`$. Thus $`N=A-I`$ satisfies $`N^{p^e}=0`$. Give $`V`$ its module structure over
```math
R=\mathbb F_p[z]/(z^{p^e}),\qquad zv=Nv.
```
The lift acts by the principal unit $`1+z`$. Apply Theorem [1.3](#label-thm-extension). This also covers $`e=0`$; if $`V=0`$ the assertion is immediate. $`\square`$

<!-- end proof-5 -->

<a id="corollary-1"></a>

**Corollary 5.1.**

For every $`d\ge1`$ and $`e\ge0`$, the regular wreath product $`(C_p)^d\wr C_{p^e}`$ satisfies [(1)](#label-eq-aa) for every word. If its exponent sums are all divisible by $`p^e`$, every attained value has probability at least the reciprocal of the order of the base group.

<!-- end corollary-1 -->

<a id="proof-6"></a>

**Proof.**

The base is elementary abelian and the complement cyclic, so Theorem [1.2](#label-thm-elementary) proves the first assertion. For the second, use the split realization and [(8)](#label-eq-strong), with $`D=1`$. $`\square`$

<!-- end proof-6 -->

The absence of a nilpotency-class bound is substantive. In $`C_p\wr C_{p^e}`$, with $`e\ge1`$, the regular base module is
```math
M=\mathbb F_p[C_{p^e}]\cong\mathbb F_p[z]/(z^{p^e}),
```
where the complement generator acts as $`1+z`$. Its commutator with $`M`$ has image $`zM`$, and successive lower-central terms are $`\gamma_j(G)=z^{j-1}M`$ for $`j\ge2`$. Thus the class is $`p^e`$.

For a small example outside the cyclic-maximal-subgroup case, consider
```math
G=(\mathbb Z/16\mathbb Z)\rtimes_3(\mathbb Z/4\mathbb Z).
```
This is defined since $`3^4\equiv1\pmod{16}`$. Its lower-central terms have orders
```math
64,\quad 8,\quad 4,\quad 2,\quad 1,
```
because $`\gamma_j(G)=2^{j-1}(\mathbb Z/16\mathbb Z)`$ for $`j\ge2`$. Every element has order dividing $`16`$. Indeed, for $`(m,t)\in G`$,
```math
(m,t)^{16}=\left(m\sum_{j=0}^{15}3^{tj},0\right)=(0,0).
```
For $`t=0,2`$, the sums modulo $`16`$ are respectively $`16`$ and $`8(1+9)`$; for $`t=1,3`$, they consist of four periods with sum $`1+3+9+11=24`$. All are divisible by $`16`$. A cyclic maximal subgroup would have order $`32`$, impossible by the exponent bound. Thus this class-four example is covered by Theorem [1.1](#label-thm-metacyclic) but not by the cyclic-maximal-subgroup hypothesis.

The split theorem also permits mixed-length modules over $`\mathbb Z/p^a\mathbb Z`$ and abelian complements of arbitrary rank, provided their actions are scalar principal units. Freeness of the module is not required. All these conclusions belong to the same chain-ring argument.

## 6. Scope and further questions

The proof singles out two properties. First, after fixing the quotient coordinates, a word is linear in the base variables. Second, all coefficient ideals are comparable, so a coefficient of least valuation supplies an image containing every other conditional image. Finite differences then ensure that this largest image occurs sufficiently often.

These properties suggest the next question: does every finite $`p`$-group with an abelian normal subgroup and cyclic quotient satisfy [(1)](#label-eq-aa)? Theorem [1.3](#label-thm-extension) answers it when the action is represented by a principal unit over a chain ring. An arbitrary action on an abelian $`p`$-group can instead generate a commutative ring with incomparable ideals. The common-image argument then does not follow from the present proof. Nor do we treat arbitrary nonsplit extensions by noncyclic abelian quotients. The general Amit–Ashurst conjecture remains unresolved here.

**Computational checks.**

The proofs above do not depend on computation. Accompanying scripts compare complete word distributions from literal multiplication with coefficient calculations and with pushforward through the split cover. The recorded checks comprise 22 models, 745 word distributions, 110,451,815 literal word evaluations, and 20,302 attained fibres. They include residue characteristics two and three, mixed module lengths, abelian complements of rank two, and nonsplit quaternion and module extensions. These finite checks test the implementations and small instances; they are not a substitute for the universal arguments.

## References

<a id="ref-AM"></a>

**\[1\]** E. Aichinger and J. Moosbauer, *Chevalley–Warning type results on abelian groups*, J. Algebra **569** (2021), 30–66. [doi:10.1016/j.jalgebra.2020.10.033](https://doi.org/10.1016/j.jalgebra.2020.10.033); preprint [arXiv:1912.08448](https://arxiv.org/abs/1912.08448).

<a id="ref-A"></a>

**\[2\]** C. Ashurst, *Fibres of words in finite groups, a probabilistic approach*, Ph.D. thesis, University of Bath, 2012. [University of Bath repository](https://researchportal.bath.ac.uk/en/studentTheses/fibres-of-words-in-finite-groups-a-probabilistic-approach/).

<a id="ref-CCT"></a>

**\[3\]** R. D. Camina, W. L. Cocke and A. Thillaisundaram, *The Amit–Ashurst conjecture for finite metacyclic $`p`$-groups*, Eur. J. Math. **9** (2023), article 46. [doi:10.1007/s40879-023-00644-x](https://doi.org/10.1007/s40879-023-00644-x).

<a id="ref-HTV"></a>

**\[4\]** I. de las Heras, T. Toti and M. Vannacci, *Engel probability in wreath products of $`p`$-groups*, preprint, July 2026. [arXiv:2607.11605v1](https://arxiv.org/abs/2607.11605).

<a id="ref-L"></a>

**\[5\]** M. Levy, *On the probability of satisfying a word in nilpotent groups of class 2*, preprint, 2011. [arXiv:1101.4286v1](https://arxiv.org/abs/1101.4286).
