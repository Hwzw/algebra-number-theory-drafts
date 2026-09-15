# Internal proof review

Henry Zweiman. September 15, 2026.

This review was performed by the originating assistant, not by a separate agent or an outside mathematician. It records the proof obligations checked and the limits of the result. Formatting checks and source searches are separate from proof validation.

## Dependency and sign checks

1. **Analytic branch.** The Robin form has common H1 domain. The derivative of the normalized eigenpair equation is invertible because the first eigenvalue is simple: pairing with u fixes the scalar derivative, normalization fixes the kernel component, and Fredholm inversion fixes the orthogonal component. Positive normalization patches the local branches over the whole real line. The argument needs only local analytic expansions, not one convergent power series on all of R.
2. **Gauge.** With nu_i dot gamma=-1, w=exp(-alpha gamma dot x)u has zero normal derivative on both rays. Direct differentiation gives Delta w=-2 alpha gamma dot grad w-(lambda+alpha^2|gamma|^2)w. Both signs were checked.
3. **Published regularity input.** Dauge's author-posted Theorem 8.1 applies to compactly supported homogeneous-Neumann weak solutions on R times a sector. At k=0 its criterion is 0<2-2/p<pi/omega. Multiplying the planar solution by a compactly supported smooth function of an extra coordinate proves the planar form used in Lemma 2.1. This reduction avoids a mixed condition at an artificial outer arc.
4. **Analytic H2 upgrade.** The cutoff and its Laplacian are analytic in H1 and L2 respectively. The weak Neumann graph space is closed, and its inclusion into H2 is bounded by the closed graph theorem and Dauge's regularity result. Analytic dependence therefore transfers through a fixed bounded map. Analyticity in C2 or C1,1 is neither assumed nor asserted.
5. **Different p ranges.** A p just above two, below 2/(2-beta) at an obtuse corner, gives C1 regularity. Separately, H2 gives grad w in every finite Lp in dimension two, and hence the forcing F in any finite Lp. The coefficient formula uses p above 2/(2-beta) only for F. Applying W2,p regularity to w at that larger p would be wrong; the manuscript explicitly avoids it.
6. **Corner positivity.** For alpha>0, k=lambda+alpha^2|gamma|^2 is positive. The weighted equation is -div(rho grad w)=k rho w. Positivity on the outer closed arc follows from interior positivity and the ordinary Hopf lemma on the open edges. Testing with (m-w)+ makes the left side negative and the right side nonnegative. The resulting zero gradient and zero arc trace show w>=m at the vertex. No smooth-boundary Hopf lemma is applied at a corner.

## Coefficient and obstruction checks

7. **Angular projection.** The cosine mode has derivative zero at both ray angles, so angular integration gives a''+a'/r-beta^2 a/r^2=b with no missing boundary term. Its homogeneous solutions are r^beta and r^(-beta); the latter is excluded by H1. The particular solution in (3.6) has the displayed positive/negative order of its two integrals.
8. **Direct formula check.** For b(r)=r^(kappa-2), kappa>beta, the particular solution is r^kappa/(kappa^2-beta^2). This agrees with direct application of the radial operator. For a=r^beta and b=0, (3.3) returns coefficient one. For an angular constant both projections vanish. These are hand checks of the formula, not numerical evidence for the theorem.
9. **Continuity.** With area measure s ds dtheta, the singular weight is s^(-beta). It is in L^{p'} exactly when beta p'<2. Thus p>2/(2-beta) makes the coefficient functional continuous. The residual is O(r^(2-2/p)), strictly higher order than r^beta. The fixed arc trace is bounded on H2 on a slightly larger sector.
10. **Semiconcavity.** In the interior, semiconcavity bounds the two Hessian eigenvalues above. The PDE bounds their sum below and above because the relevant function and gradient are bounded near the positive corner. Each eigenvalue is therefore bounded below as well. Convexity of the sector lets integration along segments extend the gradient Lipschitz bound to the vertex. Multiplication by the gauge preserves C1,1. Its zero gradient at the vertex makes the first cosine projection O(r^2), forcing c=0.
11. **Nonzero seed.** Differentiating the normalization gives integral v=0, and testing the differentiated equation with one gives mu=perimeter/area. At a vertex, v+mu|x|^2/4-gamma dot x is harmonic Neumann. Only the first mode at an obtuse corner has exponent in (1,2). If all such coefficients vanished, the Fourier expansions and smooth open-edge regularity would give C2 on the closure, contradicting ACH Corollary 8.3. The differentiated forcing is constant, so c'(0) is exactly the nonzero first-mode coefficient.
12. **Quantifiers.** A nontrivial real-analytic function on R has finitely many zeros in any compact interval. The proof gives a fixed vertex, a fixed polygon, and arbitrarily large bad parameters. It does not just give a polygon that changes with alpha. It does not show that all positive parameters are bad, or that only finitely many exceptional parameters exist on the unbounded half-line.
13. **Examples.** The displayed parallelogram has side lengths 2 and sqrt(2), so the tangential-quadrilateral necessary condition fails; its angles are pi/4 and 3pi/4. Products with intervals preserve the Robin parameter on every face. The positive product is the ground state, and slice restriction transfers failure of log-concavity. These examples are part of the same theorem and paper.

## Outcome

No remaining logical gap was identified in the stated theorem during this internal audit. The proof uses the established ACH first-variation rigidity and Dauge Neumann regularity theorem; it does not independently reprove the entirety of either source. The source audit names the exact statements inspected. No finite-element experiment, symbolic verifier, or artifact check is used as a substitute for a universal argument. Historical priority and the mathematical conclusion remain subject to expert review and correction.

## September 15 revision: interval lifting

The Section 6 proof was checked directly. Failure of semiconcavity for a C2 function on a convex open set is exactly absence of a global upper Hessian bound. Bounded gradient and a fixed nonzero interval logarithmic derivative keep the correcting tangent component bounded. Its Hessian cost is finite for each fixed positive parameter, while the polygonal positive Hessian is unbounded. Taylor expansion is taken at one fixed interior point after the positive curvature has been obtained; no uniform Taylor remainder near the corner is assumed. Both endpoints strictly exceed their midpoint, proving nonconvexity of a superlevel set. The interval derivative is explicitly nonzero. The product Robin parameter is identical on every face. Higher-dimensional slicing retains the same midpoint witness. All analytic and regularity inputs are proved in Sections 2-4; no new PDE regularity theorem is assumed.

This is an originating-assistant audit, not an independent review. The full ACH Conjecture 2 remains unresolved.

## Revision 1.2: weighted cone proof audit

1. A radial cutoff preserves Neumann data and has L2 Laplacian; convex-domain H2 regularity therefore gives h = partial_e psi in local H1, including the vertex.
2. Transverse concavity transfers by positive homogeneity only because all cone points have positive e height.
3. Face differentiation gives H nu = a nu. Eliminating the mixed component yields (7.6) exactly. Its sign depends on the strict k < 1/sqrt(2) hypothesis.
4. Codimension-two logarithmic cutoffs have vanishing H1 energy. They remove the skeleton from nonnegative tests, then pass the facet flux inequality to all compact tests by the H1 continuity of the form. Thus no boundary Hessian trace at an edge is assumed.
5. The exponential test is integrable by the separately stated strict-dual condition. Homogeneous annular norms give vanishing cutoff errors; q is nonnegative, so the resulting integral identity forces it to vanish.
6. A negative-semidefinite transverse block with zero trace is zero. Transverse affinity, homogeneity and harmonicity then force psi = 0 for degree between one and two.
7. The Robin corollary assumes a nonzero leading mode at an eligible cone. Its tangent correction uses a nonzero limiting derivative along gamma and is of order rho^(beta-1); the fixed midpoint witness then survives the Neumann perturbation.
8. The triangular-cone example proves nonempty degree range variationally. Positive spanning gives the strict-dual property; bounded convergence gives a Rayleigh quotient tending to two; ACH's equality classification gives the strict lower bound on each pointed cone. No explicit epsilon or numerical eigenvalue is asserted.
9. The exact matrix (7.16) shows the sign step fails in the remaining angle range. It is not a counterexample to the full conjecture.

This is an originating-assistant proof audit. The full conjecture, independent human review, and broad priority certification remain outside the established result.
