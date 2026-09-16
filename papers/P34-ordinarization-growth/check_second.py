"""Exact diagnostics for the complete second coefficient; not a proof by testing."""
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial, gcd
from functools import reduce
from pathlib import Path
import hashlib
import json
import check as previous


def C(n,k):
    return comb(n,k) if 0<=k<=n else 0


def candidate_counts(g,r):
    low=sum(C(m-1,r-2)*C(m,r) for m in range(g//3+1,g//2+1)) if r>=2 else 0
    high=sum(C(m-1,r-2)*C(g-m+1,r) for m in range(g//2+1,g+1)) if r>=2 else 0
    negative=0
    for m in range(g//2+1,g+1):
        q=g-m
        negative+=C(m-1,r-1)*(r*C(q,r-1)+(q//2)*C(q-1,r-2)+((q-1)**2//4)*C(q-2,r-3))
    return low,high,negative


def coefficients(r):
    cr=F(1,4**r*factorial(r)*factorial(r-1))
    low=((F(1,2**(2*r-1))-F(1,3**(2*r-1)))/((2*r-1)*factorial(r-2)*factorial(r))) if r>=2 else F(0)
    high=F(1,2*factorial(2*r-1))-2*cr if r>=2 else F(0)
    neg=F(r*(r+3),8*factorial(2*r-1))
    gamma=-F(2*r-3,4*factorial(2*r-1))-(r-F(3,2))*cr
    beta=-F(r*r+7*r-10,8*factorial(2*r-1))-F(4*r*r-4*r+3,2*(2*r-1))*cr-F(3*(r-1),(2*r-1)*9**r*factorial(r)*factorial(r-1))
    assert beta==gamma+low+high-neg
    return low,high,neg,gamma,beta


def normals(g,a,b):
    r=len(b);v=b+a;eqs=set()
    def add(terms):
        z=[0]*(2*r)
        for i,c in terms:z[i]+=c
        if not any(z) or sum(x*y for x,y in zip(z,v)):return
        q=reduce(gcd,(abs(x) for x in z));z=tuple(x//q for x in z)
        if next(x for x in z if x)<0:z=tuple(-x for x in z)
        eqs.add(z)
    for i in range(r):
        for j in range(i,r):
            for k in range(r):add([(i,1),(j,1),(k,-1)])
            for h in range(r):add([(i,1),(j,1),(r+h,-1)])
    for h in range(r):
        for i in range(r):
            for j in range(r):add([(r+h,1),(i,-1),(r+j,-1)])
    return eqs


def tuple_checks():
    total=0;residuals=0
    for g in range(1,9):
        for r in range(1,g+1):
            observed=[0,0,0]
            for b in combinations(range(1,g+1),r):
                m=b[0]
                for a in combinations(range(g+1,2*g+1),r):
                    valid=previous.literal(g,a,b)
                    bulk=previous.generic(g,a,b)
                    low=(r>=2 and g<3*m and 2*m<=g and 2*m in b
                         and all(x>g-m for x in b if x not in (m,2*m)) and a[-1]<=g+m)
                    high=(r>=2 and 2*m>g and a[-1]>g+m and a[-1]-m in a
                          and a[-2]<=g+m and b[1]>=a[-1]-g)
                    neg=sum(x+y in a for i,x in enumerate(b) for y in b[i:]) if bulk else 0
                    observed=[observed[0]+low,observed[1]+high,observed[2]+neg]
                    residual=int(valid)-int(bulk)-int(low)-int(high)+neg
                    if residual:
                        assert len(normals(g,a,b))>=2,(g,a,b,residual)
                        residuals+=1
                    total+=1
            assert tuple(observed)==candidate_counts(g,r),(g,r,observed,candidate_counts(g,r))
    return total,residuals


def interpolation_checks():
    rows=[];holdouts=0
    for r in range(1,9):
        expected=coefficients(r);d=2*r-1
        for residue in range(1,13):
            values=[candidate_counts(residue+12*j,r) for j in range(d+4)]
            for k in range(3):
                differences=previous.newton([v[k] for v in values[:d+1]])
                assert F(differences[d],factorial(d)*12**d)==expected[k],(r,residue,k)
                for j in range(d+1,d+4):
                    assert previous.at(differences,j)==values[j][k]
                    holdouts+=1
        rows.append(dict(r=r,low=str(expected[0]),high=str(expected[1]),negative=str(expected[2]),gamma=str(expected[3]),beta=str(expected[4])))
    # Independently recover the second coefficient of the cited exact r=2 formula.
    beta=coefficients(2)[4];cr=F(1,32)
    for residue in range(1,13):
        diff=previous.newton([previous.source2(residue+12*j) for j in range(5)])
        lead_j=F(diff[4],factorial(4))
        next_j=F(diff[3],factorial(3))-6*lead_j
        next_g=next_j/12**3-4*residue*lead_j/12**4
        assert next_g==beta-cr/2*(-1)**residue
    assert coefficients(1)[4]==-F(1,8)
    return rows,holdouts


if __name__=='__main__':
    tuples,residuals=tuple_checks();rows,holdouts=interpolation_checks()
    result={'all_passed':True,'date':'2026-09-16','literal_tuples_checked':tuples,
            'nonzero_residuals_verified_on_two_independent_equalities':residuals,
            'candidate_sum_periods_tested':12,'r_values_tested':list(range(1,9)),
            'exact_candidate_sum_holdouts':holdouts,'known_r2_residues_checked':12,
            'coefficients':rows,'scope':'Finite diagnostics; the all-r coefficient formula is established by the manuscript hand proof.',
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_name('second-coefficient-checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
