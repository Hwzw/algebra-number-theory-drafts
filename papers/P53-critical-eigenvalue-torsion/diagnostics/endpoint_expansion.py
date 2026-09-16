"""Formal fourth-order diagnostic, not a PDE proof or a novelty certificate.

Boundary: r=1+t*cos(2 theta)+b*t^2*cos(4 theta).
Bessel recurrences are reduced at j=j_{0,1}. Output retains exact j.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

t, z, j, b, q = s.symbols('t z j b q', nonzero=True)
N = 4

def trunc(e):
    return s.expand(sum(v*t**p[0] for p,v in s.Poly(s.expand(e),t).terms() if p[0]<=N))

def cos(n):
    return (z**n+z**(-n))/2 if n else s.Integer(1)

def harmonic(e,n):
    return s.expand(e).coeff(z,n)*(2 if n else 1)

J = {0:s.Integer(0),1:s.Integer(1)}
for n in range(1,13):
    J[n+1]=s.expand(2*n*J[n]/j-J[n-1])

def bj(n):
    return J[n] if n>=0 else (-1)**(-n)*J[-n]

def derivative(n,d):
    return s.expand(sum((-1)**k*s.binomial(d,k)*bj(n-d+2*k) for k in range(d+1))/2**d)

r=1+t*cos(2)+b*t*t*cos(4)
k2,k4=s.symbols('k2 k4')
wave=j+k2*t*t+k4*t**4
delta=trunc(wave*r-j)
delta_powers=[s.Integer(1)]
for d in range(1,5):
    delta_powers.append(trunc(delta_powers[-1]*delta))

amplitudes={0:s.Integer(1)}
for n in (2,4,6,8):
    amplitudes[n]=sum(s.Symbol(f'a{n}_{d}')*t**d for d in range(n//2,5,2))
boundary=0
for n,a in amplitudes.items():
    series=sum(derivative(n,d)*delta_powers[d]/s.factorial(d) for d in range(5))
    boundary+=trunc(a*series)*cos(n)
boundary=trunc(boundary)
eigen_solution={}
for order in range(1,5):
    coeff=s.expand(boundary.subs(eigen_solution)).coeff(t,order)
    modes=list(range(0 if order%2==0 else 2,2*order+1,4))
    equations=[harmonic(coeff,n) for n in modes]
    unknown=([k2 if order==2 else k4] if order%2==0 else [])
    unknown += [s.Symbol(f'a{n}_{order}') for n in modes if n]
    solution=s.solve(equations,unknown,dict=True)
    assert len(solution)==1
    eigen_solution.update({x:s.factor(v) for x,v in solution[0].items()})
assert s.cancel(boundary.subs(eigen_solution))==0

# Torsion is (1-rho^2)/4 plus a harmonic polynomial through order four.
harmonics={}
for n in (0,2,4,6,8):
    harmonics[n]=sum(s.Symbol(f'c{n}_{d}')*t**d for d in range(max(1,n//2),5) if (d-n//2)%2==0)
torsion_boundary=(1-r*r)/4
for n,c in harmonics.items():
    torsion_boundary+=trunc(c*trunc(r**n))*cos(n)
torsion_boundary=trunc(torsion_boundary)
torsion_solution={}
for order in range(1,5):
    coeff=s.expand(torsion_boundary.subs(torsion_solution)).coeff(t,order)
    modes=list(range(0 if order%2==0 else 2,2*order+1,4))
    unknown=[s.Symbol(f'c{n}_{order}') for n in modes]
    solution=s.solve([harmonic(coeff,n) for n in modes],unknown,dict=True)
    assert len(solution)==1
    torsion_solution.update({x:s.factor(v) for x,v in solution[0].items()})
assert s.expand(torsion_boundary.subs(torsion_solution))==0
integral=trunc(r*r/8-r**4/16)
for n,c in harmonics.items():
    integral+=trunc(c.subs(torsion_solution)*trunc(r**(n+2)))*cos(n)/(n+2)
Tnorm=s.factor(16*harmonic(trunc(integral),0))
Anorm=s.factor(harmonic(trunc(r*r),0))
Lnorm=trunc(wave.subs(eigen_solution)**2/j**2)

def log_coeffs(e):
    c2=s.factor(s.expand(e).coeff(t,2))
    c4=s.factor(s.expand(e).coeff(t,4))
    assert s.expand(e).coeff(t,0)==1
    return c2,s.factor(c4-c2*c2/2)

L2,L4=log_coeffs(Lnorm)
T2,T4=log_coeffs(Tnorm)
A2,A4=log_coeffs(Anorm)
F2=s.factor(L2+q*T2-(2*q-1)*A2)
F4=s.factor(L4+q*T4-(2*q-1)*A4)
qstar=j*j/4-s.Rational(1,2)
assert s.simplify(F2.subs(q,qstar))==0
critical=s.factor(F4.subs(q,qstar))
bcrit=s.solve(s.diff(critical,b),b)[0]
reduced=s.factor(critical.subs(b,bcrit))
x,y=s.symbols('x y')
p0=7*x**4-102*x**3+555*x**2-1280*x+768
p1=7*x**4-78*x**3+195*x**2+256*x-768
assert s.simplify(critical.subs(b,0)-p0.subs(x,j*j)/(128*(6-j*j)))==0
assert s.simplify(critical.subs(b,1)-p1.subs(x,j*j)/(128*(6-j*j)))==0
shift0=s.Poly(s.expand(p0.subs(x,y+s.Rational(23,4))),y)
shift1=s.Poly(s.expand(p1.subs(x,y+s.Rational(23,4))),y)
assert all(c>0 for c in shift0.all_coeffs())
assert all(c>0 for c in shift1.all_coeffs()[:-1])
assert p1.subs(x,s.Rational(29,5))<0
lower=sum((-1)**k*s.Rational(23,16)**k/s.factorial(k)**2 for k in range(6))
upper=sum((-1)**k*s.Rational(29,20)**k/s.factorial(k)**2 for k in range(5))
assert lower>0 and upper<0
out={
 'status':'Formal symbolic diagnostic only; analytic remainder and sign proof not supplied by this script',
 'boundary':'r=1+t*cos(2 theta)+b*t^2*cos(4 theta)',
 'bessel_zero':'j=j_{0,1}',
 'q_star':str(qstar),
 'eigen_solution':{str(k):str(v) for k,v in eigen_solution.items()},
 'torsion_solution':{str(k):str(v) for k,v in torsion_solution.items()},
 'lambda_normalized':str(s.factor(Lnorm)),
 'torsion_normalized':str(Tnorm),
 'area_normalized':str(Anorm),
 'log_F_t2':str(F2),
 'log_F_t4':str(F4),
 'critical_quartic':str(critical),
 'stationary_b':str(s.factor(bcrit)),
 'reduced_quartic':str(reduced),
 'bessel_boundary_residual_zero_through_order_4':True,
 'torsion_boundary_residual_zero_through_order_4':True,
 'critical_quadratic_coefficient_zero':True,
 'sign_certificate':{
  'method':'Rational Bessel alternating-series bounds and shifted polynomials; analytic justification in note 0242',
  'j_squared_interval':['23/4','29/5'],
  'J0_lower_at_sqrt_23_over_4':str(lower),
  'J0_upper_at_sqrt_29_over_5':str(upper),
  'P0_shifted_at_23_over_4':str(shift0.as_expr()),
  'P1_shifted_at_23_over_4':str(shift1.as_expr()),
  'P1_at_29_over_5':str(p1.subs(x,s.Rational(29,5))),
  'quartic_b0_positive':True,
  'quartic_b1_negative':True,
 },
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
