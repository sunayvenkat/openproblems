# Six translation phases and their forced actual deficits

**All six integer-translation phases of the prescribed index-six Farey tiling fail the desired long fixed-bulk matching window in both named bases.** The full quadrant repairs remain rational with the same asymptotic degree-two clearing bound. A capacity obstruction occurs before (2^{2H}) for every phase, even if its residual tokens could be rematched optimally without arithmetic restrictions. This is an exact finite classification for two bases, not an all-level impossibility theorem for other tilings or selected infinite subsequences. — [Exact six-phase certificate](translation_phases_check.py), [complete repair theorem](boundary_repairs.md).

## Which six phases are genuinely distinct, and does their repair remain cheap?

### Takeaway

The phase space is exactly (mathbb Z^2/\langle3u,2v\rangle), of size six. Small original-coordinate representatives preserve the edge-flux, corner-charge and denominator arguments uniformly; they do not introduce the (q)-sized phase shift that spoiled earlier skew-phase averages. — [Representatives and phase-aware cost summation](translation_phases_check.py).

### Cited Findings

- The whole-plane tiling has period lattice \(\Lambda=\langle3u,2v\rangle\), index six, and \(6\mathbb Z^2\subset\Lambda\). Its ownership is determined by the basis coordinates (i\bmod3,j\bmod2). Translation by (2v) cycles the original three colors. — [Bulk proof](farey_bulk.md), [first exact repair](boundary_repairs.md).
- For a phase (z\in\mathbb Z^2), the translated owner of a point (x) is (z+\operatorname{tile}_0(x-z)). The certificate chooses one (z\in\{0,\ldots,5\}^2) for each of the six distinct basis residue pairs. These are six tested partitions, not 36 duplicated phase tests. — [Exact `representatives` and `PhaseRepair.tile`](translation_phases_check.py).
- The new checker imports the previous exact repair helper with bytecode disabled, then replaces its tile and bulk-coset routines by phase-aware ones. It is not an independent implementation of the earlier repair. All new arrival, capacity and rational-cost tests use exact integers/Fractions. — [Source and dependency](translation_phases_check.py), [reused helper](boundary_repairs_check.py).

### Inferences

**TP1. Exhaustive translation classes.** Two shifts produce the same partition whenever their difference lies in \(\Lambda\). Conversely the six residue pairs ((i\bmod3,j\bmod2)) distinguish the placement of the two triomino types; the certificate directly reconstructs each owner and verifies every token in the tested region belongs to one valid three-color triple. The small representative square contains all classes because its coordinate period contains (6\mathbb Z^2). — [Exact representatives and ownership assertions](translation_phases_check.py).

The six classes for (u=(8,-5),v=(3,-2)) have representatives

\[
(0,0),(3,0),(2,0),(5,0),(4,0),(1,0)
\]

in lexicographic basis-residue order. For (u=(19,-12),v=(27,-17)), they are

\[
(0,0),(0,1),(1,0),(1,1),(2,0),(2,1).
\]

No unbounded coordinate translation or new period is introduced. — [Printed exact representative lists](translation_phases_check.py).

**TP2. Uniform full arithmetic.** Translation changes the six residue cosets but not the two normalized triple shapes or their spans (H,V). The same color-cycling period proves balanced edge flux. Every point-type coset still has two tokens of each color per (6\times6) cell; the bounds

\[
|n-H|\le10,\qquad d_j\le36(H+V+6)
\]

therefore persist. The donor count (J\le180) eventually in the actual bounded-slope regime is uniform in all six phases. The phase-aware bulk sum uses the shifted anchor congruences and the same twelve geometric streams, retaining every actual low delay. Thus the full repaired coupling cost (Q_z) clears by

\[
D_z=(63\cdot728\cdot2^6\cdot3^6)2^A3^{B+6J_z},
\quad A=6\lceil H/6\rceil,\ B=6\lceil V/6\rceil,
\]

and

\[
\log D_z=H\log2+V\log3+O(1).
\]

The constant is independent of the phase. This charges the finite corner, donor ranks and both infinite strips, rather than only the translated bulk. — [BR1–BR6](boundary_repairs.md), [full six-phase clearing assertions](translation_phases_check.py).

### Gaps

- A richer six-period torus tiling need not retain the color-cycling (2v) symmetry. It must separately establish balanced edge flux before using this repair theorem. — [Flux hypothesis BR2](boundary_repairs.md).
- Cheap translation and rationality do not imply a long actual optimality window. The capacity calculations below test precisely that missing assertion. — [Fixed-bulk capacity principle BR7](boundary_repairs.md).

## Does any translation phase preserve an actual optimal head through the arithmetic scale?

### Takeaway

No in the two prescribed examples. Every phase has a strictly positive fixed-bulk capacity deficit before (2^{2H}), while the complete enumeration runs through (2^{\lceil5H/2\rceil}). These witnesses are independent of how the residual strips or corner are coupled. — [All-event capacity certificate](translation_phases_check.py).

### Cited Findings

- If (G_B(t)) counts completed kept bulk triples and (R_j(t)) counts arrived residual tokens, every residual repair obeys
  \(G(t)\le G_B(t)+\min_jR_j(t)\). Hence its deficit is at least
  \(F_B(t)=\tau(t)-G_B(t)-\min_jR_j(t)\ge0\).
  — [Capacity proof BR7](boundary_repairs.md).
- The checker enumerates every original token whose actual arrival is at most the test threshold, including simultaneous arrivals and (27/2). The forward-delay property makes its original-time cutoff exhaustive. A completed kept triple is found from any of its arrived tokens and counted at its actual maximum. Thus the finite event list proves firstness in each tested interval. — [Exact event routine](boundary_repairs_check.py), [phase classification assertions](translation_phases_check.py).

### Inferences

**TP3. Basis (u=(8,-5),v=(3,-2)).** Here (H=8,V=5). The classification covers all actual retimed arrivals through (2^{20}). Every first deficit below equals one:

|Basis residue ((i\bmod3,j\bmod2))|Small shift|First forced (t)|Next arrival (t')|Forced full cost gap|
|---|---|---:|---:|---|
|((0,0))|((0,0))|243|288|(5/7776)|
|((0,1))|((3,0))|1458|1536|(13/373248)|
|((1,0))|((2,0))|486|576|(5/15552)|
|((1,1))|((5,0))|4608|5184|(1/41472)|
|((2,0))|((4,0))|2187|2304|(13/559872)|
|((2,1))|((1,0))|243|288|(5/7776)|

The last column is (1/t-1/t'), obtained by integrating the unit completed-count deficit. Since the latest first forced deficit is (4608<2^{16}), no translated kept bulk can be repaired into an optimal head through (2^{2H}) for this basis. This is stronger than a failure of one particular donor ordering. — [Exact six-case assertions](translation_phases_check.py).

**TP4. Basis (u=(19,-12),v=(27,-17)).** Here (H=27,V=17). The classification covers all actual retimed arrivals through (2^{68}). Again every first forced deficit equals one:

|Basis residue|Small shift|First forced (t)|Next arrival (t')|Forced full cost gap|
|---|---|---:|---:|---|
|((0,0))|((0,0))|382205952|387420489|(7153/203119913336832)|
|((0,1))|((0,1))|129140163|136048896|(13/33059881728)|
|((1,0))|((1,0))|429981696|452984832|(13/110075314176)|
|((1,1))|((1,1))|129140163|136048896|(13/33059881728)|
|((2,0))|((2,0))|805306368|816293376|(7153/427972821516288)|
|((2,1))|((2,1))|258280326|272097792|(13/66119763456)|

The latest first forced deficit is (805306368<2^{54}). Thus the hoped-for (2H)-scale optimal head is unavailable in every translation phase for this named basis, even with an ideal residual repair. — [Exact six-case assertions](translation_phases_check.py).

### Gaps

- The classification is complete over six translation classes for two bases, not over all Farey bases, all six-period partitions, or every actual-convergent subsequence. No all-level early-defect theorem follows from these finite certificates. — [Enumerated scope](translation_phases_check.py).
- A positive capacity deficit rules out exact optimality on that interval. It does not itself establish a universal asymptotic error-to-denominator lower bound for all other repairs. — [Capacity scope](boundary_repairs.md).

## What do the best-capacity phases achieve with the complete cheap repair?

### Takeaway

The best fixed-bulk phase still has an earlier deficit for the explicit low-height repair. Its exact reduced denominator and the unavoidable later capacity gap already show a non-small cleared error in each named example. This does not rule out a selected infinite family with another pattern. — [Full coupling/cost tests](translation_phases_check.py).

### Cited Findings

- For every phase the full (Q_z) is computed from the finite optimal corner, shifted period-index left matching, optimal finite bottom periods and the twelve complete bulk streams. The code asserts the entire common clearing; it does not approximate an infinite sum numerically. — [Phase-aware exact cost](translation_phases_check.py), [repair formulas BR4–BR5](boundary_repairs.md).
- The general actual dispersion theorem proves (Q_z<M) for these genuine couplings with their retained positive-density fixed-offset bulk. It does not improve their rate of convergence. — [Accepted strictness theorem](../rational-coupling-construction/coupling_strictness.md).

### Inferences

**TP5. Best capacity at (H=8).** The phase ((5,0)) has last first forced deficit among the six phases. Its complete explicit repair has

\[
Q_{(5,0)}=13501693/22643712.
\]

Its own first loss is already at (1458), with ((\tau,G)=(14,13)), rather than at the unavoidable (4608). The stated common clearing has 63 bits; the actual reduced denominator is 22643712. The bulk obstruction gives

\[
22643712\,(M-Q_{(5,0)})\ge22643712/41472=546>1.
\]

This is a certificate for this actual comparison value, not merely an inadequate upper estimate. — [Best-phase cost, first loss and exact lower product](translation_phases_check.py).

**TP6. Best capacity at (H=27).** The phase ((2,0)) has complete cost

\[
Q_{(2,0)}=11301677504582126401/18927526004379353088.
\]

Its own first loss is at (429981696), with ((\tau,G)=(94,93)), earlier than the forced (805306368). The common clearing has 90 bits, while the reduced denominator has 65 bits. Multiplying that reduced denominator by the exact forced lower gap (7153/427972821516288) is strictly greater than one. The same test for (\widehat Z=3-3Q) uses its actual reduced denominator and also gives a cleared error greater than one. — [Best-phase exact assertions](translation_phases_check.py).

The difference between a capacity-optimal residual repair and the explicit cheap one remains mathematically important. The former could improve the earlier loss, but no repair of the same selected bulk can pass the later capacity witness. A longer optimal head therefore requires a different bulk partition or a theorem for another selected sequence, not just a better finite donor ordering in these examples. — [TP3–TP6 and BR7](boundary_repairs.md), [exact event replay](translation_phases_check.py).

### Gaps

- No adequate infinite integer-cleared error family is constructed. The earlier signed hierarchy's boundary arithmetic and residual nonvanishing also remain unproved. — [Current full objective](../rational-coupling-construction/REPORT.md).
- A richer periodic or state-dependent bulk can alter the capacity function. Such a candidate needs new coverage, color-flux, arithmetic and actual-window proofs; this six-phase test does not exclude it. — [Exact phase scope](translation_phases_check.py).
- Skipped: Lean, broad model sweeps, installations, density decimals, old-folder edits and external posts. Main risk: treating a complete finite six-phase classification as an infinite no-go, or treating the capacity-zero condition as sufficient for the proposed rational repair to be optimal.
