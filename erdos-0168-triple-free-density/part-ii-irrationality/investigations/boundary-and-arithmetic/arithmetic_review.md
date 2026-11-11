# Independent review: arithmetic reductions and single-root rotation

**Verdict:** no algebraic gap or counterexample was found in the stated arithmetic reductions or the single-root rotation theorem. The unconditional identities must remain separate from the cone formula conditional on (C). Neither set of results proves the patched finite-cover formula or the target irrationality statement.

## Are smooth-cutoff separation and the conditional cone birth rule correct?

### Takeaway

Yes. The separation and its nine-entry correction table are unconditional. The birth cone follows from (C) when the correction indicators do not change; the restriction b≥4 ensures this for every a≥0, including the first point of a column.

### Cited Findings

- The reviewed statements are equations (1)–(4), with the correction table, indicator vector, and small-column qualifications. — [Arithmetic note](arithmetic.md).
- I reran the supplied checker: 120 separation checks, 54 conditional-cone comparisons against previously certified optima, and 18 strip-recurrence checks all passed; the last saved cutoff is 294912. — [Checker](arithmetic_check.mjs), [original exact-DP dataset](../../early-attacks/open-conjecture-transfer-search/168_exact_diagonal_results.json).
- The true optimum, candidate construction, and isolated/patch intervals are defined separately in the original grid analysis. — [Finite reduction and candidate](../../early-attacks/open-conjecture-transfer-search/168_grid.md).

### Inferences

**Independent separation derivation.** At d=2^a3^b, every exponent pair in the board belongs to exactly one of the rectangle i≤a,j≤b, the arm i>a, or the arm j>b. The two arm inequalities reduce respectively to `2^x≤3^k` and `3^y≤2^l`, so their rotated contributions depend only on b and a. Writing the rectangle sums as P_a and Q_b gives

```
Z_(a,b) = A_a+B_b-1+(P_a-1)(Q_b-1).
```

The three values of `P_a-1` are `(0,ω²,-1)` and those of `Q_b-1` are `(0,ω,-1)`. Their products reproduce exactly

```
[[0,0,0],[0,1,-ω²],[0,-ω,1]].
```

The rectangle partition includes a=0 and b=0 without an extra term.

**Indicator scaling.** At d, the largest possible isolated power is `2^(a+m_b)`. The unique possible patch root is `2^(a+n_b)`. Rotating by the inserted color `a+2b` removes a from both indicator colors and from both interval tests, yielding the displayed ε_b. For b≥4, n_b≥3 and m_b≥6, so none of the patch's low-exponent exceptions can occur.

The isolated indicator changes at powers of two or at `(3/2)2^A`; the patch indicator changes at `6·2^A` or `(27/4)2^A`. In the range relevant to b≥4, these are genuine smooth cutoffs with three-exponent 0, 1, or 3. Thus no correction changes at a point with b≥4, or between its preceding smooth cutoff and that point. This last observation is needed: merely saying that a discontinuity is not equal to d would not suffice if nonsmooth discontinuities could lie between successive prefixes. The b≥4 range excludes that issue.

The two corrections cannot coexist. If a patch root x exists, then `6x≤t<27x/4<8x`; the largest pure power below t is 4x, and `4x≤2t/3`, so it is not isolated.

**Cone inequalities and ties.** Let the current adjusted counts in the rotated frame be H_0,H_1,H_2. The preceding state is `(H_0-1,H_1,H_2)` because exactly color 0 was inserted and ε is unchanged. Therefore

```
min(H_0,H_1,H_2)-min(H_0-1,H_1,H_2)=1
iff H_0≤H_1 and H_0≤H_2.
```

Writing `Z=x+yω` gives `x=K_0-K_2`, `y=K_1-K_2`, and exactly the two inequalities in equation (3). The non-strict signs are correct. The passage from these count minima to the **actual** τ is precisely where (C) is used.

**Finite columns.** The note is correct to retain b=0,1,2,3 separately in the main formula. The optional b=2 extension is also valid: `m_2=3`, no patch occurs at `9·2^a`, and the rotated indicator is always `(0,0,1)`. Indicator changes do not occur at those births. I independently compared this special cone test with all 16 b=2 points in the saved exact-DP dataset; all agreed. This bounded comparison supplements the proof of the indicator statement and does not establish (C) generally. Columns b=1 and b=3 can coincide with correction changes and are not silently covered by the b≥4 argument.

### Gaps

No gap was found in these reductions. Equations (3)–(4) remain conditional on (C); the finite comparisons are not a proof of that hypothesis. The additive separation does not remove the nonlinear minimum.

## Are the base-8 cocycle, column identity, periodicity criterion, and KK limitations correct?

### Takeaway

Yes. All cocycle and resummation formulas check, including the breakpoint order, six equal directional lengths, and the binary eventual-periodicity criterion. The note correctly declines to invoke KK Proposition 7.4 without a fixed number of terms, a fixed coefficient vector, sufficient error saving, and nonvanishing.

### Cited Findings

- Equations (5)–(11) give the strip recurrence, cocycle, column resummation, and rationality criterion. — [Arithmetic note](arithmetic.md).
- I read the saved primary manuscript at Proposition 7.4 and §§6.1–6.4, Corollary 6.5, and §7.3. Proposition 7.4 fixes m, the rational vector d, and ε before choosing its constant. Corollary 6.5 supplies m≤404, a finite coefficient set, nonzero exponentially small error, and the height bound used in §7.3. — [Primary source extract](../Erdos%20theorem%20transfer%20investigation/erdos1062-fork-free-density.pdf.txt), [primary manuscript](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf).
- The density normalization and absolute smooth reciprocal summation underlying the column grouping are established in the earlier arithmetic notes. — [Density reduction](../../early-attacks/open-conjecture-transfer-search/168_irrationality.md).

### Inferences

**Strip recurrence.** Partitioning D_(2^(a+1)) into i≥1 and i=0 gives

```
W(2^(a+1)) = ω W(2^a)+S(floor((a+1)α)).
```

Multiplying by `ω^(-(a+1))` proves (5) with the stated sign. Since S is three-periodic,

```
S(floor((3n+s)α)) = S(floor(3{nα}+sα)).
```

Together with `ω^(-3n)=1`, this proves every equality in (6), including `Y_0=1`.

**Cocycle table.** For s=1,2,3 the discontinuities occur when `3x+sα` is an integer. Because `1/2<α<2/3`, these are exactly the nine points printed in the note, in the printed order. Starting at zero the three summands give Φ(0)=−ω. Updating the summand that jumps at each successive point yields exactly

```
-ω, 0, ω, -1, 0, 1, -ω², 0, ω², -ω.
```

The function is right-continuous under the floor convention; the first and last values agree across the circle endpoint. Each of `±1,±ω,±ω²` occupies total length `(1-α)/3`. For −ω this is the sum of the first and last interval lengths. Their vector sum is zero, proving mean zero. Finally `S(k+1)=1+ω²S(k)` and `sum_(s=1)^3 ω^(-s)=0` prove `Φ(x+1/3)=ω²Φ(x)`, with the argument interpreted modulo one. No boundedness or recurrence conclusion for the accumulated state follows from these computations.

**Which identities are unconditional.** The definitions of A, B, η and the recurrence (5)–(7) require no cover ansatz. Inserting one point changes τ by 0 or 1: restriction gives the lower monotonicity bound, and adding the new vertex to an old cover gives the upper bound. Hence `a_(a,b)=1-3η_(a,b)` unconditionally. Summing the geometric constant term gives (8). Grouping a by residue modulo 3 gives the exact base-8 weights in (9); only its substitution of the cone indicator for η uses (C).

Since `|a_(a,b)|≤2` and `sum 2^(-a)3^(-b)=3`, all sums are absolutely convergent. Thus grouping by columns is legitimate. The density identity gives

```
sum_(a,b) a_(a,b)/(2^a3^b)
 =3 sum ΔF(d)/d -2·3
 =9c-6,
```

which verifies (10) and its normalization.

**Rationality criterion.** In (8), the a=0 term is integral and the remaining η digits are an ordinary binary fractional expansion. A rational number has an eventually periodic base-two expansion, including both alternatives at a dyadic rational. Conversely an eventual period sums geometrically to a rational. This proves (11) without (C). A finite sum of rational multiples of {2,3}-units is rational, so eventual periodicity is necessary for the particular exact full-column evaluation proposed in the note. This criterion does not exclude other ways of combining several columns before evaluating them.

**KK interface.** The source does use two geometrically weighted series with fixed finite-step rotation coefficients, then sixteen spaced event families. The new Φ has finitely many discontinuities, but its output digit depends on the accumulated planar state Y_n as well as the phase. Therefore the same finite-event argument does not follow merely from Φ being a step function. Proposition 7.4 can be applied after a suitable finite-form construction; it does not supply that construction. The arithmetic note correctly leaves bounded dimension/coefficient control, improved relative error, and nonvanishing unresolved.

### Gaps

No error was found in equations (5)–(11). The cone-coded form (9) is conditional; (5)–(8), (10), and (11) are unconditional. Neither periodicity nor nonperiodicity of the relevant birth words is established. No uniform finite S-unit form satisfying KK's hypotheses has been produced.

## Does the single-root rotation proof survive review, and is the target still eligible?

### Takeaway

The single-root theorem is valid as written and does not require simple connectivity. The live target remained presented as unsolved at the verification time below; its requested conclusion is irrationality, not the auxiliary cover formula.

### Cited Findings

- The reviewed proof is the rotation lemma, zero-augmentation theorem, closure classification, and single-root conclusion. — [Boundary note, second section](boundary.md).
- At **2026-11-07 04:34:05 UTC** (2026-11-06 23:34:05 in America/Indianapolis), the primary page asked: “Is the limit F(N)/N as N→∞ irrational?” It showed no attempts on either proof or counterexample and no published pieces. Its displayed formal target is `True ↔ Irrational (Filter.limsup (fun N => ↑(Erdos168.F N) / ↑N) Filter.atTop)`. — [Live primary target](https://conjectures.io/problems/erdos168-erdos-168-parts-ii).

### Inferences

**Rotation step.** From a reachable left index `9w/2`, E(w) either exits or has target `q=3w/4` in Q. In the latter case q is an allowed owner avoiding a=0. The bound `w≤4t/9` gives `3q≤t`, so R(q) exists and starts at exactly the same index: `6q=9w/2`. Following R(q) either exits or reaches the left index `9q/2` through its N edge, allowing repetition with owner q. Each repetition lowers the first exponent by two. It must terminate because U is finite and has no vertical-axis labels. Every newly traversed index has a smaller first exponent than the current one, so the constructed suffix cannot revisit a vertex of the previously reached prefix. Early R exits are valid and are correctly retained.

**External E source above the rotation range.** If `4t/9<w≤2t/3`, lack of an immediate exit forces `q=3w/4` into Q. Then `t/3<q≤t/2`. Its E edge is available and its left index `9q/2>t` is external. Thus choosing w least among external E owners really does give a contradiction; the new owner q is strictly smaller. The corresponding external-R argument falls directly in the rotation range. The converse is immediate because the N matching then saturates every incident left vertex.

**Closure endpoint check.** The forbidden middle ranges are `(t/6,t/3]` and `(t/3,2t/3]`. At the last low 6-multiple p, closure first forces `6p>2t/3`, hence `p>t/9`; therefore `9p/2>t/2` cannot still be low and must also be high. This supplies the printed stricter bound `p>4t/27`. The predecessor contradiction and the at-most-one-axis-root argument then follow with the stated strict endpoints. The patch window is exactly `6x≤t<27x/4`; equality at its upper endpoint is excluded correctly.

Thus a positive set with one horizontal root has no augmentations and is closed; it contains the isolate or patch. This is a proof of the claimed single-root deficiency bound. It does not establish enough disjoint augmentations for a multi-root component, and the note explicitly withdraws the earlier overly strong disjoint-row suggestion.

The live page's displayed formal target uses limsup, whereas its prose uses a limit. The existing density-existence result reconciles them; the current auxiliary lemmas do not independently prove irrationality of either expression.

### Gaps

The remaining combinatorial cases are multi-root components and the global treatment of components meeting the vertical axis. The arithmetic return/compression and nonvanishing obligations remain separate. This review did not re-audit the full boundary-pocket charge proof, repeat numerical optimization, conduct a broad search, run Lean, or post externally. Current target status is a timestamped site observation, not a global priority certification.
