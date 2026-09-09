"""Exact modular checks supporting P02 extension; not a proof."""
from itertools import product
import json
from pathlib import Path

def mul(a,b,q):
    return [[sum(x*y for x,y in zip(row,col))%q for col in zip(*b)] for row in a]
def power(a,n,q):
    z=[[int(i==j) for j in range(len(a))] for i in range(len(a))]
    while n:
        if n&1:z=mul(z,a,q)
        a=mul(a,a,q);n//=2
    return z

# Companion of (x-2)(x-4)(x-6), with u_n=e1*T^(n-1)*v.
t=[[0,1,0],[0,0,1],[48,-44,12]]
v=[0,1,1]
records=[]
for p,r,s,m in product([2,3,5,7,11],[1,2,3,4,5,6],[1,2,3],[1,2,3,5,7]):
    if m%p==0:continue
    q=p**r;n1=(m*p**r)**s;n0=(m*p**(r-1))**s
    cmat=4 if s==1 else 2
    crec=12 if s==1 else 6
    a,b=power(t,n1,q),power(t,n0,q)
    assert all(cmat*(a[i][j]-b[i][j])%q==0 for i,j in product(range(3),repeat=2))
    a,b=power(t,n1-1,q),power(t,n0-1,q)
    assert all(crec*(x-y)%q==0 for x,y in zip(a[0],b[0]))
    records.append((p,r,s,m))
witnesses=[]
for p,r in [(2,2),(3,1)]:
    a,b=power(t,p**r-1,p),power(t,p**(r-1)-1,p)
    value=sum((x-y)*z for x,y,z in zip(a[0],b[0],v))%p
    assert value
    witnesses.append({'prime':p,'level':r,'difference_mod_p':value})
result={'local_instances':len(records),'matrix_repairs':{'s=1':4,'s=2,3':2},'uniform_recurrence_repairs':{'s=1':12,'s=2,3':6},'initial_vector_attaining_12_at_s1':v,'witnesses':witnesses,'passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
