# Internal proof and artifact review

Date: September 9, 2026. Review by the originating AI agent. No separate-agent or human referee review occurred.

## Hypotheses and component accounting

The quadratic hypothesis concerns the geometric common zero set, not only rational points. Pure dimension excludes a plane in the common zero set. The finite base field is perfect, so reduction remains reduced after algebraic extension. The rational span of an Fq-defined component descends by its Frobenius-invariant linear equations. Degrees of reduced components add. An Fq-defined degree-one irreducible component is a rational line; therefore nonlinear degree one cannot occur.

For a planar Fq-irreducible component of degree greater than two, each restricted quadric vanishes identically on its plane. This contradicts pure dimension. For an absolute conic, at least one restriction is its nonzero equation; no line component can lie in that plane. This also excludes Homma's exceptional quartic.

## Small degrees and the quartic dependency repair

A nonabsolute Fq-irreducible component is one Frobenius orbit of equal-degree geometric components. Every rational point belongs to every conjugate component. Degree two and three give at most one common point in the nonabsolute case. In degree four there are four lines or two conics; their common rational points number at most one or four. Two distinct-plane conics meet inside the intersection of their planes, and same-plane conics satisfy Bezout.

The rational-normal classification is proved using the degree bound on global sections and a degree-one pencil on the normalization. It does not assume smoothness in advance.

Beelen–Montanucci v1, p. 10, contains an algebraic slip in the final display of Lemma 3.10: (d-3)(q+1)+2 is not generally equal to (d-2)q-q+1. This does not refute the theorem. P35 avoids reliance on that general proof by including a complete quartic argument:

1. Projection from a rational point has image degree e >= 2 and generic degree delta satisfying delta e <= 4-multiplicity. Thus delta=1.
2. From a singular point, the image is a smooth conic, isomorphic to the normalization. Every other rational point lifts uniquely, giving q+2.
3. From a smooth point, the projection extends to a finite birational morphism onto a conic or cubic. The finite-length cokernel of structure sheaves gives arithmetic genus at most one.
4. In geometric genus one the plane image is smooth and the morphism is an isomorphism, so the established plane-cubic bound applies. In genus zero the normalization has q+1 points and the total delta invariant is at most one, giving q+2.

Thus the only nonclassical point-counting dependency is Homma's precisely stated result.

## Exhaustive proof cases

- Nonlinear degree b=0: geometric connectedness gives a connected rational-line graph; every added tree edge identifies a rational point.
- b>=5: the line-free bound gives (D-1)q+1+ell, and ell=D-b<=q.
- b=2 nonabsolute: (D-2)(q+1)+1<=Dq+1 follows from D-2<=2q.
- b=2 absolute: each connected line block must meet the conic. A root line intersects the rational conic plane in exactly one rational point. A spanning-tree order then contributes at most q new points per line.
- b=3,4: the bound is (D-2)(q+1)<=Dq+1 because D<=q+5<=2q+3.

The conic case uses the geometry of the attachment; geometric connectedness alone does not ensure rational intersection points for arbitrary nonlinear components.

## Complete intersections and sharpness

A regular sequence of three quadrics in five homogeneous variables gives a pure Cohen–Macaulay projective curve of scheme degree eight. Reduction can lower degree but does not alter rational points. The Koszul resolution and the vanishing of intermediate cohomology of line bundles on P4 give H1(I_X)=0 over the algebraic closure, hence H0(O_X) is the ground field. This proves geometric connectedness even when X is nonreduced.

The equations x_i(x_i-x_0)=0 for i=1,2,3 form a regular sequence because each is monic in a new variable. The affine chart contributes 8q points and the hyperplane at infinity contributes one. The known construction is credited separately from the proposed upper bound.

## Diagnostics and limits

The attached script checks field arithmetic for q=3,4,5,7,8,9,11, enumerates all 32,211 projective points across those fields, and verifies the sharp construction, an invertible coordinate transform, and a nonreduced example. It checks 632,626 numerical component cases with integer q from 3 to 150. Three secant-curve countermodels outside the hypotheses check that connectedness alone does not imply the proposed bound. These are diagnostics, not exhaustive tests of algebraic curves or substitutes for the proof.

The six-page PDF is compiled with Tectonic; its final pages are rendered and individually inspected. The Markdown conversion preserves the complete argument and references, with a separate math-parser report. The exact final hashes and QA status are in the included JSON records.
