# Explicit Lie polynomials with prescribed images over finite fields

**Henry Zweiman — September 9, 2026**

[Full paper in Markdown](manuscript.md) · [PDF](manuscript.pdf) · [LaTeX](manuscript.tex)

For every odd prime power q, the paper gives an explicit two-variable Lie polynomial of degree at most 6q-5 realizing any conjugation-invariant subset containing zero in sl_2(F_q). It proves the formula for all inputs, computes every fiber, and shows that a degree of at least ceil(q/4) is necessary for a single semisimple class together with zero, regardless of the number of variables.

This gives a proposed complete answer in rank one to [Kishnani–Singh Question 1.2](https://arxiv.org/abs/2605.19512). Their general existence classification is prior work. The new contribution is the explicit uniform construction and quantitative control. The higher-rank question and optimal degree constant remain open here.

- [Open-status and contribution assessment](ASSESSMENT.md)
- [Proof review](REVIEW.md)
- [Exact check script](check.py) and [results](check-results.json)
- [Package manifest](manifest.json) and [artifact QA](artifact-qa.json)

Run `python3 check.py` with Python 3 and SymPy. It writes `check-results.json`. The script checks generic matrix identities, 162,568 nested-bracket basis evaluations, and all 40 complete subset images over F_3 and F_5. It implements F_9 and F_25 as fields, not composite residue rings. The universal theorem is proved by hand in the manuscript.

This is one consolidated, internally checked manuscript prepared with OpenAI Codex. Historical priority and scholarly significance are provisional; no independent human peer review or journal acceptance is claimed. GitHub publication means public availability.
