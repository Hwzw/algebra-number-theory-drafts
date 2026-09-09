#!/usr/bin/env python3
"""Exact exhaustive checks; no third-party dependencies. Not an infinite proof."""
import itertools, json

def prime_poly_divides(f,g,p):
    f=list(f)
    for i in range(len(f)-len(g),-1,-1):
        t=f[i+len(g)-1]
        for j in range(len(g)):
            f[i+j]=(f[i+j]-t*g[j])%p
    return not any(f)

def field(p,m):
    for coeff in itertools.product(range(p),repeat=m):
        f=coeff+(1,)
        if all(not prime_poly_divides(f,c+(1,),p)
               for d in range(1,m//2+1)
               for c in itertools.product(range(p),repeat=d)):
            break
    size=p**m
    digits=[tuple((x//p**i)%p for i in range(m)) for x in range(size)]
    def encode(a): return sum(t*p**i for i,t in enumerate(a))
    add=[[encode([(x+y)%p for x,y in zip(a,b)]) for b in digits] for a in digits]
    mul=[]
    for a in digits:
        row=[]
        for b in digits:
            c=[0]*(2*m-1)
            for i in range(m):
                for j in range(m): c[i+j]=(c[i+j]+a[i]*b[j])%p
            for i in range(2*m-2,m-1,-1):
                t=c[i]
                for j in range(m+1): c[i-m+j]=(c[i-m+j]-t*f[j])%p
            row.append(encode(c[:m]))
        mul.append(row)
    def power(a,n):
        r=1
        while n:
            if n&1:r=mul[r][a]
            a=mul[a][a]; n//=2
        return r
    return size,f,add,mul,power
