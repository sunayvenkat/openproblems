# Canonical cover exchanges and the remaining global phase obstruction

Research round: 7 November 2026. The objective was the global formula

\[
\tau(t)=\min_j\{K_j(t)-I_j(t)-P_j(t)\},\qquad t\ge3.
\tag{C}
\]

This round does **not** prove (C). It proves the canonical exchange rule for arbitrary maximum deficiency, strengthens it to an exact repair inequality, and gives a rooted planar forest representation. Two exact obstructions show why these facts cannot yet be promoted to a global phase theorem: an arbitrary preferred-color canonical optimum need not contain any complete vertical phase, and the owner matching rank is not submodular. All new checks below concern explicitly stated claims on one fixed board each; no broad search was performed.

## What exchange inequalities follow from a canonical global optimum?

### Takeaway

The strict owner-neighborhood inequality and essential-cover property extend from deficiency-one critical sets to a minimum-cardinality maximizer of arbitrary deficiency. There is also a stronger inequality counting only corners actually uncovered by the proposed deletion, so doubly covered corners are handled correctly.

### Cited Findings

- The coloring, graph \(B(U)\), and equality between the finite cover problem and maximum deficiency are established in [168_grid.md](<../../early-attacks/open-conjecture-transfer-search/168_grid.md>).
- The earlier essential-cover and deletion inequalities were formulated for critical deficiency-one sets in [boundary.md](<../boundary-and-arithmetic/boundary.md>) and [multiroot.md](<../../early-attacks/augmentation-and-return-attacks/multiroot.md>). The extension below is proved directly; it does not assume that full-cover optimality restricts to an arbitrary critical subset.

### Inferences

#### Canonical covers and minimum-cardinality deficiency maximizers

Write

\[
D_t=\{2^a3^b:a,b\ge0,\ 2^a3^b\le t\},\quad
c(2^a3^b)=a-b\pmod3,\quad C_j=c^{-1}(j)\cap D_t.
\]

Fix \(j\). Among all globally minimum corner covers \(F\), choose one maximizing \(|F\cap C_j|\). Set

\[
U=C_j\setminus F,\qquad W=F\setminus C_j.
\]

Then \(W\) covers \(B(U)\). Conversely, for any \(U'\subset C_j\) and any vertex cover \(W'\) of \(B(U')\), the set \((C_j\setminus U')\cup W'\) hits every original upward corner. By the bipartite matching-cover theorem,

\[
\tau=K_j-\max_{U'\subset C_j}d(U'),
\qquad d(U')=|U'|-\nu(B(U')).
\tag{1}
\]

Consequently the chosen pair satisfies

\[
|W|=\nu(B(U)),\qquad d(U)=D_j:=K_j-\tau.
\tag{2}
\]

Indeed, either a smaller cover of \(B(U)\) or a larger deficiency would produce a smaller original cover. Moreover \(U\) has minimum cardinality among **all** sets attaining \(D_j\): a smaller maximizer, combined with its minimum bipartite cover, would give a global optimum containing more color-\(j\) vertices. Conversely, any minimum-cardinality maximizer gives a canonical global optimum in this way.

Since \(U'=\varnothing\) is allowed, \(D_j\ge0\). If \(D_j=0\), canonicality forces \(U=\varnothing\), so \(F=C_j\). The nontrivial case has \(D_j>0\).

#### Exact repair inequality

For a nonempty \(S\subset W\), let \(T_F(S)\subset U\) consist of the color-\(j\) labels of precisely those original corners that become uncovered after deleting \(S\). Equivalently, these are owners of edges of \(B(U)\) with neither endpoint in \(W\setminus S\). Adding these owners repairs every uncovered corner:

\[
F'=(F\setminus S)\cup T_F(S).
\]

Thus \(|T_F(S)|<|S|\) would contradict minimum cardinality of \(F\). Equality would give another minimum cover with \(|T_F(S)|=|S|>0\) additional color-\(j\) vertices, contradicting canonicality. Therefore

\[
\boxed{|T_F(S)|\ge |S|+1\quad(\varnothing\ne S\subset W).}
\tag{3}
\]

This definition is deliberately narrower than “all incident owners.” A corner hit by two vertices of \(W\) becomes uncovered only when both are removed. A corner already hit by a selected color-\(j\) vertex never becomes uncovered in this exchange. These facts prevent an invalid exchange that ignores double coverage.

Let \(N(w)\subset U\) be the owners of all \(B(U)\)-edges incident to \(w\). Then \(T_F(S)\subseteq\bigcup_{w\in S}N(w)\), so

\[
\left|\bigcup_{w\in S}N(w)\right|\ge |S|+1.
\tag{4}
\]

There is an equivalent proof from minimum-cardinality maximal deficiency: deleting all incident owners \(T\) and vertices \(S\) leaves \(W\setminus S\) covering \(B(U\setminus T)\), whose deficiency is at least \(D_j+|S|-|T|\). If \(|T|\le|S|\), this is a smaller maximizer or contradicts maximality. The empty-remainder case causes no exception: for \(D_j>0\), the empty set cannot have deficiency at least \(D_j\).

Taking \(S=\{w\}\) in (3), every \(w\in W\) uniquely hits at least two original corners with distinct owners in \(U\). Thus the essential-cover property holds even when \(D_j>1\).

#### Consequences on the vertical axis

Let \(B=\lfloor\log_3 t\rfloor\), \(v_b=3^b\), and \(q_b=2\cdot3^b\). The only corners containing \(v_b\) are

\[
\{v_{b-1},q_{b-1},v_b\}\quad(b\ge1),
\qquad
\{v_b,q_b,v_{b+1}\}\quad(b<B).
\]

If \(v_b\in W\), both must exist and both must be uniquely hit by \(v_b\). In particular \(0<b<B\), and

\[
v_{b-1},v_{b+1},q_{b-1},q_b\notin F.
\tag{5}
\]

An axis endpoint of degree one cannot be selected outside color \(j\). Thus \(v_0\in F\) is possible only for \(j=0\), and \(v_B\in F\) is possible only when \(-B\equiv j\pmod3\).

No two consecutive vertical-axis vertices can both be selected. They have different colors, so at least one lies outside color \(j\); its shared corner would then be doubly hit, leaving it with at most one uniquely hit corner, contrary to (3). This statement applies to the chosen canonical cover, not to arbitrary minimum covers.

### Gaps

These constraints do not yet force a complete vertical phase. They apply to the full minimum-cardinality maximizer \(U\) and its minimum cover \(W\). They must not be transferred to \(F\setminus C_j\) as a presumed minimum cover of an arbitrary critical subset of \(U\).

## Do canonicality or submodular uncrossing already give the global phase?

### Takeaway

No. At \(t=54\), an arbitrary preferred-color canonical cover is unique and still has no complete vertical phase. On that same board, matching rank on owner sets fails submodularity, even for sets avoiding the vertical axis. These are exact counterexamples, not numerical optimization reports.

### Cited Findings

- Both fixed-board claims were checked with the existing integer matching routine and exact diagonal dynamic program, reused by [canonical_phase_check.py](<canonical_phase_check.py>). The exhaustive 64-subset result and rank witness are saved in [canonical_phase_check.json](<canonical_phase_check.json>).
- The separate earlier \(t=729\) obstruction shows that mere connected spanning is insufficient; its precise negative-deficiency scope is consolidated in [arithmetic_and_obstruction_audit.md](<arithmetic_and_obstruction_audit.md>).

### Inferences

#### A unique canonical cover without any complete vertical phase

At \(t=54\),

\[
C_0=\{1,6,8,27,36,48\},\qquad (K_0,K_1,K_2)=(6,5,5).
\]

There is no isolate or active patch correction on this board. The exact optimum is \(\tau=5\). Exhausting all 64 subsets of \(C_0\) gives \(\max d=1\), with a unique minimum-cardinality maximizer

\[
U=\{8,27,36,48\},\qquad |U|=4.
\tag{6}
\]

Its bipartite graph is the disjoint union of two paths,

\[
4-12-24-16-32,\qquad 9-18-54.
\]

The unique minimum cover of the first path is \(\{12,16\}\), and that of the second is \(\{18\}\). Hence the **unique** global optimum maximizing its color-zero intersection is

\[
F=\{1,6,12,16,18\}.
\tag{7}
\]

Its vertical phases are \(\{1,27\}\), \(\{9\}\), and \(\{3\}\); none is contained in \(F\). Because this canonical family has a single member, no further tie-breaker *within that family* can fix the failure. In particular, minimizing overcoverage after maximizing the color-zero count cannot select a different cover.

The essential-support condition is satisfied exactly:

\[
T_F(\{12\})=\{8,36\},\quad
T_F(\{16\})=\{8,48\},\quad
T_F(\{18\})=\{27,36\}.
\]

The original corner \(\{6,12,18\}\) is triply hit, contributing two units of overcoverage. Every other original corner is hit once. Thus canonicality also does not imply the absence of overcoverage.

This counterexample does not refute a statement restricted to a preferred color minimizing \(K_j-I_j-P_j\): here color zero is not a minimizing color. Nor does it refute existential phase normalization, since the pure covers \(C_1\) and \(C_2\) are minimum covers.

#### Matching rank is not submodular on actual weighted triangles

On the same board and in color zero, put

\[
A=\{8,48\},\qquad B=\{6,8,36\}.
\]

All owners avoid the vertical axis. With \(r(V)=\nu(B(V))\), the exact values are

\[
r(A)=2,\qquad r(B)=4,\qquad
r(A\cup B)=5,\qquad r(A\cap B)=r(\{8\})=2.
\tag{8}
\]

These values have short direct certificates:

- \(B(A)\) has only two left vertices, \(12,16\), and has the matching \((12,4),(16,32)\).
- \(B(B)\) has only four right vertices, \(3,4,18,24\), and has the matching \((2,4),(9,3),(16,24),(54,18)\).
- \(B(A\cup B)\) has five left vertices and has the matching \((2,4),(9,3),(12,24),(54,18),(16,32)\).
- The singleton owner 8 supplies its two disjoint edges \((12,4)\) and \((16,24)\).

Consequently

\[
r(A)+r(B)=6<7=r(A\cup B)+r(A\cap B).
\]

Thus \(r\) is not submodular and \(d\) is not supermodular. A general union/intersection uncrossing theorem for maximizers cannot be inferred from those properties. This counterexample does not rule out some narrower closure theorem requiring additional hypotheses.

#### One bounded check of a winning-phase restriction

The targeted check [phase_fill_check.py](<phase_fill_check.py>) examines only \(t=1536\), \(j=2\). Here the three color classes have size 15, the known patch has root 256 and color two, and \(d(C_2)=0\). Every one of the 16,383 nonempty subsets of \(C_2\setminus\{256\}\) has nonpositive deficiency. The output is in [phase_fill_check.json](<phase_fill_check.json>).

This is finite evidence only. It does not classify vertical-touching critical sets containing 256, establish a full-class filling theorem, or imply any uniform winning-phase statement. No further board or parameter sweep was run.

### Gaps

The arbitrary-preferred-color phase implication and general submodularity premise are decisively false. A winning-adjusted-color comparison remains a distinct, unproved assertion. The finite \(t=1536\) check must not be reported as support sufficient for that assertion.

## What planar forest representation is valid, and where does it stop?

### Takeaway

Canonicality yields a planar forest with \(D_j\) components. It can be chosen so that its north-parent subforest is rooted at the horizontal-axis labels. This is a valid structural representation, but unused third incidences still couple different forest components; they are not independent matching-deficiency components.

### Cited Findings

- The owner lists and north-parent matching are specified in [boundary.md](<../boundary-and-arithmetic/boundary.md>).
- Same-color face adjacency and the planar triangular lattice of owners are established in [hole_filling.md](<../../early-attacks/open-proof-gap-attacks/hole_filling.md>). The proof below does not combine maximal-cardinality hole normalization with minimum-cardinality canonicality.
- The strict expansion used here is equation (4), proved in this note. The finite forest selection lemma is proved below rather than invoked without its hypotheses.

### Inferences

#### A finite forest selection lemma

Let \((N_i)_{i\in J}\) be finite vertex sets such that

\[
\left|\bigcup_{i\in S}N_i\right|\ge |S|+1
\quad\text{for every nonempty }S\subseteq J.
\tag{9}
\]

For each \(i\), allow the edges of any connected graph \(G_i\) on vertex set \(N_i\). One can select one allowed edge from each \(G_i\) so that all selected edges form a forest.

**Proof by induction on \(|J|\).** The empty and one-index cases are immediate. If a proper nonempty subfamily \(S\) is tight, its vertex union has size \(|S|+1\). By induction its chosen edges form a tree on that union. Contract the entire tree to a vertex and consider the remaining family. For a remaining subfamily \(T\) whose vertex union meets the contracted tree, applying (9) to \(S\cup T\) shows that \(T\) has at least \(|T|\) vertices outside it; after contraction it still has at least \(|T|+1\) vertices. If it does not meet the tree, (9) is unchanged. Connected allowed graphs remain connected after contraction. Induction applies, and expanding the tree preserves acyclicity.

If no proper nonempty subfamily is tight, every such subfamily has at least \(|S|+2\) vertices. Choose any allowed edge from one index, delete that index, and contract the selected edge. Every remaining union loses at most one vertex, so (9) survives. Apply induction and restore the selected edge. Lifting contracted edges always uses an edge of its original allowed graph. This proves the lemma.

#### Application to canonical owner neighborhoods

Apply the lemma to the neighborhoods \(N(w)\), \(w\in W\), using (4). Initially take each allowed graph to be the complete graph on its two or three owners. Those owners are corners of a small triangle in the same-color face lattice; every allowed pair is therefore a face-adjacency edge. The selected pair-edges are embedded in this planar triangular lattice and form a forest on \(U\). Including isolated vertices of \(U\), it has

\[
|U|-|W|=D_j
\tag{10}
\]

components. Distinct selected pairs cannot coincide, since that would violate the forest condition when the selected edges are indexed by \(W\).

#### A rooting refinement using north-parent stars

Let \(Q=\{u\in U:b(u)\ge1\}\), and let \(r=|U|-|Q|\) count the horizontal roots. Every \(N(u)\), \(u\in Q\), must be covered by \(W\). Choose one of its selected endpoints \(w(u)\). These choices are distinct, because the north-parent edges are a matching.

For each assigned neighborhood \(N(w(u))\), restrict its allowed graph to the star centered at the owner \(u\). It is still connected on the entire neighborhood. Keep the complete allowed graph at unassigned vertices of \(W\). The forest selection lemma still applies.

Orient each of the \(|Q|\) assigned pair-edges away from its north-parent owner \(u\). At the left endpoint \(u/3\), the other possible owners are \(u/6\) and \(2u/9\). At the right endpoint \(2u/3\), they are \(2u/9\) and \(4u/3\). In exponent coordinates, each directed step strictly decreases the lexicographic pair

\[
(a+2b,b):
\]

the first two multipliers decrease the first coordinate by three, while \(4/3\) preserves the first coordinate and decreases \(b\) by one. Only available owners in \(U\) can be chosen.

Thus every nonhorizontal owner has one outgoing assigned edge, no directed cycle is possible, and every directed path ends at a horizontal root. These assigned edges form a forest with exactly \(r\) components, each containing one horizontal root. The remaining number of selected pair-edges is

\[
|W|-|Q|=r-D_j.
\]

Since the complete selection is still a forest, these edges join distinct north-parent trees, leaving exactly \(D_j\) components, each with at least one horizontal root. This proof also permits vertical-axis owners: their north-parent edge exists whenever \(b\ge1\).

#### Why this is not a decomposition into positive components

A neighborhood \(N(w)\) can have three owners. Its chosen pair may lie in one forest component while its unused third owner lies in another. Thus the original vertex \(w\), and its edges in \(B(U)\), can couple different forest components. The forest components need not have disjoint bipartite graphs, independent matching numbers, or positive individual deficiency. Equation (10) alone supplies none of those conclusions.

The \(t=54\) example also shows that a rooted tree with vertical and horizontal contacts is compatible with a genuinely canonical optimum of a nonwinning color. Its owner pairs are \(8-36\), \(8-48\), and \(27-36\), forming the tree \(48-8-36-27\). Additional global comparison is essential even in this simple case.

#### Exact remaining obligation

Put \(Q_j=K_j-I_j-P_j\), choose a color minimizing \(Q_j\), and form its canonical optimum. If (C) fails, then

\[
D_j=K_j-\tau>I_j+P_j.
\]

The audited axis-avoiding bound forces a vertical obstruction, but the present exchange and forest statements do not show that it can be removed at no cost. A sufficient next theorem would convert such an obstruction into either:

1. a minimum cover containing a complete vertical phase; or
2. a rigorously charged phase change yielding some \(k\) with \(Q_k<Q_j\), contradicting the choice of \(j\).

The known small \(x=2\) patch must remain separate: on \([12,13.5)\), the prescribed color-one vertical constraint has optimum \(K_1\), not \(K_1-P_1\), while the global candidate is attained through another phase. A proof cannot require the preferred phase itself to survive in every instance.

### Gaps

No exchange accomplishing either global alternative has been established. The forest representation is not such an exchange. The exact counterexamples rule out several shortcuts but do not resolve (C), and (C) itself would still be only the finite combinatorial step toward #168(ii) irrationality. No claim of a completed open-problem solution, historical priority, Lean verification, or external publication is made.
