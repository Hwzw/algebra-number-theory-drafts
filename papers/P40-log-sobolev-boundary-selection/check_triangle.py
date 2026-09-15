#!/usr/bin/env python3
"""Exact auxiliary checks for Proposition 8.1; not a proof of Theorem 1.1.

The manuscript gives the hand proof. This script independently integrates its
trigonometric polynomial over barycentric triangle coordinates.
"""
from collections import Counter
import json
from pathlib import Path
import sympy as s

frequencies = [(2, 1), (1, 2), (1, -1), (-2, -1), (-1, -2), (-1, 1)]
c = 2 * s.pi * s.I / 3
def root(k):
    return [s.Integer(1), (-1 + s.sqrt(3)*s.I)/2,
            (-1 - s.sqrt(3)*s.I)/2][k % 3]
def interval(k):
    return s.Integer(1) if k == 0 else (root(k)-1)/(c*k)
def simplex(a, b):
    if a:
        return (root(a)*interval(b-a)-interval(b))/(c*a)
    if b:
        return -1/(c*b)+(root(b)-1)/(c*b)**2
    return s.Rational(1, 2)

terms = Counter({(0, 0): 1})
checks = []
for power, expected in enumerate([0, s.Rational(3, 2), s.Rational(3, 2)], 1):
    next_terms = Counter()
    for (a, b), count in terms.items():
        for p, q in frequencies:
            next_terms[a+p, b+q] += count
    terms = next_terms
    moment = s.simplify(s.expand(sum(count*simplex(a,b)
                         for (a,b),count in terms.items()) * s.Rational(2,2**power)))
    cell_moment = s.Rational(terms[0,0], 2**power)
    assert moment == expected == cell_moment
    checks.append(dict(power=power, triangle_moment=str(moment),
                       zero_sum_ordered_tuples=terms[0,0]))
x,y=s.symbols('x y', real=True)
v=s.cos(4*s.pi*x/3)+2*s.cos(2*s.pi*x/3)*s.cos(2*s.pi*y/s.sqrt(3))
lam=16*s.pi**2/9
assert s.simplify(s.diff(v,x,2)+s.diff(v,y,2)+lam*v)==0
assert s.simplify(s.diff(v,y).subs(y,0))==0
assert s.simplify(s.expand(((-s.sqrt(3)*s.diff(v,x)+s.diff(v,y)).subs(y,s.sqrt(3)*x)).rewrite(s.exp)))==0
assert s.simplify(s.expand(((s.sqrt(3)*s.diff(v,x)+s.diff(v,y)).subs(y,s.sqrt(3)*(1-x))).rewrite(s.exp)))==0
out=dict(status='all exact auxiliary checks passed', author='Henry Zweiman',
         sympy_version=s.__version__, moments=checks,
         pde_and_three_neumann_conditions=True,
         limitations='Does not verify the main asymptotic theorem, novelty or significance.')
Path(__file__).with_name('triangle-check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
