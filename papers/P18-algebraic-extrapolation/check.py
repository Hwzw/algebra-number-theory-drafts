"""Exact finite consistency checks; the manuscript's general proof is independent."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib,json


def bernstein_coefficients(poly,n):
    assert n>=len(poly)-1
    return [sum(a*comb(n-s,k-s) for s,a in enumerate(poly) if s<=k)
            for k in range(n+1)]


def evaluate(poly,t):
    out=0
    for a in reversed(poly):out=out*t+a
    return out


def complex_closure(q,bound=12):
    # lambda=q*i; represent a+b*lambda with integer pair (a,b).
    def star(x,y):
        a,b=x;c,d=y
        return a-q*q*(d-b), b+c-a
    def allowed(x):
        a,b=x
        return a%(q*q) in {0,1} and (a+b)%(1+q*q) in {0,1}
    S={(0,0),(1,0)};rounds=[]
    while True:
        new={star(x,y) for x in S for y in S}
        new={x for x in new if max(map(abs,x))<=bound}
        assert all(allowed(x) for x in new)
        nxt=S|new;rounds.append(len(nxt))
        if nxt==S:break
        S=nxt
    target={(a,b) for a in range(-4,5) for b in range(-4,5) if allowed((a,b))}
    return {'q':q,'intermediate_coordinate_bound':bound,'discovered':len(S),
            'round_sizes':rounds,'target_coordinate_bound':4,'predicted_target_count':len(target),
            'target_reached':len(target&S),'target_missing':sorted(target-S)}


def main():
    polynomial_cases=0
    samples=[([0,1], [1,-1]),([0,1,-1],[1,-1,1]),
             ([0,0,4,-8,4],[1,0,-4,8,-4])]
    for p,q in samples:
        for n in range(max(len(p),len(q))-1,21):
            cp,cq=bernstein_coefficients(p,n),bernstein_coefficients(q,n)
            assert all(cp[k]+cq[k]==comb(n,k) for k in range(n+1))
            for t in [F(j,17) for j in range(18)]:
                assert sum(cp[k]*t**k*(1-t)**(n-k) for k in range(n+1))==evaluate(p,t)
                polynomial_cases+=1
    rounding_bounds=0
    for n in range(2,41):
        for j in range(41):
            t=F(j,40)
            s=sum(t**k*(1-t)**(n-k) for k in range(1,n))
            assert s<=F(1,n)
            rounding_bounds+=1
    derivative_cases=0
    for modulus in range(-12,13):
        if not modulus:continue
        N=abs(modulus)+1
        for d in range(-30,31):
            positive=[d+modulus*h for h in range(-100,101) if 0<d+modulus*h<N]
            negative=[d-modulus*h for h in range(-100,101) if -N<d-modulus*h<0]
            assert positive and negative
            derivative_cases+=1
    # Source's negative quadratic sPV family X^2+mX-n, 0<n<=m.
    equal=[(m,n) for m in range(1,41) for n in range(1,m+1)
           if n<=2 and abs(1+m-n)<=2]
    assert equal==[(1,1),(2,1),(2,2),(3,2)]
    cubic=[-1,5,-6,1]
    signs=[evaluate(cubic,t) for t in [F(0),F(1,3),F(1),F(5),F(6)]]
    assert signs[0]<0<signs[1] and signs[2]<0 and signs[3]<0<signs[4]
    assert evaluate(cubic,1)!=0 and evaluate(cubic,-1)!=0
    closures=[complex_closure(q) for q in [1,2,3]]
    result={'meaning':'Finite exact consistency checks only; no universal claim is inferred from bounded reachability.',
            'bernstein_evaluation_checks':polynomial_cases,'rounding_bound_checks':rounding_bounds,
            'endpoint_derivative_checks':derivative_cases,'quadratic_equality_pairs_m_n':equal,
            'cubic_sign_values':[str(x) for x in signs],'bounded_complex_closures':closures,
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_name('check-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
