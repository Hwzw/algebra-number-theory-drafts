"""Exact diagnostic checks; these finite checks do not prove the theorem."""
from itertools import product
from pathlib import Path
import json, random


def rank(cols, p, n=None):
    if not cols: return 0
    a=[list(v) for v in zip(*cols)];h=0
    for j in range(len(cols)):
        i=next((i for i in range(h,len(a)) if a[i][j]%p),None)
        if i is None: continue
        a[h],a[i]=a[i],a[h];u=pow(a[h][j]%p,-1,p)
        a[h]=[(x*u)%p for x in a[h]]
        for i in range(h+1,len(a)):
            u=a[i][j];a[i]=[(x-u*y)%p for x,y in zip(a[i],a[h])]
        h+=1
        if h==len(a):break
    return h


def independent(cols,p):
    b=[]
    for c in cols:
        if rank(b+[c],p)>len(b):b.append(c)
    return b


def kernel(rows,p,ncols):
    a=[list(r) for r in rows];h=0;piv=[]
    for j in range(ncols):
        i=next((i for i in range(h,len(a)) if a[i][j]%p),None)
        if i is None:continue
        a[h],a[i]=a[i],a[h];u=pow(a[h][j]%p,-1,p)
        a[h]=[(x*u)%p for x in a[h]]
        for i in range(len(a)):
            if i!=h:
                u=a[i][j];a[i]=[(x-u*y)%p for x,y in zip(a[i],a[h])]
        piv.append(j);h+=1
        if h==len(a):break
    out=[]
    for j in range(ncols):
        if j not in piv:
            v=[0]*ncols;v[j]=1
            for i,c in enumerate(piv):v[c]=-a[i][j]%p
            out.append(v)
    return out


def mv(cols,v,p):
    return [sum(c[i]*x for c,x in zip(cols,v))%p for i in range(len(cols[0]))]


def unit(n,j):return [int(i==j) for i in range(n)]


def partial_decomposition(cols,n,r,p):
    us=[[unit(n,j) for j in range(r)]]
    while True:
        uj=us[-1]
        mat=[[cols[j][i] for j in range(r)]+[-v[i]%p for v in uj] for i in range(n)]
        new=independent([v[:r]+[0]*(n-r) for v in kernel(mat,p,r+len(uj))],p)
        if len(new)==len(uj):break
        us.append(new)
    reg=us[-1];chains=[]
    for j in reversed(range(len(us)-1)):
        propagated=[chain[len(chain)-2-j] for chain in chains]
        span=us[j+1]+propagated
        assert rank(span,p)==len(span)
        for v in us[j]:
            if rank(span+[v],p)>len(span):
                chain=[v]
                for _ in range(j+1):
                    assert not any(chain[-1][r:])
                    chain.append(mv(cols,chain[-1][:r],p))
                chains.append(chain);span.append(v)
        assert rank(span,p)==len(us[j])
    allcols=reg+[v for chain in chains for v in chain]
    assert rank(allcols,p)==len(allcols)
    observed=reg+[v for chain in chains for v in chain[:-1]]
    assert len(observed)==r and rank(observed,p)==r
    assert not any(v[r:]!=[0]*(n-r) for v in observed)
    for v in reg:
        assert rank(reg+[mv(cols,v[:r],p)],p)==len(reg)
    for chain in chains:
        for v,w in zip(chain,chain[1:]):assert mv(cols,v[:r],p)==w
    a=len(reg);c=len(chains);z=n-r-c
    assert z>=0 and c<=r-a
    return a,c,z


def mm(a,b,p):
    return [[sum(x*y for x,y in zip(row,col))%p for col in zip(*b)] for row in a]


def partitions(n,limit=None):
    if n==0:yield ();return
    for a in range(min(n,limit or n),0,-1):
        for rest in partitions(n-a,a):yield (a,)+rest


def power_partition(lam,k):
    out=[]
    for a in lam:
        q,s=divmod(a,k);out.extend([q+1]*s+[q]*(k-s))
    return tuple(sorted((x for x in out if x),reverse=True))


def zero_partition(a,p):
    n=len(a);b=[[int(i==j) for j in range(n)] for i in range(n)];null=[0]
    for _ in range(n+1):
        b=mm(b,a,p);null.append(n-rank(list(zip(*b)),p))
    cols=[null[i+1]-null[i] for i in range(n+1)]
    return tuple(sum(cols[j]>i for j in range(n)) for i in range(cols[0]))


def main():
    stats={};n=3;r=2;p=3
    for flat in product(range(p),repeat=n*r):
        cols=[list(flat[j*n:(j+1)*n]) for j in range(r)]
        partial_decomposition(cols,n,r,p)
    stats['exhaustive_partial_decompositions_F3_n3_r2']=p**(n*r)
    rng=random.Random(370096)
    profiles=[]
    for n in range(2,13):
        for r in range(1,n+1):
            for _ in range(12):
                cols=[[rng.randrange(7) for i in range(n)] for j in range(r)]
                profiles.append(partial_decomposition(cols,n,r,7))
    stats['random_partial_decompositions_F7']=len(profiles)
    possible={k:{m:{power_partition(lam,k) for lam in partitions(m)} for m in range(4)} for k in (2,4)}
    reachable={2:set(),4:set()};n=3;p=3
    for flat in product(range(p),repeat=n*n):
        a=[list(flat[j*n:(j+1)*n]) for j in range(n)]
        lam=zero_partition(a,p)
        for k in possible:
            if lam in possible[k][sum(lam)]:reachable[k].add(flat[:6])
    witness=(0,1,0,0,0,0)
    assert len(reachable[2])==729
    assert witness not in reachable[4]
    stats['F3_matrices_classified_for_roots_over_algebraic_closure']=3**9
    stats['reachable_prescribed_two_rows_over_F3']={str(k):len(s) for k,s in reachable.items()}
    stats['fourth_power_boundary_witness_missing']=True
    count=0
    for e in range(2,12):
        for r in range(1,40):
            n=e*(r-1)+1
            for a in range(2,r+1):
                for c in range(r-a+1):
                    assert n-r-c >= (e-1)*(a-1);count+=1
    stats['exact_padding_inequalities']=count
    count=0
    for e in range(1,15):
        for d in range(1,30):
            got=power_partition((e*(d-1)+1,),e)
            want=tuple(sorted([d]+([d-1]*(e-1) if d>1 else []),reverse=True))
            assert got==want;count+=1
    stats['balanced_Jordan_packet_identities']=count
    out=Path(__file__).with_name('check-results.json')
    out.write_text(json.dumps(stats,indent=2)+'\n');print(json.dumps(stats,indent=2))

if __name__=='__main__':main()
