# Farey transport lowers Erdős’s arithmetic cost

**The complete rational Farey coupling now has clearing exponent two, but an adequate infinite arithmetic return for Erdős #168(ii) remains unproved.** The construction combines a unimodular plane tiling, balanced periodic boundary strips, a finite corner repair, and exact sums of every infinite tail. It improves the earlier exponent-five construction without obtaining the longer accurate head needed to beat its denominator. Capacity arguments also expose losses that no boundary repair of a specified bulk can remove. All six translations and a richer integer torus class have exact finite obstructions for two named bases. A separate positive-tail approach gives strict rational comparisons and a genuine reduced-denominator obstruction on the eventual lower-convergent sequence. The fresh internal audit passes these results; the full goal remains **active and open**. ([Final audit](<final_farey_audit.md>))

## The finite theorem already supplies the exact target

Let \(F(N)\) be the largest size of a subset of \([1,N]\) containing no complete triple \(\{n,2n,3n\}\), and let \(c=\lim F(N)/N\). The remaining target here is the irrationality of \(c\). The accepted finite theorem is
\[
\tau(D_t)=\min_j\bigl(K_j(t)-I_j(t)-P_j(t)\bigr),\qquad
D_t=\{2^a3^b\le t:a,b\ge0\},\quad t\ge3.
\]
Here \(K_j\) counts the color \(a-b\bmod3\), while \(I_j,P_j\) remove the isolated-root and patch exceptions. Its ordinary proof covers every real cutoff, including fractional correction endpoints, and has two internal adversarial audits. **This finite-combinatorial obligation is finished within the written dependency chain**; the current round accepts rather than independently reproves it. ([Finite proof and verification scope](<../prefix-and-phase-audit/REPORT.md>))

The corrections have an exact positive representation. Keep every original exponent pair and its color, but delay dyadic arrivals by \(2^a\mapsto3\,2^{a-1}\) for \(a\ge1\), and row-one arrivals by \(3\,2^a\mapsto27\,2^{a-3}\) for \(a\ge2\). In particular, **the arrival \(12\mapsto27/2\) is retained**. If \(T_j(t)\) counts arrived color-\(j\) tokens, then \(\tau(t)=\min_jT_j(t)\). Their total reciprocal mass is \(143/54\). Equal-rank three-color matching has cost
\[
M=\sum_{k\ge1}\frac1{\max_jt_j(k)}=3(1-c),\qquad Z=3-3M=9c-6.
\]
Every bijective three-color coupling has cost \(Q\le M\). The existing dispersion theorem proves \(Q<M\) whenever a fixed dispersed bulk has positive density, regardless of the remaining valid edge repair. ([Token and rank identities](<../hybrid-arithmetic-closure/REPORT.md>), [strictness theorem](<../rational-coupling-construction/coupling_strictness.md>))

The arithmetic finish requires **one and the same infinite family** with \(D_nQ_n\in\mathbb Z\), \(Q_n<M\), and \(D_n(M-Q_n)\to0\). If \(M=A/B\) were rational, \(BD_n(M-Q_n)\) would be positive integers tending to zero. Separate constructions supplying strictness, small real errors, and cheap denominators cannot be combined without an identity joining them. ([Accepted arithmetic requirements](<../rational-coupling-construction/REPORT.md>))

## A complete Farey repair cuts the clearing exponent to two

Choose vectors \(u=(q,-p)\), \(v=(s,-r)\) with determinant magnitude one and opposite nonzero color increments. In basis coordinates, the two triangles
\[
\{0,u,v\},\qquad \{u+v,2u,2u+v\}
\]
tile a six-cell block repeated by \(3u,2v\). Unimodularity makes this an exhaustive partition of the original integer plane. Its period lattice has **index six** and contains \(6\mathbb Z^2\); each triple has spans \(H=\max(q,s)\), \(V=\max(p,r)\). A complete continued-fraction residue reduction produces such positive bases from every sufficiently late actual convergent, with \(H\le q_n,V\le p_n\). It covers zero colors and equal colors as well as complementary adjacent colors, so it assumes no unproved favorable-residue infinitude. Both logarithmic errors tend to zero and \(V\log3=H\log2+o(1)\). ([Tiling and complete basis reduction](<farey_bulk.md>))

Keep the triangles wholly inside the quadrant. Their complete cost consists of twelve residue-coset streams. Each separates into an actual first member, its horizontal geometric continuation, and an ordinary high-row double-geometric continuation. This handles the exceptional small roots and all low delays explicitly. The bulk clears by a fixed constant times \(2^H3^V\), but that statement alone leaves most of the target mass in the boundary strips. ([Complete bulk summation](<farey_bulk.md>))

The companion repair closes that obligation. Set \(A=6\lceil H/6\rceil\), \(B=6\lceil V/6\rceil\); split residual tokens into a finite corner and disjoint bottom and left strips. Moving a cut on a six-period cylinder changes all color counts equally. The color-cycling period \(2v\) then forces the crossing-residual color differences to vanish. Consequently **every far-edge six-period block is balanced**. This does not presume corner balance. Its color deficit is at most \(36(H+V+6)\), while the left strip has \(n=H+O(1)\) tokens of each color per period. All corner deficits therefore fit within \(J\le180\) donor periods eventually. ([Flux, capacity and corner proofs](<boundary_repairs.md>))

Take the required donors in period order and optimally match the balanced finite head by actual ranks. Match each bottom period by actual ranks; zip the remaining left color lists by residual enumeration index. The latter is deliberately a specified period enumeration, with every donor shift included. Its entire tail scales by \(3^6=729\); bottom tails scale by \(2^6=64\). This yields a complete bijection and the explicit clearing factor
\[
D=(63\cdot728\cdot2^6 3^6)\,2^A3^{B+6J},\qquad DQ\in\mathbb Z,
\]
\[
\boxed{\log D=H\log2+V\log3+O(1)=(2+o(1))H\log2.}
\]
All donors, finite heads, low delays and infinite strips are charged. This is a full clearing upper bound, not a theorem about the reduced denominator. ([Complete construction and arithmetic](<boundary_repairs.md>))

All tokens before \(X=2^{H+o(1)}\) lie in the optimally rematched head. The smooth reciprocal tail and dispersion strictness give
\[
0<M-Q=O(H2^{-H+o(1)}),\qquad Q\longrightarrow M.
\]
Thus the construction supplies infinitely many genuine strict rational comparisons. **Its guaranteed head has only one span**, while the clearing cost has two. The former skew/L construction had clearing exponent five and a roughly two-span head; lowering the denominator has not yet supplied an adequate accuracy-to-clearing ratio. ([Prefix and convergence proof](<boundary_repairs.md>), [previous construction](<../rational-coupling-construction/REPORT.md>))

## Capacity defeats every repair of the named bulks

Near equality of a triple’s arrivals does not guarantee a long optimal head. Let \(G_B(t)\) count completed kept bulk triples and \(R_j(t)\) count arrived residual tokens. Every possible boundary repair satisfies
\[
G(t)\le G_B(t)+\min_jR_j(t),\qquad
\tau(t)-G(t)\ge F_B(t):=\tau(t)-G_B(t)-\min_jR_j(t)\ge0.
\]
A positive \(F_B\) reserves more of a color in incomplete bulk triples than the actual surplus permits. If \(F_B=g\) on \([t,t')\), every repair has gap at least \(g(1/t-1/t')\). For the unshifted basis \((8,-5),(3,-2)\), the unit deficit on \([243,288)\) forces gap \(5/7776\). **No donor ordering or ideal residual rematching removes this loss while keeping that bulk.** ([Fixed-bulk theorem and exact intervals](<boundary_repairs.md>))

There are exactly six integer translation phases, with bounded original-coordinate representatives and unchanged asymptotic clearing cost. Exact all-event enumeration tests every phase for the two named bases. Their latest first unavoidable deficits occur at **4608** for spans \((8,5)\) and **805306368** for spans \((27,17)\), both before \(2^{2H}\). The best-capacity first example has complete cost \(13501693/22643712\), but its explicit repair loses earlier, at 1458. Its unavoidable later gap \(1/41472\) gives reduced-denominator times gap at least **546**. The corresponding exact product for the second best-capacity example also exceeds one. These are actual finite counterexamples to the proposed window, not merely weak upper estimates. ([Six-phase classification and exact products](<translation_phases.md>))

A broader finite class allows all 36 anchor residues modulo six and both orientations \(z+\{0,u,v\}\), \(z+\{0,-u,-v\}\): **72 integer triangle types**. Twelve disjoint masks must cover the 36 residue nodes. For each selected type \(k\), let \(P_{k,j}(t)\) count its arrived color-\(j\) vertices in incomplete retained triples. Necessary joint conditions are
\[
\sum_{k\ \mathrm{selected}}P_{k,j}(t)\le T_j(t)-\tau(t)
\]
at every head event. Nonnegative profiles permit individual bans; exhaustive exact-cover replay proves infeasibility at the following first thresholds. ([Torus model and proof](<torus_bulk.md>))

| Basis | First capacity-infeasible cutoff | Previous actual event | Exhaustive search states |
|---|---:|---:|---:|
| \((8,-5),(3,-2)\) | 6561 | 6144 | 20 |
| \((19,-12),(27,-17)\) | 3057647616 | 2902376448 | 4 |

The preceding twelve-type witnesses satisfy **all joint inequalities at every earlier event**, which establishes firstness for this finite necessary-capacity problem. Those feasible profiles have no proved balanced edge flux, corner charge or cheap global repair. Conversely, the negative certificates need none of those additional constraints. They exclude the prescribed integer period-six class for these bases, while leaving fractional couplings, larger periods, different shapes and other convergent levels untested. ([Witnesses, replay and scope](<torus_bulk.md>), [independent audit](<final_farey_audit.md>))

## Positive tail corrections expose a real denominator barrier

Put \(e(t)=\sum_jT_j(t)-3\tau(t)\ge0\). The complete positive representation gives
\[
Z=\frac{19}{54}+\int_1^\infty e(t)t^{-2}\,dt,
\qquad L_X=\frac{19}{54}+\int_1^X e(t)t^{-2}\,dt,
\quad Z-L_X=R(X).
\]
For rational \(X\), \(L_X\) is rational. Adding the complete partial-token tail correction to an optimal-head rational coupling produces exactly this same \(L_X\): the coupling dependence cancels. This scalar identity does not imply rationality of separate translated profiles. ([Exact identities and endpoint treatment](<imbalance_tails.md>))

A corrected doubling recurrence proves the uniform actual lower bound
\[
R(X)\ge\frac{2}{81X}\quad(X\ge7),
\]
already within \([X,54X]\). At \(X=2^{3q_n}\), a uniform continued-fraction grid argument also gives \(R(X)\le200/X\). More decisively, **every sufficiently late lower actual convergent** \(p/q\) satisfies
\[
v_3(L_{2^{3q}})=-3p.
\]
The unique top ternary row contributes a 3-adic unit; all other reciprocal terms have smaller ternary denominator exponent. If \(b_X\) is the reduced denominator, then \(b_X\ge3^{3p}\) and
\[
\liminf_{\text{lower convergents}}b_X(Z-L_X)\ge2/81.
\]
This specific truncation family cannot give shrinking integer-cleared errors, even after every cancellation. **The valuation theorem is eventual and lower-convergent only.** ([Tail bounds and exact valuation proof](<imbalance_tails.md>))

An explicit rational doubling counterterm also survives scrutiny. With \(r(t)=(\lfloor\log_3(2t)\rfloor+1)\bmod3\), the defect \(h(t)=[r(t)-e(2t)+e(t)]/3\) is binary for \(t\ge7\). Its forcing tail \(F_r(X)\) is rational, giving
\[
U_X=2L_{2X}-L_X+F_r(X),\qquad
U_X-Z=3\int_X^\infty h(t)t^{-2}\,dt.
\]
Uniform doubling-orbit mean \(h\to1/3\) proves this error is strictly positive and **of exact order \(1/X\)**. The available dyadic-cutoff clearing remains \(O(X^2)\). No reduced-denominator obstruction for \(U_X\), effective optimized frequency constant or finite-state closure is claimed. ([Counterterm and uniform mean proof](<imbalance_tails.md>))

## The remaining theorem must join accuracy and arithmetic

The older signed hierarchy remains a distinct viable route:
\[
81\Pi_mZ=B_m+\mathcal R_m,\qquad
\log\Pi_m\le(5/2+o(1))q_m\log2,
\]
\[
|\mathcal R_m|\le\exp[-(\sqrt5/10+o(1))q_m\log2].
\]
Its adequate real decay is proved on an actual infinite sequence. The complete \(B_m\), including four low rows and infinite boundary sides, still lacks sufficiently cheap rational denominator control; signed residual nonvanishing is also open. Subexponential extra clearing would suffice. Positive coupling strictness supplies neither obligation for this different residual. ([Hierarchy and precise missing arithmetic](<../hybrid-arithmetic-closure/REPORT.md>))

| Route | Finished | Missing or excluded |
|---|---|---|
| Signed hierarchy | Actual infinite supply, cumulative cost and adequate real decay | Cheap complete boundary arithmetic; infinitely many nonzero signed residuals |
| Earlier skew/L couplings | Complete rationality and strict nonvanishing | Two-span head does not beat exponent-five clearing |
| New Farey couplings | Complete exponent-two clearing, all boundary repairs, strictness and convergence | Longer accurate head or another proved adequate error-to-clearing estimate |
| Scalar truncation | Exact positivity and tail order; actual reduced valuation on eventual lower convergents | That lower-convergent sequence is inadequate; other counterterms remain separate |

The next constructive advance must control actual incomplete-triple capacity while preserving full rational arithmetic, or close the older hierarchy’s boundary and sign gaps. Finite capacity feasibility alone is insufficient. The final fresh audit reconstructed the proofs and passed **five supplied checkers plus an independent sixth checker**, including full joint torus witnesses and every charged repair tail. These are internal written proofs and exact finite certificates; they establish neither an adequate infinite return nor irrationality. ([Final audit and remaining obligations](<final_farey_audit.md>))

Skipped: new research or tests for this synthesis, Lean, external review and priority verification. Material risk: mistaking improved clearing, finite capacity classifications or strict comparisons for the still-missing adequate infinite arithmetic return.
