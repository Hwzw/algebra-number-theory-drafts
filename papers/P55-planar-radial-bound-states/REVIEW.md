# Proof development and originating-assistant audit

Date: 17 September 2026. Reviewer: the same OpenAI Codex assistant that wrote the proof. **This is a self-audit, not independent review.** The consolidated proof is in [manuscript](manuscript.md).

## Dependency map

1. Integral equation and energy: global regular IVP, simple zeros, finite negative-energy witnesses.
2. Last-lobe lemma: a trajectory with finitely many zeros either has a negative-energy witness or decays exponentially. This avoids relying on a global finite-node theorem in the uniqueness argument.
3. Variation Wronskian: at least one simple variation zero on every monotone part of a bound state, including the last part.
4. Uniform parameter dependence: every nearby pair intersects on each corresponding part. No assertion that the variation has *exactly* one zero is used.
5. Planar identities: $Q_s=4(F/f)'q$, and the weighted-energy derivative for $W$.
6. Transfer lemma: ordered maxima and common-level $Q$ data imply oppositely ordered minima and the next extremal $Q$ data.
7. Reflection: extrema inherit the required ordering through every finite part.
8. Tail gap: $W_2-W_1\geq\delta>0$, incompatible with two decaying endpoints.
9. Local shooting separation: below a bound-state parameter, the shot is trapped after exactly the same number of nodes; above it, another node occurs.
10. Interval topology: turns this local fact into uniqueness and ordered thresholds.
11. External prescribed-node existence: CGY arXiv:1208.0017v2, Theorem 1.1, with every nontrivial growth hypothesis checked in the manuscript.

## Adversarial checks performed

| Possible failure | Resolution in the current draft |
|---|---|
| $1<p<2$ does not give a twice differentiable nonlinearity at zero | Only $f\in C^1$ is used. Parameter differentiation and differentiation of the radial equation each require only $f'$. |
| Singular coefficient at $r=0$ | The integral kernel has norm $r^2/4$; regular IVP and parameter dependence follow from contraction. The Wronskian tends to zero at the origin. |
| Initial strict $H$ inequality vanishes in the plane | Equation (5.4) compares at $s=\alpha_1$, where the second shot's $Q$ is strictly negative. |
| Division by $f$ at its zeros | $Q$ and $F/f$ are used only where $|s|\geq\beta>1$. The inner interval uses $W$ instead. |
| Inverse derivatives are singular at extrema | Identities are used in open branches; $Q$, $r$, and $q$ have continuous finite endpoint values. First-contact arguments occur in branch interiors. |
| A crossing of $u_1,u_2$ might occur on the wrong monotone parts | Fixed radii around a reference variation zero stay inside both corresponding parts by continuous dependence. |
| First intersection might have the wrong slope order | The initial radius order and first-contact derivative give $q_1\leq q_2$; equality violates ODE uniqueness. |
| Strict comparison through $F=0$ could be lost | $W=q$ and $Q=-q^2$ at $\pm\beta$ preserve the strict gaps. In the outer argument a hypothetical equal-$q$ contact at $\beta$ contradicts a positive $Q$ gap. |
| The first minimum could be the wrong solution's endpoint | If $q_2$ vanished first, the strict interior $q_1<q_2$ order forces both endpoint slopes to vanish, contradicting the positive $Q$ gap and radius order. |
| Reflection might reverse the wrong comparison quantity | $R$ and $u'$ both change sign, so the radial expression for $Q$ is invariant. At extrema it is simply $-2r^2F$. |
| Infinite radius invalidates a strict limit inequality | The proof uses $W_2-W_1\geq\delta$, not $r_1(0)>r_2(0)$. Each decaying endpoint has $W\to0$. |
| A nearby branch could stop before the tail comparison | Loss of energy, a positive minimum, a positive asymptote, and a zero endpoint are treated separately in Proposition 6.1. |
| Local uniqueness need not imply global uniqueness | The interval partition is open on the two sides, and each bound-state point has a prescribed orientation. Components cannot have a finite endpoint of the opposite orientation. |
| Existence theorem might exclude $N=m=2$ or unrestricted $p$ | Its statement permits $N\geq m>1$; the growth expression is bounded below by $cs^2$ for every fixed $p>1$. |
| Existence theorem's $\mathbb N$ convention might exclude zero | Ground-state existence is obtained independently from the nonempty first-crossing set and a negative-energy interval near $\beta$. |
| Infinitely many zeros of general shots are tacitly ruled out | The uniqueness proof needs no such assertion. The added Lemma 8.1 separately proves finite nodal count for every shot by treating positive and zero limiting energy. It then justifies $\alpha_k\to\infty$ in Corollary 1.2. |
| Novelty is inferred from Tang's conjecture | Explicitly disallowed: CGY11 already states the whole-plane target. |

No unresolved mathematical step was identified in this originating-assistant pass. That statement is limited to this audit and is not a certificate of correctness. The highest-value independent checks are the uniform nearby-pair formulation of Lemma 5.1 and the stopping alternatives in Proposition 6.1.

## Scope deliberately not inferred

The proof supplies no finite-disk uniqueness, no radial nondegeneracy, no exact count of variation zeros, and no stability theorem. These are not automatic consequences of uniqueness. The current paper is one connected proof reconstruction, not several papers.

## Algebra check

With Python and SymPy installed, run from this paper folder:

```sh
python3 checks/check_identities.py
```

The original four identities and three classification identities are now checked. No floating-point shooting computation has been used as evidence for the theorem.

## Classification extension audit

Lemma 8.1 treats $E_\infty>0$ using bounded spacing and divergent harmonic energy loss; it treats $E_\infty=0$ using $H=r^2E$, with bounded outer-arc durations and a fixed negative-$F$ segment in each lobe. These two cases exhaust the possibilities under infinitely many zeros. Lemma 8.2 uses a coefficient bounded below by a positive constant after negative-energy trapping. The Riccati argument for the final logarithmic derivative uses finite-time blow-up to bound $-u'/u<2$, then barriers at $1\pm\delta$. These additions were checked by the originating assistant; independent review remains absent.

## Post-publication correction

Version 0.2.1 restricts $P_k$ to $N_k$ in Section 7. Without that restriction the displayed partition at $k=0$ included extra central values below or equal to $\beta$. The correction restores the literal set equality used by the interval argument. See the [revision history](CHANGELOG.md). This additional check was performed by the originating assistant.
