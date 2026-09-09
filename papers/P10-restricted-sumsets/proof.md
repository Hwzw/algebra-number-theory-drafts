# C13 — Counterexamples to a one-sided restricted-sumset conjecture

Status: full proposed infinite-family proof; independent review requested. No publication-ready claim.

## Precise source

Minghui Ouyang, *On restricted sumsets with bounded degree relations*, Mathematika 71 (2025), e70045, DOI 10.1112/mtk.70045; primary version [arXiv:2503.09121v3](https://arxiv.org/html/2503.09121v3), dated September 4, 2025.

Conjecture 1.10 asserts that for finite integer sets A,B with |B|≤|A| and a forbidden relation R⊆A×B having degree at most Δ at every vertex of B,

    |A +_R B| ≥ |A|+|B|−1−floor(5Δ/2).

Here A +_R B={a+b:(a,b)∉R}. Theorem 1.5(i) proves the weaker lower bound |A|+|B|−3Δ. The absence of a further −1 in this established bound is important.

## Theorem: unbounded-parameter counterexamples

Let k,N,U be integers satisfying

    k≥1,  N≥14k,  8k≤U≤N−6k.

Intervals below are intervals of integers, inclusive. Put

    A = [0,N+4k−1] \ ([k,2k−1] ∪ [U,U+2k−1] ∪ [N+2k,N+3k−1]),
    B = [0,N−1],

and define the missing-sum set

    D = [0,4k−1] ∪ [U,U+2k−1]
        ∪ [U+N−1,U+N+2k−2] ∪ [2N−1,2N+4k−2].

Let R={(a,b)∈A×B:a+b∈D}. Then

    |A|=|B|=N,
    max_{b∈B} deg_R(b)=3k,
    A +_R B = [0,2N+4k−2] \ D,
    |A +_R B|=2N−8k−1.

Consequently Conjecture 1.10 fails with Δ=3k, by ceil(k/2) elements. Any universal estimate

    |A +_R B| ≥ |A|+|B|−1−cΔ−O(1)

with an absolute O(1) requires c≥8/3. At k=1, the existing Theorem 1.5(i) is sharp: for every N≥14 the restricted sumset has cardinality 2N−9 when Δ=3.

### Proof: sizes and the unrestricted sumset

The three removed intervals of A are disjoint and have total length 4k. Thus |A|=(N+4k)−4k=N. Clearly |B|=N.

The endpoints 0 and N+4k−1 belong to A, and the largest gap between successive elements of A is 2k+1. Since N≥14k, the intervals a+B=[a,a+N−1], a∈A, overlap or are adjacent and cover exactly [0,2N+4k−2]. Hence A+B is that entire interval.

The four displayed intervals of D are disjoint: the first ends before U, the second before U+N−1, and the third ends before 2N−1 by U≤N−6k. They lie in A+B and have lengths 4k,2k,2k,4k. Thus |D|=12k, and the cardinality assertion follows once the degree condition is proved.

### Proof: the column-degree bound

Write D=D_0∪D_1∪D_2∪D_3 in increasing order, and set

    d_i(b)=|(A+b)∩D_i|,  d(b)=Σ_i d_i(b).

The left endpoint interval D_0 can contribute only for 0≤b≤4k−1. The right endpoint interval D_3 can contribute only for N−4k≤b≤N−1. The two middle intervals can contribute simultaneously only for

    U−4k ≤ b ≤ U+2k−1.

Indeed D_2 first meets A+b when N+4k−1+b≥U+N−1, and D_1 last meets A+b when b≤U+2k−1. The three listed ranges are disjoint because U≥8k and U≤N−6k. Outside them, no endpoint interval contributes and at most one middle interval contributes, so d(b)≤2k.

For the left endpoint range, the translated set A+b meets only D_0 and D_1. Direct intersection of intervals gives the following table. Empty endpoint overlaps are counted as zero.

| b range | d_0(b) | d_1(b) | d(b) |
|---|---:|---:|---:|
| 0≤b≤2k−1 | 3k−b | b | 3k |
| 2k≤b≤3k−1 | k | 2k | 3k |
| 3k≤b≤4k−1 | 4k−b | 2k | 6k−b≤3k |

For example, d_0(b) counts the points of [0,4k−1−b] after removing the hole [k,2k−1]; d_1(b) counts A in [U−b,U+2k−1−b]. The other two holes are outside these ranges. These observations yield every entry without an approximation.

Next let b=U−4k+t in the middle range, with 0≤t≤6k−1. Only D_1 and D_2 contribute. For D_1 the interval to intersect with A is

    [U−b,U+2k−1−b]=[4k−t,6k−1−t].

This lies near the left endpoint of A and encounters only the hole [k,2k−1]. For D_2 the interval is

    [U+N−1−b,U+N+2k−2−b]=[N+4k−1−t,N+6k−2−t].

Reflecting it about N+4k−1 gives [t−2k+1,t], again encountering only the endpoint hole [k,2k−1] in the reflected A. The resulting exact counts are:

| t range | d_1(b) | d_2(b) | d(b) |
|---|---:|---:|---:|
| 0≤t≤k−1 | 2k | t+1 | 2k+t+1≤3k |
| k≤t≤2k−1 | 2k | k | 3k |
| 2k≤t≤3k−1 | 4k−t | k | 5k−t≤3k |
| 3k≤t≤4k−1 | k | t−2k+1 | t−k+1≤3k |
| 4k≤t≤5k−1 | k | 2k | 3k |
| 5k≤t≤6k−1 | 6k−t | 2k | 8k−t≤3k |

Finally the right endpoint range follows from the left range by reflection. Namely, reflecting A about N+4k−1 changes its parameter U to

    U'=N+2k−U,

which still satisfies 8k≤U'≤N−6k. Reflecting D about 2N+4k−2 gives the displayed missing-sum set with parameter U'. Correspondingly b changes to N−1−b. Thus the left-range table applies to the right-range count as well.

This proves d(b)≤3k for all b. Equality holds at b=0 by the first table, so the maximum degree is exactly 3k. Since R deletes exactly the pairs whose sums lie in D, A +_R B=(A+B)\D, proving the theorem.

The conjectured lower bound at Δ=3k is 2N−1−floor(15k/2). Subtracting the actual cardinality 2N−8k−1 yields 8k−floor(15k/2)=ceil(k/2)>0. Letting k grow proves the necessary coefficient c≥8/3. At k=1 the actual cardinality is 2N−9=|A|+|B|−3Δ. ∎

## Original finite witness

Take k=1,N=20,U=14. Then

    A={0,2,3,...,13,16,17,...,21,23},
    B={0,1,...,19},
    D={0,1,2,3,14,15,33,34,39,40,41,42}.

The restricted sumset has 31 elements; Conjecture 1.10 predicts at least 32. The degree vector on B is

    (3,3,3,3,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3).

The degree restriction is only on B. Larger degrees at some vertices of A are permitted by the conjecture.

## Scope

This disproves Conjecture 1.10 and determines the best universal bound for Δ=3 and equal sufficiently large summands, by matching source Theorem 1.5(i). It does not determine the optimal asymptotic coefficient for all Δ: the construction forces at least 8/3, while the source bound gives at most 3. No claim is made that every aspect of the source paper fails or that its independent finite-field theorems are affected.
