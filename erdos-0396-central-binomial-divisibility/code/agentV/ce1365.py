"""Counterexample to Lemma A / DRAFT data '1365 good': piece d=455 of m=1365.
(1) level test on actual integers at large x; (2) prime pieces Phi_910(x) and their actual carries."""
import random
from famplus import phi_poly, predicted_levels, actual_levels
from verify396 import is_prime
m, d = 1365, 455
print("predicted carry levels (Laurent rule):", sorted(predicted_levels(m, d)))
random.seed(5)
for X0 in (10**3, 10**5, 10**8):
    res = []
    for _ in range(6):
        x = random.randrange(X0, 2 * X0); j = random.randrange(1, 4)
        res.append(sorted(actual_levels(j * (x**m + 1), phi_poly(2 * d, x))))
    print(f"x~{X0}: actual carry levels of j(x^m+1) base Phi_910(x):", res)
found = 0
for x in range(2, 3000):
    q = phi_poly(910, x)
    if is_prime(q):
        n = x**m + 1
        lv = sorted(actual_levels(n, q))
        print(f"x={x}: Phi_910(x) PRIME ({len(str(q))} digits); carry levels of n=x^1365+1 base q: {lv}"
              + ("  -> v_q(C(2n,n))=0 < v_q(n)=1: n NOT in E_0" if not lv else ""), flush=True)
        found += 1
        if found >= 3: break
