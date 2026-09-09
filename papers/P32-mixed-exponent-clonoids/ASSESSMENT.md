# Mathematical scope and priority assessment

Date: September 9, 2026.

## Open question and contribution

The primary statement is Question 60 in Section 7 of Fioravanti, Kompatscher and Rossi, *Clonoids over vector spaces*, [arXiv:2602.04034v1](https://arxiv.org/abs/2602.04034v1). It asks for uniform generation for the group Z/(p^2) direct sum Z/p. The source also states a broader conjecture for all finite abelian p-groups. Its cyclic and elementary abelian cases are already known.

The manuscript proves the proposed bound s+2 for Z/(p^2) direct sum (Z/p)^s, for all primes p and all s>=0, with a lower bound for actual clonoid generation over a finite field target. The s=1 case answers the explicit question. The cyclic s=0 case is included for consistency and credited as known. The result is not a solution of the full finite-module conjecture.

Targeted searches for the exact question, mixed-exponent clonoids, Fourier uniform generation, and C4/C2 or Z4/Z2 cases found no later resolution. The arXiv record still lists the February 2026 v1. This is meaningful primary-source support for the target, not an exhaustive historical-priority certification.

## Proof dependency and original argument

The substantive external input is Kovacs's theorem that the singular-matrix ideal in the finite-field matrix semigroup algebra has a multiplicative identity whenever p is invertible in the coefficient ring. The exact formulation is independently stated in Kuhn, Theorem 2.1. The manuscript derives the required field reconstruction lemma by induction through rank factorizations.

The new proof uses principal congruence characters on a permutation module. Only characters indexed by rank-one matrices can occur away from the torsion locus. Their semisimple and nilpotent forms lead to one or two fixed coordinates. Singular substitutions require a separate zero-character quotient calculation and a correction acting identically on the torsion submodule. Coefficient descent uses a linear retraction of Z[1/p,zeta_p], without dividing by p-1. A Fourier functional proves the sharp lower bound.

The public paper does not depend on the displayed coefficient formula in FKR Theorem 48. Its v1 statement and proof recurrence display different exponents. The finite-field lemma is instead obtained directly from the older Kovacs theorem, which is fully credited.

## Evidence and limitations

The universal proof is written in full. Exact checks compare character projectors against the defining group sum, verify the sandwich and quotient formulas, and test the lower-bound functional, including exhaustive matrices over Z/4 in sizes two and three. These diagnostics are not finite substitutes for an infinite proof.

The result could support further work on mixed-exponent modules and clonoid lattices. The manuscript does not claim an algorithmic complexity theorem, a complete lattice classification, a citation forecast, or a solution for multiple p^2 factors or higher exponent. Independent expert proof review and broader novelty/significance evaluation remain outstanding.
