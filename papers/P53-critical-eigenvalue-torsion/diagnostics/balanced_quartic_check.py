"""Symbolic jets for balanced degree-two deformations; not analytic proof."""
import hashlib
import json
from pathlib import Path
import sympy as S

root = Path(__file__).resolve().parent
n, s, b = S.symbols('n s b')
m2 = 1 / (2 * (n + 2))
m4 = 3 / (4 * (n + 2) * (n + 6))
N = S.factor(m4 - m2**2)
d2 = s/n - n
d4 = -n-2 + s*(n*(n+2)-s)/((n+2)*(n*(n+4)-2*s))
f02 = -(n-1)
f03 = n*(n-1)-s
f04 = (n-1)*(2*s-n*(n+1))
f22 = -(n-1)*d2-s+2*n
f23 = -(n-1)*f22+(3*n-1-s)*d2-4*n
f42 = -(n-1)*d4-s+4*(n+2)
a = d2 + (n-1)/2
A = S.factor(a*m2)
a4 = a-b
c = S.factor(-(A*(1+f02-d2)
               +(b*(f02-d2)+a4*d4)*N/m2
               +(f03/6-f22/2)*m4/m2))
B = S.factor(-(f02/2*(b*b*N+A*A+2*A*m2)
               +f03/2*(b*N+A*m2)+f04*m4/24
               -d2*A*m2-f22*(b*N+A*m2)-f23*m4/6
               +a4*(d4*b+f42/2)*N+c*d2*m2))
lam2 = 2*A
loglam4 = S.factor(2*B-A*A)
tor2 = (n+2)*(n-3)*m2/2
tor4 = S.factor((n+2)*(
    ((n-7)*b*b/2+(n*n-7*n+16)*b/2-3*(n-1)*(n-4)/4)*N
    +(48+n**3+10*n*n-27*n)*m4/24-3*n*(n-1)*m2*m2/4))
vol2 = n*(n-1)*m2/2
vol4 = n*(n-1)*b*b*N/2+n*(n-1)*(n-2)*b*N/2+n*(n-1)*(n-2)*(n-3)*m4/24
per2 = (n*n-n+2)*m2/2
per4 = S.factor((n-1)*(n-2)*b*b*N/2
    +(n-1)*(n-2)*(n-3)*b*N/2
    +(n-1)*(n-2)*(n-3)*(n-4)*m4/24
    +2*(n+2)*b*b*N+2*(n-3)*(n+1)*b*N
    +n*(n-3)*(n-4)*m4/6-(1-8*m2+16*m4)/8)

old = json.loads((root/'endpoint_expansion.json').read_text())
ob, oj, ot = S.symbols('b j t')
ol = S.sympify(old['lambda_normalized']).expand()
expected_loglam4 = (ol.coeff(ot,4)-ol.coeff(ot,2)**2/2).subs({ob:b/2,oj**2:s})/16
expected_tor4 = S.sympify(old['torsion_normalized']).expand().coeff(ot,4).subs(ob,b/2)/16
assert S.factor(loglam4.subs(n,2)-expected_loglam4)==0
assert S.factor(tor4.subs(n,2)-expected_tor4)==0
assert S.factor(per4.subs(n,2)-(b*b/S.Integer(16)-3*b/S.Integer(64)-S.Rational(1,32)))==0

qv = 2*(s/n-1)/(n+2)
qp = (4*(n-1)*s/n-2*n+6)/((n+2)*(3*n-1))
av = ((n+2)*qv-2)/n
bp = ((n+2)*qp-2)/(n-1)
cv = S.factor(loglam4+qv*(tor4-tor2**2/2)-av*(vol4-vol2**2/2))
cp = S.factor(loglam4+qp*(tor4-tor2**2/2)-bp*(per4-per2**2/2))
ef4 = 2*d4+2*(n-1)-3*(n+2)*qv
eg4 = 2*d4+n-1+(n+2)*qp*(n-7)/2-bp*(4*(n+2)+(n-1)*(n-2))/2
assert S.factor(S.diff(cv,b,2)-2*N*ef4)==0
assert S.factor(S.diff(cp,b,2)-2*N*eg4)==0
report = {'status':'Exact algebra diagnostics; hand derivation and analytic remainder are in note 0248',
          'deformation':'R=1+t*h+b*t^2*(h^2-m2), h=sum(first n/2 omega_i^2)-1/2',
          'm2':str(m2),'m4':str(m4),'degree_four_squared_norm':str(N),
          'planar_eigen_torsion_perimeter_agreement':True,
          'both_b_squared_coefficients_match_degree_four_hessian':True,
          'lambda_frequency_A':str(A),'lambda_frequency_B':str(B),
          'torsion_quartic':str(tor4),'perimeter_quartic':str(per4),
          'families':{}}
for label, coeff, qcrit in [('volume',cv,qv),('perimeter',cp,qp)]:
    bs = S.factor(-S.diff(coeff,b).subs(b,0)/S.diff(coeff,b,2))
    red = S.factor(coeff.subs(b,bs))
    num,den = S.fraction(red)
    constant = (-16*n**6*(n+2)*(n+4) if label=='volume' else
                -4*n**5*(n+2)*(n+4)*(9*n**3-6*n**2+49*n-36))
    assert S.factor(num.subs(s,0)-constant)==0
    report['families'][label]={'quartic':str(coeff),'stationary_b':str(bs),'reduced_quartic':str(red),
        'numerator_degree_in_s':int(S.degree(num,s)),'numerator_leading_coefficient':str(S.factor(S.Poly(num,s).LC())),
        'denominator':str(den),'numerator_constant_term':str(S.factor(num.subs(s,0)))}
report['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
(root/'balanced_quartic_check.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
