# Direct test of Lemma W: for the E1 family n=(12x-1)(22x+9), piece P=12x-1 (lam=1, partner 22x+9), prime q,
# x = x_q + q t, t in (T/2,T], T=X/q. B_q = #{t: all coins tails}. Compare with rho^J * T/2 where J=L-1,
# q^{L-1} <= 2 m(T) < q^L, rho=(q+1)/(2q). Report F = 2m(T)/q^{L-1} and relative error.
import sys
from sympy import primerange
X = int(sys.argv[1]); a, b, ap, bp = 12, -1, 22, 9
def coins_tails(n, q):
    t = 2*n
    while True:
        t //= q
        if t == 0: return True
        if t & 1: return False
rows = []
for q in primerange(int(sys.argv[2]), int(sys.argv[3])):
    if 12*22*130 % q == 0: continue
    xq = (-b * pow(a, -1, q)) % q
    T = X // q
    def m_of(t): x = xq + q*t; return (a*x+b)//q * (ap*x+bp)
    mT = m_of(T); L = 1
    while q**L <= 2*mT: L += 1
    J = L - 1; F = 2*mT / q**(L-1)
    cnt = sum(1 for t in range(T//2+1, T+1) if coins_tails(m_of(t)*q, q))  # n = q*m
    pred = ((q+1)/(2*q))**J * (T - T//2)
    rows.append((q, L, round(F, 2), cnt, round(pred, 1), round(cnt/pred - 1, 3)))
for r in rows: print(r)
