"""Exact algebra accompanying note 0244; not a PDE or transcendence proof."""
from pathlib import Path
import hashlib
import json
import sympy as S

n,x,q=S.symbols('n x q')
d=x-n
a=d+(n-1)/2
H2rr=-(n-1)*d-n*x+2*n
u0rrr=n*(n-1)-n*x
B=S.factor(-a*d+H2rr/2-u0rrr/6)
assert S.expand(B-(-x*x+(2*n+3)*x/3-n*(n-1)/6))==0
T2=(n+2)*(n-3)/2
T3=(n+2)*(n*n-5*n+12)/6
V2=n*(n-1)/2
V3=n*(n-1)*(n-2)/6
P2=(n*n-n+2)/2
P3=(n-3)*(n*n+2)/6
alpha=((n+2)*q-2)/n
beta=((n+2)*q-2)/(n-1)
qv=2*(x-1)/(n+2)
qp=(4*(n-1)*x-2*n+6)/((n+2)*(3*n-1))
F2=S.factor(2*a+q*T2-alpha*V2)
G2=S.factor(2*a+q*T2-beta*P2)
F3=S.factor((2*B+q*T3-alpha*V3).subs(q,qv))
G3=S.factor((2*B+q*T3-beta*P3).subs(q,qp))
assert S.cancel(F2.subs(q,qv))==0
assert S.cancel(G2.subs(q,qp))==0
assert S.Poly(F3,x).LC()==-2
assert S.cancel(S.Poly(G3,x).LC()+2)==0
# Sphere moments for h=omega_1^2-1/n, from normalized even moments.
m3=S.factor(15/(n*(n+2)*(n+4))-9/(n*n*(n+2))+2/n**3)
assert S.cancel(m3-8*(n-1)*(n-2)/(n**3*(n+2)*(n+4)))==0

# Planar perimeter calculation uses the already checked spectral/torsion jets.
root=Path(__file__).parent
old=json.loads((root/'endpoint_expansion.json').read_text())
j,b,t,z=S.symbols('j b t z')
r=1+t*(z**2+z**-2)/2+b*t*t*(z**4+z**-4)/2
dr=S.I*z*S.diff(r,z)
def trunc(e):
    return S.expand(sum(v*t**p[0] for p,v in S.Poly(S.expand(e),t).terms() if p[0]<=4))
e=trunc(r*r+dr*dr-1)
per=1
power=1
for k in range(1,5):
    power=trunc(power*e)
    per+=S.binomial(S.Rational(1,2),k)*power
per=S.factor(S.expand(per).coeff(z,0))
def logjet(e):
    e=S.expand(e)
    c2=e.coeff(t,2)
    return c2,S.factor(e.coeff(t,4)-c2*c2/2)
p2,p4=logjet(per)
l2,l4=logjet(S.sympify(old['lambda_normalized']))
t2,t4=logjet(S.sympify(old['torsion_normalized']))
g2=S.factor(l2+q*t2-(4*q-2)*p2)
qsharp=(j*j+1)/10
assert S.cancel(g2.subs(q,qsharp))==0
g4=S.factor((l4+q*t4-(4*q-2)*p4).subs(q,qsharp))
s,y=S.symbols('s y')
q0=35*s**4-510*s**3+2691*s*s-5560*s+1824
q1=35*s**4-390*s**3+1179*s*s-760*s+1056
assert S.cancel(g4.subs(b,0)-q0.subs(s,j*j)/(640*(6-j*j)))==0
assert S.cancel(g4.subs(b,1)-q1.subs(s,j*j)/(640*(6-j*j)))==0
shift0=S.Poly(S.expand(q0.subs(s,y+S.Rational(23,4))),y)
shift1=S.Poly(S.expand(q1.subs(s,y+S.Rational(23,4))),y)
assert all(c>0 for c in shift0.all_coeffs())
assert all(c>0 for c in shift1.all_coeffs()[:-1])
assert q1.subs(s,S.Rational(29,5))<0

out={
 'status':'Exact algebra checks only; hand proof and classical transcendence dependency are in note 0244',
 'notation':'x=j_(n/2-1,1)^2/n; coefficient formulas multiply mean(h^2) or mean(h^3)',
 'q_volume':str(qv),'q_perimeter':str(qp),
 'eigen_cubic_half_coefficient':str(B),
 'volume_quadratic':str(F2),'perimeter_quadratic':str(G2),
 'volume_critical_cubic':str(F3),'perimeter_critical_cubic':str(G3),
 'both_cubic_polynomials_leading_coefficient':-2,
 'chosen_h_third_moment':str(m3),
 'planar_perimeter_normalized':str(per),
 'planar_perimeter_critical_quartic':str(g4),
 'planar_Q0_shifted_at_23_over_4':str(shift0.as_expr()),
 'planar_Q1_shifted_at_23_over_4':str(shift1.as_expr()),
 'planar_Q1_at_29_over_5':str(q1.subs(s,S.Rational(29,5))),
 'planar_quartic_b0_positive_b1_negative':True,
 'source_diagnostic_sha256':hashlib.sha256((root/'endpoint_expansion.json').read_bytes()).hexdigest(),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
