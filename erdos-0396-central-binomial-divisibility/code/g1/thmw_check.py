# Thm W (closed form, T=2, rho <= 2p1-3) vs exact top_sign on random prime sets (coefficients depend only on the prime set).
import random
from sympy import primerange
from window import thmW, top_sign
random.seed(1)
cnt = bad = und = 0
for trial in range(300):
    P = random.choice([3, 5, 7, 11, 13, 17, 23, 31, 41])
    pool = list(primerange(P + 1, 6 * P + 60))
    ps = sorted(random.sample(pool, random.randint(2, min(12, len(pool)))))
    for rho in range(1, 2 * ps[0] - 2, 2):
        w = thmW(ps, rho)
        if w is None: und += 1; continue
        r = top_sign(ps, 2, rho)
        cnt += 1; bad += (r[1] < 0) != w
print(f'Thm W vs exact series: {cnt} (prime set, rho) cases decided, mismatches {bad}, undecided by closed form {und}')
