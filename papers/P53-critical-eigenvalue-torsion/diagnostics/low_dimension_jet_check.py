"""Separate finite spherical-Bessel boundary check of the cubic eigenvalue jet."""
from pathlib import Path
import hashlib,json
import sympy as S
t,z,j=S.symbols('t z j')
def trunc(e):
    return S.expand(sum(v*t**p[0] for p,v in S.Poly(S.expand(e),t).terms() if p[0]<=3))
results=[]
for n in (3,4):
    nu=S.Rational(n,2)-1
    h=z*z-S.Rational(1,n)
    r=1+t*h
    k2,k3=S.symbols('k2 k3')
    delta=trunc((j+k2*t*t+k3*t**3)*r-j)
    powers=[S.Integer(1)]
    for power in range(1,4): powers.append(trunc(powers[-1]*delta))
    B={0:S.Integer(0),1:S.Integer(1)}
    for a in range(1,10): B[a+1]=S.expand(2*(nu+a)*B[a]/j-B[a-1])
    for a in range(0,-4,-1): B[a-1]=S.expand(2*(nu+a)*B[a]/j-B[a+1])
    def derivative(a,d):
        return sum((-1)**k*S.binomial(d,k)*B[a-d+2*k] for k in range(d+1))/2**d
    factor=sum(S.binomial(-nu,k)*t**k*h**k for k in range(4))
    amps={0:S.Integer(1)}
    for ell in (2,4,6): amps[ell]=sum(S.Symbol(f'a{ell}_{k}')*t**k for k in range(ell//2,4))
    boundary=0
    for ell,amp in amps.items():
        series=sum(derivative(ell,d)*powers[d]/S.factorial(d) for d in range(4))
        boundary+=trunc(amp*trunc(factor*series))*S.gegenbauer(ell,nu,z)
    boundary=trunc(boundary)
    solution={}
    for order in range(1,4):
        e=S.expand(boundary.subs(solution)).coeff(t,order)
        unknown=([k2] if order==2 else [k3] if order==3 else [])
        unknown += [S.Symbol(f'a{ell}_{order}') for ell in range(2,2*order+1,2)]
        sol=S.solve([e.coeff(z,k) for k in range(0,2*order+1,2)],unknown,dict=True)
        assert len(sol)==1
        solution.update({a:S.factor(v) for a,v in sol[0].items()})
    assert S.cancel(boundary.subs(solution))==0
    x=j*j/n; d=x-n; a=d+S.Rational(n-1,2)
    cubic=-x*x+S.Rational(2*n+3,3)*x-S.Rational(n*(n-1),6)
    m2=S.Rational(2*(n-1),n*n*(n+2))
    m3=S.Rational(8*(n-1)*(n-2),n**3*(n+2)*(n+4))
    assert S.cancel(solution[k2]-j*a*m2)==0
    assert S.cancel(solution[k3]-j*cubic*m3)==0
    results.append({'dimension':n,'k2':str(solution[k2]),'k3':str(solution[k3]),'boundary_jet_zero':True,'matches_general_hand_formula':True})
out={'status':'Finite dimensional exact consistency checks; not a universal proof', 'checks':results,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
