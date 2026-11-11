import numpy as np
from scipy.optimize import linprog
from shapes import formula_rows, tau_rows
from shapes import sturm_rows
import sys
def lp_cover(w):
    pts = [(a, b) for b, x in enumerate(w) for a in range(x)]
    idx = {p: i for i, p in enumerate(pts)}; S = set(pts)
    T = [(idx[(a,b)], idx[(a+1,b)], idx[(a,b+1)]) for (a,b) in pts if (a+1,b) in S and (a,b+1) in S]
    A = np.zeros((len(T), len(pts)))
    for k, tr in enumerate(T):
        for i in tr: A[k, i] = -1
    r = linprog(np.ones(len(pts)), A_ub=A, b_ub=-np.ones(len(T)), bounds=(0, 1), method='highs')
    return r.fun
for t in [9,18,27,54,81,162,243,486,729,1458,2187,4374,6561,10**5,10**6,10**8]:
    w = sturm_rows(t); f = formula_rows(w); lp = lp_cover(w)
    print(t, "M", f, "LP", round(lp, 4), "M-LP", round(f - lp, 4), "|D|/3", round(sum(w)/3, 3))
