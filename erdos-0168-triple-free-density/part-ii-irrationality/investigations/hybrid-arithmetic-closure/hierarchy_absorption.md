# Exact hierarchical boundaries and the surviving arithmetic

**The low-cost arithmetic hierarchy is not constructed.** There is now an exact two-level and arbitrary-level operator identity, together with an actual infinite sequence on which its real residual tends to zero exponentially. The full boundary value, including the low rows, has not been made integral. Positive operator multiplication alone transports and enlarges the infinite sides; a finite head of even one actual boundary column has an explicitly growing ternary denominator. These facts delimit multiplication and separate-column truncation, not every signed or actual-specific hierarchy. [First-round cost budget](adaptive_induction.md), [exact certificate](hierarchy_absorption_check.py).

## What exact identity survives at two scales and at arbitrary depth?

### Takeaway

The hierarchy has an explicit boundary kernel. Its latest rational-model agreement produces an exponentially small **real** residual after all earlier shifts are charged. No fixed S-unit dimension is needed if its boundary is eventually cleared to an integer, but that last arithmetic operation is still missing. [Original retained sides](../infinite-return-construction/weighted_returns.md), [first-round budget](adaptive_induction.md).

### Cited Findings

- For the true coefficient array c in `{1,-2}`, put `d(a,b)=c(a,b+4)`. At a nonresonant convergent p/q, the operator `L=S_a^(2q)+S_a^q S_b^p+S_b^(2p)` vanishes on the true array whenever `a<q_next-q`, `b<p_next-p-4`. The high-row correction E is included in this statement. — [Weighted identity(W10)-(W12)](../infinite-return-construction/weighted_returns.md).
- There are infinitely many actual eligible convergents with `r=q_next/q>C_*=(15+sqrt5)/10`. Thinning to CF gaps of at least four gives retained denominator growth at least five. — [Supply proof](../infinite-return-construction/diophantine_supply.md), [hierarchical cost theorem(A10)-(A13)](adaptive_induction.md).
- Low rows b=0,1,2,3 have distinct exact rules. Shifting by four avoids applying the high-row annihilator to them; it does not evaluate their weighted sums. — [Full birth conventions](../global-boundary-proof/independent_audit.md).

### Inferences

**1. General positive-shift boundary formula.** For a bounded array d define

```
W(d)=sum_(a,b>=0) d(a,b)2^(-a)3^(-b),
H_A(d)=sum_(a<A,b>=0) d(a,b)2^(-a)3^(-b),
V_B(d)=sum_(a>=0,b<B) d(a,b)2^(-a)3^(-b),
R_AB(d)=sum_(a<A,b<B) d(a,b)2^(-a)3^(-b).
```

Absolute convergence and reindexing prove

```
W(S_a^A S_b^B d)
 =2^A3^B[W(d)-H_A(d)-V_B(d)+R_AB(d)].          (HA1)
```

For a polynomial `P(S_a,S_b)=sum c_AB S_a^A S_b^B`, let `Pi=P(2,3)` and

```
B_P(d)=sum c_AB2^A3^B[H_A(d)+V_B(d)-R_AB(d)].
```

Then exactly

```
Pi W(d)=B_P(d)+W(Pd).                           (HA2)
```

The combined boundary kernel at cell(a,b), including its reciprocal weight, is

```
K_P(a,b)=2^(-a)3^(-b)
         sum_(A,B: a<A OR b<B) c_AB2^A3^B,
B_P(d)=sum_(a,b>=0) K_P(a,b)d(a,b).             (HA3)
```

The union condition accounts for the corner subtraction once, including zero side widths. Every `2^A3^B R_AB(d)` is an integer when d is integer-valued. No similar assertion holds for H_A or V_B. The certificate independently verifies(HA1)-(HA3) on two finite arrays/operators with nonzero shifts. [Certificate](hierarchy_absorption_check.py).

**2. Two-level transfer with the actual residual retained.** Let `L_i=S_a^(2q_i)+S_a^q_i S_b^p_i+S_b^(2p_i)`, `F_i=2^(2q_i)+2^q_i3^p_i+3^(2p_i)`, and `B_i=B_(L_i)`. Then

```
F_2 F_1 W(d)
 =F_2 B_1(d)+B_2(L_1d)+W(L_2L_1d).            (HA4)
```

Equivalently `B_(L_2L_1)(d)=F_2B_1(d)+B_2(L_1d)`. This follows by applying(HA2) twice. The argument retains the current shifted array in `B_2(L_1d)`; replacing it by `B_2(d)` would be wrong. Iteration gives

```
P_m=product_(i=1)^m L_i,       Pi_m=product_(i=1)^m F_i,
Pi_m W(d)=B_(P_m)(d)+W(P_m d).                 (HA5)
```

The number of intermediate monomials can grow. Equations(HA3)-(HA5) are exact linear identities, not proofs that their boundary values are rational. [Certificate](hierarchy_absorption_check.py).

**3. The actual residual is small along the retained eligible scales.** Put

```
Q_-=sum_(i<m) q_i,              P_-=sum_(i<m) p_i,
A_m=q_next-q_m-2Q_-,
B_m=p_next-p_m-4-2P_-.
```

The last operator `L_m d` vanishes on the existing rectangle `a<q_next-q_m`, `b<p_next-p_m-4`. Earlier positive shifts have maxima `2Q_-`, `2P_-`; consequently

```
P_m d(a,b)=0 for 0<=a<A_m, 0<=b<B_m.           (HA6)
```

Since `|L_m d|<=6` and every earlier operator has coefficient sum three,

```
|W(P_m d)|
 <=18*3^(m-1)[2^(-A_m)+3^(-B_m)-2^(-A_m)3^(-B_m)].  (HA7)
```

The same expression with a nonpositive A_m or B_m is not claimed; the following retained sequence makes both positive eventually. All actual p_i/q_i lie in the valid slope interval eventually, and finite early choices can be discarded.

Thinning the actual good-ratio supply gives `q_i>=5q_(i-1)`. Hence `Q_-<=q_m/4` and `m=O(log q_m)`. Also `sum_(i<m)(p_i-alpha q_i)=O(1)`, since the convergent errors are bounded by reciprocal successor denominators and the retained denominators grow geometrically. Therefore `P_-=alpha Q_-+O(1)`, and

```
A_m>=(r_m-3/2)q_m,
B_m log3=A_m log2+O(1).
```

Thus the **actual**, not comparison-slope, real residual satisfies

```
|W(P_m d)|
 <=exp(-(C_*-3/2+o(1))q_m log2) ->0.            (HA8)
```

Meanwhile the cumulative clearing factor has

```
log Pi_m <=(5/2+o(1))q_m log2.                  (HA9)
```

This proves the real hierarchical decay using the actual array and unconditional supply. It does not produce an integer comparison numerator. The proof pays both the earlier shifts in(HA6) and the coefficient growth `3^(m-1)`; neither is discarded as finite-state data. [Supply theorem](../infinite-return-construction/diophantine_supply.md), [first-round cost calculation](adaptive_induction.md).

**4. Exact place of the low rows and arithmetic gap.** Define

```
L_0=sum_(a>=0,0<=b<4) c(a,b)2^(-a)3^(-b).
```

Then `W(d)=81(Z-L_0)`. Equation(HA5) is therefore

```
81 Pi_m Z = N_m^* + W(P_m d),
N_m^*=81 Pi_m L_0+B_(P_m)(d).                  (HA10)
```

The bound(HA8) is an adequate real smallness bound **if**, as an additional theorem, N_m^* belongs to a fixed rational lattice. No such theorem is proved. The b=0 part of L_0 is elementary, but the other low-row profiles and all the infinite sides remain in N_m^*. Under rationality of Z, substituting(HA10) to call N_m^* rational would be circular. Nonvanishing of the final residual would still be separate.

### Gaps

- The missing identity must clear `81 Pi_m L_0+B_(P_m)(d)`, not merely the compact mixed interior or the integer corner terms.
- No recursively discounted boundary potential or arithmetic lattice theorem for N_m^* has been constructed.
- Equation(HA8) is genuine progress in the real hierarchy but is not an arithmetic return without the preceding lattice theorem.

## What exactly prevents multiplication or a free finite-head repair from absorbing the sides?

### Takeaway

The composed operator has unavoidable formal infinite-side coefficients. Its actual a=0 boundary-column head through height T has denominator exactly `3^(T-1)`. These facts rule out declaring side multiplication or separate-column truncation free; they do not exclude a new signed identity exploiting the actual coupled states. [Boundary kernel(HA3)](hierarchy_absorption_check.py).

### Cited Findings

- The prescribed53/84 scalar model has reduced denominator `27(2^252-1)(3^159-1)/6`, with507 bits. This was independently reconstructed in the earlier audit. — [Scalar denominator audit](../infinite-return-construction/final_return_audit.md).
- The actual coefficients are exactly1 or-2, hence always one modulo three. — [Density normalization and actual birth rules](../infinite-return-construction/REPORT.md).
- The new certificate checks the boundary identities, the column-head denominator on actual high-column coefficients, and the stated two-factor repair against the saved audited rational value. It does not recompute an unbounded scalar family or treat a finite sample as proof. — [Certificate](hierarchy_absorption_check.py).

### Inferences

**1. Explicit surviving side.** Put `A_max=2sum q_i`, `B_max=2sum p_i`. All coefficients of P_m are nonnegative. There is exactly one monomial with `A=A_max`, namely the product of all pure horizontal shifts; its coefficient is one and its B exponent is zero. Therefore, at the outermost vertical boundary column,

```
K_(P_m)(A_max-1,b)=2*3^(-b),      b>=B_max.      (HA11)
```

It contains the explicit remaining profile

```
2 sum_(b>=B_max) d(A_max-1,b)3^(-b).
```

Changing d on that column changes B_(P_m) by precisely this nonzero functional. A product of the positive operators alone therefore does not formally cancel all infinite sides. For a special actual d, other identities could relate the profiles; no such relation follows from polynomial multiplication itself.

**2. Exact individual-column finite-head cost.** For every b>=0, equation(HA3) gives

```
K_(P_m)(0,b)=3^(-b) M_b,
M_b=sum_(A,B: 0<A OR b<B) c_AB2^A3^B.
```

The unique B=0 monomial contributes `2^(A_max)`. All other included monomials have positive B and are divisible by3. Hence M_b is a nonzero3-adic unit for every b. Since the actual d(0,b) is also a3-adic unit, the finite head

```
C_T=sum_(b=0)^(T-1) K_(P_m)(0,b)d(0,b)
```

has reduced denominator **exactly `3^(T-1)`**: the last summand has strictly smaller3-adic valuation than every earlier summand. No probabilistic or generic-state premise is used. This is checked on12 actual digits, while the argument proves all T. [Certificate](hierarchy_absorption_check.py).

Thus an architecture clearing this column independently must charge `(T-1)log3` additional smooth height. It cannot retain an arbitrarily long finite head at zero arithmetic cost. The real tail has the elementary bound

```
|sum_(b>=T) K_(P_m)(0,b)d(0,b)| <=3 Pi_m 3^(-T).
```

Multiplying by the separate clearing factor `3^(T-1)` cancels this tail decay rather than producing a small-error proof. This is a limitation of that bound and repair. It is **not** a lower bound on the signed tail: an infinite carry pattern can cancel exactly, and cross-column/low-row combinations can change the full scalar denominator.

**3. A concrete multiscale repair does not clear an unchanged scalar model.** For the actual named5/8 and53/84 models, use the proposed factors

```
F_(p,q)=2^(2q)+2^q3^p+3^(2p),
C=27 F_(5,8)F_(53,84).
```

The ratio84/8 exceeds five, so the pair satisfies the geometric spacing bound used for cumulative costs. C has192 bits, whereas the existing53/84 value's reduced denominator has507 bits. Direct exact arithmetic also checks `C*Z_model(53/84)` is not integral. This disproves this specific two-factor repair of the unchanged model. It does not refute a different comparison whose signed corrections alter the value or numerator. It also does not require an assertion that these two CF indices are four apart; the denominator ratio alone is the relevant bound in this check. [Earlier audited value](../../early-attacks/augmentation-and-return-attacks/returns_check.json), [new exact arithmetic](hierarchy_absorption_check.py).

### Gaps

- Positive boundary coefficients do not prove irrationality of their actual sum or prevent identities using the actual state coupling.
- The exact denominator of an individual finite head is not a denominator theorem for the full infinite N_m^*.
- A useful signed corrector must evaluate or cancel the surviving sides and low rows together, retain the actual incoming state and pay every extra smooth denominator.

## Does the retimed-token matching formulation supply the missing rational boundary?

### Takeaway

It gives a useful rigorous one-sided comparison principle: comonotone rank matching maximizes reciprocal triple cost. No low-degree rational matching or sufficiently accurate matching approximation has been constructed here. Rational color marginals alone do not determine this optimum. [Retimed process and rank layers](global_carries.md).

### Cited Findings

- The exact positive token representation gives `tau(t)=min_j T_j(t)` and
  `sum eta(d)/d=sum_k1/max(t_0(k),t_1(k),t_2(k))`, including the zero-minimum increment at27/2. Each color marginal reciprocal mass is rational. — [Global token formulas(GC6)-(GC11)](global_carries.md).
- The actual grade sign extension fails at attached low events, so a synthetic-order birth cannot automatically be treated as the largest actual arrival in a valid rank triple. — [Actual low-grade counterexamples](global_carries.md).

### Inferences

**Comonotone matching lemma.** Let the three reciprocal token lists be `x_j(k)=1/t_j(k)`, in nonincreasing order. Any bijective matching into three-color triples has cost `sum min(x_0,x_1,x_2)`. By the layer-cake identity, this equals the integral over s>0 of the number of triples whose three entries are all at least s. That number is at most

```
min_j #{k:x_j(k)>=s}.
```

Matching equal ranks attains this bound simultaneously for every s, because the three superlevel sets are initial rank intervals. Integrating proves that the equal-rank matching maximizes the cost. For infinite lists the finite superlevel counts and finite marginal reciprocal masses justify Tonelli/monotone convergence directly. Thus any fully specified genuine coupling gives a lower bound for the min-birth reciprocal mass, with strictness only if an interval of thresholds has a strict intersection deficit.

The lemma gives neither rationality nor cheap arithmetic of a proposed coupling. An invariant positive diagonal template must still match the infinite root strips and charge its preperiods. Failure of diagonal invariance of the canonical rank matching alone would not rule out every optimal coupling; the layer-cake criterion allows nonunique maximizers.

**Finite marginal counterexample.** Give colors1 and2 the same arrivals `(6,9)`. Give color0 either `(2,12)` or `(3,4)`. Its marginal reciprocal sum is `7/12` in both cases, and the other two marginals are unchanged. Yet the equal-rank costs are respectively

```
1/6+1/12=1/4,
1/6+1/9=5/18.
```

Every arrival is2,3-smooth and all lists have the same finite cardinality. This is an abstract positive-process counterexample, not the prescribed actual token coloring. It precisely shows why the rational marginal sums do not evaluate the rank maximum. [Exact rational check](hierarchy_absorption_check.py).

### Gaps

- No diagonal-invariant or other low-cost rational coupling is constructed with the required actual matching window.
- No strict actual infinite bracketing/nonvanishing theorem follows from the matching lemma alone.
- The real hierarchy(HA8) is established, but arithmetic of N_m^* and nonvanishing remain open. The adequate infinite-return objective is not completed.
- Skipped: Lean, installs, broad scans, density decimals, archived edits and external posting. Main risks are omitting the low-row contribution in(HA10), ignoring individual-head clearing costs, or interpreting formal multiplication obstructions as an impossibility theorem for actual signed hierarchies.
