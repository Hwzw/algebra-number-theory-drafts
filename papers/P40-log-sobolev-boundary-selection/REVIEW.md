# Proof and artifact review

Henry Zweiman. September 15, 2026. P40 / Q46.

The originating assistant constructed and reread this argument. This is an internal proof audit, not an independent agent review, formal proof-assistant verification or human peer review. No gap was identified in the following obligations; that finding can be revised if a counterexample, proof error or prior result is supplied.

## Theorem obligations

1. **Uniform normal geometry.** Convexity gives global exterior projection and nonnegative principal curvatures. Quadratic growth dominates the normal density by a Gaussian times a polynomial, uniformly over the compact boundary. This proves the boundary mass coefficient and controls the tails.
2. **Anchored collapse.** Convexity along each normal ray gives the increment lower bound. The tail/weight ratio is at most a constant times epsilon. Integration by parts first on smooth tests yields the zero-trace weighted Poincare estimate; approximation then passes to the weighted space.
3. **Zero-trace entropy.** The Euclidean logarithmic inequality follows from Gaussian log-Sobolev with the cross term and normalization displayed. Apply it to compactly supported transformed functions first. The potential terms are nonpositive under the stated Laplacian and growth assumptions and are eliminated before the density/Fatou passage. Unknown moments involving derivatives of the potential are not assumed.
4. **Uniform exterior entropy.** A bounded extension has a uniform trace exponent strictly above two on parallel surfaces. The normal L2 difference is bounded by the square root of the distance. Subtracting the extension leaves a zero-trace function; its entropy and mass estimates control the full exterior, including infinity. The resulting error is uniform on the stated bounded-energy families.
5. **Rescaling near constants.** The derivative estimate for the family F(a+delta z)/delta squared is uniform, including at zeros of a+delta z. Boundary convergence uses uniform integrability, not a Taylor estimate on an unbounded pointwise range. The exact mass-normalized identity (7.5) has a nonpositive correction. Dropping it yields a valid upper bound after division by arbitrarily small energy.
6. **Boundary energy lower limit.** Rescaling on each fixed normal strip, anchored collapse and compact trace convergence identify a boundary value independent of the normal variable. Weak lower semicontinuity produces its tangential energy without assuming boundary-gradient convergence for general near-extremizers.
7. **Compactness and finiteness.** High energies give quotient zero after normalization; positive limiting energies give nonlinear extremizers; vanishing energies linearize to the first spectral level. The argument excludes divergent quotients even if a Gibbs supremum were initially infinite, so eventual finiteness is not assumed circularly.
8. **Extremizer regularity.** Differentiate the full homogeneous entropy functional before normalizing its mass. The Euler equation has the stated coefficient and no extra multiplier. Subcritical logarithmic growth puts its right side in L2. Neumann H2 regularity gives compact H1 boundary traces. Rescaled extremizers approaching constants satisfy a uniformly controlled equation and converge to the spectral coefficient.
9. **Matching derivative bounds.** Normal-constant extensions give nonlinear and spectral lower tests. The order-epsilon lower bound forces order-epsilon exterior energy for near-maximizers in both branches. The uniform entropy expansion and boundary energy lower limit then give the matching upper bound. Compactness of the compactified extremizer family gives a finite attained coefficient.
10. **Nonlinear example.** The triangle eigenfunction and eigenvalue are classical. The manuscript's lattice-cell proof gives nonzero third moment and a strict entropy-quotient gap. The explicit smooth convex sublevel domains have common interior/exterior balls. Uniform extension, compactness and Rayleigh quotients prove Neumann spectral convergence. One fixed entropy test survives the rounding; no continuous selection of an eigenfunction in a multiple eigenspace is presumed.

## Dependencies

- Gaussian log-Sobolev: Gross (1975); the exact Euclidean normalization and its use are derived in Lemma 3.1.
- Sobolev extension, compact embedding and trace results on bounded smooth domains: classical facts, with their required exponents and uses stated in the manuscript. McLean is a standard reference; only its publisher front matter was accessed, not a new primary-text verification of all its chapters.
- Neumann H2 operator domain: Grubb, arXiv:1412.3744v4, Section 5, equations (5.6)--(5.7), with p=2 and I minus Laplacian. The C2 boundary hypothesis is weaker than this paper's C3 assumption.
- Triangle spectrum: Berard--Helffer (2018), Section 3.1, equations (14)--(15).
- Uniform extension on the rounded triangle family: Berard--Helffer (2021), Definition 2.1, Remark 2.2 and Proposition 2.10. The explicit family is convex and reflection symmetric after centering, with the required common inner/outer radii.
- No unpublished Q46 lemma or unproved numerical conjecture is used as a theorem dependency. Historical extremizer existence is credited but proved directly in Section 5.

## Exact auxiliary diagnostics

`python3 check_triangle.py` uses SymPy 1.14 to integrate the exponential representation in barycentric coordinates and check the PDE and all three normal conditions. The recorded moments are 0, 3/2, 3/2. This is a separate calculation from the manuscript's hexagonal-cell proof. It checks an example, not the infinite-dimensional theorem or its novelty.

## Publication artifact checks

The authoritative `manuscript.md` uses explicit inline and display LaTeX. `build.py` calls Pandoc and Tectonic; it performs no heuristic mathematical token conversion. The checked TeX body is generated from the same Markdown, with only section formatting, proof-end symbols and Polish-letter encodings adjusted. All 56 display tags and formulas agree, apart from consistent upright LS typography and two explicit spacing commands relative to the earlier draft. The prior heuristic review copy is retained only in the Q46 history.

All 13 final PDF pages were rendered and visually inspected. There is no clipping, overlap or missing mathematical glyph. Text extraction has 30,442 characters and no replacement character. The final log has no missing characters or overfull boxes; two underfull bibliography paragraphs were visually checked and are legible. Local MathJax parses all 413 expressions with zero errors. This is not a claim about GitHub's live rendering engine. Exact hashes are in `artifact-check.json` and `SHA256SUMS.txt`.
