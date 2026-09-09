# Mathematical and artifact audit

Date: 2026-09-08. Reviewer: the originating Codex agent, in a second proof-audit pass. This is not a separate-agent review, an independent human review, or a formal proof-assistant verification.

## Proof obligations reconstructed

1. **Binet decomposition.** Nonzero roots are algebraic integers from the integral recurrence. Nilpotent generalized eigenspaces give a finitely supported component, not an exponential term at zero. Uniqueness gives Galois equivariance and rationality of the transient. Negative exponents are never applied to zero roots.
2. **Fixed-m Frobenius necessity.** At every fixed positive m and fixed sigma, infinitely many prime ideals have exactly that arithmetic Frobenius. Removing denominator, multiplier, m, and transient exceptions removes only finitely many primes. Polynomial weights reduce to their constant terms, while Frobenius acts on roots only. A fixed algebraic number divisible at infinitely many primes is zero. No uniform prime for infinitely many m is required.
3. **Degenerate identities.** Roots are grouped by root-of-unity quotients before applying Skolem–Mahler–Lech. On each residue attained by an s-th power there are infinitely many sampled indices. The grouped bases are nondegenerate, so all polynomial coefficients vanish. This argument concerns an identity and makes no ineffective search for isolated zeros.
4. **Transient necessity.** First remove the transient at sufficiently large indices, use the identity lemma to recover all indices, then deduce that every sampled transient value is zero. Treating finite changes as harmless would be false.
5. **Ramified sufficiency.** A lift of residue Frobenius exists in the decomposition group. The exact sampled identity, rather than coefficientwise invariance, identifies the lower-level sum. With v(p)=1 and ramification index e, the binomial lower bound min(delta+1,p delta) reaches one after at most e−1 iterations and then gains one per iteration. This yields v>=s(r−1)−e+2 and a fixed multiplier. No unramified assumption is smuggled into the bad-prime argument.
6. **Coefficient field.** In the nondegenerate case singleton identities first force constant weights. Galois equivariance makes the coefficient field normal over Q, and restriction is onto its Galois group. The resulting invariant is the exponent of a quotient, not automatically the root-field exponent.
7. **Exponent spectrum.** Beyond the maximum prime exponent dividing M, nonunit power residues stabilize to zero at the corresponding prime-power component and unit powers repeat with Carmichael period. Transient positions beyond one disappear once 2^s exceeds the support bound. The finitely many polynomial identities then repeat.
8. **Exact multiplier algorithm, s>1.** The stronger valuation inequality gives r>=ceil((s+e−2+v_p(D))/(s−1)) as a level after which the unscaled difference already has full Dold divisibility. At each smaller level a finite modular recurrence state traversal determines preperiod and period. Checking m below N+lcm(T,p) covers all early values and all eventual coprime residue classes. Zero modulo p^r means no positive deficit. The argument deliberately excludes s=1.

## Adversarial examples and findings

- Fibonacci versus Lucas: same roots, different exact scalar admissible exponents.
- A totally real S3 splitting field with coefficient field Q(sqrt(229)): exact exponent two versus root-group exponent six. The cubic x^3−4x+1 is irreducible by the rational-root test and has discriminant 229; distinct positive conjugates ensure nondegeneracy.
- The repeated-root sequence 2^n+n*1_(n=2 mod 4) loses its entire repeated component on squares, defeating an unrestricted simplicity claim.
- n*2^n has an obstruction at every odd prime for every sampling power, supporting the nondegenerate nonsimple exclusion.
- A transient at 8 rules out s=1 and s=3; a transient at 1 rules out every s.
- A draft bibliography accidentally included D. Purser among the authors of the cited twisted-zero article. The final primary PDF has five authors; this was corrected before final compilation and hash binding.
- An initial biquadratic example distinguished fields but not group exponents. It was replaced by the S3 example, which verifies the stronger practical distinction.

No unresolved inference was found in this local audit. This is a fallible internal mathematical judgment, not a certification by another researcher.

## Computation and artifact evidence

`python3 check.py` uses exact integer recurrence states and rational valuation lower bounds. It verifies seven finite least-multiplier examples, 5,922 extended local congruences, 20,200 lifting-bound instances, and 16,200 eventual power-map instances, plus excluded-family witnesses. These are consistency checks, not premises of the proofs.

The TeX compiles without overfull boxes or unresolved references. All nine PDF pages were visually inspected in contact sheets; theorem and valuation pages were also inspected at full resolution. The complete Markdown conversion preserves the theorem/proof bodies and passed semantic round-trip checking. Its 292 math expressions passed local MathJax parsing. This does not assert that GitHub's live renderer was visually inspected.

Exact final hashes and audit bindings are in `manifest.json`, `check-results.json`, `markdown-conversion.json`, and `markdown-math-check.json`.
