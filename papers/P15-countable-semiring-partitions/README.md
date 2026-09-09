# Countable semiring partitions of real function fields

**Henry Zweiman. September 8, 2026.**

[Full manuscript (Markdown)](manuscript.md) · [PDF](manuscript.pdf) · [LaTeX](manuscript.tex)

The paper gives a complete proposed affirmative answer to the countable-decomposition question in Kiss–Somlai–Terpai, *Journal of Algebra* 664 (2025), Section 7, pp. 530–531. For every real transcendental alpha, it partitions the positive elements of Q(alpha) into countably infinitely many nonempty sets closed under addition and multiplication. A second theorem extends existence to every finitely generated transcendental subfield of the real numbers.

The construction records the positive interval containing the evaluation point and distinguishes zeros from poles at its endpoints. The direct rational-function proof is elementary. The extension uses smooth projective curves. This is one consolidated paper, including its polynomial, rational-function, and curve versions.

[Proof audit](REVIEW.md) · [Source and significance assessment](ASSESSMENT.md) · [Exact checks](check-results.json) · [Artifact manifest](manifest.json)

Prepared with OpenAI Codex assistance. The originating agent performed the internal proof audit; no independent human or separate-agent review is claimed. The source search found no later resolution among the inspected results, which does not certify historical priority. GitHub hosting is not journal acceptance. The finite-partition conjecture remains unresolved in this project.

To reproduce the optional exact checks, use Python 3 with SymPy 1.14.0:

```sh
uv run --with sympy==1.14.0 python check.py
```

Compile `manuscript.tex` with a LaTeX engine supporting AMS packages, `needspace`, and `hyperref`. The numerical checks use Sturm root counts and rational arithmetic. They test examples and do not establish the general theorem or the curve extension.
