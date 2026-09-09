# Internal proof audit

Author: Henry Zweiman. Performed by the originating Codex agent, September 8, 2026. No separate-agent or human review is claimed.

## Direct rational-function theorem

1. **Well-defined numerical representation.** Transcendence over the coefficient field makes evaluation injective and ensures every nonzero numerator and denominator is nonzero at alpha. Reduced rational functions, rather than expressions with removable singularities, define the labels.
2. **Existence of an endpoint.** Each nonzero rational function has finitely many real zeros and poles. The nearest point on either side therefore exists when that side contains any such points. No choice from an infinite accumulating set is used.
3. **Positivity throughout the interval.** A continuous nonzero real function has constant sign on a connected interval. The sign is positive because the interval contains alpha.
4. **Addition and multiplication.** Two functions from one class are finite and positive throughout the same interval. Their sum and product cannot acquire an interior zero or pole. At a shared zero both operations have limit zero. At a shared pole both one-sided limits are positive infinity, so addition cannot cancel the pole and multiplication preserves it. Reduction of fractions does not alter these limits.
5. **Missing endpoints and touching zeros.** An infinite endpoint needs no condition. A zero of even order still blocks the connected component of the strictly positive set, even when positivity resumes beyond it. Multiplicities are not part of the label.
6. **Partition and exact cardinality.** Fibres are disjoint and exhaustive. Countability of the coefficient field gives at most countably many fibres. The polynomials t-r for rational r below alpha provide infinitely many distinct fibres. Both-endpoint labels also separate the affine functions with roots above alpha.
7. **Disproof of a weaker label.** Ignoring zero/pole type fails: (t-r) times its reciprocal equals 1. Retaining only the signs of the orders avoids this defect and is stable under powers.

No unresolved step was identified in the direct proof.

## Curve extension

1. **Base field and model.** For a finitely generated real field K of positive transcendence degree, choosing all but one transcendence-basis elements as the coefficient field leaves a one-variable function field over a countable characteristic-zero field. The cited model theorem applies without assuming geometric integrality.
2. **Specified order.** The actual inclusion K into R defines a real point on the model whose image over the coefficient field is generic. Thus the resulting evaluation order is the user's field order, rather than a newly selected ordering.
3. **Genericity.** The finite supports of principal divisors and the finite ramification locus exclude that point. No nonzero field element becomes zero, and no pole occurs at evaluation.
4. **Topology.** The real locus of a smooth projective curve is a compact one-dimensional manifold. Its component through the evaluation point is a circle. A positive component after removing finitely many zeros and poles is either that circle or an arc. The label includes the arc, so two arcs sharing endpoints are not confused.
5. **Coincident ends.** The two ends may be the same real point; the limiting argument still applies from both sides. It does not assume two distinct boundary points.
6. **Infinitude.** A nonconstant rational function is unramified at the generic real point in characteristic zero and gives a local coordinate. Rational values approaching its value produce distinct nearby boundary points. Each arc has at most two boundary points, so finitely many labels cannot contain all these witnesses.
7. **Algebraic constants and disconnected base change.** The argument uses only the real component through the chosen point. A nonconstant finite map remains nonconstant there; genericity excludes its finite ramification set. Geometric connectedness is not silently assumed.

No unresolved step was identified in this proof. Infinite algebraic towers are explicitly outside its scope.

## Computational and artifact evidence

The optional script verifies 180 rational functions, 275 pairs within 11 left-label groups, and 550 sum/product certificates using exact Sturm counts. Six explicit edge checks address reduction, missing types, unequal orders, even orders, and absence of real endpoints. These checks do not prove the curve theorem.

The complete Markdown conversion is checked against the LaTeX structure and numbering. PDF rendering and all-page visual review are recorded separately in the artifact manifest. Successful compilation and syntax checks do not establish mathematical correctness.
