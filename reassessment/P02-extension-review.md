# P02: independent audit of the spectral classification and exact repair

Date: 2026-09-08. Reviewer: groups research agent. Scope: mathematics of the proposed extension; no edits to the manuscript. **Verdict: the proposed matrix classification and exact formula are correct. The uniform recurrence extension is also correct, and its exact multiplier is attained by one suitable initialization.** The root's Jordan/lifting argument needs no mathematical repair. The proofs and careful quantifiers are recorded below.

This is a proof review, not a completed independent novelty audit of the enlarged theorem. The complete spectral classification and non-squarefree exact multipliers are materially broader statements than the currently inspected P02 matrix theorem.

## 1. Precise matrix statement

Let A∈Mat_N(Z), N≥1, and let s≥1. Let m_A∈Z[x] be its monic minimal polynomial over Q, K its splitting field, and G=Gal(K/Q). Here **semisimple over Q means diagonalizable over an algebraic closure of Q**, equivalently that m_A is squarefree; it does not mean diagonalizable by a matrix over Q.

There is a positive integer C for which the matrix sequence (C A^{n^s})_{n≥1} satisfies the Dold congruences entrywise if and only if

1. A is semisimple over Q; and
2. exp(G) divides s.

When these conditions hold, let ν_p(A) be the largest Jordan-block size of A modulo p over an algebraic closure of F_p. Define

    r_p = min{r≥0 : p^{sr} ≥ ν_p(A)}
        = ceil(log_{p^s} ν_p(A)).

The exact least positive repairing integer is

    C_s(A)=∏_p p^{r_p}.

The product is finite. In particular ν_p=1 gives r_p=0. The integer-threshold definition is preferable to floating-point logarithms in any implementation.

## 2. Ramified primes cause no exception to the eigenvalue condition

Assume exp(G)|s. For any rational prime p and any prime P of O_K above it, the residue Galois group is

    Gal(O_K/P / F_p) ≅ D(P)/I(P).

This is a cyclic group of order f(P/p). The exponent of a quotient of a subgroup of G divides exp(G), hence f(P/p)|s. This statement includes ramified primes; one must use the decomposition/inertia quotient there, rather than pretend that a unique unramified Frobenius element exists in G.

Every root of m_A is an algebraic integer in O_K. Reducing the factorization of the monic polynomial m_A at P shows that all its reduced roots lie in O_K/P. Every eigenvalue of A modulo p is a root of that reduced polynomial, so

    λ^{p^s}=λ

for every eigenvalue, at every prime p. A drop in minimal-polynomial degree modulo p does not affect this sufficiency argument.

The primary reference checked is J. S. Milne, [Algebraic Number Theory](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Section 8, the decomposition/inertia discussion preceding Proposition 8.13, and Chebotarev Theorem 8.31. The relevant statements were inspected in the linked PDF; section and theorem references avoid edition-dependent page offsets.

## 3. Local sufficiency, including the exact exponent inequality

Fix p. Write ν=ν_p(A), h=min{j≥0:p^j≥ν}, and r_0=min{r≥0:p^{sr}≥ν}. Then r_0=ceil(h/s), so h≤sr_0.

On a Jordan block J=λI+R modulo p, the p^h power kills R. The eigenvalue condition therefore gives

    A^{p^{h+s}} ≡ A^{p^h} (mod p).

The commuting-power lifting lemma from P02 is valid without invertibility: if X and Y commute and X≡Y mod p^a, a≥1, then X^{p^j}≡Y^{p^j} mod p^{a+j}. Its binomial proof also covers p=2,a=1.

For r≥r_0+1, let j=s(r−1)−h≥0. Lifting the last congruence by p^j and then taking the m^s-th power gives

    A^{m^s p^{sr}} − A^{m^s p^{s(r−1)}}
       ≡0 mod p^{s(r−1)−h+1}.

This holds for every m≥1; in particular it holds for the m coprime to p required by the local Dold criterion. Multiplication by p^{r_0} supplies the needed modulus p^r, since

    r_0+s(r−1)−h+1−r
       = (sr_0−h)+(s−1)(r−r_0−1) ≥0.

For 1≤r≤r_0 divisibility after multiplication by p^{r_0} is automatic. This also handles r_0=0: then ν=1, h=0, and the preceding lifting argument begins at r=1. Thus p^{r_0} is locally sufficient with no size restriction such as 2^s≥deg(m_A).

If A is semisimple over Q, m_A is monic separable integral. For every p not dividing disc(m_A), its reduction is a squarefree annihilator of A modulo p, so ν_p=1. Only finitely many primes occur in C_s(A). Applying the local Dold criterion at each prime proves global sufficiency.

## 4. Local sharpness

Suppose r_0≥1. At local level r=r_0 and m=1, inspect

    Δ=A^{p^{sr_0}}−A^{p^{s(r_0−1)}}.

On a block of maximal size ν modulo p, the first nilpotent power vanishes and the second does not, because

    p^{s(r_0−1)} < ν ≤ p^{sr_0}.

The semisimple terms agree, by λ^{p^s}=λ. Hence Δ on that block equals

    −R^{p^{s(r_0−1)}} ≠0.

Consequently the integral matrix Δ has at least one entry which is a p-adic unit. The Dold congruence at n=p^{r_0} forces p^{r_0}|C for any entrywise repair C. This proves the exact local exponent, rather than only its prime support. No choice of Jordan basis over Z_p is required: nonvanishing over the algebraic closure implies nonvanishing of the original reduced matrix.

## 5. Global necessity

### Stability of the minimal polynomial at almost all primes

Let d=deg(m_A). Vectorize I,A,...,A^{d−1} into columns of an integer matrix. They are Q-linearly independent, so some d-by-d minor δ is a nonzero integer. If p∤δ, the reductions remain linearly independent. Since the monic relation m_A(A)=0 always reduces modulo p, the minimal polynomial modulo p has degree exactly d and equals the reduction of m_A.

The polynomial m_A is integral because it is a monic factor over Q of the monic integral characteristic polynomial; Gauss's lemma applies.

### Nonsemisimplicity over Q obstructs finite repair

If m_A has a repeated irreducible factor over Q, it has a square of a positive-degree monic integral polynomial as a factor. Its reduction is nonsquarefree at every prime. At all p∤δ, the minimal polynomial of the reduced A is therefore nonsquarefree. But x^{p^s}−x has derivative −1 in F_p[x] and is squarefree. Thus

    A^{p^s}−A ≠0 mod p

for all but finitely many primes. The Dold condition at n=p forces each such prime to divide C, which precludes a positive finite repairing integer.

### The Galois exponent is necessary

Now suppose m_A is separable but exp(G)∤s. There exists σ∈G with σ^s≠1. The action of G on all roots of m_A is faithful, because those roots generate K. Therefore σ^s moves at least one root.

Chebotarev's theorem supplies infinitely many unramified primes whose Frobenius conjugacy class is that of σ. Exclude the prime divisors of δ and disc(m_A). At the remaining primes the reduced roots are distinct, the root permutation induced by Frobenius has the same cycle structure as σ, and every root occurs in the reduced minimal polynomial. Since σ^s moves some root, that reduced root is not fixed by the p^s-Frobenius. Therefore the reduced minimal polynomial does not divide x^{p^s}−x, and A^{p^s}−A is nonzero modulo p.

Again every such prime must divide an entrywise repair C. This proves exp(G)|s. The condition involves the group exponent, not the splitting-field degree; the latter is generally a larger sufficient multiple.

## 6. Complete uniform recurrence statement

Let F=x^d+c_{d−1}x^{d−1}+...+c_0∈Z[x] be monic of degree d≥1. Fix initialization u_1,...,u_d and the recurrence from P02. Let G_F be the Galois group of the splitting field of F.

There is one positive integer repairing (u_{n^s}) for **every** integral initialization if and only if

    F is separable, F(0)≠0, and exp(G_F)|s.

Equivalently, every initialization has some finite repairing integer: taking the least common multiple of repairing integers for the d standard-basis initializations gives one multiplier for all initializations.

Under these conditions let ν_p(xF) denote the largest multiplicity of a root of xF modulo p over an algebraic closure (equivalently, the greatest exponent of an irreducible factor in its factorization over F_p). Then the exact uniform repairing integer is

    C_s(F; initialization from 1)
       = ∏_p p^{min{r≥0:p^{sr}≥ν_p(xF)}}.

Its prime support is exactly the support of F(0)disc(F), but its prime exponents need not be one.

### Uniform sufficiency

Let T be the companion matrix with ones above the main diagonal. For initial column v, use the augmented matrix B_v defined by B_v e_0=v and B_v w=Tw. The polynomial xF annihilates B_v, and it is separable over Q because F is separable and F(0)≠0. Its splitting field is that of F. Every Jordan block of B_v modulo p has size at most ν_p(xF). The matrix theorem thus gives the displayed multiplier uniformly in v. Since

    B_v^n e_0=T^{n−1}v,

its appropriate first-column entry is u_n, proving sufficiency for all initializations.

### Uniform sharpness without an observability gap

Fix p with ν=ν_p(xF)>1 and set r_0=min{r:p^{sr}≥ν}. Put q_0=p^{s(r_0−1)}, q_1=p^{sr_0}, and define

    D(x)=x^{q_1−1}−x^{q_0−1}.

Modulo p,

    D(x)=x^{q_0−1}(x^{p^s−1}−1)^{q_0}.

Every nonzero root of F modulo p lies in F_{p^s}. Such a root has multiplicity exactly q_0 in D, whereas zero has multiplicity q_0−1. Consequently

    F mod p divides D mod p  iff  ν_p(xF)≤q_0.

The right side is false by definition of r_0. A companion matrix remains cyclic over every field, so its reduced minimal polynomial is exactly F mod p, and D(T)≠0 modulo p.

The first row of D(T) is nonzero: otherwise, because D(T) commutes with T and e_1^t T^j=e_{j+1}^t for 0≤j<d, all rows would vanish. Choose an integral initialization v_p with

    e_1^t D(T)v_p ≠0 mod p.

Then u_{p^{sr_0}}−u_{p^{s(r_0−1)}} is a p-adic unit, so any multiplier working for that initialization needs p^{r_0}. This proves exact uniform sharpness.

### One initialization attains the complete uniform factor

There are finitely many relevant p. Choose a local witness v_p as above for each, and choose one v∈Z^d with v≡v_p mod p for all these primes, coordinatewise by the Chinese remainder theorem. This one initialization forces every prime exponent in C_s(F). Since the uniform multiplier is sufficient for it, its scalar failure factor is exactly C_s(F).

Thus the uniform maximum is attained. It is unnecessary to claim that one predetermined fundamental initialization always attains it.

### About the proposed augmented cyclic vector

With v=e_d, the augmented matrix B_v does have minimal polynomial xF over every residue field: e_0,B_v e_0,...,B_v^d e_0 form an integral basis, because e_d,T e_d,...,T^{d−1}e_d form an integral basis for this companion orientation. Hence this single initialization makes the augmented matrix attain the largest Jordan block ν_p(xF), simultaneously for all p.

However, a largest matrix Jordan block does not by itself show that the particular observed scalar entry is nonzero at the critical difference. The polynomial/first-row argument above avoids that issue and CRT supplies a single scalar initialization when desired.

### Necessity of the recurrence conditions

If F(0)=0, the sequence u_1=1,u_n=0 for n≥2 satisfies the recurrence and needs every prime in a repair, so uniform finite repair is impossible.

If F is nonsquarefree, then at infinitely many primes its reduction cannot divide the squarefree polynomial x^{p^s−1}−1. Therefore T^{p^s−1}−I has a nonzero first row at each such prime, by the cyclic-row argument. Among the finitely many standard-basis initializations, one is a witness for infinitely many primes and has infinite repair.

If F is separable with nonzero constant term but exp(G_F)∤s, the Chebotarev argument in Section 5, excluding the constant-term primes as well, likewise gives infinitely many primes with F∤x^{p^s−1}−1 modulo p. The same first-row and pigeonhole argument supplies a single initialization with infinite repair.

## 7. Exact checks and a useful example

The companion matrix of

    F=(x−2)(x−4)(x−6)=x³−12x²+44x−48

is

    T=[[0,1,0],[0,0,1],[48,−44,12]].

Its splitting-field Galois group is trivial. For s=1, modulo 2 its largest Jordan block has size 3, so the exact matrix multiplier is 4. The polynomial xF has a root of multiplicity 4 modulo 2 and a root of multiplicity 2 modulo 3, so the exact uniform recurrence multiplier is 4·3=12. For s=2 or 3 the corresponding multipliers are 2 and 6.

The initialization (u_1,u_2,u_3)=(0,1,1) attains scalar failure factor 12 at s=1. The local difference at p=2,r=2 is 1 modulo 2, and that at p=3,r=1 is 1 modulo 3. The general sufficiency theorem supplies 12; these two witnesses force it.

`P02-extension-check.py` and its JSON output perform 378 exact local instances for this matrix and recurrence: p∈{2,3,5,7,11}, r≤6, s∈{1,2,3}, and m∈{1,2,3,5,7} coprime to p. Every instance passed, as did the exact scalar witnesses above. These checks support the proof and are not the justification for the classification.

## 8. Transfer recommendations

- Lead the strengthened paper with the full iff spectral classification and exact local prime exponents. The older squarefree theorem becomes a consequence of the threshold p^s≥ν_p.
- State the Galois condition for the splitting field of the **minimal** polynomial of the matrix, not an arbitrarily large annihilating polynomial.
- Define semisimplicity via the algebraic closure and root multiplicity via the reduction at p.
- Keep the ramified-prime argument through D/I and distinguish it from unramified Frobenius used in the necessity proof.
- For recurrences, use xF because initialization starts at 1. The polynomial first-row argument gives exactness without silently changing the observed entry.
- Keep entrywise matrix repair, uniform recurrence repair, and an individual scalar repair distinct. A scalar trace can satisfy Dold congruences even when the entire matrix sequence has no finite repair.
- The new local exponent formula and the single-initialization attainment are proved here. A separate updated novelty/significance review is still needed before treating the enlarged manuscript as publication ready.

## 9. Authorized manuscript transfer

After the root independently reconstructed the classification and exact local proof, the root authorized a replacement manuscript. The complete TeX is now `research_program/selected_papers/P02-recurrence-repair/manuscript.tex`, with a clean 9-page PDF compiled by Tectonic. It includes every argument above that is needed for the main statements, including the critical-level necessity, the companion first-row argument and coordinatewise CRT attainment. The old restricted manuscript remains available under `research_program/papers/P02-recurrence-repair/`.

The current-source comparison and transparent access limits are recorded in `P02-source-audit.md`. The parent is responsible for the independent final transfer read and visual QA; matching Markdown is assigned to another agent. This remains one P02 paper, not multiple contributions counted separately.
