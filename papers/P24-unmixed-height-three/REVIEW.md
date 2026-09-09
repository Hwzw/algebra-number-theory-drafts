# Internal proof and reproduction audit

September 9, 2026. Review by the originating agent. No human or separate
agent review is claimed.

## Logical checks

- **Decomposition:** distinct triples give incomparable primes, unique
  isolated irreducible primary components, and no embedded primes.
  Powers of a pure-power component are primary. Thus symbolic powers
  are exactly the intersections of component powers.
- **Localization:** invert variables outside a support union, then
  descend from the Laurent extension by faithful flatness. Exactly the
  components inside that union survive. No exponent changes.
- **Zero specialization:** membership of a monomial in remaining
  variables is unchanged under setting other variables to zero. This
  proves commutation with monomial intersections; ideal powers commute
  under a surjection. The statement explicitly requires all image
  components to be proper nonzero and to have incomparable distinct
  radicals after removing identical duplicates. Both applications
  verify this requirement.
- **Dimension one:** all-power Simis equalities give no embedded primes
  in one-dimensional power quotients, hence depth one at the homogeneous
  maximal ideal. Generic complete intersection and grade at least two
  satisfy Branco Correia–Zarzuela Theorem 6.4 in rank one. The local
  minimal-generator count equals the monomial count. A shared variable
  between two generators would lower the height. The resulting disjoint
  supports in h+1 variables give at most two minimal primes and uniform
  component exponents. This uses all powers, not merely the square.
- **Support reduction:** a discrepancy between two triples cannot
  occur on a two-variable overlap. A single-variable overlap localizes
  to five variables. Any third component containing that variable would
  bridge two overlaps and contradict the discrepancy. Inverting the
  disputed variable leaves at most two extras by dimension-one rigidity.
  Two omitted extra vertices either lie in the same pair or different
  pairs, giving exactly the four cases in the paper.
- **No extras:** the stated monomial belongs to both component squares.
  Contraction to the two-variable subring commutes with monomial powers;
  all three possible generator products fail to divide the witness.
- **One extra:** the indicated zero specialization gives three distinct
  height-two primes on three variables; this contradicts the dimension-one
  bound on the number of primes.
- **Cross-pair extras:** their overlap forces equality of both exponents
  in the duplicated image ideal. Equality of radicals alone would not
  justify deleting a duplicate; the proof checks equality of ideals.
- **Same-pair extras:** three components share two variables, whose
  exponents agree. Their eight-parameter normal form is exactly the
  one in Proposition 6. The two vertex formulas are feasible and are
  uniquely determined by five active linear equations. Both r>1 and
  r<=1, including equality, place the first three coordinates strictly
  below the first component's thresholds.
- **Polyhedral obstruction:** denominator clearing uses the exact
  floor membership test to obtain a monomial in the Nth symbolic power.
  Simis makes it an ordinary-power monomial, proving NP=IP. A vertex
  of NP is a generator exponent, whereas the constructed vertex is
  outside even the first component's exponent orthants. No assertion
  about ordinary powers is inferred from integral-closure equality.
- **Conclusion:** common component exponents commute with the monomial
  intersection under weighting. MPV's prior invariance theorem gives
  the radical's Simis property and the converse.

No unresolved proof step was identified in this internal audit. That
statement is not an independent correctness certificate.

## Exact supplementary calculations

Run `python3 check.py` using only Python's standard library. The output
is recorded in `check-results.json`.

| Check | Count |
|---|---:|
| All nonempty families of triples on five labeled vertices | 1,023 |
| Families satisfying the four-variable at-most-two condition | 252 |
| Potentially discrepant marked component pairs | 165 |
| No-extra / one-extra / same-pair / cross-pair patterns | 15 / 60 / 30 / 60 |
| Rational vertex parameter choices | 2,943 |
| Vertex cases r>1 / r=1 / r<1 | 2,912 / 4 / 27 |
| Explicit two-component symbolic-square witnesses | 792 |

The support checker independently enumerates the finite set system and
checks the image supports and duplicate intersections. The vertex checker
uses exact fractions for feasibility and Gaussian elimination to verify
the active equations determine the displayed vertex. Extra larger
denominators ensure that r<1 is tested. None of these bounded samples
proves the arbitrary-exponent statement; the hand argument does so.

## Artifact checks

The LaTeX compiles to seven pages. Every final page was rendered and
visually inspected. The full Markdown conversion verifies all source
math expressions, theorem and equation references, and a semantic
roundtrip. The math renderer reports zero errors. Hashes and detailed
results are in `artifact-qa.json`, `markdown-conversion.json`,
`markdown-math-check.json`, and `manifest.json`. The GitHub live Markdown
renderer was not separately inspected.
