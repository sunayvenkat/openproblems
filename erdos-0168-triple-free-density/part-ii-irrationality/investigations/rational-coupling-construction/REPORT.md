# Coupling strictness separates Erdős’s remaining obligations

**Nonvanishing is now proved for new genuine rational coupling comparisons, but the adequate infinite arithmetic return remains unproved and the goal stays active.** Two explicit coupling families give rational values converging to the actual target from one side, with strictly nonzero errors. Their complete constructions retain every delayed boundary token and evaluate every infinite tail. The available approximation rates and denominator bounds do not yet give small integer-cleared errors. Exact phase calculations show how removing a period can replace it with an expensive smooth denominator. Signed-operator arguments identify separate cost and window barriers for defined formal constructions. The fresh audit passes these results and all six exact certificates; it does not establish irrationality or nonvanishing of the earlier signed hierarchy residual. ([Final audit](<final_coupling_audit.md>))

## Dispersion proves actual nonvanishing for coupling comparisons

The target remains Erdős #168(ii), irrationality of \(c=\lim F(N)/N\), where \(F(N)\) is the largest size of a subset of \([1,N]\) avoiding every \(\{n,2n,3n\}\). The accepted finite input is the complete ordinary proof
\[
\tau(D_t)=\min_j(K_j(t)-I_j(t)-P_j(t)),\qquad
D_t=\{2^a3^b\le t\},\quad t\ge3.
\]
Colors are \(a-b\bmod3\); \(I_j,P_j\) are the isolated-root and patch corrections. This report builds on that internally audited proof without independently redoing it. ([Finite proof and audits](<../prefix-and-phase-audit/REPORT.md>))

Keep one token of its original color at each \((a,b)\), and delay the arrivals \(2^a\to3\,2^{a-1}\) for \(a\ge1\), and \(3\,2^a\to27\,2^{a-3}\) for \(a\ge2\). The arrived-token counts are exactly \(T_j(t)=K_j-I_j-P_j\). The sole nonsmooth arrival \(12\to27/2\) has zero minimum increment. If \(\eta_{a,b}\) is the finite optimum’s increment and \(t_j(k)\) is the \(k\)-th color-\(j\) arrival, then
\[
M=\sum_{a,b}\frac{\eta_{a,b}}{2^a3^b}
=\sum_{k\ge1}\frac1{\max_j t_j(k)},\qquad
Z=3-3M=9c-6.
\]
A valid coupling partitions all tokens bijectively into triples containing one of each color. Its actual reciprocal-maximum cost \(Q(\mathcal C)\) is at most \(M\), by the layer-cake count bound. ([Token and matching inputs](<../hybrid-arithmetic-closure/global_carries.md>), [matching proof](<../hybrid-arithmetic-closure/hierarchy_absorption.md>))

The new theorem supplies **strictness**. Write \(T=\log t\), let \(N(T)\) count all arrived tokens, and put
\[
E(T)=N(T)-3\tau(e^T).
\]
Uniform irrational-rotation averaging, including moving starting phases, proves \(E(T)=o(T)\). The proof groups the root-of-unity row discrepancy into three rotation sums of a mean-zero step function; bounded retiming corrections preserve the estimate. No effective rate uniform in a coupling parameter is assumed. ([Actual discrepancy proof, CS1–CS3](<coupling_strictness.md>))

For a coupling let \(G(T)\) count completed triples and \(U(T)=N(T)-3G(T)\) count tokens in incomplete triples. Its deficit is
\[
D(T)=\tau(e^T)-G(T)=\frac{U(T)-E(T)}3\ge0.
\]
For a triple with logarithmic arrivals \(h_j\), define its dispersion \(g=\sum_j(\max h-h_j)\). Its integrated contribution to \(U\), once complete, equals \(g\). Therefore, if a subfamily has at least \(\kappa T^2\) completed triples by \(e^T\), each with \(g\ge\varepsilon>0\), then
\[
\int_0^T D(s)\,ds\ge
\left(\frac{\varepsilon\kappa}{3}+o(1)\right)T^2.
\]
Consequently
\[
M-Q(\mathcal C)=\int_0^\infty D(T)e^{-T}\,dT>0.
\]
Simultaneous arrivals and arbitrary remaining edge repairs are included in the conservation identity. ([Dispersion theorem, CS4–CS10](<coupling_strictness.md>))

A fixed-offset family on a full-index lattice inside an interior cone satisfies the criterion. So does a positive-density bounded-displacement bulk: multiplicative independence of 2 and 3 gives a positive minimum dispersion among its finitely many offset types. Constants may depend on the coupling. Thus every rational member in this class gives
\[
\widehat Z=3-3Q(\mathcal C)>Z.
\]
This establishes actual one-sided nonvanishing for the new families below. **It does not transfer to the old signed residual \(\mathcal R_m\)** without an additional coupling identity. ([Class hypotheses and scope](<coupling_strictness.md>))

## Two complete rational families expose the rate gap

The canonical coupling groups \((3n,b),(3n+1,b),(3n+2,b)\). Its actual maxima are \(6\,8^n\), \((27/2)8^n\), and \(4\,8^n3^b\) in rows zero, one, and \(b\ge2\). Summing every group gives **\(Q_{\rm row}=61/189\)**. Choose the first \(K\) actual tokens of each color, uncouple every canonical triple touching them, and optimally rematch that finite balanced union. All other triples remain. The resulting rational costs increase monotonically to \(M\), and unchanged dispersed bulk makes every error strictly positive. ([Construction RT1–RT2](<rational_templates.md>))

For a physical head cutoff \(X\), choose \(K=\tau(X)\). The repaired coupling attains the true completed count at every \(t\le X\), and every touched token arrives by \(6X\). With \(A=\lfloor\log_2X\rfloor\), \(B=\lfloor\log_3X\rfloor\), its cost clears by
\[
D_X=7\,2^{A+2}3^{\max(B,3)},\qquad D_XQ_X\in\mathbb Z,
\quad D_X\le28X^2\quad(X\ge27).
\]
The unchanged canonical tail has deficit \(\log t/(3\log3)+o(\log t)\). Integration proves the sharp real order
\[
M-Q_X=\Theta(\log X/X).
\]
These facts do not prove shrinking cleared errors or a lower bound on the reduced denominator. ([RT3–RT4](<rational_templates.md>), [sharp tail CS15–CS19](<coupling_strictness.md>))

The second family uses \(p\ge2,q\ge3\), \(p+q\not\equiv0\bmod3\), and \(u=2^q,v=3^p\). Its bulk triples are
\[
(r+3qn,b+2p),\quad(r+q+3qn,b+p),\quad(r+2q+3qn,b),
\]
for \(0\le r<q\), \(n,b\ge0\). In every horizontal block, the remaining tokens form the finite L-shape
\[
\{a<q,\ b<2p\}\ \cup\ \{q\le a<2q,\ b<p\}.
\]
It has exactly \(pq\) tokens of each color, as its root-of-unity character vanishes. Optimal finite matching of those blocks completes an exhaustive global bijection: no infinite root strip remains. ([Partition and balance RT5–RT6](<rational_templates.md>))

All later blocks use a scaled asymptotic arrival map. Its first-block optimal cost differs from the actual one by **exactly \(1/27\)**: only the first two ranks are affected, with first maximum \(3\) versus \(27/8\), and second maximum \(9\) unchanged. Summing the blocks and actual bulk maxima gives
\[
D_{p,q}=27\,v^2(u^3-1),\qquad D_{p,q}Q_{p,q}\in\mathbb Z.
\]
This includes both low-row delay factors and the entire infinite bulk. Along actual convergents, \(\log D_{p,q}=(5+o(1))q\log2\). The bulk contains a dispersed lattice family, so \(Q_{p,q}<M\) for every template. ([Exact correction and resummation RT7–RT10](<rational_templates.md>))

The coupling is certainly optimal before
\[
T_{\rm out}=\min(v^2,uv,\tfrac32u^2)=2^{(2+o(1))q}.
\]
The available upper error is of order \(q\,2^{-(2+o(1))q}\), which does not suffice with degree-five clearance. Exact all-event checks place the first deficit at \(59049=3^{10}\) for \(5/8\), with \((\tau,G)=(31,30)\), and at \(293534171136=2^{27}3^7\) for \(12/19\), with \((163,162)\). These refute transferring the old Farey window to this coupling. They are not an all-level early-defect theorem or an asymptotic denominator obstruction. ([RT11 and complete certificates](<rational_templates.md>))

## Removing a period retains exponential arithmetic cost

Translate the asymptotic skew coupling right by \(q\) or \(2q\), completing the left strip with vertical triples. Their full vertical cost is \(V=3/13\). Writing \(Q_0=Q_\infty+1/27\), the two complete phase costs are
\[
Q_r=V+(Q_\infty-V)u^{-r},\qquad r=1,2.
\]
Their equal mean cancels \(u^2+u+1\), but has fixed cost gap at least \(4/27\), already from the interval \([3,9)\). It cannot converge to \(M\). Its complete nominal clearance remains degree five. ([Phase construction and fixed deficit CP1–CP5](<coupling_phases.md>))

A deterministic fold keeps only the first \(3q\) skew columns and fills the rest with vertical triples. It removes the variable cubic period and satisfies
\[
Q_{\rm fold}-Q_0=u^{-3}(V-Q_\infty)<0,\qquad
351u^3v^2Q_{\rm fold}\in\mathbb Z.
\]
Its additional error is \(O(u^{-3})\); it preserves the earlier upper error bound and worsens the approximation. Both named first deficits remain unchanged. A cheap convex identity realizes the same value, but the independent deterministic construction supplies its actual arithmetic. ([Fold and mixture CP6–CP10](<coupling_phases.md>))

The smooth price is exact. Eventually along actual convergents, \(q\ge4\) and \(v^2\le(9/8)u^2\). The mean’s reduced dyadic denominator is \(2^{2q-3}\) for \(u>v\), or \(2^{2q}\) for \(u<v\); the fold’s is respectively \(2^{3q-3}\) or \(2^{3q}\). Thus these constructions replace the removed odd period with growing powers of two. These are scoped reduced dyadic statements, not full denominator theorems for every coupling. ([CP11–CP15 and valuation audit](<final_coupling_audit.md>))

## Signed elimination must pay its boundary and window costs

For the high array \(d(a,b)=1-3\eta_{a,b+4}\), write \(W(d)=\sum d(a,b)2^{-a}3^{-b}\). An ordinary integer shift polynomial \(P\) has a universally finite weighted boundary precisely when
\[
P(X,3)=P(2,Y)=\lambda=P(2,3),
\]
equivalently \(P=\lambda+(X-2)(Y-3)Q\). Its boundary is the integer \(-6(Qd)(0,0)\). A signed polynomial multiple of one annihilator \(L_{p,q}=X^{2q}+X^qY^p+Y^{2p}\) cannot satisfy this with \(\lambda\ne0\), because its nonconstant restriction would divide a constant. Formal cancellation remains distinct from a special rational value on the actual array. ([Classification SB1–SB3](<signed_boundaries.md>))

For adjacent slopes \(p/q<r/s\), \(qr-ps=1\), \(q,r\ge3\), every integer combination of their annihilators with finite boundary obeys
\[
2^{2\max(q,s)}3^{2\max(p,r)}\mid\lambda.
\]
Prime valuations at algebraic roots prove the bound, retaining both integral ceilings. Common rational coefficient denominators must be charged before applying it. For actual adjacent convergents this costs at least \((4+o(1))\max(q,s)\log2\), beyond the currently guaranteed matching budget. This concerns the specified universal two-generator construction, not every actual-specific relation. ([SB4–SB5](<signed_boundaries.md>))

Laurent relations do contain a fixed finite-boundary operator of evaluation \(182\). Balanced representations have linear support for the bounded actual slopes, but negative shifts cannot be discarded. Translating them back to the quadrant restores infinite sides. Its full actual residual is rigorously nonzero. A more elaborate ordinary finite-boundary repair has a 162-bit multiplier and a full residual with magnitude exceeding \(699752\,2^{64}\). Algebraic boundary cancellation has therefore been tested against actual infinite-tail bounds. ([Laurent certificates SB6–SB8](<signed_boundaries.md>), [ordinary repair WC5–WC7](<window_certificates.md>))

There is also an arbitrary-depth window barrier. Put \(w_i=q_i^+-q_i\), using each original immediate successor, and \(g_i(X)=A_i(X,3)\). If \(P=\sum_iA_iL_i\) has constant restriction and all \(\deg g_i<2w_i\), then every \(g_i\) and the constant vanish. The newest active term has degree at least \(2q_k\), while every older term has smaller degree. Any nonzero certificate forces an older degree at least \(\deg g_k+2(q_k-q_j)\), outside its known origin window. This invalidates the automatic rectangle estimate for that term; it does not rule out a new actual signed estimate beyond the windows. ([WC1–WC4 and audit](<final_coupling_audit.md>))

## One family must meet both analytic and arithmetic requirements

The accepted earlier hierarchy still gives \(81\Pi_mZ=B_m+\mathcal R_m\), with factor cost at most \(5q/2+o(q)\) and actual real residual decaying with margin \(\sqrt5/10\). Its complete boundary includes four low rows; cheap rational denominator control and residual nonvanishing remain unproved. The new coupling strictness does not identify that residual with a positive matching gap. ([Earlier hierarchy and exact open conditions](<../hybrid-arithmetic-closure/REPORT.md>))

| Construction | Arithmetic and nonvanishing | Remaining accuracy requirement |
|---|---|---|
| Earlier actual hierarchy | Boundary arithmetic and signed nonvanishing unproved | Adequate real decay already proved |
| Canonical finite-head coupling repairs | Rational and strictly one-sided | Error \(\Theta(\log X/X)\); available clearance \(O(X^2)\) |
| Skew/L couplings and fold | Rational and strictly one-sided; all tails evaluated | Proved \(2q\)-scale window and degree-five clearance do not suffice |

These are limitations of the available bounds. No general reduced-denominator lower bound or impossibility theorem for a specially selected subsequence is claimed. ([Precise arithmetic scopes](<final_coupling_audit.md>))

The fresh audit reconstructed the proofs and passed five supplied checkers plus an independent sixth checker. Its independent checks recover token ownership, full costs, first deficits, phase valuations and signed residual enclosures. Finite experiments supplement the written infinite proofs. The missing result is an adequate accuracy-to-clearing estimate for one genuine comparison family, or cheap arithmetic and nonvanishing for the earlier hierarchy’s same residual. The established strictness theorem can support a better coupling construction; it does not supply that construction. ([Final audit and verification scope](<final_coupling_audit.md>))

Skipped: Lean, external review and priority verification; this synthesis adds no experiments. The material risk is treating new-family nonvanishing or removal of a period factor as the missing adequate arithmetic return.
