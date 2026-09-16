# Sharp total variation bounds from spherical rearrangement

**Henry Zweiman. September 16, 2026. Revision 1.13.**

This preprint proves the all-order Hilbert-space case of the Nazarov-Shcheglova variation conjecture, including the exact constant and all extremizers. A Jacobi expansion turns the constrained Green form into a positive mixture of spherical Poisson interactions. A complementary measure argument proves the constant identity and coincidence of maximizing sets at p=1.

Revision 1.1 proves the identity and complete midpoint-symmetric extremizer classification for every p in an order-dependent open interval around two. Section 6 obtains convergence of maximizers through the highest derivative, proves persistence of their single peak, and controls the evaluation profile using polynomial sublevel estimates. The interval is not explicit and need not be uniform in the derivative order.

Revision 1.2 settles the fourth-order measure endpoint: C(4,1)=1/1296 and V(4,1)=1/648, with a unique normalized extremizing measure up to sign. Its five knots are 0, 1/6, 1/2, 5/6 and 1. Section 7 gives a complete alternation and polynomial-elimination proof, including symmetry and nonattainment in the ordinary Sobolev class.

Revision 1.3 proves that the optimal point-evaluation profile has its unique maximum at the midpoint for every derivative order. Its proof follows the alternating contacts, establishes that their velocities are strictly less than one, and applies credited B-spline peak monotonicity with an explicit endpoint extension. This gives the unique symmetric norm-one measure extremizer up to sign and rules out ordinary endpoint attainment in every order.

Revision 1.4 proves strict midpoint point-evaluation maximization and unique symmetric height extremizers for every finite exponent, in every order. Section 9 integrates a one-knot spline against a positive weight and bounds the velocity of the optimizing peak. This settles the k=0, target-L-infinity case of the broader symmetry conjecture, together with the endpoint results. The variation identity at the remaining exponents is still open.

Revision 1.5 proves the full variation identity and midpoint-symmetric equality classification on an order-dependent interval immediately above p=1. It treats arbitrary maximizing sequences, controls their limiting absolute measures and dual residuals, and proves persistence of a single peak despite concentration of the highest derivative. The interval width is not estimated; overlap with the interval around two is not established.

Revision 1.6 proves that every finite-exponent variation maximizer has finitely many nondegenerate critical points, nonzero explicitly normalized endpoint highest derivatives, and exactly n+r-1 simple dual-residual zeros when there are r critical points. The critical-point count is uniformly bounded on compact exponent intervals. Section 11 derives an explicit necessary Hessian condition; excluding every maximizing configuration with r>=2 remains open.

Revision 1.7 excludes every variation maximizer with exactly two interior critical points, in every order n>=3 and at every finite exponent, without assuming symmetry. Translating both switches gives a polynomial cancellation, a strictly unimodal auxiliary function and a positive second variation. The remaining finite-exponent obstruction is a maximizer with at least three switches. Section 10 also corrects a missing backslash in the spacing command of (10.6).

Revision 1.8 derives the response to every affine switch motion and excludes midpoint-symmetric three-switch maximizers in every order n>=3 and at every finite exponent. Any remaining three-switch maximizer must have the unique minimum of its central-switch dilation response strictly outside its two outer switches. Nonsymmetric three-switch configurations and configurations with at least four switches remain unresolved.

Revision 1.9 disproves the arbitrary positive derivative-weight extension in order three, even for smooth weights. Theorem 15 gives an explicit continuous weight, a rational certificate covering the entire evaluation interval, and a strict two-switch lower bound. This closes the unrestricted weighted Hilbert shortcut; the original constant-weight conjecture remains open.

Revision 1.10 proves an explicit nodal-length restriction in order three. For 1<p<3, at most two intervals of constant sign of the first derivative cover more than p(3-p)/(3p-1) of the domain. Theorem 16 uses an admissible stretching family and a constrained second variation. Additional short intervals remain possible under this necessary condition; the full conjecture remains open.

Revision 1.11 proves the full variation identity and equality classification in derivative order three for every finite p>1. Theorem 17 reconstructs the stationary profiles from their quadratic residual vertices and compares a positive action across nodal counts. Every global maximizer has one peak and equals the unique midpoint height extremizer up to a scalar. The constant identity also holds at p=infinity; classification of all equality cases there remains open. The all-order conjecture remains unresolved for the remaining exponents in orders n>=4.

Revision 1.12 completes the uniform-endpoint equality classification in order three. Every nonzero extremizer is a scalar multiple of the explicit one-peak function with third derivative +1,-1,+1,-1 at the knots (1-1/sqrt(2))/2, 1/2, and (1+1/sqrt(2))/2. The variation constant is (2-sqrt(2))/48. Together with Theorems 9 and 17, this completes the order-three conjecture at every exponent, with the measure interpretation at p=1. The remaining all-order cases in n>=4 are open.

Revision 1.13 proves that every normalized uniform-endpoint variation maximizer saturates its highest-derivative bound almost everywhere, in every order n>=2. Theorem 19 gives an all-order conserved quantity, endpoint residual normalization, a strict mean-parameter bound, null residual and first-derivative zero sets, and fixed controls near both endpoints. A separate accumulation-point argument proves finite switching, and a spline zero count gives simple critical points and exactly n+r-1 simple residual zeros. For each fixed n>=3, the number of critical points is uniformly bounded over all 1<p<=infinity; the bound is not explicit. Exact local order-four solutions identify why the order-three residual bound does not follow from the higher-order conserved quantity alone. The remaining all-order conjecture is open.

- [Exact certificate generator](certify_counterexample.py), [certificate](counterexample-certificate.json), [alternate interpolation checker](check_certificate_independent.py), and [check result](alternate-certificate-check.json). Reproduce with `uv run --with sympy python certify_counterexample.py`, followed by `uv run --with sympy python check_certificate_independent.py`.
- [Full Markdown manuscript](manuscript.md)
- [53-page typeset PDF](manuscript.pdf) and [LaTeX source](manuscript.tex)
- [Priority and significance assessment](ASSESSMENT.md)
- [Internal proof review](REVIEW.md)
- [Source audit](source-audit.json) and [download provenance](source-downloads.json)
- [Artifact checks](artifact-check.json), [MathJax checks](markdown-math-check.json), and [hashes](SHA256SUMS.txt)
- [Exact normalization diagnostic](check_jacobi.py) and [recorded results](jacobi-exact-check.json)

The full all-p conjecture remains unresolved. Revision 1.3 completes its measure endpoint in every derivative order. The point-evaluation constant, spherical rearrangement theorem and spline identities are credited prior work. All results here form one paper.

Prepared with OpenAI Codex. This is an internally audited, unreviewed preprint; no independent human verification, absolute priority certification or journal acceptance is claimed.

## Rebuild

Run `python3 build.py` with Pandoc and Tectonic on PATH. The Markdown is authoritative. The package does not redistribute third-party PDFs. The rational diagnostic uses only Python's standard library; it does not prove the general theorem.
