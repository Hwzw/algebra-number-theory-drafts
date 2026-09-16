"""Finite energy checks for note 0259; no eigenvalue computation or enclosure."""
from pathlib import Path
import json
import math
import numpy as np
import sympy as sp


def sphere_area(d):
    return 2*math.pi**((d+1)/2)/math.gamma((d+1)/2)


def w_and_derivative(t,n):
    s2=1-t*t
    w=np.empty_like(t);wp=np.empty_like(t)
    small=s2<.04
    v=s2[small];tt=t[small]
    w[small]=sum(math.comb(2*j,j)/(4**j*(n+2*j))*v**j for j in range(12))
    wp[small]=sum(-2*tt*j*math.comb(2*j,j)/(4**j*(n+2*j))*v**(j-1)
                  for j in range(1,12))
    mask=~small
    r=np.arccos(t[mask]);s=np.sqrt(s2[mask]);c=t[mask]
    integrals=[r,1-c]
    for k in range(2,n):
        integrals.append((k-1)/k*integrals[k-2]-s**(k-1)*c/k)
    w[mask]=integrals[n-1]/s**n
    wp[mask]=(n*c*w[mask]-1)/s2[mask]
    return w,wp


def integrate_energy(n,left,right,nodes):
    q,weights=np.polynomial.legendre.leggauss(nodes)
    eta=(q+1)*math.pi/4
    psi=left+(q+1)*(right-left)/2
    we=weights*math.pi/4
    wp=weights*(right-left)/2
    se=np.sin(eta)[:,None];ce=np.cos(eta)[:,None]
    t=se*np.cos(psi)[None,:]
    w,dw=w_and_derivative(t,n)
    z2=ce*ce/(n-1)  # average X_2^2 over y in S^(n-2)
    energy=w*w+z2*((1-t*t)*dw*dw-w*w-2*t*w*dw)
    density=energy*se*ce**(n-2)
    return float(sphere_area(n-2)*np.einsum("i,ij,j->",we,density,wp))


def symbolic_checks():
    n,A,om,edge,alpha=sp.symbols("n A om edge alpha", positive=True)
    removed=(sp.pi-alpha)*edge*(n-2)/(n*n*(n-1)**2)
    denominator=A*A*om/n
    dn=edge*(n-2)/(n*(n-1)**2*A*A*om)
    assert sp.simplify(removed/denominator-dn*(sp.pi-alpha))==0
    beta=sp.symbols("beta",real=True)
    assert sp.trigsimp(sp.cos(beta)*sp.cos(sp.pi/2-beta)
                       -sp.sin(beta)*sp.sin(sp.pi/2-beta))==0
    # Beta(1,L/2) projection tail at cos(r)^2.
    L,r=sp.symbols("L r",positive=True)
    x=sp.symbols("x",positive=True)
    tail=(1-x)**(L/2)
    assert sp.simplify(sp.diff(tail,x)+L/2*(1-x)**(L/2-1))==0
    # Mean-adjusted sum of coordinate denominators.
    P,m2=sp.symbols("P m2")
    assert sp.expand(P-2*P*m2+P*m2-P*(1-m2))==0
    return 4


def main():
    count=symbolic_checks()
    cases=[]
    for n in (3,4,5,8):
        A=math.sqrt(math.pi)*math.gamma(n/2)/(2*math.gamma((n+1)/2))
        D=A*A*sphere_area(n-1)/n
        expected=A*sphere_area(n-1)/n
        for fraction in (.1,.35,.7,.95):
            alpha=math.pi*fraction;b=(math.pi-alpha)/2
            results=[]
            for nodes in (100,180):
                outer=2*integrate_energy(n,b,math.pi/2,nodes)
                removed=2*integrate_energy(n,0,b,nodes)
                dn=sphere_area(n-2)*(n-2)/(n*(n-1)**2*A*A*sphere_area(n-1))
                gap=1/A-outer/D
                assert abs((outer+removed)/expected-1)<2e-9
                assert gap>0 and gap>=dn*(math.pi-alpha)-1e-10
                results.append(dict(nodes=nodes,energy_sum_relative_error=
                                    abs((outer+removed)/expected-1),
                                    trial_quotient=outer/D,
                                    actual_trial_gap=gap,
                                    lower_bound_gap=dn*(math.pi-alpha)))
            cases.append(dict(n=n,angle_fraction=fraction,sigma_hemisphere=1/A,
                              denominator=D,results=results))
    out=dict(symbolic_checks_passed=count,finite_cases=len(cases),
             rigorous_numerical_enclosures=False,
             computed_quantity="Energy of the explicit lune trial, not the actual eigenvalue",
             max_energy_sum_relative_error=max(r["energy_sum_relative_error"]
                   for c in cases for r in c["results"]),
             max_resolution_difference=max(abs(c["results"][0]["trial_quotient"]
                   -c["results"][1]["trial_quotient"]) for c in cases),cases=cases)
    Path(__file__).with_name("lune-comparison-diagnostic.json").write_text(
        json.dumps(out,indent=2)+"\n")
    print(json.dumps({k:v for k,v in out.items() if k!="cases"},indent=2))


if __name__=="__main__":
    main()
