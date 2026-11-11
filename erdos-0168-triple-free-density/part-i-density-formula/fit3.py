from rowdp import *
import sys
def sturm_rows(t):
    w = []; b = 0
    while 3**b <= t:
        a = 0
        while 2**a * 3**b <= t: a += 1
        w.append(a); b += 1
    return w
for t in [int(x) for x in sys.argv[1:]]:
    w = sturm_rows(t); Us = row_dp(w)
    print("t", t, "rows", w, "tau", int(Us[0][0]))
    for b in range(len(w)):
        U = Us[b]; wb = w[b]
        Pm = [phase_mask(wb, b, j) for j in range(3)]
        A = [int(U[p]) for p in Pm]
        Z = np.arange(1 << wb, dtype=np.int64)
        cand = np.full(1 << wb, 10**9)
        for j in range(3):
            out = Z & ~Pm[j]
            _, pc = popc(None, wb)
            cnt = pc[out]
            cand = np.minimum(cand, A[j] + cnt)
        diff = cand - U
        print(f"  b={b} w={wb} A={A} U(0)={int(U[0])} maxdiff={int(diff.max())} mindiff={int(diff.min())} #mismatch={int((diff!=0).sum())}/{1<<wb}")
