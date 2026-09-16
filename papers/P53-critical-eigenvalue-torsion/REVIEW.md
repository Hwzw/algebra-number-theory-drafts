# Proof and artifact review

Henry Zweiman. September 16, 2026.

This is an originating-assistant review, not independent human verification.


The complete consolidated manuscript was reread. The proof checks addressed the following issues.

- The first variation uses an L2-normalized eigenfunction. The radial surface Jacobian cancels the normal-speed denominator exactly. Scale invariance removes the constant multiplier on the mean-radius slice.
- The fixed-domain Dirichlet and normalized eigenpair equations give analytic maps in the stated Hölder spaces. The volume boundary equation loses one derivative; the perimeter equation loses two. The complement inverse follows from elliptic Fredholm theory and harmonic testing, rather than a formal inverse multiplier series or density of polynomials in the full Hölder norm.
- For the compact Dirichlet-to-Neumann difference, the zero-mean harmonic extension is orthogonal to the radial resonant eigenfunction. The forced zero-boundary Helmholtz solution gains two derivatives. Simplicity excludes other resonances.
- The cubic eigenvalue coefficients satisfy finite Fredholm compatibility conditions. All correction modes extend across the sphere; their boundary and PDE residuals have the stated orders. Boundary lifting and nonzero pairing with the limiting ground state justify the eigenvalue remainder. The torsion remainder follows from the maximum principle.
- The two planar signs follow from rational Bessel-series brackets and explicit polynomial signs. The fourth-order formulas come from finite boundary cancellation, not numerical eigenvalues.
- The analytic centroid slice removes translation multipliers. Dilation first removes the mean-radius multiplier; translation invariance then removes the moment multipliers. The equivariant complement is centrally even, so the centroid correction vanishes on the reduced family.
- The reduced energy on trace-free symmetric matrices has the stated cubic invariant. Two analytic divisions of the symmetric gradient exclude three distinct eigenvalues. The second division is applied to an analytic Taylor remainder, not an uncontrolled pointwise error divided by a small eigenvalue gap.
- Every two-eigenvalue matrix belongs to one of the finite block-symmetry types. The scalar implicit-function argument exhausts each branch. Multiplicity and the normalized degree-two projection distinguish the unbalanced types; the two signs of a balanced branch are congruent.
- The balanced fourth-order boundary cancellation includes all allowed modes. Analyticity and block exchange improve the scalar fifth-order remainder to sixth order. The complement correction has degree four at its leading order, and maximizing the concave quartic gives the reduced coefficient.
- The displayed rational numerator polynomials are nonzero for each dimension because their constant terms are nonzero. Classical transcendence of nonzero rational-order Bessel zeros therefore establishes nonvanishing in every even dimension. Finite diagnostic dimensions are not used to extrapolate this theorem or a universal sign.
- The endpoint competitor is fixed before varying the exponent. This gives the local/global gap without assuming a neighborhood uniform at the degenerate endpoint.

The reread found no fatal mathematical gap. It did find a reversed prose description of the planar amplitude scaling; the source note now states explicitly that the planar amplitude equals half the balanced parameter. The coefficient formulas were already consistent with that substitution. It also found assembly errors: a journal issue number had acquired an equation prefix, a terminal period prevented one section reference from updating, and two internal subheadings had duplicate numbering. These are corrected in the assembly source. The mathematical rendering check is supplemental, not evidence that such semantic errors cannot occur.


## Publication artifacts

The complete Markdown manuscript is authoritative. Equation labels are normalized by section in the publication copy; assembly-provenance.json records the exact mapping from the research draft. Long displays are reflowed without altering their identities. Final PDF rendering and formula checks are recorded in artifact-check.json. The analytic proofs, not finite diagnostics, establish the claimed general results.
