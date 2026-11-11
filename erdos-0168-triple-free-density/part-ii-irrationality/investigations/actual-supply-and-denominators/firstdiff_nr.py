"""First true-digit disagreement of a nonresonant actual model, using a later actual model
as the truth on its floor-agreement rectangle (high rows b>=4 and low rows)."""
import math, sys
from fastmodel import axes, event, CORR, low_eta, add


def first_diff(m0, m1, R, S):
    (p0, q0), (p1, q1) = m0, m1
    s0 = 1 if 2 ** q0 > 3 ** p0 else -1; s1 = 1 if 2 ** q1 > 3 ** p1 else -1
    A0, B0 = axes(p0, q0, s0); A1, B1 = axes(p1, q1, s1)
    L0, V0, L1, V1 = 3 * q0, 3 * p0, 3 * q1, 3 * p1
    hc = {}
    for a in range(R):
        k = (A0[a % L0], A1[a % L1], a % 3)
        if k not in hc: hc[k] = a
    vc = {}
    for b in range(4, S):
        b0 = 4 + (b - 4) % V0; b1 = 4 + (b - 4) % V1
        e0 = event(b0, p0, q0, s0); e1 = event(b1, p1, q1, s1)
        k = ((B0[b0][0] - e0[0], B0[b0][1] - e0[1]), (B1[b1][0] - e1[0], B1[b1][1] - e1[1]), b % 3)
        if k not in vc: vc[k] = b
    l3 = math.log2(3); best = None
    for (h0, h1, ra), a in hc.items():
        for (v0, v1, rb), b in vc.items():
            c = CORR[ra][rb]
            x0, y0 = h0[0] + v0[0] + c[0] - 1, h0[1] + v0[1] + c[1]
            x1, y1 = h1[0] + v1[0] + c[0] - 1, h1[1] + v1[1] + c[1]
            if int(x0 <= 0 and x0 - y0 <= 0) != int(x1 <= 0 and x1 - y1 <= 0):
                w = a + b * l3
                if best is None or w < best[0]: best = (round(w, 2), a, b)
    low = None
    for b in range(4):
        for a in range(R):
            st0 = add(add(A0[a % L0], B0[b]), CORR[a % 3][b % 3]); st1 = add(add(A1[a % L1], B1[b]), CORR[a % 3][b % 3])
            if low_eta(st0[0] - 1, st0[1], a, b) != low_eta(st1[0] - 1, st1[1], a, b):
                w = a + b * l3
                if low is None or w < low[0]: low = (round(w, 2), a, b)
                break
    return best, low, len(hc), len(vc)


if __name__ == '__main__':
    cases = [((15601, 24727), (31867, 50508), 24727 + 50508 + 50508, 15601 + 31867 + 31867),
             ((31867, 50508), (79335, 125743), 125743 + 176251, 79335 + 111202)]
    for m0, m1, R, S in cases:
        print(m0, 'vs truth via', m1, '-> high, low, classes:', first_diff(m0, m1, R, S), flush=True)
