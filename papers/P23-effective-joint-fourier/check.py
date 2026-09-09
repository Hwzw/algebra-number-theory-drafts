"""Exact diagnostics for Q25. Finite checks do not establish the theorem."""
import json
from pathlib import Path
from random import Random
import sympy as S

x = S.Symbol('x')
polys = [x-3, x*x-x-1, x**3-x-1,
         x**4-x**3-x*x-x+1, x**4-3*x**3+3*x*x-3*x+1]
cases = 0
rng = Random(20260909)
for p in polys:
    P = S.Poly(p, x)
    d = P.degree()
    assert P.is_irreducible
    cs = [P.nth(i) for i in range(d+1)]
    T = S.zeros(d)
    for i in range(d-1):
        T[i+1, i] = 1
    for i in range(d):
        T[i, d-1] = -cs[i]
    assert sum((cs[i]*T**i for i in range(d+1)), S.zeros(d)) == S.zeros(d)
    derivative = sum((i*cs[i]*T**(i-1) for i in range(1,d+1)), S.zeros(d))
    vi = [sum((cs[i]*T**(i-1-j) for i in range(j+1,d+1)), S.zeros(d))*derivative.inv()
          for j in range(d)]
    for trial in range(8):
        A = [rng.randrange(-9,10) for _ in range(d)]
        for n in range(d, 40):
            A.append(-sum(cs[i]*A[n-d+i] for i in range(d)))
        for k in [0,1,3,8]:
            alpha = T**(-k)*sum((vi[j]*A[k+j] for j in range(d)), S.zeros(d))
            for n in range(k, 35):
                assert S.trace(alpha*T**n) == A[n]
                cases += 1

interval_cases = 0
intervals_checked = 0
for _ in range(1500):
    e = rng.randrange(10,10**16)
    f = rng.randrange(max(1,e//17),17*e+1)
    R = rng.randrange(3,300)
    k0 = rng.randrange(1,20)
    power = R*R
    seen = [[],[]]
    while min(e,f)//power >= 2*k0:
        k,l = e//power,f//power
        assert k>=k0 and l>=k0
        assert R*k-1<=e and R*l-1<=f
        # The floors preserve comparability once the arguments exceed two.
        assert 2*f*k>=e*l and f*k<=2*e*l
        for arr,start in zip(seen,[k,l]):
            end=R*start-1
            assert end>=start
            if arr:
                assert end<arr[-1][0]
            arr.append((start,end))
        power*=R
        intervals_checked+=2
    interval_cases+=1

result={'projection_trace_identities':cases,
        'polynomials':[str(p) for p in polys],
        'paired_interval_parameter_cases':interval_cases,
        'disjoint_intervals_checked':intervals_checked,
        'all_passed':True,
        'scope':'Exact finite diagnostics of the projection identity and interval endpoints; not proof of the infinite theorem or its novelty.'}
out=Path(__file__).with_name('check-results.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
