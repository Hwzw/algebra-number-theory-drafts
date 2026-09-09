"""Exact finite coefficient proof checks for precomputed Radu bounds."""
import sys,time,json,hashlib
from pathlib import Path
here=Path(__file__).resolve().parent
sys.path.insert(0,str(here/'vendor'))
from flint import nmod_poly
from certificates import cert,specifications

def euler(n,mod,stride=1):
    a=[0]*n;a[0]=1
    j=1
    while stride*j*(3*j-1)//2<n:
      for v in [stride*j*(3*j-1)//2,stride*j*(3*j+1)//2]:
        if v<n:a[v]=(-1)**j%mod
      j+=1
    return nmod_poly(a,mod)

def coefficients(k,n,mod):
    f=euler(n,mod)
    inv=f.inverse_series_trunc(n)
    h=inv.pow_trunc(3,n).mul_low(euler(n,mod,2),n)
    return inv.mul_low(h.pow_trunc(k,n),n)

if __name__=='__main__':
  rows=[cert(*spec) for spec in specifications()]
  # Reuse each (k,mod) series across residue families.
  results=[]
  groups={}
  for row in rows:groups.setdefault((row['k'],row['mod']),[]).append(row)
  for (k,mod),rr in groups.items():
    start=time.time();n=max(x['max_coefficient'] for x in rr)+1
    series=coefficients(k,n,mod)
    for row in rr:
      tested=[];fail=[]
      for t in row['P']:
        for j in range(row['bound']+1):
          i=row['m']*j+t;v=int(series[i]);tested.append(v)
          if v:fail.append([i,v])
      row.update(check_count=len(tested),failures=fail[:10],all_zero=not fail)
      results.append(row)
    print(json.dumps(dict(k=k,mod=mod,n=n,seconds=round(time.time()-start,3),all_zero=all(x['all_zero'] for x in rr))),flush=True)
    here.joinpath('check-results.json').write_text(json.dumps(results,indent=2)+'\n')
    if not all(x['all_zero'] for x in rr):raise AssertionError(rr)
