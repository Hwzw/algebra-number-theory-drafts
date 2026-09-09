# Reconstruction of Krull monoids from conductor submonoids

**Henry Zweiman — September 9, 2026**

[Full paper in Markdown](manuscript.md) · [PDF](manuscript.pdf) · [LaTeX](manuscript.tex)

This short note gives an internally checked proposed answer to the isomorphism question following Proposition 4.3 of Geroldinger--Yan--Zhong, *On conductor submonoids of factorial monoids*, Semigroup Forum 112 (2026), 792--819. The associated conductor monoid determines the original reduced Krull monoid and its divisor theory. The same reconstruction yields an automorphism formula and an intrinsic recognition criterion.

The proof is elementary once the complete integral closure is used; the closure lemma and the uniqueness of divisor theories are classical. This is one focused research note. It does not claim reconstruction of a domain's addition or unit group, nor a solution of whole-system factorization-length realization.

- [Scope and literature assessment](ASSESSMENT.md)
- [Internal proof review](REVIEW.md)
- [Reproducible finite example checks](check.py) and [results](check-results.json)
- [Artifact quality record](artifact-qa.json) and [file hashes](manifest.json)

Run `python3 check.py` for the independent finite example checks. The universal theorems are proved in the paper and do not depend on these finite calculations. Review was performed by the originating agent; no human peer review or independent-agent review is claimed. Novelty and significance remain provisional, and publication does not certify admission among the program's target of 45 significant open-problem solutions.
