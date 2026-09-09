#!/usr/bin/env python3
"""Exact, standard-library certificate checks for the displayed formulas.

Run: python3 check.py [output.json]
These identities support the hand proof; they do not certify historical novelty.
"""
import hashlib
import json
from pathlib import Path
import sys


def normal(m):
    a, b, c, z = m
    a += b // 2
    c += b // 2
    b %= 2
    a += c // 2
    z += c // 2
    c %= 2
    return a, b, c, z


def poly(terms):
    ans = {}
    for m, coefficient in terms:
        m = normal(m)
        ans[m] = ans.get(m, 0) + coefficient
    return {m: c for m, c in ans.items() if c}


ZERO = {}
ONE = {(0, 0, 0, 0): 1}


def add(*args):
    return poly((m, c) for p in args for m, c in p.items())


def neg(p):
    return {m: -c for m, c in p.items()}


def mul(p, q):
    return poly((tuple(x+y for x, y in zip(m, n)), a*b)
                for m, a in p.items() for n, b in q.items())


def mon(a, b, c, z):
    return poly([((a, b, c, z), 1)])


def mm(p, q):
    return [[add(*(mul(p[i][j], q[j][k]) for j in range(2)))
             for k in range(2)] for i in range(2)]


def ma(p, q):
    return [[add(p[i][j], q[i][j]) for j in range(2)] for i in range(2)]


def mn(p):
    return [[neg(x) for x in row] for row in p]


def determinant(p):
    return add(mul(p[0][0], p[1][1]), neg(mul(p[0][1], p[1][0])))


def image(p):
    ans = {}
    for (a, b, c, z), coefficient in p.items():
        m = (4*a+3*b+2*c, 4*z+b+2*c)
        ans[m] = ans.get(m, 0)+coefficient
    return {m: c for m, c in ans.items() if c}


def run():
    identity = [[ONE, ZERO], [ZERO, ONE]]
    e11 = [[ONE, ZERO], [ZERO, ZERO]]
    zero_matrix = [[ZERO, ZERO], [ZERO, ZERO]]
    assert add(mon(0, 2, 0, 0), neg(mon(1, 0, 1, 0))) == ZERO
    assert add(mon(0, 0, 2, 0), neg(mon(1, 0, 0, 1))) == ZERO
    rows = []
    for r in [0, 1, 2, 3, 7, 10, 25]:
        powers = {2: mon(0, 0, 1, 2*r+1),
                  3: mon(0, 1, 0, 3*r+2),
                  4: mon(1, 0, 0, 4*r+3),
                  5: mon(0, 1, 1, 5*r+3)}
        for j, v in powers.items():
            assert image(v) == {(j, (4*r+3)*j): 1}
            assert all(sum(m) == j*(r+1) for m in v)
        p = [[add(ONE, neg(powers[4])), add(*powers.values())],
             [add(powers[2], neg(powers[3])), powers[4]]]
        q = ma(identity, mn(p))
        assert mm(p, p) == p and mm(q, q) == q
        assert mm(p, q) == zero_matrix and mm(q, p) == zero_matrix
        assert ma(p, q) == identity
        assert determinant(p) == ZERO and add(p[0][0], p[1][1]) == ONE
        delta = ma(p, mn(e11))
        assert min(sum(m) for row in delta for v in row for m in v) == 2*r+2
        w = ma(mm(p, e11), mm(q, ma(identity, mn(e11))))
        assert mm(w, e11) == mm(p, w)
        assert determinant(w) == add(ONE, neg(powers[4]))
        rows.append({'r': r, 'first_difference_degree': 2*r+2,
                     'idempotence_orthogonality_trace_determinant': True,
                     'formal_intertwiner': True,
                     'power_substitution_in_polynomial_ring': True})

    # Distinct normal monomials, with an independent semigroup description.
    degrees = []
    for degree in range(31):
        pairs = set()
        for epsilon in [0, 1]:
            for delta in [0, 1]:
                remaining = degree-epsilon-delta
                for i in range(remaining+1):
                    j = remaining-i
                    pair = (4*i+3*epsilon+2*delta, 4*j+epsilon+2*delta)
                    assert pair not in pairs
                    pairs.add(pair)
        expected = {0} if degree == 0 else set(range(4*degree+1))-{1}
        assert {s for s, t in pairs} == expected
        degrees.append({'degree': degree, 'dimension': len(pairs)})

    # In D, (1+d*z^r)^m=1+m*d*z^r; record the exact restriction on n.
    characteristic_rows = []
    for characteristic in [0, 2, 3, 5, 7]:
        for n in range(2, 10):
            coefficient = n if characteristic == 0 else n % characteristic
            characteristic_rows.append({'characteristic': characteristic,
                                        'matrix_size': n,
                                        'obstruction_coefficient': coefficient,
                                        'theorem_applies': coefficient != 0})
    return {'all_passed': True, 'arithmetic': 'integer polynomial quotient; no floating point',
            'matrix_certificates': rows, 'normal_monomial_checks': degrees,
            'characteristic_boundary_checks': characteristic_rows,
            'limitations': 'Finite certificate checks support the universal hand proof. No automated novelty or significance certification.',
            'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


if __name__ == '__main__':
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name('check-results.json')
    result = run()
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'all_passed': result['all_passed'], 'output': str(output)}))
