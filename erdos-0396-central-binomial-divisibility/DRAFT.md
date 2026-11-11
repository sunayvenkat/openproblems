# Erdős Problem #396 — E₁ and E₂ are infinite: positive density along quadratic families (working draft)

**Problem.** Is it true that for every k ≥ 0 there is an n with ∏_{i=0}^{k} (n−i) | C(2n,n)?

Write E_k for the set of such n. By computer, E_k is non-empty for k ≤ 16 (OEIS A375077, 16 terms as of July 2026). Whether E_1 is infinite was open; §12 gives an unconditional proof that E₁ and E₂ are infinite (Theorems C and D), awaiting an independent line-by-line check.

## 0. Results

**Theorem A (conditional on Dickson's conjecture for one 4-tuple).** Put P₁ = 14x+3, P₂ = 24x+17, P₃ = 24x+5, P₄ = 7x+5. Then P₁P₂ − 2P₃P₄ = 1 identically. If x ≥ 9 and all four values are prime, then n = P₁P₂ ∈ E₁. The tuple is admissible, so Dickson's conjecture for this single tuple implies that E₁ is infinite (§11).

**Theorem B (conditional on Dickson's conjecture for one 6-tuple).** Put x = 42y+9 and
- n = 3(70x+31)(252x+113),
- n−1 = 2(84x+37)(315x+142),
- n−2 = 7(180x+79)(42x+19).
If y ≥ 1 and the six linear factors are prime, then n ∈ E₂. So E₂ is infinite under Dickson's conjecture for one admissible 6-tuple, with no Conjecture G (§11).

**Theorem C (E₁ is infinite; unconditional, §12).** Put n(x) = (12x−1)(22x+9), so that n−1 = 2(11x−1)(12x+5). There is a residue class x ≡ x₀ (mod M) and a constant c > 0 such that #{x ≤ X : x ≡ x₀ (mod M), n(x) ∈ E₁} ≥ cX for all large X. In particular E₁ is infinite and #(E₁ ∩ [1,N]) ≫ N^{1/2}. No prime values of the forms are needed: the argument is a first-moment (union) bound over the prime factors of the four forms, and the limiting first moment is 0.549·(2/5) + 4·0.0479 = 0.411 < 1. The family n = 2(12x+5)(35x+32), n−1 = (70x+29)(12x+11) gives 0.375.

**Theorem D (E₂ is infinite; unconditional, §12).** Put n(x) = (14x−1)(15x−1), so that n−1 = x(210x−29) and n−2 = (6x−1)(35x+1). Then a positive proportion of x in a suitable residue class give n(x) ∈ E₂. The limiting first moment is 0.549·(5/6) + 6·0.0479 = 0.745 < 1.

The two inputs are (i) an exact "square-class rule" for the carry at a prime q | P(x) with cofactor below q/(2|κ|) (Lemma S), and (ii) joint equidistribution of all base-q digits of n(x) over x ≡ x_q (mod q) for medium primes q (Lemma W), which is a quadratic Weyl-sum estimate because the leading coefficient of n(x_q + qt)/q in t carries a factor q. Everything else is Kummer, the Chinese remainder theorem and the prime number theorem in progressions. See §12 for statements, proofs, the complete classification of quadratic families (three squares in arithmetic progression), and numerics.

These two theorems supersede Theorem 1 below: they need prime values of a few linear forms instead of Hypothesis H for 133 polynomials of degree up to about 4·10⁷. They come from agent g5 and were re-verified independently (`g/verify_g5.py`).

**Theorem 1 (conditional on Schinzel's Hypothesis H).** There are infinitely many n with n(n−1) | C(2n,n). That is, E_1 is infinite.
- The proof is an explicit construction (§8).
- It needs a finite computation: the sign of certain Laurent coefficients for the exponents 123 and 59814755.
- That computation is done (§8.4). All 5 pieces of n−1 and all 128 pieces of n are good.
- 105 pieces are settled by short proofs (A1(a), (b), (d)) or by exact level-2 coefficients (A1(e)).
- The other 28 each have an exact decisive coefficient: F(±y), the top piece of m₂, and 25 deep pieces.
- 23 of those 28 were cross-checked independently, by agent V or by the trace formula of §5.1.

**Theorem 2 (conditional on H and Conjecture G).** E_k is infinite for every k.
- *Conjecture G:* there are infinitely many pairwise coprime odd "good" exponents m (§4).
- More precisely, E_k is infinite under H as soon as one has k+1 pairwise coprime good exponents with all prime factors > log₂(k+1). Alternatively, k such exponents plus one coprime "Aurifeuillean-good" exponent suffice (§7).

**New tools** (proved unless marked):
- a digit criterion for carries (§4);
- an autocorrelation formula for the top piece (§6.1);
- an Aurifeuillean carry criterion (§7);
- inheritance and sufficient conditions for pieces (§5).

**Negative results:**
- Lemma A (all non-top pieces are good) is false: 1365 is a counterexample.
- Aurifeuillean splitting with a prime exponent never works.
- At most one block member can use Aurifeuillean splitting.
- No polynomial family under H produces new good exponents.
- The first-moment method of §12 needs linear pieces, and linear-piece families exist only for k ≤ 2: Fermat in one variable of degree 2, Yuzvinsky's bound on completely reducible fibers in several variables, and (empirically) no four split fibers in progression for cubics or quartics (§13). For k ≥ 3 the obstacle is the anatomy of quadratic polynomial values above the level X; §13.3 states the hypothesis BH_u under which a Ford–Konyagin-type argument would give every E_k.

---

## 1. Kummer and the local reduction

For a prime p, ν_p(C(2n,n)) equals the number of carries when adding n + n in base p, which is #{s ≥ 1 : (n mod p^s) ≥ p^s/2}.

**Lemma 1.** Let q be prime, 0 ≤ i < q/2, N = n − i, q^v ‖ N with v ≥ 1, and w = N/q^v. Then ν_q(C(2n,n)) = ν_q(C(2w,w)) = ν_q(C(2N,N)).

*Proof.*
- In base q, the lowest v digits of n are (i, 0, …, 0); the digits above them are those of w.
- Since 2i < q, the lowest v positions produce no carry.
- So the carries of n+n are exactly the carries of w+w, and the same holds for N+N. ∎

For q > 2k, at most one block member is divisible by q. The condition at q then says that the q-part of N = n−i divides C(2N,N).

Verified on 49478 random cases (agent V). The hypothesis q > 2i is necessary.

## 2. Small primes

Let p ≤ k+1 and n ≡ k+1 (mod p^e) with e ≥ ν_p((k+1)!) + 2.
- Then Σ_i ν_p(n−i) = ν_p((k+1)!).
- The carries of n+n at positions ≥ e include those of ⌊n/p^e⌋ + ⌊n/p^e⌋.
- So it suffices that ⌊n/p^e⌋ has at least ν_p((k+1)!) digits equal to p−1. For k = 1 this is automatic, because C(2n,n) is even.

## 3. The family F₊

Fix odd exponents m_1, …, m_{k+1}, pairwise coprime, with every prime factor > log₂(k+1). Put L = ∏ m_j.

**Exponents.**
- By the CRT, choose e_p for p ≤ k+1 with e_p ≡ ν_p(j) (mod m_j) for every j.
- Set M_0 = ∏ p^{e_p}. Then M_0/j = c_j^{m_j}.

**Polynomials.**
- Put M = M_0 B^L, n = M + (k+1) and A_j = c_j B^{L/m_j}.
- With j = k+1−i we get n − i = j(A_j^{m_j} + 1) = j ∏_{d|m_j} Φ_{2d}(A_j).

**Irreducibility.**
- Each Φ_{2d}(c_j B^{L/m_j}) is irreducible, by Capelli's theorem.
- c_j is not an ℓ-th power for ℓ | L/m_j, because j'/j is not an ℓ-th power when ℓ > log₂(k+1).
- The log₂ condition is necessary. Example (agent V): k = 7 with m_8 = 3 gives a reducible piece.

**Local conditions on B.**
- Small primes: x ↦ x^L has open image in Z_p^×, so B mod p^R can set the needed digits to p−1.
- No fixed prime divisor: for p ≤ k+1 the product of all pieces is ≡ 1; for any other p take B ≡ 0.

**Applying H.** Hypothesis H gives infinitely many B for which every piece is prime. For such B, n ∈ E_k iff every piece is *good* (§4).

Pairwise coprimality is forced: if ℓ | gcd(m_j, m_{j'}), then j/j' would have to be an ℓ-th power.

## 4. The carry criterion (digit form)

**Setup.** Let m be odd, d | m, f = Φ_{2d}, δ = φ(d) and T = ⌊m/δ⌋. Expand in base f:

  x^m + 1 = Σ_{k=0}^{T} D_k(x) f(x)^k,  with deg D_k < δ.

**Theorem 4.1** (agent AC, Thm 0). Let q = f(x) be prime with q ‖ n−i = j(x^m+1). Then for all large x,

  ν_q(C(2n,n)) = #{ s ∈ [1, T−1] : the last nonzero digit among D_1, …, D_s has negative leading coefficient }.

So the piece is *good* (at least one carry) iff some D_k with 1 ≤ k ≤ T−1 has negative leading coefficient.

*Indexing.* "Level s" is the carry of N + N at the digit position of q^{s+1}, because w = N/q. Agent V's report uses the carry exponent t = s+1.

**Equivalent forms.**
- The level-s sign is that of the first nonzero c_N, N > m − (s+1)δ, where c_N = [t^N] Φ_{2d}(t)^{−(s+1)}. Here t = 1/x, and palindromy is used.
- The factor j does not change the sign.
- The criterion was checked against direct Kummer computation with prime q in 12 cases; the carry counts match exactly (agent AC).

**Definition.** m is *good* if every piece Φ_{2d}, d | m, is good.

**Binomial reduction.** Let K = m/d, w = x^d + 1 = f·g and N = m/d. Then

  tail( (x^m+1)/f^{s+1} ) = Σ_{r=1}^{s} (−1)^{r+1} C(K,r) · tail( w^r / f^{s+1} ),

and [x^{−1−i}] tail(w^r/f^{s+1}) = [t^{rd−(s+1)δ+1+i}] (1+t^d)^r Φ_{2d}(t)^{−(s+1)}.

So the level-s sign of the piece d inside x^m+1 needs a series of length about s·d, not m (code: `aur/deep.py`).

## 5. Non-top pieces

**Digit formula.** Put w = x^d + 1 = f·g and K = m/d (odd). Then

  x^m + 1 = (w − 1)^K + 1 = Σ_{r=1}^{K} (−1)^{r+1} C(K,r) f^r g^r.

Writing g^r = Σ_j G_{r,j} f^j (deg G_{r,j} < δ) and collecting powers of f gives D_k = Σ_{r=1}^{k} (−1)^{r+1} C(K,r) G_{r,k−r}. The expansion is unique, because deg D_k < δ.

*Proof of A1(e) and A1(b).*
- D_2 = K·G_{1,1} − C(K,2)·G_{2,0}.
- If φ(d)/d > 1/2, then deg g = d − φ(d) < δ, so G_{1,1} = 0 and D_2 = −C(K,2)·(g² mod f). This is (e).
- If moreover φ(d)/d > 2/3, then deg g² = 2(d − φ(d)) < δ, so g² mod f = g². Since g is monic, lc(D_2) = −C(K,2) < 0. This is (b), and it needs only T ≥ 3.
- Similarly D_1 = K·(g mod f), and its leading coefficient is K > 0 whenever φ(d)/d > 1/2. So such pieces never carry at level 1.

**A1** (agent AC; proved).
- (a) d = 1 is good.
- (b) φ(d)/d > 2/3 ⇒ the piece is good at level 2, because D_2 = −C(K,2)g².
- (c) D_1 = K·(g mod f).
- (d) d = 3 is good.
- (e) φ(d)/d > 1/2 ⇒ D_2 = −C(K,2)(g² mod f), so the level-2 sign does not depend on K.

**Counterexample to Lemma A.** For m = 1365, the piece d = 455 has digit leads 3, 387, 13812, all positive.
- So the top piece of 1365 is good, but 1365 is not.
- Agent V confirmed this on a 709-digit prime Φ_910(288), which has 0 carries.

**Thm A3** (agent AC). For fixed squarefree d there is K_0(d) such that the piece is good for all odd K ≥ K_0(d).

**5.1 Trace predictor.**
- At a root ζ of f, L'Hôpital gives γ := g(ζ) = −H(ζ)/2, where H = (x^{2d} − 1)/Φ_{2d}. Also 1/f′(ζ) = ζH(ζ)/(2d).
- Lagrange interpolation then gives the x^{δ−1} coefficient of D_k: (−1)^{k+1} C(K,k) Σ_ζ γ^k/f′(ζ) + O(K^{k−1}) = −(K^k/(d·k!))·a_{k+1} + O(K^{k−1}), where a_n = Tr(ζ·(H(ζ)/2)^n). This matches agent AC's Thm A3.
- So for large K, level k is negative iff a_{k+1} > 0.
- The sign pattern of a_n is set by the conjugate pair with the largest |H|. It oscillates with period 2π/arg H.
- Check (`aur/trace.py`): for 9 pieces of m₂ with K ≥ 7 and exact first negative level in 3–5, the predicted first negative level was correct in all 9.
- For d = 319865 (K = 187) the dominant pair has arg H = ±0.0577π. The prediction was "positive through level 13, negative at level 14", and the exact computation confirmed it (−1.52·10^102).

**5.2 Exact low levels and effective A3 (agent g3, `code/g3/`).** Write δ = φ(d), θ = δ/d and ζ = e^{iπa/d}.
- Closed forms (checked numerically to 10^−10): |H(ζ)| = 2∏_{q|d,q>1}|2cos(πa/2q)|^{−μ(q)}; Re(ζH′/H) = (2d−δ)/2 exactly; τ_a := Im(ζH′/H)/d = −½Σ_{q|d,q>1}μ(q)tan(πa/2q)/q.
- **Lemma X (proved).** If (k+1)δ > (k−1)d + 1, then [x^{δ−1}]D_k = −C(K,k)·a_{k+1}/d exactly, for every odd K. Proof: a digit G_{r,j} of g^r reaches degree δ−1 only if (j+1)δ ≤ r(d−δ)+1; with r = k−j and j ≥ 1 this forces (k+1)δ ≤ (k−1)d+1.
  - In the band ½ < θ ≤ ⅔ this covers levels k ≤ 3, and k ≤ 4 when θ > 3/5. So a band piece is good for every K ≥ 3 if a₃ > 0 or a₄ > 0, and for every K ≥ 5 if θ > 3/5 and a₅ > 0.
  - It explains the counterexample 1365 (piece 455): the first n with a_n > 0 is 5, i.e. level 4, but T−1 = 3 when K = 3.
- **Theorem E (effective A3; proof sketch only).** Substituting x = ζe^{w/d} and integrating on the circle |w| = k/|K+β| gives
  S_k(K) = −(1/(d·k!)) Σ_ζ ζ(H/2)^{k+1}(K+β_ζ)^k(1+E_ζ),  β_ζ = 1/d + (k+1)(−θ/2 + iτ_ζ),
  with |E_ζ| ≤ e√k·(exp(0.3(k+1)k²/|K+β|²) − 1) + k!·e^{|β|+0.3(k+1)}/|K+β|^k for d ≥ 10³. The real shift is the same for all ζ, so only τ and the O(k^{3.5}/K²) term affect the sign. The shifted predictor is within 0.3% of the exact values for d = 319865, K = 187, k = 2..14 (the unshifted one is off by up to 48%).
- **Prop F (sketch).** If one conjugate pair dominates with modulus gap η and arg H(ζ₀) ∉ πZ, some n ≤ log(4δ/η)/η + 6/|sin θ₀| + 3 has a_n ≥ |z₀|^n/4. So the threshold K₀(d) is effective, but it depends on d.
- **Why this does not give G.** If all primes are ≥ P, every band piece has ω(d) ≥ 0.405P, while its cofactor K can be a single prime. Prop F needs K ≳ (log δ/η)² with log δ of size P^C, and no uniform bounds on η, θ₀, τ over such d are known. Beyond Lemma X the sign depends on K and must be computed. The first negative level also grows with ω(d): among 3-free band d, the share with first level ≥ 5 is 0, 0.05, 0.12, 0.15 for ω = 3, 4, 5, 6. There is no parity effect.
- Numerics: in 59814755, 46881835 and 37182145 every non-top piece is good, and the large-K predicted first level equals the actual one in 186 of 187 band pieces.

**Thm I (inheritance).** Let p ∤ m be prime with p > (s+1)φ(d). Then level s of piece dp in x^{mp}+1 has the same first coefficient as level s of piece d in x^m+1.
- So if m is good, mp is good for all large primes p.
- Example: 165p is good for every prime p > 160, and 195p for every prime p > 192.
- These families share primes, so they never give coprime exponents.

## 6. The top piece

**6.1 Autocorrelation formula.** For the top piece and T = 2, the decisive coefficient is

  c_{E+1} = [y^{m−1}] Ψ_m(y)² = −Σ_i ψ_i ψ_{i+φ(m)−1},

where Ψ_m = (y^m−1)/Φ_m = Σ ψ_i y^i is the inverse cyclotomic polynomial.
- In words: m is top-good at level 1 iff the autocorrelation of the coefficients of Ψ_m at lag φ(m)−1 is positive.
- Equivalently, c_{E+1} = (1/m)·Tr_{Q(ζ_m)/Q}(ζ Ψ_m(ζ)²).
- Checked on 105, 165, 195, 1155 and 1365 (`aur/autocorr.py`; agent AC's `cosform.py` checks the cosine form).

**6.2 Regimes.**
- μ(m) = −1 and T ≤ E < p_min ⇒ good at the last level. More generally, Prop C1 of agent AC.
- These need m/φ(m) to lie extremely close above an integer, a Lehmer-type condition.

**6.3 No parametric shortcut.**
- By Thm I and the two-scale formula, the sign along any family with growing primes is the sign of a fixed core.
- m/φ(m) ≥ 2 forces the core itself to have ratio ≥ 2.
- So Hypothesis H cannot manufacture new coprime good exponents. Goodness of the top piece is a property of specific integers.

**6.4 Data.**
- 738 of 1487 odd squarefree m ≤ 3·10^5 with φ(m)/m < 1/2 are fully good. **Needs recheck:** agent g3 found that agent AC's `fastser.py` reconstructs values by CRT from only two primes, so it is valid only while |coefficient| < 2.3·10^18; larger values can come out with the wrong sign. Two of AC's claimed K = 5 failures are false (d = 30261 is good at level 7, d = 43435 at level 5); only d = 25179 is a real K = 5 failure. The 738/1487 count and AC's full scans rest on that code.
- Among 3-free m: 37182145 and 46881835 are bad; 50115065 and 59814755 are top-good. The exact first coefficient for 59814755 is −74322712269080.

## 7. Aurifeuillean splitting for one block member

Let m ≡ 3 (mod 4) be squarefree and x = m y². Then Φ_{2m}(m y²) = F(y)·F(−y) with F ∈ Z[y] irreducible of degree φ(m). Each factor has y-degree φ(m) < (deg n)/2 = m, so φ(m)/m < 1/2 is no longer needed.

**7.1 Explicit F.**
- The roots of F are χ(c)ζ_{4m}^c/√m, for c ∈ [1, 2m) coprime to 2m, where χ = (m/·) is the Jacobi symbol.
- Power sums: c_{4m}(k)/2 for even k (Ramanujan sums) and χ(k)√m for odd k (Gauss sums).
- Newton's identities then give F exactly (`aur/aurif3.py`).

**7.2 Integrality lemma.**
- Write F(±y) = C(x) ± m y D(x) with C, D ∈ Z[x], so that 1/F(y)^t = F(−y)^t / Φ_{2m}(x)^t.
- Hence for every integer y, N/F(y)^t = (an integer) + T_t(y), where N = (my²)^m + 1 and T_t(y) → 0. The integer comes from polynomial parts in Z[x] and y·Z[x].
- So F(y) gets a carry at position t iff T_t(y) < 0, for large y. Checked at random y (`aur/autocorr.py`).

**7.3 The prime case fails.**
- The odd part y·(…) of the tail dominates the even part.
- So at each level exactly one of F(y), F(−y) carries.
- For prime m (and for m = 3, 15, 39, …) only one level exists, or the same factor wins every level, so one factor never carries.
- Checked for p = 3, 7, 11, 19, 23. This matches agent AC's observation on 4X⁴+1.

**7.4 Composite m with two levels works.** Take m = 3q with q ≡ 1 (mod 4). The levels are t = 2, 3.
- m = 123, 183, 267: F(y) carries at t = 2 and F(−y) carries at t = 3.
- m = 15, 39, 51, 87, 111, 159, 219, 291: the same factor wins both levels.
- Source: `aur/scanA.py`.

**7.5 At most one block member.**
- Aurifeuillean splitting for j needs A_j ≡ m_j (mod squares).
- For two members j, j' and a prime P > k+1 dividing m_j m_{j'}, the exponent of P in c_j/c_{j'} is (e_P/L)(r_j − r_{j'}), which is even. It would have to be odd. So at most one j can use the splitting.

## 8. Proof of Theorem 1

**8.1 Data.**
- Exponents: m_1 = 123 = 3·41 (Aurifeuillean, block member n−1) and m_2 = 59814755 = 5·7·11·13·17·19·37 (block member n).
- Choose e with e ≡ 0 (mod 246) and e ≡ 1 (mod m_2), and set a = (e−1)/m_2.
- Put B = 123 b², L = 123·m_2, M = 2^e B^L and n = M + 2.

**8.2 Factorizations.**
- n − 1 = A_1^{123} + 1, where A_1 = 2^{e/123}B^{m_2} = 123 y² and y = 2^{e/246}·123^{(m_2−1)/2}·b^{m_2}. With x = 123y²:

  n − 1 = (x+1) · Φ_6(x) · Φ_82(x) · F(y) · F(−y).

- n = 2(A_2^{m_2} + 1) = 2 ∏_{d | m_2} Φ_{2d}(A_2), where A_2 = 2^{a}·123^{123}·b^{246}.

This gives 133 polynomials in b, each with positive leading coefficient.

**8.3 Hypotheses of H.**
- *Irreducibility.*
  - Φ_{2d}(A_2): Capelli with exponent 246. At a prime above 2 the valuation is −a, with a ≢ 0 (mod 3, 41). At 3 the valuation is 123, which is odd.
  - x+1, Φ_6(x), Φ_82(x): binomial or Capelli. The valuation at 2 is e/123 ≢ 0 mod every prime of m_2, and the square classes −1/41 and −1/123 are not squares in Q(√−3) and Q(ζ_41) respectively.
  - F(±κ b^{m_2}): F is the minimal polynomial of a single Galois orbit. θ/κ is not an ℓ-th power for ℓ | m_2, by the valuation at a prime above 2: v = −e_𝔭·e/246, with e/246 ≡ 246^{−1} (mod ℓ).
- *No fixed prime divisor:* b ≡ 0 (mod p) makes every piece ≡ 1 (mod p).

Under H there are infinitely many b for which all 133 values are prime. Then n(n−1) = 2·(distinct large primes).

**8.4 Carries.**
- Prime 2: ν_2(n(n−1)) = 1, and C(2n,n) is even.
- Odd primes: by Lemma 1 each piece needs one carry.
  - x+1, Φ_6(x), Φ_82(x): A1(a), (d) and (b) respectively, good at level 2.
  - F(y) and F(−y): carries at positions 2 and 3 respectively (§7.4).
  - The top piece of m_2: the exact coefficient −74322712269080 is negative, so it is good at level 1.
  - The non-top pieces of m_2: **all good**. `aur/coverage.py` classifies all 128 divisors:

| class | count | reason |
|---|---|---|
| top piece d = m₂ | 1 | level 1, coefficient −74322712269080 (exact; agent V recomputed it via [t^N]Ψ²) |
| φ(d)/d > 2/3 | 82 | A1(b): lc(D_2) = −C(K,2); T ≥ 3 holds for all of them |
| ½ < φ(d)/d ≤ ⅔, lc(g² mod f) > 0 | 20 | A1(e), good at level 2 (`aur/checkB.py`) |
| ½ < φ(d)/d ≤ ⅔, lc(g² mod f) < 0 | 25 | first negative level computed by `aur/deep.py` (below) |

   The only divisor with φ(d)/d ≤ ½ is d = m₂ itself. Every proper divisor has φ(d)/d ≥ φ(m₂/37)/(m₂/37) = 0.513.

   The 25 deep pieces, with first negative level s (carry at q^{s+1}) and K = m₂/d:

| s | pieces d (K) |
|---|---|
| 3 | 385, 595, 7315, 7735, 8645, 13585, 14245, 17765, 26455, 85085, 185185 (323), 242165 (247), 286195 (209), 323323 (185) |
| 4 | 455, 6545, 12155, 20995, 776815 (77), 1616615 (37), 8544965 (7) |
| 5 | 95095 (629), 270655 (221), 629629 (95) |
| 14 | 319865 (187) |

  - Agent V confirmed 12 of these independently, with a different series method (`agentV/periodic.py`) and direct integer tests at x = 10^15 and 10^30:
    - at s = 3: 385, 595, 7315, 7735, 8645, 13585, 14245, 17765;
    - at s = 4: 455, 6545, 12155, 20995.
  - The trace predictor of §5.1 independently agrees on 95095, 185185, 270655, 629629, 776815, 1616615, 8544965 and 319865.

**8.5 What the computation rests on.**
- Every decisive coefficient sits at offset 0 of its window. So no earlier coefficient can have been mistaken for zero.
- **Exact certificate (`g4/exact.py`, `g4/level2.py`, `g/top_exact.py`).** Every one of the 128 pieces is now certified with exact integer arithmetic; nothing rests on a probabilistic stopping rule.
  - The 25 deep pieces: the offset-0 coefficient X = [x^{φ(d)−1}]D_s is computed as an exact big integer (python-flint), using Φ_n^{−(s+1)} = (−1)^{s+1}Ψ_n^{s+1}(1−t^n)^{−(s+1)} and the binomial reduction of §5. All 25 values are negative and agree digit for digit with `strict_out.txt`. A self-check asserts X = [x^{φ−1}]D_s against direct base-f expansion for every d | m with m = 105 (s ≤ 30), 1155 (s ≤ 12) and 15015 (s ≤ 5).
  - Independent cross-check: |[t^j]Φ_n^{−(s+1)}| ≤ h^{s+1}C(j+s, s) with h = height(Ψ_n) gives an a priori bound B ≥ |X|. CRT over primes with product > 2B then determines X without the flint values; it agrees in all 25 cases. For d = 319865 this needs 14 primes (log₁₀B = 125.2), so the 13-prime acceptance of `strict.py` was not by itself rigorous, though its value was right.
  - The 20 A1(e) pieces: g = −Ψ_d(−x) is recomputed exactly, g·f = x^d + 1 is checked, and R = g² mod f has deg R = φ(d) − 1 and lc(R) > 0 in every case.
  - The 82 A1(b) pieces need no numerics: 3φ(d) > 2d and T ≥ 3 are checked in integers.
  - The top piece: [t^{ρ+1}]Φ_{2m₂}(t)^{−2} with ρ = 95075, by exact integer series over the divisors e ≤ ρ+1 of m₂, equals −74322712269080.
- Remaining trust: python-flint's polynomial arithmetic, and Thm 4.1 with the binomial reduction (the self-check tests the reduction only for small m).
- The sign-to-carry rule (Thm 4.1) was checked against direct Kummer counts with prime q in 12 cases (agent AC). Agent V tested it at large x for every piece of 15, 105, 165 and 195.

## 9. Conjecture G and all k

**Conjecture G.** For every P there is a good odd m whose prime factors all exceed P.

G implies infinitely many pairwise coprime good m, and hence Theorem 2. Evidence: about 50% of eligible m are fully good in every range tested.

G is also necessary for this method: pairwise coprime exponents can share no prime, so all but finitely many of them have every prime factor above any fixed P. Every exponent needs m/φ(m) ≥ 2, because a piece of degree more than half of deg(n−i) has a single cofactor digit below f/2. With all primes above P this forces about P²/(2 log P) prime factors.

**9.1 Localization (`g/crossing.py`, `g1/verify.py`).** Write A_n(t) = Φ_{2n}(t) = ∏_{e|n}(1+t^e)^{μ(n/e)} for odd n.
- L1. For a prime p ∤ n, A_{np}(t) = A_n(t^p)/A_n(t). Hence [t^N]A_{np}^{−k} = [t^N]A_n^{k} for N < p. Iterating, the coefficients below the smallest prime of m_> depend only on m_≤ and on the parity of ω(m_>).
- L2. For m = Mq with q ∤ M prime, and N < m: [t^N]Φ_{2m}^{−2} = (−1)^N[y^N]Φ_M(y)²Ψ_M(y^q)². Checked against the direct series for M = 15, 21, 33, 35, 39 and 255.
- L3 (crossing prime). Let M/φ(M) < 2, δ = 2φ(M) − M, and let q be a prime in (2φ(M)/(δ+1), 2φ(M)/δ]. Then m = Mq has T = 2 and ρ = m − 2φ(m) = 2φ(M) − qδ ∈ [0, q). The top piece of m is good iff the first nonzero coefficient of Φ_{2M}(t)² at an index > ρ is negative. The same holds for general T with δ_T = Tφ(M) − M.
- Inflation. If T(M) = 2 and q > 2φ(M) is prime with T(Mq) = 2, the decisive top coefficient of Mq equals that of M; only its offset moves (`g/inflate.py`, 8 cases). So adding a large prime never changes the top piece.

**9.2 Theorem W (agent g1).** Let T = 2, ρ = m − 2φ(m), let Q be the set of primes of m and p₁ < p₂ the two smallest. Then mod t^{p₁p₂}, Φ_{2m}^{−2} ≡ (1+t)^{−2μ(m)}∏_{q∈Q}(1+t^q)^{2μ(m)}.
- (i) μ(m) = −1: for 3 ≤ N ≤ 2p₁−1, c_N = −2(1_Q(N) + 2·1_Q(N−1) + 1_Q(N−2)) ≤ 0. So the top piece is good whenever 3 ≤ ρ ≤ p₁. ρ = 1 is bad, because c_2 = 1.
- (ii) μ(m) = +1 and ρ ≤ 2p₁−3: c_{ρ+1} = (ρ+2) − 2Σ_{q≤ρ+1}(ρ+2−q). So the top piece is bad for ρ ≤ p₁−2.
- Last-level rule for non-top pieces (r = m mod φ(d), r+1 < p₁(d)): μ(d) = +1 gives c_{r+1} = (−1)^{r+1}C(r+T_d, T_d−1); μ(d) = −1 gives C(T_d, r+1) > 0 if T_d > r, and first nonzero c_{p₁(d)} = −T_d if T_d ≤ r. Since ρ is odd and T_d ≥ 2(p₁−1) > ρ for d < m, every proper piece is bad at its last level. Near-Lehmer m rescue only the top piece.
- Checks: 9365 cases of (i)/(ii) and 4110 cases of the last-level rule against exact series, plus 376 direct base-f digit checks; no mismatch.

**9.3 Reduction.** G(P) follows from NL(P) and Band:
- NL(P): an odd squarefree m with all primes > P, μ(m) = −1, m/φ(m) > 2, and 3 ≤ m − 2φ(m) ≤ p₁(m).
- Band: every piece with ½ < φ(d)/d ≤ ⅔ is good. (Pieces with φ(d)/d > ⅔ are good by A1(b), since T_d ≥ 8 under NL.)
- Necessary condition for NL: if p, q | m and p | q−1, then p | ρ. So ρ < p₁ forbids every such pair, as in Lehmer's totient problem. Also m ≡ ρ (mod 2^{ω(m)+1}).

**9.4 Why NL is out of reach.**
- Searches (agent g1). P = 3, m ≤ 10^15: 20 values with ρ ≤ 10^6, the smallest ρ = 84875; 12 of the 20 are top-good. P = 5, m ≤ 10^26: smallest ρ = 679213406106576341.
- A random-squarefree model (exact DP over primes) predicts about A_P·X·ln Y P-rough m ≤ Y with 0 < ρ ≤ X, with A_3 = 1.8·10^−6, A_5 = 4.1·10^−18, A_7 = 5.2·10^−41, A_11 = 6.9·10^−71. It matches the P = 3 search (31 predicted, 20 found). The first m with ρ ≤ 2p₁ is expected near 10^{2.4·10^4} for P = 3 and 10^{7.6·10^15} for P = 5.
- Greedy prime chains M → Mp keep δ = 2φ(M) − M near φ(M)^θ, where θ is the prime-gap exponent. L3 needs a prime in an interval of length about 2φ/δ², so it works for θ < (3−√5)/2 ≈ 0.382. That holds under Cramér's conjecture but is not known even under RH. Adding several primes per step does not help: the count of solutions stays about φ(M)/δ².
- No existence theorem is known for composite n with n − kφ(n) small and positive (only upper bounds: Pomerance; Banks–Luca; Banks–Güloğlu–Nevans; Luca–Pomerance). Subset-product methods give multiplicative conditions such as λ(n) | n−1, which cannot hit the additive equation n − 2φ(n) = ρ.
- So NL(P) is a Lehmer-strength problem, probably harder than G itself. G needs a mechanism for the sign of the top coefficient of huge m that does not go through near-integrality of m/φ(m).

**9.5 Bulk analysis of the top piece (agent g2, `code/g2/`).**
- Ramanujan form: Φ_m(y)^{−1} = exp(Σ_n c_m(n)y^n/n) with c_m the Ramanujan sum; log Q_1 ≡ Σ_{N<m} c_m(N)y^N/N mod y^m.
- All levels at once: with a_s = [x^{φ−1}]D_s the offset-0 coefficient of level s,
  S(z) = Σ_s a_s z^s = [y^{m+1−φ}] 1/(Φ_m(y) − z·y^φ) = Σ_{Φ_{2m}(x)=z} (x^m+1)/Φ′_{2m}(x).
  The series form is checked for five m; the root-sum form only for φ ≤ 96. For T = 2, S(z) = a_1·z (since a_2 = 0 unless m = 3φ−1).
- T = 2 cosine form: a_1 = −(1/2π)∫|Ψ_m(e^{iθ})|² cos((φ−1)θ) dθ. It agrees with §6.1.
- **Peak lemma (proved).** Let χ be the even real character mod q for q = 8, 10 or 12, and suppose χ(p) = −1 for every p | m (p ≡ ±3 mod 8, p ≡ ±2 mod 5, or p ≡ ±5 mod 12 respectively). Then
  log|Ψ_m(ζ_q^b)| = χ(b)(−1)^r 2^r B_q + log|1 − ζ_q^{bm}|,  r = ω(m),
  with B_8 = ½ log(1+√2), B_10 = log((1+√5)/2), B_12 = ½ log(2+√3). Proof: a ↦ log|1 − ζ_q^{ab}| is even on (Z/q)^×, so only χ_0 and χ occur, and Σ_{e|m}μ(m/e)f(e) = ∏_{p|m}(f(p) − 1) for completely multiplicative f. So |Ψ_m| has a doubly exponential peak at q-th roots of unity, not tied to any core.
- Numerically the integral localizes: windows of ±0.02 turns around the peak roots reproduce the bulk coefficients of Q² (sign agreement 96.8%, 99.9%, 100% for q = 8 and r = 4, 5, 6). A Gaussian saddle at the peak predicts the level-1 sign in 6 of 7 test cases, including the top-good m = 43730115 = 3·5·11·13·19·29·37 (exact a_1 = −3.602·10^41).
- Negative results. There is no top-piece trace predictor (K = 1 gives no large parameter). There is no exponential saddle (Re(yQ′/Q) = D/2 on |y| = 1). The sum rules Σ D_k(±1) constrain digit values, not leading coefficients.
- Open: a rigorous bound |Ψ_m| ≤ exp((1−ε)B_q 2^r) away from the peaks, and the sign of the localized integral. Its phase depends on the large divisors m/p and looks equidistributed, so about half of each family should be top-good, but nothing forces it.

## 10. Reproducibility

All scripts and outputs are in `erdos396/code/`. Run them from inside their own folder; they import `../agentV/fastgood.py` and `../poly.py`.

| file | purpose |
|---|---|
| `aur/aurif3.py` | exact Aurifeuillean factor F for squarefree m ≡ 3 mod 4 (Newton identities in Q(√m)) |
| `aur/scanA.py` | carry levels of F(±y) for m = 3q; shows both factors carry for m = 123, 183, 267 |
| `aur/autocorr.py` | top-piece autocorrelation identity; integrality of the F(±y) quotient at random y |
| `aur/checkB.py` → `checkB_out.txt` | A1(e) level-2 test for all band pieces of 59814755 and 50115065 |
| `aur/deep.py` → `deep_out{1,2,3}.txt` | exact first negative level via the binomial reduction plus CRT |
| `aur/levels.py` → `lev319865.txt` | level-by-level scan of d = 319865 |
| `aur/trace.py` | large-K trace predictor (§5.1) |
| `aur/coverage.py` | audit: every divisor of m₂ is accounted for |
| `aur/strict.py` → `strict_out.txt` | strict CRT recheck of the 25 decisive coefficients |
| `agentAC/`, `agentV/`, `agentU/` | agents' reports (REPORT.md) and code |
| `g/crossing.py`, `g/LEMMAS.txt` | localization L1, two-scale L2, crossing prime L3 (§9.1) |
| `g/top_exact.py`, `g/inflate.py` | exact top coefficient of m₂; reflection, trace and inflation checks |
| `g/verify_g5.py` | independent check of Theorems A and B (§11) |
| `g1/` | near-Lehmer route: Theorem W, last-level rule, searches, heuristic (§9.2–9.4) |
| `g2/` | bulk analysis of the top piece, peak lemma (§9.5) |
| `g3/` | Lemma X, effective A3, float residue method `resid.py`, band surveys (§5.2); `RESULTS.txt` |
| `g4/exact.py`, `g4/level2.py` | exact certificate of all 127 non-top pieces of m₂ (§8.5) |
| `g5/` | linear-form families for E₁ and E₂ (§11) |

**Witnesses** (agent V; checked with Miller–Rabin, Pollard–Brent and a Kummer/Legendre cross-check):
- n = 2^35 + 2 = 34359738370 ∈ E_1. It comes from the F₊ family with (m_1, m_2) = (35, 17) and B = 1, and is the smallest F₊ member of E_1 up to 10^18.
- 481469424205826 ∈ E_1, from (5, 3) with B = 6.
- 2251799813685250 ∈ E_1, from (3, 5) with B = 8.
- 2·54^17 + 3 ∈ E_2.

**Fallback exponents.** 50115065 = 5·7·11·13·17·19·31 is top-good. It has a K = 5 band piece (d = 10023013). Agent g3 settled it with exact `deep.py`: levels 2–6 are positive and level 7 = T−1 is −3.2993·10^60, re-checked at two further primes, so the piece is good at its last level even though a₃, …, a₈ < 0. All 46 band pieces of 50115065 are then good, but 45 of them rest only on g3's floating-point residue method (`g3/resid.py`); they still need an exact check before 50115065 can be used. The alternatives 183 = 3·61 and 267 = 3·89 for m_1 also have both Aurifeuillean factors carrying.

## 11. Linear-form families: E₁ and E₂ from Dickson's conjecture

The principle: a prime f with f ∥ n−i, f > 2i and n−i = f·C gives base-f digits of n equal to i followed by the digits of C. There is a carry iff some digit is ≥ f/2. If C < f this means C ≥ f/2; if f < C < 2f it means C − f ≥ f/2. So a prime near √n is harmless when its cofactor has the right size. When f and C are linear in x with ratio R = lc(C)/lc(f), the condition is R ∈ [½, 1) or frac(R) ≥ ½, with the boundary cases decided by the constant terms. No cyclotomic structure and no Conjecture G is needed.

**Lemma Q (unconditional).** Let p < q and p′ < q′ be odd primes with pq − 2p′q′ = 1, 3p ≤ 2q < 4p, and 13p′ ≤ 4q′ < 14p′. Then n = pq ∈ E₁. (Agent g5 stated it without the upper bound 2q < 4p; the base-q step needs it.)

*Proof.* ν₂(n(n−1)) = 1 and C(2n,n) is even. Every odd prime factor of n(n−1) is one of p, q, p′, q′, each to the first power, and each exceeds 2. By Kummer it suffices to find one carry of n+n in each base.
- Base p: q = p + (q−p) with p/2 ≤ q−p < p, so n has the digit q−p ≥ p/2.
- Base q: n = p·q with q/2 ≤ p < q.
- Base q′: n = 1 + 2p′·q′ with q′/2 ≤ 2p′ < q′.
- Base p′: n = 1 + 2q′·p′ and 2q′ = 6p′ + r with p′/2 ≤ r < p′. ∎

**Proof of Theorem A.** The identity P₁P₂ − 2P₃P₄ = 1 is checked by expansion. For x ≥ 9 the inequalities of Lemma Q hold with (p, q, p′, q′) = (P₁, P₂, P₄, P₃): 3P₁ ≤ 2P₂ always; 2P₂ < 4P₁ iff x ≥ 3; 13P₄ ≤ 4P₃ iff x ≥ 9; 4P₃ < 14P₄ always. Admissibility: the forms have no common zero mod 2 (x ≡ 0), mod 3 (x ≡ 2) or mod 5 (x ≡ 1, 4), and four forms cannot cover all residues mod a prime ≥ 5 other than 5 (mod 5 they exclude only 0, 2, 3). So Dickson's conjecture gives infinitely many x with all four prime. Hardy–Littlewood would give ≫ X^{1/2}/log⁴ X elements of E₁ up to X. Agent g5 found 12 such quadruple families with leading coefficient ≤ 600. ∎

**Proof of Theorem B.** The identities n − (n−1) = 1 and n − (n−2) = 2 are checked by expansion.
- Prime 2: x is odd, so n is odd and n−1 = 2·(odd)(odd); ν₂ = 1 and C(2n,n) is even.
- Prime 3 (exactly divides n): the congruence x ≡ 9 (mod 42) forces the base-3 digit 2 at position 1 of n, a carry.
- Prime 7 (exactly divides n−2, and 7 > 4): the base-7 digit at position 1 of n is 4 ≥ 7/2, a carry.
- The six large primes, with cofactor C and f:
  - f = 70x+31, C = 756x+339: C − 10f = 56x+29 ≥ f/2.
  - f = 252x+113, C = 210x+93 ∈ [f/2, f).
  - f = 84x+37, C = 630x+284: C − 7f = 42x+25 ≥ f/2 (the ratio is exactly 7.5, so the constant terms decide).
  - f = 315x+142, C = 168x+74 ∈ [f/2, f), since 336x+148 ≥ 315x+142.
  - f = 180x+79, C = 294x+133: C − f = 114x+54 ≥ f/2.
  - f = 42x+19, C = 1260x+553 = 29f + (42x+2) with 42x+2 ≥ f/2 for x ≥ 1 (the ratio is exactly 30).
- All other digits (the low digits 0, 1, 2 and the top digits) are below f/2 and do not matter. ∎

**Checks.**
- Agent g5: all 265 x < 10⁶ with four primes give n ∈ E₁ (Theorem A), and all 11 y < 3·10⁵ with six primes give n ∈ E₂ (Theorem B). The smallest Theorem B value is n = 9322443046715199. C(2n,n) ≡ 0 mod n(n−1) was checked directly for n = 10462547.
- Independent re-check (`g/verify_g5.py`, sympy factorizations of n, n−1, n−2 and carry counts): 22 of 22 four-prime x in [9, 20000) give n ∈ E₁; the first three six-prime y (9993, 55110, 64073) give n ∈ E₂.

**Limits.**
- Each of n and n−1 needs at least two large primes, because a single prime factor above √(2n) has no carry. So four forms is the minimum for E₁, and Bunyakovsky for one polynomial cannot suffice.
- For quadratic n, n−i splits over Q iff disc(n) + 4·lc(n)·i is a square. For k ≥ 3 this needs four squares in arithmetic progression, which Fermat ruled out. So E₃ needs n of degree ≥ 3 with four reducible shifts; agent g6 is searching for such identities.
- The weakest hypothesis found for E₁ is "Hypothesis Q": infinitely many prime solutions of pq − 2p′q′ = 1 in the cone of Lemma Q (prime points on a rank-4 quadric, equivalently 2×2 matrices of determinant 1 with prime entries and a doubled corner). We do not know an unconditional result of this kind; circle methods would need about eight prime variables.
- Not checked: whether Theorems A and B are already in the literature.
- Unconditional routes examined by g5 and rejected: positive density of E₁ (empirical density 0.0126 up to 2·10⁶, but D₀ lacks the stability that Hildebrand–Teräväinen methods need); Chen-type almost-primes (parity barrier, uncontrolled digit events); Maynard–Tao (a good quadruple is fixed by three of its forms, so independent sets of size ≫ K^{1/3} avoid them).

## 12. Positive density along quadratic families (agent h1)

### 12.0 Summary

Let n(x) = λ₀P₁(x)P₂(x) with P_j = a_jx + b_j, and suppose n − i = λ_i P_{2i+1}P_{2i+2} for i = 1, …, k with linear forms over ℤ. Fix a large constant z₀ and a class x ≡ x₀ (mod M), M = ∏_{q ≤ z₀} q^{e_q}, on which no prime q ≤ z₀ divides any P_j(x) except as forced by the λ's, and with the forced 2-adic and small-prime carries built in. Then n(x) ∈ E_k iff for every prime q > z₀ dividing some P_j(x) the number of carries of n(x)+n(x) in base q is at least ν_q(∏(n−i)). The theorem of this section is a first-moment bound:

  #{x ≤ X in the class : n(x) ∉ E_k} ≤ (M_∞ + o(1)) · #{x ≤ X in the class},   M_∞ = 0.549·Σ_j f_j + 0.0479·(number of forms),

where f_j ∈ [0,1] is an explicit "failure fraction" of the form P_j computed from (a_j, b_j, the partner form, λ). If M_∞ < 1, a positive proportion of x in the class give n(x) ∈ E_k. For the families of Theorems C and D, M_∞ = 0.411 (resp. 0.375 for the second E₁ family) and 0.745.

The three regimes for a prime q | P_j(x), with cofactor c = P_j(x)/q and L = ⌊log(2n)/log q⌋:
- **Top (L ≤ 3, equivalently q ≳ √P_j):** the carry at the second digit is decided by the square class of q modulo a_j (Lemma S). The failing square classes have proportion f_j. The third digit (present iff L = 3) is a fair coin.
- **Medium (L ≥ 4, z₀ < q ≲ √P_j):** all L−1 relevant digits of n in base q are jointly equidistributed over x ≡ x_q (mod q) (Lemma W). The failure probability is 2^{1−L}.
- **Small (q ≤ z₀):** removed by the residue class (admissibility).

Agent h1's code is in `code/h1/`: `search2.py` (quadruple search ranked by Σf_j), `apsq.py` (complete enumeration of quadratic families via squares in arithmetic progression), `verify.py`, `ek.py`, `trend.py`, `sample.py` (brute force and sampled E₁/E₂ proportions), `lawcheck.py`, `rulecheck.py`, `detect.py` (tests of Lemma S and of the digit laws at x ≈ 10¹⁵).

### 12.1 Coins

For an odd prime q and n ≥ 1, Kummer gives ν_q(C(2n,n)) = #{s ≥ 1 : ⌊2n/q^s⌋ odd}. Call the parity of ⌊2n/q^s⌋ the *coin at level s*; "heads" is a carry. Let q ∥ n − i with 0 ≤ i ≤ k and q > 2k, write n − i = qm. Then ⌊2n/q⌋ = 2m + ⌊2i/q⌋ = 2m is even (this is Lemma 1 of §1: the first coin is always tails), and for s ≥ 2

  ⌊2n/q^s⌋ = ⌊2m/q^{s−1} + 2i/q^s⌋ = ⌊2m/q^{s−1}⌋,

because 2m/q^{s−1} has denominator q^{s−1} and 2i/q^s < 1/q^{s−1}. So the coin at level s is heads iff (m mod q^{s−1}) ≥ q^{s−1}/2 iff the base-q digit d_{s−2}(m) exceeds (q−1)/2, or equals (q−1)/2 with the lower part large. If q^{L−1} ≤ 2m < q^L there are exactly L−1 coins, at levels 2, …, L, and n ∉ E_k because of q iff all are tails (when ν_q = 1). The coin at level L is the parity of the leading digit of 2m; call it the *top coin*.

### 12.2 Lemma S: the square-class rule for large primes

**Lemma S.** Let P = ax + b, P′ = a′x + b′ with gcd(a,b) = gcd(a′,b′) = 1, κ = ab′ − a′b ≠ 0, λ ≥ 1, and let q be a prime with q ∤ aλκ, q | P(x), c = P(x)/q, and 2|κ|c < q. Put u = q̄² (mod a) where q̄q ≡ 1 (mod a), and r = (−λκbu) mod a ∈ {0, …, a−1}. Then the coin at level 2 of n with n − i = λP(x)P′(x), q ∥ n − i, is heads iff

  2r > a, or (2r = a and λκ > 0), or (r = 0 and λκ < 0).

In particular the outcome depends only on the square class of q modulo a. Define f(P; P′, λ) = (number of squares of units u mod a for which the rule fails)/(number of squares of units mod a); for a = 1 read u = 0.

*Proof.* Here m = λcP′(x). Since ax ≡ −b (mod q), P′(x) ≡ (a′(−b) + ab′)/a = κ/a (mod q), so the level-2 coin is decided by the digit d = (λcκ·a^{−1}) mod q, heads iff d > q/2. Write ad = λcκ + ρq with ρ ∈ ℤ determined by 0 ≤ d < q: ρ ≡ −λcκ q^{−1} (mod a). Now c ≡ Pq^{−1} ≡ bq^{−1} (mod a), so ρ ≡ −λκbq̄² = r (mod a). Set g = λcκ/q, so |g| < 1/2 by hypothesis. If λκ > 0 then g ∈ (0, ½), the window for ρ is (−g, a−g), so ρ = r, and d > q/2 iff r + g > a/2 iff 2r > a or (2r = a, since g > 0). If λκ < 0 then g ∈ (−½, 0), the window is (|g|, a+|g|), so ρ = r if r ≥ 1 and ρ = a if r = 0; the condition is ρ − |g| > a/2, i.e. 2r > a (as |g| < ½ and r integer), or r = 0 (then ρ = a and a − |g| > a/2). ∎

Remarks. (1) Since c ≡ bq^{−1} (mod a), the square class of q is a function of c mod a; the rule says which residue classes of the cofactor c are bad. (2) For q with q² > 2λP(x)P′(x) only level 2 exists, so the rule decides membership; for the next range (L = 3) a second coin exists. (3) If moreover 2n < q², i.e. the form has leading coefficient above √(2λ₀a₁a₂), such a q has no coin at all and n ∉ E_k; this happens for a proportion ≍ 1/log x of x and is part of the o(1). (4) The rule was checked against the actual carries at x ≈ 10⁹, 10¹², 10¹⁵ for the two families: 3568/3568 and 5696/5696 agreements at 10¹⁵ (`detect.py`).

Which a admit f = 0? The values −λκbu run over a coset of the subgroup of squares in (ℤ/a)^×, possibly multiplied by a non-unit; f = 0 iff that coset lies in (a/2, a). For (ℤ/a)^× of exponent 2 (a | 24) the squares are {1} and any single residue > a/2 works. Among a ≤ 60 the admissible values are 1, 2, 3, 4, 6, 8, 9, 12, 15, 16, 18, 20, 21, 24, 27, 28, 30, 32, 33, 36, 39, 40, 42, 44, 45, 48, 51, 52, 54, 56, 57, 60. For E₁ the complete enumeration (12.5) shows min Σf_j = 1/3 over all admissible quadruple families with λ₀a₁a₂ ≤ 3000; no family has Σf_j = 0.

### 12.3 Lemma W: medium primes

**Setting.** Fix a form P = ax + b dividing n − i (0 ≤ i ≤ k), its partner P′ = a′x + b′ and multiplier λ, so n − i = λPP′; put κ = ab′ − a′b ≠ 0. All leading coefficients are positive. Let q be a prime with q ∤ 2aa′λκ, q > 2k and q > z₀, where z₀ exceeds every prime dividing a resultant of two of the forms. Then q | P(x) iff x ≡ x_q (mod q), 0 ≤ x_q < q. Let X be large, T = X/q, and for x ∈ (X/2, X] write x = x_q + qt; t runs over an interval of length T/2 that we write as (T/2, T] (the shift by x_q/q < 1 changes nothing below). Put c₀ = P(x_q)/q, β = P′(x_q) and

  m(t) = (n − i)/q = λ(c₀ + at)(β + a′qt) = λaa′q·t² + λ(aβ + a′c₀q)·t + λc₀β.

(W1) *Bijection.* aβ = aa′x_q + ab′ ≡ −a′b + ab′ = κ (mod q). Hence m′(t) ≡ λκ ≢ 0 (mod q) for every t, and t ↦ m(t) is a bijection of ℤ/q^j for all j ≥ 1 (induction on j: m(t + q^{j−1}s) ≡ m(t) + q^{j−1}s·m′(t) (mod q^j)). So Σ_{t mod q^j} e(h m(t)/q^j) = 0 when q^j ∤ h, and for every interval I, |Σ_{t∈I} e(h m(t)/q^j)| ≤ min(|I|, q^j).

(W2) *Gained level.* For q ∤ h the phase h·m(t)/q^j is a real quadratic polynomial in t whose leading coefficient hλaa′/q^{j−1} is a reduced fraction with denominator q^{j−1}.

(W3) *Size.* For X ≥ X₀(forms) and x ∈ (X/2, X] one has aX/3 ≤ P(x) ≤ 2aX and a′X/3 ≤ P′(x) ≤ 2a′X. Hence λaa′qT²/9 ≤ m(t) ≤ 4λaa′qT², m is increasing, m(T/2) ≥ m(T)/8, and m′(t)/m(t) = aq/P(x) + a′q/P′(x) ∈ [1/(2T), 6/T].

**Coins as a box.** By 12.1 the coin at level s ≥ 2 is tails iff the digit d_{s−2}(m) is ≤ (q−1)/2 iff {m/q^{s−1}} < ρ := (q+1)/(2q). Define L by q^{L−1} ≤ 2m(T) < q^L and J = L − 1. For every t in the range 2m(t) < q^{J+1}, so coins at levels above J+1 are vacuously tails, and "n(x) has no carry in base q" is exactly

  y(t) := ({m(t)/q}, {m(t)/q²}, …, {m(t)/q^J}) ∈ 𝔅 := [0, ρ)^J.

Put F = 2m(T)/q^{L−1} ∈ [1, q), the leading digit of 2m at the top of the range. Note ρ^J = 2^{1−L}(1 + 1/q)^{L−1} = 2^{1−L}(1 + O(L/q)). By (W3), q^L > 2m(T) ≥ 2λaa′qT²/9 and T ≥ q^{1+4ε} when q ≤ X^{1/2−ε}, so L ≥ 4 for large X: the medium regime is exactly L ≥ 4.

**Lemma W.** Fix ε ∈ (0, 1/10) and put η = ε/32. There are C₄ = C₄(forms) and X₀ = X₀(ε, forms) such that for X ≥ X₀ and every prime q as above with z₀ < q ≤ X^{1/2−ε}, writing B_q = #{t ∈ (T/2, T] : y(t) ∈ 𝔅}:

(a) if q ≥ exp((log X)^{3/4}), then |B_q − ρ^J·T/2| ≤ ρ^J·(T/2)·(C₄/F + q^{−η});

(b) if q < exp((log X)^{3/4}), then B_q ≤ ρ^{J′}·T/2 + T^{1−ε}, where J′ = ⌊(1−ε) log T/ log q⌋ ≤ J.

**Two standard inequalities.**

(ET) *Erdős–Turán–Koksma* (Drmota–Tichy, Sequences, Discrepancies and Applications, Thm 1.21). For y_1, …, y_N ∈ [0,1)^d and any integer H ≥ 1, the discrepancy D_N of the point set with respect to boxes satisfies

  D_N ≤ (3/2)^d ( 2/(H+1) + Σ_{0<‖h‖_∞≤H} r(h)^{−1} |N^{−1} Σ_{t≤N} e(h·y_t)| ),  r(h) = ∏_{j≤d} max(1, |h_j|),

and #{t : y_t ∈ box} = N·vol(box) + θ·N·D_N with |θ| ≤ 1. Also Σ_{0<‖h‖_∞≤H} r(h)^{−1} ≤ (3 + 2 log H)^d.

(Wq) *Weyl, quadratic case.* If α = u/Q with gcd(u, Q) = 1 and Q odd, then for every interval I of length N ≥ 1 and all real β₁, γ₁,

  |Σ_{t∈I} e(αt² + β₁t + γ₁)| ≤ C₅·N·(log 2Q)^{1/2}·( Q^{−1/2} + N^{−1/2} + Q^{1/2}N^{−1} ),

with an absolute constant C₅. Proof: |S|² = Σ_{|h|<N} Σ_{t∈I∩(I−h)} e(2αht + αh² + β₁h) ≤ N + 2Σ_{h=1}^{N} min(N, 1/(2‖2αh‖)); as 2α = 2u/Q with gcd(2u, Q) = 1, Vaughan's Lemma 2.2 gives Σ_{h≤N} min(N, ‖2αh‖^{−1}) ≤ 4(N/Q + 1)(N + Q log Q), whence |S|² ≪ N²/Q + N log 2Q + Q log 2Q. ∎

**Exponential sums.** For 1 ≤ j ≤ J, an integer h′ with q ∤ h′, and an interval I ⊂ (T/2, T] of length N, put E_j(h′; I) = Σ_{t∈I} e(h′m(t)/q^j). By (W1), |E_j| ≤ q^j. For j ≥ 2, (W2) and (Wq) with Q = q^{j−1} (odd, reduced since q ∤ h′λaa′) and log 2Q ≤ log 2m(T) ≤ 2 log X give

  |E_j(h′; I)| ≤ min( q^j, C₅N(2 log X)^{1/2}( q^{−(j−1)/2} + N^{−1/2} + q^{(j−1)/2}/N ) ).

**Claim 1.** Let X ≥ X₀, q ≥ exp((log X)^{3/4}), and let I ⊂ (T/2, T] have length N ≥ Tq^{−ε}/8. Then for all 1 ≤ j ≤ J−1, and also for j = J when I = (T/2, T] and F ≥ q^ε,

  |E_j(h′; I)| ≤ C₆·N·(log X)^{1/2}·q^{−ε/4},  C₆ = C₆(forms).

*Proof.* Recall T ≥ q^{1+4ε}. If q^j ≤ Nq^{−ε/4}, use |E_j| ≤ q^j; this covers j = 1, since q ≤ Nq^{−ε/4} follows from N ≥ Tq^{−ε}/8 ≥ q^{1+3ε}/8. Otherwise j ≥ 2 and Q = q^{j−1} > Nq^{−1−ε/4} ≥ Tq^{−1−5ε/4}/8 ≥ q^{11ε/4}/8, so Q^{−1/2} ≤ 3q^{−11ε/8}; also N^{−1/2} ≤ (8q^ε/T)^{1/2} ≤ 3q^{−1/2}. For the last term: if j ≤ J−1 then Q ≤ q^{L−3} = 2m(T)/(Fq²) ≤ 8λaa′T²/q by (W3) and F ≥ 1, so Q^{1/2}/N ≤ (8λaa′)^{1/2}·T·q^{−1/2}·8q^{ε}/T ≤ 8(8λaa′)^{1/2}q^{−1/4}. If j = J, N = T/2 and F ≥ q^ε, then Q = q^{L−2} = 2m(T)/(Fq) ≤ 8λaa′T²/F, so Q^{1/2}/N ≤ 2(8λaa′/F)^{1/2} ≤ 6(λaa′)^{1/2}q^{−ε/2}. In all cases the bracket in (Wq) is ≤ C q^{−ε/4}. ∎

**Claim 2 (box count on an interval).** Let X ≥ X₀, q ≥ exp((log X)^{3/4}), d ∈ {J−1, J}, and I ⊂ (T/2, T] of length N ≥ Tq^{−ε}/8; if d = J assume I = (T/2, T] and F ≥ q^ε. Then

  #{t ∈ I : ({m(t)/q^j})_{j≤d} ∈ [0,ρ)^d} = ρ^d N + θ·3N·q^{−ε/16},  |θ| ≤ 1.

*Proof.* Apply (ET) with H = ⌊q^{ε/8}⌋ < q/2. For 0 < ‖h‖_∞ ≤ H write j₀ = max{j : h_j ≠ 0}. Then h·y(t) = m(t)·Σ_j h_j q^{d−j}/q^d = h′m(t)/q^{j₀} with h′ = Σ_{j≤j₀} h_j q^{j₀−j} ≡ h_{j₀} ≢ 0 (mod q), because 0 < |h_{j₀}| < q. So Σ_{t∈I} e(h·y(t)) = E_{j₀}(h′; I), and Claim 1 applies (j₀ ≤ d). Hence

  N·D_N ≤ (3/2)^d·2N/(H+1) + (3/2)^d(3 + 2 log H)^d·C₆N(log X)^{1/2}q^{−ε/4}.

Now d ≤ J ≤ log(2m(T))/log q ≤ 2 log X/ log q ≤ 2(log X)^{1/4}, so (3/2)^d(3 + 2 log H)^d ≤ exp(2(log X)^{1/4} log(5 log X)) ≤ q^{ε/32} and (log X)^{1/2} ≤ q^{ε/32} for X ≥ X₀(ε), as log q ≥ (log X)^{3/4}. With 2/(H+1) ≤ 4q^{−ε/8} this gives N·D_N ≤ 4Nq^{−ε/8+ε/32} + C₆Nq^{−ε/4+ε/16} ≤ 3Nq^{−ε/16} for X ≥ X₀. ∎

**Proof of Lemma W(a).** Since 2^{−J} ≥ exp(−2(log X)^{1/4} log 2) ≥ q^{−ε/64}, the error 3Nq^{−ε/16} of Claim 2 is at most ρ^d N q^{−ε/32}·(3q^{−ε/64}) ≤ ρ^d N q^{−η} for X ≥ X₀.

*Case F ≥ q^ε.* Claim 2 with d = J and I = (T/2, T] gives B_q = ρ^J T/2 + θρ^J(T/2)q^{−η}.

*Case F < q^ε.* Let φ(t) = m(t)/q^J, so φ(T) = F/2 and, by (W3), φ′(t) = m′(t)/q^J ∈ [m(T/2)/(2Tq^J), 6m(T)/(Tq^J)] ⊂ [F/(32T), 3F/T]. The set 𝒯 = {t ∈ (T/2, T] : {φ(t)} < ρ} is a union of at most F/2 + 2 intervals I_r, because φ increases by at most F/2 over the range. Every I_r other than possibly the first and the last is a full piece, of length between ρ·T/(3F) ≥ T/(6F) > Tq^{−ε}/8 and ρ·32T/F ≤ 32T/F; the complementary pieces have lengths between (1−ρ)T/(3F) and 32T/F. On any interval of length ≤ 32T/F the derivative φ′ varies by a factor 1 + O(1/F): indeed |φ″| = 2λaa′q/q^J and φ′ ≥ F/(32T), so the relative change is at most 2λaa′q·(32T/F)·32T/(F q^J) = 2^{11}λaa′qT²/(F²q^J) ≤ 2^{11}·9/(2F) by q^J = 2m(T)/F ≥ 2λaa′qT²/(9F). Pairing each full piece I_r with the following complementary piece gives |I_r| = ρ(|I_r| + |I′_r|)(1 + O(1/F)), and the two boundary pieces have total length ≤ 64T/F, so

  |𝒯| = ρ·(T/2)·(1 + θ₁C₇/F),  C₇ = C₇(forms).

Now B_q = Σ_r #{t ∈ I_r : ({m(t)/q^j})_{j≤J−1} ∈ [0,ρ)^{J−1}}. For the pieces of length ≥ Tq^{−ε}/8 (all full pieces, and boundary pieces when long) Claim 2 with d = J−1 gives ρ^{J−1}|I_r| + θ·3|I_r|q^{−ε/16}; a boundary piece shorter than Tq^{−ε}/8 contributes at most Tq^{−ε}/8 + 1 trivially, and 2(Tq^{−ε}/8 + 1) ≤ ρ^J(T/2)q^{−ε/2} since ρ^J ≥ 2^{−J} ≥ q^{−ε/64}. Summing,

  B_q = ρ^{J−1}|𝒯| + O(Tq^{−ε/16}) = ρ^J(T/2)(1 + θ₁C₇/F) + O(Tq^{−ε/16}) = ρ^J(T/2)(1 + θ₁C₇/F + θ₂q^{−η}),

for X ≥ X₀, using once more Tq^{−ε/16} ≤ ρ^J(T/2)q^{−η}. This is (a) with C₄ = C₇ (after adjusting constants). ∎

**Proof of Lemma W(b).** Let J′ = ⌊(1−ε) log T/ log q⌋. Since q^{J′} ≤ T^{1−ε} and 2m(T) ≥ 2λaa′qT²/9 ≥ q·T^{1−ε} for large X, one has q^{J′+1} ≤ 2m(T) < q^L, so J′ ≤ L−2 ≤ J. The event y(t) ∈ 𝔅 implies ({m(t)/q^j})_{j≤J′} ∈ [0,ρ)^{J′}, i.e. m(t) mod q^{J′} ∈ S_{J′} := {Σ_{i<J′} d_i q^i : 0 ≤ d_i ≤ (q−1)/2}, a set of size ((q+1)/2)^{J′}. By (W1) the values m(t) mod q^{J′} run through ℤ/q^{J′} exactly once on each block of q^{J′} consecutive t, so

  B_q ≤ (⌊(T/2)/q^{J′}⌋ + 1)·((q+1)/2)^{J′} ≤ ρ^{J′}·T/2 + q^{J′} ≤ ρ^{J′}·T/2 + T^{1−ε}. ∎

**Lemma W′ (the second coin in the top regime, L = 3).** Let q | P(x) with 2|κ|·P(x)/q < q and q³ ≤ 2n, i.e. L = 3; assume q ≤ X^{2/3−ε}. The level-2 coin is decided by Lemma S and is the same for all x ≡ x_q (mod q). For the level-3 coin, #{t ∈ (T/2, T] : {m(t)/q²} < ρ} = ρ·T/2 + O(T(log X)^{3/2}(q^{−1/4} + q^{3/2}X^{−1})), hence it is tails for a proportion ½ + o(1) of the progression, uniformly in q: apply the one-dimensional (ET) with H = ⌊q^{1/4}⌋ to the phases e(h′m(t)/q²), q ∤ h′, bounded by (Wq) with Q = q and N = T/2, which gives |E_2| ≤ C₅T(2 log X)^{1/2}(q^{−1/2} + (2/T)^{1/2} + 2q^{1/2}/T); here q^{1/2}/T = q^{3/2}/X ≤ X^{−3ε/2}. The range q > X^{2/3−ε} within L = 3 has Σ 1/q = O(ε).

**What Lemma W does not cover.** Primes in (X^{1/2−ε}, √(2|κ|·2aX)) (neither medium nor top; Σ 1/q = O(ε) + o(1)), primes q ≤ z₀ (removed by the residue class), primes with q² | P(x) or dividing two forms (Σ 1/q² and finitely many), and the o(1) sub-bucket F < C₀, which only enters through the C₄/F term.

### 12.4 The first-moment theorem

**Small primes.** The forms are admissible: for every prime q ≤ z₀ there is a class x₀ mod q avoiding all P_j, and for the primes dividing the λ's the class is chosen mod a higher power so that ν_q(∏(n−i)) is minimal and the digit at position ν_q + 1 of n is ≥ q/2 (for Theorem C: x even makes n odd and ν₂(n−1) = 1 ≤ popcount(n); for Theorem D: x ≡ 2 (mod 4)). Restrict to this class mod M.

**Counting.** For x ≤ X in the class, n(x) ∉ E_k implies that some prime q > z₀ divides some P_j(x) and all coins at q are tails (primes with q² | P_j(x), or dividing two forms, contribute O(1/z₀) + o(1)). Hence

  #{bad x} ≤ Σ_j Σ_{q > z₀} #{x : q | P_j(x), all coins tails} + O((1/z₀ + ε + o(1))X).

Split by L. For L ≥ 4 and q ≥ exp((log X)^{3/4}), Lemma W(a) (summed over the dyadic ranges x ∈ (X/2^{r+1}, X/2^r]) gives per prime at most 2^{1−L}(1 + C₄/F(q) + q^{−η})·X/q. The primes with F(q) < C₀ form, inside the bucket L(q) = L, a range of ratio C₀^{1/(L−1)}, so their Σ 1/q is O(log C₀/ log X) = o(1); for the others the factor is 1 + O(1/C₀) + o(1), and C₀ → ∞ at the end. The primes z₀ < q < exp((log X)^{3/4}) contribute, by Lemma W(b), at most Σ_q (X/q)(ρ^{J′(q)} + T^{−ε}) ≤ X(log log X)·(0.51)^{(log X)^{1/4}/2} + o(X) = o(X), since (q+1)/(2q) ≤ 0.51 for q > 50 and J′(q) ≥ (log X)^{1/4}/2 there. Since Σ_{q : L(q) = L} 1/q = log((L+1)/L) + o(1), the medium regime contributes to the first moment

  m := Σ_{L ≥ 4} 2^{1−L} log((L+1)/L) = 0.02789 + 0.01139 + 0.00482 + 0.00209 + 0.00092 + … = 0.0479 per form.

For L ∈ {2, 3} write q = P_j(x)/c; the count of x ≤ X with P_j(x)/c prime in a fixed class mod a is, by the prime number theorem in progressions (fixed modulus a; c ≤ X^{1/2}, so the progression has length ≥ X^{1/2}), (1 + o(1))·aX/(φ(a)·c·log(aX/c)). The bad classes of c mod a have relative density f_j, and the weight Σ_c 1/(c log(X/c)) over c = X^v is ∫dv/(1−v): over v ∈ (0, 1/3) (L = 2) this is log(3/2) = 0.405, over v ∈ (1/3, 1/2) (L = 3, extra fair coin) it is ½log(4/3) = 0.144. So the top regime contributes f_j·0.549 per form. Altogether

  M_∞ = 0.549·Σ_j f_j + 0.0479·#forms,   and   #{good x in the class} ≥ (1 − M_∞ − O(ε + 1/z₀) − o(1))·#{x in the class}.

**Theorem C.** For n = (12x−1)(22x+9), n−1 = 2(11x−1)(12x+5): κ-values 130, −130 (pair 1) and 67, −67 (pair 2, λ = 2); f = (0, 1/5, 1/5, 0) (a = 12 and 12 have f = 0; for a = 22 and 11 one of the five square classes fails). M_∞ = 0.549·0.4 + 4·0.0479 = 0.411. Admissibility: a class mod each prime ≤ 23 avoiding all forms exists (`search2.admissible`), and four forms never cover all classes mod a prime ≥ 5. The leading coefficients 12, 22, 11, 12 are below √(2·264) = 23, so no form has the empty-coin regime of Remark (3). Since n ≍ x², #(E₁ ∩ [1,N]) ≫ N^{1/2}. For n = 2(12x+5)(35x+32), n−1 = (70x+29)(12x+11): f = (0, 1/6, 1/6, 0), M_∞ = 0.375; here 70 > √(2·840) = 41 and the form 70x+29 has the empty-coin regime, which costs only o(1). Brute force: 0.378 of x ≤ 2·10⁴ and 0.409 of x ≤ 10⁵ give n ∈ E₁ for this family.

**Theorem D.** For n = (14x−1)(15x−1), n−1 = x(210x−29), n−2 = (6x−1)(35x+1): f = (1/3, 0, 0, 1/3, 0, 1/6), M_∞ = 0.549·(5/6) + 6·0.0479 = 0.457 + 0.287 = 0.745. The forms x and 210x−29 need q > 2k = 4 in 12.1, fine for q > z₀. The forms 210x−29 and 35x+1 exceed √(2·210) = 20.5 and have empty-coin regimes, again o(1). Admissible: `search2.admissible` finds a class mod each prime ≤ 23; six forms cannot cover ℤ/q for q ≥ 7.

### 12.5 Classification of quadratic families

Let n = λ₀P₁P₂ with κ = a₁b₂ − a₂b₁ and A = λ₀a₁a₂. The discriminant of n − i as a quadratic in x is (λ₀κ)² + 4Ai. So n − i splits over ℚ iff (λ₀κ)² + 4Ai is a square. For E₁ this is (s − λ₀κ)(s + λ₀κ) = 4A, finitely many (s, κ) per A. For E₂ one needs (λ₀κ)², s², v² in arithmetic progression with common difference 4A, i.e. (Euler) A = m²pq(p²−q²) and λ₀κ = ±m(p² − 2pq − q²). For E₃ one would need four squares in arithmetic progression, impossible (Fermat), as noted in §11. Given (λ₀, a₁, a₂, κ), the constants b₁, b₂ are determined up to the shift x ↦ x + t by a₁b₂ − a₂b₁ = κ, and f_j depends only on b_j mod a_j, hence is shift-invariant. `apsq.py` enumerates all families: for E₁ with A ≤ 3000 there are 93 121 families (10 964 admissible), minimum Σf_j = 1/3, attained by the second family of Theorem C; for E₂ with A ≤ 20 000 there are 4 964 families (146 admissible), minimum Σf_j = 5/6, attained by the family of Theorem D (and its sub-progressions). No admissible E₂ family in this range has Σf_j ≤ 0.8.

### 12.6 Numerics

Proportion of x with n(x) ∈ E₁ along n = (12x−1)(22x+9) (all x, no class restriction; `verify.py`, `sample.py`):

| range of x | 1..2·10⁴ | [5·10⁵, 10⁶] | [5·10⁸, 10⁹] | [5·10¹¹, 10¹²] | [5·10¹⁴, 10¹⁵] |
|---|---|---|---|---|---|
| proportion in E₁ | 0.473 | 0.521 | 0.553 | 0.584 | 0.597 |
| mean number of bad primes | — | 0.603 | 0.558 | 0.513 | 0.492 |

The limiting first moment is 0.411; the finite-size excess comes from the windows q ∈ (√P, √(2|κ|P)) with κ = 130, 67, which shrink like 1/log x. For Theorem A's family (14x+3)(24x+17), Σf_j = 2/3 and the proportion is 0.448 at x ≤ 2·10⁴, 0.471 on [10⁵, 2·10⁵]; for (4x−1)(6x+1) with Σf_j = 1 it is 0.272.

E₂ along n = (14x−1)(15x−1): proportion 0.165 (x ≤ 10⁴), 0.196 (x ≤ 10⁵), 0.238, 0.282, 0.320, 0.327 on the dyadic ranges at 10⁶, 10⁹, 10¹², 10¹⁵; mean number of bad primes 1.227, 1.085, 1.010, 0.964 against the limit 0.745. For comparison, random n of size 10¹² lie in E₁ with probability 0.016 and in E₂ with probability 0.003.

Digit laws (`lawcheck.py`, x ∈ [5·10¹⁴, 10¹⁵], primes q ≥ 1000 with q ∥ P_j and log q/ log x < 0.45): the fraction of such q with no carry, by L, is 0.1216, 0.0588, 0.0283, 0.0144, 0.0079, 0.0031, 0.0022 for L = 4, …, 10, against 2^{1−L} = 0.125, 0.0625, 0.0313, 0.0156, 0.0078, 0.0039, 0.0020. For log q/ log P_j > 0.7 the no-carry fractions per form are (0, 0.174, 0.233, 0) against f = (0, 0.2, 0.2, 0); for the Theorem A family (0.297, 0, 0.311, 0) against (1/3, 0, 1/3, 0); for the E₂ family (0.392, 0, 0, 0.427, 0, 0.214) against (1/3, 0, 0, 1/3, 0, 1/6). In the window log q/ log P_j ∈ (0.6, 0.65) the fractions are (0, 0.119, 0.097, 0) against f/2 (`rulecheck.py`).

Direct test of Lemma W (`code/h2/lemmaW_test.py`, X = 2·10⁷, piece 12x−1): for every prime q in [1000, 1400] (L = 5, F between 60 and 200), [4000, 4100] (L = 4, F ≈ 800) and [300, 330] (L = 6), the exact count B_q of t ∈ (T/2, T] with all coins tails agrees with ρ^J·T/2 to within the Poisson noise of counts of size 300–1000 (deviations ≤ 8%). For q ∈ [2000, 2150], where F ≈ 5–6.5, the deviations are systematically negative, −2% to −22%, as allowed by the C₄/F term of Lemma W(a).

### 12.7 Status and next steps

- Proved here: Lemma S; Lemma W (12.3, with Lemma W′ for the second coin of the top regime); the first-moment theorem of 12.4; the classification 12.5. Theorems C and D therefore stand as stated, modulo the line-by-line check below.
- Lemma W is proved in 12.3 from three named inputs: the Hensel bijection (W1), Weyl's inequality for quadratic exponential sums with an exact rational leading coefficient (Wq, with Vaughan's Lemma 2.2), and the Erdős–Turán–Koksma inequality (ET). The constants are chosen in the order ε, then z₀ and C₀, then X ≥ X₀(ε, forms). The bound M_∞ < 1 has margin 0.59 for E₁ and 0.25 for E₂.
- Still to be checked line by line by a second reader: the constant bookkeeping in Claims 1–2 (all exponents are explicit: η = ε/32, H = ⌊q^{ε/8}⌋), the pairing argument for |𝒯| in Case F < q^ε, the uniformity of the prime number theorem in progressions used for the top regime (fixed modulus a, progressions of length ≥ X^{1/2}), and the o(1) accounting of the excluded windows in 12.4 (each is a range of primes with Σ 1/q = O(ε) or o(1)).
- The same accounting improves with the degree: for a degree-d family (n − i = λ_i·∏ of d linear forms for i = 0..k) the top regime is L ≤ 2d−1 and its weight per form is Σ_{L=d+1}^{2d−1} 2^{2−L} log((L+1)/L) (0.223 for d = 3, 0.093 for d = 4), the medium weight is Σ_{L ≥ 2d} 2^{1−L} log((L+1)/L) (0.0085 for d = 3, 0.0019 for d = 4), and Lemma S extends verbatim (the digit is c·∏_{j≠1} κ_j/a^{d−1} mod q). Weyl's inequality for degree d replaces the quadratic case. So E₃ and E₄ would follow from any admissible family with n − i, 0 ≤ i ≤ k, splitting into linear forms over ℤ, provided Σf_j·(top weight) + (#forms)·(medium weight) < 1; for d = 3, k = 3 this is 0.223·Σf_j + 0.10 < 1, i.e. Σf_j < 4 out of a maximum of 12. Whether such linear-form families exist for k ≥ 3 is the question left by §11 (agent g6's E₃ and E₄ identities use irreducible quadratic pieces, to which Lemma S does not apply directly).
- Not checked: the literature for Lemma S or for digit equidistribution of polynomial values at their own prime factors (Ford–Konyagin's treatment of n | C(2n,n) is the closest model).
- §13 explains why this method stops at k = 2 and what k ≥ 3 needs.

## 13. Why the first-moment method stops at k = 2, and what k ≥ 3 needs (agent h1/h2)

### 13.0 Summary

The argument of §12 has two inputs that are specific to *linear* pieces: every prime factor of a piece ax + b is at most aX, so each prime q can be studied along the progression x ≡ x_q (mod q) with at least X/(aX)·… ≥ 1/a terms (the "t-picture"), and the top regime q ∈ (√X, aX) is counted by the prime number theorem in progressions. For a piece of degree e ≥ 2 the prime factors reach X^e, and for q > X^{1+δ} the progression x ≡ r (mod q) has at most one term in [X/2, X]: neither the t-picture nor any unconditional count of x with P(x)/c prime is available. So the method needs families n − i = λ_i ∏ (linear pieces), i = 0, …, k. These exist for k ≤ 2 and, as far as we can tell, for no k ≥ 3:

- one variable, degree 2: four squares in arithmetic progression (Fermat), §12.5;
- several variables: a pencil of plane curves has at most four completely reducible members, the fiber at infinity included (Pereira–Yuzvinsky 2008, k ≤ 5; Yuzvinsky 2009, k ≤ 4, attained by the Hesse pencil), and composite pencils reduce to the one-variable case or to conics; this gives k ≤ 2;
- one variable, degree 3: the split fibers of x³ − 3Nx + q are the values Tr(β³) with β ∈ ℚ(ω), N(β) = N (Cardano); a search over all such β of height ≤ 300 for 23 norms N finds three-term progressions but no four-term one and no pair with ratio 3 (`code/h2/torus_ap.py`). The four-term variety is a complete intersection of two cubics in ℙ⁴, a surface of general type, so Bombieri–Lang predicts at most finitely many curves of solutions;
- one variable, degree 4: the completely split fibers of a fixed quartic correspond to rational points on a curve of genus 5 (the fiber product over the s-line of the two elliptic quartics y² = −s⁴ − 2ps² ∓ 2qs of agent g6's parametrization), hence are finite in number; four of them in progression impose nine square conditions on four parameters.

Consequently E₃ cannot be reached by a first-moment bound along a polynomial family, and the obstacle for k ≥ 3 is not the carries but the anatomy of values of a polynomial of degree ≥ 2 above the level X. Section 13.3 states precisely what is unconditional for an irreducible quadratic member and which single hypothesis would give E_k for every k.

### 13.1 Pieces of degree ≥ 2: the barrier

Let P be a piece of degree e ≥ 2 in a family of degree L with every piece of degree ≤ L/2 (otherwise a positive proportion of x fail for the trivial reason q² > 2n). Prime factors q of P(x) lie in (X^{1−ε}, X^{e}) with total weight Σ ρ(q)/q = log(e/(1−ε)) + o(1), a positive constant, and the coins there number L(q) − 1 ≤ 2e − 1. Three facts:

(a) *Counting.* #{x ≤ X : q | P(x)} = ρ(q)X/q + O(ρ(q)) is useless for q > X: the error summed over q ≤ X^e exceeds X. The count must go through the cofactor c = P(x)/q, and then it is the count of x ≡ r_c (mod c) with P(x)/c prime: Bunyakovsky–Bateman–Horn territory. Selberg's upper-bound sieve gives at most 2·deg(P)·(1 + o(1)) times the expected number; with that loss the top-regime weight of one quadratic piece with fair coins is ≥ 4·½·log 2 ≈ 1.39, and the union bound is dead for any family.

(b) *Determinism survives only at the very top.* Write R for the product of the other pieces of the same member and R = QP + S in ℚ[x] with deg S < e. For q | P(x) with cofactor c the level-2 digit is c·R(x) mod q = q·{c²Q(x) + c²S(x)/P(x)}, so as in Lemma S the coin depends only on c and x modulo the denominators of Q as long as c²|S(x)|/P(x) is small, i.e. c ≪ √X, i.e. q ≫ P(x)/√X ≈ X^{e−1/2}. For e = 1 this is the whole top regime; for e = 2 it is q ∈ (X^{3/2}, X²), of weight log(4/3), while q ∈ (X, X^{3/2}) (weight log(3/2)) carries a coin that is equidistributed, not deterministic, and can be counted only with (a).

(c) *Smooth values do not rescue the union bound.* For an irreducible quadratic member Q(x) = n(x) − i the events are: B₀ = {P⁺(Q(x)) > √(2n)} (no coin at all) and the coin events for q ≤ √(2n). Heuristically P(B₀) = log 2 = 0.6931 and Σ_q P(coins tails) = Σ_{L≥2} 2^{1−L} log((L+1)/L) = 0.3223, total 1.0154 > 1: the union bound fails for a *single* irreducible member even with perfect information (Ford–Konyagin's true density 0.114 is recovered only from the product structure). Restricting to x with Q(x) smooth does not help either: at smoothness exponent α (prime factors ≤ x^α) the surviving proportion is ρ(2/α) while the coin weight is still ≥ Σ_{L ≥ 3} 2^{1−L}log((L+1)/L) = 0.12, and ρ(2/α) < coin weight for every α ≤ 1. And what is known unconditionally is far weaker anyway: a positive proportion of n with P⁺(n² + 1) < n^{α} is known for α > 149/179 (Dartyge 1996), later for α > 4/5 and, with the de la Bretèche–Drappeau method, α > 0.567, all with very small implied constants; the proportion with P⁺(n²+1) > n^{1.279} is positive (Merikoski 2023), and no asymptotic for P(P⁺(Q(x)) > x) is known for any irreducible quadratic Q.

(d) *Balog–Wooley families* (NOTES §"Algebraic families") have pieces Φ_{2d}(c B^{L/m}) of degree φ(d)L/m ≥ 2 in the free variable B for every member once k ≥ 1, so (a)–(c) apply to them as well. The cyclotomic factorization is the only universal factorization of A^m ± 1 and never yields linear pieces beyond A ± 1.

### 13.2 Linear pieces: k ≤ 2

**One variable, degree 2.** §12.5.

**Several variables.** Suppose n = F(x₁, …, x_r) and n − i = λ_i ∏_j ℓ_{ij} with affine-linear ℓ_{ij}, i = 0, …, k. Restrict to a generic plane to get a pencil {F − i z^d} of plane curves of degree d with the k+1 members F − i z^d and the member z^d (i = ∞) completely reducible. If the pencil is not composite (F/z^d is not φ∘ψ with deg φ ≥ 2), Yuzvinsky's theorem (Proc. AMS 137 (2009) 1641–1648, sharpening Pereira–Yuzvinsky, Adv. Math. 219 (2008)) gives k + 2 ≤ 4, i.e. k ≤ 2. If F = g(h) is composite with h of degree ≥ 2 (h a polynomial in x₁, …, x_r), then F − i = ∏_ρ (h − ρ) over the roots ρ of g − i, and h − ρ is a product of linear forms only if the hypersurface h = ρ is reducible, which happens for at most finitely many ρ (for h quadratic, at most 3 by the discriminant); since the root sets of g − i for different i are disjoint, (k+1)·deg g ≤ 3, so k ≤ 2 again. If h is linear, F is a polynomial in one variable. So in every case k ≤ 2, except possibly for one-variable families of degree ≥ 3.

**One variable, degree 3 (Cardano).** After a translation and a scaling any cubic family is x³ − 3Nx + q, N ∈ ℚ. For β ∈ ℚ(ω), ω² + ω + 1 = 0, with N(β) = ββ̄ = N, the numbers β + β̄, ωβ + ω²β̄, ω²β + ωβ̄ are rational, sum to 0, have e₂ = −3N and product Tr(β³) = β³ + β̄³. Conversely a split cubic x³ − 3Nx − e has roots u, v, w with u + v + w = 0, u² + uv + v² = 3N = N(u − vω), and e = uvw = Tr(β³) for β = u − vω. So the split values of the family are exactly {Tr(β³) : N(β) = N}, and since every β of norm N is β₀ζ²/N(ζ) with ζ ∈ ℤ[ω] primitive (Hilbert 90), they are the numbers Tr(β₀³ζ⁶)/N(ζ)³. In coordinates β = a + bω: N(β) = a² − ab + b², Tr(β³) = (a + b)(2a − b)(a − 2b). A family for E₃ needs four values Tr(β_j³) in arithmetic progression with N(β_j) all equal; because −β also has norm N, the progression (−3e, −e, e, 3e) needs only one pair with Tr(β′³) = 3·Tr(β³), and a five-term progression through 0 (possible when 3N is a square) needs a pair with ratio 2. `torus_ap.py` enumerates, for the 23 norms N(a + bω) with 0 ≤ b ≤ a ≤ 8, all ζ = c + dω with |c|, |d| ≤ 300: 41 000–80 000 values per N. There is no pair with ratio 3 or 2, and among the values with |c|, |d| ≤ 40 (740–1444 per N) there is no four-term progression; three-term progressions do occur (also found by g6 over ℤ, `code/g6/cubic3.py`). The four-term condition on four points of the conic is a complete intersection of two cubic hypersurfaces in ℙ⁴ (canonical class O(1)), a surface of general type; the ratio-3 condition on two points is a complete intersection of type (2,3) in ℙ³, a curve of genus 4. So finitely many families at most are to be expected, and none were found.

**One variable, degree 4.** For f = X⁴ + pX² + qX + r the factorization f − c = (X² + sX + t)(X² − sX + u) forces t, u = (p + s² ∓ q/s)/2, and both quadratics split iff −(s³ + 2ps ± 2q)/s are squares, i.e. iff s is the common abscissa of rational points on the two elliptic quartics y² = −s⁴ − 2ps² − 2qs and y² = −s⁴ − 2ps² + 2qs. For fixed (p, q) this is a curve of genus 5, so a quartic has finitely many completely split fibers. Agent g6's parametrization makes the two progression conditions linear in (p, q²); a four-term progression of completely split fibers then needs nine rational squares on a four-parameter family, and `code/g6/irr_count.py` found none with small parameters.

**Norm-form pieces are excluded too, and they are exactly the countable ones.** Yuzvinsky's theorem is a statement over ℂ, and so is the composite-case argument above, so both apply verbatim when the pieces are only required to split into linear factors over ℚ̄. In particular, for k ≥ 3 there is no non-univariate family whose pieces are products of norm forms N_K(ℓ(x)) of affine-linear maps ℓ : ℚ^r → K. These are precisely the pieces with full level of distribution. If ℓ(ℤ^r) has full rank in O_K (d = [K:ℚ] ≤ r), an ideal 𝔮 gives the lattice ℓ^{−1}(𝔮), and every nonzero α ∈ 𝔮 has max_σ |σ(α)| ≥ N𝔮^{1/d} because |N(α)| ≥ N𝔮. So all successive minima are ≍ N𝔮^{1/d}, and #{x in a box of side Y : 𝔮 | ℓ(x)} = vol/N𝔮 + O((Y/N𝔮^{1/d})^{d−1} + 1) holds uniformly up to N𝔮 ≈ Y^d, the size of the piece. For an absolutely irreducible piece F of degree e ≥ 2 in m variables, counting F ≡ 0 (mod q) through complete exponential sums (Deligne) controls a single q only up to q ≈ Y^{2m/(m+2)} < Y² ≤ Y^e, and above that level the anatomy problem of 13.1 returns. So the analytic barrier of 13.1 and the algebraic barrier here are the same barrier. Pieces linear enough to be counted up to their own size are linear enough over ℚ̄ for Yuzvinsky's bound to apply.

### 13.3 The program for k ≥ 3

Fix the E₂ family n(x) = (14x−1)(15x−1) (any E₂ family will do) and k ≥ 3. For 3 ≤ i ≤ k the member Q_i(x) = n(x) − i is an irreducible quadratic (a fourth square in the progression of discriminants is impossible). The members n, n−1, n−2 are handled by §12. For Q_i the following is unconditional:

- **All primes q ≤ X^{1/2−ε}**: Lemma W applies verbatim. In (W1) only the simplicity of the root r of Q_i mod q is used (m′(t) ≡ Q_i′(r) ≢ 0 mod q); the value of the linear coefficient never enters, since the j = 1 phase is bounded by its period q. The leading coefficient of m(t) is again A·q with A = lc(Q_i), so the gained level is still there.
- **Primes q ∈ (X^{1/2}, X^{1−ε})** (L(q) ∈ {2, 3}): the level-3 coin is handled by Lemma W′. The level-2 coin is the linear sequence {Q_i(r)/q² + (Q_i′(r)/q)t} over t ≤ T = X/q < q, whose discrepancy is ≪ 1/H + Σ_{h≤H} 1/(hT‖hQ_i′(r)/q‖). Averaged over q this is small: the primes q with hQ_i′(r) ≡ ±K (mod q) are the prime divisors of the fixed integer h²Q_i(±K/h)·(denominators), at most O(log(hK)) of them, so Σ_q (ρ(q)/q)(q/(hX))/|hQ_i′(r) mod q| ≪ X^{−ε}(log X)². Hence the level-2 coin is fair on average over q in this range.
- **Primes q ∈ (X^{1−ε}, √(2n))**: weight O(ε), counted as bad.

What is missing is everything about primes q > √(2n) ≈ X√(2A), i.e. the event B₀ = {P⁺(Q_i(x)) > √(2n)}, which forces failure, together with the joint law of B₀^c and the coins. Unconditionally only |B₀| ≤ X is known. The heuristic is P(B₀) = log 2, and given 13.1(c) the first-moment bound cannot close even with P(B₀) known: the Ford–Konyagin product structure is required.

**Hypothesis BH_u(Q).** For every fixed δ > 0, uniformly for c ≤ X^{1−δ} and every class r mod c with c | Q(r):

  #{x ≤ X : x ≡ r (mod c), Q(x)/c prime} = (1 + o(1))·𝔖(Q, c, r)·X/(c·log(X²/c)),

with the Bateman–Horn singular series 𝔖. (For c = 1 this is the Hardy–Littlewood conjecture for Q; Landau's problem for x² + 1.)

**Expected theorem.** Under BH_u(Q_i) for 3 ≤ i ≤ k, a positive proportion of x in the admissible class have n(x) ∈ E_k; the density is (1 − M_∞(E₂ family) + …)·∏_{i=3}^{k} c(Q_i) with c(Q_i) the Ford–Konyagin constant of the member (c(Q) = c₁ ≈ 0.114 if the anatomy of Q(x) is Poisson–Dirichlet, as BH_u implies for the large prime factor). The proof would follow Ford–Konyagin: truncate to prime factors in (X^ε, X^{1−ε}) (at most 1/ε of them, counted by CRT in classes mod q₁⋯q_r), get the coins of one prime from Lemma W and the top coins of the others by averaging over the primes (sums over primes of e(h·n/q^L) via BH_u in place of Vaughan's identity), and use B₀ through BH_u with c ranging over the cofactors. This has not been carried out; it is a project of the size of the Ford–Konyagin paper.

**Comparison of hypotheses.** k ≤ 2: unconditional (§12). k = 3, 4: Schinzel's Hypothesis H for 8 or 10 quadratic polynomials (agent g6's quartic families, Dickson-type). All k: either H for the cyclotomic pieces of the Balog–Wooley families plus Conjecture G (§9), or BH_u for k − 2 quadratics plus a Ford–Konyagin analysis (this section). The second route needs no statement about simultaneous prime values and no Conjecture G, but it is not written.

### 13.4 Other mechanisms examined for k ≥ 3 (agent h1, second pass)

The minimal elements a(k) of E_k (OEIS A375077, k ≤ 16; `code/h2/a375077.py`) grow like 10^{k+1}, in line with the random-model density 0.114^{k+1}, and their large prime factors sit just below √(2n), each saved by exactly one carry: the record witnesses are random-model luck, not structure. The following alternatives were examined; each fails at a specific point, recorded so that it is not re-explored.

**(a) Automatic carries from the prime factors themselves.** If n − i = m with m/q ≡ −1 (mod q) for every prime q | m, then the base-q digit of n at position 1 is q − 1 for every q | m, and every carry is automatic. This condition is Σ_{q|m} 1/q + 1/m ∈ ℤ, i.e. m is a primary pseudoperfect number (2, 6, 42, 1806, 47058, …; eight are known) or a Giuga-type generalization. Sylvester's recursion s_j = 1 + ∏_{l<j} s_l produces such m = ∏ s_l whenever the s_l are prime, and gives the consecutive pair (∏_{l<j} s_l, s_j), but s_j is then prime (fatal), and no mechanism produces k + 1 consecutive such numbers. The general version, m/q ∈ [q/2, q) mod q for all q | m, can be met for a single m by choosing its primes one at a time with Dirichlet's theorem, but k + 1 consecutive such m would require the k + 1 products to be consecutive integers, which the Chinese remainder theorem cannot force (the cofactor (n − i)/∏_j q_{ij} is of size M/∏_j q_{ij} ≫ 1).

**(b) Smooth parts by CRT.** Making each n − i divisible by a prescribed smooth S_i ≈ n^{1−ε} with prescribed digits leaves cofactors c_i = (n − i)/S_i that are linear in the free parameter s (n = n₀ + sM, M = ∏S_j), so their digits are equidistributed along s. But all prime factors of c_i must be ≤ √(2n), which forces S_i ≥ √n for every i and ∏S_i ≤ n: impossible for k ≥ 2. Total controlled mass through congruences is at most log n; identities are needed for more.

**(c) Norm forms.** Pieces that are norm forms N_K(linear form in a 2-dimensional lattice parameter) have fully accessible anatomy (prime ideals in regions; Hecke). But n − i = λ_i ∏_j N_{K_{ij}}(…) identically for two values of i is impossible: comparing the monomials α^dᾱ^j forces proportional polynomials and then a nonzero constant difference of proportional norms. More generally the top-degree binary forms of n and n − i must coincide, so all members lie in one field and the cross terms force the constant terms to agree. At most one member of a family can be a norm form in the lattice parameter.

**(d) Divisor surfaces.** On the surface xy = Q(z) the irreducible member Q(z) becomes the product of two "pieces" x, y; restricting to x ∈ [√(Q/2), √(2Q)] makes both ≤ √(2n). The parameter set {z : Q(z) has a divisor in that window} has density ≍ (log z)^{−δ}(log log z)^{−3/2}, δ = 1 − (1 + log log 2)/log 2 = 0.086 (Ford's multiplication-table exponent, if it transfers to Q(z)), and the digit events must then be shown equidistributed on this thin set, which needs roots of Q mod d ≈ X in intervals of length q^{−L}: far beyond Hooley's or DFI's equidistribution. The digits of n in base q do not depend on which divisor is chosen, so the factorization structure only certifies P⁺(Q(z)) ≤ √(2n); it buys nothing for the coins. Polynomial parametrizations of the surface (Bezout in K[s] with K = ℚ(√disc Q): z − α = βγ gives Q(z(s)) = A·N(β)N(γ)) reproduce exactly agent g6's quartic families with quadratic pieces, since balance forces deg N(β) = deg N(γ) = deg z and the formerly linear pieces become quadratics in s.

**(e) Quadratic pieces with a common denominator.** In g6's families n − i = F_i(Y)G_i(Y)/H with monic quadratics F = Y² + sY + t, G = Y² − sY + u and H = 16800 or 10483200, the level-2 digit for q | F with cofactor c is (cℓ(Y) + ρq)/H with ℓ = G − F = −2sY + (u − t) and ρ ≡ −c²·ℓ(Y₀)·F(Y₀)^{−1} (mod H), so it is ρq/H + O(cY/H): deterministic, decided by the square class of c mod H, as long as c ≪ √(YH). This is the analogue of Lemma S (with H in place of a) and is what makes g6's pointwise checks work for prime pieces. Without H (H = 1) the digits of the two pieces of a member are c·ℓ and −c·ℓ, so one of the two pieces fails automatically for all its primes with small cofactor: a common denominator H is essential in quadratic-piece families. For composite pieces the deterministic regime is q > F(Y)/√(YH) ≈ Y^{3/2}, of weight log(4/3) per piece, and the regime q ∈ (Y, Y^{3/2}), of weight log(3/2) per piece, has a pseudo-random coin and needs the counts of 13.1(a). Even with fair coins and exact counts its contribution is 8·½·log(3/2) = 1.6 for E₃.

**(f) Lucas strings.** For a Lucas sequence with Q = 1 (e.g. V_n = L_{2n}), the five consecutive integers V_{2n} − 2, …, V_{2n} + 2 are D·U_n², V_{3n}/V_n, V_{2n}, (V_n − 1)(V_n + 1), V_n²: a five-term string with every member a product of primitive parts of relative size ≤ φ(d)/… . It is an exponential family (no digit equidistribution) and two of the five members are squares, which are fatal for prime pieces (a prime piece q with q² ∥ n − i has a single coin at level 3). The three-term middle is the x^m ± 1 family of §8 in disguise.

**(g) What the random model needs for consecutive integers.** Even for integers n (no polynomial structure), a Ford–Konyagin analysis of E_k needs the joint distribution of prime factors q_i | n − i up to √(2n) for all i ≤ k, i.e. equidistribution of consecutive integers in progressions to moduli ∏q_i ≈ n^{(k+1)/2}: beyond Bombieri–Vinogradov/BFI (level 1/2 to 4/7) already for k = 1. Hildebrand's theorem on consecutive smooth numbers (positive proportion of n with P⁺(n(n+1)) ≤ n^θ) holds for θ > e^{−1/2}, not for θ = 1/2. Polynomial families are the only known way to reach θ = 1/2 for k ≥ 1.

**(h) Linear pieces and the Ford–Konyagin method (see the correction in 13.5).** For a linear piece ax + b, the x with q | ax + b are parametrized by the cofactor u through ax + b = qu, so n(x) = λ₀P₁P₂ becomes the polynomial λ₀·qu·(a′qu + κ)/a in (q, u). Sums over primes q with u fixed of e(h·n/q^L) are therefore Weyl sums over primes with polynomial phases (Vinogradov–Vaughan), which is the input Ford–Konyagin use for the joint distribution of the top coins of several primes of one integer. For primes in two different pieces with product above X this is not enough; see 13.5. Together with Lemma W (one prime, all coins), the Hensel bijection, and the prime number theorem in progressions, the density of {x : n(x) ∈ E₁} along a linear-piece family should equal the random-model value, not just be positive. Simulating the model (independent Poisson–Dirichlet anatomies for the pieces, 2^{1−L} for medium primes, f_j and f_j/2 in the top regime; `code/h2/model_density.py`) gives 0.648 for n = (12x−1)(22x+9) (observed 0.597 at x ≈ 10¹⁵, rising), 0.676 for n = 2(12x+5)(35x+32), 0.541 for the Theorem A family, and 0.445 for the E₂ family n = (14x−1)(15x−1) (observed 0.327 at 10¹⁵; the convergence is slowed by the forms 210x−29 and 35x+1, whose prime factors above √(2n) fail automatically with weight ≍ 1/log x). For an irreducible quadratic member the (q, u)-parametrization does not exist (q u = Q(x) has no polynomial section), which is the precise reason 13.3 needs Hypothesis BH_u.

### 13.5 Exact density along a linear-piece family: what blocks it

Attempting to turn 13.4(h) into a theorem ("the density of {x : n(x) ∈ E₁} along n = (12x−1)(22x+9) equals the model value 0.648") shows that 13.4(h) overstates what the cofactor parametrization buys. Correction and precise obstruction:

**What is accessible.** For one piece P_j and one prime q, Lemma W gives all coins. For one piece and *several* of its primes q₁, …, q_r (q₁⋯q_r | P_j(x), so q₁⋯q_r ≤ 2a_jX), the x with this divisibility form a progression mod q₁⋯q_r of length ≥ X^{ε}, and the cofactor parametrization P_j(x) = q₁⋯q_r·u makes n a polynomial in (q₁, …, q_r, u), so the top coins of these primes are handled by Weyl sums over primes as in Ford–Konyagin. Pairs of primes in *different* pieces, q | P_j(x), q′ | P_{j′}(x), are accessible by CRT when qq′ ≤ X^{1−ε}.

**What is not.** The joint event q | P_j(x), q′ | P_{j′}(x) with qq′ ≥ X^{1+δ} has at most one solution x per pair, and the sum over pairs of such counts is the joint distribution of large prime factors of two linear forms in x, the same problem as the joint law of P⁺(n) and P⁺(n+1). Writing x = x_q + qt (t ≤ T = X/q < q′), the condition becomes t ≡ −P_{j′}(x_q)·(a_{j′}q)^{−1} (mod q′), i.e. the residue C·D̄ mod q′ (C = −P_{j′}(x_q), D = a_{j′}q) must fall in [T/2, T]. By reciprocity this is the condition that q̄′ mod D lies in a set of ≍ XD/(qq′) residues, so one needs Σ_{q′ ~ Q′ prime} e(hCq̄′/D) to save a factor ≥ Q′/T = qQ′/X over the trivial bound, uniformly in h. Kloosterman sums over primes (Fouvry–Michel; Bourgain–Garaev) save only a small fixed power Q′^{−δ′}, which covers the pairs with qq′ ≤ X^{1+θ′δ′} and no more. The coin-weighted mass of pairs beyond that is a positive constant (the pairs with θ, θ′ ∈ (1/2, 1) carry weights ≈ ¼ each), so neither the second Bonferroni term S₂ nor any higher one can be evaluated, and the Bonferroni lower bound 1 − S₁ + S₂ − S₃ cannot be used either: S₃ has no useful upper bound without the coin weights of inaccessible triples.

**Consequence.** Along a linear-piece family the first moment (one prime at a time) is fully provable and gives the positive density of §12; the exact density is not provable with current tools, for the same reason that the joint distribution of the largest prime factors of consecutive integers is unknown beyond Bombieri–Vinogradov/BFI levels. Ford–Konyagin's theorem concerns one integer n and never meets this. The values 0.648 (E₁), 0.676, 0.541 and 0.445 (E₂) in 13.4(h) are therefore model predictions, supported by the numerics of 12.6, not theorems in waiting. 13.4(h) should be read with this correction.

### 13.6 E_k as strings of consecutive elements of Pomerance's set

Let G = {m ≥ 1 : m | C(2m, m)} (density c₁ ≈ 0.11424 by Ford–Konyagin) and, for z ≥ 1, G_{>z} = {m : q^{ν_q(m)} | C(2m,m) for every prime q > z} ⊇ G.

**Proposition R.** Let m = n − i with 0 ≤ i ≤ k and let q > 2k be prime. Then ν_q(C(2n,n)) = ν_q(C(2m,m)). Consequently, if n ≡ −1 (mod q^{R_q}) for every prime q ≤ 2k with R_q > ν_q((k+1)!), then

  n ∈ E_k  ⟺  n − i ∈ G_{>2k} for all 0 ≤ i ≤ k.

*Proof.* C(2n,n)/C(2m,m) = ∏_{j=0}^{i−1} 2(2m+2j+1)/(m+j+1). For q | m and q > 2i the factors 2m+2j+1 ≡ 2j+1 and m+j+1 ≡ j+1 are nonzero mod q, so the ratio is a q-adic unit; for q ∤ m the statement is empty. For q ≤ 2k, n ≡ −1 (mod q^{R_q}) gives ν_q(n−i) = ν_q(i+1), so Σ_i ν_q(n−i) = ν_q((k+1)!) < R_q ≤ (number of digits q−1 of n) ≤ ν_q(C(2n,n)). ∎

So Erdős's question is exactly whether G (up to bounded primes) contains strings of k+1 consecutive integers for every k, i.e. whether ∩_{i≤k}(G_{>2k} + i) is non-empty. The theory of consecutive values of arithmetic sets does not apply:

- Hildebrand (1985, 1989) and Tao–Teräväinen treat *stable* sets, those with A/p = A up to density zero for most primes p. G is not stable: multiplication by p scrambles the base-q digits of m for every q ≠ p, and m ∈ G says nothing about pm ∈ G (numerically, among m ≤ 10⁵ in G the proportion with 2m ∈ G is 0.34 and with 3m ∈ G is 0.57; `code/h2/propR.py`).
- Even for stable sets Hildebrand's threshold for k consecutive elements is density > 1 − 1/(k−1), sharp by McNamara; with density 0.114 this allows at most pairs. So no general consecutive-values theorem can give E_k for k ≥ 2.
- The first obstruction inside G is already the smoothness: m ∈ G forces P⁺(m) ≤ √(2m). Strings of k+1 consecutive √(2m)-smooth integers are not known to exist for any k ≥ 1 by sieve or stability methods (Hildebrand's consecutive smooth numbers need P⁺(m(m+1)) ≤ m^θ with θ > e^{−1/2} = 0.6065). Polynomial families are the only known device producing them, and §13.2 shows they come with linear pieces only up to k = 2.

In this language §12 says: the set of x with (12x−1)(22x+9) and (12x−1)(22x+9) − 1 both in G has positive density, and likewise for three consecutive members along (14x−1)(15x−1). The random model for G (independent Poisson–Dirichlet anatomies of consecutive integers) predicts that G contains strings of every length with density c₁^{k+1}; the minimal elements a(k) of E_k (A375077) grow like 10^{k+1}, consistent with this.

### 13.7 The top piece: a palindromy identity, the radical, and the first exponent with three levels

For the top piece Φ_{2m} of x^m + 1 (m odd), §4 says level s (1 ≤ s ≤ T − 1, T = ⌊m/φ(m)⌋) carries iff the first nonzero coefficient c_N of Φ_{2m}(t)^{−(s+1)} with N > E_s = m − (s+1)φ(m) is negative. Since Φ_{2m}(t)^{−1} = R(t)/(1 + t^m) with R(t) = (t^m+1)/Φ_{2m}(t) = −Ψ_m(−t) (Ψ_m the inverse cyclotomic polynomial, of degree m − φ(m)), one has c_N = [t^N]R(t)^{s+1} for N < m, and by palindromy of R

  c_{E_s+1} = [t^{E_s+1}] R^{s+1} = [t^{sm−1}] R^{s+1} = ±[y^{m−(s+1)φ(m)+1}] Ψ_m(y)^{s+1}.

So the whole top-piece question is about the coefficients of powers of Ψ_m just above the index m − (s+1)φ(m), i.e. just below the multiples sm of m in the mirrored indexing. The calibration against §6.4 fixes the sign: for `code/h2/toppiece_T3.py` and `toppiece_scan.py` the reported c is negative exactly for the good exponents 165 (c = −1), 195 (−4) and positive for 105 (+3).

**Scan (`toppiece_scan.py`).** Among the 64 odd m ≤ 6000 with m/φ(m) ≥ 2 (all have T = 2, one level): if m is not squarefree the first nonzero coefficient beyond E₁ equals that of the radical (315 → +3 like 105, 495 → −1 like 165, 3465 → +263 like 1155, 4095 → −75 like 1365), so top-goodness is a property of rad(m). Among the 32 squarefree ones: 17 good (165, 195, 1365, 1995, 2145, 2415, 3255, 3315, 3795, 3927, 4305, 4515, 4641, 4785, 5115, 5565, 5865), 14 bad (105, 1155, 1785, 2805, 3003, 3045, 3135, 3705, 3885, 4389, 4485, 4845, 4935, 5655) and one (5313) with coefficient 0 at the first index (c = +1 at the next). The sign shows no visible dependence on m/φ(m) or on μ(m).

**The first exponent with two levels.** The smallest odd m with T ≥ 3 is m₁ = 3·5·7·11·13·17·19·23 = 111546435 (m₁/φ = 3.056). Its two decisive coefficients were computed exactly (six-prime CRT, strided passes over the 256 divisors, FFT with 11-bit splitting for the cube; `toppiece_T3.py`):

  level 1: [y^{38555716}] Ψ² = +1.11468…·10²⁸,  level 2: [y^{2060356}] Ψ³ = +2.09706…·10³⁹.

Both positive: m₁ is top-bad at both levels, so having many levels does not by itself make the top piece good. (The values ≈ 1.1·10^18 in `code/agentAC/bigm_111546435_L*.txt` were reduced modulo a single 63-bit modulus; their signs agree.) Its multiples m₁·r, which need series of length ≈ m₁r, are settled for every prime r in §13.8 by a sampled-convolution identity: about 65 % of the r up to 3φ(m₁) give a top-good m₁r.

**Consequence for the Dickson route.** Nothing changes in the logical status (H + G ⇒ all k), but the data say G is a statement about specific huge integers with no parametric handle: the two-scale formula (§6.3) shows goodness along m₀·r is that of the core m₀, the radical determines the sign, and the first core with three levels is bad.

### 13.8 Multiplying by one prime: a sampled convolution, and the complete picture along m₁·r

**Proposition (sampled convolution).** Let m₀ be odd, φ₀ = φ(m₀), e ≥ 2 with δ = m₀ − eφ₀ ≥ 0, and β_M = [y^M] Φ_{m₀}(y)^e (a palindromic polynomial of degree eφ₀). For an odd prime r ∤ m₀ put m = m₀r and define the level-(e−1) window coefficients

  w_m(t) = [y^{K_m + t}] Ψ_m(y)^e = (−1)^e [y^{K_m + t}] Φ_m(y)^{−e},  K_m = m − eφ(m) + 1, t ≥ 0,

so that the top piece of m carries at level e − 1 iff the first nonzero w_m(t) is negative (§13.7). Then

  w_{m₀r}(t) = Σ_{j ≥ 1, t+1 ≤ rj ≤ eφ₀+1+t} w_{m₀}(j−1) · β_{rj−1−t}.

*Proof.* Φ_{m₀r}(y) = Φ_{m₀}(y^r)/Φ_{m₀}(y) gives Φ_m^{−e} = Φ_{m₀}(y)^e · Φ_{m₀}(y^r)^{−e}, so [y^N]Φ_m^{−e} = Σ_a [u^a]Φ_{m₀}^{−e} · β_{N−ra}. Here K_m = rδ + eφ₀ + 1 because φ(m) = φ₀(r−1). For N = K_m + t the index N − ra = r(δ − a) + eφ₀ + 1 + t lies in [0, eφ₀] exactly when a = δ + j with t + 1 ≤ rj ≤ eφ₀ + 1 + t. Palindromy gives β_{eφ₀+1+t−rj} = β_{rj−1−t}, and (−1)^e [u^{δ+j}] Φ_{m₀}^{−e} = w_{m₀}(j−1). ∎

**Consequences.**
- *Inflation.* For r > eφ₀ + 1 only j = 1 survives. The first nonzero term is at t = r − 1 − eφ₀, with value w_{m₀}(0)·β_{eφ₀} = w_{m₀}(0). So m₀r inherits the level-(e−1) sign of m₀ (this recovers §9.1).
- *One-term range.* For (eφ₀ + 2)/2 < r ≤ eφ₀ + 1 one has w_{m₀r}(t) = w_{m₀}(0)·β_{r−1−t}. So the level sign of m₀r is sign(w_{m₀}(0)) times the sign of the first nonzero coefficient of Φ_{m₀}^e at or below index r − 1. Along a prime multiplier, top-goodness therefore becomes the question of which signs the coefficients of a cyclotomic power take at the positions p − 1.
- *Cost.* One pass over Φ_{m₀}^e and the window of m₀ gives w_{m₀r}(0), w_{m₀r}(1), … for every prime r at once, at total cost Σ_r eφ₀/r ≈ eφ₀ log log φ₀ per CRT prime. This replaces series of length ≈ m₀r.

`code/h2/toppiece_rscan.py` implements this. It was checked against the exact series (python integers, no modulus) for every prime r with m₀r < 20000 and m₀ ∈ {105, 165, 195, 1365}: all signs, offsets and values agree, including the list 1155 (+263), 1365 (−75), … of §13.7.

**The first exponent with three levels, all multipliers.** Take m₀ = m₁ = 3·5·7·11·13·17·19·23 (φ₀ = 36 495 360). Every m₁r has T = 3, since 3 < m₁r/φ(m₁r) ≤ 3.166, so it has two levels. Both levels were computed for every prime r ≥ 29 up to the inflation bound, with twelve CRT primes (range 10^111). The largest |w| was 10^84 at level 2 and 10^57 at level 1, and no first coefficient vanished.

| | primes r | level carries |
|---|---|---|
| level 2 (e = 3), 29 ≤ r ≤ 3φ₀ + 1 | 6 275 473 | 3 153 678 (50.3 %) |
| level 1 (e = 2), 29 ≤ r ≤ 2φ₀ + 1 | 4 283 547 | 2 137 216 (49.9 %) |

- The level-2 fraction is 0.497–0.507 in each of the ranges [29, 10³), …, [10⁷, 3φ₀/2), [3φ₀/2, 3φ₀]. In the one-term range it is decided by sign β_{r−1}, since w_{m₁}(0) > 0.
- Top-good (some level carries): 72.7 % of the r ≤ 2φ₀ + 1, against 75 % for independent fair levels. The correlation between the two level signs is 0.098. For 2φ₀ + 1 < r ≤ 3φ₀ + 1 it is 50.0 %, because level 1 inherits m₁'s bad sign. For r > 3φ₀ + 1 it is 0 %, because both levels inherit. Overall 4 109 232 of the 6 275 473 primes up to 3φ₀ + 1 give a top-good m₁r.
- r = 29: both levels carry, with level-2 value −7.34·10^72 (confirmed by ten-prime CRT, `toppiece_m1r_x4.py`; a six-prime run had wrapped). r = 31: level 2 only (−1.83·10^67). The first top-bad multipliers are 37, 67, 83, 89, 103.

**What this does and does not give.** The top piece is not the obstruction to Conjecture G. From any exponent m₀ with T ≥ 2, about half of the multipliers r ≤ eφ₀ (three quarters when two levels are live) make the top piece good. Which ones they are is decided by the signs of Φ_{m₀}^e at r − 1, which look like fair coins. But G(P) needs a good m with every prime factor > P. Multiplying by r keeps the small primes of m₀ and does not raise T, so the expensive step is still producing m₀ with all primes > P and m₀/φ(m₀) ≥ 2 (size about e^{P²}). The non-top pieces of m₀r are also untouched by this section. A proof of G along these lines would need (i) a prime r in (φ₀, 2φ₀] with Φ_{m₀}² having a coefficient of prescribed sign at index 2φ₀ + 1 − r (a "primes in a sign set" statement for cyclotomic coefficients), and (ii) control of the pieces dr, d | m₀, d < m₀, which obey the same sampled convolution with Φ_{2d}-data. Neither is available.

### 13.9 Two attempts that fail for structural reasons

**(a) Certificates for the top piece of exponents with all primes > P.** In the one-term range of §13.8, write r = eφ₀ + 1 − i. Then the level sign of m₀r is sign(w_{m₀}(0)) · sign(b), where b is the first nonzero of β_i, β_{i+1}, …. If w_{m₀}(0) = 0, the first window coefficient of m₀r is w_{m₀}(t₀) · β_{eφ₀}, so m₀r simply inherits m₀'s sign. Since β_i for i < D depends only on the divisors of m₀ below D, b is computable even when m₀ has hundreds of digits. So two primes r₊ and r₋ with b > 0 and b < 0 would certify that one of m₀r₊, m₀r₋ is top-good without computing m₀'s window. This would be the "mechanism that does not go through near-integrality of m/φ(m)" asked for in §9.4.

The rule was checked against the exact series for all 388 primes r in the one-term ranges of m₀ ∈ {105, 165, 195, 1155, 1365, 3003}, with no disagreement (`code/h2/endwindow_check.py`). For m₀ = product of the primes in [31, 1193] (491 digits, μ = +1) and in [31, 1201] (494 digits, μ = −1), the 34 primes r = 2φ₀ + 1 − i with i < 2·10⁴ (BPSW) all have b > 0 (`code/h2/topcert.py`). The values grow like a partition function, up to 10^75 at i ≈ 2·10⁴.

The reason is that Φ_{m₀}² ≡ (1 − y)^{2μ} ∏_{p | m₀} (1 − y^p)^{−2μ} below p₁p₂, and this series is positive-dominated as soon as p₁ is moderately large. The only negative coefficients there are β_{p+1} = −4 for p | m₀, p < 2p₁ − 1, when μ = +1. So multipliers near the end of the one-term range preserve the top sign, just as multipliers beyond it do (inflation). Sign changes happen only for r deep inside the range, where β is not explicit. For m₁, whose primes start at 3, the coefficients oscillate early, which is why §13.8 sees 50 %.

**(b) Giving the irreducible member norm-form factors by parametrizing x.** In the E₂ family (14x − 1)(15x − 1), the member n − 3 = Q(x) = 210x² − 29x − 2 is, up to constants, N_{K/ℚ}(420x − 29 + √2521) with K = ℚ(√2521). Writing 420x − 29 + √2521 = βγ with β = a + b√D, γ = c + d√D forces ad + bc = 1. So x is parametrized by a coset of a congruence subgroup of SL₂(ℤ), and Q(x) becomes the product of the two binary norm forms a² − Db² and c² − Dd², each with full level of distribution in its own row. But x = (ac + Dbd + 29)/420 is then a rank-4 quadratic form in the entries, and every formerly linear piece (14x − 1, x, 6x − 1, …) becomes an absolutely irreducible quaternary quadric. For those, the available equidistribution (spectral gap for SL₂(ℤ) in congruence classes, or the affine sieve) gives only a small power of the number of points, far below their size. The level has moved from the linear pieces to Q, not increased. This is forced by the remark in §13.2: if every piece split over ℚ̄ after the substitution, the four members would be completely reducible fibers of a non-univariate pencil over ℂ, contradicting Yuzvinsky.

### 13.10 A closed trace formula for the top coefficient, and why it does not decide the sign

Let c(m) = [y^{m-1}] Φ_m^{-2} be the level-1 top coefficient of §13.7. Expanding Φ_m^{-2} in partial fractions and using Φ_m·Ψ_m = y^m − 1, one gets the exact formula

  c(m) = (1/m²) Σ_{ζ primitive m-th root} ζ Ψ_m(ζ)² [ (2m − 1) − 2 ζ Ψ_m'(ζ)/Ψ_m(ζ) ],

with Ψ_m(ζ) = ∏_{e|m, e<m} (ζ^e − 1)^{−μ(m/e)}. Every factor is explicit in terms of sines and cotangents of πa/d over the divisors d of m.

Check (`code/h2/trace_top.py`). The formula reproduces the series value exactly for m = 105, 165, 195, 1155, 1365, 3003, 15015 and 19635. The imaginary parts are at most 10^{-6}.

Why it does not decide the sign. The plan was to read sgn c(m) off a few dominant roots ζ_a for structured huge m. The sum is not concentrated.

| m | share of Σ|term| in the top 2 | in the top 10 |
|---|---|---|
| 105 | 0.222 | 0.706 |
| 1365 | 0.178 | 0.516 |
| 15015 | 0.124 | 0.397 |
| 19635 | 0.192 | 0.571 |

The top-10 share falls with m. The value c(m) comes from cancellation among φ(m) terms of comparable size, which is the same equidistribution behaviour seen in §13.7–13.8. A sign certificate would need an equidistribution statement for the phases arg(ζ_a Ψ_m(ζ_a)²) that is uniform in m. That is a question about cyclotomic values of the same difficulty as the coefficient question itself. The formula is still useful as an O(φ(m)·τ(m)) floating-point evaluator, independent of the series, for m too large for the power-series method. The sign is reliable when |c(m)| is well above the accumulated rounding error.

### 13.11 Peak dominance in the trace formula for exponents with every prime ≡ ±3 (mod 8)

This section is numerical evidence and a heuristic mechanism, not a proof.

**Setting.** Take m odd and squarefree with every prime p | m satisfying p ≡ ±3 (mod 8), that is χ₈(p) = −1 for the even character χ₈ mod 8. By the Peak lemma (§9.5), |Ψ_m| has a doubly exponential peak at the primitive 8th roots of unity. In the trace formula of §13.10 the sum runs over primitive m-th roots ζ_a. Reparametrize by c ≡ 8a (mod m), so a ≡ c·8⁻¹ (mod m). Then for every d | m, exactly,

  a/d ≡ c(1 − d²)/(8d) (mod 1),

because 8·(1 − d²)/8 ≡ 1 (mod d). For |c| ≪ d this is −cd/8 + O(|c|/d). Expanding log|2 sin πx| on odd residues mod 8 as ¼ log 2 − B₈χ₈(x), with B₈ = ½ log(1+√2), gives the skeleton

  log R_a ≈ ¼ log 2 + B₈ χ₈(c)(2^r − 1),  r = ω(m),

up to corrections of size O(|c|·Σ_{d|m} 1/d). So the dominant terms are the units c ≡ ±1 (mod 8) of small absolute value. They exceed every other class by a factor of about exp(4B₈·2^r).

**Observation.** The largest terms sit exactly where predicted. For m = 40755 and m = 43730115 the six largest terms have 8a mod m ∈ {7, −1, 23, 31, 47, 71, 79}. That is c ≡ ±1 (mod 8) of small absolute value, avoiding c with a factor in common with m. In both cases the partial sums, taken in decreasing order of size, have the sign of c(m) from the first term on (`code/h2/trace_peak.py`).

**Single-term sign prediction.** Here is how often the sign of the largest term equals sgn c(m). The family is all such m with m/φ(m) ≥ 2. The exact series is used for m ≤ 2·10⁵, for r = 7, and the float trace sum otherwise (`code/h2/trace_peak_scan.py`, `code/h2/peak_r7.py`; raw output `peak_scan.txt`, `peak_r7.txt`).

| r = ω(m) | m in family | largest term predicts sign | mean share of Σ|term| in largest term | top-good |
|---|---|---|---|---|
| 4 | 85 (m ≤ 3·10⁶) | 41 (chance level) | 0.06 | 14 |
| 5 | 705 (m ≤ 3·10⁶) | 619 (88 %) | 0.11 | 402 |
| 6 | 9 (m ≤ 3·10⁶) | 9 | 0.45 | 4 |
| 7 | 8 (m ≤ 8·10⁷), exact six-prime CRT | 8 | 0.47–0.49 | 4 |

At r = 7 the float trace sum also agrees with the exact sign in all 8 cases. The top-good m are 43730115, 62640435, 72095595 and 79920555. The bad ones are 50821485, 64841205, 69731805 and 79186965. Accuracy and concentration rise with r, as the exp(4B₈·2^r) gap predicts.

**What this would give, and what is missing.**
- If the peak band dominates, then sgn c(m) is the sign of an explicit expression. It depends on m mod 16, on τ = m/φ(m) through the phase θ_a/2π ≡ −cm/8 − c/(8τ) + c/(8m), and on the Euler products ∏_{p|m}(1 − χ(p)/p) for the odd characters χ₋₄ and χ₋₈ mod 8, which enter through S_a. That would turn the top-piece part of Conjecture G into choosing primes ≡ ±3 (mod 8) above P with these residues and products prescribed. The non-top (Band) pieces of §9.3 would still have to be handled separately.
- Gap 1 (bulk). A rigorous bound log R_a ≤ (1 − ε)B₈·2^r for all a off the peak band. This is the open item of §9.5. The trivial bound is useless, and the sums Σ_{d|m} μ(d)e(na/d) have no product structure.
- Gap 2 (band width). The tested m have small primes (3, 5, 11, …). When every prime exceeds P, the skeleton holds for all |c| ≪ P. Then many terms c ≡ ±1 (mod 8) have nearly equal size, with log R drifting linearly in |c| at a rate set by the two Euler products. Their phases rotate by about −1/τ ≈ −½ turn per step of 8 in c. So single-term dominance is not expected for large P. The sign would come instead from a two-sided, nearly geometric sum whose closed form has not been worked out or tested.
- Untested: whether the 88 % at r = 5 rises to 100 % for every r ≥ 6, beyond the 17 cases above.
