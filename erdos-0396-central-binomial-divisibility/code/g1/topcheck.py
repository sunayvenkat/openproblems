# Exact top-piece sign (T=2, level 1) for the P=3 search hits (search_P3_e15.txt) via window.top_sign.
# DRAFT value to reproduce: m=59814755 -> -74322712269080.
import re
from window import top_sign
for line in open('search_P3_e15.txt'):
    g = re.search(r'rho=(\d+) m=(\d+) omega=(\d+) primes=\[(.*)\]', line)
    if not g: continue
    rho, m = int(g[1]), int(g[2]); ps = [int(x) for x in g[4].split(',')]
    N, s, v = top_sign(ps, 2, rho)
    print(f'm={m} omega={len(ps)} rho={rho}: first nonzero c_N at N=rho+{N-rho}, value {v} -> top {"GOOD" if s < 0 else "bad"}', flush=True)
