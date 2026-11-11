# Eisenstein ints as (x,y) = x+y*w, w^2=-1-w
def mul(a,b):
    x1,y1=a;x2,y2=b
    return (x1*x2-y1*y2, x1*y2+y1*x2-y1*y2)
def wp(k):
    k%=3
    return [(1,0),(0,1),(-1,-1)][k]
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def H(r,s):
    t=(0,0)
    for j in range(s): t=add(t,wp(j+(r*j)//s))
    return t
from fractions import Fraction
from math import gcd
bad=0;tot=0;rules={}
for q in range(1,40):
  for p in range(0,q+1):
    if gcd(p,q)!=1: continue
    for q2 in range(1,40):
      for p2 in range(0,q2+1):
        if p2*q-p*q2!=1: continue  # p/q < p2/q2 neighbors
        m=H(p+p2,q+q2)
        A=add(H(p,q),mul(wp(p+q),H(p2,q2)))
        B=add(H(p2,q2),mul(wp(p2+q2),H(p,q)))
        tot+=1
        rules['lowfirst']=rules.get('lowfirst',0)+(m==A)
        rules['upfirst']=rules.get('upfirst',0)+(m==B)
print(tot,rules)
