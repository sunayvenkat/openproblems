import pickle
from rec import H as Hdirect
digits,P,Q,Hc=pickle.load(open('actual.pkl','rb'))
# spot-check recurrence vs direct sum
for (r,s),h in list(Hc.items())[:400]:
    if s<3000: assert Hdirect(r,s)==h,(r,s)
OK={(0,1,(1,0)),(1,1,(1,0)),(2,0,(2,1)),(2,2,(2,0)),(1,2,(1,1)),(2,1,(1,0))}
res=[]
for n in range(3,len(P)-1):
    p,q,PP,QQ=P[n],Q[n],P[n+1],Q[n+1]
    r,s=p+PP,q+QQ
    if (r,s) not in Hc: break
    st=(r%3,s%3,Hc[(r,s)])
    nonres=(p+q)%3!=0
    el=nonres and st in OK
    res.append((n,digits[n+1],nonres,st,el))
E=[x for x in res if x[4]]
print('indices examined',len(res),'eligible',len(E))
big=[x for x in res if x[1]>=5]
print('digit>=5 indices',len(big),'of which eligible',sum(x[4] for x in big))
print('eligible & digit>=5 (n,a):',[(x[0],x[1]) for x in big if x[4]][:60])
print('last eligible&big n:',max([x[0] for x in big if x[4]] or [None]))
from collections import Counter
print(Counter((x[3][0],x[3][1],x[3][2] if abs(x[3][2][0])+abs(x[3][2][1])<6 else 'big') for x in res).most_common(30))
pickle.dump(res,open('res.pkl','wb'))
