"""Exact sanity checks for the proof. No finite check substitutes for the theorem."""
from pathlib import Path
import json
import sympy as s

x=s.symbols('x')
records=[]
for d,a in [(4,2),(4,4),(4,64),(8,4),(12,4)]:
 D=a**d-a
 f=x**d-D
 g=x**d+a
 H=s.Poly(s.expand(f.subs(x,g)),x)
 _, factors=s.factor_list(H.as_expr())
 assert len(factors)==1 and factors[0][1]==1
 def fval(y):return y**d-D
 def gval(y):return y**d+a
 for t in range(-6,7):
  y=gval(gval(t));b=y**(d//2)
  assert (b-1)**2<fval(y)<b*b
 records.append({'d':d,'a':a,'fg_degree':H.degree(),'fg_irreducible':True,'g_factor_degrees':[int(s.degree(p)) for p,e in s.factor_list(g)[1]],'square_gap_inputs':[-6,6]})
Path(__file__).with_name('prefix_checks.json').write_text(json.dumps(records,indent=2))
print(json.dumps(records,indent=2))
