# Counterexamples to a nullity criterion for matrix power maps

**Henry Zweiman — September 15, 2026**

Complete four-page research manuscript with a proposed negative answer to Saini--Singh Question 6.1. AI-assisted preparation and internal audit; not human peer reviewed. Historical priority and significance remain provisional.

- [PDF](manuscript.pdf)
- [Complete Markdown](manuscript.md)
- [LaTeX source](manuscript.tex)
- [Source and significance assessment](ASSESSMENT.md)
- [Proof audit](REVIEW.md)

For every k>=5, take n=k+1 and B=diag(0,0,1,...,1). The rank-three matrix with ones in positions (2,1), (4,3), and (6,5) is not X^k+B Y^k over any field. Nevertheless, n>k(nullity(B)-1). The first example has n=6 and k=5. The proof treats arbitrary X and Y; it does not infer nonexistence from a finite search.

Over algebraically closed fields of characteristic zero, the image is dense but not closed under addition. No smallest-dimension claim or full replacement classification is made. This is one manuscript, distinct from P33's completion and complementary-coefficient theorem.

Run `python3 q37-counterexample-check.py` for exact finite diagnostics. It uses the Python standard library. The JSON output checks 1,125 functionals in finite-field instances of the forced-chain lemma and 10,977 zero-primary partition cases. These checks do not replace the universal proof.

Compile `manuscript.tex` with a modern LaTeX engine or Tectonic. The complete Markdown was checked against the TeX content and has 170 successfully parsed math expressions. All four final PDF pages were visually inspected.
