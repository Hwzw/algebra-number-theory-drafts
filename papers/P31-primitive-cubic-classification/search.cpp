// Complete finite witness search for q<1511, characteristic !=3.
#include <iostream>
#include <algorithm>
#include <vector>
#include <array>
#include <numeric>
#include <cassert>
#include <cstdint>
using namespace std;using U=uint64_t;
vector<int> factors(int n){vector<int> v;for(int t=2;t*1LL*t<=n;t++)if(n%t==0){v.push_back(t);while(n%t==0)n/=t;}if(n>1)v.push_back(n);return v;}
struct F{
 int p,d,Q;vector<int> mod;
 F(int a,int b):p(a),d(b){Q=1;for(int i=0;i<d;i++)Q*=p;mod.resize(d);auto fac=factors(Q-1);bool found=false;
 for(int code=1;code<Q;code++){if(code%p==0)continue;int c=code;for(int i=0;i<d;i++){mod[i]=c%p;c/=p;}if(pow(p,Q-1)!=1)continue;bool ok=true;for(int t:fac)if(pow(p,(Q-1)/t)==1){ok=false;break;}if(ok){found=true;break;}}assert(found);}
 int add(int a,int b)const{int z=0,w=1;for(int i=0;i<d;i++){z+=((a%p+b%p)%p)*w;a/=p;b/=p;w*=p;}return z;}
 int neg(int a)const{int z=0,w=1;for(int i=0;i<d;i++){z+=((p-a%p)%p)*w;a/=p;w*=p;}return z;}
 int mul(int a,int b)const{int aa[24]={},bb[24]={};long long v[48]={};assert(d<=24);for(int i=0;i<d;i++){aa[i]=a%p;bb[i]=b%p;a/=p;b/=p;}for(int i=0;i<d;i++)for(int j=0;j<d;j++)v[i+j]+=1LL*aa[i]*bb[j];for(int i=2*d-2;i>=d;i--){int c=(v[i]%p+p)%p;for(int j=0;j<d;j++)v[i-d+j]-=1LL*c*mod[j];}int z=0,w=1;for(int i=0;i<d;i++){z+=((v[i]%p+p)%p)*w;w*=p;}return z;}
 int pow(int a,U n)const{int z=1;while(n){if(n&1)z=mul(z,a);a=mul(a,a);n>>=1;}return z;}
};
using Poly=array<int,3>;
Poly pmul(const F&f,Poly a,Poly b,int lambda){int v[5]={};for(int i=0;i<3;i++)for(int j=0;j<3;j++)v[i+j]=f.add(v[i+j],f.mul(a[i],b[j]));for(int i=4;i>=3;i--){int c=f.neg(v[i]);v[i-3]=f.add(v[i-3],f.mul(c,lambda));v[i-2]=f.add(v[i-2],c);v[i-1]=f.add(v[i-1],c);}return {v[0],v[1],v[2]};}
Poly ppow(const F&f,U n,int l){Poly z={1,0,0},x={0,1,0};while(n){if(n&1)z=pmul(f,z,x,l);x=pmul(f,x,x,l);n>>=1;}return z;}
int main(){vector<pair<int,int>> cases;for(int p=2;p<1511;p++){if(factors(p)!=vector<int>{p}||p==3)continue;int q=p;for(int r=1;q<1511;r++){cases.push_back({p,r});if(q>1510/p)break;q*=p;}}cout<<"{\"cutoff_exclusive\":1511,\"cases\":[";bool first=true;
 for(auto [p,r]:cases){int q=1;for(int j=0;j<r;j++)q*=p;F f(p,2*r);int Q=q*q;U N=U(Q)*Q*Q-1;vector<int> pf;for(int v:{q-1,q+1,q*q+q+1,q*q-q+1})for(int s:factors(v))if(find(pf.begin(),pf.end(),s)==pf.end())pf.push_back(s);U rest=N;for(int s:pf)while(rest%s==0)rest/=s;assert(rest==1);
 int l=1,exponent=-1;Poly one={1,0,0};for(int k=1;k<Q;k++){l=f.mul(l,p);if(gcd(k,Q-1)!=1)continue;if(ppow(f,N,l)!=one)continue;bool ok=true;for(int s:pf)if(ppow(f,N/s,l)==one){ok=false;break;}if(ok){exponent=k;break;}}assert(exponent>0);if(!first)cout<<",";first=false;
 cout<<"{\"q\":"<<q<<",\"p\":"<<p<<",\"r\":"<<r<<",\"Q\":"<<Q<<",\"modulus_low_coefficients\":[";for(int j=0;j<f.d;j++){if(j)cout<<",";cout<<f.mod[j];}cout<<"],\"primitive_constant_exponent\":"<<exponent<<",\"primitive_constant_code\":"<<l<<",\"root_order\":\""<<N<<"\",\"root_order_prime_divisors\":[";for(int j=0;j<(int)pf.size();j++){if(j)cout<<",";cout<<pf[j];}cout<<"],\"all_pass\":true}";cerr<<"q="<<q<<" lambda exponent "<<exponent<<"\n";
 }cout<<"],\"all_pass\":true}\n";
}
