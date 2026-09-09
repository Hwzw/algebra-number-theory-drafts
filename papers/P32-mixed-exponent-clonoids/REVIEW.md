# Internal proof and artifact review

This is an internal review, not an independent referee report.

## Logical checks

1. **Actual source operations.** Matrices over Z/(p^2) act simultaneously on both factors. All elementary-factor actions are reductions of the same matrices. No independent factor projection is assumed to be a term operation.
2. **Inner rank.** The operator span of matrices factoring through k variables is a two-sided ideal. Every lifted field matrix is lifted via its factors, preserving the claimed inner-rank bound.
3. **Field input.** Kovacs's singular-ideal unit works over a commutative ring with p invertible. It fixes each rectangular-matrix basis vector via a singular projection. Induction through rank factorizations gives the exact rank-d field identity used later.
4. **Characters.** The stabilizer of a nonzero residue a is H a=0, whose trace annihilator consists of a b^t. Thus no higher-rank character contributes. Zero residue contributes only the trivial character.
5. **Conjugation.** Rank-one matrices have the two stated normal forms. Every field change of basis lifts invertibly to Z/(p^2), and conjugation preserves the operator ideal.
6. **Sandwich identity.** On the displayed Fourier basis, the block substitution fixes the chosen lift of c e1 exactly, and its distinguished row is fixed modulo p. The two character phases cancel even when the remaining block is singular.
7. **Zero character.** The p-torsion submodule is invariant. The compressed action on the quotient averages all nonzero-residue lifts and sends zero-residue outputs into the discarded submodule. It does not silently identify the full zero-character image with a field representation.
8. **Correction.** B0 is identity on the torsion submodule and (Id-J)V lies there, so Id=J+B0(Id-J). Every term remains in the claimed ideal.
9. **Descent.** The coefficient-of-1 map on the cyclotomic free basis is D-linear and fixes 1. It may be applied after expanding the operator identity because the substitution matrices have integer entries. Multiplicativity of this retraction is not needed.
10. **Sharpness.** The functional annihilates every forbidden-rank substitution of the explicit function. A nonzero character sum would force a nonsingular reduction. Linear combinations and arbitrary clonoid compositions still factor as asserted, so this is a lower bound for actual generation, not only for uniform identities.
11. **Boundary cases.** The case s=0 uses the singleton field identity; n<=s+2 is immediate. The prime p=2 needs no exceptional argument. The finite target field can always be chosen to contain a primitive pth root.

## Exact diagnostics

- 120 comparisons with the full defining congruence-group sum, also checking projector idempotence.
- 192 nonzero-character sandwich checks, including singular blocks and factor-preserving lifts.
- 180 zero-character quotient checks with carry terms.
- Exhaustive lower-functional checks over all 256 size-two and 262144 size-three matrices over Z/4, testing every matrix with singular reduction.
- One lift for all 19683 size-three residue matrices over F3; additional documented cases for s=2 and p=5.

All checks use exact modular arithmetic and passed. Universal validity follows from the proof, not these finite tests. No further runtime or algorithmic complexity claim is inferred from them.

## Artifact checks

The six-page PDF was compiled without TeX warnings and all six rendered pages were visually inspected. Full Markdown passed semantic conversion, and all 294 math expressions passed the renderer check. Live GitHub math rendering was not inspected. Download integrity is verified separately after publication.
