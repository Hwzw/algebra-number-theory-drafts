# Priority and significance assessment

Henry Zweiman. September 15, 2026. P41, developed as Q48.

## Decision and precise contribution

Proceed as one substantial research preprint, contingent on artifact and public-publication checks. The originating assistant's proof audit identified no remaining gap in the stated theorem. The current primary-source comparison found an explicit open question and no prior result supplying the proposed answer in its stated Robin scope. This is an internal, revisable research assessment, not independent certification or a journal-acceptance prediction.

The paper gives a proposed affirmative answer to **the planar case** of Buttazzo--Cito--Solombrino's reverse Kohler--Jobin question: balls uniquely maximize the first Robin eigenvalue times a sufficiently large power of torsional rigidity among all bounded planar Lipschitz sets of prescribed area. A single exponent works for every positive Robin parameter and area. The nonlinear extension for 1<p<=n/(n-1), the parameter-uniform spectral-deficit control and the equivalent product/torsion deficits are one coherent contribution in this paper.

## Closest source and open status

[Buttazzo, Cito and Solombrino](https://link.springer.com/article/10.1007/s00032-026-00438-2), Milan Journal of Mathematics 94 (2026), 369--386, published June 1, 2026, still states the reverse inequality as **Section 5, Q2**. The inspected arXiv history lists only [2512.14927v1](https://arxiv.org/abs/2512.14927), submitted December 16, 2025. Their known positivity threshold for the infimum is a different result. The present theorem does not settle their forward question Q1 or linear Q2 in dimensions at least three.

[Bucur, Lamboley, Nahon and Prunier](https://arxiv.org/html/2304.10916v2), Corollary 1.6, already proves the full linear **Dirichlet** reverse inequality. Its current version page lists v2, October 29, 2025. The introduction, exact corollary and complete Section 6.2 proof were read. The latter uses a preceding spectral stability result; the present paper supplies a Robin torsion-composition argument. Applying it in a Dirichlet limit is not counted as a separate open-problem solution.

## Essential prior input and bounded comparison

- [Amato--Gentile--Masiello](https://link.springer.com/article/10.1007/s10231-021-01153-y), Theorem 1.2(i), supplies the pointwise comparison. Its published statement, hypotheses and dimensional exponent were checked, together with the arXiv v2 proof on pages 13--14. The range p<=n/(n-1) is essential to the cited proof. This is a substantial prior theorem, not a result of P41.
- [Alvino--Nitsch--Trombetti](https://doi.org/10.1002/cpa.22090) supplied the original planar linear result. The published Theorem 1.3 and introductory scope were checked through the University of Naples primary repository. The corresponding arXiv record lists v2, June 14, 2020.
- [Bucur--Daners](https://secure.maths.usyd.edu.au/u/daners/publ/abstracts/fkineq/isoper.pdf), Theorem 1.1, supplies Robin p-Faber--Krahn and rigidity. Positivity, simplicity, regularity and radial ball facts were checked in the introduction, Lemma 2.1 and Section 4. P41 supplies the component argument needed for disconnected competitors.
- [Amato--Barbato--Cito--Masiello--Paoli](https://arxiv.org/html/2511.11316v1), introduction, Theorems 1.1--1.4 and complete Section 4, gives quantitative Talenti and separate isoperimetric deficits. No competing product theorem was identified in these statements and applications. Its Corollary 4.1 is credited for P41's optional geometric remainder. The arXiv record lists only v1, November 14, 2025, but the rendered HTML has an internal August 24, 2026 date. The audit compared and archived the actual current HTML; it does not infer an earlier version of its contents from the metadata.
- [Barbato--Masiello--Sannipoli, 2603.26582v1](https://arxiv.org/html/2603.26582v1), introduction and all principal statements, treats convex Robin quantities with perimeter, inradius and slab remainders. These are different functionals and do not supply this product theorem.
- [Buttazzo--Fernandes Horta](https://cvgmt.sns.it/media/doc/paper/7593/BFH26.pdf), first five pages, treats Dirichlet energies and optimization over anisotropic seminorms on a fixed domain. It is not the present Robin domain problem.

These are statement/dependency comparisons of the specified portions, not claimed independent verifications of every cited paper. Exact source downloads and hashes are recorded in source-downloads.json; third-party PDFs are not republished in this package. The dated source-audit.json identifies version histories, reads, searches and limitations. Exact-topic searches returned no identified later Robin solution. No finite search excludes all prior, unindexed or unpublished work.

## Why the result is substantive

The theorem resolves an explicitly posed shape-optimization problem across the entire planar Lipschitz class, including arbitrary topology and disconnected sets. Separate isoperimetric inequalities point in opposite directions and do not prove the product bound. Convergence toward the torsion maximizer as the exponent grows would also be insufficient: it would not show exact optimality for any finite exponent.

The added mechanism is a trial function built from the inverse radial torsion coordinate on the ball, with a linear continuation below the ball's positive boundary trace. Hölder controls the competing boundary energy with the correct sign and preserves equality on the ball. The prior Talenti theorem then controls the energy numerator and the loss in the denominator. This yields a linear relative spectral estimate and, combined with a global inequality, exact product optimality. Endpoint analysis keeps the threshold bounded through both the Neumann and Dirichlet limits. These features give the argument potential use beyond this one optimization problem.

The proof is concise because it uses powerful established rearrangement and Faber--Krahn theorems. That reliance is explicit. The resolution of the full planar question, the nonlinear range in every dimension and parameter uniformity justify submitting the contribution for serious analysis/PDE review at the user's intended level. They do not guarantee a particular journal's judgment or future citations.

## Remaining uncertainty and scope

No independent mathematician has reviewed this manuscript, and no external endorsement is claimed. The assessment can change if a gap or prior result is identified. The main limitations are the linear dimensional restriction, the absence of an optimal exponent, and the fixed strictly positive Robin coefficient. The paper makes no statement for negative coefficients, the Neumann zero eigenvalue itself, arbitrary rough sets, or higher eigenvalues. The geometric asymmetry constant is inherited from prior work and is not asserted uniform in beta. The paper's main deficit equivalence and exponent are uniform.
