"""Exact finite checks of the universal identities proved in the manuscript.

These checks detect algebraic normalization errors. They do not establish
the universal theorem, spherical rearrangement, or historical priority.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import json


def trim(p):
    while len(p)>1 and not p[-1]:
        p.pop()
    return p


def add(p,q):
    return trim([(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0)
                 for i in range(max(len(p),len(q)))])


def scale(p,a):
    return trim([a*x for x in p])


def mul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return trim(r)


def diff(p,k):
    for _ in range(k):p=[(i+1)*p[i+1] for i in range(len(p)-1)] or [F(0)]
    return trim(p)


def integral(p):
    return sum((a/F(i+1) for i,a in enumerate(p)),F(0))


def run():
    records=[]
    for m in range(1,7):
        w=[F(0)]*m+[F((-1)**j*comb(m,j)) for j in range(m+1)]
        mass=integral(w)
        assert mass==F(factorial(m)**2,factorial(2*m+1))
        basis=[]
        for k in range(7):
            h=[F(0)]*k+[F(1)]
            for p in basis:
                h=add(h,scale(p,-integral(mul(w,mul(h,p)))/integral(mul(w,mul(p,p)))))
            basis.append(h)
            eigen=F(factorial(k+2*m),factorial(k))
            v=mul(w,h)
            assert scale(diff(v,2*m),(-1)**m)==scale(h,eigen)
            assert integral(mul(diff(v,m),diff(v,m)))==eigen*integral(mul(w,mul(h,h)))
            beta=sum((F((-1)**j*comb(2*m-1,j),k+j+1) for j in range(2*m)),F(0))/factorial(2*m-1)
            assert beta==1/eigen
            # Funk--Hecke eigenvalue of (1-s)^(-1), after its normalization.
            jacobi_at_one=F(factorial(k+m),factorial(m)*factorial(k))
            raw_integral=F(2**(2*m)*factorial(m-1)*factorial(k+m),factorial(k+2*m))
            coordinate_density=F(factorial(2*m+1),2**(2*m+1)*factorial(m)**2)
            riesz=coordinate_density*raw_integral/jacobi_at_one/F((2*m+1)*factorial(2*m-1))
            assert riesz==1/eigen
            records.append({'m':m,'k':k,'eigenvalue':str(eigen),'inverse_eigenvalue':str(beta),
                            'differential_identity':True,'energy_identity':True,'poisson_beta_identity':True,'riesz_multiplier_identity':True})
    return {'status':'all exact rational checks passed','meaning':'finite normalization checks only; universal proof is in the manuscript','cases':records}


if __name__=='__main__':
    result=run()
    p=Path(__file__).resolve().parent/'jacobi-exact-check.json'
    p.write_text(json.dumps(result,indent=2)+'\n')
    print(result['status'],len(result['cases']),'cases')
