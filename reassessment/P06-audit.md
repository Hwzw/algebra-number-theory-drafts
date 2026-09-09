# P06 fresh mathematical and literature audit

Audit date: 8 September 2026. Audited file: `research_program/papers/P06-stirling-repair/manuscript.tex`, SHA-256 `342863fbc8b75f0099606d96f1b913500f6e5fa39b59490df3025356e50f59fb`.

**Recommendation: retain as a substantial specialist research candidate.** I reconstructed all main proofs and found no mathematical gap. The paper proves uniform statements about an existing repair-factor problem, including a quantitative asymptotic substantially stronger than the cited divergence conjecture. It is more than a finite verification or short correction. I cannot certify the broader designation “truly significant” or predict journal acceptance. Its techniques are elementary and its audience is specialized; a major breakthrough across number theory would be an overstatement.

This is a fresh internal AI audit, not an external referee report or a formal proof certificate. Earlier AI passes were not used as evidence of correctness. The manuscript was not edited. Publication readiness still requires the citation-numbering correction below and an author-owned final literature and exposition review.

## 1. Exact relation to the source problems

Write $a_n=S(n+k-1,k)$, $F_k=\operatorname{Fail}(a)$, and $K=k-1$. The accepted Miska–Ward manuscript has the same Conjectures 1–4 as the arXiv version. In valuation notation their assertions and P06's scope are:

| Source assertion | Exact content | P06 |
|---|---|---|
| Conjecture 1 | $v_p(F_k)\geq1$ for every prime $p<k$ | Proved |
| Conjecture 2 | $v_p(F_k)=1$ for $\sqrt{k}\leq p<k$ | Proved |
| Conjecture 3 | $F_k/\operatorname{rad}(K!)\to\infty$ | Proved, with logarithm asymptotic to $\sqrt{k}$ |
| Conjecture 4(a) | $F_{p+1}=pF_p$ | Unresolved |
| Conjecture 4(b), $j>1$ | $F_{p^j+1}\mid p^{j-1}F_{p^j}$ | Unresolved |
| Conjecture 4(c), $j>1$ | $v_p(F_{p^j})=1$ | Unresolved in general |
| Conjecture 4(d) | $v_p(F_{p^j+1})=j$ | Proved |

The prior factorial upper bound is Theorem 2.2 of the accepted version. The first-level Stirling congruence is in the proof of Lemma 2.5. These are respectively Theorem 7 and Lemma 10 in the arXiv numbering. P06 should use the accepted numbering, or explicitly identify its pinpoint references as arXiv numbering. [Miska–Ward, accepted manuscript and publication record](https://eprints.ncl.ac.uk/276171), [arXiv version](https://arxiv.org/html/2102.07561).

The separate finite-cutoff proposal is

\[
 F_k=\operatorname{lcm}_{1\leq n\leq k^\sharp}
 \operatorname{denom}\!\left(\frac1n\sum_{d\mid n}\mu(n/d)S(d+k-1,k)\right),
\]

where $k^\sharp$ is the largest prime power strictly below $k$. It is explicitly unproved in §4.5 of Byszewski–Graff–Ward. The formula is not a claim that only pure prime-power indices need testing: the displayed finite range contains all indices up to $k^\sharp$. P06 correctly does not claim this cutoff. [Byszewski–Graff–Ward, §4.5](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.12531).

## 2. Independent proof reconstruction

### 2.1 Dold congruences and positivity

For $D_n=\sum_{d\mid n}\mu(n/d)a_d$, Möbius inversion gives, when $p\nmid m$,

\[
 a_{mp^r}-a_{mp^{r-1}}=\sum_{d\mid m}D_{dp^r},\qquad
 D_{mp^r}=\sum_{d\mid m}\mu(m/d)
 (a_{dp^r}-a_{dp^{r-1}}).
\]

Consequently all Dold congruences are equivalent to the local conditions

\[
 a_{mp^r}\equiv a_{mp^{r-1}}\pmod{p^r}.
\]

The quantifier over every $m$ coprime to $p$ is essential. The manuscript retains it. For $k\geq2$, the Stirling recurrence gives $a_{n+1}\geq2a_n$; hence $\sum_{d<n}a_d<a_n$, and $D_n>0$. For $k=1$, the constant sequence is realizable. Thus positive multiplication introduces no further sign obstruction and the least Dold multiplier is exactly $F_k$.

### 2.2 Integral recurrence: the zero-index check

Let $P_k(z)=\prod_{j=1}^k(1-jz)$ and $G_k(X)=\prod_{j=1}^k(X-j)$. The identity

\[
 \sum_{n\geq1}a_nz^{n-1}=P_k(z)^{-1}
\]

gives the characteristic recurrence with polynomial $G_k$. The initialization $a_0=0$ is valid: at recurrence index zero, the required vanishing coefficient is that of $z^{k-1}$ in $P_k/P_k=1$, and $k-1>0$. Thus an integral companion matrix really gives $a_n=\lambda(T^nv)$, without an exponent shift. This is an important place where an otherwise plausible matrix proof could fail; it is correct here.

### 2.3 LCM upper bound

Fix $p$, let $m=\lceil k/p\rceil$ and $h=\lceil\log_p m\rceil$. Every residue occurs at most $m$ times among $1,\ldots,k$, so over $\mathbb F_p$,

\[
 G_k(X)\mid(X^p-X)^m.
\]

It follows that $(T^p-T)^{p^h}=0$, and therefore

\[
 T^{p^{h+1}}\equiv T^{p^h}\pmod p.
\]

For commuting matrices, $X\equiv Y\pmod{p^a}$ implies $X^p\equiv Y^p\pmod{p^{a+1}}$. In the binomial expansion, the final term is divisible by $p^{ap}$, and $ap\geq a+1$ also for $p=2,a=1$. Thus no odd-prime restriction is hidden in the lifting step.

Iteration gives $T^{p^r}\equiv T^{p^{r-1}}\pmod{p^{r-h}}$ for $r\geq h+1$. Taking arbitrary positive powers proves the needed mixed-index congruence. Multiplication by $p^h$ supplies the full modulus; levels $r\leq h$ are automatic. Finally $h=0$ for $p\geq k$, and $h=\lfloor\log_p K\rfloor$ for $p<k$. This proves

\[
 F_k\mid\prod_{p<k}p^{\lfloor\log_p K\rfloor}
 =\operatorname{lcm}(1,\ldots,K).
\]

The last divisibility, rather than merely an inequality, is justified because $F_k$ is the LCM of the reduced denominators $D_n/n$.

### 2.4 Prime support by poles

If $p\nmid F_k$, the local congruences imply $a_{pn}=a_n$ modulo $p$, for every $n\geq1$. Put $B=T^{p^h}$, so $B^p=B$. This gives $B^{n+p-1}=B^n$ for positive $n$, and the Cartier invariance just obtained gives $a_{n+p-1}=a_n$. Hence

\[
 P_k(z)\mid1-z^{p-1}\quad\text{over }\mathbb F_p.
\]

There is no rational-function cancellation because the numerator is 1. When $p<k$, the factors corresponding to $j=1,p+1$ force $(1-z)^2\mid P_k(z)$. But $1-z^{p-1}$ is squarefree, including when $p=2$. Contradiction. This proof is sound, though the digit argument below gives a second, explicit proof of the same support assertion.

### 2.5 Digit congruence and valuations

Write $k=qp+c$, $0\leq c<p$, and $R=(p^r-1)/(p-1)$. Reduction modulo $p$ gives

\[
 P_k(z)=(1-z^{p-1})^qP_c(z).
\]

For $c>0$, coefficients of $P_c^{-1}$ in degrees divisible by $p-1$ are all 1 modulo $p$: inclusion–exclusion is legitimate because $c!$ is invertible. Extracting degree $(p-1)R$ yields $\binom{q+R}{R}$, including $q=0$. For $c=0$, it yields $\binom{q+R-1}{R}$. Both are

\[
 a_{p^r}\equiv\binom{J+R}{R},\qquad J=\lfloor K/p\rfloor.
\]

If $K=\sum_i d_ip^i$, then $J$ has digits $d_1,d_2,\ldots$, while $R$ has $r$ consecutive digits 1. With no digit $d_i=p-1$ among positions 1 through $r$, there is no carry and Lucas gives the product $\prod_{i=1}^r(d_i+1)$. At the first digit $p-1$, the addition produces digit zero against a lower binomial digit 1, forcing the binomial to vanish. Thus the same product formula holds in every case, including $r=0$ and $r$ beyond the digit length.

The successive difference is therefore

\[
 a_{p^r}-a_{p^{r-1}}\equiv
 d_r\prod_{i=1}^{r-1}(d_i+1)\pmod p.
\]

When this is nonzero, the local congruence forces $p^r\mid F_k$. Taking $r=h=\lfloor\log_pK\rfloor$ gives equality with the upper bound whenever all intermediate digits avoid $p-1$. The highest digit is automatically nonzero. This proves the claimed exact families. Taking the first nonzero digit in a position $s\geq1$ supplies a support witness at $p^s\leq K<k$.

Crucial limit: a zero residue in this formula says only that the difference is divisible by $p$. It does not bound its valuation from below by the amount necessary to establish a proposed smaller repair factor. Pure prime powers also do not replace all mixed indices in the local criterion.

### 2.6 Square-root asymptotic

Put $E_k=\log(F_k/\operatorname{rad}(K!))$. Prime support and the LCM bound give

\[
 0\leq E_k\leq\sum_{j\geq2}\vartheta(K^{1/j})
 =\vartheta(\sqrt K)+O(K^{1/3}(\log K)^2).
\]

Only $O(\log K)$ terms are nonempty. The crude bound $\vartheta(x)\leq x\log x$ suffices, so this estimate does not use the prime number theorem.

For $K^{1/3}<p\leq\sqrt K$, the local upper exponent is 2. The digit criterion proves exponent 2 unless the middle digit in $K=d_2p^2+d_1p+d_0$ is $p-1$. Such an exceptional prime satisfies

\[
 tp^2-p\leq K<tp^2,\quad t=d_2+1,
 \quad2\leq t\leq K^{1/3}+1.
\]

For a fixed positive integer $t\geq2$, these intervals in $K$, as the positive integer $p$ varies, are disjoint: the lower endpoint for $p+1$ exceeds the upper endpoint for $p$ by $2tp+t-p-1>0$. Therefore at most $O(K^{1/3})$ primes in this range can be exceptional. Removing their logarithmic weights and the primes below $K^{1/3}$ gives

\[
 E_k\geq\vartheta(\sqrt K)-O(K^{1/3}\log K).
\]

The claimed two-sided estimate follows. Only the final replacement of $\vartheta(\sqrt K)$ by $\sqrt K(1+o(1))$ uses the prime number theorem. In particular, this is not an argument along a subsequence or an average over $k$; it holds for every sufficiently large $k$. No unproved prime-distribution estimate is being used to count the exceptions.

## 3. Fresh finite diagnostic

`P06-independent-check.py` imports no manuscript or prior candidate code. It evaluates Stirling numbers by inclusion–exclusion modulo $p\,k!$, then divides the resulting residue exactly by (k!). This avoids invalid inversion when $p\mid k!$. It compares those values against the digit formula for every $1\leq k\leq100$, $p\in\{2,3,5,7,11\}$, and $0\leq r\leq6$: **3,500 comparisons passed**.

Results: `P06-independent-check-results.json`; ordered-row SHA-256 `de6ed54abe50f77a8321b25955c9bed1d10f679e3a8f598406bf607526ef8fbb`. This is an indexing and edge-case diagnostic, not a replacement for §2's proof or evidence for the unresolved cutoff.

## 4. Later literature and novelty limits

The following primary sources were inspected live during this reassessment:

1. **Geng-Rui Zhang (2024), Example 4(5).** This explicitly quotes the factorial bound $F_k\mid(k-1)!$. The paper's new realizability results concern other combinatorial families. It does not give P06's LCM bound, digit-based sharp valuations, or repair asymptotic. [Journal of Integer Sequences 27, Article 24.3.3](https://cs.uwaterloo.ca/journals/JIS/VOL27/Zhang/zhang9.pdf).
2. **Tom Ward (2024), §3.4.** The discussion again uses the factorial upper bound and emphasizes the unresolved minimal-multiplier computation. This is useful evidence of the problem's continuing status in 2024, though an exposition is not an exhaustive novelty search. [Patrick Moss, arXiv:2404.03464](https://arxiv.org/html/2404.03464).
3. **Mateusz Rajs (2025), Theorem 9 and surrounding recurrence results.** The stated general upper multiplier is $r_d\Delta_U\operatorname{rad}(\Delta_{\mathcal K})$, where $\mathcal K$ is the splitting field. Applied to the roots $1,\ldots,k$, the field degree is 1, so no sampling is necessary; the stated multiplier has a factor $k!\prod_{i<j}(j-i)^2$, up to sign. It is far larger than the LCM bound. The inspected text contains no matching Stirling prime-support, digit, or asymptotic theorem; its only explicit “Stirling” occurrence is bibliographic. This comparison concerns its stated theorem and does not independently certify all of that paper. [On Dold condition and fail factor of linear recurrent sequences](https://arxiv.org/html/2509.09847).
4. **Ward's OEIS entry A341617.** The live entry still records the factorial bound and warns that unrestricted finite computations give candidate repair values. The entry is an author-maintained primary record for this sequence; its displayed small values should not be silently promoted to an infinite theorem. [A341617](https://oeis.org/A341617).
5. **Earlier $p$-adic Stirling literature.** Miska's 2018 paper concerns behavior of valuations of individual Stirling numbers, through locally analytic functions. Its abstract does not claim the 2021 repair-factor conjectures. However, I did not complete a theorem-by-theorem audit of all classical Stirling congruences. In particular, the standalone digit congruence is a short consequence of a standard rational generating function and Lucas's formula; its novelty should not be advertised separately from its repair-factor applications without a more specialized historical search. [Miska, arXiv:1803.04533](https://arxiv.org/abs/1803.04533).

Targeted searches for the exact source title, authors with repair-factor terminology, the remaining conjecture labels, and the sharp-bound terminology did not identify an existing proof of the P06 package. Searches using “Stirling repair” alone were badly contaminated by biology results and are not meaningful novelty evidence. The defensible statement is **no overlapping sharp theorem found in the sources inspected**, not “the literature proves this has never been done.”

## 5. Significance and remaining research

The strongest contribution is the combination of three different levels of information: exact prime support, a uniform upper exponent, and an asymptotic for the excess above the squarefree part. The prior upper bound has logarithm of order $k\log k$; the new LCM bound has logarithm of order $k$. More substantially, the excess logarithm is determined to first order at the smaller scale $\sqrt{k}$. This yields a coherent specialist paper even though several ingredients are familiar and the proofs are short.

The elementary digit lemma by itself would be a small note. The pole obstruction alone would also be a short result. Splitting the manuscript into several papers would exaggerate the contribution: the asymptotic depends directly on the valuation criterion and LCM bound. Keep them together. A conjecture being printed in a journal is evidence of an existing question, not by itself a measure of difficulty; the honest case for significance rests on the uniform structural and asymptotic conclusions.

The main downstream problems are precise and substantial:

| Problem | Concrete missing statement | Why P06 does not already imply it |
|---|---|---|
| Prime-power parameter cancellation, Conjecture 4(c) | For $k=p^j$, prove $p^{r-1}\mid S(tp^r+p^j-1,p^j)-S(tp^{r-1}+p^j-1,p^j)$ for all $p\nmid t$, all $r\geq1$ | Current uniform exponent is $j-1$. Mod-$p$ zero residues cannot supply the required higher divisibility. The case $j=2$ is already covered; the new difficulty starts at $j\geq3$. |
| Exact finite cutoff | Show every $p$-adic maximum in the denominators $D_n/n$ occurs for $n\leq k^\sharp$ | A known upper bound and a support witness below $k$ do not locate the maximal exponent. |
| Cross-parameter identities, Conjecture 4(a),(b) | Control valuations at every prime $\ell\neq p$ as the parameter changes from $p^j$ to $p^j+1$ | Knowing only the distinguished $p$-valuation does not prove a full integer divisibility or equality. |
| General exact valuations | Classify the additional higher-congruence cancellations when an intermediate base-$p$ digit equals $p-1$ | The digit lemma is sufficient for sharpness in one family, not a necessary criterion. |

A bounded attempt during this audit did not solve these problems. At $k=p^j$, one has $P_k(z)\equiv1-z^{p^{j-1}(p-1)}\pmod p$, but this only explains first-level cancellations; it does not establish the all-level local congruence displayed above. No extension from that observation is claimed.

There is room to tighten logarithms in the displayed asymptotic error by using Chebyshev's elementary bound and optimizing the prime-range cutoff. That would be a routine refinement of the existing proof, not a separate hard open problem or an additional significant paper. I have not edited the theorem for that purpose.

## 6. Required actions before release

1. Correct or disambiguate the Miska–Ward pinpoint numbering: accepted Theorem 2.2 and Lemma 2.5 versus arXiv Theorem 7 and Lemma 10.
2. Retain the explicit exclusions of Conjecture 4(a)–(c) and the finite cutoff; mention that 4(c)'s $j=2$ case follows already if more precision is wanted.
3. Add a concise comparison with relevant 2024–2025 literature if making a current novelty claim, while avoiding any suggestion that this finite source audit is exhaustive.
4. Obtain an author-owned final review of novelty and presentation. No mathematical correction to the audited main proofs is currently required by this reassessment.

Selected-copy handoff: the citation correction has now been applied only in `research_program/selected_papers/P06-stirling-repair/manuscript.tex`, whose SHA-256 is `dd0edaaea0b37293073801784badc058ae2cac8257256fd3468860c0a6ad265b`. That copy compiled successfully with Tectonic. The original audited source remains unchanged; see the selected copy’s `ASSESSMENT.md` for the transfer record.

Source-access precision: Theorem 2.2 and Lemma 2.5 were verified directly in the institutionally deposited accepted manuscript. The publisher metadata confirms Acta Arithmetica 201 (2021), 421–435 and DOI 10.4064/aa210309-9-8, but the publisher PDF download redirected to the institute homepage. Thus the pinpoint verification is of the accepted version, not a separately inspected typeset journal PDF.
