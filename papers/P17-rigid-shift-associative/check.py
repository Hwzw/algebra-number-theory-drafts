"""Exact tangent and orbit-rank certificates for a five-dimensional algebra."""
from itertools import product
from pathlib import Path
import hashlib
import json

N=5
TABLE={(0,1,2):1,(1,0,3):1,(0,2,4):1,
       (1,3,4):1,(2,1,4):1,(3,0,4):1}


def c(i,j,k):
    return TABLE.get((i,j,k),0)


def ix(i,j,k):
    return (i*N+j)*N+k


def matrices():
    jac=[]
    for a,b,d,k in product(range(N),repeat=4):
        assert sum(c(a,b,s)*c(s,d,k)-c(d,a,s)*c(b,s,k)
                   for s in range(N))==0
        row=[0]*(N**3)
        for s in range(N):
            row[ix(s,d,k)]+=c(a,b,s)
            row[ix(a,b,s)]+=c(s,d,k)
            row[ix(b,s,k)]-=c(d,a,s)
            row[ix(d,a,s)]-=c(b,s,k)
        jac.append(row)
    orbit=[]
    for i,j,k in product(range(N),repeat=3):
        orbit.append([int(k==u)*c(i,j,v)-int(i==v)*c(u,j,k)
                      -int(j==v)*c(i,u,k)
                      for u,v in product(range(N),repeat=2)])
    assert all(sum(row[s]*orbit[s][j] for s in range(N**3))==0
               for row in jac for j in range(N*N))
    return jac,orbit


def pivots(matrix,p=1000003):
    A=[[x%p for x in row] for row in matrix]
    labels=list(range(len(A)))
    r=0; columns=[]; chosen=[]
    for j in range(len(A[0])):
        pivot=next((i for i in range(r,len(A)) if A[i][j]),None)
        if pivot is None:
            continue
        A[r],A[pivot]=A[pivot],A[r]
        labels[r],labels[pivot]=labels[pivot],labels[r]
        chosen.append(labels[r]);columns.append(j)
        u=pow(A[r][j],-1,p)
        A[r]=[x*u%p for x in A[r]]
        for i in range(r+1,len(A)):
            x=A[i][j]
            if x:
                A[i]=[(a-x*b)%p for a,b in zip(A[i],A[r])]
        r+=1
        if r==len(A):
            break
    return chosen,columns


def det_bareiss(matrix):
    A=[r[:] for r in matrix]
    n=len(A); prev=1; sign=1
    for k in range(n-1):
        r=next((i for i in range(k,n) if A[i][k]),None)
        if r is None:
            return 0
        if r!=k:
            A[k],A[r]=A[r],A[k];sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=A[i][j]*pivot-A[i][k]*A[k][j]
                assert numerator%prev==0
                A[i][j]=numerator//prev
            A[i][k]=0
        prev=pivot
    return sign*A[-1][-1]


def certificate(A):
    rows,cols=pivots(A)
    determinant=det_bareiss([[A[i][j] for j in cols] for i in rows])
    assert determinant
    return {'rank_lower_bound':len(rows),'row_indices_zero_based':rows,
            'column_indices_zero_based':cols,'minor_determinant':determinant}


def main():
    J,O=matrices()
    jc,oc=certificate(J),certificate(O)
    assert jc['rank_lower_bound']==105
    assert oc['rank_lower_bound']==20
    assert jc['rank_lower_bound']+oc['rank_lower_bound']==N**3
    result={'dimension':N,'table_zero_based':[[*key,value] for key,value in TABLE.items()],
            'shift_identity_all_basis_triples':True,
            'nonassociativity_witness':'(e1 e1)e2=0, e1(e1 e2)=e5',
            'jacobian_shape':[len(J),len(J[0])],
            'orbit_differential_shape':[len(O),len(O[0])],
            'jacobian_certificate':jc,'orbit_certificate':oc,
            'jacobian_times_orbit_exactly_zero':True,
            'characteristic_zero_tangent_dimension':20,
            'characteristic_zero_orbit_dimension':20,
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_name('check-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'jacobian_rank':105,'orbit_rank':20,
                      'jacobian_minor':jc['minor_determinant'],
                      'orbit_minor':oc['minor_determinant']}))


if __name__=='__main__':
    main()
