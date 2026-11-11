# Agent U report: literature and unconditional routes (saved by main thread)

## Summary
- E_1 infinite is not known. teorth database lists #396 open (2025-08-31). lacker/erdos396 (unrefereed) is conditional on two unproved estimates.
- Computer range is k ≤ 16: OEIS A375077 has 16 terms (28 Jul 2026); a(16) = 20021368432952099.
- No statement of "Hypothesis H ⇒ E_k infinite" found (erdosproblems forum not fetched).
- Almost-prime sieves cannot replace H as stated (Lemma W below; mid-size q is an uncontrolled digit event).
- New: Lemma X (cofactor tolerance), checked numerically (checkX.py, cofactor.py).

## 1. Literature
- Erdős–Graham 1980 (Monogr. Enseign. Math. 28): source.
- Pomerance, AMM 122 (2015) 636–644:
  - Thm 1: k ≠ 1 ⇒ n+k ∤ C(2n,n) infinitely often.
  - Thm 2: k ≥ 1 ⇒ n+k | C(2n,n) on a density-1 set; same proof gives (n+1)…(n+k) | C(2n,n) on density 1.
  - Thm 3: n−k | C(2n,n) infinitely often (n = pq+k, k<p, 3p/2<q<2p), upper density ≤ 1−log 2. A prime p > √(2n) dividing n−k kills it.
  - Thm 4: D_0 + k ∼ D_{−k}; conjecture D_0 has positive lower density.
- Pomerance, "Remarks on the middle binomial coefficient" (preprint 2026): "+"-side results only.
- Ford–Konyagin, Trans. AMS 374 (2021): n^ℓ | C(2n,n) has positive density c_ℓ. Local count to 2·10^5 gives 0.1148 for ℓ=1.
- Balog–Wooley, J. Austral. Math. Soc. A 64 (1998): cyclotomic construction = NOTES family "−".
- Hildebrand 1985/1989 stable sets; McNamara arXiv:2312.08544 shows the 1989 threshold is sharp.
- Teräväinen 2018; Tao–Teräväinen arXiv:2512.01739: correlations of multiplicative functions; 1_{D_0} is not multiplicative.
- Dehorty repo: Lean proof of the small-prime barrier (= Lemma 1). lacker repo: conditional k=1 program.

## 2. New rigorous results
Setting: q > 2k prime, q ‖ N = n−i. Condition at q: {N/q^t} ≥ 1/2 for some t ≥ 2.

**Lemma W.** (i) q > √(2N) ⇒ fails. (ii) q^r ∈ (N, 2N] for some r ≥ 2 ⇒ holds (top digit ≥ q/2).

**Lemma X.** f monic, f | t^m+1, (t^m+1)/f^{s+1} = P_s + R_s with P_s ∈ Z[t], R_s = Σ_{ν≥1} a_ν t^{−ν}, first nonzero a_{ν0} < 0. If N = j′(x^m+1), f(x) = qc, q ‖ N and j′c^{s+1}|R_s(x)| < 1/2, then the condition at q holds. (N/q^{s+1} = j′c^{s+1}P_s(x) + j′c^{s+1}R_s(x), second term in (−1/2,0).) Allowed cofactor exponents ν0/(s+1): m=165: d=1,3,15 → 1/3; 5 → 2/3; 11 → 8/3; 33 → 5/3; 55 → 10/3; 165 → 1/2. m=195: 1,3,15 → 1/3; 5 → 2/3; 13 → 10/3; 39 → 7/3; 65 → 14/3; 195 → 1/2.

**Observation S.** D_0 is not stable (disagreement density 0.18, 0.14, 0.18, 0.20 for p = 2, 3, 5, 7 up to 2·10^5).

## 3. Obstructions
- Sieve/first moment: prime factors r > R_0 of cofactors are uncontrolled; expected bad pairs ≫ 1. Needs a Schinzel-type statement.
- Stable sets / Tao–Teräväinen: handle anatomy, not digit events.
- Green–Tao–Ziegler: constraints are multiplicative.
- Balanced semiprimes for k=1: parity problem (cannot exclude the prime case).
