# For m = 3 mod 4: which levels t give a carry for F(y) and F(-y) (Aurifeuillean pieces of (m y^2)^m + 1)
import sys
from frac import test
from aurif3 import aur3, phi
ms=[int(a) for a in sys.argv[1:]] or [3,15,39,51,87,111,123,159,183,219,267,291]
for m in ms:
    F=aur3(m); Fm=[v*(-1)**i for i,v in enumerate(F)]
    L=(2*m)//phi(m)
    res={}
    for name,FF in (('F+',F),('F-',Fm)):
        res[name]=[]
        for t in range(2,L+1):
            f0,sg,c=test(m,FF,t,1)
            assert f0==0 and c==(sg<0), (m,name,t,f0,sg,c)
            res[name].append((t,'C' if c else '-'))
    both = any(c=='C' for _,c in res['F+']) and any(c=='C' for _,c in res['F-'])
    print(m, 'levels', list(range(2,L+1)), res, 'BOTH' if both else '')
