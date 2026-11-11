import math, sys
from math import gcd
from sympy import cyclotomic_poly
from modelval import val
al=math.log(2)/math.log(3)
tot=ok=fail=skip=0
for q in range(9,int(sys.argv[1])):
    for p in (math.floor(q*al), math.ceil(q*al)):
        if gcd(p,q)!=1 or (p+q)%3==0: continue
        if not (0.6<p/q<0.667): continue
        for s in (1,-1):
            try: Z=val(p,q,s)
            except (AssertionError,StopIteration): skip+=1; continue
            d=Z.denominator; tot+=1
            a=int(cyclotomic_poly(3*q,2)); b=int(cyclotomic_poly(3*p,3))
            if d%a==0 and d%b==0: ok+=1
            else: fail+=1; print('FAIL',p,q,s,d%a==0,d%b==0)
print('tested',tot,'ok',ok,'fail',fail,'nonperiodic/skipped',skip)
