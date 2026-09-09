# Internal proof and artifact review

Date: September 9, 2026. This is an AI-assisted internal review, not independent human peer review.

## Proof obligations

1. **Coefficient map.** Stacks Tag 032A supplies a complete coefficient Cohen DVR mapping to the Artinian ring and inducing its residue field, including imperfect residue fields. No injective map into the Artinian ring is assumed.
2. **Associativity.** The lifted algebra is a free module with a unit, a degree-one part, and a degree-two part. Every product of three positive-degree basis elements vanishes, so arbitrary symmetric coefficient lifts are associative.
3. **Locality and completeness.** The nilpotent ideal J has cube zero and quotient V. The maximal ideal is pT+J. Its topology agrees with the p-adic topology; finite freeness over V gives completeness, dimension one and a regular parameter p.
4. **Surjectivity.** The map to R is shown surjective by successive approximation in the three finite filtration layers. It is not inferred just from the number of generators.
5. **Kernel and regularity.** Bases are adapted to p, using X1 if p has nonzero degree-one class and Z1 if p lies in the square. Multiplication by p-a is invertible after inverting p, and has determinant p^length(R). DVR length comparison proves the quotient is exactly R.
6. **Linear-parameter hypothesis.** Projection to V takes both p and p-a to p, while the square of the maximal ideal maps into p^2V. This verifies the hypothesis needed for the converse direction of Takahashi Theorem 5.6.
7. **Gorenstein application.** The socle multiplication pairing on the graded ring is nonsingular. The number of independent quadratic relations excludes the complete-intersection case. Kimura's theorem then applies with its exact hypotheses.
8. **Positive dimension.** Linear minimal reductions over infinite residue fields preserve embedding codimension as the embedding dimension of the quotient. The length inequality forces cube zero. Non-CI and Gorenstein properties persist across the regular sequence.
9. **Finite fields.** R[t] localized at mR[t] preserves Hilbert layers, dimension, multiplicity, Gorensteinness and the non-CI condition. Liu Theorem 3.8 applies to this faithfully flat local map.
10. **Uniform bounds.** Takahashi Theorem 6.2 gives two successive bounds of the form 2 dx+1, yielding 4 dx+3. No passage from dominance to uniform dominance is made.

## Exact computational checks

`python3 check.py` uses only the standard library. It covers all nonzero scalar symmetric quadratic tensors on F2^3 and all surjective quadratic tensors Sym^2(F2^2)->F2^2, each in both positions of p. It also includes reproducibly sampled F3 tensors and square-zero examples.

All 258 quotient cases pass: 16,860 elements are enumerated, and 31,698 integral basis associativity identities are checked. The ring relation lattice is checked for stability under multiplication. Hilbert layers, socles, cube-zero multiplication, characteristic, and the position of p agree with the construction. There are 86 Gorenstein and 172 non-Gorenstein cases, in characteristics 4, 8, 9, and 27. This does not test all rings, all residue fields, or categorical dominance computationally.

## Artifact checks

The six-page PDF compiled without TeX warnings. All six rendered pages were individually inspected for clipping, overlap and glyph defects. The full Markdown contains the byline, all theorem and proof environments, equations and references. All 277 Markdown math expressions pass the syntax check. The public manifest records the exact delivered file hashes.

## Outstanding outside review

An expert should assess the universal lifting lemma, the priority of the common-deformation construction, and the novelty and value of the categorical application relative to the recent Kimura preprint. The paper has not been peer reviewed or accepted by a journal.
