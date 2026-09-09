# A rigid nonassociative shift-associative algebra in dimension five

**Henry Zweiman. September 9, 2026.**

[Full Markdown](manuscript.md) · [PDF](manuscript.pdf) · [LaTeX](manuscript.tex)

This six-page paper gives a proposed affirmative answer to the explicit rigid-nonassociative existence question after Proposition 64 in Abdelwahab–Kaygorodov–Sartayev, *Shift associative algebras* (2025). A six-product table defines a five-dimensional nilpotent algebra whose orbit is open in the variety of all five-dimensional shift-associative algebras. Five is the minimum possible dimension. Adjoining scalar factors gives rigid nonassociative examples in every higher dimension, within this same paper.

The central finite computation is certified by an explicitly specified integer minor of determinant 2. The full linearized identity has rank 105; its kernel and the change-of-basis orbit each have dimension 20. A second implementation independently reconstructs the symbolic linearization and confirms the exact ranks, determinants, and five-dimensional derivation algebra. The geometric argument and the scalar-factor extension are proved in the manuscript.

[Source and significance assessment](ASSESSMENT.md) · [Internal proof audit](REVIEW.md) · [Exact certificate](check-results.json) · [Independent computation](independent-results.json) · [Artifact manifest](manifest.json)

Reproduce the primary check with Python 3:

```sh
python3 check.py
```

The second check requires SymPy 1.14.0 and reads the certificate indices from `check-results.json`:

```sh
uv run --with sympy==1.14.0 python independent_check.py
```

Compile the TeX with AMS packages, `geometry`, `needspace`, and `hyperref`. The Markdown is a complete conversion, including all proofs and the certificate appendix.

Prepared with OpenAI Codex assistance. The originating agent performed the proof audit and both implementations; this is independent code, not independent human or separate-agent review. Historical priority and scholarly significance remain provisional. Public hosting is not journal acceptance. A full classification of five-dimensional shift-associative algebras is not claimed.
