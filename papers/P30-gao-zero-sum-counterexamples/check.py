"""Exact finite diagnostics for the universal counterexample hand proof."""
from collections import deque
from itertools import product
from pathlib import Path
import hashlib,json,time

def add(g,h,m):return (g[0]^h[0],(g[1]+h[1])%m)
def neg(g,m):return (g[0],-g[1]%m)
def sums_and_zero(seq,m):
 sums={(0,0)};zero=False
 for g in seq:
  more={add(h,g,m) for h in sums}
  zero |= (0,0) in more
  sums |=more
 return sums,zero

def subgroup(gens,m):
 found={(0,0)};queue=deque(found)
 while queue:
  x=queue.popleft()
  for g in gens:
   y=add(x,g,m)
   if y not in found:found.add(y);queue.append(y)
 return found

def check(n):
 m=2*n;q=(n+1)//2
 T=[(0,1)]*(m-3)+[(v,q) for v in [1,2,4,7]]
 sums,zero=sums_and_zero(T,m)
 assert not zero
 group=set(product(range(8),range(m)))
 missing=group-sums
 predicted={(v,k) for v in [3,5,6] for k in [n-1,n]}
 assert missing==predicted,(n,missing,predicted)
 anchor=min(missing)
 H=subgroup([add(x,neg(anchor,m),m) for x in missing],m)
 assert anchor in H and len(H)==8*n
 S=T+[(3,n)]
 sums_s,zero_s=sums_and_zero(S,m)
 assert not zero_s and sums_s==group
 U=S+[(3,n+1)]
 total=(0,0)
 for g in U:total=add(total,g,m)
 assert total==(0,0) and len(U)==m+3
 # Since U has sum zero and deleting its last term is zero-sum free, U is an atom.
 return {'n':n,'group_order':16*n,'T_length':len(T),'distinct_nonempty_sums':len(sums)-1,'missing_elements':sorted(missing),'difference_subgroup_order':len(H),'anchor_in_difference_subgroup':True,'extremal_extension_length':len(S),'atom_length':len(U)}

if __name__=='__main__':
 start=time.time();rows=[check(n) for n in range(3,102,2)]
 # A separate brute-force enumeration in the smallest case, without the DP.
 T=[(0,1)]*3+[(v,2) for v in [1,2,4,7]]
 brute=set()
 for mask in range(1,1<<7):
  s=(0,0)
  for i,g in enumerate(T):
   if mask>>i&1:s=add(s,g,6)
  assert s!=(0,0);brute.add(s)
 assert len(brute)==41
 data={'status':'pass','universal_proof':'Hand proof in manuscript; finite checks are diagnostics only','parameters_checked':'Every odd n from 3 through 101 inclusive','cases':len(rows),'base_case_nonempty_subsequences_enumerated':127,'base_case_zero_subsequences':0,'results':rows,'elapsed_seconds':time.time()-start}
 Path(__file__).with_name('check-results.json').write_text(json.dumps(data,indent=2)+'\n')
 print('PASS',len(rows),'family cases; base case all 127 nonempty subsequences; exact holes, coset obstruction, extremal extension, and longest atom checked.')
