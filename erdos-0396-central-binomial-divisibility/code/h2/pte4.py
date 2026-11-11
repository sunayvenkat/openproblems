# Quartics with many completely split fibers: 4-sets of distinct integers a<b<c<d, a+b+c+d=0.
# Group by (e2,e3); e4 values in a group = constants of split fibers. Look for 3- and 4-term APs.
import sys
from collections import defaultdict
R = int(sys.argv[1])
G = defaultdict(set)
for a in range(-R, R+1):
    for b in range(a+1, R+1):
        for c in range(b+1, R+1):
            d = -(a+b+c)
            if d <= c or d > R: continue
            e2 = a*b+a*c+a*d+b*c+b*d+c*d
            e3 = a*b*c+a*b*d+a*c*d+b*c*d
            G[(e2, e3)].add(a*b*c*d)
best = defaultdict(int); ex = {}
for key, S in G.items():
    if len(S) < 3: continue
    L = sorted(S); Ss = set(L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            h = L[j]-L[i]; k = 2
            while L[i]+k*h in Ss: k += 1
            if k >= 3:
                best[k] += 1
                if k not in ex or len(S) > len(G[ex[k]]): ex[k] = key
print('groups', len(G), 'AP counts by length', dict(best))
for k, key in sorted(ex.items()):
    print('len', k, 'key(e2,e3)', key, 'e4 values', sorted(G[key]))
