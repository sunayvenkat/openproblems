# Global hole filling for the Erdős 168 matching reduction

This note proves a global normalization of the removed-label set U. It does **not** prove the patched finite-cover formula or its irrationality consequence. The matching reduction and notation are in [cover.md](<cover.md>). The arguments below are deductions of this research round; no priority claim is made.

## Can the local honeycomb filling rule be extended to a whole polyhex?

### Takeaway

Yes. A finite connected region V of m omitted faces, whose complementary boundary edges are already present, can be filled without decreasing deficiency. If the region has h holes, the stronger inequality is

```
nu(B(U union V)) - nu(B(U)) <= m - floor(h/2),
d(U union V) >= d(U) + floor(h/2),
```

where `d(U)=|U|-nu(B(U))` and U and V are disjoint.

### Cited Findings

- Removing one color from the triangular lattice gives the honeycomb graph used in the established matching reduction. Each omitted-color label owns the three alternating edges opposite it in the three upward corner triangles. [Existing reduction and local filling proof](<cover.md>)

### Inferences

**Precise setting.** Embed exponent coordinates in the triangular lattice, with the positive coordinate directions at angle 60 degrees. Fix color `j=a-b mod3`. The omitted-color face centers form the infinite lattice

```
F_j = {(a,b) in Z^2 : a-b = j mod3}.
```

Their six face-adjacency steps are

```
(-1,-1), (2,-1), (-1,2), (1,1), (-2,1), (1,-2).
```

In numerical labels these are multiplication by `1/6,4/3,9/2,6,3/4,2/9`. Every honeycomb edge is owned by exactly one of its two incident faces, according to the unique upward corner using that edge. At any honeycomb vertex, its three incident edges are owned by its three incident faces, one each.

Let V be any nonempty finite face-connected subset of `F_j`, disjoint from U. Its union of hexagons is the region R. Assume:

1. Every face in V has all three owned corner edges available in the finite domain.
2. Every boundary edge of R whose owner is outside V has that owner in U, so that edge is already in `B(U)`.

These assumptions allow concave boundary vertices, multiple boundary cycles, and existing U islands inside holes. They do not require a simply connected region. Let m be the number of faces, h the number of bounded complementary components of R, I the number of honeycomb vertices interior to R, B the number of boundary vertices, and `E_int` the number of edges incident to two V faces.

**Boundary matching.** At a boundary vertex exactly one or two incident faces belong to V. In either case exactly one of the two boundary edges at that vertex has its owner outside V. Therefore the old boundary edges form a perfect matching P of all B boundary vertices. In particular B is even, and there are `B/2` old boundary edges and `B/2` new boundary edges.

Every boundary vertex has degree two in the boundary graph. Since any two honeycomb faces meeting at a vertex also share an edge, there are no pinched boundary vertices: the boundary is a disjoint union of simple cycles. Thus the number of boundary edges is also B.

**Euler count.** Every internal edge is owned by a V face. Counting newly added edges and applying Euler's formula to the connected cell complex gives

```
3m = E_int + B/2,
(I+B) - (E_int+B) + m = 1-h.
```

Hence

```
E_int = m+I-1+h,
I+B/2 = 2m+1-h.
```

**Matching replacement.** Take a maximum matching M after filling V. Write `M_out` for all edges of M that are not in the one-skeleton of R. This includes edges lying in holes, not only edges in the unbounded exterior. All these edges were already in `B(U)`. No interior vertex of R can be incident to such an edge.

Fix `M_out`. Let b of the B boundary vertices remain unoccupied by it. All I interior vertices remain unoccupied. The part of M on the one-skeleton of R therefore has size at most

```
floor((I+b)/2).
```

Delete from the old perfect boundary matching P every edge touching an occupied boundary vertex. At most `B-b` edges are deleted, leaving at least

```
max(0,b-B/2)
```

old edges compatible with `M_out`. This reasoning remains valid if an outside edge uses two boundary vertices, and if it lies inside a hole.

Thus M can be replaced by a matching in `B(U)` with loss at most

```
floor((I+b)/2) - max(0,b-B/2)
    <= floor((I+B/2)/2)
     = m-floor(h/2).
```

For `b<=B/2`, the inequality follows by increasing b to `B/2`. For `b>=B/2`, its left side is `floor((I+B-b)/2)`, which decreases with b. This proves both asserted inequalities.

### Gaps

There is no gap in this conditional filling statement. It does not apply to an arbitrary boundary-attached missing region: its old complementary boundary edges may be absent, and its owned corners may be truncated. Those hypotheses must not be omitted.

## Does the lemma really fill every bounded complement hole in the weighted triangle?

### Takeaway

Yes. Any finite connected component of the complement of U in the full face lattice automatically lies safely inside the finite board and satisfies the filling hypotheses. Consequently an optimal removed-label set can be chosen with no bounded complement holes.

### Cited Findings

- The finite label board is `C_j(t)={(a,b)>=0:2^a3^b<=t, a-b=j mod3}`. The objective is to maximize `d(U)` over subsets of this board. [Finite matching objective](<../open-conjecture-transfer-search/168_grid.md>)

### Inferences

Let `U subset C_j(t)` be finite and V a finite connected component of `F_j\U`. Every face adjacent to V but outside V must belong to U, by the definition of a complement component. In particular the outside owners of all complementary boundary edges are in U.

The following extremal arguments verify that V lies in the finite board, with enough margin for every owned corner to exist:

- Choose a point of V with smallest a. Its neighbor with step `(-2,+1)` is outside V, hence in U. Therefore `min_a(V)>=min_a(U)+2>=2`.
- Choose a point of V with smallest b. The neighbor with step `(+1,-2)` gives `min_b(V)>=min_b(U)+2>=2`.
- Choose the largest numerical value v in V. Its neighbor `6v` is outside V, hence in U. Therefore `max_value(V)<=max_value(U)/6<=t/6`.

In particular every label in V has positive a and b and is at most `t/6`; all six vertices of each associated hexagon, and all three owned corners, are present. Thus the global filling lemma applies to every finite complement component. The case U empty has no finite complement component.

Choose a maximizer of d over `U subset C_j(t)` and, among maximizers, one of largest cardinality. If it had a finite complement component V, filling it would not decrease d and would increase cardinality, a contradiction. Thus this maximizer has no finite complement component. The triangular face lattice has one end: outside a sufficiently large hexagonal box containing U its complement is connected. Hence the full-plane complement of this maximizer is connected.

The same conclusion holds when U is required to avoid the vertical axis. In that case `min_a(U)>=1`, so every filled hole has `min_a(V)>=3` and remains within the allowed class.

As a precise finite-board consequence, every component of `C_j(t)\U` touches the face-adjacency boundary of the board. That boundary consists of labels satisfying at least one of

```
a<=1,  b<=1,  6*2^a3^b>t.
```

Indeed a label with a,b>=2 and `6*2^a3^b<=t` has all six face neighbors in the board; conversely each displayed failure supplies an outside neighbor. This is a topological boundary-contact assertion, not yet a matching-deficiency estimate.

### Gaps

The argument excludes bounded complement holes; it does not exclude channels attached to the board boundary. It does not say that U itself is supported only near the boundary.

## What exact boundary problem remains after filling holes?

### Takeaway

The unrestricted matching optimization reduces to disjoint, simply connected polyhex components touching the horizontal axis. This is a genuine global normalization of U, but the numerical bound on their deficiency is still missing.

### Cited Findings

- If a label is divisible by 3, its north-parent edge `{u/3,2u/3}` exists, and all such edges form a matching. [North-parent baseline and desired Hall bound](<../open-conjecture-transfer-search/168_grid.md>)
- The root edges must supply the augmentation count derived from the exact N/E path formula. [Remaining augmentation bound](<cover.md>)

### Inferences

Start with a maximum-deficiency U whose full-plane complement is connected, as above. Let `U_1,...,U_k` be its face-connected components. Each component is simply connected: a hole in one component would also trap a finite component of the full complement. Its geometric boundary is therefore a single simple honeycomb cycle.

The graphs `B(U_i)` have disjoint vertex sets. Every owned edge lies on its owner's hexagon, and two honeycomb faces sharing any vertex necessarily share an edge. Thus different face-connected components cannot contribute edges incident to a common vertex. Consequently

```
nu(B(U)) = sum_i nu(B(U_i)),
d(U) = sum_i d(U_i).
```

No component of a maximizing U has negative deficiency, since deleting it would increase d. Delete the zero-deficiency components as well. This preserves the maximum and leaves the complement connected: each removed finite component attaches to the existing complement along its boundary. Every remaining component has positive deficiency.

If a component contains no horizontal-axis label, every label in it has b>=1. Its north-parent edges are a matching of size `|U_i|`, implying `d(U_i)<=0`, a contradiction. Therefore there exists a maximizer for which every nonempty component is:

1. face-connected and simply connected;
2. of positive deficiency;
3. incident to the horizontal axis b=0.

This statement also holds under the restriction that U avoid the vertical axis. For an unrestricted maximizer, the component containing label 1 may meet both axes.

For a color j minimizing the proposed patched cover bound, the exact remaining obligation is therefore

```
sum_i d(U_i) <= delta_j = I_j(t)+P_j(t)
```

for disjoint simply connected positive-deficiency components of this form. Equivalently, on each component retain the earlier quantities r_i, q_i, o_i for the N/E path subgraph. The root edges must provide enough additional matching edges that

```
sum_i [(r_i+q_i-o_i)/2
       - (nu(B(U_i))-nu_NE(B(U_i)))] <= delta_j.
```

The isolated horizontal-axis label and the known three-face patch satisfy this normalization and remain allowed obstructions. The theorem does not classify them as the only positive-deficiency components. A simply connected component can have several horizontal-axis contacts and narrow passages; neither distinct augmentations nor a bound on shared bottlenecks follows from its single boundary cycle alone.

### Gaps

The global hole-filling lemma and the component normalization are proved. The displayed deficiency/augmentation inequality is not. No new numerical sweep, Lean formalization, or claim of solving the finite candidate or #168(ii) is made in this round.
