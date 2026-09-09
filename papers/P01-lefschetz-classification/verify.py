"""Exact ancillary checks; the proof in proof.md does not depend on these tests."""
import itertools
import json
import random
from collections import defaultdict
from pathlib import Path
import sympy as sp


def popcount(n):
    return bin(n).count("1")


def survive(mask, n, edges):
    xs = mask & ((1 << n) - 1)
    ys = mask >> n
    return not (xs & ys) and all(not (xs & (1 << a) and xs & (1 << b)) for a, b in edges)


def multiply(a, b, n, edges):
    out = defaultdict(int)
    for u, c in a.items():
        for v, d in b.items():
            if not u & v and survive(u | v, n, edges):
                out[u | v] += c * d
    return {u: c for u, c in out.items() if c}


def product(factors, n, edges):
    out = {0: 1}
    for factor in factors:
        out = multiply(out, factor, n, edges)
    return out


def derivative(a):
    out = defaultdict(int)
    for u, c in a.items():
        for j in range(u.bit_length()):
            if u & (1 << j):
                out[u ^ (1 << j)] += c
    return {u: c for u, c in out.items() if c}


def independent_sets(n, edges):
    return [u for u in range(1 << n) if survive(u, n, edges)]


def witnesses(n, edges):
    factors = [{1 << i: 1, 1 << (n+i): 1, 1 << (i+1): -1, 1 << (n+i+1): -1}
               for i in range(0, n-1, 2)]
    if n % 2:
        factors.append({1 << (n-1): 1, 1 << (2*n-1): 1})
    f = product(factors, n, edges)
    assert f and all(popcount(u) == (n+1)//2 for u in f)
    linear = {1 << i: 1 for i in range(2*n)}
    assert not multiply(f, linear, n, edges)
    C = max(independent_sets(n, edges), key=popcount)
    alpha = popcount(C)
    rest = [i for i in range(n) if not C & (1 << i)]
    factors = [{1 << i: 1, 1 << (n+i): -1} for i in range(n) if C & (1 << i)]
    factors += [{1 << (n+a): 1, 1 << (n+b): -1} for a,b in zip(rest[::2], rest[1::2])]
    g = product(factors, n, edges)
    assert g and all(popcount(u) == (n+alpha)//2 for u in g)
    assert not derivative(g)
    return alpha


def exact_ranks(n, edges):
    bases = [[] for _ in range(n+1)]
    for u in range(1 << (2*n)):
        if survive(u, n, edges):
            bases[popcount(u)].append(u)
    ranks = []
    for d in range(n):
        source, target = bases[d:d+2]
        idx = {u: i for i,u in enumerate(target)}
        M = sp.zeros(len(target), len(source))
        for j,u in enumerate(source):
            for k in range(2*n):
                if not u & (1 << k) and (u | (1 << k)) in idx:
                    M[idx[u | (1 << k)], j] = 1
        ranks.append(int(M.rank()))
    return [len(b) for b in bases], ranks


def main():
    tested = 0
    rank_tested = 0
    boundary = []
    for n in range(1,5):
        possible = list(itertools.combinations(range(n),2))
        for emask in range(1 << len(possible)):
            edges = [e for j,e in enumerate(possible) if emask & (1 << j)]
            alpha = witnesses(n,edges)
            tested += 1
            h,ranks = exact_ranks(n,edges)
            actual = all(r == min(h[d:d+2]) for d,r in enumerate(ranks))
            predicted = alpha == 1 or (n % 2 and alpha <= 2)
            assert actual == bool(predicted), (n,edges,h,ranks)
            rank_tested += 1
    rng = random.Random(20260908)
    for n in range(5,11):
        possible = list(itertools.combinations(range(n),2))
        for density in [0, 0.2, 0.5, 0.8, 1]:
            for _ in range(5):
                edges = [e for e in possible if rng.random() < density]
                witnesses(n,edges)
                tested += 1
        # The published difficult dense boundary: K_n minus a triangle.
        edges = [e for e in possible if not set(e) <= {0,1,2}]
        alpha = witnesses(n,edges)
        tested += 1
        assert alpha == 3
        if n <= 6:
            h,ranks = exact_ranks(n,edges)
            d = (n+1)//2
            assert ranks[d] < min(h[d:d+2])
            boundary.append({'n':n,'hilbert':h,'ranks':ranks,'failing_degree':d})
            rank_tested += 1
    result = {'seed':20260908,'witness_graphs':tested,'exact_rational_rank_graphs':rank_tested,
              'all_labeled_graphs_through_n':4,'dense_alpha_three_boundary':boundary,
              'result':'All assertions passed. Finite checks support but do not replace proof.'}
    Path(__file__).with_name('verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
