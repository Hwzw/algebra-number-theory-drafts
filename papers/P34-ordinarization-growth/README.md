# Quasipolynomiality and collision asymptotics for ordinarization counts

**Henry Zweiman** · September 16, 2026 · P34 · revision 1.2

[Full manuscript (Markdown)](manuscript.md) · [PDF](manuscript.pdf) · [LaTeX](manuscript.tex)

The 13-page manuscript proves exact quasipolynomiality at every positive genus for fixed ordinarization number, evaluates the leading and complete second coefficients, and proves eventual strict growth for each fixed positive ordinarization number.

Revision 1.2 adds a limit with growing ordinarization number: if r tends to infinity, r^2/g tends to zero, and r^3/g tends to tau, the normalized count n(g,r)/(A_r g^(2r)) tends to exp(-tau/2). The proof combines bounds for all configurations outside the bulk with a Poisson law for forbidden holes inside it. At infinite tau the conclusion is an additive, not a relative exponential, approximation.

The full all-genus monotonicity and Bras-Amorós Fibonacci conjectures remain open. The theorem does not reach r proportional to g or provide an error rate that determines consecutive differences. This revision does not complete the broader significant-conjecture goal. These results form one paper.

The proof has been internally audited by the originating AI agent. There has been no independent review. Public hosting is not peer review. See [the assessment](ASSESSMENT.md), [the current proof review](uniform-review.md), and [the historical reviews](REVIEW.md).

## Reproduction

Run `python3 check.py`, `python3 check_second.py`, and `python3 check_uniform.py` with standard-library Python 3. Their saved outputs distinguish exact finite diagnostics from universal hand proofs. Compile `manuscript.tex` with Tectonic or a LaTeX installation containing the standard AMS and hyperref packages.

The full Markdown preserves theorem and equation references; conversion, local math-validation, and PDF review records are included. File hashes appear in [manifest.json](manifest.json) and [SHA256SUMS.txt](SHA256SUMS.txt).
