# Audits clarify what global optimality requires

**The requested audits are complete, with explicit corrections; the global finite optimum (C) remains unproved, so the goal is not complete.** Independent derivations support the general axis-avoiding classification, the coefficient extension, and the corrected conditional return argument. The subsequent research supplies canonical exchange inequalities, boundary matching and forest representations, restrictions on vertical-touching critical sets, and quantitative defect charges. Exact counterexamples rule out several proposed ways of promoting these facts to a global theorem. The new vertical arguments are written proofs with specified checks, but have not received a second independent audit. No completed step 6, irrationality proof, historical priority, or Lean verification is claimed. ([Independent audit](<independent_audit.md>), [second combinatorial and coefficient audit](<combinatorial_and_coefficient_audit.md>))

## The audited theorem stops at a prescribed vertical phase

Let \(D_t=\{2^a3^b\le t:a,b\ge0\}\), color its points by \(a-b\pmod3\), and write \(K_j=|C_j|\). A cover meets every corner \(\{u,2u,3u\}\); its minimum size is \(\tau(t)\). Put \(\delta_j=I_j+P_j\): the corrections record an isolated power of two \(x\in(2t/3,t]\), or the replacement of \(\{x,9x/2,6x\}\) by \(\{3x/2,2x\}\) when \(x=2^A\), \(A\ge1\), and \(6x\le t<27x/4\). At most one exceptional root exists across all colors. The construction proves

\[
\tau(t)\le Q(t):=\min_j(K_j-\delta_j).
\]

**(C) is equality for every \(t\ge3\)**. ([Construction and definitions](<../../early-attacks/open-conjecture-transfer-search/168_grid.md>))

For \(U\subset C_j\), let \(B(U)\) contain the opposite edge of each corner whose color-j vertex belongs to \(U\), and put \(d(U)=|U|-\nu(B(U))\). The matching reduction gives \(\tau=K_j-\max_U d(U)\). Both independent audits confirm that every inclusion-minimal positive-deficiency set avoiding \(a=0\) is exactly an isolate or the three-label patch; axis avoidance requires \(A\ge2\) for that patch. The proof checks all owner incidences, deletion including an empty remainder, selected-vertex distinctness, and the three successive strip counts, including the \(k=2\) endpoint. It assumes neither one horizontal root nor hole-freeness. Consequently

\[
d(U)\le\delta_j\quad(U\cap\{a=0\}=\varnothing).
\]

A cover containing every vertical-axis point of color \(j\) therefore has size at least \(K_j-\delta_j\). What remains missing is an **existential** statement that some minimum cover contains such a complete phase. The stronger assertion about every minimum is false. ([Audited proof and precise consequence](<combinatorial_and_coefficient_audit.md>))

The arithmetic audits preserve three explicit qualifications: **\(B\ge1\)** in the variable-integer-coefficient corollary, **\(1\le Y<X\)** in the return-tail estimate, and **\(3/5<p/q<2/3\)** in the rational floor model. The broader model range fails at \(p/q=4/7\): at \(b=7\), the two correction tests both fire. Both range corrections preserve every sufficiently late convergent used by the argument. The coefficient estimate follows from the established one-form Subspace Theorem, with fixed term count and loss \(B^{-m-\epsilon}\); it is unconditional on (C). ([Audited extension](<arithmetic_and_obstruction_audit.md>), [Luca–Ouaknine–Worrell, Theorem 1](https://arxiv.org/html/2412.07908v2#S2.Thmtheorem1))

The double-return identity retains **both infinite side sums**, and the periodic model handles all four low columns. Conditional on (C), it yields a four-unit cleared error with denominator \(27(2^{3q}-1)(3^{3p}-1)\). The corrected implication is only this: rationality forces eventual equality with the model values along any unbounded nonresonant convergent sequence satisfying \(q'/q>5+\varepsilon\). Such an infinite sequence and failure of eventual equality remain unproved; neither floor disagreement nor the finite skew checks supplies nonvanishing. ([Corrected theorem and errata](<independent_audit.md>), [KK Proposition 7.4 and its application](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf))

## Canonical exchanges and two cones expose the remaining interaction

Fix \(j\), choose a minimum cover \(F\) maximizing \(|F\cap C_j|\), and set \(U=C_j\setminus F\), \(W=F\setminus C_j\). Then \(U\) is a minimum-cardinality maximizer of deficiency \(D_j=K_j-\tau\). For nonempty \(S\subset W\), let \(T_F(S)\) be precisely the omitted owners whose corners become uncovered after deleting \(S\). Canonicality proves

\[
|T_F(S)|\ge |S|+1.
\]

This **exact repair inequality includes double coverage correctly**: a doubly hit corner needs repair only when both selected endpoints are deleted. It extends essential support and strict owner expansion beyond deficiency one. ([Canonical proof](<canonical_phase.md>))

Selecting one pair from each selected vertex's owner neighborhood gives a planar forest with \(D_j\) components. Its north-parent subforest can be rooted at the horizontal owners. Separately, the owner–selected-vertex incidence graph \(H\) admits three matchings saturating \(W\), whose unmatched owners lie respectively on the horizontal axis, above \(t/3\), and on the vertical axis together with the possible exceptional root. Every positive component of their union contacts these three boundary sets. **Neither representation gives independent deficiency components or disjoint tripods**: unused third incidences can couple forest components, and one matching-union component can carry several unmatched owners. ([Forest construction](<canonical_phase.md>), [incidence matching lift](<vertical_critical.md>))

For an origin-free vertical-touching critical set, let \(x=2^A,y=3^B\) be its least axis roots and set \(g=4/3,q=9/2\). The new proof places every owner in the union of the two cones generated from \(x,y\), and establishes

\[
A/2\le B\le2A,\quad r=(2A-B)/3,\quad s=(2B-A)/3,
\quad z=xq^s=yg^r=2^{2r}3^{2s}.
\]

Forced chains meet at \(z\). For \(r\ge1\), strict expansion gives either \(z\le2t/9\) with \(qz\in U\), or \(y>t/3\) and \(r\in\{1,2\}\). In the high branch, \(r=2\) forces \(s\le1\), while \(r=1,s=0,1\) reduces to explicitly paid finite cases. The surviving high family has \(r=1,s\ge2\) and \(t/2<z\le9t/16\); a critical example at \(t=576\) shows it is real. Origin-containing sets and \(r=0\) require separate treatment; no positive-length chain may be assumed when \(s=0\). ([Proof, endpoint qualifications, and certificates](<vertical_critical.md>))

The small patch \(\{2,9,12\}\) remains critical throughout **\([12,18)\)** because the vertical owner's east edge is absent. This is longer than its construction-indicator window \([12,27/2)\). In that latter window the prescribed color-one vertical optimum is \(K_1\), not \(K_1-P_1\). These exceptions prevent an unqualified preferred-phase normalization. The two-cone reductions and newer canonical representations remain distinct from the independently audited axis-avoiding theorem. ([Small-patch analysis](<vertical_critical.md>))

## Exact counterexamples eliminate the proposed shortcuts

At \(t=54\), the **unique** minimum cover maximizing color zero is \(\{1,6,12,16,18\}\), which contains no complete vertical phase and triple-hits one corner. Thus a further tie-breaker within an arbitrary preferred-color canonical family cannot repair normalization. The same board disproves submodularity of owner matching rank: for \(A=\{8,48\}\), \(B=\{6,8,36\}\), the ranks are \(2,4,5,2\) on \(A,B,A\cup B,A\cap B\), respectively. Neither failure disproves a theorem restricted to a winning adjusted color. ([Exact certificates](<canonical_phase_check.json>), [derivation](<canonical_phase.md>))

At \(t=1536\), \(U=C_0\setminus\{384,512\}\) has deficiency one, while the full class \(C_0\) has deficiency zero. **Unrestricted full-class filling therefore fails.** At \(t=729\), three connected color paths can meet both axes away from the origin and the outer band, avoid the exceptional root, and still have corner-free union. Their deficiencies are \((-3,-2,-2)\), so this refutes weak geometric spanning, leaving the stronger positive-critical-set obstruction open. ([Filling certificate](<vertical_critical_check.json>), [replayed spanning certificate and scope](<arithmetic_and_obstruction_audit.md>))

## Defect charges improve local bounds but require nonlocal control

For a binary cover write \(e(u)=f(u)+f(2u)+f(3u)-1\). The new directional inequalities are

\[
(f(6v)-f(v))_+\le e(2v)+e(3v)\quad(9v\le t),
\]
\[
(f(v)-f(6v))_+\le e(v)+e(4v)+e(9v)\quad(27v\le t).
\]

Within one fixed color, each direction charges every participating defect at most once. Combining directions or colors loses that guarantee. Their associated six- and nine-vertex cuts strengthen the corner LP. At \(t=486\), exact primal and dual certificates give **\(235/23>10\)**, recovering the integer lower bound 11. ([Proof and small certificate](<boundary_calibration.md>))

The uniform ceiling argument nevertheless fails at \(t=990677827584\), with 534 vertices: \(K=(178,178,178)\), \(I=P=0\), but a rational fractional point of total **\(176.511563<177\)** satisfies all 1367 corner and added inequalities. The coordinator independently replayed the optimizer-free exact verifier successfully. This refutes this cut family's proposed additive-gap bound, without supplying a binary counterexample to (C) or ruling out every stronger hierarchy. ([Rational certificate](<calibration_cap_probe.json>), [exact verifier](<verify_calibration_certificates.py>))

An exact alternative decomposes \(D_t\) into \(6D_{t/6}\) and the two axes. For a fixed inner cover \(G\), extension costs reduce to two path-cover problems coupled at the origin. Hence

\[
\tau(t)=\min_{G\text{ covers }D_{t/6}}\bigl(|G|+\mathcal E_t(G)\bigr).
\]

This minimum ranges over **all inner covers**, and \(\mathcal E_t(G)\) depends on both complete inner axis words. No reduction to minimum inner covers, scalar state, or fixed number of states has been justified. ([Exact boundary transfer](<boundary_calibration.md>))

## Conclusion

The sharp remaining obligation is: for a color minimizing \(K_j-\delta_j\), prove **\(d(U)\le\delta_j\) for every \(U\subset C_j\)**, including arbitrary vertical-touching unions. Classifying selected critical sets of deficiency one and paying for them separately by other phases does not bound aggregate deficiency. A sufficient alternative is to prove that some global minimum contains a complete vertical phase. The current exchange, matching, cone, and defect arguments establish neither statement; a boundary-word dominance theorem or an equally sharp global phase comparison is still needed.

Verification covers the stated ordinary proofs and exact finite certificates, not an unbounded global claim. The coordinator checked the new two-cone arguments and finite endpoint intervals without finding a local error, but no second full independent audit of those lemmas is complete. Finite solver observations are not uniform theorems. This synthesis added no research or experiments and changed no archived reports. Even after (C), the arithmetic return and nonvanishing obligations would remain. Lean and any external submission have not been undertaken.
