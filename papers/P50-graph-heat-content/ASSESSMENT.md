# Priority and significance assessment

Henry Zweiman. September 15, 2026. Developed as Q58.

**Current version: 1.3.** Earlier sections below retain the assessment history; the final section records the current general-measure theorem and remaining significance/source limits.

## Contribution and decision

Provisionally admit this as one research preprint under the revised standard, conditional on completing publication and public artifact verification. The complete proposed proof answers the all-times heat-content question in Bifulco-Täufer's **final** Electronic Journal of Probability 30 (2025), paper 158, Remark 2.9. It removes both the time restriction and the rational-edge-length assumption of their Theorem 2.6. The stronger theorem compares cumulative decreasing rearrangements for arbitrary nonnegative L2 initial data. Equality in heat content at a single positive time forces the mixed Dirichlet-Neumann interval. These statements constitute one paper.

The importance is the resolution of a concrete recent graph shape-optimization question together with a comparison usable for nonconstant loads and convex temperature functionals. The proposed argument makes a classical concentration mechanism work across Kirchhoff junctions and supplies a separate one-time rigidity proof. It is a short conceptual solution rather than a new general symmetrization theory. Potential uses include graph diffusion optimization, lifetime comparison and future quantitative stability, but no citation forecast is asserted.

The desired Advances in Mathematics/Transactions of the AMS level remains an editorial judgment. A reviewer could regard the application of classical methods as too short or specialized for that target. The explicit open question, unrestricted conclusion, general-data theorem and rigidity support internal admission, but do not certify venue suitability. There has been no independent expert review. The admission is revisable.

## Exact source comparison

- **Bifulco-Täufer:** final PDF obtained from the publisher's open-access link. Pages 2-7, including the form convention, main theorem and Remarks 2.7-2.9, and references on pages 18-19 were read. Their comparison uses the same total length and one Dirichlet endpoint. The final paper explicitly retains the all-times question. The arXiv record still lists only v1 (January 16, 2025).
- **Bifulco-Mugnolo:** final Annales Henri Poincare article published September 9, 2026. The introduction, Assumption 2.1, selected semigroup facts and the principal Section 6 statements were compared. These include surgeries and special heat-preserving operations. No equal-total-length all-times concentration comparison was identified. Not every combinatorial proof in that section was independently checked; it is not a dependency for our main comparison.
- **Friedlander:** the final Lemma 3 and its proof, printed pages 203-205, already give graph energy rearrangement and the branch-count equality argument. Those are credited. The proposed new rigidity step obtains equality of energies from equality of heat content at one time, through concentration, the half-time identity and differentiation of the nonnegative deficit.
- **Vazquez:** the author manuscript's Section 5.2 and Theorem 7.3 explicitly give zero-order elliptic concentration and implicit-time parabolic iteration for Euclidean equations. The mechanism is old and is prominently credited. The final journal metadata were checked; the publisher body was not read. Our proof is self-contained relative to standard rearrangement, maximum-principle and spectral facts, and does not depend on an unverified extension of his theorem.
- **Bifulco thesis:** printed pages 136-138 retain the question, establish a special mirrored-star example and observe that equality at all times implies interval rigidity via torsion. These do not contain the proposed single-time equality theorem.
- **Abstract domination:** Lenz-Schmidt-Wirth, arXiv:1711.07225v1, Example 1.28 and Theorem 3.5 were compared. Resolvent/semigroup equivalence is established general theory; the form-to-semigroup implication has additional self-dual isotone-cone hypotheses. The decreasing-function cone is not self-dual. No metric-graph-to-interval theorem was located in these inspected passages; our proof supplies the needed resolvent comparison directly. The final publication was not checked, and no new abstract domination principle is claimed.
- **Nonlocal comparison:** Ferone-Piscitelli-Volzone, arXiv:2311.00632v1, Theorems 1.1-1.2, concerns nonlocal kernels on Euclidean domains. Its introduction further confirms the established implicit-time method. The final journal body was not read; this is a comparison source, not a dependency.

The May 8, 2024 Potsdam talk abstract describing an anti-Faber-Krahn conclusion was not ignored. It contains no proof and uses inconsistent minimizer/maximizer wording. The later 2025 final paper proves the opposite small/large comparison and expressly poses the all-times question. The later primary article is the operative source; the historical discrepancy remains recorded in source-audit.json.

## Search coverage and limitations

Three complete arXiv API feeds return 3, 1 and 68 entries (71 distinct records after overlap). The graph-rearrangement query is noisy. Four subsequent queries timed out or returned HTTP 429; they are saved as failed requests, never as zero-result searches. Targeted web searches covered the exact question, authors, graph Talenti/rearrangement, concentration and abstract semigroup domination. The 2026 Mugnolo expander preprint was screened by abstract and history (v2, August 15, 2026), not by a full proof reading. Current primary seminar abstracts on graph heat geometry provided no competing theorem statement. The failed author feeds leave the successor search less complete than intended.

No matching resolution was found in the inspected primary literature. This does not exclude an unindexed, differently worded or unpublished result. source-audit.json records passages actually read and unread final comparisons. No absolute novelty certificate, independent correctness certificate or acceptance prediction is supplied. Publication is as an explicitly unreviewed AI-assisted preprint.

## Distinctness and scope

This graph parabolic theorem is separate from P49's planar annular physical-torsion stability. General data, convex functionals, time weights and lifetime interpretation remain within this one paper. No separate count is assigned to them. Weighted graphs, arbitrary couplings, quantitative stability and heat-trace comparison are outside the claims. The nonnegative continuous-form-domain killing measures treated in revision 1.1 form a specific additional class, described below.

## Revision 1.1: nonnegative killing measures (September 16, 2026)

Theorem 7.1 adds all-times heat-content and concentration maximization with fixed graph length and fixed positive mass of a finite nonnegative killing measure. It includes continuous potentials, point interactions and singular continuous measures. Equality at a single time characterizes a path with all mass at one endpoint. This is a natural extension of the existing paper, not a separate publication count or a newly certified extraordinary-conjecture solution.

The new proof feature is the cumulative boundary inequality U(L) + h kappa U'(L) <= F(L). Together with the zero-order interior inequality, it gives resolvent concentration order and survives iteration. The equality proof treats measure-valued second derivatives and excludes critical-set mass using equimeasurability with the strictly monotone Robin interval profile. No independent mathematical review was obtained.

### Additional source comparison

- **Özcan-Täufer:** arXiv:2410.18545v1, Sections 2, 8.2 and 8.3 read. Theorem 8.2 already gives the sharp atomic torsion comparison and equality case. Its minimum-concentration and rearrangement ideas are credited. Final metadata identify Journal of Mathematical Physics 67 (2026), 061508, DOI 10.1063/5.0301900. The publisher landing information dates publication June 24, 2026. The attempted final PDF route returned only an abstract and references; the final theorem body and numbering were not read. The manuscript therefore identifies the inspected preprint explicitly. Section 8.3's Kohler-Jobin problem is left open here.
- **Bifulco-Mugnolo:** final Remark 4.11 and equations (4.37) onward read in addition to the original comparison. These discuss positive semigroups for generalized delta/Robin couplings and possible path formulas. No fixed-total-killing comparison was found in that passage.
- **Kurasov-Serio:** final abstract and publication metadata checked for DOI 10.1007/s00023-019-00783-6. The subject is maximizing ground-state energy on a fixed graph under integral constraints. Only this description is relied upon; the full theorem proofs were not read.

Targeted searches combined heat content, Robin, delta, metric/quantum graphs, killing measures, rearrangement and total strength. They did not locate the same all-times fixed-mass theorem. These are bounded discovery searches, not exhaustive proof of novelty. The local extension notes retain source hashes and exact access limitations.

### Decision and frontier

Publish as revision 1.1 of the existing AI-assisted preprint, subject to final artifact and public-byte verification. The displayed proof supports the theorem internally. The extension improves the breadth of P50, but does not establish the user's extraordinary-significance threshold. The broader goal remains active. A sharp joint torsion/eigenvalue inequality for Robin or delta killing and a quantitative heat-content stability estimate remain open directions.

## Revision 1.2: sharp one-point Kohler-Jobin comparisons

September 16, 2026. Theorems 8.1-8.2 establish two sharp joint comparisons for a graph with one nonnegative delta interaction: at fixed length and strength, the endpoint-killed interval minimizes lambda_1 times T to the power 2/3; at fixed torsion and strength it minimizes lambda_1. Equality characterizes the same interval. This resolves the one-point case of the Robin joint-optimization direction, while leaving the general killing-measure problem open. It is another revision of P50, not a new paper count or completion of the extraordinary-conjecture goal.

The proof uses the established modified-torsion construction of Mugnolo-Plümer (final Theorem 5.8 and Lemmas 5.15-5.17), with its energy and moment identities rederived. The added positive minimum requires an interval strength kappa R/L and an endpoint value multiplied by sqrt(L/R). Two proved scalar monotonicities recover the desired constraints. The argument cannot be reused for general measures without additional terms; the scope restriction is mathematical, not an asserted general solution.

Additional primary checks: Mugnolo-Plumer's final relevant construction and theorem were read; Buttazzo-Cito-Solombrino's June 2026 final introduction, scaling conventions and Section 5 questions concern Euclidean domains with fixed Robin parameter and volume. Ozcan's July 15, 2026 arXiv:2607.12333v2 introduction specifies nonlinear Dirichlet-Kirchhoff conditions; it does not state a finite-strength Robin theorem. Its nonlinear proof was not audited. The final Ozcan-Taufer theorem body remains inaccessible, so claims about the explicit question and theorem numbering refer to the inspected preprint.

No matching one-point Robin joint comparison was found in the bounded searches. This remains a provisional priority assessment. The 216 finite-element diagnostic cases provided no counterexample to candidate comparisons, but their eigenvalue and torsion approximation errors have opposite directions and give no certified ratio bound. They are not proof dependencies. The published results rely on the hand proofs and internal audit only; independent review remains outstanding.

## Revision 1.3: full nonnegative-measure Kohler-Jobin comparisons

September 16, 2026. Theorems 8.1-8.2 now prove both previously open P50 comparisons for every finite nonnegative killing measure of prescribed positive total mass. Thus the restriction to one killing point is removed completely, including singular continuous measures. The fixed-length product and fixed-torsion spectral comparison both have the endpoint-killed interval as their unique optimizer.

The central estimate is Proposition 8.3. A weak eigenvalue test with G(psi), where G'=g'^2 and g(0)=0, controls the whole potential energy by g(t)^2<=tG(t). Choosing g'=mu/H gives a torsion lower bound. In decreasing rank coordinates, that bound becomes an integral of 2z-z^2, with z=sq/integral_0^s q. The coarea differential inequality compares z to ks cot(ks). This avoids the uncontrolled killing terms in the preceding modified-torsion transplant and works for every finite atomic measure; a proved common-domain form limit covers arbitrary measures. The complete proof, constants, constraints and equality cases were audited internally.

### Source and significance assessment

OT's inspected preprint Section 8.3 asks what a delta-vertex Kohler-Jobin inequality should look like and identifies the obstacle in adapting Dirichlet symmetrization. It does not state (70) or (72) as a numbered conjecture. Our statements provide sharp formulations and resolve the two precise general-measure questions posed in P50 revision 1.2. This is a full answer within P50's stated measure class, not a claim to solve the Euclidean Robin domain problem. The latter has different constraints.

The expanded source search checked potential/measure optimization and Robin eigenfunction rearrangement. Dai-Shi's arXiv:1402.2338v1, introduction, Theorem 3.1 statement, and Lemma 3.2 with proof were read: its differential inequality is a classical Chiti-type mechanism on interior superlevels of Robin domains. This is credited in the manuscript; no new general eigenfunction rearrangement method is claimed. Bucur-Buttazzo-Velichkov's arXiv:1310.1568 introduction and the final SIAM abstract concern capacitary measures in Euclidean space with a torsion constraint or inverse-power potential constraints, not fixed finite killing mass on a compact metric graph. Their full proofs were not audited. The 2026 fractional graph torsion article was screened only by its final abstract; it imposes Dirichlet vertices and is not a proof dependency.

The final OT publisher route again failed to expose the theorem body. The publisher-supplied preview on ResearchGate contains only page one, confirming the June 24, 2026 publication date and a discussion of possible Kohler-Jobin inequalities in its abstract. No final theorem number or exact final open-question wording is attributed. The MP final Dirichlet theorem, BCS final Robin-domain questions and O26 nonlinear Dirichlet scope remain the audited comparisons described above.

The improvement is substantial within graph spectral optimization: both constraints are sharp and the result covers the full finite nonnegative-measure class. The currently assembled literature evidence does not establish an extraordinary-significance assessment or absolute priority, and no independent review was obtained. The broader user goal remains active. Further source assessment and genuinely significant manuscript extensions should continue; ordinary proof or artifact completion alone is not substituted for that goal.
