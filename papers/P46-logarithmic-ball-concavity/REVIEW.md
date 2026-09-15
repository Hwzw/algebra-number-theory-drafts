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

## Material limits

The proof is for balls, with the stated product corollary. It does not settle stronger concavity on arbitrary convex domains or compute the optimal positive-power exponent. The proof and assessment remain open to expert correction. PDF compilation, MathJax parsing and public hash equality certify artifact consistency, not mathematics or originality.
