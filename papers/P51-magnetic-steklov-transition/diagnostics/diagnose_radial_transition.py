"""Floating-point diagnostic only; the proof is in note 0202.

Reproduce with the bundled Python (NumPy required). No special-function
library is needed. Logarithmic quadrature is refined once; no interval
error certification or universal theorem is claimed.
"""
import json
from pathlib import Path
import numpy as np

GAMMA = 0.5772156649015328606


def digamma(x):
    value = 0.0
    while x < 20.0:
        value -= 1.0 / x
        x += 1.0
    y = 1.0 / (x * x)
    return value + np.log(x) - 0.5 / x - y * (
        1.0 / 12.0 - y * (1.0 / 120.0 - y * (
            1.0 / 252.0 - y * (1.0 / 240.0 - y / 132.0))))


def radial(b, p, radius, step):
    a = 0.5 + p / (4.0 * b)
    z = b * radius * radius
    eta = a * z
    lo, hi = np.log(eta) - 100.0, np.log(100.0)
    count = int(np.ceil((hi - lo) / step)) + 1
    y = np.linspace(lo, hi, count)
    x = np.exp(y)
    weight = np.exp(-x - a * np.log1p(z / x))
    integral = np.trapezoid(weight, y)
    derivative = np.trapezoid(x * weight, y)
    exact_quadrature = z / radius + 2.0 * derivative / (radius * integral)
    denominator = -np.log(z) - digamma(a) - 2.0 * GAMMA
    model = 2.0 / (radius * denominator)
    return exact_quadrature, model, integral, denominator


def main():
    cases = []
    for radius in (1.0, 2.3):
        for rho in (1e-3, 1e-5, 1e-7):
            for fraction in (1.0, 0.5, 1e-6, 1e-12):
                b, p = fraction * rho, (1.0 - fraction) * rho
                coarse = radial(b, p, radius, 0.004)
                fine = radial(b, p, radius, 0.002)
                value, model, integral, denominator = fine
                cases.append(dict(
                    radius=radius, rho=rho, b_fraction=fraction,
                    p_over_b=p / b, radial_quadrature=float(value),
                    proposed_model=float(model),
                    error_over_rho=float((value - model) / rho),
                    refinement_difference=float(abs(value - coarse[0])),
                    integral_minus_shifted_log=float(integral - denominator),
                ))
    result = dict(
        status="Unvalidated floating-point consistency diagnostic; not proof",
        normalization="A=(-y,x), curl(bA)=2b",
        cases=cases,
        max_refinement_difference=max(c['refinement_difference'] for c in cases),
        max_abs_error_over_rho=max(abs(c['error_over_rho']) for c in cases),
    )
    destination = Path(__file__).with_name('radial-transition-diagnostics.json')
    destination.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'cases'}, indent=2))
    print(f"{len(cases)} cases written to {destination}")


if __name__ == '__main__':
    main()
