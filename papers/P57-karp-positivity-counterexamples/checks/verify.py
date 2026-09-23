#!/usr/bin/env python3
"""Exact certificates for the manuscript. Requires Python 3 and SymPy.
Run from any directory; results.json is written beside this file.
No floating-point root computation is used.
"""
from pathlib import Path
from itertools import permutations
import json
import sympy as s

x=s.symbols('x')
HERE=Path(__file__).resolve().parent

def increasing_tuples(total,r,start=0):
    if r==1:
        if total>=start:
            yield (total,)
        return
    for k in range(start,(total-r*(r-1)//2)//r+1):
        for rest in increasing_tuples(total-k,r-1,k+1):
            yield (k,)+rest

def expansion(f,n,r,certificate=False):
    R=r*(r-1)//2
    def at(k):
        return f[k] if 0<=k<len(f) else s.Integer(0)
    terms=[]
    out=s.Integer(0)
    for ell in increasing_tuples(n-R,r):
        minor=s.Matrix(r,r,lambda i,j:at(ell[j]+r-1-i)).det()
        vand=s.prod(ell[j]-ell[i] for i in range(r) for j in range(i+1,r))
        weight=s.factorial(n)*vand*minor/s.prod(s.factorial(u) for u in ell)
        base=s.prod(s.rf(x+j,ell[j]-j) for j in range(r))
        out+=weight*base
        terms.append({'ell':list(ell),'minor':str(minor),'vandermonde':str(vand),
                      'weight':str(weight),'basis':str(s.expand(base))})
    poly=s.Poly(out,x)
    return (poly,terms) if certificate else poly

def original_determinant_value(f,n,r,xx):
    """Original determinant, computed by permutation and truncated convolution.
    Independent of finite differences and of the minor expansion.
    """
    entries=[[[f[k]*s.rf(xx+j-i,k)/s.factorial(k) for k in range(n+1)]
              for j in range(r)] for i in range(r)]
    out=s.Integer(0)
    for perm in permutations(range(r)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(r) for j in range(i+1,r))
        acc=[s.Integer(1)]+[s.Integer(0)]*n
        for i in range(r):
            coeff=entries[i][perm[i]]
            acc=[sum(acc[k]*coeff[d-k] for k in range(d+1)) for d in range(n+1)]
        out+=sign*acc[n]
    return s.factorial(n)*out

def direct_q(f,n,alpha,beta):
    return s.Poly(sum(s.binomial(n,k)*f[k]*f[n-k]*
          (s.rf(x+alpha,k)*s.rf(x+beta,n-k)
           -s.rf(x+alpha+beta,k)*s.rf(x,n-k)) for k in range(n+1)),x)

def shift_expansion(f,n,alpha,beta):
    out=0
    for j in range(1,n+1):
        for a in range((n-j+1)//2):
            b=n-j-a
            assert a<b
            minor=f[a+j]*f[b]-f[a]*f[b+j]
            base=s.rf(x,a)*s.rf(x+beta,a)*(s.rf(x+a+beta,b-a)-s.rf(x+a,b-a))
            out+=s.factorial(n)*s.rf(alpha,j)*minor*base/(s.factorial(j)*s.factorial(a)*s.factorial(b))
    return s.Poly(out,x)

report={'arithmetic':'exact integers and rational/symbolic polynomials',
        'sympy_version':s.__version__,'checks':{}}

# General shifts: symbolic coefficients and symbolic alpha,beta, degrees 2..5.
alpha,beta=s.symbols('alpha beta')
for n in range(2,6):
    f=s.symbols('f:'+str(n+1))
    diff=direct_q(f,n,alpha,beta)-shift_expansion(f,n,alpha,beta)
    assert all(s.expand(c)==0 for c in diff.all_coeffs())
report['checks']['symbolic_general_shift_identities']=4
print('Symbolic general-shift identities passed.',flush=True)

# C2 and C5: full polynomial identity against the original defining sum.
n=18
f=[s.Integer(1+(10000 if 0<k<n else 0)+k*(n-k)) for k in range(n+1)]
gaps=[f[k]**2-f[k-1]*f[k+1] for k in range(1,n)]
assert min(gaps)>0
p=expansion(f,n,2)
q=direct_q(f,n,s.Integer(1),s.Integer(1))
assert s.Poly(q.as_expr().subs(x,x-1),x)==p
R=s.Poly(4930033*x**8+217997860*x**7+4622212322*x**6+66604657560*x**5+
         741214112737*x**4+6223968331700*x**3+35647227456908*x**2+
         120787851904080*x+180829229981400,x)
assert p==s.Poly(88128*s.rf(x+1,8)*R.as_expr(),x)
T=s.Poly(R.as_expr().subs(x,x+1),x)
assert T.all_coeffs()==[4930033,257438124,6286238266,99191968400,1151545612777,
                       9955221611636,59506512884844,214081390250960,344300941584600]
a=T.all_coeffs()
D=[s.Matrix(k,k,lambda i,j:a[2*j-i+1] if 0<=2*j-i+1<=8 else 0).det(method='domain-ge')
   for k in range(1,9)]
assert list(map(s.sign,D))==[1,1,1,1,1,1,-1,-1]
N=378576120131718481193785864*10**33+480712644384882588463864139*10**6+262343
assert N==378576120131718481193785864480712644384882588463864139262343
assert D[6]==-2**16*3**7*5**5*7**3*11*13**3*N
assert D[7]==a[8]*D[6]
report['stability_counterexample']={
 'n':18,'r':2,'alpha':1,'beta':1,'input':list(map(int,f)),
 'log_concavity_gaps':list(map(int,gaps)),
 'R_coefficients_descending':list(map(str,R.all_coeffs())),
 'T_coefficients_descending':list(map(str,T.all_coeffs())),
 'hurwitz_determinants':list(map(str,D)),
 'hurwitz_signs':list(map(int,map(s.sign,D))),
 'seventh_certificate_positive_integer':str(N),
 'original_sum_identity':True}
print('Conjectures 2 and 5: exact factorization and negative Hurwitz determinant passed.',flush=True)

# C6: formula and five-term certificate, plus independent original determinant.
n=11;f=[s.binomial(n,k) for k in range(n+1)]
p,terms=expansion(f,n,3,True)
C=s.Poly(883*x**3+5349*x**2+9926*x+5880,x)
assert p==s.Poly(15697281600*(x+2)*(x+3)*C.as_expr(),x)
assert [t['ell'] for t in terms]==[[0,1,7],[0,2,6],[0,3,5],[1,2,5],[1,3,4]]
disc=s.discriminant(C.as_expr(),x)
assert disc==-623476452956
for xx in range(13):
    assert original_determinant_value(f,n,3,xx)==p.eval(xx)
report['real_root_counterexample']={
 'n':11,'r':3,'input':list(map(int,f)),'minor_terms':terms,
 'cubic_coefficients_descending':list(map(str,C.all_coeffs())),
 'cubic_discriminant':str(disc),'independent_determinant_points':list(range(13)),
 'degree_bound_for_independent_identity':11}
print('Conjecture 6: five-term formula, discriminant, and independent determinant certificate passed.',flush=True)

# Extra independent polynomial identities for the higher-order formula.
checks=0
for r,n in [(2,5),(3,5),(3,6),(3,8),(4,12),(4,14)]:
    f=[s.Integer(1+(k*k+3*k+7)%11) for k in range(n+1)]
    p=expansion(f,n,r)
    for xx in range(n+1):
        assert original_determinant_value(f,n,r,xx)==p.eval(xx)
    checks+=1
report['checks']['additional_higher_order_polynomial_identities']=checks
print('Additional determinant identities passed.',flush=True)

# Degeneracies and finite samples of nonnegative/strict-positive coefficients.
assert expansion([s.Integer(1)]*7,6,2).is_zero
assert expansion([1,2,1,0,0],4,2)==s.Poly(12*x*(x+1),x)
report['checks']['conjecture_4_degeneracies']=2
positive_samples=0
for r in (2,3,4):
    for n in range(r*(r-1),r*(r-1)+5):
        p=expansion([s.binomial(n,k) for k in range(n+1)],n,r)
        assert p.degree()==n-r*(r-1)
        assert all(c>0 for c in p.all_coeffs())
        positive_samples+=1
report['checks']['positive_binomial_samples']=positive_samples
report['all_checks_passed']=True
(HERE/'results.json').write_text(json.dumps(report,indent=2)+'\n')
print('All exact checks passed; results.json written.',flush=True)
