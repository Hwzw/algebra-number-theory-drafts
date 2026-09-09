# P13 final manuscript transfer review

Date: 2026-09-08.
Independent reviewer: commutative-algebra agent.
Artifact: `research_program/selected_papers/P13-nilperiod-rings/manuscript.tex`.

**Verdict: PASS. No mathematical gap or required correction found.** I read the entire frozen TeX source, checked all statements against the independent extension audit and the earlier finite-ring/Corbas audit, and verified the artifact hashes. I did not edit the manuscript or rerun the already completed exhaustive checks.

## Frozen artifact identity

- Source SHA-256: `a2eed3bf0b458dd20c9e5b182d3db8d0016e17de4154a11fd9a8f3b182ecfe41`.
- PDF SHA-256 observed at review: `3ca14c1096e67407fd20f656024de51469220a64f60fbeed0335ebbd804b24b3`.
- The compilation log reports five pages and contains no TeX error markers, warnings, overfull boxes, or underfull boxes.

This signoff applies to the exact source hash above. It covers mathematical transfer, attribution, and artifact identity; visual PDF QA remains separate.

## Main theorem and radical consequences

The title and abstract accurately state the strengthened result: each individual additive period of any positive-integer power map belongs to the prime radical of any associative ring, with no identity, characteristic, finiteness, or PI restriction.

The proof reproduces the audited highest-nonzero-power argument correctly. Evaluation at zero gives a^n=0; a nonzero period has index 2≤j≤n. For b=a^(j−1) and x=br, r in the unitization, the relation ax=0 removes exactly the forbidden noncommutative words. The displayed sum has every exponent valid, and multiplication by a^(j−2)r leaves exactly x^n. The j=2 case is explicitly handled by interpreting a^0 in the unitization. Thus the actual nonzero right ideal bS^1 has uniform index bound n, to which the correctly stated classical lemma applies. Only inputs in S are used. The image of the particular period in R/P(R) remains a period, without any incorrect assumption that arbitrary quotients of nilperiod rings are nilperiod.

The corollary Nil(R)=P(R), local nilpotence, largest-nil-ideal assertion, and NI conclusion follow correctly. The statement that local nilpotence does not provide a global nilpotency exponent is accurate, as is the deliberate absence of a claim that every principal two-sided nilpotent-generated ideal is nilpotent. Such ideals are nil because they are contained in P(R).

## Classical citation scope

The manuscript explicitly identifies the bounded-index lemma as classical, separates it from the new substitution, and gives the exact Bell–Martindale pointer, printed p.93, preliminary item (V). Its left-ideal statement gives the required right-ideal version by the opposite-ring argument, which is explicitly stated. No Noetherian, torsion-free, field, or identity hypothesis is being suppressed. Nielsen Section 1 supplies the accompanying bounded-nilradical and local-nilpotence facts, including the nonunital discussion. These points were verified directly from the primary PDFs in `P13-extension-independent-review.md`.

The bibliography gives the correct Bell–Martindale authors, title, journal coordinates, and DOI. Nielsen's authorship, title, journal coordinates, and DOI agree with the primary-source bibliographic checks. The manuscript no longer presents the stronger argument as an entirely elementary self-contained proof: the abstract and proof discussion correctly acknowledge the classical external lemma.

## Finite-ring section

Every statement transfers correctly from the earlier audit:

- The central-idempotent proposition uses the square-zero elements er−ere and re−ere and the distinct idempotents e and e+a. No commutative-ring assumption occurs.
- Every element of a finite ring has an idempotent positive power, by eventual periodicity and a sufficiently large multiple of the eventual period.
- The finite classification is explicitly for nonzero finite unital rings, with the zero ring addressed separately as the empty product.
- Splitting central idempotents terminates, direct factors inherit the relevant nilperiod identities, and each factor's nonunits are exactly its nilpotents, a proper ideal. This proves locality.
- Conversely, in a finite local ring all nonunits are nilpotent. A common exponent dominates all nilpotency indices and is divisible by the unit-group exponent, producing the required power map. Translation by the nonunit ideal preserves its two cases. The finite-product argument chooses one exponent for all factors.
- The upper triangular 2-by-2 F2 example correctly disproves NI⇒nilperiod.

The added attribution to Han–Lee–Park makes clear that the decomposition of Abelian semiperfect rings into finite products of local rings is standard. I independently verified the authors, title, publication coordinates, DOI, and meaning of Abelian on the [primary publisher page](https://journal.hep.com.cn/fmc/EN/10.1007/s11464-016-0586-z). The publisher's indexed primary PDF text on printed p.123 explicitly uses Proposition 2.6 for exactly the assertion that an Abelian semiperfect ring is a finite product of local rings. This supports the cited scope and proposition number. Direct full-PDF retrieval during this final review returned a no-download-permission response, so I do not claim to have newly inspected the full proposition page. This is an access limitation, not a mathematical gap: the manuscript supplies the complete proof in the finite setting.

## Corbas theorem and source comparison

The finite-field parameters f≥1 and 0≤s<f are specified, including the identity twist with gcd(f,0)=f. The ring multiplication, inverse, local structure, and nilpotent ideal are correct.

The coefficient C_n(a) is the correct noncommutative power coefficient. Periods must be nilpotent by evaluation at zero. The proof treats a=0, nonzero fixed-field elements, and nonfixed elements separately; hence it does not repeat the invalid geometric-quotient step at fixed points in the source example. The exact period criterion is p(q−1)/(p^g−1) dividing n, and the full period group is either N or zero as stated.

The unit-group exponent is exactly E=p(q−1), and equality of power maps for exponents at least two is exactly congruence modulo E. Counting the qualifying exponent classes yields p^g−1 periodic maps. The identity power map is separately excluded and distinguished on nonzero N. The smallest twisted F4 example is correct. These are precisely the formulas previously audited symbolically and through 243 independent finite power-map checks; no changes requiring those computations to be repeated were found.

The comparison accurately names Burnette's published Example 2.2 and Table 1, which contain the contradicted nonidentity-twist assertion. It does not imply an acknowledged erratum or attribute intent. The bibliography cites the final 2025 journal paper and separately identifies the older arXiv title. The introduction correctly distinguishes the published Conjecture 2.6, PI-algebra Theorem 2.9, and matrix-ring Lemma 2.8. It claims the stronger inclusion and its consequences, not a solution of the broader weakly-periodic-ring problem.

## Final assessment

The frozen manuscript is mathematically consistent with the independent proof and source audits and presents one coherent strengthened paper. No unsupported extension was introduced during transfer. Literature search remains the bounded novelty audit already documented, not a guarantee of publication priority or acceptance. The manuscript is ready for the parent's final visual QA and selection decision.
