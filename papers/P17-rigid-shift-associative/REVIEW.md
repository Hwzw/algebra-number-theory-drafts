# Internal proof audit

**Originating-agent review, September 9, 2026. No human or separate-agent review.**

## Core algebra

- The table has exactly six nonzero products, each with coefficient 1. Its degree sequence is `(1,1,2,2,3)`.
- Both sides of the shift identity are nonzero on exactly the basis triples `(x,y,y)` and `(y,x,x)`, with value `z`. Trilinearity covers arbitrary inputs.
- `(xx)y=0` and `x(xy)=z` prove nonassociativity. The grading proves vanishing of every fourfold product for every bracketing.
- The derivation formula follows from `xx=yy=0`, `u=xy`, `v=yx`, and the two expressions `z=xu=yv`. Its converse was checked on all 25 products, including zero products. It has exactly five free parameters.

## Full tangent certificate

The linearized identity uses all 125 bilinear coordinates and all 625 scalar equations. There is no restriction to graded or nilpotent deformations. Signs and argument order agree with `(ab)c=b(ca)`.

`check.py` constructs the integer Jacobian and orbit differential, verifies their product is zero exactly, and supplies minors of determinant 2 and 3, of orders 105 and 20. Their rank lower bounds sum to 125, so the chain identity forces equality of both ranks. Modular pivots select minors only; Bareiss arithmetic evaluates the determinants over the integers. The manuscript explicitly lists the Jacobian minor and its indexing convention.

`independent_check.py` imports no primary implementation. It independently expands nested symbolic dual-number products and the basis-change action with SymPy 1.14.0, recomputes exact ranks, checks both stored minors, and verifies the derivation formula. Both implementations agree. Shared input consists of the algebra table and stored certificate indices, not the matrix-building code. This guards against implementation errors but is not an external mathematical review.

## Geometry

The tangent space of the reduced variety lies inside the kernel of the displayed identity Jacobian; the orbit tangent lies inside the reduced tangent. Equality of outer dimensions thus forces all three spaces to agree. The orbit supplies a lower bound for local dimension. Equality with tangent dimension gives a smooth point on a unique irreducible component. The orbit is locally closed and full-dimensional there, and no other component meets the orbit. Hence the orbit is open in the entire variety. Characteristic zero ensures separability of the orbit map.

Every fourfold-product identity is polynomial and therefore persists on the orbit closure. An orbit whose closure contained the rigid point would intersect its open orbit, forcing equality. Thus the nonnilpotent degeneration claim has the correct direction.

## Higher dimensions

For an idempotent, the shift identity gives `LR=L`, `RL=R`, and `L²=R²`. These imply `L=R=E` and `E²=E`. The manuscript checks image closure, kernel closure, and both cross products, so it establishes a direct product over any commutative base ring.

Over the dual numbers, the idempotent defect belongs to the square-zero ideal. The correction operator `2E-I` is invertible, with square the identity. Splitting the lifted projection yields free summands of the original ranks over the local base ring. Lifting scalar idempotents successively in the complementary factor prevents interference among factors. Basis choices reduce to the original basis, so this proves triviality as an infinitesimal deformation, not merely an abstract isomorphism of special fibers. The remaining deformation is precisely a deformation of A and is killed by the computed tangent equality.

Derivations annihilate scalar idempotents and preserve all factors, leaving the same five-dimensional derivation algebra. This proves the claimed orbit dimension for every r.

## Remaining limits

The proof uses one finite exact matrix computation with fully specified data; it is not a purely conceptual classification proof. No unresolved numerical search is used as a universal argument. Historical priority and significance remain provisional under the source assessment. The paper does not claim a full classification or that the higher-dimensional examples are nilpotent when scalar factors are present.

Artifact verification is recorded separately in `artifact-qa.json`; the Markdown conversion and mathematical syntax checks have their own machine-readable records.
