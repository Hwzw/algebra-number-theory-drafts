# Explicit Lie polynomials with prescribed images over finite fields

Henry Zweiman

September 9, 2026

## Abstract

For every odd prime power $`q`$, we give a closed formula in two Lie variables whose image on $`\mathfrak{sl}_2(\mathbb F_q)`$ is any prescribed conjugation-invariant subset containing zero. The degree is at most $`6q-5`$. The construction converts an arbitrary scalar function of the quadratic invariant into a Lie polynomial on the locus where the commutator has nonzero determinant, and vanishes elsewhere. It answers the explicit-construction question of Kishnani and Singh in rank one. We determine all fibers of the resulting class selectors: each selected nonzero conjugacy class receives the same number of input pairs. Finally, any Lie polynomial whose image is zero together with one semisimple class has degree at least $`\lceil q/4\rceil`$, even when arbitrarily many variables are allowed. Thus a linear degree bound has the correct order.

## 1. Introduction and the explicit formula

Let $`F=\mathbb F_q`$, where $`q`$ is an odd prime power, and put $`L=\mathfrak{sl}_2(F)`$. We use the bracket $`[X,Y]=XY-YX`$ and the convention $`\operatorname{ad}_X(Y)=[X,Y]`$. A Lie polynomial belongs to the free Lie algebra over $`F`$; its syntax permits scalar coefficients, addition, and brackets, but no nonzero matrix constants. Its total degree is the largest number of variable occurrences in a nonzero homogeneous component.

Lie-polynomial images are invariant under conjugation and contain zero. Lubotzky’s theorem [\[2\]](#ref-Lubotzky) gives an analogous image classification for word maps on finite simple groups. Kishnani and Singh [\[1, Theorem 1.3\]](#ref-KS) prove an existence theorem for finite simple Chevalley Lie algebras. Their Question 1.2 asks for explicit realizing polynomials; their Section 9 gives partial constructions for $`\mathfrak{sl}_2(\mathbb F_q)`$. The contribution here is a uniform two-variable formula for every admissible subset in this rank, together with a degree bound and its exact distribution. The existence classification itself is prior work.

For $`X\in L`$ define
```math
Q(X)=-\det X,\qquad
 B(X,Y)=\tfrac12\operatorname{tr}(XY),\qquad
 \Delta(X,Y)=Q([X,Y]).
```
These invariants are used to describe evaluations. They do not appear as operations in the Lie polynomial below. For $`r(t)=\sum_{k=0}^{q-1}r_kt^k\in F[t]`$, set

<a id="label-eq-word"></a>

```math
\tag{1}
 W_r(X,Y)=-\sum_{k=0}^{q-1}r_k4^{-k}
       \operatorname{ad}_{[X,Y]}^{\,2q-3}\bigl(\operatorname{ad}_X^{\,2k+2}(Y)\bigr).
```

Here $`4^{-k}`$ denotes an element of $`F`$; in particular the formula is valid in characteristic three. Each summand is an iterated bracket in $`X,Y`$.

<a id="theorem-1"></a>

**Theorem 1.**

<a id="label-thm-main"></a>

For every polynomial $`r\in F[t]`$ of degree at most $`q-1`$,

<a id="label-eq-evaluation"></a>

```math
\tag{2}
 W_r(X,Y)=\Delta(X,Y)^{q-1}r(Q(X))X
 \qquad(X,Y\in L).
```

For $`T\subseteq F`$ define

<a id="label-eq-indicator"></a>

```math
\tag{3}
 r_T(t)=\sum_{a\in T}\bigl(1-(t-a)^{q-1}\bigr),\qquad W_T=W_{r_T}.
```

Then

<a id="label-eq-image"></a>

```math
\tag{4}
 W_T(L^2)=A_T:=\{0\}\cup\{X\in L\setminus\{0\}:Q(X)\in T\}.
```

Every conjugation-invariant subset of $`L`$ containing zero is $`A_T`$ for a unique $`T\subseteq F`$. Consequently every such subset is the image of the explicit Lie polynomial [(1)](#label-eq-word), of degree at most $`6q-5`$.

<!-- end theorem-1 -->

The theorem gives a constructive answer to [\[1, Question 1.2\]](#ref-KS) for $`L=\mathfrak{sl}_2(F)`$, with no restriction on the odd prime power $`q`$ or on the chosen union. In particular it permits arbitrary mixtures of split, nonsplit, and nilpotent classes. It does not assert an explicit construction in higher rank.

## 2. The invariant identity

We prove the matrix identities over any field of characteristic different from two, before using finiteness.

<a id="lemma-1"></a>

**Lemma 2.**

<a id="label-lem-identities"></a>

For $`X,Y\in\mathfrak{sl}_2(F)`$ and $`C=[X,Y]`$, one has

<a id="label-eq-CH"></a>

<a id="label-eq-double"></a>

<a id="label-eq-orth"></a>

<a id="label-eq-transfer"></a>

```math
\begin{align}
 X^2&=Q(X)I, & XY+YX&=2B(X,Y)I,\tag{5}\\
 \operatorname{ad}_X^2(Y)&=4\bigl(Q(X)Y-B(X,Y)X\bigr),\tag{6}\\
 B(X,C)&=0, & \operatorname{ad}_C^2(X)&=4Q(C)X,\tag{7}\\
 [C,\operatorname{ad}_X^2(Y)]&=-4Q(C)X.\tag{8}
\end{align}
```
Moreover, for every $`k\geq0`$,

<a id="label-eq-recurrence"></a>

```math
\tag{9}
 \operatorname{ad}_X^{2k+2}(Y)=(4Q(X))^k\operatorname{ad}_X^2(Y).
```

<!-- end lemma-1 -->

<a id="proof-1"></a>

**Proof.**

The first equality of [(5)](#label-eq-CH) is Cayley–Hamilton for a trace-zero matrix. Polarizing it gives the second, since $`Q(X+Y)-Q(X)-Q(Y)=\operatorname{tr}(XY)`$. Multiplication by $`X`$ gives $`XYX=2B(X,Y)X-Q(X)Y`$, whence
```math
[X,[X,Y]]=X^2Y-2XYX+YX^2
          =4Q(X)Y-4B(X,Y)X.
```
Cyclicity of trace gives $`2B(X,C)=\operatorname{tr}(X^2Y)-\operatorname{tr}(XYX)=0`$. Applying [(6)](#label-eq-double) to $`C,X`$ proves [(7)](#label-eq-orth). As $`\operatorname{ad}_X^2(Y)=[X,C]`$, antisymmetry now gives
```math
[C,\operatorname{ad}_X^2(Y)]=[C,[X,C]]=-[C,[C,X]]=-4Q(C)X.
```
Finally, applying $`\operatorname{ad}_X`$ to [(6)](#label-eq-double) gives $`\operatorname{ad}_X^3(Y)=4Q(X)\operatorname{ad}_X(Y)`$, since $`\operatorname{ad}_X(X)=0`$. Iteration proves [(9)](#label-eq-recurrence); no division by $`Q(X)`$ is used. $`\square`$

<!-- end proof-1 -->

<a id="proposition-1"></a>

**Proposition 3.**

<a id="label-prop-lift"></a>

For each $`k\geq0`$ and odd prime power $`q`$,

<a id="label-eq-monomial"></a>

```math
\tag{10}
 -4^{-k}\operatorname{ad}_C^{2q-3}\bigl(\operatorname{ad}_X^{2k+2}(Y)\bigr)
       =Q(C)^{q-1}Q(X)^kX
       \quad(C=[X,Y]).
```

<!-- end proposition-1 -->

<a id="proof-2"></a>

**Proof.**

Write $`\Delta=Q(C)`$. The exponent $`2q-3`$ is $`1+2(q-2)`$. By [(9)](#label-eq-recurrence), [(8)](#label-eq-transfer), and [(7)](#label-eq-orth), the left side of [(10)](#label-eq-monomial) is
```math
\begin{align*}
 -4^{-k}(4Q(X))^k\operatorname{ad}_C^{2(q-2)}(-4\Delta X)
 &=4^{q-1}\Delta^{q-1}Q(X)^kX\\
 &=\Delta^{q-1}Q(X)^kX.
\end{align*}
```
The final equality uses $`4^{q-1}=1`$ in $`F`$. All preceding identities hold when either invariant is zero. Thus no exceptional locus was removed during the computation. $`\square`$

<!-- end proof-2 -->

Summing [(10)](#label-eq-monomial) proves [(2)](#label-eq-evaluation). This also gives a useful formulation independent of image selection: for any scalar function $`f:F\to F`$, take its unique interpolation polynomial $`r`$ of degree less than $`q`$. Formula [(1)](#label-eq-word) realizes the map $`X\mapsto f(Q(X))X`$ whenever $`\Delta(X,Y)\neq0`$, and returns zero otherwise. Only the coefficients of the scalar interpolation polynomial need to be computed; no search through free-Lie words is required.

## 3. Conjugacy classes and proof of surjectivity

<a id="lemma-2"></a>

**Lemma 4.**

<a id="label-lem-companion"></a>

For each $`t\in F`$, the set $`\{X\in L\setminus\{0\}:Q(X)=t\}`$ is one $`\operatorname{GL}_2(F)`$-conjugacy class. Every nonzero $`X\in L`$ has a partner $`Y\in L`$ satisfying $`\Delta(X,Y)=1`$.

<!-- end lemma-2 -->

<a id="proof-3"></a>

**Proof.**

A nonzero trace-zero matrix is not scalar, since the characteristic is odd. It therefore has a cyclic vector $`v`$: otherwise every vector would be an eigenvector, and applying this to two independent vectors and their sum would make the matrix scalar. In the basis $`(Xv,v)`$, its matrix is

<a id="label-eq-companion"></a>

```math
\tag{11}
 X_t=\begin{pmatrix}0&1\\t&0\end{pmatrix},\qquad t=Q(X),
```

since $`X^2v=tv`$. Thus every nonzero matrix of invariant $`t`$ is conjugate to $`X_t`$. Conversely the invariant is preserved by conjugation. With
```math
Y_0=\begin{pmatrix}0&0\\1&0\end{pmatrix}
 \quad\hbox{one has}\quad
 [X_t,Y_0]=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
```
whose $`Q`$-value is one. Conjugate $`Y_0`$ back with the same basis change. $`\square`$

<!-- end proof-3 -->

<a id="proof-4"></a>

**Proof of Theorem [1](#label-thm-main).**

The evaluation identity follows from Proposition [3](#label-prop-lift). For every $`t\in F`$, the summand $`1-(t-a)^{q-1}`$ is one if $`t=a`$ and zero otherwise. Hence $`r_T`$ is the indicator of $`T`$, even in nonprime fields. The same finite-field identity shows that $`\Delta^{q-1}`$ is the indicator of $`\Delta\neq0`$. Consequently

<a id="label-eq-selection"></a>

```math
\tag{12}
 W_T(X,Y)=
 \begin{cases}
 X,&Q(X)\in T\ \hbox{and}\ \Delta(X,Y)\neq0,\\
 0,&\hbox{otherwise}.
 \end{cases}
```

Every nonzero $`X\in A_T`$ is attained by Lemma [4](#label-lem-companion), and zero is attained at $`(0,0)`$. This proves [(4)](#label-eq-image). The same lemma classifies the nonzero conjugacy classes, proving the assertion about all admissible subsets and uniqueness of $`T`$. The $`k`$th summand of [(1)](#label-eq-word) has degree at most
```math
2(2q-3)+(2k+2)+1=4q+2k-3\leq6q-5.
```
This proves the degree bound, including $`T=\varnothing`$, for which the word is zero. $`\square`$

<!-- end proof-4 -->

It follows that for a subset $`A\subseteq L`$ the following are equivalent: $`A`$ is a Lie-polynomial image; $`A`$ contains zero and is invariant under $`\operatorname{GL}_2(F)`$-conjugation; and $`A=A_T`$ for some $`T\subseteq F`$. Necessity of conjugation invariance follows by applying a conjugation to every input of a Lie polynomial. No theorem identifying all Lie algebra automorphisms is needed for this argument.

## 4. Exact fibers and distribution on classes

Let $`\chi:F^*\to\{1,-1\}`$ be the quadratic character. The classes with $`t\neq0`$ are semisimple; they are split for $`\chi(t)=1`$ and nonsplit for $`\chi(t)=-1`$. The class with $`t=0`$ consists of the nonzero nilpotents.

<a id="theorem-2"></a>

**Theorem 5.**

<a id="label-thm-fibers"></a>

Fix $`T\subseteq F`$ and a nonzero $`Z\in A_T`$, and write $`t=Q(Z)`$. Then

<a id="label-eq-fibers"></a>

```math
\tag{13}
 |W_T^{-1}(Z)|=
 \begin{cases}
 q^2(q-1),&t=0,\\
 q(q-1)^2,&t\neq0,\ \chi(t)=1,\\
 q(q^2-1),&t\neq0,\ \chi(t)=-1.
 \end{cases}
```

Every selected nonzero conjugacy class has exactly $`q^2(q^2-1)(q-1)`$ preimages. In particular,

<a id="label-eq-zero"></a>

```math
\tag{14}
 |W_T^{-1}(0)|=q^6-|T|q^2(q^2-1)(q-1).
```

<!-- end theorem-2 -->

<a id="proof-5"></a>

**Proof.**

By [(12)](#label-eq-selection), a nonzero output $`Z`$ forces the first input to be $`Z`$. Its fiber therefore consists precisely of the $`Y`$ for which $`Q([Z,Y])\neq0`$. Conjugate $`Z`$ to $`X_t`$ in [(11)](#label-eq-companion), and write
```math
Y=\begin{pmatrix}d&a\\b&-d\end{pmatrix}.
```
A direct multiplication gives

<a id="label-eq-binary"></a>

```math
\tag{15}
 Q([X_t,Y])=(b-ta)^2-4td^2.
```

For each $`a`$, the variable $`v=b-ta`$ ranges independently over $`F`$. If $`t=0`$, the zero set of [(15)](#label-eq-binary) has $`q^2`$ elements. If $`t=s^2\neq0`$, the equation is $`(v-2sd)(v+2sd)=0`$; the two distinct lines have $`2q-1`$ points altogether. With the free choice of $`a`$, this gives $`q(2q-1)`$ zeros. If $`t`$ is a nonsquare, $`v^2=4td^2`$ forces $`v=d=0`$, giving $`q`$ zeros. Subtracting from $`q^3`$ proves [(13)](#label-eq-fibers).

For completeness, the sizes of the three types of nonzero classes are

<a id="label-eq-classsizes"></a>

```math
\tag{16}
 q^2-1,\qquad q(q+1),\qquad q(q-1),
```

respectively. These can be counted without a centralizer formula. Matrices $`\left(\begin{smallmatrix}d&a\\b&-d\end{smallmatrix}\right)`$ with $`Q=t`$ satisfy $`ab=t-d^2`$. For a fixed $`d`$ there are $`q-1`$ choices of $`(a,b)`$ if $`t-d^2\neq0`$, and $`2q-1`$ if it is zero. The number of roots of $`d^2=t`$ is one, two, or zero for the three cases, respectively. For $`t=0`$ remove the zero matrix. This yields [(16)](#label-eq-classsizes). Multiplying each class size by the corresponding value in [(13)](#label-eq-fibers) gives $`q^2(q^2-1)(q-1)`$ in all three cases. Finally $`|L^2|=q^6`$, and the $`|T|`$ selected nonzero classes are disjoint, proving [(14)](#label-eq-zero). $`\square`$

<!-- end proof-5 -->

Thus, conditional on a nonzero output from uniformly distributed inputs, the selected conjugacy classes are equally likely. Within any one class, the output is uniform as well. Uniformity over the entire selected set need not hold, since the class sizes differ.

## 5. Degree and arity limitations

The construction has degree proportional to the field size. The next bound shows that this dependence cannot be replaced by a sublinear bound valid for every admissible image.

<a id="proposition-2"></a>

**Proposition 6.**

<a id="label-prop-lower"></a>

Let $`w`$ be a Lie polynomial over $`F`$, in any finite number of variables, whose image on $`L`$ is $`\{0\}`$ together with one nonzero semisimple conjugacy class. If $`D`$ is its total degree, then $`D\geq\lceil q/4\rceil`$.

<!-- end proposition-2 -->

<a id="proof-6"></a>

**Proof.**

Let the selected class have invariant $`a\neq0`$. Choose an input tuple $`(X_1,\ldots,X_m)`$ on which $`w`$ is nonzero, and introduce a scalar indeterminate $`s`$. The ordinary polynomial
```math
f(s)=Q\bigl(w(sX_1,\ldots,sX_m)\bigr)\in F[s]
```
has degree at most $`2D`$, with $`f(0)=0`$ and $`f(1)=a`$. For every $`s\in F`$, its value is either zero or $`a`$. Hence $`f(s)(f(s)-a)`$ has all $`q`$ field elements as roots. It is a nonzero polynomial: neither factor is identically zero, by the two displayed values, and $`F[s]`$ is an integral domain. Its degree is at most $`4D`$, so the root bound gives $`q\leq4D`$. $`\square`$

<!-- end proof-6 -->

Theorem [1](#label-thm-main) and Proposition [6](#label-prop-lower) establish the optimal order of growth of the worst-case degree. They do not determine the best constant or the minimum degree for an individual image. Two variables are also necessary for every proper image other than $`\{0\}`$: a free Lie algebra on one generator is one-dimensional, so its polynomial maps are $`X\mapsto cX`$, with images only $`\{0\}`$ and $`L`$.

As a basic example, over $`\mathbb F_3`$ the nilpotent selector uses $`r_{\{0\}}(t)=1-t^2`$. Since $`4=1`$ in this field, the formula becomes
```math
W_{\{0\}}(X,Y)
 =-\operatorname{ad}_{[X,Y]}^3\bigl(\operatorname{ad}_X^2(Y)\bigr)
  +\operatorname{ad}_{[X,Y]}^3\bigl(\operatorname{ad}_X^6(Y)\bigr).
```
Each of the eight nonzero nilpotents has eighteen preimages, and the zero fiber has $`3^6-8\cdot18=585`$ elements. The same formula [(1)](#label-eq-word), with the appropriate interpolation coefficients, handles every subset of classes over every odd extension field.

## 6. Verification and further questions

The proofs above use only matrix identities, finite-field interpolation, and elementary counting. The accompanying exact checker independently expands the three basic identities in generic $`2\times2`$ matrices over an integer polynomial ring. It also evaluates the actual nested brackets in [(1)](#label-eq-word), rather than using [(2)](#label-eq-evaluation) to compute them. It checks every input pair over $`\mathbb F_3`$ and $`\mathbb F_5`$, all companion first inputs and all second inputs over $`\mathbb F_7`$ and $`\mathbb F_9`$, and a reproducible sample over $`\mathbb F_{25}`$. The nonprime fields are implemented as quadratic extensions, so their elements are not incorrectly treated as residues modulo $`q`$. All forty admissible subsets over $`\mathbb F_3`$ and $`\mathbb F_5`$ have their complete images and zero fibers checked directly. These finite tests support the universal proof; they are not a replacement for it.

The formula suggests two further problems. First, determine the smallest possible degree for a prescribed semisimple class together with zero. Second, construct analogous explicit invariant selectors in higher-rank simple Lie algebras. The rank-one proof works because a double adjoint operation transfers a scalar invariant onto the first input, and the quadratic invariant classifies all nonzero conjugacy classes. Neither property is available in this form in higher rank.

## References

<a id="ref-KS"></a>

**\[1\]** H. Kishnani and A. Singh, *Images of Lie Polynomials on simple Lie algebras*, arXiv:2605.19512v1 (2026). <https://arxiv.org/abs/2605.19512>.

<a id="ref-Lubotzky"></a>

**\[2\]** A. Lubotzky, *Images of word maps in finite simple groups*, Glasgow Math. J. **56** (2014), no. 2, 465–469. <https://doi.org/10.1017/S0017089513000396>.
