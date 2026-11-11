"""Locate the minimal-weight cell where the resonant 665/1054 model differs from the
true array.  On a<75235, b<47468 the true array equals the actual nonresonant model at
15601/24727 (floor agreement rectangle), so compare the two complete models there."""
import math
from fastmodel import axes, event, CORR, low_eta, add
from resmodel import build
p, q = 665, 1054
m = build(p, q)
P1, Q1 = 15601, 24727
s1 = 1 if 2 ** Q1 > 3 ** P1 else -1
A1, B1 = axes(P1, Q1, s1)
R, S = 24727 + 50508, 15601 + 31867
L1, V1 = 3 * Q1, 3 * P1


def rs_state(a, b):
    return m['state'](a, b)  # (x-1 applied, y), before event


def nr_state(a, b):
    x, y = add(add(A1[a % L1], B1[b if b < 4 else 4 + (b - 4) % V1]), CORR[a % 3][b % 3])
    return x - 1, y


# high rows: classes
hcls = {}
for a in range(R):
    i, r = divmod(a, m['P'])
    ar = add(m['A'][r], (i * m['da'][0], i * m['da'][1]))
    k = (A1[a % L1], ar, a % 3)
    if k not in hcls: hcls[k] = a
vcls = {}
for b in range(4, S):
    j, s = divmod(b, m['Q'])
    br = add(m['B'][s], (j * m['db'][0], j * m['db'][1]))
    e_r = m['epsilon'](b)
    bb = 4 + (b - 4) % V1
    e_1 = event(bb, P1, Q1, s1)
    k = ((B1[bb][0] - e_1[0], B1[bb][1] - e_1[1]), (br[0] - e_r[0], br[1] - e_r[1]), b % 3)
    if k not in vcls: vcls[k] = b
print('classes', len(hcls), len(vcls))
best = None
l3 = math.log2(3)
for (h1, hr, ra), a in hcls.items():
    for (v1, vr, rb), b in vcls.items():
        c = CORR[ra][rb]
        x1, y1 = h1[0] + v1[0] + c[0] - 1, h1[1] + v1[1] + c[1]
        xr, yr = hr[0] + vr[0] + c[0] - 1, hr[1] + vr[1] + c[1]
        d1 = int(x1 <= 0 and x1 - y1 <= 0); dr = int(xr <= 0 and xr - yr <= 0)
        if d1 != dr:
            w = a + b * l3
            if best is None or w < best[0]: best = (w, a, b, d1, dr, (x1, y1), (xr, yr))
print('first high-row disagreement (log2 weight, a, b, true digit, res digit, true state, res state):', best)
lowbest = None
for b in range(4):
    for a in range(R):
        x1, y1 = nr_state(a, b); xr, yr = rs_state(a, b)
        if low_eta(x1, y1, a, b) != low_eta(xr, yr, a, b):
            w = a + b * l3
            if lowbest is None or w < lowbest[0]: lowbest = (w, a, b)
            break
print('first low-row disagreement:', lowbest)
