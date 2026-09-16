# Endpoint saddles and the local classification of eigenvalue–torsion critical domains

**Henry Zweiman** · September 16, 2026 · P53 · Version 1.0

AI-assisted research preprint. Internally checked by the originating assistant; not independently verified by human experts or peer reviewed.

For volume- and perimeter-normalized products of the first Dirichlet eigenvalue and torsional rigidity, the manuscript proves proposed nonlinear ball saddles at the upper local stability endpoints in every dimension. It classifies all nearby critical domains into finitely many analytic block-symmetry branches, including balanced branches with nonzero quadratic parameter variation. It also gives exact local orbit counts and an interval of strict local but nonglobal ball maximality.

- [Complete Markdown manuscript](manuscript.md)
- [Typeset PDF](manuscript.pdf) and [portable LaTeX](manuscript.tex)
- [Proof review](REVIEW.md) and [priority and significance assessment](ASSESSMENT.md)
- [Source/read-scope audit](source-audit.json)
- [Artifact checks](artifact-check.json), [formula check](markdown-math-check.json) and [file hashes](SHA256SUMS.txt)
- [Supplementary diagnostics](diagnostics/) and [citation metadata](CITATION.cff)

The established Hessians, strict local stability results, general equivariant bifurcation mechanism, elliptic theory and Bessel-zero transcendence are explicitly credited. Some older full-text comparisons remain incomplete. The original global convex perimeter inequality and a universal higher-dimensional balanced-branch sign remain open.

The work was prepared with OpenAI Codex, including problem selection, proof development, literature searches, diagnostics and drafting, and is presented under the requested Henry Zweiman byline. Neither that byline nor GitHub hosting establishes human verification.

The Markdown is authoritative. With Pandoc and Tectonic on PATH, run `python3 build.py` in this directory to regenerate the LaTeX and PDF. The diagnostic scripts require Python, SymPy and mpmath. Run them in this order: endpoint_expansion.py, dimensional_endpoint_check.py, low_dimension_jet_check.py, bifurcation_coefficient_check.py, balanced_quartic_check.py, balanced_modal_check.py. Each writes its JSON result beside itself. They are supplementary algebra and finite modal checks; they do not prove analytic remainders, universal conclusions or novelty. Third-party article PDFs are not redistributed.
