# Proof and artifact review

Henry Zweiman. September 16, 2026.

The originating assistant reread the consolidated hand proof. This is not an independent review. The following records the substantive dependencies and checks; no numerical test substitutes for them.

## Functional setting and exterior normalization

The annular exterior must be connected. Subtracting its mean before extension gives a gradient bound that survives rescaling, even when the hole has several components. The fixed annular trace estimate and planar Sobolev embedding produce a vanishing inner-boundary form bound. An arbitrarily small gradient coefficient in the outer trace estimate permits a fixed coercive shift for negative Robin parameter as well as positive parameter.

The spectral lower bound uses weak lower semicontinuity outside a fixed disk, then shrinks the disk. It does not charge the artificial extension's gradient energy to the perforated form. Strong compactness of the outer trace handles its possibly negative coefficient. This proves convergence counting multiplicity and the complementary spectral gap needed later.

The finite-energy exterior space is a quotient by constants, anchored on one connected annulus. Zero total flux makes the boundary functional well-defined. Truncation in height followed by logarithmic radial cutoffs establishes density in the gradient norm. The exterior Fourier expansion excludes growing and logarithmic modes; removing its constant gives the unique decaying corrector. No false homogeneous Sobolev bound in dimension two is used.

## Correctors and scalar coefficients

The leading cutoff corrector has L2 size of order epsilon to the k+1 times a square-root logarithm. The boundary discrepancy is one order better than the leading derivative. The small-hole trace bound makes the H1 residual of order epsilon to the k+1-eta. The weak integration by parts uses the prescribed conormal derivative and does not assume corner H2 regularity.

The next energy coefficient uses the exact identity T=2L(A)-q(A,A)+q(R,R). Bounding the cross term merely by the product of two H1 norms would lose the desired precision. The remainder energy is smaller than order 2k+1. Mass, cutoff and complementary-projection errors are smaller as well. The first two Taylor terms are harmonic, as follows directly from the eigenfunction equation.

The projection normalization is checked using the exact pairing between the original eigenfunction and its corrector. This yields sufficient control for the local rescaled L2 limit, which does not follow from an unspecified global little-oh estimate alone.

For the nonnodal branch, the cutoff logarithmic field subtracts the scale-dependent constant before passing to physical coordinates. Its L2 norm is of order epsilon; its energy has the epsilon-squared logarithm. The sign of that logarithmic correction and the sign convention for the hole normal agree with the independent circular-sector calculations.

## Every branch of a multiple eigenvalue

The vanishing-order filtration terminates by finite dimensionality and analytic unique continuation. Each graded leading-polynomial map is injective, so each planar block has dimension at most two. The full polynomial energy matrix is strictly positive definite, including cross-degree terms for a nonspherical hole.

The exact cluster identity retains entrywise errors at the sum of the two corresponding orders. This gives a weighted matrix remainder, not merely an unweighted bound at the lowest order. The nonnodal-to-nodal entry is controlled by the boundary functional paired with the explicit nodal corrector. Its Schur correction is one power smaller than the nodal leading block, for either sign of the Robin parameter.

Increasing-order elimination is performed by a change of basis tending to the identity after weighting. Thus the transformed mass still tends to the identity. The inertia comparison bounds negative and positive generalized eigenvalues separately and multiplicatively, even when their sizes differ by many powers. The limit coefficients are the successive Schur complements, not the uncorrected diagonal blocks. This distinction is required by the 2026 Dirichlet corrigendum.

For a common-order cluster, the stronger mass estimate is identity plus order 2k, hence identity plus little-oh of epsilon. It leaves the next stiffness coefficient unchanged. Compression to a repeated leading eigenspace gives the second coefficient through ordinary finite-dimensional spectral perturbation.

## Shape construction and quantifiers

Pulling back to a fixed exterior space gives an analytic coercive family. Subtracting the mean on a fixed exterior circle preserves analytic dependence while selecting the decaying representative. Local smooth-boundary regularity justifies differentiating the pulled-back Neumann equation.

The disk variation is calculated from the zero-Neumann total field, with the radial derivative distinguished from the normal into the hole. Green's identity identifies the energy with a decaying multipole coefficient. The resulting degree-k matrix derivative depends on the 2k Fourier mode. Its two eigenvalues are opposite and nonzero for the selected Fourier series. An exact conformal calculation, valid for every positive integer k, checks both sign and factor.

Cross-degree energy blocks vanish at the disk. Therefore the first shape derivative of each Schur block is just the derivative of its diagonal block. A repeated two-dimensional block has a nonscalar first derivative; a block already simple remains simple locally. Each analytic discriminant is consequently nonzero as a function. Its zeros are discrete. A countable union over the spectrum gives the exceptional set of shape parameters.

For each good fixed shape, the weighted asymptotics separate orders and coefficients in each fixed cluster. Spectral convergence separates distinct limiting clusters. A finite window ending inside a limiting multiple eigenvalue is enlarged to include the full cluster. The resulting threshold depends on the window. No passage to a common positive threshold for the infinite spectrum is made.

## Supplementary checks and provenance

The preserved diagnostics contain six nodal circular-sector cases, two nonnodal logarithmic-slope cases, and nine synthetic weighted-matrix cases. Concentric disk eigenvalues have angular multiplicity; the scalar diagnostics restrict to one invariant angular sector. The matrices need not arise from a PDE eigenspace. Both limitations are explicit in the scripts.

The earlier review draft and its hashes are preserved internally. During its initial assembly, a broad equation-renumbering substitution accidentally changed four little-oh constants to equation labels. Visual reading caught the error; all four were corrected before the review draft was finalized. The publication copy starts from that corrected draft. Its mathematical expressions are unchanged; source attribution and status wording were updated. `assembly-provenance.json` identifies the exact input.

Final formula parsing, extracted-text integrity, rendering and visual findings are recorded separately in `artifact-check.json`. They establish artifact integrity, not correctness, novelty, or journal suitability. No third-party article PDFs are included in the public bundle.
