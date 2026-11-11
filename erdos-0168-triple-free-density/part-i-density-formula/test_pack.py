from packing import pack_rows
from shapes import tau_rows, formula_rows
import itertools, sys
def sturm_rows(t):
    w = []; b = 0
    while 3**b <= t:
        a = 0
        while 2**a * 3**b <= t: a += 1
        w.append(a); b += 1
    return w
lim = int(sys.argv[1])
sm = sorted(2**a*3**b for a in range(60) for b in range(40) if 2**a*3**b <= lim)
gaps = []
for d in sm:
    w = sturm_rows(d); nu = pack_rows(w); f = formula_rows(w)
    if nu != f: gaps.append((d, nu, f))
print("Sturmian up to", lim, ":", len(sm), "cutoffs; nu != formula at", len(gaps), gaps[:30])
