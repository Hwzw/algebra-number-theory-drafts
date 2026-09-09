# Source and significance assessment

September 9, 2026. Author: Henry Zweiman.

## Explicit open statement

Ayyer and Prasad, [*Positive definite, positive semidefinite and totally positive matrices over finite fields*](https://arxiv.org/abs/2608.17702v1), Conjecture 5.12, propose polynomial formulas in the field size on residue classes of the extension degree, for each fixed characteristic and fixed matrix size. We inspected Definition 5.1, Proposition 5.2, the small-size formulas in Section 5.1, and the exact conjecture. Their preprint was submitted August 18, 2026; no journal publication is assumed.

The manuscript gives an infinite-family obstruction in the exact fixed-characteristic sense of the conjecture. The first example is characteristic five in size two by three. It also proves the full characteristic classification in this size and the minimality of six matrix entries. It does not address their separate Conjecture 4.31 concerning positive semidefinite matrices.

## Closest existing result

The decisive input is Dawsey and McCarthy, [*Generalized Paley graphs and their complete subgraphs of orders three and four*](https://arxiv.org/abs/2006.14716), *Research in the Mathematical Sciences* 8, article 18 (2021), Corollary 2.3. The exact statement was read on page 3 of the [author PDF](https://www.math.ttu.edu/~mccarthy/publications/GeneralizedPaley.pdf). It applies to prime powers congruent to one modulo four, with an even imaginary coordinate in the sum-of-two-squares representation and a primitivity condition for split primes. This clique formula is existing work and is explicitly credited throughout the manuscript.

Gallo–Videla, arXiv:2303.04312v1, Proposition 4.1 and Theorem 4.3, were also inspected as a comparison for the extension-field recurrence. Their displayed imaginary-part identity has a factor-of-two inconsistency; our notation instead uses the unambiguous identity u_k = pi^(2k) + conjugate(pi)^(2k). The paper relies on the earlier Dawsey–McCarthy formula, not the ambiguous transcription.

## What the new claim adds

The normalization of two-row total positivity turns its count into a clique count, including the exact ordering and translation factors. This exposes a mismatch between rational generating functions and polynomial formulas on extension-degree progressions. The manuscript proves that the Gaussian terms survive every such progression, determines all characteristics where polynomial branches do hold in this size, and gives the exact minimal recurrence.

The contribution is a structural correction to a recent explicit conjecture, with a reusable connection between finite-field matrix positivity and Paley graphs. It is not a new evaluation of character sums or a solution of the general Paley clique problem. The proof is shorter once the correct existing input is identified; difficulty is not exaggerated. The significance is narrower than a universal classification of total positivity in all dimensions. It merits evaluation as a focused research contribution; no citation-count prediction or expert endorsement is claimed.

## Search boundary

Searches combined the exact 2026 preprint identifier and title with “counterexample,” “Paley,” “quasipolynomial,” and “5.12,” and checked the relevant clique-count literature. No prior statement of this matrix-count obstruction was found in the inspected results. This bounded search does not certify historical priority.

An initial route through characteristic-two matrices and projective arcs was abandoned as a proof route because the available non-quasipolynomial arc statement does not directly establish failure in the fixed characteristic required here. The manuscript uses a different, fully specified prime-tower argument. This prevents importing a weaker result as a stronger conclusion.

The all-field count, nonpolynomiality, minimal matrix size, and recurrence form one paper. Public hosting and internal AI verification remain distinct from human peer review and confirmed novelty.
