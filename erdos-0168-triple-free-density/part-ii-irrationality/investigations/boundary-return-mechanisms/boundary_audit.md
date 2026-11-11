# Independent audit of boundary exchange mechanisms

## Are the repeated exchange and both-axis compression valid?

### Takeaway

**PASS; no substantive erratum found.** The full three-triple exchange preserves actual completion times on every nonnegative period-six translate. The parameterized reverse exchange compresses each coordinate span by at least one seventh, but this is a local geometric statement. — [Audited proof](boundary_exchange.md), [independent certificate](boundary_audit_check.py).

### Cited Findings

- The supplied checker passes under Python 3.14 with `-B`. The independent checker imports no companion code: it uses doubled integer arrival times, integer masses in ninths, actual-event jumps for finite rank costs, and independently constructed root streams. Both reconstruct all three charged parameterized examples. — [Supplied checker](boundary_exchange_check.py), [independent checker](boundary_audit_check.py).
- The seed families use exactly the same nine points, each triple contains all three colors, and all nine residue pairs modulo six are distinct. Their three ordinary maxima are the same three ordinary points, with times `27648, 36864, 41472`. The special low-row retimings do not overtake those maxima. — [Seed definitions and assertions](boundary_exchange_check.py), [independent integer-time assertions](boundary_audit_check.py).
- Independent replay recovers span compressions `(37,24)->(26,17)`, `(227,143)->(181,114)`, and `(623,393)->(474,299)`, with common parent/child charged cuts `(60,36,1)`, `(348,222,1)`, and `(888,564,1)`. The last entry is the donor-period count. — [Independent mapped certificates](boundary_audit_check.py).

### Inferences

**A1. The infinite substitution follows from finite inequalities, not extrapolation.** At vertical index zero, every horizontal translation preserves the factors on the exceptional seed rows. At every positive vertical index, all seed points are ordinary. Since the ordinary maxima are already the actual maxima at the initial seed, the two complete translated families have the same three completion times at every index. Distinct residue pairs make different translated blocks disjoint. Replacing the three parent triples therefore preserves all token marginals, every completed-count value, and the full cost. — [BE1–BE2](boundary_exchange.md).

For a physical linear functional `(a,b)->a*x+b*y`, the desired fixed maxima dominate every old and new partner throughout `3/2<=y/x<=8/5`. Every comparison is affine in the ratio, so checking both interval endpoints proves the whole interval. The independent certificate performs exactly that endpoint proof. — [Independent cone certificate](boundary_audit_check.py).

**A2. The matrix step covers the entire required cone.** After choosing the dominant physical column error and its sign, the transformed errors have the form

\[
x=E(9+2t),\qquad y=E(14+3t),\qquad E>0,\quad -1\le t\le1.
\]

Hence both are positive and `17/11<=y/x<=11/7`, inside the maximum-preserving cone. The determinants of the two integer matrices are `-1` and `1`. Their action on the color row is multiplication by a common sign, and their invertibility modulo six preserves all nine distinct residue pairs. This argument does not need the original physical errors to have opposite signs. — [BE3](boundary_exchange.md).

The two entries of either *coordinate row* have absolute ratio `rho` in `[3/2,14/9]`, a different interval from the physical-error ratio. On this narrower interval, direct pairwise affine comparisons give

\[
\max\operatorname{span}(P)=|c_1|(3\rho-4),\qquad
\max\operatorname{span}(R)=|c_1|(7-4\rho).
\]

The displayed bound for `P` is attained in its first triple; the bound for `R` is attained in its third. Thus the maxima formulas hold throughout the interval, not only at sampled ratios. The inequality `7(3rho-4)<=6(7-4rho)` holds at both endpoints and therefore everywhere. It proves the reverse compression `R->P` on each axis. — [Independent affine span certificate](boundary_audit_check.py), [BE3](boundary_exchange.md).

Translation by multiples of six places the mapped seed above row one, with nonnegative first coordinates. Thus the parameterized construction uses ordinary arrivals everywhere; it does not transport the old exceptional timing rules through an arbitrary lattice map. — [Mapped construction](boundary_exchange.md).

### Gaps

- No useful infinite parent family with a sufficiently long actual optimal head is supplied. A zero-cost substitution preserves an existing head; it does not extend that head. — [BE1 and stated gaps](boundary_exchange.md).
- The reduced denominator of a fixed rational cost is invariant under these substitutions. No arithmetic improvement follows solely from the smaller individual spans. — [Complete embedding and limits](boundary_exchange.md).

## Are moment averaging, clipped flux and the complete rational repair correct?

### Takeaway

**PASS.** The moment argument has the needed initially balanced zeroth masses, and the floor-coordinate calculation gives exact edge capacities and corner masses. The complete repaired cost and every donor/crossover-free geometric tail reconstruct independently. — [BE4–BE6](boundary_exchange.md), [independent complete-cost replay](boundary_audit_check.py).

### Cited Findings

- All 36 residue nodes have weighted plane coverage one. Each color has twelve root-point units before averaging. Averaging shifts `0,1,2` twice gives integer multiplicities `1,2,3,2,1` over denominator nine. Independent assertions check `1,a,b,a^2,ab,b^2` moment equality across all colors for both fixed and transformed root families. — [Independent root and moment reconstruction](boundary_audit_check.py).
- The independently recovered cost and safe clearing factor are

\[
Q=\frac{357544920809}{704310018048},\qquad
D=125176966099650799095250944,
\]

with cuts `A=24,B=12` and one donor period. `D*Q` is an integer. — [Independent complete-cost assertion](boundary_audit_check.py).
- The reconstructed completed mass at time three is `7/9`, while the optimal count is one. The child root selection still leaves residual mass `1/9` at `(8,6)`. — [Independent critical-time and clipping assertions](boundary_audit_check.py).

### Inferences

**A3. The second-horizontal-moment statement has its required hypothesis.** Equal initial root counts make the first averaging operation balance both first moments. A second averaging balances the horizontal square because its cross terms involve already balanced first moments and zeroth counts. The vertical square is balanced by color cycling; the mixed moment uses the balanced first vertical moment. Thus the order-two averaging multiplier is sufficient here. It would not balance the horizontal square of an arbitrary initially unbalanced collection. The final proof states this qualification explicitly. — [BE4](boundary_exchange.md).

**A4. The exact floor formula is not a moment heuristic.** For each root write `a=6I+u,b=6J+v`, with residues between zero and five, and choose `A=6N,B=6M` strictly above all root coordinates. Unit residue coverage gives weighted residue sums `sum u=sum v=30` separately in each color. First-moment balance therefore makes `sum I=n` and `sum J=h` color-independent. Directly subtracting covered root rectangles from the `12NM` raw points per color gives

\[
c_j=M n+N h-\sum_{\text{color }j}wI J.
\]

This is independently replayed by counting covered copies of each root in the actual finite rectangle, rather than by importing the source formula. Expanding `IJ=(ab-av-ub+uv)/36` cancels the equal `ab` moments in color differences. The remaining nonnegative bounded residue terms give the stated range bound `5(R_a+R_b+5)/3`. — [Independent direct-rectangle comparison](boundary_audit_check.py), [BE5](boundary_exchange.md).

**A5. The uniform donor bound is numerically justified.** Put `L=q+s` and assume `p+r<=L`. The mapped block has width `11q+2s` or `2q+11s` before the constant averaging shifts. Hence its width is at least `2L`, while the final root extents are at most `11L+9` and `11L+7`. Equal first moments imply

\[
n\ge L/9-5.
\]

For `L>=180`, this is at least `L/12`. The corner range is at most `(110/3)L+35`, so its ratio to `n` is at most `440+420/L<443`; the declared ceiling bound `500` is safe. The three finite examples have their positive capacities and single donor period checked directly. No claim about all unspecified small bases is needed. — [BE5](boundary_exchange.md), [independent mapped checks](boundary_audit_check.py).

**A6. The repair covers every residual unit exactly once.** Every physical residue has total plane root weight one, so keeping the nonnegative root-index quadrant leaves a nonnegative residual. Outside the charged corner, residuals split into a bottom strip periodic horizontally and a left strip periodic vertically. The first `d_j=max c-c_j` units in the left list balance the corner; the remaining lists are zipped in residual mass order. All masses and all splits stay in ninths. After one common list period, all three partners shift vertically by six, giving the exact factor `729/728`. Bottom periods give `64/63`. The finite head, donor shifts, root exceptions and both infinite bulk continuations are therefore included in

\[
D=9\cdot63\cdot728\,2^{A+6}3^{B+6J_0+6}.
\]

The independent cost checker evaluates finite balanced rank costs by actual-event minimum-count increments, and evaluates bulk tails using actual horizontally and vertically shifted roots. It reconstructs the stated rational result without the companion's cost or arrival helpers. — [Independent checker](boundary_audit_check.py), [BE6](boundary_exchange.md).

Parent and child have the same root-point multiset after complementary completion and averaging. Consequently residual masses and all specified repairs are identical. Corresponding retained trade blocks have the same maxima. Their completed-count functions and costs therefore agree for all cutoffs by the written bijection; the supplied finite event replay is supplementary evidence. — [BE1 and complete embedding](boundary_exchange.md).

### Gaps

- The rule keeps nonnegative indices of the **old whole root block**. It does not keep every individually contained normalized child triangle. The residual point `(8,6)` lies outside both smaller child span strips and proves that substituting child spans into a boundary or clearing estimate would be invalid. — [Independent clipping assertion](boundary_audit_check.py).
- All charged cuts and donor periods remain in the cost. The result is `log D=O(q+s)`, not a coefficient-two estimate relative to the compressed child spans. — [BE6](boundary_exchange.md).

## Does the audited mechanism establish an adequate infinite return?

### Takeaway

**No.** It establishes a repeatable parameterized exchange and a complete rational embedding, with an explicit example that already loses optimality at time three. The infinite-return objective remains open. — [Scope and final gaps](boundary_exchange.md).

### Cited Findings

- The actual finish still requires one family with integer `D_H Q_H`, strictly positive error `M-Q_H`, and `D_H(M-Q_H)->0`. Neither geometric compression nor equal-cost substitution supplies that rate. — [Accepted target](../adaptive-shape-couplings/REPORT.md).
- The supplied checker and the independent checker both pass. No substantive erratum was found in the infinite proofs or the stated finite claims. — [Supplied certificate](boundary_exchange_check.py), [independent certificate](boundary_audit_check.py).

### Inferences

The new mechanism can be used inside a parent coupling once that coupling's actual window is proved. A future arithmetic advantage would need a valid global formula charging every retained root and boundary; it cannot change the reduced denominator of an already fixed cost. The audited embedding demonstrates repeatability and complete coverage, while its deficit at three prevents confusing it with a new long-head construction. — [BE1–BE6 and explicit cost](boundary_exchange.md).

### Gaps

- Still unproved: a suitable actual infinite parent family, a sufficiently long repeated agreement window, and an error small enough after all arithmetic clearing. No proof of irrationality or historical priority follows.
- Skipped Lean, external review, installations and archived edits. Material risk: confusing local span compression with cheaper arithmetic for an unchanged rational number.
