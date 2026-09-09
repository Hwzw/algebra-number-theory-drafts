"""Exhaustive direct multiplication checks for small twisted Corbas rings."""
from math import gcd

class Field:
    def __init__(self, p, modulus):
        self.p, self.modulus = p, modulus
        self.f = len(modulus)-1
        self.q = p**self.f
    def digits(self, a):
        out=[]
        for _ in range(self.f): out.append(a%self.p); a//=self.p
        return out
    def value(self, digits):
        return sum((c%self.p)*self.p**i for i,c in enumerate(digits))
    def add(self,a,b): return self.value([x+y for x,y in zip(self.digits(a),self.digits(b))])
    def mul(self,a,b):
        aa,bb=self.digits(a),self.digits(b)
        c=[0]*(2*self.f-1)
        for i,x in enumerate(aa):
            for j,y in enumerate(bb): c[i+j]=(c[i+j]+x*y)%self.p
        for i in range(len(c)-1,self.f-1,-1):
            t=c[i]
            for j in range(self.f+1):c[i-self.f+j]=(c[i-self.f+j]-t*self.modulus[j])%self.p
        return self.value(c[:self.f])
    def power(self,a,n):
        out=1
        for _ in range(n):out=self.mul(out,a)
        return out

cases=0
for p,modulus in [(2,[1,1,1]),(2,[1,1,0,1]),(3,[1,0,1])]:
    F=Field(p,modulus); q=F.q
    assert all(F.power(a,q-1)==1 for a in range(1,q))
    for s in range(F.f):
        phi=[F.power(a,p**s) for a in range(q)]
        elements=[(a,b) for a in range(q) for b in range(q)]
        def add(x,y): return F.add(x[0],y[0]),F.add(x[1],y[1])
        def mul(x,y): return F.mul(x[0],y[0]),F.add(F.mul(x[0],y[1]),F.mul(x[1],phi[y[0]]))
        E=p*(q-1); divisor=p*(q-1)//(p**gcd(F.f,s)-1)
        maps={}; periodic_maps=set()
        current={x:(1,0) for x in elements}
        for n in range(1,E+2):
            current={x:mul(current[x],x) for x in elements}
            signature=tuple(current[x] for x in elements)
            periods=[a for a in elements if all(current[add(x,a)]==current[x] for x in elements)]
            expected=[(0,b) for b in range(q)] if n%divisor==0 else [(0,0)]
            assert periods==expected,(q,s,n,periods,expected)
            maps[signature]=n
            if len(periods)>1:periodic_maps.add(signature)
            cases+=1
        assert len(maps)==E+1
        assert len(periodic_maps)==p**gcd(F.f,s)-1
        print(f'q={q}, Frobenius power={s}: distinct={len(maps)}, periodic={len(periodic_maps)} PASS')
print(f'PASS: {cases} power maps, full additive-period sets checked exhaustively')
