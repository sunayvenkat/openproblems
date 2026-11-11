# Erdős #168(i): the finite optimum, its increments, and the constant

Date: 2026-11-08. Scope: part (i) only. No Lean. No irrationality claim.

## 0. Verdict

1. **Formula (C) is correct.** For every real t ≥ 3,

   τ(t) = min_j [K_j(t) − I_j(t) − P_j(t)].

   **A complete self-contained proof is in [PROOF.md](PROOF.md).** It is written out in full with every lemma and cites no other note: §2 reduction, §3 construction, §5 axis-avoiding classification, §6 vertical-axis analysis with prefix augmentations, §7 assembly, §8–9 the only finite tables. §3 below is a compressed outline of the same chain. I also checked it against an independent exact solver: a column-transfer dynamic program, itself brute-force-checked. It agrees at all 411 smooth cutoffs up to 3·10¹⁰ and at the non-smooth breakpoint t = 27/2. The supporting lemmas (4) and (8) were also probed directly, with zero violations up to 3·10⁶.
2. **Every increment η_{a,b} has an explicit rule (§4).** η = 1 exactly when every minimising colour of the adjusted count vector Q(d⁻) is one of the colours incremented at d. The incremented colours are given by a five-line table in (a, b). In particular η = 0 at every power of two.
3. **Determination of c (§5).**

   c = 1 − (1/3) Σ η_{a,b} 2^{−a}3^{−b} = 1 − (1/3) ∫₁^∞ τ(t) t^{−2} dt.

   The constant splits into a rational main term and a geometric remainder:

   **c = 757/972 + (2/9) ∫₃^∞ H(Ŝ(t)) t^{−2} dt.**

   Here Ŝ(t) ∈ ℤ[ω] is an Eisenstein-integer walk driven by the rotation by log₂6. H is the gauge whose unit ball is an equilateral triangle.
4. **Rigorous enclosure (§6).**

   c = 0.80096575500655898909042032638808241322472498911028458781919045603644708044249630021895087751711467131844149435653902330834474 …

   This is a certified interval of width 1.3·10⁻¹²⁸. It takes 1.3 s and uses exact integer arithmetic. It agrees with Eberhard's integer-programming value (OEIS A386439, 35 digits) and extends it.
5. **New structural observation (computational, §7).** (C) is not really arithmetic. In row form it holds for every staircase whose row-gap word avoids `11` and `222` and whose top row has width ≤ 2. This was checked exhaustively on 2886 such shapes. It fails without either condition.

**Status of the determination of c.** The proof of (C) in PROOF.md is self-contained. The determination of c in §5 uses only (C) and the component reduction, both proved here. So, modulo the reader checking PROOF.md §11 items 1–7, part (i) is settled: c = 1 − (1/3) Σ η_{a,b}/(2^a3^b), with η_{a,b} given by the explicit rule in §4.

There is no remaining combinatorial theorem. An independent fresh-context referee re-derived every lemma (verdict: all PASS, no gap; see audit/AUDIT.md). Not done: external human review and Lean. Irrationality (ii) is untouched.

---

## 1. Setup and reductions

Write n = m·2^a3^b with gcd(m, 6) = 1. A triple {n, 2n, 3n} stays inside one component m·D_{N/m}, where D_t = {2^a3^b ≤ t}. Hence, **exactly**,

  N = Σ_{m≤N, (m,6)=1} |D_{N/m}|,  F(N) = N − Σ_{m≤N, (m,6)=1} τ(N/m).  (1.1)

In exponent coordinates a corner is {(a,b), (a+1,b), (a,b+1)}. Row b has width w_b = ⌊log₂(t/3^b)⌋ + 1. The gaps w_b − w_{b+1} lie in {1, 2}, and the gap word never contains `11` or `222`, since 2·log₂3 > 3 and 3·log₂3 < 5. The top row has width 1 or 2.

**Colours.** Colour (a,b) by a − b mod 3, and let C_j be colour class j with K_j = |C_j|. Every corner has one point of each colour, so each C_j is a cover.

**Matching identity.** Fix a colour j and a set U ⊂ C_j. Let B(U) be the bipartite graph, on colours j+1 and j+2, made of the opposite pairs of corners whose colour-j point lies in U. An owner u = 2^a3^b has up to three edges:

- N(u) = (u/3, 2u/3), present if b ≥ 1;
- E(u) = (3u/2, u/2), present if a ≥ 1 and 3u/2 ≤ t;
- R(u) = (2u, 3u), present if 3u ≤ t.

A vertex l on the left side can only be owned by l/2, 2l/3 or 3l. A vertex r on the right side can only be owned by r/3, 3r/2 or 2r.

Every cover has the form (C_j∖U) ∪ W, where W covers B(U). König's theorem then gives, for every j,

  D_j := max_{U⊂C_j} (|U| − ν(B(U))) = K_j − τ.  (1.2)

## 2. Upper bound: the construction

- **Isolate.** Suppose e = 2^A with A ≥ 1 and 2t/3 < e ≤ t. Then e lies in no corner and can be dropped from C_{A mod 3}.
- **Patch.** Suppose e = 2^A with A ≥ 2 and 6e ≤ t < 27e/4. The owners {e, 9e/2, 6e} have exactly four edges: (3e/2, e/2), (2e, 3e), (3e/2, 3e) and (2e, 4e). The two points {3e/2, 2e} cover all four, so swapping three points for two saves one.

  The formula's A = 1 window is [12, 27/2). It never changes the minimum: K = (3, 3, 2) there. It can therefore be dropped; this convention is used in §4. All five computational checks agree with (C) under either convention.

- **At most one exceptional root exists overall.** Each window has multiplicative width < 2. A patch forces the largest dyadic point to be 4e ≤ 2t/3, which kills any isolate.

Hence τ ≤ M := min_j Q_j, where Q_j = K_j − I_j − P_j.

## 3. Lower bound: outline (full proof in PROOF.md)

The argument is the one in the ErdosGPT notes. These are `multiroot.md`, `prefix_audit.md`, `vertical_audit_and_transfer.md` and `deep_branch.md`, consolidated in `reports/Erdos 168 prefix and phase audit.md`. I re-derived every step below. Where I checked a detail that is easy to get wrong, I say so.

**L1. Essentiality and expansion.** Take a pool P, let D* = max_{U⊂P} d(U) > 0, let U be an inclusion-minimal maximiser, and let W be a minimum cover of B(U). Then:

- each w ∈ W uniquely covers edges of at least two owners;
- for every nonempty S ⊂ W, the set T(S) of owners of all edges at S satisfies |T(S)| ≥ |S| + 1.

Proof: otherwise U∖T(S) has deficiency ≥ D*, contradicting maximality or minimality. The case T = U uses |U| = |W| + D* directly. Leaves are never in W. ✔

**L2. Axis-avoiding classification.** Let U ⊂ C_j be critical with every a ≥ 1. Then U is either an isolate {x}, or a patch {x, 9x/2, 6x} with x = 2^A, A ≥ 2, in the window above.

Re-derivation:

1. *Predecessor lemma.* If a, b ≥ 1, at least one of u/6, 2u/9, 3u/4 lies in U. Otherwise follow the leaf chain u/3 → 2u/3 → E(4u/3) → 2u ≤ t → E(u) → u/2 → 3u/2 → N(9u/2). This leaves R(u) uncovered.
2. *Cone.* Consequently U ⊂ x⟨g, q⟩ with g = 4/3, q = 9/2 and x = 2^A the least root.
3. *Chain.* The chain u_n = xq^n is forced up to the first index k with u_k > 2t/3.
4. *Columns.* Then v = gu, w = g²u and z = g³u are forced in turn. The two backward essentiality inductions start from the caps w_k > 32t/27 and γ_k = 3w_{k−1}, a leaf.
5. *Count.* This gives 4k − 2 selected vertices against at most (k+1) + k + (k−1) + (k−2) owners. That is impossible for k ≥ 2.

I checked the following details:

- every owner list, including v₀ = 4x/3 and z₁ = 32x/3 being nonsmooth;
- the availability bounds w_{k−1} ≤ 8t/27 < t/3 and v_n ≤ 2t/9;
- distinctness of the selected vertices via their g-coordinates −1, 0, 1, 2;
- that {x, 9x/2, 6x} really is critical: all proper subsets have deficiency 0.

Consequence (4): ν(B(V)) ≥ |V| for every V ⊂ A_j avoiding a = 0, where A_j is C_j minus the exceptional root. ✔

**L3. General restricted maximiser, two cones, root balance.** Disjoint N-edges force a horizontal owner, and (4) forces a vertical one. Then U ⊂ x⟨g,q⟩ ∪ y⟨g,q⟩, with x = 2^A and y = 3^B. Same-colour axis roots differ by 8 = g²q or 27 = gq².

- A > 2B is impossible: the g-chain from y reaches 2^{2B} < x.
- B > 2A is impossible: the q-chain from x reaches 3^{2A} < y, with E available since u_n ≤ 2t/9.

Hence A = 2r + s and B = r + 2s with r, s ≥ 0. ✔

**L4. Degenerate cases (P1/P2).**

- *s = 0.* Use the diagonals k = a + 2b. The forced frontier is all of k₀ − 1. Add every point on diagonals k₀ − 3, k₀ − 6, … as owners, and cover with the right-colour points on k₀ − 4, k₀ − 7, …. All new edges land on k − 1 or k + 2, so they are covered. New owners are ≤ x/8 ≤ t/12 < 4t/27, so they never equal e. The count is Σ_n [f(k₀ − 3n) − f(k₀ − 3n − 1)] with f(k) = ⌊k/2⌋ + 1, which equals ⌊B/3⌋. Maximality then forces B ≤ 2.
- *r = 0.* Symmetric, with k = 2a + b, giving A ≤ 2. ✔ (The diagonal counts were checked.)

**L5. Incomparable case (r, s ≥ 1).**

1. The vertical chain y g^m (m < r) and the horizontal chain x q^n (n < s) are forced, together with the strip g u_n.
2. If a rooted edge exists along the vertical chain, expansion forces qz ∈ U with z ≤ 2t/9. One owner, qy, has a = −1, which is why the bound is r + h + 2 and not r + h + 3; I checked this point specifically.
3. That deep case dies. The forced owners gz and qz force 2z, 3z ∈ W. This adds two vertices but at most one owner, namely 6z.
4. Hence y > t/3, so y is the top power of 3 and the only vertical owner. Therefore D* = 1. ✔

**L6. Mandatory owners (t ≥ 18).** For a colour j other than the top one with D*_j > 0, every restricted maximiser contains m_j, where m₀ = 6, m₁ = 12 and m₂ = 18. The remaining sub-case (A, B) = (2, 1) needs E(18), so it needs t ≥ 27, and it is vacuous on [18, 27). ✔

**L7. Single-exclusion common optimum.** D* ∈ {D − 1, D}. In either case some global optimum F omits a restricted maximiser in every colour simultaneously. ✔

**L8. Collision.** Suppose τ < M. Then D*_j > 0 in every colour. The two non-top colours omit two of 6, 12, 18 from F. If the top colour's minimal maximiser were origin-type or degenerate, F would also miss the third, leaving the corner {6, 12, 18} uncovered. So the top maximiser is incomparable, and τ = Q_top − 1 with Q_top minimal. ✔

**L9. Cap and P4.**

- For s ≥ 2 a cap g²z > t is impossible: the same two backward inductions apply, with 4s − 2 vertices against 4s − 2 owners.
- r = 2 forces s = 1, which is the window [216, 243).
- r = 1 forces z > t/2. Otherwise 2z ∈ W supports only gz, because R(z) is absent and 6z > t.
- P4 (r = 1): add P₀∖{y} on 2a + b ≡ k₀ − 3 (mod 3) and cover with the left-colour diagonals. On the top added diagonal, the only owner with a = 0 is y, which is excluded, so the missing frontier point 2y is never needed. The gain is ⌊(s − 1)/3⌋, so s ≤ 3. ✔

**L10. Finite remainder.** I recomputed the five surviving windows independently:

| window | K | Q | top colour | Q_top > min Q? |
|---|---|---|---|---|
| [54, 64) | (6,5,5) | (6,5,5) | 0 | yes |
| [64, 72) | (7,5,5) | (6,5,5) | 0 | yes |
| [216, 243) | (9,8,9) | (9,8,9) | 2 | yes |
| [576, 648) | (12,12,11) | (11,12,11) | 1 | yes |
| [5184, 5832) | (20,19,20) | (19,19,20) | 2 | yes |

No window contains an interior smooth birth. Each row contradicts L8. The cases 3 ≤ t < 18 were checked directly.

**Conclusion: τ = M for every real t ≥ 3.** The endpoint conventions are as follows. All windows are left-closed and right-open at smooth numbers. The only non-smooth breakpoint, 27/2, never changes the minimum.

**What could still be wrong.** I tried to break the argument at its known pressure points: quantifiers over maximisers, double coverage, vertical owners with no E-edge, boundary starts and caps, and owner lists. I found nothing. It is still a long written argument with no machine check. The computations in §7 are consistent with it but do not prove it.

## 4. Theorem 2: explicit increments

Use the convention that patches have A ≥ 2. Pass t through a smooth number d = 2^a3^b ≥ 3. The vector Q changes by +1 in the following colours, and in no others:

| d | colours incremented | reason |
|---|---|---|
| 2^a (a ≥ 1) | none | point and isolate have the same colour |
| 3·2^a, a ≤ 2 | a+1, a+2 | isolate 2^{a+1} dies; point has colour a+2 |
| 3·2^a, a ≥ 3 | a+1 | isolate dies; patch at 2^{a−1} is born in the point's colour |
| 27·2^a | a, a+2 | patch at 2^{a+2} dies; point has colour a |
| otherwise | a − b | point birth only |

Every case follows from the window endpoints and the point colours. This was checked against direct recomputation at all smooth d ≤ 10⁹.

**Rule.** Write m = min Q(d⁻). Then

  η_{a,b} = 1  ⇔  every j with Q_j(d⁻) = m is incremented at d.

The small cases are η₁ = η₂ = 0 (τ = 0 for t < 3), and η₃ = 1.

Equivalently, in the single-colour rows, η = 1 iff that colour is the *unique* minimiser. In the two-colour rows, η = 1 iff the third colour is *not* a minimiser.

Check: this rule reproduces the exact-DP increments at every smooth d ≤ 10⁹ with no mismatch.

**Corollary.** The GSW/Chung–Erdős–Graham guess that an optimiser deletes one coset of ⟨8, 6⟩ amounts to deleting a colour class, since ⟨8, 6⟩ = {a ≡ b mod 3}. That guess is false, but only by ≤ 1, and only through the two gadgets. The forum's first counterexample, k = 45 (d₄₅ = 1536, f = 14 vs balanced 15), is exactly the birth of the patch {256, 1152, 1536}. Coset deletion is first beaten earlier, at k = 24 (d = 162), by the isolate 128 = 2⁷ (2t/3 = 108 < 128 ≤ 162): min K = 8 while τ = 7. The forum's g(k) is therefore not plain min_j K_j; the k = 45 statement above is about the patch.

## 5. Determination of c

**Theorem 3.** c = 1 − (1/3) Σ_{a,b} η_{a,b} 2^{−a}3^{−b} = 1 − (1/3) ∫₁^∞ τ(t) t^{−2} dt.

*Proof.*

1. τ is nondecreasing, since restricting a cover is still a cover. Also τ ≤ |D_t| = O(log² t).
2. By (1.1), Σ_m τ(N/m) = Σ_{d≤N} η_d · #{m ≤ N/d : (m,6) = 1} = (N/3) Σ_{d≤N} η_d/d + O(|D_N|).
3. Divide by N. The error O(log² N)/N → 0, and Σ η_d/d ≤ Σ 1/d = 3 converges. This gives the series form.
4. Fubini, Σ η_d/d = Σ η_d ∫_d^∞ t^{−2} dt = ∫ τ t^{−2} dt, gives the integral form.
5. The argument re-proves that the limit exists. It matches GSW, because f_k − f_{k−1} = 1 − η_k. ∎

**Theorem 4 (gauge form).** Let ω = e^{2πi/3} and Ŝ(t) = Σ_j Q_j(t) ω^j ∈ ℤ[ω]. Let ε(t) ∈ {0, 1} indicate an active exceptional root, and let H(z) = max_j Re(−ω^{−j} z). Then

  τ(t) = (|D_t| − ε(t))/3 − (2/3) H(Ŝ(t)),

  c = 757/972 + (2/9) ∫₃^∞ H(Ŝ(t)) t^{−2} dt.

The constant 757/972 = 1 − (1/3)[13/18 − 19/324] is exact. It uses ∫₃^∞ |D_t| t^{−2} dt = 13/6, together with the isolate and patch window integrals Σ_{A≥2} 1/(3·2^A) = 1/6 and Σ_{A≥2} 1/(54·2^A) = 1/108.

Ŝ is a lattice walk. Before corrections, Ŝ = Σ_b ω^{−b} · (0, 1, or 1 + ω, according to w_b mod 3). Its steps are driven by ⌊L − b·log₂6⌋ mod 3, i.e. by a step function evaluated along the rotation by log₂6/3. Kesten's theorem makes such Birkhoff sums unbounded, though only logarithmically, because 1/3 ∉ ℤα + ℤ. That is why the optimal colour keeps switching.

Check: 757/972 + J/3, with J computed exactly to 10⁶⁰, reproduces c to 60 digits.

**What is explicit beyond GSW.**

- GSW's coefficient f_k − f_{k−1} required solving a hitting-set problem on k points.
- Here it is given by the table in §4 together with three lattice-point counts. Each is a sum of floors, updated in O(1) per step.
- The optimisers are described completely: one colour class, plus at most one isolate or patch near the horizontal axis.
- c becomes a rational number plus an integral of a quasi-periodic discrepancy functional.

## 6. Error bounds and digits

**Box truncation.** Since η ∈ {0, 1},

  0 ≤ c_{A,B} − c ≤ (1/3) Σ_{(a,b) outside the box} 2^{−a}3^{−b} = 1 − (1 − 2^{−A})(1 − 3^{−B}) = E_{A,B},

which is the bound C_{A,B} − E_{A,B} ≤ c ≤ C_{A,B}.

**Size truncation (sharper).** Let a_b be the least a with 2^a3^b > N. Then

  Σ_{d>N} 1/d = Σ_b 2·3^{−b}2^{−a_b} ≤ (2⌊log₃N⌋ + 5)/N.

This is implemented exactly in `c_digits.py`. With N = 10¹³⁰ there are 59,185 terms and the enclosure width is 1.32·10⁻¹²⁸:

0.80096575500655898909042032638808241322472498911028458781919045603644708044249630021895087751711467131844149435653902330834474373477322453997 ≤ c ≤ …74796512743284.

As a by-product, τ(10¹³⁰) = 19727.

## 7. Further findings, including negative ones

- **Shape generalisation (new, computational).** Formula (C), rewritten in row form, holds for all 2886 staircases with gap word in {1,2}*, avoiding `11` and `222`, top row ≤ 2, B ≤ 22 and w₀ ≤ 32. In row form the isolate is the condition w₀ − w₁ = 2 in colour w₀ − 1, and the patch is gaps (1, 2, 2) at the bottom, with w₃ ≥ 1, in colour w₀. Allowing `11`, or `222`, or wider tops, produces counterexamples, for instance [12, 10, 8, 6, 5, 3, 2]. This suggests a purely local proof is possible, with the proof's numeric thresholds 2t/3, 2t/9, 4t/27 reading as gap-word conditions. I did not attempt to prove it.
- **No LP or packing shortcut.** The fractional-cover gap M − LP grows: 2.41 at t = 10⁸. The disjoint-corner packing number is far below τ: 132 of 142 cutoffs ≤ 10⁶ differ. So no König or LP certificate exists.
- **No tropical-rank-3 normal form.** The value functions on the bottom row and column 0 are not min_j(A_j + |Z∖P_j|), so a transfer-operator proof with three phase states fails. Mixed axis patterns occur in optimal covers, and the "every optimum contains a vertical phase" normalisation is false. The audited proof avoids it correctly.

## 8. Literature

| item | status |
|---|---|
| Limit exists; c = (1/3)Σ_{k∈K} 1/d_k (GSW 1977, [GrSpWi77]) | established |
| 0.8003194838 ≤ c ≤ 0.8009611 (Chung–Erdős–Graham 2002, via forum); their f = g conjecture fails at k = 45 | established (the upper bound was mis-stated, per Eberhard) |
| c = 0.80096575500655898909042032638808241… by integer programming (Eberhard 2025, OEIS A386439) | established numerics |
| Exact finite formula (C) for all t | new; proof in the ErdosGPT notes, audited internally (two passes) and here |
| Explicit η rule, gauge/Eisenstein form, 757/972 main term, 128 certified digits | new; conditional only on (C) |
| Explanation of the k = 45 counterexample as a patch birth | new, follows from (C) |
| Locally balanced staircase generalisation | new; computational evidence only |
| Irrationality (ii) | open; untouched |

The erdosproblems page says the value "can be estimated by elementary arguments" and cites Eberhard's 0.800965…. Nothing there gives a closed rule for the increments or for the structure of the optimisers.

## Files (this folder)

- `tau_dp.py`: exact τ by column transfer, plus formula (C).
- `brute_check.py`: brute-force validation of the DP.
- `eta_rule.py`: increment table and η rule, checked against the DP.
- `c_digits.py`: certified enclosure. Run `python c_digits.py 130`.
- `walk.py`: gauge identity and the 757/972 + J/3 check.
- `lemma_probe.py`: direct tests of lemmas (4) and (8).
- `shapes.py`, `test_S*.py`: the shape generalisation.
- `packing.py`, `lp.py`, `rowdp.py`, `fit3.py`, `col0.py`: the negative results.

Sources: [erdosproblems.com/168](https://www.erdosproblems.com/168), [forum thread](https://www.erdosproblems.com/forum/thread/168), [OEIS A386439](https://oeis.org/A386439), [Chung–Erdős–Graham paper](https://mathweb.ucsd.edu/~fan/wp/linear.pdf).
