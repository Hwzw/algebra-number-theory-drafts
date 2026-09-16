"""Finite matrix diagnostics for note 0235; not a PDE proof or novelty test."""
import json
from pathlib import Path
import mpmath as mp
mp.mp.dps = 90
C=mp.matrix([[4,1,2],[1,3,-1],[2,-1,5]])
B=mp.matrix([[1,mp.mpf('0.2'),-1],[mp.mpf('0.2'),-1,mp.mpf('0.3')],[-1,mp.mpf('0.3'),2]])
orders=[1,1,3]
coeff=[(7+mp.sqrt(5))/2,(7-mp.sqrt(5))/2,mp.mpf(35)/11]
rows=[]
for sign in [0,1,-1]:
 for raw in ['0.01','0.003','0.001']:
  e=mp.mpf(raw); D=mp.diag([e**k for k in orders]); An=-D*(C+e*B)*D
  if sign:
   A=mp.matrix(4);A[0,0]=sign*2*e
   for i in range(3):
    A[0,i+1]=A[i+1,0]=(i+1)*e**(orders[i]+1)
    for j in range(3):A[i+1,j+1]=An[i,j]
  else:A=An
  n=A.rows
  G=mp.eye(n)
  for i in range(n):
   for j in range(n):G[i,j]+=e/(i+j+3)
  L=mp.cholesky(G);Li=L**-1
  eig=list(mp.eigsy(Li*A*Li.T,eigvals_only=True))
  if sign==1: ordinary=eig[-1];nodal=eig[:-1]
  elif sign==-1:ordinary=eig[0];nodal=eig[1:]
  else:ordinary=None;nodal=eig
  ratios=[nodal[i]/(-coeff[i]*e**(2*orders[i])) for i in range(3)]
  if sign:ratios.append(ordinary/(sign*2*e))
  # Finite convergence check at successively smaller parameters.
  error=max(abs(x-1) for x in ratios)
  rows.append({'nonnodal_sign':sign,'epsilon':raw,'ratios':[str(x) for x in ratios], 'max_relative_error':str(error)})
 for a,b in zip(rows[-3:-1],rows[-2:]):
  assert mp.mpf(b['max_relative_error'])<mp.mpf(a['max_relative_error'])
 assert mp.mpf(rows[-1]['max_relative_error'])<mp.mpf('0.01')
result={'purpose':'Finite diagnostics only; not a realization by a PDE eigenspace and not proof.', 'digits':mp.mp.dps,'nodal_orders':orders,'exact_schur_complement':'35/11','cases':rows,'all_checks_passed':True}
p=Path(__file__).with_name('multiscale-matrix-check.json');p.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'cases':len(rows),'all_checks_passed':True,'last_errors':[rows[i]['max_relative_error'] for i in [2,5,8]]},indent=2))
