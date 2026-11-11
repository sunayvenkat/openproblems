# Cubics f = x^3 - N x + c splitting over Z: roots {u, v, -u-v}, N = u^2+uv+v^2, c = uv(u+v).
# Find N whose split-constants contain a k-term AP (then n(x) = (f(x)-c0)/D has n-i split for i<k).
import sys
from collections import defaultdict
NM = int(sys.argv[1]); C = defaultdict(set); B = int((4*NM/3)**0.5)+2
for u in range(-B, B+1):
    for v in range(u, B+1):
        N = u*u+u*v+v*v
        if 0 < N <= NM: C[N].add(u*v*(u+v))
best = []
for N, S in C.items():
    if len(S) < 8: continue
    L = sorted(S); Ss = set(L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            d = L[j]-L[i]; k = 2
            while L[i]+k*d in Ss: k += 1
            if k >= 4: best.append((k, N, L[i], d))
best.sort(reverse=True); print(len(best)); print(best[:15])
