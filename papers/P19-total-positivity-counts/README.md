# Paley cliques and nonpolynomial counts of totally positive matrices

**Henry Zweiman — September 9, 2026**

[Full Markdown manuscript](manuscript.md) · [Six-page PDF](manuscript.pdf) · [LaTeX source](manuscript.tex)

This paper gives a proposed negative answer to Conjecture 5.12 of Ayyer–Prasad (2026). It determines the count of totally positive two-by-three matrices over every finite field and shows that, in every prime characteristic congruent to one modulo four, no polynomial formula in the field size holds even eventually on any progression of extension degrees. Six entries is the smallest matrix size permitting such a counterexample.

The proof connects two-row matrices to Paley cliques, uses the existing four-clique formula of Dawsey–McCarthy, and proves that its Gaussian exponential terms cannot disappear under any periodic restriction. The count has a rational generating function and an exact minimal recurrence of order seventeen. This is one consolidated paper; the Paley clique evaluation itself is not new.

The [source assessment](ASSESSMENT.md) and [internal proof audit](REVIEW.md) record the contribution, existing inputs, and review limits. Historical priority and significance remain provisional. No result is claimed for the separate positive-semidefinite conjecture.

## Reproduction

```sh
python3 check.py
```

The standard-library checker uses 29 prime and extension fields, with direct enumeration of the original matrix entries over nine small fields. It also checks the displayed recurrences. See [results](check-results.json). These finite checks support the formulas; the all-progression nonexistence statement is established by the written proof.

Compile the LaTeX source with Tectonic or a compatible LaTeX installation. All six PDF pages were rendered and visually inspected, and the complete Markdown conversion passed local math checks; see [artifact QA](artifact-qa.json) and [hash manifest](manifest.json).
