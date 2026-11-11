# Boundary calibration, directional defect charges, and an exact cut obstruction

Research round, 7 November 2026. **The global finite optimum (C) remains unproved.** This route establishes quantitative defect charges, derives two valid integer cuts, and tests their precise proposed uniform consequence. The cuts repair the known 33-point LP obstruction, but a rational certificate on one previously saved 534-point cap disproves the uniform ceiling bound for this cut family. An exact six-shell boundary transfer is also derived below. No broader numerical sweep or Lean work was performed; earlier folders were not edited.

## Can overcoverage quantitatively pay for changes of phase?

### Takeaway

Yes, in a precise directional sense. For each fixed color, either type of change between \(v\) and \(6v\) can be charged to overcovered corners with no repeated charge on that side of the inequality. This is stronger than the earlier zero-defect rigidity, but does not yet compare an arbitrary boundary word with a single global phase.

### Cited Findings

* The scalar energy identity and exact-cover rigidity were already proved in [168_cover_review.md](<../../early-attacks/open-conjecture-transfer-search/168_cover_review.md>); they are not new conclusions of this round.
* The patched candidate is a proved construction upper bound, while the new axis-avoiding classification gives a fixed-vertical-phase lower bound. [Candidate definition](<../../early-attacks/open-conjecture-transfer-search/168_grid.md>), [classification](<../../early-attacks/augmentation-and-return-attacks/multiroot.md>), [independent audit](<independent_audit.md>).

### Inferences

Let \(F\subseteq D_t\) meet every corner, \(f(v)=1_F(v)\), and

\[
e(r)=f(r)+f(2r)+f(3r)-1\ge0\qquad(3r\le t).
\]

Write \(E=\sum_re(r)\), \(M=\#\{r:3r\le t\}\), and
\(B(F)=\sum_{v\in F}(3-\deg(v))\). The known identity is

\[
3|F|=M+B(F)+E.
\]

Since a pure color phase has \(E=0\), the desired formula is equivalent to

\[
B(F)+E\ge \min_j\bigl(B(C_j)-3I_j-3P_j\bigr).
\tag{1}
\]

The minimum must include the correction inside each color term. The identity alone proves no such inequality.

**Directional defect lemma.** For every smooth \(v\),

\[
\boxed{(f(6v)-f(v))_+\le e(2v)+e(3v)\quad(9v\le t),}\tag{2}
\]

and

\[
\boxed{(f(v)-f(6v))_+\le e(v)+e(4v)+e(9v)\quad(27v\le t).}\tag{3}
\]

These are unconditional inequalities for binary covers.

For (2), the only nontrivial case is \(f(v)=0,f(6v)=1\). The corner at v forces \(f(2v)+f(3v)\ge1\), and then
\(e(2v)+e(3v)=f(2v)+f(4v)+f(3v)+f(9v)\ge1\).

For (3), suppose \(f(v)=1,f(6v)=0\). If \(e(v)\ge1\), there is nothing to prove. Otherwise \(f(2v)=f(3v)=0\). The corners at \(2v,3v\) force \(f(4v)=f(9v)=1\). The corner at \(6v\) forces \(f(12v)+f(18v)\ge1\), and thus \(e(4v)+e(9v)\ge1\). This proves (3). All other cases have left side zero.

**No repeated charge within a fixed color.** Color an anchor by \(c(r)=a-b\pmod3\). Fix j and any set V of color-j labels satisfying the relevant cutoff. In (2), the anchor sets \(2V\) and \(3V\) have different colors, and each multiplication map is injective. In (3), the sets \(V,4V,9V\) have three different colors. Consequently

\[
\begin{aligned}
\#\{v\in V:f(v)=0,f(6v)=1\}
 &\le\sum_{r\in2V\cup3V}e(r)\le E,\\
\#\{v\in V:f(v)=1,f(6v)=0\}
 &\le\sum_{r\in V\cup4V\cup9V}e(r)\le E.
\end{aligned}\tag{4}
\]

The two estimates are separate: an energy atom can appear in one charge of each direction. Summing both right sides must not be described as a single injective charge. Summing across all colors also loses the one-charge property. No canonical-cover assumption is used.

**The associated integer cuts.** Removing the positive-part notation from (2)–(3), and substituting the e's, gives the valid inequalities

\[
\boxed{\sum_{m\in\{1,2,3,4,6,9\}} f(mv)\ge2\quad(9v\le t),}\tag{5}
\]

\[
\boxed{\sum_{m\in\{2,3,4,6,8,9,12,18,27\}} f(mv)\ge3
\quad(27v\le t).}\tag{6}
\]

The first is also the elementary observation that the three corners rooted at \(v,2v,3v\) have no common vertex. Both cuts were additionally checked on all binary assignments of their ten-vertex local support. The analytic proofs above establish them generally.

The cuts have a useful stability interpretation even for fractional feasible points: if the appropriate local overcoverage is zero, they force the corresponding inequality between \(f(v)\) and \(f(6v)\). When both sets of local defects vanish, they recover equality. The ordinary corner LP did not encode this implication.

### Gaps

Equations (2)–(4) control directed changes in one color; they do not show that boundary gains are bounded by those changes with the sharp coefficient needed in (1). In particular, they do not justify combining minimum energy with a different canonical color-maximizing choice of cover. No bound \(E\le1\) for all optimal covers is asserted.

## Do these integer cuts give a uniform calibration of the patched formula?

### Takeaway

No. They give an exact new certificate at \(t=486\), where the ordinary fractional method failed, but the proposed uniform ceiling bound is false for this cut family on an actual 2–3 cap. The failure is verified by rational arithmetic, not inferred from solver tolerances.

### Cited Findings

* The previous unrestricted fractional obstruction at \(t=486\) has integer optimum 11 and fractional optimum \(2468/249\). A simpler fractional point of weight 10 was also saved. [Earlier exact obstruction](<../../early-attacks/open-proof-gap-attacks/cover.md>).
* This round's single small-cap test, exact primal/dual certificate, and local binary verification are [calibration_486.py](<calibration_486.py>) and [calibration_486.json](<calibration_486.json>).
* The one adversarial large-cap test and exact rational feasible point are [calibration_cap_probe.py](<calibration_cap_probe.py>) and [calibration_cap_probe.json](<calibration_cap_probe.json>). A separate [optimizer-free verifier](<verify_calibration_certificates.py>) checks the certificates using only integers and rational numbers.

### Inferences

Let \(\Lambda(t)\) minimize \(\sum_{v\in D_t}x_v\) under the corner constraints, all translated cuts (5)–(6), and \(0\le x_v\le1\). Every binary cover is feasible, so \(\tau(t)\ge\lceil\Lambda(t)\rceil\). If \(Q(t)=\min_j(K_j-I_j-P_j)\), a sufficient uniform theorem would be

\[
\Lambda(t)>Q(t)-1.\tag{7}
\]

This particular theorem is false.

**Repair at 486.** The new relaxation on the 33 vertices, with 50 inequalities, has exact optimum

\[
\Lambda(486)=\frac{235}{23}>10.
\]

The small test allowed \(x_v\ge0\) without an upper bound; its rational primal already lies in \([0,1]\), so the value also applies to the bounded formulation above. The saved dual has nonnegative weights and total incident weight at every vertex at most one. Its weighted right-hand sides sum to \(235/23\), equal to the feasible primal objective. Thus weak duality alone certifies equality, without trusting the numerical optimizer. Taking the ceiling proves 11, agreeing with the independently rerun exact integer DP and the known construction.

For a compact description of the dual, all following weights have denominator 23. Corner numerators are

\[
\begin{array}{c|rrrrrrrrrrrrrrrr}
r&1&4&6&9&12&16&27&32&36&72&81&96&108&128&144&162\\\hline
23y_r&11&1&11&7&1&1&11&10&7&3&7&3&8&23&10&8.
\end{array}
\]

For six-vertex cuts, the root/numerator pairs are
\((1,12),(4,10),(8,12),(9,4),(48,10),(54,7)\).
The only nine-vertex cut used has root nine and numerator one. All other dual weights are zero. The old weight-ten half-integral point violates (5) at \(v=48\): its six entries sum to \(3/2\), not two.

**Exact failure at one actual large cap.** Choose the already saved smooth cutoff

\[
t=990677827584,
\qquad |D_t|=534.
\]

Exact prime-exponent enumeration gives

\[
(K_0,K_1,K_2)=(178,178,178),\qquad
(I_0,I_1,I_2)=(P_0,P_1,P_2)=(0,0,0).
\]

Thus \(Q(t)=178\), computed with integer comparisons at both correction endpoints. The saved certificate has denominator \(10^6\), all coordinates between zero and one, and satisfies **all 1367** applicable corner, six-vertex, and nine-vertex inequalities. Its total is

\[
\sum_vx_v=\frac{176511563}{1000000}=176.511563<177=Q(t)-1.
\tag{8}
\]

The optimizer was used only to suggest a point. Each coordinate was rounded upward to a rational multiple of \(10^{-6}\), clipped at one, and every resulting inequality was then checked with integers. The separate verifier reconstructs the smooth board and every inequality from the certificate; it does not call SciPy. Therefore (8) is an exact upper bound for \(\Lambda(t)\), sufficient to disprove (7), whether or not the unknown exact integer optimum at this larger cap equals 178.

This is a counterexample to the proposed calibration, **not** a cover of size 177 and not a counterexample to (C). It shows only that these two local cut families leave an additive gap greater than one. It says nothing about all larger local hierarchies or about using additional nonlocal information in (4).

### Gaps

No uniform dual or peeling proof for (7) can exist, because (8) refutes it. No further gadgets were added by numerical trial. Only the known small obstruction and one previously saved large cap were tested; there was no prefix sweep. A successful use of the defect charges must retain information not captured by this relaxation.

## What exact boundary information remains available beyond this relaxation?

### Takeaway

There are exact vector-valued boundary identities and a six-shell transfer that reduces extension of a fixed inner cover to two path problems. Neither permits forgetting the inner boundary word. They describe a nonlocal obligation precisely, rather than turning a growing boundary into an assumed finite state.

### Cited Findings

* The growing-width diagonal DP was already available, and remains an exact algorithm rather than a proof of the patched formula. [Original exact DP](<../../early-attacks/open-conjecture-transfer-search/exact_168_diagonal.py>).
* The distinction between an arbitrary optimal cover and a specially chosen representative is essential in the [independent audit](<independent_audit.md>). No simultaneous canonical properties are assumed in the deductions below.

### Inferences

**Three disjoint corner packings.** Fix an anchor color i. The corners rooted at color-i labels are pairwise vertex-disjoint: a vertex's three possible parent roots have three different colors. Let \(M_i\) be their number, let \(E_i\) be the overcoverage on those corners, and let \(B_i(F)\) count selected vertices outside their union. Partitioning F gives the exact identity

\[
\boxed{|F|=M_i+E_i+B_i(F).}\tag{9}
\]

For \(t\ge3\), the uncovered boundary sites in this packing are explicitly

\[
\begin{aligned}
B_i(F)={}&|F\cap C_i\cap(t/3,t]|\\
&+|F\cap C_{i+1}\cap(\{a=0\}\cup(2t/3,t])|\\
&+|F\cap C_{i+2}\cap\{b=0\}|.
\end{aligned}\tag{10}
\]

The three terms have distinct vertex colors, so there is no double counting within (10). Summing (9) over i recovers the scalar energy identity. For a pure phase \(C_j\), \(E_i=0\), hence \(B_i(C_j)=K_j-M_i\). Thus the global lower bound would require the paid extra selections \(E_i+B_i(F)\) to dominate the smallest adjusted phase-boundary cost. That conclusion is not contained in (9).

The packing also supplies an exact local lift. If a packet rooted at u is singly hit, give it state 0, 1, or 2 according as its selected vertex is \(u,2u,3u\). For smooth interior u and \(g=4/3,q=9/2\), suppose the packets rooted at \(u,gu,qu,6u\) exist and are singly hit. The two intervening corner constraints become

\[
\begin{aligned}
&[s_u=1]\ \lor\ [s_{gu}=2]\ \lor\ [s_{6u}=0],\\
&[s_u=2]\ \lor\ [s_{qu}=1]\ \lor\ [s_{6u}=0].
\end{aligned}\tag{11}
\]

For multiply hit packets, use a nonempty subset of states and pay its cardinality minus one in \(E_i\). Boundary vertices outside packets pay in \(B_i\). This retains the exact cover constraints, but is not a free three-phase contour model: for example packet states \((0,2,1,1)\) at \((u,gu,qu,6u)\) satisfy both constraints with one hit each, despite using three states. No topological simplicity of interfaces follows merely from this lift.

**An exact six-shell boundary transfer.** For \(t\ge6\),

\[
D_t=6D_{t/6}\ \dot\cup\ \{2^a:a\ge0,2^a\le t\}
\ \dot\cup\ \{3^b:b\ge1,3^b\le t\}.
\]

Fix any cover \(G\) of \(D_{t/6}\) and place its dilation \(6G\) in the interior. Let \(h_a\), \(1\le a\le H=\lfloor\log_2t\rfloor\), and \(v_b\), \(1\le b\le B=\lfloor\log_3t\rfloor\), be the remaining horizontal and vertical selection bits. Let z be the bit at one. All still-unchecked constraints are exactly

\[
\begin{array}{ll}
h_a+h_{a+1}\ge1-1_G(2^{a-1}),
&1\le a\le\lfloor\log_2(t/3)\rfloor,\\
v_b+v_{b+1}\ge1-1_G(3^{b-1}),
&1\le b\le B-1,\\
z+h_1+v_1\ge1.&
\end{array}\tag{12}
\]

Indeed, a corner rooted off both axes belongs to the dilated inner board. A horizontal-axis corner has inner vertex \(3\cdot2^a=6\cdot2^{a-1}\); a vertical-axis corner has inner vertex \(2\cdot3^b=6\cdot3^{b-1}\). The remaining corner is rooted at one. This proves both necessity and sufficiency of (12).

For each fixed first bit s, let \(H_G(s)\) be the minimum number of selected horizontal-axis bits satisfying the first line, with \(h_1=s\). Define \(V_G(r)\) similarly. Each is a two-state path vertex-cover DP; without an endpoint condition a run of m required consecutive edges costs \(\lceil m/2\rceil\). The exact minimum extension cost is

\[
\mathcal E_t(G)=\min_{s,r\in\{0,1\}}
\left(H_G(s)+V_G(r)+1_{s=r=0}\right).
\tag{13}
\]

Consequently the exact global recursion is

\[
\boxed{\tau(t)=\min_{G\text{ covers }D_{t/6}}
\bigl(|G|+\mathcal E_t(G)\bigr).}\tag{14}
\]

Restriction of an outer cover gives an admissible G; conversely every extension satisfying (12) gives an outer cover, so neither direction loses competitors. The minimum in (14) is over **all** inner covers, not merely minimum inner covers. Both entire inner axis words determine which path edges are required. Keeping only \(|G|\), or only its minimum value \(\tau(t/6)\), is not justified. A scalar or fixed-state recurrence would need a separate dominance theorem for these boundary words.

### Gaps

No dominance theorem for (13)–(14), no sharp nonlocal charge deriving (1), and no vertical-phase normalization was proved in this round. The exact obstruction (8) closes the proposed two-cut LP route in its stated form. It does not close every energy or boundary-DP route. The finite formula (C), and hence its use in the separate irrationality argument, remain unresolved.
