# Direction F / set-level routes: rigorous record (NO-RESOLUTION)

Notation: p prime, a_p = Phi_{2p}(2) = (2^p+1)/3, M_p = 2^p-1. Omega counts prime factors with multiplicity.
Status tags: PROVED, CITED, HEURISTIC, OPEN (to my knowledge; no literature check was possible offline).

## Lemmas

**L1 (PROVED).** p >= 5 implies 3 || 2^p+1, a_p = (2^p+1)/3, gcd(a_p, 3) = 1, tau(2^p+1) = 2 tau(a_p).
Proof: ord_9(2) = 6 and p = +-1 mod 6, so 2^p = 2 or 5 mod 9 and 2^p+1 = 3 or 6 mod 9. Also Phi_{2p}(x) = (x^p+1)/(x+1).

**L2 (PROVED).** Let p >= 5.
(a) Every prime Q | a_p has ord_Q 2 = 2p, so Q = 1 mod 2p. Also Q = 1 or 3 mod 8, and Q = 1 mod 8 iff Q = 1 mod 4.
(b) a_p = 3 mod 8. So the number of prime factors Q = 3 mod 8, counted with multiplicity, is odd. a_p is not a square, tau(a_p) is even, and tau(2^p+1) = 0 mod 4.
(c) Every prime q | M_p has ord_q 2 = p, q = 1 mod 2p, and q = +-1 mod 8.

Proof of (a). Q is odd and Q != 3 by L1. Q != p, because 2^p+1 = 3 mod p. Q divides 2^{2p}-1, but Q does not divide 2^p-1 (else Q | 2) and does not divide 2^2-1. Hence ord_Q 2 = 2p.
By Euler's criterion, (2/Q) = 1 iff 2p | (Q-1)/2 iff 4p | Q-1 iff 4 | Q-1, using p odd and p | Q-1.
If Q = 1 mod 4, then (2/Q) = 1, so Q = +-1 mod 8, hence Q = 1 mod 8. If Q = 3 mod 4, then (2/Q) = -1, so Q = +-3 mod 8, hence Q = 3 mod 8.

Proof of (b). 2^p+1 = 1 mod 8, and 3^{-1} = 3 mod 8. Odd squares are 1 mod 8.

Proof of (c). 2 = (2^{(p+1)/2})^2 mod q.

Verification: checked numerically by full factorization of a_p for all 5 <= p <= 113 (phi.py, phi_out.txt). The tau values agree with the prompt's data.

**L3 (PROVED, disjoint fibres).** For every integer d > 1, at most one prime p >= 5 has d | a_p, and at most one prime p has d | M_p. No prime divides both some a_p and some M_{p'}.
Proof: take a prime Q | d and use ord_Q 2 from L2, which is 2p or p'.

**L4 (PROVED, no covering).** Let S be any set of primes. Then #{p >= 5 : gcd(a_p M_p, prod S) > 1} <= |S|. For finite S, a_p M_p is coprime to S once 2p+1 > max S.
Corollary: no Sierpinski-type covering-congruence argument, using finitely many fixed moduli, can force a_p to be composite for all large p.

**L5 (PROVED, Euler-Lagrange).** Let p >= 5 with q = 2p+1 prime. If p = 1 mod 4, then q | a_p. If p = 3 mod 4, then q | M_p. These divisors are proper for p >= 7, and for p >= 5 respectively.
Proof: 2^p = (2/q) mod q, and q = 3 mod 8 or q = 7 mod 8 respectively.

**L6 (PROVED, no finite polynomial certificate).** Let f_1, ..., f_m be nonconstant polynomials in Z[x]. Consider the primes p for which no f_j(p) divides a_p (the trivial case f_j(p) = +-1 is excluded automatically). This set has positive lower relative density among the primes. The same holds with M_p in place of a_p.

Proof.
Case f_j(0) = 0. Then p | f_j(p), but p does not divide a_p. Also f_j(p) = 0 divides nothing. So f_j(p) never divides a_p.
Case f_j(0) != 0. Schur's theorem (proof below) says that infinitely many primes divide nonzero values of f_j. So choose pairwise distinct primes l_j that do not divide f_j(0), with l_j | f_j(n_j) for some integer n_j. Set r_j = n_j mod l_j. Then r_j != 0 mod l_j.
By CRT and Dirichlet's theorem (CITED: Dirichlet 1837, primes p = r mod L with gcd(r, L) = 1 have relative density 1/phi(L)), the primes p = r_j mod l_j for all j have relative density prod 1/(l_j - 1) > 0.
For such p > max l_j, l_j divides f_j(p), so f_j(p) is not +-1. If f_j(p) divided a_p, then l_j would divide a_p. That contradicts L2(a), since every prime factor of a_p is >= 2p+1 > l_j.

Schur's theorem (PROVED). Suppose only the primes l_1..l_s divide nonzero values of f. Let a_0 = f(0) != 0 and N = l_1...l_s. Then f(a_0 N y) = a_0 (1 + N y h(y)) with h in Z[y], and 1 + N y h(y) is nonconstant. Pick y with 1 + N y h(y) not in {0, 1, -1}. That value is 1 mod every l_i, so it has a prime factor outside the list. Contradiction.

Meaning of L6: "for each large p, exhibit a divisor of a_p from a fixed finite family" (such as 2p+1 in L5, or 2kp+1 with k bounded) can never prove P_K finite.

**L7 (PROVED, elementary).** Let n >= 1. Then Omega(n) <= tau(n) - 1, because prod (1 + a_i) >= 1 + sum a_i. Also omega(n) <= log_2 tau(n) and tau(n) <= 2^Omega(n).
Consequences:
- p in P_K with p >= 5 implies tau(a_p) <= K/2, Omega(a_p) <= K/2 - 1 and omega(a_p) <= log_2(K/2).
- The P_K are nested, so beta_K is nondecreasing in K. By L2(b), beta_K = beta_{4 floor(K/4)}.

**L8 (PROVED).** M_p is composite iff omega(M_p) >= 2.
Proof. Suppose M_p = q^k with k >= 2. If k is even, then q^k = 1 mod 4, but M_p = 3 mod 4. If k is odd, then q^k + 1 = (q+1)(q^{k-1} - ... + 1), and the second factor is odd and > 1, so it cannot divide 2^p.

## Theorems (route 3: what each route would solve)

**Thm A (PROVED).** Suppose beta_K > 0 for some K >= 4, and fix 0 < c < beta_K. Then infinitely many primes p satisfy all of the following at once:
(i) Omega(a_p) <= K/2 - 1 and omega(a_p) <= log_2(K/2). Every prime factor of a_p is = 1 mod 2p and lies in {1, 3} mod 8.
(ii) omega(M_p) >= exp(c log p / log log p). In particular M_p is composite, and omega(M_p) >= (log p)^A for every fixed A.
Proof: by definition, beta_K > 0 forces P_K to be infinite and the limsup to exceed c. Then apply L1, L2 and L7.
So a disproof would prove: (a) infinitely many composite Mersenne numbers M_p (OPEN); (b) infinitely many p with a_p a bounded almost-prime (OPEN). It would prove both at once, on one common set of p.

**Thm B (PROVED).** Suppose P_K is finite. Then for all large p, tau(a_p) >= 2 floor(K/4) + 2. In particular:
- a_p is composite for all large p;
- there are only finitely many Wagstaff primes;
- there are infinitely many composite a_p (OPEN).
Also, P_K is finite for every K iff Omega(a_p) -> infinity (by L7). Route 2 can prove beta_K = 0 for all K only by proving this, which is the opposite of the standard Wagstaff-type heuristic (HEURISTIC: #{p <= x : a_p prime} ~ C log x).

**Thm C (PROVED, sieve breaking point).** Let A = (a_p) for 5 <= p <= x, and let S(A, z) be the number of p for which a_p has no prime factor < z. Then S(A, z) >= pi(x) - 2 - pi(z), by L3. So sifting below z = o(x) is free.
To get Omega(a_p) <= C one must sift up to z = a_p^{1/(C+1)}, which is about 2^{p/(C+1)}. In the range x < Q < 2^{x/(C+1)}, every count |A_Q| is 0 or 1 by L3. The only information there is the exact event 2^p = -1 mod Q. That is the unbounded-depth condition the fake models scramble.
A level of distribution D that is polynomial in |A| = pi(x) reaches only z of size x^{O(1)}. In a weighted sieve, the Omega bound scales like log(max a)/log D, which is about x / log x. That matches the trivial bound and gives nothing. (This last sentence is a method-scope remark, not a theorem about all methods.)

## Computations (scratchpad\F)
- check.py / check_out_2000.txt: a BPSW test (self-tested against a sieve up to 2*10^5 and against known base-2 strong pseudoprimes). It finds the Wagstaff exponents 5 < p <= 2000 to be exactly 5,7,11,13,17,19,23,31,43,61,79,101,127,167,191,199,313,347,701,1709. These are probable primes only, not primality proofs. The list matches the data's tau = 4 list for p <= 293. The run also checks L2(b) for p < 3000, L3 for 600 primes, and L5 for p < 20000.
- omega.py: the complete factorizations of M_p for p in P_4 with p <= 127 reproduce the data's omega values (11:2, 23:2, 43:3, 79:3, 101:2, rest 1).
- phi.py / phi_out.txt: factorizations of a_p for 5 <= p <= 113 confirm L2 and the data's tau(2^p+1).
