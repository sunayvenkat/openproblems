# Agent V referee report (saved by main thread from the agent's hand-back)

## Summary
- Lemma A FALSE; DRAFT claim "1365 good" FALSE: piece d = 455 bad (all levels s = 1,2,3 positive). Φ_910(288) is a 709-digit prime with 0 carries, so 288^1365+1 ∉ E_0. Scaled copies (6825,2275), (9555,3185), (17745,5915) also bad.
- DRAFT §§1–4 logic VERIFIED given good m: Lemma 1, §3, Capelli, open image, digit setting, no fixed prime divisor, H step. log₂(k+1) condition is necessary (k = 7, m_8 = 3 gives reducible Φ_2(A_1) = y³+1).
- A375077 (n−k ≥ 2): k=1 210, 2480, 8178, 45153, 3648841, 7979090, 101130029; 339949252 ∈ E_8 but ∉ E_9 (n−9 prime).

## Witnesses (verifier IN)
| k | n | construction |
|---|---|---|
| 1 | 34359738370 = 2^35+2 | F₊ with (m_1,m_2) = (35,17), B = 1; smallest F₊ member of E_1 up to 10^18 |
| 1 | 481469424205826 | (5,3), B = 6 |
| 1 | 2251799813685250 | (3,5), B = 8 |
| 2 | 564577950256479015091764461571 = 8264970432³+3 = 2·54^17+3 | variant |

## Claim-by-claim
- §1 VERIFIED. §2 Lemma 1 VERIFIED (49478 random cases); q > 2i needed ((827022652314,4,5): 9 vs 6 carries). For i < q ≤ 2i: carries(n) ≥ carries(n−i)+1.
- §3 VERIFIED with FIX: "are the carries" → "at least the carries"; equality with e_p ≥ ν_p((k+1)!)+2. e = ν_p((k+1)!) fails at (k,p,n) = (2,3,245).
- §4.1 CRT VERIFIED (coprimality sufficient). §4.2 Capelli VERIFIED (sympy for (3,5),(5,3),(3,5,7)). §4.3 open image VERIFIED (sharp for odd p; bijective for p = 2, L odd); digit setting VERIFIED (k=2,(3,5,7): b ≡ 61 mod 216). No fixed prime divisor VERIFIED. §4.4 VERIFIED.
- §5 Laurent rule VERIFIED at x ~ 10^12 for m ∈ {15,105,165,195}, all pieces, j ≤ 3; factor j does not change the sign (threshold grows with j).
- §5 data: 165, 195, 15015, 51051, 255255 fully good; 105, 1155, 37182145 bad at top; 1365 FALSE.

## Tools (agentV/)
verify396.py (Miller–Rabin + Pollard–Brent, Kummer vs Legendre cross-check), brute.py (segmented sieve: |E_0|=11359, |E_1|=1028, |E_2|=99, |E_3|=8, |E_4|=1 up to 10^5), stress.py, laurent_test.py, bigx.py, fastgood.py.

## Audit of the k = 1 construction (m_1 = 123 Aurifeuillean, m_2 = 59814755)
Naming: "level s" (agentAC, checkB, deep.py) = carry exponent t = s+1.
1. F(±y): VERIFIED. aur3(123): deg 80, F(0) = 1, lc 123^40, F(y)F(−y) = Φ_246(123y²), F = C(x) + 123y D(x) with C, D in Z[x]. Tail signs by exact Z[x] division: F(+y) carries at t = 2 (not t = 3); F(−y) carries at t = 3 (not t = 2). Direct test: 240 random cases, 0 mismatches. t ≥ 4 irrelevant (F^4 ~ x^160 > N).
2. Irreducibility and fixed divisors: VERIFIED (e = 9032028006; e/123 and e/246 nonzero mod every ℓ | m_2; a = 151 nonzero mod 3 and 41; square classes fine; sympy: F irreducible). F(0) = 1, so b ≡ 0 mod p makes every piece ≡ 1.
3. Pieces d = 1, 3, 41 of x^123+1: VERIFIED good at t = 3 (coefficients −7503, −2460, −3).
4. m_2 top piece: VERIFIED (−74322712269080 at E+1 = 95076, also via [t^N]Ψ²). Non-top pieces: agrees with checkB on all 21 pieces it checked; higher-t confirmations for 385, 595, 7315, 7735, 8645, 13585, 14245, 17765 (t = 4) and 455, 6545, 12155, 20995 (t = 5). Remaining pieces were left to deep.py (main thread).
5. Small primes: VERIFIED (n ≡ 2 mod 4, n−1 odd).
Tools: aurcheck.py, periodic.py, direct_m2.py.
