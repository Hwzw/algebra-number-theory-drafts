# Internal proof and artifact review

Henry Zweiman. September 15, 2026.

This is the originating assistant's audit of the completed manuscript, not a separate agent's or a human referee's independent review. No numerical experiment substitutes for a proof step.

## Proof obligations

1. **Signs and orientation.** The positive tangent satisfies that (outward normal, tangent) is positively oriented. With star dx=dy, holomorphic u+iv satisfies dv=star du, Tv=Au and Av=-Tu. Thus Af=-iTf, verified by the unit disk mode exp(ins). The Green/Stokes identity leaves the nonnegative norm of dv-star du, so the trace criterion works on any genus and with any number of boundary components.
2. **Mean-zero inverse.** A has only the global constants in its kernel. For connected boundary, the Neumann compatibility condition is exactly zero boundary mean, and the boundary mean fixes the additive constant of the inverse. H is defined only on that space.
3. **Period defect.** The period map takes values in a 2g-dimensional de Rham space when there is one boundary component. On its kernel a global conjugate exists, and Hf=-v, H squared f=-f. This proves a finite-rank bound by factoring through the period image. It does not assert existence of a conjugate for all f.
4. **Exact Fourier identity.** A positive real symmetric two-by-two matrix S satisfies (inverse S times J) squared=-I/det S. Under exact commutation, A and H preserve every Fourier plane. Infinitely many nonzero scalar defects would give infinite rank; no asymptotic symbol estimate is being promoted to exact equality.
5. **Holomorphic kernel on high modes.** Reality and self-adjointness force equal real diagonal entries in the complex plus/minus basis. The determinant identity makes the holomorphic kernel one-dimensional. Strict energy positivity gives positive-frequency coefficient larger in modulus, allowing the stated normalization. The determinant of A+iT has the required negative n squared sign.
6. **Projection and multiplication.** Both A and T commute with the orthogonal projection to an entire Fourier plane. The projection therefore preserves the holomorphic-trace algebra. The frequency-one coefficients of the product of modes n and n+1 are c_n and c_(n+1), with no other frequency-one contribution. If c_n is nonzero, positivity proves the ellipse coefficient has modulus below one.
7. **Exceptional quotient.** When every sufficiently high negative coefficient is zero, the two holomorphic extensions obey the power identity by boundary uniqueness. Their quotient is meromorphic and its nth power is holomorphic, ruling out poles. Nonvanishing of the denominator at the boundary gives smoothness there. The quotient is not assumed holomorphic without this argument.
8. **Degree and topology.** The real-linear boundary ellipse map has positive determinant 1-|c| squared. The argument principle counts one preimage with multiplicity inside and zero outside; zeros are finite because the boundary trace avoids the chosen value. Open mapping rules out interior points on the image boundary. The resulting interior biholomorphism and boundary bijection give a homeomorphism of compact bordered surfaces.
9. **Smooth cap.** A smooth annular collar reduces general capping to smooth disk-annulus welding. Compatible metrics on the welded conformal surface restrict conformally to the old pieces. Only the original line elements on the uncapped boundary are restored. No matching of normal metric jets or a seam conformal factor of one is assumed. Two-dimensional energy invariance gives the exact sum of piece energies.
10. **Trace minimization.** Matching H^(1/2) traces glue piecewise H^1 functions across the smooth seam. Minimizing on each piece and then over the seam yields the form infimum. Zero trace on the nonempty uncapped boundary gives Poincare coercivity for A_YY, so A_YY+B is invertible on the full seam space, including constants. B alone is never inverted.
11. **Operator and measure.** The disk radius and arclength identification make B=square root of Delta_Y, also after orientation reversal. The metric on X is unchanged, hence there is no missing boundary-density factor in the Schur complement.
12. **Preserved commutation.** Block identities are first used on smooth functions. Self-adjointness makes spectral projections commute with the diagonal seam block; density transfers this to forms. Uniqueness of the seam solution gives commutation of the inverse with the projections. The argument covers absent matching eigenvalues and the constant eigenspace. Smooth Fourier expansion then proves the full commutation identity.
13. **Iteration and scope.** Each cap reduces the boundary count by one and leaves genus unchanged. The final one-boundary theorem establishes genus zero. Only then is Speciel's existing classification invoked. The theorem is orientable and smooth; neither a nonorientable nor an approximate-commutation extension is asserted.

No unresolved logical gap was identified in this audit. This remains subject to external verification and correction.

## Source and priority obligations

ASSESSMENT.md and source-audit.json state the exact primary texts, arXiv histories, inspected portions and remaining limits. The complete final Speciel paper retains the stated open problem. Classical finite-period and welding results are credited. The later stability and ball-rigidity papers were compared within the documented scope. Absence of a found competing paper is not an absolute novelty certificate.

## Artifact obligations

manuscript.md is authoritative. The PDF was compiled through portable LaTeX. All 264 mathematical expressions passed local MathJax parsing, and all 31 display tags agree uniquely between Markdown and TeX. The nine-page PDF has 22,243 extracted text characters without replacement characters. Every page of the exact final PDF was rendered at 105 dpi and visually inspected, with no clipping, overlap or missing glyphs. The TeX log reports no overfull or underfull boxes or missing characters. Hashes and exact evidence are recorded in artifact-check.json. These checks do not inspect GitHub's live mathematics renderer or certify the theorem.
