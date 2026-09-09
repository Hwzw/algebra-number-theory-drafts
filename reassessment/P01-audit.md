# P01 fresh audit and structural reassessment

Date: 2026-09-08. This is a fresh assessment for the revised five-paper goal. Earlier internal passes are not treated as evidence of significance by themselves.

Reviewed original file: `papers/P01-lefschetz-classification/manuscript.tex`, SHA256 `e87454ba80b976b38e6c53dc4e5a3bb97ef5d724e6abda3f1465b94491699f3c`. That file was not edited.

**Assessment:** the original classification proof is correct and resolves an explicitly published recent conjecture. Its proof is short and elementary once the right subalgebra is noticed; it should not be described as technically deep merely because the statement was open. A fresh reconstruction found a substantially more useful exact module splitting. That splitting gives integral diagonal forms for every Lefschetz power, all-characteristic ranks and Jordan data, every failure degree/power in characteristic zero, and sharp characteristic thresholds. These belong in one coherent replacement manuscript. They materially strengthen the case for a specialized research paper, but do not establish broad field-changing significance or external priority.

## 1. Independent reconstruction of the original proof

The monomial basis consists of x_S y_T with S a face and S∩T empty. Its existence works over Z, hence every field.

1. Setting z_i=x_i+y_i gives z_i²=0. The map B_n→A is injective because its pure-y coefficient matrix is the identity. Pairwise difference products give a nonzero multiplication kernel in degree ceil(n/2); the formulas work in characteristic two as well.
2. A face of size c gives the displayed differentiation product of degree floor((n+c)/2). Its monomials survive and are distinct. The sum of derivatives annihilates it. On squarefree monomial bases this operator is the transpose of multiplication; the manuscript correctly avoids calling it a quotient derivation.
3. Nonzero degree-t quotient A/(L) forces all earlier quotient degrees nonzero. Combining that cokernel with the universal kernel proves non-maximal rank of one and the same map. The parity inequalities are correct.
4. The support filtration in the positive cases is valid. A block-triangular map whose corresponding diagonal blocks are all injective (respectively all surjective) is injective (respectively surjective). The shifted Boolean thresholds line up exactly for r≤1 and for odd n,r≤2.
5. In the remaining strong-Lefschetz negative case n=2m+1,r=2, the degree-m product is killed by L². The differentiated degree-(m+2) witness is nonzero, including m=1; the unused vertex makes multiplication by y_v valid. Hence both kernel and cokernel are present.
6. The monomial coefficient-torus argument, including descent from the algebraic closure for finite fields, is sound. The use of real inner products to prove integer-matrix characteristic-zero ranks is legitimate.

No mathematical error was found in the original manuscript. These checks do not depend on its existing verification script.

## 2. Exact published target and current source checks

The **published** Holleben–Nicklasson article was obtained from the institutional repository, not only from an abstract: [journal PDF](https://diva-portal.org/smash/get/diva2%3A2053155/FULLTEXT01.pdf). It is saved as `reassessment/sources/Holleben-Nicklasson-published.pdf`, with extracted text beside it. It has 20 pages, was available online March26,2026, and is JPAA230(2026),108238, DOI[10.1016/j.jpaa.2026.108238](https://doi.org/10.1016/j.jpaa.2026.108238).

Conjecture1.3 (p.3) and Conjecture3.15 (p.10) assert WLP failure for the square-zero whiskered graph algebra when α(G)≥3. Theorem3.10 supplies the face-dependent cokernel; Corollary3.12 covers α(G)≥n/3+2. Remark3.16 records the seven-vertex checks and explicitly says injectivity must also be considered. Propositions3.2/3.5 supply the known positive graph cases. Theorem4.6 gives the older idealization obstruction. These statements match the references used in P01.

[Author arXiv v2](https://arxiv.org/html/2502.00155v2) was also inspected, as was [Cooper–Faridi–Holleben–Nicklasson–VanTuyl v2](https://arxiv.org/html/2306.04393v2), Theorem1.2. The latter proves endpoint ranks in odd characteristic and lower-half injectivity in characteristic zero; it does not contain a complete classification.

## 3. Zeng and novelty limits

The primary [SSRN record](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7385138), DOI[10.2139/ssrn.7385138](https://doi.org/10.2139/ssrn.7385138), identifies Zijian Zeng's *The Whiskered-Graph Weak Lefschetz Conjecture for Graphs on Eight Vertices*, posted September3,2026, written September1,2026, three pages. Its abstract describes an eight-vertex computation, reduced to 6,021 isomorphism classes of independence number three, with explicit kernel certificates. It does not announce the general theorem or an operator splitting.

The actual SSRN PDF could not be obtained: the official delivery URL returned HTTP403 in a direct read-only download, and browser retrieval failed. The saved response `sources/Zeng-7385138-response.dat` is HTML, **not a PDF**. Therefore no claim is made to have audited Zeng's full proof, citations, or code. Its abstract-level scope is accurately described, and its priority in the eight-vertex case should be credited.

Fresh searches combined the conjecture title, author names, “whiskered” with “Jordan type”, “positive characteristic”, “direct sum”, “square-zero”, and “Lefschetz classification”. The [author's current research page](https://hollebenthiago.github.io/research/) was inspected as a further primary chronology check. No primary source for the full classification or the splitting was located. This is evidence of a bounded search, not a guarantee of novelty against unindexed or unpublished work.

## 4. Stronger mechanism found during this audit

The change z_i=x_i+y_i preserves the local ideal exactly:

    (x_i²,y_i²,x_i y_i) = (x_i²,z_i²,x_i z_i)

in the changed coordinates, over Z. But L becomes Σz_i. Consequently

    A_Z ≅ ⊕_{S∈Δ} B_{n−|S|}(-|S|)

as graded Z[L]-modules. This is an actual simultaneous splitting for all powers, rather than merely a filtration or a Hilbert-series identity. It is the new central statement in `P01/extension.md`.

The full extension proves:

- an explicit integral diagonal form for every L^e, using the classical Wilson theorem;
- all-characteristic ranks from face numbers, including all modular rank drops;
- the exact characteristic-zero maximal-rank condition 2i+e≤n or 2i+e≥n+r, for 0≤i<i+e≤n;
- the sharp WLP characteristic threshold p>ceil(n/2) in the combinatorial positive cases;
- SLP exactly for r≤1 and characteristic zero or p>n;
- ordinary and graded Jordan type in every characteristic, and recovery of the f-vector from ordinary Jordan type in characteristic zero;
- a larger family of standard Gorenstein idealizations failing WLP, with the G-quadratic graph case credited to its known structural theorem.

The integral diagonal form for Boolean inclusion matrices is **not** new. The primary reproving paper [Ghorbani et al., Corollary3](https://arxiv.org/pdf/0709.3144) was read, including its explicit credit to Wilson/Bier and unimodular proof. The source is saved locally. The new claim is the exact reduction of these whiskered-algebra operators to those classical matrices. The elementary Frobenius obstructions and the known r=1 SLP sufficient condition are also credited as existing/routine ingredients.

## 5. Independent exact evidence for the extension

`P01/check_extension.py` builds each L^e directly in the **original x/y monomial basis**, using monomial containment times e!. It does not assume or use the new z-basis to construct matrices. Exact Gaussian elimination modulo2,3,5,7,11 is compared against the formula.

All 6,905 matrix-rank comparisons passed, covering every simplicial complex with the full vertex set for n≤4 (1,2,9,114 complexes respectively), plus ten selected complexes on5/6 vertices. Every degree and positive power was checked, along with the exact WLP and SLP criteria. `P01/check-results.json` records the result. These computations support the hand proof; they do not establish the unbounded theorem.

## 6. Significance and selected-paper judgment

The original argument is a short solution of a current specialized conjecture, not a long technically hard proof. The structural extension gives it a more substantial identity: a full integral operator description with exact characteristic and Jordan consequences. It removes the graph-size and independence-ratio limitations in current results and makes the generic Jordan problem insensitive to incidences beyond the f-vector. The downstream idealization theorem produces new G-quadratic Gorenstein WLP failures through an existing construction.

My recommendation is to retain P01 among serious candidates for the revised five-paper collection, provided the extension receives independent review and is incorporated into one coherent manuscript. The positive-characteristic corollaries should not be marketed as independent hard discoveries, and the unresolved SSRN full-text comparison should remain disclosed in the assessment. A claim that this meets an unspecified universal standard of “truly significant/hard” cannot be certified by another internal pass. Its defensible standing is a plausible substantive specialized commutative-algebra paper, based on a named open problem and a reusable operator decomposition.
