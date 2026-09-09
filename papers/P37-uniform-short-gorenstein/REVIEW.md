# Internal proof review

September 9, 2026. The following is an internal audit of the proposed proof. It is not an independent referee report.

## 1. Ring and module reductions

The socle is the one-dimensional degree-two part, so the degree-one multiplication pairing is nonsingular. A module without free summands is annihilated by the socle: a vector not annihilated by it gives an injective copy of the self-injective ring, which splits. Every such module therefore admits the two-layer grading used in the proof. The stronger radical-equals-socle assertion is used only when no simple summand exists.

The reduction to persistent modules is legitimate because a simple summand in any stable shift already puts the residue field in level one. The proof does not assume that every module is persistent.

## 2. Identity of maps under reflection

The first normalized syzygy is computed from the actual graded free cover. For a pairing matrix Q its arrows are Q times the projections from the kernel of the original row map. Under an arrow change g the kernel changes by `g^(-T)`, not by g or its inverse without transpose. Consequently two syzygies give the twist `Q Q^(-T)`, which is the identity because Q is symmetric.

The check program verifies this as an identity on kernel spaces and arrow maps in 288 examples over F2, F3, F5 and F7, and 24 further examples with an invertible alternating matrix over F2. This checks the transpose and characteristic-two issues directly. Diagonalization is neither used nor assumed.

## 3. Growth and bristle quotients

The two eigenvectors of the cosyzygy recurrence have positive coordinates. Positivity of every positive and negative iterate forces nonnegative coefficients, and the irrational slopes exclude zero coefficients. This proves the two-direction growth and the limiting ratio used in the proof.

Maps to a bristle are pairs of linear functionals with at most e*u equations in u+v unknowns. The positive lower bound yields a nonzero map over finite fields as well as infinite ones. Generation in degree zero forces its top map to be nonzero; the one-dimensional top and nonzero bristle arrows then force surjectivity. No generic-rank argument or algebraic-closure descent is needed.

## 4. The uniform step

Ringel's theorem is applied first to fix X, an even shift of M. A basis of bristle eigenvectors fixes h=dim X_0 and a bristle presentation of X. Only then is the distant source Y_n chosen. Every bristle in that fixed presentation is a quotient of Y_n for all sufficiently large n. Thus the number of source copies does not increase with n.

The resulting kernel is at level two since both other terms of the short exact sequence are at level one from M. Assuming that kernel is persistent allows repeated normalized syzygy exactness: at every step the covers are the natural covers of the degree-zero spaces. The resulting epimorphism from M^h to Omega^n X contradicts the chosen dimensions. A zero kernel is excluded by the same argument. This proves that a shift of the kernel contains k.

This step uses no unproved global exactness of syzygy on all modules and no unproved equivalence of a stable category with a Kronecker derived category. It also does not require bristles themselves to be in level one.

## 5. Sharpness and consequences

A bristle has quadratic-form value 2-e<0. Before a first hypothetical simple syzygy in either direction, the minimal-cover/injective-envelope dimension formulas preserve this value, whereas a simple graded vector has value one. Nonprojective indecomposability is preserved by stable syzygy. Hence k cannot be a summand of any finite sum of shifts of that bristle. This proves the lower bound for the dominant index.

Every stable object is an extension of two semisimple modules, yielding level four from any nonzero M. The paper claims the generation-time upper bound only, not realization of every time below it.

The non-coefficient-field corollary uses the earlier common deformation and two regular-element inequalities, giving seven. Both regular parameters must be outside the square of the maximal ideal. The coefficient-ring map need not be injective; the proof explicitly avoids that assumption.

## 6. Concrete witness and artifact checks

For the F2 algebra with Q=I3 and M=B(1,0,0), the program constructs the epimorphism `(Omega^-2 M)^5 -> Omega^2 M` and verifies all three arrow-commutation equations and surjectivity in both degrees. Its kernel has graded dimensions (5,23), radical dimension 15, and eight displayed simple summands. The matrices are recorded in `check-results.json`.

The six-page PDF was compiled without TeX warnings and every final page was visually inspected. Full Markdown includes the Henry Zweiman byline, theorem numbering, formulas, proofs, and references. All 278 Markdown math expressions passed local MathJax parsing. This does not assert a live GitHub renderer test or independently establish the mathematics.
