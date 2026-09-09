# A rigid nonassociative shift-associative algebra in dimension five

Henry Zweiman

September 9, 2026

## Abstract

We construct a five-dimensional complex nilpotent algebra satisfying $`(ab)c=b(ca)`$ whose orbit is open in the variety of all five-dimensional algebras satisfying this identity. It is nonassociative and has a five-dimensional derivation algebra. Its space of infinitesimal deformations has dimension twenty and consists entirely of infinitesimal changes of basis. An explicit integer minor of determinant two certifies the tangent calculation. This answers the rigid nonassociative existence question of Abdelwahab, Kaygorodov, and Sartayev in the smallest possible dimension. The orbit closure is a twenty-dimensional irreducible component consisting of nilpotent algebras. An idempotent-splitting argument further gives rigid nonassociative examples in every dimension at least five.

## 1. Introduction and the main result

An algebra is *shift-associative* if its bilinear product satisfies

<a id="label-eq-shift"></a>

```math
\tag{1}
 (ab)c=b(ca).
```

The same identity has also been studied under the name nearly associative; see [\[2\]](#ref-BBR). Throughout this paper algebras are finite-dimensional over $`\mathbb C`$ and need not have a unit. Let $`\mathcal S_n`$ denote the affine variety of shift-associative products on $`\mathbb C^n`$. The group $`\operatorname{GL}_n(\mathbb C)`$ acts by
```math
(g\cdot\mu)(a,b)=g\mu(g^{-1}a,g^{-1}b).
```
We call a product *rigid* when its orbit is Zariski open in $`\mathcal S_n`$.

Abdelwahab, Kaygorodov, and Sartayev [\[1\]](#ref-AKS) classify the complex algebras of dimension four and prove that five is the smallest dimension in which nonassociativity occurs. Their Proposition 59 supplies a five-dimensional nonassociative example. After Proposition 64 they ask whether a rigid nonassociative shift-associative algebra exists. We answer that question by the following six-product table. The new point is rigidity, rather than the existence of nonassociativity in dimension five.

<a id="theorem-1"></a>

**Theorem 1.**

<a id="label-thm-main"></a>

Let $`A`$ have ordered basis $`(x,y,u,v,z)`$ and nonzero products

<a id="label-eq-table"></a>

```math
\tag{2}
 xy=u,\qquad yx=v,\qquad xu=z,\qquad yv=z,\qquad uy=z,\qquad vx=z.
```

All products omitted from this table are zero. Then $`A`$ is shift-associative, nonassociative, and nilpotent. It is rigid in $`\mathcal S_5`$. Its orbit and its space of infinitesimal deformations both have dimension $`20`$, and $`\dim\operatorname{Der}(A)=5`$.

The orbit closure of $`A`$ is a $`20`$-dimensional irreducible component of $`\mathcal S_5`$, all of whose algebras have every fourfold product equal to zero. Five is the minimum dimension of a rigid nonassociative shift-associative algebra.

<!-- end theorem-1 -->

The infinitesimal calculation allows all $`125`$ structure constants to vary. In particular, the rigidity assertion is in the entire variety $`\mathcal S_5`$, not only a subvariety with a fixed grading, annihilator, or nilpotency bound. We give a fully specified exact minor in the appendix, together with reproducible arithmetic. A second symbolic implementation independently verifies the linearization and its rank.

<a id="theorem-2"></a>

**Theorem 2.**

<a id="label-thm-extension"></a>

For every $`r\ge0`$, the direct-product algebra $`A\oplus\mathbb C^r`$ is a rigid nonassociative point of $`\mathcal S_{5+r}`$. Its orbit has dimension $`(5+r)^2-5`$, and every infinitesimal deformation is induced by a change of basis.

<!-- end theorem-2 -->

The higher-dimensional statement follows from splitting lifted scalar idempotents over the dual numbers. It does not require a separate classification or a new rank computation in each dimension.

## 2. The algebra and its derivations

The grading with degrees $`1,1,2,2,3`$ on $`(x,y,u,v,z)`$ is compatible with every product in [(2)](#label-eq-table). Consequently every product of four elements, with any bracketing, vanishes. The only basis triples $`(a,b,c)`$ for which $`(ab)c`$ is nonzero are $`(x,y,y)`$ and $`(y,x,x)`$, and the value is $`z`$ in both cases. The same statement holds for $`b(ca)`$, proving [(1)](#label-eq-shift) by trilinearity. On the other hand,
```math
(xx)y=0,\qquad x(xy)=z,
```
so $`A`$ is nonassociative. Its square is $`\langle u,v,z\rangle`$, the span of all triple products is $`\langle z\rangle`$, and its two-sided annihilator is $`\langle z\rangle`$.

<a id="lemma-1"></a>

**Lemma 3.**

<a id="label-lem-der"></a>

Relative to the ordered basis $`(x,y,u,v,z)`$, the derivations of $`A`$ are precisely the matrices

<a id="label-eq-der"></a>

```math
\tag{3}
 \begin{pmatrix}
 a&0&0&0&0\\
 0&a&0&0&0\\
 c&h&2a&0&0\\
 -c&-h&0&2a&0\\
 e&j&c+h&-c-h&3a
 \end{pmatrix},\qquad a,c,e,h,j\in\mathbb C.
```

Matrix columns are images of basis vectors.

<!-- end lemma-1 -->

<a id="proof-1"></a>

**Proof.**

Write $`D(x)=a x+b y+c u+d v+e z`$ and $`D(y)=f x+g y+h u+i v+j z`$. Applying $`D`$ to $`xx=yy=0`$ gives $`b=f=0`$, $`d=-c`$, and $`i=-h`$. Applying $`D`$ to $`u=xy`$ and $`v=yx`$ then gives
```math
D(u)=(a+g)u+(c+h)z,\qquad
 D(v)=(a+g)v-(c+h)z.
```
Finally, $`z=xu=yv`$ gives $`D(z)=(2a+g)z=(a+2g)z`$, hence $`g=a`$. These necessary conditions yield [(3)](#label-eq-der). Conversely, substitution in all products in [(2)](#label-eq-table) and all zero products verifies the derivation rule for every matrix in [(3)](#label-eq-der). $`\square`$

<!-- end proof-1 -->

## 3. Infinitesimal deformations and rigidity

For a fixed product $`\mu`$, write $`Z_\mu`$ for the space of bilinear maps $`\theta`$ for which $`\mu+\varepsilon\theta`$ satisfies [(1)](#label-eq-shift) over $`\mathbb C[\varepsilon]/(\varepsilon^2)`$. Expanding the identity gives

<a id="label-eq-J"></a>

```math
\tag{4}
\begin{split}
 (J_\mu\theta)(a,b,c)={}&\theta(\mu(a,b),c)+\mu(\theta(a,b),c)\\
 &-\theta(b,\mu(c,a))-\mu(b,\theta(c,a)).
\end{split}
```

Thus $`Z_\mu=\ker J_\mu`$. Define $`B_\mu`$ as the image of

<a id="label-eq-delta"></a>

```math
\tag{5}
 (\delta_\mu g)(a,b)=g\mu(a,b)-\mu(ga,b)-\mu(a,gb),
 \qquad g\in\operatorname{End}(\mathbb C^n).
```

It is the tangent space to the orbit; in characteristic zero the orbit map is separable. Differentiating the change-of-basis action also gives $`J_\mu\delta_\mu=0`$, so $`B_\mu\subseteq Z_\mu`$. The kernel of $`\delta_\mu`$ is $`\operatorname{Der}(\mu)`$.

<a id="lemma-2"></a>

**Lemma 4.**

<a id="label-lem-criterion"></a>

If $`Z_\mu=B_\mu`$, then $`\mu`$ is rigid, and its orbit closure is an irreducible component of $`\mathcal S_n`$.

<!-- end lemma-2 -->

<a id="proof-2"></a>

**Proof.**

Let $`d=\dim B_\mu`$, the orbit dimension. The Zariski tangent space of the reduced variety $`\mathcal S_n`$ is contained in $`Z_\mu`$, since its defining ideal contains the shift equations. On the other hand, the orbit tangent space is contained in that Zariski tangent space. The hypothesis therefore makes both tangent spaces $`d`$-dimensional. The local dimension at $`\mu`$ is at least $`d`$ because of the orbit and is at most the tangent dimension. Equality implies that $`\mu`$ is a smooth point, on a unique irreducible component of dimension $`d`$.

The orbit is locally closed, irreducible, and $`d`$-dimensional, so its closure is that component and the orbit is open in it. The same uniqueness of a component holds at every point of the orbit, by the group action. Removing the other components and the boundary of the orbit in its component therefore exhibits the orbit as open in $`\mathcal S_n`$. $`\square`$

<!-- end proof-2 -->

<a id="proposition-1"></a>

**Proposition 5.**

<a id="label-prop-rank"></a>

For the table [(2)](#label-eq-table), $`\operatorname{rank}J_\mu=105`$ and $`Z_\mu=B_\mu`$ has dimension $`20`$.

<!-- end proposition-1 -->

<a id="proof-3"></a>

**Proof.**

There are $`125`$ bilinear coordinates and $`625`$ scalar linearized shift equations. Lemma [3](#label-lem-der) gives $`\dim B_\mu=25-5=20`$, so $`\dim Z_\mu\ge20`$ and $`\operatorname{rank}J_\mu\le105`$. The appendix specifies a $`105\times105`$ submatrix of $`J_\mu`$ with integer determinant $`2`$. This proves the opposite rank inequality over $`\mathbb C`$, hence $`\dim Z_\mu=20`$. The inclusion $`B_\mu\subseteq Z_\mu`$ is consequently equality. $`\square`$

<!-- end proof-3 -->

<a id="proof-4"></a>

**Proof of Theorem [1](#label-thm-main).**

Section 2 establishes the algebraic assertions. Proposition [5](#label-prop-rank) and Lemma [4](#label-lem-criterion) prove rigidity and the component assertion. The vanishing of every fourfold product is a set of polynomial identities, so it persists on the orbit closure. Finally, [\[1, Corollary 58 and Proposition 59\]](#ref-AKS) show that every complex shift-associative algebra of dimension at most four is associative. This proves minimality. $`\square`$

<!-- end proof-4 -->

<a id="corollary-1"></a>

**Corollary 6.**

<a id="label-cor-nil"></a>

The variety $`\mathcal S_5`$ contains a nilpotent rigid algebra and has an irreducible component containing no nonnilpotent algebra. No nonnilpotent five-dimensional shift-associative algebra degenerates to $`A`$.

<!-- end corollary-1 -->

<a id="proof-5"></a>

**Proof.**

Only the last statement remains. If $`A`$ belonged to the closure of another orbit, its open orbit would meet that other orbit. Distinct orbits are disjoint, so the two orbits would coincide, contrary to nonnilpotency. $`\square`$

<!-- end proof-5 -->

In the terminology of [\[1\]](#ref-AKS), $`\mathcal S_5`$ thus fails the Vergne property, the Grunewald–O’Halloran property, and the Vergne–Grunewald–O’Halloran property. These assertions concern shift-associative algebras; they make no claim about the corresponding Lie-algebra conjectures.

## 4. Adjoining scalar factors

We give the splitting argument over a commutative ring so that it also applies to infinitesimal deformations.

<a id="lemma-3"></a>

**Lemma 7.**

<a id="label-lem-idem"></a>

Let $`M`$ be a shift-associative algebra over a commutative ring and let $`e^2=e`$. Left and right multiplication by $`e`$ coincide with an idempotent operator $`E`$. There is a direct-product decomposition
```math
M=EM\oplus\ker E,
```
and $`EM`$ is a commutative associative algebra with identity $`e`$.

<!-- end lemma-3 -->

<a id="proof-6"></a>

**Proof.**

Put $`L(a)=ea`$ and $`R(a)=ae`$. Substitution of two copies of $`e`$ into the shift identity gives
```math
LR=L,\qquad RL=R,\qquad R^2=L^2.
```
The first two relations imply $`L^2=L`$ and $`R^2=R`$, so $`L=R=E`$ and $`E^2=E`$. For $`a\in EM`$ and $`b\in\ker E`$, the shift identity gives
```math
ab=(ea)b=a(be)=0,\qquad ba=(eb)a=b(ae)=0.
```
If $`a,b\in\ker E`$, then $`E(ab)=(be)a=0`$, so $`\ker E`$ is closed. For $`a,b\in EM`$, the same formula gives $`E(ab)=ba`$ and $`E(ba)=ab`$. Applying $`E^2=E`$ shows $`ab=ba=E(ab)`$, so $`EM`$ is closed and commutative. It has identity $`e`$; commutativity and the shift identity give associativity. This proves all assertions. $`\square`$

<!-- end proof-6 -->

<a id="lemma-4"></a>

**Lemma 8.**

<a id="label-lem-lift"></a>

Let $`B`$ be a complex shift-associative algebra and let $`\widetilde B`$ be a deformation over $`R=\mathbb C[\varepsilon]/(\varepsilon^2)`$, free as an $`R`$-module with reduction $`B`$. Every idempotent of $`B`$ lifts to an idempotent of $`\widetilde B`$. If the corresponding factor of $`B`$ is one-dimensional, its lift splits off an $`R`$-algebra factor isomorphic to $`R`$.

<!-- end lemma-4 -->

<a id="proof-7"></a>

**Proof.**

Choose any lift $`\widehat e`$ of the idempotent and put $`w=\widehat e*\widehat e-\widehat e\in\varepsilon\widetilde B`$. On $`\varepsilon\widetilde B`$, multiplication by $`\widehat e`$ is multiplication by the original $`e`$, whose left and right operators equal the idempotent $`E`$ of Lemma [7](#label-lem-idem). For $`s\in\varepsilon\widetilde B`$,
```math
(\widehat e+s)*(\widehat e+s)-(\widehat e+s)=w+(2E-I)s.
```
Since $`(2E-I)^2=I`$, choose $`s=-(2E-I)w`$. The resulting lift is idempotent, so Lemma [7](#label-lem-idem) splits the deformed algebra. Its image and kernel are direct summands of a finite free module over the local ring $`R`$, hence free with their original ranks. If the image has rank one, the lifted idempotent is a basis for it by reduction modulo $`\varepsilon`$, and the factor is $`R`$ with its usual multiplication. $`\square`$

<!-- end proof-7 -->

<a id="proof-8"></a>

**Proof of Theorem [2](#label-thm-extension).**

Take any infinitesimal deformation of $`B=A\oplus\mathbb C^r`$. Lift the idempotent of the first scalar factor and split it by Lemma [8](#label-lem-lift). In the complementary factor repeat with the remaining scalar idempotents. Induction decomposes the deformation as $`r`$ copies of $`R`$ and an infinitesimal deformation of $`A`$. Choosing bases in these free summands that reduce to the original bases gives an isomorphism reducing to the identity on $`B`$.

Proposition [5](#label-prop-rank) says that every infinitesimal deformation of $`A`$ is trivial by such a basis change. Hence every infinitesimal deformation of $`B`$ is trivial, so $`Z_B=B_B`$. Lemma [4](#label-lem-criterion) proves rigidity. The original nonassociativity witness remains in its $`A`$-factor.

For the dimension, a derivation annihilates every scalar idempotent $`e`$: the derivation rule gives $`D(e)=2E D(e)`$, and $`I-2E`$ is invertible. From $`eb=0`$ for $`b`$ in the complementary factor it follows that $`E D(b)=0`$. Thus derivations preserve the factors, vanish on the scalar factors, and restrict arbitrarily to $`\operatorname{Der}(A)`$. Therefore $`\dim\operatorname{Der}(B)=5`$ and the orbit dimension is $`(5+r)^2-5`$. $`\square`$

<!-- end proof-8 -->

## 5. Further questions

The component supplied here does not classify $`\mathcal S_5`$. Determining its orbit boundary, identifying the other components, and deciding which contain nonassociative rigid points remain natural next problems. The scalar-factor construction gives examples in every higher dimension, but it does not give nilpotent rigid examples in every such dimension. The existence and minimum dimensions of further indecomposable nilpotent rigid shift-associative algebras are separate questions.

## 6. An exact tangent-rank certificate

<a id="label-app-cert"></a>

For this appendix only, number $`(x,y,u,v,z)`$ by $`0,1,2,3,4`$. Write $`c_{ij}^k`$ for the constants in [(2)](#label-eq-table). Flatten a bilinear coordinate $`\theta_{ij}^k`$ to column $`25i+5j+k`$ and a scalar equation indexed by $`(a,b,d,k)`$ to row $`125a+25b+5d+k`$. All indices range from $`0`$ to $`4`$. The row is the coefficient vector of

<a id="label-eq-row"></a>

```math
\tag{6}
 \sum_{s=0}^4\left(c_{ab}^s\theta_{sd}^k+\theta_{ab}^s c_{sd}^k
 -c_{da}^s\theta_{bs}^k-\theta_{da}^s c_{bs}^k\right).
```

Select all columns in increasing order except the following twenty:

    4,9,28,29,33,34,39,44,54,59,
    69,79,82,84,89,94,104,109,114,119.

Select the following $`105`$ rows, in exactly the displayed order:

    7,2,4,9,32,28,34,29,57,53,59,54,129,5,6,14,8,154,15,16,
    109,18,19,33,84,134,157,132,159,150,151,152,153,30,31,39,
    127,40,41,42,43,44,38,64,79,128,163,137,139,164,35,36,37,
    89,204,55,56,125,58,65,66,67,68,69,94,126,279,144,130,131,
    133,135,136,189,138,80,81,82,83,90,91,92,93,12,50,22,24,17,
    160,147,149,174,210,61,62,63,105,106,107,108,115,116,117,
    118,119.

The resulting integer matrix has determinant $`2`$. This value can be reproduced from [(6)](#label-eq-row) by fraction-free elimination: starting with previous pivot $`q=1`$, swap a nonzero pivot into position $`(k,k)`$ when needed, and replace each entry southeast of that pivot by
```math
M_{ij}\longleftarrow\frac{M_{kk}M_{ij}-M_{ik}M_{kj}}q\quad(i,j>k).
```
Then zero the entries below the pivot and set $`q`$ to that pivot. Track the sign of row swaps; the signed final entry is the determinant. Every division in this computation is exact.

The supplementary file `check.py` constructs [(6)](#label-eq-row), verifies the shift identity, and evaluates this certificate using integer arithmetic and the stated elimination. Modular arithmetic is used only to select the minor, not to infer a characteristic-zero rank from an upper bound. The stored file `check-results.json` fixes all selected indices. The script also verifies $`J_\mu\delta_\mu=0`$ entry by entry and gives a $`20\times20`$ orbit-differential minor of determinant $`3`$. Together the two nonzero minors and the chain identity independently force ranks $`105`$ and $`20`$.

The second implementation, `independent_check.py`, instead constructs the nested products with symbolic dual-number coefficients and expands the change-of-basis action. SymPy 1.14.0 gives exact ranks $`105`$ and $`20`$, re-evaluates the two determinants as $`2`$ and $`3`$, and verifies the five-parameter derivation formula. It does not import the first implementation. Both scripts and their result records are supplied with the manuscript at [`github.com/Hwzw/algebra-number-theory-drafts`, paper P17](https://github.com/Hwzw/algebra-number-theory-drafts/tree/main/papers/P17-rigid-shift-associative). The finite matrix certificate is the computational part of the proof. The geometric criterion and the extension to all higher dimensions are proved in the text.

## Preparation and verification

This manuscript was prepared with OpenAI Codex assistance in problem selection, proof development, computation, literature checking, and writing. The originating agent performed the internal proof audit and both computational implementations; no separate-agent or human referee review is claimed. The accompanying source assessment records the literature-search scope. Historical priority remains subject to further scholarly review.

## References

<a id="ref-AKS"></a>

**\[1\]** H. Abdelwahab, I. Kaygorodov, and B. Sartayev, *Shift associative algebras*, Rendiconti del Circolo Matematico di Palermo Series 2 **74** (2025), article 145. [doi:10.1007/s12215-025-01261-1](https://doi.org/10.1007/s12215-025-01261-1).

<a id="ref-BBR"></a>

**\[2\]** E. Barreiro, S. Benayadi, and C. Rizzo, *Nearly associative algebras*, Journal of Algebra **658** (2024), 821–868. [doi:10.1016/j.jalgebra.2024.06.016](https://doi.org/10.1016/j.jalgebra.2024.06.016).
