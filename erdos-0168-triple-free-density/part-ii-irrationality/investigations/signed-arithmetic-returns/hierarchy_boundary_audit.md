# Independent audit of actual boundary filters

## Does the full doubling potential retain its fractional-axis contribution?

### Takeaway

**PASS, with no substantive erratum.** The full Mellin moment and both filtered moments reconstruct exactly, including all small cutoffs. Their cancellation does not evaluate the actual column series. — [Audited proof, HB1–HB5](hierarchy_boundary.md), [independent certificate](hierarchy_boundary_audit_check.py).

### Cited Findings

- The supplied checker passes. The independent checker imports no companion code: it computes the original smooth-board color counts and applies the isolate/patch corrections to obtain the finite optimum. It then reconstructs actual births by left and right cutoffs. This differs from the supplied delayed-token event enumeration. — [Supplied certificate](hierarchy_boundary_check.py), [independent board reconstruction](hierarchy_boundary_audit_check.py).
- The actual birth measure is supported on \(2^a3^b\). A new pure power of two is isolated when inserted, so \(\eta_{a,0}=0\) for every \(a\). The first two ternary-axis births satisfy \(\eta_{0,1}=\eta_{0,2}=1\). In particular, the minimum has no jump at \(27/2\). — [Accepted finite/token input](../hybrid-arithmetic-closure/global_carries.md), [independent clocks](hierarchy_boundary_audit_check.py).
- Direct actual-board calculations recover the fractional jumps \(+1\) at \(27/2\) and \(-1\) at \(3^{11}/2\), as well as the complete grid/fractional formulas on the tested clock range. — [Independent exact replay](hierarchy_boundary_audit_check.py).

### Inferences

Write
\[
M=\sum_{a,b\ge0}\eta_{a,b}2^{-a}3^{-b},\qquad
F_i=\sum_b\eta_{i,b}3^{-b},\qquad
G_j=\sum_a\eta_{a,j}2^{-a}.
\]
For \(\kappa(t)=\#\{k\ge0:3^{3k+2}\le2t\}\) and
\(h(t)=\tau(2t)-\tau(t)-\kappa(t)\), shifting the actual birth measure gives
\[
\Delta h(2^a3^b)=\eta_{a+1,b}-\eta_{a,b},
\quad
\Delta h(3^b/2)=\eta_{0,b}-\mathbf1_{b\equiv2\pmod3}.
\]
The two support sets are disjoint. The zero minimum jump at \(27/2\) cannot generate a new quarter-grid atom. — [HB1–HB2](hierarchy_boundary.md), [independent jump checks](hierarchy_boundary_audit_check.py).

These manipulations are absolutely convergent. Since \(M\le3\), the sum of the absolute reciprocal jump weights is at most \(3M+3/13\). Also \(\tau(t)=O((1+\log t)^2)\), so \(h(t)/t\to0\); the Mellin identity does not require a new proof of the stronger eventual binary-defect theorem. The functions vanish near zero. Change of variable over the **whole** positive half-line therefore gives
\[
\int_0^\infty h(t)t^{-2}\,dt=2M-M-\frac3{13}.
\]
No integration interval near zero was discarded. Separating that same jump measure gives
\[
J_{\rm grid}
=\sum_{a,b}\frac{\eta_{a+1,b}-\eta_{a,b}}{2^a3^b}
=M-2F_0,
\quad
J_{\rm frac}=2F_0-\frac3{13}.
\]
Thus the unknown cancels exactly. Moreover
\(J_{\rm frac}\ge2(1/3+1/9)-3/13=77/117>0\), so omitting that part is numerically false for the actual process. — [HB3–HB5 and accepted absolute convergence](hierarchy_boundary.md), [independent moment split](hierarchy_boundary_audit_check.py).

Under \(M\in\mathbb Q\), rationality of \(J_{\rm grid}\) is equivalent to rationality of \(F_0\). The ternary digits of \(F_0\) lie in \(\{0,1\}\), so rationality is equivalent to eventual periodicity of that digit word; no ambiguous all-twos expansion occurs. Neither direction asserts that the actual word is eventually periodic or nonperiodic. — [HB2 scope](hierarchy_boundary.md).

### Gaps

- Rationality of the full potential supplies no separate evaluation of either filtered moment.
- This audit proves neither irrationality of \(F_0\) nor impossibility of an additional actual-orbit identity relating it to \(M\).
- Eventual binary behavior is an accepted earlier result, but it is unnecessary for the Mellin equalities audited here. — [Earlier doubling proof](../farey-transport-corrections/imbalance_tails.md).

## Do the mixed filters evaluate new row or column constants?

### Takeaway

**PASS.** The pure filters are triangular encodings of the actual profiles, and mixed filters add an explicit finite corner. Their full moments alone provide no additional profile evaluation. — [HB6–HB9](hierarchy_boundary.md), [independent downscaled-atom certificate](hierarchy_boundary_audit_check.py).

### Cited Findings

- For \(\lambda=2^A3^B\), the full moment of \(\tau(\lambda t)-\tau(t)\) is \((\lambda-1)M\), while the exterior atoms of the downscaled birth measure have moment
\[
E_{A,B}=\lambda\sum_{i<A\ {\rm or}\ j<B}\eta_{i,j}2^{-i}3^{-j}.
\]
The subtraction of \(\tau(t)\) contributes no exterior atoms. — [HB6–HB7](hierarchy_boundary.md).
- Independent exact downscaling checks include atoms below one, the zero-scale case, binary and ternary triangular recurrences, and the mixed \((A,B)=(3,2)\) corner identity. — [Independent certificate](hierarchy_boundary_audit_check.py).

### Inferences

The formulas follow by partitioning the nonnegative exponent grid into the column strip, row strip and their intersection:
\[
E_A-2E_{A-1}=2F_{A-1},\qquad
T_B-3T_{B-1}=3G_{B-1},
\]
\[
E_{A,B}=3^BE_A+2^AT_B-
2^A3^B\sum_{i<A,j<B}\eta_{i,j}2^{-i}3^{-j}.
\]
Every last sum is a finite rational number. The identities include their low-cutoff atoms because the Mellin integration starts at zero. In particular, \(G_0=0\) yields \(T_1=0\), but \(T_2\) has an actual exterior atom at \(1/3\) from \(\eta_{0,1}=1\). The first free row therefore does not propagate to later rows. — [HB8–HB9](hierarchy_boundary.md), [independent mixed-filter checks](hierarchy_boundary_audit_check.py).

### Gaps

- Triangularity does not mean the actual profile numbers are linearly independent.
- These identities do not exclude additional dynamical information; they only show that full-potential rationality has not supplied it. — [Audited scope](hierarchy_boundary.md).

## Does the complete hierarchy dictionary include every side and low row?

### Takeaway

**PASS.** The displayed integer dictionary reconstructs the complete numerator \(81\Pi L_0+B_P(d)\), including all four low rows. Its coefficients expose the arithmetic still needed; they do not prove the actual constants independent or irrational. — [HB10–HB13](hierarchy_boundary.md), [retained hierarchy HA1–HA10](../hybrid-arithmetic-closure/hierarchy_absorption.md).

### Cited Findings

- With \(c_{a,b}=1-3\eta_{a,b}\) and \(d(a,b)=c_{a,b+4}\), the boundary of a shift \((A,B)\) is \(2^A3^B(H_A+V_B-R_{A,B})\). The low contribution must be added as \(81\Pi L_0\). — [HA1–HA3 and HA10](../hybrid-arithmetic-closure/hierarchy_absorption.md).
- The independent checker extracts column and row coefficients from far-tail kernel values, then verifies their finite residual against the claimed corner formula on a nontrivial three-factor operator and actual finite-board coefficients. It does not use the companion coefficient routine. — [Independent three-factor reconstruction](hierarchy_boundary_audit_check.py).

### Inferences

For \(P=\sum r_{A,B}X^AY^B\), write
\[
U_i=\sum_b c_{i,b}3^{-b}=\frac32-3F_i,\qquad
V_j=\sum_a c_{a,j}2^{-a}=2-3G_j.
\]
Expanding the horizontal strip gives
\[
H_A(d)=81\sum_{i<A}2^{-i}U_i
-81\sum_{i<A,j<4}c_{i,j}2^{-i}3^{-j};
\]
the vertical strip gives \(\sum_{k<B}3^{-k}V_{k+4}\). Substitution yields exactly HB10–HB12, including both negative finite corrections. The integer assertions are valid termwise: the relevant multipliers contain \(2^{A-i}3^{B+4-j}\) or \(2^{A-i}3^{B-k}\), with nonnegative integer exponents in every stated range. Absolute convergence justifies the infinite profile regrouping. — [Dictionary formulas and proof](hierarchy_boundary.md).

For the product of the three-term positive hierarchy operators, the all-horizontal monomial uniquely supplies
\(\alpha_{A_{\max}-1}=162\), and the all-vertical monomial uniquely supplies \(\beta_{B_{\max}+3}=3\). Every profile coefficient in the displayed ranges is positive. The only absorbed row is \(V_0=2\), whose term is \(162\Pi\). Hence the formal remaining dictionary is
\[
U_0,\ldots,U_{A_{\max}-1},
\qquad V_1,\ldots,V_{B_{\max}+3}.
\]
The independent kernel residual vanishes outside the finite corner, so no infinite tail was silently included in the integer correction. Its actual finite-array test is a certificate of this identity, not a numerical evaluation of the unknown infinite profiles. — [HB13](hierarchy_boundary.md), [independent coefficient and corner checks](hierarchy_boundary_audit_check.py).

### Gaps

- No fixed rational lattice or cheap common denominator for this complete actual profile combination is established.
- Signed residual nonvanishing remains separate.
- Validation: the supplied checker and independent checker both pass; no substantive erratum was found. Skipped Lean, outside literature, installations and broader exploration. The material risk is treating formal profile bookkeeping as arithmetic closure. — [Supplied checker](hierarchy_boundary_check.py), [independent checker](hierarchy_boundary_audit_check.py).
