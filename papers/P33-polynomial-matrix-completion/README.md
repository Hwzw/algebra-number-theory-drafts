# Sharp completion bounds for polynomial values of matrices

**Henry Zweiman — September 9, 2026**

A complete six-page manuscript with a full Markdown edition and reproducible exact checks. This is an internally checked proposed result, not an independently certified solution or a peer-reviewed publication.

For an algebraically closed field of characteristic zero, let E(f) be the maximum, over values lambda, of the minimum multiplicity of a root of f(t)-lambda. The manuscript proves that every prescription of r rows of an n by n matrix extends to f(X) exactly when n > E(f)(r-1). It classifies surjectivity and image linearity for sums A_i f_i(X_i) when the coefficient column spaces form a direct sum. For complementary A and B, AX^k+BY^l is surjective exactly when n > k(rank A-1) and n > l(rank B-1).

The broad source question is Gangwal--Mandal--Verma Question 1.1. The overlapping-coefficient problem, including Saini--Singh Question 6.1, remains unresolved here. The existing nilpotent obstruction and classical Kronecker decomposition are credited.

- [Full Markdown manuscript](manuscript.md)
- [PDF manuscript](manuscript.pdf)
- [LaTeX source](manuscript.tex)
- [Scope and priority assessment](ASSESSMENT.md)
- [Proof review](REVIEW.md)
- [Exact check program](check.py) and [results](check-results.json)
- [File manifest](manifest.json)

Run `python3 check.py` with Python 3.8 or later. The program uses only the standard library. Its finite checks support the written proof; they do not establish an infinite theorem by enumeration.
