"""Independent dual-number expansion and exact SymPy verification."""
from itertools import product
from pathlib import Path
import hashlib,json
import sympy as s

n=5
base=Path(__file__).parent
t=s.symbols('t0:125')
eps=s.Symbol('epsilon')
mu=[[[0]*n for _ in range(n)] for _ in range(n)]
for i,j,k in [(0,1,2),(1,0,3),(0,2,4),(1,3,4),(2,1,4),(3,0,4)]:
    mu[i][j][k]=1
table=[[[mu[i][j][k]+eps*t[(i*n+j)*n+k] for k in range(n)]
        for j in range(n)] for i in range(n)]
unit=[[int(i==j) for j in range(n)] for i in range(n)]


def multiply(a,b):
    return [s.expand(sum(a[i]*b[j]*table[i][j][k] for i,j in product(range(n),repeat=2)))
            for k in range(n)]


equations=[]
for a,b,c in product(unit,repeat=3):
    left=multiply(multiply(a,b),c)
    right=multiply(b,multiply(c,a))
    for x,y in zip(left,right):
        f=s.expand(x-y)
        assert f.subs(eps,0)==0
        equations.append(f.coeff(eps,1))
J,_=s.linear_eq_to_matrix(equations,t)
record=json.loads((base/'check-results.json').read_text())
certificate=record['jacobian_certificate']
minor=J.extract(certificate['row_indices_zero_based'],certificate['column_indices_zero_based'])
assert minor.det(method='domain-ge')==2
assert J.rank()==105
f=s.symbols('f0:25')
G=s.eye(n)+eps*s.Matrix(n,n,f)
H=s.eye(n)-eps*s.Matrix(n,n,f)
orbit_equations=[]
for i,j,k in product(range(n),repeat=3):
    value=sum(G[k,r]*sum(H[a,i]*H[b,j]*mu[a][b][r]
                         for a,b in product(range(n),repeat=2)) for r in range(n))
    orbit_equations.append(s.expand(value).coeff(eps,1))
O,_=s.linear_eq_to_matrix(orbit_equations,f)
assert J*O==s.zeros(625,25)
assert O.rank()==20
certificate=record['orbit_certificate']
assert O.extract(certificate['row_indices_zero_based'],certificate['column_indices_zero_based']).det()==3
a,c,e,h,j=s.symbols('a c e h j')
D=s.Matrix([[a,0,0,0,0],[0,a,0,0,0],[c,h,2*a,0,0],[-c,-h,0,2*a,0],[e,j,c+h,-c-h,3*a]])
assert O*s.Matrix(list(D))==s.zeros(125,1)
assert s.Matrix.hstack(*[s.Matrix(list(D.diff(x))) for x in [a,c,e,h,j]]).rank()==5
result={'status':'passed','construction':'Symbolic dual-number expansion of both nested products and an independent basis-change expansion.',
        'sympy_version':s.__version__,'jacobian_rank_exact':105,'orbit_rank_exact':20,
        'jacobian_minor_exact':2,'orbit_minor_exact':3,'derivation_formula_verified':True,
        'primary_result_sha256':hashlib.sha256((base/'check-results.json').read_bytes()).hexdigest(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(base/'independent-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
