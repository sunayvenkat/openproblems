"""
Standalone verification script for Tasks H1 and H2.
Verifies the exact identity and the uniform error bound |E_n| <= 9 * 2^{2q - Q}.
"""
import sys
from pathlib import Path
from mpmath import mp
mp.dps = 100

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'research_notes' / 'Erdos 168 actual supply and denominators'))
from fastmodel import add, rot, side, HINC, VINC

CORR = (((0, 0), (0, 0), (0, 0)), ((0, 0), (1, 0), (1, 1)), ((0, 0), (0, -1), (1, 0)))

alpha = mp.log(2) / mp.log(3)
beta = 1 / alpha

def get_true_axes(max_a, max_b):
    A = [(1, 0)]
    for a in range(1, max_a + 1):
        fl = int(mp.floor(a * alpha))
        step = rot(HINC[fl % 3], -a)
        A.append(add(A[-1], step))
    B = [(1, 0)]
    for b in range(1, max_b + 1):
        fl = int(mp.floor(b * beta))
        step = rot(VINC[fl % 3], -2 * b)
        B.append(add(B[-1], step))
    return A, B

def get_event(b):
    m = lambda k: int(mp.floor(k * beta))
    iso = (m(b) - m(b - 1) == 2)
    pat = (m(b - 1) - m(b - 3) == 4)
    if iso:
        return rot((1, 0), m(b) - 2 * b)
    elif pat:
        return rot((1, 0), m(b - 1) - 1 - 2 * b)
    else:
        return (0, 0)

def eta_tilde_true(a, b, A, B):
    c = CORR[a % 3][b % 3]
    e = get_event(b) if b >= 4 else (0, 0)
    x = A[a][0] + B[b][0] - 1 + c[0] - e[0]
    y = A[a][1] + B[b][1] + c[1] - e[1]
    if b == 0:
        return 0
    elif b == 1:
        return 1 if (x >= 1 and y >= 0) else 0
    elif b == 2:
        return 1 if (x <= -1 and x - y <= 0) else 0
    elif b == 3:
        return 1 if (min(x, 0) <= y) else 0
    else:
        return 1 if (x <= 0 and x - y <= 0) else 0

def eta_tilde_model(a, b, A_model, B, L):
    c = CORR[a % 3][b % 3]
    e = get_event(b) if b >= 4 else (0, 0)
    a_mod = a % L
    x = A_model[a_mod][0] + B[b][0] - 1 + c[0] - e[0]
    y = A_model[a_mod][1] + B[b][1] + c[1] - e[1]
    if b == 0:
        return 0
    elif b == 1:
        return 1 if (x >= 1 and y >= 0) else 0
    elif b == 2:
        return 1 if (x <= -1 and x - y <= 0) else 0
    elif b == 3:
        return 1 if (min(x, 0) <= y) else 0
    else:
        return 1 if (x <= 0 and x - y <= 0) else 0

cases = [
    (5, 8, 1, 8, 19),      # 5/8, W=27, 2q-Q = -3
    (12, 19, -1, 19, 65),  # 12/19, W=84, 2q-Q = -27
]

max_a = 150
max_b = 60
A_true, B_true = get_true_axes(max_a, max_b)

for p, q, s, q_curr, q_next in cases:
    W = q_curr + q_next
    L = 3 * q_curr
    A_model = [(1, 0)]
    for a in range(1, L):
        step = rot(HINC[side(a, p, q, s) % 3], -a)
        A_model.append(add(A_model[-1], step))
    
    mismatches = 0
    for b in range(max_b):
        for a in range(W):
            if eta_tilde_true(a, b, A_true, B_true) != eta_tilde_model(a, b, A_model, B_true, L):
                mismatches += 1
    
    diff_sum = mp.mpf(0)
    for b in range(max_b):
        row_diff = mp.mpf(0)
        for a in range(W, max_a):
            e_tr = eta_tilde_true(a, b, A_true, B_true)
            e_md = eta_tilde_model(a, b, A_model, B_true, L)
            row_diff += (e_tr - e_md) * mp.power(2, -a)
        diff_sum += row_diff * mp.power(3, -b)
    
    E_n = -3 * (mp.power(2, L) - 1) * diff_sum
    bound = 9 * mp.power(2, 2 * q - q_next)
    print(f'p/q={p}/{q}: mismatches below W={W}: {mismatches}')
    print(f'   |E_n| = {abs(E_n)}')
    print(f'   bound = {bound}')
    print(f'   ratio = {float(abs(E_n) / bound):.6f}')
    assert mismatches == 0
    assert abs(E_n) <= bound

    # Verify Theorem 5: G_n(b) mod 3 and mod 9
    C0 = (1 << (L + 1)) - 2
    for b in range(max_b):
        gb = sum((1 - 3 * eta_tilde_model(a, b, A_model, B_true, L)) * (1 << (L - a)) for a in range(L))
        # Part 1: G_n(b) mod 3
        expected_mod3 = 0 if q % 2 == 0 else 2
        assert gb % 3 == expected_mod3, f"Failed mod 3 at b={b}"
        # Part 2: G_n(b) = C0 - 3 * delta mod 9
        delta = sum(eta_tilde_model(a, b, A_model, B_true, L) * ((-1) ** (L - a)) for a in range(L)) % 3
        assert (gb - C0 + 3 * delta) % 9 == 0, f"Failed mod 9 at b={b}"
    print(f'   Theorem 5 mod 3 and mod 9 checks passed for all {max_b} rows.')

print('ALL CHECKS PASSED!')
