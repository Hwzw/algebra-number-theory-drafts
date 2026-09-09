# Internal proof and artifact review

Date: 2026-09-09. Review by the originating agent; no independent human or separate-agent review is claimed.

## Proof obligations

| Obligation | Argument checked | Result |
|---|---|---|
| Closure and boundary | The zero-weight equation is `u=2v+5w`; the two boundary generators are independent. A boundary times a conductor element stays in the conductor. | Pass |
| Mori, without finite-generation assumptions | Four coordinate-minimum witnesses, one adjacent-layer witness, and one weight witness give equality of full quotient-group colon sets. The finite-witness property implies ACC on divisorial ideals. | Pass |
| Quotient group | Ratios of the five stated conductor elements generate all four ambient primes. | Pass |
| Complete integral closure | The conductor element certifies every nonnegative vector; a negative coordinate contradicts almost integrality as powers increase. | Pass |
| Exact conductor | The conductor ideal is included; every boundary element fails after multiplication by `x`. | Pass |
| Weak-C scope | The current source's two conditions are reproduced. Equality on a finite prime set and parameter one verify the class condition. No local-tameness hypothesis is silently removed. | Pass |
| Full atom list | Boundary atoms are the two free generators. Degrees two and three exclude a two-conductor-factor split; boundary divisibility gives the remaining conditions. Degree at least four always splits. | Pass |
| First-layer lengths | Fix the number of the second boundary generator, maximize the first, and impose maximality of the second. This gives the exact two cutoffs, including negative floor values, zero capacities, and singleton ranges. | Pass |
| Higher layers | Each leftover monomial splits into an `a` part and a `b,c` part, both boundary-free. Every count of at least two conductor atoms is thus available, and the resulting intervals join without a gap. | Pass |
| Finite distance set | The first-layer function decreases by one or two, with a possible initial repeat. Other lengths are intervals or singletons; an explicit example contains both distances. | Pass |
| Ray formula | The endpoint at packing count zero differs from the later floor formula. Odd and even positive packing counts produce exactly the two residue classes stated. | Pass |
| Every bounded choice of period | A core interval of length at least `d+3` inside the two-residue portion forces `3` to divide `d`. The terminal point's globally permitted residue then forces a missing core point. This yields the linear bound and rules out every finite difference set. | Pass |

The crucial distinction is between a finite exceptional tail with arbitrary residues and a standard AAMP tail. The proof uses the latter's explicit global residue containment, rechecked against the cited primary source.

## Independent finite computations

`check.py` uses only the Python standard library and verifies:

- 1,575 exponent vectors for the atom characterization using direct nontrivial decompositions;
- 1,132 complete factorization-length sets in the same finite box using the independently found atoms;
- 6,150 first-layer formulas against exhaustive two-generator packing enumeration;
- 100 members of the explicit ray against exhaustive packings;
- 1,600 pairs of ray index and prescribed AAMP difference using an exact minimum-bound calculation.

All passed. These are finite tests supporting hand proofs; they do not replace the Mori argument or the proof that bounds diverge. The earlier isl and Z3 investigation of another weight family is not a dependency of this manuscript.

## Remaining external evaluation

The source-level open statement and defining hypotheses were checked, but priority, correctness and significance have not been certified by a human expert or a journal. The strongest remaining audit question is whether the cited problem intended extra hypotheses beyond its literal reference to Definition 5.1. The manuscript states its interpretation and does not claim the stronger variants.
