#  Sharp orders of arithmetical critical groups  via canonical lattice simplices

September 2026

## Abstract

We identify the critical group of an arithmetical structure on a connected simple graph with the vertex-lattice quotient of a canonical lattice simplex. Applying the sharp multiplicity theorem of Averkov, Kasprzyk, Lehmann and Nill, we determine the largest possible critical-group order among all such structures on graphs with a fixed number of vertices. Complete graphs attain the bound. The same bound holds for stars with a fixed number of leaves, proving the largest-order conjecture of Archer, Diaz-Lopez, Glass and Louwsma. We also determine the maximizing arithmetical structures on complete graphs and stars.

## 1. Introduction and main result

Let $`G`$ be a connected simple graph on $`[n]=\{1,\ldots,n\}`$, with $`n\geq2`$, and let $`A(G)`$ be its adjacency matrix. An *arithmetical structure* on $`G`$ is a pair of positive integer vectors $`(d,r)`$ such that $`r`$ is primitive and
```math
Lr=0,\qquad L=\mathop{\mathrm{diag}}(d)-A(G).
```
Its critical group is the finite abelian group
```math
\mathcal K(G;d,r)=\mathop{\mathrm{Tor}}(\mathbb Z^n/L\mathbb Z^n).
```
The ordinary graph Laplacian is the case $`r=\mathbf 1`$. Arithmetical structures allow other diagonal entries, producing critical groups whose orders can be much larger than the numbers of spanning trees of the underlying graphs.

Write $`s_1=2`$ and $`s_{j+1}=s_1\cdots s_j+1`$ for Sylvester’s sequence, and define

<a id="label-eq-bound"></a>

```math
\tag{1}
 M_n=\begin{cases}
 n^{n-2},&2\leq n\leq4,\\
 128,&n=5,\\
 3(s_{n-2}-1)^2,&n\geq6.
 \end{cases}
```

For stars we use the convention that $`S_n`$ has $`n`$ leaves and hence $`n+1`$ vertices.

<a id="theorem-1"></a>

**Theorem 1.**

<a id="label-thm-main"></a>

For every arithmetical structure on a connected simple graph $`G`$ with $`n\geq2`$ vertices,
```math
|\mathcal K(G;d,r)|\leq M_n.
```
For each $`n`$, the bound is attained by an arithmetical structure on the complete graph $`K_n`$. Moreover, $`M_n`$ is the largest critical-group order among arithmetical structures on the star $`S_n`$.

<!-- end theorem-1 -->

Archer, Diaz-Lopez, Glass and Louwsma [\[1\]](#ref-ADGL) determine critical groups of arithmetical structures on stars and complete graphs. Their Conjecture 24 asserts the last conclusion of Theorem [1](#label-thm-main) for $`n\geq6`$, together with its complete-graph counterpart. Their notation is $`a_1=1`$ and $`a_{j+1}=a_j^2+a_j`$, so that $`a_j=s_j-1`$. Thus Theorem [1](#label-thm-main) proves that conjecture and gives a sharp bound over all connected simple graphs with a fixed number of vertices.

The geometric input is the sharp canonical-simplex multiplicity bound of Averkov, Kasprzyk, Lehmann and Nill [\[2\]](#ref-AKLN). We use their theorem, including its equality classification, as an external result; we do not give a new proof of that bound. Taking the convex hull of Laplacian columns is the earlier construction of Braun and Meyer [\[4\]](#ref-BM). Balletti, Hibi, Meyer and Tsuchiya [\[3\]](#ref-BHMT) show that ordinary Laplacian simplices of simple strongly connected digraphs have a unique interior lattice point. Our observation is that a symmetric arithmetical Laplacian gives such a simplex in the saturated lattice perpendicular to its positive kernel vector, and that its critical group is exactly the vertex-lattice quotient. This makes the multiplicity theorem applicable to the graph-order problem.

## 2. The simplex and its vertex-lattice quotient

For a rank-$`m`$ lattice $`N`$, a full-dimensional lattice simplex $`P\subset N\otimes_\mathbb Z\mathbb R`$ is called *canonical* if its unique interior lattice point is the origin. Its *multiplicity* is the index
```math
\operatorname{mult}_N(P)
 =\left[N:\sum_{v\text{ a vertex of }P}\mathbb Zv\right].
```
In particular, the ambient lattice is part of this definition.

<a id="lemma-1"></a>

**Lemma 2.**

<a id="label-lem-bridge"></a>

Let $`(d,r)`$ be an arithmetical structure on a connected simple graph with $`n\geq2`$ vertices. Let $`v_1,\ldots,v_n`$ be the columns of $`L=\mathop{\mathrm{diag}}(d)-A(G)`$ and set
```math
N=\{x\in\mathbb Z^n:r^{\mathsf T}x=0\},\qquad
 P=\mathop{\mathrm{conv}}(v_1,\ldots,v_n).
```
Then $`P`$ is a canonical $`(n-1)`$-dimensional simplex in $`N`$, and
```math
N/\sum_{i=1}^n\mathbb Zv_i\cong\mathcal K(G;d,r).
```

<!-- end lemma-1 -->

<a id="proof-1"></a>

**Proof.**

Put $`R=\mathop{\mathrm{diag}}(r)`$. The matrix $`RLR`$ is the weighted Laplacian with edge weights $`r_i r_j`$, because
```math
r_i^2d_i=\sum_{j:\{i,j\}\in E(G)}r_i r_j.
```
Consequently, for every $`z\in\mathbb R^n`$,
```math
z^{\mathsf T}RLRz
 =\sum_{\{i,j\}\in E(G)}r_i r_j(z_i-z_j)^2.
```
Connectedness implies that $`L`$ has rank $`n-1`$ and $`\ker_{\mathbb R}L=\mathbb Rr`$. Symmetry puts each $`v_i`$ in $`N`$. The only linear relation among the columns is a multiple of $`\sum_i r_i v_i=0`$. Since $`\sum_i r_i>0`$, no nonzero relation is an affine relation, so the columns are affinely independent. The positive coefficients $`r_i/\sum_jr_j`$ express $`0`$ as an interior point of their simplex.

Every coordinate of every $`v_i`$ is at least $`-1`$. For each $`j`$, column $`v_j`$ has positive $`j`$th coordinate $`d_j`$: every vertex has a neighbor, and $`d_jr_j`$ is the positive sum of the neighboring $`r`$-entries. An interior point of $`P`$ uses all vertices with strictly positive coefficients. Each of its coordinates is therefore strictly greater than $`-1`$. An interior lattice point $`x`$ has all $`x_j\geq0`$; the equation $`r^{\mathsf T}x=0`$ and positivity of $`r`$ force $`x=0`$. This proves that $`P`$ is canonical. Its vertices are primitive, since each column has an entry $`-1`$ at a neighboring vertex.

Finally, primitivity of $`r`$ gives an exact sequence
```math
0\longrightarrow N/L\mathbb Z^n
 \longrightarrow\mathbb Z^n/L\mathbb Z^n
 \xrightarrow{\;r^{\mathsf T}\;}\mathbb Z
 \longrightarrow0.
```
The left term is finite because $`\operatorname{rank}L=n-1`$. It equals the torsion subgroup of the middle term: torsion maps to zero in $`\mathbb Z`$, and every element of the finite kernel is torsion. The columns generate $`L\mathbb Z^n`$, giving the claimed isomorphism. $`\square`$

<!-- end proof-1 -->

We state the precise geometric input in lattice language.

<a id="theorem-2"></a>

**Theorem 3 (Averkov–Kasprzyk–Lehmann–Nill).**

<a id="label-thm-AKLN"></a>

Let $`P`$ be a canonical $`m`$-dimensional lattice simplex, where $`m\geq1`$. Then
```math
\operatorname{mult}(P)\leq M_{m+1}.
```
Up to a lattice isomorphism, the simplex attaining equality is unique. It is
```math
\begin{cases}
 \mathop{\mathrm{conv}}(0,(m+1)e_1,\ldots,(m+1)e_m)-\mathbf 1,&1\leq m\leq3,\\[2pt]
 \mathop{\mathrm{conv}}(0,2e_1,8e_2,8e_3,8e_4)-\mathbf 1,&m=4,\\[2pt]
 \mathop{\mathrm{conv}}(0,s_1e_1,\ldots,s_{m-2}e_{m-2},3te_{m-1},3te_m)-\mathbf 1,
 &m\geq5,
 \end{cases}
```
where $`t=s_{m-1}-1`$ in the last line and the displayed models have ambient lattice $`\mathbb Z^m`$.

<!-- end theorem-2 -->

This is Proposition 2.8 and Theorem 2.9 of [\[2\]](#ref-AKLN). Combining it with Lemma [2](#label-lem-bridge), with $`m=n-1`$, proves the upper bound in Theorem [1](#label-thm-main).

## 3. Attainment and the star bound

We record an elementary order formula. If $`L`$ is a symmetric positive semidefinite integral matrix of rank $`n-1`$ with primitive null vector $`r`$, then

<a id="label-eq-adjugate"></a>

```math
\tag{2}
 \mathop{\mathrm{adj}}(L)=c\,rr^{\mathsf T},\qquad
 c=|\mathop{\mathrm{Tor}}(\mathbb Z^n/L\mathbb Z^n)|.
```

Indeed the rank-one adjugate is a rational multiple of $`rr^{\mathsf T}`$. All its entries are integral, and $`\gcd_{i,j}(r_i r_j)=1`$, so the multiple is an integer. The gcd of the $`(n-1)`$-minors is the order of the torsion cokernel by Smith normal form. Positivity of the nonzero eigenvalues fixes the positive sign in [(2)](#label-eq-adjugate).

Let $`q_1,\ldots,q_n`$ be positive integers with

<a id="label-eq-unit"></a>

```math
\tag{3}
 \sum_{i=1}^n\frac1{q_i}=1.
```

Put $`\ell=\mathop{\mathrm{lcm}}(q_1,\ldots,q_n)`$, $`r_i=\ell/q_i`$ and $`d_i=q_i-1`$. All $`q_i\geq2`$, and $`r`$ is primitive: for each prime dividing $`\ell`$, some denominator has its full valuation. Since $`\sum_i r_i=\ell`$, these data define an arithmetical structure on $`K_n`$ with
```math
L=\mathop{\mathrm{diag}}(q_1,\ldots,q_n)-J,
```
where $`J`$ is the all-ones matrix. Deleting row and column $`j`$ and applying the determinant lemma gives the principal cofactor
```math
\prod_{i\ne j}q_i\left(1-\sum_{i\ne j}\frac1{q_i}\right)
 =\frac{\prod_i q_i}{q_j^2}.
```
By [(2)](#label-eq-adjugate),

<a id="label-eq-order"></a>

```math
\tag{4}
 |\mathcal K(K_n;d,r)|=\frac{\prod_iq_i}{\ell^2}.
```

This is also the order consequence of the group formula in [\[1\]](#ref-ADGL).

For $`2\leq n\leq4`$, take $`q_i=n`$ for every $`i`$; formula [(4)](#label-eq-order) gives $`M_n=n^{n-2}`$. For $`n=5`$, take
```math
q=(2,8,8,8,8),
```
giving order $`128`$. For $`n\geq6`$, put

<a id="label-eq-extremal"></a>

```math
\tag{5}
 t=s_{n-2}-1=\prod_{i=1}^{n-3}s_i,\qquad
 q=(s_1,\ldots,s_{n-3},3t,3t,3t).
```

The telescoping identity $`\sum_{i=1}^{n-3}1/s_i=1-1/t`$ proves [(3)](#label-eq-unit). Here $`\ell=3t`$, and [(4)](#label-eq-order) gives
```math
\frac{t(3t)^3}{(3t)^2}=3t^2=M_n.
```
These are the extremal constructions already proposed in [\[1\]](#ref-ADGL); their optimality follows from the upper bound.

Now consider an arithmetical structure on $`S_n`$. Denote its center by $`0`$, put $`q_i=d_i`$ at its leaves, and let $`d_0`$ be its central label. The arithmetical equations give $`r_i=r_0/q_i`$ and
```math
\sum_{i=1}^n\frac1{q_i}=d_0.
```
Primitivity implies $`r_0=\ell=\mathop{\mathrm{lcm}}(q_1,\ldots,q_n)`$. The principal cofactor obtained by deleting the center is $`\prod_iq_i`$, so [(2)](#label-eq-adjugate) gives

<a id="label-eq-starorder"></a>

```math
\tag{6}
 |\mathcal K(S_n;d,r)|=\frac{\prod_iq_i}{\ell^2}.
```

Replace each $`q_i`$ by $`q'_i=d_0q_i`$. The new tuple satisfies [(3)](#label-eq-unit), has least common multiple $`d_0\ell`$, and determines a complete-graph structure of order
```math
\frac{\prod_i q'_i}{(d_0\ell)^2}
 =d_0^{n-2}|\mathcal K(S_n;d,r)|.
```
The complete-graph bound therefore proves the stronger inequality

<a id="label-eq-center"></a>

```math
\tag{7}
 d_0^{n-2}|\mathcal K(S_n;d,r)|\leq M_n.
```

This scaling is the order calculation underlying [\[1, Proposition 20\]](#ref-ADGL). Conversely, each maximizing unit-fraction tuple above defines a star structure with $`d_0=1`$ and order $`M_n`$ by [(6)](#label-eq-starorder). This completes the proof of Theorem [1](#label-thm-main).

## 4. Maximizing structures on complete graphs and stars

The equality classification in the geometric theorem gives more than the numerical answer to the conjecture.

<a id="corollary-1"></a>

**Corollary 4.**

<a id="label-cor-equality"></a>

Up to permutation of vertices, the maximizing arithmetical structure on $`K_n`$ is unique for each $`n\geq2`$. It is given by $`d_i=q_i-1`$ and $`r_i=\ell/q_i`$, where $`\ell=\mathop{\mathrm{lcm}}(q_i)`$ and
```math
q=\begin{cases}
 (n,\ldots,n),&2\leq n\leq4,\\
 (2,8,8,8,8),&n=5,\\
 (s_1,\ldots,s_{n-3},3t,3t,3t),&n\geq6,
 \end{cases}
```
with $`t=s_{n-2}-1`$. For $`S_n`$ with $`n\geq3`$, the maximizing structure is likewise unique up to permutation of leaves: its central label is $`d_0=1`$, its leaf labels are the displayed $`q_i`$, and $`(r_0,r_1,\ldots,r_n)=(\ell,\ell/q_1,\ldots,\ell/q_n)`$.

<!-- end corollary-1 -->

<a id="proof-2"></a>

**Proof.**

For a complete-graph structure put $`q_i=d_i+1`$ and $`h=\sum_i r_i`$. The equations give $`q_i r_i=h`$, hence $`\sum_i1/q_i=1`$. The barycentric coordinates of $`0`$ in the simplex of Lemma [2](#label-lem-bridge) are $`r_i/h=1/q_i`$. Lattice isomorphisms preserve these coordinates up to permutation. The equality models in Theorem [3](#label-thm-AKLN) have reciprocal barycentric coordinates precisely the tuples in the statement. For the last model, the nonzero-axis vertices have coordinates $`1/s_1,\ldots,1/s_{n-3},1/(3t),1/(3t)`$, and the remaining coordinate is $`1/(3t)`$ by the telescoping identity. The low-dimensional models give the other two tuples. Thus equality determines $`q`$ up to permutation. It then determines $`d`$ and the primitive vector $`r`$ uniquely.

For a star with $`n\geq3`$, equality in [(7)](#label-eq-center) forces $`d_0=1`$. Its leaf tuple therefore determines a complete-graph structure of the same order, so the first part applies. The displayed constructions establish existence in every case. $`\square`$

<!-- end proof-2 -->

For $`S_2`$ every arithmetical critical group is trivial, and uniqueness is not asserted. Nor do we classify all graphs attaining the universal bound in Theorem [1](#label-thm-main). The numerical bound and its attainment need no such classification.

## References

<a id="ref-ADGL"></a>

**\[1\]** K. Archer, A. Diaz-Lopez, D. Glass, and J. Louwsma, *Critical groups of arithmetical structures on star graphs and complete graphs*, Electron. J. Combin. **31** (2024), no. 1, Paper P1.5. [doi:10.37236/11729](https://doi.org/10.37236/11729).

<a id="ref-AKLN"></a>

**\[2\]** G. Averkov, A. Kasprzyk, M. Lehmann, and B. Nill, *Sharp bounds on fake weighted projective spaces with canonical singularities*, in *Varieties, Polyhedra, Computation*, EMS Series of Congress Reports, EMS Press, 2025, pp. 319–334. [doi:10.4171/ecr/22/10](https://doi.org/10.4171/ecr/22/10). Preprint: [arXiv:2105.09635](https://arxiv.org/abs/2105.09635).

<a id="ref-BHMT"></a>

**\[3\]** G. Balletti, T. Hibi, M. Meyer, and A. Tsuchiya, *Laplacian simplices associated to digraphs*, Ark. Mat. **56** (2018), 243–264. [doi:10.4310/ARKIV.2018.v56.n2.a3](https://doi.org/10.4310/ARKIV.2018.v56.n2.a3).

<a id="ref-BM"></a>

**\[4\]** B. Braun and M. Meyer, *Laplacian simplices*, Adv. Appl. Math. **114** (2020), 101976. [doi:10.1016/j.aam.2019.101976](https://doi.org/10.1016/j.aam.2019.101976).
