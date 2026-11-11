# Calibration for cubic route: count 3-term and 4-term APs of r-values within one norm class N = 3a^2 + w^2.
import sys
from collections import defaultdict
B = int(sys.argv[1]); groups = defaultdict(set)
for a in range(0, B):
    for wv in range(0, 2 * B):
        N = 3 * a * a + wv * wv
        if N: r = a * (N - 4 * a * a); groups[N] |= {r, -r}
c3 = c4 = 0
for N, R in groups.items():
    if len(R) < 3: continue
    L = sorted(R); S = set(L)
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            d = L[j] - L[i]
            if d and L[i] + 2 * d in S and L[i] + d != 0:
                c3 += 1
                if c3 <= 3: print("3-AP N=%d" % N, L[i], L[j], L[i] + 2 * d)
                if L[i] + 3 * d in S: c4 += 1
print("3-APs", c3, "4-APs", c4)
