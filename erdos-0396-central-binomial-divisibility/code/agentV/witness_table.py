"""Per-piece table for F+ witnesses: piece, its factorisation, and for prime pieces Laurent prediction vs Kummer."""
from famplus import phi_poly, predicted_levels, actual_levels
from verify396 import factor, is_prime, verify, carries, vp
from lemC import divisors
W = [(34359738370, 1, [(2, 4, 17), (1, 2, 35)]),          # n = 2^35+2 : n = 2(4^17+1), n-1 = 2^35+1
     (481469424205826, 1, [(2, 62208, 3), (1, 864, 5)]),   # (m1,m2)=(5,3), B=6
     (2251799813685250, 1, [(2, 1024, 5), (1, 131072, 3)])]# (m1,m2)=(3,5), B=8
for n, k, blocks in W:
    print(f"n = {n}, k = {k}: verifier says {'IN' if verify(n, k)[0] else 'OUT'} E_k")
    for i, (j, A, m) in enumerate(blocks):
        assert j * (A**m + 1) == n - i
        print(f"  n-{i} = {j}*({A}^{m}+1)")
        for d in divisors(m):
            q = phi_poly(2 * d, A); f = factor(q)
            s = f"    Phi_{2*d}({A}) = {q} = {dict(sorted(f.items()))}"
            if is_prime(q):
                s += f"  prime: Laurent pred levels {sorted(predicted_levels(m, d))}, Kummer levels {sorted(actual_levels(n, q))}"
            else:
                s += "  carries per prime: " + ", ".join(f"{p}:{carries(n,p)}>={vp(n-i,p)}" for p in sorted(f) if p > 2 * k)
            print(s)
