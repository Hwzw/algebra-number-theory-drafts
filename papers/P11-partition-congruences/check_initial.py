"""Independent exact-integer recurrence, no FLINT and no modular division."""
import json
from pathlib import Path

def exact_coefficients(k,N):
    sig=[0]*(N+1)
    for d in range(1,N+1):
      for n in range(d,N+1,d):sig[n]+=d
    b=[(3*k+1)*sig[j]-(2*k*sig[j//2] if j%2==0 else 0) for j in range(N+1)]
    a=[1]
    for n in range(1,N+1):
      v=sum(b[j]*a[n-j] for j in range(1,n+1))
      assert v%n==0
      a.append(v//n)
    return a
if __name__=='__main__':
 rows=[]
 for c in range(5):
   k=125*c+58;a=exact_coefficients(k,116)
   assert a[66]%3125==625*c*(c-2)%3125
   assert a[116]%3125==-625*c*(c-2)%3125
   rows.append(dict(c=c,k=k,n66=a[66],n116=a[116],r66=a[66]%3125,r116=a[116]%3125))
 Path(__file__).with_name('initial-checks.json').write_text(json.dumps(rows,indent=2)+'\n')
 print(json.dumps(rows,indent=2))
