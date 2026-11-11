# Probe outside the (2^q,3^p) span: clearers d = sum c_m * 2^{E2(m)} 3^{E3(m)} whose exponents mix THREE
# consecutive convergents (n-1, n, n+1), restricted to cost below the window W = q_n + q_{n+1}.
# A cheap clearer would be a lattice vector with O(1) coefficients and ~zero last coordinate.
import sys, pickle, time, itertools, math
from sympy.polys.matrices import DomainMatrix
from sympy import ZZ
sys.set_int_max_str_digits(0)
base = r"../actual-supply-and-denominators"
M = pickle.load(open(base + "/models.pkl", "rb"))
Nz, Dz = M[(79335, 125743)]
PREC = 301900
Zi = (Nz << PREC) // Dz
L3 = math.log2(3)
CAP = 150
C = [(1,1),(1,2),(2,3),(5,8),(12,19),(41,65),(53,84),(306,485),(665,1054),(15601,24727),(31867,50508),(79335,125743)]
for n in range(4, 11):
    (p0, q0), (p1, q1), (p2, q2) = C[n - 1], C[n], C[n + 1]
    W = q1 + q2
    mons = set()
    for e in itertools.product(range(3), range(4), range(2)):
        E2 = e[0] * q0 + e[1] * q1 + e[2] * q2
        for f in itertools.product(range(3), range(4), range(2)):
            E3 = f[0] * p0 + f[1] * p1 + f[2] * p2
            if E2 + E3 * L3 <= 1.01 * W: mons.add((E2, E3))
    mons = sorted(mons, key=lambda m: m[0] + m[1] * L3)
    full = len(mons)
    if len(mons) > CAP: mons = mons[:CAP]        # keep the cheapest CAP
    k = len(mons); T = 8 * (k + 1)
    assert max(m[0] + m[1] * L3 for m in mons) + T + 64 < PREC
    rows = []
    for t, (E2, E3) in enumerate(mons):
        x = ((2 ** E2 * 3 ** E3) * Zi) & ((1 << PREC) - 1)
        r = [0] * (k + 1); r[t] = 1; r[k] = x >> (PREC - T); rows.append(r)
    rows.append([0] * k + [1 << T])
    t0 = time.time()
    B = DomainMatrix(rows, (k + 1, k + 1), ZZ).lll().to_Matrix().tolist()
    def dval(v): return sum(int(v[t]) * 2 ** mons[t][0] * 3 ** mons[t][1] for t in range(k) if v[t])
    cand = sorted(B, key=lambda v: max(abs(int(x)) for x in v))
    zero = sum(1 for v in B if dval(v) == 0)
    best = next(v for v in cand if dval(v) != 0)
    mx = max(abs(int(x)) for x in best)
    sup = [(mons[t], int(best[t])) for t in range(k) if best[t]]
    cov = max(m[0] + m[1] * L3 for m in mons) / W
    print(f"n={n} p/q={p1}/{q1} W={W} monomials={k}/{full} cost covered={cov:.2f}W T={T}; exact-zero relations in basis={zero}; "
          f"shortest d!=0 vector: max-entry bits={mx.bit_length()} support={len(sup)} last={abs(int(best[k])).bit_length()} bits ({time.time()-t0:.0f}s)", flush=True)
    if mx.bit_length() <= 4: print("   CANDIDATE:", sup[:12])
