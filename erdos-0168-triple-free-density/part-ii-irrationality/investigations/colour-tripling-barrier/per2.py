import pickle, math, itertools
eta=pickle.load(open('eta700.pkl','rb'))
th=math.log2(3); LMAX=700
def L(a,b): return a+b*th
pts=sorted(eta.items(), key=lambda kv: L(*kv[0]))
def firstmis(m,n,bmin=4):
    for (a,b),e in pts:
        if b<bmin: continue
        k=(a+m,b+n)
        if k[1]<bmin or k[0]<0: continue
        if L(*k)>=LMAX-1 or L(a,b)>=LMAX-1: continue
        if k in eta and eta[k]!=e: return round(L(a,b),1)
    return None
Q=[1,2,3,8,19,65,84,485]; P=[1,1,2,5,12,41,53,306]
res=[]
for k in range(3,7):
  for i in (1,2,3):
    for j in (-3,-2,-1,0,1,2,3):
      m,n=i*Q[k],j*P[k]
      fm=firstmis(m,n); res.append((fm if fm else 999,(m,n),k,i,j))
res.sort(reverse=True)
for r in res[:25]: print(r)
