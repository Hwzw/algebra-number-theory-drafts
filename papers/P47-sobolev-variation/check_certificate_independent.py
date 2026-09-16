"""Alternate exact verification by values and polynomial interpolation, not expansion."""
from pathlib import Path
from fractions import Fraction as F
import sympy as s,json,math
root=Path(__file__).resolve().parent;data=json.loads((root/'counterexample-certificate.json').read_text())
cs=[F(v) for v in data['reciprocal_weight']['centers']];ms=data['reciprocal_weight']['rectangle_masses'];e=F(data['reciprocal_weight']['half_width']);bg=F(data['reciprocal_weight']['background'])
# Integrate each rectangle separately, adding the constant background.
rects=[(F(0),F(1),bg)]+[(c-e,c+e,F(m)/(2*e)) for c,m in zip(cs,ms)]
def mon(k,l,r):return (r**(k+1)-l**(k+1))/F(k+1)
def moment(k):return sum(w*mon(k,l,r) for l,r,w in rects)
A=s.Matrix(3,3,lambda i,j:s.Rational(moment(i+j)));Ai=A.inv()
def mixed(k,a,p):
 out=F(0)
 for l,r,w in rects:
  r=min(r,a)
  if r>l:out+=w*sum(F(math.comb(p,j))*(-1)**j*a**(p-j)*mon(k+j,l,r) for j in range(p+1))
 return out
def D(a):
 b=s.Matrix([s.Rational(mixed(k,a,2)) for k in range(3)]);return s.Rational(mixed(0,a,4))-(b.T*Ai*b)[0]
# Profiles have degree <=10; 11 exact values determine them.
degree=10;V=s.Matrix([[s.Rational(i,degree)**j for j in range(degree+1)] for i in range(degree+1)]);Vi=V.inv();mins=[]
for row in data['certified_subintervals']:
 l=F(row['left']);r=F(row['right']);values=s.Matrix([s.Rational(data['threshold'])-D(l+(r-l)*F(i,degree)) for i in range(degree+1)]);powers=Vi*values
 bs=[sum(powers[k]*s.Rational(math.comb(i,k),math.comb(degree,k)) for k in range(i+1)) for i in range(degree+1)]
 # Degree elevation may change the minimum but preserves positivity.
 assert min(bs)>0
 lower=math.floor(F(row['minimum_bernstein_coefficient'])*10**9)
 assert min(bs)>=s.Rational(lower,10**9),(row,min(bs),lower)
 mins.append(str(min(bs)))
a,b=map(F,data['switches'])
# Cross term integrated on t<a, where both truncated powers are active.
cross=F(0)
for l,r,w in rects:
 r=min(r,a)
 if r<=l:continue
 cross+=w*sum(F(math.comb(2,i)*math.comb(2,j))*(-1)**(i+j)*a**(2-i)*b**(2-j)*mon(i+j,l,r) for i in range(3) for j in range(3))
bv=s.Matrix([s.Rational(mixed(k,a,2)-mixed(k,b,2)) for k in range(3)])
J=s.Rational(mixed(0,a,4)+mixed(0,b,4)-2*cross)-(bv.T*Ai*bv)[0]
assert J==s.Rational(data['two_switch_dual_energy']);assert J>s.Rational(967,10**6)
out={'passed':True,'method':'Exact integral evaluations at 11 rational points per interval, Vandermonde interpolation, degree10 Bernstein coefficients; separate exact mixed-kernel integration','subintervals':len(mins),'all_printed_lower_bounds_verified':True,'exact_two_switch_energy_matches':True,'two_switch_energy_gt_967_over_million':True,'independent_expert_review':False}
(root/'alternate-certificate-check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
