# Open status, scope, and significance

September 9, 2026. Henry Zweiman. Internally checked proposed complete classification; outside correctness, historical priority, and significance remain provisional.

## Exact target and prior work

Awasthi and Sharma, *Primitive transformation shift registers over finite fields*, Journal of Algebra and Its Applications 18 (2019), 1950171, [DOI](https://doi.org/10.1142/S0219498819501718), Conjecture 9.1, asks for primitive cubics X^3+X^2+X+lambda over F_(q^2) with lambda primitive. Their discussion takes q prime. The original arXiv text and the [author-hosted final revision dated August 18, 2018](https://web.iitd.ac.in/~rksharma/Research%20Publications/Journal/Primitive_TSRs_Enumeration_revised%20%281%29.pdf), PDF page 12, were checked. The latter has 14 pages. It is an author revision, not a verified copy of the publisher's final typesetting; the publisher body was inaccessible.

A. K. Sharma, [arXiv:2608.07262v1](https://arxiv.org/abs/2608.07262v1), August 7, 2026, Section 4, already disproves q=3. P31 explicitly credits this. Section 5 claims a sufficient condition for larger fields and leaves the remaining field sizes unsettled. Its argument substitutes freeness in a larger multiplicative group for primitive membership in the required subfield. P31 explains that gap and gives an independent argument; it does not rely on the disputed sufficient condition. The broader statement is also incompatible with a direct norm obstruction.

Targeted searches of the specific family, Conjecture 9.1, primitive TSRs, and prescribed cubic coefficients did not locate an earlier complete classification. Older prescribed-first-two-coefficient results located in Cohen--Mills and Cohen's survey treat higher degrees; they do not supply this specific cubic classification. This is a source audit, not an exhaustive proof of historical priority.

## Proposed new result

For every prime power q, the required polynomial exists if and only if the characteristic differs from three. The positive direction covers every surviving field, not only sufficiently large fields. The negative direction covers every power of three, extending the already known q=3 example. The same paper gives different asymptotic main terms in odd and even characteristic.

The hard part is the exact coefficient parametrization, the nonconstant tensor-induction check, and the sieve with a complete finite boundary. The norm and discriminant obstructions alone were not treated as a separate paper. The result addresses a concrete published conjecture and supplies a method for related coefficient restrictions. No citation-count forecast is made.

## Essential external theorem

Fu and Wan, [A class of incomplete character sums, arXiv:1303.3650v3](https://arxiv.org/abs/1303.3650v3), revised January 6, 2025; published in Quarterly Journal of Mathematics 65 (2014), 1195--1211. Proposition 2.1 and Theorem 4.2, including their proof arguments relevant to rank-one tame Kummer sheaves, were read. The 2025 correction concerns Theorem 4.6's additive-character hypothesis; P31 uses the corrected version and does not invoke Theorem 4.6. The geometric nonconstancy requirement is explicitly checked using disjoint simple zeros. Rank, weight, genus, punctures, domains, and zero Swan conductors are accounted for.

The character-sum theorem is a credited classical dependency. The manuscript does not claim a self-contained proof of its cohomological foundations.

## Verification and limitations

The infinite argument reduces to q<1511. All 261 prime powers in that interval outside characteristic three have explicit certificates. An independent Python implementation verifies their base fields, primitive constants, cubic irreducibility, exact root orders, complete factor supports, and coverage. Exact rational/integer checks verify the finite sieve table and the base case for its infinite tail. This finite part is proof by exhaustive certificates, not experimental evidence for an unchecked range.

All review was performed by the originating agent, using separate implementations. No separate-agent, human expert, proof-assistant, or journal review is claimed. One manuscript is prepared for this combined result; no extra count is assigned to characteristic regimes, field sizes, or supporting lemmas. Publication does not automatically certify a significant solution toward the 45-paper goal.
