# Adaptive shapes and forced optimal triples

## Can actual optimality survive replacing long equal-rank shapes?

### Takeaway

**Yes in an exact finite example.** A constructive integer matching uses ten normalized shapes of spans at most \(8\times5\) and agrees with every actual optimum count through \(2^{19}\), beyond \(2^{2\cdot8}\). This is a finite optimal head, not a complete rational periodic coupling. — [Standalone construction and all-event replay](adaptive_structure_check.py).

### Cited Findings

- Original token \((a,b)\) has color \(a-b\bmod3\), ordinary arrival \(2^a3^b\), dyadic delay \(3/2\) for \(a\ge1\), and row-one delay \(9/8\) for \(a\ge2\). The fractional endpoint \(27/2\) is retained. The optimum completed count is \(\tau(t)=\min_jT_j(t)\). — [Accepted framework](../fractional-farey-transport/REPORT.md), [independent reconstruction](adaptive_structure_check.py).
- The checker constructs 43 disjoint three-color triples covering the first 43 tokens of every color. Every span is at most \(8,5\), and direct replay gives \(G(t)=\tau(t)\) at every actual arrival through \(524288=2^{19}\). It prints the entire witness and its ten shapes. No optimizer or archived checker is imported. — [Function check_short_head](adaptive_structure_check.py).
- The next balanced reset is from count 43 at 497664 to count 44 at 589824. The three new points are \(\{(0,12),(8,7),(16,2)\}\), of span \(16,10\). — [Exact reset enumeration](adaptive_structure_check.py).

### Inferences

**AS1. A zero-cost alternating trade.** Equal-rank matching at ranks 27–29 uses color-zero points \((2,8),(13,1),(4,7)\). Cycle these to \((13,1),(4,7),(2,8)\), retaining the other colors. The new triples are
\[
\{(13,1),(10,3),(14,0)\},\quad
\{(4,7),(12,2),(7,5)\},\quad
\{(2,8),(1,9),(9,4)\}.
\]
Their spans are \(4\times3,8\times5,8\times5\); their completion times remain exactly \(27648,36864,41472\). Thus the trade preserves the completed-count function at every real cutoff and preserves cost. An overspan equal-rank triple alone does not prove a universal span obstruction. — [Trade assertions](adaptive_structure_check.py).

**AS2. A forced genuinely new collinear shape.** If a point arrives in a minimum color at \(t\), every optimal coupling must complete its mass by \(t\). A partner cannot have been present at an earlier zero-surplus event of its own color: all its mass would already have been consumed. Candidate partners therefore lie after their respective last earlier zero-surplus events.

For \(z=(12,5)\) at \(995328\), eligible color-zero partners are \((15,3),(4,10)\); the only eligible color-two partner is \((18,1)\). Only the first choice fits an \(8\times5\) box. A bounded-span optimal coupling must therefore use
\[
\{(12,5),(15,3),(18,1)\},
\]
normalized as \(\{(0,4),(3,2),(6,0)\}\). This collinear progression along \((3,-2)\) differs from the old reflected Farey shapes. Collinear triples must not be excluded merely because the predecessor used unimodular triangles. — [Exact eligible pools](adaptive_structure_check.py), [earlier six-triangle obstruction](../fractional-farey-transport/obstruction.md).

The ten finite-head shapes, in coordinate-minimum normalization, are:

~~~
((0,0),(0,1),(1,0))   ((0,2),(1,1),(2,0))
((0,3),(1,2),(4,0))   ((0,3),(3,1),(4,0))
((0,4),(1,3),(6,0))   ((0,4),(3,2),(6,0))
((0,4),(5,1),(6,0))   ((0,5),(1,4),(8,0))
((0,5),(3,3),(8,0))   ((0,5),(5,2),(8,0))
~~~

### Gaps

- The placements need not repeat modulo six. They prove neither whole-plane coverage, balanced edge flux, a complete rational cost, nor a feasible actual-repair polytope. Appending the equal-rank tail gives a complete optimal coupling but supplies no rationality for its cost. — [Arithmetic obligations](../fractional-farey-transport/fractional_arithmetic.md).
- Some new shapes exploit low-row delays. The first traded triple's raw-time dispersion is \(\log(27/16)\); vertical translation beyond the delayed rows destroys its special alignment. Boundary-only exchanges are an unproved possible alternative to globally repeating every such shape. — [Arrival definitions and trade](adaptive_structure_check.py).

## Can balanced resets force long triples independently of the palette?

### Takeaway

**Yes.** Consecutive balanced levels differing by one force a specific triple in every optimal coupling, including fractional couplings. Exact witnesses exclude every bounded-span palette for the two specified minimal-corner repair instances and charge necessary corner enlargement. They do not give reduced-denominator lower bounds. — [Exact reset certificates](adaptive_structure_check.py).

### Cited Findings

- Through \(2^{54}\), box \(27,17\) has 161 singleton balanced-reset bursts, 29 exceeding the box. Their minimum spans are \(30,19\), and maximum spans \(47,30\). — [Function check_forced_corner_bounds](adaptive_structure_check.py).
- Through \(2^{168}\), box \(84,53\) has 1420 such bursts, 82 exceeding the box. Their minimum spans are \(87,55\), and maximum spans \(150,95\). — [Independent exact enumeration](adaptive_structure_check.py).

### Inferences

**AS3. Forced-reset lemma.** Suppose all three arrived counts equal \(k\) at \(s\), and all equal \(k+1\) at \(t>s\). Exactly three new tokens arrive, one per color. Optimality at \(s\) uses all earlier token mass in completed triples; none can mix with later tokens. Optimality at \(t\) must consequently couple exactly the three new tokens with mass one. No integrality, periodicity, palette or denominator assumption enters this proof. Exact optimality at both endpoints is essential. — [Unit-marginal framework](../fractional-farey-transport/fractional_arithmetic.md), [reset data](adaptive_structure_check.py).

**AS4. Consequence for the componentwise architecture.** Suppose all kept bulk shapes have spans at most \(H,V\). A forced overspan triple cannot be a bulk triple. If both spans are at least six, it cannot fit either a six-wide bottom block or a six-high left block. Under that repair architecture it must lie in the finite corner \([0,A)\times[0,B)\), requiring
\[
A>\max a,\qquad B>\max b.
\]
This conclusion is independent of the number of bounded shapes and their nonnegative real weights. It does not apply to an unrestricted repair mixing arbitrary corner and edge components.

The first examples are:

- Box \(27,17\): balanced 114 at 3439853568 to balanced 115 at 3623878656, new points \((0,20),(27,3),(30,1)\), span \(30,19\).
- Box \(84,53\): balanced 852 at 516303566764041166064713728 to balanced 853 at 523347633027360537213511521, new points \((84,3),(87,1),(0,56)\), span \(87,55\).

These first excesses are only bounded constants. Enlarging the corner could absorb them without changing an asymptotic exponent. All specified head events give stronger bounds:

| Bulk spans | Head | Overspan forced bursts | Necessary corner | Six-rounded bounds |
|---|---|---:|---|---|
| \(27,17\) | \(2^{54}\) | 29 | \(A\ge53,\ B\ge34\) | \(54,36\) |
| \(84,53\) | \(2^{168}\) | 82 | \(A\ge168,\ B\ge96\) | \(168,96\) |

For the first row, horizontal necessity uses \((24,18),(5,30),(52,0)\), between balanced counts 304 and 305. Vertical necessity uses \((38,9),(19,21),(0,33)\), between counts 301 and 302. For the second row, the respective witnesses are \((17,95),(167,0),(82,54)\) and \((2,95),(152,0),(67,54)\). The checker prints exact endpoint times and reconstructs every point from actual arrivals. — [Hardcoded summary assertions and complete endpoint certificates](adaptive_structure_check.py).

### Gaps

- These are support necessities. Substituting the resulting \(A,B\) into the existing safe clearing formula charges \(2^A3^B\), but does not prove these factors remain in the reduced denominator. An expensive upper bound alone is not an arithmetic impossibility theorem. — [Clearance scope](../fractional-farey-transport/fractional_arithmetic.md).
- Larger periods, different repair components, changing the allowed box or another actual convergent level can evade a finite witness. No infinite favorable or unfavorable state supply is proved. — [AS3–AS4 hypotheses](adaptive_structure_check.py).

## Do all nonresonant convergents yield the same forced progression?

### Takeaway

**No: an exact counterexample breaks that inference.** Four smaller actual convergents have an isolated balanced-reset progression, but \(q=485,p=306\) has the same three consecutive arrivals with an unbalanced starting state. Consecutive near-isotime arrivals alone do not force their matching. — [Function check_progression](adaptive_structure_check.py).

### Cited Findings

For
\[
P_{q,p}=\{(0,2p+2),(q,p+2),(2q,2)\},
\]
the arrival times are \(9\,3^{2p},9\,2^q3^p,9\,2^{2q}\). Exact checks give:

| \(q,p\) | Before first arrival | After last arrival | Only three arrivals? |
|---|---|---|---|
| \(8,5\) | \(43,43,43\) | \(44,44,44\) | Yes |
| \(19,12\) | \(189,189,189\) | \(190,190,190\) | Yes |
| \(65,41\) | \(1900,1900,1900\) | \(1901,1901,1901\) | Yes |
| \(84,53\) | \(3127,3127,3127\) | \(3128,3128,3128\) | Yes |
| \(485,306\) | \(99852,99851,99852\) | \(99853,99852,99853\) | Yes |

The last check counts exact integer numerators and denominators directly at the three thresholds. It uses no large event sort, floating logarithm or solver. — [Standalone direct reconstruction](adaptive_structure_check.py).

### Inferences

The first four rows satisfy AS3 and force span \(2q,2p\). The fifth remains unbalanced, so AS3 cannot apply. Consequently nonresonance and continued-fraction quality alone do not automatically supply the proposed balanced return. The counterexample must be retained in any future universal obstruction or favorable-state selection argument. — [Explicit unequal counts](adaptive_structure_check.py).

### Gaps

- No theorem selecting infinitely many balanced progression states, or infinitely many states evading them, is established. Neither four positive cases nor the fifth counterexample proves the adequate infinite arithmetic return. — [Precise open target](../fractional-farey-transport/REPORT.md).
- Skipped: Lean, installs, external review, priority claims and archived edits. Material risk: treating a finite optimal head as a rational infinite coupling, or treating support certificates as reduced-denominator or infinite-family impossibility theorems.
