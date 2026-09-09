#!/usr/bin/env python3
"""Independent exact verifier: finite sieve, coverage, fields and cubic witnesses."""
from pathlib import Path
from fractions import Fraction
from math import gcd, prod
import json, time
BASE=Path(__file__).resolve().parent

def factors(n):
    ans=[];p=2
    while p*p<=n:
        if n%p==0:
            ans.append(p)
            while n%p==0:n//=p
        p+=1
    if n>1:ans.append(n)
    return ans

def prime(n):return n>=2 and factors(n)==[n]

def sieve():
    ps=[n for n in range(2,272) if prime(n)];rows=[]
    for t in range(1,57):
        candidates=[]
        for k in range(t+1):
            s=t-k
            if not s:score=Fraction(2**t-1)
            else:
                delta=1-sum((Fraction(1,p) for p in ps[k:t]),Fraction())
                if delta<=0:continue
                score=2**k*(Fraction(s-1,1)/delta+2)-1
            candidates.append((score,k))
        score,k=min(candidates);target=6*score
        if t<=15:
            assert Fraction(1511)-Fraction(1,1511)>target
            proof='1511-1/1511 > 6*score'
        else:
            T=(target.numerator+target.denominator-1)//target.denominator+1
            assert prod(ps[:t])>T**6
            assert Fraction(T)-Fraction(1,T)>target
            proof='primorial > T^6; T-1/T > 6*score'
        rows.append({'omega':t,'core_size':k,'score':[score.numerator,score.denominator],'T':1511 if t<=15 else T,'proof':proof})
    assert len(ps)>=58 and prod(ps[:57])>(6*2**57)**6 and ps[57]>64
    return {'rows':rows,'tail_start':57,'tail_primorial':str(prod(ps[:57])),'tail_rhs':str((6*2**57)**6),'next_prime':ps[57],'tail_induction':'Every following prime exceeds 64, so the primorial grows faster than (6*2^t)^6.','all_pass':True}

class Field:
    def __init__(self,p,mod):self.p=p;self.mod=mod;self.d=len(mod);self.q=p**self.d;self.zero=(0,)*self.d;self.one=(1,)+(0,)*(self.d-1)
    def elem(self,v):return tuple(v+[0]*(self.d-len(v)))
    def plus(self,a,b):return tuple((x+y)%self.p for x,y in zip(a,b))
    def minus(self,a):return tuple(-x%self.p for x in a)
    def mul(self,a,b):
        c=[0]*(2*self.d-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):c[i+j]+=x*y
        for i in range(len(c)-1,self.d-1,-1):
            u=c[i]%self.p
            for j,z in enumerate(self.mod):c[i-self.d+j]-=u*z
        return tuple(x%self.p for x in c[:self.d])
    def power(self,a,n):
        z=self.one
        while n:
            if n&1:z=self.mul(z,a)
            a=self.mul(a,a);n//=2
        return z
    def code(self,a):return sum(v*self.p**i for i,v in enumerate(a))

def check_witness(w):
    p,r,q=w['p'],w['r'],w['q'];Q=q*q
    assert prime(p) and p!=3 and q==p**r and 2<=q<1511
    F=Field(p,w['modulus_low_coefficients']);assert F.q==Q
    z=F.elem([0,1]);one=F.one;zero=F.zero
    assert F.power(z,Q-1)==one
    assert all(F.power(z,(Q-1)//s)!=one for s in factors(Q-1))
    # The quotient ring has an element of exact order Q-1. All nonzero elements
    # are therefore units, proving this modulus defines a field.
    lam=F.power(z,w['primitive_constant_exponent']);assert gcd(w['primitive_constant_exponent'],Q-1)==1
    assert F.code(lam)==w['primitive_constant_code']
    h=(lam,one,one,one)
    def trim(a):
        a=list(a)
        while a and a[-1]==zero:a.pop()
        return a
    def rem(a,b):
        a=trim(a);b=trim(b);inv=F.power(b[-1],Q-2)
        while len(a)>=len(b):
            shift=len(a)-len(b);c=F.minus(F.mul(a[-1],inv))
            for i,v in enumerate(b):a[i+shift]=F.plus(a[i+shift],F.mul(c,v))
            a=trim(a)
        return a
    def mul(a,b):
        c=[zero]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):c[i+j]=F.plus(c[i+j],F.mul(x,y))
        # h is monic, so this reduction uses no inversion.
        for i in range(len(c)-1,2,-1):
            u=F.minus(c[i])
            for j in range(3):c[i-3+j]=F.plus(c[i-3+j],F.mul(u,h[j]))
        return trim(c[:3])
    def power(n):
        a=[zero,one];v=[one]
        while n:
            if n&1:v=mul(v,a)
            a=mul(a,a);n//=2
        return v
    # An independent irreducibility test for a cubic: no linear factor over F_Q.
    a=power(Q);a += [zero]*max(0,2-len(a));a[1]=F.plus(a[1],F.minus(one));a=trim(a)
    b=list(h)
    while a:b,a=a,rem(b,a)
    assert len(trim(b))==1
    N=Q**3-1;assert str(N)==w['root_order'];pf=sorted(set(sum((factors(v) for v in [q-1,q+1,q*q+q+1,q*q-q+1]),[])))
    assert pf==sorted(w['root_order_prime_divisors'])
    rest=N
    for s in pf:
        while rest%s==0:rest//=s
    assert rest==1 and power(N)==[one]
    assert all(power(N//s)!=[one] for s in pf)
    return {'q':q,'base_field_order':Q,'degree_over_prime_field':2*r,'irreducible_cubic':True,'primitive_constant':True,'exact_root_order':str(N),'all_pass':True}

def main():
    start=time.monotonic();s=sieve();data=json.loads((BASE/'witnesses.json').read_text());ws=data['cases']
    expected={p**r for p in range(2,1511) if p!=3 and prime(p) for r in range(1,11) if p**r<1511}
    assert len({x['q'] for x in ws})==len(ws) and {x['q'] for x in ws}==expected
    rows=[]
    for i,w in enumerate(ws):
        rows.append(check_witness(w))
        if i%40==0:print(f'Verified {i+1}/{len(ws)}',flush=True)
    out={'finite_sieve':s,'coverage_count':len(ws),'coverage_complete':True,'witnesses':rows,'all_pass':True,'elapsed_seconds':time.monotonic()-start}
    (BASE/'check-results.json').write_text(json.dumps(out,indent=2)+'\n');print('All',len(ws),'witnesses and exact sieve pass',flush=True)
if __name__=='__main__':main()
