"""Independent certificate reconstruction and direct eta-product checks.

Does not import either of the author's certificate/coefficient modules.
The full pass uses the same exact FLINT library but a different eta-product
expression; small coefficients are also checked by integer product expansion.
"""
import argparse
from fractions import Fraction
from math import gcd, comb
from pathlib import Path
import hashlib
import json
import sys
import time

CANDIDATE = Path(__file__).resolve().parent
RECORDS = json.loads((CANDIDATE / 'check-results.json').read_text())


def reconstruct(row):
    k, m, t, exponent = (row[x] for x in ('k', 'm', 't', 's'))
    modulus = 5 ** exponent
    lift = (3*k + modulus) // modulus
    r = {1: modulus*lift-3*k-1, 2: k, 5: -(modulus//5)*lift, 10: 0}
    assert r == {int(d): v for d, v in row['r'].items()}
    assert row['N'] == 10 and row['mod'] == modulus and 0 <= t < m
    kap = gcd(m*m-1, 24)
    assert all(10 % p == 0 for p in (2, 5) if m % p == 0)
    assert m in (25, 125)  # establishes the complete prime support of m
    assert all(m*10 % d == 0 for d, v in r.items() if v)
    sigma = sum(d*v for d, v in r.items())
    assert kap*10*sum(v*(m*10//d) for d, v in r.items()) % 24 == 0
    assert kap*10*sum(r.values()) % 8 == 0
    assert 10 % (24*m // gcd(kap*(-24*t-sigma), 24*m)) == 0
    assert m % 2 == 1  # the sixth Delta-star condition is inapplicable
    orbit = set()
    for x in range(24*m):
        if gcd(x, 24*m) != 1:
            continue
        sq = x*x % (24*m)
        assert (sq-1) % 24 == 0
        orbit.add((t*sq + (sq-1)//24*sigma) % m)
    assert sorted(orbit) == row['P']
    minima = {}
    for cusp in (1, 2, 5, 10):
        vals = []
        for ell in range(m):
            vals.append(sum(Fraction(v*gcd(d*(1+kap*ell*cusp), m*cusp)**2, d*m)
                            for d, v in r.items()))
        minima[cusp] = min(vals)
    assert {str(c): str(v) for c, v in minima.items()} == row['lower24']
    aux = int(row['aux']['1'])
    assert aux >= 0 and all(v + aux >= 0 for v in minima.values())
    nu = Fraction(18*(sum(r.values())+aux)-aux, 24) - Fraction(sigma, 24*m) - Fraction(min(orbit), m)
    bound = nu.numerator // nu.denominator
    assert str(nu) == row['nu'] and bound == row['bound']
    assert row['max_coefficient'] == m*bound+max(orbit)
    assert row['check_count'] == len(orbit)*(bound+1)
    assert row['all_zero'] and row['failures'] == []
    return r


def product_initial(k, n):
    out = [1] + [0]*n
    for part in range(1, n+1):
        colors = (3*k+1) if part % 2 else (2*k+1)
        weights = [comb(colors+j-1, j) for j in range(n//part+1)]
        nxt = [0]*(n+1)
        for i, v in enumerate(out):
            for j in range((n-i)//part+1):
                nxt[i+j*part] += v*weights[j]
        out = nxt
    return out


def euler_series(length, modulus, stride, poly):
    coefficients = [0]*length
    coefficients[0] = 1
    j = 1
    while stride*j*(3*j-1)//2 < length:
        for power in (j*(3*j-1)//2, j*(3*j+1)//2):
            if power*stride < length:
                coefficients[power*stride] = 1 if j % 2 == 0 else modulus-1
        j += 1
    return poly(coefficients, modulus)


def full_check():
    sys.path.insert(0, str(CANDIDATE/'vendor'))
    from flint import nmod_poly
    groups = {}
    for row in RECORDS:
        groups.setdefault((row['k'], row['mod']), []).append(row)
    results = []
    for (k, modulus), rows in groups.items():
        started = time.time()
        n = max(row['max_coefficient'] for row in rows) + 1
        r = reconstruct(rows[0])
        # Direct congruent eta product f1^r1*f2^r2/f5^(-r5).
        # This differs from the author's f1^(-1)*(f2/f1^3)^k.
        a = euler_series(n, modulus, 1, nmod_poly).pow_trunc(r[1], n)
        b = euler_series(n, modulus, 2, nmod_poly).pow_trunc(r[2], n)
        c = euler_series(n, modulus, 5, nmod_poly).inverse_series_trunc(n).pow_trunc(-r[5], n)
        series = a.mul_low(b, n).mul_low(c, n)
        early = product_initial(k, 116)
        assert all(int(series[i]) == v % modulus for i, v in enumerate(early))
        count = 0
        for row in rows:
            for residue in row['P']:
                for j in range(row['bound']+1):
                    index = row['m']*j+residue
                    assert int(series[index]) == 0, (k, modulus, index, int(series[index]))
                    count += 1
        result = dict(k=k, modulus=modulus, through=n-1, tested=count,
                      seconds=round(time.time()-started, 3), status='PASS')
        results.append(result)
        print(json.dumps(result), flush=True)
        (CANDIDATE/'independent-results.json').write_text(json.dumps(results, indent=2)+'\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--full', action='store_true')
    args = parser.parse_args()
    for row in RECORDS:
        reconstruct(row)
    initial = json.loads((CANDIDATE/'initial-checks.json').read_text())
    for row in initial:
        coefficients = product_initial(row['k'], 116)
        assert coefficients[66] == row['n66'] and coefficients[116] == row['n116']
        c = row['c']
        assert coefficients[66] % 3125 == 625*c*(c-2) % 3125
        assert coefficients[116] % 3125 == -625*c*(c-2) % 3125
    print('PASS: 35 exact certificates and five independent integer expansions.', flush=True)
    if args.full:
        full_check()
