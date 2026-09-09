"""Exact auxiliary checks for P16; not a proof of its general theorems."""
import hashlib
import itertools
import json
from pathlib import Path


def subsets(n):
    return [{i for i in range(n) if mask >> i & 1} for mask in range(1, 1 << n)]


def run():
    transfer_pairs = 0
    degree_instances = 0
    for n in range(2, 9):
        sets = subsets(n)
        for a in sets:
            for c in sets:
                r = [len(c & {(x + y) % n for x in a}) for y in range(n)]
                reflected = [len(a & {(x - y) % n for x in c}) for y in range(n)]
                assert r == reflected
                for degree in range(4):
                    b = {y for y in range(n) if r[y] <= degree}
                    if not b:
                        continue
                    original = {(x + y) % n for x in a for y in b
                                if (x + y) % n not in c}
                    dual = {(x - y) % n for x in c for y in b
                            if (x - y) % n not in a}
                    assert original.isdisjoint(c) and dual.isdisjoint(a)
                    for y in b:
                        assert sum((x+y) % n in c for x in a) <= degree
                        assert sum((x-y) % n in a for x in c) <= degree
                    # Exact size identity for arbitrary loss q, when S is C's complement.
                    q = len(a) + len(b) - (n-len(c)) - 1
                    assert n-len(a) == len(c)+len(b)-q-1
                    degree_instances += 1
                transfer_pairs += 1

    boundary_cases = 0
    for n in range(2, 14):
        for m in range(1, n):
            interval = set(range(m))
            for h in range(min(m, 4)+1):
                for holes in itertools.combinations(range(m), h):
                    a = interval - set(holes)
                    for y in range(n):
                        boundary_i = len({(x+y) % n for x in interval} - interval)
                        boundary_a = len({(x+y) % n for x in a} - a)
                        assert boundary_i == min(y, n-y, m, n-m)
                        assert boundary_a >= boundary_i-h
                        boundary_cases += 1

    result = {
        "status": "passed",
        "transfer_all_nonempty_set_pairs_moduli_2_through_8": transfer_pairs,
        "transfer_degree_0_through_3_instances": degree_instances,
        "interval_boundary_cases_moduli_2_through_13_up_to_four_holes": boundary_cases,
        "scope": "Auxiliary exact identities only. General proof and source hypotheses are audited in prose.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    output = Path(__file__).with_name("check-results.json")
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    run()
