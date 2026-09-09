# Open-status and contribution assessment

Author: Henry Zweiman. Audit date: September 9, 2026.

## Exact question

Richard Stanley's [MathOverflow question 461829](https://mathoverflow.net/questions/461829/), Addendum 2 dated January 29, 2024, explicitly asks for an analytic estimate of the average number of unit-circle zeros of reciprocal polynomials

$$N_S(x)=1-(1-x)\sum_{j\in S}x^j$$

with maximum element of S fixed and odd. This is also referenced in the aside on printed page 9 of [Some enumerative applications of cyclotomic polynomials](https://doi.org/10.54550/ECA2026V6S1R4), ECA 6:1 (2026), Article S2R4.

The live question inspected on the audit date had two answers: Silverman's Salem-polynomial observation and Pasten's lower bound of two unit-circle roots. Neither provides the requested asymptotic. The published 2026 source still presents the phenomenon without this explanation.

## Contribution

The manuscript proves that the expected fraction is asymptotic to 1/sqrt(3), and establishes the corresponding mean angular measure. It answers this particular average-count question. The exact independent-sign parametrization, zero-law symmetrization of the fixed term, and endpoint estimate connect the constrained integer family to an applicable general theorem.

The contribution is an application of established probability and discrepancy results. It is not a new universality theorem. The constant 1/sqrt(3) itself is classical. Gaussian reciprocal-polynomial analogues and random cosine polynomials were already known to have this limiting fraction. The constrained discrete ensemble and its fixed boundary terms require the verification supplied here.

## Closest sources and distinctions

- [Nguyen and Vu](https://arxiv.org/abs/1711.03615), American Journal of Mathematics 144 (2022), 1–74: the general real universality theorem is the principal input. Conditions C1/C2 and Lemma 9.2 are verified on the exact basis in the paper. No direct invocation of their special trigonometric theorem with missing frequency hypotheses is made.
- [Edelman and Kostlan](https://arxiv.org/abs/math/9501224), Bulletin AMS 32 (1995), 1–37: supplies the Gaussian zero-density formula for differentiable function bases. The covariance calculation is carried out in this paper.
- [Soundararajan](https://arxiv.org/abs/1802.06506), American Mathematical Monthly 126 (2019), 226–236: supplies deterministic angular discrepancy, used only for the original bounded-coefficient integer polynomials.
- [Conrey, Farmer, and Imamoglu](https://arxiv.org/abs/0812.1752), Proceedings AMS 137 (2009), 1835–1839: explains prior random-cosine and reciprocal-polynomial connections and general lower bounds. It does not state Stanley's later constrained-ensemble asymptotic.
- [Pirhadi's pairwise equal-block paper](https://arxiv.org/abs/1905.13349) and [palindromic-block paper](https://arxiv.org/abs/1908.08154): inspected as nearby models. These concern Gaussian block dependence and do not supply the discrete constrained-family argument claimed here.

## Search scope and limits

The September 9 search used the exact question title, question identifier, Stanley's name with reciprocal polynomials/average zeros/universality, the cyclotomic-paper title, and dependent random trigonometric-polynomial terminology. It inspected Stanley's current question and published article, the general universality source, the Gaussian formula, the discrepancy source, and nearby random-polynomial literature.

No inspected source supplies this explicit answer. This bounded search does not establish exhaustive historical priority. No independent human referee or separate-agent review has occurred. The result is a complete internally checked proposed solution, with priority and significance provisional.

## Significance and scope

The value is a precise answer to a named research question at the intersection of integer polynomials, cyclotomic enumeration, and random-function universality. The representation may support later work on fluctuations, irreducibility, and noncyclotomic roots. No predicted citation count is evidence of significance.

This is one consolidated paper. The angular-measure theorem and the product-count corollary do not create extra paper counts. The paper does not solve the classification of cyclotomic sets or the complete-intersection conjecture for cyclotomic numerical semigroups. It also does not prove a law of large numbers, a variance asymptotic, or an effective global error rate.
