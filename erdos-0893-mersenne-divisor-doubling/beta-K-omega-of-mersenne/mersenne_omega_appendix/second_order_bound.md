# W2 — Pointwise improvement of the trivial bound for omega(M_p): result

VERDICT: NO-IMPROVEMENT of the first-order constant log2/2. What is proved:
(A) explicit second-order bound (fake-invariant);
(C) reduction: improving the constant is equivalent to a smooth-part statement in the window [p^{2-eta}, p^{2+eta}];
(B) barrier: for almost all p there are "fake" prime sets/integers sharing every listed non-exact property
    (congruences mod 2p, 8, mod 2^i p^j with i,j up to c*eps*p, fixed-depth residue conditions, BT, size)
    with (log2/2 - eps) p/log p prime factors; so no argument built only on those properties can beat log2/2;
(D) every exact-divisibility tool tested is quantified and shown weaker than trivial, or circular.

Notation: p odd prime, Q_p = {q prime : q | M_p}, k = omega(M_p) = |Q_p|, q_1<...<q_k, L = log p.
Base facts (PROVED, elementary): q | M_p => ord_q 2 = p => q ≡ 1 (mod 2p); 2 ≡ (2^{(p+1)/2})^2 (mod q) => (2/q)=1 => q ≡ ±1 (mod 8).
Hence q lies in exactly two classes mod 8p: a_1 = 1 and a_2 ∈ {1+2p, 1+6p} (the one ≡ 7 mod 8).  [checked: 1+2p ≡ 3 or 7 mod 8 as p ≡ 1 or 3 mod 4; 1+4p ≡ 5.]
Also q|M_p <=> 2 ∈ mu_p(F_q) = (F_q^*)^{m_q}, m_q := (q-1)/p   (exact divisibility = unbounded-depth condition).

---------------------------------------------------------------------------------------------------
## Cited theorems (exact statements, hypotheses uniform in p)

[MV] Montgomery–Vaughan, "The large sieve", Mathematika 20 (1973) 119–134, Thm 2:
     for 1 <= r < x and (a,r)=1:  pi(x; r, a) < 2x / (phi(r) log(x/r)).   No other hypothesis. Applied with r = 8p, x = q_j > 8p.
[LS] Multiplicative large sieve (Montgomery–Vaughan 1973, Thm 1 + Gallagher; Iwaniec–Kowalski Thm 7.13):
     sum_{r<=R} (r/phi(r)) sum*_{chi mod r} |sum_{M<n<=M+N} a_n chi(n)|^2 <= (R^2 + N - 1) sum |a_n|^2. Any complex a_n.
[BV] Bombieri–Vinogradov (Davenport, Multiplicative Number Theory, 3rd ed., Ch. 28): for every A>0, with B = A+5,
     sum_{r <= x^{1/2}(log x)^{-B}} max_{y<=x} max_{(a,r)=1} |psi(y;r,a) - y/phi(r)| <<_A x (log x)^{-A}.  (ineffective constant; fine for "almost all p")
[HB] Heath-Brown, Proc. LMS (3) 64 (1992) 265–338: least prime ≡ a (mod R), (a,R)=1, is <= c_0 R^{5.5}, c_0 absolute, all R >= 2.

---------------------------------------------------------------------------------------------------
## Theorem A (PROVED; fake-invariant). Second-order trivial bound.
For every odd prime p:
 (a) q_1 >= 2p+1 and q_j >= 4p(j-1)+1 for j >= 2;
 (b) q_j > j (p-1) log((j-1)/2) for j >= 8;
 (c) sum_j log q_j <= log M_p < p log 2.
Consequently omega(M_p) <= (log2/2) * p / (log p - kappa + O(loglog p / log p)),  kappa = (1 - log(log2/2))/2 = 1.02983...
(The naive bound q_j >= 2pj+1 gives instead denominator log p - (1/2)loglog p + O(1).)

Proof. (a) Integers n>1 in the two classes, n <= y, number at most 2*floor(y/8p)+1; so j <= q_j/(4p)+1; q_j odd.
(b) For j>=8, q_j >= 28p+1 > 8p, so [MV] applies to r=8p, phi(8p)=4(p-1):
    j <= pi(q_j;8p,a_1)+pi(q_j;8p,a_2) < 4q_j/(4(p-1) log(q_j/8p)), and q_j/8p >= (j-1)/2 > e by (a).
(c) prod q_j | M_p.
Asymptotics: may assume k >= p/L^2. Put c = kL/p (c <= 1 by (a),(c)). Sum (b) over 8 <= j <= k:
sum log j = k log k - k + O(log k); loglog((j-1)/2) >= 0 for all j >= 8 and, for k/L <= j <= k,
loglog((j-1)/2) >= log(log k - log 3L) = loglog p - O(loglog p/L) (as log k >= L - 2 loglog p). With log k = L - loglog p + log c:
  sum log q_j >= k(2L + log c - 1 - O(loglog p/L)) - O(L).
With (c): f(c) := c(2 + (log c - 1)/L) <= log 2 + O(loglog p/L^2); f is increasing on (e^{-2L}, 1], so c <= c* with
f(c*) = RHS, c* = log2/2 + O(1/L), and expanding, c <= (log2/2)(1 + kappa/L + O(loglog p/L^2)).  QED
(O-constants effective, not optimized.)
Numerics (numerics.py, bound_BT): implied kappa = 1.13 (p=1e3), 1.27 (1e5), 1.20 (1e7), 1.18 (1e8): slow convergence to 1.03.
Model value (true density 1/(2p log x) in the two classes, i.e. PNT in APs mod 8p up to ~p^2, NOT provable pointwise):
kappa_model = kappa - log 2 = 0.3367. The 0.693 gap is exactly the factor 4 in [MV] (2 from BT, 2 from log(x/r) vs log x at x~r^2).

## Lemma C (PROVED; fake-invariant). Concentration in the critical window.
Fix 0<eta<1, eps>0. If omega(M_p) >= (log2/2 - eps) p/L, then, with W = [p^{2-eta}, p^{2+eta}],
  #{q|M_p : q < p^{2-eta}} <= p^{1-eta},   #{q|M_p : q > p^{2+eta}} <= ((2+log 2) eps/eta + o_eps(1)) p/L.
Proof. First: integers ≡1 (2p) below p^{2-eta}. Second: let k_+ be the count above p^{2+eta}, C=1/eps. By (b), for j >= k/C,
log q_j >= 2L - log(C/c) - o(1). So p log2 >= (k - k/C - k_+)(2L - a) + k_+(2+eta)L with a = log(C/c)+o(1) >= 0,
giving eta L k_+ <= p[2eps + (log 2)/C] + O(p log C / L).  QED
Corollary C'. "omega(M_p) <= c p/log p for some c<log2/2 and all large p"  <=>  "for some eta,delta>0 and all large p,
#{q|M_p, q∈W} <= (log2/2 - delta) p/L"  <=>  (by (b), shrinking eta if needed) "prod_{q|M_p, q∈W} q <= 2^{(1-delta')p}".
(Proof of the middle "<=": if omega >= (log2/2 - eps)p/L with eps(1 + 2.7/eta) < delta, Lemma C gives a window count
> (log2/2 - delta)p/L.)
So the whole question is the W-smooth part of M_p, where m_q = (q-1)/p ∈ [p^{1-eta}, p^{1+eta}], i.e. depth m_q ≈ sqrt(q).

## Theorem B (PROVED, using [BV],[HB]; this IS a fake model). Barrier.
Fix eps ∈ (0,1/10), D >= 3. For all primes p outside a set of relative density 0 (in every dyadic [P,2P]), and p >= p_0(eps,D),
for all integers 3 <= i <= eps p/12 and 1 <= j <= eps p/(12 L), there is a set Q'_p of primes and a prime r with:
 (i)   every q ∈ Q'_p ∪ {r}: q ≡ 1 (mod 2p), q ≡ 7 (mod 8), q ≢ 1 (mod l) for every odd prime l <= D;
       hence for every d <= D with d | m_q one has d ∈ {1,2}, and the only depth-<=D power-residue condition that true
       divisors satisfy (2 is a QR mod q) holds;
 (ii)  |Q'_p| >= (log2/2 - eps) p/log p, all elements in [p^2, p^2 L^{2B+4}] ⊂ W  (B = 8, from A = 3);
 (iii) N' := r * prod Q'_p  satisfies N' <= 2^{p(1-eps/3)} < M_p and N' ≡ M_p (mod 2^i p^j)
       (so N' ≡ -1 mod 2^i, and for j >= 2 N' satisfies the Fermat-quotient congruence sum v_q m'_q ≡ (2^{p-1}-1)/p mod p,
       q = 1+2p m'_q, and its mod p^j analogues);
 (iv)  Brun–Titchmarsh holds (they are primes); P(N') >= min Q'_p >= p^2 > p exp(log p/(104 loglog p)), so Stewart's
       lower bound holds; a factor ≡ 1 (2p) exists (Zsigmondy analogue). (If r happens to lie in Q'_p, N' has a square
       factor; omega(N') >= |Q'_p| still.)
Proof. Dyadic P, p ∈ [P,2P], x := P^2 L^{2B+4}; modulus R1 = 8p * prod_{3<=l<=D} l <= x^{1/2}(log x)^{-B} for large P.
Allowed classes mod R1: a_2 mod 8p (≡7 mod 8) times residues ≢ 0,1 mod each l: count prod(l-2) >= 1.
[BV] with A=3: #{p ∈ [P,2P]: psi(x;R1,a) < x/(2phi(R1)) for some allowed a} << P/L^2 = o(pi-count).
For the other p, partial summation (psi-theta << sqrt x << x/(phi(R1) L)) gives >> x/(phi(R1) log x) >> P L^{2B+2}
primes ≡ a (R1) in [p^2, x]; take k' (even) of them with k' = (log2/2 - eps)p/L + O(1).
Size: log prod Q'_p <= k' log x = (log 2 - 2 eps)p + O(p loglog p / L).
r: CRT class mod R := 2^i p^j * prod l, namely r ≡ M_p (prod Q'_p)^{-1} (mod 2^i p^j) [this is ≡ 7 mod 8 since k' even
and M_p ≡ 7, ≡ 1 mod p since M_p ≡ 1 mod p], and r ≡ -1 mod each l. Coprime class. [HB]: r <= c_0 R^{5.5},
log r <= 5.5(eps p log2/12 + eps p/12) + O_D(1) <= 0.78 eps p. Total log N' <= (log2 - 1.2 eps)p + o(p).  QED
Corollary B'. No statement of the form "every finite set Q of primes with properties (i)–(iv) (for some N' ≡ M_p mod 2^i p^j)
has |Q| <= c p/log p", c < log2/2, holds for all large p. Any improvement of the constant must use exact divisibility
(2^p ≡ 1 mod q, i.e. depth m_q ≈ sqrt q) for a positive proportion of the q in W, or the 2-adic congruence at depth
>= eps p/12 bits (Lemma D2 shows the full 2-adic congruence is equivalent to N = M_p, i.e. to the problem itself).
UNPROVED extension: matching M_p mod a fixed R0 that shares primes l <= D needs a least-prime-in-Chebotarev-class bound;
not needed for the barrier.

---------------------------------------------------------------------------------------------------
## D. Exact-divisibility routes tested (each step labelled)

D1 (multiplicative relations among the q's / M_p mod small moduli / mod p^2). PROVED (Thm B): any finite set of congruences
of M_p modulo 2^i p^j R0 (R0 fixed, coprime to p and to l<=D, i,j as in B) is matched by fake N'. The per-q conditions
"2 ∈ (F_q^*)^{m_q}" are single bits; the only identity coupling different q is prod q^{v_q} = M_p (size + congruences).
Breaking point: no known reciprocity law relates (2/q)_{m_q} for different q with m_q ~ p (Eisenstein reciprocity has fixed
prime degree; here the degree varies with q). Fake-model status: everything used is matched by N'.

D2 (cofactor / S-unit 1 + AB = 2^p). PROVED (trivial lemma): if 0 < N < 2^p and N ≡ -1 (mod 2^p) then N = 2^p - 1.
So "1+AB = 2^p" carries no information beyond A | M_p unless B is constrained; B = M_p/A is arbitrary with prime factors
> X. S-unit/Baker–Yu theory needs AB to be S-smooth or bounds v_q (multiplicity). The extremal configuration has all
v_q = 1 (Theorem A only uses prod q, not q^{v_q}), so multiplicity bounds cannot help: CIRCULAR / VACUOUS.
"ord_A 2 = p" is equivalent to A | M_p: no extra content. Thm B matches 2-adic congruences up to depth eps p/12.

D3 (Lenstra / Coppersmith–Howgrave-Graham–Nagaraj). PROVED: pigeonhole over classes mod s >= M_p^{1/4+eps} gives at best
2^omega <= C(eps) s, i.e. omega <= (1/4+eps)p + O(1) — worse than p/log p by a factor log p. To win one needs all 2^omega
divisors in <= 2^{O(p/log p)} classes mod some s >= 2^{p/4}; the only known class constraints are mod 8p (bounded depth)
and d e ≡ -1 (mod 2^p), which constrains pairs, not classes of d. Breaking point: no candidate modulus.

D4 (Stepanov / Heath-Brown–Konyagin / additive energy of H_q). Fake-invariant: H_q = <2> = mu_p is the UNIQUE subgroup of
order p of F_q^*, so any bound on |H ∩ (H+a)|, Heilbronn sums, BGK sums holds for mu_p in every F_q with q ≡ 1 (p) and
never sees "2 ∈ H". The 2-dependent version (coincidences 2^a+2^b ≡ 2^c+2^d mod q <=> q | sparse u) PROVED quantitatively:
E(H) >= p^4/q, trivial solutions <= 2p^2, and 2^a+2^b-2^c-2^d = 0 only trivially (binary uniqueness); each nonzero u has
<= (p+1)log2/log(2p) prime factors ≡ 1 (2p). Hence sum_{q|M_p} (p^4/q - 2p^2) <= p^4 (p+1) log 2/log(2p), i.e.
sum_{q|M_p} 1/q <= O(p/log p) + 2 omega/p^2 — weaker than the trivial sum_{q|M_p} 1/q <= 1 by a factor p. Inserting a
Corvaja–Zannier/Levin gcd bound (omega(gcd(u,M_p)) <= eps p/log p) only changes p/log p to eps p/log p: still useless.
Breaking point: forced coincidences per q are the equidistribution count p^{2T}/q, the number of sparse u is p^{2T-1}:
counting loses a factor q/p >= p.

D5 (large sieve with chi(2) = 1 — genuinely uses exact divisibility). PROVED: for q | M_p, the characters mod q trivial on
mu_p are exactly those with chi^{m_q} = 1; there are m_q - 1 nontrivial ones, all primitive, and chi(2) = 1 for each.
[LS] with a_n = 1_{n = 2^t, 0<=t<J}, N = 2^{J-1}, J = 1 + ceil(2 log_2 R):
  sum_{q|M_p, q<=R} (m_q - 1) <= (R^2 + 2^{J-1}) / J <= 3R^2/(2 log_2 R).
Trivially sum_{q|M_p,q<=R} m_q <= (R/p) omega <= R. So this exact-divisibility step loses a factor R/log R. Breaking point:
the only n with chi(n) known are 2-powers, density log N / N; the large sieve's R^2 duality term dominates.

D6 (Kummer–Chebotarev, even under GRH). CITED (Lagarias–Odlyzko 1977, GRH form: |pi_C(x) - (|C|/|G|) Li x| <=
c((|C|/|G|) x^{1/2} log(d_L x^{n_L}) + log d_L)). For q ∈ W the condition is splitting in K_m = Q(zeta_m, 2^{1/m}),
n_L ≈ m phi(m) ≈ p^2 ≈ q: the error BOUND is >= c sqrt(x) log x vs main term ~ 1/log p: useless even on GRH; and pointwise there is ONE
candidate q = pm+1 per m, so Chebotarev (a count of primes) is not even the right object. Window m ~ sqrt q is exactly
Hooley's middle range in Artin's conjecture, where only Brun–Titchmarsh (fake-invariant) is available.

D7 (dense divisibility in [2p, p^{1+delta}]). PROVED: any set of primes ≡ 1 (2p) in [2p, X] with X <= p^2/(2 log p) has
at most X/(2p) elements, so log(product) <= (X/2p) log X <= (p/(4 log p)) * 2 log p = p/2 < p log 2. So size can never refute
divisibility by ALL such primes below p^2/(2 log p); a refutation must use exact divisibility at depth m <= p/(2 log p).
For X = Kp (K fixed) dense divisibility is predicted to occur infinitely often (Bateman–Horn + Chebotarev; UNPROVED
heuristic, e.g. 2p+1 prime and p ≡ 3 mod 4 already forces 2p+1 | M_p), so no theorem can refute it there without
disproving that heuristic. For X = p^{1+delta} it is heuristically impossible, but every known tool is D1/D4/D5/D6.
Size refutation becomes available only for X >= p^2 L^{C} (almost all p, via [BV]): PROVED but fake-invariant and weak.

---------------------------------------------------------------------------------------------------
## Numerics (numerics.py; exhaustive over q = 2pk+1 <= p^2)
- p <= 6000: max #{q <= p^2 : q | M_p} = 4 (p = 397); mean 0.57; extremal value (log2/2)p/log p ≈ 236 at p ≈ 6000.
- Consistent with the given data (count <= omega for every p <= 293; 0 violations).
- Second-order bounds (naive / BT / (log2/2)p/log p): p=1e5+3: 3457 / 3382 / 3010; p=1e7+19: 239907 / 232322 / 215022.
Reality is ~p/(log p) times smaller than any proven bound; the gap is entirely in W, where only Thm B-type information is available.

## Fake-model status
A, C, B, D7: fake-invariant by design (B is an explicit fake model, proving the barrier). D5 and D4(2-dependent) are the
only steps that use exact divisibility; both are proved and both are quantitatively weaker than trivial. D2: circular.
No step of a would-be improvement survives the hostile re-read; none is claimed.
