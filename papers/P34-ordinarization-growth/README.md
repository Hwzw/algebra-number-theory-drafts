# Quasipolynomiality and eventual growth at fixed ordinarization number

**Henry Zweiman** · September 9, 2026 · P34

[Full manuscript (Markdown)](manuscript.md) · [PDF](manuscript.pdf) · [LaTeX](manuscript.tex)

This six-page manuscript proposes an affirmative answer to Cyrusian and Kaplan's Remark 3.7: for every fixed positive ordinarization number, the semigroup count is quasipolynomial at every positive genus. It gives a uniform leading coefficient, the exact period-two oscillation of the next coefficient, and positive parity-dependent leading terms for consecutive differences. These imply eventual strict growth for every fixed positive ordinarization number.

The full monotonicity conjecture at every genus remains open. The threshold is not uniform in a growing ordinarization number. These theorems form one paper.

The proof and finite diagnostics have been internally checked by the originating AI agent. There has been no independent human or separate-agent review. Historical priority, significance, and journal readiness are provisional; public hosting is not peer review. See the [source and significance assessment](ASSESSMENT.md) and [internal proof review](REVIEW.md).

## Reproduction

Run `python3 check.py` with standard-library Python 3. The script writes `check-results.json`; runtime is machine-dependent. Compile `manuscript.tex` with Tectonic or a current LaTeX installation containing the standard AMS and hyperref packages. The full Markdown conversion preserves the theorem and equation references; its conversion and math-validation records are included.

The checks cover exact tuple closure, exceptional additive relations, independently generated semigroup trees, known small-ordinarization formulas, and exact rational bulk interpolation. Finite checks are diagnostic evidence and do not prove the universal assertions. File hashes appear in [manifest.json](manifest.json).
