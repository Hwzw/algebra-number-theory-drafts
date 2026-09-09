"""Exhaust all bilinear ring multiplications on F_2^2, including nonunital.

The power-map search is exact: iterate until a whole power function repeats.
This is only a sanity check of the infinite hand proof.
"""
from itertools import product
from pathlib import Path
import json

stats=dict(bilinear_tables=0,associative_tables=0,nilperiod_tables=0,
           nilperiod_nonunital_tables=0,nilperiod_noncommutative_tables=0,
           nilpotent_principal_ideals_checked=0)
for constants in product(range(4),repeat=4):
    stats['bilinear_tables']+=1
    def mul(a,b):
        out=0
        for i in range(2):
            for j in range(2):
                if a>>i&1 and b>>j&1:out^=constants[2*i+j]
        return out
    M=[[mul(a,b) for b in range(4)] for a in range(4)]
    if not all(M[M[a][b]][c]==M[a][M[b][c]] for a,b,c in product(range(4),repeat=3)):continue
    stats['associative_tables']+=1
    seen=set()
    f=tuple(range(4))
    periods={0}
    nil={0}
    while f not in seen:
        seen.add(f)
        nil.update(a for a in range(4) if f[a]==0)
        periods.update(a for a in range(4) if all(f[x^a]==f[x] for x in range(4)))
        f=tuple(M[f[x]][x] for x in range(4))
    if not nil<=periods:continue
    stats['nilperiod_tables']+=1
    unital=any(all(M[e][x]==M[x][e]==x for x in range(4)) for e in range(4))
    commutative=all(M[x][y]==M[y][x] for x,y in product(range(4),repeat=2))
    stats['nilperiod_nonunital_tables']+=not unital
    stats['nilperiod_noncommutative_tables']+=not commutative
    assert all(a^b in nil for a,b in product(nil,repeat=2))
    for a in nil:
        ideal={0,a}
        while True:
            bigger=ideal|{x^y for x,y in product(ideal,repeat=2)}|{M[x][y] for x in ideal for y in range(4)}|{M[y][x] for x in ideal for y in range(4)}
            if bigger==ideal:break
            ideal=bigger
        assert ideal<=nil,(constants,a,ideal,nil)
        stats['nilpotent_principal_ideals_checked']+=1
stats['status']='PASS'
Path(__file__).with_name('C20-verification.json').write_text(json.dumps(stats,indent=2)+'\n')
print(json.dumps(stats))
