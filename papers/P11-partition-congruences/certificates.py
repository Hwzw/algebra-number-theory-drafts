"""Construct exact Radu certificates; no infinite claim without all checks passing."""
from fractions import Fraction as F
from math import gcd,ceil,floor
import json
from pathlib import Path

def cert(k,m,t,s):
    mod=5**s
    # An exact congruent eta product: f1^mod = f5^(mod/5) mod mod.
    lift=(3*k+mod)//mod
    r={1:mod*lift-3*k-1,2:k,5:-mod//5*lift,10:0}
    N=10
    kap=gcd(m*m-1,24)
    sig=sum(d*x for d,x in r.items())
    assert sig==-k-1
    assert (kap*N*sum(x*(m*N//d) for d,x in r.items()))%24==0
    assert (kap*N*sum(r.values()))%8==0
    assert N%(24*m//gcd(kap*(-24*t-sig),24*m))==0
    squares={a*a%(24*m) for a in range(24*m) if gcd(a,24*m)==1}
    P=sorted({(t*a+(a-1)//24*sig)%m for a in squares})
    vals={c:min(sum(F(x*gcd(d*(1+kap*l*c),m*c)**2,d*m) for d,x in r.items()) for l in range(m)) for c in [1,2,5,10]}
    a=(m*(5*k+2)+49)//50
    expected={1:-F(m*(5*k+2),50),2:-F(m*(k+1),25),5:-F(5*k+2,2*m),10:-F(k+1,m)}
    assert vals==expected
    assert a==max(0,ceil(-min(vals.values())))
    nu=F((sum(r.values())+a)*18-a,24)-F(sig,24*m)-F(min(P),m)
    return dict(k=k,m=m,t=t,s=s,mod=mod,r=r,N=N,P=P,lower24={str(c):str(v) for c,v in vals.items()},aux={1:a},nu=str(nu),bound=floor(nu),max_coefficient=m*floor(nu)+max(P))

def specifications():
    """Single authoritative manifest of the 35 proved base cases."""
    families=[(58,25,16,3),(83,125,41,3),(100,125,124,3),
              (5,125,69,3),(30,125,69,3),(60,125,14,3),
              (60,125,89,3),(58,125,91,4),(58,125,66,4)]
    return ([(k+125*c,m,t,s) for k,m,t,s in families for c in range(s)]
            +[(k+625*c,125,66,5) for k in [58,308] for c in range(3)])

if __name__=='__main__':
    rows=[cert(*spec) for spec in specifications()]
    Path(__file__).with_name('certificates.json').write_text(json.dumps(rows,indent=2)+'\n')
    print(json.dumps(dict(certificates=len(rows),maximum_index=max(x['max_coefficient'] for x in rows))))
