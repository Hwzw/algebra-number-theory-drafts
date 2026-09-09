"""Independent finite diagnostics for Q32; no finite computation proves the theorem."""
from itertools import product
from math import lcm,gcd
from pathlib import Path
import json,time

def add(g,h,ns): return tuple((x+y)%n for x,y,n in zip(g,h,ns))
def neg(g,ns): return tuple(-x%n for x,n in zip(g,ns))
def order(g,ns): return lcm(*(n//gcd(x,n) for x,n in zip(g,ns)))
def is_atom(seq,ns):
 z=(0,)*len(ns)
 total=z
 for g in seq: total=add(total,g,ns)
 if total!=z:return False
 sums={z}
 for g in seq[:-1]:
  new={add(s,g,ns) for s in sums}
  if z in new:return False
  sums |=new
 return True

def reps(x,n):
 x%=n
 return (0,) if x==0 else (x,x-n)

def run(b,outside):
 ns=(2,)+(4,)*b+(8,) if outside else (4,)*b+(8,)
 offset=int(outside)
 f=(0,)*(len(ns)-1)+(1,)
 hs=[]
 for i in range(b):
  h=list(f);h[offset+i]=1;hs.append(tuple(h))
 base=set([f,neg(f,ns)]+hs+[neg(h,ns) for h in hs])
 counts={'b':b,'outside':outside,'elements':0,'witness_atoms':0,'all_constructed_atoms':0,'largest_witness_length':0}
 for g in product(*(range(n) for n in ns)):
  if order(g,ns)!=8 or (outside and g[0]!=1) or (not outside and g in base):continue
  counts['elements']+=1
  multiplier=2 if outside else 1
  found=False
  for aa in product(*(reps(multiplier*g[offset+i],4) for i in range(b))):
   for c in reps(multiplier*g[-1]-sum(aa),8):
    seq=[neg(g,ns)]*multiplier
    for h,a in zip(hs+[f],aa+(c,)):
     seq += [h if a>=0 else neg(h,ns)]*abs(a)
    assert is_atom(seq,ns),(b,outside,g,aa,c,seq)
    counts['all_constructed_atoms']+=1
    if len(seq)%3!=2:
     found=True;counts['witness_atoms']+=1
     counts['largest_witness_length']=max(counts['largest_witness_length'],len(seq))
  assert found,('No forbidden length witness',b,outside,g)
 return counts

if __name__=='__main__':
 start=time.time();results=[]
 for b in range(4):
  for outside in [False,True]:
   r=run(b,outside);results.append(r);print(r,flush=True)
 output={'status':'pass','scope':'All order-eight elements in C4^b+C8 and all order-eight elements outside K in C2+C4^b+C8, b=0..3; every constructed atom independently checked for minimality, and a length not congruent to 2 mod 3 found for every forbidden element.','results':results,'elapsed_seconds':time.time()-start,'limitation':'Finite diagnostics only; not a proof of the universal theorem.'}
 Path(__file__).with_name('check-results.json').write_text(json.dumps(output,indent=2)+'\n')
