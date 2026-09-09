# Source, novelty, and significance assessment

September 9, 2026. Bounded literature audit by OpenAI Codex. Priority is provisional.

## The question actually addressed

The primary source is Minghui Ouyang, *On restricted sumsets with bounded degree relations*, Mathematika 71 (2025), no. 4, e70045, [revised author version](https://arxiv.org/html/2503.09121v3), September 4, 2025. Immediately before Conjecture 1.13, the paper identifies obtaining a linear size condition with an absolute coefficient as an obstacle. The conjecture itself proposes coefficient 2. P16 proves an absolute coefficient and an explicit sparse-column result at the coefficient-2 boundary. It does not solve the entire numbered conjecture.

This distinction matters: an automated problem catalog paraphrases the issue as a statement for every positive coefficient and describes arbitrary maps as matchings. Those paraphrases are not used. The primary paper both distinguishes one-sided relations from matchings and supplies constructions showing additional size restrictions are necessary.

## Opened sources and exact uses

| Source | Checked location | Use |
|---|---|---|
| Ouyang, revised author text above | Theorem 1.5(i), Corollary 1.8(i), paragraph before Conjecture 1.13 | Integer bound, separate qualitative transfer deduction, and the problem statement |
| Grynkiewicz, [arXiv:2402.15028v1](https://arxiv.org/html/2402.15028v1), Mathematika 71 (2025), e70030 | Theorems 1.4 and 2.4 | Exact high-density inverse theorem and the minimizing-subset form of Petridis' inequality |
| Green--Ruzsa, [arXiv:math/0403338v2](https://arxiv.org/pdf/math/0403338), Bull. London Math. Soc. 38 (2006), 43--52 | Definition on printed page 1, Theorem 1.3 on page 2 | Two-sided preservation of sum equalities and explicit small-doubling rectification threshold |
| Lev, *The rectifiability threshold in abelian groups*, Combinatorica 28 (2008), 491--497 | Original author PDF, definition on page 1 and Theorem 1 on page 2 | Cardinality rectification with ceiling(log_2 p) |
| Lev, [Restricted set addition in groups, II](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v7i1r4/pdf), EJC 7 (2000), R4 | Sections 1--3, all four main theorem statements | Earlier arbitrary mapping restrictions, counterexamples, total-relation bounds, and matching assumptions |
| Lev, [Restricted set addition in abelian groups: results and conjectures](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.485.pdf), JTNB 17 (2005), 181--193 | Survey's setup and conjecture discussion | Distinguishes classical equality restrictions and their conjectures from the present arbitrary maps |
| Pollard, JLMS (2) 8 (1974), 460--462; exact statement also in Grynkiewicz's [author paper on extending Pollard](https://www.diambri.org/Mathpdfs/pollard--vFIN.pdf), Theorem B | Level-t statement; original journal metadata | Truncated representation lower bound at t=2 |

Lev's original rectification author PDF was accessed at [this author-uploaded copy](https://www.researchgate.net/profile/Vsevolod-Lev/publication/220441643_The_rectifiability_threshold_in_abelian_groups/links/53f205640cf2bc0c40e6fc57/The-rectifiability-threshold-in-abelian-groups.pdf). The ceiling is confirmed by the defining inequality in its proof. Pollard's original journal body was not opened; the exact theorem was checked in primary research papers that use and extend it.

Grynkiewicz's abstract contains inconsistent density formulas; the theorem body, with p-r-3, is the input. The separate logarithmic inverse theorem attributed to his book was not used in P16 because its original statement had not been opened. Ouyang's journal full-text URL redirected to an abstract, so the exact statements are attributed to his revised author text, not an unread journal body.

## Comparison and bounded novelty search

Lev's 2000 theorem for arbitrary relations controls the loss by their total cardinality; it does not give the present constant loss for unbounded b. His sharper structural assumptions include degree bounds on both sides and are not silently applied to arbitrary one-sided maps. Ouyang's theorem assumes a fixed density gap. The complement transfer fixes that gap for a hypothetical counterexample and gives the qualitative extension immediately; P16 credits this dependence explicitly. The explicit theorem uses a different quantitative route through the high-density inverse theorem and controlled doubling.

Searches combined restricted sumsets, one-sided degree, Ouyang, Conjecture 1.13, complement, duality, linear size condition, logarithmic, and 2026. The author's publication list, updated June 2026, was checked. No matching subsequent resolution appeared among the inspected results. Search absence is not proof of priority; unindexed work and independent discoveries remain possible.

The collection's P10 addresses Ouyang's different integer conjecture at degrees divisible by three, using explicit counterexamples and an exact degree-three extremum. P16 concerns positive bounds over prime fields at degree one and uses neither P10's construction nor its theorem. These are distinct mathematical questions; the logarithmic bound and the constant refinements within P16 are not counted separately.

## Significance and admission judgment

The result answers an explicit question in a recent research paper and provides a reusable complement-transfer reduction. Its main limitation is the extremely small positive-density constant, and it leaves the sharp full conjecture unresolved. The qualitative observation is elementary once the existing theorem is available; the quantitative proof adds endpoint deletion and a complete treatment of the comparable case. This supports one research-note manuscript, with moderate and provisional significance, rather than a claim of a major conjecture resolution or a forecast of citations.

The internal proof/source audit supports public circulation as a proposed mathematical result. It does not certify the user's overall count of significant solved open problems. No human referee, independent expert endorsement, or journal acceptance has been obtained.
