# Canonical-cover audit and aggregate boundary dominance

Research round, 7 November 2026. The canonical repair, connected-neighborhood forest selection, north-rooted refinement, and three-matching incidence representation pass the independent audit below. The deep-branch proof has also received an independent reconstruction from another researcher. The prefix exchanges (P1)–(P2) and their aggregate consequence (P3) are new self-contained derivations in this note, **pending a separate independent audit**; they should be reported as proofs under review until that check is complete. None establishes the global finite optimum, and the final phase-count inequality remains an unproved candidate.

## Are the canonical repair and forest proofs correct?

### Takeaway

Yes. The exact repair inequality handles doubly covered corners correctly, and the elementary forest induction is valid. The forest must be interpreted as an indexed multigraph forest, so selecting the same pair twice is a parallel-edge cycle. Its components are not independent deficiency components. [Audited source](<../global-boundary-proof/canonical_phase.md>).

### Cited Findings

- The authoritative proof is [canonical_phase.md](<../global-boundary-proof/canonical_phase.md>).
- Its finite counterexamples and bounded winning-phase check are supplied by [canonical_phase_check.py](<../global-boundary-proof/canonical_phase_check.py>), [its output](<../global-boundary-proof/canonical_phase_check.json>), [phase_fill_check.py](<../global-boundary-proof/phase_fill_check.py>), and [its output](<../global-boundary-proof/phase_fill_check.json>). These source files were read. The 64-subset calculation at \(t=54\) was independently repeated in memory, without writing to the earlier folder.
- The owner lists and axis-avoiding theorem used below were independently audited in [combinatorial_and_coefficient_audit.md](<../global-boundary-proof/combinatorial_and_coefficient_audit.md>).

### Inferences

#### Canonicality and the exact repair

Fix \(j\). For any \(U\subset C_j\) and cover \(W\) of \(B(U)\), the set \((C_j\setminus U)\cup W\) covers every upward corner. Conversely any corner cover \(F\) gives such a pair \(U=C_j\setminus F\), \(W=F\setminus C_j\). The bipartite matching-cover equality consequently gives
\[
\tau=K_j-\max_{U\subset C_j}d(U).
\]
For an optimum \(F\), its corresponding \(W\) is minimum and \(d(U)=D_j=K_j-\tau\). Maximizing the preferred-color part of \(F\) is exactly minimizing \(|U|\) among these maximizers. If \(D_j=0\), the empty owner set is the unique minimum-cardinality choice and \(F=C_j\).

For nonempty \(S\subset W\), let \(T_F(S)\) consist of owners of precisely the corners that become uncovered when \(S\) is deleted. These owners lie in \(U\): a corner whose preferred-color vertex already lies in \(F\) cannot become uncovered. A corner with two selected nonpreferred endpoints contributes only if both are removed. Adding \(T_F(S)\) repairs all uncovered corners, and these added owners are disjoint from \(F\). Therefore
\[
|(F\setminus S)\cup T_F(S)|=|F|-|S|+|T_F(S)|.
\]
If \(|T_F(S)|<|S|\), optimality fails. Equality increases the preferred-color count of a minimum cover, contradicting canonicality. Thus \(|T_F(S)|\ge|S|+1\).

This implies the all-incident-owner inequality \(|N_W(S)|\ge|S|+1\), because \(T_F(S)\subseteq N_W(S)\). Equivalently, \(W\setminus S\) covers \(B(U\setminus N_W(S))\), whose deficiency is at least \(D_j+|S|-|N_W(S)|\). The empty remainder cannot invalidate this argument when \(D_j>0\): its deficiency is zero, or directly \(|U|>|W|\ge|S|\). Taking a singleton \(S\) proves that every \(w\in W\) uniquely covers at least two distinct owners.

These arguments also apply to an **inclusion-minimal** maximizer, without requiring minimum cardinality among all maximizers. Equality after removing owners would create a proper maximizing subset, which is enough for a contradiction.

#### Vertical-axis claims

A vertical point \(3^b\) lies in at most its preceding and following vertical corners. If it belongs to \(W\), essentiality requires both corners to exist and be uniquely covered there. This excludes the two axis endpoints from \(W\) and forces all four other vertices of those two corners outside \(F\). Two consecutive selected vertical points would doubly cover their common corner; at least one is nonpreferred and would then have at most one unique incident corner. Hence no two consecutive vertical points are selected in the canonical cover. These claims pass, but do not force a complete phase.

#### Connected-neighborhood forest selection

For a finite family of vertex sets \(N_i\) with \(|\bigcup_{i\in S}N_i|\ge|S|+1\) for every nonempty index subset \(S\), allow the edges of an arbitrary connected graph \(G_i\) on each \(N_i\). The claimed selection of one edge per index as a forest is valid.

If a proper nonempty subfamily \(S\) is tight, induction supplies \(|S|\) forest edges on \(|S|+1\) vertices, hence a spanning tree. Contract it. A remaining subfamily \(T\) meeting this tree has at least \(|T|\) vertices outside it, by applying the expansion condition to \(S\cup T\); contraction therefore leaves at least \(|T|+1\) vertices. A disjoint \(T\) is unchanged. Each allowed connected graph remains connected after quotienting. A remaining graph cannot collapse to a single unusable vertex, since the singleton expansion condition still requires at least two vertices. Apply induction and expand the tree.

If no proper nonempty subfamily is tight, every such union has at least \(|S|+2\) vertices. Select an edge from one index, delete that index, and contract the edge. Every remaining union loses at most one vertex, so the expansion condition survives. Induction and lifting complete the proof.

The selected edges are indexed by their originating \(G_i\). Parallel copies of the same pair count as a cycle of length two, and loops cannot be selected after contraction. The induction enforces this convention. All selected edges therefore remain distinct and the final component count is valid.

For canonical \(W\), each neighborhood \(N(w)\) has two or three owners. The possible owners at a physical vertex form an elementary triangle of the owner lattice, so every allowed pair is a planar nearest-neighbor edge. The selected forest has \(|W|\) edges on \(U\), including isolated owners, hence \(D_j=|U|-|W|\) components.

#### North-rooted refinement

For every nonhorizontal owner \(u\), choose one selected endpoint of \(N(u)\). The choices are distinct because the north edges form a matching. At that assigned neighborhood, restricting allowed pairs to a star centered at \(u\) preserves connectedness; the selection lemma still applies.

Orient each assigned edge away from \(u\). Its other owner is \(u/6\), \(2u/9\), or \(4u/3\). The first two decrease \(a+2b\) by three; the last preserves \(a+2b\) and decreases \(b\). Thus \((a+2b,b)\) strictly decreases lexicographically. Every nonhorizontal owner has one outgoing edge, every horizontal owner has none, and paths terminate at horizontal roots.

If there are \(r\) horizontal roots, the assigned forest has \(|U|-r\) edges and exactly \(r\) components, each with one root. The remaining \(r-D_j\) selected edges join distinct assigned trees because the full selection is acyclic. The final forest has \(D_j\) components, each with a horizontal root.

An unused third owner of a selected neighborhood may lie in a different forest component. That original selected vertex then couples the components in \(B(U)\). No matching-number additivity or positive-deficiency assertion for the individual components follows.

#### Finite negative claims

The read-only \(t=54\) repeat returned \(D_0=1\) and the unique smallest maximizer \(\{8,27,36,48\}\), of size four. Its two path components have unique minimum covers \(\{12,16\}\) and \(\{18\}\), giving the unique preferred-color-zero canonical cover \(\{1,6,12,16,18\}\). It contains no complete vertical phase. The corner \(\{6,12,18\}\) is triply covered; all other corners are hit once.

The four matching certificates for the submodularity witness were independently checked against the owned-edge lists. Their ranks are \(2,4,5,2\), so \(2+4<5+2\). No submodular uncrossing premise is available.

The \(t=1536\) checker examines all 16,383 nonempty subsets after removing root 256. Sets without horizontal roots are skipped only after counting them; the north matching proves their deficiency nonpositive. Its reported absence of a positive set is therefore logically consistent with its loop. That larger finite check was not rerun in this audit and is not a uniform theorem.

### Gaps

No gap was found in the canonical repair, forest selection, rooted refinement, or stated finite counterexamples. These statements do not establish a winning-phase exchange, independent forest components, rank submodularity, or matroid circuit elimination for critical owner sets.

## Does the incidence graph really have the three boundary matchings?

### Takeaway

Yes. The three partial matchings can each be extended while preserving every already matched owner. Their union has a valid componentwise unmatched-count identity, but does not split a defect-\(D\) component into \(D\) disjoint tripods. [Representation under audit](<../global-boundary-proof/vertical_critical.md>).

### Cited Findings

- The graph \(H\), three matching constructions, and claimed limitations are stated in the final section of [vertical_critical.md](<../global-boundary-proof/vertical_critical.md>).
- The axis-avoiding classification says that deleting the unique exceptional root removes every possible positive axis-avoiding critical subset. [Independent combinatorial audit](<../global-boundary-proof/combinatorial_and_coefficient_audit.md>).

### Inferences

Let \(U\) be an inclusion-minimal maximum-deficiency set with \(D>0\), and \(W\) a minimum cover. Let \(H\) join an owner to every selected vertex on one of its available owned edges. Strict owner expansion gives Hall's condition on the \(W\) side, so \(H\) has a matching saturating \(W\).

The north edges are pairwise vertex-disjoint; selecting a \(W\)-endpoint on each yields a partial matching of \(H\) saturating every nonhorizontal owner. The rooted edges of owners \(u\le t/3\) are also pairwise disjoint and give the corresponding partial matching of all low owners.

For the third partial matching, let \(A\) contain the nonvertical owners other than the exceptional root, when that root exists in the preferred color. Every subset \(A'\subset A\) satisfies \(\nu(B(A'))\ge|A'|\). The set \(N_H(A')\subset W\) covers \(B(A')\), so \(|N_H(A')|\ge|A'|\). Hall's condition therefore supplies a matching saturating \(A\).

Starting from any of these partial matchings, ordinary augmenting paths preserve all already matched owners: an augmentation has an unmatched owner at one end and an unmatched selected vertex at the other, with matched owners internal to the path remaining matched. Repeated augmentation reaches the known maximum size \(|W|\). Thus the unmatched owners of the three completed matchings lie respectively on the horizontal axis, in \(u>t/3\), and on the vertical axis or the exceptional root.

The incidence graph is a subgraph of the planar triangular lattice. In a component of the union of the three matchings, every selected vertex is matched by each matching within that component. Each matching therefore leaves exactly \(|U_{\rm comp}|-|W_{\rm comp}|\) owners unmatched there. This number is nonnegative and identical for all three matchings. Isolated owners, when present, obey the same count.

A positive component touches all three boundary sets, but it may have several unmatched owners of each type. Nothing in this argument produces separate disjoint tripods, proves an independent deficiency decomposition, or controls the adjusted phase counts. No outside planar-web theorem has been invoked.

### Gaps

The representation is correct but supplies no nonlocal boundary charge by itself. Any additional use of a Temperley-type correspondence, planar-web reduction, or positivity theorem would require its precise hypotheses; none is assumed here.

## What new aggregate dominance and collision reductions follow?

### Takeaway

The incomparable deep branch is now excluded by a separate exact strip count. For degenerate two-cone maximizers, adding a fully controlled triangular prefix increases deficiency by \(\lfloor A/3\rfloor\) or \(\lfloor B/3\rfloor\). This limits the least roots of a canonical maximizer and yields a common-optimum collision reduction when no patch correction is active. The final high-branch phase comparison remains open.

### Cited Findings

- The full deep-branch proof, with explicit owner overlaps and cutoffs, is saved in [deep_branch.md](<deep_branch.md>). It uses strict owner expansion and applies to arbitrary-deficiency canonical sets having the stated two-cone hypotheses.
- The predecessor cones, root coordinates, high-branch dichotomy, and their origin and degenerate qualifications were established in [vertical_critical.md](<../global-boundary-proof/vertical_critical.md>). The derivations below identify which arguments extend to aggregate maximizers rather than silently treating every maximizer as critical.

### Inferences

#### Restricted maximizers and root balance

Fix a color \(j\). If it has an exceptional isolate or patch root \(e\), exclude that owner; otherwise exclude nothing. Let
\[
D_j^*=\max\{d(U):U\subset C_j,\ e\notin U\},
\]
where the exclusion is omitted if no \(e\) exists. Suppose \(D_j^*>0\), choose an inclusion-minimal maximizer \(U\), and take a minimum cover \(W\).

The strict all-incident-owner inequality still holds: deleting owners preserves the allowed pool. Essentiality and the interior predecessor proof therefore hold too. Every axis-avoiding subset of this allowed pool has nonpositive deficiency, so \(U\) touches both axes.

If \(1\in U\), both least roots are the origin. Otherwise write them as \(2^A,3^B\), with \(A,B\ge1\). The two-cone inclusion follows exactly as for critical sets. The proof excluding \(A>2B\) uses only the forced vertical chain and still works. If \(B>2A\), the horizontal chain must stop at a numeric cutoff before the forbidden smaller vertical root. The three-strip count either contradicts strict expansion or forces an isolated/patch root. In the latter cases the root is precisely the excluded exceptional root, an impossibility. Thus
\[
A/2\le B\le2A,\qquad
r=(2A-B)/3\ge0,\quad s=(2B-A)/3\ge0.
\]

For \(r,s\ge1\), the deep-branch exclusion and the vertical-strip dichotomy force \(y=3^B>t/3\). There is only one vertical owner in \(U\): the next same-color vertical root is \(27y>t\). Removing \(y\) leaves an allowed axis-avoiding set, so \(D_j^*=d(U)\le1\). In this case \(D_j^*=1\), and inclusion-minimality makes \(U\) genuinely critical. This controls aggregate deficiency in this branch without decomposing it into critical components.

#### Prefix dominance for \(s=0\)

Here \(A=2B\), \(x=4^B\), \(y=3^B\). Put \(k=a+2b\), \(k_0=2B\). In the nonnegative quadrant, the vertical cone based at \(y\) is exactly the set of this color with \(k\ge k_0\): the second cone coordinate is \((k-2B)/3\), and its nonnegativity also makes the first coordinate nonnegative. Consequently every owner of \(U\) has \(k\ge k_0\).

The forced chain \(v_m=yg^m\), \(0\le m\le B\), selects all right endpoints \(2v_m/3\), \(0\le m<B\). These are exactly **all** vertices on the diagonal \(k=k_0-1\), and belong to \(W\). The last forced east edge gives \(x\le2t/3\).

Let \(P\) contain all preferred-color points on
\[
k=k_0-3,\ k_0-6,\ldots\ge0,
\]
and let \(R\) contain all right-color points on
\[
k=k_0-4,\ k_0-7,\ldots\ge0.
\]
The set \(P\) is disjoint from \(U\). Every right endpoint of a newly owned edge has diagonal \(k-1\) for a north/east edge, or \(k+2\) for a rooted edge. It consequently lies either in \(R\) or on the already selected frontier \(k_0-1\). Thus \(W\cup R\) covers \(B(U\cup P)\).

All these points lie on the board. On \(a+2b=k\), the largest numerical label is \(2^k\), so every added owner is at most \(x/8\le t/12\); every new cover point is at most \(x/16\). In particular no added owner is the excluded exceptional root, since every isolate or patch root exceeds \(4t/27\).

The number of points on a diagonal \(k\ge0\) is \(\lfloor k/2\rfloor+1\), with the value zero at \(k=-1\). Pair each owner diagonal \(k_0-3n\) with cover diagonal \(k_0-3n-1\). The difference is one exactly when \(n\) is even. Therefore
\[
|P|-|R|=\lfloor B/3\rfloor,
\]
and
\[
d(U\cup P)\ge |U|+|P|-|W|-|R|
=D_j^*+\lfloor B/3\rfloor. \tag{P1}
\]
Maximality rules out \(B\ge3\). No assertion of full-class filling is used: the new owners and the precise repairing cover are explicitly identified.

#### Prefix dominance for \(r=0\)

Here \(B=2A\), \(x=2^A\), \(y=9^A\). Use \(k=2a+b\), \(k_0=2A\). The horizontal cone is exactly the preferred-color part of \(k\ge k_0\). The forced \(q\)-chain selects every left vertex on \(k=k_0-1\), namely its east-left endpoints.

Add preferred-color diagonals \(k_0-3,k_0-6,\ldots\) and left-color cover diagonals \(k_0-4,k_0-7,\ldots\). A new north/east edge has left diagonal \(k-1\), and a new rooted edge has left diagonal \(k+2\), so the same repair is valid. On \(2a+b=k\), the largest label is \(3^k\); all added owners are at most \(y/27\le t/27\), and cannot be the excluded exceptional root.

The same diagonal count gives
\[
d(U\cup P)\ge D_j^*+\lfloor A/3\rfloor. \tag{P2}
\]
Thus \(A\le2\). This includes the degenerate-axis availability conditions and does not use the erroneous assumption that the small vertical patch ends at \(27/2\).

#### Mandatory small owners outside the top vertical color

Let \(j_{\rm top}\) be the color of \(3^{\lfloor\log_3t\rfloor}\). Every incomparable-root maximizer is in that color, since its unique vertical root exceeds \(t/3\).

For any other color with \(D_j^*>0\), the root possibilities left by (P1)–(P2) force the following owners:

| Color | Remaining root configuration | Forced owner |
|---|---|---|
| 0 | origin | \(6\) |
| 1 | \(r=0,A=1\), or \(s=0,B=2\) | \(12\) |
| 2 | \(r=0,A=2\), or \(s=0,B=1\) | \(18\), for \(t\ge18\) |

For color zero, \(R(1)\) forces exactly one of \(2,3\) into \(W\); selecting both would destroy essentiality. The selected endpoint then forces owner \(6\). The color-one statements follow from the \(q\)-chain plus its first strip, or the \(g\)-chain \(9,12,16\). For color two, the \(q\)-chain \(4,18,81\) forces 18. In the other case the \(g\)-chain is \(3,4\); once \(t\ge9\), its rooted strip forces 18, so the interval \(9\le t<18\) cannot support that canonical configuration. The very small boards remain separate finite base cases.

These statements concern every inclusion-minimal global maximizer in the relevant allowed pool. Every maximizing set contains such a subset, so the forced owner belongs to **every** maximizing set in that pool. This is stronger than separately choosing unrelated canonical covers.

#### A common-optimum reduction when there is no patch correction

Assume \(t\ge18\), no patch indicator is active, and suppose for contradiction that a minimum cover \(F\) has
\[
\tau< M=\min_j(K_j-I_j).
\]
Its omitted sets \(U_j=C_j\setminus F\) all attain \(D_j=K_j-\tau>I_j\).

If an isolated owner exists, its graph is empty. Every maximum-deficiency set of its color contains it, and deleting it decreases maximum deficiency exactly by one. Thus \(U_j\setminus\{e\}\) is a maximizer in the restricted pool, with deficiency \(D_j-1>0\). In the other colors no deletion is needed.

The two colors different from \(j_{\rm top}\) therefore omit their corresponding two members of \(\{6,12,18\}\) from the **same** cover \(F\). If a minimal maximizing subset of the top color were origin-containing or degenerate, it would force the third member outside \(F\), leaving the corner \(\{6,12,18\}\) uncovered. Hence the top color has an incomparable-root maximizing subset. Its restricted maximum deficiency is exactly one, by the aggregate argument above. Consequently
\[
\boxed{\tau=K_{j_{\rm top}}-I_{j_{\rm top}}-1.} \tag{P3}
\]
Under the counterexample assumption, \(j_{\rm top}\) must therefore minimize the isolated-point-adjusted color count, and the top color must support one of the high critical configurations.

This does not finish the contradiction. A statement that membership in the high numerical window alone forces a nonwinning phase has not been proved. Actual critical-set existence may be essential. With a patch correction, deleting its root need not decrease matching deficiency exactly by one; the passage to simultaneous restricted maximizers must be justified separately.

### Gaps

The canonical audit is complete. The deep-branch exclusion and prefix repairs are new proofs, not a global solution. The remaining obligations are the high-branch phase comparison, the active-patch case, and explicit treatment of the small base boards if these reductions are assembled into a global theorem. No broad enumeration, forward closure, full-class filling, submodular uncrossing, independent forest-component count, or matroid circuit elimination has been assumed.
