"""Finite circular-hole checks of note 0233; not a proof or priority check.

The full disk eigenvalue has angular multiplicity two. We work in one fixed
cosine angular sector, which remains invariant for concentric holes. These
are consistency checks of the coefficients, not examples of the theorem's
full-domain simplicity hypothesis.
"""

from pathlib import Path
import json
import mpmath as mp

mp.mp.dps = 90


def derivative(fn, k, x):
    return (fn(k - 1, x) - fn(k + 1, x)) / 2


def check(k, alpha_text):
    alpha = mp.mpf(alpha_text)

    def outer_j(t):
        return t * derivative(mp.besselj, k, t) + alpha * mp.besselj(k, t)

    # The first positive root is bracketed by adjacent grid points.
    left = mp.mpf("0.05")
    for j in range(2, 401):
        right = mp.mpf(j) / 20
        if outer_j(left) * outer_j(right) < 0:
            break
        left = right
    else:
        raise RuntimeError("Failed to bracket the unperturbed sector root")
    t0 = mp.findroot(outer_j, (left, right))
    norm2 = mp.pi * mp.quad(lambda r: r * mp.besselj(k, t0 * r) ** 2, [0, 1])
    a2 = (t0**k / (2**k * mp.factorial(k))) ** 2 / norm2
    leading = 2 * k * mp.pi * a2
    next_coefficient = 4 * alpha * mp.pi * a2
    rows = []
    for eps_text in ("0.01", "0.003", "0.001"):
        eps = mp.mpf(eps_text)

        def determinant(t):
            inner_j = t * derivative(mp.besselj, k, t * eps) - alpha * mp.besselj(k, t * eps)
            inner_y = t * derivative(mp.bessely, k, t * eps) - alpha * mp.bessely(k, t * eps)
            outer_y = t * derivative(mp.bessely, k, t) + alpha * mp.bessely(k, t)
            return outer_j(t) - inner_j * outer_y / inner_y

        root = mp.findroot(determinant, (t0 * mp.mpf("0.999"), t0 * mp.mpf("1.001")))
        shift = root**2 - t0**2
        ratio = (shift + leading * eps ** (2 * k)) / (next_coefficient * eps ** (2 * k + 1))
        rows.append({"epsilon": eps_text, "second_coefficient_ratio": mp.nstr(ratio, 24),
                     "determinant_residual": mp.nstr(abs(determinant(root)), 6)})
    assert abs(mp.mpf(rows[-1]["second_coefficient_ratio"]) - 1) < mp.mpf("0.05")
    return {"k": k, "alpha": alpha_text, "unperturbed_root": mp.nstr(t0, 24),
            "leading_coefficient": mp.nstr(leading, 24),
            "next_coefficient": mp.nstr(next_coefficient, 24), "samples": rows}


def main():
    result = {"status": "finite coefficient consistency only", "precision_decimal_digits": mp.mp.dps,
              "multiplicity_caveat": __doc__.split("\n\n", 1)[1].strip(),
              "cases": [check(k, a) for k, a in [(1, "0.7"), (2, "0.7"), (3, "0.7"),
                                                   (1, "-0.5"), (2, "-0.5"), (3, "-0.5")]],
              "nonnodal_radial_cases": [check_nonnodal(a) for a in ("0.7", "-0.5")]}
    target = Path(__file__).with_name("round-coefficient-check.json")
    target.write_text(json.dumps(result, indent=2) + "\n")
    print("Six nodal sector checks and two nonnodal logarithmic slope checks passed; 24 roots. Not a proof.")
    for row in result["cases"]:
        print(row["k"], row["alpha"], row["samples"][-1]["second_coefficient_ratio"])
    for row in result["nonnodal_radial_cases"]:
        print("nonnodal slope", row["alpha"], row["last_two_logarithmic_slope_ratio"])


def check_nonnodal(alpha_text):
    alpha = mp.mpf(alpha_text)

    def outer(t):
        return t * derivative(mp.besselj, 0, t) + alpha * mp.besselj(0, t)

    left = mp.mpf("0.05")
    for j in range(2, 401):
        right = mp.mpf(j) / 20
        if outer(left) * outer(right) < 0:
            break
        left = right
    else:
        raise RuntimeError("Failed to bracket the radial root")
    root0 = mp.findroot(outer, (left, right))
    u02 = 1 / (2 * mp.pi * mp.quad(lambda r: r * mp.besselj(0, root0 * r) ** 2, [0, 1]))
    first = 2 * mp.pi * alpha * u02
    log_coefficient = -2 * mp.pi * alpha**2 * u02
    rows = []
    for eps_text in ("0.01", "0.0001", "0.00000001"):
        eps = mp.mpf(eps_text)

        def determinant(t):
            j_inner = t * derivative(mp.besselj, 0, t * eps) - alpha * mp.besselj(0, t * eps)
            y_inner = t * derivative(mp.bessely, 0, t * eps) - alpha * mp.bessely(0, t * eps)
            y_outer = t * derivative(mp.bessely, 0, t) + alpha * mp.bessely(0, t)
            return outer(t) - j_inner * y_outer / y_inner

        root = mp.findroot(determinant, (root0 * mp.mpf("0.999"), root0 * mp.mpf("1.001")))
        ratio = (root**2 - root0**2 - first * eps) / (log_coefficient * eps**2 * mp.log(1 / eps))
        rows.append({"epsilon": eps_text, "logarithmic_coefficient_ratio": mp.nstr(ratio, 24),
                     "determinant_residual": mp.nstr(abs(determinant(root)), 6)})
    # A constant epsilon^2 term can swamp the raw ratio even at epsilon=1e-8.
    # Keep the raw values; the divided difference tests the log coefficient.
    prev, last = rows[-2:]
    prev_log = mp.log(1 / mp.mpf(prev["epsilon"]))
    last_log = mp.log(1 / mp.mpf(last["epsilon"]))
    slope = (mp.mpf(last["logarithmic_coefficient_ratio"]) * last_log
             - mp.mpf(prev["logarithmic_coefficient_ratio"]) * prev_log) / (last_log - prev_log)
    assert abs(slope - 1) < mp.mpf("0.02")
    return {"alpha": alpha_text, "positive_radial_root": mp.nstr(root0, 24),
            "first_coefficient": mp.nstr(first, 24), "log_coefficient": mp.nstr(log_coefficient, 24),
            "samples": rows, "last_two_logarithmic_slope_ratio": mp.nstr(slope, 24),
            "initial_check_history": "An initial raw-ratio tolerance 0.3 at epsilon=1e-8 failed for alpha=-0.5. The raw deviations times log(1/epsilon) approached a nonzero constant, consistent with the O(epsilon^2) remainder. Replaced that unsuitable criterion with the displayed divided-difference diagnostic; no theorem changed."}


if __name__ == "__main__":
    main()
