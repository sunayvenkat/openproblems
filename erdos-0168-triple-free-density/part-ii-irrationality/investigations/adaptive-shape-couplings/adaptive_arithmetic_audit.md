# Fresh audit of adaptive palette arithmetic

## Does the arbitrary-shape construction include all masses, delays and arithmetic factors?

### Takeaway

**PASS.** AS1–AS3 extend the complete fractional repair to arbitrary finite three-color palettes, including collinear shapes and triangles with determinant greater than one. One common weight denominator suffices. No substantive erratum was found; all stated balances and all boundary costs remain necessary hypotheses. — [Construction](adaptive_arithmetic.md), [supplied checker](adaptive_arithmetic_check.py), [independent mixed-palette checker](adaptive_arithmetic_audit_check.py).

### Cited Findings

- The supplied checker passes its determinant-four and collinear examples. It reconstructs their complete costs \(36581/88452\) and \(10064165/16982784\), respectively, and the actual head identity at all 101 events through \(2^{18}\). These are finite arithmetic checks, not adequate-return examples. — [Supplied checker](adaptive_arithmetic_check.py).
- The new audit checker imports no companion code. It mixes the two geometries with anchor weights \(1/9\) and \(2/9\), so their combined physical marginals equal one. It computes rank costs from actual event increments, rather than importing the supplied interval-overlay routine, and computes bulk tails from actual roots shifted horizontally or vertically. — [Independent checker](adaptive_arithmetic_audit_check.py).
- The independent complete costs are \(13575941/25474176\) at period six and \(1075369770751/2008384035840\) at period twelve. Both satisfy the asserted full one-\(S\) clearance with \(S=9\). Global event replay covers all 280 and 179 actual events through \(2^{30}\) and \(2^{24}\), respectively, and retains the arrival \(27/2\). The period-six replay includes later blocks on both edges. — [Independent exact output](adaptive_arithmetic_audit_check.py).

### Inferences

**AA1. Distinct colors replace any determinant assumption.** Three offsets of different colors cannot have the same residue modulo a period divisible by three. For a fixed anchored type, a physical point therefore has at most one owner. Coverage at every residue node gives unit full-plane marginals, bounds every weight by one, and gives total type mass \(m^2/3\). Keeping only wholly contained triples leaves nonnegative residual mass. At a point with \(a\ge H,b\ge V\), every owner anchor is nonnegative, so no residual remains. These statements use coordinate spans and colors, not area or unimodularity. — [AS1](adaptive_arithmetic.md).

**AA2. The boundary partition is exhaustive and repeats exactly.** For cuts \(A\ge H,B\ge V\), the corner and the two disjoint families of edge blocks contain all residual mass. On a bottom block horizontal containment has already stabilized; on a left block vertical containment has stabilized. Periodic type weights then give the asserted repeated residual masses. Equal total color mass in the corner and both root blocks is an explicit constraint. Nothing in coverage alone supplies these six equations. — [AS1–AS2](adaptive_arithmetic.md), [independent residual reconstruction](adaptive_arithmetic_audit_check.py).

**AA3. Rank splitting pays only one \(S\).** If \(Sx\) is integral, all residual point masses, cumulative rank endpoints and differences of those endpoints lie in \(S^{-1}\mathbb Z\). The three rank partitions are overlaid by taking endpoint differences; denominators are not multiplied across colors. An empty balanced component has no triples or cost. Thus one \(S\) clears every repaired finite mass. — [AS2](adaptive_arithmetic.md), [independent event-increment rank reconstruction](adaptive_arithmetic_audit_check.py).

**AA4. The low rows and all geometric tails are charged.** For bottom points \(a\ge A\ge m\ge6\), shifting horizontally by \(m\) scales actual times by \(2^m\), including both low-row retimings. For left points \(b\ge B\ge m\), vertical shifts scale ordinary times by \(3^m\). A bulk root has coordinates at most \(H+m-1,V+m-1\). Its first actual member handles exceptional small roots; its positive horizontal translates have stabilized low-row delays, and positive vertical translates are ordinary. The displayed three-term bulk sum follows by summing these disjoint geometric pieces. — [AS2](adaptive_arithmetic.md), [actual shifted-root calculation](adaptive_arithmetic_audit_check.py).

Every root reciprocal denominator divides \(2^{A+m}3^{B+m}\): ordinary coordinates obey that bound; dyadic retiming gives denominator \(3\,2^{a-1}\); row-one retiming gives \(27\,2^{a-3}\), with the \(a=2\) reciprocal equal to \(2/27\). Since \(B\ge6\), this includes every low exception. Multiplication by the two odd geometric factors and \(S\) proves
\[
D=S(2^m-1)(3^m-1)2^m3^m\,2^A3^B,\qquad DQ\in\mathbb Z.
\]

The formula is a sufficient full clearing factor, not a reduced-denominator lower bound. Its factors do not multiply with the number of shapes because all weights share \(S\) and all roots fit the same prime-power box. — [AS2](adaptive_arithmetic.md).

**Buffer clarification.** The same construction and exact factor work for larger cuts \(A,B\) with \(A\ge H,B\ge V\), \(A,B\ge m\), using their actual values. Fixed additional whole periods retain the \(O(m)\) overhead in AS6. Unbounded additional buffers must instead be charged explicitly; a linear enlargement cannot be hidden in that \(O(m)\). This is consistent with the buffered finite companion example and does not give it an infinite feasibility interpretation. — [AS1–AS2 and AS6](adaptive_arithmetic.md), [buffered witness and its charged factor](adaptive_capacity.md).

**AA5. Collinear shapes still give strictness.** A positive-weight type has a quadratic number of deep ordinary translates on its full-index anchor lattice. Its distinct exponent points have distinct smooth monomials, so its logarithmic dispersion is positive even if all three points are collinear. The accepted integrated partial-mass argument applies with the actual imbalance \(o(T)\). Its constants may depend on the candidate; no positive uniform dispersion across growing palettes is required. — [AS3](adaptive_arithmetic.md), [accepted weighted strictness audit](../fractional-farey-transport/fractional_arithmetic_audit.md).

### Gaps

- The balances and head constraints can be infeasible. Exact complete arithmetic proves neither such feasibility nor a useful error estimate by itself. — [Construction scope](adaptive_arithmetic.md), [companion exact examples and obstruction](adaptive_capacity.md).
- The finite checks exercise the two stated geometries and periods six and twelve. The arbitrary-palette and general-period assertions rest on the reconstructed written proof, rather than on a finite enumeration of all shapes. — [Independent certificate](adaptive_arithmetic_audit_check.py).

## Is the minimum-color head criterion exact, with the stated coefficient and support bounds?

### Takeaway

**PASS.** The new criterion is exactly equivalent to the completed mass of the specified componentwise repair. It replaces the exponential color-choice projection by polynomially many local inequalities, without new variables. The determinant bound may use an actual vertex's positive support, but sparsity is not guaranteed. — [AS4–AS6](adaptive_arithmetic.md), [independent all-event identity checks](adaptive_arithmetic_audit_check.py).

### Cited Findings

- For a balanced finite component, actual-arrival rank matching completes the minimum of its three arrived masses. The audit independently obtains that completed mass from the jumps of the minimum at actual events, and checks the scaled copies too. — [Independent checker](adaptive_arithmetic_audit_check.py).
- At every checked event, the audit directly verifies both conservation and the equivalence between zero total defect and the proposed zero-partial-mass/local-minimum conditions. All simultaneous arrivals are processed together. — [Independent event loop](adaptive_arithmetic_audit_check.py).

### Inferences

**AA6. Choosing one global minimum color is sufficient.** The exhaustive marginal partition gives, for each color \(j\),
\[
T_j=G_B+P_j+\sum_E C_{E,j}.
\]
For any chosen minimizing \(j\), \(T_j=\tau\). Subtracting the actual completed mass \(G_B+\sum_E\min_\ell C_{E,\ell}\) gives exactly AS4. Every term is nonnegative. Thus head equality holds precisely when \(P_j=0\) and \(C_{E,j}\le C_{E,\ell}\) for every component and every color. One minimizing color suffices even at ties; imposing all is harmless. — [AS4–AS5](adaptive_arithmetic.md).

Incomplete bulk profiles have nonnegative integer coefficients. Their vanishing therefore bans every type with positive profile at that chosen minimum color. These are valid zero-surplus bans for fractional weights; no integer-only ban at positive surplus is imported. Each residual component mass is affine with integer coefficients in the original weights. All relevant cutoff positions are actual token arrivals, independent of those weights. Consequently the local conditions are finite linear constraints and check the actual repair, rather than an ideal unrestricted residual matcher. — [AS4](adaptive_arithmetic.md).

**AA7. Size and height are genuinely polynomial.** Forward retiming implies at most \((KH+1)^2\) arrived points for \(X\le2^{KH}\). There are \(O_K(1+H/m)\) possibly arrived edge blocks. Each event requires at most three color comparisons per component, after collecting support bans once per type. This gives the stated \(O_K(H^2(1+H/m))\) head rows. A point belongs to at most one owner of a specified type, so each affine component coefficient is bounded by its point count. Root balance regions have polynomial area. All coefficients and right sides are therefore bounded by a constant times \((K+1)^2(H+V+m)^2\). This is a formulation-size bound, not an efficient-search or nonemptiness theorem. — [AS4–AS5](adaptive_arithmetic.md).

**AA8. One determinant clears every coordinate.** Nonnegative coverage bounds all variables by one, giving a compact feasible polytope. At a vertex its active integer normals span the ambient variable space: otherwise a small two-sided movement orthogonal to all active normals preserves every inactive strict inequality and contradicts extremality. Selecting independent active equations and using Cramer's rule gives one common denominator, bounded by the product of row norms. — [AS5](adaptive_arithmetic.md).

For a vertex with \(s\) positive coordinates, fixing its zero coordinates first leaves active restricted normals spanning all \(s\) support directions by the same two-sided argument. Hence the determinant dimension can indeed be \(s\). An initially irrational feasible point causes no problem: compact nonemptiness supplies a rational vertex; alternatively its fixed zero-coordinate face has such a vertex. Neither argument promises that a feasible vertex is sparse. — [Support-sensitive statement in AS5](adaptive_arithmetic.md).

### Gaps

- A large palette need not have small surviving support or a sparse feasible vertex. Such a claim would need its own proof; the audit does not infer it from the support-sensitive bound. — [AS5 gaps](adaptive_arithmetic.md).
- Replacing all separate components by a single global residual component changes the construction. The resulting capacity condition cannot inherit the presently proved cheap-tail arithmetic. — [AS4 gaps](adaptive_arithmetic.md).

## Do the continued-fraction palettes preserve the arithmetic implication without assuming feasibility?

### Takeaway

**PASS as a conditional theorem.** The pure-convergent palette has logarithmic denominator overhead \(O(\log^3H)\); fixed bounded two-term combinations have \(O(\log^5H)\). These bounds include all earlier vectors, without requiring their individual dispersions to tend to zero. Actual infinite long-head feasibility remains open. — [AS7–AS9](adaptive_arithmetic.md).

### Cited Findings

- The supplied checker verifies the actual continued-fraction cylinder containing the stated prefix using integer power comparisons. The independent checker separately canonicalizes its first small palette, obtaining eleven shapes, and generates 28 directions from bounded two-term coefficients, including \((4,-3)\). It does not import the supplied palette generator. — [Supplied CF certificate](adaptive_arithmetic_check.py), [independent generation](adaptive_arithmetic_audit_check.py).
- The algebraic identity \(\{0,u,u-v\}-u=\{0,-u,-v\}\) and reflection of a collinear progression demonstrate why canonical translation/permutation deduplication is necessary. — [AS7 and normalized generator](adaptive_arithmetic.md).

### Inferences

**AA9. Both size estimates include all variables.** The recurrence \(q_{i+2}\ge2q_i\), including the two initial denominator-one convergents, gives \(J\le2\lfloor\log_2H\rfloor+2\). Opposite-color unordered pairs, two orientations, and eligible collinear progressions contribute at most \(2\binom J2+J=J^2\) shapes before deduplication. With fixed period, \(d=Rm^2=O(\log^2H)\). Applying the full determinant height bound gives \(\log S=O(\log^3H)\). — [AS7](adaptive_arithmetic.md).

Bounded coefficients produce at most \((2B_0+1)^2J^2\) directions. Opposite-color pairs and eligible collinear progressions then give \(R=O(B_0^4\log^4H)\). For fixed \(B_0,m\), the full dimension bound gives \(\log S=O(\log^5H)\). If either grows, AS6 must charge its actual \(d=Rm^2\), including the \(d\log(d+1)\) term. — [AS8](adaptive_arithmetic.md).

Older vectors may retain fixed nonzero dispersion. That does not spoil the cost bound: the relevant arithmetic quantity is the enclosing box \(H\log2+V\log3\), while strictness only needs one positive dispersed type for each fixed candidate. At actual convergent boxes \(H=q_n,V=p_n\), the convergent error gives \(V\log3=H\log2+o(1)\). Thus the subexponential determinant overhead preserves clearing exponent two without an individual near-isotime assumption on all shapes. — [AS2–AS3 and AS9](adaptive_arithmetic.md).

**AA10. The tail estimate uses actual head equality.** Once \(G(X)=\tau(X)\), monotonicity yields \(0\le\tau(t)-G(t)\le\tau(t)-\tau(X)\) for \(t\ge X\). The latter increment is bounded by newly arrived mass. Integration against \(t^{-2}\) is therefore bounded by its reciprocal arrival tail, \(O(\log X/X)\); bounded forward retimings preserve this order. With a feasible head through \(2^{(2+\varepsilon)H}\), complete rationality, strictness and the proved subexponential overhead give positive cleared errors tending to zero. Rational \(M\) would make a fixed-denominator multiple of them positive integers tending to zero. — [AS9](adaptive_arithmetic.md), [earlier detailed tail audit](../fractional-farey-transport/fractional_arithmetic_audit.md).

### Gaps

- **OPEN:** an actual infinite sequence of nonempty balanced head polytopes through \(2^{(2+\varepsilon)H}\). Neither palette cardinality nor the finite companion witnesses supply it. The accepted finite optimum and density identities are earlier dependencies, not independently re-proved here. — [AS9 gaps](adaptive_arithmetic.md), [finite findings](adaptive_capacity.md), [structural limits](adaptive_structure.md).
- Skipped Lean, external review, priority checks and new model exploration. Material risk: confusing the audited conditional arithmetic theorem, or its polynomial local formulation, with a proof of infinite actual feasibility or of irrationality. — [Audit scope and independent certificate](adaptive_arithmetic_audit_check.py).
