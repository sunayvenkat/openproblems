# Independent review: global hole filling for the color-class matching graph

**Verdict: the proposed filling lemma is valid under the precise whole-face assumptions below.** Concave boundary vertices, holes, and old edges inside holes do not invalidate the matching replacement. The argument also proves a useful unconditional normalization: a deficiency maximizer of largest cardinality has connected complement in the full infinite face-center lattice. This is an auxiliary result; it does not prove the sharp candidate (C) or irrationality.

## Does the boundary ownership claim survive concave corners and holes?

### Takeaway

Yes. At every boundary vertex exactly one of the two boundary edges is owned outside the added region. Those old boundary edges form a perfect matching of all boundary vertices, including every hole boundary.

### Cited Findings

- For a color-j label u, the owned edges are N(u)={u/3,2u/3}, E(u)={u/2,3u/2}, and R(u)={2u,3u}. They alternate around its honeycomb hexagon with edges owned by u/6, 4u/3, and9u/2. — [Current cover definitions and local filling proof](cover.md)

### Inferences

**Precise hypotheses.** Work in the infinite honeycomb graph obtained by removing color j from the triangular lattice. Each edge has one owner among its two incident color-j hexagons; each hexagon owns three alternating sides. Let U be a set of allowed color-j labels, and let V be a nonempty finite set of omitted labels, disjoint from U, such that:

1. The union R of the hexagons in V is connected by shared edges.
2. Every label in V has all three of its owned edges available in the finite domain.
3. Every boundary edge of R owned by a face outside V already belongs to B(U).

In the weighted triangle, condition2 means that both exponents of u are positive and 3u≤t. It puts all six hexagon vertices in the domain. Given those vertices, an outside-owned boundary edge is available whenever its owner belongs to U, because the corresponding three vertices are then all in the domain. Thus condition3 agrees with the coordinator's ownership hypothesis. Merely saying that a center lies in D_t, without condition2 or an equivalent whole-face condition, would not suffice.

At a vertex of the honeycomb exactly three hexagons meet. A boundary vertex of R has either one or two incident V-faces:

- With one V-face, the boundary edges are the two consecutive sides of that face at the vertex. Exactly one is owned by that face, so exactly one is owned outside V.
- With two V-faces, the boundary edges are the two consecutive sides of the unique outside face. Exactly one is owned by that outside face, again giving exactly one outside-owned boundary edge.

This includes concave corners. A boundary vertex therefore has exactly two boundary edges, one old and one new. There are no pinched boundary vertices: in the hexagonal tiling any two faces meeting at a vertex also share an edge. Hence the boundary is a disjoint union of simple cycles, and the outside-owned edges form a matching P that covers each boundary vertex exactly once. If B is the number of boundary vertices, there are B boundary edges and |P|=B/2.

Every geometric interior edge has both incident faces in V, so its owner lies in V and it is absent from B(U). Every interior vertex has all three incident faces in V, so every edge incident to it is new. This proves the needed "no old interior edges" assertion rather than assuming it.

### Gaps

None in the boundary argument under the listed hypotheses. Truncated hexagons touching the finite domain boundary require a separate argument; they are not covered just because their centers are allowed labels.

## Is the Euler and matching replacement calculation correct?

### Takeaway

Yes. It proves the slightly stronger inequality

\[
d(U\cup V)\ge d(U)+\lfloor h/2\rfloor,
\]

where h is the number of holes of R. In particular deficiency cannot decrease.

### Cited Findings

- The deficiency is d(U)=|U|−ν(B(U)); the exact finite-cover reduction maximizes this quantity over U. — [Matching reduction](../open-conjecture-transfer-search/168_grid.md)

### Inferences

Write m=|V|, I for the number of interior honeycomb vertices, E_int for the number of interior edges, and B for the number of boundary vertices/edges. Each V-face contributes its three owned edges, every interior edge has its owner in V, and precisely half the boundary edges have their owner in V. Therefore

\[
3m=E_{\rm int}+B/2.
\tag{1}
\]

The connected planar graph forming R has I+B vertices, E_int+B edges, and m+h bounded faces: the m hexagons and the h holes. Euler's formula gives

\[
I-E_{\rm int}+m=1-h,
\qquad E_{\rm int}=m+I-1+h.
\tag{2}
\]

Combining (1)–(2),

\[
I+B/2=2m+1-h.
\tag{3}
\]

There is no parity restriction forcing h to be odd. For example, use axial coordinates with face adjacencies ±(1,0), ±(0,1), ±(1,1). The 5×5 rhombus {0,…,4}² with faces (1,1) and (3,3) removed is connected and has two separate holes. It has m=23, E_int=44, B=50, I=20, so I+B/2=45=2m+1−2. The construction embeds in a sufficiently large weighted triangle after translating all exponents to be positive; selecting the surrounding outside faces supplies the required old boundary edges.

Now take any matching M in B(U∪V). Keep all edges of M that are not sides or interior edges of R; call the kept set M_out. These edges all belong to B(U), because every edge added by V lies in the closure of R. This classification deliberately treats edges lying inside holes as outside R, so those matching edges are retained as well.

Let b be the number of boundary vertices unused by M_out. Every interior vertex is unused by M_out. Thus the removed portion M_in has at most

\[
\left\lfloor\frac{I+b}{2}\right\rfloor
\]

edges. Start with the old boundary perfect matching P from the first section. Deleting the B−b unavailable boundary vertices destroys at most B−b edges of P, leaving at least

\[
\max(0,B/2-(B-b))=\max(0,b-B/2)
\]

old edges disjoint from M_out. Adding those retained edges of P produces a matching of B(U).

For every integer 0≤b≤B,

\[
\left\lfloor\frac{I+b}{2}\right\rfloor-\max(0,b-B/2)
\le\left\lfloor\frac{I+B/2}{2}\right\rfloor.
\tag{4}
\]

For b≤B/2 the first term is increasing in b. For b≥B/2, subtracting b−B/2 makes the expression nonincreasing. Its maximum is therefore attained at b=B/2. Using (3), the last bound is

\[
\left\lfloor\frac{2m+1-h}{2}\right\rfloor
=m-\lfloor h/2\rfloor.
\]

Apply this replacement to a maximum matching M. It proves

\[
\nu(B(U\cup V))-\nu(B(U))\le m-\lfloor h/2\rfloor,
\]

and subtracting from |U∪V|−|U|=m yields the asserted deficiency bound.

Old edges outside R may meet either outer or inner boundary vertices; their effect is exactly the unavailable set of B−b vertices. Old edges entirely in a hole are likewise retained. Neither case requires an additional topological assumption.

### Gaps

None in this replacement proof under the whole-face and old-boundary-edge hypotheses. It does not characterize the maximum matching, nor establish the desired sharp bound on maximum deficiency.

## Are finite complementary components automatically valid interior regions in D_t?

### Takeaway

Yes. Any finite component V of the complement of U in the full face-center lattice satisfies a,b≥2 and 2^a3^b≤t/6. The filling lemma therefore applies automatically. A largest-cardinality deficiency maximizer has connected full-plane complement.

### Cited Findings

- The finite domain is D_t={(a,b)∈Z²:a,b≥0, 2^a3^b≤t}, and color j is a+2b modulo3. — [Domain and coloring](../open-conjecture-transfer-search/168_grid.md)

### Inferences

The full infinite color-j face-center lattice consists of all integer exponent pairs satisfying the color congruence, with neighbor differences

\[
\pm(1,1),\qquad\pm(-2,1),\qquad\pm(1,-2).
\]

Let U⊆C_j(D_t) be finite, and let V be a finite nonempty connected component of its complement in this full infinite lattice. **Every neighbor of V lying outside V must belong to U:** otherwise that neighbor would lie in the same complementary component.

Choose a vertex v_a=(a,b) of V minimizing its first coordinate. Its neighbor (a−2,b+1) has smaller first coordinate, so is outside V and hence in U. Thus min a_V≥2. Similarly, at a vertex minimizing b, the neighbor (a+1,b−2) lies in U, proving min b_V≥2.

Finally choose v_max maximizing the positive real value u=2^a3^b on the finite set V. Its neighbor (a+1,b+1) has value 6u, so cannot lie in V and must belong to U. Hence

\[
\max_{v\in V}2^{a(v)}3^{b(v)}\le t/6.
\tag{5}
\]

These three extrema may be different vertices; each conclusion is a bound on the corresponding minimum or maximum over all V. Consequently every v∈V has both exponents positive and 3u≤t/2<t. All three owned edges exist, and every outside-owned boundary face belongs to U by the component argument. Thus V is a feasible whole interior region, and filling it does not decrease d.

Because C_j(D_t) is finite, select U maximizing d(U), and among those maximizers select one with largest cardinality. If its full-plane complement had any finite component V, the above fill would give a feasible U∪V with d(U∪V)≥d(U). A strict increase contradicts maximal deficiency; equality contradicts maximal cardinality. Therefore no finite complementary component exists.

A finite vertex set in the triangular lattice has exactly one unbounded complementary component. To see this directly, use the lattice basis (1,1), (−2,1). The adjacency graph includes the ordinary horizontal and vertical edges of Z². Outside a sufficiently large square containing U, those grid edges connect the entire exterior; every unbounded component meets that exterior. Hence there is only one unbounded component. With no finite components remaining, the full-plane complement of the chosen U is connected.

This proves the auxiliary normalization:

> For every color j and weighted triangle D_t, there exists a set U attaining max(|U|−ν(B(U))) whose complement in the full infinite color-j face-center lattice is connected.

### Gaps

Connected complement does not force U to be connected, give a monotone boundary, prevent multiple corridors to infinity, or provide distinct augmentations for horizontal-axis defects. None of those stronger claims follows from this lemma. The sharp formula (C), its weighted irrationality argument, and the parent open-target goal remain unresolved.

No additional numerical search or formalization was needed for this review; the conclusions above are proved by the explicit ownership, Euler, and matching arguments.
