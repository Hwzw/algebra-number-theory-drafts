"""Matching/LP check independent from the saturation parametrization in the proof.

Enumerates all LP vertices for fractional optimum and uses exact dynamic programming for ordinary
matching. Float LP outputs are checked to lie within 1e-7 of a halfinteger.
The graph-pair enumeration covers all demand totals <= 14 for two 5-cycles.
"""
from functools import lru_cache
from itertools import product, combinations
from collections import Counter
from math import comb
from pathlib import Path
import json
import numpy as np

@lru_cache(None)
def match(b):
    return max([0]+[1+match(tuple(v-(i==j or i==(j+1)%5) for i,v in enumerate(b)))
                     for j in range(5) if b[j] and b[(j+1)%5]])

inc=np.array([[int(i==j or i==(j+1)%5) for j in range(5)] for i in range(5)])
rows=np.vstack([inc,-np.eye(5)])
bases=[]
selectors=[]
for inds in combinations(range(10),5):
    mat=rows[list(inds)]
    if abs(np.linalg.det(mat))<0.1: continue
    bases.append(np.linalg.inv(mat))
    selectors.append(inds)
bases=np.array(bases)
selectors=np.array(selectors)
hist=Counter()
lpchecks=0
for b in product(range(15),repeat=5):
    T=sum(b)
    if T>14: continue
    bounds=np.array(b+(0,)*5)
    vertices=np.einsum('kij,kj->ki',bases,bounds[selectors])
    feasible=(vertices@rows.T<=bounds+1e-8).all(axis=1)
    optimum=vertices[feasible].sum(axis=1).max()
    twice=round(2*optimum)
    assert abs(twice-2*optimum)<1e-7
    exact=match(b)
    assert exact==twice//2
    hist[(T,twice,exact)]+=1
    lpchecks+=1

holes=Counter()
for (t1,f1,a1),n1 in hist.items():
    for (t2,f2,a2),n2 in hist.items():
        T=t1+t2
        if T>14: continue
        for m in range(1,8):
            if 2*T-f1-f2<=2*m and T-a1-a2>m:
                holes[m]+=n1*n2

for m in range(1,8):
    expected=comb(m+4,9) if m>=5 else 0
    assert holes[m]==expected,(m,holes[m],expected)
report=dict(status='PASS',cycle_lp_and_exact_dp_checks=lpchecks,
            correction_counts={str(m):holes[m] for m in range(1,8)},
            method='Independent exhaustive LP-vertex enumeration and exact integer matching dynamic programming; complete two-cycle demands total <=14 relevant to m<=7')
Path(__file__).with_name('correction-verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
