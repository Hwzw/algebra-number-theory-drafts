# Proof review

Date: September 9, 2026. This is an internal review by the same AI system that developed the manuscript, not an independent human or separate-agent review.

## Algebraic reduction

Reciprocity is equivalent to complementary indicator pairs a_j+a_(d-j)=1, including the pair (0,d). There are exactly b free signs when d=2b+1. Uniform signs therefore represent uniform admissible sets without weights or omissions.

The half-integer sine representation follows from substituting a_j=(1+delta_j)/2 and pairing delta_j=-delta_(d-j). The substitution theta=pi-2t changes sine terms to signed odd-frequency cosines. Exact Laurent-polynomial checks verify the whole transformed identity for all 63 admissible cases through b=5.

N(1)=1 and N(-1) is odd and nonzero. The two open semicircles account for every unit-circle root. The exponential change of variables is locally invertible, and its nonzero factors preserve multiplicity. The factor two in the total count is essential.

## Symmetrization

R and -R have the same law. The zero multisets of R-D and -(R+D) therefore have the same law. An independent sign on D changes neither zero counts nor their joint distribution. This is stronger than merely matching expectations.

The analytic expression with sec(t) is used only in the open interval. The actual basis passed to universality is multiplied by cos(t), making every function entire and real on the whole real line. This avoids a global-domain ambiguity in the theorem's assumptions.

## External theorem hypotheses

Published Nguyen–Vu Theorem 2.6, printed page 10, is used with k=1 and l=0. C1 and C2 are on printed pages 7–8. The parameters can be chosen epsilon=1/2, alpha_1=1/2, C1=2, and the theorem's prescribed A and c1. The proof verifies the needed estimates for every fixed positive A,c1, so no optimization of these parameters is needed.

- The b+1 coefficients are independent, centered, variance one, with matching first two moments and uniformly bounded 5/2 moments.
- The entire trigonometric polynomial has degree at most 2b+2. Multiplication by the appropriate exponential gives an algebraic polynomial of degree at most 4b+4. Local exponential injectivity bounds the local complex-root count by 4b+4, including multiplicity. This is below the b^2 truncated-moment threshold for large b.
- The distinguished term has a nonzero highest Fourier coefficient. Identically zero functions occur with probability zero in both ensembles.
- Rescaled basis functions and first two derivatives are uniformly bounded in the needed complex neighborhoods. The squared-basis sum is at least c_a b. This verifies delocalization and both derivative-square estimates; the mean term vanishes.
- The sign ensemble is bounded deterministically by O(b). Gaussian coefficient tails give a polynomial bound outside exponentially small probability. These imply the theorem's exponential size threshold and arbitrary fixed polynomial exceptional probability.
- Lemma 9.2 on printed page 38 permits an arbitrary index set of size b. The odd frequencies are valid. Its good point is deterministic, and its small-ball bound is uniform over the target. Conditioning on the distinguished coefficient therefore preserves the bound. Division by cos at this point is legitimate and uniformly bounded in the bulk.
- The radius conversion is explicit: a t interval of length 1/(200b) maps within 1/400 of the chosen z center. The lemma's polynomial small-ball scale dominates the required exponential scale for all sufficiently large b.
- A fixed smooth partition in z has O(b) pieces, supports narrower than 1/100, and bounded derivatives through order six. The macroscopic comparison error is O(b^(1-c)); it is not incorrectly claimed to remain O(b^-c).

## Gaussian computation

The comparison is a centered Gaussian function, including its distinguished term. Its variance, value-derivative covariance, and derivative variance are respectively b/2+O(1), O(b), and (2/3)b^3+O(b^2) on every fixed compact subinterval. The exact sum of odd squares is b(4b^2-1)/3.

Geometric sums and summation by parts give all oscillatory error estimates. The distinguished term has size O(1) and derivative O(b); it contributes only within the stated errors. The covariance determinant is positive for large b. Edelman–Kostlan Theorem 3.1 applies and gives density 2b/(pi sqrt(3))+O(1). Multiplication by cos(t) changes no interior zeros.

## Endpoints and limit

Soundararajan Theorem 2 bounds angular discrepancy for all complex roots of a monic polynomial. Here the constant coefficient is one and the unit-circle supremum is at most 2b+3. Restricting to unit-circle roots preserves the upper bound. The two excluded t intervals correspond to two upper-semicycle arcs of length 2a each, giving normalized mass O(a)+O(sqrt(log b/b)). No Gaussian endpoint bound or unjustified interchange of a shrinking cutoff and the universality constants is used: b tends to infinity first, then a tends to zero.

The expected measures have uniformly bounded mass, so smooth bulk convergence extends to continuous tests. Conjugation, the Jacobian 2, and normalization by 2b+2 give the final density 1/(2pi sqrt(3)). The arc statement follows because the limit has no atoms. Product counts add algebraic multiplicities exactly.

## Computational and bibliographic audit

The check script enumerates all 1,023 sets for 0<=b<=9. It verifies reciprocal coefficient lists and the exact Chebyshev representation, then uses squarefree factorization and Sturm root counts weighted by multiplicity. All ten totals agree with Stanley's posted data. Numerical near-unit-root tolerances are not used.

Source inspection confirmed the relevant theorem numbers in Nguyen–Vu, Edelman–Kostlan, and Soundararajan. Crossref DOI metadata corrected the Conrey–Farmer–Imamoglu page range to 1835–1839 before publication. The source question's maximum-element notation is distinguished from the degree, which is one larger.

## Review outcome

No unresolved proof obligation was identified within the manuscript's stated scope. Finite computation supports identities and counts but is not treated as an asymptotic proof. Priority, mathematical interest, and journal suitability remain open to expert evaluation; this review does not certify 45 qualifying solutions or a citation impact.
