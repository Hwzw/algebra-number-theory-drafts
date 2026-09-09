def T(h,p,q):
    delta=sum(h[1:])%p
    out=[0]*q
    out[0]=(-h[1]-delta)%p
    for k in range(2,q):out[q-k]=(-k*(h[k]+(delta if k<=q-2 else 0)))%p
    return out
if __name__ == "__main__":
    for p,r in [(3,2),(3,3),(5,1),(5,2),(7,1),(7,2),(11,1),(13,1),(17,1),(19,1)]:
        q=p**r; h=[0]*q; h[1]=1
        seq=[]
        for n in range(1,51):
            seq.append((-1)**n*(-h[q-2])%p)
            h=T(h,p,q)
        print(q,seq)
