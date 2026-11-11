# Split depressed cubics x^3 - 3N x - e3 <-> rational (u,v,w), u+v+w=0, u^2+uv+v^2 = 3N, e3 = uvw.
# Rational points: (U,V,W) coprime, u=U/W, v=V/W. Group by N = (U^2+UV+V^2)/(3W^2); within a group look for 4-term APs of e3.
import sys
from math import gcd
from fractions import Fraction as Fr
from collections import defaultdict
H = int(sys.argv[1])
groups = defaultdict(set)
for W in range(1, H+1):
    for U in range(-H, H+1):
        for V in range(U, H+1):          # unordered pair (u,v) -> same triple up to permutation
            if gcd(gcd(abs(U), abs(V)), W) != 1: continue
            Q = U*U + U*V + V*V
            if Q == 0: continue
            g = gcd(Q, 3*W*W); key = (Q//g, 3*W*W//g)
            groups[key].add(Fr(-U*V*(U+V), W**3))
n3 = n4 = 0; big = 0; ex4 = []
for key, S in groups.items():
    if len(S) < 4: continue
    L = sorted(S); big = max(big, len(L))
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            d = L[j] - L[i]
            if L[i] + 2*d in S:
                n3 += 1
                if L[i] + 3*d in S:
                    n4 += 1
                    if len(ex4) < 10: ex4.append((key, L[i], d))
print('H', H, 'groups', len(groups), 'largest group', big, '3-APs', n3, '4-APs', n4)
for e in ex4: print('  N =', Fr(*e[0]), 'start', e[1], 'step', e[2])
