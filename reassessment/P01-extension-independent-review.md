# P01 extension: fresh independent proof audit

Date: 2026-09-08. Reviewer: `/root/review_finite_fields`.
Target: `reassessment/P01/extension.md`, Theorems A–D, Corollaries B1/C1/E/E1, Proposition F.

**Verdict: mathematical pass for the stated family and for Proposition F in its stated negative graph cases.** I reconstructed the arguments, checked the primary inputs, and wrote a fresh checker using the original monomial basis. This is independent of earlier portfolio reviews and the author's checker. It is not a novelty certification or a publishability decision. The original 1990 Wilson article was not obtained; its exact theorem was checked in a primary reproving paper.

## 1. Integral splitting

The change `z_i=x_i+y_i` is invertible over the integers. Both inclusions of the transformed local ideal follow from the four displayed identities, including in characteristic two: neither division by two nor semisimplicity is used. The nonface ideal in the x variables is unaffected. Thus `x_S z_T`, with `S` a face and `T` disjoint from `S`, is indeed a monomial basis.

Multiplication by any z variable fixes the x support. For fixed S the surviving z monomials are exactly a square-zero complete intersection on its complement. This proves an actual simultaneous direct-sum decomposition of the graded operator module, over Z, with the claimed shift. It does not prove an algebra direct-product decomposition, and the author correctly avoids that claim. This is the essential structural observation on which all subsequent formulas rest.

The setup requires that every singleton is a face. It explicitly has full vertex set [n], n≥1, so `f_1=n` and `r≥1` are legitimate. Results using singleton blocks would need adjustment if ghost vertices were allowed.

## 2. Wilson input, orientations, and factorials

I read Corollary 3 and its proof in Ghorbani–Khosrovshahi–Maysoori–Mohammad-Noori, [Inclusion Matrices and Chains](https://arxiv.org/pdf/0709.3144), PDF page 10, printed page 9. Its range is `0≤t≤k≤v−t`; the diagonal entries are `C(k−j,t−j)`, with multiplicities `C(v,j)−C(v,j−1)`, for `0≤j≤t`. The proof uses unimodular integer matrices, rather than merely equivalence over the rationals. Consequently it supports integral cokernels and reduction modulo every prime. The diagonal is not asserted to be in divisibility order, and must not be called a Smith normal form without further operations.

For a Boolean block, the matrix of `U^e` is exactly `e!` times the transpose of the subset inclusion matrix: each selected e-subset occurs in e! orders and all repeated-index terms vanish. When `2q+e≤a`, use `(t,k)=(q,q+e)`. Otherwise complements and transpose give `(t,k)=(a−q−e,a−q)`. Both satisfy Wilson's complete range, including its equality boundaries. This gives `t=min(q,a−q−e)` and the stated diagonal `e! C(t+e−j,e)` with the correct multiplicities.

Multiplying a unimodular equivalence by the scalar e! preserves that equivalence and scales its diagonal. Thus the factorial cannot be discarded in small characteristic. The rank formula retains it correctly; in particular all powers with `e≥p` vanish in characteristic p. Source or target degrees outside a Boolean block contribute only zero columns or rows. Direct sums account for those independently, so the rectangular zero portion and cokernel free part are correct.

As a small diagnostic, in B_4 the degree-one to degree-three map U² has diagonal entries 6 once and 2 three times. Its rank is zero in characteristic two and three in characteristic three. The formula has both behaviors.

## 3. Exact maximal-rank region

A shifted block of face size s has symmetry center `(n+s)/2`. Its degree-i and degree-(i+e) dimensions have the asserted strict comparison on either side of `2i+e=n+s`. This comparison includes zero-source and zero-target boundaries. In characteristic zero the Boolean rank is the smaller dimension.

Therefore `2i+e≤n` makes every block injective, and `2i+e≥n+r` makes every block surjective. In the intermediate range the empty-face block has a strict dimensional kernel. Set `h=2i+e−n`. The assumptions imply `0<h<r` and `h≤i`; a face of size `h+1` exists by downward closure. Its target is nonzero. If its source vanishes this immediately gives a cokernel; otherwise its source dimension is strictly smaller than its target dimension. The independent direct summands make both defects persist in the full map. This proves both necessity and sufficiency without a cancellation issue.

Putting e=1 gives exactly `ceil(n/2)≤i≤floor((n+r)/2)−1`. The interval is empty precisely for r=1 or for n odd and r≤2. For SLP the only extra combinatorial case is n odd, r=2: writing `n=2m+1`, the map with `(i,e)=(m,2)` lies strictly in the mixed range. Since r=2 implies n≥3, its degrees are valid. This verifies all parity and endpoint cases.

## 4. WLP and SLP over arbitrary fields

The reduction from existence of some Lefschetz form to the particular L is valid. Diagonal changes of the original variables preserve the monomial ideal and identify all coefficient-torus forms. A nonempty maximal-rank open set intersects that torus over an infinite field. Over a finite field, pass to the algebraic closure for this implication, then use invariance of the ranks of the explicitly defined L under field extension. SLP requires only finitely many rank conditions in this finite algebra, so the same argument applies simultaneously to all powers.

The mixed-range failures are dimensional block obstructions and remain valid in every characteristic. For the additional WLP obstruction, `p≤ceil(n/2)` gives a nonzero element `L^(p−1)` in degree p−1, killed by L. Nonvanishing follows from the empty-face block and the coefficient `(p−1)!`. Every shifted binomial difference in the claimed low range is nonnegative. The empty block gives strict growth except at the odd central boundary, where singleton blocks give it. Thus this is a kernel in a strictly dimension-increasing map, not a harmless kernel in a surjective range.

For WLP sufficiency, all e=1 diagonal entries are positive integers at most `ceil(n/2)`; hence their ranks are unchanged when p exceeds that threshold. The parity-specific bounds in the text are correct. For SLP, p≤n forces the noninjective zero map `L^p:A_0→A_p`, with nonzero target. When p>n every factor of every positive diagonal entry lies between 1 and n, so every power has its characteristic-zero rank. The sharp conditions in Theorem D follow, including n=1.

## 5. Jordan data

The second difference of total ranks counts ordinary Jordan lengths. The two-variable difference of graded ranks counts strings with a prescribed initial and terminal degree: a string [u,v] contributes to `r_ab` exactly when `u≤a≤b≤v`. Homogeneous Jordan strings exist for a finite degree-one nilpotent map over any field; no eigenvalue extension is needed.

In characteristic zero the Boolean symmetric strings have the displayed lengths, starts, and binomial-difference multiplicities. After the shift by s they occupy `[s+b,n−b]`. The unique longest string has length n+1. Equating the multiplicity of length n−s+1 gives the displayed triangular recurrence, whose coefficient on f_s is one. Hence ungraded Jordan type recovers n and the f-vector in characteristic zero. The text correctly restricts this recovery assertion to characteristic zero and does not assert integral Jordan strings.

## 6. Gorenstein application and a resolved source gap

Proposition F's operator argument is sound. Every surviving monomial of degree below n has an unused index whose y variable extends it. Since this is a monomial quotient, there is no additional socle obtained by cancellation. Thus A is level of socle degree n, its shifted dual is generated in degree one, and the idealization is standard graded Gorenstein with socle degree n+1.

In the negative cases, `d=ceil(n/2)` satisfies `n<2d+1<n+r`, giving nonsurjectivity on A in degree d for every linear form by the torus argument. WLP on T would force surjectivity from degree d to d+1: for n even the dimensions are equal by symmetry; for n odd the source is central and WLP unimodality makes it at least the next dimension. The quotient T→A would pass that surjectivity to A, a contradiction. This uses a quotient, not an unjustified restriction of a surjective map.

An earlier graph paragraph used Cohen–Macaulayness where shellability was needed and omitted the apolar identification hypotheses. I reported these issues; the current text resolves both. For `Ind(w(G))`, purity follows because every facet chooses exactly one element of each whiskered pair, flagness follows from being a graph independence complex, and shellability follows from Holleben–Nicklasson Theorem 2.1. For r≥2, an independent pair gives the genuine binomial relation `m_uv*m_empty=m_u*m_v`, while distinct monomials are linearly independent. Thus the simplicial form is Perazzo, and their Lemma 4.5 applies.

I checked these statements against the stored published Holleben–Nicklasson PDF (JPAA 230 (2026), 108238), including Theorems 2.1/4.4/4.6 and Lemma 4.5, and checked the underlying [D’Alì–Venturello Proposition 8.3](https://arxiv.org/html/2106.05051v2#S8). The latter requires a **pure flag** complex and characteristic zero, and identifies shellability with the quadratic Gröbner basis property. All these hypotheses hold here. The broader idealization obstruction method was already used in [Holleben–Nicklasson Theorem 4.6](https://arxiv.org/html/2502.00155v2); the present change is its enlarged exact range.

Minor scope clarification sent to the author: read the graph G-quadratic assertion as applying to the stated negative cases, or explicitly say “In these graph cases.” The supplied Perazzo argument uses r≥2. No classification of WLP for all these idealizations is proved or claimed.

## 7. Independent finite checks and limits of this verdict

The new script `reassessment/P01-extension-independent-check.py` imports neither author code nor previous review code. It enumerates all simplicial complexes containing all singletons on n=1,...,4. It constructs the original `x_S y_T` basis, applies the original multiplication rule repeatedly, and computes ranks by exact rational or modular Gaussian elimination. Separately it expands the new basis in the original one and checks integral intertwining identities.

The completed run reports:

```
PASS: 126 complexes on all vertex sets [n], n=1,...,4.
PASS: 7608 integral change-of-basis/multiplication intertwining identities.
PASS: 6005 direct all-power rank comparisons over Q,F2,F3,F5,F7.
PASS: all maximal-rank loci, WLP/SLP classifications, graded strings,
      modular length bounds, f-vector recovery.
```

These checks target independent matrix calculations and boundary cases; the proofs above establish arbitrary n and characteristic. They do not certify novelty. The Boolean diagonal theorem and characteristic-zero strings are classical, and the positive r=1 SLP case is already in Holleben–Nicklasson Proposition 3.2. The integral splitting plus its complete transfer of ranks is a coherent structural extension of the existing P01 candidate, not several separate new papers. A focused prior-art search for this splitting remains necessary before claiming it as new. Final manuscript incorporation, exposition audit, and visual QA are outside this extension-file signoff.

## 8. Selected manuscript transfer audit and frozen inputs

I subsequently read the entire selected manuscript source, including the abstract, every statement and proof, scope discussion, and bibliography. Theorem A transfers to Section 2; the integral diagonal and rank formulas to Section 3; the full locus to Section 4; sharp classifications to Section 5; Jordan data to Section 6; and the corrected idealization application to Section 7. No mathematical change or lost hypothesis was found. The WLP sufficiency proof is shortened using the valid bound t+1≤ceil(a/2)≤ceil(n/2). The idealization statement now says “these are G-quadratic”, resolving the scope clarification. All singletons and n≥1 are explicit at setup. The modular factorial and all range conventions are retained. **Final TeX mathematical/exposition transfer: pass.** Compilation and visual QA remain with the parent/author.

I independently located the primary SSRN record for [Zeng, The Whiskered-Graph Weak Lefschetz Conjecture for Graphs on Eight Vertices](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7385138). Its abstract confirms the eight-vertex scope, exact integer kernel certificates, author, and September 3, 2026 posting date. The manuscript makes only that limited description. The full PDF remains unavailable to this reviewer, so its proof and bibliography were not audited. No theorem in the selected manuscript depends on it.

Audited SHA-256 values (2026-09-08):

- `reassessment/P01/extension.md`: `6e940c42579450a2ac6a72be34dd6573c71a18620f6430a4707b7ee1a3c22126`
- `selected_papers/P01-lefschetz-classification/manuscript.tex`: `ebdabb763c8e6088bad906257f7be655c0a9b505971eb1b5b5f0a9d95219f6b9`
- `reassessment/P01-extension-independent-check.py`: `9fce2a22836f10f758d51e962a83bbfbe8287cd360f05af42c4cb5729dd787e5`

### Final layout-only revision

The author shortened the attribution paragraph immediately after the graph corollary to resolve an overfull line. I read the revised paragraph on 2026-09-08: it still credits the known characteristic-zero positive graph cases and complete-graph SLP sufficiency to Holleben–Nicklasson, identifies Frobenius as the necessity argument, and states the conjecture consequence accurately. The detailed proposition/conjecture citations remain in the introduction. This revision preserves the mathematical and attribution signoff. The final selected TeX SHA-256 is `6d797bebcb29dd4d3c017643b812e94b76260a43cb80aef2d94a8eff3ca05b50`, superseding the TeX hash above. No new computation was warranted.
