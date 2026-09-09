"""Exact modular checks; all arithmetic uses Python integers."""
from math import gcd

def mul(a,b,m):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%m for i in range(2) for j in range(2))
def matpow(a,n,m):
    b=(1,0,0,1)
    while n:
        if n&1:b=mul(b,a,m)
        a=mul(a,a,m);n//=2
    return b

def u(n,P,Q,m):return matpow((P,-Q,1,0),n,m)[2]

primes=[2,3,5,7,11,13,17,19]
checks=0
for P in range(-12,13):
 for Q in range(-12,13):
  D=P*P-4*Q
  for p in primes:
   for r in range(1,6):
    mod=p**r
    for t in [1,2,3,5,9]:
     delta=(u(t*p**(2*r),P,Q,mod)-u(t*p**(2*r-2),P,Q,mod))%mod
     assert delta*(p if D%p==0 else 1)%mod==0,(P,Q,p,r,t,delta)
     if r>=2: assert delta==0,(P,Q,p,r,t,delta)
     if r==1 and t==1 and D%p==0:assert delta%p==p-1,(P,Q,p,delta)
     checks+=1
print('PASS',checks,'local Lucas congruences and minimality witnesses')
