"""Exact checks: reciprocity, trigonometric reduction, and Sturm zero counts."""
import itertools,json,time
from pathlib import Path
import sympy as s
x,y,w=s.symbols('x y w')
rows=[]; identities=0; start=time.time()
expected=[2,8,22,54,126,308,660,1538,3350,7368]
for b in range(10):
 d=2*b+1; m=b+1; total=0
 for eps in itertools.product([-1,1],repeat=b):
  a=[0]*(d+1); a[d]=1
  for k,e in enumerate(eps): a[b+1+k]=(e+1)//2; a[b-k]=1-a[b+1+k]
  p=s.Poly(1-(1-x)*sum(a[j]*x**j for j in range(1,d+1)),x)
  assert p.all_coeffs()==list(reversed(p.all_coeffs()))
  assert p.eval(1)==1 and p.eval(-1)%2==1
  # x^(-m)p(x)=p_m+sum_{j>=1}p_{m+j}(x^j+x^-j).
  c=[s.Integer(2),y]
  for j in range(2,m+1): c.append(s.expand(y*c[-1]-c[-2]))
  q=s.Poly(p.nth(m)+sum(p.nth(m+j)*c[j] for j in range(1,m+1)),y)
  assert s.expand(x**m*q.as_expr().subs(y,x+1/x)-p.as_expr())==0
  # Squarefree decomposition explicitly retains multiplicities.
  u=2*sum(mult*f.count_roots(-2,2) for f,mult in q.sqf_list()[1])
  total+=int(u)
  # Exact Laurent identity with theta=pi-2t, w=e^(it).
  # H=cos(t)(R+D); T=-2H.
  if b<=5:
   cos=lambda j:(w**j+w**(-j))/2
   H=sum((-1)**k*eps[k]*cos(1)*cos(2*k+1) for k in range(b))
   H+=(-1)**b*(cos(1)*cos(2*b+1)+cos(2*b+2)/2)
   T=(-w**-2)**(-m)*p.as_expr().subs(x,-w**-2)
   assert s.expand(T+2*H)==0
   identities+=1
 rows.append({'b':b,'maximum_S':d,'degree':2*b+2,'polynomials':2**b,'unit_circle_zeros':total,'expected':expected[b],'fraction':total/(2**b*(2*b+2))})
 assert total==expected[b],rows[-1]
 print(rows[-1],flush=True)
out={'method':'exact rational polynomial identities and squarefree Sturm counts including multiplicity','laurent_identities':identities,'cases':rows,'all_passed':True,'elapsed_seconds':time.time()-start}
Path(__file__).with_name('check-results.json').write_text(json.dumps(out,indent=2)+'\n')
