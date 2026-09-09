# Complement transfer and density bounds for one-sided restricted sumsets

**Henry Zweiman. September 9, 2026.**

[Full Markdown](manuscript.md) · [PDF](manuscript.pdf) · [LaTeX](manuscript.tex)

This six-page paper gives a proposed affirmative answer to the existence-of-an-absolute-linear-coefficient question immediately before Conjecture 1.13 in Ouyang's revised 2025 paper. It proves the degree-one restricted-sumset bound under the original boundary `|A|+2|B|<=p` when `|B|<=cp`, with explicit `c=3520^(-145200)/206`. A companion theorem gives a logarithmic bound with a better threshold for some fixed column counts.

The proof combines a complement transfer, deletion of unique-representation endpoints, a published inverse theorem, and rectification. The sharp conjecture with no sparsity restriction on B remains unresolved. The constant is extremely small and not optimized.

[Internal proof audit](REVIEW.md) · [Source and significance assessment](ASSESSMENT.md) · [Auxiliary checks](check-results.json) · [Artifact manifest](manifest.json)

The qualitative existence result is already a short consequence of the transfer and Ouyang's theorem; the manuscript states this explicitly. The new explicit bound and the logarithmic variant are part of one paper. P10 in the collection concerns a different conjecture, over the integers at larger degrees, and is not used in this proof.

Prepared with OpenAI Codex assistance. Review was performed by the originating agent, without a separate agent or human referee. Historical priority and scholarly significance remain provisional. Public hosting is not journal acceptance.

The optional exact checks need only Python 3:

```sh
python3 check.py
```

They check finite instances of the transfer and interval-boundary identities. They are not a substitute for the general proof. Compile the TeX with AMS packages, `geometry`, `needspace`, and `hyperref`.
