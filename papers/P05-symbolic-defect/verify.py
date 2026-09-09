"""Independent bounded checks; no computation is used as the infinite proof."""
from itertools import product, combinations
from math import comb
import json
from pathlib import Path

def independent(n, edges):
    return [v for v in product(range(2), repeat=n) if all(v[i]+v[j]<=1 for i,j in edges)]

def ordinary(n, edges, m):
    gens=independent(n,edges)
    out={(0,)*n}
    for _ in range(m):
        out={tuple(a+b for a,b in zip(u,v)) for u in out for v in gens}
    return out

def full_symbolic_min(n,edges,m):
    graph=edges+[(i,n+i) for i in range(n)]
    out=set()
    for v in product(range(m+1),repeat=2*n):
        if not all(v[i]+v[j]>=m for i,j in graph): continue
        if any(v[k]>0 and all(v[i]+v[j]-(i==k)-(j==k)>=m for i,j in graph) for k in range(2*n)): continue
        out.add(v)
    return out

checks=0
for n in range(1,4):
    possible=list(combinations(range(n),2))
    for mask in range(1<<len(possible)):
        edges=[e for j,e in enumerate(possible) if mask>>j&1]
        for m in range(1,4):
            predicted={tuple(m-v for v in b)+b for b in product(range(m+1),repeat=n) if all(b[i]+b[j]<=m for i,j in edges)}
            assert predicted==full_symbolic_min(n,edges,m)
            checks+=1

graph_checks=0
for n in range(1,6):
    possible=list(combinations(range(n),2))
    for mask in range(1<<len(possible)):
        edges=[e for j,e in enumerate(possible) if mask>>j&1]
        for m in (1,2,3):
            syms={b for b in product(range(m+1),repeat=n) if all(b[i]+b[j]<=m for i,j in edges)}
            ords=ordinary(n,edges,m)
            assert ords<=syms
            if m==1: assert ords==syms
            graph_checks+=1

complete=[]
for n in range(1,7):
    edges=list(combinations(range(n),2))
    for m in range(1,7):
        q=m//2
        count=sum(1 for b in product(range(m+1),repeat=n) if all(b[i]+b[j]<=m for i,j in edges))
        upper=q if m%2==0 else q+1
        predicted=(q+1)**n+n*sum(k**(n-1) for k in range(1,upper+1))
        assert count==predicted
        complete.append(dict(n=n,m=m,symbolic=count,defect=count-comb(m+n,n)))

result=dict(status='PASS',full_exponent_minimality_checks=checks,graph_power_checks=graph_checks,complete_core_checks=complete)
Path(__file__).with_name('verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='complete_core_checks'}))
