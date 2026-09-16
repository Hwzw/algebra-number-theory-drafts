# Internal review of the convex-deformation theorem

Henry Zweiman. September 16, 2026. Originating-assistant review, not independent expert verification.

1. **Exact question.** The published P46 Section 7 asks whether the normalized square-root-log conclusion survives controlled deformations. The theorem constructs arbitrarily small smooth uniformly convex deformations where it fails. It does not rename the weaker small-rescaling concavity property as the question being disproved.
2. **Cubic obstruction.** Along a line, sqrt(w)=|t|sqrt(a+b t+O(t^2)). Its second derivative has opposite one-sided limits b/sqrt(a) and -b/sqrt(a). Both must be nonnegative for convexity. C4 regularity permits the differentiated remainder.
3. **Tensor conclusion.** Vanishing of every diagonal cubic value implies vanishing of the symmetric tensor by polarization. A nonzero cubic yields failure arbitrarily close to the maximum.
4. **Ball input.** The already proved estimate -D2 log U >= A I with A>1 is used, not inferred merely from strict log-concavity. The positive boundary slope and C2,gamma regularity come from the previous boundary argument, which addresses the non-Lipschitz nonlinearity.
5. **Ground-state eigenvalue.** L U=-2U exactly. The ground-state form identity makes this the simple first eigenvalue, rather than only a negative test quotient.
6. **Potential domain.** U is comparable to distance. The logarithmic potential is infinitesimally form-bounded by Hardy's inequality, so the form domain remains H01 and the resolvent is compact.
7. **Poincare constant.** The density is U squared, hence its potential Hessian is at least 2A. The constant is 1/(2A), giving L >= 2A-2 on the perpendicular complement.
8. **Vanishing boundary density.** The proof first uses smooth weighted Neumann problems on smaller concentric balls. The convex-boundary Bochner term has the correct nonnegative sign. Radius exhaustion and form approximation justify the desired weighted inequality.
9. **Kernel exclusion.** Testing a zero mode against U makes it perpendicular to U; positivity on that complement gives zero. No eigenvalue-count guess is used.
10. **Holder-space invertibility.** Division by a defining function loses one derivative. Multiplication by rho log rho is Holder of every exponent below one. The potential term is compact from C2,gamma Dirichlet functions to C0,gamma, so Fredholm index zero and kernel exclusion give an isomorphism.
11. **Boundary nonlinearity.** The implicit-function theorem is not applied to the scalar function at zero. Writing u=rho b with b uniformly positive makes 2rho b log rho + 2rho b log b an analytic map in the stated Banach spaces.
12. **Genuine domains.** The explicit radial graph is smooth, converges in every Ck norm, and has positive principal curvatures for small parameter. The radial cutoff gives a diffeomorphism identical near the old maximum.
13. **Positive branch.** The branch stays in the positive-Hopf cone. It solves the actual equation on the deformed domain, not a formal first-order residual equation.
14. **Shape derivative.** Its Eulerian boundary value is -Uprime(R)Y3, with the negative outward derivative from the ball. The material and Eulerian derivatives differ by DU dot V; V vanishes near zero.
15. **Boundary regularity of the derivative.** A nonzero boundary trace times the logarithmic potential can prevent C2 regularity at the boundary. The proof asserts only C1,gamma there and interior smoothness.
16. **Angular equation.** Degree three gives eigenvalue 3(N+1) on the unit sphere. Harmonic projection commutes with the radial linear operator. Homogeneous Dirichlet uniqueness removes every other mode.
17. **Nonzero cubic coefficient.** The regular radial equation after factoring r cubed is an integral equation in dimension N+6. Zero initial coefficient forces the zero solution and contradicts the nonzero boundary data. A negative-part test in the angular subspace gives its positive sign.
18. **Actual maximum.** The strict value gap away from the old center and a negative-definite Hessian nearby yield a unique global maximum. Its first derivative with respect to the shape parameter is zero because the degree-three shape derivative has zero gradient at zero.
19. **Moving-center correction.** The maximum moves by O(epsilon squared). Therefore the base fourth derivative does not cancel the order-epsilon cubic tensor. The calculation is performed at the moved maximum.
20. **Logarithmic jet.** At a critical point the third derivative of -log u is exactly -D3u/u. The e1 diagonal value has nonzero leading coefficient -6c/U(0).
21. **Ordinary log-concavity.** On an interior compact set it follows from the original strict bound and C2 convergence. A common boundary collar follows from uniform Hopf slope, positive curvature and C2,gamma bounds; the Schur complement handles the mixed terms.
22. **Scope of uniqueness.** Only the branch near the ball solution is classified by the implicit-function theorem. Global uniqueness of all positive solutions on arbitrary deformed domains is not asserted.
23. **Priority distinction.** GMS's final page-44 question is about balls and was answered by the previous revision. The present theorem answers P46's subsequent deformation question. Ishige-Salani-Takatsu's small-rescaling definition is explicitly distinguished. The weighted Poincare input is classical and credited.
24. **Evidence boundary.** The argument is a hand proof with no numerical PDE or finite parameter search as a dependency. MathJax, compilation, rendered pages and public byte checks establish artifact consistency, not independent correctness or novelty.

**Internal conclusion:** The proof supports the stated counterexample near every ball in every dimension at least two. Publish as a revision of P46 after final artifact checks. Do not claim an extraordinarily verified broad conjecture solution, a new paper count, or completion of the larger goal.

## Review of the retained ball results

# Internal proof and artifact review

Henry Zweiman. September 15, 2026.

This is the originating assistant's fresh audit of its own proof, not an independent referee report or human mathematical review. No subagents were used in this stage. Artifact results are recorded separately in artifact-check.json.

## Proof audit

1. **Normalization and center.** Differentiating the radial equation gives z''+((N+1)/r-2rz)z'=2z(z-1), with z(0)=2 log U(0)/N. The center boundary term in the integrating factor vanishes because z'=O(r). The Volterra equation gives uniqueness near any positive center and legitimizes the needed even expansions without assuming the global series in advance.
2. **Amplitude and signs.** A central value between zero and the Gaussian threshold would force a positive decreasing z bounded above by its center value, contradicting blowup of the logarithm at a finite zero. Equality is the exact Gaussian. Above the threshold the same identity makes z strictly increasing. Radial symmetry is credited to the published non-Lipschitz result; it is not deduced from the concavity being proved.
3. **Recurrence.** The symmetric convolution factor is n+1, and the denominator is (n+1)(2n+N+2). Separating the two endpoint products for n>=1 proves coefficient positivity; n=0 is handled separately. Dropping the negative term yields c_n<=A^(n+1), giving a genuinely convergent local solution. The integrated series satisfies the original equation because its residual has zero derivative and zero central limit.
4. **Global convergence.** A positive series with a finite convergence radius is singular at the positive real endpoint. The manuscript proves this with monotone convergence and the Taylor series at the hypothetical regular endpoint. A smaller radius than R^2 would contradict analytic ordinary-ODE continuation of the actual positive solution. A larger radius would contradict its logarithmic blowup. Division by 2j preserves the second series' radius.
5. **Convexity.** Positive even coefficients express sqrt(w) as a norm of nonnegative convex monomials. The probability identity in (4.3) was recomputed: its right-hand side is 2 variance + mean*(mean-1). All moments are finite within the convergence radius. The center is a norm-type cusp, not a C2 point. The exponent threshold follows from the radial leading power r^(2 beta), so necessity is local and applies to every solution.
6. **Boundary.** Bounded continuous forcing gives finite U'(R) and U''(R). Assuming zero slope, energy dissipation and monotonicity of -U' near the boundary give v<=C U sqrt(log(1/U)). The resulting infinite travel-time integral contradicts finite R. This replaces an unqualified Hopf lemma with a complete proof valid when f'(0)=-infinity, including N=1.
7. **Positive powers.** The Hessian condition is alpha<=w''/w'^2. The ratio is positive, tends to infinity at the center and one at the boundary, and is strictly below one near the boundary. Its positive minimum is attained in the interior. Center and boundary extension are explicitly checked.
8. **Parameter and product consequences.** For n>=1 the c_n are nonnegative polynomials in delta=A-1 without constant term. Their scaled comparison yields the normalized-profile inequalities. The simple-zero asymptotic excludes equal first zeros for different centers. This uniqueness conclusion is credited prior work. The product formula solves the PDE by separation and its transformed concavity follows from the finite-dimensional norm argument.

## Dependency and novelty audit

The externally used PDE results are existence and radial symmetry from Gallo--Mosconi--Squassina. The central IVP and analytic continuation facts are standard ODE results; the potentially delicate real-axis series singularity is proved in full. Neither finite computation nor symbolic tests are used as a substitute for any universal argument. No numerical experiment is needed by this manuscript.

The early note 0178 tentatively raised uniqueness as potentially new. The subsequent primary-source check found Ben Chrouda 2022 and corrected that interpretation before publication. The current June 2026 Liu--Sun--Zou v2 and current author version of the parabolic concavity paper were checked. The precise extent of the source inspection and its limits are recorded in ASSESSMENT.md and source-audit.json.

## Original revision limits (historical)

The original revision was for balls, with the stated product corollary. It does not settle stronger concavity on arbitrary convex domains or compute the optimal positive-power exponent. The proof and assessment remain open to expert correction. PDF compilation, MathJax parsing and public hash equality certify artifact consistency, not mathematics or originality.
