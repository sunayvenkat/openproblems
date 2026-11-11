# Strict re-check of the decisive (piece, level) pairs of m2 = 59814755: the CRT value of the
# offset-0 coefficient must agree for three consecutive prime counts (deep.py required two).
from deep import coeffs_mod, crt, PR
m = 59814755
DEC = {385: 3, 595: 3, 7315: 3, 7735: 3, 8645: 3, 13585: 3, 14245: 3, 17765: 3, 26455: 3, 85085: 3,
       455: 4, 6545: 4, 12155: 4, 20995: 4, 95095: 5, 185185: 3, 242165: 3, 270655: 5, 286195: 3,
       323323: 3, 629629: 5, 776815: 4, 1616615: 4, 8544965: 4, 319865: 14}
for d, s in DEC.items():
    rs = []
    for k, P in enumerate(PR, 1):
        rs.append(int(coeffs_mod(m, d, s, 1, P)[0]))
        if k >= 4 and len({crt(rs[:j], PR[:j]) for j in (k - 2, k - 1, k)}) == 1:
            v = crt(rs, PR[:k]); break
    else:
        v = None
    print(d, 'level', s, 'primes', k, 'value', v, 'NEG' if v is not None and v < 0 else 'CHECK', flush=True)
