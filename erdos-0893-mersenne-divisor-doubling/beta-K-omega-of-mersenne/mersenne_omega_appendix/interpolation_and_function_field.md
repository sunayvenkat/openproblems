# W5 (wild card) — NOT a proof of the conjecture

Verdict: NO-RESOLUTION. This file holds only the proved obstruction lemmas for the two lines pursued.
Every statement is labelled PROVED / CITED / UNPROVED. Numerical sanity checks: `checks.py` (same folder), all pass.

Notation: p odd prime, M_p = 2^p - 1, q always a prime dividing M_p, v_q = v_q(M_p).

## Basic facts (PROVED)
- F1. q ≡ 1 (mod 2p), so q ≥ 2p+1 and ω(M_p) ≤ p·log2 / log(2p+1). (ord_q 2 = p, q odd, Fermat; then (2p+1)^ω ≤ M_p < 2^p.)
- F2. v_q(M_p) = v_q(2^{q-1} - 1). (LTE: v_q(2^{pk}-1) = v_q(2^p-1)+v_q(k) with k=(q-1)/p, q ∤ k.) Checked numerically for p ≤ 127.
- F3. Σ_{q|M_p} log q/(q-1) ≤ (log 2)/2, and Σ_{q|M_p, q>p^2} log q/(q-1) ≤ (2 log p + 1)/p.
  Proof: x ↦ log x/(x-1) is decreasing on x > 1 (derivative sign = 1 - 1/x - log x < 0). Each term ≤ log(2p+1)/(2p); multiply by F1.
  Second: each term ≤ log(p^2)/(p^2-1) ≤ (2log p+1)/p^2, times ω ≤ p. Data: max over p ≤ 127 is 0.3243 ≤ 0.3466.

## Line 1: Schneider–Lang / Mahler interpolation of z ↦ 2^z at all q | M_p simultaneously

Class 𝒯: choose P(X,Y) = Σ_{i≤L1, j≤L2} a_ij X^i Y^j ∈ Z[X,Y]; study the integers g(n) = P(n, 2^n), using
(a) archimedean size, (b) q-adic information at q | M_p coming from analyticity of z ↦ 2^z on classes mod p,
(c) Siegel's lemma / zero estimates. (Derivatives are excluded from global combination because d/dz 2^z produces
log 2 at ∞ and log_q 2 at q, which are not values of one algebraic number; this is why Schneider–Lang's hypothesis
"the derivation maps K[f1,f2] to itself" fails for (z, 2^z) over any number field K. Only integer values can be
combined through the product formula.)

**Lemma T1 (residue reduction, PROVED; uses exact divisibility).** If n = r + pk then g(n) ≡ P(n, 2^r) (mod q^{v_q}).
Proof: 2^n = 2^r (2^p)^k and 2^p ≡ 1 (mod q^{v_q}).
Corollary: if g vanishes mod q at > L1 integers of the class r that are distinct mod q (automatic for k < q), then
q | c_i(2^r) for every i, where c_i(Y) = Σ_j a_ij Y^j. So all q-specific vanishing data are statements
"q divides the sparse integer Σ_{j≤L2} a_ij 2^{jr}" — exactly Direction B (round-1 failure: needs a uniform-in-L2
gcd bound gcd(Σ a_j 2^{jr}, 2^p-1) that is false/unknown).

**Lemma T2 (factorisation-blind extrapolation, PROVED; valid for every n0 ≥ 1, prime or not).**
Let n0 ≥ 1, M = 2^{n0} - 1, r ≥ 0, G(k) = P(r + n0 k, 2^{r+n0 k}). Then Δ^s G(0) ≡ 0 (mod M^{max(0,s-L1)}).
Hence if G(0) = … = G(N-1) = 0 with N > L1, then M^{N-L1} | G(k) for every k ≥ 0.
Proof: G(k) = Σ_j c_j(k) β_j^k with β_j = (1+M)^j and c_j ∈ Z[k] of degree ≤ L1. For one term,
Δ(c β^k) = β^k [(β-1)E + Δ] c, so Δ^s(cβ^k) = β^k Σ_t C(s,t)(β-1)^t E^t Δ^{s-t} c. Terms with s - t > L1 vanish, and
M | β - 1, so every surviving term at k = 0 is an integer divisible by M^{s-L1}. Newton's formula
G(k) = Σ_{s≤k} C(k,s) Δ^s G(0) (exact for integer k ≥ 0) and Δ^s G(0) = 0 for s < N give the corollary.
Checked numerically for n0 ∈ {7, 11, 12, 30}.

**Proposition T3 (the bounds are PROVED via F3; "only place" describes the standard q-adic Schwarz lemma and is not a theorem).** The only place where individual q enter q-adic analytic extrapolation (Schwarz lemma for
exp(λ_q z), |λ_q|_q = |M_p|_q) is the factorial loss q^{N/(q-1)} per place; over all q | M_p it totals
exp(N Σ log q/(q-1)) ≤ 2^{N/2} (F3), against the main term M_p^N ≈ 2^{pN}; and primes q > p^2 contribute at most
exp(N(2log p+1)/p). Lemma T2 shows even that loss is avoidable (no q appears at all).
So the analytic part of 𝒯 cannot distinguish "M_p has one prime factor > p^2" from "M_p has p^{c/loglog p} of them".

**Theorem T (obstruction for 𝒯, PROVED as a decomposition; the meta-conclusion is informal).**
Every q-adic input to 𝒯 is either (i) a consequence of Lemma T2, whose proof never uses primality of the exponent and
holds verbatim for M_n, n composite, where ω(M_n) ≥ τ(n) - 2 (so (i) alone fails the composite calibration), or
(ii) the residue condition of Lemma T1, i.e. q | Σ_j a_j 2^{jr}, which is Direction B.
Moreover in the Siegel + Liouville count for (ii) the only quantity that appears is Σ_r log D_r = Σ_q |R_q| log q
(D_r = Π_{q: r ∈ R_q} q, R_q the prescribed vanishing classes), which is independent of how the total is split
among primes; the inequality is Liouville-tight for every split (round-1 failure A). ω never enters.
Breaking point: a lower bound for gcd structure of sparse integers Σ_{j≤L} a_j 2^{jr} against 2^p - 1, uniform in L
growing with p. UNPROVED (and round 1 found the needed uniform gcd bound false).

## Line 2: function-field analogue

Let l be an odd prime, A = F_l[T], a ∈ A of degree d ≥ 1, p an odd prime ≠ l, f = ord_p(l). ω, τ count monic
irreducible / monic divisors.

**Theorem FF (PROVED).** (1) ω(a^p - 1) ≤ d(1 + (p-1)/f), with equality for a = T.
(2) ω(a^p + 1) ≥ (p-1)/f, hence τ(a^p+1) ≥ 2^{(p-1)/f}.
(3) Therefore τ(a^p+1) ≤ K ⇒ ω(a^p - 1) ≤ d(1 + log_2 K): the FF analogue of β_K = 0 holds, with ω even bounded.
Proof. Over the algebraic closure a^p ∓ 1 = Π_ζ (a - ζ) over ζ ∈ μ_p (resp. -μ_p). For ζ ≠ ζ' the factors differ
by the nonzero constant ζ' - ζ, so are coprime. Frobenius orbits on μ_p∖{1} and on -μ_p∖{-1} all have size f
(l odd so ord_{2p} l = f); N_O = Π_{ζ∈O}(a - ζ) ∈ A, pairwise coprime, nonconstant (degree df). This gives (2).
For (1): an irreducible P | N_O has a root θ with a(θ) = ζ, so F_l(θ) ⊇ F_l(ζ) = F_{l^f} and f | deg P; since
Σ_{P|N_O} deg P ≤ df, N_O has ≤ d distinct irreducible factors; a - 1 has ≤ d. For a = T, Φ_p(T) splits into
exactly (p-1)/f irreducibles. (3): τ ≥ 2^ω. Checked on 108 random cases (l ∈ {3,5,7}, p ≤ 13, d ≤ 3).

**Why it does not transfer (PROVED as stated).** Part (1) is exactly the trivial degree bound: every prime dividing
Φ_p(a) has residue field of size ≥ l^f. Its Z-analogue is F1 (q ≥ 2p+1), i.e. ω ≤ p log2/log(2p+1) — no gain.
The whole content of (3) is the coupling: the single constant-field Frobenius f controls both a^p - 1 and a^p + 1.
In Q(ζ_p) every prime over q | M_p and over q' | Φ_{2p}(2) has residue degree 1 (prompt's exact dictionary), so
there is no common invariant; the Z-translation of (3) is a coupling inequality ω(Φ_{2p}(2)) ≥ G(ω(M_p)) with G
unbounded, which is Direction E (round-1 failure) and which the fake models (which fake Φ_p(2) and Φ_{2p}(2)
independently) do not constrain. Data: p = 43, 79, 191 have Φ_{2p}(2) prime and ω(M_p) = 3, 3, 5.
Abc / Mason–Stothers is irrelevant: they bound the radical from below, never ω from above (M_p is nearly squarefree).

Faithful (geometric) analogue — context only, nothing depends on it. CITED from memory, not re-verified
(Rosen, Number Theory in Function Fields, GTM 210, Ch. 12): for the Carlitz module C and monic irreducible P of
degree n, a prime Q ∤ P divides C_P(1) iff the Carlitz annihilator of 1 mod Q is (P); then P | Q - 1. deg C_P(1) is about
l^{n-1}, so the trivial bound is ω(C_P(1)) ≲ |P|/(l n), the analogue of p/log p. Bounding this further is, as far as
I can determine, open: RH for curves gives effective Chebotarev, but the relevant Carlitz–Kummer fields have genus
~ |Q|^2/|P|^2, so error terms exceed main terms once deg Q > (1+ε) deg P (UNPROVED estimate).
So the only FF case that is provable is the constant-field one, and its mechanism has no number-field counterpart.

## Calibration and fake-model status
- T2 holds for composite exponent ⇒ it alone fails the calibration; T1 is the only step using exact divisibility
  (2^p ≡ 1 mod q^{v_q}); it fails in fake models; it leads only to Direction B.
- FF (3) uses p prime only to make all orbits the same size f; for odd composite n the same argument gives
  ω(a^n-1) ≤ d·log_2 K. This is consistent because τ(a^n+1) ≤ K already forces few orbits. The Z-analogue (P_K
  forces τ(n) small via Zsigmondy for Φ_{2e}(2), e | n) is also true. The calibration is not violated, but the
  Z-transfer needs coupling.
