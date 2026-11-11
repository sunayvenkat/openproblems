# Directions D and E: rigorous no-go lemmas (NO-RESOLUTION)

Notation. p >= 5 prime, M = M_p = 2^p - 1, Phi = Phi_{2p}(2) = (2^p+1)/3, F = (2^{p-1}-1)/p.
K = Q(zeta), zeta = zeta_p, alpha = 2 - zeta, beta = 2 + zeta (so alpha + beta = 4).
Prime factors with multiplicity: M = prod_{i<=w} q_i, q_i = 1 + 2p m_i (w = Omega(M)); Phi = prod Q_j^{v_j}, Q_j = 1 + 2p n_j.
Status tags: PROVED / CITED / UNPROVED. All theorem/chapter numbers in citations are from memory (no internet) and unverified; the statements are standard.
No CITED result is used in any claimed bound on beta_K - they enter only no-go remarks.

## D. p-adic symmetric-function constraints

**D1 (PROVED).** sum_{k=1}^{w} (2p)^{k-1} e_k(m_1..m_w) = F exactly; likewise sum_k (2p)^{k-1} e_k(n) = F/3 (an integer: 3 | 2^{p-1}-1, p != 3).
Proof: expand prod(1+2p m_i) = 1 + sum_k (2p)^k e_k, set equal to M = 1 + 2pF; Phi = 1 + 2p(F/3) since (2^p+1)/3 - 1 = (2^p-2)/3. Checked numerically for all p <= 109 (t1_data.py).

**D2 (PROVED). The whole depth-J content of D is one group equation.** For J >= 1, the reduction of D1 mod p^J reads
sum_{k=1}^{J} (2p)^{k-1} e_k == F (mod p^J)   <=>   prod_i (1 + 2p m_i) == M (mod p^{J+1}),
because terms with k > J carry p^{k-1}, k-1 >= J, and both sides are odd. Let U_J = {x in (Z/p^{J+1})^* : x == 1 mod p}, cyclic of order p^J;
m -> 1+2pm is a bijection Z/p^J -> U_J. Multiplication U_J^w -> U_J is a surjective homomorphism, so the solution set in (Z/p^J)^w is a coset of size exactly
**p^{J(w-1)}**, i.e. density p^{-J} **independent of w**. Every residue pattern is realised by infinitely many primes (Dirichlet, modulus 2p^{J+1}).
Hence: for no w >= 1 and no J does "many factors" force an impossible congruence pattern. (Brute-force check of the count: p = 5,7,11, J = 1,2, w = 2,3; t2_fibres.py.)

**D3 (PROVED). Individual e_k are not pinned.** For w >= 3, J = 2: e_1 mod p^2 takes every value == F (mod p) on the solution set.
Proof: the condition is sum_i u_i == u_0 (mod p^2), u = log_p(1+2pm)/(2p) == m - p m^2 (mod p^2). With sum m_i = F + pt, this becomes
sum m_i^2 == c(t) (mod p). Put m_4..m_w = 0, m_3 = F - m_1 - m_2 (mod p): m_1^2 + m_2^2 + (F-m_1-m_2)^2 is a quadratic polynomial whose quadratic
part 2(m_1^2 + m_1 m_2 + m_2^2) has discriminant -3*4 != 0 (p != 3), hence (after completing squares: nondegenerate binary form + const) it takes every value mod p.
Lift m_1 mod p^2 to fix sum m_i == F + pt. (Observed numerically for real factorizations: (e_1 - F)/p mod p takes many values, p <= 109.)
Wieferich case (F == 0 mod p) only forces e_1 == 0 mod p. Nothing more.

**D4 (PROVED, structural).** If p^{J+1} > M then D at depth J with 0 < prod q_i < p^{J+1} forces prod q_i = M exactly; so full-depth D is the
statement "the q_i are the prime factorisation of M", whose unique solution is the real one; it cannot be contradicted, and gives no bound on w.

**D5 (fake-model test; CITED, used only for the no-go).** D survives the fake models. Given a fake model whose largest fake prime is q* >= Y^L,
Y = 8p^{J+1}R (R the bounded modulus of all congruence conditions kept), replace q* by a prime q** == q* (mod 8R), q** == M * (prod of other fake primes)^{-1}
(mod p^{J+1}), q** in (q*/Y, q*]. Existence: Linnik's theorem in the quantitative form psi(x;Y,a) >= c x /(phi(Y) sqrt Y) for x >= Y^L
(Iwaniec-Kowalski, Analytic Number Theory, Ch. 18; theorem number not verified from memory) together with the trivial bound psi(x/Y;Y,a) <= (x/Y^2+1) log x.
Size changes by a factor <= Y, i.e. log changes by O(J log p) = o(p) for J = o(p/log p). Non-abelian bounded-depth conditions (e.g. quartic residuacity of 2)
would need a Linnik-type least prime in a fixed Chebotarev class (Lagarias-Montgomery-Odlyzko type) - CITED loosely, not checked. Conclusion: any argument using D at depth J = o(p/log p)
plus bounded-depth laws plus sizes fails audit check 1; at depth >= p log 2/log p, D is D4 (tautological).

**Verdict D: dead in principle (i).**

## E. Coupling alpha = 2 - zeta with beta = 2 + zeta

**E1 (PROVED).** N(beta) = Phi_p(-2) = Phi. For p >= 5: every Q | Phi has ord_Q 2 = 2p (Q odd, Q != 3 since v_3(2^p+1) = 1, Q not dividing M as gcd(2^p-1,2^p+1)=1),
so Q == 1 (mod 2p), Q splits completely in K, and the only prime above Q containing beta is (Q, zeta+2) (need a == -2 for (Q, zeta - a)); it occurs to the exponent v_Q(Phi)
since Z[zeta]/(beta) = Z/Phi. Hence #prime ideals of beta = omega(Phi) <= log_2 tau(Phi) = log_2(tau(2^p+1)/2) <= log_2(K/2). Same for alpha with omega(M).
Data check: omega(M), omega(Phi), tau(2^p+1) recomputed for p <= 109 agree with the given data.

**E2 (PROVED). p-th power level = D mod p.** With (x/P)_p == x^{(NP-1)/p} mod P: at P = (q, zeta-2), 2 == zeta, so (2/P)_p = zeta^{(q-1)/p} = zeta^{2 m_q};
at P = (Q, zeta+2), 2 == -zeta and (Q-1)/p even, so (2/P)_p = zeta^{2 n_Q}. Thus (2/alpha)_p = zeta^{2F}, (2/beta)_p = zeta^{2F/3} (by D1 mod p).
Stickelberger (CITED: Washington, Introduction to Cyclotomic Fields, Thm 6.2 / Ireland-Rosen Ch. 14: (g(chi_P)^p) = P^{theta}, theta = sum_{a} a sigma_a^{-1})
gives prod_q g(chi_q)^{p v_q} = eps * prod_a sigma_a^{-1}(alpha)^a with eps a unit; since theta + (complex conj) theta = p * Norm, |tau(eps)| = 1 for all embeddings tau,
so eps is a root of unity (Kronecker). The Gauss-sum product identity therefore carries one root of unity of information - the D-mod-p congruence (classical Eisenstein route).

**E3 (PROVED). Collapse of every power-residue law between alpha and beta.** Let n >= 1, n = p^j n' (p not dividing n'), L = Q(zeta_{lcm(p,n)}),
gcd(n, M Phi) = 1. Then
  (beta/alpha O_L)_n = (4/alpha O_L)_n = zeta_p^{ 4F [L:M_j] u }   and   (alpha/beta O_L)_n = (4/beta O_L)_n = zeta_p^{ (4F/3) [L:M_j] u },
with M_j = Q(zeta_{p^j}), u == n'^{-1} (mod p); both are 1 if j = 0.
Proof. alpha == 4 mod beta and beta == 4 mod alpha. Let P | q | alpha be a prime of L, f its residue degree over q. x := 4 has order p mod q and lies in <r>, r := zeta mod P (r = 2).
(i) n'-part: computed in M' = K(zeta_{n'}) (norm compatibility (x/P)_{L} = (x/N_{L/M'}P)_{M'} for x in M', mu_{n'} in M' - PROVED directly from x^{(N^f-1)/n'} and N == 1 mod n').
The local symbol eps == x^{(q^f-1)/n'} lies in mu_{n'} and in <x>, of order p; gcd(n',p)=1 so eps = 1.
(ii) p^j-part, in M_j (j >= 1): G = Gal(M_j/K) = {a == 1 mod p} acts trivially on mu_p, eps = zeta_p^{t(q^f-1)/p^j} (x = r^t, t = 2 for x = 4 at alpha, t = 2 at beta with r = -2),
product over the [G:D] = p^{j-1}/f primes gives zeta_p^{t (q^f-1)/p^j * p^{j-1}/f}; writing q = 1 + p^s u0 one checks (q^f-1)/p^j * p^{j-1}/f == (q-1)/p (mod p) in both cases s >= j, s < j
(binomial expansion, p odd). So the p^j-part equals the p-th power symbol in K, i.e. E2. (iii) combine: the symbol lies in mu_n, its p^{j}-th power is 1 by (i), its n'-th power is given by (ii).
Consequence (with the general reciprocity law, CITED: Neukirch, Algebraic Number Theory, Ch. VI Thm 8.3: (a/b)_n (b/a)_n^{-1} = prod_{v | n inf} (a,b)_v for coprime a,b prime to n,
in a field containing mu_n; L totally complex): every n-th power reciprocity law between alpha and beta reduces to prod_{v|n}(alpha,beta)_v = zeta_p^{-8F[L:M_j]u/3},
an identity in which **neither side depends on the factorisations** of alpha or beta (only on p, n, F). Laws of degree m = (q-1)/p are the case n = m.

**E3' (PROVED). Other numerators.** Any gamma in Z[zeta] satisfies gamma == gamma(2) (mod (q, zeta-2)), so symbols at primes of alpha reduce to symbols of rational
integers c. For p not dividing n and c in Q^* (coprime to alpha, n): (c/alpha O_L)_n is in {+-1}, and = 1 if n is odd. Proof: G = Gal(L/K) = (Z/n)^* permutes the primes over q
transitively, (c/sigma P) = sigma((c/P)); eps := (c/P) lies in mu_g, g = gcd(n, q-1) (c mod P is in F_q); product over G/D is eps^{sum of coset reps}, and the reps reduce mod g
to equal multiples of (Z/g)^*, whose sum is 0 mod g when g >= 3. For n = p: Eisenstein reciprocity (CITED: Ireland-Rosen, Ch. 14, Thm 1; zeta*alpha = 2zeta - zeta^2 is primary)
gives (c/alpha)_p = (zeta alpha / c)_p, computable mod c without factoring alpha - blind to omega(M).

**E4 (PROVED). Degree-(q-1)/p information at divisors is tautological.** For q | M and any n | q-1 with p not dividing n, 2 is an n-th power mod q, because <2> has order p
and p*n | q-1. So "2 is an m-th power residue mod q" (m = (q-1)/p) is equivalent to ord_q 2 = p and adds nothing at the divisors; its whole content sits at the
primes q == 1 (mod 2p) that do NOT divide M. Reciprocity laws about alpha only see primes dividing alpha. Same for -2 at Q | Phi.
Per-prime exact form (CITED identity J(chi,chi) = conj(chi)(4) J(chi,rho), Berndt-Evans-Williams, Gauss and Jacobi Sums, Thm 2.1.4; verified numerically for all q < 400, t5_jacobi.py):
q | 2^{2p}-1 with q == 1 (2p)  <=>  J(chi,chi) = J(chi,rho) for every chi of order dividing (q-1)/p, order >= 3. These identities live in Q(zeta_{m_q}), a field depending on q;
no law links fields Q(zeta_{m_q}) and Q(zeta_{n_Q}); the only link between {q} and {Q} is M + 2 = 3 Phi, whose reductions mod q (3 Phi == 2) and mod Q (M == -2) are tautologies.

**E5 (PROVED, remark).** Additive coupling (alpha + beta = 4, M + 2 = 3 Phi, norm forms 1 - (sqrt2)^p, 1 + (sqrt-2)^p, and in Q(zeta_8): i^p(1-s) + (1 + i^p s) = 1 + i^p, s = sqrt2^p)
is of abc/Mason type; such inequalities bound rad from BELOW and are consistent with M squarefree with many factors; they cannot bound omega(M) from above.

**E6 (heuristic, UNPROVED).** Function-field analogue: over F_l, omega(T^p - 1) = omega(T^p + 1) = 1 + (p-1)/ord_p(l) exactly - perfect coupling, produced by the automorphism T -> -T
(Frobenius orbits on mu_p vs -mu_p). Z has no automorphism moving 2 to -2; in the standard independent (Wagstaff-type) model the events q | M_p and Q | Phi are Chebotarev
conditions in unrelated Kummer fields Q(zeta_m, 2^{1/m}), Q(zeta_n, (-2)^{1/n}), so conditioning on tau(2^p+1) <= K does not change the law of omega(M_p).

**Verdict E: dead in principle (i)** for reciprocity / Stickelberger / norm-form couplings (E3-E5). What remains is the unconditional counting problem.

## Breaking point (both)
Needed: for p in P_K, #{q <= 2^p : q == 1 (2p), 2^p == 1 (q)} <= exp(o(log p / loglog p)).
Known (to my knowledge, unconditionally, for any infinite set of p): <= (log2/2 + o(1)) p / log p (Brun-Titchmarsh). Heuristic truth: ~ C log p.
