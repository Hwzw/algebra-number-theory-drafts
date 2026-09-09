#!/usr/bin/env python3
"""Exact finite ideal identities and complete finite-quotient conductor checks."""
import itertools
import json
from pathlib import Path


def compositions(n, r):
    if r == 1:
        yield (n,)
    else:
        for i in range(n+1):
            for tail in compositions(n-i, r-1):
                yield (i,) + tail


def leq(a, b):
    return all(x <= y for x, y in zip(a, b))


def minimal(vectors):
    vectors = set(vectors)
    return tuple(sorted(a for a in vectors if not any(b != a and leq(b, a) for b in vectors)))


def colon(gens, p):
    return minimal(tuple(max(0, x-int(j == p)) for j, x in enumerate(a)) for a in gens)


def reconstruct(gens):
    rank = len(gens[0])
    classes = {}
    for p in range(rank):
        classes.setdefault(colon(gens, p), []).append(p)
    colors = list(classes.values())
    patterns = minimal(tuple(sum(a[p] for p in color) for color in colors) for a in gens)
    expanded = []
    for pattern in patterns:
        choices = [list(compositions(n, len(color))) for n, color in zip(pattern, colors)]
        for parts in itertools.product(*choices):
            a = [0]*rank
            for color, part in zip(colors, parts):
                for p, x in zip(color, part):
                    a[p] = x
            expanded.append(tuple(a))
    assert minimal(expanded) == minimal(gens)
    return len(colors)


def quotient_case(name, modulus, weights, colors, cap, basis, unit_order=1, unit_step=1):
    # States retain a finite unit group, the divisor class, and truncated color counts.
    r = max(colors)+1
    zero = (0, 0, (0,)*r)
    def mul(a, b):
        return ((a[0]+b[0]) % unit_order, (a[1]+b[1]) % modulus,
                tuple(min(cap, x+y) for x, y in zip(a[2], b[2])))
    generators = [(1 % unit_order, 0, (0,)*r)]
    for w, color in zip(weights, colors):
        v = tuple(int(j == color) for j in range(r))
        generators.append((0, w % modulus, v))
    states = {zero}
    todo = [zero]
    while todo:
        a = todo.pop()
        for g in generators:
            b = mul(a, g)
            if b not in states:
                states.add(b)
                todo.append(b)
    states = sorted(states)
    def in_f(a):
        return a[1] == 0 and any(leq(b, a[2]) for b in basis)
    def in_m(a):
        return in_f(a) or (not any(a[2]) and a[0] % unit_step == 0)
    h_states = [a for a in states if a[1] == 0]
    proper = any(not in_m(a) for a in h_states)
    table = {a: tuple(in_m(mul(a, b)) for b in states) for a in states}
    h_indices = [i for i, a in enumerate(states) if a[1] == 0]
    conductor = {a for a in states if all(table[a][i] for i in h_indices)}
    expected = {a for a in states if in_f(a)} if proper else set(h_states)
    assert conductor == expected
    signatures = {
        table[a]
        for a in states if any(a[2]) or a == zero
    }
    assert len(signatures) <= 1 + modulus*(cap+1)**r
    return dict(name=name, finite_quotient_states=len(states),
                full_context_comparisons=len(states)**2,
                reduced_class_count=len(signatures), proper=proper,
                exact_conductor_verified=True)


def run():
    identities = []
    for rank in range(2, 5):
        for degree in range(1, 6):
            gens = list(compositions(degree, rank))
            assert reconstruct(gens) == 1
            identities.append(dict(kind='total_degree', rank=rank, degree=degree))
    for pairs in range(1, 7):
        gens = [tuple(int(j in (2*i, 2*i+1)) for j in range(2*pairs)) for i in range(pairs)]
        assert reconstruct(gens) == 2*pairs
        identities.append(dict(kind='matching', pairs=pairs, prime_profiles=2*pairs))
    # Symmetric but nonuniform threshold patterns on two pairs of prime colors.
    for left in range(1, 4):
        for right in range(1, 4):
            gens = [a+b for a in compositions(left, 2) for b in compositions(right, 2)]
            assert reconstruct(gens) == 2
            identities.append(dict(kind='two_colors', left=left, right=right))
    cases = []
    for degree in range(2, 7):
        q = quotient_case('degree_'+str(degree), 1, (0, 0), (0, 0), degree, [(degree,)])
        assert q['reduced_class_count'] == degree+1
        cases.append(q)
    cases.append(quotient_case('reduced_maximal_exception', 1, (0,), (0,), 1, [(1,)]))
    cases.append(quotient_case('units_repair_maximal', 1, (0,), (0,), 1, [(1,)], 3, 3))
    cases.append(quotient_case('all_units_maximal_exception', 1, (0,), (0,), 1, [(1,)], 3, 1))
    cases.append(quotient_case('parity_mixed_ideal', 2, (1, 1), (0, 1), 1, [(1, 1)], 4, 2))
    cases.append(quotient_case('class_three_degree', 3, (1, 1), (0, 0), 3, [(3,)], 2, 2))
    cases.append(quotient_case('opposite_classes', 3, (1, 1, 2, 2), (0, 0, 1, 1), 1, [(1, 1)]))
    cases.append(quotient_case('finite_matching', 1, (0,)*4, (0, 1, 2, 3), 1,
                               [(1, 1, 0, 0), (0, 0, 1, 1)]))
    assert cases[6]['reduced_class_count'] == 2
    return dict(status='pass', exact_monomial_ideal_identities=len(identities),
                ideal_cases=identities, complete_finite_quotient_cases=cases,
                total_context_comparisons=sum(x['full_context_comparisons'] for x in cases),
                scope='Full finite quotients and exact finite monomial ideals; infinite-rank necessity and the general theorem have hand proofs.')


if __name__ == '__main__':
    result = run()
    Path(__file__).with_name('check-results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('ideal_cases','complete_finite_quotient_cases')}, indent=2))
