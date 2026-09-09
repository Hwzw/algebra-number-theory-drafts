# Internal proof audit

September 9, 2026. Reviewed by the originating Codex agent. No separate-agent or human referee review is claimed.

## Proof obligations checked

1. **Definition and normalization.** Positivity means a nonzero square, including in characteristic two. All minors retain natural index order. Writing column i as a_i times (1,r_i) preserves positivity exactly and gives s^n choices of the first row. This establishes the normalization without assuming row reorderings preserve minors in odd characteristic.

2. **Clique factors.** For q congruent to one modulo four, minus one is a square, so the difference condition is symmetric. The tuple (0,r_1,...,r_n) is an ordered clique. An unordered clique has (n+1)! orderings, and translation distributes ordered cliques equally among q possible first vertices. For n=3, these factors combine with the existing clique denominator to give 512 in the matrix formula. The reduction is also checked against a separate two-parameter normalization fixing the first column.

3. **Directed case.** For q congruent to three modulo four, the local Paley tournament on the positive elements is regular of degree (q−3)/4. The character-sum proof accounts explicitly for excluded arguments zero and one and the sign of minus one. Counting transitive triples by their unique source gives N times binomial(d,2), without an extra ordering factor. The small cases q=3 and q=7 yield zero as required.

4. **Known input and Gaussian primitivity.** Dawsey–McCarthy Corollary 2.3 was inspected with its prime-power hypotheses. For p congruent to one modulo four, powers of a Gaussian prime give the required even imaginary coordinate. Reduction of twice the real coordinate modulo that Gaussian prime proves p does not divide the real coordinate. The arbitrary nonprimitive sum-of-squares representation is not substituted into the source theorem. For an inert prime and even extension degree, the source permits zero imaginary coordinate.

5. **No polynomial branch.** The exact count expands into seventeen nonzero exponential terms. All seven polynomial coefficients were expanded and checked. Gaussian unique factorization proves that the two relevant phase quotients are not roots of unity. Absolute values separate different exponents, and the nontorsion result rules out every remaining collision after raising bases to an arbitrary positive power. Restricting to any progression multiplies coefficients by nonzero constants. Vandermonde independence then rules out eventual equality with a polynomial, of any degree. This is not an inference from a failed finite interpolation.

6. **Minimal recurrence.** The product of the seventeen distinct factors annihilates the sequence. Conversely any annihilating polynomial must vanish at every base because all coefficients are nonzero. Pairing conjugates gives the displayed integer polynomial of degree seventeen. The noncollision argument applies on each progression, so its order does not decrease there.

7. **Smallest size and scope.** Fewer than six entries means one row, one column, or a two-by-two matrix. Their formulas are polynomial in each characteristic, with at most a parity split in the last case. Transposition preserves the relevant minors. This proves minimality by entry count, without claiming that every larger size fails or that the semidefinite conjecture is resolved.

## Checks and artifacts

The checker constructs quotient-field arithmetic and verifies that every nonzero element has a multiplicative inverse via exponent q−1. It evaluates the elementary two-parameter matrix condition over 29 fields, including eleven extension fields. Over fields of order at most 49 it also counts the three-ratio normalization. Over nine fields of order at most 13 it enumerates all six original entries and tests the three determinants directly, examining 185,550 matrices in total. All methods agree with the formulas.

Exact recurrence checks cover four split primes and 23 shifts for each order-seventeen recurrence, together with 39 trace-recursion checks per prime. These finite checks do not prove minimality or the infinite no-polynomial assertion; the written arguments do.

The complete six-page PDF was rendered at 100 dpi and every page was visually inspected. No clipping or overlapping text was observed. Full Markdown conversion verified 187 source math expressions; all 194 resulting math expressions passed the local renderer. Live GitHub Markdown rendering was not separately inspected.

## Decision

No missing step was identified in the internally reviewed proofs of the stated results. Publish as one complete proposed resolution with explicit attribution to the known clique formula. Historical priority and scholarly significance remain provisional, and the collection-wide count of qualifying significant solutions is not certified by this audit.
