# A complete classification of a primitive cubic family

**Henry Zweiman** · September 9, 2026

[Complete Markdown paper](manuscript.md) · [Seven-page PDF](manuscript.pdf) · [LaTeX source](manuscript.tex)

For every prime power q, this paper proposes that a primitive polynomial X^3+X^2+X+lambda over F_(q^2), with lambda primitive, exists exactly when the characteristic is not three. This completely determines the surviving cases of Awasthi--Sharma Conjecture 9.1. The already published q=3 counterexample is credited. Counting estimates distinguish odd and even characteristic.

The proof uses an explicit Kummer parametrization, the Fu--Wan incomplete-character-sum theorem with its geometric hypotheses checked, and an exact sieve. The infinite argument covers q>=1511. Explicit certificates cover all 261 remaining prime powers outside characteristic three.

Run `python3 check.py` to verify the [witnesses](witnesses.json), cubic irreducibility and exact root orders, complete finite coverage, all rational sieve inequalities, and the base case of the infinite-tail induction. The verifier uses only the Python standard library. [Stored results](check-results.json) and the optional [C++ witness generator](search.cpp) are provided. To regenerate witnesses, compile the generator with `c++ -std=c++17 -O2 search.cpp -o search` and run `./search > regenerated-witnesses.json`.

The [source assessment](ASSESSMENT.md) and [proof review](REVIEW.md) explain the established dependencies, prior counterexample, and scope. [Artifact QA](artifact-qa.json) records seven inspected PDF pages and complete Markdown checks; the [manifest](manifest.json) records SHA-256 hashes.

This is one AI-generated, internally checked proposed manuscript. No human expert review, separate-agent review, journal acceptance, or exhaustive priority certification is claimed. It does not settle the higher-degree subfield-coefficient problem or automatically certify a significant solution toward the 45-paper goal.
