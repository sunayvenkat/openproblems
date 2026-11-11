# Do the certified convergent denominators Q_k of Z carry S-unit structure?
# A structured clearer d = N*k' + r (N a large S-unit, r tiny) has Q == r mod 2^x 3^y with x,y large.
import pickle, sys, math
sys.set_int_max_str_digits(0)
base = r"../actual-supply-and-denominators"
cf = pickle.load(open(base + "/zcf_best.pkl", "rb"))
def val(n, l):
    if n == 0: return 10**9
    k = 0
    while n % l == 0: n //= l; k += 1
    return k
h0, h1 = 1, 0   # denominators: k_{-2}=1, k_{-1}=0
hits = []; best_generic = 0
for k, a in enumerate(cf):
    h0, h1 = h1, a * h1 + h0
    Q = h1
    bits = Q.bit_length()
    if bits < 64: continue
    s = 0; arg = None
    for r in range(-8, 9):
        v2 = val(Q - r, 2); v3 = val(Q - r, 3)
        t = v2 + 1.585 * v3
        if t > s: s, arg = t, (r, v2, v3)
    if s > 40: hits.append((k, bits, round(s), arg, a.bit_length()))
    else: best_generic = max(best_generic, s)
print("convergents scanned:", len(cf), "largest generic score (bits):", round(best_generic, 1))
print("structured convergents (index, den bits, S-unit bits, (r,v2,v3), next partial quotient bits):")
for h in hits: print("  ", h)
