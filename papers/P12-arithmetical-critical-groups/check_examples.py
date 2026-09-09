"""Exact indexing checks; no numerical evidence is used as a proof."""
from fractions import Fraction
from functools import reduce
from math import gcd, lcm, prod
from pathlib import Path
import json
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def order(matrix):
    sf = smith_normal_form(Matrix(matrix), domain=ZZ)
    factors = [abs(int(sf[i, i])) for i in range(sf.rows) if sf[i, i]]
    return prod(factors), factors


def complete(q):
    return [[(q[i] if i == j else 0) - 1 for j in range(len(q))]
            for i in range(len(q))]


def star(q):
    n = len(q)
    central = sum(Fraction(1, x) for x in q)
    assert central.denominator == 1
    L = [[0] * (n + 1) for _ in range(n + 1)]
    L[0][0] = int(central)
    for i, x in enumerate(q, 1):
        L[0][i] = L[i][0] = -1
        L[i][i] = x
    return L


records = []
s = [2]
for _ in range(9):
    s.append(prod(s) + 1)
for n in range(2, 10):
    if n <= 4:
        q = [n] * n
        expected = n ** (n - 2)
    elif n == 5:
        q, expected = [2, 8, 8, 8, 8], 128
    else:
        t = s[n - 3] - 1
        q = s[:n - 3] + [3 * t] * 3
        expected = 3 * t * t
    ell = lcm(*q)
    r = [ell // x for x in q]
    assert reduce(gcd, r) == 1
    assert sum(Fraction(1, x) for x in q) == 1
    assert Matrix(complete(q)) * Matrix(r) == Matrix.zeros(n, 1)
    kc, fc = order(complete(q))
    ks, fs = order(star(q))
    assert kc == ks == expected == prod(q) // ell**2
    records.append(dict(n=n, denominators=q, order=kc,
                        complete_invariant_factors=fc,
                        star_invariant_factors=fs))

q = [2, 2, 2, 2]
old = order(star(q))[0]
new = order(complete([2 * x for x in q]))[0]
assert old == 4 and new == 2**2 * old == 16

output = dict(description='Exact SNF and kernel checks of all stated extremal formulas for 2<=n<=9, plus a nonunit star center.',
              records=records, star_scaling=dict(q=q, central_label=2, old=old, new=new))
Path(__file__).with_name('exact_checks.json').write_text(json.dumps(output, indent=2) + '\n')
print('PASS: 8 extremal pairs, primitive kernels, and nonunit star scaling')
