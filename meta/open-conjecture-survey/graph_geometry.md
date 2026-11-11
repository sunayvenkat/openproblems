# Open graph and geometry transfers

## Which different problems are currently open in the pool?

### Takeaway
The current live pages verify open targets #23, #94's regular-polygon variant, #835, and #982. No complete solution was obtained. Several superficially close targets are already solved or fail the proposed input's hypotheses.

### Cited Findings
- **#23 remains offered:** every triangle-free graph on 5n vertices should become bipartite after deleting at most n² edges. Its live page has an open proof/disproof offer and two partial contributions. [Exact pool statement](https://conjectures.io/problems/erdos23-erdos-23).
- **#94, regular-polygon variant, remains offered and was added on 6 November 2026:** for every sufficiently large n, the sum of squared distance multiplicities of every convex n-point set should be at most that of the regular n-gon. Its pinned Lean statement has the eventual quantifier over all n. [Exact pool statement](https://conjectures.io/problems/erdos94-erdos-94-variants-regular-ngon).
- **#835 remains offered:** does some k>2 permit a coloring of the k-subsets of [2k] in k+1 colors so that all colors appear in every (k+1)-subset? Its existing contributions reduce to prime parameters and establish Johnson-graph identities and a lower bound for J(18,9). [Exact pool statement and contributions](https://conjectures.io/problems/erdos835-erdos-835?mode=counterexample).
- **#982 remains offered:** every convex polygon on n vertices should have a vertex determining at least floor(n/2) different distances to the other vertices. [Exact pool statement](https://conjectures.io/problems/erdos982-erdos-982).
- **#579 is excluded:** despite stale search results calling it open, its live page says approved 6 October 2026, credited to Jordan. [Current accepted status](https://conjectures.io/problems/erdos579-erdos-579).
- **Erdos Critical Minimum Degree is excluded:** its result was certified in October 2026. It is the edge-critical statement associated with #1032, not a fresh target. [Accepted result](https://conjectures.io/results/e76a593e-d1f7-4946-b724-a86f2b8ec5f8).
- **#641 is excluded:** the negative regular-subgraph result of Janzer–Steiner–Sudakov is prior work discussed in Nguyen–Walczak. The strengthened no-cubic-subgraph consequence of the Kohlmeyer–Kruer method is also already discussed there. [Primary exposition](https://arxiv.org/html/2609.40192).
- **#642 asks an intriguing different question:** if every cycle of a graph has strictly fewer chords than vertices, must its edge count be O(n)? The canonical statement gives an O(n(log n)^8) upper bound due to Draganić–Methuku–Munhá Correia–Sudakov. Pool membership was not verified: the guessed conjectures.io detail URL failed. [Canonical statement](https://www.erdosproblems.com/latex/642).

### Inferences
- An open-looking entry in a search-engine excerpt is not sufficient: #579 demonstrates a real stale-status failure. The successful target must be checked through its live detail page.
- #835 shares middle-level subset geometry with the #96/#97 construction, but that alone supplies no coloring or impossibility theorem for the Johnson graph. Its existential quantifier requires all k to be ruled out for a disproof.
- The triangle-free high-chromatic graphs behind #108 are sparse and have no supplied quantitative max-cut defect at the n²/25 scale required to disprove #23. Arbitrarily high chromatic number alone is compatible with a tiny proportion of edges obstructing bipartiteness.

### Gaps
- No graph target in the verified pool was solved in this screen.
- The #642 problem is a research lead, not yet a confirmed pool target.
- The source papers' mathematical seed constructions were not independently re-proved in this subtask.

## Can the no-cubic construction refute the cycle-and-chord problem?

### Takeaway
No: the tempting bridge “every Hamiltonian n-vertex graph with at least n chords contains a cubic subgraph” is false already on eight vertices. A stronger bounded-degree-core version is also false. This rules out a direct transfer of the known #108 input to #642 by that route.

### Cited Findings
- Nguyen–Walczak's primary exposition states that the Kohlmeyer–Kruer method supplies graphs of arbitrarily large fractional chromatic number while suppressing all bounded-maximum-degree subgraphs to degeneracy two. It also discusses the earlier Pyber–Rödl–Szemerédi construction of graphs with superlinear density and no cubic subgraph. [Primary paper, Theorem 2.1 and random-model discussion](https://arxiv.org/html/2609.40192).
- #642 concerns an entire cycle's induced chords, which do not have a fixed maximum-degree bound. [Problem statement](https://www.erdosproblems.com/latex/642).

### Inferences
**Explicit counterexample to the cubic bridge.** Let H be the join of an independent two-vertex set {x,y} with the disjoint union of two three-vertex paths a_i-b_i-c_i, i=1,2. Thus x and y are each adjacent to all six path vertices; x,y are not adjacent; and the only other edges are those of the two paths. Then H has 8 vertices and 16 edges. It has the Hamiltonian cycle

\[
x,a_1,b_1,c_1,y,a_2,b_2,c_2,x,
\]

so the remaining 8 edges are exactly 8 chords of an 8-vertex cycle.

Nevertheless H contains no nonempty cubic subgraph. A cubic subgraph cannot use zero hubs, since the remaining graph has maximum degree two. It cannot use exactly one hub: any included path endpoint has degree at most two, and without endpoints a path middle vertex also has degree at most one. Suppose both hubs are used. Within either P3, a selected endpoint must have its middle vertex and both hubs as neighbors. A nonempty contribution from one path must therefore consist of one path edge or the whole path. In the one-edge case, the hub degrees contributed are (2,2). In the whole-path case, the endpoints already contribute (2,2), and the middle vertex must use exactly one of its hub edges, giving (3,2) or (2,3). Two nonempty paths would give each hub degree at least four. One nonempty path never gives degree three at both hubs. Both possibilities are impossible.

The counterexample was discovered by a SAT cutting-plane search over graphs containing a fixed Hamiltonian cycle and was independently verified by enumerating all 65,535 nonempty edge subsets. The independent verifier does not use a SAT solver or the discovery graph's labeling:

- `verify_hamiltonian_cubic.mjs` constructs the graph from the join definition, checks the displayed cycle, enumerates all edge subsets, and asserts that none has all active degrees three.
- `hamiltonian_cubic_counterexample.json` records the graph and exact counts.
- `check_hamiltonian_cubic.mjs` is the discovery search; it proved no witness at orders six and seven before finding this order-eight witness.

**Why bounded-degree degeneracy does not repair the generic bridge.** Fix any Δ. Choose a graph G with average degree at least four whose every subgraph of maximum degree at most Δ is 2-degenerate. Such a G can be obtained by taking a sufficiently high-chromatic graph from the published construction and then a suitable nonempty minimum-degree core. List its n vertices cyclically and insert a new degree-two vertex between every consecutive pair. The resulting graph H is Hamiltonian on 2n vertices, has |E(G)|+2n≥4n edges, and thus at least 2n chords. Every subgraph of H of minimum degree at least three omits all the inserted vertices, so lies in G. Consequently H has no subgraph with minimum degree at least three and maximum degree at most Δ. No theorem of the form “many chords force a bounded-degree three-core” can hold without additional structural hypotheses.

This construction is only an obstruction to a proposed implication. H itself need not have large chromatic number or satisfy the hypothesis of #642. It is not a disproof of #642.

### Gaps
- A transfer to #642 would need to exploit detailed structure of the particular random construction, beyond absence of cubic or bounded-degree three-core subgraphs.
- No such stronger structural property was proved here.

## What prevents a direct convex-unit-distance transfer?

### Takeaway
The remaining geometric targets impose conditions or scales not supplied by the convex unit-distance construction. Its unbounded unit degree alone does not contradict #94 or #982, and it violates the no-four-concyclic hypothesis in #98 and #213.

### Cited Findings
- The Kohlmeyer–Kruer–Price construction gives strictly convex configurations with unit-distance minimum degree growing on a log-log scale, using a product of small rotations of a finite incidence configuration. [Pinned source](https://github.com/lkruer/erdos-96-97-proof/blob/0e98f5f9bdaf36007e3eb405cbefe2eda778a9b2/96-97.tex).
- #98 concerns sets with no three collinear and no four concyclic, asking whether their minimum possible number of distinct distances divided by n tends to infinity. #213 asks for arbitrarily large integral-distance sets with the same general-position constraints. [Pool catalog](https://conjectures.io/problems).
- #94's live regular-polygon variant concerns the complete distance energy, and #982 concerns every vertex's entire pinned-distance set, not only the unit-distance class. [#94](https://conjectures.io/problems/erdos94-erdos-94-variants-regular-ngon); [#982](https://conjectures.io/problems/erdos982-erdos-982).

### Inferences
- Four unit neighbors of one point lie on the same unit circle. Thus using the construction with unit minimum degree at least four directly violates the hypotheses of #98 and #213.
- A unit-degree guarantee k can force only k−1 identifications among the n−1 distances from a vertex; k of order log log n does not force the fewer-than-n/2 distinct distances needed to refute #982.
- For #94, the regular polygon has energy of order n³ (for unordered-pair multiplicities it is n²(n−1)/2 when n is odd). A unit-distance class of size O(n log log n) contributes only O(n²(log log n)²), insufficient by itself to exceed the regular energy.
- The rotational product does give guaranteed coincidences beyond the unit class. For a q-by-...-by-q exponent box of dimension m, a difference word δ has multiplicity \(\prod_i(q-|\delta_i|)\), and
  \[
  \sum_\delta\prod_i(q-|\delta_i|)^2=
  \left(\frac{2q^3+q}{3}\right)^m.
  \]
  If the finite seed has v points, the scale guaranteed just by these common-rotation identities is proportional to \(v^2((2q^3+q)/3)^m\), whereas n³ equals \(v^3q^{3m}\). Their ratio decays roughly as \((2/3)^m/v\). This calculation is not an upper bound on all geometric coincidences, but shows that the immediate guaranteed coincidences do not establish a counterexample. New systematic collapses between different seed pairs or exponent differences would be needed.

### Gaps
- No upper bound on the complete energy of the construction was proved, so the calculation does not rule out all possible refinements of a #94 attack.
- No geometric target was solved, and no new solution is claimed.
