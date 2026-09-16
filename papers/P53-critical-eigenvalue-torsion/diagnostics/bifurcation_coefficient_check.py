"""Exact coefficient checks for note 0245, not a proof of bifurcation."""
import hashlib
import json
from pathlib import Path

import sympy as S

root = Path(__file__).resolve().parent
n, x, q, ell, d = S.symbols("n x q ell d")
s, b = S.symbols("s b")
qv = 2 * (x - 1) / (n + 2)
qp = (4 * (n - 1) * x - 2 * n + 6) / ((n + 2) * (3 * n - 1))
beta = ((n + 2) * q - 2) / (n - 1)
ef = 2 * d + 2 * (n - 1) - (n + 2) * q * (ell - 1)
eg = (2 * d + n - 1 + (n + 2) * q * (n + 1 - 2 * ell) / 2
      - beta * (ell * (ell + n - 2) + (n - 1) * (n - 2)) / 2)
ef2 = S.factor(ef.subs({ell: 2, d: x - n}))
eg2 = S.factor(eg.subs({ell: 2, d: x - n}))
assert S.simplify(ef2.subs(q, qv)) == 0
assert S.simplify(eg2.subs(q, qp)) == 0
assert S.diff(ef2, q) == -n - 2
assert S.simplify(S.diff(eg2, q) + (n + 2) * (3 * n - 1) / (2 * (n - 1))) == 0

endpoint = json.loads((root / "endpoint_expansion.json").read_text())
dimensional = json.loads((root / "dimensional_endpoint_check.json").read_text())
j = S.Symbol("j")
cf = S.sympify(endpoint["critical_quartic"]).subs(j**2, s)
cg = S.sympify(dimensional["planar_perimeter_critical_quartic"]).subs(j**2, s)
d4 = -4 + s * (8 - s) / (8 * (6 - s))
ef4 = ef.subs({n: 2, ell: 4, d: d4, q: (s - 2) / 4})
eg4 = eg.subs({n: 2, ell: 4, d: d4, q: (s + 1) / 10})
assert S.simplify(S.diff(cf, b, 2) - ef4) == 0
assert S.simplify(S.diff(cg, b, 2) - eg4) == 0
bf = -(3 * s**3 - 67 * s**2 + 320 * s - 192) / (4 * s * (11 * s - 64))
bg = -(15 * s**3 - 347 * s**2 + 1720 * s - 1248) / (4 * (79 * s**2 - 560 * s + 576))
assert S.simplify(S.diff(cf, b).subs(b, bf)) == 0
assert S.simplify(S.diff(cg, b).subs(b, bg)) == 0
# Independent exact negativity certificate for both b^2 coefficients on
# 23/4 < s < 29/5. The second numerator is increasing on this interval.
a, z = S.Rational(23, 4), S.Rational(29, 5)
assert 11 * z - 64 < 0
p = 79 * s**2 - 560 * s + 576
assert S.diff(p, s).subs(s, a) > 0
assert p.subs(s, z) < 0
report = {
    "status": "Exact algebra diagnostics only; analytic bifurcation proof is note 0245",
    "degree_two_volume_coefficient": str(ef2),
    "degree_two_perimeter_coefficient": str(eg2),
    "both_critical_coefficients_zero": True,
    "volume_transversality": str(S.diff(ef2, q)),
    "perimeter_transversality": str(S.factor(S.diff(eg2, q))),
    "quartic_b_squared_matches_degree_four_hessian": True,
    "both_quartic_b_squared_coefficients_strictly_negative_on_certified_interval": True,
    "planar_volume_b": str(bf),
    "planar_perimeter_b": str(bg),
    "volume_reduced_quartic": str(S.factor(cf.subs(b, bf))),
    "perimeter_reduced_quartic": str(S.factor(cg.subs(b, bg))),
    "source_report_sha256": {
        name: hashlib.sha256((root / name).read_bytes()).hexdigest()
        for name in ("endpoint_expansion.json", "dimensional_endpoint_check.json")
    },
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(root / "bifurcation_coefficient_check.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
