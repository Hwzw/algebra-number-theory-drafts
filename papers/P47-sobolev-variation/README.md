# Sharp total variation bounds from spherical rearrangement

**Henry Zweiman. September 16, 2026. Revision 1.6.**

This preprint proves the all-order Hilbert-space case of the Nazarov-Shcheglova variation conjecture, including the exact constant and all extremizers. A Jacobi expansion turns the constrained Green form into a positive mixture of spherical Poisson interactions. A complementary measure argument proves the constant identity and coincidence of maximizing sets at p=1.

Revision 1.1 proves the identity and complete midpoint-symmetric extremizer classification for every p in an order-dependent open interval around two. Section 6 obtains convergence of maximizers through the highest derivative, proves persistence of their single peak, and controls the evaluation profile using polynomial sublevel estimates. The interval is not explicit and need not be uniform in the derivative order.

Revision 1.2 settles the fourth-order measure endpoint: C(4,1)=1/1296 and V(4,1)=1/648, with a unique normalized extremizing measure up to sign. Its five knots are 0, 1/6, 1/2, 5/6 and 1. Section 7 gives a complete alternation and polynomial-elimination proof, including symmetry and nonattainment in the ordinary Sobolev class.

Revision 1.3 proves that the optimal point-evaluation profile has its unique maximum at the midpoint for every derivative order. Its proof follows the alternating contacts, establishes that their velocities are strictly less than one, and applies credited B-spline peak monotonicity with an explicit endpoint extension. This gives the unique symmetric norm-one measure extremizer up to sign and rules out ordinary endpoint attainment in every order.

Revision 1.4 proves strict midpoint point-evaluation maximization and unique symmetric height extremizers for every finite exponent, in every order. Section 9 integrates a one-knot spline against a positive weight and bounds the velocity of the optimizing peak. This settles the k=0, target-L-infinity case of the broader symmetry conjecture, together with the endpoint results. The variation identity at the remaining exponents is still open.

Revision 1.5 proves the full variation identity and midpoint-symmetric equality classification on an order-dependent interval immediately above p=1. It treats arbitrary maximizing sequences, controls their limiting absolute measures and dual residuals, and proves persistence of a single peak despite concentration of the highest derivative. The interval width is not estimated; overlap with the interval around two is not established.

Revision 1.6 proves that every finite-exponent variation maximizer has finitely many nondegenerate critical points, nonzero explicitly normalized endpoint highest derivatives, and exactly n+r-1 simple dual-residual zeros when there are r critical points. The critical-point count is uniformly bounded on compact exponent intervals. Section 11 derives an explicit necessary Hessian condition; excluding every maximizing configuration with r>=2 remains open.

- [Full Markdown manuscript](manuscript.md)
- [Twenty-eight-page typeset PDF](manuscript.pdf) and [LaTeX source](manuscript.tex)
- [Priority and significance assessment](ASSESSMENT.md)
- [Internal proof review](REVIEW.md)
- [Source audit](source-audit.json) and [download provenance](source-downloads.json)
- [Artifact checks](artifact-check.json), [MathJax checks](markdown-math-check.json), and [hashes](SHA256SUMS.txt)
- [Exact normalization diagnostic](check_jacobi.py) and [recorded results](jacobi-exact-check.json)

The full all-p conjecture remains unresolved. Revision 1.3 completes its measure endpoint in every derivative order. The point-evaluation constant, spherical rearrangement theorem and spline identities are credited prior work. All results here form one paper.

Prepared with OpenAI Codex. This is an internally audited, unreviewed preprint; no independent human verification, absolute priority certification or journal acceptance is claimed.

## Rebuild

Run `python3 build.py` with Pandoc and Tectonic on PATH. The Markdown is authoritative. The package does not redistribute third-party PDFs. The rational diagnostic uses only Python's standard library; it does not prove the general theorem.
