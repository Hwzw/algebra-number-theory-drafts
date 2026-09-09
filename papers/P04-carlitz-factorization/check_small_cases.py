"""Exact finite checks, supplementary to the hand proof; only prime q tested.

Enumerate every possible numerator root-multiplicity vector of a divisor.
Check all relevant prime fixed-divisor inequalities using exact arithmetic.
No bounded factorization search is used as a substitute for the proof.
"""

from itertools import product
import json


def coefficients(n, p):
    out = []
    while n:
        out.append(n % p)
        n //= p
    return out


def encode(c, p):
    return sum(a * p**i for i, a in enumerate(c))


def subtract(a, b, p):
    aa, bb = coefficients(a, p), coefficients(b, p)
    return encode(
        [((aa[i] if i < len(aa) else 0) -
          (bb[i] if i < len(bb) else 0)) % p
         for i in range(max(len(aa), len(bb)))], p)


def divide(a, b, p):
    aa, bb = coefficients(a, p), coefficients(b, p)
    q = [0] * max(0, len(aa) - len(bb) + 1)
    while aa and len(aa) >= len(bb):
        shift = len(aa) - len(bb)
        factor = aa[-1] * pow(bb[-1], -1, p) % p
        q[shift] = factor
        for i, bi in enumerate(bb):
            aa[shift + i] = (aa[shift + i] - factor * bi) % p
        while aa and aa[-1] == 0:
            aa.pop()
    return encode(q, p), encode(aa, p)


def irreducibles(p, s):
    found = []
    for d in range(1, s + 1):
        for f in range(p**d, 2 * p**d):  # monic, degree d
            if all(divide(f, g, p)[1] for g, gd in found if gd <= d // 2):
                found.append((f, d))
    return found


def valuation(a, pi, p, cap):
    if not a:
        return cap
    v = 0
    while v < cap:
        a1, rem = divide(a, pi, p)
        if rem:
            break
        a = a1
        v += 1
    return v


def check(p, exponents):
    s = len(exponents) - 1
    roots = list(range(p**s))
    multiplicities = [sum(a for i, a in enumerate(exponents)
                          if f < p**i) for f in roots]
    prime_data = []
    for pi, d in irreducibles(p, s):
        cap = s // d + 1
        rows = {tuple(valuation(subtract(x, f, p), pi, p, cap)
                      for f in roots) for x in range(p**(cap * d))}
        target = sum(a * sum(p**(i - j * d) for j in range(1, i // d + 1))
                     for i, a in enumerate(exponents))
        prime_data.append((rows, target))
    expected = {tuple(sum(b for i, b in enumerate(bs) if f < p**i)
                      for f in roots)
                for bs in product(*(range(a + 1) for a in exponents))}
    accepted = set()
    tested = 0
    for u in product(*(range(w + 1) for w in multiplicities)):
        tested += 1
        complement = tuple(w - z for w, z in zip(multiplicities, u))
        valid = True
        for rows, target in prime_data:
            mu = min(sum(v * z for v, z in zip(row, u)) for row in rows)
            muj = min(sum(v * z for v, z in zip(row, complement)) for row in rows)
            if mu + muj != target:
                valid = False
                break
        if valid:
            accepted.add(u)
    assert accepted == expected, (p, exponents, accepted ^ expected)
    return {"q": p, "exponents": exponents, "numerators_tested": tested,
            "divisor_classes": len(accepted), "status": "PASS"}


if __name__ == "__main__":
    cases = [(2, (1, 1, 1)), (2, (2, 1, 2)),
             (2, (1, 1, 1, 1)), (3, (1, 1, 1))]
    print(json.dumps([check(p, a) for p, a in cases], indent=2))
