# Erdős 168(ii): exact grid investigation

Status, 2026-11-06: **the catalog conjecture is not solved here**. The live target asks whether the limiting density of sets avoiding `{n,2n,3n}` is irrational. The work below gives an exact finite dynamic program, a rigorously valid family of improved covers, and strong finite evidence for a specific formula. Its lower bound for arbitrary size, and the irrationality implication, remain unproved.

Live target: <https://conjectures.io/problems/erdos168-erdos-168-parts-ii>.

## Reduction and notation

Write every positive integer uniquely as `m 2^a 3^b`, with `(m,6)=1`. Each forbidden triple lies in a single `m` component. For real `t >= 1`, put

`D_t = {(a,b) in Z_{≥0}^2 : 2^a 3^b <= t}`.

Let `tau(t)` be the least number of deleted points meeting every oriented corner

`{(a,b),(a+1,b),(a,b+1)}` contained in `D_t`.

Then the largest allowed subset of `D_t` has size `alpha(t)=|D_t|-tau(t)`. In particular, this local problem is weaker than the all-divisibility fork restriction in Kohlmeyer–Kruer's #1062 theorem. Their local extremal formula cannot simply be substituted for `alpha(t)`.

## An explicit candidate, with a proved upper bound

Let

`K_j(t) = #{(a,b) in D_t : a-b = j (mod 3)}`, `j=0,1,2`.

Every corner contains exactly one point of each color, so each color class is a cover. There are two rigorous corrections.

1. **Isolated point.** If `z=2^A <= t < (3/2)2^A`, the point `z` belongs to no corner and can be removed from color `A mod 3`. For `t>=3`, this is the only isolated vertex. Indeed every point divisible by 3 belongs to the corner rooted at one third of it, and a pure power of 2 belongs to a corner precisely when its half has triple endpoint at most `t`.

2. **Axis patch.** Let `x=2^a` with `a>=1` and

   `6x <= t < 27x/4`.

   From color `a mod 3`, delete the three cover points

   `{x, 9x/2, 6x}`

   and insert

   `{3x/2, 2x}`.

   This reduces the cover size by one. All removed points have color `a`, all inserted points have color `a+1`. To check validity, a corner containing `x` is rooted at `x` or `x/2`, and is met by `2x` or `3x/2`; there is no third-parent corner because `x` is a pure power of 2. The point `9x/2` can occur as the third member of the corner rooted at `3x/2`; its possible half-parent has largest member `27x/4 > t`, and its own rooted corner is also outside the domain. The point `6x` has third-parent `2x`; its half-parent and its own rooted corner have largest members at least `9x > t`. Thus every potentially uncovered corner is still met. The two new points are not originally in the color class.

The intervals for different pure powers `x` are disjoint, so there is at most one axis patch at a given `t`. It does not overlap the isolated-point removal.

Define `I_j(t)` to be the indicator for the isolated point of color `j`, and `P_j(t)` the indicator for the axis patch of color `j`. For `t>=3` the **proved construction bound** is

`tau(t) <= min_{j=0,1,2} [K_j(t)-I_j(t)-P_j(t)]`.

The **unproved candidate** is equality for every `t`.

## Two useful small instances

At `t=162`, there are 24 vertices and raw color sizes `(8,8,8)`. The cover

`{2,9,12,16,54,72,96}`

has size 7. This is a single color class with isolated point 128 omitted; it does **not** demonstrate a change of color in the interior. Descending greedy selection gives only 16 allowed vertices, whereas the exact optimum is 17.

At `t=1536`, there are 45 vertices, all active, with color sizes `(15,15,15)`. Color 2 admits the patch

`{256,1152,1536} -> {384,512}`.

A resulting size-14 cover is

`{3,4,18,24,32,81,108,144,192,384,486,512,648,864}`.

The exact integer dynamic program proves `tau(1536)=14`, hence `alpha(1536)=31`. This is the first failure, among smooth prefixes, of the minimum-color formula with only the isolated-point correction.

There is also a short rational certificate independent of the DP: give the corner rooted at `v` weight `w(v)/4`, where `w=2` on

`{1,2,3,4,8,9,12,16,27,36,48,54,72,81,216,243,288,324,432,486}`,

`w=1` on `{32,96}`, `w=3` on `{64}`, and `w=4` on `{384,512}`, with all other weights zero. The weights sum to `53/4`. For each vertex `n`, the total incident numerator `w(n)+w(n/2)+w(n/3)` is at most 4 (a nonintegral or absent root contributes zero). Multiplying the cover constraints by these weights proves every cover has size at least `53/4`, hence at least 14. The integer verifier in `exact_168_diagonal.py` checks this certificate and the size-14 cover. Data: `168_1536_simple_dual.json`.

## Exact diagonal dynamic program

For `k=a+b`, the present points on diagonal `k` form an interval

`I_k = {L_k,L_k+1,...,k}`

in coordinate `a`, where

`L_k=max(0,ceil((k log 3-log t)/log(3/2)))`.

The implementation obtains these intervals from exact integer powers, avoiding floating-point boundary decisions. A corner rooted on diagonal `k` has coordinates `a` below and adjacent coordinates `a,a+1` on diagonal `k+1`. Thus a deleted mask `U` on the upper diagonal forces exactly those lower positions whose two upper children are both undeleted.

Let `d_k(S)` be the minimum number of deleted points in diagonals `k,k+1,...`, conditioned on the deletion mask `S` on diagonal `k`. At the highest diagonal, `d_k(S)=|S|`. The recurrence is

`d_k(S) = |S| + min_{U: M(U) subset S} d_{k+1}(U)`,

where `M(U)` is the just-described mandatory mask. Every forbidden corner crosses exactly this one boundary, so the recurrence is exhaustive in both directions. It is an exact integer algorithm. A subset-min transform evaluates all transitions without enumerating every pair of masks. The final optimum is `min_S d_0(S)`.

Its state width grows with `log t`; this is **not** a finite-state formula independent of `t` and does not by itself enable the #1062 irrationality argument.

Implementation: `exact_168_diagonal.py`. Exact results: `168_exact_diagonal_results.json`.

## Verification and historical priority

The exact integer DP checked every one of the first 120 smooth prefixes, through `t=294912`, and found equality with the patched candidate. This includes exact optimality of both displayed small examples. The separate SciPy/HiGHS experiment `check_168_diagonal.py` checked every nontrivial smooth prefix with `t<=10^12`, ending at the 534-point prefix `t=990677827584`, with no candidate discrepancy. Its 532 records are in `168_diagonal_results.json`. Its solver conclusions are numerical, while every returned cover is checked with integer combinatorial conditions.

The candidate also agrees with **all 5000 prefixes** reconstructed from the full 3335 first-hit records in [OEIS A004059](https://oeis.org/A004059). The source attributes records from the 44th onward to Sean Eberhard (September 2025). His [published program](https://oeis.org/A004059/a004059.py.txt) builds a binary Gurobi model with one corner constraint per triple; it does not impose the color ansatz. Thus this is independent numerical evidence, not circular validation, but it is not an exact certificate for those larger instances. The fetched data are `168_oeis_full_first_hits.txt`.

The raw three-color construction and isolated-point correction are old. [Chung–Erdős–Graham, *On sparse sets hitting linear forms*](https://www.math.ucsd.edu/~ronspubs/02_04_linear_forms.pdf), pages 8–9, explicitly conjecture their optimality. The displayed `t=1536` cover refutes that printed conjecture. Priority of this counterexample or the repaired candidate has **not** been established; modern numerical tables already record its optimal value. It is not a resolution of #168(ii).

[Veselinov's 2026 paper](https://arxiv.org/html/2604.15515v1) supplies the leading `2/3` asymptotic for smooth-prefix independence, a reciprocal-sum expression for the density, and local insertion observations. It does not provide the exact patched formula. Its warning that a nonperiodic smooth-denominator coefficient sequence can still sum to a rational number is directly relevant: merely showing nonperiodicity does not prove irrationality.

## Remaining mathematical gaps

A useful exact reformulation from the parent investigation is the following. Fix a color class `C_j`. For `U subset C_j`, form a bipartite graph `B(U)` on the other two colors: each corner whose color-`j` point lies in `U` contributes the edge between its other two points. Then

`tau(t) = |C_j| - max_{U subset C_j} (|U| - nu(B(U)))`,

where `nu` is the maximum matching size. This follows from the bipartite vertex-cover theorem: remove `U` from `C_j` and optimally cover precisely the newly uncovered corners with vertices of the other two colors.

The edges of `B(U)` split into three directional matchings. For a label `u=2^a3^b`, its north-parent edge exists exactly when `b>=1`; its east-parent edge exists when `a>=1` and `3u<=2t`; and its rooted-corner edge exists when `3u<=t`. The north-parent matching alone has size `|U|-#{u in U:b=0}`. Consequently, positive matching deficiency requires removal of pure powers of 2. An improvement involving only interior points, or only the vertical axis, is impossible. Classifying augmenting paths from that horizontal axis is a concrete route to the missing lower bound; the classification has not been completed.

One partial boundary lemma is proved. Regard the other colors as a bipartition in which the north-parent edge for label `u` has left endpoint `u/3` and right endpoint `2u/3`. Multiply left-endpoint values by 3. The possible left labels generated by `u` are then:

* `u` itself, if `b>=1`;
* `(9/2)u`, if the east-parent edge exists;
* `6u`, if the rooted-corner edge exists.

Suppose `U` avoids the vertical axis and is closed under every available generated left label (so these labels all belong to `U`, even though generation could in principle leave `D_t`). Then every `u in U` lies in

`(4t/27,t/6] union (2t/3,t]`.

Proof: a point in `(t/6,t/3]` generates `6u>t`, while one in `(t/3,2t/3]` generates `(9/2)u>t`; neither can be in a closed set. If `u<=t/6`, take the last low point `p` along its successive `6`-multiples. Both children must be high, forcing `p>4t/27`. If at least one earlier `6` step occurred, its predecessor `q=p/6` also generates `r=(9/2)q=3p/4`, which lies in `(t/9,t/8]`. If `r` is on the vertical axis, this already contradicts the hypothesis; otherwise it generates `(9/2)r`, lying in `(t/2,9t/16]`, the forbidden middle interval. Hence no earlier step occurred and `u=p` lies in the asserted patch interval.

Thus a closed set can contain a horizontal-axis root only at the isolated-point or axis-patch location. This is **not yet the needed Hall inequality**: sets with external generated labels can contain multiple axis roots, and matching depends on both endpoints, not only the left labels. The lemma must not be promoted to a proof of the candidate.

An additional numerical observation (three constrained MILPs at each of the first 120 smooth prefixes) is that forcing every vertical-axis point of color `j` into the cover gives optimum `K_j-I_j-P_j` individually. Proving this fixed-boundary assertion, plus showing some global optimum has such a boundary phase, would suffice. A simple packing proof cannot work in this form: for the 100-point prefix and fixed color 1, the fractional cover optimum is approximately `32.2644`, whereas the asserted integer optimum is 34.

**Precise next lower-bound lemma (unproved).** Fix `j` and `U subset C_j` avoiding the vertical axis. Put `r=#{u in U:b=0}` and `delta_j=I_j(t)+P_j(t)`. The desired inequality is

`nu(B(U)) >= |U|-delta_j`.

The north-parent matching has size `|U|-r`, so this asks for at least `r-delta_j` augmentations. Equivalently, for every vertex cover `W` of `B(U)`, let `D` count north-parent matching edges whose two endpoints both lie in `W`, and let `E` count vertices of `W` outside all north-parent matching edges. Then

`|W|=|U|-r+D+E`,

and the needed charging inequality is `r <= D+E+delta_j`. Contracting the north-parent matching gives directed alternating arcs `6u -> (9/2)u` and `(9/2)u -> (3/4)u`, both strictly decreasing in numerical value. A proof would have to route or charge distinct horizontal-axis roots to distinct doubled pairs or external vertices, except for the isolated/patch defect. The closure classification above describes defect sets without exits, but does not rule out several roots sharing a bottleneck. No such routing or charging theorem has been proved in this research round.

All local processes have completed. In particular, the SciPy run formerly using execution session `94566` ended successfully and must not be polled again. The current files are a research checkpoint, not a completed proof of #168(ii).

* Prove the lower bound matching the patched construction for every weighted triangle, or find its first counterexample.
* Any normalization to covers using at most two colors must use the actual weighted-triangle geometry: a collaborator found that normalization false for arbitrary Ferrers shapes with repeated row lengths.
* Even an exact patched formula still leaves the nonlinear minimum of three color counts. Their discrepancies are unbounded; a bounded-state argument cannot silently assume otherwise.
* A possible direction is to exploit bounded discrepancy along continued-fraction return times (Denjoy–Koksma), rather than bounded discrepancy at every time. Exact repeated blocks, appropriate return offsets, and the Subspace-Theorem nonvanishing argument would all still need proof.
