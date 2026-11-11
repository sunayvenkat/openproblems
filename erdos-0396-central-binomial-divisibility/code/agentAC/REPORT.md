# Agent AC report: Lemmas A and C (saved by main thread from the agent's hand-back)

## Status
| Item | Status |
|---|---|
| Digit form of the criterion (Thm 0, Cor 0.1) | Proved |
| Criterion vs direct Kummer | 12/12 agree, exact carry counts (`verify_kummer.txt`) |
| Lemma A as stated | FALSE: (m,d) = (1365, 455), K = 3; also K = 5: d = 25179, 30261, 43435 |
| Sufficient conditions A1(a–e) | Proved |
| Thm I (inheritance d → dp, incl. top piece) | Proved; 271 prime/seed pairs confirmed |
| Thm A3 (fixed d, all large odd K) | Proved (K_0(d) not explicit) |
| Conjecture A*: failures only for 1/2 < φ(d)/d < 2/3 and K ∈ {3,5} | Numerical only |
| Lemma C | OPEN |
| Cor I.2 (m good ⇒ mp good for large p); 165p (p>160), 195p (p>192) fully good | Proved (not coprime) |
| Prop C1 (last-level top criterion) | Proved; Lehmer-type hypothesis |
| Goodness decided by order type of primes? | No (3·5·7·p irregular for p < 96) |

## 1. Digit criterion
Notation: m odd, d | m, f = Φ_{2d}, δ = φ(d). Base-f expansion x^m+1 = Σ_{k=0}^{T} D_k f^k, deg D_k < δ, T = ⌊m/δ⌋, D_0 = 0, D_T monic.

**Thm 0.** For x ≥ x_0(s): w mod q^s ≥ q^s/2 (w = j′(x^m+1)/q) iff the last nonzero digit among D_1..D_s has negative leading coefficient. Hence ν_q(C(2n,n)) = #{s ∈ [1,T−1] : last nonzero digit among D_1..D_s negative}; the piece is good iff some D_k (1 ≤ k ≤ T−1) is negative. (Proof: w/q^s = integer + j′R_s/f^{s+1}, R_s = Σ_{k≤s} D_k f^k; degree ranges [kδ,(k+1)δ) are disjoint.)

**Cor 0.1.** The decisive coefficient is c_N = [t^N]Φ_{2d}(t)^{−(s+1)} with N ∈ (E, m−δ]; the factor (1+t^m) never matters. Finite-x caveat: for (1365,455) at x = 1000 a carry appears at level 3 although all digits are positive; at x = 10^6, 10^9 none. Only the asymptotic statement is needed under H.

## 2. Criterion vs Kummer
(m,d,k,j′) = (15,1,3,2) 7/7; (15,3,3,1) 3/3; (15,5,2,3) 1/1; (21,3,4,2) 4/4; (21,7,1,1) 1/1; (45,9,2,2) 3/3; (45,15,3,1) 1/1; (105,105,1,1) 0/0; (105,35,2,1) 2/2; (165,165,1,2) 1/1; (195,195,2,3) 1/1; (195,65,1,1) 1/1 (Kummer/predicted, prime q).

## 3. Lemma A
K = m/d, y = x^d+1 = f·g, g = ∏_{e|d,e<d} Φ_{2e}, g^r = Σ_j G_{r,j} f^j. Exactly: D_k = Σ_{r=1}^{k} (−1)^{r+1} C(K,r) G_{r,k−r}.
- Counterexample (1365, 455): δ = 288, T = 4, D_1, D_2, D_3 leads 3, 387, 13812 (all positive). Checked four ways.
- **A1.** (a) d = 1 good (D_2 < 0). (b) φ(d)/d > 2/3 ⇒ good at level 2 (D_2 = −C(K,2)g²). (c) D_1 = K·(g mod f): level-1 transfer from d's own top piece. (d) d = 3 good (D_2 = −3C(K,2)x). (e) φ(d)/d > 1/2 ⇒ D_2 = −C(K,2)(g² mod f), level-2 sign independent of K.
- **Thm I.** p ∤ m prime, p > (s+1)φ(d): level s of piece dp in x^{mp}+1 has the same first window coefficient as level s of piece d in x^m+1, at N′ = p(E+j_0). Two-scale formula (any p): c′_{E′+i} = Σ_{l≥1} π_{(s+1)φ(d)+i−lp} c_{E+l}, π = coefficients of Φ_{2d}^{s+1}.
- **Thm A3.** For squarefree odd d > 1 there is K_0(d) with the piece good for all odd K ≥ K_0(d). (Trace formula for the K^k coefficient of lc(D_k): −a_{k+1}/(d·k!), a_n = Tr(ζ(−γ)^n), γ = g(ζ); a_n ≢ 0 by linear independence of primitive g_0-th roots, g_0 = gcd(d,φ(d)) squarefree; dominant conjugates oscillate.)

## 4. Lemma C
- T = 2 for m < 1.1·10^8, window starts at ρ_0+1, ρ_0 = m − 2φ(m).
- Trace identity (checked by `cosform.py`): c_{E+i} = (−1)^{i+1} A_i/m, A_i = Tr(ρ^i Ψ_m(ρ)²) = −Σ_{k∈(Z/m)^*} |Ψ_m(e^{2πik/m})|² cos(2πk(i−φ)/m).
- **Prop C1.** m squarefree, ω(m) odd, T = ⌊m/φ⌋ ≥ 2, ρ_0 = m − Tφ, p_1 least prime. If T ≤ ρ_0 and some prime q | m has ρ_0 < q+T < 2p_1, the top piece is good at level T−1 (mod t^{2p_1}: Φ_{2m}^{−T} ≡ (1+t)^T(1 − TΣ_q t^q)). Lehmer-type hypothesis; not producible by polynomial / H families.
- Data: of 1487 odd squarefree m ≤ 3·10^5 with φ(m)/m < 1/2, 765 top-good, 738 fully good. Coprime to 3: 37182145 bad, 46881835 bad, 50115065 good, 59814755 good (top).
- Workarounds ruled out: effective exponent mℓ; coprimality is necessary (gcd(m_j,m_j′) | gcd_p(ν_p(j)−ν_p(j′)) = 1); Aurifeuillean splitting for two j′ simultaneously; non-monic pieces (x integer); 4X⁴+1 (one factor carries).

## Files (agentAC/)
core.py, fastser.py, fullgood.py, check455.py, verify_kummer.py, lemA_scan*.py, a3check.py, topscan.py, bigscan.py, fullscan.py, inherit_test.py, family165.py, cosform.py, bigm.py, coprime3.py and their .txt outputs.
