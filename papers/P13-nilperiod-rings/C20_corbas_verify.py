"""Independent finite tables for Corbas rings; no symbolic power formula used."""
from itertools import product
from math import gcd
from pathlib import Path
import json

results=[]
for p,f,modulus in [(2,1,[0]),(3,1,[0]),(2,2,[1,1]),
                    (2,3,[1,1,0]),(3,2,[1,0]),(2,4,[1,1,0,0])]:
    q=p**f
    def digits(a):return [(a//p**i)%p for i in range(f)]
    def encode(v):return sum((c%p)*p**i for i,c in enumerate(v))
    def add(a,b):return encode([x+y for x,y in zip(digits(a),digits(b))])
    def mul(a,b):
        v=[0]*(2*f-1)
        for i,x in enumerate(digits(a)):
            for j,y in enumerate(digits(b)):v[i+j]=(v[i+j]+x*y)%p
        for i in range(2*f-2,f-1,-1):
            for j in range(f):v[i-f+j]=(v[i-f+j]-v[i]*modulus[j])%p
        return encode(v[:f])
    A=[[add(a,b) for b in range(q)] for a in range(q)]
    M=[[mul(a,b) for b in range(q)] for a in range(q)]
    assert all(any(M[a][b]==1 for b in range(1,q)) for a in range(1,q))
    def powfield(a,k):
        out=1
        for _ in range(k):out=M[out][a]
        return out
    for s in range(f):
        phi=[powfield(a,p**s) for a in range(q)]
        assert all(phi[M[a][b]]==M[phi[a]][phi[b]] for a,b in product(range(q),repeat=2))
        size=q*q
        RA=[[A[a%q][b%q]+q*A[a//q][b//q] for b in range(size)] for a in range(size)]
        RM=[[M[a%q][b%q]+q*A[M[a%q][b//q]][M[a//q][phi[b%q]]] for b in range(size)] for a in range(size)]
        seen={}
        power=tuple(range(size))
        n=1
        periods=[]
        while power not in seen:
            seen[power]=n
            actual={r for r in range(size) if all(power[RA[x][r]]==power[x] for x in range(size))}
            divisor=p*(q-1)//(p**gcd(f,s)-1)
            expected=set(range(0,size,q)) if n%divisor==0 else {0}
            assert actual==expected,(p,f,s,n,actual,expected)
            if len(actual)>1:periods.append(n)
            power=tuple(RM[power[x]][x] for x in range(size))
            n+=1
        assert seen[power]==2
        assert n-2==p*(q-1)
        assert len(periods)==p**gcd(f,s)-1
        results.append(dict(p=p,f=f,s=s,size=size,first_repeat=n,
                            periodic_exponents=periods,periodic_map_count=len(periods)))
Path(__file__).with_name('C20-corbas-verification.json').write_text(json.dumps(dict(status='PASS',rings=len(results),results=results),indent=2)+'\n')
print(json.dumps(dict(status='PASS',rings=len(results),power_maps=sum(r['first_repeat']-1 for r in results))))
