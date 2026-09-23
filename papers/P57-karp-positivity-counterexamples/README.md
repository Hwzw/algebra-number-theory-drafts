# Positivity and counterexamples for rising-factorial Toeplitz determinants

**Henry Zweiman** · September 22, 2026 · P57 · Version 1.0

A separate manuscript addressing Karp's 2012 Conjectures 1, 2, 4, 5, and 6. The earlier [Conjecture 3 paper](../P56-karp-rising-factorial-zeros/README.md) remains separate.

| Conjecture | Result |
| --- | --- |
| 1 | Proved for all positive shift parameters. |
| 2 and 5 | Disproved by an exact stability counterexample with a positive strictly log-concave input. |
| 4 | The literal assertion fails for degenerate inputs; a general minor expansion gives coefficient nonnegativity and exact criteria for degree and strict positivity. |
| 6 | Disproved for determinant order three using the degree-eleven binomial sequence. |

- [Complete manuscript](manuscript.md)
- [Nine-page PDF](manuscript.pdf)
- [LaTeX source](manuscript.tex)
- [Exact verification script](checks/verify.py)
- [Exact certificates and results](checks/results.json)
- [Literature and source comparison](LITERATURE.md)
- [Originating-assistant audit](REVIEW.md)
- [Citation metadata](CITATION.cff)

The counterexamples have integer-arithmetic certificates, not merely numerical root estimates. The manuscript develops the general positive expansions explicitly and credits the standard tools used. Historical priority has not been established.

Prepared with OpenAI Codex; not peer reviewed or independently verified by a human expert.

## Reproduce

Run `python3 checks/verify.py` with SymPy installed. Run `python3 build.py` with Pandoc and Tectonic on PATH, or specify their executable paths through `PANDOC` and `TECTONIC`. The build writes `manuscript.tex` and `manuscript.pdf` beside the source.
