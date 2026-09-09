#!/usr/bin/env python3
"""Exact finite diagnostics for the mixed-exponent proof; not its universal proof."""
import itertools as it
import json
import random
from pathlib import Path

rng = random.Random(35092026)

def vectors(p, n):
    return list(it.product(range(p), repeat=n))

def mv(M, x, p):
    return tuple(sum(a*b for a,b in zip(row,x)) % p for row in M)

def rank(M,p):
    a=[list(r) for r in M]; k=0
    for j in range(len(a[0])):
        i=next((i for i in range(k,len(a)) if a[i][j]%p),None)
        if i is None: continue
        a[k],a[i]=a[i],a[k]
        inv=pow(a[k][j],-1,p); a[k]=[(x*inv)%p for x in a[k]]
        for i in range(k+1,len(a)):
            c=a[i][j];a[i]=[(x-c*y)%p for x,y in zip(a[i],a[k])]
        k+=1
        if k==len(a): break
    return k

def root(p,l):
    return next(z for z in range(2,l) if pow(z,p,l)==1)

def add(out,key,val,l):
    out[key]=(out.get(key,0)+val)%l
    if not out[key]: del out[key]

def push(vec,M,p,l):
    out={}
    for (u,v),coef in vec.items():
        add(out,(mv(M,u,p*p),tuple(mv(M,c,p) for c in v)),coef,l)
    return out

def projector_basis(T,u,v,p,l):
    """Orbit character formula, separately checked against the full group sum."""
    n=len(u); a=tuple(x%p for x in u); z=root(p,l)
    if not any(a):
        return {(u,v):1} if not any(any(r) for r in T) else {}
    i=next(i for i,x in enumerate(a) if x)
    b=tuple(t*pow(a[i],-1,p)%p for t in T[i])
    if any(T[i][j]%p != a[i]*b[j]%p for i in range(n) for j in range(n)):
        return {}
    inv=pow(p**n,-1,l);out={}
    for w in vectors(p,n):
        exp=-sum(x*y for x,y in zip(b,w))%p
        key=(tuple((x+p*y)%(p*p) for x,y in zip(u,w)),v)
        add(out,key,inv*pow(z,exp,l),l)
    return out

def project(vec,T,p,l):
    out={}
    for (u,v),coef in vec.items():
        for key,c in projector_basis(T,u,v,p,l).items():add(out,key,coef*c,l)
    return out

def group_projector(T,u,v,p,l):
    n=len(u);z=root(p,l);out={};inv=pow(p**(n*n),-1,l)
    for flat in it.product(range(p),repeat=n*n):
        H=[flat[i*n:(i+1)*n] for i in range(n)]
        Hu=mv(H,u,p)
        tr=sum(T[i][j]*H[j][i] for i in range(n) for j in range(n))%p
        add(out,(tuple((x+p*y)%(p*p) for x,y in zip(u,Hu)),v),inv*pow(z,(-tr)%p,l),l)
    return out

def check_projectors():
    count=0
    for p,l,n in [(2,3,3),(3,7,2)]:
        for _ in range(60):
            T=[[rng.randrange(p) for _ in range(n)] for _ in range(n)]
            u=tuple(rng.randrange(p*p) for _ in range(n))
            v=(tuple(rng.randrange(p) for _ in range(n)),)
            a=projector_basis(T,u,v,p,l);b=group_projector(T,u,v,p,l)
            assert a==b,(p,T,u)
            assert project(a,T,p,l)==a
            count+=1
    return count

def check_sandwiches():
    count=0
    for p,l,s in [(2,3,0),(2,3,1),(2,5,2),(3,7,0),(3,7,1),(5,11,0)]:
        n=s+3
        for a0 in [1,2]:
            T=[[0]*n for _ in range(n)];T[0][a0-1]=1
            for _ in range(16):
                m=n-a0
                U=[[rng.randrange(p*p) for _ in range(s)] for _ in range(m)]
                W=[[rng.randrange(p*p) for _ in range(m)] for _ in range(s)]
                M=[[int(i==j and i<a0) for j in range(n)] for i in range(n)]
                for i in range(m):
                    for j in range(m):M[a0+i][a0+j]=sum(U[i][k]*W[k][j] for k in range(s))%(p*p)
                u=(rng.randrange(1,p),)+(0,)*(n-1)
                v=tuple(tuple(rng.randrange(p) for _ in range(n)) for _ in range(s))
                E=projector_basis(T,u,v,p,l)
                lhs=project(push(E,M,p,l),T,p,l)
                rhs=projector_basis(T,u,tuple(mv(M,c,p) for c in v),p,l)
                assert lhs==rhs,(p,s,a0,M)
                count+=1
    return count

def check_zero_quotient():
    count=0
    for p,l,s in [(2,3,1),(3,7,1),(5,11,0)]:
        n=s+3;T=[[0]*n for _ in range(n)]
        for _ in range(60):
            M=[[rng.randrange(p*p) for _ in range(n)] for _ in range(n)]
            u=tuple(rng.randrange(p*p) for _ in range(n))
            if not any(x%p for x in u):u=(1,)+u[1:]
            v=tuple(tuple(rng.randrange(p) for _ in range(n)) for _ in range(s))
            lhs=project(push(projector_basis(T,u,v,p,l),M,p,l),T,p,l)
            lhs={key:c for key,c in lhs.items() if any(x%p for x in key[0])}
            u1=mv(M,u,p*p);v1=tuple(mv(M,c,p) for c in v)
            rhs=projector_basis(T,u1,v1,p,l) if any(x%p for x in u1) else {}
            assert lhs==rhs,(p,s,M,u)
            count+=1
    return count

def lower_value(M,p,l,s):
    """Evaluate Lambda(f composed M) from the actual function table definition."""
    n=s+2;z=root(p,l);total=0
    v=tuple(tuple(int(i==j) for i in range(n)) for j in range(2,n))
    if tuple(mv(M,c,p) for c in v)!=v:return 0
    for w in vectors(p,n):
        u=tuple((int(i==0)+p*w[i])%(p*p) for i in range(n))
        y=mv(M,u,p*p)
        if tuple(x%p for x in y)!=(1,)+(0,)*(n-1):continue
        value=pow(z,(y[1]//p)%p,l)
        total+=pow(z,(-w[1])%p,l)*value
    return total*pow(p**n,-1,l)%l

def check_lower():
    rows=[]
    for p,l,s,mode in [(2,3,0,'all_R'),(2,3,1,'all_R'),(3,7,1,'all_residues_one_lift'),(2,5,2,'targeted_and_random'),(5,11,1,'targeted_and_random')]:
        n=s+2;count=0;sing=0
        Id=[[int(i==j) for j in range(n)] for i in range(n)]
        assert lower_value(Id,p,l,s)==1
        if mode=='all_R':
            flats=it.product(range(p*p),repeat=n*n)
        elif mode=='all_residues_one_lift':
            flats=(tuple(x+p*rng.randrange(p) for x in flat) for flat in it.product(range(p),repeat=n*n))
        else:
            mats=[]
            # All residue choices for the free second column, with multiple carry lifts.
            for col in vectors(p,n):
                for _ in range(p):
                    M=[[int(i==j) if j!=1 else col[i] for j in range(n)] for i in range(n)]
                    mats.append(tuple(M[i][j]+p*rng.randrange(p) for i in range(n) for j in range(n)))
            mats.extend(tuple(rng.randrange(p*p) for _ in range(n*n)) for _ in range(400))
            flats=mats
        for flat in flats:
            M=[flat[i*n:(i+1)*n] for i in range(n)];count+=1
            if rank(M,p)==n:continue
            sing+=1
            assert lower_value(M,p,l,s)==0,(p,s,M)
        rows.append(dict(p=p,target_prime=l,s=s,mode=mode,matrices=count,singular_residue_matrices=sing,status='PASS'))
    return rows

if __name__=='__main__':
    out=dict(projector_definition_checks=check_projectors(),nonzero_sandwich_checks=check_sandwiches(),zero_character_quotient_checks=check_zero_quotient(),lower_obstruction=check_lower(),status='PASS',scope='Exact finite diagnostics only; the universal proof uses character orthogonality and the cited Kovacs theorem. No floating point arithmetic.')
    path=Path(__file__).with_name('check-results.json');path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
