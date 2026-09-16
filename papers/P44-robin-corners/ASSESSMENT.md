# Priority and significance assessment

Henry Zweiman. September 15, 2026. P44 revision 2.0.

## Current internal assessment

The manuscript contains complete written arguments for two conclusions: discrete-exception failure of polygonal log-concavity across the positive parameter axis, and the full small-positive-parameter quasiconcavity conjecture for convex polyhedra outside products of circumsolids. The latter is new in revision 2.0. The originating assistant's proof audit found no remaining gap in the stated results. This is an internal assessment of an AI-assisted preprint, not independent expert verification, peer review, an absolute priority certificate, or a journal-acceptance prediction.

The new proof does not assume an unrestricted transverse-cone lemma. It uses quasiconcavity to exclude the known planar-type modes at every open codimension-two face, then obtains global rigidity from a Hessian-norm identity. A thin-tube Hessian energy estimate controls the faces of codimension at least three using only continuity of the gradient. Its two cutoff energies need not each vanish; their product does. This is the substantive analytic step beyond the earlier restricted cone result.

## Exact originating conjectures and prior inputs

[Andrews--Clutterbuck--Hauer, Cambridge Journal of Mathematics 8 (2020), 243-310](https://doi.org/10.4310/CJM.2020.v8.n2.a1), final Section 10, asks for eventual log-concavity on every bounded convex domain (Conjecture 1, printed p.306) and nonconvex ground-state superlevel sets at all sufficiently small positive parameters on every convex polyhedron of dimension at least three outside products of circumsolids (Conjecture 2, printed p.307). Both exact final statements were read. The arXiv history retains v2, February 20, 2018, as its latest listed version.

The current result matches Conjecture 2's quantifiers: every fixed domain in that class, every dimension at least three, and every parameter in a domain-dependent interval (0, alpha0). It imposes no cone angle condition, symmetry, simplicity of vertices, or assumed nonzero eligible corner mode. Its proof first handles the inconsistent-normal case by the existing ACH argument; only the remaining consistent-normal case uses the new energy argument.

The Robin perturbation, quadratic classification (final Corollaries 8.2--8.3), spherical Neumann lower bound and equality classification (Theorem 9.1), inconsistent-normal obstruction, and planar odd-mode argument are prior work and are credited. The local mode expansion is explicitly referenced to arXiv v2 Proposition 4.4 because numbering changed in the final paper. The full Section 9 arguments and the relevant spectral proof were read in the primary v2 text, with final statements and selected final passages checked. The complete 68-page final article was not independently re-proved.

The new edge lemma gives its own uniform Taylor and reflection argument. It does not rely on an unproved reading of the abbreviated ACH Theorem 9.4 after affine subtraction, and it proves quadraticity only for degree-two modes on wedge-times-Euclidean cones, where a direct tangential-derivative argument suffices.

## Regularity sources

[Maz'ya, Comptes Rendus Mathematique 347 (2009), 517-520](https://doi.org/10.1016/j.crma.2009.03.001) supplies the bounded-gradient estimate for homogeneous Neumann problems on bounded convex domains with forcing in Lq, q greater than dimension. The complete four-page final note and the complete eight-page arXiv v2 preprint were read. The final note states the theorem and applications but omits the full proof; the longer preprint contains the proof. Local copies and hashes are retained. The manuscript derives uniform gradient convergence of the cone expansion using this theorem, polynomial eigenfunction bounds, and an elementary eigenvalue-counting bound. It does not infer C1 from a W2,p estimate with an unavailable p greater than dimension.

[Tolksdorf, Calculus of Variations and PDE 59 (2020), 154](https://doi.org/10.1007/s00526-020-01811-8), final Section 4, recalls the scalar convex homogeneous-Neumann H2 estimate and convex approximation argument. This is the input used here; no Stokes theorem is used. Dauge's published wedge theorem remains the regularity input for the earlier polygonal analytic-coefficient result. These standard results are dependencies, not new claims of the present manuscript.

## Current comparison and priority limits

[Edelen--Li, arXiv:2608.17194v1](https://arxiv.org/abs/2608.17194v1), August 17, 2026, is a relevant recent comparison located during the current audit. Its complete introduction, main assertions, tensor cutoff argument (Lemma 2.5), product-cone argument (Lemma 3.3), and local regularity statement (Theorem 3.5) were read. The checked history lists v1 only. Its sharp spectral and C2 regularity theorem assumes non-obtuse dihedral angles; it does not state the general Robin quasiconcavity theorem proved here. Its bounded-tensor logarithmic-cutoff method and tangential product differentiation are closely related standard steps and are acknowledged. We do not use its sharp spectral theorem, and its full proof was not independently audited. The present higher-codimension estimate and use of the Hessian norm allow potential unboundedness there; quasiconcavity supplies edge regularity even for obtuse edges.

[Crasta--Fragala, Cambridge Journal of Mathematics 9 (2021), 177-212](https://doi.org/10.4310/CJM.2021.v9.n1.a3), and [Ye--Zhang, arXiv:2609.06223v1](https://arxiv.org/abs/2609.06223v1), September 5, 2026, establish eventual concavity for smooth uniformly convex domains, with the latter reaching C3,1 regularity. Their hypotheses exclude the polygonal counterexamples. The complete relevant preprint introductions and main statements were read. The final Crasta--Fragala full text was not successfully opened; institutional final metadata and abstract were checked. Their proofs are not dependencies of the present paper. No claim of a single smooth-domain large-parameter counterexample is made.

Targeted searches on September 15 covered Robin quasiconcavity, the exact conjecture, circumsolids, Neumann quadratic rigidity, polyhedral Hessian identities, corner singularities, analytic coefficient persistence, and current 2025--2026 work. No competing full quasiconcavity solution or prior analytic-persistence disproof was identified in the inspected sources. This is a bounded search; unindexed, unpublished, or overlooked work remains possible. The newly located Edelen--Li preprint is included precisely because a narrow search of Robin titles alone would miss related methods.

## Publication and significance boundaries

Revision 1.1 added persistent prism nonquasiconcavity; revision 1.2 added a cone theorem under strict-dual and face-angle restrictions. Those revisions did not solve the full polyhedral conjecture. Revision 2.0 adds the global proof and supersedes that limitation. All these contributions remain one paper, P44; no corollary or revision increases the publication count.

Resolving both published ACH conjectures is a substantial manuscript-level advance with a concrete global rigidity mechanism. The originating conjectures concern an active specialized spectral-geometry problem. The present evidence does not establish that they meet the user's broader standard of an extraordinarily well-researched conjecture, comparable in reach to the major general conjectures motivating the program. That separate goal is therefore not automatically marked complete by this revision. Independent expert proof and priority review remains outstanding.

The unrestricted transverse-cone assertion of ACH Remark 9.6 is still a local frontier. The sharp Robin fundamental-gap problem is also unresolved here. Neither the PDF build, MathJax parsing, public byte checks, nor the internal AI audit is evidence that these other questions are solved.
