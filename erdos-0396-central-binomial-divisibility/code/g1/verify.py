# Task (a): exact checks of the mod t^{p1} / t^{2p1} structure and of the last-level window rule.
#   run from code/g1:  python verify.py > verify_out.txt
import sys
from math import comb
sys.path.insert(0, '../agentV'); sys.path.insert(0, '..')
from fastgood import pf, phi, series, first_sign, sqfree_divs
from poly import cyclo, digits

def sqfree_odd(n):
    return n % 2 == 1 and all(n % (p * p) for p in pf(n))

def mu(n):
    return (-1) ** len(pf(n))

def binom_series(a, N):
    # (1+t)^a mod t^(N+1), any integer a
    out, c = [], 1
    for k in range(N + 1):
        out.append(c); c = c * (a - k) // (k + 1)
    return out

def mulser(a, b, N):
    r = [0] * (N + 1)
    for i, x in enumerate(a[:N + 1]):
        if x:
            for j in range(min(len(b), N + 1 - i)): r[i + j] += x * b[j]
    return r

# 1. exact product formula  Phi_{2d}(t) = prod_{e|d} (1+t^e)^{mu(d/e)}  (d odd), via the series code
bad1 = 0
for d in range(1, 400, 2):
    if not sqfree_odd(d): continue
    f = list(cyclo(2 * d)); N = len(f) - 1
    s = series(2 * d, 1, N) if d > 1 else [1, 1]
    bad1 += [int(v) for v in s[:N + 1]] != f
print('1. Phi_{2d}(t) = prod (1+t^e)^mu(d/e): mismatches over odd sqfree d<400:', bad1)

# 2. Phi_{2d}^{-k} == (1+t)^{-k mu}(1 + k mu sum_{q|d} t^q)  mod t^{2 p1}
bad2 = cnt2 = 0
for d in range(3, 3000, 2):
    if not sqfree_odd(d): continue
    ps = pf(d); p1 = ps[0]; m_ = mu(d); N = 2 * p1 - 1
    for k in (1, 2, 3, 5, 8):
        s = [int(v) for v in series(2 * d, -k, N)]
        corr = [0] * (N + 1); corr[0] = 1
        for q in ps:
            if q <= N: corr[q] += k * m_
        pred = mulser(binom_series(-k * m_, N), corr, N)
        bad2 += s != pred; cnt2 += 1
print(f'2. mod t^(2p1) refinement: {cnt2} (d,k) cases, mismatches {bad2}')

# 3. last level of piece d (s = T_d - 1, T_d = m // phi(d)), window start r = m mod phi(d).
#    If r+1 < p1(d): mu(d)=+1 -> first coeff c_{r+1} = (-1)^{r+1} C(r+T_d, T_d-1);
#    mu(d)=-1 -> C(T_d, r+1) if T_d >= r+1, else (if p1(d) < 2 p1(d) window) c_{p1} = -T_d.
bad3 = cnt3 = 0; signs = {}
for m in range(3, 4000, 2):
    if not sqfree_odd(m): continue
    for d in [e for e in range(1, m + 1) if m % e == 0]:
        dl = phi(2 * d); Td = m // dl; r = m - Td * dl
        p1d = pf(d)[0] if d > 1 else 10 ** 9
        if Td < 2 or r + 1 >= p1d or r + 1 >= m: continue
        if mu(d) == 1:
            pi, pv = r + 1, (-1) ** (r + 1) * comb(r + Td, Td - 1)
        elif Td >= r + 1:
            pi, pv = r + 1, comb(Td, r + 1)
        else:
            if p1d >= m: continue
            pi, pv = p1d, -Td
        fs = first_sign(m, d, Td - 1)
        c = series(2 * d, -Td, pi) if d > 1 else binom_series(-Td, pi)
        ok = fs is not None and fs[0] == pi and int(c[pi]) == pv and fs[1] == (1 if pv > 0 else -1)
        bad3 += not ok; cnt3 += 1
        key = (mu(d), 'r=0' if r == 0 else ('Td<=r' if Td <= r else 'Td>r'))
        signs.setdefault(key, set()).add(1 if pv > 0 else -1)
print(f'3. last-level window rule: {cnt3} (m,d) cases with r+1<p1(d), mismatches {bad3}')
print('   sign sets by (mu(d), regime):', {k: sorted(v) for k, v in signs.items()})

# 4. direct digit check (no series): sign of the last nonzero digit among D_1..D_s, s = T_d - 1
bad4 = cnt4 = 0
for m in range(3, 400, 2):
    if not sqfree_odd(m): continue
    xm = [1] + [0] * (m - 1) + [1]
    for d in [e for e in range(1, m + 1) if m % e == 0]:
        dl = phi(2 * d); Td = m // dl
        if Td < 2: continue
        D = digits(xm[:], list(cyclo(2 * d)))
        s = Td - 1
        nz = [k for k in range(1, s + 1) if k < len(D) and D[k]]
        dig = (1 if D[nz[-1]][-1] > 0 else -1) if nz else None
        fs = first_sign(m, d, s)
        bad4 += dig != (fs[1] if fs else None); cnt4 += 1
print(f'4. digit-vs-series sign at the last level: {cnt4} (m,d) with m<400, mismatches {bad4}')
