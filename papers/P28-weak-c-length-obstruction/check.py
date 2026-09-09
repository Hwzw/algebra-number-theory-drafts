"""Independent finite checks; the universal counterexample has a written proof.

Python standard library only. Run: python3 check.py
"""
from bisect import bisect_left, bisect_right
from functools import lru_cache
from itertools import product
from pathlib import Path
import json


def member(z):
    n, u, v, w = z
    return min(z) >= 0 and (n >= 2 or (n == 0 and u == 2*v+5*w))


def predicted_atom(z):
    n, u, v, w = z
    return z in [(0, 2, 1, 0), (0, 5, 0, 1)] or (
        n in (2, 3) and (u < 2 or v == 0) and (u < 5 or w == 0))


def independent_atom(z):
    if not member(z) or not any(z):
        return False
    for p in product(*(range(t+1) for t in z)):
        if any(p) and p != z and member(p) and member(tuple(x-y for x, y in zip(z, p))):
            return False
    return True


def first_layer(u, v, w):
    g0 = min(w, max(0, (u-2*v)//5))
    g1 = min(w, u//5)
    assert g0 <= g1
    return {1+j+min(v, (u-5*j)//2) for j in range(g0, g1+1)}


def all_lengths_formula(z):
    n, u, v, w = z
    if not member(z):
        return set()
    if n == 0:
        return {v+w}
    first = first_layer(u, v, w)
    if n <= 3:
        return first
    return set(range((n+2)//3, n//2+max(first)))


def packing_brute(u, v, w):
    answer = set()
    for j in range(min(w, u//5)+1):
        for i in range(min(v, (u-5*j)//2)+1):
            r = u-2*i-5*j
            if (r < 2 or i == v) and (r < 5 or j == w):
                answer.add(1+i+j)
    return answer


def aamp_bound(lengths, d):
    """Exact best bound: a core must lie between consecutive forbidden holes."""
    ls = sorted(lengths)
    a, b = ls[0], ls[-1]
    residues = {x % d for x in ls}
    holes = [a-1] + [x for x in range(a, b+1) if x not in lengths and x % d in residues] + [b+1]
    answer = b-a
    for left, right in zip(holes, holes[1:]):
        i, j = bisect_right(ls, left), bisect_left(ls, right)-1
        if i <= j:
            answer = min(answer, max(ls[i]-a, b-ls[j]))
    return answer


def main():
    points = sorted(product(range(7), range(9), range(5), range(5)), key=sum)
    atoms = []
    for z in points:
        actual = independent_atom(z)
        assert actual == predicted_atom(z), z
        if actual:
            atoms.append(z)

    @lru_cache(None)
    def recursive(z):
        if not any(z):
            return frozenset({0})
        out = set()
        for atom in atoms:
            remainder = tuple(x-y for x, y in zip(z, atom))
            if member(remainder):
                out.update(1+l for l in recursive(remainder))
        return frozenset(out)

    tested = 0
    for z in points:
        if member(z):
            assert recursive(z) == all_lengths_formula(z), z
            tested += 1

    packing_tests = 0
    for u, v, w in product(range(41), range(15), range(10)):
        assert first_layer(u, v, w) == packing_brute(u, v, w), (u, v, w)
        packing_tests += 1

    rays = []
    for n in range(1, 101):
        predicted = {2*n+2+3*j+r for j in range(n) for r in (0, 1)} | {5*n+1}
        assert packing_brute(10*n+2, 5*n, 2*n) == predicted, n
        if n in (1, 2, 3, 10, 100):
            rays.append({"N": n, "minimum": min(predicted), "maximum": max(predicted), "cardinality": len(predicted)})

    obstruction_tests = 0
    for n, d in product(range(1, 41), range(1, 41)):
        t = {3*j+r for j in range(n) for r in (0, 1)} | {3*n-1}
        bound = aamp_bound(t, d)
        assert 2*bound >= 3*n-d-3, (n, d, bound)
        obstruction_tests += 1

    result = {
        "status": "pass",
        "independent_atom_points": len(points),
        "independent_atoms_in_box": len(atoms),
        "full_factorization_length_sets": tested,
        "maximal_packing_formula_cases": packing_tests,
        "explicit_ray_cases": 100,
        "aamp_obstruction_cases": obstruction_tests,
        "sample_ray_summaries": rays,
        "scope": "finite checks supplement, and do not replace, the hand proofs of Mori, weak C, and unbounded obstruction",
    }
    Path(__file__).with_name("check-results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
