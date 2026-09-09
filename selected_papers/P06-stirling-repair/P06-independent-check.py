"""Independent finite diagnostic for P06's digit congruence, not a proof.

Use inclusion-exclusion modulo p*k! before exact division by k!, so the
calculation remains valid even when p divides k!. No manuscript code imported.
"""
import hashlib
import json
from math import comb, factorial
from pathlib import Path


def stirling_mod(n, k, p):
    fac = factorial(k)
    modulus = p * fac
    residue = sum((-1) ** (k - j) * comb(k, j) * pow(j, n, modulus)
                  for j in range(1, k + 1)) % modulus
    assert residue % fac == 0
    return residue // fac


def predicted(k, p, r):
    remaining, answer = (k - 1) // p, 1
    for _ in range(r):
        answer = answer * (remaining % p + 1) % p
        remaining //= p
    return answer


def main():
    primes = [2, 3, 5, 7, 11]
    count = 0
    digest = hashlib.sha256()
    for k in range(1, 101):
        for p in primes:
            for r in range(7):
                actual = stirling_mod(p ** r + k - 1, k, p)
                expected = predicted(k, p, r)
                assert actual == expected, (k, p, r, actual, expected)
                digest.update(f'{k},{p},{r},{actual}\n'.encode())
                count += 1
    result = {
        'status': 'PASS',
        'meaning': 'Finite diagnostic only; the audit reconstructs the proof separately.',
        'method': 'Inclusion-exclusion modulo p*k!, followed by exact division by k!',
        'k_range': [1, 100], 'primes': primes, 'r_range': [0, 6],
        'checks': count, 'rows_sha256': digest.hexdigest()
    }
    destination = Path(__file__).with_name('P06-independent-check-results.json')
    destination.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
