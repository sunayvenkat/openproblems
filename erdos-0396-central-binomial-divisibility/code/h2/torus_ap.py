# All rational beta with Norm(beta)=N: beta = beta0 * zeta^2 / N(zeta), zeta in Z[w] primitive. Split cubic x^3-3Nx-e3 iff e3 = Tr(beta^3).
# Search: (i) ratio-3 pairs (symmetric 4-AP -3a,-a,a,3a), (ii) general 4-APs (O(n^2), smaller H).
import sys
from math import gcd
from fractions import Fraction as Fr
def mul(p, q): return (p[0]*q[0] - p[1]*q[1], p[0]*q[1] + p[1]*q[0] - p[1]*q[1])
def norm(p): return p[0]*p[0] - p[0]*p[1] + p[1]*p[1]
def tr(p): return 2*p[0] - p[1]
def values(b0, H):
    b03 = mul(mul(b0, b0), b0); S = set()
    for c in range(-H, H+1):
        for d in range(0, H+1):
            if d == 0 and c <= 0: continue
            if gcd(abs(c), d) != 1: continue
            z = (c, d); z2 = mul(z, z); z6 = mul(mul(z2, z2), z2)
            v = Fr(tr(mul(b03, z6)), norm(z)**3); S.add(v); S.add(-v)
    return S
H = int(sys.argv[1]); H2 = int(sys.argv[2])
seen = set()
for a in range(1, 9):
    for b in range(0, a+1):
        N = norm((a, b))
        if N in seen: continue
        seen.add(N)
        S = values((a, b), H)
        r3 = [v for v in S if v != 0 and 3*v in S]
        r2 = [v for v in S if v != 0 and 2*v in S]
        msg = 'N=%d pts=%d ratio3=%d ratio2=%d zero=%s' % (N, len(S), len(r3), len(r2), 0 in S)
        if r3: msg += ' EX3 ' + str(r3[:3])
        if 0 in S and r2: msg += ' EX2 ' + str(r2[:3])
        # general 4-AP on smaller set
        S2 = values((a, b), H2); L = sorted(S2); n4 = 0; ex = None
        for i in range(len(L)):
            for j in range(i+1, len(L)):
                dlt = L[j]-L[i]
                if L[i]+2*dlt in S2 and L[i]+3*dlt in S2:
                    n4 += 1; ex = ex or (L[i], dlt)
        msg += ' | 4AP(H=%d, pts=%d)=%d %s' % (H2, len(S2), n4, ex or '')
        print(msg, flush=True)
