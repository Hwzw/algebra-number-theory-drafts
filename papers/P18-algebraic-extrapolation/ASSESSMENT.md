# Source and significance assessment

Author: Henry Zweiman. Audit date: September 9, 2026.

## Published questions and the proposed answer

The primary comparison is Fenner, Green, and Homer, [*Fixed-Parameter Extrapolation and Aperiodic Order*](https://link.springer.com/article/10.1007/s00454-025-00816-4), *Discrete & Computational Geometry* 76 (2026), 1–74, published June 11, 2026. Section 11 explicitly poses the following questions.

| Source statement | Proposed resolution in this manuscript |
|---|---|
| Conjecture 11.1: discreteness forces the strong PV property | Theorem 2, using the exact membership theorem and the extended source's algebraic-integrality theorem |
| Question 11.2: equality with the natural model set | Theorem 3: both absolute endpoint values of the minimal polynomial must be at most two |
| Question 11.3: relative density outside the interpolation regime | Corollary 5, from the model-set theorem and the source's topological-closure dichotomy |
| Conjectures 11.4–11.5: finite generation of the natural model set | Theorem 4 for every nondegenerate strong PV parameter, with an explicit seed-cardinality bound |
| Question 11.6: periodicity for nonreal quadratic integers | Theorem 3: a finite union of cosets of the endpoint ideal |

The source's phrase “any strong PV number” requires care in the finite-generation assertion: zero and one satisfy the vacuous conjugate definition but select an input, so no finite seed generates the full integer set. The manuscript states and explains these exceptions.

The earlier [2018 open-problems article](https://mathcs.clarku.edu/~fgreen/papers/sigactopen.pdf), *SIGACT News* 49(3), 35–47, was also inspected for historical context. Exact claim numbering above follows the 2026 publication, not the earlier version.

## What is and is not new

The principal claim is the arbitrary-degree polynomial lifting theorem and the resulting arithmetic classification for every algebraic integer other than zero and one. The classification combines interval inequalities at the internal real embeddings with two finite endpoint congruences. It then yields the stated geometric and generation consequences through one common proof.

Integer approximation with integral endpoint values is classical, attributed to Chlodovsky and Kantorovich. We checked the discussion and Bernstein-rounding estimate in C. S. Güntürk and W. Li, [*Uniform Approximation by Polynomials with Integer Coefficients via the Bernstein Lattice*](https://arxiv.org/abs/2311.10901v1). That theorem, Bernstein positivity, and the existing two-label polynomial characterization are proved in the manuscript for transparency, without novelty claims.

The integer-parameter classification and the four real quadratic equality families are already in Fenner–Green–Homer. Recovering them is a consistency check. The new claim is the all-degree classification, including the congruence coordinate and finite generation. The several consequences do not justify separate paper counts.

## External proof dependencies

The [extended version, arXiv:1212.2889v6](https://arxiv.org/pdf/1212.2889v6), has results omitted from the shorter published presentation. We inspected the exact statement of Theorem 8.2 (printed page 29): discreteness implies algebraic integrality for arbitrary complex parameters. The global classification uses this theorem; its long proof is not independently reproduced here.

The same version's Corollary 3.5 (printed pages 17–18) and Theorem 2.19 (printed page 10) supply the accumulation/convex-closure dichotomy and the ambient interval, real-line, or plane closure. These are used only for the nondiscrete case of relative density. The manuscript proves the lattice and approximation ingredients used in its algebraic-integer results, apart from standard Bernstein approximation and Minkowski's convex body theorem.

## Search boundary and significance

Searches included the exact primary title, author publication records, and combinations of “strong PV,” “discrete,” “classification,” “conjecture,” “extrapolation,” “integer polynomial,” “congruence,” and “quasicrystal addition” with “finite generation.” The 2026 published questions and the 2020 extended statements were checked directly. No later resolution was found in the inspected results as of the audit date. This is a bounded literature search, not a certification that every relevant preprint or equivalent formulation has been excluded.

If correct and new, a classification in all degrees answers a linked group of explicit questions and gives a reusable lifting method connecting integer approximation, algebraic arithmetic, and model sets. Quantitative construction depth and optimal seed size remain natural further problems. The manuscript does not prove optimal complexity, and no future citation count is predicted. Historical priority, correctness, and scholarly importance remain open to expert review.
