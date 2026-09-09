#!/usr/bin/env python3
"""Literal carry multiplication versus split-cover pushforward for 0128."""
from pathlib import Path
from fractions import Fraction
from itertools import product
import hashlib
import json
import time
import numpy as np
from importlib.util import spec_from_file_location, module_from_spec

core_path=Path(__file__).with_name('q43-chain-ring-check.py')
spec=spec_from_file_location('q43core',core_path)
core=module_from_spec(spec)
spec.loader.exec_module(core)


def check(kind,p,lengths,q,unit,c,k):
    start=time.time()
    # Use a split model only to supply the base addition and the scalar action.
    base=core.Model(kind,p,lengths,[q],[unit],k)
    ci=base.bindex[tuple(c)]
    multiples=[0]
    while True:
        nxt=int(base.add[multiples[-1],ci])
        if nxt==0: break
        multiples.append(nxt)
    hsize=len(multiples)
    assert base.act[1 if q>1 else 0,ci]==ci
    cover=core.Model(kind,p,lengths,[q*hsize],[unit],k)
    n=base.n; ids=np.arange(n,dtype=np.int32)
    # Literal nonsplit multiplication adds c whenever the top sum wraps modulo q.
    raw=base.add[ids[:,None]//q,base.act[ids[:,None]%q,ids[None,:]//q]]
    carry=(ids[:,None]%q+ids[None,:]%q)//q
    mul=base.add[raw,np.where(carry,ci,0)]*q+(ids[:,None]%q+ids[None,:]%q)%q
    inv=np.array([np.flatnonzero(mul[a]==0)[0] for a in ids],dtype=np.int32)
    assert np.all(mul[ids,inv]==0) and np.all(mul[inv,ids]==0)
    cid=np.arange(cover.n,dtype=np.int32)
    project=base.add[cid//cover.q,np.array(multiples)[(cid%cover.q)//q]]*q+(cid%cover.q)%q
    assert np.all(project[cover.mul]==mul[project[:,None],project[None,:]])
    kernel=np.flatnonzero(project==0)
    assert len(kernel)==hsize
    assert np.all(cover.mul[kernel[:,None],cid[None,:]]==cover.mul[cid[None,:],kernel[:,None]])
    if n<=81:
        a=ids[:,None,None];b=ids[None,:,None];d=ids[None,None,:]
        assert np.all(mul[mul[a,b],d]==mul[a,mul[b,d]])
        assoc={'scope':'exhaustive','triples':n**3}
    else:
        rng=np.random.default_rng(4312);a,b,d=rng.integers(0,n,size=(3,4096))
        assert np.all(mul[mul[a,b],d]==mul[a,mul[b,d]])
        assoc={'scope':'sampled','triples':4096,'seed':4312}
    inputs=np.indices((n,)*k,dtype=np.int32).reshape(k,-1)
    records=[];fibres=0;minratio=None
    for w in core.words(p,k):
        values=np.zeros(inputs.shape[1],dtype=np.int32)
        for letter in w:
            x=inputs[abs(letter)-1]
            values=mul[values,x if letter>0 else inv[x]]
        literal=np.bincount(values,minlength=n)
        lifted=np.zeros(cover.n,dtype=np.int64)
        for ts in product(range(cover.q),repeat=k):
            top,cs=cover.coeffs(w,ts)
            depth=min(cover.val(a) for a in cs)
            per=cover.m**k//len(cover.ideal[depth])
            lifted[np.array(cover.ideal[depth])*cover.q+top] += per
        pushed=np.zeros(n,dtype=np.int64)
        np.add.at(pushed,project,lifted)
        assert np.all(pushed%(hsize**k)==0)
        assert np.array_equal(literal,pushed//(hsize**k))
        exponent=[sum(1 if x==i else -1 if x==-i else 0 for x in w) for i in range(1,k+1)]
        image_t={sum(a*b for a,b in zip(exponent,ts))%cover.q for ts in product(range(cover.q),repeat=k)}
        image_k={sum(a*b for a,b in zip(exponent,ts))%hsize for ts in product(range(hsize),repeat=k)}
        D,Kpower=len(image_t),len(image_k)
        assert D<=q*Kpower
        assert all(int(count)*cover.m*D>=cover.n**k for count in lifted if count)
        for g in np.flatnonzero(literal):
            good=sum(lifted[y]>0 for y in np.flatnonzero(project==g))
            assert good>=Kpower
            ratio=Fraction(int(literal[g]),n**(k-1))
            assert ratio>=1
            minratio=ratio if minratio is None else min(minratio,ratio)
            fibres+=1
        records.append({'word':list(w),'image_size':int(np.count_nonzero(literal)),
                        'top_image_size':D,'central_power_image_size':Kpower,
                        'histogram_sha256':hashlib.sha256(literal.astype('<i8').tobytes()).hexdigest()})
    return {'kind':kind,'p':p,'lengths':lengths,'quotient_order':q,'unit':unit,'carry':list(c),
            'group_order':n,'split_cover_order':cover.n,'central_kernel_order':hsize,
            'variables':k,'word_count':len(records),'literal_tuples_per_word':n**k,
            'full_homomorphism_pairs':cover.n**2,'attained_fibres_checked':fibres,
            'associativity':assoc,'least_AA_ratio':str(minratio),'seconds':round(time.time()-start,3),'words':records}


def main():
    specs=[('integer',2,[2],2,3,[2],3),
           ('integer',2,[3],2,7,[4],3),
           ('integer',2,[4],2,15,[8],3),
           ('integer',2,[3],4,3,[4],3),
           ('integer',3,[2],9,4,[3],2),
           ('poly',2,[3],4,1,[0,0,1],3),
           ('poly',2,[3,1],4,1,[0,0,0,1],3),
           ('poly',3,[2],3,1,[0,1],3),
           ('poly',3,[4],9,1,[0,0,0,1],2),
           ('integer',2,[1],2,1,[1],3)]
    report={'status':'running','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'core_sha256':hashlib.sha256(core_path.read_bytes()).hexdigest(),'models':[],
            'scope':'Finite consistency checks of the cyclic-cover argument; not a universal proof.'}
    dest=Path(__file__).with_suffix('.json')
    for spec in specs:
        result=check(*spec);report['models'].append(result)
        dest.write_text(json.dumps(report,indent=2)+'\n')
        print({k:v for k,v in result.items() if k!='words'},flush=True)
    report['status']='passed'
    report['totals']={'models':len(report['models']),
                      'word_distributions':sum(x['word_count'] for x in report['models']),
                      'literal_word_evaluations':sum(x['word_count']*x['literal_tuples_per_word'] for x in report['models']),
                      'attained_fibres':sum(x['attained_fibres_checked'] for x in report['models'])}
    dest.write_text(json.dumps(report,indent=2)+'\n');print('ALL PASS',report['totals'],flush=True)


if __name__=='__main__': main()
