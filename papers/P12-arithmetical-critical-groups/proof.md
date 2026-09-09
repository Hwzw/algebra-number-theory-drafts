# Sharp orders of arithmetical critical groups via canonical simplices

Status: complete proof using an explicitly cited sharp geometric theorem; independent proof review, bounded source audit, and final manuscript transfer passed. This file does not claim a new proof of the geometric theorem.

Let s_1=2 and s_{j+1}=s_1...s_j+1 be Sylvester's sequence. Set

M_n = n^(n-2) for 2<=n<=4, M_5=128, and M_n=3(s_{n-2}-1)^2 for n>=6.

## Theorem A

For every connected simple graph G on n>=2 vertices and every arithmetical structure (d,r) on G, the associated critical group satisfies |K(G;d,r)|<=M_n. For each n the bound is attained on the complete graph K_n.

Here r is a primitive positive integer vector and L=diag(d)-A(G) satisfies Lr=0; K is the torsion subgroup of Z^n/LZ^n.

## Lemma 1: the lattice and simplex

Set N={x in Z^n:r dot x=0}, and let v_i be column i of L (equivalently row i, since L is symmetric). Then P=conv(v_1,...,v_n) is an (n-1)-dimensional lattice simplex in N_R, its only interior lattice point is 0, and

N/(Zv_1+...+Zv_n) is isomorphic to K(G;d,r).

Proof. Let R=diag(r). The matrix RLR is the weighted graph Laplacian with edge weights r_i r_j: its diagonal entry at i is r_i^2 d_i = sum_{j adjacent i}r_i r_j. Thus for real z,

z^T RLR z = sum_{ij in E(G)}r_i r_j(z_i-z_j)^2.

Connectedness gives rank L=n-1 and the real kernel of L is the real span of r. Symmetry gives r dot v_i=0. The unique linear relation among v_i is proportional to sum_i r_i v_i=0. Because sum_i r_i is nonzero, there is no nonzero affine relation, proving affine independence. The normalized positive coefficients r_i/sum_j r_j put 0 in the relative interior of P.

Each coordinate of every v_i is at least -1 because G is simple. For each coordinate j, v_j has coordinate d_j>0: each vertex has a neighbor and the arithmetical equation forces d_j>0. An interior point of the simplex is a convex combination with every coefficient strictly positive, so each coordinate is strictly greater than -1. If x is an interior lattice point, every x_j is an integer >=0. Since all r_j>0 and r dot x=0, x=0. Each v_i is primitive in N because it has coordinate -1 at a neighbor.

The homomorphism Z^n -> Z, x -> r dot x, is surjective since r is primitive, with kernel N. The image LZ^n is contained in N and has finite index there. Thus

0 -> N/LZ^n -> Z^n/LZ^n -> Z -> 0

is exact. Its finite left term equals the torsion subgroup of its middle term: every torsion element maps to zero in Z, and every element of the finite kernel is torsion. This proves the asserted group isomorphism. QED.

## Geometric input

Averkov, Kasprzyk, Lehmann and Nill, *Sharp bounds on fake weighted projective spaces with canonical singularities*, arXiv:2105.09635, Proposition 2.8 and Theorem 2.9, prove the following. If P is a d-dimensional lattice simplex whose unique interior lattice point is 0, its multiplicity [N:sum_{v vertex of P}Zv] is at most

(d+1)^(d-1) for 1<=d<=3; 128 for d=4; and 3(s_{d-1}-1)^2 for d>=5.

Their theorem additionally classifies equality, although Theorem A only needs the bound. Their main result is not reproved here.

Applying this input to Lemma 1 with d=n-1 proves the upper bound in Theorem A.

## Attainment on complete graphs

For any positive integers q_1,...,q_n with sum_i 1/q_i=1, put ell=lcm(q_1,...,q_n), r_i=ell/q_i, d_i=q_i-1. Then r is primitive (for every prime dividing ell, some q_i has the full valuation of ell), sum_i r_i=ell, and

L=diag(q_i)-J, Lr=0.

Its critical-group order is prod_i q_i / ell^2. For completeness, delete row and column j and apply the determinant lemma to diag(q_i:i!=j)-J. The cofactor is

prod_{i!=j}q_i (1-sum_{i!=j}1/q_i) = prod_i q_i / q_j^2.

For a symmetric integer rank n-1 matrix with primitive null vector r, the adjugate is c rr^T. The order of its torsion cokernel is the gcd of all (n-1)-minors, namely c because gcd_{i,j}(r_i r_j)=1. Comparing the displayed cofactor with r_j^2=ell^2/q_j^2 gives the formula.

For 2<=n<=4 choose q_i=n for every i, obtaining n^(n-2).

For n=5 choose q=(2,8,8,8,8), obtaining 128.

For n>=6 put t=s_{n-2}-1=prod_{i=1}^{n-3}s_i and choose

q=(s_1,...,s_{n-3},3t,3t,3t).

The telescoping identity sum_{i=1}^{n-3}1/s_i=1-1/t proves the unit-fraction equation. Since each s_i divides t, ell=3t. The product is t(3t)^3, giving order 3t^2. This completes Theorem A. QED.

## Theorem B: the star conjecture

For n>=2, the maximum order of an arithmetical critical group on the star S_n with n leaves is M_n. Consequently Conjecture 24 of Archer, Diaz-Lopez, Glass and Louwsma is true.

Proof. Let d_0 be the central label and q_i=d_i the leaf labels. The leaf equations and primitive normalization give ell=lcm(q_i), r_0=ell and r_i=ell/q_i, while the central equation says sum_i1/q_i=d_0. Archer et al., Theorem 1, gives

|K(S_n;d,r)|=prod_i q_i/ell^2.

Replace q_i by q_i'=d_0 q_i. These satisfy sum_i1/q_i'=1, and their least common multiple is d_0 ell. Therefore the complete-graph construction above gives a critical group of order

prod_i q_i'/(d_0 ell)^2=d_0^(n-2)|K(S_n;d,r)|.

Theorem A bounds this by M_n and d_0>=1. Conversely each unit-fraction construction attaining M_n defines an arithmetical structure on S_n with d_0=1 and the same order. QED.

This also proves the sharper statement d_0^(n-2)|K(S_n;d,r)|<=M_n, consistent with the order increase in Archer et al., Proposition 20.

## Equality on stars and complete graphs

For K_n, the barycentric coordinates of 0 in P are exactly r_i/sum_j r_j=1/q_i. The equality classification in the AKLN theorem fixes these coordinates up to permutation: q=(n,...,n) for 2<=n<=4; q=(2,8,8,8,8) for n=5; and the Sylvester triple-tail tuple above for n>=6. Thus these are the unique maximizing arithmetical structures on K_n up to vertex permutation.

For S_n with n>=3, equality implies d_0=1 because M_n>0 and d_0^(n-2)|K|<=M_n. The clique-star correspondence and complete-graph equality classification then give the same unique maximizing leaf tuple, up to leaf permutation. For n=2, every arithmetical structure has trivial critical group, so uniqueness is false and is not claimed.

No uniqueness assertion is made among all connected simple graphs with n vertices.
