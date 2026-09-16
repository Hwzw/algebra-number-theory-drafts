"""Finite n=3 coefficient checks for note 0257, not certified enclosures."""
from pathlib import Path
import json
import math
import numpy as np
import sympy as sp
from verify_harmonic_center import kernel


def exact_checks():
    e,L,A,m=sp.symbols("e L A m")
    Q=(A-e*(1+L*A*A)*m)/(A*A-2*e*A*m)
    assert sp.simplify(sp.diff(Q,e).subs(e,0)+(L-A**-2)*m)==0
    h,g2=sp.symbols("h g2")
    area=(1+e*e*h*h)**(-L/2)*sp.sqrt(1+e*e*g2/(1+e*e*h*h))
    assert sp.simplify(sp.diff(area,e,2).subs(e,0)-(g2-L*h*h))==0
    x,s,c=sp.symbols("x s c")
    # y=sqrt(L)-x and x'=(L-x*x-(L-1)*c*x)/s.
    residual=-(L-x*x-(L-1)*c*x)/s+(sp.sqrt(L)+x)/s*(sp.sqrt(L)-x)-(L-1)*c*x/s
    assert sp.simplify(residual)==0
    # Uniform proof 0258: Hessian of the area integrand at zero.
    u,p=sp.symbols("u p")
    J=(1+u*u)**(-L/2)*sp.sqrt(1+p*p/(1+u*u))
    assert sp.simplify(sp.diff(J,u,2).subs({u:0,p:0})+L)==0
    assert sp.simplify(sp.diff(J,p,2).subs({u:0,p:0})-1)==0
    assert sp.diff(J,u,p).subs({u:0,p:0})==0
    assert all(sp.diff(J,u,i,p,3-i).subs({u:0,p:0})==0 for i in range(4))
    # I'(r)=sin(r)^L, r=arccot(u), so dI/du is the formula in 0258.
    derivative=(1+u*u)**(-L/2)*(-1/(1+u*u))
    assert sp.simplify(derivative+(1+u*u)**(-(L+2)/2))==0
    return 6


def check(a,c,linear,eps,nodes):
    x,q=np.polynomial.legendre.leggauss(nodes);q=q/2
    h0=np.sqrt(a*a*(1-x*x)+c*c*x*x)
    h=h0+linear*x
    hx=(c*c-a*a)*x/h0+linear
    mean=float(np.dot(q,h))
    d=float(np.dot(q,h*h-(1-x*x)*hx*hx/2))
    coeff=(2-16/math.pi**2)*(mean-math.sqrt(d))
    assert coeff>0 and np.min(h)>0 and d>0
    cot=eps*h
    sr=1/np.sqrt(1+cot*cot);cr=cot*sr
    rx=-eps*hx/(1+cot*cot)
    W=np.sqrt(1+(1-x*x)*rx*rx/(sr*sr))
    area=sr*sr*W
    P=float(np.dot(q,area))
    X0=cr;Xz=sr*x
    nu0=-sr/W
    nuz=(cr*x-rx*(1-x*x)/sr)/W
    def balance(beta):
        t=math.cos(beta)*X0+math.sin(beta)*Xz
        tangent=-math.sin(beta)*X0+math.cos(beta)*Xz
        return float(np.dot(q,area*kernel(t)*tangent))
    lo,hi=-.5,.5
    assert balance(lo)>0 and balance(hi)<0
    for _ in range(60):
        mid=(lo+hi)/2
        if balance(mid)>0:lo=mid
        else:hi=mid
    beta=(lo+hi)/2
    t=math.cos(beta)*X0+math.sin(beta)*Xz
    sint=np.sqrt(1-t*t)
    pn=math.cos(beta)*nu0+math.sin(beta)*nuz
    f=kernel(t)*sint;fp=1-2*t*kernel(t)
    Q=float(np.dot(q,area*f*fp*(-pn/sint))/np.dot(q,area*f*f))
    R=math.asin(math.sqrt(P))
    fR=(R-math.sin(R)*math.cos(R))/(2*math.sin(R)**2)
    sigma=1/fR-2/math.tan(R)
    observed=(sigma-Q)/eps
    return dict(a=a,c=c,linear=linear,epsilon=eps,nodes=nodes,
                predicted_coefficient=coeff,observed_coefficient=observed,
                absolute_error=abs(observed-coeff),
                center_beta=beta,
                center_first_order_error=abs(beta/eps+linear),
                center_residual=balance(beta)/P,
                minimum_sampled_cosine=float(np.min(t)))


def main():
    symbolic=exact_checks()
    params=[(1,2,0),(2,1,0),(1,2,.4),(2,1,.4)]
    epsilons=[.02,.01,.005,.0025]
    cases=[check(*p,e,400) for p in params for e in epsilons]
    fine=[check(*p,epsilons[-1],800) for p in params]
    errors=[]
    for i,p in enumerate(params):
        group=cases[i*4:(i+1)*4]
        assert all(group[j+1]["absolute_error"]<group[j]["absolute_error"]
                   for j in range(3))
        assert all(row["minimum_sampled_cosine"]>0 and
                   abs(row["center_residual"])<1e-12 for row in group)
        errors.append(abs(group[-1]["observed_coefficient"]-fine[i]["observed_coefficient"]))
    result=dict(symbolic_identities_passed=symbolic,
                profiles=len(params),main_cases=len(cases),
                rigorous_numerical_enclosures=False,
                max_final_coefficient_error=max(x["absolute_error"] for x in fine),
                max_resolution_difference=max(errors),cases=cases,refined_cases=fine)
    Path(__file__).with_name("hemisphere-profile-diagnostic.json").write_text(
        json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k not in ("cases","refined_cases")},indent=2))


if __name__=="__main__":
    main()
