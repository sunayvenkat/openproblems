# Erdős #396 — shared working notes (main thread)

**Problem.** For every k ≥ 0, is there n with ∏_{i=0}^{k}(n−i) | C(2n,n)?
Let E_k = set of such n. Known: k ≤ 14 by computer (OEIS A375077; k=14 min n = 359503904702190).
Open: even whether E_1 is infinite. Pomerance: n−k | C(2n,n) infinitely often; ∏(n+i) | C(2n,n) density 1.
Ford–Konyagin: density of {n : n | C(2n,n)} is 0.1142...

## Kummer facts
- ν_p(C(2n,n)) = #{s ≥ 1 : (n mod p^s) ≥ p^s/2} = #{s ≥ 1 : ⌊2n/p^s⌋ odd} = number of carries in n+n base p.
- Equivalent form: n ∈ E_k ⟺ (2n)!(n−k−1)!/(n!)^3 ∈ Z ⟺ ∀p: 3 s_p(n) ≥ s_p(2n) + s_p(n−k−1) + k + 1.

## Lemma 1 (local reduction at large primes)
q prime, q > 2i, q^v || N := n−i (v ≥ 1), w = N/q^v. Then base-q digits of n are (digits of i) then (digits of w) shifted by v.
Hence ν_q(C(2n,n)) = ν_q(C(2w,w)) = ν_q(C(2N,N)). So for q > 2k the condition at q only concerns each N = n−i separately:
**q^{ν_q(N)} | C(2N,N)** ("N is a q-governor"). This is the forum's "small prime barrier".

## Small primes by CRT
If n ≡ −1 (mod p^e) with e > ν_p((k+1)!), then ν_p(C(2n,n)) ≥ e and Σ_i ν_p(n−i) = ν_p((k+1)!). So small primes are automatic.

## Algebraic families (Balog–Wooley style)
Choose M = M_0 B^L with M/j a perfect m_j-th power for each j ≤ k+1:
need e_p := ν_p(M_0) ≡ ν_p(j) (mod m_j) ∀p,j. CRT ⇒ m_j pairwise coprime (j/j' is never an ℓ-th power for large ℓ).
Then A_j := (M/j)^{1/m_j} = c_j B^{L/m_j}.

### Family "−": n = M − 1, n−i = j(A_j^{m_j} − 1), j = i+1.  **BAD under H**:
the piece A_j − 1 = q prime gives n = j(1+q)^{m} − 1, whose base-q digits are j·C(m,r) (all small).
So there are no carries, and the condition fails. In general Φ_1-type pieces are fatal.

### Family "+": n = M + (k+1), n−i = j'(A^{m}+1) with j' = k+1−i ∈ [1,k+1], m = m_{j'} odd.
A^m + 1 = ∏_{d|m} Φ_{2d}(A). Size condition: all pieces must be ≤ √(2n), so φ(m)/m < 1/2.
- Small primes p ≤ k+1: n ≡ k+1 (mod p^{e_p}). Carries come from the digits of M/p^{e_p} = U_p B^L.
  B^L ranges over an open subgroup of Z_p^*, so choose B mod p^{R'} to make the high digits p−1. Then there are enough carries.
- Irreducibility: Φ_{2d}(c B^r) (r = L/m coprime to 2m) is irreducible in B iff c is not an ℓ-th power for primes ℓ | r.
  This holds because c_{j'}'s exponent vector ≡ (ν(j'')−ν(j'))/m mod ℓ.
- No fixed prime divisor: for p ≤ k+1, M ≡ 0 mod p^{e_p}, so ∏(M/j'+1) ≡ 1. For other p, take B ≡ 0 mod p.
- So **under Schinzel's Hypothesis H** there are infinitely many B (in the progression) with every piece Φ_{2d}(A_{j'}) prime.
  Then n−i = j' × (distinct huge primes), and the only remaining condition is ≥ 1 carry for each piece.

### Carry criterion for a piece (polynomial/Laurent form)
Piece f = Φ_{2d}(x), monic in x = A_{j'}; δ = deg f = φ(d). For s ≥ 1:
the fractional part of (x^m+1)/f(x)^{s+1} as x → +∞ is the negative-power part of its Laurent expansion at ∞
= Σ_{N>E} c_N x^{E−N}, where E = m − (s+1)δ and c_N = [t^N] (1+t^m) f(t)^{−(s+1)} (f palindromic).
Carry at level s+1 ⟺ the first nonzero c_N (N > E) is **negative**.
**Piece good ⟺ some s ∈ [1, ⌊m/δ⌋−1] gives a negative first coefficient.** This is independent of j', c, B.
Use the product formula Φ_n(t) = ∏_{e|n}(1−t^e)^{μ(n/e)} for power series (code: lemC.py).

### Data so far
- m=105: all non-top pieces good; **top piece d=105 BAD** (first coeff at N=10 positive).
- m=165 (3·5·11), m=195 (3·5·13): **all pieces good**.
- Theory needed: infinitely many pairwise-coprime odd "good" m with φ(m)/m < 1/2, each m containing many primes.
  Only small m are computable, so a structural proof is needed.
  - Lemma A: non-top pieces (d < m, N = m/d ≥ 3 odd) are good. Expected via the alternating binomial expansion of (y−1)^N with y = x^d + 1.
  - Lemma C: the top piece d = m. Lowest digit lc = [t^{m−2φ+1}] Φ_{2m}(t)^{−2}, the first nonzero one. Also lc(u mod f) = Tr(u(ζ)/f'(ζ)).

### Goal theorem
**Hypothesis H ⇒ E_k is infinite for every k.** It remains to prove Lemmas A and C (or find a workaround).
