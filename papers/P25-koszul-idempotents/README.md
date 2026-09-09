# Primitive idempotents that cannot be homogenized in Koszul algebras

**Author:** Henry Zweiman. **Date:** September 9, 2026.

[Full Markdown paper](manuscript.md) · [PDF](manuscript.pdf) · [LaTeX](manuscript.tex)

This paper gives an explicit proposed negative answer to Dramburg's Question 6.2, including over the complex numbers. The algebra is a matrix algebra over a two-dimensional quadratic complete-intersection domain and is Koszul. In that same algebra, primitive idempotents can agree with a homogeneous idempotent to arbitrarily high finite order while no algebra automorphism makes them homogeneous. Conjugacy holds after completion.

The construction works over every field: matrix size two outside characteristic two, and size three in characteristic two. These are cases of one paper.

The matrix/projective-module method and Picard obstruction are classical. The paper credits Petersson, Kanwar--Leroy--Matczuk and de Jong, and distinguishes their examples from the simultaneous grading and split-center hypotheses here. See [assessment](ASSESSMENT.md) and [proof review](REVIEW.md). Internal verification is not outside peer review, and historical priority and significance remain provisional.

Run `python3 check.py` to reproduce the exact certificate checks using only Python's standard library. They check the displayed identities in the integer polynomial quotient, the formal intertwiner, initial degrees, monomial descriptions, and characteristic boundaries. The universal argument is in the paper, not inferred from finite cases.
