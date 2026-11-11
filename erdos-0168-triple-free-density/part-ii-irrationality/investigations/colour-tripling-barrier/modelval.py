import math
from fractions import Fraction as Fr
from model import model
def val(p,q,s,verbose=False):
    e=model(p,q,s,13*q,13*p+4)
    def row(b):
        a0=next(a0 for a0 in range(3*q) if all(e[(a,b)]==e[(a+3*q,b)] for a in range(a0,6*q)))
        head=sum(Fr(1-3*e[(a,b)],2**a) for a in range(a0))
        per=sum(Fr(1-3*e[(a,b)],2**a) for a in range(a0,a0+3*q))/(1-Fr(1,2**(3*q)))
        return head+per,a0
    Z=0
    for b in range(4):
        r,a0=row(b); Z+=r/3**b
        if a0 and verbose: print('  low row',b,'period starts',a0)
    for b in range(4,4+3*p):
        for a in range(3*q): assert e[(a,b)]==e[(a,b+3*p)]
    Z+=sum(row(b)[0]/3**b for b in range(4,4+3*p))/(1-Fr(1,3**(3*p)))
    return Z
if __name__=="__main__":
  for p,q in [(5,8),(12,19),(41,65),(53,84)]:
    for s in (1,-1):
        Z=val(p,q,s,True); d=Z.denominator
        D=27*(2**(3*q)-1)*(3**(3*p)-1)
        print(p,q,s,'den bits',d.bit_length(),'D bits',D.bit_length(),'divides',D%d==0,'Z~%.15f'%float(Z))
