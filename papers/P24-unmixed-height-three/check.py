"""Exact checks supporting, but not replacing, the hand proof in the manuscript."""
from itertools import combinations, product
from fractions import Fraction as F
from pathlib import Path
import json

HERE = Path(__file__).parent


def solve(rows, rhs):
    n = len(rhs)
    a = [list(row) + [value] for row, value in zip(rows, rhs)]
    for j in range(n):
        pivot = next((k for k in range(j, n) if a[k][j]), None)
        if pivot is None:
            return None
        a[j], a[pivot] = a[pivot], a[j]
        scale = a[j][j]
        a[j] = [entry / scale for entry in a[j]]
        for k in range(n):
            if k != j and a[k][j]:
                scale = a[k][j]
                a[k] = [u - scale * v for u, v in zip(a[k], a[j])]
    return tuple(a[k][-1] for k in range(n))


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def connected(family, vertex, start, end):
    reached = {start}
    while True:
        new = reached | {b for a in reached for b in family
                         if vertex in b and len(a & b) == 2}
        if new == reached:
            return end in new
        reached = new


def supports():
    V = frozenset(range(5))
    triples = [frozenset(c) for c in combinations(V, 3)]
    fours = [frozenset(c) for c in combinations(V, 4)]
    result = {'families_checked': 1023, 'dimension_one_compatible_families': 0,
              'marked_disagreement_pairs': 0,
              'types': {'zero': 0, 'one': 0, 'two_same': 0, 'two_cross': 0}}
    for mask in range(1, 1 << len(triples)):
        fam = [triples[j] for j in range(len(triples)) if mask >> j & 1]
        if any(sum(p <= S for p in fam) > 2 for S in fours):
            continue
        result['dimension_one_compatible_families'] += 1
        for P, R in combinations(fam, 2):
            if len(P & R) != 1:
                continue
            x, = P & R
            if connected(fam, x, P, R):
                continue
            result['marked_disagreement_pairs'] += 1
            assert P | R == V
            extra = [q for q in fam if q not in (P, R)]
            assert all(x not in q for q in extra)
            assert len(extra) <= 2
            if not extra:
                result['types']['zero'] += 1
            elif len(extra) == 1:
                result['types']['one'] += 1
                # The extra meets one pair in one vertex, the other in two.
                A, B = P - {x}, R - {x}
                if len(extra[0] & A) == 2:
                    A, B = B, A
                b, = extra[0] & A
                c = min(B)
                keep = frozenset((x, b, c))
                images = {q & keep for q in fam}
                assert images == {frozenset(t) for t in combinations(keep, 2)}
            else:
                missing = [next(iter((V - {x}) - q)) for q in extra]
                A, B = P - {x}, R - {x}
                same = (set(missing) <= A or set(missing) <= B)
                if same:
                    result['types']['two_same'] += 1
                    if set(missing) <= B:
                        P, R, A, B = R, P, B, A
                    assert all(B <= q for q in [R] + extra)
                    assert all(len(q & r) == 2 for q, r in combinations([R] + extra, 2))
                else:
                    result['types']['two_cross'] += 1
                    remaining = V - {x} - set(missing)
                    keep = remaining | {x}
                    images = [q & keep for q in fam]
                    assert set(images) == {frozenset(t) for t in combinations(keep, 2)}
                    assert extra[0] & keep == extra[1] & keep == remaining
                    # Direct two-variable overlap forces each duplicate exponent equal.
                    assert extra[0] & extra[1] == remaining
    return result


def vertices():
    counts = {'parameter_choices': 0, 'r_gt_one': 0, 'r_eq_one': 0, 'r_lt_one': 0}
    for a, b, c, alpha, beta, gamma in product(range(1, 4), repeat=6):
        for d, e in product((1, 3), repeat=2):
            r = F(alpha, a) + F(beta, b) + F(gamma, c)
            rows = [(F(1,a),F(1,b),F(1,c),F(0),F(0)),
                    (F(1,alpha),F(0),F(0),F(1,d),F(1,e)),
                    (F(0),F(1,beta),F(0),F(1,d),F(1,e)),
                    (F(0),F(0),F(1,gamma),F(1,d),F(1,e))]
            units = [tuple(F(i == j) for i in range(5)) for j in range(5)]
            if r > 1:
                v = (F(alpha)/r,F(beta)/r,F(gamma)/r,F(d)*(1-1/r),F(0))
                basis = rows + [units[4]]
                rhs = [F(1)]*4 + [F(0)]
                counts['r_gt_one'] += 1
            else:
                v = (F(a)*(1-F(beta,b)-F(gamma,c)),F(beta),F(gamma),F(0),F(0))
                basis = [rows[0],rows[2],rows[3],units[3],units[4]]
                rhs = [F(1)]*3 + [F(0)]*2
                counts['r_eq_one' if r == 1 else 'r_lt_one'] += 1
            assert all(t >= 0 for t in v)
            assert all(dot(row,v) >= 1 for row in rows)
            assert all(F(0) < v[i] < bound for i,bound in enumerate((a,b,c)))
            assert solve(basis,rhs) == v
            counts['parameter_choices'] += 1
    # Ensure the branch r<1, absent from some small parameter boxes, is tested.
    assert counts['r_gt_one'] and counts['r_eq_one']
    for a,b,c in product((4,5,7), repeat=3):
        alpha=beta=gamma=1; d=2; e=3
        r=F(1,a)+F(1,b)+F(1,c)
        assert r<1
        v=(F(a)*(1-F(1,b)-F(1,c)),F(1),F(1),F(0),F(0))
        assert v[0]>=1 and 0<v[0]<a and v[1]<b and v[2]<c
        assert v[0]/a+v[1]/b+v[2]/c==1
        rows = [(F(1,a),F(1,b),F(1,c),F(0),F(0)),
                (F(1),F(0),F(0),F(1,d),F(1,e)),
                (F(0),F(1),F(0),F(1,d),F(1,e)),
                (F(0),F(0),F(1),F(1,d),F(1,e))]
        units = [tuple(F(i == j) for i in range(5)) for j in range(5)]
        assert all(dot(row,v) >= 1 for row in rows)
        assert solve([rows[0],rows[2],rows[3],units[3],units[4]],
                     [F(1)]*3+[F(0)]*2) == v
        counts['r_lt_one']+=1; counts['parameter_choices']+=1
    return counts


def pair_witnesses():
    count = 0
    for A,B,C in product(range(1,13), repeat=3):
        if not A<B:
            continue
        t=max(2*A,B)
        assert t//A>=2 and t//B+1>=2
        assert t<2*B and t<A+B and C<2*C
        count+=1
    return count


def main():
    result={'status':'Exact supplementary audit; hand proof is the theorem argument',
            'support_audit':supports(),'vertex_audit':vertices(),
            'two_component_witnesses':pair_witnesses()}
    (HERE/'check-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
