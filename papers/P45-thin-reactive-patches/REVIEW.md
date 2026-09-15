# Proof review

Henry Zweiman. September 15, 2026. P45, developed as Q53.

This is the originating assistant's internal proof audit. No independent mathematician or other agent has reviewed this manuscript. Rendering checks are separate from mathematical validation.

## Operator and normalization

The physical kernel is 1/(2pi distance), with decreasing eigenvalues nu_k and exterior Steklov eigenvalues mu_k=1/nu_k. The pullback has factor sqrt(epsilon J). After division by epsilon, its kernel is sqrt(JJ')/(2pi physical distance). The symmetric transverse sections have exact physical area epsilon A. These factors yield the limiting multiplier 2h/pi and the capacitance factor 1/(2pi).

The positive kernel alone would not prove a positive quadratic form. The manuscript uses the Gaussian representation to establish strict positivity and injectivity, and uses kernel positivity separately for simplicity of the top eigenvalue. Compactness follows by deleting the near-diagonal singularity, whose Schur norm tends to zero.

## Strong convergence and eigenvalues

The near-diagonal change of variables produces a bounded two-dimensional singular integral, not a divergent one-dimensional estimate. The far denominator replacement has total O(1) error. Hölder continuity is used for the uniform row remainder. Continuous transverse integrals, rather than an assumption of transverse constancy, prove strong convergence on a dense set. Schur bounds then extend it to L2.

The limit is noncompact, so no operator-norm convergence is asserted. Curvature is different: the difference BEFORE logarithmic normalization has O(1) norm. The Taylor error is bounded relative to Q by C(|d|+epsilon), uniformly even when y=z. Embeddedness controls separated arclength points. Periodic reference distance has the same local logarithmic singularity.

Strong convergence does not generally imply eigenvalue convergence. Here a separate row upper bound and a finite-dimensional minimax lower bound establish every fixed-index limit. The upper bound gives localization for any normalized eigenvector, including arbitrary choices in a multiple eigenspace. The zero-measure maximum-set assumption is used only for weak escape and weight vanishing; it is not silently imposed on rectangles.

## Spectral measure and all reactivities

The moving normalized constant input is sqrt(J)/sqrt(A), not exactly constant on curved strips. It converges strongly, so continuous functional calculus gives the area-weighted width distribution. The zero eigenspace from transverse oscillations has zero mass for the limiting input.

At finite scaled reactivity, resolvent convergence is uniform after division by t on each compact interval including zero. This is insufficient at perfect reaction. The manuscript supplies a separate three-dimensional logarithmic test potential, with full angular Jacobian and endpoint hemispheres. The factor 1/(4pi) in its energy bound is derived from -Delta v=2f delta_plane and the quadratic variational identity. This avoids assuming regularity of the Hölder patch boundary or continuity of inverse operators.

The capacity upper bound and monotonicity give convergence at infinity. Monotonicity in t and continuity of the limit on the compactified half-line give uniform absolute convergence; compact-interval convergence after division by t gives the stronger relative convergence near zero. The latter step is necessary and is explicit. No rate of convergence is claimed.

The one-pole comparison uses exact area and convergence of perfect capacitance in a harmonic mean. Strict Jensen inequality proves its equality condition. The nonconstant-profile limiting error tends to zero at both endpoints, so its positive maximum is attained at a finite positive t. The rhombus expression was integrated directly and its small-t slope matches area/(2pi).

## Tubes and weight reversal

The tube eigenvalue remainder is O(epsilon) before dividing by epsilon. Caps cannot be treated by a crude small-area norm estimate without losing this precision. The proof instead bounds strip rows, cap rows, and the constant Rayleigh quotient. A cap sees only one longitudinal logarithm. Endpoint logarithms in the strip average are integrable. Area and perimeter include both semicircles for an arc.

For three separated disks, r is chosen above both lambda_1/lambda_0 and 1/sqrt(2), and below one. This puts the two satellite ground states in an isolated second cluster. The first-order off-diagonal entry is positive r^2m^2/(4pi), so the even state is the larger eigenvalue; the block-diagonal limit alone would not determine it. The Schur complement controls the splitting and eigenvectors. The limit of F1/F0 is 2r^2>1.

The separation R is fixed BEFORE the channel width tends to zero. Norm continuity under small-area addition follows from both cross-block Schur bounds. The first two simple eigenprojections and the constant input then converge, preserving the strict inequality. No convexity is claimed for the connected three-disk example.

## Scope and verdict

No gap was identified in this internal audit of the stated results. The proof is analytic and does not depend on finite computation. The results do not include sharp subleading spectral asymptotics, fixed-index weight limits on positive-length maximum sets, singular center curves, or a convex example with F1>F0. Independent proof and priority review remain necessary before treating the claims as established by the community.
