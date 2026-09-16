"""Separate finite modal boundary calculation in dimensions four and six."""
import hashlib
import json
from pathlib import Path
import sympy as S

root=Path(__file__).resolve().parent
t,y,z,s,b=S.symbols('t y z s b')
target=json.loads((root/'balanced_quartic_check.json').read_text())
nn=S.Symbol('n')
rows=[]
for n in (4,6):
    alpha=S.Rational(n,4)-1
    angular=[]
    for degree in range(5):
        poly=S.jacobi(degree,alpha,alpha,2*y).expand()
        angular.append(S.factor(poly/S.Poly(poly,y).LC()))
    Q=angular[2]
    A,B=S.symbols('A B')
    amps=S.symbols('a11 a22 a13 a33 a24 a44')
    a11,a22,a13,a33,a24,a44=amps
    shift=t*y+t*t*(b*Q+A)+t**3*A*y+t**4*(B+A*b*Q)
    def trunc(expr):
        return S.Poly(S.expand(expr),t).as_dict()
    powers=[{(0,):S.Integer(1)}]
    for degree in range(1,5):
        terms={}
        for (i,),v in powers[-1].items():
            for (j,),w in trunc(shift).items():
                if i+j<=4:terms[(i+j,)]=terms.get((i+j,),0)+v*w
        powers.append(terms)
    cprev=S.Integer(n)
    dns={1:1-cprev}
    for ell in range(2,9):
        cprev=S.factor(n+2*ell-2-s/cprev)
        dns[ell]=ell-cprev
    def radial_jet(ell,order):
        coeff=[S.Integer(0),S.Integer(1)] if ell==0 else [S.Integer(1),dns[ell]]
        for degree in range(order-1):
            nextc=S.Symbol('nextc')
            f=sum(coeff[j]*z**j for j in range(len(coeff)))+nextc*z**(degree+2)
            ode=((1+z)**2*S.diff(f,z,2)+(n-1)*(1+z)*S.diff(f,z)
                 +(s*(1+z)**2-ell*(ell+n-2))*f)
            coeff.append(S.factor(S.solve(S.expand(ode).coeff(z,degree),nextc)[0]))
        return coeff[:order+1]
    boundary=0
    for start,amp,degree in [(0,1,0),(1,a11,1),(2,a22,2),(3,a13,1),(3,a33,3),(4,a24,2),(4,a44,4)]:
        jet=radial_jet(2*degree,4-start)
        for derivative,coefficient in enumerate(jet):
            for (power,),value in powers[derivative].items():
                if power+start<=4:
                    boundary+=amp*angular[degree]*coefficient*value*t**(power+start)
    solved={}
    for order,unknowns in [(1,[a11]),(2,[A,a22]),(3,[a13,a33]),(4,[B,a24,a44])]:
        residual=S.Poly(S.expand(boundary).coeff(t,order).subs(solved).expand(),y)
        solution=S.solve(residual.all_coeffs(),unknowns,dict=True)[0]
        solved.update({key:S.factor(value) for key,value in solution.items()})
        assert all(S.factor(value.subs(solved))==0 for value in residual.all_coeffs())
    expected_A=S.sympify(target['lambda_frequency_A']).subs(nn,n)
    expected_B=S.sympify(target['lambda_frequency_B']).subs(nn,n)
    assert S.factor(solved[A]-expected_A)==0
    assert S.factor(solved[B]-expected_B)==0
    rows.append({'dimension':n,'all_boundary_modes_zero_through_order_four':True,
                 'frequency_A_matches_general_formula':True,'frequency_B_matches_general_formula':True})
    print(json.dumps(rows[-1]),flush=True)
report={'status':'Finite exact checks; not a universal proof or independent review',
        'checks':rows,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(root/'balanced_modal_check.json').write_text(json.dumps(report,indent=2)+'\n')
