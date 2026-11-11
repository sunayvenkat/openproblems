import sys
sys.path.insert(0,r"../../../part-i-density-formula")
from fractions import Fraction as Fr
from c_digits import enclosure
lo,hi,n,ones,tau=enclosure(10**int(sys.argv[1]))
Zlo,Zhi=9*lo-6,9*hi-6
def cf(x,n):
    out=[]
    for _ in range(n):
        a=x.numerator//x.denominator; out.append(a); x=x-a
        if x==0: break
        x=1/x
    return out
A=cf(Zlo,400); B=cf(Zhi,400)
k=0
while k<min(len(A),len(B)) and A[k]==B[k]: k+=1
print('certified CF terms',k); print(A[:k])
print('max',max(A[:k]))
