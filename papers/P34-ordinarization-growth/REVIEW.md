# P34: internal proof review

Date: September 9, 2026. Reviewer: the originating AI agent. No separate-agent or human review has occurred.

## Mathematical obligations

1. **Encoding and closure.** A genus-g semigroup has Frobenius number at most 2g−1 by the injection of nongaps into gaps. Exactly r nongaps at most g imply exactly r gaps above g. The tuple is unique. Low–low sums require both the small-nongap condition and exclusion from A; low–high sums require the explicit difference condition. High–high sums exceed every encoded gap. Permitting the endpoint 2g in the ambient box creates no additional valid semigroup.
2. **Quasipolynomial at every positive genus.** Every predicate is homogeneous in the tuple and g. Strict inequalities are retained; no constant one is introduced. The normalized real Boolean set is bounded. An arrangement yields relative interiors of rational polytopes. Closed Ehrhart counts and face inclusion-exclusion work for every positive dilation, including lower-dimensional affine hulls with missing lattice residues. The argument does not assert that one polynomial applies to all genera or that g=0 must follow the same formula.
3. **Exceptional loci.** Failure of either bulk inequality in a valid tuple forces 2b1=bi or ar−b1=ah. In the bulk, mixed sums are automatic and only bi+bj=ah can violate closure. This logical argument also holds for the real normalized sets, enabling the geometric comparison.
4. **Constant correction coefficient.** All exceptional hyperplanes are proper linear hyperplanes in the tuple variables alone. A cell of dimension 2r−1 has affine hull exactly its containing hyperplane. The full lattice of that linear space occurs at every dilation. Normalized leading volume is constant and rational; lower-dimensional cells are O(g^(2r−2)). This excludes a periodic term at degree 2r−1 in the signed correction. An O(g^(2r−1)) estimate by itself would not establish growth.
5. **Uniform binomial expansion.** Binomial polynomials vanish at nonnegative upper indices below the lower index, so the expansion needs no excluded endpoint cases. Summing the uniform remainder loses exactly one power. The r=1 case is evaluated separately.
6. **Endpoint sign and size.** The first bulk index is g/2+1 in even genus and g/2+1/2 in odd genus. The trapezoidal lower-end coefficient is 1/2−delta. Thus even minus odd at the next degree is −f(1/2)/2=−C_r. The beta integral yields A_r as stated.
7. **Growth and exact period.** The constant correction changes only the average second coefficient. The difference of successive leading terms is 2r A_r g^(2r−1), and the parity term contributes C_r (−1)^g g^(2r−1). Both resulting constants are positive. The residual O terms are subtracted directly, not differentiated. A residue-class polynomial identity identifies the exact top coefficients and their period two.
8. **Scope.** Constants in the error estimates depend on fixed r. No uniform threshold, full period, explicit beta_r, or all-genus monotonicity result is claimed.

## Independent finite diagnostics

`check.py` uses integer and Fraction arithmetic. Its literal closure test explicitly constructs the candidate semigroup up to the maximum relevant sum. It agrees with the structural predicate on 66,187 tuples through genus 9. All 584 symmetric-difference cases satisfy a stated exceptional equality.

A separate minimal-generator tree algorithm produces 11,770 semigroups cumulatively through genus 16 (4,806 at genus 16). It agrees with tuple counts on the overlap and with the published r=1 and r=2 formulas. For r=1 through 12, exact Newton interpolation of both bulk parities verifies the top two coefficients, the parity gap, the positive increment constants, and 936 later evaluations. This validates examples and implementation, not universal mathematics.

The first manuscript draft confused the cumulative tree total with the genus-16 count. The text was corrected before publication. The final executable and saved output agree.

## Artifact review

The final six-page PDF compiled without warnings. Every final page was visually inspected for legibility, missing glyphs, equation alignment, overlaps, page numbering, and references. The full Markdown retains every theorem and proof; the conversion record and MathJax validation record are included. There are 229 validated math expressions and no reported math-parser errors. GitHub live rendering was not independently inspected.

No unresolved proof gap was identified in this internal review. This is not independent certification of correctness or novelty.
