# Per-event laws at X=1e15, best E1 family: medium q (theta<.45): bad vs 2^-(L-1); theta in (.55,.65): bad vs fs/2.
import random, math
from collections import defaultdict
from sympy import factorint
from verify import carries
forms = [(12,-1),(22,9),(11,-1),(12,5)]; fs = [0, .2, .2, 0]
random.seed(3); X = 10**15; med = defaultdict(lambda: [0, 0, 0.0]); mid = [[0, 0] for _ in forms]
for _ in range(6000):
    x = random.randrange(X//2, X); P = [a*x+b for a, b in forms]; n = P[0]*P[1]
    for j, Pj in enumerate(P):
        for q, e in factorint(Pj).items():
            if e > 1 or q < 1000: continue
            th = math.log(q)/math.log(Pj); bad = carries(n, q) < 1
            if th < .45:
                L = int(math.log(2*n)/math.log(q)); m = med[L]; m[0] += 1; m[1] += bad; m[2] += 2.0**(1-L)
            elif .6 < th < .65: mid[j][0] += 1; mid[j][1] += bad
for L in sorted(med):
    t, b, p = med[L]; print('L', L, 'events', t, 'bad rate %.4f' % (b/t), 'model %.4f' % (p/t))
print('mid bucket bad rate per form:', [round(b/t, 3) for t, b in mid], 'model fs/2:', [f/2 for f in fs])
