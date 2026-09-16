"""Exact continuous weighted-Hilbert obstruction; all decisive checks use rationals."""
from pathlib import Path
import sympy as s,json,math
x,t=s.symbols('x t');R=s.Rational
centers=list(map(lambda k:R(k,100),[3,6,13,85,87,97]));masses=[1,1,1,1000,3000,5];eps=R(1,1000);background=R(1,100)
ends=sorted([R(0),R(1)]+[c+d for c in centers for d in [-eps,eps]])
pieces=[]
for l,r in zip(ends[:-1],ends[1:]):
 mid=(l+r)/2;rho=background+sum(R(w)/(2*eps) for c,w in zip(centers,masses) if c-eps<mid<c+eps);pieces.append((l,r,rho))
def integ_monom(k,l,r):return (r**(k+1)-l**(k+1))/(k+1)
mom=[sum(rho*integ_monom(k,l,r) for l,r,rho in pieces) for k in range(5)]
A=s.Matrix(3,3,lambda i,j:mom[i+j]);Ai=A.inv()
def primitive(k,p,z):
 return sum(s.binomial(p,j)*(-1)**j*x**(p-j)*z**(k+j+1)/R(k+j+1) for j in range(p+1))
def profile(l,r):
 vals=[]
 for k,p in [(0,2),(1,2),(2,2),(0,4)]:
  ans=0
  for a,b,rho in pieces:
   if b<=l:ans+=rho*(primitive(k,p,b)-primitive(k,p,a))
   elif a==l and b==r:ans+=rho*(primitive(k,p,x)-primitive(k,p,a))
  vals.append(s.expand(ans))
 b=s.Matrix(vals[:3]);return s.Poly(s.expand(vals[3]-(b.T*Ai*b)[0]),x)
def bernstein(poly,l,r):
 p=s.Poly(poly.as_expr().subs(x,l+(r-l)*t),t);d=p.degree();cs=[p.nth(k) for k in range(d+1)]
 return [sum(cs[k]*R(math.comb(i,k),math.comb(d,k)) for k in range(i+1)) for i in range(d+1)]
threshold=R(9,10000);certs=[]
def certify(poly,l,r,depth=0):
 bs=bernstein(s.Poly(threshold-poly.as_expr(),x),l,r)
 if min(bs)>0:certs.append({'left':str(l),'right':str(r),'minimum_bernstein_coefficient':str(min(bs))});return
 assert depth<20,(l,r)
 mid=(l+r)/2;certify(poly,l,mid,depth+1);certify(poly,mid,r,depth+1)
for i,(l,r,rho) in enumerate(pieces):
 poly=profile(l,r);certify(poly,l,r);print('profile segment',i,'certified',flush=True)
a=R(3,7);b=R(6,7)
# Two-switch load: H modulo P2 is (a-t)_+^2-(b-t)_+^2.
cut=sorted(set(ends+[a,b]));raw=0;bv=s.zeros(3,1)
for l,r in zip(cut[:-1],cut[1:]):
 mid=(l+r)/2;rho=next(w for c,d,w in pieces if c<=mid<=d)
 h=(a-t)**2 if mid<a else 0
 if mid<b:h-=(b-t)**2
 def integrate(expr):
  po=s.Poly(s.expand(expr),t);return sum(co*integ_monom(k[0],l,r) for k,co in po.terms())
 raw+=rho*integrate(h*h)
 for k in range(3):bv[k]+=rho*integrate(t**k*h)
J=s.factor(raw-(bv.T*Ai*bv)[0]);assert J>threshold
out={'date':'2026-09-16','order':3,'reciprocal_weight':{'background':str(background),'half_width':str(eps),'centers':[str(c) for c in centers],'rectangle_masses':masses},'switches':[str(a),str(b)],'threshold':str(threshold),'two_switch_dual_energy':str(J),'two_switch_decimal':float(J),'strict_margin':str(J-threshold),'all_one_switch_energies_strictly_below_threshold':True,'certificate_method':'Exact rational Bernstein positivity on a partition of every polynomial profile segment','certified_subintervals':certs,'moment_matrix_positive_definite':'rho >= 1/100 and monomials independent','scope':'Continuous positive bounded piecewise-constant derivative weight a=1/rho. This disproves the arbitrary-weight Hilbert norm identity, not the original constant-weight all-p conjecture.'}
Path(__file__).with_name('counterexample-certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('EXACT CERTIFICATE PASSED',len(certs),float(J),flush=True)
