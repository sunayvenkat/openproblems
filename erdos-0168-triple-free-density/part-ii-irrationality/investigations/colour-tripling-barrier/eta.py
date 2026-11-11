# compute eta grid via increment rule (exact integer ordering of 2^a3^b)
import sys
from fractions import Fraction as Fr
def increments(a,b):
    if b==0: return []
    if b==1:
        return [(a+1)%3] if a>=3 else [(a+1)%3,(a+2)%3]
    if b==3: return [a%3,(a+2)%3]
    return [(a-b)%3]
def run(LA):
    N=2**LA
    pts=[]
    b=0
    while 3**b<=N:
        a=0
        while 2**a*3**b<=N: pts.append((2**a*3**b,a,b)); a+=1
        b+=1
    pts.sort()
    # Q at t=2 (just below 3): points 1,2 ; Q_vector(2): K counts of {1:(0,0)->0, 2:(1,0)->1}; isolate e=2 (A=1): 2t/3<2<=2 yes -> K[1]-=1
    Q=[1,0,0]
    eta={}
    eta[(0,0)]=0; eta[(1,0)]=0
    for d,a,b in pts:
        if d<3: continue
        inc=increments(a,b); m=min(Q)
        e=int(all(j in inc for j in range(3) if Q[j]==m))
        for j in inc: Q[j]+=1
        eta[(a,b)]=e
    return eta,pts
if __name__=="__main__":
    eta,pts=run(int(sys.argv[1]))
    import pickle; pickle.dump(eta,open('eta%s.pkl'%sys.argv[1],'wb'))
    M=sum(Fr(1,2**a*3**b) for (a,b),e in eta.items() if e)
    print(float(1-M/3))
