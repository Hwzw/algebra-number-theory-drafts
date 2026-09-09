"""Finite consistency checks; the infinite claims require the written proofs."""
from itertools import product
from math import isqrt
from fractions import Fraction
from pathlib import Path
import hashlib
import json


class Field:
    def __init__(self, p, modulus):
        self.p = p
        self.modulus = modulus
        self.d = len(modulus) - 1
        self.q = p ** self.d
        self.digits = [self.decode(a) for a in range(self.q)]
        assert modulus[-1] == 1
        assert all(self.power(a, self.q - 1) == 1 for a in range(1, self.q))
        self.squares = {self.mul(a, a) for a in range(1, self.q)}
        assert len(self.squares) == (self.q - 1 if p == 2 else (self.q - 1) // 2)

    def decode(self, a):
        out = []
        for _ in range(self.d):
            out.append(a % self.p)
            a //= self.p
        return out

    def encode(self, a):
        return sum((x % self.p) * self.p ** j for j, x in enumerate(a))

    def sub(self, a, b):
        return self.encode([x - y for x, y in zip(self.digits[a], self.digits[b])])

    def mul(self, a, b):
        v = [0] * (2 * self.d - 1)
        for i, x in enumerate(self.digits[a]):
            for j, y in enumerate(self.digits[b]):
                v[i + j] += x * y
        for i in range(len(v) - 1, self.d - 1, -1):
            c = v[i] % self.p
            for j in range(self.d):
                v[i - self.d + j] -= c * self.modulus[j]
        return self.encode(v[:self.d])

    def power(self, a, n):
        out = 1
        while n:
            if n & 1:
                out = self.mul(out, a)
            a = self.mul(a, a)
            n //= 2
        return out


def gaussian_mul(z, w):
    a, b = z
    c, d = w
    return a * c - b * d, a * d + b * c


def gaussian_power(z, k):
    r = (1, 0)
    for _ in range(k):
        r = gaussian_mul(r, z)
    return r


def split_prime(p):
    for b in range(2, isqrt(p) + 1, 2):
        a = isqrt(p - b * b)
        if a * a + b * b == p:
            return a, b
    raise AssertionError(p)


def predicted(p, k):
    q = p ** k
    if p == 2:
        return (q - 1) ** 4 * (q - 2) * (q - 3)
    if q % 4 == 3:
        out = Fraction((q - 1) ** 4 * (q - 3) * (q - 7), 512)
    elif p % 4 == 3:
        out = Fraction((q - 1) ** 4 * (q - 9) ** 2, 512)
    else:
        a, b = gaussian_power(split_prime(p), k)
        assert a * a + b * b == q and a % p != 0 and b % 2 == 0
        out = Fraction((q - 1) ** 4 * ((q - 9) ** 2 - 4 * b * b), 512)
    assert out.denominator == 1
    return int(out)


def check_field(p, mod):
    f = Field(p, mod)
    s = f.squares
    common = [x for x in s if f.sub(x, 1) in s]
    normalized = sum(f.sub(y, x) in s for x in common for y in common)
    count = normalized * len(s) ** 4
    assert count == predicted(p, f.d), (p, mod, count, predicted(p, f.d))
    row = {'p': p, 'degree': f.d, 'modulus': mod, 'q': f.q,
           'elementary_matrices': normalized, 'total_count': count}
    if f.q <= 49:
        tuples = sum(f.sub(b, a) in s and f.sub(c, a) in s and f.sub(c, b) in s
                     for a, b, c in product(s, repeat=3))
        assert tuples * len(s) ** 3 == count
        row['independent_column_normalization_count'] = tuples
    if f.q <= 13:
        mul = [[f.mul(a, b) for b in range(f.q)] for a in range(f.q)]
        direct = sum(f.sub(mul[a][e], mul[b][d]) in s
                     and f.sub(mul[a][h], mul[c][d]) in s
                     and f.sub(mul[b][h], mul[c][e]) in s
                     for a, b, c, d, e, h in product(s, repeat=6))
        assert direct == count
        row['direct_original_matrix_count'] = direct
        row['original_matrices_examined'] = len(s) ** 6
    return row


def polymul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def recurrence_check(p):
    a, b = split_prime(p)
    tr = 2 * (a * a - b * b)
    poly = [1]
    for d in range(7):
        poly = polymul(poly, [-p ** d, 1])
    for j in range(5):
        poly = polymul(poly, [p ** (2 * j + 2), -tr * p ** j, 1])
    vals = [predicted(p, k) for k in range(1, 41)]
    for k in range(len(vals) - 17):
        assert sum(c * vals[k + j] for j, c in enumerate(poly)) == 0
    u = [2, tr]
    for k in range(2, 41):
        u.append(tr * u[-1] - p * p * u[-2])
        z = gaussian_power((a, b), 2 * k)
        assert u[-1] == 2 * z[0]
    return {'p': p, 'minimality_is_proved_in_notes_not_by_this_check': True,
            'recurrence_order': 17, 'recurrence_checks': len(vals) - 17,
            'trace_recurrence_checks': 39, 'characteristic_polynomial_ascending': poly}


def main():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 53, 61, 73, 89, 97]
    cases = [(p, [0, 1]) for p in primes]
    cases += [(2, [1, 1, 1]), (2, [1, 1, 0, 1]), (2, [1, 1, 0, 0, 1]),
              (3, [1, 0, 1]), (3, [1, 2, 0, 1]), (5, [2, 0, 1]),
              (5, [1, 1, 0, 1]), (5, [2, 0, 0, 0, 1]), (7, [1, 0, 1]),
              (13, [2, 0, 1]), (17, [3, 0, 1])]
    fields = [check_field(p, m) for p, m in cases]
    results = {'status': 'all checks passed', 'finite_checks_only': True,
               'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               'fields': fields, 'recurrences': [recurrence_check(p) for p in (5, 13, 17, 29)],
               'p5_initial_counts': [predicted(5, k) for k in range(1, 7)]}
    dest = Path(__file__).with_name('check-results.json')
    dest.write_text(json.dumps(results, indent=2) + '\n')
    print(json.dumps({'fields_checked': len(fields),
                      'direct_matrix_fields': sum('direct_original_matrix_count' in r for r in fields),
                      'status': results['status']}))


if __name__ == '__main__':
    main()
