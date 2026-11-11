# group-size distribution and 3-term APs allowing e1 != 0 is same after shift; here count groups with >=3 e4-values.
import sys
from collections import defaultdict, Counter
R = int(sys.argv[1]); G = defaultdict(set)
for a in range(-R, R+1):
    for b in range(a+1, R+1):
        for c in range(b+1, R+1):
            d = -(a+b+c)
            if d <= c or d > R: continue
            G[(a*b+a*c+a*d+b*c+b*d+c*d, a*b*c+a*b*d+a*c*d+b*c*d)].add(a*b*c*d)
C = Counter(len(S) for S in G.values()); print(sorted(C.items()))
big = [(k, sorted(S)) for k, S in G.items() if len(S) >= 4]
print(big[:10])
