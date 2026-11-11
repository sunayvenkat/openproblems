from shapes import *
import sys
bad = 0; tot = 0
for B in range(0, 9):
    for gaps in itertools.product([1, 2], repeat=B):
        for wl in range(1, 8):
            w = [wl]
            for g in reversed(gaps): w.insert(0, w[0] + g)
            if sum(w) > 60: continue
            tot += 1
            if tau_rows(w) != formula_rows(w):
                bad += 1
                if bad <= 25: print("FAIL", w, "tau", tau_rows(w), "formula", formula_rows(w), "K", Kcounts(w))
print("class S tested", tot, "fails", bad)
