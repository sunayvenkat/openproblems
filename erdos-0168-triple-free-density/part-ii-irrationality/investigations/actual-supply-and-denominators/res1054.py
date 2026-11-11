import time, math, pickle
from resmodel import model_value, smooth
from fastmodel import side
p, q, pn, qn = 665, 1054, 15601, 24727
t = time.time()
z, st, m = model_value(p, q)
d = z.denominator
t2, t3, rest = smooth(d)
# floors must match the true floors on a<R=q+qn, b<S=p+pn (Farey argument); check exactly on a range
def true_floor(n, base, log):  # floor(n*log_log(base)) exactly: largest k with log^k <= base^n
    v = base ** n; k = int(n * math.log(base) / math.log(log)) - 2; pw = log ** k
    while pw * log <= v: pw *= log; k += 1
    return k
sig = m['sigma']
bad_a = next((n for n in range(1, q + qn + 1) if side(n, p, q, sig) != true_floor(n, 2, 3)), None)
bad_b = next((n for n in range(1, p + pn + 1) if side(n, q, p, -sig) != true_floor(n, 3, 2)), None)
R, S = q + qn, p + pn
err_log2 = math.log2(9) + math.log2(2.0 ** -40 * 2 ** (-(R - 40)) if False else 1) - R  # 9*2^-R dominates
print(dict(p=p, q=q, sigma=sig, case=m['case'], den_bits=d.bit_length(), v2=t2, v3=t3,
           nonS_bits=rest.bit_length(), diag_bits=(2 ** q * 3 ** (2 * p) - 1 if sig > 0 else 2 ** (2 * q) * 3 ** p - 1).bit_length(),
           first_floor_disagreement_a=bad_a, first_floor_disagreement_b=bad_b, R=R, S=S,
           log2_err_bound=round(math.log2(9) - R + math.log2(1 + 2.0 ** (R - S * math.log2(3))), 2),
           stats=st, secs=round(time.time() - t, 1)))
pickle.dump((z.numerator, z.denominator), open('res1054.pkl', 'wb'))
