# Validation and adversarial targets

The main argument is a hand proof. The supplied exact-arithmetic script is supplementary and checks every root-multiplicity vector in four small cases. It uses prime fields q=2,3; prime-power fields are covered only by the general proof, not this script.

Command:

    python3 research_program/candidates/C14-integer-valued-polynomials/check_small_cases.py

Observed results on 2026-09-08:

| q | Exponent vector (a_0,…,a_s) | Numerator vectors checked | Divisor classes | Result |
|---|---|---:|---:|---|
| 2 | (1,1,1) | 48 | 8 | PASS |
| 2 | (2,1,2) | 216 | 18 | PASS |
| 2 | (1,1,1,1) | 2880 | 16 | PASS |
| 3 | (1,1,1) | 2304 | 8 | PASS |

The script checks fixed-divisor compatibility of a numerator and its complementary numerator at every irreducible prime of degree at most s. Higher-degree primes contribute zero because V_s occupies fewer residue classes than the field size. The accepted vectors agree exactly with the exponent boxes predicted by the theorem.

## Required independent checks

1. In Lemma 1, for s=kd+r, every π^k-residue fiber has q^r roots and therefore an unoccupied π^{k+1}-child. The chosen y must satisfy the simultaneous valuation equality for every root, including when k=0 and when x is itself a root.
2. Fixed-divisor additivity must hold for arbitrary nonnegative weights, not just uniform weights. Its role is to show that division by B_s preserves integer-valuedness after all root exponents are known to be at least c.
3. The degree-s prime in Lemma 2 has denominator exponent exactly a_s. Applying inequalities to the complementary factor must force equality on the outer shell.
4. Constants in K and primes absent from the original denominator must remain accounted for. The valuation criterion ranges over all finite primes.
5. The base s=0 handles possible constant factors and arbitrary powers of X.
6. The final theorem must genuinely exceed the prime-power theorem in Tichy–Windisch. The explicit Question 3.1 supplies that comparison; a later unpublished or recently posted solution could still affect priority.

Independent proof review passed: see `research_program/reviews/C14-proof-review.md`. The reviewer independently checked the full proof and primary sources, and ran additional exact computations. Final manuscript signoff is being performed separately.

## Manuscript compilation and visual QA

The complete six-page manuscript was compiled with the workspace's local Tectonic binary, using `--keep-logs`. Its log contains no overfull or underfull boxes, warnings, or undefined references. All six pages of the final PDF were rendered at 1400-pixel scale and visually inspected after the Wagner attribution was added. The text, displayed equations, theorem statements, page numbers, and three references are legible and unclipped; no layout defect was found.

Stable files at this QA pass:

- `manuscript.tex`: SHA256 `a74eba0f334bff2fedba3639cf6090cd705a5344923d0d146d2f04b2a386b5e2`.
- `manuscript.pdf`: SHA256 `2f162727197c3d43e689b22c1623b5709fa9a82687e8a1acdfaeb2fe60de6ddf`.

The final manuscript includes the all-prime criterion, the full arbitrary-exponent divisor theorem, the mixed-index families and exact divisor counts, and a proved contrast with ordinary binomial products in Int(Z). Wagner's earlier residue counts are explicitly credited. No publication-priority guarantee is made.
