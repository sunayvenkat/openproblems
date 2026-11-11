# Probe: does Z admit structured cheap denominators d (cost < window) with tiny ||dZ||?
import sys, pickle, itertools
sys.path.insert(0, r"../actual-supply-and-denominators")
sys.set_int_max_str_digits(0)
N, D, R, S = pickle.load(open(sys.path[0] + "/z24727.pkl", "rb"))
PREC = 20000                      # bits of Z used (true precision ~75000)
Zi = (N << PREC) // D             # floor(Z*2^PREC); Z in (1,2)?
def dist(d):                      # -log2 ||d Z||, valid while d.bit_length() < PREC-64
    x = (d * Zi) & ((1 << PREC) - 1)
    x = min(x, (1 << PREC) - x)
    return PREC - x.bit_length()
conv = [(5,8,19),(12,19,65),(41,65,84),(53,84,485),(306,485,1054),(665,1054,24727)]
for p, q, Q in conv:
    W = q + Q
    f = {'2q-1': 2**q-1, 'Phi3(2q)': 4**q+2**q+1, '3p-1': 3**p-1, 'Phi3(3p)': 9**p+3**p+1}
    extra = {'2q3p-1': 2**q*3**p-1, '|2q-3p|': abs(2**q-3**p), '2^3q-3^3p': abs(8**q-27**p),
             '2^2q+2q3p+3^2p': 4**q+2**q*3**p+9**p, '2q3p+1':2**q*3**p+1, '6^?': 2**(2*q)*3**(2*p)+2**q*3**p+1}
    best = []
    cands = {}
    for r in range(0, 5):
        for sub in itertools.combinations(f, r):
            d = 1
            for k in sub: d *= f[k]
            cands['*'.join(sub) or '1'] = d
    for k, v in extra.items():
        cands[k] = v
        for k2, v2 in f.items(): cands[k + '*' + k2] = v * v2
    xmax = min(3 * q, 600)
    ntests = 0
    for name, d in cands.items():
        for m in (1, 3, 9, 27):
            dd = d * m
            for x in range(0, xmax):
                c = dd.bit_length() + x
                if c > PREC - 200: break
                s = dist(dd << x); ntests += 1
                # gain = bits of smallness beyond cost-vs-window need: want s large; flag s>=24
                if s >= 22: best.append((s, c, name, m, x))
    best.sort(reverse=True)
    print(f"p/q={p}/{q} W={W} tests={ntests} log2(tests)={ntests.bit_length()} hits(s>=22): {best[:8]}", flush=True)
