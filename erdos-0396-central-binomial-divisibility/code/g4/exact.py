# Rigorous decisive coefficients for the 25 deep pieces of m2 = 59814755 (DRAFT §4, §8.4-8.5).
# Method B (exact): big-integer polynomials (python-flint), no CRT.
#   X(m,d,s) = [x^-1] tail((x^m+1)/f^{s+1}) = sum_{r=1}^{s} (-1)^{r+1} C(K,r) sum_a C(r,a) ph[r d-(s+1)phi(d)+1-a d],
#   ph[j] = [t^j] Phi_n(t)^{-(s+1)}, n = 2d.  Since Phi_n * Psi_n = t^n - 1 (Psi_n = inverse cyclotomic poly),
#   Phi_n^{-(s+1)} = (-1)^{s+1} Psi_n^{s+1} (1-t^n)^{-(s+1)}, so ph[j] = (-1)^{s+1} sum_k C(k+s,s) [t^{j-kn}] Psi_n^{s+1}.
# Method A (cross-check): |ph[j]| <= h^{s+1} C(j+s,s) with h = height(Psi_n) (coefficients of 1/Phi_n are -Psi_n
#   repeated with period n), giving an a priori bound B >= |X|; deep.coeffs_mod residues over primes with prod > 2B
#   then determine X by CRT independently of flint.
# Offset 0 is the top of the tail: (x^m+1)/f^{s+1} = sum_k D_k f^{k-s-1}, deg D_k < deg f, so only D_s/f reaches
#   x^-1 and X = [x^{phi(d)-1}] D_s.  X < 0 => deg D_s = phi(d)-1, lc(D_s) = X < 0, D_s is the last nonzero digit
#   among D_1..D_s, so level s carries (Thm 4.1) with no "first nonzero" choice.  selfcheck() tests X = [x^{phi-1}]D_s.
# Usage (from code/g4):  python exact.py [--crt]
import sys, time
from math import comb, log10
from flint import fmpz_poly
sys.path.insert(0, '../agentV'); sys.path.insert(0, '../aur')
from fastgood import pf, phi

m2 = 59814755
DEC = {385: 3, 595: 3, 7315: 3, 7735: 3, 8645: 3, 13585: 3, 14245: 3, 17765: 3, 26455: 3, 85085: 3,
       455: 4, 6545: 4, 12155: 4, 20995: 4, 95095: 5, 185185: 3, 242165: 3, 270655: 5, 286195: 3,
       323323: 3, 629629: 5, 776815: 4, 1616615: 4, 8544965: 4, 319865: 14}


def psi(n):
    # Psi_{p n'}(t) = Psi_{n'}(t^p) Phi_{n'}(t) for p not dividing n'; verified exactly: Psi_n Phi_n = t^n - 1
    P, q = fmpz_poly([1]), 1
    for p in pf(n):
        P = P.inflate(p) * fmpz_poly.cyclotomic(q); q *= p
    c = (P * fmpz_poly.cyclotomic(n)).coeffs()
    assert len(c) == n + 1 and c[0] == -1 and c[n] == 1 and sum(1 for v in c if v) == 2
    return P


def X(m, d, s, Psi=None):
    K, dl, n = m // d, phi(d), 2 * d
    Psi = Psi or psi(n)
    L = s * d - (s + 1) * dl + 2
    Q = Psi.truncate(L).pow_trunc(s + 1, L)
    def ph(j):
        return 0 if j < 0 else (-1) ** (s + 1) * sum(comb(k + s, s) * int(Q[j - k * n]) for k in range(j // n + 1))
    return sum((-1) ** (r + 1) * comb(K, r) * sum(comb(r, a) * ph(r * d - (s + 1) * dl + 1 - a * d)
               for a in range(r + 1)) for r in range(1, s + 1))


def bound(m, d, s, h):
    K, dl = m // d, phi(d)
    return h ** (s + 1) * sum(comb(K, r) * sum(comb(r, a) * comb(j + s, s) for a in range(r + 1)
                              if (j := r * d - (s + 1) * dl + 1 - a * d) >= 0) for r in range(1, s + 1))


def selfcheck(m, smax):
    # X(m,d,s) must equal [x^{phi(d)-1}] of the base-f digit D_s of x^m+1, for every d | m
    for d in (e for e in range(1, m + 1) if m % e == 0):
        f, dl = fmpz_poly.cyclotomic(2 * d), phi(d)
        q = fmpz_poly([1] + [0] * (m - 1) + [1])
        for s in range(0, min(smax, m // dl - 1) + 1):
            q, D = divmod(q, f)
            if s >= 1:
                assert X(m, d, s) == D[dl - 1], (m, d, s)
    print('selfcheck ok', m, flush=True)


if __name__ == '__main__':
    selfcheck(105, 30); selfcheck(1155, 12); selfcheck(15015, 5)
    crt_on = '--crt' in sys.argv
    if crt_on:
        from deep import coeffs_mod, crt, PR
    old = {}
    for line in open('../aur/strict_out.txt', encoding='utf-8-sig'):
        w = line.split(); old[int(w[0])] = (int(w[4]), int(w[6]))
    for d, s in DEC.items():
        t0 = time.time()
        K, T = m2 // d, m2 // phi(d)
        assert K % 2 == 1 and 1 <= s <= T - 1
        Psi = psi(2 * d)
        v = X(m2, d, s, Psi)
        te = time.time() - t0
        h = max(abs(int(c)) for c in Psi.coeffs())
        B = bound(m2, d, s, h)
        assert abs(v) <= B
        msg = (f'd={d} K={K} s={s} T={T} sign={"NEG" if v < 0 else "POS" if v > 0 else "ZERO"} digits={len(str(abs(v)))} '
               f'matches_strict={v == old[d][1]} exact_time={te:.1f}s h={h} log10B={log10(B):.1f}')
        if crt_on:
            k, M = 0, 1
            while M <= 2 * B: M *= PR[k]; k += 1
            t1 = time.time()
            vc = crt([int(coeffs_mod(m2, d, s, 1, P)[0]) for P in PR[:k]], PR[:k])
            msg += f' crt_primes={k} (strict used {old[d][0]}) crt_equal={vc == v} crt_time={time.time() - t1:.1f}s'
        print(msg + f'\n  value={v}', flush=True)
