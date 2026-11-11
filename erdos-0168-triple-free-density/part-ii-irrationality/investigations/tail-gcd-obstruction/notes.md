# The Single-Clearer Divisibility Obstruction and Cross-Factor Elimination (Route M)

**Date:** 2026-11-10  
**Status:** **Single-clearer modular obstruction rigorously proved; cross-factors eliminated; certified in `verify_single_clearer_obstruction.py`.**  
**Labels:** **[P]** Rigorous mathematical derivation; **[C]** Exact reproducible Python certification.

---

## 1. Executive Summary & Mathematical Resolution

Previous attempts to close Route M via pair-level clearer GCDs ($\gcd(D_{n_1}, D_{n_2}) \le 4914$) failed due to **cross-factors**: as documented in `codex_review.md`, an outside prime $\ell \notin \{2, 3, 7, 13\}$ can divide the horizontal factor $2^{3q_1}-1$ of the first clearer and the vertical factor $3^{3p_2}-1$ of the second clearer, as occurred at $(5/8, 12/19)$ where $\gcd = 24570 = 5 \times 4914$.

Here we prove that **cross-factors do not exist at all** in the true divisibility obstruction to rationality.

Under the rationality hypothesis $Z = A/B$, Lemma 8.1 establishes that $B$ must divide $D_n$ for **every single** sufficiently late adequate nonresonant convergent $n \in K$. Thus, we do not need to bound the joint GCD of pairs or triples of clearers. We only need to show that this **specific, fixed denominator $B$ cannot divide $D_n$** at an individual convergent $n$.

At a **single** convergent $n$, $D_n = 27 (2^{3q_n}-1)(3^{3p_n}-1)$. A prime $\ell$ divides $D_n$ if and only if $m_2(\ell) \mid q_n$ or $m_3(\ell) \mid p_n$. There is no cross-interaction between different indices because only one clearer $D_n$ is involved!

---

## 2. The Single-Clearer Divisibility Obstruction (SCDO)

### Theorem 1 (Single-Clearer Divisibility Obstruction).
*Let $Z = A/B$ with $A \in \mathbb{Z}$, $B \in \mathbb{Z}_{\ge 1}$, and $\gcd(A, B) = 1$. Let $K = \{n \ge 1 : \sigma_n = p_n + q_n \not\equiv 0 \pmod 3, \ a_{n+1} \ge 5\}$.*

1. **Eventual Divisibility (Lemma 8.1):**  
   *There exists an integer cutoff $N_0(B)$ such that for all $n \in K$ with $n \ge N_0(B)$:*
   \[
   B \mid D_n, \quad \text{where } D_n = 27(2^{3q_n}-1)(3^{3p_n}-1).
   \]

2. **The Associated Modulus $M_B$:**  
   *Let the prime factorization of $B$ be:*
   \[
   B = 2^{v_2(B)} 3^{v_3(B)} 7^{v_7(B)} 13^{v_{13}(B)} \prod_{i=1}^r \ell_i^{k_i},
   \]
   *where $\ell_1, \dots, \ell_r$ are distinct primes outside $\{2, 3, 7, 13\}$.*  
   *For each $\ell_i$, define the multiplicative orders:*
   \[
   m_2(\ell_i) := \frac{\operatorname{ord}_{\ell_i}(2)}{\gcd(\operatorname{ord}_{\ell_i}(2), 3)} \ge 2, \qquad m_3(\ell_i) := \frac{\operatorname{ord}_{\ell_i}(3)}{\gcd(\operatorname{ord}_{\ell_i}(3), 3)} \ge 2.
   \]
   *Define the fixed positive integer:*
   \[
   \boxed{M_B := 2 \times 3 \times 7 \times 13 \times \prod_{i=1}^r m_2(\ell_i) m_3(\ell_i).}
   \]

3. **Obstruction at a Single Coprime Convergent:**  
   *Suppose there exists an index $n \in K$ with $n \ge N_0(B)$ satisfying:*
   \[
   \gcd(p_n, M_B) = 1 \quad \text{and} \quad \gcd(q_n, M_B) = 1.
   \]
   *Then:*
   \[
   \boxed{\gcd(B, D_n) \le 2^1 \cdot 3^3 \cdot 7^1 \cdot 13^1 = 4914.}
   \]
   *In particular, since $B \mid D_n$, this forces:*
   \[
   B = \gcd(B, D_n) \le 4914.
   \]
   *This directly contradicts the certified continued-fraction denominator lower bound $B \ge 2^{150990} > 10^{45452} > 4914$.*

---

## 3. Proof of Theorem 1

*Proof.*  
**Step 1 (Eventual Divisibility):**  
For $n \in K$, $a_{n+1} \ge 5$, so $q_{n+1} \ge 5q_n + q_{n-1}$. By the accepted rectangle error bound (R13):
\[
|D_n (Z - z_n)| \le 486 (1 + o(1)) 2^{5q_n - q_{n+1}} \le 486 (1 + o(1)) 2^{-q_{n-1}} \longrightarrow 0 \quad \text{as } n \to \infty.
\]
Under $Z = A/B$, multiplying by $B$ gives:
\[
|A D_n - B (D_n z_n)| = B |D_n (Z - z_n)|.
\]
Since $D_n z_n \in \mathbb{Z}$, the left-hand side is an integer. For all $n \ge N_0(B)$, $B |D_n (Z - z_n)| < 1$, so the integer must be zero:
\[
A D_n = B (D_n z_n) \implies B \mid A D_n \implies B \mid D_n \quad (\text{since } \gcd(A, B) = 1).
\]

**Step 2 (Valuation Bounds from Coprimality):**  
Let $n \in K$ satisfy $n \ge N_0(B)$ and $\gcd(p_n, M_B) = \gcd(q_n, M_B) = 1$.  
We evaluate the $p$-adic valuation of $\gcd(B, D_n)$ at every prime:

1. **Prime 2:**  
   Since $2 \mid M_B$, $\gcd(p_n, M_B) = 1 \implies p_n$ is odd.  
   By the corrected LTE formula, $v_2(D_n) = 1$ for odd $p_n$.  
   Therefore, $v_2(\gcd(B, D_n)) \le v_2(D_n) = 1$.

2. **Prime 3:**  
   Since $2 \mid M_B$, $\gcd(q_n, M_B) = 1 \implies q_n$ is odd.  
   By the corrected LTE formula, $v_3(D_n) = 3$ for odd $q_n$.  
   Therefore, $v_3(\gcd(B, D_n)) \le v_3(D_n) = 3$.

3. **Prime 7:**  
   Since $7 \mid M_B$, $\gcd(q_n, M_B) = 1 \implies 7 \nmid q_n$.  
   Furthermore, $p_n$ is odd.  
   By the valuation formula:
   \[
   v_7(D_n) = 1 + v_7(q_n) + \mathbf{1}_{\{p_n \text{ even}\}} (1 + v_7(p_n)) = 1 + 0 + 0 = 1.
   \]
   Therefore, $v_7(\gcd(B, D_n)) \le v_7(D_n) = 1$.

4. **Prime 13:**  
   Since $13 \mid M_B$, $\gcd(p_n, M_B) = 1 \implies 13 \nmid p_n$.  
   Furthermore, $q_n$ is odd, so $4 \nmid q_n$.  
   By the valuation formula:
   \[
   v_{13}(D_n) = 1 + v_{13}(p_n) + \mathbf{1}_{\{4 \mid q_n\}} (1 + v_{13}(q_n)) = 1 + 0 + 0 = 1.
   \]
   Therefore, $v_{13}(\gcd(B, D_n)) \le v_{13}(D_n) = 1$.

5. **Outside Primes $\ell_i$:**  
   For each prime factor $\ell_i \mid B$ with $\ell_i \notin \{2, 3, 7, 13\}$:  
   By definition of $M_B$, $m_2(\ell_i) \mid M_B$ and $m_3(\ell_i) \mid M_B$.  
   The coprimality condition gives:
   \[
   \gcd(q_n, M_B) = 1 \implies m_2(\ell_i) \nmid q_n,
   \]
   \[
   \gcd(p_n, M_B) = 1 \implies m_3(\ell_i) \nmid p_n.
   \]
   By Theorem 2 (Multiplicative Order Criterion), $\ell_i \mid D_n \iff m_2(\ell_i) \mid q_n \text{ or } m_3(\ell_i) \mid p_n$.  
   Since neither holds, $\ell_i \nmid D_n$.  
   Consequently, $v_{\ell_i}(\gcd(B, D_n)) = 0$.

**Step 3 (Assembly of Bound):**  
Multiplying the prime power bounds:
\[
\gcd(B, D_n) \le 2^1 \cdot 3^3 \cdot 7^1 \cdot 13^1 = 4914.
\]
Since $B \mid D_n$, we have $\gcd(B, D_n) = B$. Thus $B \le 4914$.  
This contradicts $B \ge 2^{150990}$. $\blacksquare$

---

## 4. Verification and Empirical Certification

In [`verify_single_clearer_obstruction.py`](verify_single_clearer_obstruction.py):
1. **Order Criteria:** Tested all 164 outside primes $\ell \le 1000$; 100% satisfy $m_2(\ell) \ge 2$ and $m_3(\ell) \ge 2$.
2. **LTE Valuation Formulas:** 100% match exact integer values on all tested coprime pairs.
3. **Prefix Convergent Analysis:** In the prefix of 106 adequate nonresonant convergents ($N \le 500$):
   - $p_n$ is odd for 63/106 (59.4%).
   - $q_n$ is odd for 71/106 (67.0%).
   - Both $p_n$ and $q_n$ are odd for 28/106 (26.4%).
   - $\gcd(p_n q_n, 7) = 1$ for 84/106 (79.2%).
   - $\gcd(p_n q_n, 13) = 1$ for 90/106 (84.9%).
4. **Refutation of Test Denominators:** Candidate denominators $B \in \{2^{57}, 10^{45452}, 447175, 24570, 83538, 248832\}$ were tested and each was refuted at an individual adequate convergent (e.g., $n = 20$, $p/q = 397573379/630138897$, $a_{21} = 15$).

---

## 5. Precise Remaining Theoretical Boundary (Tasks M1–M7)

Theorem 1 replaces the multi-clearer GCD and tail-GCD requirements with a **single-convergent condition**:
Under hypothetical rationality $Z = A/B$, the single fixed integer $M_B$ determines a finite congruence condition.

The full status across Route M tasks is:
- **Tasks M2–M6 (Valuation Bounds & Nonpersistence):** Proved conditionally on the existence of coprime convergents in $K$. At any index $n \in K$ with $\gcd(p_n, M_B) = \gcd(q_n, M_B) = 1$, all prime valuations are strictly bounded simultaneously.
- **Task M7 (Contradiction Assembly):** Proved. If such an index exists beyond $N_0(B)$, $B \le 4914 < 2^{150990}$ is an immediate contradiction.
- **Task M1 (Actual Adequate Supply):** Remains **OPEN**. It requires proving that $K = \{n : \sigma_n \ne 0, a_{n+1} \ge 5\}$ is infinite and that its reduction modulo $M_B$ visits the coprime locus beyond $N_0(B)$. As documented in `supply_barrier.md`, proving $a_{n+1} \ge 5$ infinitely often for $\log 2 / \log 3$ is an open Diophantine problem.
