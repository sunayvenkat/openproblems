import mpmath
from rec import mul,wp,add,H
mpmath.mp.dps=4000
L2,L3=mpmath.log(2),mpmath.log(3)
alpha=L2/L3
# CF digits, verified at two precisions
def cf(x,n):
    d=[]
    for _ in range(n):
        a=int(mpmath.floor(x)); d.append(a); x=1/(x-a)
    return d
NT=600
d1=cf(alpha,NT)
mpmath.mp.dps=4400
d2=cf(mpmath.log(2)/mpmath.log(3),NT)
k=0
while k<NT and d1[k]==d2[k]: k+=1
NT=k-5
digits=d1[:NT]
print('certified-by-two-precisions digits:',NT, digits[:40])
mpmath.mp.dps=4000
# convergents
p=[0,1];q=[1,0]  # p_{-2}=0,q_{-2}=1 ; p_{-1}=1,q_{-1}=0
for a in digits:
    p.append(a*p[-1]+p[-2]); q.append(a*q[-1]+q[-2])
P=p[2:];Q=q[2:]   # P[n]/Q[n] = n-th convergent, n>=0 ; digits[n]=a_n
# H along convergents: compute H via recurrence of intermediate fractions
Hc={}
Hc[(0,1)]=H(0,1); Hc[(1,1)]=H(1,1)
def Hrec(r,s,lo,hi):
    # lo,hi neighbors (r,s)=lo+hi
    return add(Hc[lo],mul(wp(lo[0]+lo[1]),Hc[hi]))
# walk Stern-Brocot path
lo,hi=(0,1),(1,1)
def less(r,s): # r/s < alpha
    return mpmath.mpf(r)/s<alpha
target=(P[NT-1],Q[NT-1])
steps=0
while True:
    m=(lo[0]+hi[0],lo[1]+hi[1])
    if m[1]>Q[NT-2]: break
    Hc[m]=Hrec(*m,lo,hi)
    if less(*m): lo=m
    else: hi=m
    steps+=1
print('SB steps',steps)
import pickle
pickle.dump((digits,P,Q,Hc),open('actual.pkl','wb'))
