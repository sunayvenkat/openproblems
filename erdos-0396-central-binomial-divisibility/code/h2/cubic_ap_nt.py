# cubic fibers x^3 - N x + c split: roots (u, v, -u-v), N=u^2+uv+v^2, c=uv(u+v). Nontrivial 3-APs (middle != 0) and any 4-APs.
import sys
from collections import defaultdict
NM = int(sys.argv[1]); C = defaultdict(set); B = int((4*NM/3)**0.5)+2
for u in range(-B, B+1):
    for v in range(u, B+1):
        N = u*u+u*v+v*v
        if 0 < N <= NM: C[N].add(u*v*(u+v))
ap3 = []; ap4 = 0
for N, S in C.items():
    if len(S) < 3: continue
    L = sorted(S); Ss = set(L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            d = L[j]-L[i]
            if L[i]+2*d in Ss:
                if L[i]+d != 0: ap3.append((N, L[i], d))
                if L[i]+3*d in Ss: ap4 += 1
print('N<=', NM, 'nontrivial 3-APs', len(ap3), ap3[:8], '4-APs', ap4)
