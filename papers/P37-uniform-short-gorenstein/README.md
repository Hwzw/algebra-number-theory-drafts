# P37: Uniform dominance of short Gorenstein algebras

**Henry Zweiman — September 9, 2026**

This six-page manuscript proposes the sharp equality `dx(R)=1` for every commutative graded Artinian Gorenstein algebra with Hilbert function `(1,e,1)`, `e>=3`, over any field. Every nonzero stable object therefore generates the residue field in one cone, and the whole stable category in at most three extensions.

- [Full Markdown paper](manuscript.md)
- [PDF paper](manuscript.pdf)
- [LaTeX source](manuscript.tex)
- [Source and significance assessment](ASSESSMENT.md)
- [Internal proof review](REVIEW.md)
- [Exact check program](check.py) and [results](check-results.json)

The proof uses Ringel's existing eventual bristle-generation theorem. Its new step combines this theorem with a syzygy/reflection identity and epimorphisms from distant cosyzygies to produce a single cone between sums of shifts of the original module. Kimura's qualitative dominance theorem is credited as prior work. P36's common deformation gives the corollary `dx(R)<=7` for arbitrary short Gorenstein local rings without a coefficient field.

Takahashi's global Question 6.12 is **not** settled: the result proves uniformity for the specified class. The exact Orlov spectrum and sharp mixed-characteristic bound remain open in this manuscript.

The checks cover 312 finite-field reflection identities, including alternating pairings in characteristic two, and an explicit cone whose kernel has eight simple summands. They do not prove the general theorem or certify novelty. Run `python3 check.py` to regenerate the results.

**Status:** AI-generated research manuscript, internally checked but not independently peer reviewed. Correctness, historical priority, significance, and journal suitability remain subject to outside assessment. This is one manuscript; the earlier polynomial and logarithmic auxiliary bounds are not separate papers.
