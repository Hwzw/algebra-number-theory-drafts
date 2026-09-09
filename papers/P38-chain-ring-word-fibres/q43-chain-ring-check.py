#!/usr/bin/env python3
"""Exact finite checks of 0127; literal group evaluation is separate from ring coefficients."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json
import math
import random
import time
import numpy as np


def invword(w):
    return [-x for x in reversed(w)]


def comm(u, v):
    return invword(u) + invword(v) + u + v


def words(p, k):
    out = [[], [1], [1, -1], [1, 2], comm([1], [2])]
    out += [[1] * a for a in sorted({2, 3, 4, 8, 9, p, p*p})]
    out += [[1]*p + [2]*p, [1]*p + comm([1], [2]),
            comm([1]*p, [2]), comm([1], [2]*p)]
    e = [1]
    for _ in range(5):
        e = comm(e, [2])
        out.append(e)
    if k == 3:
        out += [comm([1], [2]) + comm([2], [3]),
                [1]*p + comm([2], [3]),
                [1]*p + comm([2], [3]) + comm([1], [2]),
                comm(comm([1], [2]), [3]), comm([1]*p, [2, 3])]
    rng = random.Random(43000 + p*100 + k)
    alphabet = list(range(1, k+1)) + list(range(-k, 0))
    for j in range(12):
        u = [rng.choice(alphabet) for _ in range(5+j)]
        v = [rng.choice(alphabet) for _ in range(3+j//2)]
        out.append(u if j % 3 == 0 else comm(u, v))
    return list(dict.fromkeys(tuple(w) for w in out))


class Model:
    def __init__(self, kind, p, lengths, tmods, units, k):
        self.kind, self.p, self.lengths = kind, p, lengths
        self.L, self.tmods, self.k = max(lengths), tmods, k
        self.tops = list(product(*(range(n) for n in tmods)))
        self.tindex = {t:i for i,t in enumerate(self.tops)}
        self.q = len(self.tops)
        self.rzero = (0,) * self.L if kind == 'poly' else 0
        self.rone = (1,) + (0,)*(self.L-1) if kind == 'poly' else 1
        self.units = units
        coords = [p] * sum(lengths) if kind == 'poly' else [p**l for l in lengths]
        self.coords = coords
        self.base = list(product(*(range(n) for n in coords)))
        self.bindex = {b:i for i,b in enumerate(self.base)}
        self.m, self.n = len(self.base), len(self.base)*self.q
        self.add = np.array([[self.bindex[tuple((a+b)%n for a,b,n in zip(x,y,coords))]
                             for y in self.base] for x in self.base], dtype=np.int32)
        # Literal action: polynomial case uses repeated Jordan shifts, not ring multiplication.
        self.act = np.empty((self.q, self.m), dtype=np.int32)
        for ti,t in enumerate(self.tops):
            for mi,m in enumerate(self.base):
                v = list(m)
                if kind == 'poly':
                    # Each chosen generator is (1+z)^exponent.
                    for a, exponent in zip(t, units):
                        for _ in range(a*exponent):
                            offset, result = 0, []
                            for length in lengths:
                                block = v[offset:offset+length]
                                result += [block[0]] + [(block[j]+block[j-1])%p for j in range(1,length)]
                                offset += length
                            v = result
                else:
                    scalar = math.prod(pow(u,a,p**self.L) for a,u in zip(t,units))
                    v = [(a*scalar)%n for a,n in zip(v,coords)]
                self.act[ti,mi] = self.bindex[tuple(v)]
        self.tadd = np.array([[self.tindex[tuple((a+b)%n for a,b,n in zip(x,y,tmods))]
                              for y in self.tops] for x in self.tops], dtype=np.int32)
        ids = np.arange(self.n, dtype=np.int32)
        self.mul = self.add[ids[:,None]//self.q, self.act[ids[:,None]%self.q,ids[None,:]//self.q]]*self.q + self.tadd[ids[:,None]%self.q,ids[None,:]%self.q]
        self.inverse = np.empty(self.n, dtype=np.int32)
        for a in range(self.n):
            candidates = np.flatnonzero(self.mul[a] == 0)
            assert len(candidates)==1
            self.inverse[a] = candidates[0]
        assert np.all(self.mul[ids,self.inverse] == 0)
        assert np.all(self.mul[self.inverse,ids] == 0)
        # Check the action descends to each specified cyclic factor.
        for j,mod in enumerate(tmods):
            scalar = self.rpow(self.unit_ring(j), mod)
            assert scalar == self.rone
        self.ideal = []
        for s in range(self.L+1):
            if kind == 'poly':
                def inside(v):
                    start=0
                    for length in lengths:
                        if any(v[start:start+min(s,length)]): return False
                        start += length
                    return True
            else:
                def inside(v):
                    return all(x%(p**min(s,length))==0 for x,length in zip(v,lengths))
            self.ideal.append([i for i,v in enumerate(self.base) if inside(v)])
        self.rho = []
        for t in self.tops:
            value=self.rone
            for j,a in enumerate(t): value=self.rmul(value,self.rpow(self.unit_ring(j),a))
            self.rho.append(value)

    def radd(self,a,b):
        return tuple((x+y)%self.p for x,y in zip(a,b)) if self.kind=='poly' else (a+b)%(self.p**self.L)

    def rneg(self,a):
        return tuple(-x%self.p for x in a) if self.kind=='poly' else -a%(self.p**self.L)

    def rmul(self,a,b):
        if self.kind!='poly': return a*b%(self.p**self.L)
        return tuple(sum(a[j]*b[i-j] for j in range(i+1))%self.p for i in range(self.L))

    def rpow(self,a,n):
        out=self.rone
        for _ in range(n): out=self.rmul(out,a)
        return out

    def unit_ring(self,j):
        if self.kind!='poly': return self.units[j]
        a=(1,1)+(0,)*(self.L-2) if self.L>1 else (1,)
        return self.rpow(a,self.units[j])

    def val(self,a):
        if self.kind=='poly': return next((i for i,x in enumerate(a) if x),self.L)
        if not a: return self.L
        j=0
        while a%self.p==0: j,a=j+1,a//self.p
        return j

    def coeffs(self,w,topids):
        # Formula (3) directly scans signed prefix sums in the complement.
        pre=[0]*len(self.tmods)
        cs=[self.rzero for _ in topids]
        for letter in w:
            i=abs(letter)-1
            t=self.tops[topids[i]]
            if letter<0:
                pre=[(a-b)%n for a,b,n in zip(pre,t,self.tmods)]
                cs[i]=self.radd(cs[i],self.rneg(self.rho[self.tindex[tuple(pre)]]))
            else:
                cs[i]=self.radd(cs[i],self.rho[self.tindex[tuple(pre)]])
                pre=[(a+b)%n for a,b,n in zip(pre,t,self.tmods)]
        return self.tindex[tuple(pre)],cs

    def verify(self):
        started=time.time()
        if self.n<=81:
            a=np.arange(self.n,dtype=np.int32)[:,None,None]
            b=np.arange(self.n,dtype=np.int32)[None,:,None]
            c=np.arange(self.n,dtype=np.int32)[None,None,:]
            assert np.all(self.mul[self.mul[a,b],c]==self.mul[a,self.mul[b,c]])
            assoc={'scope':'exhaustive','triples':self.n**3}
        else:
            rng=np.random.default_rng(4301)
            a,b,c=rng.integers(0,self.n,size=(3,4096))
            assert np.all(self.mul[self.mul[a,b],c]==self.mul[a,self.mul[b,c]])
            assoc={'scope':'sampled','triples':4096,'seed':4301}
        inputs=np.indices((self.n,)*self.k,dtype=np.int32).reshape(self.k,-1)
        ws=words(self.p,self.k)
        fibres=0; minratio=None; records=[]; depth_seen=set()
        for wi,w in enumerate(ws):
            values=np.zeros(inputs.shape[1],dtype=np.int32)
            for letter in w:
                var=inputs[abs(letter)-1]
                values=self.mul[values,var if letter>0 else self.inverse[var]]
            literal=np.bincount(values,minlength=self.n)
            predicted=np.zeros(self.n,dtype=np.int64)
            tops=defaultdict(list)
            for ts in product(range(self.q),repeat=self.k):
                r,cs=self.coeffs(w,ts)
                depth=min(self.val(x) for x in cs)
                tops[r].append((cs,depth))
                per=self.m**self.k//len(self.ideal[depth])
                predicted[np.array(self.ideal[depth])*self.q+r] += per
            assert np.array_equal(literal,predicted), (self.kind,self.p,self.lengths,w)
            D=len(tops)
            top_records=[]
            for r,items in tops.items():
                s=min(depth for cs,depth in items)
                depth_seen.add(s)
                good=sum(depth==s for cs,depth in items)
                assert good*(2**s)>=len(items)
                if s<self.L:
                    chosen=next(i for cs,depth in items if depth==s for i,c in enumerate(cs) if self.val(c)==s)
                    support=sum(self.val(cs[chosen])==s for cs,depth in items)
                    assert support*(2**s)>=len(items)
                    assert self.m>=2**s*len(self.ideal[s])
                else: support=len(items)
                attained=[i for i in range(self.m) if literal[i*self.q+r]>0]
                assert attained==self.ideal[s]
                for b in attained:
                    count=int(literal[b*self.q+r])
                    ratio=Fraction(count,self.n**(self.k-1))
                    assert ratio>=1
                    minratio=ratio if minratio is None else min(minratio,ratio)
                    if s<self.L:
                        assert count*D*(2**s)*len(self.ideal[s]) >= self.n**self.k
                    else: assert count*D==self.n**self.k
                    fibres+=1
                top_records.append({'top':self.tops[r],'s':s,'top_fibre':len(items),'good':good,'chosen_support':support})
            records.append({'word':list(w),'image_size':int(np.count_nonzero(literal)),
                            'histogram_sha256':hashlib.sha256(literal.astype('<i8').tobytes()).hexdigest(),
                            'top_data':top_records})
        return {'kind':self.kind,'p':self.p,'module_lengths':self.lengths,'complement_orders':self.tmods,
                'action_parameters':self.units,'group_order':self.n,'variables':self.k,
                'word_count':len(ws),'literal_tuples_per_word':self.n**self.k,
                'attained_fibres_checked':fibres,'least_AA_ratio':str(minratio),
                'depths_checked':sorted(depth_seen),'associativity':assoc,
                'seconds':round(time.time()-started,3),'words':records}


def main():
    specs=[('poly',2,[4],[4],[1],3),
           ('poly',2,[3,1],[4],[1],3),
           ('poly',2,[2,1],[2,2],[1,1],3),
           ('poly',3,[3],[3],[1],3),
           ('poly',2,[4,2],[4],[1],2),
           ('poly',3,[3,1],[3],[1],2),
           ('integer',2,[3],[2],[7],3),
           ('integer',2,[4],[4],[3],3),
           ('integer',2,[3,1],[2,2],[3,5],3),
           ('integer',3,[3],[9],[4],2),
           ('integer',3,[2,1],[3],[4],3),
           ('integer',2,[1,1],[4],[1],3)]
    report={'status':'running','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'Finite checks, not a proof of the universal theorem. Literal word evaluation uses multiplication tables; predictions use scalar coefficient ideals.',
            'models':[]}
    dest=Path(__file__).with_suffix('.json')
    for spec in specs:
        result=Model(*spec).verify()
        report['models'].append(result)
        dest.write_text(json.dumps(report,indent=2)+'\n')
        print({k:v for k,v in result.items() if k!='words'},flush=True)
    report['status']='passed'
    report['totals']={'models':len(report['models']),
                      'word_distributions':sum(x['word_count'] for x in report['models']),
                      'literal_word_evaluations':sum(x['word_count']*x['literal_tuples_per_word'] for x in report['models']),
                      'attained_fibres':sum(x['attained_fibres_checked'] for x in report['models'])}
    dest.write_text(json.dumps(report,indent=2)+'\n')
    print('ALL PASS',report['totals'],flush=True)


if __name__=='__main__': main()
