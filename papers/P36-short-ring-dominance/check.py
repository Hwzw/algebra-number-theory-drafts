#!/usr/bin/env python3
"""Exact finite quotient diagnostics; the universal theorem is proved by hand.
Uses only the Python standard library. Run: python3 check.py [output.json]
"""
from itertools import product
from pathlib import Path
import json, random, sys

def rank_mod(rows, p):
    a = [list(r) for r in rows]
    r = 0
    for c in range(len(a[0]) if a else 0):
        pivot = next((i for i in range(r, len(a)) if a[i][c] % p), None)
        if pivot is None: continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c] % p, -1, p)
        a[r] = [(v * inv) % p for v in a[r]]
        for i in range(len(a)):
            if i != r:
                q = a[i][c]
                a[i] = [(x - q*y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a): break
    return r

def inspect(p, e, f, coefficients, mode):
    n = 1 + e + f
    basis = [tuple(int(i == j) for i in range(n)) for j in range(n)]
    zero = (0,) * n
    tensor = [[[0]*f for _ in range(e)] for _ in range(e)]
    pairs = [(i,j) for i in range(e) for j in range(i,e)]
    for c,(i,j) in enumerate(pairs):
        tensor[i][j] = tensor[j][i] = [coefficients[t][c] for t in range(f)]
    def mul(v,w):
        out = [v[0]*w[0]] + [v[0]*w[i] + w[0]*v[i] for i in range(1,n)]
        for i in range(e):
            for j in range(e):
                for t in range(f): out[1+e+t] += v[1+i]*w[1+j]*tensor[i][j][t]
        return tuple(out)
    for u,v,w in product(basis, repeat=3):
        assert mul(mul(u,v),w) == mul(u,mul(v,w))
    a = basis[1 if mode == 'p_in_degree_one' else 1+e]
    columns = [tuple(p*x-y for x,y in zip(b,mul(a,b))) for b in basis]
    assert all(columns[j][i] == 0 for j in range(n) for i in range(j))
    assert all(columns[j][j] == p for j in range(n))
    def normal(v):
        v = list(v)
        for j in range(n):
            q = v[j] // p
            for i in range(j,n): v[i] -= q*columns[j][i]
        assert all(0 <= x < p for x in v)
        return tuple(v)
    def times(v,w): return normal(mul(v,w))
    for col,b in product(columns,basis): assert normal(mul(col,b)) == zero
    assert normal(tuple(p*x for x in basis[0])) == normal(a)
    reps = list(product(range(p),repeat=n))
    generators = [normal(v) for v in basis[1:]]
    def subgroup(gens):
        seen = {zero}; queue = [zero]
        for v in queue:
            for g in gens:
                w = normal(tuple(x+y for x,y in zip(v,g)))
                if w not in seen: seen.add(w); queue.append(w)
        return seen
    maximal = subgroup(generators)
    products2 = [times(u,v) for u,v in product(generators,repeat=2)]
    square = subgroup(products2)
    assert len(maximal) == p**(e+f)
    assert len(square) == p**f
    assert all(times(v,g) == zero for v,g in product(square,generators))
    assert (normal(a) in square) == (mode == 'p_in_degree_two')
    socle = [v for v in reps if all(times(v,g) == zero for g in generators)]
    degree_one_radical = sum(all(sum(v[i]*tensor[i][j][t] for i in range(e)) % p == 0
                                  for j in range(e) for t in range(f))
                             for v in product(range(p),repeat=e))
    assert len(socle) == p**f * degree_one_radical
    for i,j in pairs:
        rhs = [0]*n
        for t in range(f): rhs[1+e+t] = tensor[i][j][t]
        assert times(generators[i],generators[j]) == normal(rhs)
    char = p
    while normal(tuple(char*x for x in basis[0])) != zero: char *= p
    assert char in (p*p,p*p*p)
    return {'p':p,'e':e,'f':f,'mode':mode,'order':len(reps),'characteristic':char,
            'socle_order':len(socle),'gorenstein':len(socle)==p,
            'basis_associativity_checks':n**3}

def main():
    rows=[]
    # All nonzero scalar quadratic tensors in embedding dimension three over F2.
    for coeff in product(range(2),repeat=6):
        if not any(coeff): continue
        for mode in ['p_in_degree_one','p_in_degree_two']:
            rows.append(inspect(2,3,1,[coeff],mode))
    # All surjective Sym^2(F2^2) -> F2^2 tensors, including non-Gorenstein rings.
    for flat in product(range(2),repeat=6):
        coeff=[flat[:3],flat[3:]]
        if rank_mod(coeff,2) != 2: continue
        for mode in ['p_in_degree_one','p_in_degree_two']:
            rows.append(inspect(2,2,2,coeff,mode))
    rng=random.Random(41036)
    for _ in range(20):
        coeff=[rng.randrange(3) for _ in range(6)]
        if not any(coeff): coeff[0]=1
        for mode in ['p_in_degree_one','p_in_degree_two']:
            rows.append(inspect(3,3,1,[coeff],mode))
    for p in [2,3]:
        for e in range(1,5): rows.append(inspect(p,e,0,[],'p_in_degree_one'))
    result={'status':'passed','scope':'Exact finite diagnostics, not a substitute for the universal proof',
            'quotient_cases':len(rows),'elements_enumerated':sum(r['order'] for r in rows),
            'basis_associativity_checks':sum(r['basis_associativity_checks'] for r in rows),
            'gorenstein_cases':sum(r['gorenstein'] for r in rows),
            'non_gorenstein_cases':sum(not r['gorenstein'] for r in rows),
            'characteristics':sorted(set(r['characteristic'] for r in rows)),
            'cases':rows}
    out=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('check-results.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))
if __name__=='__main__': main()
