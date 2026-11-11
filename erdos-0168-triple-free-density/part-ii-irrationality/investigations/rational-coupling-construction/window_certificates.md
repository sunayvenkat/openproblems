# Window-limited signed certificates and an explicit escape test

**Status: no adequate arithmetic return is proved.** A signed combination of arbitrarily many retained annihilators cannot have a nonzero target coefficient and formally finite boundary if all multiplier shifts remain inside their known origin windows. In fact a larger algebraic degree range is still excluded. Any successful formal combination must make at least one older multiplier leave its known window by an explicit amount. One ordinary signed finite-boundary construction is exhibited beyond those windows; its complete actual residual is huge, not small. These statements leave actual-specific signed cancellation and other comparison constructions open. — [Exact followup certificate](window_certificates_check.py), [first-round classification](signed_boundaries.md).

## Can a many-scale polynomial certificate stay inside every known annihilation window?

### Takeaway

No nonzero constant evaluation is possible for the proposed class. The proof uses only the leading X degree after specializing Y=3, so it handles arbitrary signed rational coefficients and arbitrary finite depth. The exact successor is the original immediate continued-fraction successor. — [Certificate](window_certificates_check.py), [actual origin rectangles](../hybrid-arithmetic-closure/hierarchy_absorption.md).

### Cited Findings

- For the actual high array d(a,b)=c(a,b+4), the i-th annihilator L_i=S_a^(2q_i)+S_a^q_i S_b^p_i+S_b^(2p_i) vanishes on the proved rectangle a<q_i^+-q_i, b<p_i^+-p_i-4. The plus sign here denotes the original immediate successor, not the next retained scale. — [HA6 and the latest-annihilator rectangle](../hybrid-arithmetic-closure/hierarchy_absorption.md).
- Formal finite support of the weighted boundary is equivalent to P(X,3)=P(2,Y)=lambda=P(2,3). If P has integer coefficients, the remaining finite boundary is an explicit integer head. — [SB1-SB3](signed_boundaries.md).
- The followup executable checks leading-degree behavior on fixed subsets of the four known scales5/8,12/19,41/65,53/84, with their immediate successors, and three degree-endpoint patterns. The argument below, not this finite check, proves arbitrary depth. — [Certificate](window_certificates_check.py).

### Inferences

Write the retained convergents in increasing index order. Their denominators q_i are strictly increasing after discarding the initial repeated denominator1. Put

```
w_i=q_i^+-q_i>0,
L_i(X,Y)=X^(2q_i)+X^q_i Y^p_i+Y^(2p_i),
P=sum_i A_i(X,Y)L_i(X,Y),
g_i(X)=A_i(X,3).
```

All A_i are finite polynomials with nonnegative exponents, and may have rational signed coefficients. Give the zero polynomial degree minus infinity. The ordering of actual convergents implies

```
q_j^+<=q_k whenever j<k.                              (WC1)
```

This remains true when retained indices are skipped. — [Successor convention](../infinite-return-construction/diophantine_supply.md), [degree checks](window_certificates_check.py).

**Window-limited theorem, with a stronger safe range.** If every effective multiplier satisfies

```
deg g_i<2w_i,                                        (WC2)
```

and P(X,3) is constant, then every g_i is zero and that constant is zero. In particular the user's proposed actual-window condition deg_X A_i<w_i implies the conclusion. Even the weak endpoint deg_X A_i<=w_i remains inside the excluded algebraic range. The larger range(WC2) is an algebraic strengthening; shifts w_i<=a<2w_i are not asserted to lie in the actual zero window. — [Certificate and endpoint tests](window_certificates_check.py).

**Proof.** Suppose some g_i is nonzero, and let k be the largest active retained index. Its contribution to P(X,3) has degree

```
D_k=deg g_k+2q_k>=2q_k,
```

because L_k(X,3) is monic of degree2q_k. For every earlier active j, (WC1)-(WC2) give

```
deg[g_j L_j(X,3)]<2w_j+2q_j=2q_j^+<=2q_k.
```

Thus the leading term of the latest active contribution cannot cancel. The restriction is nonconstant, a contradiction. Terms whose A_i(X,3) vanish contribute nothing to this specialization and have already been excluded from the active set. This proves the claim, regardless of their raw bidegrees. — [Exact polynomial verification](window_certificates_check.py).

**The weak doubled endpoint.** If only deg g_i<=2w_i is assumed, a cancellation of the largest active contribution requires all of the following: deg g_k=0; some earlier active j is its immediate original predecessor, q_j^+=q_k; and deg g_j=2w_j. These are necessary leading-degree conditions, not sufficient for a constant identity. If no two active indices are adjacent, the theorem still holds at this weak doubled endpoint. In particular it holds for the retained scales separated by at least four steps in the existing hierarchy. — [Same leading-degree proof](window_certificates_check.py), [retained-scale spacing](../hybrid-arithmetic-closure/adaptive_induction.md).

Rational coefficients do not evade the argument: a common positive integer clearing all coefficients preserves both the effective degrees and the constant-restriction condition. Its denominator must still be charged in any arithmetic application. — [Coefficient-clearing scope](signed_boundaries.md).

### Gaps

- This is a theorem about formal polynomial certificates and their known origin windows. It does not prove that an actual weighted residual is nonzero, irrational, or large whenever a multiplier leaves a window. — [Actual arithmetic gap](../hybrid-arithmetic-closure/hierarchy_absorption.md).
- It does not cover negative-index extensions, an identity valid only on the actual array, state-dependent cancellation, or a different rational matching construction. — [First-round scope](signed_boundaries.md).
- Vertical degree bounds were not needed. Imposing the actual vertical windows only narrows this already excluded class. — [Actual rectangles](../hybrid-arithmetic-closure/hierarchy_absorption.md).

## How far must an older multiplier escape, and what real estimate is then missing?

### Takeaway

The leading-degree argument gives an explicit necessary overshoot for every nonzero constant restriction. At least one older effective coefficient must have degree at least twice the separation to the largest active denominator. The existing rectangle-annihilation proof then supplies no positive origin-width estimate for that term. This loss does not rule out a separate signed real estimate. — [Proof and exact example](window_certificates_check.py).

### Cited Findings

- A positive shift of width a consumes that much of an available origin zero interval. The prior real hierarchy explicitly paid all older maximum shifts before asserting its remaining rectangle. — [HA6-HA8](../hybrid-arithmetic-closure/hierarchy_absorption.md).
- Direct finite-boundary signed combinations can exist outside the windows; the two-adjacent-annihilator cost theorem bounds their universally cleared coefficient. — [SB4-SB5](signed_boundaries.md).

### Inferences

Suppose P(X,3)=lambda!=0 and choose the largest active k as above, without assuming(WC2). The coefficient at degree D_k=deg g_k+2q_k must be canceled by at least one older term. That term has degree at least D_k. Hence for some j<k,

```
deg g_j>=deg g_k+2(q_k-q_j)
        =deg g_k+2w_j+2(q_k-q_j^+).                  (WC3)
```

Since q_k-q_j^+>=0, this coefficient has degree at least2w_j+deg g_k. Its excess over the available origin width is at least

```
deg g_j-w_j>=deg g_k+2q_k-q_j-q_j^+>0.              (WC4)
```

If the retained scales are not adjacent, q_k>q_j^+, so the overshoot beyond twice the old window is strict. Specialization cannot increase the raw X degree, so an actual monomial of A_j has X exponent at least this large. — [Exact degree calculation](window_certificates_check.py).

The standard support argument for A_j L_j d can only preserve an origin horizontal width w_j-deg_X A_j. Equation(WC3) makes that nonpositive for the required older term. The local annihilation theorem therefore cannot by itself show that term has an exponentially late first support. A signed combination may still have cancellation after summation, or the actual array may satisfy additional identities; such an estimate would be a new theorem, not a consequence of the individual windows. — [Original support argument](../hybrid-arithmetic-closure/hierarchy_absorption.md).

### Gaps

- Effective degree constraints do not bound the best possible signed scalar cancellation outside the windows. No universal lower bound on actual residual magnitude follows from(WC3). — [Scoped window result](window_certificates_check.py).
- A family with a different real saving might tolerate larger coefficients or clearing factors. The existing no-extra-hypothesis supply does not establish that saving. — [Current proved cost interface](../infinite-return-construction/diophantine_supply.md).
- Additional low-row and boundary identities still have to be proved together for the full target Z. — [Full target identity HA10](../hybrid-arithmetic-closure/hierarchy_absorption.md).

## Does one explicit beyond-window signed construction retain a small actual residual?

### Takeaway

One fully specified ordinary signed combination does achieve a finite integer boundary for the high array. It uses a162-bit target factor at the pair5/8,12/19, and its complete actual residual has magnitude greater than699752*2^64. It is an explicit failed repair, not a general impossibility result. — [Complete construction and exact actual-tail certificate](window_certificates_check.py).

### Cited Findings

- The first note constructs integer Laurent coefficients A_L,B_L for the fixed P0=-X^3Y^3+27X^3+8Y^3-34, with P0=A_L L_(5,8)+B_L L_(12,19). Its balanced construction has no negative Y exponents. — [SB6-SB8](signed_boundaries.md), [coefficientwise certificate](signed_boundaries_check.py).
- Swapping variables and the two generators gives another balanced Laurent representation of P0 with no negative X exponents. The new checker reconstructs and verifies both polynomial identities coefficientwise. — [Certificate](window_certificates_check.py).
- The only actual digit routine used here is the earlier standalone exact finite-count implementation; its dependency is imported explicitly. The followup adds no new floor conventions or low-row readout assumptions. — [Dependency](signed_boundaries_check.py), [followup](window_certificates_check.py).

### Inferences

Let the opposite Laurent representation be P0=A_R L_(5,8)+B_R L_(12,19). Multiplying the first representation by X^M and the second by Y^N makes their coefficients ordinary integer polynomials. The exact balanced representations in this example give

```
M=78,               N=48.
```

The asserted one-sided nonnegative supports follow directly from the balanced paths: for the X-inverse path the current Y exponent is three times a nonnegative remainder, and a U^3 step occurs only when that remainder is at least p; its subtracted3p stays nonnegative. For the Y-inverse path the determinant-one identity gives the same assertion with the corresponding remainder. Swapping variables yields the other orientation. The checker also verifies the nonnegative supports explicitly. — [Path formulas](signed_boundaries.md), [support assertions](window_certificates_check.py).

Define

```
T=X^M Y^N-3^N X^M-2^M Y^N,
P=P0*T,
A=(Y^N-3^N)X^M A_L-2^M Y^N A_R,
B=(Y^N-3^N)X^M B_L-2^M Y^N B_R.
```

Then P=A L_(5,8)+B L_(12,19) is an ordinary integer polynomial combination. Moreover

```
T(X,3)=T(2,Y)=-2^M3^N,
P(X,3)=P(2,Y)=lambda=-182*2^78*3^48.                 (WC5)
```

Thus its high-array boundary is a finite integer head by(SB1)-(SB3). The absolute value of lambda has162 bits; no small-evaluation or uncharged Laurent coefficient is being substituted for it. — [Exact ordinary combination and restrictions](window_certificates_check.py).

After specializing Y=3 the effective multiplier degrees are

```
deg A(X,3)=62,          deg B(X,3)=40.
```

The actual origin widths are11 for5/8 and46 for12/19. The latest multiplier fits its horizontal width, while the older one does not, and the degree necessity is attained exactly:

```
62=40+2*(19-8).                                     (WC6)
```

This is a complete finite-boundary example illustrating why the largest-window argument cannot simply ignore its older coefficient. — [Exact degree assertions](window_certificates_check.py).

**The real residual fails.** For this P and the actual d(a,b)=c(a,b+4), the full infinite enclosure proves

```
-699753*2^64 < W(Pd) < -699752*2^64.                 (WC7)
```

The checker sums W(Pd) on a<28,b<20, using actual digits at every shifted point. With v=2^(-28)+3^(-20)-2^(-28)3^(-20), the omitted weighted region has total weight3v. Since |Pd|<=2 sum|p_AB|, its entire omitted contribution has magnitude at most6v sum|p_AB|. Adding this explicit two-sided error gives(WC7), including strict coarse dyadic endpoints. This is a bound on the full weighted residual, not merely one nonzero coefficient or finite sample. — [Tail-bound implementation and assertion](window_certificates_check.py).

The high-array identity lambda W(d)=integer+W(Pd) is therefore arithmetically exact but has no useful small cleared error in this example. The full target additionally contains the true low-row term81lambda L_0; it has not been evaluated by this construction. Neither a strong real estimate nor a cheap full-target numerator has been obtained. — [High-array boundary theorem](signed_boundaries.md), [low-row relation](../hybrid-arithmetic-closure/hierarchy_absorption.md).

### Gaps

- One failed explicit signed repair does not exclude all coefficients beyond the known windows. A different real cancellation, actual-state relation or nonlinear matching construction remains possible. — [Scope of(WC3)](window_certificates_check.py).
- No adequately small real residual with a cheap rational full boundary, and no infinite nonvanishing theorem for such a family, is proved here. The requested goal remains active and unmet. — [Current frontier](../hybrid-arithmetic-closure/hierarchy_absorption.md).
- Skipped: Lean, broad scans, installs, archived edits, density decimals, external posting and priority assessment. The material risk is promoting an algebraically finite boundary to an adequate actual return while omitting the outside-window residual, coefficient cost, or remaining low rows.
