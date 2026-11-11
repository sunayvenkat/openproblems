# Actual weighted responses and complete shift boundaries

## Can shifts turn the four responses into an arithmetic identity for Z?

### Takeaway

No value-level arithmetic closure was found. Exact reindexing gives a useful complete boundary dictionary: every horizontal or vertical shift exposes an infinite actual profile, and the original rationality hypothesis does not currently evaluate those profiles. The formula below is a proved identity for the actual arrays, with every low row and infinite strip retained. — [Accepted actual responses](../response-closure-tests/response_relations.md), [exact checker](weighted_closure_check.py).

### Cited Findings

- The target array is (f_0(a,b)=c_{a,b}=1-3\eta_{a,b}\), and (f_j=g_j\), (1\le j\le4\), are the four canonical actual response arrays. They are integer-valued and bounded in absolute value by three. The target weighted value is (Z=9c-6\), while the four other full weighted values are (G_j\). Their complete low-row rules are part of their definitions. — [RR1–RR5](../response-closure-tests/response_relations.md).
- The earlier determinant243 only excludes direct same-index affine coefficient closure. It is not independence of weighted numerical values. — [RR6 and limitations](../response-closure-tests/response_relations.md).
- The full hierarchy dictionary already retains unknown one-dimensional row and column profiles. Rationality of the whole potential does not by itself rationalize its summands. — [Complete boundary audit](../signed-arithmetic-returns/hierarchy_boundary_audit.md).

### Inferences

**WC1. Complete weighted shift identity.** For any bounded integer array (f\), define
\[
W(f)=\sum_{a\ge0,\ b\ge4}f(a,b)2^{-a}3^{-b},\qquad
S_a^uS_b^vf(a,b)=f(a+u,b+v),
\]
and, for nonnegative integers (u,v\),
\[
\begin{aligned}
C_u(f)&=\sum_{0\le a<u,\ b\ge4} f(a,b)2^{-a}3^{-b},\\
R_v(f)&=\sum_{a\ge0,\ 4\le b<4+v} f(a,b)2^{-a}3^{-b},\\
K_{u,v}(f)&=\sum_{0\le a<u,\ 4\le b<4+v}f(a,b)2^{-a}3^{-b}.
\end{aligned}
\]
Then
\[
\boxed{W(S_a^uS_b^vf)=2^u3^v\bigl(W(f)-C_u(f)-R_v(f)+K_{u,v}(f)\bigr).}
\tag{WC1}
\]
Proof: substitute (i=a+u,k=b+v\) in the left sum, multiply its weights by (2^u3^v\), and use inclusion–exclusion on the two missing strips. Absolute convergence justifies the substitutions. The corner is finite and rational; the two strips remain infinite. The checker independently tests the exact formula on finite-supported restrictions of all five actual arrays for all (u,v\in\{0,1,3,6\}\). That test verifies boundary conventions; the displayed substitution proves the infinite identity. — [Checker](weighted_closure_check.py).

For single shifts this becomes particularly transparent. Write
\[
V_i(f)=\sum_{b\ge4}f(i,b)3^{-b},\qquad
H_k(f)=\sum_{a\ge0}f(a,k)2^{-a}.
\]
Then
\[
W(S_af)=2W(f)-2V_0(f),\qquad
W(S_bf)=3W(f)-H_4(f)/27.
\tag{WC2}
\]
Thus even the simplest reindexing is not a relation among (Z,G_1,\ldots,G_4\) alone. It adds an actual axis series. Neither term in WC2 is being put into a finite rational corner. — [Definitions and arithmetic profile gap](../signed-arithmetic-returns/hierarchy_boundary_audit.md).

**WC2. Exact polynomial dictionary.** If (P(X,Y)=\sum_{u,v}\lambda_{u,v}X^uY^v\) is any finite rational polynomial, define
\[
A_i=\sum_{u>i,v}\lambda_{u,v}2^u3^v,\qquad
B_\ell=\sum_{u,v>\ell}\lambda_{u,v}2^u3^v.
\]
Summing WC1 gives
\[
\boxed{
W(P(S_a,S_b)f)=P(2,3)W(f)
-\sum_i2^{-i}A_iV_i(f)
-\sum_\ell3^{-(4+\ell)}B_\ell H_{4+\ell}(f)
+\sum_{u,v}\lambda_{u,v}2^u3^vK_{u,v}(f).
}
\tag{WC3}
\]
All sums other than the explicitly defined profiles are finite. The last sum is rational. WC3 describes the boundary arithmetic that must be proved or cancelled in a proposed shifted closure; it supplies no unproved rationality of those profiles. — [WC1 checker](weighted_closure_check.py), [accepted profiles and low rows](../response-closure-tests/response_relations.md).

To return from (W\) to the full weighted values, define
\[
L(f)=\sum_{a\ge0,\ 0\le b<4}f(a,b)2^{-a}3^{-b}.
\]
Exactly (W(f_0)=Z-L(f_0)\) and (W(g_j)=G_j-L(g_j)\). Although there are only four low rows, each has infinitely many horizontal terms. The original target retains its exceptional origin birth; the response arrays do not acquire one. Consequently a shift argument must pay both the WC3 profiles and these low-row values. — [Full canonical definitions and low-row ray dictionary](../response-closure-tests/response_relations.md).

### Gaps

- No relation (G_j\in\mathbb Q+\mathbb QZ\), and no sufficient rational boundary combination under (Z\in\mathbb Q\), was established. WC1–WC3 are an exact reindexing interface, not an arithmetic evaluation.
- A value-specific identity could still cancel the infinite profiles. The results below do not exclude it.

## Do short actual shifted coefficient identities supply that closure?

### Takeaway

Two exact integer determinants rule out the simplest proposed pointwise filters, including shifts through one full color period. These are scoped coefficient obstructions only: they do not prove rational independence, irrationality, or a prohibition on numerical weighted coboundaries. — [Determinants and independent target entries](weighted_closure_check.py).

### Cited Findings

- The checker reconstructs actual floors by integer comparisons, computes the actual axis recurrences and complete response tests, and independently checks every target coefficient used against original colored-board counts and exceptional-root corrections. All calculations use integers and exact fractions, not floating-point rank. — [Checker](weighted_closure_check.py), [accepted axis definitions](../boundary-and-arithmetic/arithmetic.md), [completed finite theorem superseding old conditional language](../prefix-and-phase-audit/REPORT.md).
- Modular elimination is used only to select independent rows. Fraction-free integer elimination then computes the complete determinant exactly and asserts its displayed value. — [Checker](weighted_closure_check.py).

### Inferences

**WC3. Unit-shift box obstruction.** There are no rational coefficients, not all zero, satisfying
\[
\lambda_0+\sum_{j=0}^{4}\sum_{u=0}^{3}\sum_{v=0}^{3}
\lambda_{j,u,v}f_j(a+u,b+v)=0
\quad\text{for every }a\ge0,b\ge4.
\tag{WC4}
\]
The constant and eighty shifted arrays have an (81\times81\) evaluation matrix with determinant
\[
8649772697327523432457189461277550575610520\ne0.
\]
The row set is compactly specified by
\[
\begin{aligned}
&(0,b),\quad b\in[4,39]\cup[51,54]\cup[60,80],\\
&(1,b),\quad b\in[4,14]\cup\{17\},\\
&(2,b),(3,b),\quad b\in\{4,5,11,12\}.
\end{aligned}
\]
Intervals here mean inclusive integer ranges. If WC4 held, evaluation on these rows would give a nonzero vector in the kernel of an invertible rational matrix, a contradiction. This is a proof for the specified entire-domain pointwise identity class, using finite counter-certificates; it is not extrapolation of a finite nullspace. — [Exact determinant certificate](weighted_closure_check.py).

**WC4. Color-preserving block obstruction.** The analogous constant plus forty-five arrays with (u,v\in\{0,3,6\}\) have rank46 and integer determinant
\[
-259979518176473365480584\ne0.
\]
Therefore there is no nontrivial constant-coefficient pointwise identity in that second specified class either. Its exact row set is emitted by the checker. These shifts preserve both color residues and test a natural two-block recurrence beyond the smaller box. — [Exact determinant certificate](weighted_closure_check.py).

The interpretation is narrow. A derivation that first seeks one of these pointwise relations, then sums it using WC3, cannot work. The result says nothing about a longer filter, coefficients depending on mechanical-word phases, an identity valid only after an arbitrary finite prefix, or an identity arising only at weights ((1/2,1/3)\). In particular it does not establish independence of (Z,G_j\) or of any boundary-profile values.

### Gaps

- The actual special value relation required for cheaper arithmetic remains open.
- No eventual pointwise identity is excluded: finite witnesses near the boundary cannot disprove a relation asserted only outside a sufficiently large finite region.
- No impossibility theorem for arbitrary combined arithmetic returns follows from WC3 or WC4.

## What does this change in the infinite return problem?

### Takeaway

The search can now bypass the two tested short pointwise-filter classes, while retaining an exact formula for every boundary term of a more sophisticated proposal. A new arithmetic identity must evaluate or cancel actual infinite profiles; index shifting alone supplies no such evaluation. The original infinite-return objective remains open. — [Current accepted frontier](../response-closure-tests/REPORT.md), [new exact certificates](weighted_closure_check.py).

### Cited Findings

- The four fixed coefficients give the analytic error expansion, but their rationality under target rationality is unproved. A stronger separate nonvanishing argument does not change that arithmetic distinction. — [RR7–RR8 and gaps](../response-closure-tests/response_relations.md).
- This work proves WC1–WC4 and tests their concrete certificates; it constructs no cheaper adequate infinite sequence and asserts no actual favorable-state frequency. — [Checker and formulas above](weighted_closure_check.py).

### Inferences

- A promising remaining closure mechanism would need either a genuinely value-specific cancellation of the WC3 profiles or a nonlocal state identity with a separately proved arithmetic evaluation. The finite rank test does not adjudicate either mechanism.
- Repeated-state elimination of a shared (G_j\) can be studied without assuming it rational, but its integer coefficients and scalar-model denominator costs must still be charged. That is the neighboring arithmetic research task, not a conclusion of this note.

### Gaps

- No irrationality proof or adequate infinite arithmetic return is claimed.
- Skipped: larger coefficient searches, Lean, installations, external review and priority checks. Material risk: confusing a pointwise filter obstruction with independence of weighted actual values, or confusing finite strip width with finite support.
