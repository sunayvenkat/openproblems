"""Direction B numerical checks. Pure python (no sympy)."""
import itertools, math, cmath, random
from math import comb, gcd, log

def small_factors(p, bound=10**7):
    M = 2**p - 1; fs = []
    k = 1
    while 2*p*k+1 <= bound:
        q = 2*p*k+1
        if pow(2, p, q) == 1 and all(q % r for r in range(3, int(q**.5)+1, 2)):
            fs.append(q)
        k += 1
    return fs

def collision(p, d, T):
    """find distinct T-subsets A,B of [0,p) with d | sum_A 2^a - sum_B 2^b (pigeonhole)."""
    seen = {}
    for A in itertools.combinations(range(p), T):
        r = sum(pow(2, a, d) for a in A) % d
        if r in seen:
            return seen[r], A
        seen[r] = A
    return None

def check_P3():
    print("== P3: pigeonhole-forced sparse multiples, gcd with M_p ==")
    for p in [29, 43, 79, 191, 223]:
        M = 2**p - 1
        fs = small_factors(p, 10**6)
        print("p", p, "small prime factors of M_p (<1e6):", fs)
        for d in fs + ([fs[0]*fs[1]] if len(fs) > 1 and fs[0]*fs[1] < 10**8 else []):
            T = 1
            while comb(p, T) <= d: T += 1
            if comb(p, T) > 5*10**6: print("  d", d, "T", T, "too big, skip"); continue
            A, B = collision(p, d, T)
            u = sum(2**a for a in A) - sum(2**b for b in B)
            assert u != 0 and u % d == 0
            g = gcd(u, M)
            print(f"  d={d} T={T} C(p,T)={comb(p,T)} terms<= {2*T} gcd(u,M_p)={g}  log g/log C={log(g)/log(comb(p,T)):.3f}")
    # P3 also holds for d NOT dividing M_p (universality)
    p = 29
    for d in [2003, 2087, 3001]:  # random odd moduli < C(29,3)=3654
        A, B = collision(p, d, 3)
        u = sum(2**a for a in A) - sum(2**b for b in B)
        print(f"  universality: p=29 d={d} (d|M_p? {(2**29-1)%d==0}) 6-term multiple found, u%d={u%d}")

def norm_log(f, p):
    """log |N(f(zeta_p))| via complex product; f dict exp->coef, exps reduced mod p."""
    s = 0.0
    for j in range(1, p):
        z = sum(c*cmath.exp(2j*math.pi*e*j/p) for e, c in f.items())
        s += math.log(abs(z))
    return s

def check_P2():
    print("== P2: resultant bound sum_{q,j}[q|f(2^j)] log q <= log|N f(zeta)| <= (p-1)/2 log(p||f||^2/(p-1)) ==")
    random.seed(1)
    for p in [29, 43, 79]:
        fs = small_factors(p, 10**7)
        for trial in range(3):
            T = random.choice([3, 4, 6])
            ex = random.sample(range(p), T)
            f = {e: random.choice([1, -1]) for e in ex}
            lhs = 0.0
            for q in fs:
                for j in range(1, p):
                    if sum(c*pow(2, (e*j) % p, q) for e, c in f.items()) % q == 0:
                        lhs += log(q)
            nl = norm_log(f, p)
            rhs = (p-1)/2*log(p*T/(p-1))
            print(f"  p={p} T={T} lhs(known q)={lhs:.2f}  log|N|={nl:.2f}  bound={rhs:.2f}")
            assert lhs <= nl + 1e-6 and nl <= rhs + 1e-6

def mu_gen(q, p):
    while True:
        g = random.randrange(2, q-1)
        w = pow(g, (q-1)//p, q)
        if w != 1: return w

def isprime(n):
    if n < 2: return False
    for r in range(2, int(n**.5)+1):
        if n % r == 0: return False
    return True

def check_fake():
    print("== Fake-model invariance of collision counts N_q(T) (T=2, 4-term) ==")
    random.seed(2)
    p = 43; T = 2
    C = comb(p, T)
    def Nq(q, w):
        cnt = {}
        for A in itertools.combinations(range(p), T):
            r = sum(pow(w, a, q) for a in A) % q
            cnt[r] = cnt.get(r, 0) + 1
        return sum(v*(v-1) for v in cnt.values())
    true_q = [431]
    fake_q = [q for q in range(2*p+1, 2000, 2*p) if isprime(q) and pow(2, p, q) != 1][:4]
    for q in true_q:
        print(f"  TRUE q={q}: N_q={Nq(q,2)}  C^2/q={C*C/q:.1f}")
    for q in fake_q:
        print(f"  FAKE q={q}: N_q={Nq(q,mu_gen(q,p))}  C^2/q={C*C/q:.1f}")
    print("== joint alignment: p=29, q1=233,q2=1103, count 4-term u with q1q2|u, generator twist k ==")
    p = 29; q1, q2 = 233, 1103; T = 3
    for k in [1, 2, 3, 5, 7]:
        w2 = pow(2, k, q2)
        cnt = {}
        for A in itertools.combinations(range(p), T):
            r = (sum(pow(2, a, q1) for a in A) % q1, sum(pow(w2, a, q2) for a in A) % q2)
            cnt[r] = cnt.get(r, 0) + 1
        print(f"  k={k}: pairs={sum(v*(v-1) for v in cnt.values())}  C^2/(q1q2)={comb(p,T)**2/(q1*q2):.1f}")

def check_phi():
    print("== Phi_p check: f with <p nonzero coefficients, deg<p, f(zeta)!=0 ==")
    random.seed(3)
    p = 31
    mn = 1e9
    for _ in range(2000):
        T = random.randint(1, p-1)
        ex = random.sample(range(p), T)
        f = {e: random.choice([1, -1]) for e in ex}
        mn = min(mn, abs(sum(c*cmath.exp(2j*math.pi*e/p) for e, c in f.items())))
    print("  min |f(zeta_31)| over 2000 random sparse f:", mn)

if __name__ == "__main__":
    check_phi(); check_P2(); check_P3(); check_fake()
