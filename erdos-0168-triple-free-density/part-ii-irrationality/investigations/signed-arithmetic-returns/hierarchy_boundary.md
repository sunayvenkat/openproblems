# Actual dilation potentials retain the hierarchy boundary

## Does the binary doubling potential make the actual boundary rational?

### Takeaway

No such conclusion follows from its full Mellin integral. That integral is an affine rational expression in the original target, while its restriction to the original exponent grid leaves an actual axis profile which cancels against fractional-axis jumps. This is an exact obstruction to that particular closure argument, not a proof that the actual profile is irrational. — [Exact certificate](hierarchy_boundary_check.py), [positive token and doubling input](../farey-transport-corrections/imbalance_tails.md).

### Cited Findings

- The accepted positive process has \(\tau(t)=\min_jT_j(t)\), \(M=\int_0^\infty\tau(t)t^{-2}\,dt=\sum_{a,b\ge0}\eta_{a,b}2^{-a}3^{-b}\). Its only nonintegral arrival is \(27/2\), where the minimum has zero jump. All nonzero birth jumps therefore lie at \(2^a3^b\). In particular \(\eta_{a,0}=0\) for every \(a\), and \(\eta_{0,1}=\eta_{0,2}=1\). — [Token identities](../hybrid-arithmetic-closure/global_carries.md), [independent actual-time check](hierarchy_boundary_check.py).
- For \(t\ge7\), the established doubling defect is binary. With \(m=\lfloor\log_3(2t)\rfloor\), its expression is \(\tau(2t)-\tau(t)-\lfloor(m+1)/3\rfloor\). — [Actual doubling proof](../farey-transport-corrections/imbalance_tails.md).
- The old retained-boundary identity does not evaluate its infinite sides. The present calculation examines whether the binary defect's **full** rationality under \(M\in\mathbb Q\) supplies that evaluation. — [Hierarchy identity HA1–HA10](../hybrid-arithmetic-closure/hierarchy_absorption.md).

### Inferences

**HB1. An exact full-potential identity, including small cutoffs.** Define for every \(t>0\)
\[
\kappa(t)=\#\{k\ge0:3^{3k+2}\le2t\},\qquad
h(t)=\tau(2t)-\tau(t)-\kappa(t).
\]
Thus \(h\) equals the binary defect above for \(t\ge7\); this definition retains its entire finite small-cutoff part as well. Let
\[
F_i=\sum_{b\ge0}\eta_{i,b}3^{-b},\qquad
G_j=\sum_{a\ge0}\eta_{a,j}2^{-a}.
\]
The relevant axis value is \(F_0\).

The signed jump measure of \(h\) has precisely two types of atoms:
\[
\Delta h(2^a3^b)=\eta_{a+1,b}-\eta_{a,b}\quad(a,b\ge0),
\tag{HB1}
\]
\[
\Delta h(3^b/2)=\eta_{0,b}-\mathbf1_{\{b\equiv2\pmod3\}}
\quad(b\ge0).
\tag{HB2}
\]
The two sets of locations are disjoint. These identities follow directly by shifting the nonzero jump measure of \(\tau\); the zero jump at \(27/2\) introduces no additional quarter-grid atom.

All reciprocal jump sums converge absolutely. Integration by parts is valid because \(h\) vanishes near zero and is bounded for large \(t\). Since
\[
\sum_{k\ge0}\frac{1}{3^{3k+2}/2}=\frac3{13},
\]
one obtains
\[
\int_0^\infty h(t)t^{-2}\,dt=M-\frac3{13}.
\tag{HB3}
\]
Crucially, its two filtered jump moments are
\[
J_{\rm grid}=M-2F_0,\qquad
J_{\rm fractional}=2F_0-\frac3{13}.
\tag{HB4}
\]
Their sum gives HB3 and eliminates \(F_0\) identically. Therefore \(M\in\mathbb Q\) makes the **sum** rational without establishing rationality of either filtered part.

This omitted part is nonzero in the actual target. The fractional jump at \(t=27/2\) is \(+1\), while the jump at \(t=3^{11}/2\) is \(-1\). More globally,
\[
J_{\rm fractional}\ge2(1/3+1/9)-3/13=\frac{77}{117}>0.
\tag{HB5}
\]
Thus simply deleting the fractional-axis contribution is contradicted by exact actual births, without an irrationality or probabilistic assumption. — [Actual clock and Mellin replay](hierarchy_boundary_check.py).

**HB2. What this proposed closure would really require.** Under \(M\in\mathbb Q\), rationality of \(J_{\rm grid}\) is equivalent to rationality of \(F_0\). Because its ternary digits \(\eta_{0,b}\) are zero or one, \(F_0\) is rational exactly when that actual axis birth word is eventually periodic: ordinary rational long division proves one direction, and a geometric sum proves the other; the ambiguous ternary tail of twos is absent. No eventual-periodicity or nonperiodicity theorem for this actual word is proved here.

### Gaps

- The calculation does not exclude an additional special identity implying \(F_0\in\mathbb Q\) under \(M\in\mathbb Q\).
- It does not prove irrationality of \(F_0\), or nonvanishing of the signed hierarchy residual.
- The positive lower bound HB5 is for an omitted fractional-axis observable, not for an irrationality approximation error.

## Do mixed dilation filters remove the remaining column and row profiles?

### Takeaway

Every full finite dilation-potential moment already belongs to the one-dimensional space \(\mathbb Q M\). Its exterior-grid filters are triangular encodings of the individual column and row series; mixed filters add their finite corner correction, not an independent arithmetic evaluation. — [Exact finite-filter replay](hierarchy_boundary_check.py).

### Cited Findings

- The actual birth measure is supported on the nonnegative \(2,3\) exponent grid, as established above. The existing hierarchy applies only finitely many positive shifts at each stage. — [Positive process](../hybrid-arithmetic-closure/global_carries.md), [retained hierarchy](../hybrid-arithmetic-closure/hierarchy_absorption.md).
- The checker evaluates the following filters both by actual downscaled birth atoms and by direct profile sums. No synthetic freely chosen array substitutes for the actual timing check. — [Certificate](hierarchy_boundary_check.py).

### Inferences

**HB3. The rank-one full moment and its lost exterior.** For \(A,B\ge0\), let
\[
D_{A,B}(t)=\tau(2^A3^Bt)-\tau(t).
\]
Its full Mellin integral is
\[
\int_0^\infty D_{A,B}(t)t^{-2}\,dt=(2^A3^B-1)M.
\tag{HB6}
\]
For a finite polynomial \(P(X,Y)=\sum r_{A,B}X^AY^B\), all integer or rational linear combinations of these identities thus lie in \(\mathbb Q M\). Adding explicitly evaluated forcing terms gives at most \(\mathbb Q M+\mathbb Q\).

The positive downscaled birth atoms outside the original exponent grid contribute
\[
E_{A,B}=2^A3^B
\sum_{\substack{i,j\ge0\\i<A\ {\rm or}\ j<B}}
\frac{\eta_{i,j}}{2^i3^j}.
\tag{HB7}
\]
For pure filters put \(E_A=E_{A,0}\), \(T_B=E_{0,B}\). Then
\[
E_A=2^A\sum_{i<A}2^{-i}F_i,\qquad
T_B=3^B\sum_{j<B}3^{-j}G_j,
\]
\[
E_A-2E_{A-1}=2F_{A-1},\qquad
T_B-3T_{B-1}=3G_{B-1}.
\tag{HB8}
\]
Here \(E_0=T_0=0\). Consequently the pure-filter system is triangular and invertible in the displayed profiles; it has not evaluated them. The mixed exterior is exactly
\[
E_{A,B}=3^BE_A+2^AT_B-
2^A3^B\sum_{i<A,j<B}\frac{\eta_{i,j}}{2^i3^j}.
\tag{HB9}
\]
Its last term is a finite rational corner. Thus mixed filters contain the same column and row unknowns, with no further relation supplied by their full moments.

There is one genuine free row: \(G_0=0\). Therefore \(T_1=0\), so the first ternary dilation has no exterior birth atoms. This does not bootstrap to higher rows. Already \(\tau(9t)-\tau(t)\) has a nonzero exterior atom at \(t=1/3\), coming from \(\eta_{0,1}=1\). The second ternary filter introduces \(G_1\).

### Gaps

- Formal triangularity does not assert rational linear independence of the actual numerical profile values.
- Filtered moments might satisfy additional actual-orbit identities. Such identities are not consequences of HB6 or the rationality of its full moments.
- This is a classification of the proposed scalar dilation-potential closure, not a new universal polynomial-boundary impossibility theorem.

## Which exact actual constants remain in the complete hierarchy numerator?

### Takeaway

The full boundary, including all four low rows, has an explicit **integer** profile dictionary. Every column up to the largest horizontal shift and every required high row appears formally; one known low row can be absorbed. This precisely identifies the missing arithmetic statement without declaring those actual constants independent. — [Dictionary proof and actual-array checks](hierarchy_boundary_check.py).

### Cited Findings

- Put \(c=1-3\eta\), \(d(a,b)=c(a,b+4)\), \(L_0=\sum_{a\ge0,b<4}c(a,b)2^{-a}3^{-b}\), and \(\Pi=P(2,3)\). The required comparison numerator is \(\mathcal B_P=81\Pi L_0+B_P(d)\), not merely \(B_P(d)\). — [Exact hierarchy HA10](../hybrid-arithmetic-closure/hierarchy_absorption.md).
- Both the actual single operator at \(5/8\) and a two-factor operator are checked against finite actual-array restrictions. The proof below applies to every finite positive-shift polynomial. — [Exact certificate](hierarchy_boundary_check.py).

### Inferences

**HB4. Complete profile dictionary.** Here \(P\in\mathbb Z[X,Y]\), as for every hierarchy operator. Write
\[
U_i=\sum_{b\ge0}c(i,b)3^{-b}=\frac32-3F_i,\qquad
V_j=\sum_{a\ge0}c(a,j)2^{-a}=2-3G_j.
\]
Let \(A_{\max},B_{\max}\) be the maximum exponents of \(P\). Absolute convergence and the retained-boundary formula give
\[
\boxed{\mathcal B_P=
\sum_{i<A_{\max}}\alpha_iU_i+
\sum_{j<B_{\max}+4}\beta_jV_j+K_P,}
\tag{HB10}
\]
where
\[
\alpha_i=81\sum_{A>i}r_{A,B}2^{A-i}3^B,
\]
\[
\beta_j=\begin{cases}
81\Pi\,3^{-j},&0\le j<4,\\
\displaystyle\sum_{B>j-4}r_{A,B}2^A3^{B-j+4},&j\ge4,
\end{cases}
\tag{HB11}
\]
and the explicitly finite correction is
\[
K_P=-\sum_{A,B}r_{A,B}2^A3^B\left[
81\sum_{i<A,j<4}\frac{c(i,j)}{2^i3^j}
+\sum_{i<A,k<B}\frac{c(i,k+4)}{2^i3^k}\right].
\tag{HB12}
\]
All \(\alpha_i,\beta_j,K_P\) are integers. In HB12, every finite denominator divides its displayed multiplier; this is why no unknown infinite side was absorbed into the word “integer.”

For \(P=P_m=\prod_i(X^{2q_i}+X^{q_i}Y^{p_i}+Y^{2p_i})\), every displayed profile coefficient is positive and
\[
A_{\max}=2\sum q_i,\quad B_{\max}=2\sum p_i,\quad
\alpha_{A_{\max}-1}=162,\quad
\beta_{B_{\max}+3}=3.
\tag{HB13}
\]
The last two values use the unique all-horizontal and all-vertical monomials. Also \(V_0=2\) is known, so its term \(162\Pi\) can be absorbed into the finite integer. The remaining formal dictionary consists of
\[
U_0,\ldots,U_{A_{\max}-1},\qquad
V_1,V_2,V_3,V_4,\ldots,V_{B_{\max}+3}.
\]
Its size grows with the retained scales. A fixed-dimensional seed theorem cannot be applied merely by naming this growing list. Conversely, the dictionary is not a proof that its actual values are independent or that a special linear combination cannot have cheap arithmetic.

**What would close the goal.** An actual-orbit identity must evaluate the **entire** integer combination HB10, perhaps under \(M\in\mathbb Q\), with a proved common rational clearing cost inside the hierarchy budget. Rationality of full dilation potentials, a single free row, or the finite corner does not establish that statement. The present work has not constructed such an identity.

### Gaps

- No rational/fixed-lattice theorem for \(\mathcal B_{P_m}\), or sufficiently cheap common clearing factor, is proved.
- The new actual jump and dictionary identities do not settle the hierarchy's signed residual nonvanishing.
- Skipped: Lean, outside literature search, installations, external posting and archived edits. Risk: interpreting a full-potential rationality identity as rationality of its filtered boundary pieces.
