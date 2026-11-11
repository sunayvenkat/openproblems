# Erdős 168: an exact integer boundary path matrix

This note proves a boundary matrix formula for the normalized matching problem. It does **not** prove the sharp finite-cover candidate or the irrationality target. All claims below concern the actual domain `D_t={(a,b)>=0:2^a3^b<=t}` unless explicitly stated otherwise. No priority claim is made.

## Can the matching deficiency be expressed by an explicit boundary matrix?

### Takeaway

Yes. If `U` has connected complement in the infinite color-j face lattice, put `Q={u in U:b(u)>0}` and `r=|U|-|Q|`. An explicitly defined nonnegative integer matrix `P_U` counts directed paths between boundary vertices and satisfies

```
nu(B(U)) = |Q| + rank_Q(P_U),
d(U) = r - rank_Q(P_U).
```

The formula uses ordinary rational matrix rank, not generic rank or a numerical relaxation.

### Cited Findings

- The existing reduction identifies `d(U)=|U|-nu(B(U))` and the N, E, R owned edges. Hole filling permits a maximizer whose full-plane complement is connected. — [Matching reduction](../../early-attacks/open-conjecture-transfer-search/168_grid.md), [proved normalization](../../early-attacks/open-proof-gap-attacks/hole_filling.md).
- Exact integer matching, rational rank, and independently computed path counts agree in all **11,811** nonempty connected hole-free shapes in the three color classes of every smooth prefix through `t=486`. This includes shapes not touching the horizontal axis. Run `dual_check.py --rank`; this is a bounded consistency check, not the proof. — [Exact checker](dual_check.py).
- The relation between matching number and ordinary adjacency rank for hexagonal systems is established in the literature. Fajtlowicz, John, and Sachs also move unmatched vertices to boundary extrema before applying a determinant argument. The proof below adapts the boundary mechanism to the present owned-edge graph, which need not be a hexagonal system in their two-connected sense. — [Authors' paper, pp. 198–199](https://www.researchgate.net/publication/27186432_On_Maximum_Matchings_and_Eigenvalues_of_Benzenoid_Graphs), [publisher record](https://hrcak.srce.hr/index.php/en/clanak/12).

### Inferences

**1. Index both bipartitions by their N owners.** Take left color `j+1` and right color `j-1`. A physical left vertex `(a,b)` receives index `(a,b+1)`; a physical right vertex `(a,b)` receives index `(a-1,b+1)`. In numerical notation these are multiplication by 3 and by 3/2. Indices may have first exponent -1; these are legitimate boundary indices, not labels required to lie in `D_t`.

An N edge owned by `u` becomes the diagonal entry `(u,u)`. All such edges with `u in Q` are present. Let

```
e=(-2,1),  f=(-1,-1).
```

The other two edges owned by `u` become

```
R(u): u-f   -> u-f+e,
E(u): u-f+e -> u+e.
```

Thus each owner supplies two consecutive sides of a square in the basis `(e,f)`, subject to the actual edge availability conditions. Every directed edge decreases the first exponent strictly. The network is a DAG, even before imposing simple connectivity.

Let `X` be the left indices outside `Q` and `Y` the right indices outside `Q`, including only indices of actual vertices incident to `B(U)`. Define

```
P_U(x,y) = number of nonempty directed paths x -> y
           whose internal vertices all lie in Q,
           for x in X and y in Y.
```

Do not count the length-zero path when an index belongs to both X and Y. A path stops on reaching an external right index; it cannot pass through a missing N edge.

**2. Exact elimination.** Let `A` be the unweighted bipartite adjacency matrix of `B(U)`, with rows and columns indexed as above. Choose any origin in the color-j lattice. If `v=p e+q f` relative to this origin, multiply row v and column v by `(-1)^(p+q)`. Every non-N entry changes from +1 to -1, and every N entry remains +1.

Order the core Q by decreasing first exponent. The resulting core block is `I-T`, where T is the nonnegative directed adjacency matrix restricted to Q and is strictly triangular. Hence

```
(I-T)^(-1) = I+T+T^2+...,
```

a finite integer sum. In core/exterior block form, the Schur complement is

```
-T_XY - T_XQ (I-T)^(-1) T_QY = -P_U.
```

Consequently, for **every** U, including ones with holes,

```
rank_Q(A) = |Q| + rank_Q(P_U) <= nu(B(U)).                 (1)
```

The last inequality follows from the determinant expansion: a nonzero k-by-k minor contains a nonzero permutation product, hence a matching of size k.

**3. Why equality holds after the proved hole filling.** Assume the complement of U in the full infinite face lattice is connected. Every simple cycle C in `B(U)` encloses only U faces. Indeed, an omitted face inside C could reach infinity through omitted adjacent faces; that route would have to cross an edge of C with both incident faces omitted. Each edge of C has its owner in U, a contradiction.

The weighted triangle is the intersection of three linear half-planes in exponent coordinates and is convex. All vertices of C lie in it, so every honeycomb vertex enclosed by C lies in it as well. Since all enclosed faces belong to U, all honeycomb edges strictly inside C are present. Thus all bounded faces of `B(U)` are elementary hexagons. This statement concerns the graph, not the larger abstract union of all owner hexagons, some of which are truncated at the board boundary.

Start from the matching consisting of all N edges owned by Q and augment to a maximum matching M. Augmentation never leaves a previously matched vertex unmatched. Every vertex strictly inside a cycle has all incident faces in U, so its incident N edge belongs to that starting matching. Therefore every vertex unmatched by M lies on the unbounded face.

Delete these unmatched vertices and call the resulting induced graph H. The matching M is perfect on H. Deleting vertices on the unbounded face can merge bounded faces with the unbounded face but cannot create a new bounded nonhexagonal face. Thus every bounded face of H is still a hexagon.

The square bipartite adjacency matrix of H has nonzero determinant. To see this directly, compare any two perfect matchings. Their symmetric difference is a union of alternating cycles. For one such cycle of length `2k`, let n be its number of interior vertices, F the number of enclosed hexagons, and E the number of edges strictly inside the cycle. Euler and edge-face counting give

```
n-E+F=1,
6F=2E+2k,
2F=n+k-1.
```

Because the cycle alternates with a perfect matching, all its interior vertices are matched internally, so n is even. It follows that k is odd. The two determinant terms differ on this cycle by the permutation sign `(-1)^(k-1)=+1`. All nonzero determinant terms therefore have the same sign; at least one exists because M is perfect. The determinant is nonzero.

This provides a minor of A of size `|M|=nu(B(U))` with nonzero determinant. Together with (1), it proves the asserted exact rank formula.

The argument applies componentwise when U is disconnected. In particular it applies to the positive simply connected components furnished by the existing normalization.

### Gaps

The equality is proved under the connected full-plane complement hypothesis. No equality of ordinary rank and matching number is asserted for arbitrary U with holes. Formula (1) remains valid without that hypothesis.

## Can boundary color counts replace the path matrix?

### Takeaway

No. Even a face-connected, hole-free positive-deficiency component on an actual weighted triangle can have fewer matching edges than the size of its smaller bipartition. The obstruction can persist when the component avoids the vertical axis.

### Cited Findings

- The checker finds and verifies the two explicit examples below using only integer graph operations. It also checks face connectivity and connected complement. — [Exact checker](dual_check.py).
- The known isolated point and three-face patch are valid cover improvements; the following examples do not contradict their proposed sharp bound. — [Construction and candidate](../../early-attacks/open-conjecture-transfer-search/168_grid.md).

### Inferences

**Example 1: a vertical-axis bottleneck.** At `t=54`, choose color 0 and

```
U={8,27,36,48}.
```

The face-adjacency graph has edges `8--36`, `8--48`, `27--36`, and `36--48`. Its abstract polyhex is connected and has no hole. Its owned-edge graph consists of the two disjoint paths

```
9 -- 18 -- 54,
4 -- 12 -- 24 -- 16 -- 32.
```

The two bipartitions each have four vertices, but their matching numbers are respectively 1 and 2, for total 3. Hence `d(U)=4-3=1`. A matching of size 3 is `{9--18,4--12,16--32}`; the vertex cover `{18,12,16}` certifies the reverse bound. The path matrix has one row and one column and is `[0]`.

This is compatible with the finite candidate: at t=54 the color sizes are `(6,5,5)`, so color 0 is not minimizing. The example demonstrates a bottleneck inside a normalized owner component, not a failure of the proposed optimum.

**Example 2: an axis-avoiding positive component.** At `t=128`, choose color 1 and

```
U={16,54,72,96,128}.
```

Every label has positive first exponent. The first four faces are twice the previous four-face polyhex; the fifth face joins through `96--128`. The union remains connected and hole-free. The edge graph has components

```
18 -- 36 -- 108,
8 -- 24 -- 48 -- 32 -- 64,
81 -- 27.
```

Both bipartitions have size 5 and the matching number is `1+2+1=4`, so `d(U)=1`. The label 128 owns no available edge. Its deficiency is exactly the allowed isolated-point defect. Here r=2, Q has size 3, and, with rows and columns ordered as in the checker,

```
P_U = [[0,0],[0,1]],
rank(P_U)=1.
```

Removing the isolated label leaves a zero-deficiency four-face block which already fails smaller-side saturation. Thus a further normalization to inclusion-minimal positive components might discard this attachment; the present simply connected positive-component normalization does not.

**Known three-face patch.** At `t=1536`, the patch component `{256,1152,1536}` has r=1, two N edges, and no external left index. Its path matrix has no rows and rank 0, giving d=1. The formulation records the known patch without requiring a rainbow matching indexed by its three owners.

### Gaps

These examples disprove the proposed shortcut of saturating the smaller bipartition, even on normalized actual-board components. They do not classify inclusion-minimal positive components, refute the finite candidate, or show that the path-matrix rank bound is false.

## What sharp boundary statement remains, and does the new formulation solve it?

### Takeaway

The desired inequality becomes a precise rank lower bound for an explicitly computable integer boundary response matrix. This gives a usable exact object for a boundary calibration, but its required uniform rank bound is still unproved.

### Cited Findings

- The finite candidate for a minimizing color j requires total deficiency at most `delta_j=I_j+P_j`, after splitting into normalized positive components. — [Exact remaining obligation](../../early-attacks/open-proof-gap-attacks/hole_filling.md).
- The unrestricted fractional-cover ceiling method already fails at t=486, so replacing this integer rank by the old cover LP would lose necessary information. — [Exact LP obstruction](../../early-attacks/open-proof-gap-attacks/cover.md).
- Among the 11,811 shapes checked above, 74 satisfy the single-deletion criticality condition used in the following lemma. Every one satisfies its reachability conclusion. — [Exact checker, `--rank`](dual_check.py).

### Inferences

For normalized components `U_i`, let `r_i` be their numbers of horizontal-axis labels. The remaining statement is exactly

```
sum_i rank_Q(P_Ui) >= sum_i r_i - delta_j.                (2)
```

Unlike a bipartition-size bound, (2) accounts for shared bottlenecks and zero-deficiency attachments. Unlike an unrestricted fractional cover, it retains integer path counts and rational linear dependencies.

One possible way to prove (2) is to select a nonzero minor of the block-diagonal boundary matrix with at least `sum r_i-delta_j` rows. In the directed square grid its determinant is a signed count of families of paths. A valid argument would have to establish either an explicit unique family or that all relevant nonintersecting families have the same permutation sign. Merely counting external endpoints, observing a single boundary cycle, or showing each root has some exit is insufficient; different roots can compete for the same internal capacity-one vertices.

The actual cap word cycles through boundary colors in runs of length 2 or 3, apart from end runs. That may constrain an admissible minor, but no deduction from that cyclic run condition to (2) has been established in this note. The matrix theorem does not turn the original unproved Hall inequality into a solved rank estimate.

**Additional critical-set lemma: no neutral core nodes.** Let U be inclusion-minimal among positive-deficiency sets. This lemma does not require hole filling. Then `nu(B(U))=|U|-1`, and every core node q is either reachable from X or can reach Y in the contracted network:

```
Q subset Reach(X) union CoReach(Y).                       (3)
```

Proof: For each q in U, minimality implies `nu(B(U\{q}))>=|U|-1`, whereas `nu(B(U))<=|U|-1` by positive deficiency. Edge deletion cannot increase the matching number, so both are exactly `|U|-1`. In particular a maximum matching exists that uses none of the edges owned by q, including N(q) when q is in Q.

Compare any maximum matching M with the N matching. Their symmetric difference has no alternating cycle: contracting its N edges would give a directed cycle in the square-grid DAG. It also has no path containing more N edges than M edges, since flipping such a path would augment M. Every nontrivial path therefore touches an endpoint free in N. If q is on such a path, following its direction shows that q is reachable from an external left index, can reach an external right index, or both. Thus a q satisfying neither property must have its N edge in every maximum matching. This contradicts the maximum matching obtained after deleting its owner and proves (3).

In particular, when r=1, the critical matching number equals |Q| and there is no exterior-to-exterior augmenting path. Therefore the two sets in (3) are disjoint: the core partitions into vertices reachable from exterior left endpoints and vertices that can reach exterior right endpoints. No core vertex can be neutral.

This condition eliminates unused interior branches, but does **not** exclude a cap absorber reached from X and having no route to Y: it belongs to the first permitted class. Any classification of single-root critical sets must still rule out, charge, or normalize such absorbers. Neither (3) nor P=0 alone supplies that classification.

### Gaps

The uniform rank lower bound (2) remains open. No finite-cover theorem or irrationality conclusion follows here. The bounded exact checks stop at t=486 for the matrix identity; no large numerical sweep, Lean formalization, or external posting was performed.
