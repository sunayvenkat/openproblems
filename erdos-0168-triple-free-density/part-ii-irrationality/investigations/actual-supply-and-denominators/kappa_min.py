"""Minimal clearing exponent any approximation family can have at an actual index.

From the certified CF prefix of Z (zcf_best.pkl): for a target error 2^-E, any rational
y != Z with |Z-y| <= 2^-E and den(y) <= 2^{(E-1)/2} is a convergent C_k (Legendre), and
|Z - C_k| > 1/((a_{k+1}+2) h_k^2).  So den(y) >= min{h_k : h_k^2 (a_{k+1}+2) >= 2^E}.
We report kappa_min = log2(that h_k)/q for E = q+Q-slack.
"""
import pickle, math, sys
sys.set_int_max_str_digits(0)
pre = pickle.load(open('zcf_best.pkl', 'rb'))
h0, h1 = 0, 1
H = []
for a in pre:
    h0, h1 = h1, a * h1 + h0; H.append(h1)
logs = [math.log2(h) for h in H]
conv = [(5, 8, 19), (12, 19, 65), (41, 65, 84), (53, 84, 485), (306, 485, 1054), (665, 1054, 24727),
        (15601, 24727, 50508), (31867, 50508, 125743)]
for slack in (0, 20, 60):
    print('slack', slack)
    for p, q, Q in conv:
        E = q + Q - slack
        k = next((k for k in range(len(pre) - 1) if 2 * logs[k] + math.log2(pre[k + 1] + 2) >= E), None)
        if k is None:
            print('  ', (p, q), 'beyond certified range'); continue
        lb = min(logs[k], (E - 1) / 2)
        print('   %s res=%s a_next=%d  E=%d  min den bits=%.1f  kappa_min=%.3f  generic E/2q=%.3f'
              % ((p, q), (p + q) % 3 == 0, Q // q, E, lb, lb / q, E / (2 * q)))
