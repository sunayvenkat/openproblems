# Coupled weighted defects and the remaining side-tail obstruction

**Status, 7 November 2026: no adequate infinite-return construction has been proved.** The new exact result is a joint order-swap response, including its same-color term. It reduces coupled horizontal/vertical floor defects to weighted local times on rays of the count-state lattice. A finite-dimensional translation closure or an exact weighted boundary resummation does **not** follow from the minimum identities. In particular, nonvanishing is not the only residual obligation: the fixed or sufficiently controlled arithmetic coefficients and the additional exponential saving are still missing.

The global finite formula (C) is now established by the separate prefix-and-phase work. Earlier arithmetic notes called it conditional; their algebra may now use that proved input. Nothing here changes or independently re-audits that finite proof. — [Current finite result](../prefix-and-phase-audit/REPORT.md).

## What is the exact response of a coupled floor-order defect?

### Takeaway

The correct paired response is a discrete Hessian of the minimum, multiplied by a difference of **two** reciprocal weights. Distinct-color swaps give double-minimum ray local time; same-color swaps also matter and give a diagonal Hessian. Thus resonance of the rational crossing does not automatically extend weighted birth agreement.

### Cited Findings

- The separated actual state is the sum of the two accumulated axis cocycles plus the residue correction, and the birth is a cone test on that state, with the bounded indicator correction included. The cocycles themselves remain unbounded. — [Exact arithmetic reduction](../boundary-and-arithmetic/arithmetic.md), [independent review](../boundary-and-arithmetic/arithmetic_review.md).
- The existing double-return formula leaves two infinite weighted side series. Its periodic model uses periods `P=3q,Q=3p` and denominator `27(2^P−1)(3^Q−1)`. — [Exact return and model identities](../../early-attacks/augmentation-and-return-attacks/returns.md).

### Inferences

The following is an elementary exact calculation, proved here. Put

```
m(Q)=min(Q_0,Q_1,Q_2),    D_i m(Q)=m(Q+e_i)−m(Q).
```

Consider two adjacent vertex insertions at physical weights `d1,d2`, with colors `i,j`. Assume no correction indicator changes at either insertion or across the swap. This condition holds for an isolated swap of vertices whose three-exponents avoid `0,1,3`; swaps involving those low rows require the actual indicator event and are not covered by this formula alone. Let `Q` be the adjusted count vector immediately before the pair. In the order `d1,d2`, the two increments are

```
eta(d1)=D_i m(Q),       eta(d2)=D_j m(Q+e_i).
```

In the reversed order they are

```
eta'(d1)=D_i m(Q+e_j),  eta'(d2)=D_j m(Q).
```

Consequently, with `H_ij=D_i D_j m`,

```
sum eta'/d − sum eta/d = H_ij(Q)(1/d1−1/d2),
sum c'/d   − sum c/d   = −3 H_ij(Q)(1/d1−1/d2).       (W1)
```

This identity includes the diagonal `i=j` case. Direct evaluation gives

```
i≠j: H_ij(Q)=1_[Q_i=Q_j<Q_k], where {i,j,k}={0,1,2};
i=j: H_ii(Q)=−1_[Q_i+1=min(Q_j,Q_k)].                 (W2)
```

Thus an off-diagonal response is supported on one half-ray in the state lattice modulo common translation. A diagonal response is supported on two shifted half-rays and their shared endpoint.

**Correction of a tempting but false argument.** A same-color swap preserves the sequence of color-count vectors **by rank**, but can change which physical vertex receives the increment. At the abstract fixed-indicator state `Q=(0,1,2)`, two color-0 insertions have increments `(1,0)`. For symbolic distinct same-color physical weights `d1,d2`, swapping the insertion order changes the weighted increment sum from `1/d1` to `1/d2`. This is an abstract local calculation, not an exhibited adjacent smooth-board pair. Therefore a resonant mediant, or any same-color inversion family, cannot simply be deleted from a weighted comparison. I initially proposed that deletion during this investigation and withdrew it after the coordinator supplied this counterexample.

For a primitive inversion family

```
d1=2^f d,    d2=3^g d,    d=2^a3^b,
```

the exact paired contribution, whenever those swaps are legitimately realized as adjacent swaps, has the form

```
−3(2^(−f)−3^(−g))
   sum_(a,b in the family) H_(i(a,b),j(a,b))(Q_(a,b))/(2^a3^b).   (W3)
```

For a finite reordering, bubble-sort into adjacent transpositions and sum (W1), evaluating each Hessian in its **current** pre-swap context. This gives a rigorous finite identity without assuming that the original inversion pairs were already adjacent. The resulting context need not equal the original cone state; that distinction must not be suppressed when proposing an infinite formula. Absolute summation over infinitely many swaps additionally needs a convergence or truncation argument.

The primitive factor does not itself give an additional exponential saving. For convergent or bounded-combination pairs with `f log2−g log3=O(1/q)`,

```
|2^(−f)−3^(−g)|
 = 2^(−f)|1−exp(f log2−g log3)|
 = O(2^(−f)/q).                                      (W4)
```

This is a polynomial improvement over a single reciprocal, whereas the target requires a further fixed exponential improvement relative to the smallest unit and the arithmetic height.

### Gaps

- (W3) is a paired local-time reduction, not an evaluation of its coefficient series as rational numbers or fixed rational-coefficient S-unit forms.
- A full infinite comparison must organize all adjacent transpositions, including their changing contexts and the low-row indicator events. No such infinite organization with the required arithmetic bounds is proved here.
- Neither the nonresonance of a convergent nor the resonance of a first floor defect settles these weighted local times.

## Do the minimum identities give a finite module or a weighted Tanaka cancellation?

### Takeaway

The exact minimum identities partition the count states into cones, rays, and triple ties; they do not make the ray coefficients rational under the sole assumption that the original density is rational. The state-translation module is infinite-dimensional. Weighted telescoping on a periodic model retains its whole period denominator and numerator.

### Cited Findings

- The required arithmetic theorem fixes its coefficient vector and number of S-unit coordinates. A new unknown real local-time coefficient cannot be inserted merely because it is well-defined. — [Kohlmeyer–Kruer, Proposition 7.4 and its application](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf), [saved primary manuscript](../Erdos%20theorem%20transfer%20investigation/erdos1062-fork-free-density.pdf.txt).
- Existing Hecke–Mahler results treat polynomial functions of floor sequences or sequences satisfying an explicit sparse-difference condition. They do not state that arbitrary half-ray codings of an accumulated planar cocycle have a finite arithmetic boundary reduction. — [Luca–Ouaknine–Worrell, primary paper](https://people.mpi-sws.org/~joel/publications/hecke-mahler25.pdf).

### Inferences

**Exact identities.** Write `T_i=1+D_i`. Since

```
T_0 T_1 T_2 m=m+1,
```

we have

```
D_0 D_1 D_2 m(Q)=1_[Q_0=Q_1=Q_2],                   (W5)

sum_i D_i m(Q)+sum_(i<j) H_ij(Q)
 +1_[Q_0=Q_1=Q_2]=1.                               (W6)
```

For (W5), apply `D_2` to `H_01=1_[Q_0=Q_1<Q_2]`; it changes only when all three coordinates are equal. Equation (W6) is also the explicit partition into a unique minimum, exactly two tied minima, and three tied minima.

**No finite-dimensional state-translation closure.** Restrict the translates of `H_01` to `Q=(0,0,t)`. Then

```
H_01(Q+n e_2)=1_[t+n≥1].                            (W7)
```

Every finite collection of these functions with distinct integer `n` is linearly independent: its members have distinct single jump locations, so taking the difference across each jump forces the corresponding coefficient to vanish. Therefore a finite-dimensional vector space of state functions that contains `H_01` cannot be stable under all integer state translations. The common-translation identity only removes the `(1,1,1)` direction; it does not remove this obstruction in the remaining state plane.

This does not rule out a special identity after evaluation on the actual logarithmic cocycle, nor a finite set of shifts tailored to one return. It does rule out claiming general finite closure from (W5)–(W6).

**Rationality does not propagate by these identities alone.** Choose an arbitrary binary word `x_a` and the additively separated artificial count state

```
Q(a,b)=(0,0,x_a).
```

For every `a,b`, `D_0 m(Q(a,b))=0`, so its original cone/birth readout has rational weighted sum (the corresponding `c=1` sum is exactly `3`). But

```
H_01(Q(a,b))=x_a,
sum_(a,b≥0) H_01(Q(a,b))/(2^a3^b)
  = (3/2) sum_(a≥0) x_a/2^a.                        (W8)
```

For example, choose `x_a=1` precisely at positive square indices. Its binary expansion is not eventually periodic, so (W8) is irrational. This example is not the actual rotation cocycle: it is a proof that additive separation, the minimum identities, and rationality of one weighted birth readout do not by themselves imply rationality of the new ray coefficients. Any successful transfer must use further special arithmetic of the actual axis cocycles.

**What weighted telescoping actually costs.** For a `P`-periodic ray word `h_a`, the unique `P`-periodic solution of

```
h_a=2 G_a−G_(a+1)
```

is

```
G_a = [sum_(j=0)^(P−1) 2^(P−1−j) h_(a+j)]/(2^P−1). (W9)
```

Then `sum_(a≥0)h_a2^(−a)=2G_0`. This is exact weighted cancellation, but the transfer value stores the entire period numerator and keeps its denominator. A nonzero nonnegative ray occupation on a closed periodic state cycle cannot be an ordinary unweighted coboundary, because its sum over that cycle is positive.

Likewise solving `(2−S_a)(3−S_b)G=h` on a `P`-by-`Q` periodic tile gives denominator dividing

```
(2^P−1)(3^Q−1),
```

and the numerator is the weighted full tile. Thus a proposed two-dimensional weighted Tanaka identity must prove an additional cancellation; merely moving the tile numerator into a transfer function does not improve the arithmetic height.

### Gaps

- No finite module of **actual** cocycle-evaluated density constants was proved.
- No identity deriving the ray or point local-time coefficients from the sole hypothesis `c in Q` was found.
- An exact periodic transfer function exists, but its numerator can have exponential height; calling it a boundary value does not make it an admissible fixed coefficient.

## Does finite-defect renormalization already give the required infinite construction?

### Takeaway

A fixed multiple of a convergent length contains only boundedly many floor defects, but a defect persists as a state translation and its weighted paired response is an entire local-time series. The rational preperiod construction or the periodic resolvent reintroduces the missing arithmetic cost. The full infinite-return objective remains unproved.

### Cited Findings

- The current periodic model matches both axis floor words through `q+q′−1` and `p+p′−1`; clearing its denominator costs `6q log2+o(q)`. Its established sufficient supply condition remains `q′/q>5+delta`. — [Model, exact matching theorem, and height bound](../../early-attacks/augmentation-and-return-attacks/returns.md).
- The aligned skew identity supplies a genuine degree-two **interior annihilator**, but the separately computed `53/84` scalar model still has reduced denominator `D/6`, nearly the full degree-six denominator. Therefore the interior annihilator is not a global scalar denominator reduction. — [Sibling skew investigation](skew_denominator.md).
- The companion Diophantine investigation provides unconditional nonresonant return supply below the much larger threshold needed by that degree-six model. — [Sibling Diophantine investigation](diophantine_supply.md).

### Inferences

**Bounded floor-defect count.** Fix `C>0`, take a convergent `p/q` with next denominator `q′`, and set `epsilon=alpha−p/q`. For `1≤n≤Cq`,

```
|n epsilon|<C/q′.
```

Once `q′>C`, a non-tie floor disagreement can occur only when the rational grid residue `np mod q` is within `Cq/q′≤C` integer grid positions of the relevant endpoint of the unit interval. There are at most `ceil(C)` such residue classes and each occurs at most `ceil(C)` times in this index range. The exact-tie multiples of `q` are handled correctly by the one-sided convention and have displacement below one. Thus there are at most `ceil(C)^2` floor mismatches. The reciprocal floor word has the same bound with `p,p′`. This is a fixed-complexity description on any chosen fixed multiple of a return length.

A single such mismatch alters one cocycle increment, and therefore shifts the **accumulated** axis state on every subsequent index until another defect. In a finite window, the axis correction is a piecewise constant lattice vector with boundedly many pieces. Pairing reciprocal defects improves the description to (W1)–(W3); it does not make their context indicators disappear.

**Why a direct rational patch does not finish.** If a periodic model is changed after an index `f` and stays in the new periodic state, its weighted sum acquires a factor `2^(−f)` times a periodic-model value. A vertical patch similarly acquires `3^(−g)`. Combining both generally requires an S-preperiod factor `2^f3^g`, in addition to the period denominator. Equivalently, keeping a bounded number of separate patch values creates a bounded number of **variable exponential-height tile numerators** as coefficients. Neither representation has the fixed rational coefficient input of Proposition 7.4. The near equality of the paired weights contributes the factor (W4), which supplies only polynomial saving.

There is a sharper exact algebraic relation in the high-column rational model. After the correct affine recentering, its aligned skew covariance implies

```
c~(a+2q,b)+c~(a+q,b+p)+c~(a,b+2p)=0.                (W10)
```

The weighted interior polynomial is `u^2+uv+v^2`, for `u=2^q,v=3^p`; its logarithmic size is only `2q log2+o(q)`. If its two side-boundary generating functions admitted a joint fixed-coefficient compression, this cost would be compatible with the available ordinary-convergent matching windows. But (W9), the ray-translation independence, and the actual full scalar denominator show why that compression cannot simply be assumed. This is the exact remaining place where a new construction would have to outperform the current model.

**Exact retained sides for (W10).** To avoid absorbing the exceptional low rows, put `d(a,b)=c(a,b+4)` and define

```
D=sum_(a,b≥0) d(a,b)/(2^a3^b),
H_r=sum_(0≤a<r,b≥0) d(a,b)/(2^a3^b),
V_s=sum_(a≥0,0≤b<s) d(a,b)/(2^a3^b),
R=sum_(0≤a<q,0≤b<p) d(a,b)/(2^a3^b),
L d(a,b)=d(a+2q,b)+d(a+q,b+p)+d(a,b+2p).
```

Absolute convergence and three separate index shifts give, for **any** bounded array `d`,

```
(u^2+uv+v^2)D
 = u^2 H_(2q)+uv H_q+uv V_p+v^2 V_(2p)−uv R
   +sum_(a,b≥0) Ld(a,b)/(2^a3^b).                   (W11)
```

The corner `uvR` is an integer for integer `d`; every `H` and `V` displayed here is still a semi-infinite weighted side strip. For the rational model, (W10) makes the last series zero. The actual total is its four low-row series plus `D/81`; none of those row series has been silently evaluated.

For the actual array, agreement with the model on `a<N=q+q′, b<M=p+p′` proves `Ld=0` whenever `a<R_A=q′−q` and `b<R_B=p′−p−4`, provided these ranges are positive. Since `|Ld|≤6`, the explicit remaining-series bound is

```
|sum Ld/(2^a3^b)|
 ≤18(2^(−R_A)+3^(−R_B)−2^(−R_A)3^(−R_B)).           (W12)
```

This is a real small residual along the supplied long returns, but (W11) is not yet an arithmetic linear form: its weighted side strips are unknown real coefficients. Equation (W12) must not be presented as a completed extra-exponential rational approximation.

**Small independent exact checks.** An inline standard-library Python check evaluated all `Q in {-2,-1,0,1,2}^3` and all nine ordered color pairs. It checked (W1) against the two physical insertion orders, (W2) against its explicit support conditions, and (W5)–(W6) independently. Results: `1125` swap checks, `125` triple/partition checks, and the same-color counterexample all passed. For each size `1,...,8`, distinct ray translates in (W7) were checked by a difference matrix equal to the identity. A separate finite rational-array check verified (W11), its corner integrality, and all signs for `(q,p)=(1,1),(2,1),(1,3),(3,2)`. All `62` binary periodic words of lengths at most five independently verified (W9) and its weighted-sum endpoint. No new persistent script, dependency, old-file edit, finite optimization scan, or density decimal was produced.

### Gaps

- The desired infinite sequence with fixed or adequately controlled coefficients, height `exp(O(L))`, and additional exponential error has not been constructed.
- The construction is not complete up to nonvanishing: the side local-time coefficient reduction and the exponential estimate still fail to close.
- No assertion that such a construction is impossible is made. The negative conclusions concern the specific universal translation, direct periodic-resolvent, and direct finite-preperiod repairs analyzed above.
- No Lean, external submission, dependency installation, broad scan, or new decimal calculation was attempted.
