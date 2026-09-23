# Negative real zeros of a rising-factorial transform

**Henry Zweiman** · September 22, 2026 · P56 · Version 1.0

A proof of the coefficient-pairing assertion for rising factorials, together with its extension to the positive-endpoint form of Karp's 2012 Conjecture 3. The manuscript proves the needed factorial-transform lemma by interlacing and treats zero endpoints separately.

- [Read the complete proof](manuscript.md)
- [Typeset PDF](manuscript.pdf)
- [LaTeX source](manuscript.tex)
- [Exact algebra and sample checks](checks/verify.py)
- [Verification results](checks/results.json)
- [Scope and source assessment](ASSESSMENT.md)
- [Proof audit](REVIEW.md)
- [Citation metadata](CITATION.cff)

For Karp's strictly negative-zero conclusion, the theorem assumes $f_0f_n>0$. General finite $PF_\infty$ inputs yield a zero polynomial or real nonpositive zeros; $12x(x+1)$ is an explicit boundary example.

Prepared with OpenAI Codex. Not peer reviewed or independently verified by a human expert. No priority determination is claimed.

Run `python3 checks/verify.py` with SymPy installed. Run `python3 build.py` with Pandoc and Tectonic on PATH to regenerate the LaTeX and PDF from the Markdown manuscript.
