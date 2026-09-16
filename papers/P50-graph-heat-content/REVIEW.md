# Internal proof audit

Henry Zweiman. September 15, 2026. Conducted by the originating assistant; not independent review.

## Main comparison

1. **Operator normalization.** A is nonnegative minus the second derivative. The heat semigroup is exp(-tA). The interval is Neumann at 0 and Dirichlet at L, matching decreasing rearrangement. Reflection aligns it with the primary source.
2. **Graph hypotheses.** Finite positive-length edges, nonempty Dirichlet set, and connectivity outside that set are explicit. Loops count twice in vertex sums. Dirichlet vertices need not be leaves for the inequality. Degree-two subdivisions do not change the problem.
3. **Regular resolvent loads.** Strictly positive nonconstant edgewise polynomials are dense in the nonnegative L2 cone and need no vertex compatibility. The resolvent is analytic past each closed edge. A constant solution edge would force a constant polynomial load, which is excluded. Thus critical values are finite in the approximation step. The proof does not incorrectly assume this for arbitrary L2 data.
4. **Flux sign.** Integration over a superlevel set gives h times the sum of absolute boundary derivatives, with a positive sign. Internal vertex fluxes cancel because every incidence near an included vertex belongs to the superlevel set. Positive levels contain no Dirichlet vertices.
5. **One boundary point is sufficient.** A simple path from a maximum to the zero Dirichlet set crosses every intermediate value. Hence N>=1 even with cycles or multiple edges. Cauchy-Schwarz gives ab>=N squared, and therefore -hU''+U<=F, in the needed direction.
6. **No hidden singular part.** The path-length estimate makes the rearrangement globally Lipschitz. The nonflat analytic approximation makes exceptional mass ranks finite. Thus U is W2-infinity and the differential inequality has a valid weak interpretation. Its mixed boundary data are U(0)=0 and U'(L)=0; the latter follows from essential infimum zero, not from giving a point positive measure.
7. **Interval monotonicity.** The resolvent derivative has nonpositive forcing and nonpositive endpoint data. Positive-part testing gives a decreasing interval profile. Monotone smooth approximation handles rough decreasing data.
8. **Cumulative-order induction.** The interval cumulative equation preserves concentration order. This is essential: a comparison only against the rearranged previous graph profile would not by itself justify iteration without that order property.
9. **Density and Euler limit.** Hardy-Littlewood proves L2 contraction of decreasing rearrangement. Resolvent boundedness passes the regular-load inequality to general loads. Spectral dominated convergence proves the Euler limit for every fixed time, while the supremum-over-sets formula passes cumulative inequalities uniformly in the rank s. No finite computation substitutes for this limit.

## Rigidity

10. **Half-time factor.** Q(t)=||S(t/2)1||2 squared, and Q'(t)=-energy(S(t/2)1). The derivative has factor one, not two.
11. **Equimeasurability.** Weak concentration plus equal squared norms implies equality of distributions by the continuous stop-loss integrals. Equality of total mass alone would not suffice.
12. **Energy equality.** The already-proved nonnegative heat-content difference has an interior zero at the specified time. Its derivative vanishes there. This yields exact energy equality, avoiding an invalid claim that strict discrete defects survive the Euler limit.
13. **Strict concavity.** Sub-Markovianity makes the constant-load heat profile decrease in time. Thus Aw>=0; coercivity and positivity show it is nonzero. Applying the positivity-improving semigroup at half time makes Aw>0 on open edges. Spectral smoothing gives edgewise smoothness, so each edge is strictly concave and has at most one critical point. This statement is made only for the constant initial datum.
14. **Energy coarea.** There are finitely many exceptional values. Coarea gives energies integral a and integral 1/b. Equality plus ab>=N squared implies N=1 almost everywhere. The rearranged profile has the requisite Sobolev representative by the Lipschitz lemma.
15. **Topology.** Every Dirichlet incidence gives a positive outgoing derivative, so small regular levels count the sum of Dirichlet degrees. It must be one. At a branching standard vertex, zero outgoing derivatives are decreasing incidences by strict concavity. Pigeonhole on increasing/decreasing incidences produces at least two preimages on an interval of levels. The argument covers loop incidences by disjoint small neighborhoods. A connected graph with degree at most two and a leaf is a path.

## Corollaries, attribution and limits

The interval eigenfunction expansion was checked analytically: squared constant-function coefficients are 8L divided by pi squared times the odd square. Positive time weighting uses Tonelli and strict pointwise inequality. The torsion constant L cubed divided by three follows directly from the interval quadratic solution. The convex-function comparison is a standard stop-loss integral consequence; it is not counted separately.

Friedlander's energy and branching argument, Vazquez's zero-order comparison and Euler strategy, and the existing torsion result are expressly credited. The mathematical proof contains no computational hypothesis. Markdown/LaTeX checks and PDF inspection concern artifact integrity only. The final source and source-search limitations are in ASSESSMENT.md and source-audit.json. No unresolved proof gap was identified in this internal audit, but external expert scrutiny remains necessary before claiming independent verification.
