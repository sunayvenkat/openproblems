"""§4.2 irreducibility: sympy check on small families, and the k=7 necessity example for the log2 condition."""
import sys
from math import prod
from sympy import symbols, cyclotomic_poly, factor_list, Poly
from famplus import family
from lemC import divisors
from verify396 import vp
B = symbols('B')
for k, ms in [(1, [3, 5]), (1, [5, 3]), (2, [3, 5, 7])]:
    M0, L, c, e = family(k, ms)
    red = []
    for j in range(1, k + 2):
        m = ms[j - 1]; r = L // m
        for d in divisors(m):
            f = cyclotomic_poly(2 * d, c[j] * B**r)
            fl = factor_list(f)[1]
            if len(fl) != 1 or fl[0][1] != 1: red.append((j, d, len(fl)))
    print(f"k={k} m={ms} M0=2^{e.get(2)}*3^{e.get(3, 0)}: reducible pieces {red}")
# necessity of 'prime factors of m_j > log2(k+1)': k=7, m_8 = 3 (8/1 = 2^3)
k = 7; ms = [5, 7, 11, 13, 17, 19, 23, 3]; L = prod(ms)
def crt_e(p):
    return next(x for x in range(1, L + 1) if all((x - vp(j, p)) % ms[j - 1] == 0 for j in range(1, k + 2)))
# solve each e_p by CRT (pairwise coprime moduli)
from sympy.ntheory.modular import crt
E = {p: int(crt(ms, [vp(j, p) % ms[j - 1] for j in range(1, k + 2)])[0]) for p in (2, 3, 5, 7)}
c1exp = {p: E[p] // ms[0] for p in E}
print("k=7, m_8=3: e_p =", E, " exponents of c_1 =", c1exp, " all divisible by 3:", all(v % 3 == 0 for v in c1exp.values()),
      " 3 | r_1 = L/5:", (L // 5) % 3 == 0)
print("  => A_1 = c_1 B^{r_1} = y^3, so Phi_2(A_1) = y^3+1 = (y+1)(y^2-y+1) is REDUCIBLE in B")
