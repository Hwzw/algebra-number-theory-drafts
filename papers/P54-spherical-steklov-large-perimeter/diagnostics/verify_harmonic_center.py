"""Exact identities and finite checks for note 0256; not a universal proof.

Uses NumPy/SymPy. Shifted gnomonic ellipsoids are smooth strictly convex
spherical domains. All numerical checks are floating-point diagnostics.
"""
from pathlib import Path
import json
import math
import numpy as np
import sympy as sp


def symbolic_checks():
    L, t, u, pn, qn, pq, H, b, bp, w = sp.symbols(
        "L t u pn qn pq H b bp w", real=True)
    div = b * (-L*u-H*qn) + bp*(pq-t*u-pn*qn)
    target = bp*pq-w*u-(b*H+bp*pn)*qn
    assert sp.expand((div-target).subs(w,L*b+t*bp)) == 0
    s = sp.symbols("s", positive=True)
    wf = sp.Function("w")
    assert sp.simplify(sp.diff(s**L*wf(t*s),s)
                       -s**(L-1)*(L*wf(t*s)+t*s*sp.Subs(
                           sp.Derivative(wf(sp.Symbol("z")),sp.Symbol("z")),
                           sp.Symbol("z"),t*s))) == 0
    r = sp.symbols("r", positive=True)
    I = sp.Function("I")(r)
    J = sp.sin(r)**(L+1)-(L+1)*sp.cos(r)*I
    assert sp.simplify((sp.diff(J,r)-(L+1)*sp.sin(r)*I)
                       .subs(sp.diff(I,r),sp.sin(r)**L)) == 0
    assert sp.simplify((sp.diff(I/sp.sin(r)**(L+1),r)
                       -J/sp.sin(r)**(L+2))
                       .subs(sp.diff(I,r),sp.sin(r)**L)) == 0
    # Restrict the potential to a unit-speed great circle:
    # t''=-t, W'=-w, W''=-w'.
    tp, wp = sp.symbols("tp wp")
    assert sp.expand((-wp)*tp**2+(-w)*(-t)
                     -(-wp*tp**2+w*t)) == 0
    return 5


def kernel(t):
    """n=3 harmonic kernel w(t), including a stable near-one series."""
    t = np.clip(t, -1+1e-15, 1)
    v = 1-t*t
    out = np.empty_like(t)
    near = (t > 0) & (v < 0.01)
    # The series has positive coefficients and starts at 1/3.
    out[near] = sum(
        math.comb(2*j,j)/(4**j*(2*j+3))*v[near]**j
        for j in range(10))
    z = ~near
    out[z] = (np.arccos(t[z])-t[z]*np.sqrt(v[z]))/(2*v[z]**1.5)
    return out


def case(A, C, shift, nodes):
    x, weights = np.polynomial.legendre.leggauss(nodes)
    avg_weights = weights/2
    yz = shift+C*x
    ynorm2 = A*A*(1-x*x)+yz*yz
    den = np.sqrt(1+ynorm2)
    m2 = (1-x*x)/A**2+x*x/C**2
    h0 = 1+shift*x/C
    normalden = np.sqrt(m2+h0*h0)
    area = A*A*C*normalden/den**3
    P = float(np.dot(avg_weights,area))  # perimeter divided by 4*pi

    def balance(beta):
        t = (np.cos(beta)+np.sin(beta)*yz)/den
        tangent = (-np.sin(beta)+np.cos(beta)*yz)/den
        return float(np.dot(avg_weights, area*kernel(t)*tangent))

    lo, hi = math.atan(shift-C), math.atan(shift+C)
    assert balance(lo)>0 and balance(hi)<0
    for _ in range(65):
        mid=(lo+hi)/2
        if balance(mid)>0:
            lo=mid
        else:
            hi=mid
    beta=(lo+hi)/2
    t=(np.cos(beta)+np.sin(beta)*yz)/den
    sr=np.sqrt(np.maximum(0,1-t*t))
    pn=(-np.cos(beta)*h0+np.sin(beta)*x/C)/normalden
    radial_normal=-pn/sr
    f=kernel(t)*sr
    fp=1-2*t*kernel(t)
    D=float(np.dot(avg_weights,area*f*f))
    N=float(np.dot(avg_weights,area*f*fp*radial_normal))
    R=math.asin(math.sqrt(P))
    fR=(R-math.sin(R)*math.cos(R))/(2*math.sin(R)**2)
    sigma=(1-2/math.tan(R)*fR)/fR
    moments={}
    for k in (1,2,4,8):
        lhs=float(np.dot(avg_weights,area*sr**k*((2+k)-k*radial_normal)))
        rhs=2*P**(1+k/2)
        moments[str(k)]=(lhs-rhs)/rhs
    residual=balance(beta)/P
    assert np.min(t)>0
    assert abs(residual)<1e-10
    assert np.min(radial_normal)>0
    assert np.max(radial_normal)<1+1e-10
    return dict(A=A,C=C,shift=shift,nodes=nodes,beta=beta,
                normalized_perimeter=P,minimum_sampled_cosine=float(np.min(t)),
                normalized_center_residual=residual,trial_ratio=N/D/sigma,
                relative_moment_deficits=moments)


def main():
    count=symbolic_checks()
    params=[(.5,.5,0),(.5,.5,.5),(.5,.5,2),
            (1,1,1),(2,2,1),(.4,2,1),(2,.4,1),
            (1,4,3),(4,1,3),(.3,6,2),(6,.3,2),
            (2,8,4),(8,2,4),(1,1,8),(5,5,8)]
    low=[case(*p,240) for p in params]
    high=[case(*p,480) for p in params]
    diffs=[max(abs(a["trial_ratio"]-b["trial_ratio"]),
               abs(a["beta"]-b["beta"]),
               *(abs(a["relative_moment_deficits"][k]
                    -b["relative_moment_deficits"][k]) for k in ("1","2","4","8")))
           for a,b in zip(low,high)]
    result=dict(symbolic_identities_passed=count,finite_case_count=len(params),
                rigorous_numerical_enclosures=False,
                universal_proof="See note 0256; finite checks do not prove it.",
                moment_claim="Only sampled cases; common-center moment theorem not proved.",
                max_resolution_difference=max(diffs),
                min_sampled_cosine=min(a["minimum_sampled_cosine"] for a in high),
                max_trial_ratio=max(a["trial_ratio"] for a in high),
                min_relative_moment_deficit=min(
                    v for a in high for v in a["relative_moment_deficits"].values()),
                low_resolution=low,high_resolution=high)
    Path(__file__).with_name("harmonic-center-diagnostic.json").write_text(
        json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items()
                      if k not in ("low_resolution","high_resolution")},indent=2))


if __name__=="__main__":
    main()
