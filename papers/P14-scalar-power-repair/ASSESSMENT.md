# Scope, sources, and significance assessment

Date: 2026-09-08. Author: Henry Zweiman. Assessment by the same Codex agent that developed the manuscript; no separate-agent or human review is claimed.

## Contribution

The manuscript gives a finite necessary-and-sufficient criterion for finite Dold repair of **individual** scalar power subsequences of arbitrary integral constant-coefficient recurrences. It includes polynomial Binet weights, root-of-unity quotient classes, and finite transients. Its nondegenerate specialization replaces the full splitting-field exponent by the exact exponent of the Binet coefficient field. It also proves eventual periodicity of the admissible exponent spectrum and a terminating least-multiplier computation for every fixed exponent greater than one.

This is a classification problem formulated in this research program. The manuscript does **not** describe it as a numbered conjecture from the literature. The unresolved scalar direction is explicit in the existing P02 research frontier, but that local statement by itself is not evidence that the problem is historically open.

## Closest primary statements checked

1. **Luca–Ward**, final 2023 JIS article, [official PDF](https://cs.uwaterloo.ca/journals/JIS/VOL26/Ward/ward9.pdf), Theorem 1 and its proof, printed pp. 3–7. Their theorem supplies sufficient conditions for simple recurrences, using a sampling exponent divisible by the root-field Galois exponent and at least the field degree. P14 does not claim that the sufficient use of Galois exponents is new. Its distinction is the scalar iff criterion, cancellation cases, coefficient field, and finite exponent spectrum.
2. **Rajs**, [arXiv:2509.09847v1 full text](https://arxiv.org/html/2509.09847v1), Theorem 8 in Section 4 and Theorem 9 in Section 5, with the adjacent Binet and Frobenius proofs. The former concerns the unsampled trace form. The latter is a sufficient result for simple recurrences along exponents divisible by the splitting-field degree. The informal paragraph preceding Theorem 9 has a smaller displayed multiplier than the theorem itself; this assessment uses the actual theorem statement.
3. **Minton**, [2014 DOI](https://doi.org/10.1090/S0002-9939-2014-12168-X), bibliographic details verified against [the author's publication page](https://gminton.org/research.html). The original AMS PDF could not be retrieved. The precise relevant unsampled trace classification was checked in **Byszewski–Graff–Ward**, [published Theorem 2.4](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.12531), which attributes it to Minton Theorem 2.15 and Remark 2.16. Original-paper access remains a limitation of the novelty comparison. The new manuscript credits the established result and does not purport to re-prove a novel s=1 classification.
4. **Bilu–Luca–Nieuwveld–Ouaknine–Worrell**, [author-hosted final PDF](https://people.mpi-sws.org/~joel/publications/twisted-zeros24.pdf), Theorem 1.8 on PDF p. 5: a nonzero nondegenerate recurrence over a characteristic-zero field has finitely many zeros. The manuscript uses this standard theorem with distinct nonzero bases over a number field after progression decomposition. It does not use the article's new twisted-zero conclusions.
5. **Milne**, [Algebraic Number Theory](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Section 8 decomposition/inertia theory and Theorem 8.31 (printed p. 147; PDF p. 149). These justify the residue-Frobenius lift at every prime and the infinitely many primes in each Frobenius conjugacy class. The manuscript's valuation estimate is proved directly.

Queries also covered Dold/Gauss congruences with scalar recurrences, coefficient fields, power subgroups, sampling, power subsequences, and ultimately periodic exponent sets. No closer classification was found in the inspected results. This is bounded search evidence, **not a proof of historical priority**. Search-result summaries that were irrelevant or not primary sources were not used as theorem evidence.

## Relation to P02

P02 concerns simultaneous repair of all matrix entries or all initializations for a recurrence polynomial. That quantifier makes the full root action detectable. P14 instead characterizes exactly what remains after scalar observation, including components that disappear only on the sampled indices. Its S3 example has an exact scalar sampling exponent of two although the full root-group exponent is six. P14 does not rely on the correctness of P02: it proves its own sufficiency and necessity using the published external inputs above. The two projects are connected, but neither scalar cancellation nor the general exponent spectrum follows from the simultaneous classification.

## Significance judgment and count boundary

The case for a substantive specialist paper is a general classification, a smaller exact invariant, a treatment of degeneracy rather than its exclusion, and a rigorous finite computational consequence. Its reusable mechanisms support further questions about efficient local repair, exponent spectra, and positivity. This is stronger than a numerical example, a small parameter extension, or splitting a corollary into a separate paper.

The proof and artifacts have passed the local audit documented in REVIEW.md. The manuscript is suitable for public circulation as a proposed research contribution. Exact historical novelty and journal-level significance remain provisional, especially pending full comparison with Minton and broader expert scrutiny. **Do not count this as an externally verified significant open-problem solution or certify the 45-paper goal from file counts.**
