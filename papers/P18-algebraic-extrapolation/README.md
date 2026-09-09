# Integer-polynomial lifting and the classification of algebraic extrapolation sets

**Henry Zweiman — September 9, 2026**

[Full Markdown manuscript](manuscript.md) · [Nine-page PDF](manuscript.pdf) · [LaTeX source](manuscript.tex)

This manuscript gives an exact arithmetic description of finite extrapolation sets for algebraic-integer parameters. Integer-polynomial lifting supplies the central argument: an integer polynomial residue class has a representative strictly between zero and one on the unit interval precisely when it satisfies the internal-root inequalities and two endpoint congruences.

The consequences include the strong-PV discreteness classification, a model-set description with a finite congruence coordinate, an exact criterion for equality with the full internal cube, and finite generation of that cube. They address the questions in Section 11 of Fenner–Green–Homer, *Discrete & Computational Geometry* 76 (2026). All of these related consequences form **one paper**. Finite-generation assertions explicitly exclude the degenerate parameters zero and one.

The [source assessment](ASSESSMENT.md) distinguishes the new claim from classical approximation and known special cases. The [proof audit](REVIEW.md) records the internal review and external theorem dependencies. This is an internally checked proposed solution, with historical priority and significance subject to scholarly review; it has not received human referee review.

## Reproduction

The general arguments are in the manuscript. Optional finite consistency checks use only Python's standard library:

```sh
python3 check.py
```

The saved [check results](check-results.json) cover Bernstein identities, endpoint arithmetic, published quadratic cases, and bounded complex examples. Finite examples do not prove the general theorems. Compile `manuscript.tex` with Tectonic or a compatible LaTeX installation. The [artifact record](artifact-qa.json) documents the inspection of all nine PDF pages and the full Markdown conversion. The [manifest](manifest.json) provides hashes of the publication files.
