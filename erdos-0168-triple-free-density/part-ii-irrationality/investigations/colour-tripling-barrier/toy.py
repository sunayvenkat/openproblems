from fractions import Fraction as Fr
import math
# T1 = sum_{b>=0} 3^-b 2^-floor(b*log2 3)
def fl(b):  # floor(b log2 3) exactly
    x=3**b; return x.bit_length()-1
N=400
T=sum(Fr(1,3**b*2**fl(b)) for b in range(N))
# continued fraction
def cf(x,n):
    out=[]
    for _ in range(n):
        a=x.numerator//x.denominator; out.append(a); x=x-a
        if x==0: break
        x=1/x
    return out
c=cf(T,60)
print([ (k,a.bit_length()) for k,a in enumerate(c) if a>50])
print(c[:30])
