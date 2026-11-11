# Continued-fraction induction of the actual cocycle and weighted tie rays

**Status: an adequate infinite weighted-return theorem is not proved.** This round supplies an exact continued-fraction register induction, a special invariant for nonresonant tails, and an exact weighted-profile lift. It also gives a genuine-path test against literal finite ray-profile closure. The arithmetic reduction, adequate error margin, and nonvanishing remain open. The finite formula (C) is taken as proved. [Current report](../infinite-return-construction/REPORT.md), [final previous audit](../infinite-return-construction/final_return_audit.md).

All new assertions below are proved in the Inferences paragraphs. The companion [exact certificate](cf_induction_check.py) uses only integer and Fraction arithmetic and runs with Python `-B`; it adds no dependency or imported bytecode. It checks the specific recurrences and examples, rather than proving an infinite theorem by finite enumeration.

## What exact induction reaches the actual axis states and their rational recentering?

### Takeaway

The axis endpoint data form a finite modular controller coupled to an Eisenstein-integer register. On a tail with no resonant convergent, adjacent rotation-center distances are invariant and the entire prefix path has radius O(CF depth), independently of the sizes of the nonresonant partial quotients. These are genuine restrictions on the actual cocycle; they do not make the register finite.

### Cited Findings

- The starting identity is the actual axis recurrence `A_a-A_(a-1)=omega^(-a) S(floor(a alpha))`, with `S(m)=(1-omega^(2m+2))/(1-omega^2)`. The analogous reciprocal recurrence supplies B. [Exact separated arithmetic](../boundary-and-arithmetic/arithmetic.md), [independent arithmetic review](../boundary-and-arithmetic/arithmetic_review.md).
- Lower Christoffel words concatenate under Farey addition in increasing slope order. The relevant standard factorization is given in Chapter 3 of [Berstel, Lauve, Reutenauer and Saliola, *Combinatorics on Words*](https://webpages.math.luc.edu/~lauve/papers/wordsbook.pdf). Here the binary word has length q and p ones, so the Christoffel path's geometric slope is p/(q-p), an increasing transform of p/q.
- The rational-model recenter constants and their exact sum are already proved: `c_A=-H_A/[(1-omega^2)(1-rho)]`, `c_B=K-2/3-c_A`, where `rho=omega^(-(p+q))` and K is one of the two stated barycenters. [Skew-center derivation](../infinite-return-construction/skew_denominator.md).

### Inferences

**1. The parity-sensitive word induction.** For coprime `0<p<q`, define

```
C(p,q)=(h_1,...,h_q),
h_k=floor(kp/q)-floor((k-1)p/q),
Q(p,q)=sum_(k=1)^q omega^(-(k+floor(kp/q))),
rho(p,q)=omega^(-(p+q)).
```

For a binary word W, let `|W|` be its length, `p(W)` its number of ones, `Q_W` the same sum using prefix numbers of ones, and `rho_W=omega^(-|W|-p(W))`. Exact concatenation gives

```
Q_UV=Q_U+rho_U Q_V,       rho_UV=rho_U rho_V.       (I1)
```

Let `p_n/q_n` be the usual convergents with `p_0/q_0=0/1`. In our slope interval `a_1=1`, so the initial words are `C_0=0,C_1=1`. For `n>=1` and `a=a_(n+1)`, Farey concatenation gives

```
C_(n+1)=C_n^a C_(n-1)     if n is even,
C_(n+1)=C_(n-1) C_n^a     if n is odd.             (I2)
```

The order matters. Replacing both cases by the usual one-sided standard-word recurrence changes the root-sum register. Set `G_a(r)=1+r+...+r^(a-1)`. Then

```
Q_(n+1)=G_a(rho_n)Q_n+rho_n^a Q_(n-1)                 (n even),
Q_(n+1)=Q_(n-1)+rho_(n-1)G_a(rho_n)Q_n                (n odd).
                                                               (I3)
```

The phase and parity are finite control. When `rho_n!=1`, both `G_a(rho_n)` and `rho_n^a` depend only on `a mod3`. When `rho_n=1`, the factor is a itself; silently reducing that case modulo3 is incorrect.

**2. Connection to the ACTUAL, origin-anchored axis.** Put `sigma_n=sign(alpha-p_n/q_n)` and `rho=rho_n`. The actual floors through `1<=k<=q_n` agree with the one-sided rational floors. For `k<q_n`, the rational values are at distance at least `1/q_n` from the next integer and the convergent error is smaller. At `k=q_n`, the actual floor is p for a lower convergent and p-1 for an upper convergent. Therefore the true endpoint sum is

```
Q_n^true=Q_n                         if sigma_n=+1,
Q_n^true=Q_n+(omega-1)rho_n          if sigma_n=-1.   (I4)
```

Summing the axis recurrence, without changing its initial state `A_0=1`, gives

```
A_(q_n)=2/3+omega^(-q_n)/3
        -omega^2 Q_n^true/(1-omega^2).              (I5)
```

This directly computes the actual accumulated period endpoint. It does not introduce a freely selectable initial lattice state. At a nonresonant index the rational-model recenter constant is exactly

```
c_A,n=-omega^2 Q_n^true/[(1-omega^2)(1-rho_n)].      (I6)
```

The existing Beatty partition then supplies `c_B,n=K_n-2/3-c_A,n`; the reciprocal actual period endpoint follows from its axis formula. Thus (I3)-(I6) reach both recenter constants rather than merely an auxiliary word statistic. The isolated/patch correction E and the distinct four low-column rules remain as in the established model.

**3. The special Euclidean-isometry invariant.** Associate to a word its affine map

```
T_W(z)=Q_W+rho_W z.
```

Equation (I1) says `T_UV=T_U composed with T_V`. If W is nonresonant, this is an order-three rotation with center

```
gamma_W=Q_W/(1-rho_W),       T_W^3=identity.        (I7)
```

Suppose indices n-1,n,n+1 are all nonresonant. Write `delta=gamma_n-gamma_(n-1)` and `rho_n=r`. The possibilities in (I3) are precisely:

| a mod3 | phase restriction | gamma_(n+1)-gamma_n, n even | same difference, n odd |
|---|---|---|---|
| 0 | either | -delta | -delta |
| 1 | rho_(n-1)=r | r^2 delta | r delta |
| 2 | rho_(n-1)=r^2 | r delta | r^2 delta |

For example, in the middle even case, the composition of two r-rotations has center `-r gamma_n-r^2 gamma_(n-1)`; subtracting `gamma_n` yields `r^2 delta`. The other entries follow by the same substitution. In particular,

```
|gamma_(n+1)-gamma_n|=|gamma_n-gamma_(n-1)|=L.      (I8)
```

On a no-resonance tail, the centers therefore follow a bounded-step walk in a fixed triangular lattice. The direction is controlled by parity, phases and the digit modulo3. The bounded one-sided correction in (I4) only changes finitely many residue-dependent offsets. Consequently `c_A,n=O(n)` on such a tail, even if its partial quotients are unbounded.

**4. Radius control reaches every prefix, not only endpoints.** Let `P_n` be the set of root sums of ALL prefixes of C_n, including the empty prefix, and define `R_n=max_(z in P_n)|z-gamma_n|`. A repeated block C_n^a is a union of copies of P_n rotated about gamma_n, since `T_n^3=identity`. Its radius about that center is still R_n, regardless of a. In either concatenation order, the centers of the two kinds of copied prefix paths are at distance at most L from the new center; this follows from the same center triangle used in (I8). Hence

```
R_(n+1)<=max(R_n,R_(n-1))+L.                       (I9)
```

Together with (I8), this bounds every prefix root sum by O(n). The harmonic term in (I5)'s prefix version is bounded. Thus the actual A path through a convergent prefix also has size O(n). Since convergent denominators grow at least as fast as Fibonacci numbers, this yields `A_a=O(log(a+2))` on an eventually no-resonance slope. The implied constants depend on the finite initial segment. The same conclusion applies to B through its exact complementary center relation or the reciprocal word construction.

This is a specific arithmetic constraint on this cocycle. It is stronger than applying a general bounded-variation estimate that retains the sum of all partial quotients. It still permits unbounded discrepancy and infinitely many translated tie thresholds.

### Gaps

- No theorem here shows that the ACTUAL logarithmic slope has an eventually no-resonance tail. The formulas (I1)-(I6) apply regardless; the invariant/radius conclusions require the stated nonresonance hypothesis.
- Finite modular control is not a finite register. The exact unbounded example below prevents that inference.
- The scalar model's adequate eligible-jump supply and the smaller-cost alternative remain unproved. Nothing here promotes generic transcendence to bounded partial quotients or to infinitely many resonant indices.

## How do weighted tie-ray readouts induce, and what arithmetic cost remains?

### Takeaway

There is a fully exact weighted transfer on the actual incoming state. Nonresonant block repetition reduces in triples, but the readout profile must remain an operator on translated states. At weights 1/2 and 1/3 the reduction retains the cubic period denominators; the endpoint invariant does not supply the missing degree-two arithmetic clearing.

### Cited Findings

- The paired floor-order correction is `-3 H_ij(Q)(1/d_1-1/d_2)`, with the same-color Hessian included. Its coefficient is a weighted tie-ray local time. The exact degree-two interior identity retains four semi-infinite strips. [Weighted-return derivation](../infinite-return-construction/weighted_returns.md), [independent audit](../infinite-return-construction/final_return_audit.md).
- The actual prescribed 53/84 rational model has reduced denominator exactly `27(2^(3q)-1)(3^(3p)-1)/6`. Thus a uniform cancellation inferred only from skew covariance is false. [Exact denominator check and interpretation](../infinite-return-construction/skew_denominator.md).
- The fixed-dimensional arithmetic acceptance condition includes fixed rational coefficients, a minimum-unit scale capped at 1, exponential height control, nonzero error and a fixed exponential improvement. The current available generic budget is strictly below `(25+sqrt(5))/10` in units of `q log2`. [Supply and acceptance note](../infinite-return-construction/diophantine_supply.md), [primary manuscript, Proposition 7.4](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf).

### Inferences

**1. Extended state keeps all necessary residues.** For a horizontal word W, use the state `s=(A,r,m)`, where r is the current a modulo3 and m the current floor modulo3. Reading one bit h applies

```
r <- r+1 mod3,  m <- m+h mod3,
A <- A+omega^(-r) S(m).                            (I10)
```

For a prefix of length k with u ones, this is the actual strip recurrence. In particular, its displacement over W is

```
D_W(r,m)=omega^(-r)/(1-omega^2)
          [sum_(k=1)^|W| omega^(-k)-omega^(2m+2) Q_W].
                                                               (I11)
```

Let `P_W h(s)=h(s after W)` be the pullback of any readout h. This notation applies to the cone digit, any tie Hessian, and the low-column rules: for fixed b, the actual `B_b-1+C_(r,b)-E_b` is retained inside h, including its r dependence. No initial A or B state is altered.

Define the weighted prefix profile

```
L_W(t) h(s)=sum_(k=1)^|W| t^k h(s after first k bits).
```

Directly splitting a concatenated word at its boundary yields

```
L_UV(t)=L_U(t)+t^|U| P_U L_V(t).                   (I12)
```

The shift of the incoming state in `P_U L_V` is essential: omitting it erases precisely the translated ray profiles at issue. A reciprocal vertical version uses weight t=1/3. Applying the two versions to a joint readout gives the actual two-axis weighted profile, with their shared cone/tie condition retained.

**2. Nonresonant triples really close the endpoint map.** If `rho_W!=1`, (I1) gives `Q_(W^3)=0`. Its length and number of ones are multiples of3, so (I11) gives zero displacement and the residue state also returns. Therefore

```
P_W^3=identity                                    (I13)
```

on the entire extended state space. This statement is valid independently of the actual incoming state; its application uses that actual state. It does not assume planar cocycle recurrence.

Put q=|W|. For `a=3k+r`, `0<=r<3`, (I12)-(I13) give

```
L_(W^a)
 = [(1-t^(3kq))/(1-t^(3q))]
      [L_W+t^q P_W L_W+t^(2q)P_W^2 L_W]
   +t^(3kq) L_(W^r).                              (I14)
```

This is an exact compression of arbitrarily large nonresonant partial quotients. Its profile entries have not become scalar rational constants. At a resonant W, `Q_(W^a)=aQ_W`; after the residue return its endpoint can be a nonzero translation. Formula (I13) must not be used there.

**3. The profile's size and arithmetic are different costs.** On a no-resonance tail the radius bound leaves only O(n^2) possible lattice states in a convergent profile, times finitely many residue states. Thus a growing-register dynamic program is legitimate. Its weighted coefficients are still sums of powers `2^(-k)` for k as large as q. Their integer numerators after clearing `2^q` can have size `exp(O(q))`. There is no subexponential numerator bound from an O(log q) spatial radius.

Likewise, (I14) at t=1/2 retains `1-2^(-3q)`; its vertical counterpart retains `1-3^(-3p)`. Combining them gives the established degree-six common denominator, not a new degree-two one. The original degree-two interior operator still has its four unknown weighted side strips. The exact induction is a way to compute and study those strips, not a proof that they are rational, fixed-coefficient terms, or functions of the sole original Z under `Z in Q`.

**4. Physical first crossings must be tracked separately.** For a zero/one ray readout h, let `e_W^h(s)` be its first successful prefix, or infinity. Then exactly

```
e_UV^h(s)=min(e_U^h(s), |U|+e_V^h(s after U)).      (I15)
```

This permits record-level searches through induced words while retaining physical positions and actual contexts. Neither an O(n) threshold register nor an O(n^2) spatial profile specifies where its first crossing occurs on the original axis.

In particular, the unipotent register growth in the next section is growth ACROSS changing CF words. A fixed nonresonant word has the order-three endpoint return (I13); repeating that word does not accumulate that unipotent drift. Therefore a preperiod of length `q times register` cannot be asserted merely from the drift. Such a cost must be proved for the chosen construction, rather than imported from a different physical repetition.

### Gaps

- No fixed-dimensional arithmetic compression of the ray profiles or four side strips has been proved. The growing-profile construction supplies no uniform version of the fixed-term S-unit lower bound.
- No improved clearing exponent, adequate infinite sequence, or nonzero exponentially small arithmetic error has been obtained.
- Profile support size, coefficient height and physical first-crossing positions are three separate quantities. The present induction controls the first and expresses the latter two exactly; it does not establish their required return bounds.

## Does a genuine no-resonance path force finite ray closure or useful record stabilization?

### Takeaway

No literal finite closure follows even on a very structured genuine path: an explicit no-resonance quadratic slope has unipotent recenter drift, and its actual sampled axis states distinguish arbitrarily many translated tie rays. This does not exclude a construction with controlled integer parameters. The first few exact crossings also warn that a ray threshold of the recenter's size can be encountered far before the current original prefix ends.

### Cited Findings

- Generic integer-translation independence alone does not refute special closure on actual axis paths; the previous audit explicitly limits that obstruction. [Prior audit, second question, point 4](../infinite-return-construction/final_return_audit.md).
- The actual logarithmic slope is transcendental, and explicit transcendental no-resonance tails already show that generic transcendence does not force the older eligible jump threshold. [Supply theorem and countermodels](../infinite-return-construction/diophantine_supply.md), [audited 3/21 countermodel](../infinite-return-construction/final_return_audit.md).
- All finite word, center, profile and first-crossing values cited below are independently recomputed by [cf_induction_check.py](cf_induction_check.py). No density decimal or floating-point logarithm is used.

### Inferences

**1. A nonresonant unipotent family.** Consider the comparison slope

```
alpha_*=[0;1,1,1,1,1,3,overline(2,1)].
```

It belongs to `(3/5,2/3)`; at n=6 its adjacent convergents are `5/8,18/29`, with sum residues `1,2`. Starting with these residues, each block (2,1) changes `(s_(n-1),s_n)=(2s,s)` to another pair of this form and never produces zero. Thus every subsequent convergent is nonresonant and every outgoing ratio is less than3. This is a comparison slope, not the actual logarithm.

Let t count blocks (2,1,2,1), starting at n=6, and write `(Q_t,Q_t^prev)` for the two endpoint registers. Their phases return after each four-digit block to `rho=omega,rho_prev=omega^2`. Applying the parity-correct recurrence gives

```
 [Q_(t+1)     ]   [ -omega^2       omega^2 ] [Q_t     ]
 [Q_(t+1)^prev] = [ -1             1-omega ] [Q_t^prev].        (I16)
```

The matrix has trace2, determinant1 and a nonzero square-zero difference from the identity. The initial register pair is `(-omega,-omega)`, so induction gives

```
Q_t=(t-1)omega,          Q_t^prev=-t-omega,
c_A,t=(1-t)/3.                                    (I17)
```

All these n=6+4t convergents are lower convergents, so their one-sided sign is positive. In particular, the unbounded recentering is not an artifact of endpoint conventions.

The denominator pair transforms by

```
 [q_(t+1)     ]   [11 4] [q_t     ]
 [q_(t+1)^prev] = [ 8 3] [q_t^prev],      (q_0,q_0^prev)=(29,8).
                                                               (I18)
```

Its eigenvalues are `7+4sqrt(3)` and its reciprocal. Modulo3, the matrix has order3. Thus `q_(3ell)=2 mod3`. Substituting (I17) in the ACTUAL endpoint identity (I5) gives

```
A_(q_(3ell))=1-ell+ell omega.                      (I19)
```

These are actual states on one fixed irrational cocycle, reached from A_0=1. No phase or lattice state is selected independently.

**2. Tie rays separate those actual sampled states.** In Eisenstein coordinates `z=x+y omega`, the distinct-color Hessian `H_02` is exactly

```
H_02(z)=1_[x=0 and y>=1].
```

Indeed `x=Q_0-Q_2` and `y=Q_1-Q_2`, so this is `Q_0=Q_2<Q_1`. For integers `L>=1` put

```
h_L(z)=H_02(z+L-1).
```

Equation (I19) then proves

```
h_L(A_(q_(3ell)))=1_[ell=L].                       (I20)
```

The translates are linearly independent AFTER restriction to this actual path: evaluation at `ell=L` isolates each coefficient. This is a genuine-path failure of literal finite-dimensional ray-profile closure, rather than the older unrestricted-state counterexample. It says nothing by itself about linear independence or rationality of their weighted numerical sums, and nothing rules out a controlled growing parameter family.

**3. Record parameters can be cheap while physical crossings are early.** From the proved logarithmic axis bound and (I19), the first hit `a_L` of h_L on this comparison path satisfies

```
exp(cL)<=a_L<=C(7+4sqrt(3))^(3L)                  (L sufficiently large)
                                                               (I21)
```

for constants c,C>0. The lower bound follows because a successful hit has real Eisenstein coordinate `1-L`, whereas `|A_a|=O(log(a+2))`. The upper bound uses the explicit hit at `q_(3L)`. Thus first-hit indices are exponential in threshold size, not forced to be `q times threshold`.

A more pointed finite certificate reads the entire ACTUAL prefix through the lower convergent `42258/68039`. It finds exactly:

| L | first a with H_02(A_a+L-1)=1 | state at the first hit |
|---|---:|---|
| 1 | 209 | omega |
| 2 | 3083 | -1+omega |
| 3 | 43121 | -2+omega |

For these three levels the positions equal

```
f_L=q_L-q_L^prev/2-14,
f_0=11, f_1=209, f_2=3083, f_3=43121.             (I22, finite observation)
```

The all-L first-crossing formula in (I22) is NOT proved here. At current scale t=3L, the recenter satisfies `-c_A=L-1/3`, while the observed crossing scale is q_L and q_(3L) grows like q_L cubed. This is a concrete warning against inferring useful linear-prefix stabilization from the size of the recenter. Establishing an exact record recursion such as (I22), with a proof of firstness rather than just a hit, is a separate targeted next step. It would still have to supply a useful arithmetic return, not just early crossings.

### Gaps

- The comparison slope alpha_* is quadratic. It is not a counterexample to a special theorem for the actual transcendental `log_3 2`; the induction identities themselves apply to that actual slope.
- The ray independence (I20) defeats fixed finite functional closure, not every parameterized arithmetic induction. O(CF depth) parameters might still be manageable if the weighted coefficients and physical crossings satisfy stronger new identities.
- Neither the infinite first-crossing formula suggested by (I22) nor a degree-two weighted arithmetic return has been proved. The requested infinite-return goal remains open.
- This round skipped Lean, installs, broad scans, density decimals, old-file edits and external submission. The material mathematical risk is mistaking exact endpoint induction or small profile support for controlled weighted arithmetic coefficients.
