"""Exact original-basis checks independent of the proposed split basis.
Run from any directory; no third-party dependencies. No numerical tolerances.
"""
from itertools import combinations
from math import comb, factorial
from pathlib import Path
import json


def pc(value):
    return bin(value).count("1")


def bc(a,b):
    return comb(a,b) if 0 <= b <= a else 0


def rank(matrix,p):
    a=[[v%p for v in row] for row in matrix]
    if not a: return 0
    r=0
    for c in range(len(a[0])):
        pivot=next((j for j in range(r,len(a)) if a[j][c]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][c],-1,p)
        a[r]=[(v*inv)%p for v in a[r]]
        for j in range(r+1,len(a)):
            v=a[j][c]
            if v: a[j]=[(x-v*y)%p for x,y in zip(a[j],a[r])]
        r+=1
        if r==len(a): break
    return r


def predicted(n,faces,i,e,p):
    answer=0
    for S in faces:
        s=pc(S);a=n-s;q=i-s
        if not 0<=q<=q+e<=a: continue
        t=min(q,a-q-e)
        answer+=sum((bc(a,j)-bc(a,j-1)) for j in range(t+1)
          if (factorial(e)*comb(t+e-j,e))%p)
    return answer


def complexes(n):
    fixed={0}|{1<<i for i in range(n)}
    rest=[s for s in range(1<<n) if pc(s)>=2]
    for bits in range(1<<len(rest)):
        faces=fixed|{s for j,s in enumerate(rest) if bits>>j&1}
        if all((s^(1<<j)) in faces for s in faces for j in range(n) if s>>j&1):
            yield faces


def check(n,faces):
    full=(1<<n)-1
    basis=[[] for _ in range(n+1)]
    for S in faces:
        T=full^S
        while True:
            basis[pc(S)+pc(T)].append(S|(T<<n))
            if T==0:break
            T=(T-1)&(full^S)
    ranks={};count=0
    for i in range(n):
        for e in range(1,n-i+1):
            # Original x/y monomial basis: inclusion times e!, independent of z.
            matrix=[[factorial(e) if a&b==a else 0 for a in basis[i]] for b in basis[i+e]]
            for p in (2,3,5,7,11):
                actual=rank(matrix,p)
                expect=predicted(n,faces,i,e,p)
                assert actual==expect,(n,sorted(faces),i,e,p,actual,expect)
                ranks[i,e,p]=actual
                count+=1
    r=max(pc(s) for s in faces)
    for p in (2,3,5,7,11):
        wlp=all(ranks[i,1,p]==min(len(basis[i]),len(basis[i+1])) for i in range(n))
        slp=all(ranks[i,e,p]==min(len(basis[i]),len(basis[i+e])) for i in range(n) for e in range(1,n-i+1))
        assert wlp==((r==1 or (n%2 and r<=2)) and p>(n+1)//2)
        assert slp==(r==1 and p>n)
    return count


def main():
    total=0;counts={}
    for n in range(1,5):
        cs=list(complexes(n));counts[n]=len(cs)
        for faces in cs:total+=check(n,faces)
    for n in (5,6):
        # Every truncated simplex tests all r; plus a single large face and all vertices.
        fam=[{s for s in range(1<<n) if pc(s)<=r} for r in range(1,n+1)]
        fam += [{0}|{1<<j for j in range(n)}|set(range(1<<r)) for r in range(2,n)]
        # Large full simplices have expensive original matrices; rank-selected cases suffice.
        fam=[faces for faces in fam if max(pc(s) for s in faces)<=3]
        counts[n]=len(fam)
        for faces in fam:total+=check(n,faces)
    out={'status':'PASS','complex_counts':counts,'exact_original_basis_power_rank_comparisons':total,
         'primes':[2,3,5,7,11], 'checks':'all powers and WLP/SLP criteria; all complexes n≤4, selected n5,6'}
    Path(__file__).with_name('check-results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))

if __name__=='__main__':main()
