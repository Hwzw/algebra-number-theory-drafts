# The average number of unit-circle zeros in Stanley's reciprocal polynomial family

**Henry Zweiman — September 9, 2026**

[Full paper in Markdown](manuscript.md) · [PDF](manuscript.pdf) · [LaTeX](manuscript.tex)

For S chosen uniformly with maximum element 2b+1 and reciprocal polynomial N_S(x)=1-(1-x) sum_(j in S) x^j, the paper proves that the average number of unit-circle zeros is (2b+2)/sqrt(3)+o(b), with multiplicity. It also proves convergence of the mean angular measure.

This answers the average-count question in [Stanley's January 2024 addendum](https://mathoverflow.net/questions/461829/), also referenced in his [2026 ECA paper](https://doi.org/10.54550/ECA2026V6S1R4). The proof applies Nguyen–Vu universality after an exact sign representation and zero-law symmetrization, and controls endpoints by angular discrepancy.

The result is a complete internally checked proposed solution. Historical priority and significance remain provisional; it has not received independent human peer review. The constant and the universality theorem are established results, explicitly credited in the paper. The broader cyclotomic classification remains unresolved here.

- [Open-status and contribution assessment](ASSESSMENT.md)
- [Proof review and external-hypothesis audit](REVIEW.md)
- [Exact check script](check.py) and [results](check-results.json)
- [Package manifest](manifest.json) and [artifact QA](artifact-qa.json)

The script requires Python 3 and SymPy. Run `python3 check.py` to reproduce 1,023 exact cases and 63 Laurent identities. It writes `check-results.json`. The asymptotic theorem is proved in the manuscript, not inferred from these finite cases.

This is one paper. The angular theorem and count corollary are not counted separately. GitHub publication denotes public availability, not journal acceptance.
