"""Independent exact function-value transfer versus polynomial transfer."""
from field_arithmetic import field
from transfer_experiment import T
import json

def run(p,r,steps):
 q=p**r;size,modulus,add,mul,powr=field(p,r)
 inv=[powr(x,q-2) for x in range(q)]
 def swap(x):return 1 if x==0 else 0 if x==1 else x
 op=[[swap(add[inv[z]][inv[x]]) for x in range(q)] for z in range(q)]
 w=list(range(q));h=[0]*q;h[1]=1;seq=[]
 for n in range(1,steps+1):
  moment=0
  for z in range(q):moment=add[moment][mul[z][w[z]]]
  actual=mul[(-1 if n%2 else 1)%p][moment]
  predicted=((-1)**(n+1)*h[q-2])%p
  assert actual==predicted,(q,n,actual,predicted)
  seq.append(actual)
  nw=[0]*q
  for z in range(q):
   for x in range(q):
    y=op[z][x];nw[y]=add[nw[y]][mul[w[z]][x]]
  w=nw;h=T(h,p,q)
 return {'q':q,'modulus':list(modulus),'coefficients':seq,'independent_methods_agree':True}

results=[run(p,r,30) for p,r in [(3,2),(3,3),(5,1),(5,2),(7,1),(7,2),(11,1)]]
assert results[3]['coefficients'][5]==0
for row in results[:2]:assert all(c==2 for c in row['coefficients'][1:])
print(json.dumps(results,indent=2))
