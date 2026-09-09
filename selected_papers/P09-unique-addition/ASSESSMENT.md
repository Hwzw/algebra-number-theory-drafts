# P09: finite-length metabelian reconstruction

Status: new consolidated manuscript prepared September 8, 2026, pending final-source transfer review and parent QA. Earlier drafts under `research_program/papers/` and public copies have not been edited. This folder is one proposed paper, not multiple entries for its corollaries.

## Main contribution

Every centerless metabelian Lie algebra over a commutative unital ring, with finite-length underlying module, has unique addition as a Lie ring. The target of a bracket-preserving bijection can be an arbitrary Lie ring, without the source scalar structure. This covers all fields in finite dimension and all finite Lie rings, including additive groups of exponent p^a for a>1.

The proof recovers addition on each abelian Fitting image of an adjoint map. It then places the defect on the derived algebra inside the image of its centralizer, where the finitely many generator adjoints commute and have zero joint power-kernel. This eliminates the need for a globally invertible adjoint. Explicit algebras over every finite field demonstrate why that is a genuine additional case: all adjoints on their derived algebra are singular.

The separate faithful-action theorem is retained because it allows arbitrary infinite abelian translation groups and a possibly nonmetabelian acting Lie ring. It is not presented as a second paper. The common-centralizer family quantifies separation from a previous sufficient condition, with exact number s+1.

## Closest sources and overlap

* [Arzhantsev 2025](https://arxiv.org/html/2401.06241v2), Theorem 2 and Example 2/Problem 4: the two-centralizer criterion and the matrix question. The matrix answer is an application; the theorem here treats a full finite-length class and permits unbounded common-centralizer number.
* [Ferreira–Guzzo 2019, primary PDF](https://repositorio.usp.br/directbitstream/0349dfbc-0e9b-4e54-9b61-9081fba14522/2952053.pdf), Theorem 1.1 and the n=2 proof of Theorem 4.1, reproducing/extending [Qi–Hou 2011](https://doi.org/10.1080/03081080903582094): the associative-unital affine case, including the matrix question, follows by a central-extension adaptation of their proof. This overlap is credited prominently. The source hypotheses do not directly cover arbitrary acting Lie subrings or the full finite-length metabelian class.
* [Sosnov 2026](https://arxiv.org/html/2606.08201v1): current matrix Lie-ring reconstruction results. No metabelian or finite-length Fitting-image theorem was found there.

The source audit is bounded; no exhaustive priority guarantee is claimed. Detailed fresh comparison is in `research_program/reassessment/P09-audit.md`, and the complete extension-development proof is in `P09-extension.md` beside it. Earlier AI approval is not evidence of external validation.

## Significance and limits

The strengthened theorem is a coherent structural reconstruction result with characteristic-independent field and finite-ring consequences. It addresses substantially more than the original matrix example and survives the identified triangular precedent. It merits evaluation as a specialist research paper; internal proof agreement does not objectively certify exceptional significance or journal acceptance.

The theorem identifies bracket-preserving bijections with Lie-ring isomorphisms on the stated source class. Over a prime field this also gives linearity. It does not prove semilinear rigidity over arbitrary fields, an efficient bracket-table reconstruction algorithm, or additivity for bracket-preserving injections.

The general centerless-Lie-ring problem is not solved. Nonmetabelian Fitting images need not be abelian; infinite-dimensional adjoint chains need not stabilize. These are the exact points at which the proof stops.

## Validation record

The original theorem was freshly reconstructed and its triangular overlap checked directly in primary sources. The all-field extension was independently reconstructed by root; the arithmetic reviewer reported a hand-proof pass and subsequently checked the finite-length generalization. The independent report is `research_program/reassessment/P09-extension-independent-review.md`. The final consolidated TeX, including its generalized Fitting-image lemma and full module argument, is a separate transfer-review target; review was requested after the clean build. No automatic promotion is claimed here.

One Tectonic compilation invocation succeeded, producing seven pages with no warnings, overfull boxes, or underfull boxes in the log. Final visual QA is assigned to root.

* TeX SHA256: `2c304a0ff786141c14f8355c7fe82c56c4b5cf8e4633ec76ddde922cbc6d3890`.
* PDF SHA256: `de865d11c74edaf1d50233a8d13228c9ecd64257f5efd2f4c5f83549117bb73d`.

These hashes identify the exact source sent for final transfer review. A later source revision requires a corresponding renewed record.

## Final artifact check

The root has now read the complete selected TeX, inspected every PDF page, and checked the matching complete Markdown conversion records. The source/PDF hashes and all resolved-reference, proof-body, and math-preservation checks are recorded in the collection manifest and per-paper reports. No internal mathematical finding remains open in this selected statement. Live GitHub visual rendering and human mathematical verification are separate from these local checks.
