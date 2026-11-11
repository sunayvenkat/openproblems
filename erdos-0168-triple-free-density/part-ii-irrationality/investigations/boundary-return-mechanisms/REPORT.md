# Rational returns expose Erdős’s arithmetic cost

**A complete rational coupling is now proved optimal through \(2^{q+q_{\mathrm{next}}-1}\) at every relevant nonresonant convergent \(p/q\), but the adequate infinite arithmetic return remains unproved.** Its genuine maximum-arrival cost includes explicit corrections absent from the cheaper scalar model. Two complete examples have reduced denominators of 137 and 439 bits, and exact positive-gap bounds show that their long heads do not beat those denominators. An exact continued-fraction state recursion also gives a transcendental countermodel to a proposed generic supply argument. Separately, a periodic exchange compresses both coordinate spans while preserving cost, with all boundary clipping retained. Three fresh audits pass; the full goal remains **active and open**. ([Rational-order audit](<rational_order_audit.md>), [state audit](<cf_state_audit.md>), [exchange audit](<boundary_audit.md>))

## Token order gives a genuine long head

Let \(c\) be the limiting maximum density of sets avoiding every triple \(\{n,2n,3n\}\). The established finite theorem supplies positive tokens \((a,b)\), colored by \(a-b\bmod3\), with arrived counts \(T_j(t)\) and optimum completed count \(\tau(t)=\min_jT_j(t)\). The optimal reciprocal completion cost is \(M=3(1-c)\). Thus irrationality of \(M\) proves the target. Ordinary arrivals are \(2^a3^b\). Effective exponents are \((a-1,1)\) when \(b=0,a\ge1\), and \((a-3,3)\) when \(b=1,a\ge2\); all other tokens keep \((A,B)=(a,b)\). Original colors remain unchanged, including the token arriving at \(27/2\). These are accepted proved dependencies, rather than new claims of this round. ([Finite and token foundation](<../adaptive-shape-couplings/REPORT.md>))

For coprime \(3/5<p/q<2/3\) with \(p+q\not\equiv0\pmod3\), put \(\sigma=\operatorname{sign}(q\log2-p\log3)\). Order tokens by
\[
(pA+qB,\ \sigma A),
\]
where \((A,B)\) are their effective exponents, and couple equal ranks of the three colors. Every grade sublevel is finite and each color list is infinite, so this defines a **complete genuine coupling**. Its cost \(Q_{p,q}\) uses the maximum of the three actual arrivals, regardless of their model order. ([Definition and completeness, RO1](<rational_order.md>))

Let \(P/q_{\mathrm{next}}\) be the immediate successor of an actual convergent \(p/q\), and set \(N=q+q_{\mathrm{next}}-1\). Farey-neighbor exclusion prevents any ordering reversal between effective exponents \(0\le A\le N\): a reversal would exhibit an intervening rational with denominator below \(q+q_{\mathrm{next}}\). Predecessor closure matters too. Every actual token arriving by \(2^N\) has integer grade at most \(pN+1\); since \(p\ge2\) and \(B\ge0\), every model predecessor also has \(A\le N\). The sole negative effective exponent, at \(27/2\), is handled separately using \(3/5<p/q\). Thus the whole prefix agrees, including simultaneous arrivals and tokens outside an initially selected board. ([Full prefix proof and independent reconstruction](<rational_order_audit.md>))

Consequently \(G(t)=\tau(t)\) through \(X=2^N\), and the smooth-token tail gives \(M-Q_{p,q}=O(\log X/X)\). A quadratic-density family of dispersed ordinary triples proves \(Q_{p,q}<M\) for each candidate. No positive dispersion uniform in \(q\) is assumed. This is a new full-token coupling theorem; the old scalar coefficient model already had a raw \(q+q_{\mathrm{next}}\)-scale window. The smaller \(q_{\mathrm{next}}-q\) window followed an annihilator and must not be confused with either statement. ([Strictness and window scope, RO2–RO3 and RO8](<rational_order.md>))

## Actual maxima carry the crossover denominator

The full cost is rational, with a proved infinite decomposition. Nonresonance makes rational-grade and cumulative color discrepancies eventually periodic with period \(L=3pq\). Grade translation adds one arrival of each color, while cumulative ranks have a common quadratic part. Beyond an explicit threshold, cross-grade triples use only adjacent grades. Their leading and trailing endpoints have identical rank polynomials under every later period, giving finitely many affine templates. This establishes all future triples; checking additional periods is supplementary evidence. ([All-period proof, RO4–RO5](<rational_order.md>))

Within a grade, model order equals physical order. Only cross-grade triples change the scalar model-birth value \(M^\sigma_{p,q}\):
\[
Q_{p,q}=M^\sigma_{p,q}-C_{\rm fin}-\sum_\nu C_\nu,
\qquad C_{\rm fin},C_\nu\ge0.
\]
Here \(C_{\rm fin}\) evaluates every cross-grade correction before the proved template threshold. Subsequent endpoint streams grow with \(U=2^{3q}\) and \(V=3^{3p}\). If one template's slower and faster streams have roots \(c_s,c_f\), bases \(R_s<R_f\), and first crossover \(k\), its complete infinite-tail correction is
\[
C_\nu=
\frac{1}{c_sR_s^k(1-R_s^{-1})}
-\frac{1}{c_fR_f^k(1-R_f^{-1})}.
\]
Within that template the pre-crossover correction is zero; the separate finite head \(C_{\rm fin}\) is not omitted. Every starting power is retained. The independent audit also summed the same-grade bulk directly through its two geometric poles, without importing the scalar value. ([Complete actual-cost proof and independent sum](<rational_order_audit.md>))

The scalar value clears by \(27(U-1)(V-1)\). The actual cost instead has a safe factor
\[
(U-1)(V-1)2^{A_*}3^{B_*},
\]
where \(A_*,B_*\) include every finite-head and crossover exponent. **No useful uniform small-height bound is proved for these extra powers.** Assigning the scalar denominator to \(Q_{p,q}\) would discard part of its actual maximum cost. ([Charged arithmetic, RO6–RO7](<rational_order.md>))

| Model | Proved optimal head | First unit-deficit interval | Reduced denominator |
|---|---|---|---:|
| \(5/8\) | \(2^{26}\) | \([2^{27}3^7,\ 2^8 3^{19})\) | 137 bits |
| \(12/19\) | \(2^{83}\) | \([2^{103}3^2,\ 2^{19}3^{55})\) | 439 bits |

The exact reduced denominators are \(2^{54}3^{27}\cdot1028780687935\) and \(2^{137}3^{121}\cdot1351932287187751456719735745864595\). For a deficit of one on \([t,t')\), the error is at least \(1/t-1/t'\). Multiplying by the actual reduced denominator gives more than \(6\times10^{27}\) in the first example and an explicit positive integer greater than one in the second. These are cancellation-aware failures of the two named comparisons, not merely weak safe bounds. **They do not prove an all-level valuation obstruction or exclude an exceptional infinite subsequence.** ([Exact fractions, firstness and reduced-denominator bounds](<rational_order_audit.md>))

## Exact states defeat a generic supply shortcut

The state before the critical arrivals
\[
\{(0,2p+2),(q,p+2),(2q,2)\}
\]
now has an all-convergent formula. For every sufficiently late actual convergent, best approximation identifies the earlier ordinary high-row tokens exactly with
\[
pa+q(b-2)<2pq,\qquad a\ge0,\ b\ge2.
\]
The corrected low rows end at \(a=2q+2\) and \(a=2q+1\). No other token arrives inside the critical interval. Hence the total pre-count is
\[
N=2pq+p+5q+4.
\]
This needs no assumption \(q_{\mathrm{next}}>2q\). Total divisibility by three is only a necessary balance test. ([Actual comparison and low-row proof, CR1–CR2](<cf_return_state.md>))

Splitting the rational triangle into residues modulo three gives nine Euclidean floor sums. A second exact formula uses the Christoffel-word transform
\[
H(p,q)=\sum_{a=0}^{q-1}\omega^{a+\lfloor pa/q\rfloor},
\qquad \omega^2+\omega+1=0.
\]
Word concatenation supplies a parity-sensitive continued-fraction recurrence, including resonant steps. Together with \((p,q)\bmod3\), it recovers all three counts and the complete nonresonant balance table. Both methods use \(O(\log q)\) Euclidean steps; that is not a unit-cost bit-complexity claim. They explain the unequal actual pre-state \((99852,99851,99852)\) at \(306/485\). ([Corrected recurrence, balance table and independent audit](<cf_state_audit.md>))

A stronger generic supply argument is false. After the actual prefix through \(12/19\), both digit blocks
\[
A=(3,3),\qquad B=(1,3,2,3)
\]
return the **full** state: parity, both preceding/current residues and both transforms. Every intermediate state is balanced and nonresonant. Arbitrary concatenations therefore preserve those states, while all outgoing denominator ratios remain below four. Choosing \(B\) at factorial block positions and \(A\) elsewhere gives a provably transcendental abstract slope. Let \(m_j\) count digits through the exceptional block at position \(j!\). Its quadratic all-threes-tail approximants have heights \(O(16^{m_j})\), errors \(O(2^{-m_{j+1}})\), and \(m_{j+1}/m_j\to\infty\); a nonzero integer resultant contradicts algebraicity of every fixed degree. Nonperiodicity alone is not being used as a transcendence proof. ([Full-state loops and resultant argument, CR5–CR6](<cf_return_state.md>))

Thus transcendence alone cannot force either infinitely many escape states or infinitely many ratios exceeding five. This is an **abstract state-map countermodel**, not the actual logarithmic slope and not a claim about fixed \(2,3\) token counts at another slope. It need not share every quantitative arithmetic property of \(\log_3 2\). A logarithm-specific supply theorem, or a construction handling the balanced states too, remains necessary. ([Countermodel scope and audit](<cf_state_audit.md>))

## Periodic compression retains its boundary bill

The whole earlier three-triple exchange repeats under \((6n,6m)\), \(n,m\ge0\). Its old and new families use the same nine residue-distinct points and have the same ordinary maxima \(27648,36864,41472\), which already dominate the exceptional low-row arrivals. Horizontal translates preserve retimings; positive vertical translates are ordinary and retain those maxima. Thus every translated block preserves token marginals, the full completed-count function and cost. Loss of one individual tie does not invalidate the complete exchange. ([Infinite substitution and exact cone proof](<boundary_audit.md>))

A bounded unimodular transformation puts any eligible positive Farey basis into the exchange’s physical-error cone. Separate coordinate-projection inequalities prove a reverse compression factor at most **\(6/7\) on both axes**. The mapped seed is translated above the delayed rows, so this does not transport exceptional timing rules through an arbitrary lattice map. It is a parameterized local mechanism, with no supplied long-head parent family. ([Matrices, color preservation and both cone intervals, BE2–BE3](<boundary_exchange.md>))

The other 27 residue nodes can be completed and horizontally averaged with weights \((1,2,3,2,1)/9\). **Initially balanced zeroth masses are essential:** two color averages then balance every first and second root moment. Exact floor-coordinate subtraction proves balanced periodic edge flux and only linear corner imbalance. Positive edge capacity gives uniformly bounded donor periods in the parameterized regime. Every split stays in ninths, and all donor shifts and geometric tails remain charged. ([Moment hypothesis, exact clipping and donor proof](<boundary_audit.md>))

The complete parent and child embeddings have the same
\[
Q=\frac{357544920809}{704310018048},\qquad
D=125176966099650799095250944,\quad DQ\in\mathbb Z,
\]
with cuts \(A=24,B=12\) and one donor period. They already lose optimality at \(t=3\), where \(\tau=1\) and \(G=7/9\). Moreover, residual mass \(1/9\) remains at \((8,6)\), outside the smaller child \(8\times5\) span strips. The construction keeps indices of the **old whole block**, not every individually contained normalized child triple. Its original clipping positions cannot be replaced by the smaller drawing. A true zero-cost substitution changes neither \(Q\) nor its reduced denominator. ([Complete cost and explicit clipping certificate](<boundary_audit.md>))

## The finish still needs one joined estimate

The required actual infinite family must satisfy
\[
D_nQ_n\in\mathbb Z,\qquad Q_n<M,\qquad
D_n(M-Q_n)\longrightarrow0.
\]
If \(M=a/b\) were rational, these conditions would produce positive integers \(bD_n(M-Q_n)\) tending to zero. The rational-order family now supplies rationality, strictness and a proved long head together. Its complete height remains uncontrolled at the needed scale. Geometric compression cannot erase that height, and generic transcendence cannot supply the missing favorable states. The older signed hierarchy separately retains its boundary-arithmetic and signed-nonvanishing obligations. ([Remaining arithmetic target](<rational_order.md>))

Three supplied exact checkers and three independent checkers pass alongside the written proofs. The audits separately reconstruct actual token prefixes, full infinite costs, residue clipping, state formulas and countermodel loops. Two displayed CF formulas were corrected; no substantive gap was reported. Further progress must link a repeatable actual mechanism to an affordable **actual-maximum** cost, rather than combine the cheapest arithmetic and longest head from different constructions. The irrationality proof and active goal remain unfinished. ([Rational-order audit](<rational_order_audit.md>), [state audit](<cf_state_audit.md>), [exchange audit](<boundary_audit.md>))

Skipped: new research or tests for this synthesis, Lean, external review and priority verification. Material risk: conflating long agreement, abstract state supply or geometric compression with the still-unproved affordable infinite arithmetic return.
