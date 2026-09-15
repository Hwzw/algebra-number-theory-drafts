#!/usr/bin/env python3
"""Exact diagnostics for note 0141. Universal nonexistence uses its hand proof."""
from pathlib import Path
from itertools import product
import hashlib
import json
import time


def rref(rows, p):
    a = [[x % p for x in row] for row in rows]
    if not a:
        return a, []
    pivots = []
    for j in range(len(a[0])):
        pivot = next((i for i in range(len(pivots), len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        r = len(pivots)
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][j], -1, p)
        a[r] = [(x*inv) % p for x in a[r]]
        for i in range(len(a)):
            if i != r:
                c = a[i][j]
                a[i] = [(x-c*y) % p for x, y in zip(a[i], a[r])]
        pivots.append(j)
    return a, pivots


def rank(a, p):
    return len(rref(a, p)[1])


def nullspace(a, p):
    reduced, pivots = rref(a, p)
    out = []
    for j in range(len(a[0])):
        if j in pivots:
            continue
        v = [0]*len(a[0])
        v[j] = 1
        for i, pivot in enumerate(pivots):
            v[pivot] = -reduced[i][j] % p
        out.append(v)
    return out


def partial_chain_case(p, m, r):
    assert 2*r <= m
    N = [[int(i % 2 == 0 and j == i+1 and i < 2*r) for j in range(m)] for i in range(m)]
    histogram = {}
    for phi in product(range(p), repeat=m):
        # V = span(u) direct-sum W. Extra free directions are unnecessary.
        L = [list(phi)] + N
        kernel = nullspace(L, p)
        embedded_kernel = [[0] + v for v in kernel]
        joint = [L[i] + [v[i] for v in embedded_kernel] for i in range(m+1)]
        intersection = rank(L, p) + len(kernel) - rank(joint, p)
        assert rank(L, p) >= r
        assert intersection >= r-1 >= 1
        histogram[intersection] = histogram.get(intersection, 0)+1
    return {"prime": p, "dimension_W": m, "rank_N": r,
            "all_functionals_checked": p**m, "intersection_dimension_histogram": histogram}


def partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    maximum = min(n, maximum or n)
    for j in range(maximum, 0, -1):
        for rest in partitions(n-j, j):
            yield (j,) + rest


def rigidity_checks():
    checked = 0
    nonsemisimple = 0
    for n in range(2, 21):
        k = n-1
        # The zero-primary dimension may be smaller than the full dimension.
        # The remaining part is invertible, so it cannot affect a zero chain.
        for zero_dim in range(n+1):
            for shape in partitions(zero_dim):
                powered_blocks = [((s-1-j)//k)+1 for s in shape for j in range(min(k, s))]
                if any(s >= 2 for s in powered_blocks):
                    assert zero_dim == n and shape == (n,)
                    total_rank = n-zero_dim+sum(s-1 for s in powered_blocks)
                    assert total_rank == 1
                    nonsemisimple += 1
                checked += 1
    return {"dimensions": [2, 20], "zero_primary_partitions_checked": checked,
            "nonsemisimple_cases": nonsemisimple}


def main():
    start = time.time()
    cases = [partial_chain_case(p, m, r) for p, m, r in
             [(2, 4, 2), (3, 4, 2), (5, 4, 2),
              (2, 5, 2), (3, 5, 2), (2, 6, 2), (2, 6, 3)]]
    rigidity = rigidity_checks()
    examples = []
    for k in range(5, 21):
        n = k+1
        B = [[int(i == j and i >= 2) for j in range(n)] for i in range(n)]
        C = [[int(i in [1, 3, 5] and j == i-1) for j in range(n)] for i in range(n)]
        assert rank(B, 2) == n-2 and rank(C, 2) == 3
        assert n > k*((n-rank(B, 2))-1)
        examples.append({"k": k, "n": n, "nullity_B": 2, "rank_target": 3})
    record = {
        "status": "passed", "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "forced_chain_cases": cases,
        "total_functionals_checked": sum(x['all_functionals_checked'] for x in cases),
        "power_rigidity": rigidity, "coefficient_and_target_checks": examples,
        "first_example": {"B": [[int(i == j and i >= 2) for j in range(6)] for i in range(6)],
                          "C": [[int(i in [1, 3, 5] and j == i-1) for j in range(6)] for i in range(6)]},
        "seconds": round(time.time()-start, 3),
        "scope": "Finite exact checks of proof ingredients and explicit matrices. No enumeration of all X,Y and no deduction of characteristic-zero nonexistence from finite fields. The universal contradiction is proved in note 0141."
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({k: v for k, v in record.items() if k not in ['coefficient_and_target_checks', 'first_example']}, indent=2))


if __name__ == '__main__':
    main()
