# Referee audit of `PROOF.md` (lower bound τ(t) ≥ min_j (K_j − I_j − P_j), t ≥ 3)

Auditor: independent adversarial referee (Claude), 2026-11-08. I did not edit `PROOF.md` or any existing file. All my code lives in this `audit/` folder. It uses none of the parent directory's code.

**Overall verdict: the lower bound is proved.** I re-derived every step of §§2–9 by hand. I found no mathematical error and no logical gap. I found a few presentational omissions, listed in §C. Each is closed in one line, and none affects correctness. Independent computation agrees with every lemma statement I could test, and with the formula itself on all 336 breakpoints t ∈ [3, 3·10⁹].

---

## A. Per-section verdicts

Notation: points are written (a, b) = 2^a3^b; g = (2, −1) and q = (−1, 2).

### §1 Notation, (U): PASS
The corner T(r) = {(a,b), (a+1,b), (a,b+1)} has colours c, c+1, c−1. The ratios 2, 3, 3/2 are distinct, so two points determine the corner. The exponent map (m,n) ↦ (2m−n, −m+2n) has determinant 3, which gives injectivity (U). The image is exactly the colour-preserving sublattice {a ≡ b mod 3}, which has index 3. So "same colour ⇔ differ by g^m q^n" holds, and the cone-coordinate computations rely on exactly this.

### Lemma 2.1 (edges/owners): PASS
I re-derived the three positions of u in a corner:
- u = r gives (2u, 3u), present iff 3u ≤ t.
- u = 2r gives (3u/2, u/2), present iff a ≥ 1 and 3u/2 ≤ t.
- u = 3r gives (u/3, 2u/3), present iff b ≥ 1.

The colours are j+1 for 2u, 3u/2, u/3 and j+2 for 3u, u/2, 2u/3. Inverting gives the owner lists:
- left vertex l: owners l/2, 2l/3, 3l;
- right vertex v: owners v/3, 3v/2, 2v.

The three left (and right) endpoints of one owner are distinct. So the degree of a vertex in B(U) equals the number of distinct owners at it. **Machine check:** for every 3-smooth t ≤ 2200 and every colour, the edges built directly from the corners equal the Lemma 2.1 lists (`audit_struct.py`, `lemma21_check`).

### Lemma 2.2 (matching identity), 2.3 (deletion): PASS
Take a cover F, and set U = C_j∖F and W = F∖C_j. If the owner of a corner is not in F, the corner must be hit on its other two points, so W covers B(U). Then |F| = K_j − |U| + |W| ≥ K_j − d(U), by König. Conversely, (C_j∖U) ∪ W is a cover. Equality gives the "moreover" part. Lemma 2.3 holds because ν cannot increase under edge deletion. **Machine check:** τ = K_j − D_j for all three colours and every 3-smooth t ≤ 2200. Here τ comes from the DP and D_j from exhaustive matchings, two independent computations.

### §3 (exceptional roots, Lemmas 3.1, 3.2): PASS
- The isolate window (2t/3, t] has ratio 3/2. The patch window e ∈ (4t/27, t/6] has ratio 9/8. So each holds at most one power of 2.
- A patch root gives t < 27e/4 < 8e, so the top power of 2 is 4e ≤ 2t/3, which is not an isolate.
- Upper bound for a patch root:
  - 9e/2 = (A−1, 2) and 6e = (A+1, 1) have colour A.
  - Their only present edges are N, because E(9e/2) needs 27e/4 ≤ t, E(6e) needs 9e ≤ t, and both R edges need more.
  - e has exactly E and R.
  - All four edges meet {3e/2, 2e}, which gives the cover of size K−1.
- The A = 1 window [12, 13.5): K = (3,3,2) under either convention, so min = 2. The convention remark is harmless. In the "A ≥ 2" convention I_j + P_j = δ_j holds exactly for t ≥ 18, and that is what §7 uses.

### Lemma 4.1 (essentiality/expansion), forcing: PASS
(i) Let O be the owners uniquely served by w. Every other edge at w has its far end in W∖{w}, so W∖{w} covers B(U∖O).
- O = ∅ contradicts the minimality of W.
- O = {u} gives d(U∖{u}) ≥ D, which contradicts tightness.

(ii) W∖S covers B(U∖T(S)).
- If T(S) ⊊ U, then d(U∖T(S)) ≥ D + |S| − |T(S)|. When T(S) ≠ ∅, tightness gives d < D. When T(S) = ∅, U∖T(S) = U is not a proper subset, but the inequality itself reads D ≥ D + |S|, which is impossible. (The text says only "tightness forces"; see §C.1.)
- If T(S) = U, then |U| = |W| + D > |S|.

**Forcing** at a vertex whose N/E/R edge from one owner is uniquely covered: w needs a second uniquely-served owner, so some other listed candidate is in U, its edge is present and its far endpoint is not in W. At a **doubly covered** vertex both remaining candidates are needed. That is what drives the backward inductions (see §B).

**Machine check:** I took every tight set (d = D > 0 and every proper subset < D) for 3-smooth t ≤ 2200, 121 sets. For every minimum vertex cover W of each, 126 covers enumerated exhaustively, 4.1(i) holds. For t ≤ 400, 4.1(ii) holds for every nonempty S ⊂ W.

### Lemma 5.1 (predecessor): PASS
- Step 1: the owners of u/3 are u/6, 2u/9 and u, so u/3 is a leaf and 2u/3 ∈ W.
- Step 2: the owners of 2u/3 are 2u/9, u (uniquely served, because u/3 ∉ W) and 4u/3. So 4u/3 ∈ U, its E edge is present, and 2u ∉ W. That edge being present means 2u ≤ t, so 3u/2 ≤ t and E(u) is present.
- Step 3: u/2 has owners u/6, 3u/4 and u, so it is a leaf and 3u/2 ∈ W.
- Step 4: the owners of 3u/2 are 3u/4, u and 9u/2. So 9u/2 ∈ U, 3u ∉ W, and 3u ≤ 9u/2 ≤ t, so R(u) is present.
- Neither endpoint of R(u) is in W, a contradiction.

**Machine check:** the predecessor property holds in every tight set found.

### Lemma 5.2 (classification of a ≥ 1 critical sets): PASS
- A critical set is tight. Lemma 5.1 descent (÷gq, ÷q, ÷g) ends at an element with b = 0, because a ≥ 1 throughout. The b = 0 elements are x·8^ℓ = x(g²q)^ℓ, so U ⊂ x⟨g,q⟩.
- **x > 2t/3:** x owns no edge, and criticality gives U = {x}, an isolate.
- **Step 2:**
  - u_n/2 has the other owners x g^{−1}q^{n−1} and x g^{−1}q^n, which are outside the cone by (U). So it is a leaf and L_n ∈ W.
  - Forcing at L_n (owners 3u_n/4 ∉ U, u_n, u_{n+1}) gives u_{n+1} ∈ U and 3u_n ∉ W.
  - The chain runs while u_n ≤ 2t/3. It must stop because U is finite, and k ≥ 1 because x ≤ 2t/3.
  - For n < k, u_n ≤ u_k/q ≤ 2t/9, so R(u_n) is present and A_n = 2u_n ∈ W.
- **Step 3:**
  - L_n has owners u_n and u_{n+1}; the third candidate 3u_n/4 is outside the cone.
  - A_n has owners u_n, g u_n and 6u_n = g u_{n+1}. g u_0 = (A+2, −1) is not a board point.
  - So |S₀| = 2k and the bound set has size 2k+1, which puts all of it in U and gives u_k ≤ 3t/4.
- **Step 4:**
  - g u_n/3 = 2u_{n−1} ∈ W, so N(g u_n) is doubly covered if β_n ∈ W. Then both g u_{n−1} (R) and g²u_n (E) must be uniquely served, so 2g u_n ∉ W.
  - At n = k, g²u_k > 32t/27 > t, so β_k ∉ W. For n < k, g u_n ≤ 2t/9, R(g u_n) is present, and 3g u_n = β_{n+1}.
  - So β_n ∈ W ⇒ β_{n+1} ∈ W. Backward induction from n = k is correct in direction and base, and gives B_n = 2g u_n ∈ W for n < k.
  - B_n has owners g u_n, g²u_n and g²u_{n+1}, with g²u_k off the board. The counts are 3k−1 vs 3k, so the g²u_n (n < k) lie in U.
- **Step 5 (k ≥ 2):**
  - w_n ≤ (32/81)u_k ≤ 8t/27 < t/3, so R(w_n) is present for n ≤ k−1.
  - γ_k = 3w_{k−1} = 2w_k/3 has the other owners w_k and g w_k, both off the board, so it is a leaf.
  - For 2 ≤ n < k, b(w_n) = 2n−2 ≥ 2, and w_n/3 = 2g u_{n−1} = B_{n−1} ∈ W. So γ_n ∈ W ⇒ g³u_n ∈ U and 2w_n ∉ W ⇒ γ_{n+1} ∈ W. Backward induction gives C_n ∈ W for 1 ≤ n < k.
  - C_n has owners w_n, g³u_n and g³u_{n+1}. g³u_1 has b = −1 and g³u_k > t.
  - The count is |S₂| = 4k−2 against a bound set of size 4k−2, a contradiction.
  - **Boundary k = 2:** S₂ = {L₀, L₁, A₀, A₁, B₁, C₁} (6 vertices) and the bound set is {u₀, u₁, u₂, gu₁, gu₂, w₁} (6). The contradiction holds.
  - Distinctness: after dividing by 2x the coordinates are (−1,n), (0,n), (1,n), (2,n), distinct by (U).
- **Step 6 (k = 1):** the forced set is {x, 9x/2, 6x}. Its d is 1: the matching E(x), N(6x) has size 2 and the cover {3x/2, 2x} has size 2. That gives the patch root (A ≥ 2, 6x ≤ t < 27x/4).

**Machine check:** I enumerated all 33 critical sets with a ≥ 1 for t ≤ 2200 exhaustively. Each is exactly an isolate singleton or a patch triple.

### Corollary 5.3: PASS
A minimal positive-deficiency subset has d = 1 by Lemma 2.3, so it is critical. It must contain the unique exceptional root, which 𝒜_j excludes. **Machine check:** every V ⊂ 𝒜_j with a ≥ 1 has d ≤ 0, for t ≤ 2200.

### §6 preamble, Lemma 6.1, (6.1): PASS
- Lemma 6.1: distinct owners have disjoint N edges, since each endpoint determines its owner. Corollary 5.3 handles a set with a ≥ 1 throughout.
- (6.1): Lemma 5.1 descent goes to an axis element, and same-colour axis elements differ by 8 = g²q or 27 = gq².
- Integrality of r and s: A + B ≡ 0 (mod 3), y = x g^{−r}q^s, A = 2r+s, B = r+2s.
- The "neither cone if m < 0 and n < s" remark is correct.

**Machine check:** I enumerated all 69 inclusion-minimal maximisers for t ≤ 2200 exhaustively, and sampled 152 more (distinct per t, j) for 18 ≤ t ≤ 60000 by ILP. All lie in x⟨g,q⟩ ∪ y⟨g,q⟩ and contain both axes.

### Lemma 6.2 (root balance): PASS
- **r < 0:** then s > A > 0, so y lies in the x-cone and U ⊂ x⟨g,q⟩. The horizontal chain gives u_A = 3^{2A} ∈ U:
  - each E(u_n) is present, because u_n < u_A/q ≤ 2t/9 and a ≥ 1;
  - its right endpoint is a leaf, because the other owners have m = −1.
  
  Since 2A < B, this element on the a = 0 axis is smaller than y, a contradiction.
- **s < 0:** symmetric, with the vertical chain. N is always present, v_i/3 is a leaf (its other owners have q-coordinate −1), and forcing at 2v_i/3 gives v_{i+1}. So v_B = 4^B < x lies on the b = 0 axis, a contradiction.

### Lemma 6.3 (augmentation), (6.2): PASS
d(U∪P) ≥ D* + |P| − |R|, and maximality over 𝒜_j gives D* ≥ d(U∪P). R points need not be vertices. For (6.2): f(k) − f(k−1) = [k even, k ≥ 0], and the sum counts even n = 2m with 6m ≤ 2A, which is ⌊A/3⌋.

### Lemma 6.4 (D1 ⇒ B ≤ 2): PASS
I re-derived every claim:
- The frontier 2v_i/3 = (2i+1, B−i−1) covers all B = f(2B−1) points of a + 2b = 2B−1.
- The y-cone has k = 2B + 3n.
- P and R are on the board, because 2^a3^b ≤ 2^{a+2b} ≤ x/8 ≤ t/12.
- P avoids e, because t/12 < 4t/27.
- The colour is k ≡ 2B ≡ −B.
- P is disjoint from U, since U has k ≥ 2B.
- Right endpoints sit at N (a+1, b−1) → k−1, E (a−1, b) → k−1 and R (a, b+1) → k+2. The diagonal k+2 is the frontier when n = 1 and an R diagonal when n ≥ 2. So W ∪ R covers B(U∪P).
- The count is ⌊B/3⌋ ≤ 0.

### Lemma 6.5 (D2 ⇒ A ≤ 2): PASS
This mirrors 6.4 with k = 2a+b and left endpoints:
- N (a, b−1) → k−1;
- E (a−1, b+1) → k−1;
- R (a+1, b) → k+2.

The board bound is 3^{2A−3} = y/27, and the colour is −k ≡ A. **Machine check (6.4, 6.5):** every D1 or D2 maximiser found has B ≤ 2 or A ≤ 2 respectively (25 exhaustive, 67 by ILP).

### Lemma 6.6 (incomparable case): PASS
- **Vertical chain:** the other owners of v_i/3 are x g^{i−r−1}q^{s−1} and x g^{i−r}q^{s−1}, both outside both cones. E(z) is present, so z ≤ 2t/3.
- **Horizontal chain:** u_n ≤ z/q ≤ 4t/27, and a(u_n) ≥ 2r+1 ≥ 3 (the text says ≥ 2r, which is weaker but true). The leaf at u_n/2 comes from m = −1 and n′ < s. R(u_n) is present.
- **H ⊂ U:** the counts are 2s against 2s+1, with g u_0 off the board.
- **Rooted vertical edges:**
  - 2v_i/3 has the third candidate v_i/q = x g^{i−r}q^{s−1}, which lies in neither cone.
  - 3v_i has owners v_i, q v_i and q v_{i+1}, and q v_0 = (−1, B+2) is off the board.
  - The bound set has size r+h+2 against |S_V| = r+h+1. Then q v_{h+1} ≤ t gives 3v_{h+1} ≤ 2t/3, so h = r−1, qz ∈ U and z ≤ 2t/9.
- **Deep case:**
  - E(gz) = (2z, 2z/3) with 2z/3 = 3u_{s−1} ∉ W, so 2z ∈ W.
  - N(qz) = (3z/2, 3z) with 3z/2 = 2v_{r−1} ∉ W, so 3z ∈ W.
  - H ∩ V = {z}: V has m ≤ 0, and its m = 0 elements are z and qz = x q^{s+1}, which is not in H.
  - The owners of 2z are z, gz and 6z; the owners of 3z are z, qz and 6z.
  - |T(S)| ≤ 2s+2r+2 = |S|, a contradiction.
- **(a)–(d):** 3y > t. Then g^r < 2 gives r ≤ 2. 27y > t gives (c), so j = −B with B = ⌊log₃t⌋. Corollary 5.3 on U∖{y}, plus Lemma 2.3, gives d = 1.

**Machine check:** every case-(I) maximiser found satisfies (a)–(d). Property (e) was checked against *every* minimum vertex cover W.

### Lemma 6.7 (cap): PASS
This is the same two-column argument as 5.2 Steps 4–5, with the cap g²u_s > t replacing u_k > 2t/3. The bounds g u_n ≤ 8z/27 ≤ 16t/81 and g²u_n ≤ 32z/81 ≤ 64t/243 < t/3 hold. The base β_s ∉ W holds because g²u_s > t. γ_s is a leaf because g²u_s and g³u_s are off the board. The counts are 4s−2 against 4s−2. **Boundary s = 2:** S₂ has 6 elements, and the bound set is H (5) plus {g²u₁}, also 6.

### Lemma 6.8 (case-(I) windows): PASS
- **r = 2:** g²z > 256t/243 > t, so s = 1. Then x = 32, y = 81 and z = 144, which gives [216, 243).
- **r = 1, z ≤ t/2:** 2z ∈ W is served only by gz, because R(z) needs 3z ≤ t while z > 4t/9, and 6z > t. This contradicts 4.1(i).
- **Windows:** z = 4·9^s gives [6·9^s, 8·9^s) ∩ [64·9^{s−1}, ∞). That is [54,72), [576,648) and [5184,5832).

**Machine check:** the case-(I) maximisers found are t = 54, 64 (r=1, s=1), t = 216 (r=2, s=1), t = 576 (r=1, s=2) and t = 5184 (r=1, s=3; found by ILP). All lie in the windows. So every window, including s = 3, is actually realised, and no case (I) occurs outside them up to t = 60000.

### Lemma 6.9 (r = 1 ⇒ s ≤ 3): PASS
- U ∩ {2a+b < 2A} = {y}, because y-cone points with m′ = 0 are y q^{n′} and need a = −n′ ≥ 0.
- P is on the board (≤ 3^k ≤ y) and avoids e: the top diagonal with a ≥ 1 is at most 2y/9 = z/6 ≤ t/9, the lower ones at most y/27, and both are below 4t/27.
- For n = 1 the R-endpoint 2p has a ≥ 2. The points with a ≥ 2 on 2a+b = 2A−1 are exactly the 3u_n/2 for n < s, since A = s+2. These lie in W by 6.6(e).
- The count is ⌊(s+2)/3⌋ − 1 = ⌊(s−1)/3⌋ ≤ 0.
- The bound is sharp: a case-(I) maximiser with s = 3 exists at t = 5184.

### Lemma 6.10 (mandatory owners): PASS
- **Case list exhaustive:** not-(O) means A, B ≥ 1, so r = s = 0 is impossible. D1 has B = r ≥ 1 and D2 has A = s ≥ 1. 6.4 and 6.5 bound them by 2.
- **Colours:** c(x) = A mod 3, which gives (O):0; D2 A=1:1; D1 B=2 (x=16):1; D2 A=2:2; D1 B=1 (x=4):2. All correct.
- **(O):** the owners of 2 are {1, 6} and the owners of 3 are {1, 6}. If both 2 and 3 are in W, each serves only owner 6, which violates 4.1(i).
- **D2 A=1:** 1 is a leaf, so 3 ∈ W. Forcing at 3 gives 9 ∈ U and 6 ∉ W, so 4 ∈ W. S = {3, 4} has owners in {2, 9, 12}, which forces 12 ∈ U.
- **D1 B=2 and D2 A=2:** these come directly from the forced chains.
- **D1 B=1:** 1 is a leaf, so 2 ∈ W. Forcing gives 4 ∈ U and 6 ∉ W, so 9 ∈ W, because R(3) is present for t ≥ 9. S = {2, 9} has owners in {3, 4} ∪ {18 if t ≥ 27}.

**Machine check:** m_j ∈ U for every non-(I) maximiser found with t ≥ 18. There were 65 non-(I) maximisers exhaustively for t ≤ 2200 (the assertion is applied to those with t ≥ 18) and 147 by ILP for 18 ≤ t ≤ 60000. In the case-(I) examples m_j ∉ U (for example t = 54: U = {8, 27, 36, 48} has no 6). So the case split is genuinely needed, and the test would have caught a misclassification.

### Lemma 7.1 (common optimum): PASS
- For colours other than j_e, any minimum cover works (Lemma 2.2, with 𝒜 = C).
- For j_e, D−1 ≤ D* ≤ D.
  - If D* = D, the cover (C∖V) ∪ W* has size τ and C∖F = V.
  - If D* = D−1, every minimum F has d(C∖F) = D > D*, so e ∈ C∖F, and removing e leaves d ≥ D*.

### Theorem 7.2: PASS
- For t ≥ 18, K_j − Q_j = I_j + P_j = δ_j, because there is at most one exceptional root and the A = 1 window lies below 18. Then τ < M gives D_j > δ_j and D*_j ≥ D_j − δ_j > 0.
- U_j, chosen minimal inside (C_j∖F) ∩ 𝒜_j attaining D*_j, is an inclusion-minimal maximiser of 𝒜_j. Its proper subsets lie inside the same set. So all §6 hypotheses hold, including the maximality that 6.3 needs.
- 6.6(c) puts case (I) only in j_top. 6.10 plus F ∩ U_j = ∅ means F misses {6, 12, 18} unless U_{j_top} is in case (I). Then D = 1+δ, τ = Q_top − 1 and Q_top = M, which contradicts the table.

### §8 table: PASS (recomputed independently)
I recomputed every row, giving the same row widths, K, I, P, Q, j_top, Q_top and M:
- [54,64): (6,5,5), j_top 0, 6 > 5.
- [64,72): (6,5,5), j_top 0, 6 > 5.
- [216,243): (9,8,9), j_top 2, 9 > 8.
- [576,648): (11,12,11), j_top 1, 12 > 11.
- [5184,5832): (19,19,20), j_top 2, 20 > 19.

There is no 3-smooth number strictly inside any window, and Q is identical at both ends of each.

### §9 (3 ≤ t < 18): PASS
The corners are T(1) and T(2) for t < 9, and also T(3) and T(4 when t ≥ 12) for t < 18. The point 2, and the set {3, 4}, hit all of them. T(1) ∩ T(2) ∩ T(3) = ∅. The DP values are τ = 1, 1, 1, 1, 2, 2, 2 at t = 3, 4, 6, 8, 9, 12, 16, and they equal M under both patch conventions.

## B. Specific adversarial points checked
1. **Forcing completeness.** At every forcing or leaf step I listed all three Lemma 2.1 candidates and checked why each excluded one is not in U. The reason is always one of: off the board (negative coordinate or > t), outside the relevant cone (via (U)), or "neither cone" in case (I). No candidate is missed.
2. **Backward inductions** (5.2 Steps 4–5, 6.7). At a doubly covered vertex, *both* remaining candidates must be uniquely served. So β_n ∈ W forces g²u_n ∈ U and 2g u_n ∉ W, which then propagates *upward* to β_{n+1} ∈ W. The base is at the top index, where the needed owner is off the board. Direction and base are correct.
3. **Tight vs maximal.** 4.1, 5.1, 5.2, 6.1, 6.2, 6.6, 6.7, 6.8 and 6.10 use only tightness. 6.4, 6.5 and 6.9 (via 6.3) need maximality over 𝒜_j, and the U_j of 7.2 have it.
4. **P disjoint, in pool, on board** in 6.4, 6.5 and 6.9: verified above, including avoidance of e via e > 4t/27.
5. **Lemma 6.3 R counts:** R may include non-vertices or W points, and the inequality only becomes weaker.

## C. Minor presentational omissions (no effect on correctness)
1. 4.1(ii): when T(S) = ∅, "tightness" is not the reason, since U∖∅ = U. The displayed inequality D ≥ D + |S| gives the contradiction directly.
2. 6.6: the text does not state that the elements of S_H and S_V are distinct. Distinctness follows from (U): 3u_n/2 vs 2u_m has ratio g^{−1}q^{n−m}, and 2v_i/3 vs 3v_{i′} has ratio q g^{i′−i}, so neither ratio is 1. (5.2 and 6.7 do state it.)
3. 6.6 horizontal chain: a(u_n) ≥ 2r+1, not "≥ 2r". Both are true, and only a ≥ 1 is needed.
4. 5.2 Step 4 and 6.7 at n = 1: g u_0 is off the board, so β_1 ∈ W already contradicts 4.1(i). The general wording covers this implicitly.
5. §3: the sentence about the "formula's A = 1 patch window" mixes conventions. The conclusion min Q = min Q̄ is right under both, and §7 uses the A ≥ 2 convention, where I_j + P_j = δ_j holds exactly.
6. The §8 "to reproduce" command depends on the parent directory's scripts. My recomputation does not use them.

## D. Scripts and outputs (all in `audit/`)
- `audit_formula.py`: exact column DP for τ, the formula Q under both A = 1 patch conventions, and the §8 and §9 tables. Output `out_formula_3e9.txt`: **336 3-smooth t in [3, 3·10⁹], 0 mismatches**, plus the tables quoted above. I also checked the DP against brute-force minimum covers for all 3-smooth t ≤ 150 (agrees).
- `audit_struct.py`: exhaustive per-colour subset enumeration. It checks Lemmas 2.1, 2.2, 4.1 (all minimum vertex covers), 5.1, 5.2, 5.3, 6.1, (6.1), 6.2, 6.4, 6.5, 6.6(a–e), 6.8, 6.9 and 6.10.
  - `out_struct_1000.txt` (4.1(ii) checked for all S when t ≤ 400): all assertions pass.
  - `out_struct_2200.txt`: all assertions pass. 121 tight sets, 126 minimum vertex covers, 33 critical a ≥ 1 sets, 69 minimal maximisers (O: 40, D1: 10, D2: 15, I: 4).
- `audit_ilp.py`: MILP (scipy) search for minimum-cardinality maximisers with forbidden-set exploration (BFS of depth ≤ 2), for 3-smooth 18 ≤ t ≤ 60000. Output `out_ilp_60000.txt`: all assertions pass. Tally: O 80, D1 22, D2 45, I(r=1,s=1) 2, I(r=2,s=1) 1, I(r=1,s=2) 1, I(r=1,s=3) 1 (the last at t = 5184).

Limits: the computations are finite evidence. The universal claim rests on the written argument, which I checked line by line. The ILP stage samples maximisers rather than enumerating all of them. Lemma 7.1 was checked by hand only.

## E. Overall verdict
**The lower bound τ(t) ≥ min_j(K_j − I_j − P_j) for all real t ≥ 3 is proved.** §9 covers t < 18, and Theorem 7.2 with §8 covers t ≥ 18. Together with Lemma 3.2 this gives Theorem (C). I found no counterexample to any lemma and no invalid inference. The only issues are the cosmetic items in §C.
