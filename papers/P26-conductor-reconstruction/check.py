#!/usr/bin/env python3
"""Exact finite examples; the paper's general proofs are independent of this file."""
import itertools
import json
import math
from pathlib import Path


def vectors(rank, degree):
    if rank == 1:
        yield (degree,)
    else:
        for first in range(degree + 1):
            for tail in vectors(rank - 1, degree - first):
                yield (first,) + tail


def leq(a, b):
    return all(x <= y for x, y in zip(a, b))


def run():
    vector_checks = 0
    permutation_checks = 0
    examples = []
    # These cyclic data have at least two primes in each occupied nonzero class.
    cases = [(d, (1,) * r) for r in (2, 3, 4) for d in range(2, 6)]
    cases += [(2, (0, 1, 1)), (3, (1, 1, 2, 2)), (4, (1, 1, 3, 3))]
    for modulus, weights in cases:
        rank = len(weights)
        zero = (0,) * rank
        # Minimal zero-sum vectors have total degree <= |G| (partial sums).
        atoms = []
        for degree in range(1, modulus + 1):
            for a in vectors(rank, degree):
                if sum(x*w for x, w in zip(a, weights)) % modulus == 0:
                    if not any(leq(b, a) for b in atoms):
                        atoms.append(a)
        for p in range(rank):
            divisible = [a for a in atoms if a[p]]
            assert divisible
            gcd_vector = tuple(min(a[j] for a in divisible) for j in range(rank))
            assert gcd_vector == tuple(int(j == p) for j in range(rank))
        generated = {zero}
        for degree in range(1, 2 * modulus + 3):
            for a in vectors(rank, degree):
                if any(leq(b, a) and tuple(x-y for x, y in zip(a, b)) in generated
                       for b in atoms):
                    generated.add(a)
                expected = sum(x*w for x, w in zip(a, weights)) % modulus == 0
                assert (a in generated) == expected
                vector_checks += 1
        actual = 0
        atom_set = set(atoms)
        for perm in itertools.permutations(range(rank)):
            permuted = {tuple(a[perm[j]] for j in range(rank)) for a in atoms}
            preserves = permuted == atom_set
            predicted = any(
                all(weights[perm[j]] % modulus == unit * weights[j] % modulus
                    for j in range(rank))
                for unit in range(1, modulus) if math.gcd(unit, modulus) == 1
            )
            assert preserves == predicted
            actual += int(preserves)
            permutation_checks += 1
        gamma_order = sum(
            sorted((unit * w) % modulus for w in weights) == sorted(weights)
            for unit in range(1, modulus) if math.gcd(unit, modulus) == 1
        )
        kernel_order = math.prod(math.factorial(weights.count(g)) for g in set(weights))
        assert actual == gamma_order * kernel_order
        examples.append(dict(modulus=modulus, weights=weights, atoms=len(atoms),
                             automorphisms=actual, gamma=gamma_order, kernel=kernel_order))
    rank_one = []
    for d in range(2, 10):
        # Relative saturation holds, but the ambient prime gcd is d, not 1.
        assert min(d*n for n in range(1, 10)) == d != 1
        rank_one.append(d)
    return dict(status='pass', vector_checks=vector_checks,
                permutation_checks=permutation_checks, cyclic_examples=examples,
                rank_one_exclusions=rank_one,
                scope='Exact finite consistency checks; universal proofs are in the manuscript.')


if __name__ == '__main__':
    result = run()
    Path(__file__).with_name('check-results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ('cyclic_examples',)}, indent=2))
