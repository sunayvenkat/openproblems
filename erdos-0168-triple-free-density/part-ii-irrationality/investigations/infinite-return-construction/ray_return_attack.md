# True-phase excursions and actual ray-return control: final attack

**Final status: FAIL to construct the adequate infinite sequence.** A new actual-cocycle argument rules out the simplest long-excursion architecture: one fixed raw minimizing color cannot persist through arbitrarily long logarithmic windows. A rotating winner is a different problem and remains unproved. No special arithmetic identity closing the paired ray-local-time coefficients was obtained. Thus the remaining gap is still larger than nonvanishing.

This note uses the already proved finite formula (C), the exact strip cocycle, and the first-round paired weighted response. It does not infer a finite-state process from unbounded count discrepancies. — [Finite result](../prefix-and-phase-audit/REPORT.md), [axis cocycle](../boundary-and-arithmetic/arithmetic.md), [weighted first round](weighted_returns.md).

## Can an adjustable true cutoff create a long interval with one raw winning phase?

### Takeaway

No infinite sequence of such intervals exists. Three successive doubling cutoffs with the same adjusted minimizing color already bound the raw discrepancy absolutely; the actual three-doubling rotation cocycle has a uniform finite escape time from every fixed bounded set. This obstruction is independent of how large the initial cutoff is.

### Cited Findings

- The exact recurrence, with `omega^3=1` and `omega!=1`, is
  `W(T+log2)=omega W(T)+S(floor((T+log2)/log3))`, where `S` takes values `1,−omega,0`. — [Saved exact horizontal recurrence](../../early-attacks/open-conjecture-transfer-search/168_irrationality.md).
- The exact three-step increment is the nine-breakpoint zero-mean step function `Phi` from the separated arithmetic calculation. — [Equations (5)–(7)](../boundary-and-arithmetic/arithmetic.md).
- The phase-zero discrepancy sums are unbounded, by the saved Kesten argument for the thirds interval. The primary bounded-remainder criterion is that an interval length belongs to `Z theta+Z`; a rational nonintegral third does not. — [Existing complete reduction](../../early-attacks/open-conjecture-transfer-search/168_irrationality.md), [Kelly–Sadun, Theorem 1](https://arxiv.org/html/1404.0455), [Kesten's original article](https://geodesic.mathdoc.fr/articles/10.4064/aa-12-2-193-212/).

### Inferences

Here and below `W(T)=sum_j omega^j K_j(exp(T))`, and the actual minimizing quantities are `Q_j=K_j−e_j` with each `e_j in {0,1}`. The following argument is new to this investigation.

**Three-cutoff bound.** Suppose color `j` is an adjusted minimizer at all three cutoffs `T,T+log2,T+2log2`; ties are allowed. Rotate by the fixed factor `omega^(−j)` and write the first discrepancy as `z=x+y omega`. At any cutoff where color 0 minimizes the adjusted counts,

```
x<=1,             x−y<=1.                           (R1)
```

The unit strip errors, after this fixed rotation, have both integer linear forms `x` and `x−y` of absolute value at most one. Therefore

```
z_1=omega z+s_1,      z_2=omega^2 z+omega s_1+s_2.
```

Applying (R1) to `z_1` gives `−y<=2` and `−x<=2`. Applying it to `z_2` gives `y−x<=3` and `y<=3`. In particular

```
−2<=x<=1,        −2<=y<=3,         |W(T)|<=5.         (R2)
```

This does not assume that the isolated/patch indicator stays constant: its bounded values were included in (R1).

**Exact actual rotation sampled every three doublings.** Put `alpha=log2/log3` and `x=T/(3log3) mod1`. Direct iteration of the strip recurrence gives

```
W(T+3n log2)−W(T)=sum_(k=0)^(n−1) Phi(x+k alpha),    (R3)
Phi(x)=sum_(s=1)^3 omega^(−s) S(floor(3x+s alpha)).
```

This is the actual cocycle, not the rational periodic model. Its phase-zero sums are unbounded by the cited argument.

**Every phase is unbounded.** If the partial sums of `Phi` starting at some phase `y` were bounded by `M`, those starting at the dense orbit phases `y+r alpha` would be bounded by `2M`, by subtracting two prefixes. For every fixed length `n`, the sum is locally constant away from its finitely many discontinuities. Phase 0 never hits a breakpoint of `Phi`: each displayed breakpoint is a rational affine expression in `alpha`, and equality to `k alpha mod1` would make `alpha` rational. A dense orbit point can therefore be placed in the same continuity cell as 0 for this fixed length. Its sum equals the phase-zero sum, giving the uniform bound `2M` for every `n`, a contradiction.

**Uniform finite escape.** For every fixed `M`, there is a finite `N(M)` such that, for every phase `x`, some `n<=N(M)` has

```
|sum_(k=0)^(n−1) Phi(x+k alpha)|>M.                  (R4)
```

Otherwise take phases with arbitrarily long bounded prefixes and a convergent subsequence on the phase circle. Pass to a consistent one-sided approach at the limit. For each fixed prefix the step-function sums converge to that one-sided code. Along a fixed irrational orbit each of the finitely many breakpoints is met at most once, so the one-sided limit code differs from the chosen endpoint code by only a uniformly bounded total error for all prefix lengths. It would give a phase with bounded sums for all lengths, contradicting the previous paragraph. No bounded-discrepancy hypothesis was assumed in this compactness argument.

Now if one fixed raw color `j` were a minimizing adjusted color throughout an interval `[T0,T0+L]`, (R2) would give `|W(T)|<=5` for `T` up to `T0+L−2log2`. In particular all the prefixes in (R3) through

```
n=floor((L−2log2)/(3log2))
```

would have absolute value at most 10. Equation (R4), with `M=10`, implies

```
L < (3 N(10)+2) log2.                               (R5)
```

This is a finite bound depending on the fixed irrational slope, but **not** on `T0`. It rules out the proposed arbitrarily long fixed-raw-winner windows. The proof is non-effective here: no numerical value of `N(10)` is claimed or required for the obstruction.

### Gaps

- (R5) is an obstruction to one proposed architecture, not an infinite-return construction.
- A raw winner that rotates or switches is not covered by (R5). An unbounded cocycle can have one-sided heavy phases, so unboundedness alone must not be used to rule out a rotating-frame cone excursion.
- No explicit finite escape certificate or numerical value of `N(10)` was computed.

## Would a rotating-frame cone excursion have the right arithmetic scale?

### Takeaway

It could only help after its exact winner switches and their weighted events are controlled. A cutoff state found arbitrarily far away is insufficient: the starting logarithmic cutoff must be comparable to, and for the simplest finite-head model shorter than, the controlled window. Existing scalar heavy-point theorems supply neither the two cone inequalities nor that weighted switch description for the actual cocycle.

### Cited Findings

- The correct co-rotating dyadic frame is `V_n=omega^(−n)W(T0+n log2)`. Its increments are fixed rotation step functions, while its accumulated state is unbounded. — [Exact axis process](../boundary-and-arithmetic/arithmetic.md).
- Ralston's primary heavy-point theorem concerns the scalar `1/2`-discrepancy and nonnegative sums of one function; it identifies the strictly heavy set as a singleton. It does not assert simultaneous heaviness for the two linear forms defining our lattice cone. — [Ralston, Theorem 1 and the definition of the heavy sets](https://arxiv.org/pdf/1106.0577).
- The prior balanced-block theorem gives a positive-measure set of adjustable phases for a finite color-count return and an `O(1/q)` margin. It only proves equality at discrete cutoffs, and the saved weighted counterexample shows that endpoint equality does not equate the interval contributions. — [Balanced blocks and exact orbit segment](../../early-attacks/open-conjecture-transfer-search/168_irrationality.md), [weighted interval obstruction](../../early-attacks/open-proof-gap-attacks/weighted.md).

### Inferences

The raw recurrence rotates a large discrepancy by a cube root under each doubling. Any attempt to keep a large initial state in one cone must therefore state its rotating frame explicitly. In the frame `V_n`, the preferred **raw** color rotates by `n mod3`; the raw minimum need not remain linear between those discrete sample cutoffs. Choosing a cone for the sampled process alone does not identify where the actual minimizing color switches within each shell. Those switches are exactly where the ray local times from the first round enter the weighted calculation.

**What an adequate finite-head excursion would buy, if it existed.** Suppose one had a bounded-complexity coefficient model `rho` whose coefficients lie in a fixed finite rational alphabet and whose full weighted sum is rational with a fixed denominator, and the actual coefficients agree with it at every smooth event in

```
exp(T0)<d<exp(T0+L).
```

For example a truly fixed raw phase would give such a model: the color count and the isolated/patch changes each sum as finite geometric progressions of ratio `1/8`, plus fixed initial exceptions. The rational approximant obtained from the exact true head below `exp(T0)` and the model tail has denominator dividing a fixed multiple of

```
Lambda(T0)=2^floor(T0/log2) 3^floor(T0/log3),
log Lambda(T0)=2T0+O(1).                             (R6)
```

The elementary smooth reciprocal tail estimate gives error at most

```
C(T0+L+1) exp(−T0−L).
```

Under rationality of `Z`, clearing (R6) would give an integer error bounded by

```
C'(T0+L+1) exp(T0−L).                               (R7)
```

All cleared S-units could be chosen at least 1, and the projective height is at most `exp(2T0+O(1))`. Thus the **bound** in (R7) supplies a fixed extra exponential saving if

```
L−T0>=eta L                                         (R8)
```

for some fixed `eta>0`. Nonvanishing could then be treated separately. This is an actual height calculation, rather than an assertion that an excursion at any remote time is useful. An uncontrolled `T0/L` destroys this bound. The fixed-raw-phase version is ruled out by (R5); no suitable rotating model `rho` with the required weighted switch description was constructed.

An adjustable phase is not an independent free initial lattice state. The phase in (R3) is determined by `T0 mod 3log3`; adding `3m log3` preserves it but evolves the actual discrepancy through another unbounded cocycle. Density of the rotation orbit or mere unboundedness of the state gives no theorem that a cone excursion of length `L` can be started by `T0=O(L)` with a specified positive margin. Nor does it produce the stronger ratio (R8).

### Gaps

- No simultaneous two-inequality cone-excursion theorem with `T0=O(L)`, let alone the stronger useful ratio, was proved for the actual logarithmic cocycle.
- No phase-margin estimate for such an excursion was proved. The existing balanced-return phase margin is not an excursion margin.
- No finite arithmetic description of the rotating winner's inter-shell switches was found.
- The scalar heavy-point theorem cannot be promoted to that missing multidimensional statement.

## Do the correlated actual floor defects close the ray coefficients after all?

### Takeaway

Pairing remains essential, but it leaves a genuine actual-cocycle local-time coefficient. The degree-two interior identity has a small residual along the available returns, while retaining four semi-infinite side strips. No actual-rotation identity reducing those strips or their Hessian responses to the sole original density was obtained.

### Cited Findings

- The exact paired response is `−3 H_ij(Q)(1/d1−1/d2)`, including `H_ii`; its coefficient is a half-ray or shifted-ray local time. The exact retained-side operator identity is (W11), with its residual estimate (W12). — [First-round proof and counterexamples](weighted_returns.md).
- The scalar rational model for `p/q=53/84` has reduced denominator exactly `D/6`, so its cyclic interior relation does not by itself lower the scalar rational denominator to degree two. — [Exact skew investigation](skew_denominator.md).
- The available nonresonant Diophantine supply does not establish the degree-six model's sufficient ratio `q'/q>5+delta`. — [Diophantine supply and sharp obstruction](diophantine_supply.md).

### Inferences

In (W11), write `u=2^q,v=3^p`. The interior polynomial `u^2+uv+v^2` has logarithmic size `2q log2+o(q)`, but its exact boundary consists of

```
u^2 H_(2q)+uv H_q+uv V_p+v^2 V_(2p)−uvR.
```

The last term is an integer; the four strips are real weighted series. True/model agreement makes the remaining interior series small on the proved rectangle, but leaves these four coefficients. Pairing reciprocal floor defects converts parts of the strips into local times (W1)–(W3), with the actual contexts evolving through the same accumulated cocycles.

The discrete Hessian identities do not alone prove those coefficients rational, and the actual dynamics explored here did not add the necessary special relation. A long fixed raw phase would have killed the relevant nonlinear switches and made geometric resummation possible; (R5) shows that route cannot provide an infinite sequence. A rotating or induced return could still work, but would require an exact arithmetic description of the switches and their local-time weights, with controlled start time and height. Those obligations were not met.

**Narrow exact checks.** The companion script independently enumerates integer states `x,y in [-12,12]` and both strip errors in the seven-element superset of rotated possible unit errors; every state satisfying the three raw-minimum cone tests satisfies (R2). It also directly enumerates color counts for the 50 integer cutoffs `1,...,50`, verifying both the one-doubling recurrence and its three-doubling iteration. The hand calculation `D_3={1,2,3}` checks the color convention independently. — [Exact checker](ray_return_check.py).

### Gaps

- The requested adequate infinite-return theorem remains unproved.
- No proof that the paired ray coefficients are rational or belong to a fixed finite algebraic coefficient family under `c in Q` was obtained.
- Extra exponential saving, with the required arithmetic form and controlled height, is still missing; nonvanishing is therefore not the only issue left.
- This is a failure account for the specified attempts, not an impossibility theorem for a different return architecture.
- No Lean, dependency installation, broad scan, new density decimals, old-note edits, or external submission was performed.
