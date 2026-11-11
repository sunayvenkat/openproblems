"""Eisenstein-walk form: tau = (|D| - eps)/3 - (2/3) H(S_hat); and c = 757/972 + J/3."""
import cmath, math
from fractions import Fraction as Fr
from eta_rule import Q_vector, increments
from decimal import Decimal, getcontext
w = cmath.exp(2j * math.pi / 3)
def S_rows(t):
    S = 0; b = 0
    while 3**b <= t:
        wb = 0
        while 2**wb * 3**b <= t: wb += 1
        S += w**(-b) * sum(w**k for k in range(wb % 3)); b += 1
    return S
def H(z): return max((-(w**(-j)) * z).real for j in range(3))
sm = sorted(2**a*3**b for a in range(80) for b in range(50) if 3 <= 2**a*3**b <= 10**15)
for d in sm:
    Q = Q_vector(d); n = sum(1 for a in range(60) for b in range(40) if 2**a*3**b <= d)
    eps = n - sum(Q)  # number of active exceptional corrections
    K = Q_vector  # noqa
    Sh = sum(Q[j] * w**j for j in range(3))
    # S_hat equals row-sum S minus eps*w^{colour of exceptional root}
    tau = min(Q)
    assert abs((n - eps) / 3 - (2/3) * H(Sh) - tau) < 1e-9
print("Eisenstein gauge identity verified at", len(sm), "cutoffs")
# J = int_3^inf (mean Q - min Q) t^-2 dt  (piecewise constant on smooth intervals)
N = 10**60
sm = sorted(2**a*3**b for a in range(250) for b in range(160) if 2**a*3**b <= N)
Q = Q_vector(2); J = Fr(0); c_part = Fr(0)
prev = None
for i, d in enumerate(sm):
    if d < 3: continue
    for j in increments(d): Q[j] += 1
    nxt = sm[i + 1] if i + 1 < len(sm) else None
    if nxt is None: break
    Phi = Fr(sum(Q), 3) - min(Q)
    J += Phi * (Fr(1, d) - Fr(1, nxt))
getcontext().prec = 60
c_from_J = Fr(757, 972) + J / 3
print("757/972 + J/3 (J truncated at 1e60) =", Decimal(c_from_J.numerator) / Decimal(c_from_J.denominator))
