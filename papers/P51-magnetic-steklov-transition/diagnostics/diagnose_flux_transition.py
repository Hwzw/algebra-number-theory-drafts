"""Floating-point checks of the proposed uniform small-flux radial normal form.
Not a proof or an interval-validated computation. Uses the defining integral,
not the Kummer connection formula used in the hand proof.
"""
import json
from pathlib import Path
import numpy as np
from diagnose_radial_transition import digamma

NODES, WEIGHTS = np.polynomial.legendre.leggauss(24)
NODES, WEIGHTS = (NODES + 1) / 2, WEIGHTS / 2

def gamma_quotient_shift(a, flux):
    # Integral of digamma avoids cancellation of lgamma at large a or small flux.
    c = -sum(w * (digamma(1-flux*t)+digamma(1+flux*t))
             for t,w in zip(NODES,WEIGHTS))
    h = sum(w * digamma(a+flux*t) for t,w in zip(NODES,WEIGHTS))
    return c+h

def radial(b,p,radius,flux,step):
    a=.5+p/(4*b);z=b*radius**2;eta=a*z
    lo,hi=np.log(eta)-100.,np.log(100.)
    n=int(np.ceil((hi-lo)/step))+1
    y=np.linspace(lo,hi,n);x=np.exp(y)
    weight=np.exp(-x-a*np.log1p(z/x)-flux*np.log1p(x/z))
    integral=np.trapezoid(weight,y);moment=np.trapezoid(x*weight,y)
    value=(flux+z+2*moment/integral)/radius
    denominator=-np.log(z)-gamma_quotient_shift(a,flux)
    model=(2/denominator if flux==0 else flux/np.tanh(flux*denominator/2))/radius
    return float(value),float(model),float(denominator)

def main():
    cases=[]
    for radius in (1.,2.3):
        for rho in (1e-3,1e-6,1e-10):
            for fraction in (1.,.5,1e-6,1e-12):
                b,p=fraction*rho,(1-fraction)*rho
                for flux in (-.25,-.05,-1e-8,0.,1e-8,.05,.25):
                    coarse=radial(b,p,radius,flux,.004)
                    val,model,den=radial(b,p,radius,flux,.002)
                    cases.append(dict(radius=radius,rho=rho,b_fraction=fraction,flux=flux,
                        integral_value=val,model=model,denominator=den,
                        error_over_rho=(val-model)/rho,
                        refinement_difference=abs(val-coarse[0])))
    result=dict(status='Unvalidated floating-point consistency checks, not proof',
        formula='sigma = nu/R coth(nu D_nu/2), continuous at nu=0',
        case_count=len(cases),max_refinement_difference=max(c['refinement_difference'] for c in cases),
        max_abs_error_over_rho=max(abs(c['error_over_rho']) for c in cases),cases=cases)
    Path(__file__).with_name('flux-transition-diagnostics.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))
if __name__=='__main__':main()
