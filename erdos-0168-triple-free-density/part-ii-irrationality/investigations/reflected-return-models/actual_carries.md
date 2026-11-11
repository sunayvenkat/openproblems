# Actual-array carries: one exact forbidden motif, but no arithmetic closure

**Status: the adequate infinite weighted-return construction remains unproved.** This round proves a genuine local constraint on the actual array: for every `a>=0,b>=4`, the four birth digits at `d,2d,3d,6d` cannot be `1001` in that order. Every other binary four-cell motif occurs in the actual array. Both directions of the three-cell carry and both directions of the four-cell carry therefore occur, including well above the exceptional low columns. The one forbidden motif does not give canonical normalization or irrationality: an explicit rational, nonperiodic countermodel obeys it, can retain any finite actual head, and can have the full fifteen-motif language. This countermodel does **not** reproduce the full actual floor/cocycle constraints. — [Finite optimum theorem](../prefix-and-phase-audit/REPORT.md), [exact certificate](actual_carries_check.py).

## What constraints do the actual four-cell states satisfy?

### Takeaway

The actual corrected states have a unit mixed curl and a three-element horizontal edge alphabet. Those two exact facts already exclude `1001`, without bounding the accumulated cocycle state. An additional six-element vertical alphabet follows from a five-interval dyadic-mantissa partition and retains both exceptional-root types. — [State derivation](../boundary-and-arithmetic/arithmetic.md), [certificate](actual_carries_check.py).

### Cited Findings

- The proved finite formula is `tau(t)=min_j(K_j(t)-I_j(t)-P_j(t))`; the isolated root has `2t/3<e<=t`, and the patch root has `6e<=t<27e/4`, with dyadic `e>=2`. There is at most one active exceptional root. — [Finite theorem and intervals](../prefix-and-phase-audit/REPORT.md).
- For `b>=4`, the actual rotated corrected state is
  `z_ab=A_a+B_b-1+C_ab-E_b`, with
  `C_ab=(1-omega^(-a))(1-omega^(-2b))/3` and `omega^2+omega+1=0`.
  If `z=x+y omega`, then the birth digit is
  `F(z)=1_{x<=0, x-y<=0}`. The accumulated states `A,B` remain unbounded. — [Exact separation and cone convention](../boundary-and-arithmetic/arithmetic.md), [unconditional use after finite proof](../infinite-return-construction/REPORT.md).
- The narrow certificate directly constructs actual digits from the proved finite formula through `6*2^13*3^25`, independently cross-checks the fifteen witnesses by complete-row counting, verifies tiny cover optima by brute force through cutoff36, and checks the finite edge tables and carry examples exactly. No decimal density is calculated. — [Certificate](actual_carries_check.py).

### Inferences

**Exact unit curl.** Put `j=a-b mod3` and write `z,z10,z01,z11` for the corrected states at `d,2d,3d,6d`. The separated `A,B,E` contributions cancel from the mixed difference, while

```
C_(a+1,b+1)-C_(a+1,b)-C_(a,b+1)+C_(a,b)
 = omega^(-a-2b) (1-omega^(-1))(1-omega^(-2))/3
 = omega^(-j).
```

Consequently

```
z11=z01+u+r,        z10=z+u,        r=omega^(-j).       (AC1)
```

This is valid for all integer contexts reached by the actual process; it does not replace that process by a finite-state one. — [Separation identity](../boundary-and-arithmetic/arithmetic.md), [symbolic certificate](actual_carries_check.py).

**Horizontal edge.** Doubling the cutoff rotates the raw color-count discrepancy by `omega`, with the vertical-axis strip
`S_m=sum_{h=0}^m omega^(2h)`, where `m=floor(log_3(2d))`. Its three possible values are `1,-omega,0`. Doubling an active exceptional root doubles its dyadic root and rotates its color by exactly the same amount as the inserted point; its rotated correction is therefore unchanged. Thus

```
u=omega^(-j-1)S_m.
```

In the coordinate convention `omega=(0,1)`, this gives the complete allowed alphabets

| j | r | u |
|---|---|---|
|0|1|`0, omega^2, -1`|
|1|omega^2|`0, omega, -omega^2`|
|2|omega|`0, 1, -omega`|

The table does not assert that the three choices occur at every fixed index; the actual strip floor chooses one. — [Exact strip recurrence](../infinite-return-construction/ray_return_attack.md), [certificate](actual_carries_check.py).

**Forbidden-motif theorem.** Suppose `F(z)=1,F(z10)=0,F(z01)=0,F(z11)=1`.

- For `j=0`, both nonzero possible `u` weakly decrease each cone form `x` and `x-y`, so they cannot move an inside point outside.
- For `j=1`, `u=0` cannot leave, and `u=omega` weakly decreases the two forms. The only remaining possibility is `u=-omega^2`, but then `u+r=0`, giving `z11=z01`, a contradiction.
- For `j=2`, `u=0` cannot leave. If `u=-omega`, then `u+r=0` again. If `u=1`, then `u+r=-omega^2=(1,1)`, which weakly increases both forms; it cannot move an outside point inside.

These are all cases, so `1001` is impossible. In particular, `j=0` gives the stronger residue-specific implication `eta(2d)>=eta(d)`. The proof is over every integer state, with no compactness or sampling assumption. — [Exact edge/curl certificate](actual_carries_check.py).

**Vertical edge, retaining the actual exceptions.** Let `A=floor(log_2 d)`, `s=d/2^A in[1,2)`, and `k=A-j mod3`. The exceptional-root vector relative to the inserted color is

```
E(s,k)=omega^k        for 1<=s<3/2,
       omega^(k+1)    for 3/2<=s<27/16,
       0              for 27/16<=s<2.                (AC2)
```

The second interval is exactly the patch with root `2^(A-2)`; its root is valid here because `b>=4`. Set `h=1` for `s<4/3` and `h=2` otherwise, and let `P_n=sum_{ell=0}^n omega^ell`, which has values `1,-omega^2,0` according to `n mod3`. The horizontal-axis strip under tripling gives the exact increment

```
v=z01-z
 =omega^(1-j) P_(j+k+h)+E(s,k)-E(3s/2^h,k+h+1).     (AC3)
```

All terms in (AC3) are constant on the five left-closed intervals with endpoints
`1,9/8,4/3,3/2,27/16,2`. For `s<4/3`, the new exceptional vector is `omega^k` precisely when `s<9/8`; for `s>=4/3`, it is always `omega^k`. Evaluating the three `k` classes gives, in `(x,y)` coordinates,

|j|Possible v|
|---|---|
|0|`(-1,-1),(-1,0),(-1,1),(0,0),(0,1),(1,1)`|
|1|`(0,-1),(0,0),(0,1),(1,0),(1,1),(2,1)`|
|2|`(-1,-2),(-1,-1),(-1,0),(0,-1),(0,0),(1,0)`|

This table is a necessary local alphabet, not an assertion that `u,v` may be assigned independently along an actual orbit. — [Exceptional-root definitions](../prefix-and-phase-audit/REPORT.md), [five-interval exact certificate](actual_carries_check.py).

**Low events must remain separate.** At `2^a` with `a>=1`, insertion of the dyadic point is cancelled in the adjusted count by the new isolated-root indicator, giving `eta=0`; at the origin `a=0`, `eta_0,0=0` directly because no corner exists. At `3*2^a`, `a>=2`, the isolate `2^(a+1)` disappears while the patch `2^(a-1)` appears: insertion cancels the new patch coordinate, leaving a unit increase in a different adjusted color. At `27*2^a`, the patch `2^(a+2)` disappears, while the new point increases another color. For the uncorrected rotated state `x+y omega`, the exact low-column readouts are therefore

|b|eta_ab|
|---|---|
|0|`0`|
|1|`1_{x>=1,y>=0}`, except `eta_0,1=1`|
|2|`1_{x<=-1,x-y<=0}`|
|3|`1_{min(x,0)<=y}`|

The exceptional readout at3 is retained explicitly. The would-be patch roots at cutoff6 (`a=1`) and cutoff3 (`a=0`) are1 and1/2, respectively, so neither is an admissible patch root. These are exactly the existing audited low-column rules, now interpreted using the proved finite optimum. The `b>=4` theorem above does not discard or absorb them. — [Complete low-column table](../infinite-return-construction/REPORT.md), [small exact checks](actual_carries_check.py).

### Gaps

- The state curl and finite edge alphabets do not bound the actual state, determine the number or timing of ray crossings, or imply a finite translation module.
- No invariant involving the actual floor selections that is strong enough to control all future carries was proved. The isolated forbidden motif is only a necessary condition.

## Do these actual local constraints prevent the arithmetic carries?

### Takeaway

No. The exact actual array contains fifteen of the sixteen four-cell binary patterns, including all endpoints of both elementary carries. Even the no-`1001` condition can survive an actual local carry. A rational nonperiodic countermodel shows why that condition, the full fifteen-pattern language, and any finite actual head still fall short of irrationality. — [Exact certificate](actual_carries_check.py).

### Cited Findings

- At `x=1/2,y=1/3`, `x-y-xy=0` and `1-x-y-xy=0`; equivalently `1/(2d)=1/(3d)+1/(6d)` and `1/d=1/(2d)+1/(3d)+1/(6d)`. Thus binary three-cell patterns `100<->011` and four-cell patterns `1000<->0111` have identical weighted mass. — [Exact rational checks](actual_carries_check.py).
- The following actual witnesses use the order `d,2d,3d,6d`; all have `b>=4`. The table comes from exact integer arithmetic and the proved finite formula, not floating logarithms or a rational-slope model. — [Certificate](actual_carries_check.py), [finite theorem](../prefix-and-phase-audit/REPORT.md).

|Pattern|a|b|d|
|---|---:|---:|---:|
|0000|2|4|324|
|0001|4|5|3888|
|0010|1|4|162|
|0011|7|5|31104|
|0100|4|6|11664|
|0101|8|4|20736|
|0110|13|25|6940988288557056|
|0111|8|5|62208|
|1000|2|6|2916|
|1010|18|4|21233664|
|1011|0|4|81|
|1100|1|6|1458|
|1101|8|6|186624|
|1110|0|6|729|
|1111|0|5|243|

### Inferences

**Actual carry surviving the one forbidden motif.** At `d=486=2*3^5`, the actual three digits at `972,1458,2916` are `0,1,1`. Replacing them by `1,0,0` preserves the total weighted sum exactly. Every adjacent four-cell square affected by this modification still avoids `1001`; the remainder of the array is unchanged. Hence no-`1001` alone does not give a unique representation even starting from the actual array. The modified array is not asserted to arise from the actual min-birth formula or to preserve the stronger residue-specific transition rule. — [Exact affected-square and weighted-mass checks](actual_carries_check.py).

**Rational, nonperiodic countermodel with the same sole forbidden motif.** For each `k>=0`, choose either of the following row pairs at `b=2k,2k+1`:

```
Type A: eta_(a,2k)=0,         eta_(a,2k+1)=1,     for all a.
Type B: eta_(a,2k)=a mod2,    eta_(a,2k+1)=0,     for all a.
```

Their masses agree, since

```
Type A: sum_a 2^(-a) 3^(-2k-1)=2*3^(-2k-1),
Type B: sum_(a odd) 2^(-a) 3^(-2k)=(2/3)*3^(-2k).
```

The entire sum is therefore exactly
`sum_k (2/3)*9^(-k)=3/4`, for **every** sequence of choices. An explicitly nonperiodic choice, for example choosing B precisely at square indices, gives a nonperiodic array. — [Exact mass and all boundary-pattern checks](actual_carries_check.py).

Inside pairs the possible four-cell motifs are `0011,0100,1000`; across pair boundaries they are `1100,1101,1110,0000,0001,0010`. None is `1001`. This exhausts the four combinations of adjacent pair types and both horizontal parities. A finite-box test is not being used in place of this exhaustive boundary argument. — [Certificate](actual_carries_check.py).

**Any finite actual head can be retained.** Keep an arbitrary finite actual rectangle, and put zeros elsewhere above a later tail. Cutting the rectangle at its right or bottom edge cannot create `1001`, because its required lower-right1 is then zero; at its top edge, the required upper-left1 is zero. After one full zero-row buffer, attach the row-pair construction, translated to the desired row. Its weighted value is a rational power of3 times `3/4`, and the retained head is a finite rational sum. The result remains rational and can be nonperiodic. Choosing the retained rectangle large enough to contain the fifteen displayed witnesses gives **exactly the same complete four-cell language** as the actual high-column array. One may retain any prescribed finite set of actual smooth prefixes by enlarging the rectangle. This is a scope countermodel for the symbol-language strategy, not a countermodel to the actual floor/cocycle process. — [Mass and language checks](actual_carries_check.py).

### Gaps

- This does not show that there are infinitely many independently usable carry sites in the actual array. The witness table is finite, and the countermodel deliberately does not satisfy the full actual recurrence.
- The countermodel may violate actual residue-specific transition constraints, including the `j=0` implication. It refutes deductions using the sole forbidden motif, complete unlabelled four-cell language, and a finite actual head; it says nothing stronger.
- No canonical one-base expansion with controlled actual carry propagation was constructed. Nonperiodicity of the raw array still cannot be promoted to nonperiodicity of such an expansion.

## Does the carry analysis close the weighted-return objective?

### Takeaway

No. The new local theorem is an actual-array constraint and the counterexamples sharply delimit its force, but neither supplies arithmetic control of the semi-infinite ray or hybrid coefficients. The missing step remains the adequate upper construction itself, rather than only a later nonvanishing proof. — [Current return audit](../infinite-return-construction/REPORT.md), [weighted-response obstruction](../infinite-return-construction/weighted_returns.md).

### Cited Findings

- An adjacent distinct-color or same-color event interchange changes the weighted birth sum by the corresponding exact min-Hessian times a difference of reciprocal event weights. The Hessian must be evaluated in the current pre-swap context. Arbitrarily reusing the original context is invalid. — [Exact min-Hessian identities](../infinite-return-construction/weighted_returns.md).
- The retained-side degree-two identity leaves four semi-infinite weighted strips. Rationality of the original total does not presently imply rationality of these strips or of the actual weighted ray local times. — [Retained sides and arithmetic gap](../infinite-return-construction/weighted_returns.md), [current report](../infinite-return-construction/REPORT.md).
- The independent continued-fraction branch obtains a mixed four-array residual supported past both first mismatch thresholds, but its approximating combination still contains the two infinite hybrid profiles. — [Current record-return analysis](cf_induction.md), [exact checker](record_returns_check.py).

### Inferences

The kernel carries above preserve weighted mass by an arithmetic identity. Replacing an actual min-birth pattern by a carry-equivalent pattern gives no information about whether the replacement is produced by the actual cocycles. For a return proof one would need an exact rule that resums the actual carry propagation, including its axis and low-column terms, and bounds its arithmetic cost. The curl theorem supplies only a local relation between states; the cone readout remains nonlinear and records which unbounded contexts meet a boundary. No identity derived here eliminates the combination of the two hybrid profiles, and the finite carry table does not justify such an elimination. — [Actual edge/curl proof above and certificate](actual_carries_check.py), [min-Hessian context obligation](../infinite-return-construction/weighted_returns.md).

### Gaps

- No actual infinite sequence with the required weighted exponential error, fixed coefficient arithmetic, controlled clearing height, and nonzero remainder was constructed.
- No claim of direct irrationality, eventual nonperiodicity of a canonical one-base word, or arithmetic closure of the mixed hybrids is made.
- Only this note and its narrowly targeted exact certificate were written. No prior notes were edited; no Lean, dependency installation, external posts, density decimals, or broad repository scan was used.
