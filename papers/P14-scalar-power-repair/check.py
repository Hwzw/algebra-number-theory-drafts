"""Exact finite consistency checks; not a proof or a novelty certificate.

Uses only the Python standard library. The state traversal implements the
finite stopping rule independently of closed forms used in extended checks.
"""
from fractions import Fraction
from math import gcd, lcm
from pathlib import Path
import hashlib
import json


def vp(x, p, cap):
    if x == 0:
        return cap
    result = 0
    while result < cap and x % p == 0:
        result += 1
        x //= p
    return result


def state_cycle(initial, coeffs, modulus):
    # coeffs run from oldest coordinate to newest; states start at n=1.
    state = tuple(x % modulus for x in initial)
    seen = {}
    values = [None]
    n = 1
    while state not in seen:
        seen[state] = n
        values.append(state[0])
        nxt = sum(c * x for c, x in zip(coeffs, state)) % modulus
        state = state[1:] + (nxt,)
        n += 1
    start, period = seen[state], n - seen[state]

    def at(index):
        if index >= n:
            index = start + (index - start) % period
        return values[index]

    return start, period, at


def exact_factor(initial, coeffs, s, local_data):
    result, evidence = 1, []
    for p, ramification, denominator_valuation in local_data:
        numerator = s + ramification - 2 + denominator_valuation
        cutoff = (numerator + s - 2) // (s - 1)
        exponent = 0
        for r in range(1, cutoff):
            modulus = p ** r
            start, period, at = state_cycle(initial, coeffs, modulus)
            witness = None
            level_exp = 0
            tested = 0
            for m in range(1, start + lcm(period, p)):
                if m % p == 0:
                    continue
                difference = (at((m*p**r)**s) - at((m*p**(r-1))**s)) % modulus
                deficit = r - vp(difference, p, r)
                tested += 1
                if deficit > level_exp:
                    level_exp, witness = deficit, m
            exponent = max(exponent, level_exp)
            evidence.append(dict(p=p, r=r, preperiod_endpoint=start,
                                 period=period, tested_m=tested,
                                 exponent=level_exp, witness_m=witness))
        result *= p ** exponent
    return result, evidence


def fib(n, modulus):
    a, b = 0, 1
    for bit in bin(n)[2:]:
        c = a * (2*b-a) % modulus
        d = (a*a+b*b) % modulus
        a, b = (d, (c+d) % modulus) if bit == '1' else (c, d)
    return a


def lucas(n, modulus):
    return (2*fib(n+1, modulus)-fib(n, modulus)) % modulus


cases = [
    ('Fibonacci squares', (1, 1), (1, 1), 2, [(5, 2, 1)], 5,
     lambda n, mod: fib(n, mod)),
    ('Fibonacci fourth powers', (1, 1), (1, 1), 4, [(5, 2, 1)], 5,
     lambda n, mod: fib(n, mod)),
    ('Lucas squares', (1, 3), (1, 1), 2, [(5, 2, 0)], 1,
     lambda n, mod: lucas(n, mod)),
    ('Rational weights denominator four', (1, 6), (-5, 6), 2,
     [(2, 1, 2)], 2, lambda n, mod: ((pow(5, n, 4*mod)-1)//4) % mod),
    ('Rational weights denominator eight', (1, 10), (-9, 10), 2,
     [(2, 1, 3)], 2, lambda n, mod: ((pow(9, n, 8*mod)-1)//8) % mod),
    ('Index one initialization', (2, 5), (-6, 5), 2,
     [(2, 1, 1), (3, 1, 1)], 6,
     lambda n, mod: (pow(2, n-1, mod)+pow(3, n-1, mod)) % mod),
    ('Periodic cubic residue selector', (1, 0, 0), (1, 0, 0), 2,
     [(3, 2, 1)], 3, lambda n, mod: int(n % 3 == 1)),
]

records = []
extended_instances = 0
for name, initial, coeffs, s, local, expected, direct in cases:
    factor, evidence = exact_factor(initial, coeffs, s, local)
    assert factor == expected, (name, factor, expected)
    for p in [2, 3, 5, 7, 11, 13]:
        for r in range(1, 7):
            modulus = p**r
            for m in range(1, 31):
                if m % p == 0:
                    continue
                diff = direct((m*p**r)**s, modulus) - direct((m*p**(r-1))**s, modulus)
                assert factor*diff % modulus == 0, (name, p, r, m)
                extended_instances += 1
    records.append(dict(name=name, factor=factor, local_evidence=evidence))

# Adversarial families: excluded odd Fibonacci sampling, repeated roots,
# and a finite transient at 8. These are explicit witnesses, not searches
# interpreted as universal nonexistence.
witnesses = []
for s in [1, 3, 5]:
    for p in [3, 7, 13, 17]:
        delta = (fib(p**s, p)-1) % p
        assert delta != 0
        witnesses.append(dict(family='Fibonacci odd', s=s, p=p, delta=delta))
for s in range(1, 7):
    for p in [3, 5, 7, 11]:
        delta = ((p**s)*pow(2, p**s, p)-2) % p
        assert delta != 0
for m in range(1, 101):
    assert (m*m) % 4 in (0, 1)
    assert ((m*m) * int((m*m) % 4 == 2)) == 0
for s in range(1, 13):
    hit = any(m**s == 8 for m in range(1, 9))
    assert hit == (s in (1, 3))

# Exact Fourier identity for the period-four repeated-root example.
# Four times q_n = 1 - i^n + (-1)^n - (-i)^n.
for b in range(4):
    z = (1+0j) - (1j)**b + (-1)**b - (-1j)**b
    assert z.imag == 0 and z.real == 4*int(b == 2)

# Check the elementary valuation lower-bound recurrence with exact fractions.
lifting_cases = 0
for p in [2, 3, 5, 7]:
    for e in range(1, 51):
        delta = Fraction(1, e)
        for t in range(0, 101):
            assert delta >= t-e+2
            delta = min(delta+1, p*delta)
            lifting_cases += 1

# Eventual power-map periodicity, without assuming units modulo M.
periodic_cases = 0
for modulus in range(1, 81):
    units = [a for a in range(modulus) if gcd(a, modulus) == 1]
    lam = 1
    if modulus > 1:
        for a in units:
            v, order = a % modulus, 1
            while v != 1:
                v = v*a % modulus
                order += 1
            lam = lcm(lam, order)
    # A=modulus is a coarse threshold larger than all prime exponents.
    for s in range(modulus, modulus+5):
        for a in range(modulus):
            assert pow(a, s, modulus) == pow(a, s+lam, modulus)
            periodic_cases += 1

folder = Path(__file__).resolve().parent
result = dict(status='pass', kind='finite consistency checks only',
              exact_factor_cases=records, extended_local_instances=extended_instances,
              excluded_family_witnesses=witnesses,
              lifting_inequality_instances=lifting_cases,
              eventual_power_map_instances=periodic_cases,
              manuscript_tex_sha256=hashlib.sha256((folder/'manuscript.tex').read_bytes()).hexdigest(),
              check_script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(folder/'check-results.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k: v for k, v in result.items() if k not in ['exact_factor_cases', 'excluded_family_witnesses']}, indent=2))
