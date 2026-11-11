# Independent weighted response shift audit

## Are the complete shift and polynomial boundary formulas correct?

### Takeaway

**PASS; no substantive correction.** WC1–WC3 are exact absolutely convergent identities. They expose complete infinite strips and the separate low rows; they do not evaluate those profiles arithmetically. The supplied checker and the new standalone checker both pass. — [Claimed formulas](weighted_closure.md), [supplied checker](weighted_closure_check.py), [independent checker](weighted_audit_check.py).

### Cited Findings

- The accepted five arrays are the original target (f_0=c) and the four canonical actual responses (f_1,ldots,f_4=g_R). Their full weighted values are respectively (Z) and (G_R); all coefficients have absolute value at most three. The target retains its exceptional origin birth, whereas the reindexed responses do not acquire one. — [Accepted definitions RR1–RR3](../response-closure-tests/response_relations.md), [earlier independent reconstruction](../response-closure-tests/response_audit.md).
- The new independent checker imports no archived or companion calculation. It reconstructs the axes from the original colored-board counts at (2^a) and (3^b), the target from the exact finite-cover theorem, and the responses from the accepted canonical endpoints using minimum differences rather than the supplied inequality tests. All rank and weighted calculations use integers or `Fraction`. — [Independent implementation](weighted_audit_check.py), [proved finite theorem](../prefix-and-phase-audit/REPORT.md).

### Inferences

For a bounded array (|f|le M), write

\[
W(f)=\sum_{a\ge0,b\ge4}f(a,b)2^{-a}3^{-b}.
\]

The total weight of this domain is (1/27), so (|W(f)|\le M/27). Consequently every reindexing and finite linear combination used below is absolutely convergent. — [WC1 definitions](weighted_closure.md).

For (u,v\ge0), substitute (i=a+u,k=b+v). This gives

\[
W(S_a^uS_b^vf)
=2^u3^v\sum_{i\ge u,k\ge4+v}f(i,k)2^{-i}3^{-k}.
\]

The missing complement is the union of (i<u,k\ge4) and (i\ge0,4\le k<4+v); their intersection is exactly the finite corner. Therefore

\[
W(S_a^uS_b^vf)=2^u3^v\bigl(W(f)-C_u(f)-R_v(f)+K_{u,v}(f)\bigr).
\tag{A1}
\]

This confirms both zero-shift cases and the factors. In particular, with (V_i(f)=\sum_{b\ge4}f(i,b)3^{-b}) and (H_k(f)=\sum_{a\ge0}f(a,k)2^{-a}),

\[
W(S_af)=2W(f)-2V_0(f),\qquad
W(S_bf)=3W(f)-H_4(f)/27.
\tag{A2}
\]

The factor (1/27) in the second formula is (3\cdot3^{-4}), not a dropped row. — [Claimed WC1–WC2](weighted_closure.md), [independent exact finite-supported verification](weighted_audit_check.py).

For (P(X,Y)=\sum\lambda_{u,v}X^uY^v), summing A1 gives bulk coefficient (P(2,3)). The vertical profile (V_i) occurs precisely when (u>i), with coefficient

\[
-2^{-i}\sum_{u>i,v}\lambda_{u,v}2^u3^v.
\]

Likewise (H_{4+\ell}) occurs precisely when (v>\ell), with coefficient

\[
-3^{-(4+\ell)}\sum_{u,v>\ell}\lambda_{u,v}2^u3^v.
\]

The remaining term is (\sum\lambda_{u,v}2^u3^vK_{u,v}), a finite rational sum for integer (f) and rational (P). This reconstructs WC3 exactly. It also proves that setting (P(2,3)=0) removes the bulk but does not remove its infinite boundary profiles. — [WC3](weighted_closure.md), [independent test using a nonseparable rational polynomial](weighted_audit_check.py).

Finally (L(f)=\sum_{a\ge0,0\le b<4}f(a,b)2^{-a}3^{-b}) has (|L(f)|\le80M/27), and the full weighted value is exactly (W(f)+L(f)). Four rows have finite width in the (b) direction, but still infinitely many (a) terms. Thus (W(c)=Z-L(c)) and (W(g_R)=G_R-L(g_R)) do not replace these low rows by rational constants. — [Complete low-row rules](../response-closure-tests/response_relations.md), [independent low-row split check](weighted_audit_check.py).

### Gaps

- No arithmetic evaluation of the actual strip or low-row values follows from A1–A2 or WC3. Rationality of (Z) has not been proved to rationalize these summands. — [Accepted boundary arithmetic gap](../signed-arithmetic-returns/hierarchy_boundary_audit.md).
- These formulas do not rule out an evaluation-specific cancellation of their complete boundary terms. — [Scope of the new claim](weighted_closure.md).

## Do the two exact rank certificates reconstruct independently?

### Takeaway

**PASS.** Both claimed full determinants reproduce from independently reconstructed actual entries, using ordinary exact rational Gaussian elimination rather than the supplied modular row selection and fraction-free determinant routine. The resulting obstructions have precisely their stated pointwise scope. — [Independent checker](weighted_audit_check.py), [supplied determinant certificate](weighted_closure_check.py).

### Cited Findings

- For the constant and all eighty shifts (f_j(a+u,b+v)), (j=0,ldots,4), (0\le u,v\le3), the claimed (81\times81) determinant is
  \[
  8649772697327523432457189461277550575610520.
  \]
  The independent checker reconstructs every entry on the published row set from original-board axes and minimum-difference response tests and obtains exactly this integer. — [Row specification and claim WC4](weighted_closure.md), [independent calculation](weighted_audit_check.py).
- For the constant and forty-five shifts with (u,v\in\{0,3,6\}), the claimed (46\times46) determinant is
  \[
  -259979518176473365480584.
  \]
  It too reproduces exactly on the supplied witness rows, whose list is hard-coded in the independent checker. — [Color-preserving claim](weighted_closure.md), [independent calculation](weighted_audit_check.py).
- The original supplied checker also passes both exact determinants and all its finite-supported shift tests. The independent checker additionally checks the complete polynomial profile coefficients and the separation of full, high and low weighted contributions. — [Supplied checker](weighted_closure_check.py), [independent checker](weighted_audit_check.py).

### Inferences

An everywhere pointwise rational relation in either claimed finite shift class would give a nonzero rational kernel vector for its displayed evaluation matrix. Since the determinant is nonzero, no such relation exists. This is a valid finite certificate against an asserted everywhere identity; it is not an extrapolation from finitely many observed values. — [WC4 and block obstruction](weighted_closure.md), [independent determinants](weighted_audit_check.py).

The witnesses include boundary-adjacent indices (a=0,1). Accordingly this audit does not strengthen the theorem to an eventual identity class outside an arbitrary finite region. Nor does finite pointwise independence entail independence after applying the single linear functional (W). Its kernel can contain nonzero arrays, and a weighted-value identity need not be a coefficientwise identity. — [Explicit limitations of the claimed theorem](weighted_closure.md).

### Gaps

- Longer filters, state-dependent coefficients, eventual identities and weighted numerical relations remain outside the proved rank claims. — [Scope limitations](weighted_closure.md).
- No irrationality or algebraic independence of (Z,G_R), or of any boundary profiles, has been proved by these determinants. — [Existing response arithmetic gap](../response-closure-tests/response_relations.md).

## What is the final audit disposition for the infinite-return goal?

### Takeaway

**PASS for WC1–WC4 in their stated scope; no adequate infinite arithmetic return is obtained from this component.** There is no substantive audit erratum. The exact dictionary clarifies which infinite boundary values a more sophisticated closure must evaluate or cancel, and the two finite rank certificates exclude only the tested pointwise routes. — [Audited notes](weighted_closure.md), [independent checker](weighted_audit_check.py).

### Cited Findings

- The completed finite cover theorem remains an input, and the four canonical response definitions remain the previously audited input. This audit checks their use in the new shift and rank claims, not a new proof of the whole combinatorial foundation. — [Finite proof](../prefix-and-phase-audit/REPORT.md), [canonical response audit](../response-closure-tests/response_audit.md).
- Both supplied and independent scripts finished successfully. The independent script uses no companion imports and no floating arithmetic, and touches no archived work. — [Independent certificate](weighted_audit_check.py), [supplied certificate](weighted_closure_check.py).

### Inferences

- Arithmetic closure remains a genuine separate obligation. Neither the new stronger nonvanishing result researched in parallel nor rationality of the target evaluates the profiles appearing in WC3 without a further proved identity. — [Boundary dictionary and open interface](weighted_closure.md).
- A numerical weighted coboundary remains possible only as an unproved lead here; no proposed infinite boundary cancellation has been accepted silently. — [Scope and gaps](weighted_closure.md).

### Gaps

- Skipped: larger searches, independent reproof of the archived finite theorem, Lean and external review. Material risk: promoting the finite pointwise obstruction to a prohibition on weighted special-value identities or all arithmetic returns. — [Audited scope](weighted_closure.md).
