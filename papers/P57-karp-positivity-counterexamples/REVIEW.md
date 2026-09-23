# Originating-assistant audit

This is an audit by the drafting assistant, not independent peer review.

## Proof checks

- The arbitrary-shift expansion uses rising (alpha)_j/j!, not generalized falling binomial coefficients. Vandermonde gives this positive expansion exactly.
- Pairing indices a<b gives the Toeplitz minor f_(a+j) f_b - f_a f_(b+j) with the displayed positive orientation.
- The j=1, a=0, b=n-1 summand proves all strict coefficient inequalities under Karp's strict log-concavity hypothesis, including when an endpoint is zero.
- The higher-order finite-difference operations have determinant one. The row factors contribute (-1)^R, canceled by row reversal of the Hankel-indexed minor.
- Cauchy--Binet contributes the power z^(sum ell - R); including the extracted z^(2R) gives n=sum ell+R.
- Every remaining factorial basis polynomial is monic of degree n-r(r-1). Under PF_r no cancellation is possible between its nonnegative weights.
- Its constant coefficient is positive exactly when ell_0=0. If ell_0>0, it has precisely one factor x and every other constant shift is positive.
- The fixed-factor corollary uses q_j=ell_j-j nondecreasing, not merely nonnegative.

## Exact counterexample checks

- The n=18 input has positive endpoints and strict log-concavity in every required index. Its minimum exact gap is 20163.
- Its displayed factorization was verified symbolically against the original defining sum, independently of the higher-order minor formula.
- The ninth coefficient and leading-coefficient indexing in the degree-eight Hurwitz matrix were checked. Delta_7 is negative, with its exact integer factorization verified.
- A negative Hurwitz determinant implies an open-right-half-plane zero by applying the strict criterion to T(x+epsilon) and taking epsilon down to zero. No approximate-root certification is needed.
- Q(x)=P(x+1), so the stability counterexample for Q gives a root of P with real part greater than one.
- The n=11 binomial input is PF_infinity by convolution of eleven copies of (1,1).
- The order-three formula contains exactly five increasing tuples. Their exact minors and weights reproduce the displayed factorization.
- The cubic discriminant is the exact negative integer -623476452956.
- Thirteen original-determinant evaluations independently verify the degree-at-most-eleven identity. The check uses permutation expansion and truncated series products, not finite differences.

## Presentation and scope

The manuscript treats Conjecture 4's zero-output and zero-constant-term cases explicitly. It does not describe false conjectures as proved. It distinguishes its results from the earlier Conjecture 3 manuscript and from unverified claims of historical priority.

The supplementary verification script checks exact identities and the concrete certificates. Such finite checks do not replace the arbitrary-degree proofs.
