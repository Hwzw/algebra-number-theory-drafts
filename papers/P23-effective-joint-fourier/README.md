# Effective joint Fourier decay at independent Pisot and Salem scales

**Henry Zweiman**, September 9, 2026. Proposed research preprint, five pages.

[Full Markdown](manuscript.md) · [PDF](manuscript.pdf) · [LaTeX](manuscript.tex)

The manuscript proves a proposed effective bound of
`exp(-c log log u / log log log u)` for two Fourier products at independent
Pisot or Salem parameters, allowing positive algebraic rescalings. A
combined fractional-part estimate supplies the proof and extends the
bound to convolutions of homogeneous self-similar measures with algebraic
translations. An explicit mixed Pisot–Salem example is included.

The qualitative Pisot product criterion is classical. This paper does
not claim to solve it for the first time, nor to improve the decay of a
single Salem factor. The quantitative target was formulated in this
research program; no independently verified prior open-problem statement
for this exact bound has been located. See the [source assessment](ASSESSMENT.md).

The [proof review](REVIEW.md) records the arguments and exact finite
diagnostics. To run the latter, use Python with SymPy 1.14:

```sh
python3 check.py
```

These are AI-generated proposed results. The originating agent performed
the review; no human or separate-agent verification is claimed. Novelty,
significance, and journal readiness remain provisional. The related
results comprise one manuscript, not several papers counted by theorem.
