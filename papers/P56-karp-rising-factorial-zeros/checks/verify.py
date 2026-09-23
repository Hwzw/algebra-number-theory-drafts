#!/usr/bin/env python3
"""Exact finite checks supporting, but not replacing, the manuscript's proof."""
import json
from pathlib import Path
import sympy as s

x, t, alpha = s.symbols('x t alpha')
counts = {'difference_identities': 0, 'basis_recurrences': 0,
          'gamma_factorizations': 0, 'coefficient_pairing_cases': 0,
          'karp_cases': 0, 'factorial_transform_cases': 0, 'boundary_cases': 0}

def equal(a, b):
    assert s.expand(a-b) == 0

def direct(c):
    n = len(c)-1
    return s.Poly(sum(c[k]*(s.rf(x,k)*s.rf(x,n-k)
        -s.rf(x+1,k)*s.rf(x-1,n-k)) for k in range(n+1)), x)

def real_negative(poly):
    assert poly.eval(0) > 0
    intervals = s.polys.polytools.intervals(poly, eps=s.Rational(1,10**8))
    assert sum(m for _,m in intervals) == poly.degree()
    assert all(bounds[1] < 0 for bounds,_ in intervals)
    return intervals

for j in range(1,10):
    equal(s.rf(x,j)**2-s.rf(x+1,j)*s.rf(x-1,j),
          j*s.rf(x,j-1)*s.rf(x+1,j-1))
    counts['difference_identities'] += 1

for d in range(7):
    for r in range(d+1):
        b=s.rf(x,r)*s.rf(x+r+alpha,d-r)
        equal(s.rf(x,r)*s.rf(x+r+alpha,d+1-r),(x+alpha+d)*b)
        equal(s.rf(x,r+1)*s.rf(x+r+alpha+1,d-r),x*b.subs(x,x+1))
        counts['basis_recurrences'] += 2

for n in range(2,11):
    m,eps=divmod(n,2)
    gamma=s.symbols('g:'+str(m+1))
    C=s.Poly(sum(gamma[j]*t**j*(1+t)**(n-2*j) for j in range(m+1)),t)
    c=[C.nth(k) for k in range(n+1)]
    R=sum((r+1)*gamma[r+1]*4**(m-1-r)*s.rf(x,r)
          *s.rf(x+r+s.Rational(3,2),m-1-r) for r in range(m))
    equal(direct(c).as_expr(),2**eps*s.rf(x+1,m-1+eps)*R)
    counts['gamma_factorizations'] += 1

for n in range(3,11):
    for roots in [[s.Integer(1)]*n,[s.Rational(i+1,i+2) for i in range(n)]]:
        p=s.Poly(s.prod(t+v for v in roots),t)
        a=[p.nth(k) for k in range(n+1)]
        for weighted in (False,True):
            c=[a[k]*a[n-k]*(s.binomial(n,k) if weighted else 1) for k in range(n+1)]
            result=direct(c)
            assert result.degree()==n-2
            real_negative(result)
            counts['karp_cases' if weighted else 'coefficient_pairing_cases'] += 1

for d in range(1,7):
    h=s.Poly(s.prod(1+(j+1)*t for j in range(d)),t)
    R=s.Poly(sum(h.nth(r)*s.rf(x,r)*s.rf(x+r+s.Rational(3,2),d-r)
                 for r in range(d+1)),x)
    intervals=real_negative(R)
    assert all(intervals[i+1][0][0]-intervals[i][0][1] > 1 for i in range(d-1))
    counts['factorial_transform_cases'] += 1

for a in [[1,2,1,0,0],[0,0,1,2,1]]:
    c=[s.binomial(4,k)*a[k]*a[4-k] for k in range(5)]
    equal(direct(c).as_expr(),12*x*(x+1))
    counts['boundary_cases'] += 1

report={'status':'passed','arithmetic':'exact symbolic identities and rational real-root isolation',
        'sympy_version':s.__version__,'checks':counts,
        'scope':'Finite supporting checks; the all-degree proof is in manuscript.md.'}
(Path(__file__).resolve().parent/'results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
