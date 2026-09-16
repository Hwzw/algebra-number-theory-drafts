"""Finite signed-flux diagnostic of note 0205, never a proof."""
import json
from pathlib import Path
import numpy as np
from diagnose_flux_transition import radial

def trigamma(x):
    value=0.
    while x<20:
        value+=1/(x*x);x+=1
    return value+1/x+1/(2*x*x)+1/(6*x**3)-1/(30*x**5)+1/(42*x**7)-1/(30*x**9)+5/(66*x**11)

def main():
    cases=[]
    for fraction in (1.,.5,.001):
        a=.5+(1-fraction)/(4*fraction)
        for s in (-2.,.5,2.):
            target=s**3*trigamma(a)/(2*np.sinh(s/2)**2)
            for ell in (20.,40.,80.,160.):
                rho=np.exp(-ell);flux=s/ell;b=fraction*rho;p=(1-fraction)*rho
                pos=radial(b,p,1.,flux,.002)[0];neg=radial(b,p,1.,-flux,.002)[0]
                scaled=ell**3*(pos-neg)
                cases.append(dict(b_fraction=fraction,s=s,ell=ell,flux=flux,scaled_difference=scaled,
                                  predicted_limit=float(target),absolute_difference=abs(scaled-target)))
    p=Path(__file__).with_name('flux-asymmetry-diagnostics.json')
    p.write_text(json.dumps(dict(status='Unvalidated floating-point diagnostic; not a proof',cases=cases),indent=2)+'\n')
    print(json.dumps([c for c in cases if c['ell']==160.],indent=2))
if __name__=='__main__':main()
