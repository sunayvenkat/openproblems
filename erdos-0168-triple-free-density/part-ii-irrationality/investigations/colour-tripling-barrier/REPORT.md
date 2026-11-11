# Erdős #168(ii): the colour-tripling barrier and a Z-free nonvanishing criterion

Date: 2026-11-08. Scope: part (ii), irrationality of c. No Lean. **No proof of irrationality is claimed.**

## 0. Verdict

Erdős #168(ii) is still open after this round. What changed:

1. **Why every slope model costs 2^{6q} (proved).** An exact affine shift lemma (L1) shows the q-step shift acts on the horizontal state by the rotation u = ω^{2p−q}. That rotation is trivial exactly when p+q ≡ 0 (mod 3).
   - When u ≠ 1, only the 3q-step shift kills the state dependence, because 1+u+u² = 0.
   - When u = 1, the state drifts linearly and no short period exists.

   So the 27(2^{3q}−1)(3^{3p}−1) denominator is forced by the colour structure. It is not a weakness of the construction.
2. **The colour factor 3 is the whole obstruction (accounting, L4).** The same error with ideal periods (q,0),(0,p) would give D|Z−z| ≍ 2^{q−Q}. That tends to 0 for *every* irrational slope, with no partial-quotient hypothesis. The forced tripling turns this into 2^{5q−Q}.
3. **Nonvanishing reduced to model arithmetic (proved, L3).** Assume the working error bound (W4). Then Z is irrational as soon as the reduced denominators of the models are unbounded along the supply subsequence. This replaces the state-eligibility nonvanishing hypotheses with a finite statement about explicit periodic arrays. Z does not appear in it.
4. **Evidence for that arithmetic (computational).** On 110 nonresonant slopes, the reduced model denominator always contains the full Φ_{3p}(3). It contains the full Φ_{3q}(2) in 108 cases. The two failures each lose exactly one primitive prime (103 and 1249), which looks like a 1/ℓ accident. So the strong form "Φ_{3q}(2) always divides den" is **false**. The weak form "den → ∞" survives every test.
5. **Generic continued fraction of Z (computational).** Z has 127 certified partial quotients, maximum 283, geometric mean 2.57 (Khinchin's constant is 2.685). A single-index two-base toy sum has explosive partial quotients (2^{802}-scale). So two bases alone are not the obstruction. The obstruction is the walk memory together with the colour tripling.

**Remaining gap.** One of the following is needed:

- (G1) the partial-quotient supply at nonresonant convergents, together with (G2) unbounded model denominators; or
- (G′) an approximant family with cost ≤ 2^{(2+o(1))q} whose error is still ≲ 2^{−(q+Q)}.

(G1) is the open question of whether log 2/log 3 has partial quotients ≥ 5 infinitely often at nonresonant indices. Even unboundedness of its partial quotients is unknown.

## 1. Working inputs (used, not re-proved)

- **W1** (part i). The finite formula τ = min_j Q_j and the η rule. My independent implementation (`eta.py`) reproduces c = 0.800965755006559…. Increments follow the stated table, starting from Q(2) = (1,0,0). No dependency error was found.
- **W2** (separable relative state, from exact_transport.md). For b ≥ 4, η_{a,b} = F(ζ_{a,b}) with ζ_{a,b} = A_a + B_b − 1 + C_{a mod 3, b mod 3} − E_b and F(x+yω) = 1{x≤0, x≤y}. Here A_{a+1} − A_a = ω^{−a−1}S(⌊(a+1)α⌋), S = (1, −ω, 0) and α = log₃2.
- **W3** (scalar models). For nonresonant p+q ≢ 0 (mod 3), D_{p,q}Z̃_{p,q} ∈ ℤ with D_{p,q} = 27(2^{3q}−1)(3^{3p}−1).
- **W4** (error bound, task statement). For suitable consecutive nonresonant convergents p/q, P/Q, D|Z − Z̃| ≤ 486(1+o(1))·2^{5q−Q}.
- **W5.** Z = 9c − 6 = 3 − 3M, keeping the exceptional (0,1) birth and all low rows.

## 2. Results proved here

### L1. Affine shift lemma

The table S satisfies S(n+1) = ω²S(n) + 1 for all n. Check: 1 ↦ −ω ↦ 0 ↦ 1. Hence S(n+p) = ω^{2p}S(n) + c_p with c_p = Σ_{k<p} ω^{2k}.

Let p/q be a convergent of α, with next denominator Q. For 1 ≤ i ≤ Q−1 we have ⌊(i+q)α⌋ = ⌊iα⌋ + p. This is standard best-approximation: the first i with {iα} inside the defect interval is i = Q. Summing increments gives, for 0 ≤ a ≤ Q−1,

  A_{a+q} = A_q + u·(A_a − 1) + c_p ω^{−q} g(a mod 3),  u = ω^{2p−q},

where g(a) = Σ_{i=1}^{a} ω^{−i}, which is 3-periodic and bounded. The vertical walk B satisfies the same lemma with P(n+1) = ωP(n) + 1.

*Check:* `tripling.py` verifies L1 exactly in ℤ[ω] for p/q = 12/19, 41/65, 53/84 and 306/485. In each case the first failure is at a = Q exactly.

### L2. Forced tripling

u = 1 ⟺ q ≡ 2p (mod 3) ⟺ p+q ≡ 0 (mod 3), the resonant case.

- **Nonresonant (u ≠ 1).** Compose L1 three times; this is valid while a + 3q stays in the agreement range. The coefficient of A_a becomes u³ = 1. The accumulated drift is multiplied by 1+u+u² = 0. So A_{a+3q} − A_a is independent of the state. Verified: the drift is constant, equal to 0, 1, 0 and 0 in the four cases, on the observed ranges a < 27, 19, 317 and 84. These match Q − 2q except at 41/65, where Q − 2q < 0.
- **Resonant (u = 1).** A_{a+kq} − A_a grows linearly in k with step A_q − 1 + c_pω^{−q}g. There is no state-free short return.

Consequence: in the nonresonant case, the q-shift changes the horizontal state by a nontrivial rotation relative to the unrotated vertical state B_b. A rotation does not preserve the cone F. The cheapest state-free horizontal symmetry is the 3q-shift, and symmetrically the 3p-shift vertically.

Numerical confirmation:
- (q,0) and (0,p) near-periods fail at L ≈ 6 for every convergent tested.
- 3(q,−p) agrees up to L ≈ Q+q; for example 570.6 versus 569 at q = 84.

### L3. Nonvanishing via model denominators (Z-free)

Let K be an infinite set of nonresonant suitable convergents with q_{k+1} − 5q_k → ∞ along K. Suppose den(Z̃_k) is unbounded on K. Then Z ∉ ℚ.

*Proof.* Suppose Z = A/B. By W3 and W4, N_k = B·D_k(Z − Z̃_k) ∈ ℤ and |N_k| ≤ 486B(1+o(1))2^{5q−Q} → 0. So N_k = 0 for large k ∈ K. Then Z̃_k = A/B, so den(Z̃_k) divides B, contradicting unboundedness. ∎

The hypothesis concerns only the explicit doubly periodic model arrays. Under the supply condition it is equivalent to the conclusion, so it is a reformulation, not a shortcut. What it gains is that it can be attacked by cyclotomic algebra on finite periodic data, with no reference to Z or to the state-eligibility tables.

*Sufficient condition:* some primitive prime divisor of 2^{3q_k}−1 or of 3^{3p_k}−1 survives in den(Z̃_k), since such primes tend to ∞.

### L4. Cost accounting

With error ≍ 2^{−(q+Q)} (W4), a model of denominator ≍ 2^{cq} gives D|Z−z| ≍ 2^{(c−1)q−Q}.

- **Forced value c = 6.** This gives 5q − Q, as in W4.
- **Ideal 2D value c = 2,** from periods (q,0),(0,p) costing ≍ 2^q·3^p. This gives q − Q ≤ −q_{k−1} → −∞ for every convergent. Irrationality would then follow from W4-type errors with no Diophantine hypothesis on log 2/log 3.

Any construction that recovers c ≤ 2, by avoiding the colour factor 3 while keeping the error, closes the problem modulo nonvanishing (L3).

## 3. Computations (reproducible; scripts in research_notes/Erdos 168 colour tripling barrier/)

| Check | Result |
|---|---|
| Reduced den of Z̃^± at 5/8, 12/19, 41/65, 53/84 (`modelval.py`) | 42–507 bits vs D 53–509 bits: no hidden gcd saving; all values reproduce Z = 1.2086917950590… |
| Full Φ_{3q}(2) and Φ_{3p}(3) dividing den, 110 nonresonant slopes q ≤ 74 (`c1test.py`) | Φ_{3p}(3): 110/110. Φ_{3q}(2): 108/110. Failures 11/17⁻ (missing prime 103) and 33/52⁻ (missing prime 1249) |
| Resonant reduced slopes 29/46, 7/11, 22/35 | Not periodic under (q,0), (0,p), (3q,0) or (0,3p) |
| Near-period scan (`per2.py`) | Longest agreements along 3(q,−p), reaching L ≈ Q+q; the (3q,0) agreement stops earlier (324 at q = 84) |
| CF of Z, certified from the 10^130 enclosure (`cfz.py`) | 127 terms, last convergent ≈ 10^64, max partial quotient 283, geometric mean 2.57 |
| Toy T₁ = Σ_b 3^{−b}2^{−⌊b log₂3⌋} (`toy.py`) | Partial quotients 876, 4.5·10⁶, 4.8·10²⁷, …, 2^{802}: single-index two-base Sturmian sums carry explosive structure |

## 4. Arguments tried and broken

1. **Strong cyclotomic divisibility.** "Φ_{3q}(2)Φ_{3p}(3) divides den(Z̃)" is false: 11/17 and 33/52 are counterexamples. Only the weak form is plausible.
2. **Resonant strip (Brion-type) identity.** Periodicity along r = 3(q,−p) gives the exact relation M(1−ρ³) = V − ρ³H + E, with ρ³ = 3^{3p}/2^{3q}. Here V and H are the strips a < 3q and b < 3p, and E is supported beyond the first r-defect, so E ≲ 2^{−(q+Q)}. The relation is correct, but the strips are infinite single-index sums. Approximating them reintroduces (3^{3p}−1)(2^{3q}−1), and the cost returns to 2^{6q}.
3. **Subspace theorem with S = {2,3,∞}.** S-unit factors are free only for transcendence-type gains. For irrationality the requirement stays |D(Z−z)| < H^{−ε}, which is the same 5q − Q condition.
4. **Eisenstein Liouville.** Split M into colour Fourier modes with complex denominators 2^q − ω^{∓1}, each of absolute value ≈ 2^q. Z is real, so both conjugate modes are needed, and the cost is the norm, ≈ 4^q per pair. That gives no gain.
5. **Discounted-cocycle rigidity on ×6 diagonals.** M = Σ_a 2^{−a}G_{a,0} + Σ_b 3^{−b}G_{0,b} with base-6 diagonal numbers G. For a single diagonal, rationality forces finitely many discounted transfer values on a dense rotation orbit, which jump-size arguments contradict. However, rationality of M does not isolate a diagonal: 2^i3^jM mod 1 carries uncontrolled off-quadrant terms.
6. **Semiconvergents inside a large resonant partial quotient.** They are all nonresonant, but cost 2^{6(q_{k−1}+jq_k)} against agreement ≈ q_{k+1}/(a−j). The ratio is never favourable, so large quotients at resonant indices are wasted.

## 5. Precise remaining gap

**Conditional theorem (proved above from W1–W5).** Suppose there is an infinite set K of nonresonant suitable convergents of log₃2 such that:

- **(G1)** q_{k+1} − 5q_k → ∞ along K; and
- **(G2)** den(Z̃_k) is unbounded along K, for which it suffices that a primitive prime divisor of 2^{3q_k}−1 survives.

Then c is irrational.

**Open.**
- (G1) is a Diophantine statement about log 2/log 3 at nonresonant indices. It does not follow from transcendence, and its badly-approximable status is unknown.
- (G2) is open, but finite and Z-free.

**Unconditional alternative (G′).** Build approximants with cost exponent ≤ 2 in units of q, defeating the colour tripling of L2, while keeping the error 2^{−(q+Q)}. L4 shows this alone would suffice.

Skipped: Lean, external review, novelty search beyond one web search (no published resolution found), and a proof of W4.
