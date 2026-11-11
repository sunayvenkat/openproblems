# Boundary reductions sharpen an unfinished transfer

**No different currently unsolved conjectures.io problem has been proved.** Erdős #168(ii) remained presented as unsolved at **2026-11-07 04:34:05 UTC**, or 23:34:05 on 6 November in America/Indianapolis. It asks whether the limiting density of sets avoiding every triple \(\{n,2n,3n\}\) is irrational. Kohlmeyer–Kruer's #1062 tools remain a proposed route, but the necessary combinatorial and arithmetic inputs are incomplete. This round proves a single-root matching theorem, an exact boundary path-matrix identity, and an unconditional separation of color discrepancies; it derives further arithmetic formulas conditional on the finite-cover conjecture. Independent reviews found no fatal gap in these deductions. **The original objective remains unmet**, and no priority claim is made for the auxiliary results. ([Target](https://conjectures.io/problems/erdos168-erdos-168-parts-ii), [timestamped review](<arithmetic_review.md>))

## The finite construction still needs a global lower bound

Write \(F(N)\) for the largest triple-avoiding subset size in \([1,N]\), and \(c=\lim F(N)/N\). Existence is known, so the site's formal limsup target agrees with this limit. Let \(D_t=\{(a,b)\ge0:2^a3^b\le t\}\), and let \(\tau(t)\) be the minimum number of points meeting every upward corner. Color by \(a-b\pmod3\), with classes \(C_j\) of sizes \(K_j\). Write \(I_j\) for an isolated power of two in \((2t/3,t]\), and \(P_j\) for the valid replacement
\[
\{x,9x/2,6x\}\longmapsto\{3x/2,2x\},
\qquad x=2^a, a\ge1,\quad 6x\le t<27x/4.
\]
Each correction belongs to the color of its removed axis point. The proved construction gives \(\tau\le\min_j(K_j-I_j-P_j)\); **(C) denotes the unproved assertion of equality**. The known smooth-component density reduction connects this finite problem to #168(ii). ([Primary density analysis](https://arxiv.org/html/2604.15515v1), [construction](<../../early-attacks/open-conjecture-transfer-search/168_grid.md>))

For \(U\subseteq C_j\), let \(B(U)\) join the other two vertices of each corner whose color-j point lies in U. Then
\[
d(U)=|U|-\nu(B(U)),\qquad \tau=K_j-\max_U d(U).
\]
Earlier hole filling permits a maximizer with connected complement in the full face lattice. Its positive-deficiency components can be taken simply connected and must meet the horizontal axis \(b=0\). This maximal-cardinality normalization is **not** the separate choice of an inclusion-minimal positive, or “critical,” set. ([Hole-filling proof](<../../early-attacks/open-proof-gap-attacks/hole_filling.md>))

## One horizontal root now forces the known defects

**Single-root theorem.** If U avoids the vertical axis \(a=0\) and contains at most one horizontal-axis label, then \(d(U)\le I_j+P_j\), without assuming simple connectivity. The north-parent edges \(N(u)=\{u/3,2u/3\}\) match all \(Q=\{u\in U:b>0\}\). With one root, positive deficiency therefore means this baseline is already maximum. ([Proof](<boundary.md>), [independent audit](<boundary_review.md>))

Index left and right vertices by their N owners. The residual arcs are
\[
R(w):6w\to9w/2,\qquad E(w):9w/2\to3w/4.
\]
From a reachable left index \(9w/2\), with \(w\le4t/9\), either E exits immediately or its target \(q=3w/4\) is matched. Then R(q) starts at the same left index and continues the search. Each repetition lowers the first exponent by two; an exit is unavoidable, including possible early R exits. A smallest-owner argument handles larger external E sources. Consequently zero augmentation is equivalent to closure under every available generated label \(6u\) and \(9u/2\). Closure forces
\[
U\subset(4t/27,t/6]\cup(2t/3,t].
\]
Its sole horizontal root is therefore the isolate or the patch root. ([Reviewed rotation argument](<arithmetic_review.md>))

Separately, criticality forces deficiency one and requires every minimum-cover vertex to uniquely cover edges of at least two owners. Leaf arguments place the smallest label on \(b=0\) and force the initial triple \(\{x,9x/2,6x\}\). **Only inside the patch window does this force the entire critical set to equal that triple**; outside it, continuation remains possible.

A boundary-pocket extension supplies another proved restriction. For an added connected m-face region V with h holes, let \(q_2\) count complementary boundary edges with both endpoints available but absent from the old graph, and \(p_0\) those with neither endpoint available. Matching replacement gives
\[
\Delta\nu\le m+\left\lfloor(1-h+q_2-p_0)/2\right\rfloor.
\]
Thus charge \(q_2-p_0\le h\) permits filling. For a finite-board complementary component, the charge equals \(\sum_{v\in V}\sigma_t(v)\), where \(v=2^a3^b\) and
\[
\sigma_t(v)=\mathbf1_{a\ge1,\,2t/9<v\le t/3}
-\mathbf1_{v=1}-\mathbf1_{b=0,\,v>t/2}
-\mathbf1_{v>2t/3\ \mathrm{or}\ (a=0,\,v>t/3)}.
\]
Every surviving pocket of a largest-cardinality maximizer must have charge at least \(h+1\). This is necessary, not a total-deficiency bound. ([Charge proof and endpoint audit](<boundary_review.md>))

## An exact path matrix preserves the missing bottlenecks

For normalized U, let \(r=|U|-|Q|\). Define \(P_U(x,y)\) as the number of nonempty residual paths from an unmatched left index x to an unmatched right index y, with every internal index in Q. Then
\[
\boxed{\nu(B(U))=|Q|+\operatorname{rank}_{\mathbb Q}P_U,
\qquad d(U)=r-\operatorname{rank}_{\mathbb Q}P_U.}
\]
This uses ordinary rational rank. Signing the **rectangular bipartite adjacency matrix** A produces a nilpotent core \(I-T\); its Schur complement is \(-P_U\). Connected full-plane complement ensures the relevant alternating cycles enclose complete hexagonal patches, making their determinant terms have the same sign. Hence \(\operatorname{rank}A=\nu\). The full symmetric adjacency matrix instead has rank \(2\nu\). ([Self-contained proof](<dual.md>), [audit](<boundary_review.md>))

Bipartition sizes cannot replace this matrix. At \(t=128\), the hole-free, axis-avoiding component \(U=\{16,54,72,96,128\}\) has two bipartitions of size five but matching number four. Its deficiency is the allowed isolate, accompanied by a neutral attachment. Distinct residual rows also do not guarantee disjoint complete paths: their exits can coincide. That earlier inference has been withdrawn.

Exact matching, rational rank, and path counts agreed in **11,811 bounded cases through \(t=486\)**; the reviewer inspected the checker but did not rerun that enumeration. Three MILPs at \(t=1536,3072,24576\) reported infeasibility when seeking positive deficiency while retaining a patch vertex and fixing the vertical-axis color. They sought **alternative mechanisms matching or improving the patched bound**, not strictly beating it; their statuses are numerical, not exact certificates. ([Evidence and qualifications](<boundary_review.md>))

## Axis separation exposes the unresolved arithmetic

Let \(\omega^3=1\ne\omega\), \(W(t)=\sum_{2^i3^j\le t}\omega^{i+2j}\), and
\[
A_a=\omega^{-a}W(2^a),\quad B_b=\omega^{-2b}W(3^b),\quad
Z_{a,b}=\omega^{-a-2b}W(2^a3^b).
\]
Partitioning the exponent triangle into a rectangle and two arms proves the **unconditional identity**
\[
Z_{a,b}=A_a+B_b-1+C_{a\bmod3,b\bmod3},\qquad
C=\begin{pmatrix}0&0&0\\0&1&-\omega^2\\0&-\omega&1\end{pmatrix}.
\]
The reviewer reran 120 separation checks, 54 cone comparisons against certified optima, and 18 strip checks. These supplement the proof and do not establish (C). ([Arithmetic derivation](<arithmetic.md>), [review](<arithmetic_review.md>))

For \(b\ge4\), let \(\varepsilon_b\) be the isolated/patch indicator vector rotated to the inserted color; it is independent of a. Define
\[
\mathcal C_b=\{x+y\omega:x\le\varepsilon_{b,0}-\varepsilon_{b,2},\quad
x-y\le\varepsilon_{b,0}-\varepsilon_{b,1}\}.
\]
**Conditional on (C)**, the birth digit \(\eta_{a,b}=\Delta\tau(2^a3^b)\) equals \(\mathbf1_{\mathcal C_b}(Z_{a,b})\), with ties included. Corrections do not change at these births; the low columns are handled separately.

Writing \(R_b=\sum_{a\ge0}(1-3\eta_{a,b})2^{-a}\), the conditional complete-column output is
\[
R_b=2-3\sum_{r=0}^2 2^{-r}\sum_{n\ge0}8^{-n}
\mathbf1_{\mathcal C_b}(Z_{3n+r,b}),\qquad
9c-6=\sum_{b\ge0}3^{-b}R_b.
\]
The underlying axis state evolves by a nine-breakpoint, mean-zero step-function increment over rotation by \(\alpha=\log_3 2\): \(Y_n=A_{3n}\), \(Y_{n+1}=Y_n+\Phi(\{n\alpha\})\). The output depends on the accumulated, unbounded planar state, not just rotation phase. Unconditionally,
\[
R_b\in\mathbb Q\quad\Longleftrightarrow\quad
(\eta_{a,b})_{a\ge0}\text{ is eventually periodic}.
\]
Neither periodicity nor nonperiodicity is proved. A finite number of base-8 series is **not** a finite number of S-unit terms. ([Complete formulas and limitations](<arithmetic.md>))

## Conclusion

Kohlmeyer–Kruer Proposition 7.4 fixes the number of terms and rational coefficient vector. Their application supplies at most 404 terms, suitable height, an extra exponential error saving, and nonvanishing. Here a previous unconditional weighted identity controls height, but fixed-dimensional compression, the stronger error estimate, and nonvanishing remain missing. Endpoint returns alone do not supply weighted cancellation. ([Primary #1062 manuscript, §§6–7](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf), [weighted obstruction](<../../early-attacks/open-proof-gap-attacks/weighted.md>))

The smallest next combinatorial obligation is an adequate nonzero minor proving \(\sum_i\operatorname{rank}P_{U_i}\ge\sum_i r_i-(I_j+P_j)\) for a winning color, beginning with axis-avoiding multi-root components; vertical-axis components still need global color comparison. This synthesis performed no new search or computation. Status is timestamped, not a global priority certification; an inaccessible benzenoid attribution was not independently verified, and the rank result rests on its self-contained proof. No Lean verification or external submission was undertaken. The missing finite-cover and S-unit proofs remain the material limitations.
