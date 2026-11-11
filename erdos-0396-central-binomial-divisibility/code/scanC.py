import sys; sys.path.insert(0,'.')
from lemC import *
from itertools import combinations
P=[3,5,7,11,13,17,19,23,29,31]
out=[]
for r in (3,4):
    for c in combinations(P,r):
        m=1
        for p in c: m*=p
        if m>12000: continue
        if phi(m)/m>=0.5: continue
        g,res=piece_report(m,m)
        allg=all(piece_report(m,d)[0] for d in divisors(m) if d<m)
        out.append((m,c,round(phi(m)/m,3),g,allg,res))
for o in sorted(out): print(o)
