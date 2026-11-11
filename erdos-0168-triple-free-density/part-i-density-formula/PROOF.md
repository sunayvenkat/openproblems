# Self-contained proof of the finite formula (C) and the determination of c

This note proves everything it uses from first principles and cites no other note. The proof's architecture (matching reduction, axis-avoiding classification, two cones, prefix augmentations, a common optimum) follows the ErdosGPT notes. Every lemma is written out in full here so that it can be checked line by line. Computation is used in only two places, and both are finite. §9 checks a table of eight intervals with t < 18. §8 checks five explicit intervals of t, and only after the symbolic argument has reduced every remaining case to them.

---

## 1. Notation

Let t ≥ 3 be real. The **board** is the set of points u = 2^a3^b ≤ t with a, b ≥ 0. Write a(u) = a and b(u) = b. The colour of u is c(u) = a − b (mod 3), C_j is the set of board points of colour j, and K_j = |C_j|.

For a board point r with 3r ≤ t, the **corner** rooted at r is T(r) = {r, 2r, 3r}. Note that 3r ≤ t already implies 2r ≤ t. Corners are exactly the sets {n, 2n, 3n} inside the board. The three points of a corner have three different colours, namely c, c+1 and c−1.

A corner is determined by any two of its points, since the three pairwise ratios 2, 3 and 3/2 are distinct. A **cover** is a set of points that meets every corner. τ = τ(t) is the minimum size of a cover.

We use the multipliers g = 4/3 and q = 9/2. In exponents, g = (2, −1) and q = (−1, 2). Note that gq = 6, g²q = 8 and gq² = 27. The exponent map (m, n) ↦ (2m − n, −m + 2n) has determinant 3, so it is injective. Hence:

**(U) Unique coordinates.** For a fixed base point p, every point has at most one representation p·g^m q^n with (m, n) ∈ ℤ².

The **cone** of p is p⟨g,q⟩ = {p g^m q^n : m, n ≥ 0}.

## 2. The bipartite reduction

Fix a colour j. Call colour j+1 the *left* side and colour j+2 the *right* side. For a set U ⊂ C_j, let B(U) be the bipartite graph whose edges are the pairs T ∖ {u}, taken over every corner T whose colour-j point u lies in U. We say u **owns** that edge.

**Lemma 2.1 (edges and owners).** A point u = 2^a3^b ∈ C_j owns at most three edges, listed as (left, right):

- N(u) = (u/3, 2u/3), present if and only if b ≥ 1;
- E(u) = (3u/2, u/2), present if and only if a ≥ 1 and 3u/2 ≤ t;
- R(u) = (2u, 3u), present if and only if 3u ≤ t.

Each edge has exactly one owner. A left vertex l can be owned only by l/2 (through R), 2l/3 (through E) or 3l (through N). A right vertex v can be owned only by v/3 (through R), 3v/2 (through N) or 2v (through E). In each case the candidate must be a board point of U and the edge must be present.

*Proof.* The point u lies in T(r) as r = u, as 2r, or as 3r.

- r = u gives the edge {2u, 3u}, present iff 3u ≤ t.
- r = u/2 needs a ≥ 1. It gives {u/2, 3u/2}, present iff 3u/2 ≤ t.
- r = u/3 needs b ≥ 1. It gives {u/3, 2u/3}, which is always present because u ≤ t.

For the sides: 2u, 3u/2 and u/3 have colour j+1, while 3u, u/2 and 2u/3 have colour j+2. A corner is determined by two of its points, so each edge has exactly one owner. Solving l ∈ {2u, 3u/2, u/3} and v ∈ {3u, u/2, 2u/3} for u gives the owner lists. ∎

Write ν for the maximum matching size and d(U) = |U| − ν(B(U)) for the **deficiency**.

**Lemma 2.2 (matching identity).** For every colour j, τ = K_j − D_j, where D_j = max_{U⊂C_j} d(U). Moreover, if F is any minimum cover, then U = C_j ∖ F satisfies d(U) = D_j, and F ∖ C_j is a minimum vertex cover of B(U).

*Proof.* Let F be a cover, U = C_j ∖ F and W = F ∖ C_j. Take an edge of B(U). Its owner is not in F, so the corner must be hit by an endpoint, and W covers B(U). By König's theorem, |F| = K_j − |U| + |W| ≥ K_j − d(U).

Conversely, take any U ⊂ C_j and a minimum vertex cover W of B(U). Then (C_j ∖ U) ∪ W is a cover: a corner whose colour-j point lies outside U is hit by that point, and otherwise its opposite pair is an edge of B(U), which W meets. Its size is K_j − d(U). Taking the minimum over U gives the first claim. Equality in the first inequality gives the second. ∎

**Lemma 2.3 (deletion).** For any U and u, d(U ∖ {u}) ≥ d(U) − 1, because ν cannot increase when edges are removed.

## 3. Exceptional roots and the upper bound

Let e = 2^A. We say e is an

- **isolate** if A ≥ 1 and 2t/3 < e ≤ t;
- **patch root** if A ≥ 2 and 6e ≤ t < 27e/4.

In either case e has colour A mod 3. The formula's A = 1 patch window is [12, 27/2). Writing a bar for counts that ignore that window, Q̄_j = K_j − I_j − P̄_j satisfies Q̄_j ≥ Q_j. On [12, 27/2), K = (3, 3, 2), so min Q = min Q̄ = 2; outside that window Q̄ = Q. Hence **min_j Q_j = min_j Q̄_j for every t ≥ 3**, and we write M for this common value.

**Lemma 3.1 (at most one exceptional root, and e > 4t/27).**

- A window (2t/3, t] or (4t/27, t/6] has ratio < 2, so it contains at most one power of 2.
- If a patch root e exists, then t < 27e/4 < 8e. So the largest power of 2 on the board is 4e ≤ 2t/3, and there is no isolate.
- An isolate satisfies e > 2t/3, and a patch root satisfies e > 4t/27. ∎

Let δ_j ∈ {0, 1} indicate that the exceptional root has colour j, and let ε = Σ_j δ_j.

**Lemma 3.2 (upper bound).** τ ≤ M.

*Proof.* C_j is a cover, since every corner has a point of each colour.

- *Isolate e.* Here 3e > t, 3e/2 > t and b(e) = 0, so by Lemma 2.1 e lies in no corner. Hence C_j ∖ {e} is a cover.
- *Patch root e (A ≥ 2).* The points 9e/2 = (A−1, 2) and 6e = (A+1, 1) are board points of colour A. By Lemma 2.1 their edges are:
  - for e: E(e) = (3e/2, e/2) and R(e) = (2e, 3e), since 3e ≤ 6e ≤ t; there is no N edge because b = 0;
  - for 9e/2: N = (3e/2, 3e) only, since E needs 27e/4 ≤ t and R needs 27e/2 ≤ t;
  - for 6e: N = (2e, 4e) only, since E needs 9e ≤ t and R needs 18e ≤ t.

  All four edges meet {3e/2, 2e}, so (C_j ∖ {e, 9e/2, 6e}) ∪ {3e/2, 2e} is a cover of size K_j − 1.
- *The A = 1 window [12, 27/2).* The cover {3, 4} has size 2, which equals M there, as checked in §9. ∎

## 4. Tight sets

A set U ⊂ C_j is **tight** if d(U) = D > 0 and every proper subset U′ ⊊ U has d(U′) < D. Two kinds of tight set are used:

- critical sets (D = 1, every proper subset has d ≤ 0);
- inclusion-minimal maximisers: U ⊂ 𝒜 attains max_{V⊂𝒜} d(V), and no proper subset does.

Let W be a minimum vertex cover of B(U), so |W| = |U| − D. An edge at w ∈ W is **uniquely covered** by w if its other endpoint is not in W.

**Lemma 4.1 (essentiality and expansion).** Let U be tight and W as above.

- (i) Each w ∈ W uniquely covers edges of at least two distinct owners. In particular, a vertex of degree 1 in B(U) is not in W.
- (ii) For every nonempty S ⊂ W, the set T(S) of owners of all edges incident to S (including doubly covered ones) satisfies |T(S)| ≥ |S| + 1.

*Proof.*

(i) Let O be the set of owners of the edges that w uniquely covers. Every other edge at w has its other endpoint in W, so W ∖ {w} covers B(U ∖ O). If O = ∅, then W ∖ {w} covers B(U), which contradicts the minimality of W. If O = {u}, then d(U ∖ {u}) ≥ (|U| − 1) − (|W| − 1) = D, which contradicts tightness.

(ii) W ∖ S covers B(U ∖ T(S)). If T(S) ≠ U, then d(U ∖ T(S)) ≥ D + |S| − |T(S)|. When T(S) = ∅ this already reads d(U) ≥ D + |S| > D, a contradiction. Otherwise U ∖ T(S) is a proper subset, and tightness forces |T(S)| > |S|. If T(S) = U, then |T(S)| = |W| + D > |S|. ∎

We use (i) in the following form, which we call **forcing**. Suppose w ∈ W, and one edge at w is uniquely covered while the other possible owners at w are known. Then w must uniquely cover an edge of some other owner. That owner lies in U, its edge is present, and the far endpoint of that edge is not in W.

## 5. Axis-avoiding sets

**Lemma 5.1 (predecessor).** Let U ⊂ C_j be tight and u ∈ U with a(u), b(u) ≥ 1. Then at least one of u/6, 2u/9, 3u/4 lies in U.

*Proof.* Suppose none does.

1. The left endpoint u/3 of N(u) has possible owners u/6, 2u/9 and u. Only u is in U, so u/3 is a leaf, and u/3 ∉ W by 4.1(i). Hence 2u/3 ∈ W.
2. The right vertex 2u/3 has possible owners 2u/9 (not in U), u (whose N edge is uniquely covered here) and 4u/3. Forcing gives 4u/3 ∈ U, E(4u/3) present, and its left endpoint 2u ∉ W. In particular 2u ≤ t, so 3u/2 ≤ t, and E(u) is present because a ≥ 1.
3. The right endpoint u/2 of E(u) has possible owners u/6, 3u/4 and u, so it is a leaf. Hence 3u/2 ∈ W.
4. The left vertex 3u/2 has possible owners 3u/4 (not in U), u, and 9u/2. Forcing gives 9u/2 ∈ U and its right endpoint 3u ∉ W. Since 9u/2 ≤ t, we get 3u ≤ t, so R(u) = (2u, 3u) is present.
5. Neither endpoint of R(u) is in W. This is a contradiction. ∎

**Lemma 5.2 (classification).** Let U ⊂ C_j be critical with a(u) ≥ 1 for all u ∈ U. Then U is exactly one of the following:

- {x} with x = 2^A an isolate;
- {x, 9x/2, 6x} with x = 2^A, A ≥ 2, a patch root.

*Proof.*

**Step 1 (cone).** By Lemma 5.1 and induction on u, every u ∈ U equals r·g^m q^n with m, n ≥ 0 and r ∈ U satisfying b(r) = 0. (The predecessor steps divide by 6 = gq, by q, or by g, and terminate because u decreases.) The elements with b = 0 have the same colour, so they are 2^A·8^ℓ, where x = 2^A is the least of them and 8 = g²q. Hence U ⊂ x⟨g,q⟩, and A ≥ 1 because a(x) ≥ 1. If x > 2t/3, then x owns no edge, and criticality gives U = {x}. So assume x ≤ 2t/3.

**Step 2 (horizontal chain).** Let u_n = x q^n, so a(u_n) = A − n and b(u_n) = 2n. Suppose u_n ∈ U and E(u_n) is present.

- The right endpoint u_n/2 has possible owners u_n/6 = x g^{−1} q^{n−1} and 3u_n/4 = x g^{−1} q^n. These have g-coordinate −1, so by (U) they are not in U. So u_n/2 is a leaf, and L_n := 3u_n/2 ∈ W.
- The left vertex L_n has possible owners 3u_n/4 (not in U), u_n, and 9u_n/2 = u_{n+1}. Forcing gives u_{n+1} ∈ U, N(u_{n+1}) present, and 3u_n ∉ W.

The point u_{n+1} lies in U, so a(u_{n+1}) ≥ 1, and the chain stops only when E(u_k) is absent, i.e. when u_k > 2t/3. Thus k ≥ 1 and u_0, …, u_k ∈ U. For n < k we have u_n ≤ u_k/q ≤ 2t/9, so R(u_n) is present. Since 3u_n ∉ W, we get A_n := 2u_n ∈ W.

**Step 3 (first count).** Let S₀ = {L_n, A_n : n < k}, so |S₀| = 2k.

- Owners of L_n: u_n and u_{n+1}.
- Owners of A_n (a left vertex): u_n (R), g u_n (E), and 6u_n = g u_{n+1} (N).
- g u_0 = (A+2, −1) is not a board point.

So T(S₀) ⊂ {u_0, …, u_k} ∪ {g u_1, …, g u_k}, a set of 2k + 1 elements. By 4.1(ii) all of them lie in U. Since g u_k ≤ t, we also get u_k ≤ 3t/4.

**Step 4 (second column).** For 1 ≤ n ≤ k, N(g u_n) has left endpoint g u_n/3 = 2u_{n−1} = A_{n−1} ∈ W. Let β_n = 2g u_n/3. Its possible owners are 2g u_n/9 = g u_{n−1} (R), g u_n (N, doubly covered if β_n ∈ W) and g² u_n (E).

- If β_n ∈ W, forcing requires g² u_n ∈ U with E(g² u_n) uniquely covered, so 3g²u_n/2 = 2g u_n ∉ W.
- But g² u_k = (16/9)u_k > 32t/27 > t, so β_k ∉ W.
- For n < k, g u_n ≤ g u_k/q ≤ 2t/9, so R(g u_n) = (2g u_n, 3g u_n) is present, and 3g u_n = β_{n+1}. Hence β_n ∈ W implies 2g u_n ∉ W, which implies β_{n+1} ∈ W.

At n = 1 the owner g u_0 is not a board point, so β_1 ∈ W is impossible outright; the same holds in Lemma 6.7. By backward induction from β_k ∉ W, every β_n ∉ W, and B_n := 2g u_n ∈ W for 1 ≤ n < k.

The owners of B_n are g u_n, g² u_n and g² u_{n+1}. With S₁ = S₀ ∪ {B_n}, of size 3k − 1, and g² u_k off the board, T(S₁) lies in a set of (k+1) + k + (k−1) = 3k elements. So all of them lie in U.

**Step 5 (third column; assume k ≥ 2).**

- w_n := g² u_n ≤ (32/81) u_k ≤ 8t/27 < t/3 for n ≤ k − 1, so R(w_n) is present.
- γ_k := 2w_k/3 = 3w_{k−1} is the right endpoint of R(w_{k−1}). Its other possible owners, w_k and g w_k, are off the board, so it is a leaf and γ_k ∉ W.
- For 2 ≤ n < k, N(w_n) is present because b = 2n − 2 ≥ 2, and its left endpoint w_n/3 = B_{n−1} ∈ W. If γ_n := 2w_n/3 ∈ W, forcing requires g³ u_n ∈ U with E uniquely covered, so 2w_n ∉ W, and then the present edge R(w_n) forces 3w_n = γ_{n+1} ∈ W.

By backward induction, γ_2, …, γ_k ∉ W, and C_n := 2w_n ∈ W for 1 ≤ n < k. (For n = 1 only R(w_1) is used; w_1 = 8x has no N edge.)

The owners of C_n are w_n, g³ u_n and g³ u_{n+1}. Here g³ u_1 has b = −1, and g³ u_k > t. With S₂ = S₁ ∪ {C_n}, of size 4k − 2, we get

T(S₂) ⊂ {u_0..u_k} ∪ {g u_1..g u_k} ∪ {w_1..w_{k−1}} ∪ {g³ u_2..g³ u_{k−1}},

a set of size (k+1) + k + (k−1) + (k−2) = 4k − 2. This contradicts 4.1(ii).

*Distinctness.* After dividing by 2x, the selected vertices L, A, B, C have coordinates (−1, n), (0, n), (1, n) and (2, n), which are distinct by (U).

**Step 6 (k = 1).** Here {x, 9x/2, 6x} ⊂ U with 6x ≤ t and 9x/2 > 2t/3, i.e. t < 27x/4. Also 9x/2 = (A−1, 2) needs A ≥ 2 because a ≥ 1. This set has deficiency 1: its four edges (listed in §3) are covered by two vertices and contain a matching of size 2. Criticality forces U to equal it. ∎

**Corollary 5.3.** Let 𝒜_j = C_j minus the exceptional root, if that root has colour j. Then ν(B(V)) ≥ |V| for every V ⊂ 𝒜_j with a(v) ≥ 1 for all v ∈ V.

*Proof.* If d(V) > 0, choose a positive-deficiency subset of V that is minimal under inclusion. It is critical, so by Lemma 5.2 it contains an isolate or a patch root of colour j. That root is the unique exceptional root by Lemma 3.1, which is excluded from 𝒜_j. ∎

## 6. Tight sets touching the vertical axis

From here on, U ⊂ 𝒜_j is an inclusion-minimal maximiser of D*_j := max_{V⊂𝒜_j} d(V) > 0. In particular U is tight, and W is a minimum vertex cover of B(U).

**Lemma 6.1 (two roots).** U contains a point with b = 0 and a point with a = 0.

*Proof.* The N edges of distinct owners are disjoint: the left endpoint u/3 and the right endpoint 2u/3 each determine u. So if every point of U had b ≥ 1, then ν ≥ |U|. If every point had a ≥ 1, Corollary 5.3 would give d ≤ 0. ∎

Let x = 2^A be the least element of U with b = 0, and y = 3^B the least with a = 0.

- **Case (O):** 1 ∈ U. Then x = y = 1 and j = 0.
- Otherwise A, B ≥ 1. As in Step 1 of Lemma 5.2 (Lemma 5.1 applies to every u with a, b ≥ 1), every u ∈ U lies in the cone of an axis element of U. Axis elements of the same colour differ by powers of 8 = g²q on the horizontal axis and 27 = gq² on the vertical axis, so

  **(6.1)  U ⊂ x⟨g,q⟩ ∪ y⟨g,q⟩.**

Since c(x) = c(y), we have A ≡ −B (mod 3). So r := (2A − B)/3 and s := (2B − A)/3 are integers, with A = 2r + s, B = r + 2s, and y = x g^{−r} q^{s}.

**Lemma 6.2 (root balance).** In case not-(O), r ≥ 0 and s ≥ 0.

*Proof.*

*If r < 0 (i.e. B > 2A).* Then x = y g^{r} q^{−s} has negative coordinates relative to y, so the y-cone lies inside the x-cone, and U ⊂ x⟨g,q⟩. Let u_n = x q^n for n ≤ A. Then u_A = 3^{2A} < 3^B = y ≤ t. For n < A we have a(u_n) = A − n ≥ 1 and u_n ≤ 3^{2A}/q ≤ 2t/9, so E(u_n) is present. Its right endpoint u_n/2 has possible owners with g-coordinate −1, so it is a leaf. Forcing at 3u_n/2, exactly as in Step 2 of Lemma 5.2, gives u_{n+1} ∈ U. Hence 3^{2A} ∈ U is an element with a = 0 smaller than y, a contradiction.

*If s < 0 (i.e. A > 2B).* Now the x-cone lies inside the y-cone. Let v_i = y g^i for i ≤ B. For i < B, N(v_i) is present (b = B − i ≥ 1). Its left endpoint v_i/3 has possible owners v_i/6 and 2v_i/9, which have q-coordinate −1 relative to y, so it is a leaf. Hence 2v_i/3 ∈ W. At 2v_i/3 the possible owners are 2v_i/9 (not in U), v_i (uniquely covered) and 4v_i/3 = v_{i+1}. Forcing gives v_{i+1} ∈ U. Hence 2^{2B} = v_B ∈ U is an element with b = 0 smaller than x, a contradiction. ∎

The remaining cases are:

- **(D1)** s = 0, r ≥ 1, so x = 4^B and y = 3^B;
- **(D2)** r = 0, s ≥ 1, so y = 9^A;
- **(I)** r, s ≥ 1.

For a point p = x g^m q^n, its coordinates relative to y are (m + r, n − s). So **p lies in neither cone if m < 0 and n < s.**

**Lemma 6.3 (augmentation).** Let P ⊂ 𝒜_j ∖ U, and let R be a set of points such that W ∪ R covers B(U ∪ P). Then |P| ≤ |R|.

*Proof.* d(U ∪ P) ≥ |U| + |P| − |W| − |R| = D* + |P| − |R|, and this is at most D* by maximality. ∎

Let f(k) = #{(a, b) ∈ ℤ²_{≥0} : a + 2b = k}. Then f(k) = ⌊k/2⌋ + 1 for k ≥ 0, and f(k) = 0 for k < 0. The same count holds for 2a + b = k. So f(k) − f(k−1) is 1 for even k ≥ 0 and 0 otherwise. For an integer A ≥ 0,

**(6.2)  Σ_{n≥1} [f(2A − 3n) − f(2A − 3n − 1)] = #{even n ≥ 2 : 3n ≤ 2A} = ⌊A/3⌋.**

**Lemma 6.4 (P1).** In case (D1), B ≤ 2.

*Proof.* Here x = y g^{r} with r = B, so U ⊂ y⟨g,q⟩.

1. *Frontier.* The chain argument of Lemma 6.2's second case, run for i < B, gives v_i ∈ U, 2v_i/3 ∈ W and v_B = x ∈ U. The edge E(x) is present (it was forced), so x ≤ 2t/3. Put k = a + 2b. The points 2v_i/3 = (2i+1, B−i−1), for i < B, are all the lattice points on the diagonal k = 2B − 1. Every y-cone point satisfies k = 2B + 3n ≥ 2B.
2. *The sets P and R.* Let P be all lattice points on k = 2B − 3n (n ≥ 1), and R all lattice points on k = 2B − 3n − 1 (n ≥ 1).
   - Since 2^a3^b ≤ 2^k ≤ 2^{2B−3} = x/8 ≤ t/12, all of these points lie on the board. P points are smaller than 4t/27, so none is e.
   - Their colour is a − b ≡ k ≡ 2B ≡ −B = c(y), so P ⊂ 𝒜_j. They lie below the cone, so P is disjoint from U.
3. *Covering.* For an owner p ∈ P on diagonal k, the right endpoints of its edges are:
   - N: 2p/3 = (a+1, b−1), on diagonal k − 1;
   - E: p/2 = (a−1, b), on k − 1;
   - R: 3p, on k + 2.

   The diagonal k − 1 belongs to R. The diagonal k + 2 is the frontier 2B − 1 when n = 1, which lies in W, and belongs to R when n ≥ 2.
4. *Count.* Lemma 6.3 and (6.2) with A = B give ⌊B/3⌋ ≤ 0. ∎

**Lemma 6.5 (P2).** In case (D2), A ≤ 2.

*Proof.* Here y = x q^{A}, so U ⊂ x⟨g,q⟩.

1. *Frontier.* For u_n = x q^n with n < A, we have a = A − n ≥ 1 and u_n ≤ y/q ≤ 2t/9. So E(u_n) is present, and its right endpoint is a leaf (both other owners have g-coordinate −1). Forcing gives 3u_n/2 ∈ W and u_{n+1} ∈ U. Put k = 2a + b. The points 3u_n/2 = (A−n−1, 2n+1), for n < A, are all the lattice points on k = 2A − 1. Every x-cone point satisfies k = 2A + 3m ≥ 2A.
2. *The sets P and R.* Let P be all lattice points on k = 2A − 3n, and R all lattice points on 2A − 3n − 1 (n ≥ 1). Since 2^a3^b ≤ 3^k ≤ 3^{2A−3} = y/27 ≤ t/27, all of these lie on the board, and none is e. Their colour is a − b ≡ −k ≡ A = c(x).
3. *Covering.* The left endpoints of an owner p's edges are:
   - N: p/3, on diagonal k − 1;
   - E: 3p/2 = (a−1, b+1), on k − 1;
   - R: 2p = (a+1, b), on k + 2.

   These lie in R, or in the frontier when n = 1, as in P1.
4. *Count.* (6.2) gives ⌊A/3⌋ ≤ 0. ∎

**Lemma 6.6 (incomparable case).** In case (I):

- (a) y > t/3;
- (b) r ∈ {1, 2};
- (c) y is the only point of U on the vertical axis, so j = j_top := −⌊log₃ t⌋ mod 3;
- (d) d(U) = 1;
- (e) with u_n = x q^n and z = u_s = y g^r = 2^{2r}3^{2s}: z ≤ 2t/3, and for n < s, u_n, g u_{n+1} ∈ U, 3u_n/2, 2u_n ∈ W, and 3u_n ∉ W.

*Proof.*

**Vertical chain.** Let v_i = y g^i = x g^{i−r} q^{s} for i ≤ r. For i < r, N(v_i) is present (b = B − i > 0). The other owners of v_i/3 are x g^{i−r−1}q^{s−1} and x g^{i−r}q^{s−1}. Each has m < 0 and n < s, so by the remark before Lemma 6.3 neither is in U, and v_i/3 is a leaf. Forcing as in Lemma 6.2 gives 2v_i/3 ∈ W, v_{i+1} ∈ U, and 2v_i ∉ W. The edge E(z) is present, so z ≤ 2t/3.

**Horizontal chain.** For n < s, a(u_n) = A − n ≥ 2r + 1 ≥ 3 and u_n ≤ z/q ≤ 4t/27, so E(u_n) is present. The other owners of u_n/2 are x g^{−1}q^{n−1} and x g^{−1}q^{n}, which have m < 0 and n′ < s, so u_n/2 is a leaf. Forcing gives 3u_n/2 ∈ W, u_{n+1} ∈ U and 3u_n ∉ W. The edge R(u_n) is present (3u_n ≤ 4t/9), so 2u_n ∈ W.

Let S_H = {3u_n/2, 2u_n : n < s}, a set of 2s left vertices. Its owners lie in H := {u_0..u_s} ∪ {g u_1..g u_s}, a set of 2s + 1 elements (g u_0 has b = −1). By 4.1(ii), H ⊂ U. This proves (e).

**Rooted vertical edges.** Let h be the largest i < r with 3v_i ≤ t, if one exists. For i ≤ h, R(v_i) is present and 2v_i ∉ W, so 3v_i ∈ W. Let S_V = {2v_i/3 : i < r} ∪ {3v_i : i ≤ h}, a set of r + h + 1 right vertices.

- Owners of 2v_i/3: v_i and v_{i+1}. (The third candidate, v_i/q, lies in neither cone.)
- Owners of 3v_i: v_i, q v_i and q v_{i+1}.
- q v_0 = 9y/2 has a = −1.

The vertices of S_H are left and those of S_V are right, so the two sets are disjoint. Within each set the vertices are distinct by (U). So T(S_V) lies in a set of (r + 1) + (h + 1) elements, and by 4.1(ii) all of them lie in U. In particular q v_{h+1} ≤ t, so 3v_{h+1} ≤ 2t/3. By the maximality of h this forces h + 1 = r. Hence q z ∈ U and z ≤ 2t/9.

**The deep case is impossible.**

1. E(g z) = (2z, 2z/3) is present, because 2z ≤ t. Its right endpoint is 2z/3 = 3u_{s−1} ∉ W, so 2z ∈ W.
2. N(q z) = (3z/2, 3z) has left endpoint 3z/2 = 2v_{r−1} ∉ W, so 3z ∈ W.
3. Let S = S_H ∪ S_V ∪ {2z, 3z}, which has 2s + 2r + 2 elements. The two new vertices are distinct from all the earlier ones:
   - 2z = 2u_s, and 3u_n/2 = 2u_s is impossible;
   - 3z = 3v_r, and 2v_i/3 = 3v_r would force v_i > v_r.
4. Let V = {v_0..v_r} ∪ {q v_1..q v_r}. In x-coordinates its elements have m ≤ 0, while elements of H have m ∈ {0, 1} and n ≤ s. So H ∩ V = {z}, and |H ∪ V| = 2s + 2r + 1.
5. The owners of 2z are z, g z and 6z. The owners of 3z are z, q z and 6z. So T(S) ⊂ H ∪ V ∪ {6z}, whose size is at most |S|. This contradicts 4.1(ii).

**Conclusion.** So no rooted vertical edge exists. That means 3y > t, which is (a). Then g^r = z/y < (2t/3)/(t/3) = 2, so r ≤ 2, which is (b). The next same-colour power of 3 is 27y > t, which gives (c). Finally, Corollary 5.3 gives d(U ∖ {y}) ≤ 0, and Lemma 2.3 then gives (d). ∎

**Lemma 6.7 (cap).** In case (I), if s ≥ 2 then g² z ≤ t.

*Proof.* Suppose g² z > t.

**First column.** For 1 ≤ n ≤ s, N(g u_n) has left endpoint 2u_{n−1} ∈ W. Let β_n = 2g u_n/3, whose possible owners are g u_{n−1}, g u_n and g² u_n.

- If β_n ∈ W, forcing gives g² u_n ∈ U and 2g u_n ∉ W. At n = s this is impossible, because g² u_s > t.
- For n < s, g u_n ≤ g z/q ≤ 16t/81, so R(g u_n) is present, and β_n ∈ W implies 3g u_n = β_{n+1} ∈ W.

By backward induction, every β_n ∉ W, and 2g u_n ∈ W for 1 ≤ n < s. Let S₁ be these vertices together with S_H, so |S₁| = 3s − 1. Its owners lie in H ∪ {g² u_1..g² u_{s−1}}, a set of size 3s. So all of them lie in U.

**Second column.** For n ≤ s − 1, g² u_n ≤ 32z/81 ≤ 64t/243 < t/3, so R(g² u_n) is present.

- γ_s = 3g² u_{s−1} is a leaf, because its other owners g² u_s and g³ u_s are off the board. So γ_s ∉ W.
- For 2 ≤ n < s, N(g² u_n) is present and has left endpoint 2g u_{n−1} ∈ W. If γ_n = 2g² u_n/3 ∈ W, forcing gives 2g² u_n ∉ W, and then γ_{n+1} ∈ W.

By backward induction, 2g² u_n ∈ W for 1 ≤ n < s. Let S₂ = S₁ ∪ {2g² u_n}, so |S₂| = 4s − 2. Its owners lie in

H ∪ {g² u_1..g² u_{s−1}} ∪ {g³ u_2..g³ u_{s−1}},

a set of size 4s − 2. (g³ u_1 has b = −1, and g³ u_s > t.) This contradicts 4.1(ii). The selected vertices are distinct by (U): after dividing by 2x their g-coordinates are −1, 0, 1 and 2. ∎

**Lemma 6.8 (case (I) windows).** In case (I), t lies in one of the intervals [54, 72), [216, 243), [576, 648) or [5184, 5832), provided the prefix bound s ≤ 3 holds when r = 1. That bound is Lemma 6.9.

*Proof.* Throughout, y ≤ t < 3y by Lemma 6.6(a).

- **r = 2.** Here z = g² y > 16t/27, so g² z > t, and Lemma 6.7 forces s = 1. Then x = 32, y = 81 and z = 144. The conditions z ≤ 2t/3 and y ≤ t < 3y give [216, 243).
- **r = 1: first, z > t/2.** Suppose z ≤ t/2. Then E(g z) is present, and its right endpoint 3u_{s−1} is not in W, so 2z ∈ W. The other possible owners of 2z are z, whose R edge needs 3z ≤ t but z = g y > 4t/9, and 6z > t. So 2z uniquely covers edges of only one owner, which contradicts 4.1(i).
- **r = 1, the windows.** Here z = 4·9^s and z ≤ 2t/3 < 2z.
  - s = 1 gives [54, 72).
  - s ≥ 2: Lemma 6.7 gives t ≥ g² z = 64·9^{s−1}, so t ∈ [64·9^{s−1}, 8·9^s). With s ≤ 3 this gives [576, 648) and [5184, 5832). ∎

**Lemma 6.9 (P4).** In case (I) with r = 1, s ≤ 3.

*Proof.* We have A = s + 2, B = 2s + 1 and y = 3^{2s+1}. Put k = 2a + b and k₀ = 2A.

1. *Only y is below the cone line.* The x-cone points have k = k₀ + 3m ≥ k₀. A y-cone point y g^{m′}q^{n′} = x g^{m′−1}q^{n′+s} has k < k₀ only if m′ = 0, and then a = −n′ ≥ 0 forces it to be y. So U ∩ {k < k₀} = {y}, and k(y) = k₀ − 3.
2. *The sets P and R.* Let P₀ be all lattice points on the diagonals k₀ − 3n (n ≥ 1), let P = P₀ ∖ {y}, and let R be all lattice points on k₀ − 3n − 1 (n ≥ 1).
   - All these points have colour j and lie on the board, since each is at most 3^k ≤ y.
   - Points of P on k₀ − 3 have a ≥ 1, so they are at most 2·3^{k₀−5} = 2y/9 = z/6 ≤ t/9. Lower diagonals give points at most y/27. Hence no point of P equals e, which exceeds 4t/27.
   - P is disjoint from U by step 1.
3. *Covering.* For a new owner p, the left endpoints of N(p) and E(p) lie on k − 1, which belongs to R. The left endpoint 2p of R(p) lies on k + 2: that diagonal belongs to R when n ≥ 2, and is k₀ − 1 when n = 1.
   - When n = 1, p ≠ y has a(p) ≥ 1, so a(2p) ≥ 2.
   - The lattice points of k₀ − 1 with a ≥ 2 are exactly the 3u_n/2 = (A−n−1, 2n+1) with n < s, which lie in W by Lemma 6.6(e).

   So W ∪ R covers B(U ∪ P). The frontier point 2y, with a = 1, is never needed: its only owner on these diagonals is y ∉ P.
4. *Count.* By (6.2), |P| − |R| = ⌊A/3⌋ − 1 = ⌊(s − 1)/3⌋. Lemma 6.3 gives s ≤ 3. ∎

**Lemma 6.10 (mandatory owners, t ≥ 18).** Let U be as at the start of §6, and suppose U is not in case (I). Then:

- if j = 0, then 6 ∈ U;
- if j = 1, then 12 ∈ U;
- if j = 2, then 18 ∈ U.

*Proof.* By Lemmas 6.2, 6.4 and 6.5, the possible cases are (O); (D1) with B ∈ {1, 2}; and (D2) with A ∈ {1, 2}. Their colours are c(x) = A mod 3:

| case | colour |
|---|---|
| (O) | 0 |
| (D2), A = 1 (x = 2, y = 9) | 1 |
| (D1), B = 2 (x = 16, y = 9) | 1 |
| (D2), A = 2 (x = 4, y = 81) | 2 |
| (D1), B = 1 (x = 4, y = 3) | 2 |

We treat each in turn.

- **(O).** R(1) = (2, 3) is present. The owners of 2 are 1 and 6, and the owners of 3 are 1 and 6. If both 2 and 3 were in W, R(1) would be doubly covered, and each of them would uniquely cover edges of at most the single owner 6, contradicting 4.1(i). So exactly one of them is in W. It must uniquely cover R(1) and an edge of 6, so 6 ∈ U.
- **(D2), A = 1.**
  1. E(2) = (3, 1) is present, and 1 is a leaf, so 3 ∈ W.
  2. Forcing at 3, whose owners are 2 and 9, gives 9 ∈ U and 6 ∉ W.
  3. R(2) = (4, 6) is present, so 4 ∈ W. The owners of 4 are 2 and 12.
  4. Applying 4.1(ii) to S = {3, 4} gives |{2, 9, 12} ∩ U| ≥ 3, so 12 ∈ U.
- **(D1), B = 2.** The forced chain v_0 = 9, v_1 = 12 (Lemma 6.4, step 1) gives 12 ∈ U.
- **(D2), A = 2.** The forced chain u_0 = 4, u_1 = 18 (Lemma 6.5, step 1) gives 18 ∈ U.
- **(D1), B = 1.**
  1. N(3) = (1, 2), and the left vertex 1 is a leaf, so 2 ∈ W.
  2. Forcing at 2, whose owners are 3 and 4, gives 4 ∈ U and 6 ∉ W.
  3. R(3) = (6, 9) is present because t ≥ 18 ≥ 9, so 9 ∈ W.
  4. The owners of 9 are 3 and 18, the latter through E(18) = (27, 9), which is present only if t ≥ 27.
  5. Apply 4.1(ii) to S = {2, 9}. If t < 27, the owners are contained in {3, 4}, a contradiction, so this case does not occur. If t ≥ 27, the owners are contained in {3, 4, 18}, which forces 18 ∈ U. ∎

Note that {6, 12, 18} = T(6) is a corner for t ≥ 18, and its points have colours 0, 1 and 2.

## 7. Assembly for t ≥ 18

**Lemma 7.1 (common optimum).** There is a minimum cover F such that, for every colour j, the set (C_j ∖ F) ∩ 𝒜_j attains D*_j.

*Proof.*

- If no exceptional root exists, every minimum cover works, by Lemma 2.2.
- Otherwise let j_e be the colour of e. By Lemma 2.3, D* ≥ D − 1, where D = D_{j_e} and D* = D*_{j_e}.
  - *If D* = D:* take a maximiser V ⊂ 𝒜_{j_e} and a minimum vertex cover W* of B(V). The cover F = (C_{j_e} ∖ V) ∪ W* has size K_{j_e} − D = τ, so it is a minimum cover, and C_{j_e} ∖ F = V.
  - *If D* = D − 1:* every minimum cover F has d(C_{j_e} ∖ F) = D > D*, so e ∈ C_{j_e} ∖ F, and removing e leaves deficiency ≥ D − 1 = D*.

  In either case the other colours are handled by Lemma 2.2. ∎

**Theorem 7.2.** For t ≥ 18, τ ≥ M.

*Proof.* Suppose τ < M.

1. For every j, D_j = K_j − τ > K_j − Q_j = δ_j. Lemma 2.3 then gives D*_j ≥ D_j − δ_j > 0.
2. Take F as in Lemma 7.1. In each colour, choose an inclusion-minimal maximiser U_j ⊂ (C_j ∖ F) ∩ 𝒜_j.
3. By Lemma 6.6(c), only the colour j_top can be in case (I). Lemma 6.10 then gives m_j ∉ F for each j ≠ j_top, where (m_0, m_1, m_2) = (6, 12, 18).
4. If U_{j_top} were not in case (I), Lemma 6.10 would also give m_{j_top} ∉ F. Then F would miss the corner {6, 12, 18}. So U_{j_top} is in case (I), and D*_{j_top} = 1 by Lemma 6.6(d).
5. Then D_{j_top} ≤ D*_{j_top} + δ_{j_top} = 1 + δ_{j_top}. Combined with D_{j_top} > δ_{j_top}, this gives τ = Q_{j_top} − 1. Since τ < Q_j for all j, Q_{j_top} = M.
6. But by Lemma 6.8, t lies in one of the windows of §8, where Q_{j_top} > M. This is a contradiction. ∎

## 8. The five windows (the only computation for t ≥ 18)

All windows are left-closed and right-open. In each window:

- No 3-smooth number lies strictly inside it.
- Every isolate or patch endpoint is 3-smooth: isolate windows are [2^A, 3·2^{A−1}) and patch windows are [3·2^{A+1}, 27·2^{A−2}). So K, I and P are constant on the window.

The row widths (w_0, w_1, …) at the left endpoint give K, by counting a ≡ b + j (mod 3) row by row.

| window | row widths | K | δ | Q | j_top | Q_top > M? |
|---|---|---|---|---|---|---|
| [54, 64) | 6,5,3,2 | (6,5,5) | – | (6,5,5) | 0 | 6 > 5 |
| [64, 72) | 7,5,3,2 | (7,5,5) | isolate 64 (colour 0) | (6,5,5) | 0 | 6 > 5 |
| [216, 243) | 8,7,5,4,2 | (9,8,9) | – | (9,8,9) | 2 | 9 > 8 |
| [576, 648) | 10,8,7,5,3,2 | (12,12,11) | isolate 512 (colour 0) | (11,12,11) | 1 | 12 > 11 |
| [5184, 5832) | 13,11,10,8,7,5,3,2 | (20,19,20) | isolate 4096 (colour 0) | (19,19,20) | 2 | 20 > 19 |

The top colour is j_top = −⌊log₃t⌋ mod 3, with ⌊log₃t⌋ = 3, 3, 4, 5, 7 respectively. To reproduce: `python -c "from shapes import sturm_rows; from eta_rule import Q_vector; print([(t, sturm_rows(t), Q_vector(t)) for t in (54,64,216,576,5184)])"`.

## 9. The cases 3 ≤ t < 18

- **3 ≤ t < 9.** The corners are T(1) and, for t ≥ 6, T(2). The point 2 meets both. T(1) exists, so τ = 1.
- **9 ≤ t < 18.** The corners are rooted at 1, 2, 3, and at 4 when t ≥ 12. The set {3, 4} meets all of them. The corners T(1), T(2) and T(3) have empty common intersection, so τ ≥ 2, and τ = 2.

The formula gives M = 1 on [3, 9) and M = 2 on [9, 18). On [12, 27/2) this holds under both patch conventions: K = (3, 3, 2), and the A = 1 patch gives (3, 2, 2).

## 10. Conclusion and consequences

By Lemma 3.2, Theorem 7.2 and §9:

**Theorem (C).** For every real t ≥ 3, τ(t) = min_j (K_j − I_j − P_j). For 1 ≤ t < 3, τ(t) = 0.

The consequences then follow unconditionally:

- the increment table and η rule (`REPORT.md` §4);
- the identity c = 1 − (1/3) Σ η_{a,b}/(2^a3^b) = 1 − (1/3) ∫ τ t^{−2} dt (`REPORT.md` §5, proved there in full);
- the gauge form c = 757/972 + (2/9) ∫₃^∞ H(Ŝ) t^{−2} dt;
- the certified enclosure of c to 128 digits (`REPORT.md` §6).

## 11. Precise list of what a verifier must check

1. **Lemma 2.1.** The owner lists are the only place where the arithmetic of 2 and 3 enters.
2. **Every forcing step.** The "other possible owners" must lie outside U. Membership is decided by (U) and the cone inclusion: either the remark before Lemma 6.3, or the single-cone inclusions in D1 and D2.
3. **The owner counts.** Lemma 5.2 steps 3–5, Lemma 6.6, Lemma 6.7, and the distinctness of the selected vertices.
4. **The numeric availability bounds.** 2t/9, 4t/27, 8t/27, 16t/81, 64t/243 and 32t/27.
5. **The augmentation lemmas 6.4, 6.5 and 6.9.**
   - Endpoint diagonals: k − 1 for N and E, k + 2 for R.
   - The board and e-exclusion bounds: x/8, y/27, z/6.
   - The missing frontier point 2y in Lemma 6.9.
6. **The quantifier structure of §7.** The covers W used inside the lemmas belong to each U_j separately. Only U_j ⊂ C_j ∖ F is used for the collision.
7. **The finite tables of §8 and §9.**

No step uses matching submodularity, hole-freeness, disjoint augmenting paths, or the false normalisation "some optimum contains a vertical phase".

**Remaining gaps.** For part (i), there is no mathematical gap left, provided items 1–7 above survive the reader's checks. This document has not been externally reviewed or formalised in Lean.

## 12. Audit log (2026-11-08)

**Machine-checked identities.** `python symbolic_audit.py` runs 101 checks. They cover every exponent identity, owner list, colour/side assignment, cone-coordinate claim, availability ratio and diagonal claim used in §§2–6. The identities are checked as exact symbolic vector equalities in sympy, with symbolic A, B, n, i, k, r, s. So they hold for all parameter values, not just sampled ones. The ratio bounds are exact rationals. The only exhaustive-range check is (6.2) for A < 500; the text proves it in general (even n with 3n ≤ 2A).

**Adversarial re-read, step by step.** The following were re-checked by hand:

- **(a) Alternatives outside both cones.** Every forcing step's "other possible owners" lie outside both cones. The remark before Lemma 6.3 covers case (I). The single-cone inclusions cover Lemma 6.2 and D1/D2.
- **(b) Two owners needed.** Every forcing at a doubly covered vertex needs both remaining owners, because 4.1(i) needs two distinct uniquely covered owners. This is what makes the backward inductions go in the stated direction.
- **(c) Expansion counts at the boundary.** The counts are checked at the boundaries n = 1, k = 2 and s = 2, using the nonsmooth bottoms g u_0, g³ u_1, q v_0 and the off-board caps.
- **(d) Pool bookkeeping in §7.** D*_j ≥ D_j − δ_j holds because only the exceptional colour has a smaller pool.
- **(e) Complete case list.** Lemma 6.10 covers all cases: r = s = 0 forces x = 1.
- **(f) Lemma 7.1.** It is used only through U_j ⊂ C_j ∖ F. The vertex covers W inside the lemmas are chosen separately for each U_j.

The one error found was a wrong row-width list for t = 216 in §8. The K-vector in the table was already correct, and the list is now fixed.

**What is and is not established.**

- Given the checks above, Theorem (C) and the determination of c in `REPORT.md` §5 follow with no further hypothesis.
- No other theorem is needed for part (i).
- Two things have not happened: independent human review, and formalisation in Lean.

**Independent audit (fresh context).** An independent referee pass, with no access to this session's reasoning, re-derived §§2–9 by hand. It wrote its own solvers in `audit/`, sharing no code with the parent folder:

- an exact column DP, checked against brute force; it matches the formula at all 336 breakpoints in [3, 3·10⁹];
- an exhaustive search of tight sets for t ≤ 2200, and of every S ⊂ W for t ≤ 400;
- a MILP search over 152 maximisers for t ≤ 60000.

Verdict: every lemma PASS, no error, no gap. The case-(I) maximisers occur exactly at t = 54, 64, 216, 576 and 5184, so every window in §8 is realised and the bound s ≤ 3 in Lemma 6.9 is sharp. The referee's six presentational notes have been applied above where they change the text: the T(S) = ∅ case, the distinctness of S_H and S_V, a(u_n) ≥ 2r + 1, and the n = 1 base case. Full report: `audit/AUDIT.md`.
