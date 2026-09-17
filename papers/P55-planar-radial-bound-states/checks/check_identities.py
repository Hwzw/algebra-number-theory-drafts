"""Exact algebra checks. These are not a proof of the shooting theorem."""
import sympy as s

p, x, y = s.symbols('p x y', real=True)
g = (x/(p+1)-s.Rational(1,2))/(x-1)
derivative = s.factor(g+(p-1)*x*s.diff(g,x))
positive_form = (2*y**2+p*(p-1)*y+(p-1)**2*(p+1)/2)/(2*(p+1)*(x-1)**2)
assert s.simplify(derivative-positive_form.subs(y,x-(p+1)/2)) == 0

r, q, F, f, R, Rp = s.symbols('r q F f R Rp', nonzero=True)
rs, qs = -r/q, -r*r*f/q
Q = 4*R*q-q*q-2*r*r*F
Qs = s.diff(Q,r)*rs+s.diff(Q,q)*qs+s.diff(Q,F)*f+s.diff(Q,R)*Rp
assert s.simplify((Qs-4*Rp*q).subs(R,F/f)) == 0
W2 = q*q+2*r*r*F
W2s = s.diff(W2,r)*rs+s.diff(W2,q)*qs+s.diff(W2,F)*f
assert s.simplify(W2s+4*r*r*F/q) == 0

t, a = s.symbols('t a', positive=True)
# Write -2F=a>=0, t^2>a on the positive-energy branch.
h = a/(t*s.sqrt(t*t-a))
assert s.simplify(s.diff(h,t)+a*(2*t*t-a)/(t*t*(t*t-a)**s.Rational(3,2))) == 0
u, up, upp, eta = s.symbols('u up upp eta', positive=True)
weighted_energy_derivative = 2*r*(up*up/2+F)+r*r*(up*upp+f*up)
assert s.simplify(weighted_energy_derivative.subs(upp,-up/r-f)-2*r*F) == 0
# y=sqrt(r)*(u-1), A=f(u)/(u-1).
y_second = s.sqrt(r)*upp+up/s.sqrt(r)-(u-1)/(4*r**s.Rational(3,2))
y_equation = y_second+(f/(u-1)+1/(4*r*r))*s.sqrt(r)*(u-1)
assert s.simplify(y_equation.subs(upp,-up/r-f)) == 0
eta_derivative = (-upp/u+up*up/u**2).subs(upp,-up/r-u**p+u).subs(up,-eta*u)
assert s.simplify(eta_derivative-(eta**2-eta/r-1+u**(p-1))) == 0
print('PASS: seven identities: power derivative; Q; W^2; h; weighted energy; oscillation transform; Riccati.')
print('No ODE existence, comparison, or uniqueness theorem is certified by this script.')
