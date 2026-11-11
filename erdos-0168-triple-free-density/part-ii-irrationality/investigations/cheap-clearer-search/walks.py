# True axis walks A_a, B_b (floors of slope 79335/125743 agree with alpha for a<301994, b<190537).
# Coordinates: state z = x + y*w; birth (b>=4) iff u<=0 and v<=0 with u = x-1 (+corr), v = x-y (+corr).
import sys
sys.path.insert(0, r"../actual-supply-and-denominators")
from fastmodel import add, rot, side, HINC, VINC, event, CORR
from collections import Counter
p, q, sign = 79335, 125743, 1
NA, NB = 300000, 190000
A = [(1, 0)]
for a in range(1, NA): A.append(add(A[-1], rot(HINC[side(a, p, q, sign) % 3], -a)))
B = [(1, 0)]
for b in range(1, NB): B.append(add(B[-1], rot(VINC[side(b, q, p, -sign) % 3], -2 * b)))
def uv(z): return (z[0], z[0] - z[1])
for name, W in (("A (horizontal)", A), ("B (vertical)", B)):
    U = [uv(z) for z in W]
    print(name, "steps", len(W), "distinct states", len(set(W)))
    print("   u range", min(t[0] for t in U), max(t[0] for t in U), " v range", min(t[1] for t in U), max(t[1] for t in U))
    c = Counter(U)
    print("   most common (u,v):", c.most_common(8))
    # running extremes at powers of 4
    k = 16
    while k <= len(W):
        seg = U[:k]
        print(f"   first {k}: u in [{min(t[0] for t in seg)},{max(t[0] for t in seg)}], v in [{min(t[1] for t in seg)},{max(t[1] for t in seg)}]")
        k *= 4
import pickle
pickle.dump((A, B), open(r"(local scratch path, not included)", "wb"))
