# Priority and significance assessment

Henry Zweiman. September 15, 2026. P42, developed as Q49.

## Decision

The completed manuscript is suitable for publication as one substantial research preprint with completed artifact verification. The originating assistant's adversarial proof audit found no remaining gap in the stated theorem. This is a revisable internal assessment, not human peer review, historical-priority certification, or a prediction of journal acceptance.

The main contribution is exact Euclidean optimality for eigenvalue-torsion products on balls over the entire normalized symmetric-seminorm class, in both extreme ranges of the product exponent, together with two-sided angular-deficit estimates and the optimal supremum norm stability power. The proof covers every dimension n>=2 and every energy exponent p>1. These results are consolidated into one paper.

## Explicit open problem and current sources

[Buttazzo and Fernandes Horta, arXiv:2603.09851v1](https://arxiv.org/html/2603.09851v1), Section 6, asks whether the norm optimizer for sufficiently small positive q in the maximizing problem, or sufficiently large q in the minimizing problem, is Euclidean. Its inspected arXiv history lists only v1, March 10, 2026; the CVGMT entry has the same last-update date. The introduction, definitions, Section 4 ball and extreme-exponent statements, and Sections 5-6 were read. The questions concern general fixed domains; this manuscript solves their ball cases only. Their Theorem 4.10 already proves the small-q ball conclusion through q=1 in the quadratic-seminorm subclass. That result is credited, and the present thresholds do not improve its range within that subclass.

[Fernandes Horta and Montenegro, Calc. Var. 64 (2025), 273](https://doi.org/10.1007/s00526-025-03114-2), published September 30, 2025, treats eigenvalue-only anisotropy optimization. The latest arXiv version is 2406.18683v4, September 15, 2024. The publisher's complete HTML was obtained by an ordinary direct request, despite the web-tool extract showing only a subscription preview. Sections 1.3-1.4, the principal statements in Section 1.7, and the entire Section 3.1 proof were read. Published Theorem 1.5 gives Euclidean eigenvalue maximality and rigidity. This endpoint is not claimed as new. Neither the stated product theorem nor a torsion term was identified in the full publisher text.

[Haddad, Fernandes Horta and Montenegro, JDE 447 (2025), 113635](https://doi.org/10.1016/j.jde.2025.113635), was read through the University of Seville's primary repository PDF. The introduction and Theorems 1.1-1.6 treat asymmetric eigenvalue optimization in low dimensions, a different objective. The present paper explicitly assumes symmetric seminorms.

The two works in progress listed in [BFH] concern Lane-Emden energies and higher-dimensional membrane optimization. Exact-title and author/topic searches did not identify publicly available versions. Their unpublished contents cannot be excluded as a source of overlapping work. Exact-topic searches also found no later answer to the ball persistence questions. Search absence is not proof of absolute priority.

## Dependence on convex geometry and rearrangement

[Alvino, Ferone, Trombetti and Lions](https://www.numdam.org/item/AIHPC_1997__14_2_275_0/), Section 2, Theorem 3.1 and equation (3.5), printed pages 278-279 and 283-284, were checked in the original PDF. Their hypotheses permit nonsmooth coercive norms. Their body K is the unit ball of H, while its polar is the support body used in the present paper. The level-set formula supplies the spectral comparison factor (volume(K)/volume(B))^(p/n) after that notation change. This is a substantial existing theorem, not a new result here.

[Besau, Hoehner and Kur](https://doi.org/10.1093/imrn/rnz277), arXiv:1905.08862v2, provides context for intrinsic and dual volume deviations. The introduction, principal approximation statement and radial-moment identities were inspected; no full audit of that work is claimed. We do not claim separate novelty for the elementary support cap calculation or the general use of convex-body deviations. The manuscript proves its precise integral comparison directly, including the finite covering argument.

The full source-download record is included as metadata. Third-party source PDFs are not republished with this preprint. The dated source-audit.json states exactly what was read and the limitations of the search.

## Why this is a substantive contribution

The problem combines two quantities that move in opposite directions as the energy changes. The known eigenvalue extremizer, the known torsion extremizer, and convergence of optimizers at an endpoint do not give exact optimality for any finite exponent. A fixed smooth perturbation calculation would likewise leave open angular perturbations whose supports concentrate as the perturbation tends to zero.

The proof closes that uniformity gap over an infinite-dimensional class. An integral support-to-radial comparison controls both the dual torsion trial and the volume factor in convex symmetrization linearly in the same angular deficit. Elementary global bounds then include seminorms of every rank. The exact product deficit has a sharp order for localized cap truncations, giving a quantitative refinement beyond optimizer identification. The same method works for all p>1 with the correct nonlinear torsion normalization.

This supplies an affirmative resolution of two explicitly posed ball problems, a quantitative theorem, and a method potentially applicable to other homogeneous variational quantities. Those features justify serious analysis/PDE review at the revised program's intended standard. The restriction to balls, the dependence on a classical symmetrization theorem, and the rough exponent thresholds are material limitations. A journal may judge the contribution more narrowly; neither journal placement nor future citation count is guaranteed.

## Counting and remaining frontier

Count at most one paper after verified publication. Do not count the two optimization regimes, the nonlinear extension, the geometric lemma, or the sharpness family separately. General-domain persistence, the best q thresholds, asymmetric anisotropies, and estimates uniform at p=1 or p=infinity remain outside the theorem. No independent mathematician has reviewed this manuscript.
