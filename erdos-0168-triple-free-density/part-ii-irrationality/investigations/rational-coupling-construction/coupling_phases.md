# Coupling phases and the exact price of period removal

**Status: the tested phase constructions do not supply an adequate arithmetic return.** Three genuine horizontal phases have exact rational costs. Their equal convex average removes the cubic cyclotomic factor but loses approximation already on the fixed interval `[3,9)`. A one-block folding construction removes the entire variable cubic period while retaining the original accuracy up to `O(u^-3)`; its denominator instead acquires an exactly growing dyadic factor. These are precise tradeoffs for the constructed phases, not an impossibility theorem for other couplings or coefficients. — [Phase certificate](coupling_phases_check.py), [first-round construction](rational_templates.md).

## What are the complete shifted phases and their exact average?

### Takeaway

Right shifts by q and 2q can be completed bijectively by explicit vertical triples in the left strip. The resulting three costs have a simple affine dependence on `u^-r`. Their equal average has a cheaper-looking period but a fixed positive actual gap, so it cannot be the desired convergent family. — [Exact identities and ownership inputs](coupling_phases_check.py).

### Cited Findings

- The first-round skew/L coupling is completely bijective, with `u=2^q,v=3^p`, `p>=2,q>=3`, and `p+q!=0 mod3`. If `O` is the optimal finite asymptotically retimed L-block cost and
  `S=1/M0+1/(3M1)+1/(6M2)`, then its cost is
  `Q0=1/27+Qinf`, where `Qinf=u^3 O/(u^3-1)+2u^2 S/(u^2+u+1)`.
  All M values include the actual low-token delays. — [RT5-RT10](rational_templates.md), [certified helper](rational_templates_check.py).
- For any genuine three-color coupling with cost Q, the actual mass M satisfies `Q<=M`; the associated rational target comparison is `Zhat=3-3Q>=Z`. Convex combinations preserve this inequality. Strictness for the constructed bulk classes is separately proved. — [Matching principle](../hybrid-arithmetic-closure/hierarchy_absorption.md), [actual strictness](coupling_strictness.md).
- The new phase checker reuses the first-round certified template and also checks the vertical ownership, the finite strip repair, the phase formulas and exact dyadic valuations on the two prescribed slopes. It does not independently reprove the shared template helper. — [Certificate](coupling_phases_check.py).

### Inferences

**CP1. Exact endpoint repair for two shifted phases.** In every original column a, group the original tokens at `b=3m,3m+1,3m+2`. Each group has all three colors. Its largest actual arrival is always `9*27^m*2^a`. This remains true for m=0 because every retimed b=0 or b=1 arrival is smaller than that b=2 endpoint. Therefore the complete vertical cost in a strip `0<=a<h` is

```
C_vert(h)=(3/26)sum_(a<h)2^-a
         =V(1-2^-h),                 V=3/13.     (CP1)
```

For r=1,2, fill the strip `a<rq` by this vertical coupling and translate the entire asymptotic skew/L coupling right by rq in `a>=rq`. There are no origin exceptions in that translated part because `a>=q>=3`; its actual retiming is exactly the asymptotic retiming used to define Qinf. The two regions are disjoint, cover every token, and require no unevaluated root strips. Hence

```
Q1=V+(Qinf-V)/u,
Q2=V+(Qinf-V)/u^2,
Q0=Qinf+delta,                       delta=1/27.  (CP2)
```

These formulas use actual reciprocal maxima. The three costs are not merely formal generating-function substitutions. — [Vertical group and phase assertions](coupling_phases_check.py).

**CP2. Exact equal-average formula.** Write `D_u=u^2+u+1`. Then

```
Qbar=(Q0+Q1+Q2)/3
    =V(1-D_u/(3u^2)) + u O/[3(u-1)]
      +(2/3)S+1/81.                              (CP3)
```

The factor `D_u` cancels from the cubic resummation, but the formula introduces smooth dyadic powers. The complete universal clearance from the first-round bound on O is

```
D_bar=1053*u^2*v^2*(u-1),       D_bar Qbar in Z.   (CP4)
```

Here `1053=13*81` is fixed. Along actual convergents the nominal exponent remains five: `log D_bar=(5+o(1))q log2`. No coefficient denominator is omitted; CP3 itself proves CP4. — [Exact formula and numerator assertions](coupling_phases_check.py).

**CP3. The average has a fixed actual deficit.** On `3<=t<9`, the actual positive-token minimum is one. The unshifted skew/L coupling completes exactly one triple there, because its L0 block contains all these early tokens and is optimally matched. Each shifted phase completes no triple: its left vertical groups start completing at9, and its right translated part has no arrival before `(3/2)u>9`. Thus the mean completed count is `1/3`, while the actual count is one. Integrating this exact deficit gives

```
M-Qbar >= (2/3) integral_3^9 t^-2 dt = 4/27.      (CP5)
```

The equality at the single endpoint9 does not affect the integral. Consequently this equal average cannot converge to M along the actual convergents. The statement is for these explicit repaired phases; it does not exclude other phases whose early heads are rematched differently. — [Exact early-head and integral checks](coupling_phases_check.py), [positive-token minimum](../hybrid-arithmetic-closure/global_carries.md).

### Gaps

- CP3 removes a period factor but not the full exponential arithmetic cost; CP5 already destroys the required accuracy for this unmodified equal average. — [CP3-CP5 certificate](coupling_phases_check.py).
- A q-dependent optimal rematching of larger strip heads could change the gap, but all new smooth head denominators and matching windows would then need proof. No such additional construction is asserted. — [First-round finite repair budget](rational_templates.md).

## Can the cubic period be removed while preserving the skew comparison's accuracy?

### Takeaway

Yes as an exact deterministic coupling: keep one horizontal skew/L block and fill the entire right tail by vertical triples. Its error is worse than the original skew cost by exactly `u^-3(Qinf-V)`, a uniformly small positive amount. Its full denominator uses only powers of2 and3 and a fixed factor13, but the nominal exponent remains five. — [Exact folding certificate](coupling_phases_check.py).

### Cited Findings

- The original skew coupling divides tokens into horizontal blocks of width3q; each block is the disjoint union of its bulk skew triples and finite L-shaped residual. — [Complete RT5-RT6 partition](rational_templates.md).
- Its actual first-block residual cost is `O+1/27`, and its bulk sum over r within one block is `2(u-1)S/u`. Every later complete horizontal block has the asymptotic pattern scaled by `u^(3n)`. — [RT7-RT9](rational_templates.md).

### Inferences

**CP4. A deterministic folded coupling.** Retain the actual skew/L coupling only on the original columns `0<=a<3q`. In `a>=3q`, use the canonical vertical coupling independently in every column. This is a disjoint, exhaustive, genuine three-color coupling. Its exact cost is

```
Q_fold=O+1/27 + 2(u-1)S/u + V/u^3.              (CP6)
```

Since `Qinf` is the whole asymptotic skew cost, the same formula is

```
Q_fold=(1-u^-3)Qinf+1/27+V/u^3,
Q_fold-Q0=u^-3(V-Qinf).                         (CP7)
```

The sign matters: Qinf is at least `8/27` from its first asymptotic rank triple, whereas `V=3/13<8/27`. Therefore

```
Q_fold<Q0<M,
M-Q_fold=(M-Q0)+u^-3(Qinf-V).                  (CP8)
```

Folding is worse as an approximation. Its loss is `O(u^-3)` with an absolute bound, since every valid cost is bounded by the fixed total token reciprocal mass. It preserves the previously proved upper error bound but does not improve it. — [Cost and sign assertions](coupling_phases_check.py), [strictness](coupling_strictness.md).

The variable factor `u^3-1` is absent from CP6, and

```
D_fold=351*u^3*v^2,       D_fold Q_fold in Z.     (CP9)
```

Indeed O has dyadic denominator at most `2^(2q-1)` and ternary denominator at most `3^(2p-1)`. Each term in `2(u-1)S/u` clears by `27u^3v^2`, while `V/u^3` adds only the fixed prime13. The constant351 is `13*27`. The nominal cost remains `(5+o(1))q log2` along actual convergents. This is genuine fixed-odd-factor rationality, not a degree reduction. — [Full clearing assertion](coupling_phases_check.py).

Both couplings have exactly the same original triples whenever `a<3q`, and no token in `a>=3q` arrives before `(3/2)u^3`. Their completed counts therefore agree below that threshold. In particular both first-deficit certificates survive unchanged:

```
5/8:   first deficit t=59049;
12/19: first deficit t=293534171136.
```

Both are below `(3/2)u^3`. Thus removing the period has not supplied a longer actual agreement window in either prescribed example. This is not a generic first-defect theorem. — [First-round all-event certificates](rational_templates_check.py), [partition identity above](coupling_phases_check.py).

**CP5. A cheap-looking convex identity, with its full value charged.** The same value can be obtained from two phases. In the left strip of phase1, the union of canonical vertical columns0 and1 has old cost `1/6`, while optimal rematching of those six tokens has cost `7/18`; improvement is `2/9`. Mixing that finite repaired phase with its unrepaired version with weight `1/6` gives a valid randomized phase of cost `Q1+1/27`. With

```
epsilon=1/[u^2(u-1)],
Q_fold=(1-epsilon)Q0+epsilon(Q1+1/27).            (CP10)
```

The coefficient of Qinf is `1-u^-3`; hence its cubic denominator cancels. The extra `(u-1)` in epsilon is not charged a second time: the final value is independently realized by the deterministic coupling CP6 and clears by CP9. Conversely this identity does not make the denominator a degree-two one. No fixed-coefficient S-unit theorem is being applied to the varying mixture coefficients. — [Finite head, convex identity and clearance assertions](coupling_phases_check.py).

### Gaps

- The period-free value is a new explicit valid comparison, but it inherits the skew family's early actual defects and lacks an adequate error-to-height estimate. — [CP7-CP9 and first-deficit scopes](rational_templates.md).
- Averaging cannot improve the best constituent's one-sided accuracy. Any benefit must come from a real net denominator reduction, which is not established here. — [Actual matching inequality](coupling_strictness.md).

## What is the exact smooth-denominator price in the eventual actual regime?

### Takeaway

The introduced dyadic cost is provable, not only a nominal bound. On every sufficiently large actual convergent in the stated nonresonant class, Qbar has an exact dyadic denominator of order `u^2`, and Q_fold one of order `u^3`. This explains precisely how the removed period reappears as a smooth arithmetic cost for these constructions. — [Valuation proof and exact checker](coupling_phases_check.py).

### Cited Findings

- Along actual convergents `v/u ->1`; eventually `v^2<=(9/8)u^2`. For q>=4 this makes `M0=(3/2)u^2`, `M1=(9/8)u^2`, and `M2=max(u^2,v^2)`. — [Exact bulk maxima](rational_templates.md), [regime assertions](coupling_phases_check.py).
- The original Q0 has an odd denominator because its known clearing factor is `27v^2(u^3-1)`. The finite O has `v_2(O)>=1-2q`. — [RT8-RT10](rational_templates.md).

### Inferences

Write `v_2(2)=1`. In the eventual regime,

```
u>v: S=61/(54u^2),
u<v: S=26/(27u^2)+1/(6v^2).                     (CP11)
```

Substitution into CP3 gives

```
Qbar=175/1053-1/(13u)+uO/[3(u-1)]
      +712/(1053u^2),                         u>v;
Qbar=175/1053-1/(13u)+uO/[3(u-1)]
      +595/(1053u^2)+1/(9v^2),                u<v. (CP12)
```

The O term has valuation at least `1-q`; the `1/(13u)` term has valuation `-q`. For q>=4 the displayed `u^-2` term has uniquely smaller valuation: its numerator712 has valuation3, while595 is odd. Therefore exactly

```
v_2(Qbar)=3-2q   if u>v,
v_2(Qbar)=-2q    if u<v.                         (CP13)
```

For CP6 the analogous expressions are

```
Q_fold=O+1/27+(793u-712)/(351u^3),             u>v;
Q_fold=O+1/27+(676u-595)/(351u^3)
                    +(u-1)/(3uv^2),          u<v. (CP14)
```

The first displayed numerator has valuation3 for q>=4; the second is odd. These terms have uniquely smaller valuation than O, the constant, and the remaining term. Consequently

```
v_2(Q_fold)=3-3q  if u>v,
v_2(Q_fold)=-3q   if u<v.                        (CP15)
```

These are exact reduced dyadic-denominator statements for all sufficiently large actual nonresonant convergents satisfying the regime, not extrapolations from two tests. They do not determine every odd factor of the full reduced denominators. — [Two-adic assertions](coupling_phases_check.py).

The exact prescribed checks give:

|p/q|v2(Q0)|v2(Qbar)|v2(Q_fold)|
|---|---|---|---|
|5/8|nonnegative|-13|-21|
|12/19|nonnegative|-38|-57|

For5/8 the mean is `20983316797/59391221760` and the folded cost is `11866997053/19874709504`. For12/19 their reduced denominators are respectively `4762170051736063020789248557056` and `1587393044957308375656560590848`. The checker reproduces both exact formulas and the original-minus-folded positive sign. — [Exact output](coupling_phases_check.py).

### Gaps

- The exact tradeoff is limited to these explicitly completed horizontal phases and this one-block fold. It does not exclude a different signed identity, better endpoint repair, nonhorizontal template or selected family with additional arithmetic cancellation. — [Construction scopes above](coupling_phases_check.py).
- No adequate infinite arithmetic return, control of the earlier hierarchy's full boundary value, or irrationality proof is supplied. — [Current goal and acceptance criterion](../hybrid-arithmetic-closure/REPORT.md).
- Skipped: Lean, installations, broad scans, density decimals, archived edits and external posts. Main risk: counting the removal of an odd period factor as a height saving while ignoring its replacement dyadic denominator, or interpreting a cheap convex identity as improved approximation accuracy.
