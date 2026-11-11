# Adaptive shape arithmetic

## Can genuinely different and collinear shapes retain complete cheap arithmetic?

### Takeaway

**Yes. Unimodularity and noncollinearity are unnecessary.** The complete repair theorem extends to any finite palette of distinct three-color shapes in a common coordinate box. The new dependence on palette size is explicit, including all weighted boundaries and tails. This remains a construction theorem conditional on its stated balances, not a long-head feasibility theorem. — [Standalone exact certificate](adaptive_arithmetic_check.py), [audited two-shape predecessor](../fractional-farey-transport/fractional_arithmetic_audit.md).

### Cited Findings

- The accepted token at \((a,b)\) has color \(a-b\bmod3\), actual arrival \(2^a3^b\), except dyadic arrivals \(a\ge1\) are multiplied by \(3/2\), and row-one arrivals \(a\ge2\) by \(9/8\). Thus the arrival \(27/2\) is retained. The rank optimum is \(M=3(1-c)\). — [Accepted input and complete finite dependencies](../fractional-farey-transport/REPORT.md).
- The new checker imports no companion checker. It tests an area-four triangle and a collinear triangle, reconstructing fractional marginals, all finite rank pieces, complete geometric costs, and the actual completed-mass identity at all 101 arrival events through \(2^{18}\), including both later edge periods. — [Certificate](adaptive_arithmetic_check.py).
- For the collinear shape \(\{(0,4),(3,2),(6,0)\}\), giving every anchor mass \(1/3\) produces balanced corner and edges and exact complete cost \(10064165/16982784\). Its actual optimal prefix ends at 72 and first loss is 81. The area-four example has cost \(36581/88452\) and first loss 3. These certify nonvacuity and arithmetic, not an adequate head. — [Exact output](adaptive_arithmetic_check.py).

### Inferences

**AS1. General palette and geometry.** Let \(\mathcal S_1,\ldots,\mathcal S_R\) be distinct sets of three integer points, each with one point of every color. Translate each by its coordinatewise minimum and sort its points. This is a canonical representative modulo translations and permutations. Assume every representative lies in \([0,H]\times[0,V]\), with \(H,V\ge1\). Collinear shapes are allowed. Fix \(m\ge6\) divisible by six. For every shape and anchor residue modulo \(m\), introduce a nonnegative weight \(x_k\): there are \(d=Rm^2\) variables. Three distinct colors ensure distinct residues modulo \(m\), so each physical point belongs to at most one owner of a given type. Impose unit coverage at each of the \(m^2\) residue nodes. Then \(0\le x_k\le1\), \(\sum x_k=m^2/3\), and the plane lifts have unit marginals. No determinant assumption enters. — [Finite residue checks](adaptive_arithmetic_check.py), [mass argument generalized from FA1](../fractional-farey-transport/fractional_arithmetic.md).

Retain every wholly quadrant-contained weighted triple. At a quadrant point \(z\), its residual mass is
\[
w_x(z)=1-\sum_{\text{kept owners of }z}x_k\ge0.
\]
If \(a\ge H,b\ge V\), every possible owner is contained, so the residual vanishes. Put
\[
A=m\lceil H/m\rceil,\qquad B=m\lceil V/m\rceil.
\]
Partition the residual into \(C=[0,A)\times[0,B)\), bottom blocks
\(R_n=[A+mn,A+m(n+1))\times[0,B)\), and left blocks
\(L_n=[0,A)\times[B+mn,B+m(n+1))\).
Residual masses repeat under the corresponding \(m\)-shift: in bottom blocks no horizontal crossing is possible; in left blocks no vertical crossing is possible. Impose equal color mass separately in \(C,R_0,L_0\). These six linear equations are substantive restrictions, not automatic consequences of coverage.

**AS2. Full cost and one weight denominator.** If \(Sx_k\) are integers, every residual mass is a multiple of \(1/S\). Overlay the three ordered actual-arrival mass partitions in each balanced component. All cumulative endpoints and their differences remain in \(S^{-1}\mathbb Z\); only one factor \(S\) is needed. Repeat the bottom repair horizontally, scaling actual arrivals by \(2^m\), and the left repair vertically, scaling by \(3^m\). These exact scalings retain all low delays because \(A,B\ge m\ge6\). Zero balanced mass gives an empty repair. The full residual cost is
\[
q_C+\frac{2^m}{2^m-1}q_R+\frac{3^m}{3^m-1}q_L.
\]

For any normalized bulk type, its least contained anchor has both coordinates at most \(m-1\). Let \(M_{\rm act},M_{\rm asym},M_{\rm raw}\) be its first actual, horizontally stabilized, and ordinary maxima. Its entire stream contributes
\[
x_k\left(\frac1{M_{\rm act}}+
\frac1{(2^m-1)M_{\rm asym}}+
\frac{2^m}{(2^m-1)(3^m-1)M_{\rm raw}}\right).
\]
The first member retains exceptional roots; later horizontal members have stable low-row retimings; every positive vertical translate is ordinary. Root coordinate bounds and the bounded timing corrections therefore give the safe complete clearance
\[
D=S(2^m-1)(3^m-1)2^m3^m\,2^A3^B,\qquad DQ(x)\in\mathbb Z. \tag{AS2}
\]
The number of shapes does not introduce another factor: all their masses share \(S\), and all root denominators divide the same prime-power box bound. This is a clearing upper bound, not a reduced-denominator lower bound. — [All terms verified for nonunimodular and collinear examples](adaptive_arithmetic_check.py), [original timing proof](../fractional-farey-transport/fractional_arithmetic_audit.md).

**AS3. Strictness includes collinear shapes.** At least one type has positive weight. Its deep ordinary translates have a quadratic anchor count on a full-index lattice; the anchors, rather than the three offsets, supply the two-dimensional count. Three distinct smooth monomials have distinct actual ordinary times, even when their exponent points are collinear. The logarithmic dispersion is therefore positive. The accepted integrated partial-mass proof, with actual imbalance \(o(T)\), gives \(Q(x)<M\) candidate by candidate. No uniform dispersion in the growing box is asserted. — [Weighted dispersion proof](../fractional-farey-transport/fractional_arithmetic.md).

### Gaps

- These balance equations can be infeasible together with a required head. Enlarging the palette does not prove feasibility, and an arbitrary optimal finite matching need not fit the box. — [Companion capacity investigation](adaptive_capacity.md).
- Nearly equal arrival times are unnecessary for the arithmetic theorem and insufficient for head agreement. The useful asymptotic box condition is \(V\log3=H\log2+o(H)\), regardless of the individual shapes' dispersions. — [AS2 derivation above; prior failed head inference](../farey-transport-corrections/REPORT.md).

## Can actual head feasibility be imposed by polynomially many local inequalities?

### Takeaway

**Yes. A minimum-color conservation identity replaces the previous exponentially many color-choice inequalities.** This is an exact characterization of the specified repaired coupling, not merely a necessary global residual-capacity condition. It also allows the determinant dimension to be reduced to the actual positive support of a feasible vertex. — [Exact all-event identity check](adaptive_arithmetic_check.py).

### Cited Findings

- Componentwise actual rank matching completes exactly the minimum arrived mass of its three colors. The predecessor encoded sums of these minima by all possible choices of component colors. — [FA5–FA7 and audit](../fractional-farey-transport/fractional_arithmetic_audit.md).
- The current checker independently reconstructs the explicitly repaired completed mass and tests the new equivalence at every actual event, including ties and \(27/2\). — [Certificate](adaptive_arithmetic_check.py).

### Inferences

**AS4. Choose one actual minimum color.** At a cutoff \(t\), let \(T_j(t)\) be total arrived tokens, \(\tau(t)=\min_jT_j(t)\), \(G_B(t;x)\) completed bulk mass, and \(C_{E,j}(t;x)\) arrived residual mass in repair component \(E\). Let \(P_j(t;x)\) be arrived color-\(j\) mass belonging to incomplete retained bulk triples. Conservation is
\[
T_j=G_B+P_j+\sum_E C_{E,j}.
\]
Choose any deterministic global minimum color \(j(t)\), so \(T_{j(t)}=\tau\). The actual repaired completed mass is
\(G=G_B+\sum_E\min_\ell C_{E,\ell}\). Consequently
\[
\boxed{\tau-G=P_{j(t)}+
\sum_E\left(C_{E,j(t)}-\min_\ell C_{E,\ell}\right).} \tag{AS4}
\]
Every term is nonnegative. Thus equality with the optimum at this cutoff is **equivalent** to
\[
P_{j(t)}=0,\qquad
C_{E,j(t)}\le C_{E,\ell}\quad\text{for every }E,\ell. \tag{AS5}
\]
One may use the least minimizing color; imposing all minimizing colors is redundant but valid. Simultaneous arrivals are processed together. Right-continuity and checking every actual event through \(X\) cover every intervening real cutoff. Zero arrived components can be omitted.

Since \(P_j=\sum_k p_{k,j}(t)x_k\) with nonnegative integer coefficients, its vanishing simply sets to zero every type with \(p_{k,j}(t)>0\). These are zero-surplus bans, never integer-only bans at positive surplus. The second family is linear because each component mass is an affine integer-coefficient function of \(x\). Coverage, six balances, these bans and local inequalities therefore give an exact finite linear formulation in the original variables. It avoids every auxiliary minimum variable and the exponentially many combinations in the earlier projection.

For \(X\le2^{KH}\), the number \(N_X\) of arrived points is at most \((KH+1)^2\). The number of possibly arrived edge components is \(O_K(1+H/m)\). After collecting support bans once per type, the head requires at most
\[
O_K\!\left(H^2(1+H/m)\right)
\]
local linear inequalities, besides \(O(d+m^2)\) nonnegativity, coverage and ban rows. Coefficients are bounded by a constant times
\(L_K=(K+1)^2(H+V+m)^2\): each selected component uses each arrived point at most once, and root balances have polynomial area. This proves a polynomial-size formulation, not a complexity guarantee for any chosen exact implementation.

**AS5. General and support-sensitive vertex bounds.** The feasible polytope is bounded by coverage. A nonempty finite bounded polytope has a vertex; select \(d\) independent active integer equations. One determinant clears all coordinates:
\[
S\le(\sqrt d\,C L_K)^d.
\]
Thus
\[
\log D\le H\log2+V\log3+
O\!\left(m+d\log(H+V+m)+d\log(d+1)\right). \tag{AS6}
\]
If the chosen vertex has only \(s\) positive coordinates, delete its zero coordinates first. Active nonzero rows restricted to that support must span all \(s\) directions, or a small two-sided feasible movement would contradict extremality. One may therefore use
\[
S\le(\sqrt s\,C L_K)^s
\]
instead. A large palette is affordable if its feasible vertex is sufficiently sparse, but no such sparsity theorem is assumed. After zero-surplus bans, the surviving variable count is another immediate valid dimension bound.

### Gaps

- Polynomial formulation size does not imply nonemptiness or a practical exact search at every large box. Nor does a large palette automatically have a sparse feasible vertex. — [Companion exact search](adaptive_capacity.md).
- The equivalence uses the **actual separate repair components**. Replacing them by one ideal global residual component changes the construction and loses the present cheap-tail theorem. — [Prior capacity-versus-repair distinction](../fractional-farey-transport/fractional_arithmetic_audit.md).

## Can all earlier continued fractions and bounded sums be included affordably?

### Takeaway

**Yes. All earlier convergents cost only a polylogarithmic arithmetic overhead, and bounded two-term sums remain affordable.** This supplies concrete growing palettes without assuming an infinite favorable residue pattern. Actual infinite long-head feasibility is still the missing theorem. — [Exact normalized palette generator](adaptive_arithmetic_check.py).

### Cited Findings

- The checker certifies the actual continued-fraction prefix \(0/1,1/1,1/2,2/3,5/8,12/19,41/65,53/84\) by its recurrence and the exact cylinder inequalities \(3^{94}<2^{149}\), \(2^{84}<3^{53}\). Pure-convergent palettes below have 11, 16 and 27 shapes at boxes \((8,5),(27,17),(84,53)\), respectively. — [Integer comparisons and generator](adaptive_arithmetic_check.py).
- Apparent extra triangles obtained by reanchoring can be duplicates: \(\{0,u,u-v\}-u=\{0,-u,-v\}\). Reflection of the collinear set \(\{0,w,2w\}\) is also its translate. The checker normalizes and deduplicates these exactly. — [Canonical-shape assertion](adaptive_arithmetic_check.py).

### Inferences

**AS7. Pure-convergent palette.** At the actual convergent \(p_n/q_n\), put \(H=q_n,V=p_n\). Let \(w_i=(q_i,-p_i)\) for all earlier convergents, with color increment \(q_i+p_i\bmod3\). Include both orientations of \(\{0,w_i,w_j\}\) whenever the increments are opposite and nonzero. Include \(\{0,w_i,2w_i\}\) for a nonzero increment whenever \(2q_i\le H,2p_i\le V\). Every normalized shape fits the box and has three colors. Quotient by canonical translations and permutations.

Because \(q_{i+2}\ge2q_i\), the number \(J\) of available vectors is at most \(2\lfloor\log_2H\rfloor+2\). Even before deduplication there are at most \(2\binom J2+J=J^2\) shapes. Hence for fixed period six,
\[
R=O(\log^2H),\quad d=O(\log^2H),\quad
\log S=O(\log^3H)=o(H).
\]
Unlike the fixed-palette case, \(S\) need not be polynomial; its proved subexponential bound is sufficient.

**AS8. Bounded two-term combinations.** Fix an integer \(B_0\ge1\). Form all vectors
\[
w=a w_i+b w_j,\qquad |a|,|b|\le B_0,
\]
then retain nonzero vectors \((q,-p)\) with \(0\le q\le H,0\le p\le V\). There are at most \((2B_0+1)^2J^2\) such vectors. Form opposite-color pair triangles, their reflections, and eligible collinear triples exactly as above. Their normalized spans still fit the box, and their number is
\[
R=O(B_0^4\log^4H).
\]
For fixed \(B_0,m\), AS6 gives
\[
\log S=O(\log^5H)=o(H). \tag{AS8}
\]
This genuinely includes directions absent from the pure convergents: \((4,-3)=(1,-1)+(3,-2)\), for example. It does not assert that such directions solve the head problem. Growing \(m,B_0\) must pay their full \(d=Rm^2\) cost in AS6; no fixed-palette bound may be used silently.

**AS9. Exact conditional finish.** Suppose one of these growing palettes has a nonempty balanced actual-head polytope at infinitely many actual levels through \(X=2^{(2+\varepsilon)H}\), for fixed \(\varepsilon>0\). Then \(V\log3=H\log2+o(1)\), and AS2, AS6–AS8 provide rational vertices with
\[
DQ\in\mathbb Z,\quad \log D=2H\log2+o(H).
\]
AS3 gives strictness. Head equality and monotonicity bound the remaining positive cost by \(O(\log X/X)\). Thus
\[
0<D(M-Q)\le \exp(o(H))\,O(H)\,2^{-\varepsilon H}\longrightarrow0.
\]
Rationality of \(M\) would then yield positive integers tending to zero. This is a complete arithmetic implication for much richer palettes, without proving its infinite feasibility premise. — [Tail and integer-contradiction argument](../fractional-farey-transport/fractional_arithmetic_audit.md).

### Gaps

- **OPEN:** an actual infinite feasible sequence through a super-two-span head. Pure-convergent or bounded-sum palette cardinality alone supplies no such sequence. The other researchers' finite evidence must be read with its exact palette and repair scope. — [Capacity findings](adaptive_capacity.md), [structural findings](adaptive_structure.md).
- Skipped: Lean, installations, broad scans, external review, priority claims and archived edits. Material risk: confusing polynomial local constraints or subexponential weight denominators with actual infinite feasibility.
