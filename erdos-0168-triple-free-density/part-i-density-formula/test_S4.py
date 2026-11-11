from shapes import *
import sys
forb = sys.argv[1].split(','); maxB=int(sys.argv[2]); maxw=int(sys.argv[3]); tops=[int(x) for x in sys.argv[4].split(',')]
bad = 0; tot = 0
for B in range(0, maxB + 1):
    for gaps in itertools.product([1, 2], repeat=B):
        s = ''.join(map(str, gaps))
        if any(f in s for f in forb if f): continue
        for wl in tops:
            w = [wl]
            for g in reversed(gaps): w.insert(0, w[0] + g)
            if w[0] > maxw: continue
            tot += 1
            t, f = tau_rows(w), formula_rows(w)
            if t != f:
                bad += 1
                if bad <= 8: print("FAIL", w, "gaps", s, "tau", t, "formula", f, "K", Kcounts(w))
print(forb, tops, "tested", tot, "fails", bad)
