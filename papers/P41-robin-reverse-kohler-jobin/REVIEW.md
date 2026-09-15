# Proof and artifact review

Henry Zweiman. September 15, 2026.

This record describes the originating assistant's internal adversarial review. No separate agent or human referee supplied an independent proof check. A manuscript and successful rendering are not certifications of correctness or novelty.

## Proof obligations checked

1. **Conventions.** The Robin energy uses beta times the boundary p-norm; tau is integral w. Thus the elementary global bound is lambda tau^(p-1)<=V^(p-1), and the scale parameter is beta R^(p-1). The ball torsion formula differentiates to -v'=(r/n)^(1/(p-1)) and has the required boundary flux.
2. **Admissible tests and trace.** The pointwise comparison bounds w. Compact-interval C1 functions h and H extend Lipschitz, so H(w) is a valid weak test. Traces commute with composition, and truncations transfer the essential bounds to the boundary. No boundary regularity of a competing eigenfunction is used.
3. **Boundary sign.** The exact correction is h(w)^p-w^(p-1) integral_0^w |h'|^p. Hölder makes it nonpositive. A linear continuation of h to zero makes the correction vanish at the ball boundary. Omitting this continuation or dropping the correction without its sign would invalidate the proof.
4. **Inverse radial coordinate.** The flux identity gives h' explicitly. It matches the linear extension at the boundary, has a finite center limit and defines a C1 function even though v' vanishes at the center. The mean value theorem verifies the endpoint derivative. The radial average decreases with radius, so h' increases with the torsion coordinate.
5. **Reference normalization.** The eigenfunction has p-norm one. Therefore integral_B H(v)=lambda_B and integral_B h(v)^p=1. The maximum derivative of h^p is p lambda_B^(1/(p-1)) phi(0)^p, with no missing radial factor n.
6. **Rearrangement directions.** H increases and w#<=v, giving the numerator upper bound. The same pointwise order turns the Lipschitz difference of h^p into L times the nonnegative L1 torsion deficit. The Rayleigh denominator is used only when its explicit lower bound is positive. The trial is nonzero.
7. **Near and far regimes.** c>=1 follows from h(0)=0 and normalization. k lies in (0,1]. For theta>=1-1/(2c), the logarithmic inequality yields lambda/lambda_B<=theta^(-2c). For smaller theta, the global bound gives the second exponent in (4.7). Both cover their common endpoint and theta=1. No optimizer-existence claim substitutes for this global estimate.
8. **Uniformity.** On the unit ball, the flux bound and normalization bound phi(0) uniformly. At beta=0, lambda/(n beta)->1 and the eigenfunction tends uniformly to the normalized constant, giving c->p and k->1. At beta=infinity, the boundary term tends to zero, radial flux convergence gives gradient-energy convergence, and the Dirichlet variational principle identifies the limit. A fixed-parameter trial gives continuity at interior parameter values. These facts imply finite sup c and positive inf k, hence finite sup q0. No numerical parameter grid is used as a proof.
9. **Components and equality.** A bounded Lipschitz set has finitely many Lipschitz components. Componentwise Faber--Krahn plus strict ball-radius monotonicity gives the full-set inequality and excludes disconnected equality. For q>=1+sup q0, product equality forces theta=1 and hence eigenvalue equality, so known rigidity identifies the ball.
10. **Deficit estimate.** theta^q<=R_q<=theta^(q-q0)<=theta proves both sides with Bernoulli; the threshold includes the extra one needed for the rightmost inequality. The optional asymmetry remainder is explicitly inherited from an existing torsion result.

## Source and scope check

See ASSESSMENT.md and source-audit.json for the exact source portions read. Theorem 1.1 answers only the planar linear case of BCS Q2; the nonlinear statement is limited to the verified Talenti range. The known linear Dirichlet reverse theorem is credited. The forward Robin question and linear dimensions at least three remain open here. All related results are consolidated in this one paper.

## Artifact verification

The authoritative source is manuscript.md with explicit inline and display mathematics. build.py converts it through Pandoc into portable LaTeX and compiles with Tectonic. The completed artifact-check.json records the final file hashes, page count, extracted text, local MathJax parsing and visual page review. Syntax and rendering checks do not validate mathematical assertions.
