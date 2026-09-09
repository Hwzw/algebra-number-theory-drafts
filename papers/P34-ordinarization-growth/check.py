"""Exact finite diagnostics; the universal statements require the manuscript proof."""
from fractions import Fraction as F
from math import comb, factorial
from itertools import combinations
from pathlib import Path
import json,time

def structural(g,A,B):
    aa=set(A);bb=set(B)
    return (all((x+y>g or x+y in bb) and x+y not in aa for i,x in enumerate(B) for y in B[i:])
            and all(a-b<=g or a-b in aa for a in A for b in B))

def literal(g,A,B):
    S=({0}|set(B)|set(range(g+1,4*g+1)))-set(A)
    return all(x+y in S for x in S for y in S if x+y<=2*g)

def generic(g,A,B):return bool(B) and 2*B[0]>g and A[-1]<=g+B[0]

def on_exception(A,B):
    return (any(2*B[0]==b for b in B)
            or any(A[-1]-B[0]==a for a in A)
            or any(x+y==a for i,x in enumerate(B) for y in B[i:] for a in A))

def all_tuples(maxg):
    count=0;diff=0;counts={}
    for g in range(1,maxg+1):
        row=[1]+[0]*g
        for r in range(1,g+1):
            for B in combinations(range(1,g+1),r):
                for A in combinations(range(g+1,2*g+1),r):
                    good=structural(g,A,B)
                    assert good==literal(g,A,B),(g,A,B)
                    row[r]+=good;count+=1
                    if good!=generic(g,A,B):
                        assert on_exception(A,B),(g,A,B)
                        diff+=1
        counts[g]=row
    return count,diff,counts

def tree_counts(maxg):
    # Gaps determine S; remove one minimal generator above F to get children.
    level={frozenset()};out={0:[1]}
    for g in range(maxg):
        nxt=set()
        for gaps in level:
            frob=max(gaps,default=-1)
            m=next(x for x in range(1,2*g+3) if x not in gaps)
            for x in range(max(1,frob+1),frob+m+2):
                if x in gaps:continue
                if all(y in gaps or x-y in gaps for y in range(1,x)):
                    nxt.add(gaps|{x})
        level=nxt;row=[0]*(g+2)
        for gaps in level:
            r=sum(x not in gaps for x in range(1,g+2));row[r]+=1
        out[g+1]=row
    return out

def M(g,r):return sum(comb(g-m,r-1)*comb(m,r) for m in range(g//2+1,g+1) if g-m>=r-1 and m>=r)
def newton(vals):
    coeff=[]
    while vals:
        coeff.append(vals[0]);vals=[b-a for a,b in zip(vals,vals[1:])]
    return coeff

def at(c,t):return sum(v*comb(t,j) for j,v in enumerate(c) if t>=j)
def bulk_checks():
    out=[];checked=0
    for r in range(1,13):
        d=2*r;co=[]
        target=F(1,2*factorial(d))+F(1,2*4**r*factorial(r)**2)
        for e in [0,1]:
            c=newton([M(2*j+e,r) for j in range(d+1)])
            for j in range(d+1,4*d+1):assert at(c,j)==M(2*j+e,r);checked+=1
            aj=F(c[d],factorial(d));bj=F(c[d-1],factorial(d-1))-aj*d*(d-1)/2
            a=aj/2**d;b=bj/2**(d-1)-d*e*a
            assert a==target;co.append(b)
        jump=F(1,4**r*factorial(r)*factorial(r-1))
        assert co[1]-co[0]==jump
        assert 2*r*target-jump==F(r,factorial(d))
        out.append({'r':r,'leading':str(target),'second_even':str(co[0]),'second_odd':str(co[1]),'parity_jump':str(jump),'delta_odd':str(2*r*target-jump),'delta_even':str(2*r*target+jump)})
    return checked,out

def source2(g):
    x=F(g);e=g%12
    if e==0:y=x*(x**3-F(2548,297)*x**2+F(336,11)*x-F(1376,33))
    elif e==1:y=(x-1)*(x**3-F(1927,297)*x**2+F(3611,297)*x-F(541,297))
    elif e==2:y=(x-2)*(x**3-F(1954,297)*x**2+F(5548,297)*x-F(3352,297))
    elif e==3:y=(x-3)*(x**3-F(1333,297)*x**2+F(449,99)*x+F(51,11))
    elif e==4:y=x**4-F(2548,297)*x**3+F(3088,99)*x**2-F(4192,99)*x-F(512,297)
    elif e==5:y=x**4-F(2224,297)*x**3+F(1910,99)*x**2-F(1576,99)*x-F(6499,297)
    elif e==6:y=x**4-F(2548,297)*x**3+F(336,11)*x**2-F(1520,33)*x+48
    elif e==7:y=x**4-F(2224,297)*x**3+F(1846,99)*x**2-F(952,99)*x-F(4643,297)
    elif e==8:y=x**4-F(2548,297)*x**3+F(3152,99)*x**2-F(4384,99)*x-F(7552,297)
    elif e==9:y=x**4-F(2224,297)*x**3+18*x**2-F(40,3)*x+F(39,11)
    elif e==10:y=x**4-F(2548,297)*x**3+F(3088,99)*x**2-F(4624,99)*x+F(13744,297)
    else:y=(x+1)*(x**3-F(2521,297)*x**2+F(8251,297)*x-F(11683,297))
    return y*F(11,384)

if __name__=='__main__':
    start=time.time();n,h,tuples=all_tuples(9);tree=tree_counts(16)
    for g,row in tuples.items():assert row==tree[g],(g,row,tree[g])
    for g,row in tree.items():
        if g:
            assert row[1]==(F(3,8)*g*g-F(1,4)*g if g%2==0 else F(3,8)*(g*g-1))
            if g>=2:assert row[2]==source2(g),(g,row[2],source2(g))
    nbulk,bulk=bulk_checks()
    result={'all_passed':True,'literal_vs_structural_tuples':n,'symmetric_difference_hyperplane_cases':h,'tree_counts_through_genus':16,'tree_total_semigroups':sum(sum(x) for x in tree.values()),'tree_counts':tree,'bulk_holdout_evaluations':nbulk,'bulk_coefficients':bulk,'scope':'Exact finite diagnostics only; no finite calculation proves quasipolynomiality or eventual monotonicity for arbitrary r.','elapsed_seconds':round(time.time()-start,3)}
    Path(__file__).with_name('check-results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['tree_counts','bulk_coefficients']},indent=2))
