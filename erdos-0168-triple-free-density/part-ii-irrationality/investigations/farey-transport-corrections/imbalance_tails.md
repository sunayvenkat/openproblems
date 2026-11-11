# Positive imbalance tails and a doubling correction

**Status: two strict rational comparison constructions and sharp real tail bounds are proved, but no adequate arithmetic infinite return is obtained.** The exact positive scalar identity is `Z=19/54+integral E(T)e^-T dT`. Its truncation has a universal error at least `2/(81X)` and error at most `C/X` at actual Denjoy denominators. On every sufficiently late lower actual convergent, its **reduced** ternary denominator is exactly `3^(3p)`, so no integer clearing produces an error tending to zero on that sequence. A separate exact doubling counterterm gives a rational upper comparison with error of exact order `1/X` for every cutoff; its forcing is a bounded indicator with uniform doubling-orbit frequency. Neither result supplies the required accuracy-to-clearing ratio. — [Exact certificate](imbalance_tails_check.py), [accepted target and arithmetic requirements](../rational-coupling-construction/REPORT.md).

## Does correcting the complete partial-token tail produce a better arithmetic object?

### Takeaway

It produces a strict rational **lower** comparison for Z, but the construction becomes independent of the chosen coupling: the corrected value is exactly the scalar imbalance truncation. The reduction to this one positive integral is legitimate; it does not imply rationality of arbitrary translated cone profiles. — [Token and rank inputs](../hybrid-arithmetic-closure/global_carries.md), [exact arithmetic certificate](imbalance_tails_check.py).

### Cited Findings

- The accepted finite theorem gives `tau(t)=min_j Q_j(t)`, where Q counts positive tokens of original color `a-b mod3`, delayed from `2^a` to `3*2^(a-1)` for a>=1 and from `3*2^a` to `27*2^(a-3)` for a>=2. The single nonsmooth arrival is27/2 and its minimum jump is zero. — [Full retiming proof GC6-GC11](../hybrid-arithmetic-closure/global_carries.md).
- Their total reciprocal mass is143/54; the optimal triple cost is `M=sum eta(d)/d=3(1-c)`, and `Z=3-3M=9c-6`. — [Marginal and rank formulas](../hybrid-arithmetic-closure/global_carries.md), [target normalization](../rational-coupling-construction/REPORT.md).
- The actual corrected color imbalance is `o(log t)`, with a uniform moving-phase rotation proof. — [CS1-CS3](../rational-coupling-construction/coupling_strictness.md).
- The new certificate independently enumerates the delayed tokens with integer doubled arrival times. It checks the jump and interval forms of the truncation, exact doubling identities on a whole finite partition, two finite-window lower bounds, three prescribed CF scales and all stated denominator assertions. — [Certificate](imbalance_tails_check.py).

### Inferences

Write N(t)=sum_j Q_j(t) for physical cutoff t, and use two notations to keep physical and logarithmic time distinct:

```
e(t)=N(t)-3tau(t)>=0,             E(T)=e(exp(T)).
R(X)=integral_X^infinity e(t)t^-2 dt.
```

All arrivals are at least one. Applying Tonelli separately to N and tau gives the exact identity

```
integral_1^infinity e(t)t^-2dt
 =143/54-3M=Z-19/54,
Z=19/54+integral_0^infinity E(T)e^-T dT.          (IT1)
```

Consequently rationality of Z is equivalent to rationality of **this complete scalar integral**. No individual orbit, row or translated profile is inferred rational.

For any rational X>=1 define

```
L_X=19/54+integral_1^X e(t)t^-2dt
   =19/54+sum_(s<=X) Delta e(s)/s-e(X)/X.        (IT2)
```

The sum is over actual token arrivals; it is finite. Thus L_X is rational, nondecreasing in X, and `Z-L_X=R(X)`. At an endpoint X the inserted jump cancels between its reciprocal and `e(X)/X`, so the formula respects simultaneous arrivals and right-continuous counts. The weighted total variation is finite because it is bounded by the reciprocal token mass plus3M.

For a genuine rational coupling C let G_C(t) count completed triples and put `U_C(t)=N(t)-3G_C(t)`. Suppose it realizes the optimum through cutoff X, as do the accepted finite-head repairs. Since `U_C-e=3(tau-G_C)` and that difference is zero before X,

```
Q(C)+(1/3)integral_X^infinity U_C(t)t^-2dt
 =M+(1/3)R(X).                                  (IT3)
```

The U-tail integral is rational: its full integral is `143/54-3Q(C)`, and its finite head is rational. Transforming the corrected cost by `3-3*(cost)` yields **exactly L_X**, independently of C. Correcting the complete canonical partial-token tail therefore does not retain a new family whose denominator can be counted separately from L_X.

The earlier `e(t)=o(log t)` gives `R(X)=o(log X/X)`. For a dyadic cutoff X=2^n, let B=floor(log_3 X). Every finite reciprocal in IT2 clears by

```
D_L=2^n*3^max(B,3),             D_L L_X in Z.     (IT4)
```

The negative dyadic exponent at27/2 creates a numerator, not an extra reciprocal denominator. The endpoint is dyadic and the constant19/54 is covered for n>=1. For X>=27 this gives `D_L<=X^2`; no reduced-denominator upper bound beyond that clearing statement is needed here.

### Gaps

- The logarithmic improvement from `Theta(log X/X)` for the canonical repair to `o(log X/X)` is not an adequate power saving. The sharper results below still do not give a successful arithmetic return. — [Existing canonical estimate](../rational-coupling-construction/coupling_strictness.md).
- Rationality of the scalar IT1 is an affine restatement of rationality of Z, not fixed-dimensional compression of an arbitrary boundary profile.

## How small can the actual positive imbalance tail be at continued-fraction returns?

### Takeaway

It is never smaller than a fixed constant times1/X. At the actual Denjoy subsequence `X=2^(3q_n)` it is also bounded above by a constant times1/X. For lower convergents an exact reduced-denominator calculation proves that this truncation sequence is arithmetically inadequate even if every possible cancellation is allowed. — [Exact certificate](imbalance_tails_check.py), [uniform averaging input](../rational-coupling-construction/coupling_strictness.md).

### Cited Findings

- The raw complex color sum is `W(t)=sum_(2^a3^b<=t) omega^(a-b)`, with `omega^2+omega+1=0`. Correcting the exceptional root subtracts its root of unity; at most one root is active. The positive-token count vector is the corrected color vector. — [Finite definitions and correction windows](../prefix-and-phase-audit/REPORT.md).
- The raw doubling identity adds the vertical-axis strip, while the correction rotates with its dyadic root. The invalid inverse root1 affects only the small patch window. — [Actual doubling structure](../hybrid-arithmetic-closure/global_carries.md), [exact token check](imbalance_tails_check.py).
- The rational-grid proof of uniform averaging already controls a block whose length is a CF denominator by an absolute constant, uniformly in phase. — [CS1-CS2 proof](../rational-coupling-construction/coupling_strictness.md).

### Inferences

**Exact corrected doubling recurrence.** Let V(t) be the root-of-unity sum of Q(t), and put `m=floor(log_3(2t))`. For t>=7,

```
V(2t)=omega V(t)+s(m),
s(m)=1,-omega,0 according as m=0,1,2 mod3.       (IT5)
```

Indeed doubling maps every existing original point to its next horizontal point, leaving the vertical-axis strip `sum_(b=0)^m omega^-b`. An active dyadic correction doubles to the next valid root and rotates by omega. Conversely every active correction at2t has a valid inverse for `t>=27/4`; the only excluded inverse-patch root has t in[6,27/4). The safer threshold7 avoids all small exceptions.

Since `e(t)=0` exactly when V(t)=0, `s(m)!=0` implies

```
e(t)+e(2t)>=1.                                  (IT6)
```

Choose the first boundary `c=3^(floor(log_3(2X))+1)/2`, so `X<c<=3X`. Either `[c,3c)` has nonzero s throughout, or the next interval `[3c,9c)` does. Thus there is `[u,3u)` inside `[X,27X]`, with `u<=9X`, on which IT6 holds. Integrating and using the substitution v=2t gives

```
2/(3u)
 <=integral_u^(3u) [e(t)+e(2t)]t^-2dt
 <=3 integral_X^(54X) e(t)t^-2dt.
```

Therefore for **every X>=7**,

```
integral_X^(54X)e(t)t^-2dt >=2/(81X),
R(X)>=2/(81X)>0.                                (IT7)
```

This is a full actual finite-window lower bound. It uses no asymptotic conjecture, numerical density or signed-error estimate.

**Uniform actual Denjoy upper bound.** Let p/q be any sufficiently late actual convergent of `alpha=log_3 2`; then q/p is a convergent of `beta=log_2 3`. Set `X=2^(3q)` and `T0=log X`. For s>=0 the raw row endpoint is

```
B_s=floor((T0+s)/log3),
B_0=3p-1 or3p,
K_s=(B_s+1)-3p<=s/log3+2.                       (IT8)
```

In the exact row identity CS2, group b=3k+r. Each group starts with p terms of the zero-mean step function `g(u)=omega^floor(3u)`, rotated by beta, followed by the remaining K_s terms across the three groups. The rational p-grid count in each third differs from p/3 by at most two. Perturbing each grid point by less than1/p can affect only a bounded number near the two endpoints; ten safely bounds each third's count error. Hence each p-block has complex sum at most30, uniformly in its initial phase. The raw initial geometric sum has modulus at most one, and `|1-omega|>=1`; consequently

```
|W(exp(T0+s))|<=91+K_s<=93+s/log3.
```

Correcting at most one root changes the modulus by at most one. Root-of-unity filtering gives

```
e(exp(T0+s))=-2 min_j Re(omega^-j V(exp(T0+s)))
           <=188+2s/log3.
```

Integrating s>=0 proves

```
2/(81X)<=R(X)<=(188+2/log3)/X<200/X.             (IT9)
```

This proves actual `Theta(1/X)` along all sufficiently late actual CF denominators, including both parities. The full uniform block bound is used; a small endpoint value alone would not control the future tail.

**Exact reduced ternary denominator on lower convergents.** Now take a lower actual convergent, so `q alpha-p>0`, and let n=3q. Eventually

```
3^(3p)<X=2^(3q)<2*3^(3p),       B=3p>=4.         (IT10)
```

There is exactly one arrival in the head with ternary exponent B: the ordinary token `(0,B)` at3^B. Its imbalance jump is `1-3eta_(0,B)`, which is a3-adic unit. No high-row indicator changes there, and no retimed low token has ternary exponent beyond3. Every other head term in IT2 has ternary denominator exponent below B; `e(X)/X` has no ternary denominator and19/54 has exponent three. Thus

```
v_3(L_X)=-3p.                                  (IT11)
```

This is an **exact reduced-denominator result**, not a bound inferred from the chosen common denominator. If b_n is the reduced denominator of L_X, every integer clearing factor is at least `b_n>=3^(3p)`. Combining with IT7 gives

```
liminf_(lower convergents) b_n*(Z-L_X) >=2/81.    (IT12)
```

Here `3^(3p)/2^(3q)->1`. No integer-cleared error from this lower-CF truncation sequence tends to zero. The checker verifies v3=-15 for5/8 and v3=-123 for41/65, using actual delayed-token counts; it also records the upper12/19 case without extrapolating its denominator.

### Gaps

- IT12 rules out the **specific lower-convergent scalar truncations**. It does not establish a denominator lower bound for all upper-convergent truncations, for a Richardson combination, or for an independently constructed coupling.
- The lower bound IT7 forbids an extra exponential real saving for the uncorrected imbalance tail. It does not forbid subtracting a genuinely new rational model of that tail with its own proved arithmetic.
- This block argument supplies no small fixed lattice for the previous multiscale boundary `B_m` and no nonvanishing theorem for its signed residual.

## Does the exact doubling defect provide a stronger rational counterterm?

### Takeaway

It gives a new strict rational upper comparison with a uniform `Theta(1/X)` real error, by subtracting an explicitly rational forcing tail. A uniform doubling-orbit frequency theorem proves strictness and a matching lower real order. Its available clearing factor is still `O(X^2)`; no adequate arithmetic family is proved. — [Exact correction certificate](imbalance_tails_check.py), [uniform averaging input](../rational-coupling-construction/coupling_strictness.md).

### Cited Findings

- Positive-strip addition changes a minimum by at most one after subtracting its balanced complete cycles; all corrections double covariantly for t>=7. — [Retiming and IT5 above](../hybrid-arithmetic-closure/global_carries.md), [full partition check](imbalance_tails_check.py).
- Uniform averaging applies to every finite step function on an irrational rotation, including moving initial phases. — [CS1](../rational-coupling-construction/coupling_strictness.md).

### Inferences

Write `m+1=3k+r`, r in{0,1,2}. At t>=7 the exact count-vector recurrence is

```
Q(2t)=pi Q(t)+k*(1,1,1)+v_r,
v_0=0, v_1=e_0, v_2=e_0+e_2,
```

where pi is cyclic color permutation. Define the residual minimum increment

```
h(t)=min(pi Q(t)+v_r)-min Q(t) in{0,1}.
```

It is zero when r=0. Hence exactly

```
e(2t)-e(t)=r(t)-3h(t),
r(t)=(floor(log_3(2t))+1) mod3.                 (IT13)
```

The forcing r is log-periodic with ratio27. Its complete tail integral is rational at every rational X. If `m=floor(log_3(2X))`, `r_j=(m+j+1) mod3`, direct summation of three geometric intervals gives

```
F_r(X)=integral_X^infinity r(t)t^-2dt
      =r_0/X+(-8r_0+6r_1+2r_2)/(13*3^m).         (IT14)
```

Now define

```
J_X=2L_(2X)-L_X,
U_X=J_X+F_r(X),
H(X)=integral_X^infinity h(t)t^-2dt.
```

Changing variables in the two tails proves

```
Z-J_X=2R(2X)-R(X)=F_r(X)-3H(X),
U_X-Z=3H(X),          0<=H(X)<=1/X.             (IT15)
```

Thus this counterterm is a rational upper comparison once strictness is proved. It is not obtained by assuming a separate profile rational under Z rational; its rational part is written explicitly.

**Uniform orbit mean and strictness.** Set `x=log_3(t)/3 mod1`, and let s(m) be the period-three root strip in IT5. Three doublings give

```
V(8t)-V(t)=Phi(x),
Phi(x)=omega^2*s(floor(3x+alpha))
      +omega*s(floor(3x+2alpha))
      +s(floor(3x+3alpha)).                     (IT16)
```

Each summand's unweighted mean is `(1-omega)/3`, and `1+omega+omega^2=0`, so Phi has mean zero. It is a finite step function. Under8t the phase rotates by alpha, and uniform averaging therefore gives

```
sup_(t>=7)|V(8^n t)-V(t)|=o(n).
```

The imbalance norm `e(z)=-2 min_j Re(omega^-j z)` is2-Lipschitz and invariant under cyclic rotation. Hence the same uniform o(n) bound holds for `e(8^nt)-e(t)`. The r-values on3n successive doublings form a finite-step rotation sequence of mean one, with rotation step alpha/3. Summing IT13 gives

```
sup_(t>=7)| (1/(3n))*sum_(j<3n) h(2^j t)-1/3 | ->0.  (IT17)
```

This is a uniform **bounded-output** theorem; it does not bound the accumulated state itself or close its literal register.

Choose a fixed integer M=3n large enough that every t>=7 has `sum_(j<M)h(2^jt)>=1`. Integrating that inequality for t in[X,2X] and changing variables in the disjoint dyadic intervals gives

```
1/(2X)<=sum_(j<M)2^j integral_(2^jX)^(2^(j+1)X) h(s)s^-2ds
       <=2^(M-1) H(X).
```

Consequently, for every X>=7,

```
2^-M/X <= H(X)<=1/X,
3*2^-M/X <= U_X-Z<=3/X.                        (IT18)
```

The fixed M depends only on the actual logarithmic rotation. No explicit optimized M or unproved effective discrepancy rate is claimed. In particular these rational comparisons have nonzero errors for every cutoff, but their error remains exactly of power1/X.

For X=2^n the complete value clears by

```
D_U=13*2^(n+1)*3^max(floor(log_3(2X)),3),
D_U U_X in Z,           D_U=O(X^2).             (IT19)
```

The code checks IT13 on every endpoint and interval of its actual finite partition and cross-checks the compact forcing formula against direct periodic summation. At the three prescribed scales, lower/upper denominator bit lengths are respectively46/45,108/115,390/391; none is treated as an asymptotic denominator theorem.

### Gaps

- IT18-IT19 do not prove a shrinking integer-cleared error. No reduced-denominator lower bound for U_X is asserted.
- A uniformly averaged bounded h-output is not an eventual-periodicity theorem, a fixed-state model or a finite S-unit expansion.
- No irrationality, adequate infinite arithmetic return, old-boundary lattice theorem or old signed-residual nonvanishing is established.
- Skipped: Lean, broad scans, density decimals, installs, old-folder edits, external posting and external review. Material risk: treating a logarithmic or same-power tail improvement as the exponential arithmetic saving required by the full goal.
