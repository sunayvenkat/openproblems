# Rational valid couplings and their complete arithmetic

**Status: genuine rational comparison families are constructed, but no adequate arithmetic infinite return is proved.** One family is a monotone finite-head repair of an explicit row coupling. A second uses complete skew triples and balanced L-shaped blocks, and has an explicit degree-five clearing factor without a crossover preperiod. Both are valid three-color bijections; the separate strictness theorem makes their actual errors nonzero. The proved windows and denominator bounds do not yet give the required small integer-cleared errors. — [Exact certificate](rational_templates_check.py), [strictness proof](coupling_strictness.md), [previous arithmetic frontier](../hybrid-arithmetic-closure/REPORT.md).

## Can a global rational coupling retain any actual optimal finite head?

### Takeaway

Yes. A complete canonical coupling has exact reciprocal-maximum cost `61/189`. Replacing the finite union of its triples touching the first K actual arrivals of each color by its equal-rank optimum gives monotone rational lower comparisons converging to the actual optimum. Every unchanged bulk triple and every low retimed token is accounted for. — [Certificate](rational_templates_check.py), [positive token representation](../hybrid-arithmetic-closure/global_carries.md).

### Cited Findings

- Tokens retain their original identity `(a,b)` and color `a-b mod3`. Their actual arrival is `2^a3^b`, except dyadic tokens with `a>=1` are multiplied by `3/2`, and row-one tokens with `a>=2` by `9/8`. This includes the single nonsmooth arrival `12 -> 27/2`. — [Full retiming identity GC6-GC8](../hybrid-arithmetic-closure/global_carries.md).
- If M denotes the true min-birth reciprocal mass, then `M=sum eta_(a,b)/(2^a3^b)` and `Z=3-3M=9c-6`. Equal-rank matching of all three color lists maximizes the sum of reciprocal actual triple maxima. — [Rank and matching proofs](../hybrid-arithmetic-closure/hierarchy_absorption.md).
- The new standard-library certificate checks the canonical row formulas, three exact finite-head repairs, two complete skew-template costs and their actual first-deficit events. No old file is imported or edited; all arrival comparisons use integers/Fractions. — [Certificate source](rational_templates_check.py).

### Inferences

**RT1. An explicit global coupling.** For every `n,b>=0`, put the three original tokens

```
(3n,b), (3n+1,b), (3n+2,b)
```

in one triple. Every token occurs once and the colors are all distinct. Their arrival maximum, with the actual delays, is

```
b=0: 6*8^n;
b=1: (27/2)*8^n;
b>=2: 4*8^n*3^b.
```

The small `b=0,n=0` triple has arrivals `1,3,6`; the `b=1,n=0` triple has arrivals `3,6,27/2`, so the same formulas already cover both exceptional heads. Consequently

```
Q_row = (1/6)/(1-1/8) + (2/27)/(1-1/8)
      + (1/4)/(1-1/8)*sum_(b>=2)3^-b
      = 4/21+16/189+1/21 = 61/189.                 (RT1)
```

This is a true reciprocal-maximum cost, not a synthetic insertion cost. — [Exact row assertions](rational_templates_check.py).

**RT2. Finite balanced repair.** Fix K and choose the first K actual tokens of each color, breaking equal-arrival ties by original token identity. Call their union H. Let U be the union of all canonical row triples meeting H. It is finite and has the same number of tokens of each color. Replace the coupling on U by the equal-rank coupling of U and retain every canonical triple outside U. This is a bijective three-color coupling, and its exact rational cost is

```
Q_K=61/189-Q_row(U)+M(U).                         (RT2)
```

The first K tokens of each color in U are precisely H, since H was an initial segment of the entire color list. Thus its first K equal-rank triples are the actual first K optimal triples. If U grows, the previous coupling together with the additional original triples is a valid candidate on the larger union; optimal rematching can only improve its cost. Hence `Q_K` is nondecreasing. It converges to M because its nonnegative cost includes the first K terms of the true optimal series and is bounded above by M. These arguments use finite matching optimality and monotone convergence only. — [Accepted matching theorem](../hybrid-arithmetic-closure/hierarchy_absorption.md), [repair assertions](rational_templates_check.py).

For a cutoff X, take `K=min_j T_j(X)=tau(X)` and call this cost `Q_X`. Its completed-triple count equals the actual `tau(t)` at every `t<=X`: the first `tau(t)<=K` globally optimal rank triples have already been included. The largest touched arrival is at most `6X`, since a canonical group changes its first exponent by at most two and the delay factor is at most `3/2`. Beyond that largest touched arrival, the old and rematched finite union have both completed exactly `|U|/3` triples, so the canonical and repaired completed counts are identical. — [Repair proof above](rational_templates_check.py), [strictness and sharp tail analysis](coupling_strictness.md).

**RT3. Full rational clearance.** Suppose `X>=1` is an integer, `A=floor(log_2 X)` and `B=floor(log_3 X)`. Every head token originally had time at most X, since the actual delays are forward. Every original token in U therefore has `a<=A+2,b<=B`. After retiming its exponent pair has

```
a_actual<=A+2,       b_actual<=max(B,3).
```

Negative first exponents at `27/2` create numerators, not additional reciprocal denominators. Each maximum in a rematched triple is one of these actual arrivals. Every reciprocal cost in RT2 therefore clears by

```
D_X=7*2^(A+2)*3^max(B,3),       D_X Q_X in Z.      (RT3)
```

The factor seven also clears the unchanged cost `61/189`; the ternary factor contains `27`. For `X>=27`, `D_X<=28X^2`. This is an upper bound, not a reduced-denominator lower bound. — [Exact numerator assertions](rational_templates_check.py).

Prefix exactness gives

```
0<=M-Q_X<=sum_(2^a3^b>X)2^-a3^-b
             <=(3/2)(A+3)/X.                    (RT4)
```

Indeed for each `a<=A`, the omitted geometric b-tail is at most `3/(2X)` after multiplying by `2^-a`. The rows `a>A` contribute at most `3/X`. The strictness theorem supplies `Q_X<M` for every finite X; it also sharpens the true error order to `Theta(log X/X)` for this fixed canonical-tail family. This does not give a lower bound on its reduced denominator. The estimates RT3-RT4 do not establish a shrinking cleared error. — [Tail proof above](rational_templates_check.py), [canonical-tail strictness](coupling_strictness.md).

The targeted exact values are:

|X|K|Number of touched row triples|Q_X|Reduced denominator|
|---|---|---|---|---|
|3|1|2|185/378|378|
|256|9|12|21575/36288|36288|
|524288|43|48|388193459317/650132324352|650132324352|

The corresponding last optimal-head arrivals are `3,243,497664`. These three checks establish no asymptotic denominator claim. — [Certificate output](rational_templates_check.py).

### Gaps

- This explicit family solves the existence, rationality, bijectivity, convergence and nonzero-error issues for a comparison family, but not the required approximation-to-height ratio. — [RT3-RT4 and strictness scope](coupling_strictness.md).
- The finite-head operation alone does not exploit a long continued-fraction agreement window. Its unchanged row tail has a strictly positive asymptotic deficit. — [Canonical-tail proof](coupling_strictness.md).

## Can a rational skew template avoid infinite root strips and crossover preperiods?

### Takeaway

Yes. Complete skew triples plus a balanced L-shaped repair partition every token. Optimal finite L-block matching and one explicit origin correction give a rational cost clearing by `27*3^(2p)*(2^(3q)-1)`, of nominal exponent five along actual convergents. The two actual tests show that its optimum-count agreement can end near the `2q` scale. — [Exact skew certificate](rational_templates_check.py).

### Cited Findings

- Nonresonance means `p+q` is not zero modulo three. Along a primitive skew chain, the color changes by `p+q`, so three consecutive chain points have all three colors. — [Existing grade geometry](../reflected-return-models/two_sided_models.md).
- The new construction uses the positive tokens with their original colors, including every delay. Equal-rank matching is used only on finite explicitly balanced blocks. — [Retiming and matching inputs](../hybrid-arithmetic-closure/hierarchy_absorption.md), [new checker](rational_templates_check.py).

### Inferences

**RT5. Complete partition.** Let `p>=2,q>=3`, `p+q!=0 mod3`, and put `u=2^q,v=3^p`. For every `0<=r<q,n>=0,b>=0`, create the bulk triple

```
(r+3qn,b+2p), (r+q+3qn,b+p), (r+2q+3qn,b).        (RT5)
```

They have three distinct original colors. In each horizontal block of width `3q`, the uncovered original tokens are exactly the translate of

```
L={(a,b):0<=a<q,0<=b<2p}
  union {(a,b):q<=a<2q,0<=b<p}.                   (RT6)
```

There is no infinite root-strip remainder. The L-block has `3pq` tokens and pq of each color. To verify balance, let `omega^3=1`, `omega!=1`, `A_q=sum_(r<q)omega^r`, `B_p=sum_(s<p)omega^-s`. Its character is

```
A_q B_p(1+omega^-p+omega^q)=0.
```

If p or q is divisible by three, the corresponding geometric sum is zero. Otherwise nonresonance forces `p=q mod3`, and the parenthetical factor is `1+omega+omega^2`. The same is true after horizontal translation by `3qn`. Therefore any finite equal-rank matching of each L-block completes a genuine global coupling. — [Color and coverage assertions](rational_templates_check.py).

**RT6. Stable finite block and exact origin correction.** Define the asymptotic arrival map by multiplying every row-zero token, including `a=0`, by `3/2`, and every row-one token, including `a=0,1`, by `9/8`. This is exactly the actual map on every translated L-block with `n>=1`. Let `O_0` be the optimal finite actual cost on L and `O_inf` its optimal cost with that asymptotic map. Then

```
O_0-O_inf=1/27.                                  (RT7)
```

Only three token arrivals change. Up to the first two ranks the color lists are

```
color0: actual(1,6),       asymptotic(3/2,27/4);
color1: actual(3,9),       asymptotic(3,9);
color2: actual(3,6),       asymptotic(27/8,6).
```

All these tokens belong to L when `q>=3,p>=2`. No affected token remains above the first two ranks; every later rank in each color is unchanged. The first triple maximum changes from `3` to `27/8`, while the second remains `9`. The cost difference is `1/3-8/27=1/27`. This is a complete head correction, not a discarded exception. — [Exact rank and correction assertion](rational_templates_check.py).

Use an optimal actual matching on L at n=0; on every translated block n>=1 repeat an optimal asymptotic matching, scaled by `u^(3n)`. Their total cost is

```
O_0+O_inf/(u^3-1)=1/27+u^3 O_inf/(u^3-1).        (RT8)
```

Every reciprocal maximum in `O_inf` clears by `2^(2q-1)*3^(2p-1)`. Multiplication by `u^3` removes the entire dyadic part. The finite-block contribution hence clears by `3^(2p-1)*(u^3-1)`; the constant `1/27` is already covered because `p>=2`. — [Arrival exponent bounds and certificate](rational_templates_check.py).

**RT7. Exact bulk sum.** Let

```
M0=max(v^2,uv,(3/2)u^2),
M1=max(v^2,uv,(9/8)u^2),
M2=max(v^2,uv,u^2).
```

For RT5 its actual arrival maximum is `2^r u^(3n)3^b M_b`, with `M_b=M2` for `b>=2`. The low bottom token is already in the admissible delayed range since `a+2q>=6`; the other two tokens are above row one. Thus all maxima are evaluated exactly without a moving crossover. Summing r,n,b gives

```
Q_bulk=2u^2/(u^2+u+1) * [1/M0+1/(3M1)+1/(6M2)].  (RT9)
```

The cancellation of `u-1` is from the complete sum over `r<q`, not an assumed period reduction. In each term, the numerator `2u^2` cancels every dyadic denominator from the chosen maximum. The result clears by `27v^2(u^2+u+1)`. Consequently the complete valid cost

```
Q_(p,q)=O_0+O_inf/(u^3-1)+Q_bulk,
D_(p,q)=27v^2(u^3-1),          D_(p,q)Q_(p,q) in Z. (RT10)
```

For actual convergents, `log D_(p,q)=(5+o(1))q log2`. This is the full nominal clearing cost, including all low retiming and finite-block terms. It is not a reduced-denominator theorem or a sufficiently small cost for the previous generic single-rectangle supply. — [Exact cost and clearing assertions](rational_templates_check.py).

The bulk contains a full-index lattice-coset subfamily of translates of one nondegenerate triple. Its actual logarithmic span is `2|q log2-p log3|>0`. The separate strictness theorem therefore gives `Q_(p,q)<M`, and the new rational comparison `Zhat_(p,q)=3-3Q_(p,q)` is strictly above Z for every such template. This is the true actual-max coupling; it has no sign ambiguity from synthetic birth conventions. — [Strictness theorem CS7/CS11](coupling_strictness.md).

### Gaps

- RT10 constructs a rational, bijective, strictly one-sided comparison for every nonresonant p/q in the stated range. It does not establish an adequate accuracy-to-denominator bound. — [Actual strictness and arithmetic scope](coupling_strictness.md).
- The full factor `u^3-1` remains in both targeted reduced costs below. A general cancellation of it must be proved, not inferred from the bulk's smaller cyclotomic denominator. — [Exact reduced values](rational_templates_check.py).

## How long does the actual optimality window last, and what remains for the return?

### Takeaway

The coupling is certainly optimal before the first actual token outside L0 arrives, at a scale asymptotic to `2q`. The two exact examples have their first deficits already near that scale. They refute assuming the old Farey window for this different coupling; they do not prove an asymptotic impossibility or rule out phase/refinement repairs. — [All-event first-deficit certificate](rational_templates_check.py).

### Cited Findings

- The previous scalar model and hybrid have their own proved Farey windows. Such a window does not transfer to a new coupling without checking completed actual triples. — [Previous window and arithmetic audit](../hybrid-arithmetic-closure/final_hybrid_audit.md).
- The new checker accumulates every actual token arrival, with simultaneous events retained, and every completed triple maximum. It compares the two counts at every event through the selected limits; all comparisons satisfy `G(t)<=tau(t)`. — [Exact enumeration](rational_templates_check.py).

### Inferences

The earliest actual arrival outside L0 is exactly

```
T_out=min(v^2,uv,(3/2)u^2).                       (RT11)
```

These are the three bulk tokens at r=n=b=0. All other bulk arrivals are later, and the next horizontal L-block starts no earlier than `(3/2)u^3`. For `t<T_out`, every arrived token belongs to L0; its optimal finite matching therefore gives exactly `tau(t)` completed triples. The error is bounded by the actual min-birth reciprocal tail from T_out onward. Along actual convergents `T_out=2^((2+o(1))q)`, so the available bound has order `q*2^(-(2+o(1))q)`. Combining this with the degree-five nominal denominator does not give a shrinking cleared error. This is a limitation of the proved bound, not a signed-error lower bound. — [Complete partition and first-event assertions](rational_templates_check.py).

The two targeted exact results are:

|p/q|Q_(p,q)|First t with G(t)<tau(t)|tau(t),G(t)|
|---|---|---|---|
|5/8|7302767222/12230589735|59049=3^10|31,30|
|12/19|72910517586918632358010200787/122107157304408335741677589853|293534171136=2^27*3^7|163,162|

The first checker runs through every relevant arrival up to `2^27` for5/8 and `2^45` for12/19. Thus firstness is proved in each finite range, which contains the stated first deficit. The5/8 result in particular precedes its old Farey horizontal threshold `2^(8+19)`. No all-level firstness or generic early-defect claim is inferred from the two examples. — [Complete event certificate](rational_templates_check.py).

There are now two complete genuine rational coupling families, with all multiplicities and infinite tails evaluated. Their errors have the correct one-sided sign and are nonzero by actual strictness. The missing improvement is a different matching/phase/refinement whose full rational clearance is small enough relative to its proved long actual agreement window. Convex phase combinations may preserve one-sidedness, but any new mixture denominator and every uncovered strip must be charged. Merely canceling a cubic period factor can replace it with an equally expensive smooth preperiod, so it is not automatically an improvement. This last possibility is a candidate for further analysis, not a theorem claimed here. — [Existing arithmetic acceptance criterion](../hybrid-arithmetic-closure/REPORT.md).

### Gaps

- No constructed coupling yet satisfies the required shrinking integer-cleared error or the degree-two hierarchy acceptance hypotheses. The adequate infinite-return objective remains unproved. — [RT3-RT4, RT10-RT11 and previous acceptance](../hybrid-arithmetic-closure/REPORT.md).
- No full reduced-denominator lower bound is claimed; special cancellations or a different selected infinite family remain possible. — [Certificate scope](rational_templates_check.py).
- Skipped: Lean, installations, broad scans, density decimals, old-folder edits and external posts. Main risk: transferring a synthetic/Farey agreement window to a genuine coupling, or treating a nominal upper clearance bound as an asymptotic denominator obstruction.
