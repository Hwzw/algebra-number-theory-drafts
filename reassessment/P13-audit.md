# Fresh reassessment of P13: nilperiod rings

Date: 2026-09-08. Reviewer: `/root/review_groups`.

This is a new proof and literature audit under the revised requirement of five substantial papers. It does not reuse the former admission verdict. No manuscript was modified.

## File actually audited

`research_program/papers/P13-nilperiod-rings/manuscript.tex`

SHA-256: `ec153cc90dbfa1778ea3b449356f9addee126289f0629e3b0bfdf0416d1fd466`.

The shortened path `papers/P13-nilperiod-rings/manuscript.tex` does not exist at the workspace root; the file above is the research-program manuscript. A separate publication copy also exists under `github-publication/`, but is not the subject of this audit.

## Main conclusions

1. The existing mathematical proof is correct, including rings without identity and arbitrary characteristic.
2. The finite classification is a modest consequence of central idempotents and standard semiperfect-ring decomposition, and its main structural ingredient needs additional attribution.
3. The Corbas calculation is a useful correction and a short exact computation, not evidence of a difficult broad advance.
4. The NI conjecture is genuinely stated in the cited source, and the inspected older NR-ring theory does not subsume its general solution. Nevertheless, the existing elementary NI argument and two auxiliary results do not by themselves justify a confident description as one of five hard, truly significant advances. It is a plausible short specialist note; the source is a recent narrowly posed conjecture, and I found no evidence that it is a major or long-standing field obstacle.
5. A stronger theorem emerged during this fresh audit: **in every associative ring, each additive period of every power map belongs to the prime radical.** Consequently every nilperiod ring is 2-primal and its nilpotents form a locally nilpotent ideal. The complete proof and exact external lemma are in [P13-extension.md](P13-extension.md), which is undergoing independent review. This supplies a substantially better mathematical center for a revised paper, although it is still a concise application of classical radical theory and must be described honestly.

## Independent reconstruction of the current proof

For a square-zero period a of exponent n and x=ar, the identity ax=0 leaves only x^n and x^(n-1)a in the expansion of (x+a)^n. Its period property gives x^(n-1)a=0, and multiplying by r gives (ar)^n=0. This works for r in a unitization because x=ar still belongs to the original ring. No period property of the unitization is assumed.

For each u,v in the unitization, the identity (uav)^(n+1)=u(avu)^n av shows that every two-sided multiple is nilpotent. Additive closure of nilpotents follows directly from (b+a)^n=b^n and b being nilpotent, so every finite sum of those multiples is nilpotent. Thus the principal two-sided ideal is nil. Importantly, the argument proves pointwise nilpotence, not a common nilpotency exponent for all its elements.

For a general nilpotent a of index j, induction applies to a^2, whose index is at most ceil(j/2). The ideal (a^2) is nil, so nilpotents of the quotient lift to nilpotents of the ring and the quotient remains nilperiod. The image of a is square-zero. Its generated ideal is nil in the quotient, and a nil extension of a nil ideal is nil elementwise: y^m in I and (y^m)^t=0 imply y^(mt)=0. The induction is valid over all nilperiod rings simultaneously, including the smaller quotient ring, and is not circular.

The central-idempotent argument is also correct. For e^2=e, the elements er-ere and re-ere are square-zero, and adding either to e produces an idempotent. A period identity at e therefore forces each to vanish. This proves that R is Abelian in the standard ring-theoretic sense: all idempotents are central. It does not prove that multiplication in R is commutative.

The finite unital decomposition then works. A finite monogenic multiplicative semigroup contains an idempotent power. Splitting by central idempotents gives components with only zero and one idempotents; each element is therefore a unit or nilpotent. The NI result makes the nonunits an ideal. Conversely, in a finite local ring every nonunit is nilpotent and a sufficiently large multiple of the unit-group exponent sends nonunits to zero and units to one. Translation by a nonunit preserves this distinction. A common exponent works for a finite product.

The Corbas formula is accurate. The second coordinate of (a,b)^n is b times the geometric sum C_n(a). A nonzero additive period must have first coordinate zero, and it exists exactly when C_n vanishes everywhere. At a=1 this forces p|n; away from the fixed field the condition is that every a/phi(a) have nth power one. That image group has order (q-1)/(p^g-1). The group exponent p(q-1) distinguishes the eventual power maps, while all nonunits square to zero. The count p^g-1 and the separate identity-map exception follow. No omitted characteristic-two or identity-twist case was found.

## Source and subsumption findings

### Burnette: actual source scope

The [published 2025 article](https://gradmath.org/wp-content/uploads/2025/07/GJM2025-Burnette.pdf) explicitly states Conjecture 2.6 and proves the PI-algebra case in Theorem 2.9. Its preceding matrix lemma and its Corbas example were inspected. The final paper, not the earlier characteristic-zero-only preprint statement, is the right comparison. The manuscript makes that distinction correctly. The finite case of NI was already observed there; the current finite classification should not be presented as though its NI ingredient were previously unknown.

### Additive closure and NR-ring theory

[Janez Šter, *Rings in which nilpotents form a subring*](https://arxiv.org/abs/1510.07523), Carpathian J. Math. 32 (2016), 251-258, DOI [10.37193/cjm.2016.02.13](https://doi.org/10.37193/cjm.2016.02.13), proves that additive closure of nilpotents already implies their multiplicative closure (Theorem 2.6 in the inspected preprint). It does not imply that they form an ideal: Remark 3.2 gives F<x,y>/(x^2), whose nilpotents form a square-zero subring but whose yx is not nilpotent. Thus the elementary additive-closure observation in P13 only supplies NR, and the additional period-based ideal argument has real content. The exchange/bounded-index hypotheses in Šter's NI result are absent from P13 and cannot silently be imported.

### Finite classification is based on an established structural equivalence
+[Juncheol Han, Yang Lee and Sangwon Park, *Structure of Abelian rings*](https://journal.hep.com.cn/fmc/EN/10.1007/s11464-016-0586-z), Front. Math. China 12 (2017), 117-134, Proposition 2.6, states that an Abelian unital ring is semiperfect exactly when it is a finite direct product of local rings. The [primary PDF](https://journal.hep.com.cn/fmc/EN/PDF/10.1007/s11464-016-0586-z) also traces this to standard local-idempotent decomposition. Finite rings are semiperfect. Hence once the one-line nilperiod-to-central-idempotent argument is given, the forward classification is a standard structural application. The reverse direction is the elementary finite unit/nonunit exponent argument. It remains a useful complete characterization, but is not a second deep contribution.

### The stronger radical result and its dependency

The fresh extension uses the bounded-index one-sided nil-ideal lemma of Levitzki, not the Noetherian nil-ideal theorem. [Bell and Martindale, 1987](https://doi.org/10.4153/CMB-1987-014-x), printed page 93, preliminary item (V), gives the unrestricted left-ideal statement and its semiprime consequence. [Nielsen's primary author PDF](https://mathdept.byu.edu/~pace/BoundedNilradical_web.pdf), Section 1, explicitly treats the bounded nilradical and its inclusion in the prime radical without requiring an identity. Full hypotheses, proof application, and nonunital details are recorded in the extension note.

The decisive strengthening is not a claim that all NR or NI rings are 2-primal. It is the direct statement about individual power-map periods. Passing their identities to a semiprime quotient and using the highest nonzero power isolates a bounded-nil principal right ideal. The proof does not need to assume that arbitrary quotients are nilperiod.

### Search limits

Fresh exact-term searches for nilperiod rings, the NI conjecture, power-map additive periods, semiprime rings, and the prime radical did not locate a later resolution or a directly subsuming older result. Search discovery was checked against primary texts where relevant; database labels and snippets were not treated as proof of open status. Older work about multiplicative power-map identities or derivations satisfying power identities has different hypotheses. This audit does not establish global priority, and the low visibility of the terminology makes negative search evidence especially weak.

## Recommendation under the five-paper goal

Do not carry forward the former automatic admission of the NI-only manuscript as proof that the revised significance goal is met. Preserve it as a correct short note and replace its center only if the new prime-radical theorem survives independent review. A revised manuscript should lead with the theorem for individual periods in arbitrary rings, derive 2-primality and local nilpotence, credit the classical bounded-index lemma, retain the finite classification as an attributed corollary, and place the Corbas correction as an application.

The stronger formulation is a credible research candidate because it both settles the named conjecture and gives a general restriction on power-map translations beyond nilperiod rings. It is still a short proof built on an old radical theorem. Whether that clears the user's deliberately high threshold requires comparison against the other candidates and, ideally, specialist external assessment; internal proof checks alone cannot certify that a paper is hard or truly significant. No claim of such certification is made here.
