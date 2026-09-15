# Proof and artifact review

Henry Zweiman. September 15, 2026.

This is the originating assistant's internal adversarial audit. No subagent or human referee supplied an independent review. Artifact checks establish file integrity and rendering, not theorem correctness.

## Mathematical obligations checked

1. **Convex representation.** The support body is the polar unit ball, contained in the Euclidean ball and touching its boundary. A contact vector supplies a rank-one projection lower bound for every normalized symmetric seminorm. Degenerate competitors are included without assuming a minimizer exists.
2. **Function spaces and positivity.** Chordwise Poincare is first applied to compactly supported smooth functions, then transferred by W^{1,p} density. It bounds all energy denominators away from zero relative to the Lp norm. Holder supplies the finite torsion upper bound. The constants need not be sharp.
3. **Torsion convention.** T is the root of the variational supremum in (1.2), hence integral w. The Euclidean radial function has flux -x/n, integral V n^(-1/(p-1))/(n+p'), and gradient p-energy equal to T. Radial trials give T_H/T_E >= m_H^(-1/(p-1)), with this root essential.
4. **Cap estimate.** A support loss e cuts the unit ball by a plane. Directions within angle sqrt(e)/4 have loss at least e/2; this is valid for all e in (0,1], including degenerate limiting cases. The truncation formula is justified because the unconstrained maximizing point lies beyond the plane.
5. **Covering argument.** Metric projection relates the original direction to the cap center by distance at most sqrt(2e). Each compact subset of a distance superlevel set has a finite cover by enlarged caps. A finite decreasing-radius selection gives disjoint original caps, with every discarded enlargement covered by a fixed dilation of a retained cap. Inner regularity removes the compact restriction. Strict level sets are preserved because e>t. This replaces an initially proposed uncountable greedy construction.
6. **Radial comparison.** The gauge is 2-Lipschitz from the inball condition. The inequality rho^(-1)-1 <= g(theta)-g(z) has the correct direction because g(z)<=1. Layer-cake integration then gives a linear L1 radial bound. Symmetry is unnecessary for this geometric lemma.
7. **Near-Euclidean coercivity.** Normalized H is 1-Lipschitz. A value at most 1/2 creates a fixed positive angular deficit; its contrapositive guarantees an inball for small delta. The radial volume and negative moment estimates use derivatives on [1/2,1], avoiding singular dual norms.
8. **Rearrangement input.** Original AFTL hypotheses, body polarity, volume scaling and exponent p/n were checked. The manuscript derives the factor from equation (3.5) and uses Theorem 3.1 for the general Sobolev statement. Equimeasurability preserves the eigenvalue denominator. No rigidity assertion from that source is needed.
9. **Nonlinear duality.** The upper torsion estimate uses F=|grad w_E|^(p-2)grad w_E. Holder gives a power p-1 of integral H^circ(F)^p' before the root is taken. Radiality then gives T_H/T_E <= integral_S H^circ(theta)^p'. Using grad w_E instead of F for p unequal to two would be wrong; the manuscript does not do this.
10. **Global exponent thresholds.** Near delta=0 the logarithmic product estimates have coefficients -1+qC and q/(p-1)-2pC/n. The stated thresholds make them at most -1/2 or at least one. Far from zero, the fixed eigenvalue and torsion bounds give strict gaps uniformly over the full class. Both regions cover their common boundary, and delta=0 forces Euclidean equality by continuity.
11. **Two-sided deficit estimate.** The maximum-regime upper bound uses (1-C delta)^(p/n) >= 1-max{1,p/n}C delta, valid on either side of p=n. The minimum-regime upper bound follows by the mean value theorem on [1,3/2]. Far-region constants use eta>0 and delta<1. No compactness of the optimizer map is assumed.
12. **Sharpness.** Opposite cap truncations contain (1-epsilon)B, have support deficit exactly epsilon, and still touch the unit sphere when n>=2. The deficit is supported in caps of angular radius O(sqrt(epsilon)). Its angular integral is O(epsilon^((n+1)/2)), and the upper product estimate proves optimality of the lower stability power. No assertion of optimality within a prescribed smoothness or curvature subclass is made.

No remaining logical gap was identified in this audit. The conclusion remains subject to outside verification and correction.

## Source and scope obligations

See ASSESSMENT.md and source-audit.json. The published HM theorem number is 1.5, matching arXiv v4; an earlier inspected version used different numbering and is not the citation target. BFH's quadratic-seminorm theorem and its general-domain frontier are distinguished. The nonlinear extension and the two extreme regimes are consolidated, not counted as separate papers.

## Artifact obligations

manuscript.md is authoritative and uses explicit mathematical delimiters. build.py converts it to portable LaTeX with Pandoc and compiles with Tectonic. The final artifact-check.json records MathJax syntax, display-tag consistency, extracted text, exact hashes and visual review of every final PDF page. It does not claim that GitHub's live renderer or an external expert has checked the mathematics.
