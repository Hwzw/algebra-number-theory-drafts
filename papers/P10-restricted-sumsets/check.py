"""Exact checks of the interval family. No third-party dependencies."""
from pathlib import Path
import json

def interval(a,b):
    return set(range(a,b+1))

def family(k,N,U):
    A=interval(0,N+4*k-1)-(interval(k,2*k-1)|interval(U,U+2*k-1)|interval(N+2*k,N+3*k-1))
    B=interval(0,N-1)
    D=interval(0,4*k-1)|interval(U,U+2*k-1)|interval(U+N-1,U+N+2*k-2)|interval(2*N-1,2*N+4*k-2)
    return A,B,D

def check(k,N,U):
    assert k>=1 and N>=14*k and 8*k<=U<=N-6*k
    A,B,D=family(k,N,U)
    S={a+b for a in A for b in B}
    deg=[sum(a+b in D for a in A) for b in sorted(B)]
    assert len(A)==len(B)==N
    assert S==interval(0,2*N+4*k-2)
    assert max(deg)==3*k
    assert len(D)==12*k
    assert len(S-D)==2*N-8*k-1
    assert 2*N-1-15*k//2-len(S-D)==(k+1)//2
    return deg

if __name__=='__main__':
    triples=0
    for k in range(1,9):
        for N in range(14*k,14*k+21):
            for U in range(8*k,N-6*k+1):
                check(k,N,U);triples+=1
    witness={'k':1,'N':20,'U':14,'B_degrees':check(1,20,14),
             'restricted_size':31,'conjectured_lower_bound':32}
    report={'exact_parameter_triples_checked':triples,'all_passed':True,'witness':witness}
    Path(__file__).with_name('check-results.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))
