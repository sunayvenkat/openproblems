# Fractional transport isolates Erdős’s feasibility gap

**The fractional construction now has a proved arithmetic finish conditional on one precise infinite feasibility theorem, but Erdős #168(ii) remains open.** Complete fractional Farey repairs preserve clearing exponent two, including every boundary component and infinite tail. Their actual optimal-head conditions form a polytope in the original 72 variables, and a single active determinant gives polynomial weight denominators whenever that polytope is nonempty. This removes a previously unproved arithmetic obligation from the proposed fractional route. Exact certificates nevertheless show that fractional weights fail at the same first cutoffs as integer tilings for both tested bases. A separate two-event argument excludes arbitrary nonperiodic weights on the first basis’s two prescribed shapes. Both fresh adversarial audits pass; the goal remains **active**, with actual infinite long-head feasibility still unproved. ([Arithmetic audit](<fractional_arithmetic_audit.md>), [capacity audit](<fractional_capacity_audit.md>))

## Complete fractional repairs preserve cheap arithmetic

Let \(c\) be the limiting maximum density of sets avoiding every triple \(\{n,2n,3n\}\). The earlier finite theorem gives the exact minimum corner-cover size on \(D_t=\{2^a3^b\le t\}\), including its isolated-root and patch corrections. Its positive token representation colors \((a,b)\) by \(a-b\bmod3\), with ordinary arrival \(2^a3^b\), except dyadic arrivals have factor \(3/2\) for \(a\ge1\), and row-one arrivals have factor \(9/8\) for \(a\ge2\). In particular, the exceptional arrival \(12\mapsto27/2\) remains present. If \(T_j(t)\) are arrived color counts, then \(\tau(t)=\min_jT_j(t)\), and the optimal three-color rank cost is \(M=3(1-c)\). These are accepted proved dependencies, not re-proved in this continuation. ([Finite foundation and token identities](<../farey-transport-corrections/REPORT.md>))

Choose a positive unimodular Farey basis \(u=(q,-p),v=(s,-r)\) with opposite nonzero color increments. Put \(H=\max(q,s)\), \(V=\max(p,r)\). The two reflected shapes \(\{0,u,v\}\) and \(\{0,-u,-v\}\), anchored at all 36 original-coordinate residues modulo six, give 72 types. Assign nonnegative weights \(x_k\), requiring total incident weight one at every residue node. Their plane lifts therefore have unit token marginals; coverage also implies \(x_k\le1\) and \(\sum_kx_k=12\). Keep every wholly quadrant-contained weighted triangle. The remaining token mass is nonnegative and lies in \(a<H\) or \(b<V\). ([Complete construction, FA1](<fractional_arithmetic.md>))

Set \(A=6\lceil H/6\rceil\), \(B=6\lceil V/6\rceil\), with \(A,B\ge6\). Partition residual mass into the finite corner, six-wide bottom blocks, and six-high left blocks. Impose equal color mass separately in the corner and each of the two root edge blocks: **balance is an explicit constraint**, not an assumed property of arbitrary fractional weights. Match each component by overlaying its three actual-arrival rank intervals. If a common integer \(S\) clears the weights, every cumulative mass endpoint and every resulting interval length lies in \(S^{-1}\mathbb Z\). Splitting mass therefore introduces **one factor \(S\)**, without multiplying denominators across colors. Balanced zero-mass components require no repair. ([Rank construction and balances, FA1–FA2](<fractional_arithmetic.md>))

Bottom blocks scale by 64 even in the delayed low rows; left blocks scale by 729 above them. Root repair costs \(q_C,q_R,q_L\) consequently contribute \(q_C+(64/63)q_R+(729/728)q_L\). The complete bulk streams separately retain the first actual member, the horizontal geometric continuation, and the ordinary high-row continuation. Every exceptional root and infinite edge is charged, giving

\[
D=S(63\cdot728\cdot2^6 3^6)2^A3^B,
\qquad DQ(x)\in\mathbb Z.
\]

For the actual near-isotime bases, \(V\log3=H\log2+o(1)\). Polynomial \(S\) therefore preserves \(\log D=(2+o(1))H\log2\). This is a full clearing upper bound, not a reduced-denominator lower bound. ([All tails and clearance, FA3](<fractional_arithmetic.md>), [independent reconstruction](<fractional_arithmetic_audit.md>))

The construction is non-vacuous. Balanced nonintegral phase mixtures give exact complete costs \(60728105/101896704\) and \(22603355036644932679/37855052008758706176\), with weight denominators three and two. Their verified optimal heads extend through 64 and 33554432 respectively. These demonstrate complete fractional repairs and their arithmetic; **neither demonstrates the required long head**. ([Exact examples, FA4](<fractional_arithmetic.md>))

## The actual head needs only 72 variables

Let \(g_k(t)\) count completed retained triples of type \(k\), and \(C_{E,j}(t;x)\) be arrived residual mass of color \(j\) in component \(E\). The specified repair has exact completed mass

\[
G_x(t)=\sum_k g_k(t)x_k+\sum_E\min_j C_{E,j}(t;x).
\]

The second sum includes every edge block with an arrived token, not merely its root. Valid marginal conservation gives \(G_x(t)\le\tau(t)\). Optimality through \(X\) is therefore exactly \(G_x(t)\ge\tau(t)\) at every actual arrival event \(t\le X\). This controls the **constructed repair itself**, rather than the weaker capacity of an imagined unrestricted residual matching. ([Actual functional, FA5](<fractional_arithmetic.md>))

Each component count is affine with integer coefficients in \(x\). A sum of component minima exceeds a threshold precisely when the corresponding linear inequality holds for every selection of one color per component. Thus all head conditions project directly into the original 72 variables. The inequality family can be large, but it introduces no auxiliary denominators. Between actual arrivals the counts are constant, so the system is finite. ([Projection proof, FA5–FA6](<fractional_arithmetic.md>))

Fix \(K\) and \(X\le2^{KH}\). Forward retiming bounds the number of head tokens by \((KH+1)^2\). Because the repair components are disjoint, a selected color sum uses each head token at most once. This bounds coefficients across the **entire inequality**, without multiplying a blockwise estimate by the number of blocks. Coverage, balances and head conditions have integer coefficients and right sides bounded by

\[
L=4(K+1)^2(H+V+12)^2.
\]

The resulting polytope is bounded by \(0\le x_k\le1\). If nonempty, it has a vertex with 72 independent active integer equations. One determinant clears every coordinate simultaneously:

\[
S=|\det\mathcal A|\le(\sqrt{72}\,L)^{72},
\qquad Sx\in\mathbb Z^{72}.
\]

Hence \(\log S=O(\log H)\). **Actual feasibility now implies cheap complete arithmetic**, regardless of how many projected head inequalities are needed. This proves neither nonemptiness nor an efficient search algorithm. ([Height and vertex theorem, FA6–FA7](<fractional_arithmetic.md>), [fresh audit](<fractional_arithmetic_audit.md>))

For original-coordinate period \(m\) divisible by six, the same written argument uses \(2m^2\) variables and proves overhead \(O(m+m^2\log(H+V+m))\). The condition \(m^2\log(H+m)=o(H)\), with \(V=O(H)\), preserves exponent two. This parameterized arithmetic theorem leaves larger-period feasibility open; finite checkers exercise period six only. ([General-period implication, FA8](<fractional_arithmetic.md>))

## Zero-surplus certificates exclude both tested bases

Fractional weights do not rescue the two tested period-six examples. Let \(P_{k,j}(t)\) count arrived color-\(j\) vertices in incomplete retained type-\(k\) triangles. Any optimal-head repair must satisfy

\[
\sum_kP_{k,j}(t)x_k\le T_j(t)-\tau(t).
\]

When the right side is zero, every type with positive profile must have zero weight. A positive right side would merely limit its weight; the proof never imports an invalid integer-only exclusion at positive surplus. ([Fractional capacity derivation](<fractional_capacity.md>))

| Basis \(u,v\) | First fractional capacity failure | Previous arrival | Surviving types |
|---|---:|---:|---:|
| \((8,-5),(3,-2)\) | 6561 | 6144 | 50 |
| \((19,-12),(27,-17)\) | 3057647616 | 2902376448 | 53 |

At each threshold an explicit integer potential on the 36 residue nodes has nonnegative sum on every surviving triangle, but total potential \(-2\) or \(-3\). Coverage one makes its weighted sum equal that negative total, contradicting nonnegative triangle weights. Positive combinations of actual zero-surplus rows extend these certificates to all 72 original variables. The contradiction works for arbitrary nonnegative real weights, without an optimizer or integrality assumption. ([Potentials and full Farkas rows](<fractional_capacity.md>))

The second certificate also has a short signed Hall interpretation. Fifteen specified nodes, with two compensating nodes subtracted, require 13 units of coverage. Every surviving triangle contributes at most one such unit, while total triangle mass is \(36/3=12\). Thus coverage would require \(13\le12\). Earlier twelve-type covers satisfy every joint capacity inequality at all 50 and 308 preceding events. They establish exact firstness for the **necessary-capacity problem**, without asserting balanced flux, complete repairs or rational costs for those witnesses. ([Hall interpretation and firstness](<fractional_capacity.md>), [independent geometry replay](<fractional_capacity_audit.md>))

## Two actual events also obstruct nonperiodic weights

For the first basis, a local argument removes periodicity entirely. Assign arbitrary nonnegative spatial weights to the two shapes, with whole-plane marginal one, retain every wholly contained triangle, and repair the residual arbitrarily. All six triangles through \(z=(12,5)\) lie wholly in the quadrant. Two contain the color-two token \((7,8)\), arriving at 839808, but remain incomplete until 995328. The other four contain \(z\), arriving at 995328, and finish later. ([Six incidences and local-support lemma](<obstruction.md>))

Actual counts are \((46,46,46)\) on \([839808,884736)\), and \((48,47,47)\) on \([995328,1062882)\). On the first interval color two has zero surplus; on the second color one does. Retained incomplete mass in either minimum color forces at least that much completed-count deficit. The intervals are disjoint, and their two edge groups partition the six incident triangles whose weights sum to one. Integration gives

\[
M-Q\ge\min\left(\frac1{839808}-\frac1{884736},
\frac1{995328}-\frac1{1062882}\right)
=\frac{13}{214990848}>0.
\]

Consequently this retained-bulk class cannot agree with the optimum **through 995328 inclusively**, even with irrational, nonperiodic weights. Whole-plane coverage and retaining all contained triangles are essential: a method allowed to discard contained bulk triangles falls outside the theorem. The result concerns this fixed basis and these two shapes; it supplies neither an infinite-family denominator obstruction nor a theorem for every coupling. ([Integrated proof and audited endpoint](<fractional_capacity_audit.md>))

## Infinite actual feasibility remains the missing theorem

Every constructed candidate has \(Q<M\). The dispersion proof extends to fractional mass: at least one positive-weight bulk type contributes a quadratic family of genuinely dispersed ordinary triples, while actual color imbalance is sublinear in logarithmic time. Integrated partial-token mass then forces a positive cost deficit. Constants can depend on the candidate; no uniform positive dispersion across levels is assumed. ([Weighted strictness, FA9](<fractional_arithmetic.md>))

The remaining sufficient theorem is precise: for some fixed \(\varepsilon>0\), prove nonempty balanced actual-head polytopes at infinitely many actual Farey levels \(H\to\infty\), through \(2^{(2+\varepsilon)H}\). If a feasible head is larger, first restrict it to this fixed exponential target before applying the coefficient bound. Choose the rational vertices above. Head equality and monotonicity give \(\tau(t)-G(t)\le\tau(t)-\tau(X)\) for \(t\ge X\), so the smooth reciprocal tail bounds \(M-Q=O(\log X/X)\). Complete clearing and strictness then yield

\[
DQ\in\mathbb Z,
\qquad 0<D(M-Q)\le H^{O(1)}2^{-\varepsilon H}\longrightarrow0.
\]

Rationality \(M=a/b\) would make \(bD(M-Q)\) positive integers tending to zero, a contradiction. The growing-period version also suffices under its sublinear-overhead hypothesis. **The infinite feasibility premise has not been proved.** The older signed hierarchy separately retains its unresolved boundary arithmetic and signed nonvanishing obligations. ([Conditional finish, FA10](<fractional_arithmetic.md>), [precise tail audit](<fractional_arithmetic_audit.md>))

Validation comprises three supplied exact checkers and two independent checkers, all passing, alongside the written proofs. Independent arithmetic replay covers every actual event through \(2^{24}\) and \(2^{48}\), including later periods on both edges; independent capacity replay reconstructs all original Farkas columns and every preceding witness event. These finite checks support the general arguments without supplying infinite feasibility. Further progress must establish that actual feasibility in an unexcluded class, rather than re-clearing already adequate fractional denominators. ([Arithmetic audit](<fractional_arithmetic_audit.md>), [capacity audit](<fractional_capacity_audit.md>))

Skipped: new research or tests for this synthesis, Lean, external review and priority verification. Material risk: treating conditional cheap arithmetic or scoped obstructions as the still-unproved infinite return or an irrationality proof.
