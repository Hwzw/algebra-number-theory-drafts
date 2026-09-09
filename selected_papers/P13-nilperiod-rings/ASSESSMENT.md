# P13 revised candidate: power-map periods and the prime radical

This separate revised manuscript leads with the new general statement that every additive period of every power map on every associative ring belongs to the prime radical. It applies to rings without identity and in all characteristics. Nilperiod rings are consequently 2-primal, and their nilpotent elements form a locally nilpotent ideal.

The previous NI-only manuscript and the public-repository copy have not been changed. The older elementary NI proof is omitted here because it proves a weaker conclusion and would duplicate the new argument.

## Mathematical evidence

- [Fresh audit of the original paper](../../reassessment/P13-audit.md): the old proof is sound, but its finite classification has a standard decomposition ingredient and its significance should not be inferred from former automatic admission.
- [Full strengthening and source audit](../../reassessment/P13-extension.md): complete proof for individual periods using the highest nonzero power of a nilpotent element.
- [Independent review of the strengthening](../../reassessment/P13-extension-independent-review.md): proof and exact nonunital bounded-index lemma pass, including the principal right ideal containing the nonzero highest power.

The revised source transfers that proof directly. The external ingredient is the classical bounded-index one-sided nil-ideal lemma: a semiprime ring has no nonzero nil one-sided ideal whose elements satisfy a common power-zero identity. This is not the Noetherian version of Levitzki's theorem. Bell--Martindale (1987), page 93 item (V), supplies the unrestricted statement, and Nielsen (2013), Section 1, confirms the nonunital radical formulation. Both are cited.

The finite classification and Corbas counts are retained as applications. Han--Lee--Park (2017), Proposition 2.6, is now credited for the standard Abelian semiperfect decomposition into local rings; the finite proof remains self-contained. The main theorem and its corollary now assert 2-primality explicitly. The only retained limitation is the important distinction between local nilpotence and a common nilpotency exponent for the entire ideal.

## Significance and priority limits

The stronger result provides a better research contribution than the NI-only version: it locates individual periods in arbitrary rings, gives semiprime vanishing, and strengthens the named conjecture to 2-primality and local nilpotence. The proof remains concise and uses classical radical theory. The finite classification and small-ring count should not be counted as separate difficult achievements.

Fresh primary-source comparisons found no directly subsuming result. This does not certify global priority or establish that the result meets every specialist's threshold for a major paper. In particular, an internal proof pass is not evidence that a problem was historically hard. This is a strengthened candidate for the revised five-paper selection, subject to the root's comparative significance assessment and final manuscript review.

## Build and current artifacts

One Tectonic build invocation completed successfully on 2026-09-08 and produced a five-page PDF. The log has no mathematical undefined references or layout warnings. The compiler's normal internal second TeX pass resolved references; no auxiliary computation was added.

Command from the workspace root:

```sh
research_program/tools/tectonic/tectonic --keep-logs research_program/selected_papers/P13-nilperiod-rings/manuscript.tex
```

Reviewed author-stage hashes:

- `manuscript.tex`: `a2eed3bf0b458dd20c9e5b182d3db8d0016e17de4154a11fd9a8f3b182ecfe41`
- `manuscript.pdf`: `3ca14c1096e67407fd20f656024de51469220a64f60fbeed0335ebbd804b24b3`

These hashes record the authored transfer and build. Root-level final text review, visual PDF inspection, and Markdown conversion remain outstanding at this stage.

## Final artifact check

The root has now read the complete selected TeX, inspected every PDF page, and checked the matching complete Markdown conversion records. The source/PDF hashes and all resolved-reference, proof-body, and math-preservation checks are recorded in the collection manifest and per-paper reports. No internal mathematical finding remains open in this selected statement. Live GitHub visual rendering and human mathematical verification are separate from these local checks.
