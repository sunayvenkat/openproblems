"""Task 5: witnesses n in E_k from family F+ (n = M+k+1, M/j' = A_{j'}^{m_{j'}}, m odd >= 3) and a
partial variant (only j' = 1, 2 structured).  Candidates are factored piece by piece (algebraic
pieces Phi_{2d}(A) first), with early rejection; survivors go through verify396.verify with facs."""
import sys
from math import isqrt, prod, gcd
from verify396 import is_prime, factor, carries, vp, verify, SMALL
from famplus import phi_poly
from lemC import divisors

HARD = 10**30      # shortcut: composite cofactors above this go to sympy ECM only if ECM=True (else UNDECIDED)
ECM = False


def iroot(x, r):
    y = int(round(x ** (1.0 / r))) if x < 10**300 else int(2 ** (x.bit_length() / r))
    while y ** r > x: y -= 1
    while (y + 1) ** r <= x: y += 1
    return y


def pieces_of(j, A, m):
    return [j] + [phi_poly(2 * d, A) for d in divisors(m)]


def check(n, k, parts):
    """parts[i]: list of integers with product n-i.  Returns 'IN', 'OUT:<reason>' or 'UNDECIDED'."""
    facs = []; hard = []                          # hard: (i, f, composite cofactor) left for ECM
    for i, ps in enumerate(parts):
        assert prod(ps) == n - i
        f = {}
        for x in ps:
            for p in SMALL:                       # trial division first
                if p * p > x: break
                while x % p == 0: f[p] = f.get(p, 0) + 1; x //= p
            if x > 1:
                if is_prime(x) or x < HARD:
                    for p, e in factor(x).items(): f[p] = f.get(p, 0) + e
                else:
                    hard.append((i, f, x))
            for p in f:                           # early rejection on any large prime found so far
                if p > 2 * k and carries(n, p) < vp(n - i, p):
                    return f"OUT:q={p} (i={i}) lacks carries"
        facs.append(f)
    if hard and not ECM:
        return "UNDECIDED"
    for i, f, x in hard:                          # only reached when nothing else rejected
        from sympy import factorint
        for p, e in factorint(x).items(): f[int(p)] = f.get(int(p), 0) + e
    ok, rows = verify(n, k, facs)
    return "IN" if ok else "OUT:" + ",".join(str(p) for p, a, b in rows if a > b)


def fplus_k1(NMAX):
    """all n = M+2 <= NMAX with M = A^{m1} = 2 C^{m2}, m1, m2 odd >= 3.
    Then gcd(m1,m2)=1 and M = 2^e S^(m1 m2), S odd, e = 0 mod m1, e = 1 mod m2."""
    out = []; top = NMAX.bit_length()
    for m1 in range(3, top + 1, 2):
        for m2 in range(3, top + 1, 2):
            L = m1 * m2
            if gcd(m1, m2) > 1: continue
            for e in range(m1, top + 1, m1):
                if (e - 1) % m2: continue
                S = 1                              # S = 1 allowed for any L; S >= 3 needs 3^L small
                while 2 ** e * S ** L + 2 <= NMAX and (S == 1 or L <= top):
                    M = 2 ** e * S ** L
                    out.append((M + 2, m1, m2, iroot(M, m1), iroot(M // 2, m2)))
                    S += 2
    return sorted(set(out))


if __name__ == "__main__":
    what = sys.argv[1]
    if what == "k1":
        NMAX = int(float(sys.argv[2]))
        cands = fplus_k1(NMAX)
        print(f"F+ k=1 candidates n <= {NMAX:.0e}: {len(cands)}")
        for n, m1, m2, A, C in cands:
            r = check(n, 1, [pieces_of(2, C, m2), pieces_of(1, A, m1)])
            if r == "IN" or r == "UNDECIDED":
                print(f"  n={n}  (m1,m2)=({m1},{m2}) A={A} C={C}: {r}", flush=True)
    elif what == "k2full":
        # n = M+3, M = A^{m1} = 2C^{m2} = 3D^{m3}: M = 2^{e2+L a} 3^{e3+L b} B^L
        for ms in [(3, 5, 7), (3, 7, 5), (3, 5, 11), (3, 11, 5), (5, 3, 7), (3, 7, 11)]:
            L = prod(ms)
            e2 = next(e for e in range(1, L + 1) if e % ms[0] == 0 and (e - 1) % ms[1] == 0 and e % ms[2] == 0)
            e3 = next(e for e in range(1, L + 1) if e % ms[0] == 0 and e % ms[1] == 0 and (e - 1) % ms[2] == 0)
            for B in range(1, 7):
                M = 2 ** e2 * 3 ** e3 * B ** L
                if M > 10**80: break
                A, C, D = iroot(M, ms[0]), iroot(M // 2, ms[1]), iroot(M // 3, ms[2])
                assert A ** ms[0] == M and 2 * C ** ms[1] == M and 3 * D ** ms[2] == M
                n = M + 3
                r = check(n, 2, [pieces_of(3, D, ms[2]), pieces_of(2, C, ms[1]), pieces_of(1, A, ms[0])])
                print(f"  k=2 F+ m={ms} B={B} n~10^{len(str(n))-1}: {r}", flush=True)
    elif what in ("k2var", "k3var"):
        # variant: only n-k = A^{m1}+1 and n-k+1 = 2(C^{m2}+1) structured; M divisible by lcm(1..k+1)
        k = 2 if what == "k2var" else 3; NMAX = int(float(sys.argv[2])); lcm = 6 if k == 2 else 12
        found = 0
        for n0, m1, m2, A, C in fplus_k1(NMAX):
            M = n0 - 2
            if M % lcm: continue
            n = M + k + 1
            parts = [[n - i] for i in range(k - 1)] + [pieces_of(2, C, m2), pieces_of(1, A, m1)]
            r = check(n, k, parts)
            if r in ("IN", "UNDECIDED"):
                print(f"  k={k} variant n={n} (m1,m2)=({m1},{m2}) A={A} C={C}: {r}", flush=True); found += 1
        print("done", what, "found", found)
