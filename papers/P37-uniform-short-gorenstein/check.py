"""Exact finite-field checks for the proposed uniform-dominance theorem.

These tests check matrix identities and one finite module witness. They do not
replace Ringel's theorem, the general proof, or the historical-priority audit.
"""
import itertools
import json
import random
from pathlib import Path


def transpose(a):
    return [list(r) for r in zip(*a)]


def rref(a, p):
    a = [[x % p for x in row] for row in a]
    piv = []
    row = 0
    for col in range(len(a[0])):
        j = next((j for j in range(row, len(a)) if a[j][col]), None)
        if j is None:
            continue
        a[row], a[j] = a[j], a[row]
        z = pow(a[row][col], -1, p)
        a[row] = [(x*z) % p for x in a[row]]
        for j in range(len(a)):
            if j != row and a[j][col]:
                z = a[j][col]
                a[j] = [(x-z*y) % p for x, y in zip(a[j], a[row])]
        piv.append(col)
        row += 1
        if row == len(a):
            break
    return a, piv


def rank(a, p):
    return len(rref(a, p)[1])


def kernel(a, p):
    r, piv = rref(a, p)
    n = len(a[0])
    free = [j for j in range(n) if j not in piv]
    out = [[0]*len(free) for _ in range(n)]
    for j, f in enumerate(free):
        out[f][j] = 1
        for i, c in enumerate(piv):
            out[c][j] = -r[i][f] % p
    return out


def mul(a, b, p):
    return [[sum(x*y for x, y in zip(row, col)) % p
             for col in transpose(b)] for row in a]


def inverse(a, p):
    n = len(a)
    out, piv = rref([row+[int(i == j) for j in range(n)]
                     for i, row in enumerate(a)], p)
    assert piv[:n] == list(range(n))
    return [row[n:] for row in out]


def horizontal(blocks):
    return [sum((b[i] for b in blocks), []) for i in range(len(blocks[0]))]


def diagonal(blocks):
    height = sum(len(b) for b in blocks)
    width = sum(len(b[0]) for b in blocks)
    out = [[0]*width for _ in range(height)]
    r = c = 0
    for b in blocks:
        for i, row in enumerate(b):
            out[r+i][c:c+len(row)] = row
        r += len(b)
        c += len(b[0])
    return out


def twist(g, arrows, p):
    return [[[sum(g[i][j]*arrows[j][r][c] for j in range(len(g))) % p
              for c in range(len(arrows[0][0]))]
             for r in range(len(arrows[0]))] for i in range(len(g))]


def syzygy(q, arrows, p):
    a = len(arrows[0][0])
    k = kernel(horizontal(arrows), p)
    blocks = [k[i*a:(i+1)*a] for i in range(len(arrows))]
    return twist(q, blocks, p)


def cosyzygy(q, arrows, p):
    return [transpose(t) for t in syzygy(q, [transpose(t) for t in arrows], p)]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def coordinates(basis, values, p):
    rows = rref(transpose(basis), p)[1]
    square = [basis[i] for i in rows]
    result = mul(inverse(square, p), [values[i] for i in rows], p)
    assert mul(basis, result, p) == values
    return result


def check_reflection(q, arrows, p):
    e = len(q)
    a = len(arrows[0][0])
    k = kernel(horizontal(arrows), p)
    u = len(k[0])
    projections = [k[i*a:(i+1)*a] for i in range(e)]
    l0 = kernel(horizontal(projections), p)
    qit = transpose(inverse(q, p))
    change = [[qit[i//u][j//u]*int(i % u == j % u)
               for j in range(e*u)] for i in range(e*u)]
    lq = mul(change, l0, p)
    first_omega = twist(q, projections, p)
    assert not any(any(row) for row in mul(horizontal(first_omega), lq, p))
    assert rank(lq, p) == e*u-rank(horizontal(first_omega), p)
    second_omega = twist(q, [lq[i*u:(i+1)*u] for i in range(e)], p)
    second_sigma = [l0[i*u:(i+1)*u] for i in range(e)]
    assert second_omega == second_sigma


def one_cone_example():
    p, e = 2, 3
    q = identity(e)
    m = [[[1]], [[0]], [[0]]]
    x = syzygy(q, syzygy(q, m, p), p)
    y = cosyzygy(q, cosyzygy(q, m, p), p)
    ax, bx = len(x[0][0]), len(x[0])
    uy, vy = len(y[0][0]), len(y[0])
    chosen = []
    for v in itertools.product(range(p), repeat=ax):
        images = [mul(t, [[z] for z in v], p) for t in x]
        cols = horizontal(images)
        if rank(cols, p) != 1:
            continue
        w = next([r[0] for r in c] for c in images if any(r[0] for r in c))
        pivot = next(i for i, z in enumerate(w) if z)
        c = [im[pivot][0] for im in images]
        candidates = [list(t[0]) for t in chosen]+[list(v)]
        if rank(candidates, p) == len(candidates):
            chosen.append((v, w, c))
        if len(chosen) == ax:
            break
    assert len(chosen) == ax
    f0_blocks, f1_blocks = [], []
    for v, w, c in chosen:
        equations = []
        for i in range(e):
            for j in range(uy):
                row = [0]*(uy+vy)
                row[j] = -c[i] % p
                for r in range(vy):
                    row[uy+r] = y[i][r][j]
                equations.append(row)
        hom = kernel(equations, p)
        f = [row[0] for row in hom]
        assert any(f[:uy]) and any(f[uy:])
        f0_blocks.append([[z*t % p for t in f[:uy]] for z in v])
        f1_blocks.append([[z*t % p for t in f[uy:]] for z in w])
    f0, f1 = horizontal(f0_blocks), horizontal(f1_blocks)
    assert rank(f0, p) == ax and rank(f1, p) == bx
    source = [diagonal([t]*ax) for t in y]
    for i in range(e):
        assert mul(f1, source[i], p) == mul(x[i], f0, p)
    k0, k1 = kernel(f0, p), kernel(f1, p)
    karrows = [coordinates(k1, mul(t, k0, p), p) for t in source]
    radical_rank = rank(horizontal(karrows), p)
    simple_summands = len(k1[0])-radical_rank
    assert simple_summands >= 8
    return {'field': 2, 'pairing': q, 'M': [1, 1], 'X=Omega^2M': [ax, bx],
            'Y=Omega^-2M': [uy, vy], 'source_copies': ax,
            'kernel': [len(k0[0]), len(k1[0])],
            'kernel_radical_dimension': radical_rank,
            'displayed_simple_summands': simple_summands,
            'bristle_eigenvectors': [list(v) for v, _, _ in chosen],
            'epimorphism_top_matrix': f0, 'epimorphism_radical_matrix': f1}


def run():
    rng = random.Random(3742001)
    checks = 0
    alternating_checks = 0
    for p in (2, 3, 5, 7):
        for e in (3, 4, 5):
            for _ in range(24):
                while True:
                    q = [[0]*e for _ in range(e)]
                    for i in range(e):
                        for j in range(i, e):
                            q[i][j] = q[j][i] = rng.randrange(p)
                    if rank(q, p) == e:
                        break
                a = rng.randrange(1, 4)
                b = rng.randrange(1, 4)
                if b == e*a:
                    b -= 1
                while True:
                    arrows = [[[rng.randrange(p) for _ in range(a)]
                               for _ in range(b)] for _ in range(e)]
                    if (rank(horizontal(arrows), p) == b
                            and rank(sum(arrows, []), p) == a):
                        break
                check_reflection(q, arrows, p)
                checks += 1
            if p == 2 and e == 4:
                q = [[0, 1, 0, 0], [1, 0, 0, 0],
                     [0, 0, 0, 1], [0, 0, 1, 0]]
                for _ in range(24):
                    arrows = [[[rng.randrange(2) for _ in range(2)]
                               for _ in range(2)] for _ in range(e)]
                    check_reflection(q, arrows, p)
                    alternating_checks += 1
    return {'status': 'passed', 'reflection_identity_checks': checks,
            'additional_characteristic_two_alternating_checks': alternating_checks,
            'explicit_one_cone_witness': one_cone_example(),
            'scope': 'Finite matrix identities and a concrete one-cone module witness',
            'not_verified_by_this_script': ['Ringel theorem', 'general proof',
                                            'historical novelty', 'significance']}


if __name__ == '__main__':
    result = run()
    out = Path(__file__).with_name('check-results.json')
    out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items()
                      if k != 'explicit_one_cone_witness'}, indent=2))
    print(json.dumps({k: v for k, v in result['explicit_one_cone_witness'].items()
                      if 'matrix' not in k}, indent=2))
