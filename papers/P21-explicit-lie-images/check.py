#!/usr/bin/env python3
"""Independent matrix and finite-field checks; the manuscript gives the proof."""
from itertools import product
from pathlib import Path
from collections import Counter
from random import Random
import json
import sympy as s


def symbolic():
    a,b,c,d,e,f=s.symbols('a b c d e f')
    X=s.Matrix([[a,b],[c,-a]]); Y=s.Matrix([[d,e],[f,-d]])
    br=lambda U,V:U*V-V*U
    Q=lambda U:-U.det()
    C=br(X,Y)
    clean=lambda M:all(s.expand(v)==0 for v in M)
    checks=[clean(br(X,br(X,Y))-4*(Q(X)*Y-s.trace(X*Y)*X/2)),
            clean(br(C,br(X,br(X,Y)))+4*Q(C)*X),
            clean(br(C,br(C,X))-4*Q(C)*X)]
    assert all(checks)
    return {'generic_matrix_identities':len(checks),'coefficient_ring':'Z[a,b,c,d,e,f]','all_pass':True}


class Field:
    def __init__(self,p,degree):
        self.p=p; self.q=p**degree; self.degree=degree
        n=next(i for i in range(2,p) if pow(i,(p-1)//2,p)==p-1) if degree==2 else 0
        self.n=n
        self.add=[[((a%p+b%p)%p)+p*((a//p+b//p)%p) for b in range(self.q)] for a in range(self.q)]
        self.neg=[((-a%p)%p)+p*((- (a//p))%p) for a in range(self.q)]
        self.mul=[[((a%p*(b%p)+n*(a//p)*(b//p))%p)+p*((a%p*(b//p)+(a//p)*(b%p))%p) for b in range(self.q)] for a in range(self.q)]
    def power(self,a,k):
        z=1
        while k:
            if k&1:z=self.mul[z][a]
            a=self.mul[a][a]; k//=2
        return z
    def scale(self,a,x):return tuple(self.mul[a][v] for v in x)
    def plus(self,x,y):return tuple(self.add[a][b] for a,b in zip(x,y))
    def bracket(self,x,y):
        # Independent explicit coordinates of XY-YX for X=[[d,a],[b,-d]].
        d,a,b=x; e,c,f=y; A=self.add; M=self.mul; N=self.neg; two=2%self.p
        sub=lambda u,v:A[u][N[v]]
        return (sub(M[a][f],M[c][b]),M[two][sub(M[d][c],M[e][a])],M[two][sub(M[b][e],M[f][d])])
    def Q(self,x):
        d,a,b=x
        return self.add[self.mul[d][d]][self.mul[a][b]]
    def basis(self,x,y):
        C=self.bracket(x,y); u=y; ans=[]
        inv4=self.power(4%self.p,self.q-2); coeff=self.neg[1]
        for k in range(self.q):
            u=self.bracket(x,self.bracket(x,u))
            v=u
            for _ in range(2*self.q-3):v=self.bracket(C,v)
            ans.append(self.scale(coeff,v)); coeff=self.mul[coeff][inv4]
        return ans
    def indicator(self,T):
        # Coefficients built by literal multiplication of (z-a)^(q-1).
        out=[0]*self.q
        for a in T:
            poly=[1]
            for _ in range(self.q-1):
                nxt=[0]*(len(poly)+1)
                for i,v in enumerate(poly):
                    nxt[i]=self.add[nxt[i]][self.mul[self.neg[a]][v]]
                    nxt[i+1]=self.add[nxt[i+1]][v]
                poly=nxt
            out[0]=self.add[out[0]][1]
            out=[self.add[u][self.neg[v]] for u,v in zip(out,poly)]
        return out
    def evalpoly(self,r,t):
        a=0
        for v in reversed(r):a=self.add[self.mul[a][t]][v]
        return a


def audit(p,degree,mode):
    F=Field(p,degree); q=F.q; zero=(0,0,0); allv=list(product(range(q),repeat=3))
    assert all(F.power(a,q-1)==1 for a in range(1,q))
    xs=allv if mode=='all' else [(0,1,t) for t in range(q)]
    rng=Random(230909+q)
    pairs=((rng.choice(allv),rng.choice(allv)) for _ in range(256)) if mode=='sample' else product(xs,allv)
    count=0; basis_checks=0; fiber=Counter(); saved=[]
    for x,y in pairs:
        values=F.basis(x,y); t=F.Q(x); Delta=F.Q(F.bracket(x,y)); gate=F.power(Delta,q-1)
        for k,v in enumerate(values):
            expect=F.scale(F.mul[gate][F.power(t,k)],x)
            assert v==expect,(q,x,y,k,v,expect)
            basis_checks+=1
        if x!=zero and values[0]==x:fiber[x]+=1
        if mode=='all':saved.append((x,values))
        count+=1
    fiber_checks=0
    if mode!='sample':
        for x in xs:
            if x==zero:continue
            t=F.Q(x)
            expected=q*q*(q-1) if not t else q*(q-1)**2 if F.power(t,(q-1)//2)==1 else q*(q*q-1)
            assert fiber[x]==expected,(q,x,fiber[x],expected)
            fiber_checks+=1
    interp=0; image_checks=0
    # All subsets for q<=9, including non-prime field coefficients.
    subsets=range(1<<q) if q<=9 else [0,1,3,(1<<q)-1]
    for mask in subsets:
        T={i for i in range(q) if mask>>i&1}; r=F.indicator(T)
        for t in range(q):
            assert F.evalpoly(r,t)==int(t in T); interp+=1
        if mode=='all':
            images=set(); zeros=0
            for x,values in saved:
                w=zero
                for coeff,v in zip(r,values):w=F.plus(w,F.scale(coeff,v))
                images.add(w); zeros+=w==zero
            assert images=={zero}|{x for x in allv if F.Q(x) in T}
            assert zeros==q**6-len(T)*q*q*(q*q-1)*(q-1)
            image_checks+=1
    return {'q':q,'field':f'F_{p}' if degree==1 else f'F_{p}[u]/(u^2-{F.n})','input_mode':mode,'pairs':count,'direct_nested_bracket_basis_checks':basis_checks,'exact_fibers_checked':fiber_checks,'indicator_values_checked':interp,'complete_subset_images_checked':image_checks,'all_pass':True}


if __name__=='__main__':
    result={'symbolic':symbolic(),'fields':[],'role':'Exact consistency checks; universal statements proved in manuscript.'}
    for spec in [(3,1,'all'),(5,1,'all'),(7,1,'canonical'),(3,2,'canonical'),(5,2,'sample')]:
        row=audit(*spec); result['fields'].append(row); print(json.dumps(row),flush=True)
    output=Path(__file__).with_name('q23-check.json' if Path(__file__).name=='q23-check.py' else 'check-results.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
