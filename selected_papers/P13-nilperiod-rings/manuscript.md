# Additive periods of power maps lie in the prime radical

Henry Zweiman

## Abstract

We prove that every additive period of every power map on an associative ring belongs to its prime radical. No identity, characteristic, finiteness, or polynomial-identity assumption is required. The proof combines a substitution using the highest nonzero power of a nilpotent element with the classical bounded-index one-sided nil-ideal lemma. It follows that every nilperiod ring is 2-primal and that its nilpotents form a locally nilpotent ideal. This strengthens the NI conclusion conjectured by Burnette. We also characterize finite unital nilperiod rings as finite products of local rings, and determine the periodic power maps on Corbas rings, correcting the count for nonidentity twists.

## 1. Introduction

All rings are associative and may lack an identity unless otherwise stated. For a ring $`R`$, let $`\mathop{\mathrm{Nil}}(R)`$ be its set of nilpotent elements, and let $`P(R)`$ be its prime radical, also called the lower nilradical. Thus $`P(R)`$ is the intersection of the prime ideals, or equivalently the smallest ideal for which $`R/P(R)`$ is semiprime. The prime radical is locally nilpotent: every finite subset generates a nilpotent subring. In particular, $`P(R)`$ is a nil ideal; see, for example, [\[4, Section 1\]](#ref-Nielsen).

For an integer $`n\geq1`$, set $`\alpha_n(x)=x^n`$ and define its additive period group by
```math
\mathop{\mathrm{Per}}(\alpha_n)=\{a\in R:(x+a)^n=x^n\text{ for every }x\in R\}.
```
Evaluation at zero gives $`\mathop{\mathrm{Per}}(\alpha_n)\subseteq\mathop{\mathrm{Nil}}(R)`$. Our main result locates these periods more precisely.

<a id="theorem-1"></a>

**Theorem 1.**

<a id="label-thm-main"></a>

For every associative ring $`R`$ and every positive integer $`n`$,
```math
\mathop{\mathrm{Per}}(\alpha_n)\subseteq P(R).
```
Consequently, every power map on a semiprime ring has trivial additive period group.

<!-- end theorem-1 -->

Following Burnette [\[2\]](#ref-Burnette), a ring is *nilperiod* if every nilpotent element belongs to $`\mathop{\mathrm{Per}}(\alpha_n)`$ for some $`n`$, which may depend on the element. A ring is *NI* if its nilpotents form a two-sided ideal, and it is *2-primal* if $`\mathop{\mathrm{Nil}}(R)=P(R)`$.

<a id="corollary-1"></a>

**Corollary 2.**

<a id="label-cor-nilperiod"></a>

Every nilperiod ring is 2-primal. Its nilpotent elements form a locally nilpotent two-sided ideal, which is both its prime radical and its largest nil ideal. In particular, every nilperiod ring is an NI-ring.

<!-- end corollary-1 -->

<a id="proof-1"></a>

**Proof.**

Theorem [1](#label-thm-main) gives $`\mathop{\mathrm{Nil}}(R)\subseteq P(R)`$, while the reverse containment holds in every ring. The other conclusions follow from the standard properties of the prime radical. $`\square`$

<!-- end proof-1 -->

Burnette’s Conjecture 2.6 asks whether every nilperiod ring is NI, and his Theorem 2.9 establishes this for PI algebras. Corollary [2](#label-cor-nilperiod) proves the conjecture and strengthens its conclusion. Theorem [1](#label-thm-main) also treats individual periods in rings that need not be nilperiod. In particular, it extends the absence of nonzero periods in matrix rings over division rings used in [\[2, Lemma 2.8\]](#ref-Burnette) to all semiprime rings.

The main proof uses the classical fact that a semiprime ring has no nonzero one-sided nil ideal of bounded index. The new reduction is short: given a period $`a`$ of nilpotency index $`j`$, evaluate its identity at $`x=a^{j-1}r`$ and multiply by $`a^{j-2}r`$. This produces the bounded-index right ideal to which the classical result applies.

The remaining results concern finite rings and power-map counts. As usual, a unital ring is local if its nonunits form a proper ideal.

<a id="theorem-2"></a>

**Theorem 3.**

<a id="label-thm-finite"></a>

A nonzero finite unital ring is nilperiod if and only if it is a finite direct product of finite local rings.

<!-- end theorem-2 -->

The zero ring may be included as the empty product. The structural decomposition behind this result is standard; we explicitly credit it in Section 3. Section 4 gives an exact computation for the twisted rings in [\[2, Example 2.2\]](#ref-Burnette).

## 2. Periods in semiprime rings

We use the following classical bounded-index lemma. Its left-ideal form is stated in [\[1, p. 93, item (V)\]](#ref-BM); the right-ideal form follows by passing to the opposite ring. The bounded nilradical discussion in [\[4, Section 1\]](#ref-Nielsen) also records the result in the nonunital setting.

<a id="lemma-1"></a>

**Lemma 4 (Bounded-index one-sided nil ideals).**

<a id="label-lem-levitzki"></a>

Let $`S`$ be an associative ring, not necessarily unital. If $`S`$ has a nonzero right ideal $`I`$ and a fixed positive integer $`N`$ such that $`y^N=0`$ for every $`y\in I`$, then $`S`$ has a nonzero nilpotent two-sided ideal. In particular, a semiprime ring has no nonzero nil right ideal of bounded index.

<!-- end lemma-1 -->

This lemma requires neither a chain condition on ideals nor a restriction on the characteristic. The uniform bound concerns the elements of $`I`$, not all nilpotents of $`S`$.

<a id="proof-2"></a>

**Proof of Theorem [1](#label-thm-main).**

First let $`S`$ be semiprime and let $`a\in\mathop{\mathrm{Per}}(\alpha_n)`$. Since $`a^n=0`$, a nonzero $`a`$ has a minimal nilpotency index $`j`$ satisfying $`2\leq j\leq n`$. Suppose that this is the case, and put $`b=a^{j-1}\ne0`$.

Let $`S^1=\mathbb Z\oplus S`$ be the standard unitization, with multiplication
```math
(m,u)(k,v)=(mk,mv+ku+uv).
```
If $`S`$ already has an identity, we may take $`S^1=S`$. For any $`r\in S^1`$, the element $`x=br`$ lies in $`S`$, so the period identity applies to $`x`$. Also $`ax=a^jr=0`$. In the word expansion of $`(x+a)^n`$, a word vanishes whenever an $`a`$ occurs before an $`x`$, since such a word contains adjacent factors $`ax`$. The remaining words have the form $`x^{n-k}a^k`$, and terms with $`k\geq j`$ vanish. Hence

<a id="label-eq-expansion"></a>

```math
\tag{1}
 0=(x+a)^n-x^n=\sum_{k=1}^{j-1}x^{n-k}a^k.
```

Right-multiply [(1)](#label-eq-expansion) by $`a^{j-2}r`$, interpreting $`a^0=1`$ in $`S^1`$ if $`j=2`$. The term with $`k=1`$ becomes
```math
x^{n-1}a^{j-1}r=x^n,
```
while all terms with $`k\geq2`$ vanish because $`a^{k+j-2}=0`$. Therefore
```math
(br)^n=0\qquad(r\in S^1).
```
The nonzero principal right ideal $`bS^1=\mathbb Zb+bS`$ of $`S`$ is thus nil of bounded index $`n`$. This contradicts Lemma [4](#label-lem-levitzki), so $`a=0`$. Notice that we have only evaluated the period identity at elements of $`S`$; no period property of $`S^1`$ is assumed.

Now take an arbitrary ring $`R`$ and $`a\in\mathop{\mathrm{Per}}(\alpha_n)`$. Its period identity descends to the quotient $`R/P(R)`$. Since this quotient is semiprime, the first part of the proof shows that the image of $`a`$ is zero. Thus $`a\in P(R)`$. $`\square`$

<!-- end proof-2 -->

<a id="remark-1"></a>

**Remark 5.**

Local nilpotence in Corollary [2](#label-cor-nilperiod) does not supply a uniform nilpotency exponent for the entire ideal $`\mathop{\mathrm{Nil}}(R)`$. Nor does the proof assert that each nilpotent element generates a nilpotent two-sided ideal. It does imply that every such generated ideal is nil, since it lies in $`P(R)`$.

<!-- end remark-1 -->

## 3. Idempotents and finite rings

<a id="proposition-1"></a>

**Proposition 6.**

<a id="label-prop-central"></a>

Every idempotent in a nilperiod ring is central.

<!-- end proposition-1 -->

<a id="proof-3"></a>

**Proof.**

Let $`e^2=e`$ and $`r\in R`$. The element $`a=er-ere`$ satisfies $`a^2=0`$, $`ea=a`$, and $`ae=0`$. Thus $`e+a`$ is idempotent. A period identity for $`a`$, evaluated at $`e`$, gives
```math
e+a=(e+a)^n=e^n=e.
```
Hence $`er=ere`$. Similarly, $`b=re-ere`$ is square-zero and $`e+b`$ is idempotent, so the same argument gives $`re=ere`$. Therefore $`er=re`$. $`\square`$

<!-- end proof-3 -->

<a id="lemma-2"></a>

**Lemma 7.**

<a id="label-lem-idempotent-power"></a>

Every element of a finite ring has an idempotent positive power.

<!-- end lemma-2 -->

<a id="proof-4"></a>

**Proof.**

For $`x`$ in a finite ring there exist positive integers $`a,b`$ such that $`x^{a+b}=x^a`$. Choose $`n\geq a`$ divisible by $`b`$. Eventual periodicity of the powers then gives $`x^{2n}=x^n`$. $`\square`$

<!-- end proof-4 -->

The forward structural implication is an instance of the standard fact that an Abelian semiperfect ring is a finite direct product of local rings [\[3, Proposition 2.6\]](#ref-HLP). Finite rings are semiperfect. We include an elementary proof in this finite setting.

<a id="proof-5"></a>

**Proof of Theorem [3](#label-thm-finite).**

Suppose first that $`R`$ is finite, unital, and nilperiod. By Proposition [6](#label-prop-central), its idempotents are central. Successively split the identity into orthogonal nonzero central idempotents until each component contains no idempotents except zero and its identity. The process terminates since $`R`$ is finite. It gives
```math
R\cong R_1\times\cdots\times R_t.
```
Each direct factor is nilperiod: a nilpotent in it lifts to a nilpotent with zero coordinates in the other factors, and the corresponding period identity restricts to that factor. Its nilpotents therefore form an ideal by Corollary [2](#label-cor-nilperiod).

For $`x\in R_i`$, Lemma [7](#label-lem-idempotent-power) gives $`x^n=0`$ or $`x^n=1_{R_i}`$. Thus $`x`$ is either nilpotent or a unit. The nonunits of $`R_i`$ are exactly its nilpotents, which form a proper ideal, so $`R_i`$ is local.

Conversely, let $`R`$ be finite and local, with nonunit ideal $`M`$. Its only idempotents are zero and one: if $`e^2=e`$, one of $`e,1-e`$ is a unit, and $`e(1-e)=0`$ gives the conclusion. For $`x\in M`$, an idempotent power remains in $`M`$, so it must be zero. Thus $`\mathop{\mathrm{Nil}}(R)=M`$. Choose $`n`$ at least the maximum of the nilpotency indices of the elements of $`M`$, and divisible by the exponent of the finite group $`R^\times`$. Then
```math
x^n=\begin{cases}0,&x\in M,\\1,&x\notin M.\end{cases}
```
Translation by any element of $`M`$ preserves membership in $`M`$. Consequently every element of $`\mathop{\mathrm{Nil}}(R)`$ is a period of $`\alpha_n`$. For a finite direct product of finite local rings, choose one $`n`$ satisfying these requirements in all factors. $`\square`$

<!-- end proof-5 -->

<a id="example-1"></a>

**Example 8.**

An NI-ring need not be nilperiod, even when finite. The upper triangular $`2\times2`$ matrices over $`\mathbb F_2`$ have nilpotents $`\{0,E_{12}\}`$, a square-zero ideal. But for $`e=\operatorname{diag}(1,0)`$ and $`a=E_{12}`$, the distinct matrices $`e`$ and $`e+a`$ are both idempotent. Hence $`(e+a)^n\ne e^n`$ for every $`n\geq1`$.

<!-- end example-1 -->

## 4. Power maps on Corbas rings

Let $`q=p^f`$, where $`p`$ is prime and $`f\geq1`$, and choose $`0\leq s<f`$. Let $`\phi(a)=a^{p^s}`$ be the corresponding automorphism of $`\mathbb F_q`$, and put $`g=\gcd(f,s)`$. We allow $`s=0`$, so the identity automorphism has $`g=f`$. Consider the Corbas ring

<a id="label-eq-corbas"></a>

```math
\tag{2}
 R=\mathbb F_q\oplus\mathbb F_q,\qquad
 (a,b)(c,d)=(ac,ad+b\phi(c)).
```

This is an associative unital ring, with identity $`(1,0)`$ and square-zero ideal $`N=\{0\}\oplus\mathbb F_q`$. If $`a\ne0`$, the element $`(a,b)`$ has inverse
```math
\bigl(a^{-1},-a^{-1}b\phi(a^{-1})\bigr).
```
Thus $`R`$ is local and $`\mathop{\mathrm{Nil}}(R)=N`$.

The following calculation corrects the assertion in [\[2, Example 2.2 and Table 1\]](#ref-Burnette) that nonidentity twists have no periodic power maps. It also determines exactly which exponents occur.

<a id="theorem-3"></a>

**Theorem 9.**

<a id="label-thm-corbas"></a>

For the ring [(2)](#label-eq-corbas), set
```math
M=\frac{q-1}{p^g-1}.
```
Then
```math
\mathop{\mathrm{Per}}(\alpha_n)=
 \begin{cases}
 N,&pM\mid n,\\
 \{0\},&pM\nmid n.
 \end{cases}
```
There are exactly $`p^g-1`$ distinct periodic power maps on $`R`$.

<!-- end theorem-3 -->

<a id="proof-6"></a>

**Proof.**

Direct induction gives
```math
(a,b)^n=\bigl(a^n,bC_n(a)\bigr),\qquad
 C_n(a)=\sum_{j=0}^{n-1}a^j\phi(a)^{n-1-j}.
```
Every additive period must lie in $`N`$, by evaluation at zero. For $`y\ne0`$, the element $`(0,y)`$ is a period exactly when $`C_n(a)=0`$ for all $`a\in\mathbb F_q`$. At $`a=1`$ this forces $`p\mid n`$, and hence $`n\geq2`$. The condition at $`a=0`$ then holds. If $`a\ne0`$ and $`a=\phi(a)`$, then $`C_n(a)=na^{n-1}`$, which also vanishes. For $`a\ne\phi(a)`$ the geometric sum gives
```math
C_n(a)=\frac{a^n-\phi(a)^n}{a-\phi(a)}.
```
Its vanishing is equivalent to $`(a/\phi(a))^n=1`$. The homomorphism $`a\mapsto a/\phi(a)`$ on the cyclic group $`\mathbb F_q^\times`$ has kernel $`\mathbb F_{p^g}^\times`$ and therefore image of order $`M`$. Consequently $`C_n`$ vanishes everywhere if and only if $`p\mid n`$ and $`M\mid n`$. Since $`p\nmid M`$, this is $`pM\mid n`$. The argument also determines the full period group as stated.

For the count, the unit group of $`R`$ has exponent $`E=p(q-1)`$. The displayed power formula shows that every unit has $`E`$th power one. Elements $`(a,0)`$ realize order $`q-1`$, while $`(1,b)`$ with $`b\ne0`$ have order $`p`$, so the exponent is exactly $`E`$. All nonunits have square zero. Therefore, for $`n,m\geq2`$, the maps $`\alpha_n`$ and $`\alpha_m`$ agree exactly when $`n\equiv m\pmod E`$: sufficiency follows from the unit and nonunit cases, and necessity from the definition of the unit-group exponent. There are thus $`E`$ distinct maps with exponent at least two, and among their exponent classes exactly
```math
\frac{E}{pM}=p^g-1
```
are periodic. The identity map $`\alpha_1`$ is distinct from these maps on nonzero elements of $`N`$ and has no nonzero additive period. $`\square`$

<!-- end proof-6 -->

<a id="example-2"></a>

**Example 10.**

For $`q=4`$ and the nontrivial automorphism $`\phi(a)=a^2`$, one has $`p=2`$, $`g=1`$, $`M=3`$, and $`E=6`$. The power map $`\alpha_6`$ equals $`(1,0)`$ on all units and zero on $`N`$, so its period group is $`N`$. It is the unique distinct periodic power map on this noncommutative sixteen-element ring.

<!-- end example-2 -->

## References

<a id="ref-BM"></a>

**\[1\]** H. E. Bell and W. S. Martindale III, *Centralizing mappings of semiprime rings*, Canad. Math. Bull. **30** (1987), no. 1, 92–101. [doi:10.4153/CMB-1987-014-x](https://doi.org/10.4153/CMB-1987-014-x).

<a id="ref-Burnette"></a>

**\[2\]** C. Burnette, *On power maps over periodic rings*, Graduate J. Math. **10** (2025), no. 1, 5–16. [Published article](https://gradmath.org/wp-content/uploads/2025/07/GJM2025-Burnette.pdf). Earlier preprint: *On power maps over weakly periodic rings*, [arXiv:2207.14283](https://arxiv.org/abs/2207.14283).

<a id="ref-HLP"></a>

**\[3\]** J. Han, Y. Lee, and S. Park, *Structure of Abelian rings*, Front. Math. China **12** (2017), no. 1, 117–134. [doi:10.1007/s11464-016-0586-z](https://doi.org/10.1007/s11464-016-0586-z).

<a id="ref-Nielsen"></a>

**\[4\]** P. P. Nielsen, *Bootstrapping the bounded nilradical*, J. Pure Appl. Algebra **217** (2013), no. 9, 1711–1715. [doi:10.1016/j.jpaa.2012.12.002](https://doi.org/10.1016/j.jpaa.2012.12.002).
