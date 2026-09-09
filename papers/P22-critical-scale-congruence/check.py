#!/usr/bin/env python3
"""Exact finite consistency checks for Henry Zweiman's critical-scale paper.
Uses only the Python standard library. The manuscript contains the general proofs.
F_4 uses u^2+u+1 and F_9 uses u^2-2 over its prime field.
"""
from pathlib import Path
from itertools import product
from functools import lru_cache
from fractions import Fraction
import json

class Field:
    def __init__(self,p,degree):
        self.p=p; self.q=p**degree; self.degree=degree
        n=next(i for i in range(2,p) if pow(i,(p-1)//2,p)==p-1) if degree==2 else 0
        self.n=n
        self.add=[[((a%p+b%p)%p)+p*((a//p+b//p)%p) for b in range(self.q)] for a in range(self.q)]
        self.neg=[((-a%p)%p)+p*((- (a//p))%p) for a in range(self.q)]
        self.mul=[[((a%p*(b%p)+n*(a//p)*(b//p))%p)+p*((a%p*(b//p)+(a//p)*(b%p))%p) for b in range(self.q)] for a in range(self.q)]
    def power(self,a,k):
        z=1
        while k:
            if k&1:z=self.mul[z][a]
            a=self.mul[a][a]; k//=2
        return z

class F4:
 def __init__(self):
  self.q=4;self.n=None
  self.add=[[a^b for b in range(4)] for a in range(4)];self.neg=list(range(4))
  self.mul=[[( ((a&1)*(b&1)+(a>>1)*(b>>1))%2 )+2*( ((a&1)*(b>>1)+(a>>1)*(b&1)+(a>>1)*(b>>1))%2 ) for b in range(4)] for a in range(4)]
 def power(self,a,n):
  v=1
  while n:
   if n&1:v=self.mul[v][a]
   a=self.mul[a][a];n//=2
  return v

class Ring:
 def __init__(self,p,e):self.F=F4() if (p,e)==(2,2) else Field(p,e);self.q=self.F.q
 def norm(self,a):
  a=list(a)
  while a and not a[-1]:a.pop()
  return tuple(a)
 def add(self,a,b):
  A=self.F.add
  return self.norm([A[a[i] if i<len(a) else 0][b[i] if i<len(b) else 0] for i in range(max(len(a),len(b)))])
 def neg(self,a):return tuple(self.F.neg[v] for v in a)
 def sub(self,a,b):return self.add(a,self.neg(b))
 @lru_cache(maxsize=100000)
 def mul(self,a,b):
  if not a or not b:return ()
  v=[0]*(len(a)+len(b)-1);A=self.F.add;M=self.F.mul
  for i,x in enumerate(a):
   for j,y in enumerate(b):v[i+j]=A[v[i+j]][M[x][y]]
  return self.norm(v)
 def power(self,a,n):
  b=(1,)
  while n:
   if n&1:b=self.mul(b,a)
   a=self.mul(a,a);n//=2
  return b
 def divmod(self,a,b):
  assert b
  r=list(a);out=[0]*max(0,len(a)-len(b)+1);inv=self.F.power(b[-1],self.q-2)
  while len(r)>=len(b):
   k=len(r)-len(b);v=self.F.mul[r[-1]][inv];out[k]=v
   for j,x in enumerate(b):r[k+j]=self.F.add[r[k+j]][self.F.neg[self.F.mul[v][x]]]
   r=list(self.norm(r))
  return self.norm(out),tuple(r)
 def quo(self,a,b):
  x,r=self.divmod(a,b);assert not r,(a,b,r)
  return x
 def values(self,N):return [self.norm(a) for a in product(range(self.q),repeat=N+1)]
 def tpower(self,n):return (0,)*n+(1,)
 def primes(self,N):
  out=[]
  for d in range(1,N+1):
   for coeff in product(range(self.q),repeat=d):
    P=tuple(coeff)+(1,)
    if all(self.divmod(P,Q)[1] for Q in out if 2*(len(Q)-1)<=d):out.append(P)
  return out
 def numerator(self,i,A):
  v=(1,)
  for B in self.values(i-1) if i else [()]:v=self.mul(v,self.sub(A,B))
  return v
 def E(self,i,A):return self.quo(self.numerator(i,A),self.numerator(i,self.tpower(i)))

def general_check(R,M):
 q=R.q;count=q**(M+1)
 def digits(n):
  out=[]
  while n:out.append(n%q);n//=q
  return tuple(out)
 xs=[digits(n) for n in range(count)];primes=R.primes(M)
 Pi=[(1,)]
 for m in range(1,M+1):
  v=(1,)
  for P in primes:
   if len(P)-1<=m:v=R.mul(v,P)
  Pi.append(v)
 B=[];prefix=[(1,)]*count
 for n in range(count):
  if n:
   for j in range(n,count):prefix[j]=R.mul(prefix[j],R.sub(xs[j],xs[n-1]))
  den=prefix[n]
  B.append([()]*n+[R.quo(prefix[j],den) for j in range(n,count)])
 def values(coeff):
  return [sum_poly(R,[R.mul(coeff[i],B[i][j]) for i in range(j+1)]) for j in range(count)]
 def CP(out):
  for P in primes:
   seen={}
   for x,y in zip(xs,out):
    a=R.divmod(x,P)[1];b=R.divmod(y,P)[1]
    if a in seen and seen[a]!=b:return False
    seen[a]=b
  return True
 coeff=[Pi[len(x)-1] if x else (1,) for x in xs]
 assert CP(values(coeff))
 defect=coeff.copy();defect[q**M]=R.add(defect[q**M],(1,));assert not CP(values(defect))
 delta=[(1,)]+[()]*(count-1);recovered=[]
 for n in range(count):
  v=R.sub(delta[n],sum_poly(R,[R.mul(recovered[i],B[i][n]) for i in range(n)]))
  recovered.append(v)
 for m in range(1,M+1):assert len(recovered[q**m])-1==(q**(m+1)-q)//(q-1)-m
 return {'domain_count':count,'prime_degree_limit':M,'Newton_basis_values':count*(count+1)//2,'positive_and_negative_congruence_models_pass':True,'delta_coefficients_recovered_directly':True}

def sum_poly(R,terms):
 v=()
 for x in terms:v=R.add(v,x)
 return v

def check(p,e,N):
 R=Ring(p,e);q=R.q;xs=R.values(N);primes=R.primes(N)
 H=[R.numerator(i,R.tpower(i)) for i in range(N+1)]
 Pi=[]
 for i in range(N+1):
  v=(1,)
  for P in primes:
   if len(P)-1<=i:v=R.mul(v,P)
  Pi.append(v)
 E=[[R.quo(R.numerator(i,A),H[i]) for A in xs] for i in range(N+1)]
 index={A:j for j,A in enumerate(xs)}
 basis_checks=0
 for i in range(N+1):
  assert len(H[i])-1==i*q**i
  for j in range(N+1):
   v=E[i][index[R.tpower(j)]]
   assert (not v if j<i else len(v)-1==(j-i)*q**i)
   basis_checks+=1
 def function(coeff):
  out=[]
  for k in range(len(xs)):
   a=()
   for i,c in enumerate(coeff):a=R.add(a,R.mul(c,E[i][k]))
   out.append(a)
  return out
 def recover(out):
  coeff=[]
  for n in range(N+1):
   a=out[index[R.tpower(n)]]
   for i,c in enumerate(coeff):a=R.sub(a,R.mul(c,E[i][index[R.tpower(n)]]))
   coeff.append(a)
  return coeff
 def CP(out):
  for P in primes:
   buckets={}
   for A,v in zip(xs,out):
    res=R.divmod(A,P)[1];val=R.divmod(v,P)[1]
    if res in buckets and buckets[res]!=val:return False
    buckets[res]=val
  return True
 models=[Pi,[(1,)]+[()]*N]
 for i in range(1,N+1):
  a=Pi.copy();a[i]=R.add(a[i],(1,));models.append(a)
 model_results=[]
 for coeff in models:
  out=function(coeff);assert recover(out)==coeff
  divisibility=all(not R.divmod(a,b)[1] for a,b in zip(coeff,Pi))
  preserves=CP(out);assert divisibility==preserves
  # Exact coefficient-transform bound, scaled to avoid rational arithmetic.
  for n,a in enumerate(coeff):
   alpha=len(a)-1 if a else -10**9
   rhs=q**n-1+max((q-1)*(len(out[index[R.tpower(j)]])-1)-(q**j-1) for j in range(n+1))
   assert (q-1)*alpha<=rhs
  model_results.append({'preserves_prime_congruences':preserves,'coefficient_criterion':divisibility})
 boundary=function(Pi)
 degrees=[]
 for n in range(N+1):
  dn=len(Pi[n])-1;v=boundary[index[R.tpower(n)]]
  maxdeg=max(len(y)-1 for A,y in zip(xs,boundary) if len(A)-1==n)
  assert maxdeg*(q-1)<=q*q**n
  degrees.append({'n':n,'d_n':dn,'degree_at_t_n':len(v)-1,'max_degree_on_shell':maxdeg})
 # General Newton coefficients for delta at zero, at n=q^m.
 newton=[]
 for m in range(1,N+1):
  A=R.tpower(m);numer=R.numerator(m,A);denom=A
  for B in R.values(m-1):
   if B:denom=R.mul(denom,R.neg(B))
  # Coefficient sign is irrelevant to degree; exact quotient is tested.
  coeff=R.quo(numer,denom)
  expected=(q**(m+1)-q)//(q-1)-m
  assert len(coeff)-1==expected
  newton.append({'m':m,'index':q**m,'coefficient_degree':expected,'d_m':len(Pi[m])-1})
 return {'q':q,'field':f'F_{p}' if e==1 else ('F_2[u]/(u^2+u+1)' if p==2 else f'F_{p}[u]/(u^2-{R.F.n})'),'N':N,'input_count':len(xs),'basis_values_checked':len(xs)*(N+1),'triangular_degree_checks':basis_checks,'models':model_results,'boundary_degrees':degrees,'general_newton_obstruction':newton,'general_Newton_check':general_check(R,2 if q==2 else 1),'all_pass':True}


def basis_check(p,e,s,D):
 R=Ring(p,e);q=R.q;xs=R.values(D);ps=R.primes(D)
 E=[[R.E(i,A) for A in xs] for i in range(s)]
 Pi=(1,)
 for P in ps:
  if len(P)-1<s:Pi=R.mul(Pi,P)
 height=Fraction(D-s)+Fraction(q+1,q-1)
 residues=[[R.divmod(A,P)[1] for A in xs] for P in ps]
 degrees=[];buckets=0;values=0
 for j in range(q**s):
  digits=[];v=j
  for i in range(s):digits.append(v%q);v//=q
  assert sum(a*q**i for i,a in enumerate(digits))==j
  ys=[]
  for k,A in enumerate(xs):
   y=Pi
   for i,a in enumerate(digits):y=R.mul(y,R.power(E[i][k],a))
   assert len(y)-1 < height*q**s
   if len(A)-1>=s-1:
    expected=len(Pi)-1+sum(a*(len(A)-1-i)*q**i for i,a in enumerate(digits))
    assert len(y)-1==expected
   ys.append(y);values+=1
  degrees.append(max(len(y)-1 for y in ys))
  for P,rs in zip(ps,residues):
   seen={}
   for y,r in zip(ys,rs):
    out=R.divmod(y,P)[1]
    if r in seen:assert seen[r]==out
    else:seen[r]=out
   buckets+=len(seen)
 return {'q':q,'s':s,'D':D,'basis_count':q**s,'input_count':len(xs),
         'literal_basis_value_checks':values,'prime_count':len(ps),
         'residue_buckets_checked':buckets,'max_value_degree':max(degrees),
         'strict_height_bound':str(height*q**s),'all_pass':True}

def parameter_check():
 count=0;recurrence=0
 for q in range(2,258):
  ell=1
  while q**ell<16:ell+=1
  kappa=Fraction(q+1,q-1);c=Fraction(1,16*q**(ell+1))
  assert ell<=4 and (ell+kappa)/q**ell<=Fraction(7,16)
  assert c>Fraction(1,256*q*q)
  J=4*q**(ell+1)
  assert J*c==Fraction(1,4)
  for M in range(ell+1,ell+12):
   s=M-ell;T=q**M//4
   assert (T+1)*q**s*(J+1)>q**(2*M+1)
   for r in range(20):
    bound=Fraction(1,4*q**r)+Fraction(r+ell+kappa,q**(ell+r))+Fraction(1,4)
    assert bound<=Fraction(15,16)
    D=M+r
    direct=sum((q-1)*(D-i)*q**i for i in range(s))
    closed=(Fraction(D-s)+Fraction(q,q-1))*q**s-D-Fraction(q,q-1)
    assert direct==closed
    count+=1
   recurrence+=1
 return {'integer_q_range':[2,257],'height_and_propagation_cases':count,
         'dimension_inequality_cases':recurrence,'all_pass':True}


if __name__=='__main__':
 result={'purpose':'Exact consistency checks; no finite computation proves the infinite growth theorem.',
         'parameter_checks':parameter_check(),'digit_basis':[],'additive_and_Newton':[]}
 print(json.dumps(result['parameter_checks']),flush=True)
 for args in [(2,1,3,4),(3,1,2,3),(2,2,2,2),(3,2,1,2)]:
  row=basis_check(*args);result['digit_basis'].append(row);print(json.dumps(row),flush=True)
 for args in [(2,1,4),(3,1,3),(2,2,2),(3,2,2)]:
  row=check(*args);result['additive_and_Newton'].append(row);print(json.dumps(row),flush=True)
 result['all_pass']=True
 Path(__file__).with_name('check-results.json').write_text(json.dumps(result,indent=2)+'\n')
