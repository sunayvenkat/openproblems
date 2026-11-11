from itertools import combinations
from tau_dp import max_indep
def brute(t):
    pts=[(a,b) for a in range(40) for b in range(30) if 2**a*3**b<=t]
    S=set(pts); idx={p:i for i,p in enumerate(pts)}
    cs=[(idx[(a,b)],idx[(a+1,b)],idx[(a,b+1)]) for (a,b) in pts if (a+1,b) in S and (a,b+1) in S]
    n=len(pts)
    for k in range(n+1):
        for C in combinations(range(n),k):
            c=set(C)
            if all(x in c or y in c or z in c for x,y,z in cs): return k
for t in [1,2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108,128,144]:
    mi,n=max_indep(t); assert n-mi==brute(t),(t,n-mi,brute(t))
print("brute ok")
