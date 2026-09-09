# Internal proof and artifact review

Henry Zweiman. September 9, 2026. Review by the originating AI agent; no independent human referee or formal proof assistant was used.

## General growth proof

1. **Integral values.** The denominator H_i is the product of the monic degree-i polynomials. Its valuation at a degree-d prime is the sum of q^(i−kd) for kd≤i. Uniform fibers of V_i modulo P^k give at least that valuation in e_i(A). Therefore E_i(A) lies in R at every input.
2. **Prime congruences despite denominators.** For G_(s,j), all primes of degree ≤s−1 divide every value through Pi_(s−1). At larger primes every H_i is a unit, so the rational polynomial has coefficients in the local ring. This is why only one copy of each small prime is needed.
3. **Dimension.** Each digit polynomial has X-degree j. Thus the displayed coefficient arrays inject into K[X,Y]. The number of unknowns is strictly greater than q^(2M+1), while the value-height bound gives at most that many scalar equations on all q^(M+1) initial inputs. Nonzero coefficients cannot merely represent the zero polynomial.
4. **Finite exceptions.** M is chosen after bounding the values at all exceptional inputs. The growth assumption then bounds every input in V_(M+1), not merely its outer shell.
5. **Propagation.** With D=M+r, the upper bound divided by q^D is at most 15/16 for all r≥0. A least-degree nonzero value is divisible by Pi_D and has smaller degree than Pi_D, an impossibility. The exact lower bound d_D≥q^D follows from t^(q^D)−t dividing Pi_D.
6. **Rationality.** Clearing denominators yields an algebraic relation. The finitely many zeros of its leading Y-coefficient are explicitly excluded and then absorbed into the height constant. Bell–Nguyen Theorem 3.1 applies with U=t because U'=1 and the resulting values f(t^n) have linear degree growth. This last theorem is an explicit external dependency.

## Linear and Newton statements

- The additive expansion is defined on the F_q-basis 1,t,t^2,... and is locally finite. Its coefficient criterion follows prime by prime using the first d basis vectors modulo a degree-d prime.
- The transform bound includes every earlier coefficient and allows deg 0=−infinity. Its extra scale is 1/(q−1), strictly smaller than the primorial limit q/(q−1).
- Boundary equality deg f_*(t^n)=d_n is only eventual. At q=2,n=2 cancellation actually occurs; the proof and checks do not assert equality at every index.
- General Newton denominators have the claimed valuations because *aligned* digit blocks give complete residue systems. The partial block omits the residue of A_n. This does not assert the stronger simultaneous prime-power sequence property discussed by Li and Sha.
- The bounded delta function is not prime-congruence-preserving. Its coefficient growth obstructs only an argument that ignores congruences; it is not a counterexample to Question 4.1.

## Exact checks

The shipped `check.py` is self-contained and uses only Python's standard library. The finite-field multiplication is explicit; F_4 and F_9 are included as extension fields. The final packaged script was run successfully, producing `check-results.json`.

- 8,570 literal digit-basis values; their degrees and prime-congruence residue buckets all pass.
- 2,863 literal additive-basis values and 59 triangular degree checks.
- 19 additive coefficient models: eight preserving examples and eleven deliberately failing examples agree with the divisibility criterion.
- General Newton bases: 36, 45, 136, and 3,321 triangular values for q=2,3,4,9; preserving and deliberately failing models agree with the coefficient criterion. Delta coefficients are recovered directly.
- 56,320 height/propagation parameter cases and 2,816 dimension cases with exact rational arithmetic, for integer q from 2 to 257. The hand inequalities, not this finite range, prove the assertions for all prime powers.

## Artifact review and unresolved assessment

The final PDF has seven pages. Every page was rendered at 100 dpi and visually inspected. No clipping, overlap, missing mathematical glyphs, or overfull TeX boxes remain. The complete Markdown conversion preserves all source mathematical expressions; the rendering checker reports zero errors. File hashes identify these versions.

The proof above is an internal audit. Historical priority, outside mathematical review, the unread final journal text of the principal source, and the sharp arbitrary-function threshold remain separate limitations. Public hosting does not remove them.
