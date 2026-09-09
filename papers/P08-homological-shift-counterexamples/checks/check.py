"""Exact monomial checks; independent colon computation verifies the shift formula."""
from itertools import combinations
from pathlib import Path
import json

def monomials(n,d):
    if n==1:
        yield (d,)
    else:
        for j in range(d+1):
            for t in monomials(n-1,d-j):
                yield (j,)+t

def divides(a,b): return all(x<=y for x,y in zip(a,b))
def minimal(g):
    g=set(g)
    return {u for u in g if not any(v!=u and divides(v,u) for v in g)}
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def unit(n,j): return tuple(int(k==j) for k in range(n))
def component(g,n,d): return {u for u in monomials(n,d) if any(divides(v,u) for v in g)}
def exchange(B):
    for u in B:
        for v in B:
            for t in range(len(u)):
                if u[t]>v[t]:
                    if not any(tuple(u[k]-int(k==t)+int(k==s) for k in range(len(u))) in B
                               for s in range(len(u)) if u[s]<v[s]):
                        return False
    return True

def check(r,a):
    n=r+2
    x=[unit(n,j) for j in range(r)]
    yz=tuple([0]*r+[1,1]); ya=tuple([0]*r+[a,0])
    g=x+[yz,ya]
    colon_shifts={i:set() for i in range(r+3)}
    for j,u in enumerate(g):
        colon=minimal({tuple(max(v[k]-u[k],0) for k in range(n)) for v in g[:j]})
        assert all(sum(v)==1 for v in colon)
        variables=[v.index(1) for v in colon]
        for i in range(len(variables)+1):
            for F in combinations(variables,i):
                colon_shifts[i].add(tuple(u[k]+int(k in F) for k in range(n)))
    for i in colon_shifts:
        colon_shifts[i]=minimal(colon_shifts[i])
        formula=set()
        for j,extra in [(i+1,(0,0)),(i,(1,1)),(i,(a,0)),(i-1,(a,1))]:
            if 0<=j<=r:
                for F in combinations(range(r),j):
                    formula.add(tuple(int(k in F) for k in range(r))+extra)
        assert colon_shifts[i]==minimal(formula),(r,a,i)
    # Exhaustive exchange checks in bounded components; the hand proof covers all d.
    degrees=list(range(1,a+2))
    for d in degrees:
        B=component(g,n,d)
        assert exchange(B),(r,a,d)
    witnesses=[]
    for i in range(1,r+1):
        F=set(range(i-1)); t=i-1
        u=tuple(int(k in F or k==t) for k in range(r))+(a-2,2)
        v=tuple(int(k in F) for k in range(r))+(a,1)
        w=tuple(int(k in F) for k in range(r))+(a-1,2)
        H=colon_shifts[i]
        assert any(divides(b,u) for b in H)
        assert any(divides(b,v) for b in H)
        assert not any(divides(b,w) for b in H)
        assert [j for j in range(n) if u[j]<v[j]]==[r]
        witnesses.append({'i':i,'u':u,'v':v,'failed_exchange':w})
    assert len(colon_shifts[r+1])==1 and not colon_shifts[r+2]
    return {'r':r,'a':a,'checked_components':degrees,'witnesses':witnesses}

if __name__=='__main__':
    # Covers varying numbers of intermediate shifts and several degree gaps.
    cases=[(r,a) for r in range(1,4) for a in range(3,6)]
    results=[check(r,a) for r,a in cases]
    out={'status':'PASS','cases':results,
         'scope':'Exact bounded exchange and colon checks; not a substitute for the uniform proof.'}
    Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':'PASS','cases':len(results),'components':sum(len(c['checked_components']) for c in results),'failure_witnesses':sum(len(c['witnesses']) for c in results)}))
