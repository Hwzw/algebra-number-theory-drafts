"""Exact finite checks for the growing-ordinarization proof.

No sampling or finite calculation proves the limit theorem.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import check as previous


def C(n,k):
    return comb(n,k) if 0<=k<=n else 0


def levels(maxg):
    level={frozenset()}
    yield 0,level
    for g in range(maxg):
        nxt=set()
        for gaps in level:
            frob=max(gaps,default=-1)
            m=next(x for x in range(1,2*g+3) if x not in gaps)
            for x in range(max(1,frob+1),max(m,frob+m)+1):
                if x not in gaps and all(y in gaps or x-y in gaps for y in range(1,x)):
                    nxt.add(gaps|{x})
        level=nxt
        yield g+1,level


def bulk_count(g,r,literal=False):
    total=0;fibers=0
    for m in range(g//2+1,g+1):
        for rest in combinations(range(m+1,g+1),r-1):
            b=(m,)+rest
            forbidden={x+y for i,x in enumerate(b) for y in b[i:] if x+y<=g+m}
            exact=C(m-len(forbidden),r)
            if literal:
                actual=sum(previous.literal(g,a,b) for a in combinations(range(g+1,g+m+1),r))
                assert actual==exact,(g,r,b,forbidden)
            total+=exact;fibers+=1
    return total,fibers


def outside_bounds(g,r):
    if r<2:return 0,0
    low=sum(C(m+r-4,r-2)*C(m+r-1,r) for m in range(2,g//2+1))
    high=sum(C(g-m,r-1)*(C(m+r-1,r)-C(m,r)) for m in range(g//2+1,g+1))
    return low,high


def run():
    semigroups=0;fibers=0;chain_checks=0;rows=[]
    for g,level in levels(16):
        semigroups+=len(level)
        if not g:continue
        full=Counter();valid_bulk=Counter();low=Counter();high=Counter();by_mr=Counter()
        for gaps in level:
            b=tuple(x for x in range(1,g+1) if x not in gaps)
            r=len(b);full[r]+=1
            if not r:continue
            a=tuple(sorted(x for x in gaps if x>g));m=b[0]
            assert all(x+m>g or x+m in b for x in b)
            assert all(x-m<=g or x-m in a for x in a)
            q=g//m;assert q<=r
            by_mr[m,r]+=1;chain_checks+=1
            if previous.generic(g,a,b):valid_bulk[r]+=1
            elif 2*m<=g:low[r]+=1
            else:high[r]+=1
        for (m,r),count in by_mr.items():
            if 2*m<=g:
                assert count<=C(m+r-g//m-2,r-g//m)*C(m+r-1,r)
        for r in range(1,g+1):
            v,f=bulk_count(g,r,literal=g<=8);fibers+=f
            assert v==valid_bulk[r],(g,r,v,valid_bulk[r])
            lo,hi=outside_bounds(g,r)
            assert low[r]<=lo and high[r]<=hi,(g,r,low[r],high[r],lo,hi)
            assert full[r]==v+low[r]+high[r]
        rows.append({'g':g,'all_semigroups':len(level),'valid_nonordinary_bulk':sum(valid_bulk.values()),
                     'valid_low_minimum':sum(low.values()),'valid_high_hole':sum(high.values())})
    examples=[]
    for r in [2,4,8,12,20]:
        g=r**3
        m=previous.M(g,r)
        ar=F(1,2*factorial(2*r))+F(1,2*4**r*factorial(r)**2)
        lo,hi=outside_bounds(g,r)
        row={'r':r,'g':g,'r_cubed_over_g':1,
             'bulk_over_leading':str(F(m,1)/(ar*g**(2*r))),
             'low_bound_over_bulk':str(F(lo,m)),'high_bound_over_bulk':str(F(hi,m))}
        if r<=4:
            value,_=bulk_count(g,r)
            row['exact_valid_bulk_over_bulk']=str(F(value,m))
        examples.append(row)
    result={'date':'2026-09-16','all_passed':True,'tree_semigroups_through_genus_16':semigroups,
            'individual_multiplicity_chain_checks':chain_checks,'exact_bulk_fibers_checked':fibers,
            'literal_fiber_closure_through_genus':8,'tree_vs_fiber_counts_through_genus':16,
            'outside_count_bounds_through_genus':16,'rows':rows,'exact_scale_examples':examples,
            'scope':'Exact finite diagnostics only. The asymptotic theorem follows from the manuscript proof, not these examples.',
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_name('uniform-checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['rows','exact_scale_examples']},indent=2))
    for row in examples:
        print({k:float(F(v)) if isinstance(v,str) else v for k,v in row.items()})


if __name__=='__main__':
    run()
