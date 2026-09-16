#!/usr/bin/env python3
"""Finite Fourier consistency check of an auxiliary flat-flux coefficient.

Not interval arithmetic and not a proof of any obstacle theorem.
The obstacle is F(w)=w+epsilon/w, so its boundary is an ellipse.
"""
from pathlib import Path
import json
import numpy as np

def run(epsilon,cutoff):
    samples=8192
    theta=2*np.pi*np.arange(samples)/samples
    speed=np.abs(1-epsilon*np.exp(-2j*theta))
    coeff=np.fft.fft(speed)/samples
    perimeter=float(2*np.pi*coeff[0].real)
    nall=np.fft.fftfreq(samples)*samples
    mask=nall!=0
    harmonic_term=float(2*np.pi/perimeter**2*np.sum(np.abs(coeff[mask])**2/np.abs(nall[mask])))
    modes=np.arange(-cutoff,cutoff+1)
    gram=coeff[(modes[:,None]-modes[None,:])%samples]
    chol=np.linalg.cholesky(gram)
    inv=np.linalg.solve(chol,np.eye(len(modes)))
    results=[]
    for flux in [.02,.01,.005]:
        matrix=(inv*np.abs(modes-flux)[None,:])@inv.conj().T
        eigenvalue=float(np.linalg.eigvalsh(matrix)[0])
        scaled=(eigenvalue-2*np.pi*flux/perimeter)/flux**2
        results.append(dict(flux=flux,eigenvalue=eigenvalue,scaled_quadratic_coefficient=scaled,predicted_limit=-4*np.pi**2*harmonic_term/perimeter))
    return dict(ellipse_parameter=epsilon,cutoff=cutoff,perimeter=perimeter,S_K=harmonic_term,cases=results)
if __name__=='__main__':
    out=dict(status='Floating-point consistency diagnostic, not proof',results=[run(e,n) for e in [.2,.6] for n in [40,80]])
    dest=Path(__file__).with_name('flat-geometric-diagnostics.json');dest.write_text(json.dumps(out,indent=2)+'\n')
    for r in out['results']: print(r['ellipse_parameter'],r['cutoff'],r['cases'][-1])
