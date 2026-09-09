# Internal mathematical review

The originating agent reviewed this manuscript. No separate-agent or
human expert review is claimed.

## Arguments checked

1. The rank-two height estimate uses every relevant place. Real rank
   failure would contradict multiplicative independence or Northcott
   finiteness. Finding a certified nonzero logarithm minor establishes
   effectivity without invoking an effective Northcott theorem.
2. The logarithm inequality retains the varying height of the
   approximant ratio. The field is fixed and contained in the real
   numbers; it need not be totally real. Terms with zero exponents or
   value one can be omitted. Positive algebraic numbers use real logs.
3. A near-integer interval gives an exact integer recurrence. The
   Lagrange projection lies in the parameter field and has logarithmic
   height O(k). The error at the interval endpoint is O(theta^(k-L)).
   The constants do not depend on the interval ratio. Conjugates on the
   unit circle and degree-one parameters are explicitly included.
4. The two floored starting indices are comparable once both underlying
   real quotients exceed twice the fixed cutoff. Their sum is at most
   (e+f)/R^2. Both intervals fit within the actual Fourier-factor ranges.
5. Algebraic rescalings contribute the factor t/s to gamma. The identity
   (t/s) theta^e phi^(-f)=b/a is used; omitting this factor would be wrong.
6. Exact equality Z=1 is excluded before applying the nonzero-logarithm
   estimate. Its height is linear in e+f, whereas the coefficient height
   is O((e+f)/R^2).
7. For Z!=1 the error exponent is proportional to R(k+l), while the
   lower bound costs O((k+l) log E). Choosing R=ceil(H log(E+2)) gives a
   contradiction with a fixed sufficiently large H, uniformly in the
   chosen intervals.
8. Distinct geometric intervals are disjoint under the exact floor
   inequality. There are at least a constant times log E/log log E of
   them. Reversing indices maps them into genuine nonnegative factors.
   Since E is comparable to log u, the claimed iterated logarithms follow.
9. The self-similar corollary uses the exact squared-modulus identity for
   a finite probability sum and two distinct algebraic translations.
   Effectivity for the weights is claimed only for algebraic input.
10. The explicit quartic is Salem: its reciprocal substitution has one
    root greater than two and another in (-2,2), and the quadratic
    discriminant is not a square in Q(sqrt(5)) because it has a negative
    conjugate. Powers preserve the field of a number with a unique
    conjugate outside the unit disk, proving independence from the
    degree-two Pisot parameter.

## Exact diagnostics

`python3 check.py`, with SymPy 1.14.0, passes:

- 5,120 exact trace/projection identities over five quotient algebras,
  including degree one, two Pisot polynomials, and two Salem polynomials;
- 1,500 paired-interval parameter cases and 18,046 disjoint intervals,
  checking floor inequalities, comparability, endpoints, and no overlap.

The implementation constructs multiplication matrices and checks traces
against independently iterated integer recurrences. It does not test the
asymptotic decay numerically. These finite diagnostics are consistency
evidence; the infinite assertion rests on the hand proof and the stated
logarithm theorem. They do not establish historical novelty.

## Document checks

The final five-page PDF was compiled without TeX layout/reference
warnings and all five rendered pages were visually inspected. The full
Markdown conversion and 191 rendered mathematical expressions passed.
Hashes and verification metadata accompany the files.
