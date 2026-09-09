# P01 assessment for the revised five-paper goal

Date: 2026-09-08. This is one consolidated paper. The original P01 remains preserved under `research_program/papers/`; this selected version is a substantive rewrite, not a duplicate contribution.

## Concrete advance

The paper proves an exact integral decomposition of the whiskered square-zero algebra as a module over its Lefschetz operator. It reduces every power of that operator simultaneously to shifted Boolean inclusion matrices. This gives integral diagonal forms, ranks in every characteristic, exact WLP/SLP characteristic thresholds, every characteristic-zero failing degree and power, and ordinary/graded Jordan data. In characteristic zero the Jordan type recovers the face numbers. A final application extends the known family of G-quadratic Gorenstein idealizations failing WLP.

It settles Holleben–Nicklasson Conjectures1.3/3.15, published in JPAA230(2026),108238. The published 20-page article was obtained from its institutional repository and its exact hypotheses and numbered statements inspected. The prior graph results covered positive cases, certain negative independence-number ranges, and finite computational cases. The new splitting removes these size restrictions.

## What is already known

Wilson's integral diagonal form for Boolean inclusion matrices, the resulting Boolean rank calculations, and characteristic-zero Boolean Jordan strings are classical. The paper explicitly credits Wilson and the primary reproving paper by Ghorbani–Khosrovshahi–Maysoori–Mohammad-Noori (Corollary3), which also records Bier's contribution. Wilson's original article was not obtained; its exact theorem was verified in that primary reproving source.

The positive graph WLP cases and the complete-graph SLP sufficient condition in large characteristic are due to Holleben–Nicklasson. Frobenius gives elementary small-characteristic obstructions. The idealization quotient argument and the shellability-to-G-quadratic theorem are established ingredients; the latter is checked against D'Alì–Venturello Proposition8.3, including the pure-flag and characteristic-zero hypotheses. The novel assertions are the simultaneous splitting and the consequences for this entire algebra family, not rediscovery of those external theorems.

## Why this is more than a small special case

The operator splitting works integrally and for every simplicial complex, including nonflag and nonpure examples. It supplies all powers and all primes rather than a single WLP witness. It proves a named, current conjecture, determines the exact failure locus, and produces downstream Gorenstein examples. The formulas allow replacement of large multiplication matrices by face counts and explicit binomial divisibility tests.

The key insight is elementary. Once it is recognized, much of the extension follows efficiently from classical algebra and combinatorics. This should not be advertised as a technically difficult proof or as a major breakthrough across commutative algebra. Its defensible significance is a plausible substantial specialized paper with a reusable structural theorem. Internal review does not certify external priority or a journal's valuation.

## Current literature and limitations

The source comparison and search chronology are recorded in `../../reassessment/P01-audit.md`. Fresh searches found no primary statement of the full splitting or classification. Search absence is not proof of originality.

Zijian Zeng's SSRN preprint, posted September3,2026, is credited for the eight-vertex case. Its primary abstract describes an exact computational verification on6,021 relevant isomorphism classes. The full PDF returned HTTP403 and could not be inspected. Consequently the assessment does not claim to have audited its internal argument or citations. The stated scope comes from its primary abstract.

No classification is claimed for arbitrary monomial powers, all very well-covered graphs, all Artinian reductions, or all Perazzo/Gorenstein idealizations.

## Validation and status

The author reconstructed the original classification independently and derived the stronger splitting. `check_extension.py` directly constructs the original x/y multiplication matrices and passes6,905 exact rank comparisons over F2,F3,F5,F7,F11, covering all complexes on at most4 vertices and selected5/6-vertex examples. The independent reviewer separately checked126 complexes and6,005 power ranks over Q,F2,F3,F5,F7. Both are supporting bounded checks; the infinite statements have hand proofs.

Fresh independent hand review of the full extension, including the idealization application, passed. Final selected-manuscript transfer review passed. The eight-page PDF compiles without warnings; visual inspection and Markdown export remain artifact gates managed separately; no external submission has been made.

## Final artifact check

The root has now read the complete selected TeX, inspected every PDF page, and checked the matching complete Markdown conversion records. The source/PDF hashes and all resolved-reference, proof-body, and math-preservation checks are recorded in the collection manifest and per-paper reports. No internal mathematical finding remains open in this selected statement. Live GitHub visual rendering and human mathematical verification are separate from these local checks.
