"""Exact diagnostics for the manuscript; finite tests do not prove the general theorem."""
from itertools import product
from pathlib import Path
import json,time

class Field:
    def __init__(self,p,f):
        self.p=p;self.f=f;self.n=len(f)-1;self.q=p**self.n
        digs=lambda a:[a//p**i%p for i in range(self.n)]
        encode=lambda c:sum((v%p)*p**i for i,v in enumerate(c))
        self.add=[[encode([(x+y)%p for x,y in zip(digs(a),digs(b))])for b in range(self.q)]for a in range(self.q)]
        self.neg=[encode([-v for v in digs(a)])for a in range(self.q)]
        self.mul=[]
        for a in range(self.q):
            row=[]
            for b in range(self.q):
                c=[0]*(2*self.n-1)
                for i,x in enumerate(digs(a)):
                    for j,y in enumerate(digs(b)):c[i+j]+=x*y
                for k in range(len(c)-1,self.n-1,-1):
                    v=c[k]%p
                    for j in range(self.n+1):c[k-self.n+j]-=v*f[j]
                row.append(encode(c[:self.n]))
            self.mul.append(row)
        for a in range(1,self.q):assert any(self.mul[a][b]==1 for b in range(1,self.q))
    def sub(self,a,b):return self.add[a][self.neg[b]]
    def points(self,n):
        for i in range(n+1):
            for tail in product(range(self.q),repeat=n-i):yield (0,)*i+(1,)+tail

def grids():
    result=[];tested=0
    for p,f in [(3,[0,1]),(2,[1,1,1]),(5,[0,1]),(7,[0,1]),(2,[1,1,0,1]),(3,[1,0,1]),(11,[0,1])]:
        K=Field(p,f);q=K.q;sets=[set(),set(),set()]
        for x in K.points(4):
            tested+=1
            if all(K.mul[x[i]][K.sub(x[i],x[0])]==0 for i in [1,2,3]):sets[0].add(x)
            y=tuple(K.add[x[i]][x[i+1]] for i in range(4))+(x[4],)
            if all(K.mul[y[i]][K.sub(y[i],y[0])]==0 for i in [1,2,3]):sets[1].add(x)
            if all(K.mul[x[i]][x[i]]==0 for i in [1,2,3]):sets[2].add(x)
        expected={(1,a,b,c,t) for a,b,c in product([0,1],repeat=3) for t in range(q)}|{(0,0,0,0,1)}
        assert sets[0]==expected
        assert len(sets[1])==8*q+1
        assert len(sets[2])==q+1
        result.append({'q':q,'grid_points':len(sets[0]),'transformed_grid_points':len(sets[1]),'nonreduced_line_support_points':len(sets[2])})
    return tested,result

def connected_countermodel():
    result=[]
    for q in [7,11,13]:
        def norm(v):
            z=next(x for x in v if x%q);u=pow(z,-1,q);return tuple(x*u%q for x in v)
        cubic={norm((1,t,t*t,t*t*t))for t in range(q)}|{(0,0,0,1)}
        seen=set(cubic);lines=0
        for s,p in product(range(q),repeat=2):
            if any((t*t-s*t+p)%q==0 for t in range(q)):continue
            u=(1,0,-p,-s*p);v=(0,1,s,s*s-p)
            line={norm(tuple(u[i]+t*v[i]for i in range(4)))for t in range(q)}|{norm(v)}
            assert len(line)==q+1 and not line&seen
            seen|=line;lines+=1
        assert lines==(q*q-q)//2
        D=lines+3;assert len(seen)-D*q-1==q*(q-5)//2
        result.append({'q':q,'lines':lines,'degree':D,'points':len(seen),'excess_over_Dq_plus_one':len(seen)-D*q-1})
    return result

def cases():
    checked=0
    for q in range(3,151):
        for D in range(1,q+6):
            for b in range(D+1):
                ell=D-b
                if b==1:continue
                target=D*q+1
                if b==0:upper=target
                elif b==2:upper=max((D-1)*q+1,ell*(q+1)+1)
                elif b in [3,4]:upper=(D-2)*(q+1)
                else:upper=(D-1)*q+1+ell
                assert upper<=target,(q,D,b,upper,target)
                checked+=1
    return checked

if __name__=='__main__':
    start=time.time();n,grid=grids();result={'all_passed':True,'projective_points_evaluated':n,'field_and_grid_cases':grid,'component_inequality_cases':cases(),'connectedness_countermodels':connected_countermodel(),'scope':'Finite diagnostics of examples and case arithmetic; not a proof of the general geometric theorem.','elapsed_seconds':round(time.time()-start,3)}
    Path(__file__).with_name('check-results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
