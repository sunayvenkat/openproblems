# Adaptive induction and complementary resonances

**The adequate infinite weighted-return construction remains unproved.** This note gives an exact induction on the complementary resonance pattern, an all-level counterexample to its proposed birth-mask saturation mechanism, and a conditional adaptive denominator budget that fits the already proved convergent supply. The counterexample is a genuine origin-anchored **comparison-slope cocycle**, not the target logarithm or an assertion of finite-board optimality. The adaptive budget does not supply the missing recursive side-strip absorption identity. [Current frontier](../reflected-return-models/REPORT.md), [exact certificate](adaptive_induction_check.py).

## What additional structure follows when every late nonresonant outgoing digit is one?

### Takeaway

The complementary tail consists of four-digit blocks `(k,1,1,1)` starting at resonant convergents. Its resonant endpoint root sum has bounded magnitude, but the preceding root register undergoes an explicit unipotent drift. Bounded resonant drift therefore does not imply bounded base states or cheap scalar clearing. [Supply classification](../infinite-return-construction/diophantine_supply.md), [exact induction](../reflected-return-models/cf_induction.md).

### Cited Findings

- Put `s_n=p_n+q_n mod3`. Resonant indices have `s_n=0`. If all sufficiently late good indices have outgoing digit one, resonances occur exactly four indices apart and their intervening digits are one. The outgoing resonant digit k is unrestricted. — [Supply proof, equations(4)-(6)](../infinite-return-construction/diophantine_supply.md).
- For the lower Christoffel word `C_n`, its root sum Q and phase rho obey the parity-sensitive concatenation rule, with `rho_n=omega^(-(p_n+q_n))`. — [CF induction, (I1)-(I6)](../reflected-return-models/cf_induction.md).
- A resonant rational model has bounded nonzero affine block drifts; the already established cone formulas retain possible preperiod factors in powers of2 and3. — [Resonant model proof, (R1)-(R12)](../infinite-return-construction/resonant_models.md).

### Inferences

**1. Exact four-step transfer, including both parities.** At a resonant index n write `Q=Q_n`, `P=Q_(n-1)`, `rho_n=1`, `rho_(n-1)=r`, where `r` is omega or omega squared. Apply outgoing digits `(k,1,1,1)`. Straight substitution into the parity-sensitive root recurrence gives:

```
n even: Q_new=-r^2 Q,
        P_new=(1-k r^2)Q-r^2 P;
n odd:  Q_new=-r Q,
        P_new=(r^2-k)Q-r^2 P.
```

The new resonant phase is one and its preceding phase is `r^2`. These formulas hold for arbitrary Eisenstein-register values Q,P. The certificate independently composes the four one-step transfers for both parities, both phases, and digits1,2,5. The symbolic substitution proves the general formulas, rather than that finite check. [Certificate](adaptive_induction_check.py).

Two successive four-digit blocks with outgoing digits k,l restore Q and r. They give:

```
n even: P_new=P+(k+l+1)Q;
n odd:  P_new=P+(k+l+1)r Q.                    (A1)
```

Thus the normalized preceding register is monotone along a fixed nonzero lattice direction when Q is nonzero. The magnitude of Q remains fixed. The denominator pair has the separate exact four-step transfer

```
(q_new,v_new)^T=[[3k+2,3],[2k+1,2]](q,v)^T,
```

where v is the preceding denominator. It cannot be substituted for the root-register transfer. [Parity-sensitive recurrence](../reflected-return-models/cf_induction.md), [certificate](adaptive_induction_check.py).

**2. One fixed comparison cocycle realizes the unbounded register.** Let

```
alpha_g=(sqrt(5)-1)/2=[0;overline1].
```

Use resonant indices `n=6+8j`, `j>=0`. Write their lower convergents as `p_j/q_j` and preceding upper convergents as `u_j/v_j`. Their initial data and exact transfers are

```
(p_0,q_0,u_0,v_0)=(8,13,5,8),
(q_(j+1),v_(j+1))^T=[[34,21],[21,13]](q_j,v_j)^T,
(p_(j+1),u_(j+1))^T=[[34,21],[21,13]](p_j,u_j)^T,
Q_res,j=1,                    Q_prev,j=3j-omega.  (A2)
```

The root formula follows from (A1) with k=l=1 and the direct initial root sums. The length matrix is the square of the four-step k=1 matrix. In particular `q_j=1 mod3` and `p_j=u_j=v_j=2 mod3` for every j. Its Perron eigenvalue is `lambda=(47+21sqrt(5))/2=phi^8`; hence `q_j=Theta(lambda^j)` and `v_j=Theta(lambda^j)`. These are ordinary elementary matrix deductions. [Certificate](adaptive_induction_check.py).

### Gaps

- The comparison slope is quadratic and differs from `log_3(2)`. Equations(A1)-(A2) do not classify the actual target's continued fraction.
- Equation(A1) supplies a controlled one-dimensional register, not a weighted-profile closure. A recursive arithmetic use of that register is still missing.
- The preceding register's unbounded magnitude alone is not a lower bound on the reduced denominator of the complete two-variable scalar sum.

## Does bounded resonant drift force a cheap preperiod or much later birth-mask defects?

### Takeaway

No universal implication of either type holds on this complementary pattern. The golden comparison gives an unbounded genuine low-row preperiod and explicit birth-readout defects already at reciprocal index `S+1`, with horizontal index only `Theta(sqrt(q))`. The latter is an absolute-support obstruction, not a lower bound for a signed infinite approximation error. [Definitions and low rules](../global-boundary-proof/independent_audit.md), [certificate](adaptive_induction_check.py).

### Cited Findings

- The origin-anchored horizontal axis identity is `3A_a=2+omega^(-a)+(2+omega)Q_A(a)`. At an upper convergent endpoint, the actual root sum differs from the ordinary lower rational word by `(omega-1)rho`. — [CF induction, (I4)-(I5)](../reflected-return-models/cf_induction.md).
- For `b=1,a>0`, the uncorrected state `z=x+y omega` has birth readout `1_[x>=1,y>=0]`. For `b>=4`, the corrected state is `A+B-1+C-E` and the readout is `F(x+y omega)=1_[x<=0,x-y<=0]`. — [Audited low and high rules, (A5)](../global-boundary-proof/independent_audit.md).
- At resonant lower convergents with `q=1 mod3`, the exact model shifts are `A_(a+3q)=A_a+2+omega` and the harmonic-removed vertical drift is `h_B=(-1+omega)/3`. — [Resonant drift table](../infinite-return-construction/resonant_models.md).

### Inferences

**Scope.** All true states in this section are reached from the fixed origin of the golden comparison cocycle using its irrational floors and prescribed corrections. The model states use the specified one-sided rational floors of `p_j/q_j`. Neither is being identified with optimal finite boards at this comparison slope. For the target logarithmic slope, the original finite theorem and birth rules remain valid; no claim transfers the following trajectories to that target.

**1. Origin-anchored states and a genuine row denominator cost.** At `a=v_j`, the actual upper-endpoint correction changes `3j-omega` to `3j+2`. Substitution into the axis identity yields

```
A_(v_j)=(j+1)(2+omega).
```

The last three floor values before v are `u-2,u-1,u-1`. Their axis increments are respectively `1,-1,-omega^2`. Therefore

```
A_(v_j-1)=A_(v_j-3)=(2j+1)+j omega.             (A3)
```

The denominator `q_j-v_j` is the lower convergent two indices earlier. Its ordinary root sum is

```
Q_(n-2)=Q_res-omega Q_prev=-(3j+1)omega.
```

Consequently its actual and model horizontal state is

```
A_(q_j-v_j)=(j+1)-j omega.                      (A4)
```

Every index in (A3)-(A4) is a legitimate positive prefix. The floor assertions also follow directly from the Fibonacci error relation; the smallest v is8, so no origin exception is involved. [Certificate](adaptive_induction_check.py).

At b=1, the model has `B_1=0`. Since `q-v=2 mod3`, the residue term is `C_(2,1)=-omega`. Thus at the sequence of actual model indices `a_i=q-v+3qi`, the uncorrected state is

```
z(a_i,1)=(j+2i)+(-j-1+i)omega,
eta_M(a_i,1)=1_[i>=j+1].                       (A5)
```

There are therefore zeros through `a=q-v+3jq`, followed on this residue by ones. The full b=1 model row is eventually all ones: on each of its finitely many residues modulo3q, the state increases by `(2,1)` and eventually satisfies both low-row inequalities. Let L be the last zero index in that complete row. Then

```
L>=q_j-v_j+3j q_j,
sum_(a>=0) eta_M(a,1)/2^a
    =2-sum_(a:eta_M(a,1)=0)2^(-a)
```

has reduced denominator **exactly `2^L`**. The common numerator is odd because its last-zero contribution is odd and all earlier contributions are even. This is a genuine individual-row arithmetic lower bound, stronger than merely observing a large register. It is **not** a denominator lower bound for the full two-dimensional model value: carries between rows may cancel dyadic factors. The existing 8/13 scalar cancellation data already make that qualification essential. [Known full denominator example](../infinite-return-construction/resonant_models.md), [certificate](adaptive_induction_check.py).

**2. Full corrected defects just beyond the reciprocal floor window.** Let the immediate successor be `(p+u)/(q+v)` and put

```
R_j=2q_j+v_j,             S_j=2p_j+u_j,
b_j=S_j+1.
```

Both model axes match their comparison true axes for `a<R,b<S`. At b=S the reciprocal true floor is one below the model floor. At b=S+1 they agree again. Thus the accumulated vertical states differ there by `-omega`. These facts can also be seen from the exact golden error relation: if `beta=1/alpha_g`, then `(2q+v)-(2p+u)beta=(2-phi)(q-p beta)>0`, smaller than its initial value at p/q=8/13. Adding beta gives floor `2q+v+1` at b=S+1. [Farey convention](../global-boundary-proof/independent_audit.md), [certificate](adaptive_induction_check.py).

For completeness, the vertical base state can be derived without selecting a free translation. The complementary Beatty root sums through `v+u+2` give `Q_A(v+1)+Q_B(u+1)=0`. Here `Q_A(v+1)=3j+2+omega`. Substituting into

```
3B_b=2+omega^b+(1-omega)conjugate(Q_B(b))
```

gives `B_(u+1)=(1-j)+(j+1)omega`. Shifting by2p adds `omega-1`, including the harmonic correction. Hence

```
B_M(b_j)=-j+(j+2)omega,
B_T(b_j)=-j+(j+1)omega.                         (A6)
```

At this same b the model has the patch correction `E_M=omega`, while the true comparison has the isolated correction `E_T=1`. Indeed the model reciprocal floors at `S-2,S,S+1` are `n-4,n,n+1`; the true middle value is `n-1`. Therefore **the fully corrected true state is the model state minus1**, not merely minus omega. Both correction types are retained. [Correction tests](../global-boundary-proof/independent_audit.md), [certificate](adaptive_induction_check.py).

Now choose the horizontal coordinate by

```
j=2h:      a_j=v_h-1;
j=2h-1:    a_j=v_h-3,           h>=1.             (A7)
```

Equation(A3) supplies `A_(a_j)=(2h+1)+h omega`. In the even case a is1 modulo3 and `C_(1,1)=1`; in the odd case a is2 modulo3 and `C_(2,1)=-omega`. Combining (A6), E and C gives

```
j=2h:      z_M=1+(3h+1)omega,    z_T=(3h+1)omega;
j=2h-1:    z_M=1+(3h-1)omega,    z_T=(3h-1)omega.
```

All imaginary coefficients displayed are positive. Hence for **every j>=0**,

```
a_j<R_j,    b_j=S_j+1,
eta_T(a_j,b_j)=1,        eta_M(a_j,b_j)=0.        (A8)
```

These are hits, not claims about the earliest complete weighted defect. The smallest case uses a=7,b=22. Since `a_j=Theta(sqrt(q_j))`, the absolute coefficient discrepancy has weighted mass at least

```
3*2^(-a_j)*3^(-b_j)
    =3^(-S_j)*exp(-Theta(sqrt(q_j))).            (A9)
```

Thus the absolute-support method cannot gain an additional factor `exp(-delta q_j)` over the vertical-tail scale on this complementary pattern. This proves failure of the proposed generic birth-mask saturation mechanism. It does not lower-bound the signed total error or prohibit coherent carry cancellation. [Certificate](adaptive_induction_check.py).

The narrow direct checks cover the ordinary rational models8/13,55/89,377/610, and independently check the all-level formulas at j=0,1,2, including17,711/28,657. Floors use integer square roots, cross-checked with adjacent rational brackets; no floating-point logarithms are used. The derived all-level witnesses are `(7,22),(374,988),(376,46369)`. The last zeros on the selected low residue are at least5,2063,182888 respectively. [Certificate](adaptive_induction_check.py).

### Gaps

- No extension from this quadratic comparison to the target logarithm is asserted.
- The individual-row denominator does not survive automatically after summing all rows.
- Equation(A9) concerns the sum of absolute coefficient discrepancies. Opposite signed cells or complete-grade carry relations may cancel it in a scalar error.
- The all-level defects need not be the first defects; the separate finite band checks are not used as proofs of firstness at all levels.

## Can a hierarchy with growing term count fit the proved actual convergent supply?

### Takeaway

Yes at the arithmetic bookkeeping level: one degree-two clearing factor at each of a suitably spaced subsequence of scales has total cost at most `5q/2`, below the available matching exponent. This removes a needless fixed-term restriction for an integer-cleared hierarchical architecture. The actual recursive absorption of the four infinite sides is still unproved. [Existing degree-two identity](../infinite-return-construction/weighted_returns.md), [actual supply](../infinite-return-construction/diophantine_supply.md).

### Cited Findings

- The actual logarithmic slope has infinitely many eligible convergents with successor ratio greater than `C_*=(15+sqrt5)/10`. — [Supply theorem and hypotheses](../infinite-return-construction/diophantine_supply.md).
- The operator of nominal degree two leaves four infinite weighted sides. Their arithmetic absorption has not been proved. — [Weighted identity (W10)-(W12)](../infinite-return-construction/weighted_returns.md).
- Once `D_j L_j` is integral, rationality of Z puts every cleared error in a fixed rational lattice. No fixed S-unit term count is then required for the elementary discreteness implication. — [Current arithmetic audit](../reflected-return-models/final_reflected_audit.md).

### Inferences

**Conditional hierarchical acceptance theorem.** Thin the proved infinite eligible set so its retained CF indices differ by at least four. The recurrence gives

```
q_(n+4)>=5q_n+3q_(n-1)>=5q_n,
sum_(i<=j) q_i <=(5/4)q_j.                      (A10)
```

Suppose a genuinely constructed rational comparison L_j has bounded coefficients, matches the true array in the last retained Farey rectangle, and has clearing integer

```
D_j=C*S_j*product_(i<=j) F_i,
log F_i=2q_i log2+o(q_i),
log S_j=o(q_j),            D_j L_j in Z.          (A11)
```

Here C is a fixed integer; S_j explicitly charges any additional head or S-unit cost. A concrete candidate degree-two factor is `2^(2q_i)+2^(q_i)3^(p_i)+3^(2p_i)`, but no claim is made that it clears the unknown sides. The geometric bound and a split of finitely many early factors give

```
log D_j <=(5/2+o(1))q_j log2.                   (A12)
```

For actual logarithmic convergents, the matching rectangle supplies real error `exp(-(1+r_j+o(1))q_j log2)`, with `r_j>C_*`. Therefore

```
|D_j(Z-L_j)|
 <=exp(-(C_*-3/2+o(1))q_j log2) ->0.            (A13)
```

The fixed margin is positive because `C_*>3/2`. If Z is rational, these integer-cleared errors must eventually vanish. A separate nonvanishing/nonstabilization theorem would then finish the irrationality argument. This proof allows a growing number of intermediate terms because the **complete rational sum has actually been collapsed to one integer numerator**. It does not extend the fixed-dimensional KK theorem to unbounded dimension. [Matching rectangle estimate](../infinite-return-construction/REPORT.md), [arithmetic audit](../reflected-return-models/final_reflected_audit.md).

This is less restrictive than requiring a one-shot degree-two scalar formula. A recursively absorbed side profile could in principle use one factor per retained scale. Conversely, an uncontrolled preperiod term of order `j q_j`, an unknown irrational hybrid, or an exact finite head with uncharged denominator invalidates (A11). Equation(A5) explains why bounded resonant drift alone does not establish its small S_j hypothesis.

### Gaps

- No identity currently constructs L_j satisfying (A11). In particular, the four weighted sides of the degree-two operator have not been recursively absorbed.
- Spacing the indices is cheap for the denominator sum, but any recursive construction must prove its own matching rectangle and cannot assume arbitrary skipping preserves a needed induction relation.
- The actual adequate upper-return family and its nonvanishing remain unproved.
- Skipped: Lean, installs, broad scans, density decimals, archived edits and external submission. Main risk: treating the conditional degree-two hierarchy budget as an actual compression theorem, or turning a comparison-path absolute-support obstruction into a target-slope signed-error lower bound.
