# Erdős 168(ii): G2 is i.o. nonvanishing, transcendence upgrade, and why G1 is Diophantine

Date: 2026-11-08. Status: **Erdős 168(ii) is NOT proved here.** Labels: **[P]** proved from the
working inputs, **[C]** exact finite computation (reproducible scripts in this folder),
**[Conj]** conjecture. Working inputs used without re-proof: part (i) (finite formula, η rule,
Z = 9c−6 = 3−3M with the exceptional birth (0,1) and all low rows), the accepted complete
nonresonant model (two_sided_models_check.model), the accepted resonant cone model
(resonant_models.md R7–R11), the rectangle bound R13, SD2/SD3/SD5 nonvanishing, Lemma R2.

Notation: α = log2/log3 = [0;1,1,1,2,2,3,1,5,2,23,2,2,1,1,55,…], p_n/q_n convergents,
s_n = p_n+q_n mod 3, q = q_n, Q = q_{n+1}, z_n the correct-side complete model.

## 0. Side conventions (dependency check)

- `two_sided_models_check.model(p,q,sign)` and `fastmodel.model_value`: `side(n,p,q,+1)=⌊np/q⌋`,
  `side(n,p,q,−1)=⌈np/q⌉−1`. The correct side (limit from α) is **sign=+1 iff 2^q>3^p iff p/q<α
  (lower convergent)**. This is the selection used by the archived `returns_check.json`.
- `colour tripling barrier/model.py` orders ties by `sigma*b`; there the correct side is
  **sigma=+1 iff p/q is an upper approximant**. The two scripts use opposite sign names for the
  same correct side. No dependency error was found; the codex review's reading of the 11/17⁻ and
  33/52⁻ losses (wrong side for upper approximants) is confirmed by this dictionary.
- Exact check [C]: for 665/1054 the first floor disagreements with the true floors occur exactly
  at a = q+q' = 25781 and b = p+p' = 16266 (R = q+q', S = p+p' as in R13).

## 1. G2 is exactly infinitely-often nonvanishing [P]

**Lemma A.** Let K be infinite, z_n ∈ ℚ, and z_n → Z along K. The following are equivalent:
1. den(z_n) is unbounded on K (G2);
2. z_n ≠ Z for infinitely many n ∈ K;
3. (z_n)_{n∈K} is not eventually constant.

*Proof.* (1⇒3) An eventually constant sequence has eventually constant denominator.
(3⇒2) If z_n = Z for all large n ∈ K the sequence is eventually constant.
(2⇒1) If den(z_n) ≤ d on K then z_n ∈ (1/d!)ℤ, a discrete set; a convergent sequence in a
discrete set is eventually equal to its limit, so z_n = Z eventually, contradicting (2). ∎

The actual models converge: R13 gives |Z−z_n| ≤ 18·2^{−(q+Q)}. Hence:

- **A1.** G2 is not an arithmetic statement independent of nonvanishing: every proof of G2 is a
  proof of infinitely-often nonvanishing on K, and conversely. "A separate nonvanishing theorem is
  unnecessary" is true only in the sense that G2 *is* that theorem.
- **A2.** On every infinite K inside the proved eligible classes (balanced SD2, any resonant first
  mediant SD3/SD5) G2 already holds, by the uniform nonvanishing theorems. In particular, on the
  (L\*) family of supply_barrier.md, **G2 is proved; only G1 is missing.**
- **A3.** Surviving primitive primes are a sufficient condition for (2), never a necessary one.
  The data below (full Φ_{3q}(2)Φ_{3p}(3) survival with gcd(N,Φ)=1 at every computed actual
  nonresonant convergent) is consistent with survival, but survival is not structurally forced:
  the 110-slope survey losses (103, 1249) occur at the heuristic 1/ℓ rate, and the residue of N
  modulo a primitive ℓ is a primitive-frequency DFT of a cone-coded 2D array with no closed form.
  For the conditional finish the real-analytic nonvanishing route (A2) is strictly better.
- **A4 (finite form).** Nonvanishing at one index is certified by any later model:
  |z_n − z_m| > ε_n + ε_m ⇒ z_n ≠ Z. Section 3 does this for every computed index.

## 2. Transcendence upgrade via the p-adic Subspace Theorem [P]

**Lemma B.** If infinitely many actual nonresonant n have a_{n+1} ≥ 6, then Z (hence c) is not
an algebraic irrational. No nonvanishing hypothesis is needed for this half.

*Proof.* Put x = (27·2^{3q}3^{3p}, 27·2^{3q}, 27·3^{3p}, 27, N_n) ∈ ℤ⁵, so
D_n = x₁−x₂−x₃+x₄. Suppose Z is algebraic irrational. Take S = {∞,2,3}; at ∞ the forms
L₀ = Z(x₁−x₂−x₃+x₄) − x₅, x₁,…,x₄; at 2 and 3 the coordinate forms. They are independent at
each place and have algebraic coefficients. The first four coordinates are S-units, whose
S-norm is 1, and |N|₂|N|₃ ≤ 1. Hence
  ∏_v ∏_i |L_{v,i}(x)|_v ≤ |D_nZ − N_n| ≤ 18·D_n·2^{−(q+Q)}.
Also gcd(x) | 27, and H(x) ≍ D_n = 2^{6q+O(1)} because 3^p/2^q → 1. If a_{n+1} ≥ 6 then
Q ≥ 6q+q_{n−1}, so the product is < H(x)^{−1/7} for large n. Schlickewei's p-adic Subspace
Theorem puts infinitely many x in one proper subspace Σc_ix_i = 0, c ∈ ℚ⁵∖{0}.
- If c₅ ≠ 0, then z_n = N_n/D_n → −c₁/c₅, so Z ∈ ℚ, a contradiction.
- If c₅ = 0, divide by 2^{3q}3^{3p}: c₁ = 0. Then c₂2^{3q} + c₃3^{3p} + c₄ = 0. Since
  3^{3p}/2^{3q} → 1 we get c₂ = −c₃, and then c₂(2^{3q}−3^{3p}) = −c₄ with |2^{3q}−3^{3p}| → ∞.
  So c = 0, a contradiction. ∎

**Corollary B1.** Under (L\*) with digit threshold 6 instead of 5, c is transcendental.
If the (L\*) digits are unbounded, Z has irrationality exponent ∞ (Z is a Liouville number).
Equivalently: c is rational or transcendental unless the nonresonant partial quotients of α are
eventually ≤ 5. The same argument at resonant indices needs only (1+δ)·log₂D_* < (error
exponent), because D_* = 2^{v₂}3^{v₃}(W−1) is a two-term S-unit sum.

## 3. Transcendence alone cannot supply any nonresonant digit ≥ 2 [P]

**Lemma C.** Let n be resonant (s_n = 0). The digit block (A, 1, 1, 1), with A ≥ 1 placed at the
resonant index, returns the system to a resonant index four steps later. All three intermediate
indices are nonresonant and carry next digit 1.

*Proof.* With s_n = 0: s_{n+1} = A·0 + s_{n−1} = u ≠ 0, s_{n+2} = u + 0 = u, s_{n+3} = 2u,
s_{n+4} = 2u + u = 0. ∎

The actual index n = 9 (665/1054) is resonant with s_8 = 2. So every tail
(A₁,1,1,1,A₂,1,1,1,…) after the actual prefix [0;1,1,1,2,2,3,1,5,2] keeps all nonresonant
digits equal to 1, while the resonant digits A_k are arbitrary. Take A_k ∈ {2,3} independent and
uniform. The SD8 mass-distribution argument then gives transcendental slopes of this form with
finite algebraic approximation exponents in every degree. So the converse barrier of B3 is
sharper than recorded: transcendence and approximation measures cannot even give infinitely many
*nonresonant* digits ≥ 2. Any digit-free route must clear the **resonant** indices. This is where
the actual large digits 23 and 55 sit (Section 4).

## 4. The exact remaining lemma

With Lemma A, the conditional finish needs **only**:

**(L\*)** infinitely many n with a_{n+1} ≥ 5 and t_{n+1} = 2 (resonant first mediant). Or its
balanced variant (L_bal), or any other proved-nonvanishing state class.

(L\*) ⇒ (D5): α has infinitely many partial quotients ≥ 5. We know no proof of (D5). Baker and
Matveev bounds give only upper bounds a_{n+1} ≤ Cq_n^K. Gelfond–Schneider gives only
non-periodicity. Markov–Lagrange theory gives L(α) ≥ 3, which digits ≤ 2 already realise.
Lemma C shows this information cannot even reach nonresonant digit 2. A focused literature search
(2026-11-08) found no theorem on large partial quotients of log2/log3. Spiegelhofer (2022)
records that boundedness is unknown.

G1 is therefore a statement about the specific Gauss-map orbit of α lifted to the level-3
cover. No currently available method controls that orbit. This note does not claim it.

## 5. Finite certificates on the actual family [C]

Scripts: fastmodel.py, actual_models.py, resmodel.py, res1054.py, certify.py, firstdiff.py,
firstdiff_nr.py, kappa_min.py, zcf.py. Outputs: actual_models_out.txt, certify_out.txt,
nonvanish_out.txt. Only exact rational and integer arithmetic is used (Python 3.14 standard
library; sympy only for divisor lists).

**5.1 Fast exact evaluator.** The tile is a finite bilinear form in occupation integers: cells
are grouped by (A_a, a mod 3) and (B_b − event_b, b mod 3), and the cone test depends only on the
pair of keys. The evaluator agrees exactly with the accepted two_sided_models_check.model on 5/8,
12/19, 41/65, 53/84 and 11/17, on both sides. Run time is 2 s at q=24727 and 286 s at q=176251.
The resonant evaluator reproduces the archived 7/11 and 8/13 reduced denominators exactly and
passes brute-force tail checks at 7/11, 8/13, 22/35 and 29/46.

**5.2 Reduced denominators and cyclotomic survival.** These are all actual nonresonant
convergents with 8 ≤ q ≤ 176251, on the correct side:

| n | p/q | a_{n+1} | side | den bits / D bits | Φ_{3q}(2) ∣ den | Φ_{3p}(3) ∣ den | gcd(N,Φ_{3q}(2)), gcd(N,Φ_{3p}(3)) |
|---|---|---|---|---|---|---|---|
| 4 | 5/8 | 2 | lower | 44/53 | yes | yes | 1, 1 |
| 5 | 12/19 | 3 | upper | 108/119 | yes | yes | 1, 1 |
| 6 | 41/65 | 1 | lower | 393/395 | yes | yes | 1, 1 |
| 7 | 53/84 | 5 | upper | 507/509 | yes | yes | 1, 1 |
| 8 | 306/485 | 2 | lower | 2908/2915 | yes | yes | 1, 1 |
| 10 | 15601/24727 | 2 | lower | 148363/148367 | yes | yes | 1, 1 |
| 11 | 31867/50508 | 2 | upper | 303048/303053 | yes | yes | 1, 1 |
| 12 | 79335/125743 | 1 | lower | 754461/754463 | yes | yes | 1, 1 |
| 13 | 111202/176251 | 1 | upper | 1057509/1057511 | yes | yes | 1, 1 |

On the actual, correctly oriented family, none of these nine cases shows primitive cyclotomic
cancellation. The survey losses 11/17⁻ and 33/52⁻ do not recur. This is finite evidence, not a
theorem.

**5.3 Nonvanishing at every computed index.** Write ε_n = 9(2^{−R}+3^{−S}−2^{−R}3^{−S}).
The best model (n=12) has ε ≈ 2^{−301990.8}. Every other computed model, including the resonant
one, satisfies |z_n − z_12| > ε_12, so **z_n ≠ Z for n = 4,…,11**. The n=12 model is certified
by n=13: |z_12 − z_13| = 2^{−302018.25} > ε_13. Effective error exponents
W_eff = −log₂|Z − z_n|:

| p/q | q+Q (window) | W_eff | W_eff − log₂den(z_n) |
|---|---|---|---|
| 53/84 | 569 | 578.33 | **+71.3** |
| 306/485 | 1539 | 1548.90 | −1359 |
| 665/1054 (resonant) | 25781 | **63973.13** | **+45789.1** |
| 15601/24727 | 75235 | 75252.35 | −73111 |
| 31867/50508 | 176251 | **212338.04** | −90710 |

Normalised first-order errors (z_{n'}−z_n)2^{q+Q} are 0.042, 0.0022, −0.0073, −0.00155,
0.00105, 6.0·10⁻⁶ and −5.0·10⁻⁸. These are consistent with the predicted size
(2^{−s}−3^{−r})Γ ≈ 2^{−(q+Q)}Γ/Q. The exception is n = 11, where the first-order term
vanishes; see 5.6.

**5.4 Certified continued fraction of Z, and a giant partial quotient.** The n=12 model gives
Z ∈ [z_12 − ε, z_12 + ε] with ε < 2^{−301990}. The two endpoints share **71,933** CF terms;
the last convergent has a 150,991-bit denominator. Term a_{10707} has **27,607 bits**. The
convergent just before it, [CF(z̃) prefix…, 4, 1], is exactly the resonant model
z̃(665/1054), whose denominator has 18184 bits. All other terms are tiny: the next largest have
21, 18 and 18 bits. Excluding a_{10707}, the geometric mean is ≈ 2.68, Khinchin-like.

So **α's resonant digit a_{10}=23 produces, through the complete resonant model, a
2^{27607}-size partial quotient of Z**. This is a certified, explicit Liouville-type spike. It
agrees with Lemma B and Corollary B1: Z looks generic except at scales where α has a large
digit that some complete model can exploit.

**5.5 Denominator exclusion.**
- From the Z enclosure and its common CF prefix (cylinders are intervals):
  **den(Z) ≥ 2^{150990}**, hence den(c) ≥ 2^{150986}. The archived bound was 2^{56}.
- From two models only: z̃(665/1054) ≠ Z and |Z − z̃| ≤ 2^{−63973}, so den(Z) ≥ 2^{45789}.
  This bound does not depend on precision. It is a denominator-growth event on the actual
  family.

**5.6 Effective windows and the deep-state mechanism.** The first true digit disagreements are
located by grouping cells into state-pair classes:
- n=10: the classical mediant pair at the window edge, (75235,1) and (0,47469), both of weight
  2^{−75236.58}. They nearly cancel, leaving 2^{−75252}.
- n=11: no digit changes at the window. The first true disagreement is at **(212202, 78)**, of
  weight 2^{−212325.6}; the first low-row disagreement is at (217472, 2).
- 665/1054 (resonant): the floors disagree from a = 25781, but the first true digit
  disagreement is at **(63840, 78)**, of weight 2^{−63963.6}.

Mechanism: when the state at the floor-disagreement position lies deep inside one cone region,
the perturbed true state stays in the same region. Digits flip only after an excursion of the
true walk. At resonance this is systematic, because over the window the model state drifts
linearly by about a_{n+1}/3 units of d_A.

**[Conj R-EW]** At resonant currents, W_eff ≥ (1+θ)(q+Q) for a fixed θ > 0. Together with a
uniform O(q) resonant S-cost, resonant indices would then certify from a fixed resonant digit
threshold. The data at 665/1054 gives θ ≈ 1.48 and log₂D_* ≈ 17.25q. This trades G1 for
another digit condition; it does not remove it.

**5.7 No-go for cheap families (κ_min).** κ_min(n) is the least log₂den/q of any rational y ≠ Z
with |Z−y| ≤ 2^{−(q+Q)+slack}. It follows from the certified CF via Legendre's theorem and the
convergent error bounds. At 53/84 (a_{n+1}=5):
- κ_min = 3.372 (slack 0), 3.262 (slack 20) and 3.009 (slack 60).
- So the "ideal" κ=2 family (L4) is impossible at this actual index.
- The κ=3 digit-free exit (B3/L_κ) is also impossible there with any error constant ≤ 2^{60}.

B3 allows o(q_{n−1}) = o(65) slack, so this refutes B3 quantitatively at the one testable
index, not as an asymptotic statement. At the digit-2 indices κ_min ≈ 1.5–1.75, which is
generic behaviour. A cheap family must therefore adapt its cost to the next digit: a uniform
κ < (a_{n+1}+1)/2 forces large partial quotients of Z.

## 6. Arguments tried and broken here

1. **S-adic product formula, to relax G1 (from Q−5q → ∞ to 3Q > 5q).** The models z_n do have
   2-adic and 3-adic meaning: periodic sums reflect to negative indices, whose digits stabilise
   inside the agreement window. The cleared integers x_n = B(N_n − D_nZ) would be divisible by
   large powers of 2 and 3 if z_n → A/B in ℚ₂ and ℚ₃. The obstruction is identification: nothing
   forces the 2-adic limit to equal the real limit A/B. If they differ, |x_n|₂ is bounded below
   and nothing is gained. Combining consecutive models removes A/B, but then the statement
   concerns explicit rationals only. **Broken.**
2. **Primitive-prime survival as the route to G2.** By Lemma A it is unnecessary. It is also not
   structurally forced: N mod ℓ is a primitive-frequency DFT of a cone-coded walk array. That DFT
   has a closed form for Christoffel words, but not for cone codings of cumulative walks.
   **Abandoned in favour of A2.**
3. **Sheared period lattices**, for example (q,p) together with (3q,0). Quadrant generating
   functions carry denominators from the minimal axis periods Λ∩(ℤ×0) and Λ∩(0×ℤ), which are
   again 3q and 3p. **No cost reduction.**
4. **Lifting to the colour-trivial rotation γ = log6/log8.** The colour sums are Birkhoff sums
   of ω^{⌊3u⌋} under rotation by γ. The lift absorbs the tripling into the denominators of γ,
   but the agreement windows are still set by α. The requirement becomes "lifted digit ≥ 2" at
   lifted indices corresponding to nonresonant α-indices, which is the same supply problem.
   **No gain.**
5. **Semiconvergents inside a large resonant digit.** They are all nonresonant, but they cost
   6(kq+h) against a window of (k+1)q+h. **Confirms B4.**
6. **Digit-free κ≤3 (B3).** Refuted with explicit constants at 53/84 (5.7). By Lemma C it would
   need resonant-index models anyway.

## 7. Exact status

- **Proved:** Lemma A (G2 ⟺ infinitely-often nonvanishing), Lemma B (transcendence upgrade
  under infinitely many nonresonant digits ≥ 6), Lemma C (transcendence cannot give nonresonant
  digits ≥ 2).
- **Certified:** nonvanishing at all actual indices with q ≤ 125743; full cyclotomic survival
  at nine actual nonresonant convergents; den(c) ≥ 2^{150986}; a 27607-bit partial quotient of
  Z, explained by the resonant model; κ_min at 53/84.
- **Remaining lemma (unchanged in substance, now sharp):** (L\*), or any infinite state class
  with proved nonvanishing and a_{n+1} ≥ 5. By Lemma A this is exactly G1 on such a class. It
  implies (D5) for log2/log3, which is open. Resonant classes can be added by proving
  [Conj R-EW] together with a uniform resonant S-cost bound, but a digit condition remains.

Skipped:
- Lean.
- A proof of [Conj R-EW].
- The resonant model at 190537/301994 (a=55). It needs a subquadratic base-3 conversion, and
  without a model at q≈1.7·10⁷ it gives no nonvanishing certificate.
- External review.
