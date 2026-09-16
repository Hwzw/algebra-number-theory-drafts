# Q60 proof and source review

Henry Zweiman. September 16, 2026.

This review was performed by the same assistant that developed the proof. It is not independent expert review. The final expanded manuscript is provisionally admitted as P51; earlier checkpoint decisions are historical. Publication is verified separately.

## Proof audit

1. **Realization and infinity.** The positive-parameter problem uses the magnetic graph space, including square integrability. The Landau inequality is applied only after zero extension of a zero-trace function, where it is valid. The lower bound is 2b+p. The zero-parameter problem uses bounded harmonic extension, constructed by planar inversion; it does not require constants to be square integrable.
2. **The large-ratio regime.** Differentiation of the radial integral is at fixed a, appropriate to the radial variable. The remainder is expressed through az, comparable to b+p, uniformly for all a at least 1/2. A fixed-a special-function expansion would not cover p/b tending to infinity. The proof avoids that error.
3. **Uniform angular index.** Both variational bounds hold for every nonzero integer mode and either sign. The free-end minimizer on the finite annulus is displayed. The cutoff identity has its boundary contribution equal to |n| and controls the cross term uniformly. This is weaker than known special disk refinements and is not claimed as their resolution.
4. **Boundary operator topology.** Smooth parameter dependence in the order-zero symbol class is needed for the L2 norm rate. The proof uses finitely many symbol seminorms and the smooth fixed-domain Dirichlet inverse, rather than an unsupported assertion that individual order-zero differences are uniformly small. The off-diagonal blocks are smoothing because their boundary arguments are separated.
5. **Schur formula.** The two outward conormals at the matching circle give C+T, not C-T. The bounded inverse is controlled by the positive zero-parameter operator. Off-diagonal smoothing on both sides of a bounded L2 inverse is enough for the inner-boundary smoothing claim; no unnecessary assertion about that inverse on all distributions is used.
6. **Capacity constants.** The Green-function normal points into the obstacle. The signs, the rank-one inverse correction and the mean value on the matching circle give the exact cancellation of R. The field is 2b. The magnetic constant log(4)-gamma differs from the scalar constant log(4)-2gamma.
7. **Spectrum and geometry.** The all-index error follows from a bounded self-adjoint difference. Fixed-cluster power-series convergence is not asserted uniformly over clusters. The second-order ground-state contribution is negative. The disk gap includes both a strict capacity deficit and a nonnegative harmonic-measure term. Its limit is uniform over the joint quadrant, but the eventual comparison threshold depends on the obstacle.

No fatal proof gap was identified in this internal pass. This is an assessment of the displayed argument, not a certificate of correctness. The parameter-dependent pseudodifferential lemma is the most appropriate point for a specialist to scrutinize first.

## Corrections made during this pass

- Repaired a control-character corruption in the audit-note LaTeX fraction; the math validator then passed.
- Corrected a u1/nu1 notation mismatch in the ground-state calculation.
- Made equation numbers sequential and updated their references.
- Replaced an unnecessarily broad smoothing-inverse assertion by the explicit off-diagonal composition argument.
- Added the free-end minimizer behind the uniform angular lower bound.
- Generalized the already-derived fixed-magnetic-axis disk gap to the joint nonnegative quadrant using the uniformly bounded logarithmic shift; this is one theorem consequence within this paper.

## Closest literature and access boundaries

The final Christiansen–Datchev Section 4 was read in full and the main theorem page visually inspected. Its scalar rank-one/capacity mechanism is prior work. The final ground-state proposition is 4.2, rather than 4.1 in arXiv v3.

Helffer–Nicoleau's author page links the March 25, 2025 preprint. Relevant disk statements and the general-domain open paragraph were compared there. The final journal preview was read, but the complete final PDF returned HTTP 403. No final-body comparison is claimed. Bundrock and coauthors' June 23, 2026 v3 independently retains the expected general-domain magnetic equivalence in Remark 1.6 and suggests a qualitative route.

Kachmar–Lotoreichik's complete exterior Section 3, including the proof of Theorem 3.6, was read. Their trial function uses distance to the obstacle and estimates moments of parallel curves using symmetry. Their allowed field interval and restricted geometric class differ from the present fixed-obstacle eventual conclusion. The candidate must not be advertised as proving their entire conjectural field range.

The general-domain Helffer–Kachmar–Nicoleau author PDF has a bounded-domain weak-field perturbation section. The flux article's inspected introduction distinguishes its weak-field disk Neumann result from its strong-field Steklov refinement. The September 15, 2026 JDE singular Sturm–Liouville article was screened through primary abstract/theorem statements and concerns the strong-field regime. These proofs were not all read, and none is a proof dependency here.

The full machine-readable source record and exact download hashes are in source-audit.json and source-downloads.json. Failed downloads are retained as failures. Targeted search results did not reveal the same general-obstacle joint expansion, but that is not exhaustive priority evidence.

## Checks and their limits

The Markdown math validator checks parsing, not mathematical truth. PDF compilation and visual inspection check artifact integrity. The 24 retained floating-point radial cases check numerical consistency across selected ratios and two radii; they are not interval certificates or substitutes for the uniform hand proof. No noncircular PDE computation is used to infer a theorem.

## Small-flux extension audit

The expanded manuscript was checked in the same internal workflow, not by an independent reviewer.

1. **Radial cancellation.** The Kummer connection formula is used with its correct nonintegral second parameter. Both gamma factors and the bracket change sign at negative flux. Uniform coefficient estimates for M and its parameter derivatives control their cancellation, including arbitrarily large a. The radial derivative holds a and flux fixed.
2. **Scalar axis.** A compact-support upper bound and local weak compactness with the positive scalar mass justify b tending to zero. This does not assume a fixed-flux special-function remainder is uniform at zero.
3. **All angular modes.** The nonzero exponents are at least 3/4. The free-end lower bound and cutoff upper bound are uniform in the angular index; the convenient error exponent 3/8 is not asserted sharp.
4. **General obstacle and singular gauge.** The pole is inside the obstacle, outside the bounded matching region. Landau coercivity is proved on compactly supported functions in the exterior and extended by density, without extending the singular potential through its pole. The circle operator with its zero mode removed is analytic in signed flux. The bounded-region Dirichlet inverse gives analytic dependence by a local Neumann series; the principal symbol is fixed.
5. **Crossover and signed difference.** Conjugation makes the auxiliary simple ground eigenvalue even in flux. This does not assert that the actual constant-field problem is even. The gamma quotient yields the odd denominator term. Comparing the radial coefficients and then applying the mean-value theorem to the auxiliary eigenvalue gives the third-order law. No derivative of the uncontrolled operator error is taken.
6. **Scope.** Only one specified flux pole is treated. The error to the parameter-dependent model is algebraic; convergence to the fixed nonzero-flux limit still has its slower fractional power. A multivariate analytic operator family does not imply analytic individual branches at a multiple eigenvalue.

No fatal gap was identified in this pass. This remains an internal assessment. The finite-parameter boundary-calculus claim and its uniform L2 topology remain appropriate specialist review points.

The final artifact pass corrected accidental equation-reference substitution inside O_R(1), and explicitly justified bounded-operator analyticity. The MathJax parser would not detect that semantic substitution, illustrating why parsing is separate from proof review.

## Added primary-source comparison

Helffer–Nicoleau's full author-preprint Section 5.2 was reread. Provenzano–Savo's cylinder formulas and full Appendix B proofs of Theorems 16–17 were compared: their compact-annulus argument uses conformal energy invariance and convergence of eigenfunction moduli to a constant. It concerns a fixed compact annulus. Cekic–Siffert's final JFA introduction, Theorems A/B and Examples 2.2–2.3 were read; these supply compact-surface high-frequency and cylinder comparisons. The DLMF connection identity is a classical input. Exact versions, inspected scope and unresolved final-text access are in source-audit.json.

The extension retains 168 radial transition cases and 36 signed-asymmetry cases. Quadrature refinement agreement for the former is at most 2.22e-16, while the largest radial-model error divided by rho is about 1.816. The latter show approach toward the derived limit along four logarithmic scales, with finite-scale discrepancies retained. Neither diagnostic is an interval certificate, a noncircular PDE computation or a proof.

## Geometric transition audit

The same-assistant audit checked the additional Section 11 argument as follows.

- The exterior conformal map satisfies F(w)/w nonzero with zero winding. Its logarithm removes the exact part of the pulled-back flat potential. The flat boundary space is weighted by |F'|, and the operator is the weighted circle multiplier. Its decaying finite-energy modes need not be square integrable; no positive-parameter L2 condition is incorrectly retained at the flat limit.
- On the positive side of zero flux the circle multiplier is exactly affine. Its action on the constant vector gives the first derivative and reduced-resolvent quadratic coefficient. The displayed Fourier identity for the harmonic-measure term fixes every factor of 2 pi. The term vanishes only for a disk.
- The auxiliary ground branch is even in flux. The zero-flux axis and exact flat-flux curve determine its full quadratic polynomial; this is an identity of analytic Taylor coefficients, not inference from a numerical fit. On a circular annulus, the constant-mode transfer formula independently gives the same coefficients.
- The derivative bounds for nu coth(nu d/2) are uniform at nu=0 and at large nu times d. The fixed capacity shift therefore has a cubic error in |nu|+1/log(1/rho), without assuming a bounded scaled flux.
- The disk deficit contains a nonnegative capacity term and a strictly positive harmonic-measure square for every nondisk. The cubic error is smaller on a sufficiently small rectangular parameter neighborhood. The operator error is negligible relative to the inverse-logarithmic square uniformly over that neighborhood. The constants depend on the shape; there is no assertion uniform over all obstacles.

The 12 retained finite-Fourier checks on two ellipses, with cutoffs 40 and 80 and three small positive fluxes, are consistent with the flat quadratic coefficient. At flux 0.005 the coefficient differs from its asymptotic limit by about 0.24 percent and 0.16 percent for the two shapes; these finite errors are retained. The geometric theorem itself is proved analytically and is not inferred from these cases.

The complete final Colbois–Provenzano–Savo Theorem 16 proof, circle spectrum in Theorem 33 and Appendix C were inspected. Their classical bounded-domain inequality and conformal ingredients are credited. Current arXiv histories and additional searches are preserved in source-audit.json. The admission reasons and remaining priority/significance uncertainty are stated in ASSESSMENT.md.
