# Proof audit

September 22, 2026. Performed by the OpenAI Codex assistant that drafted the manuscript; no independent reviewer is claimed.

- The transform recurrence is derived from both basis identities, with the degree index advanced consistently.
- The leftmost interlacing root is -alpha-i+1. The manuscript corrects the off-by-one error in an earlier conversational draft.
- The signs at every endpoint are stated explicitly. There are i disjoint sign-change intervals for a degree-i polynomial, proving the full count.
- The limit with zero factor parameters preserves degree because the leading coefficient is h(1)>0, and excludes zero through h0(alpha)_d>0.
- The reciprocal-pair factorization includes repeated roots at -1 and the odd-degree unpaired factor.
- The shifted rising-factorial difference and the even/odd duplication factors are written out. The remaining transform parameter is alpha=3/2.
- The derivative gamma'(t/4) has positive constant term except in the explicitly excluded binomial case. Rolle's theorem includes repeated roots and the constant derivative case.
- The two input applications exclude that exceptional case by Cauchy--Schwarz. Their coefficient ratios are at least n^2 and n^3, respectively.
- The Karp polynomial includes the binomial coefficient via a third ordinary Hadamard factor; it is not silently identified with the unweighted polynomial.
- Zero endpoints are handled by an explicit approximation and exact counterexamples to unrestricted strict negativity.

The reproducible exact checks and their counts are in checks/verify.py and checks/results.json. Finite computations do not prove the general theorems. Historical novelty and independent human review remain unestablished.
