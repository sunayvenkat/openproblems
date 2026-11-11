# Independent audit of adaptive coupling witnesses

## Does the buffered witness define the claimed complete rational coupling and actual optimal head?

### Takeaway

**PASS; no substantive errata found.** The 32 weights, unit marginals, balanced repairs, complete cost and all 80 head events reconstruct exactly. This is one complete rational example, not an infinite arithmetic return. — [Construction](adaptive_capacity.md), [supplied checker](adaptive_capacity_check.py), [independent checker](adaptive_witness_audit_check.py).

### Cited Findings

- Both supplied checkers pass under Python 3.14 with bytecode disabled. The independent checker imports no companion functions: it reads only certificate constants using literal evaluation, generates its own 28-vector/118-shape palette and 4248 anchored types, and uses doubled integer arrival times, retaining \(27/2\) exactly. — [Independent methods](adaptive_witness_audit_check.py).
- Every residue node receives total numerator seven, and the active numerators sum to 84. The corner and bottom/left root blocks at \(A=18,B=12\) have per-color numerators 239, 50 and 52. Clipped residual numerators are nonnegative and at most seven. — [Independent marginal checks](adaptive_witness_audit_check.py).
- The recovered complete cost and safe clearing factor are
  \[
  Q=\frac{20605867009283}{34511190884352},\qquad
  D=2086759741982823677952
   =7(63\cdot728\cdot2^6 3^6)2^{18}3^{12},
  \quad DQ\in\mathbb Z.
  \]
  All buffers and infinite tails are included. — [Independent complete sum](adaptive_witness_audit_check.py), [AC2–AC3](adaptive_capacity.md).
- Direct enumeration of actual weighted completed triples agrees with \(\tau\) at all 80 events through \(2^{16}\); the first deficit is one at 73728. This independent test sums completion events instead of reusing the supplied component-minimum implementation. — [Independent head replay](adaptive_witness_audit_check.py).

### Inferences

The normalization makes containment equivalent to nonnegative minimum anchors. Plane residue coverage gives unit marginals; clipping leaves residual mass only in \(a<8\) or \(b<5\). The corner and all bottom/left periods partition it. Outside both cuts the residual is zero.

The independent repair expands each numerator into clones of mass \(1/7\), sorts each color by actual arrival and zips equal ranks. This differs from the supplied interval-overlay algorithm and consumes all component mass once. Bottom groups repeat with factor 64, left groups with 729. For each bulk root, the independent sum partitions anchors into the actual root, horizontal continuation with geometric factor \(64/63\), and positive vertical continuation with factor \((64/63)(729/728)\). The latter has no low-row delays; horizontal continuation is in the stabilized dyadic regime. These disjoint classes exhaust the infinite anchor quadrant. — [Independent stream and clone construction](adaptive_witness_audit_check.py), [full repair definitions](adaptive_capacity.md).

### Gaps

- Strictness \(Q<M\) uses the accepted positive-dispersion theorem, audited in the separate arithmetic branch. No infinite weight/head sequence or shrinking denominator-cleared errors is constructed. The safe factor is not a reduced-denominator lower bound. — [AC5 and open target](adaptive_capacity.md), [arithmetic extension](adaptive_arithmetic.md).

## Do the obstruction certificates cover the full palette and correct head hypothesis?

### Takeaway

**PASS.** All 4248 original types are covered by actual zero-surplus bans or the explicit 42-row balance dual. The 729 argument is correctly conditioned on support restrictions from the entire \(2^{16}\) head. — [AC6–AC8](adaptive_capacity.md), [independent replay](adaptive_witness_audit_check.py).

### Cited Findings

- Independent physical-triangle/zero-event interval tests leave exactly 339 types through \(2^{16}\) and 165 through \(2^{17}\). Each eliminated type has an arrived minimum-color vertex before its completion. No positive-surplus integer-only exclusion is used. — [Independent zero-event test](adaptive_witness_audit_check.py).
- Rebuilding all coverage and component-balance equations gives the integer multiplier vector \(y\) with
  \[
  y^Tb=83,\qquad (y^TE)_k\le0
  \quad\text{for every surviving }k.
  \]
  Thus \(Ex=b,x\ge0\) would imply \(83\le0\). Valid bans handle every omitted original column. — [Independent 42-row reconstruction](adaptive_witness_audit_check.py).
- Under the full \(2^{16}\) support restriction, none of the 339 types covers \((0,6)\) by a contained bulk triangle. At 729 the minimal-cut left component has \(C_0=1,C_1=0\), while color zero is a global minimum. — [Independent incidence and count checks](adaptive_witness_audit_check.py).

### Inferences

Minimum-color arrived mass cannot be reserved in an incomplete retained triangle if head equality is to hold. The bans therefore apply to arbitrary nonnegative real weights without an optimizer. On the remaining support, the integer dual contradicts the exact marginal/balance equations.

The 729 argument reasons backward from constraints throughout the longer head; it does not locate the first infeasibility threshold of the unrestricted minimal-cut class. The buffered positive witness confirms that changing the component decomposition matters. — [Precise model qualifiers](adaptive_capacity.md).

### Gaps

- The negative certificate concerns this 118-shape period-six balanced decomposition at the stated cuts. Larger palettes, different periods, cut phases or mixed-component repairs are not excluded. No infinite infeasibility theorem follows. — [Finite certificate scope](adaptive_capacity.md).

## Are the trades, forced-reset arguments and convergent counterexample sound?

### Takeaway

**PASS.** The 43-triple finite head and zero-cost exchange are genuine. Balanced resets force the specified triples and corner-support bounds. The \(306/485\) example correctly breaks automatic extrapolation from four smaller balanced progressions. — [Structural proofs](adaptive_structure.md), [supplied checker](adaptive_structure_check.py), [independent checker](adaptive_witness_audit_check.py).

### Cited Findings

- The independent checker stores the 43-triple witness directly, verifying 129 distinct tokens, one of each color per triple, spans at most \(8\times5\), ten normalized shapes and coverage of the first 43 tokens of each color. Every actual event count through \(2^{19}\) equals its completed count. It does not rerun the matching search. — [Independent fixed certificate](adaptive_witness_audit_check.py).
- The alternating trade uses the same nine tokens and preserves individual completion times 27648, 36864 and 41472, hence preserves both the completed-count function and cost. — [Independent trade assertions](adaptive_witness_audit_check.py), [AS1](adaptive_structure.md).
- Independent reset enumeration reproduces the statistics \((161,29,53,34)\) for box \(27,17\) and \((1420,82,168,96)\) for box \(84,53\): singleton balanced bursts, oversized bursts and necessary corner bounds. — [Independent enumeration](adaptive_witness_audit_check.py), [AS3–AS4](adaptive_structure.md).
- Exact integer-power comparisons independently certify the ordinary convergents through \(665/1054\). A separate row-count formula verifies all five progression states without a large event sort. For \(q=485,p=306\), it obtains
  \[
  (99852,99851,99852)\longrightarrow(99853,99852,99853).
  \]
  Exactly three arrivals occur, but neither endpoint is balanced; \(1054>2\cdot485\) does not repair that failure. — [Independent exact CF and row counts](adaptive_witness_audit_check.py).

### Inferences

If all three arrived counts equal \(k\), optimality consumes all earlier mass. A later balanced count \(k+1\) leaves exactly three new tokens with no old mass available. Optimality at that endpoint forces those three together with mass one, including for fractional couplings.

A forced triple exceeding the bulk box cannot be a bulk triple. Horizontal and vertical spans at least six exclude six-wide bottom and six-high left repair blocks. Within this architecture it must fit the corner, yielding the stated bounds \(A\ge53,B\ge34\) and \(A\ge168,B\ge96\). These are support necessities, not reduced-denominator bounds.

The 485 progression retains unmatched surplus, so three consecutive new arrivals need not be matched together. This counterexample invalidates automatic balanced-return extrapolation without proving infinitely many favorable or unfavorable states. — [AS3–AS4 and counterexample](adaptive_structure.md).

### Gaps

- The 43-triple certificate is a finite partial matching, not a periodic whole-plane extension or cheap rational infinite cost. The separate S7 construction supplies a full rational cost with the shorter head. Some traded shapes rely on low-row retimings and cannot be vertically repeated on that basis alone. — [Structural scope](adaptive_structure.md).
- Infinite adequate returns and irrationality remain unproved. Lean, external review, installations, broad scans and archived edits were skipped. Material risk: promoting finite optimality or support necessities to universal or arithmetic impossibility claims. — [Remaining objective](../fractional-farey-transport/REPORT.md).
