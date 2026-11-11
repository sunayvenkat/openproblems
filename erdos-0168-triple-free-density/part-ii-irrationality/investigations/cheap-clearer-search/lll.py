# LLL probe: small integer c_ij with || sum c_ij 2^{iq}3^{jp} Z || tiny  => hidden cheap clearer
import sys, pickle
from sympy.polys.matrices import DomainMatrix
from sympy import ZZ
sys.set_int_max_str_digits(0)
base = r"../actual-supply-and-denominators"
M = pickle.load(open(base + "/models.pkl", "rb"))
Nz, Dz = M[(79335, 125743)]
PREC = 301900
Zi = (Nz << PREC) // Dz
T = 160
def frac(m):   # round(2^T * {m Z})
    x = (m * Zi) & ((1 << PREC) - 1)
    return x >> (PREC - T)
conv = [(12,19,65),(41,65,84),(53,84,485),(306,485,1054),(665,1054,24727),(15601,24727,50508),(31867,50508,125743)]
for p, q, Q in conv:
    W = q + Q
    mons = [(i, j) for i in range(4) for j in range(4) if (i + j) * q + T + 64 < PREC]
    k = len(mons)
    rows = []
    for t, (i, j) in enumerate(mons):
        r = [0] * (k + 1); r[t] = 1; r[k] = frac(2 ** (i * q) * 3 ** (j * p)); rows.append(r)
    rows.append([0] * k + [1 << T])
    B = DomainMatrix(rows, (k + 1, k + 1), ZZ).lll().to_Matrix().tolist()
    out = []
    for v in B:
        c = v[:k]; last = abs(int(v[k]))
        cost = max(((i + j) for (i, j), ci in zip(mons, c) if ci), default=0)
        out.append((max(abs(int(x)) for x in c).bit_length(), last.bit_length(), cost, [(mons[t], int(c[t])) for t in range(k) if c[t]] if max(abs(int(x)) for x in c) < 100 else '...'))
    out.sort(key=lambda z: (z[0] + z[1]))
    print(f"p/q={p}/{q} W/q={W/q:.2f} k={k} generic bits~{T//(k+1)}; best (coefbits,lastbits,maxdeg,vec):")
    for o in out[:3]: print("   ", o)
    sys.stdout.flush()
