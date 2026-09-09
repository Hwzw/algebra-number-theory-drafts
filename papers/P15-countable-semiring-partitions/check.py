"""Exact finite checks for endpoint labels; these are not the general proof.

Run with Python 3 and SymPy. Each input is positive on the whole interval
(2, 4), so the rational test point 31/10 also represents any transcendental
alpha in that interval for these same-label operations. Sturm counts verify
that cancellation creates no intervening real zero or pole.
"""
from pathlib import Path
import hashlib
import json
import random
import sympy as s

t = s.Symbol('t')
probe = s.Rational(31, 10)
rng = random.Random(9152026)
roots = [-3, -2, 0, 1, 2, 4, 5, 6]


def order(poly, point):
    n = 0
    while poly.eval(point) == 0:
        poly = poly.exquo(s.Poly(t-point, t))
        n += 1
    return n


def certify(expr, endpoint, kind):
    num, den = map(lambda p: s.Poly(p, t, domain=s.QQ),
                   s.fraction(s.cancel(expr)))
    assert num.eval(probe) / den.eval(probe) > 0
    lo = -s.oo if endpoint is None else s.Rational(endpoint)
    if endpoint is not None:
        exponent = order(num, lo) - order(den, lo)
        assert (exponent > 0) == (kind == 'Z') and exponent != 0
    for poly in (num, den):
        if endpoint is not None:
            while poly.eval(lo) == 0:
                poly = poly.exquo(s.Poly(t-lo, t))
        assert poly.count_roots(lo, probe) == 0


groups = {}
for _ in range(180):
    chosen = rng.sample(roots, rng.randrange(0, 5))
    exponents = {r: rng.choice([-2, -1, 1, 2]) for r in chosen}
    expr = s.Integer(rng.randrange(1, 5))
    for r, e in exponents.items():
        expr *= (t-r)**e
    expr *= (t*t+1)**rng.choice([-1, 0, 1])
    if expr.subs(t, probe) < 0:
        expr = -expr
    left = [r for r in chosen if r < probe]
    a = max(left) if left else None
    kind = None if a is None else ('Z' if exponents[a] > 0 else 'P')
    certify(expr, a, kind)
    groups.setdefault((a, kind), []).append(expr)

pairs = 0
for (a, kind), values in groups.items():
    for _ in range(25):
        f, g = rng.choice(values), rng.choice(values)
        certify(f+g, a, kind)
        certify(f*g, a, kind)
        pairs += 1

# Cancellation and the necessity of keeping endpoint types separate.
assert s.cancel((t-2)/(t-2)) == 1
assert s.cancel((t-2) * (t-2)**-1) == 1
certify(1/(t-2) + 1/(t-2)**2, 2, 'P')
certify((t-2) + (t-2)**2, 2, 'Z')
certify((t-2)**2 + (t-2)**4, 2, 'Z')
certify((t*t+1) + 1/(t*t+1), None, None)

folder = Path(__file__).resolve().parent
result = {
    'input_functions': 180,
    'nonempty_left_label_groups': len(groups),
    'same_label_pairs': pairs,
    'sum_and_product_sturm_certificates': 2*pairs,
    'explicit_edge_cases': 6,
    'status': 'passed',
    'scope': 'exact rational-function examples; not a proof or a test of the curve theorem',
    'proof': 'manuscript.tex',
    'sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
               for p in [folder/'manuscript.tex', Path(__file__).resolve()]},
}
(folder/'check-results.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
