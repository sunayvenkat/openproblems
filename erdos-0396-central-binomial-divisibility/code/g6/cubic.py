# Route (b): n = (X^3 + pX + r)/h.  Shift splits iff it has root a with -3a^2 - 4p = w^2; then r_i = a(N/4 - a^2), N = -4p.
# So for each N = 3a^2 + w^2 collect the values r(a) = a(N - 4a^2)/4 (one per split cubic) and look for 4-term APs.
import sys
from collections import defaultdict
B = int(sys.argv[1])
groups = defaultdict(set)
for a in range(0, B):
    for wv in range(0, 2 * B):
        N = 3 * a * a + wv * wv
        if N == 0: continue
        r = a * (N - 4 * a * a)          # = 4 r(a); sign symmetric
        groups[N].add(r); groups[N].add(-r)
hits = 0
for N, R in groups.items():
    if len(R) < 4: continue
    L = sorted(R)
    S = set(L)
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            d = L[j] - L[i]
            if L[i] + 2 * d in S and L[i] + 3 * d in S:
                hits += 1
                if hits <= 20: print("N =", N, "AP", [L[i] + k * d for k in range(4)])
print("groups", len(groups), "4-AP hits", hits)
