# Independent audit of the boundary and dual arguments

**Verdict:** no mathematical counterexample or fatal gap was found in the zero-augmentation theorem, single-root classification, boundary-pocket charge, normalized bipartite-rank formula, or no-neutral-core lemma. The proofs below were independently reconstructed from the definitions. None requires the conjectural cover formula(C).

Three reporting qualifications matter: the rank equality uses the **rectangular bipartite adjacency matrix**; the targeted MILPs search for a positive-deficiency alternative matching or improving the patched bound, not strictly beating it; and the reported enumeration totals were not rerun in this audit. The finite-cover formula, multi-root augmentation bound, vertical-axis comparison, and irrationality remain unresolved.

## Are zero augmentation, generated-left closure, and the single-root bound proved?

### Takeaway

Yes, for U avoiding the vertical axis. Full membership in Q is essential: nonsmooth target indices and indices on the excluded vertical axis are genuine exits, not internal states. The proof in boundary.md handles these cases and early R exits correctly.

### Cited Findings

- The assertions and residual arcs being audited are in [boundary.md](boundary.md). The underlying owned edges and finite domain are in [the original matching reduction](../../early-attacks/open-conjecture-transfer-search/168_grid.md).
- The independent source for the allowed hole normalization is [hole_filling.md](../../early-attacks/open-proof-gap-attacks/hole_filling.md). Its maximal-cardinality choice is distinct from inclusion-minimal positive criticality.

### Inferences

Let Q={u∈U:b(u)>0}; the N baseline has |Q| edges. With left indices3l and right indices3r/2, the nonmatching arcs are

\[
R(w):6w\longrightarrow9w/2,
\qquad E(w):9w/2\longrightarrow3w/4.
\]

Their exponent differences are respectively(−2,+1) and(−1,−1). Thus every nonmatching step strictly decreases the first exponent. A right target outside Q is unmatched, even if it happens to be a smooth allowed label not in U. A nonsmooth index or an index on a=0 is likewise outside Q under the axis-avoidance hypothesis.

**Rotation lemma, independently checked.** Suppose w∈U, w≤4t/9, and the left index9w/2 is reachable from an external left vertex. E(w) exists. If q=3w/4∉Q, E(w) exits. Otherwise q∈U has positive first exponent and3q=9w/4≤t. Hence R(q) exists and starts at the same left index6q=9w/2. Follow R(q). Its target either exits immediately or enters Q, allowing the same argument with owner q. Each replacement w↦3w/4 decreases the first exponent by two. Iteration must terminate with an exit. An early R exit is fully legitimate. Strictly decreasing exponents prevent the continuation from revisiting the incoming path.

At w=4t/9 the required R(q) has3q=t and is present. If w has first exponent1 or2, q is respectively nonsmooth or on the excluded vertical axis, so the E exit occurs immediately. These are not exceptions to the lemma.

**Closure equivalence.** If an R edge starts externally, its owner satisfies w≤t/3, and it either exits directly or reaches the rotation lemma. Thus absence of augmentation excludes every external R source.

If an E edge starts externally, choose its smallest numerical owner w. When w≤4t/9 the rotation lemma applies. Otherwise w≤2t/3, and failure of an immediate exit forces q=3w/4∈Q, with t/3<q≤t/2. E(q) exists and has external left index9q/2>t, contradicting the minimal choice of w. This also covers the endpoint w=2t/3.

Conversely, if every E/R left endpoint is matched by N, the N matching saturates every incident left vertex and is maximum. Therefore no augmentation is equivalent to

\[
6u\in U\quad\text{whenever }R(u)\text{ exists},
\qquad 9u/2\in U\quad\text{whenever }E(u)\text{ exists}.
\]

These generated labels have positive three-exponent, so membership in U equals membership in Q. However their first exponent still matters: for example an E owner with first exponent1 cannot belong to an axis-avoiding closed set, because its generated label has first exponent0.

**Closed-set classification.** R excludes labels in(t/6,t/3], and E excludes labels in(t/3,2t/3]. A low label can therefore only lead, under repeated multiplication by6, to a last low p≤t/6. Its successor6p is high, so p>t/9. This makes9p/2>t/2, so that generated label must also be high, forcing p>4t/27. If there were a preceding q=p/6, then r=9q/2=3p/4 lies in(t/9,t/8] and is in U. Its E edge generates9r/2∈(t/2,9t/16], an excluded interval. Thus no preceding step exists and

\[
U\subset(4t/27,t/6]\cup(2t/3,t].
\]

The lower endpoint4t/27 is correctly strict. The upper endpointt/6 is correctly included. A low horizontal root x gives6x≤t<27x/4<8x, making4x the largest power of two at most t; since4x≤2t/3, there can be no high horizontal root. Each interval individually contains at most one power of two.

For exactly one horizontal root, positive deficiency forces ν=|U|−1=|Q|, so the baseline has no augmentation and closure applies. The high root is an isolate. A low root forces{x,9x/2,6x}; on6x≤t<27x/4 its owned graph is a four-edge path and has deficiency1. This proves d(U)≤I_j+P_j. With no root, the N matching directly gives d(U)≤0. Additivity across face components is valid because distinct face components cannot share a honeycomb vertex.

**Critical sets.** Independently, inclusion-minimal positive deficiency gives d(U)=1 by deleting one label and comparing matching sizes. A minimum cover vertex must uniquely cover edges of at least two different owners; otherwise deleting that vertex and its one owner gives a smaller positive-deficiency set. This justifies excluding leaves from the cover. The two leaf/essentiality chains in boundary.md correctly force the smallest label onto b=0 and then force the initial three patch labels. The claimed available edges follow from the forced neighboring owners being in D_t. These arguments apply only under the explicitly stated avoidance of a=0.

The natural interpretation of the cap word is the color of the rightmost point in each horizontal row. Under that definition its stated runs of2 or3 are valid: a row drop of2 preserves the color and a drop of1 advances it by1 modulo3. The inequalities3/2<log₂3<5/3 forbid consecutive drops11 and three consecutive drops222, giving runs2 or3 apart from end runs. The report should define the cap word if it uses this observation.

### Gaps

- The theorem finds one augmentation when closure fails; it does not supply enough disjoint augmentations for multiple roots.
- Criticality and the maximal-cardinality hole normalization cannot be simultaneously imposed without another proof. The audited text explicitly keeps them separate.
- Components meeting the vertical axis are outside the single-root theorem's scope. No statement here proves(C).

## Is the boundary-pocket replacement and the charge q2−p0 correct?

### Takeaway

Yes. The replacement inequality is valid even with truncated faces, and the explicit charge accounts correctly for negative-coordinate endpoints and cap equalities.

### Cited Findings

- The abstract boundary matching and Euler relation are proved in [hole_filling.md](../../early-attacks/open-proof-gap-attacks/hole_filling.md). Their truncated-domain extension and charge are stated in [boundary.md](boundary.md).

### Inferences

For a connected m-face region V with h holes, let I and B count geometric interior and boundary vertices. The full abstract polyhex gives I+B/2=2m+1−h. Its outside-owned boundary edges form a perfect matching P, irrespective of which vertices remain in D_t.

Partition P into p2 old available edges, q2 available-but-absent edges, p1 edges with one available endpoint, and p0 with none. The number of available boundary vertices is A=2p2+2q2+p1. Put z=A−p2=B/2+q2−p0; indeed0≤z≤A.

Keep all matching edges outside the polyhex one-skeleton, including those in holes. If b available boundary vertices remain free, at most⌊(I+b)/2⌋ inside edges are lost. Of the p2 old boundary edges at least max(0,b−z) survive the occupied boundary vertices. The maximum replacement loss occurs at b=z, giving

\[
\nu(B(U\cup V))-\nu(B(U))
\le\left\lfloor\frac{I+z}{2}\right\rfloor
=m+\left\lfloor\frac{1-h+q2-p0}{2}\right\rfloor.
\]

Thus charge q2−p0≤h suffices for nondecreasing deficiency. This argument does not assume every owned edge of V is available. Using I as an upper bound is enough; in fact each interior vertex is the average of its three incident V centers in exponent coordinates, so convexity of D_t makes it available.

For a finite-board complement component V, every outside owner that lies in the board is in U. The complete endpoint audit for v=2^a3^b∈V is:

| Outside owner and edge | Both endpoints available | No endpoints available |
|---|---|---|
| v/6; {v/3,v/2} | a,b≥1; owner is then in the board | a=b=0, hence v=1 |
| 4v/3; {2v/3,2v} | b≥1 and v≤t/2; owner is then in the board | b=0 and v>t/2 |
| 9v/2; {3v/2,3v} | a≥1 and v≤t/3 | v>2t/3, or a=0 and v>t/3 |

Only the last row can have both endpoints available while its owner is outside the board: this happens exactly when a≥1 and2t/9<v≤t/3. At v=2t/9 the owner equals t and is inside; at v=t/3 the endpoint3v=t remains available. At v=2t/3 with a≥1 the endpoint3v/2=t is available, so that case is p1, not p0. These verify the strict and closed endpoints in σ_t.

Every counted p0 or q2 edge has an owner outside the board, hence outside V. It is therefore a genuine boundary edge, counted once. The resulting additive formula in boundary.md is correct. Its maximal-cardinality conclusion, Σ_Vσ_t≥h(V)+1 for every remaining nonempty component, follows by contrapositive from the replacement bound and integer charge.

The additional boundary-contact assertion is also valid: each of N, E, R alone forms a matching when present for all labels. Positive deficiency therefore requires a missing edge of each type. Under axis avoidance, this forces a horizontal-axis contact and a label strictly above2t/3.

### Gaps

The charge is a necessary condition on surviving pockets, not a sufficient matching obstruction or a bound on total deficiency. Nothing in the replacement establishes the missing multi-root rank/augmentation estimate.

## Are the path-matrix rank theorem, no-neutral-core lemma, and evidence labels sound?

### Takeaway

Yes. The Schur-complement identity holds for every U. Equality with matching number is proved under connected full-plane complement. The no-neutral-core lemma needs only the stated single-deletion matching property and does not require hole normalization. Numerical claims remain separate from these proofs.

### Cited Findings

- The complete matrix construction and determinant proof are in [dual.md](dual.md); their exact implementation is [dual_check.py](dual_check.py).
- The targeted optimization model and saved statuses are in [test_alternative_patch.py](test_alternative_patch.py) and [alternative_patch_results.json](alternative_patch_results.json).

### Inferences

**Elimination.** The core Q consists exactly of available N edges. In the basis e=(−2,1), f=(−1,−1), every non-N arc changes the parity of the sum of basis coordinates. Multiplying corresponding row and column signs therefore leaves diagonal N entries+1 and makes every other entry−1. Strict decrease of the first exponent makes T nilpotent. Its core inverse is I+T+T²+⋯, and the exterior Schur complement is−P_U, with nonempty paths and no passage through a missing N edge. Hence rank(A)=|Q|+rank(P_U)≤ν for every U. The determinant-expansion proof of the inequality is valid.

**Normalized equality.** If the full-plane complement of U is connected, an omitted face inside a simple cycle of B(U) would have a dual face path to infinity. The embedded dual path must cross a cycle edge with both incident faces omitted, impossible because that edge's owner is in U. Thus all enclosed faces are in U. Convexity of D_t places all enclosed honeycomb vertices and owned corners in the board, so the interior is a complete hexagonal patch.

Every vertex strictly inside a cycle is matched by the initial N matching. Augmenting this matching to a maximum never makes an already matched vertex unmatched. Therefore all unmatched vertices are on the unbounded face. Deleting them cannot create a new bounded nonhexagonal face: each deletion opens or merges faces into the already incident unbounded face.

For an alternating cycle of length2k in the resulting perfect-matched graph H, all interior vertices are matched internally, so their number n is even. The enclosed hexagonal patch satisfies n−E+F=1 and6F=2E+2k, whence2F=n+k−1 and k is odd. Thus switching along that cycle changes determinant sign by(−1)^(k−1)=+1. All perfect-matching terms have the same sign, and the determinant is nonzero. This supplies a minor of sizeν, proving rank(A)=ν and the claimed path-matrix formula.

Here A is the **rectangular bipartite adjacency matrix**. If one instead uses the full symmetric adjacency matrix [[0,A],[Aᵀ,0]], its rank is2ν, notν. The source note defines A correctly; the distinction should survive into the report.

**No neutral core.** For critical U with m labels, deleting any owner q leaves matching number m−1=ν(B(U)); hence some maximum matching avoids N(q). Compare such a maximum M with N. Their symmetric difference has no alternating cycle because contraction would give a directed cycle in the exponent-decreasing DAG. It has no path with one more N edge than M edge, since flipping that path would augment M. Every remaining nontrivial path has an endpoint unmatched in N. A q whose N edge is absent from M therefore lies on a path from an external left index or to an external right index. This proves Q⊆Reach(X)∪CoReach(Y).

When r=1, N is already maximum. A core vertex in both reachability sets would give an X-to-Y augmenting path; strict exponent decrease makes the concatenation a valid simple path. Thus the two sets are disjoint in this case. Neutral nodes are excluded, but reachable dead ends are not. This is exactly the limitation recorded in dual.md.

**Examples and provenance.** The two displayed graphs at t=54 and128 have precisely the listed owned edges. Their component path lengths are respectively(2,4) and(2,4,1), giving matching sizes3 and4. The stated bipartition sizes, deficiencies, and path matrices follow. The t=1536 patch has no external left index and two N edges, so its path matrix has rank0. These examples were checked directly from the edge definitions, without a new search.

The checker correctly uses exact integer augmentation, Fraction-based rank, finite-box hole detection with a connected exterior collar, and DAG path counts that stop outside Q. Its --rank scope is every connected hole-free nonempty subset of each color class through the33rd smooth prefix, t=486; the17-label guard does not remove any class in that range. The reported totals11,811 and74 were **not independently rerun** in this audit. The74 counter concerns the weaker single-deletion condition; that condition is nevertheless sufficient for the no-neutral proof above. No claim of exhaustive critical-set classification follows.

The MILP code imposes cover size≤K_j−1, fixes the color-j vertical-axis vertices in the cover, and requires at least one patch vertex to remain in the cover. Therefore it searches for a positive-deficiency alternative that **matches or improves** the patched bound, not strictly beats it. The three saved HiGHS infeasibility statuses agree with the prose's numerical-only qualification. They are not exact infeasibility certificates and do not establish unrestricted patch necessity.

### Gaps

- The external benzenoid-paper attribution was not independently verified: the cited publisher page could not be retrieved during this audit. The new graph theorem was instead assessed from its self-contained proof, so this access limitation does not support or undermine that proof.
- No enumeration or MILP was rerun; no new experiments were needed for the mathematical review. Reported finite totals remain attributed to their original checker run.
- The uniform lower bound on rank(P_U), sufficient independent augmentations for multiple roots, the comparison of vertical-axis components across color phases, (C), and irrationality are all still unproved. None of the audited auxiliary theorems resolves the open target.
