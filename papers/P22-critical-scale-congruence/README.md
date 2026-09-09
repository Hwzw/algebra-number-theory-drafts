# Critical-scale growth bounds for congruence-preserving functions over finite fields

**Henry Zweiman — September 9, 2026**

[Complete Markdown paper](manuscript.md) · [PDF](manuscript.pdf) · [LaTeX source](manuscript.tex)

This seven-page manuscript proposes an improvement of the Bell–Nguyen growth theorem for functions on F_q[t] preserving congruences modulo every irreducible polynomial. The sufficient bound is increased from q^n/(27qn) to a fixed positive multiple of q^n. The simple explicit bound q^n/(256q^2) suffices for every prime power q.

The argument uses classical integer-valued Carlitz digit polynomials with a squarefree primorial factor in the auxiliary-polynomial method. The final rationality theorem is due to Bell and Nguyen. The same paper gives the sharp threshold q/(q−1) for F_q-linear functions, a boundary example, and a general Newton-coefficient description.

**Scope:** The sharp arbitrary-function version of Bell–Nguyen Question 4.1 remains unresolved. The paper answers the growth-scale enlargement problem preceding that question. Its related theorems and examples are one paper.

The [source assessment](ASSESSMENT.md) identifies the exact source version, earlier interpolation results, and the remaining journal-version access limitation. The [proof review](REVIEW.md) records internal verification. These are proposed research results; historical priority, significance, and correctness have not been certified by independent human peer review.

Run the exact checks with Python 3, using only its standard library:

```sh
python3 check.py
```

[Recorded results](check-results.json) include 8,570 digit-basis values, 2,863 additive-basis values, general Newton tests in four finite fields, and exact parameter inequalities. Finite checks support the hand proofs; they do not prove an infinite theorem. [Artifact QA](artifact-qa.json) and [file hashes](manifest.json) identify the reviewed versions.
