# scalar model: order by p*a+q*b (slope q/p for log2 3), tie by sign sigma
import sys
from fractions import Fraction as Fr
from eta import increments
def model(p,q,sigma,Amax,Bmax):
    pts=[(p*a+q*b, sigma*b, a,b) for a in range(Amax) for b in range(Bmax)]
    pts.sort()
    # need Q at "t just below 3": points (0,0),(1,0) ; isolate rule handled by increments; start Q=[1,0,0]
    Q=[1,0,0]; eta={}
    eta[(0,0)]=0; eta[(1,0)]=0
    for g,_,a,b in pts:
        if (a,b) in ((0,0),(1,0)): continue
        inc=increments(a,b); m=min(Q)
        eta[(a,b)]=int(all(j in inc for j in range(3) if Q[j]==m))
        for j in inc: Q[j]+=1
    return eta
if __name__=="__main__":
    p,q,s=map(int,sys.argv[1:4])
    A,B=9*q,9*p
    e=model(p,q,s,A+3*q,B+3*p)
    # completeness: points valid only if all points with smaller grade present: grade < min(p*(A+3q), q*(B+3p))
    gmax=min(p*(A+3*q),q*(B+3*p))
    bad=[(a,b) for a in range(A) for b in range(B) if p*(a+3*q)+q*b<gmax and e[(a+3*q,b)]!=e[(a,b)] and b>=4]
    bad2=[(a,b) for a in range(A) for b in range(4,B) if p*a+q*(b+3*p)<gmax and e[(a,b+3*p)]!=e[(a,b)]]
    print('horiz period violations',len(bad), bad[:5]); print('vert violations',len(bad2),bad2[:5])
