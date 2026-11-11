# Erdős 168(ii): exact form of the scalar supply requirement, and why it is a Diophantine barrier

Date: 2026-11-08. Status: **the missing joint supply theorem is NOT proved here.** This note (i) proves an exact recurrence and initial state, (ii) proves that the resonant half of eligibility is a pure mod-3 residue condition, so the transforms drop out of that branch, (iii) proves that the supply theorem implies a partial-quotient statement about log2/log3 for which no proof is known, and (iv) proves an unconditional "transcendence threshold" lemma that identifies a cheaper model family as the only digit-free exit. Computations are labelled **[C]**, proofs **[P]**, and conjectures **[Conj]**.

Notation: α = log2/log3 = [0;1,1,1,2,2,3,1,5,2,23,…], convergents p_n/q_n, digits a_n, and
s_n = p_n + q_n mod 3, so s_{n+1} = a_{n+1}s_n + s_{n−1}.
Throughout, p/q = p_n/q_n is the current convergent, P/Q = p_{n+1}/q_{n+1} is the successor, and r/s = (p+P)/(q+Q) is the first mediant.

## 1. The exact Christoffel/Eisenstein recurrence [P]

Put H(r,s) = Σ_{j<s} ω^{j+⌊rj/s⌋}.

**Lemma R1.** Let p/q < p'/q' be Farey neighbours (p'q − pq' = 1) and r/s = (p+p')/(q+q'). Then
H(r,s) = H(p,q) + ω^{p+q} H(p',q').
The LOWER word comes first.

*Proof.* For 0 ≤ j < q, an integer in (pj/q, rj/s] would give a fraction m/j ∈ (p/q, r/s] with j < q < s. No such fraction exists between Farey neighbours, so ⌊rj/s⌋ = ⌊pj/q⌋.

For j = q+i with 0 ≤ i < q', we have rq − ps = 1 and rq' − p's = −1. Hence
r(q+i)/s − p = p'i/q' + (q'−i)/(sq').
Any integer m > p'i/q' satisfies m − p'i/q' ≥ 1/q' > (q'−i)/(sq'). Therefore ⌊r(q+i)/s⌋ = p + ⌊p'i/q'⌋. The exponent becomes (p+q) + i + ⌊p'i/q'⌋, and summing proves the lemma. ∎

**Initial state.** Start from the Farey neighbours 0/1 < 1/1, with H(0,1) = H(1,1) = 1 and multiplier exponents 1 and 2 (mod 3). Descend the Stern–Brocot tree using the exact test r/s < α ⟺ 3^r < 2^s. Every intermediate fraction, every convergent and every first mediant (p_n+p_{n+1})/(q_n+q_{n+1}) lies on this path: the mediant is the first intermediate fraction toward p_{n+2}. The state (lower, upper, both transforms, parity of the current endpoint) therefore evolves exactly by Lemma R1, including through resonant intermediate fractions. No state information is discarded.

[C] Lemma R1 was also checked against direct sums on all 947 neighbour pairs with q, q' < 40, and on the first 400 actual path fractions with s < 3000. It agrees with the archived H(UV) = H_U + xH_V. The sides of the first 14 convergents were checked exactly by comparing 3^r with 2^s.

## 2. The resonant branch of eligibility is a residue condition [P]

**Lemma R2.** For every sufficiently late n, the following are equivalent:
1. n is eligible through the resonant mediant states (1,2,1+ω) or (2,1,1), with a nonresonant current.
2. s_n + s_{n+1} ≡ 0 (mod 3).
3. t_{n+1} = 2, where t_k := s_{k−1}/s_k ∈ P¹(F₃).

In (3), the residues evolve by the Möbius map t_{k+1} = 1/(a_{k+1} + t_k) on the four-point projective line. Equivalently, s_n ≢ 0 and a_{n+1} ≡ −1 − t_n (mod 3).

*Proof.* The mediant multiplier is ω^{r+s} = ω^{s_n+s_{n+1}}, so a resonant mediant means (2). SD3 (state_supply.md, re-audited in supply_audit.md) shows two things for every one of the 24 reachable neighbouring states. If the mediant is resonant, both parents are nonresonant. And the mediant transform is −xC/(1−x), so its full state is one of the two listed in S. This needs no bound on the parent transforms. Hence (1) ⟺ (2).

s_n and s_{n+1} cannot both vanish: they are the values of the nonzero functional (p,q) ↦ p+q on a basis of F₃². So (2) means s_n ≠ 0 and s_{n+1} = −s_n, which is t_{n+1} = 2. Expanding s_{n+1} gives the last form. ∎

**Corollary R3 (sufficient lemma with no transforms).** The scalar route closes, using the proved uniform resonant nonvanishing SD5 and the accepted clearing, if

  **(L\*)** there are infinitely many n with a_{n+1} ≥ 5 and t_{n+1} = 2, i.e. a_{n+1} ≡ −1 − t_n (mod 3).

The same index n carries the nonresonant current model (clearing D_n), the resonant mediant (nonvanishing), and the digit (Q − 5q ≥ q_{n−1} → ∞). So supply, nonvanishing and clearing all hold on ONE sequence.

[C] On all 589 actual indices 3 ≤ n ≤ 591, criterion (3) reproduces resonant-branch eligibility with 0 mismatches. These are 595 digits that agree at 4000 and 4400 working digits; that is a two-precision check, not interval arithmetic. Of these indices, 159 are eligible: 153 resonant and 6 balanced (n = 4, 5, 7, 8, 106, 179). There are 168 indices with a_{n+1} ≥ 5. **39 indices satisfy the joint condition: 38 through (L\*) and one balanced (n = 7, a_8 = 5).** The last one found is n = 591, with a = 7. The balanced branch dies out numerically because the transforms grow (most mediant transforms have norm ≥ 6). This is finite evidence only.

## 3. Why the requested theorem is a Diophantine barrier [P]

**B1. The supply theorem implies the digit statement.** The requested joint statement implies

  **(D5)** log2/log3 has infinitely many partial quotients ≥ 5.

The implication is trivial. No proof of (D5) is known to us.

- Baker/Matveev-type bounds give only upper bounds, a_{n+1} ≤ C q_n^K.
- Transcendence of α (Gelfond–Schneider) excludes only eventually periodic continued fractions.
- Uncountably many digit sequences in {1,2,3,4}^ℕ give transcendental numbers, so no argument that uses only "α is transcendental, with a finite irrationality measure" can give (D5). SD8 strengthens this to finite algebraic approximation exponents in every degree.
- Spiegelhofer (arXiv:2105.11173v2, 2022) records that even boundedness of the partial quotients of log3/log2 is unknown. Our searches found no later result. We do not claim a definitive literature status for (D5).

Consequently, proving the requested theorem would also settle (D5), which current techniques do not reach. We did not prove it.

**B2. Digit supply is not enough even through the resonant branch.** Tails with t_n ≡ 1 and every digit a ≡ 0 (mod 3) keep t ≡ 1: indeed 1/(a+1) = 1. Such a tail never has t_{n+1} = 2, and it never has a resonant current. Its digits can be arbitrarily large, and it can be non-periodic. So even unbounded partial quotients would not give (L\*). On such tails, every eligible index must come from the balanced branch, which depends on the unbounded transforms. This is the precise obstruction Step 4 of the brief asks about: the uncovered states are the nonresonant mediants whose current fibre has t = 1 and s constant. No nonvanishing theorem for them is available.

**B3. Transcendence threshold (unconditional lemma).** Suppose, at every sufficiently late index n with a_{n+1} ≥ 2 (in ALL residue/transform states), there are complete rational models y_n and integers d_n with
d_n y_n ∈ ℤ, log₂ d_n ≤ 3q_n + o(q_{n−1}), |Z − y_n| ≤ 2^{−(q_n+q_{n+1}) + o(q_{n−1})}, and y_n ≠ Z.
Then Z, and hence c, is irrational, with no Diophantine input beyond Gelfond–Schneider.

*Proof.* α is transcendental, so its continued fraction is not eventually all 1s. Hence infinitely many n have a_{n+1} ≥ 2. For these n,
q_{n+1} − 2q_n = (a_{n+1} − 2)q_n + q_{n−1} ≥ q_{n−1},
so log₂(d_n|Z − y_n|) ≤ −q_{n−1} + o(q_{n−1}) → −∞. If Z = A/B, then B d_n(Z − y_n) is a nonzero integer tending to 0, which is a contradiction. ∎

**Converse barrier.** For a clearing exponent κ ≥ 4, transcendence alone cannot supply the indices. Non-periodic tails over {1,2} have q_{n+1}/q_n < 3 for every late n, and uncountably many of them are transcendental. The existing nonresonant models have κ = 6. The idealized resonant diagonal models have κ = 3 nominally, but their 2,3-power costs are uncontrolled (resonant_models.md, R10–R11), and B2-type tails avoid resonant currents anyway.

**B4. Intermediate fractions cannot meet the threshold.** Take a model of cost 3·den at an intermediate fraction F_k = (kp_n + p_{n−1})/(kq_n + q_{n−1}). Its first crossed jump is at F_{k+1}, so the gain exponent is (k+1)q + h − 3(kq + h) = (1 − 2k)q − 2h < 0. Current-side fan members are worse. The threshold can only be met at convergents.

## 3b. Correction to B2, and a stronger avoidance phenomenon [C, with one proved step]

**B2 needs a correction: the balanced branch can rescue the t ≡ 1 tails.** With a nonresonant current, write x = ω^{s_n} ≠ 1. The intermediate words toward p_{n+1} append a_{n+1} copies of the current word. By Lemma R1 the transform therefore changes affinely, with period 3 in the number of copies, because 1 + x + x² = 0. **[P]** So a_{n+1} ≡ 0 (mod 3) returns H(p_{n+1}) to H(p_{n−1}), and the mediant state depends only on the state at n and on a_{n+1} mod 3.

On a t ≡ 1 fibre with every digit ≡ 0 (mod 3), the full state is therefore frozen. Starting from the actual t = 1 state reached at n = 8, five random tails with digits in {3,6,9} put **every** index in the balanced state (2,2,2). That gives 22–33 joint visits per tail. **[C]** So B2 is a correct statement about the resonant branch only. It does not produce tails that avoid the full joint condition from that start. Other t = 1 starting states were not enumerated.

**B5. Avoidance with large digits only. [C]** Here eligibility at n depends only on (state at n, a_{n+1} mod 3), with the eligible residues in a set E(state). Along the actual prefix n < 120, |E| takes the values 0, 1, 2, 3 at 27, 82, 3 and 5 indices respectively; |E| = 0 occurs exactly at resonant currents. A greedy tail did the following: append a digit from {5,6,7} whose residue lies outside E, or the digit 4 if no such digit exists. After the actual 41-digit prefix it produced 40 further digits, 39 of them ≥ 5 and one equal to 4, with **no joint visit**. The tail visited mediant transforms of norm up to 676, and 13 resonant currents.

So, abstractly, even "all late digits ≥ 5" does not imply joint supply with the present eligibility classes. Joint supply is genuinely stronger than (D5). It needs residue-level information about the digits of log2/log3, or a larger nonvanishing class covering nonresonant mediants with unbounded transforms, and a clearing theorem for resonant currents. This is a finite-depth abstract construction, not a proof that an infinite avoiding tail exists; extending it indefinitely is **[Conj]**, but the greedy step never failed in 180 steps from three starts.

## 4. What remains, stated exactly

One of the following lemmas would finish the original scalar route. All other ingredients are the accepted inputs: SD3, SD5, the clearing D_n and the error bound 486(1+o(1))2^{5q−Q}.

- **(L\*)** infinitely many n with a_{n+1} ≥ 5 and t_{n+1} = 2. **[Conj, consistent with the data in §2.]** It implies (D5).
- **(L_bal)** infinitely many n with a_{n+1} ≥ 5, a nonresonant current, and a first-mediant state in the balanced set 𝓑 with actual transforms. This also implies (D5).
- **(L_κ)** digit-free alternative: complete models with κ ≤ 3, as in B3, together with nonvanishing at all late indices with a_{n+1} ≥ 2. This avoids (D5) entirely but needs a new construction. The nonresonant tripling comes from the affine rotation ω^{p+q}, which has period 3. That is why the existing family has κ = 6, and not a removable artifact.

Geometric reading (interpretation, not used in the proofs): (t_n) is the Gauss-map orbit of α lifted to the PGL₂(F₃) skew product, i.e. the level-3 coding of the geodesic ray of α. (L\*) asks for infinitely many cusp excursions of depth ≥ 5 that land on one prescribed point of the level-3 fibre. Ergodic theory gives this for almost every slope, but not for the specific slope log2/log3.

## 5. Audit of quantifiers and dependencies

- "Sufficiently late" in SD5 is uniform over the resonant class, so any infinite set of (L\*) indices has an infinite late tail.
- Correct-side convention: the current model is approached from α's side, matching the clearing and error statements. Lemma R2 does not depend on parity.
- Normalisation check: c = 1 − M/3 gives 9c − 6 = 3 − 3M = Z, consistent with Σ 2^{−a}3^{−b} = 3. The exceptional birth (0,1) and the low rows sit inside the accepted complete models and are untouched here.
- No dependency errors were found in the parts used (SD1, SD3, SD5, the clearing). Part (i) is used as an accepted input, without re-audit.

Files: `rec.py` (Lemma R1 check), `actual.py` (digits and path transforms), `elig.py` (eligibility classification), `resid.py` (Lemma R2 versus the data). Run `python actual.py`, then `python elig.py`, then `python resid.py` in this folder; `actual.py` needs mpmath 1.3 and takes several minutes.

Skipped: interval-certified digits beyond the exact first 14 convergents, Lean, external review. Main risk: (L\*) and (D5) are unproved. This note shows that the original scalar route cannot be finished without new Diophantine information about log2/log3, or without a new κ ≤ 3 model family.
