# Paley cliques and nonpolynomial counts of totally positive matrices

Henry Zweiman

September 9, 2026

## Abstract

An element of a finite field is positive if it is a nonzero square, and a matrix is totally positive if all its minors are positive. We determine the number of totally positive two-by-three matrices over every finite field. For a fixed prime $`p`$, this count is polynomial in the field size on residue classes of the extension degree if and only if $`p=2`$ or $`p\equiv3\pmod4`$. For every prime $`p\equiv1\pmod4`$, no polynomial formula holds even eventually on any arithmetic progression of extension degrees. This disproves the quasipolynomial-type conjecture of Ayyer and Prasad in the smallest possible number of matrix entries. The proof reduces two-row total positivity to Paley clique counts and uses the known four-clique formula of Dawsey and McCarthy. We identify the surviving Gaussian exponential terms and the exact minimal recurrence of order seventeen.

## 1. Introduction and results

Let $`S_q=\{x^2:x\in\mathbb F_q^\times\}`$. Following the finite-field positivity convention used in [\[1\]](#ref-AP), call the elements of $`S_q`$ positive. For positive integers $`m,n`$, let $`\operatorname{TP}_{m,n}(\mathbb F_q)`$ consist of the matrices all of whose square minors belong to $`S_q`$. Rows and columns in a minor retain their natural order. In particular all entries must be nonzero squares. Write
```math
T_{m,n}(q)=|\operatorname{TP}_{m,n}(\mathbb F_q)|,\qquad T(q)=T_{2,3}(q).
```

Ayyer and Prasad [\[1, Conjecture 5.12\]](#ref-AP) ask whether, for each prime $`p`$ and pair $`m,n`$, there is a positive integer $`t`$ and rational polynomials $`g_0,\ldots,g_{t-1}`$ of degree $`mn`$ such that

<a id="label-eq-conjecture"></a>

```math
\tag{1}
 T_{m,n}(p^k)=g_i(p^k)\quad\text{whenever }k\equiv i\pmod t.
```

Their structural formula from zeta-function rationality is a finite sum of powers of algebraic numbers. The additional restriction in [(1)](#label-eq-conjecture) is much stronger. The distinction already matters for two-by-three matrices.

<a id="theorem-1"></a>

**Theorem 1.**

<a id="label-thm-count"></a>

For every prime power $`q`$,

<a id="label-eq-count"></a>

```math
\tag{2}
 T(q)=
 \begin{cases}
 (q-1)^4(q-2)(q-3),&q\text{ even},\\[3pt]
 \dfrac{(q-1)^4(q-3)(q-7)}{512},&q\equiv3\pmod4,\\[7pt]
 \dfrac{(q-1)^4\big((q-9)^2-4y^2\big)}{512},&q\equiv1\pmod4.
 \end{cases}
```

In the last line, write $`q=p^k=x^2+y^2`$ with $`y`$ even, choosing $`p\nmid x`$ when $`p\equiv1\pmod4`$. When $`p\equiv3\pmod4`$ and $`k`$ is even, take $`y=0`$. The value of $`y^2`$ is determined by these conditions.

<!-- end theorem-1 -->

<a id="theorem-2"></a>

**Theorem 2.**

<a id="label-thm-towers"></a>

Fix a prime $`p`$. The sequence $`T(p^k)`$ has polynomial formulas in $`p^k`$ on finitely many residue classes of $`k`$ if and only if
```math
p=2\quad\text{or}\quad p\equiv3\pmod4.
```
If $`p\equiv1\pmod4`$, then for every $`t\ge1`$ and $`r\ge0`$ there is no polynomial $`P\in\mathbb Q[X]`$ such that
```math
T(p^{r+t\ell})=P(p^{r+t\ell})
```
for all sufficiently large integers $`\ell`$. Thus [(1)](#label-eq-conjecture) fails for $`(m,n)=(2,3)`$ and every such prime, including $`p=5`$.

<!-- end theorem-2 -->

<a id="corollary-1"></a>

**Corollary 3.**

<a id="label-cor-minimal"></a>

Six is the smallest number of entries in a matrix size for which Conjecture 5.12 of [\[1\]](#ref-AP) can fail. Both sizes $`2\times3`$ and $`3\times2`$ exhibit failure.

<!-- end corollary-1 -->

Our proof also identifies the minimal constant-coefficient recurrence. If $`p\equiv1\pmod4`$, choose $`p=a^2+b^2`$ with $`a`$ odd and $`b`$ nonzero and even, and put

<a id="label-eq-alpha"></a>

```math
\tag{3}
 \pi=a+bi,\qquad \alpha=\pi^2,\qquad A=\alpha+\overline\alpha=2(a^2-b^2).
```

<a id="theorem-3"></a>

**Theorem 4.**

<a id="label-thm-recurrence"></a>

For $`p\equiv1\pmod4`$, the sequence $`T(p^k)`$ has minimal constant-coefficient recurrence over $`\mathbb Q`$ of order seventeen. Its characteristic polynomial is

<a id="label-eq-recurrence"></a>

```math
\tag{4}
 \prod_{d=0}^6(X-p^d)
 \prod_{j=0}^4\left(X^2-Ap^jX+p^{2j+2}\right).
```

Every arithmetic-progression subsequence also has minimal recurrence order seventeen.

<!-- end theorem-3 -->

The four-clique evaluation used below is an existing result [\[2, Corollary 2.3\]](#ref-DM), extending work of Evans, Pulham, and Sheehan. We do not claim a new Paley clique formula. The contribution is its connection to total positivity and the resulting exact characteristic-dependent obstruction to the proposed polynomial form. The complete count, counterexample, and recurrence are consequences of this one connection. We make no claim here about the separate positive-semidefinite counting conjecture in [\[1, Conjecture 4.31\]](#ref-AP).

## 2. Two rows and Paley graphs

The normalization underlying our argument works for any number of columns.

<a id="proposition-1"></a>

**Proposition 5.**

<a id="label-prop-normalization"></a>

Let $`s=|S_q|`$. Then $`T_{2,n}(q)`$ equals $`s^n`$ times the number of ordered tuples $`(r_1,\ldots,r_n)`$ satisfying

<a id="label-eq-tuple"></a>

```math
\tag{5}
 r_i\in S_q\quad(1\le i\le n),\qquad
 r_j-r_i\in S_q\quad(i<j).
```

If $`q\equiv1\pmod4`$ and $`K_{n+1}(P_q)`$ denotes the number of unordered $`(n+1)`$-vertex cliques in the Paley graph, then

<a id="label-eq-cliques"></a>

```math
\tag{6}
 T_{2,n}(q)=\left(\frac{q-1}{2}\right)^n
 \frac{(n+1)!}{q}K_{n+1}(P_q).
```

<!-- end proposition-1 -->

<a id="proof-1"></a>

**Proof.**

Write the columns of the matrix as $`(a_i,b_i)^T`$. Its entries are positive exactly when $`a_i\in S_q`$ and $`r_i=b_i/a_i\in S_q`$. The minor in columns $`i<j`$ is
```math
a_ib_j-a_jb_i=a_ia_j(r_j-r_i).
```
Since $`a_ia_j`$ is a nonzero square, positivity is equivalent to [(5)](#label-eq-tuple). Each admissible tuple has exactly $`s^n`$ choices of the first row.

For $`q\equiv1\pmod4`$, minus one is a square, so adjacency in $`P_q`$ is symmetric. The tuple condition says precisely that $`(0,r_1,\ldots,r_n)`$ is an ordered clique. There are $`(n+1)!K_{n+1}(P_q)`$ ordered cliques altogether. Translating the first vertex to zero is a bijection between ordered cliques with any prescribed first vertex and those with first vertex zero. Division by $`q`$ gives [(6)](#label-eq-cliques). $`\square`$

<!-- end proof-1 -->

For even $`q`$, the set $`S_q`$ is all of $`\mathbb F_q^\times`$. The tuple condition simply requires distinct nonzero entries, and hence

<a id="label-eq-even"></a>

```math
\tag{7}
 T_{2,n}(q)=(q-1)^n\prod_{h=1}^n(q-h).
```

When $`n\ge q`$, the product contains a zero factor, as it should. This recovers the characteristic-two formula in [\[1, Section 5.1\]](#ref-AP).

## 3. The exact two-by-three count

We first dispose of the directed case with an elementary character sum.

<a id="lemma-1"></a>

**Lemma 6.**

<a id="label-lem-tournament"></a>

Suppose $`q\equiv3\pmod4`$. In the tournament whose vertices are $`S_q`$ and whose arrows point from $`x`$ to $`y`$ when $`y-x\in S_q`$, every vertex has outdegree $`(q-3)/4`$.

<!-- end lemma-1 -->

<a id="proof-2"></a>

**Proof.**

Let $`\chi`$ be the quadratic character, with $`\chi(0)=0`$. For a fixed $`x\in S_q`$, division by $`x`$ reduces its outdegree to the number of $`z`$ such that $`z,z-1\in S_q`$. Excluding $`z=0,1`$, this is
```math
\frac14\sum_{z\ne0,1}(1+\chi(z))(1+\chi(z-1)).
```
The two linear character sums here are $`-1`$ and $`-\chi(-1)=1`$. Also
```math
\sum_{z\in\mathbb F_q}\chi(z(z-1))=-1.
```
To see the last identity directly, the number of solutions of $`w^2=z(z-1)`$ is $`q`$ plus that sum. The substitution $`u=2z-1`$, $`v=2w`$ turns the equation into $`(u-v)(u+v)=1`$, which has exactly $`q-1`$ solutions since the characteristic is odd. The outdegree is therefore $`(q-3)/4`$. Since $`\chi(-1)=-1`$, exactly one of the two possible arrows occurs between any two distinct vertices. $`\square`$

<!-- end proof-2 -->

<a id="proof-3"></a>

**Proof of Theorem [1](#label-thm-count).**

For even $`q`$, apply [(7)](#label-eq-even) with $`n=3`$. For $`q\equiv3\pmod4`$, the normalized tuples in Proposition [5](#label-prop-normalization) are the transitive triples in the tournament of Lemma [6](#label-lem-tournament), with their unique forward ordering. Every such triple has a unique source. A vertex has $`d=(q-3)/4`$ outgoing neighbors, and each unordered pair of those neighbors gives one transitive triple with that source. The number of tuples is
```math
\frac{q-1}{2}\binom{(q-3)/4}{2}
 =\frac{(q-1)(q-3)(q-7)}{64}.
```
Multiplication by $`((q-1)/2)^3`$ gives the second line of [(2)](#label-eq-count). The formula also applies at $`q=3,7`$, where the count is zero.

For $`q\equiv1\pmod4`$, the known formula [\[2, Corollary 2.3\]](#ref-DM) is

<a id="label-eq-known"></a>

```math
\tag{8}
 K_4(P_q)=\frac{q(q-1)\big((q-9)^2-4y^2\big)}{2^9\cdot3},
```

with exactly the representation conditions on $`x,y`$ in the theorem. Substituting [(8)](#label-eq-known) in [(6)](#label-eq-cliques), and using $`4!=24`$, gives the last line of [(2)](#label-eq-count). $`\square`$

<!-- end proof-3 -->

The distinction between a prime field and a prime-power field is essential in [(8)](#label-eq-known). For split primes the condition $`p\nmid x`$ selects the primitive Gaussian representation; choosing an arbitrary representation of $`q`$ as two squares can give an incorrect count.

## 4. Extension degrees and nonpolynomiality

Fix $`p\equiv1\pmod4`$ and use [(3)](#label-eq-alpha). The Gaussian integers form a unique factorization domain, and $`\pi`$ and $`\overline\pi`$ are nonassociate primes above $`p`$. Write
```math
\pi^k=x_k+iy_k.
```
Then $`x_k`$ is odd, $`y_k`$ is even, and $`x_k^2+y_k^2=p^k`$. Moreover $`p\nmid x_k`$: modulo the Gaussian prime $`\pi`$, the equality
```math
2x_k=\pi^k+\overline\pi^{,k}
```
has a nonzero right-hand side. Thus this is an admissible representation in Theorem [1](#label-thm-count). With
```math
u_k=\alpha^k+\overline\alpha^{,k}
 =2(x_k^2-y_k^2)=2p^k-4y_k^2,
```
we obtain the exact formula

<a id="label-eq-exponential"></a>

```math
\tag{9}
 512T(p^k)=(p^k-1)^4\left(p^{2k}-20p^k+81+u_k\right).
```

In particular,

<a id="label-eq-u"></a>

```math
\tag{10}
 u_0=2,\qquad u_1=A,\qquad u_{k+2}=Au_{k+1}-p^2u_k.
```

<a id="lemma-2"></a>

**Lemma 7.**

<a id="label-lem-nontorsion"></a>

Neither $`\alpha/p`$ nor $`\alpha/\overline\alpha`$ is a root of unity.

<!-- end lemma-2 -->

<a id="proof-4"></a>

**Proof.**

We have $`\alpha/p=\pi/\overline\pi`$. If a positive power of this quotient were one, unique factorization would equate positive powers of the distinct Gaussian primes $`\pi`$ and $`\overline\pi`$. This is impossible. The second quotient is $`(\pi/\overline\pi)^2`$, so it is not torsion either. $`\square`$

<!-- end proof-4 -->

We use a standard elementary independence fact: if $`z_1,\ldots,z_h`$ are distinct nonzero complex numbers, then the sequences $`z_i^\ell`$ are linearly independent, even when restricted to all sufficiently large $`\ell`$. Indeed $`h`$ consecutive equations give a Vandermonde matrix, multiplied by a nonsingular diagonal matrix.

<a id="proof-5"></a>

**Proof of Theorem [2](#label-thm-towers).**

When $`p=2`$, the first line of [(2)](#label-eq-count) is a polynomial of degree six. When $`p\equiv3\pmod4`$, the odd and even extension degrees have respectively the polynomials
```math
\frac{(X-1)^4(X-3)(X-7)}{512},\qquad
 \frac{(X-1)^4(X-9)^2}{512}.
```

Now suppose $`p\equiv1\pmod4`$. Expanding [(9)](#label-eq-exponential) expresses $`512T(p^k)`$ as a sum of powers with bases

<a id="label-eq-bases"></a>

```math
\tag{11}
 1,p,\ldots,p^6,
 \qquad p^j\alpha,\ p^j\overline\alpha\quad(0\le j\le4).
```

The seven coefficients in the first group, in increasing order of powers of $`p^k`$, are
```math
81,\ -344,\ 567,\ -448,\ 167,\ -24,\ 1.
```
Each coefficient in the second group is $`(-1)^{4-j}\binom4j`$, so all seventeen coefficients are nonzero.

These bases remain pairwise distinct after taking any positive integral power $`t`$. Distinct absolute values separate different values of $`j`$ in the second group. For a fixed $`j`$, the two conjugate bases cannot acquire equal $`t`$-th powers by Lemma [7](#label-lem-nontorsion). A base from the second group cannot acquire the same $`t`$-th power as any $`p^d`$: equality of absolute values would give $`d=j+1`$, and equality of values would force $`(\alpha/p)^t=1`$ or its conjugate. The bases in the first group are already distinct positive reals.

On restricting to $`k=r+t\ell`$, every coefficient is multiplied by the nonzero $`r`$-th power of its base, and every base is replaced by its $`t`$-th power. A polynomial in $`p^{r+t\ell}`$ is a linear combination only of sequences with bases $`p^{dt}`$, $`d\ge0`$. Subtracting it from the expansion leaves nonzero coefficients at all ten bases from the second group. The independence fact above rules out eventual equality. This proves the stated stronger failure on every progression. $`\square`$

<!-- end proof-5 -->

<a id="proof-6"></a>

**Proof of Corollary [3](#label-cor-minimal).**

If $`mn<6`$, then either $`m=1`$, $`n=1`$, or $`m=n=2`$. A one-row or one-column count is $`|S_q|^{mn}`$, which is polynomial in $`q`$ for each characteristic. The two-by-two counts, also given in [\[1, Section 5.1\]](#ref-AP), are
```math
T_{2,2}(q)=
 \begin{cases}
 (q-1)^3(q-2),&q\text{ even},\\
 (q-1)^3(q-5)/32,&q\equiv1\pmod4,\\
 (q-1)^3(q-3)/32,&q\equiv3\pmod4.
 \end{cases}
```
They follow by the same normalization and the count of simultaneous squares $`z,z-1`$. For each fixed prime these formulas have period at most two in the extension degree. Theorem [2](#label-thm-towers) supplies the six-entry counterexample. Transposition preserves all minors and gives the other orientation. $`\square`$

<!-- end proof-6 -->

## 5. The exact recurrence and its meaning

<a id="proof-7"></a>

**Proof of Theorem [4](#label-thm-recurrence).**

A sequence $`z^k`$ is annihilated by the shift operator minus $`z`$. Thus the expansion with bases [(11)](#label-eq-bases) is annihilated by the product of these seventeen linear factors. Pairing conjugate factors gives [(4)](#label-eq-recurrence), since $`\alpha\overline\alpha=p^2`$.

Conversely, if a polynomial $`H`$ in the shift operator annihilates the sequence, applying it to the expansion multiplies the coefficient at each base $`z`$ by $`H(z)`$. Independence and nonzero coefficients force $`H`$ to vanish at all seventeen distinct bases. Hence its degree is at least seventeen. The product in [(4)](#label-eq-recurrence) has rational, indeed integer, coefficients, proving minimality over $`\mathbb Q`$. The same argument applies to every progression, using the noncollision proof in Theorem [2](#label-thm-towers). $`\square`$

<!-- end proof-7 -->

For the simplest prime $`p=5`$, take $`\pi=1+2i`$, so $`A=-6`$ and
```math
u_{k+2}=-6u_{k+1}-25u_k,\qquad u_0=2,\ u_1=-6.
```
The initial matrix counts are
```math
T(5)=0,\qquad T(25)=124416,\qquad T(125)=6206061120.
```
The general proof does not infer nonpolynomiality from these initial values. It identifies bases that cannot become powers of $`p`$ after any finite periodic restriction.

The generating function of $`T(p^k)`$ is rational, as the zeta-function approach in [\[1\]](#ref-AP) predicts. The obstruction is the presence of the ten bases $`p^j\alpha`$ and $`p^j\overline\alpha`$, rather than a failure of rationality. More generally, whenever a counting sequence is given as a finite sum of exponentials, one must group bases whose ratios are roots of unity before testing for polynomial behavior on progressions. A surviving base outside the powers of $`p`$ times roots of unity prevents the proposed form. Here the arithmetic of split Gaussian primes verifies that no such cancellation occurs.

The correspondence [(6)](#label-eq-cliques) also relates wider two-row matrices to larger Paley cliques. It offers a way to transfer counting information and existence bounds between the two problems. Exact higher-column formulas and the separate semidefinite conjecture are not settled in this paper.

## Preparation and verification

This manuscript was prepared with OpenAI Codex assistance in problem selection, proof development, literature checking, computation, and writing. The originating agent performed the internal audit; no human referee or separate-agent review is claimed. The accompanying assessment records the priority-search limits and credits the existing clique formula. Optional finite checks in 29 prime and extension fields, including direct enumeration of the original six entries over nine small fields, agree with the formulas. The general nonpolynomiality and minimality arguments are proofs independent of these finite checks.

## References

<a id="ref-AP"></a>

**\[1\]** A. Ayyer and S. Prasad, *Positive definite, positive semidefinite and totally positive matrices over finite fields*, arXiv:2608.17702v1 (2026). [arXiv:2608.17702v1](https://arxiv.org/abs/2608.17702v1).

<a id="ref-DM"></a>

**\[2\]** M. L. Dawsey and D. McCarthy, *Generalized Paley graphs and their complete subgraphs of orders three and four*, Research in the Mathematical Sciences **8**, article 18 (2021). [arXiv:2006.14716](https://arxiv.org/abs/2006.14716).
