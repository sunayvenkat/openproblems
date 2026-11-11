exec(open('tail.py').read())
import pickle,random
from collections import Counter
digits,P,Q,Hc=pickle.load(open('actual.pkl','rb'))
def analyze(ds):
    pts=run(ds)
    Hd={}
    for L,U in pts:
        Hd[(L[0],L[1])]=L[2];Hd[(U[0],U[1])]=U[2]
    p=[0,1];q=[1,0]
    for a in ds: p.append(a*p[-1]+p[-2]); q.append(a*q[-1]+q[-2])
    p=p[2:];q=q[2:]
    rows=[]
    for n in range(2,len(p)-2):
        r,s=p[n]+p[n+1],q[n]+q[n+1]
        if (r,s) not in Hd: break
        st=(r%3,s%3,Hd[(r,s)])
        t=None if (p[n]+q[n])%3==0 else ((p[n-1]+q[n-1])*pow((p[n]+q[n])%3,-1,3))%3
        nonres=(p[n]+q[n])%3!=0
        rows.append((n,ds[n+1],t,nonres and st in OKB,nonres and st in OKS,st,Hd[(p[n],q[n])]))
    return rows
# find actual index with t_n==1
rows=analyze(digits[:60])
c=[r for r in rows if r[2]==1]
print('actual t=1 indices',[r[0] for r in c][:10])
n0=c[2][0]
random.seed(1)
for trial in range(5):
    ds=digits[:n0+1]+[random.choice([3,6,9]) for _ in range(40)]
    rr=[r for r in analyze(ds) if r[0]>=n0]
    print('trial',trial,'t values',Counter(r[2] for r in rr),'bal elig',sum(r[3] for r in rr),'res elig',sum(r[4] for r in rr),
          'bal&a>=5',sum(r[3] and r[1]>=5 for r in rr))
    print('  mediant states',Counter(r[5] for r in rr).most_common(6))
