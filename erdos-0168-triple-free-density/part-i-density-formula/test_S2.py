from shapes import *
bad = 0; tot = 0
for B in range(0, 13):
    for gaps in itertools.product([1, 2], repeat=B):
        for wl in (1, 2):
            w = [wl]
            for g in reversed(gaps): w.insert(0, w[0] + g)
            if w[0] > 22: continue
            tot += 1
            t, f = tau_rows(w), formula_rows(w)
            if t != f:
                bad += 1
                if bad <= 40: print("FAIL", w, "gaps", [w[i]-w[i+1] for i in range(len(w)-1)], "tau", t, "formula", f, "K", Kcounts(w))
print("tested", tot, "fails", bad)
