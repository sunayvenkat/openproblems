# Unimodular Farey bulk couplings

**The full arithmetic return is not proved.** There is a new exact full-plane three-color tiling with constant index six, a congruence-complete reduction of actual convergent pairs to suitable bases, and a rational formula for every wholly contained quadrant triple. Its complete bulk cost has fixed-period arithmetic and a clearing factor of nominal degree at most two. The omitted boundary strips still require a complete repair, and no long actual optimum-agreement window is asserted. The accompanying exact certificate passes ownership, color, span, period, resummation and clearing checks. — [Certificate](farey_bulk_check.py), [previous actual arithmetic frontier](../rational-coupling-construction/REPORT.md).

## Can adjacent Farey data produce a complete near-isotime plane tiling?

### Takeaway

Yes. A unimodular basis with opposite nonzero color increments gives a two-triangle tiling of every six-cell basis block. Every sufficiently late actual convergent supplies such a positive-coordinate basis by an explicit finite case reduction; no assumption about infinitely many favorable residue pairs is needed. — [Exact ownership and basis certificate](farey_bulk_check.py).

### Cited Findings

- Token identity is the original exponent pair, its color is `a-b mod3`, and its actual arrival is `2^a3^b`, with dyadic and row-one delays retained. The old skew/L family required a period of width `3q` and nominal degree-five clearing. — [Accepted positive-token input and old construction](../rational-coupling-construction/rational_templates.md).
- A valid three-color coupling with a positive-density fixed-offset bulk is strictly below the actual rank optimum. This gives nonvanishing only after a complete global coupling has been constructed. — [Actual dispersion strictness theorem](../rational-coupling-construction/coupling_strictness.md).
- The new checker treats original lattice ownership independently of any optimum formula. It certifies the actual continued-fraction cylinder by `2^485>3^306` and `2^569<3^359`, and uses one fixed all-one comparison prefix solely to exercise the missing residue cases. — [Certificate](farey_bulk_check.py).

### Inferences

**FB1. Exact full-plane partition.** Let `u=(q,-p)`, `w=(s,-r)`, with `|qr-ps|=1`, and suppose their colors are the two distinct nonzero residues. In basis coordinates tile every translate of the rectangle `{0,1,2} x {0,1}` by

```
T1={(0,0),(1,0),(0,1)},
T2={(1,1),(2,0),(2,1)},
```

and repeat by `(3,0),(0,2)`. Each original coordinate point occurs exactly once because the basis map is an integer bijection. With increments `(1,2)`, both triangles have colors `{0,1,2}`; increments `(2,1)` reverse the same three residues. Translation rotates all colors together and preserves the property. In physical exponent coordinates the two offset lists are

```
{0,u,w},                 {u+w,2u,2u+w}.                (FB1)
```

These are genuine triples of original tokens, not a synthetic insertion order. — [Ownership and color assertions](farey_bulk_check.py).

For `epsilon=qr-ps`, the basis coordinates of `(a,b)` are exactly

```
i=epsilon*(ra+sb),       j=-epsilon*(pa+qb).
```

Take Euclidean residues `i mod3,j mod2`; the first shape owns residues `(0,0),(1,0),(0,1)`, and the second owns the other three. This supplies a global ownership function, including negative indices. The period lattice `<3u,2w>` has index six and contains `6 Z^2`, so `(6,0)` and `(0,6)` are actual periods. This is constant-index periodicity, not a period whose physical length is `3q`. — [Exact owner and period implementation](farey_bulk_check.py).

Both shapes have identical coordinate spans. The second, after translation, is the reflection of the first. For positive `q,s,p,r`, those spans are

```
H=max(q,s),             V=max(p,r).                    (FB2)
```

Let `e_u=q log2-p log3`, `e_w=s log2-r log3`. Every triangle has logarithmic span at most `|e_u|+|e_w|`, and dispersion at most twice that quantity. Thus actual approximating bases give near-isotime triples. This geometric statement alone gives no long optimum window. — [Span assertions and explicit shapes](farey_bulk_check.py).

**FB2. Every late actual convergent has a suitable basis.** Write `v_n=(q_n,-p_n)` and `gamma_n=q_n+p_n mod3`, with `v_n=a_n v_(n-1)+v_(n-2)`. Two adjacent colors cannot both be zero, since that would make their determinant divisible by three. After finitely many initial indices all coordinates used below are positive in `q` and negative in `p`.

Choose the following pair:

|Condition|Chosen basis|
|---|---|
|Adjacent colors are opposite and nonzero|`v_n, v_(n-1)`|
|`gamma_n=0`|`v_(n-1), v_n-v_(n-1)`|
|`gamma_(n-1)=0`|`v_(n-2), v_(n-1)-v_(n-2)`|
|Equal nonzero adjacent colors and `a_n>=2`|`v_(n-1), v_n-2v_(n-1)`|
|Equal nonzero adjacent colors and `a_n=1`|`v_(n-3), v_(n-2)-v_(n-3)`|

The last row is valid because the recurrence makes `gamma_(n-2)=0`. Every row preserves determinant magnitude one and gives opposite nonzero colors. Positivity in the fourth row follows from `v_n-2v_(n-1)=(a_n-2)v_(n-1)+v_(n-2)`. Every selected denominator is at most `q_n` and numerator at most `p_n`, so `H<=q_n,V<=p_n`. Every selected error is a fixed-coefficient combination of errors from at most three preceding convergents, hence tends to zero. The chosen spans tend to infinity because their denominators are at least a preceding denominator of fixed lag. — [Case-complete basis checks](farey_bulk_check.py).

The two selected errors have opposite signs: ordinary adjacent errors do, and subtracting an error of the opposite sign preserves the other sign. Thus the pair can be labeled lower/upper with `e_u>0>e_w`. The checker records these concrete choices from the actual prefix:

|Current fraction|Selected exponent vectors|`(H,V)`|
|---|---|---|
|`5/8`|`(8,-5),(3,-2)`|`(8,5)`|
|`12/19`|the same pair|`(8,5)`|
|`41/65`|`(19,-12),(27,-17)`|`(27,17)`|
|`53/84`|`(84,-53),(65,-41)`|`(84,53)`|
|`306/485`|`(84,-53),(317,-200)`|`(317,200)`|

The construction need not change at every convergent; no monotonicity of costs is asserted. — [Exact certificate output](farey_bulk_check.py).

### Gaps

- This is a full-plane tiling. Keeping its quadrant-contained triples leaves the crossing-triple boundary tokens unmatched. A complete repaired coupling and its optimality window are separate obligations. — [Previous coupling arithmetic requirements](../rational-coupling-construction/REPORT.md).
- Small logarithmic dispersion is not an exponentially accurate density approximation. The new strictness theorem applies only after the repair gives a valid global coupling. — [Strictness scope](../rational-coupling-construction/coupling_strictness.md).

## Does the entire quadrant-contained bulk have cheap exact rational arithmetic?

### Takeaway

Yes. Every wholly contained triangle belongs to one of twelve geometric families with periods six in both coordinates. The exact actual bulk cost, including low-row delays and invalid-small-root exceptions, clears by a fixed constant times `2^H3^V`. This is a bulk bound only. — [Complete bulk resummation](farey_bulk_check.py).

### Cited Findings

- Actual retiming is forward and keeps colors: row zero uses factor `3/2` for `a>=1`, row one uses `9/8` for `a>=2`; the exceptions at `(0,0),(0,1),(1,1)` must remain distinct from the asymptotic map. — [Retiming definitions](../rational-coupling-construction/rational_templates.md).
- The certificate independently sums the high double-geometric part, the actual first low-row member and its asymptotic geometric tail. It tests their scale recurrences and full integer clearance. — [Exact arithmetic source](farey_bulk_check.py).

### Inferences

**FB3. Twelve normalized families.** For each shape subtract its coordinatewise minimum, obtaining offsets `delta_j` with `0<=delta_a<=H`, `0<=delta_b<=V`, and minimum zero in each coordinate. The six anchor cosets modulo six are obtained from `3n u+2m w`, `n=0,1`, `m=0,1,2`, then adding that coordinate minimum. Thus every contained triangle is uniquely

```
{(A0+6n,B0+6m)+delta_j : j=0,1,2},
n,m>=0,                0<=A0,B0<6.                    (FB3)
```

There are two shapes times six cosets. Quadrant containment is exactly nonnegativity of the coordinatewise-minimum anchor; no hidden root strip is omitted from the bulk sum. — [Families/ownership verification](farey_bulk_check.py).

If `B>=2`, none of the three tokens is delayed. For one family let `Bh=B0` when `B0>=2`, and `Bh=B0+6` otherwise. Its high cost is

```
  1/max_j(2^(A0+delta_a,j)3^(Bh+delta_b,j))
  ------------------------------------------------ .             (FB4)
             (1-2^-6)(1-3^-6)
```

If `B0=0` or `1`, the remaining row has actual first cost `c_act=1/max arrival(A0+delta_a,B0+delta_b)`. Let `c_inf` use the asymptotic delay map on this same first triangle. At `n>=1` every first exponent has increased by at least six, so the asymptotic map is exactly actual. The complete extra low-row cost is

```
c_act+c_inf/63.                                         (FB5)
```

Equations(FB4)-(FB5), summed over twelve families, evaluate **every** wholly contained actual triangle. There is no variable crossover maximum: all three arrivals scale together by 64 horizontally and by 729 in the high vertical tail. — [Exact recurrence assertions](farey_bulk_check.py).

**Complete bulk clearing.** In(FB4), `A0<=5` and `Bh<=7`; geometric resummation supplies numerator `2^6 3^6`. A safe denominator is `63*728*2^H3^(V+1)`. Every actual or asymptotic reciprocal in(FB5) clears by `2^(H+5)3^(V+3)`, including the fractional `27/2` arrival. Therefore, with a fixed integer

```
C=2^5*3^3*63*728,
D_bulk=C*2^H*3^V,
D_bulk Q_bulk in Z.                                    (FB6)
```

For the actual reduced bases, the largest numerator and denominator belong to the same chosen vector after the finite initial cases: if positive Farey neighbors had `q>s` but `p<r`, then `qr-ps>=q>1`; if `p=r`, determinant one forces `p=1`. Thus `V log3=H log2+o(1)` follows from that vector's vanishing error. Consequently `log D_bulk=2H log2+O(1)<=2q_n log2+O(1)`. This is a complete rational bulk cost and a genuine reduction from variable cubic periods; it is not a clearing bound for an unknown full repair. — [Exact integrality assertions](farey_bulk_check.py).

There is a sharper ordinary-high-row bound for a direct adjacent pair labeled lower `u=(q,-p)` and upper `w=(s,-r)`. The winning vertices in the normalized first shape are the `u` vertex, and in the second the `u-w` vertex. Their largest first exponent is q and largest second exponent r. Thus the high cost clears by a fixed constant times `2^q3^r`, of nominal cost `(q+s)log2` on adjacent actual convergents. Low retiming can move the winner to the rightmost point; a general full-contained bound must retain the `2^H` factor. It must not count the sharp high-row estimate as the whole arithmetic. — [Exact normalized shapes and actual retiming](farey_bulk_check.py).

For the direct `5/8,2/3` pair the complete contained bulk is exactly `503/108864`. Its first assigned token arrives at216 and its first completed bulk triple at384. These exact values are also the values for the selected basis at `12/19`; they demonstrate that no long Farey window is supplied by determinant one alone. They do **not** identify a first deficit of any repaired full coupling. — [Certificate output](farey_bulk_check.py).

### Gaps

- No omitted boundary token has been coupled in this note. Its repair cost can introduce smooth factors or early deficits not present in(FB6). — [Previous full-arithmetic gap](../rational-coupling-construction/REPORT.md).
- The nominal bulk degree-two cost does not prove that the complete coupling has that cost, nor that its error is smaller than `D_bulk^-1`. — [Actual acceptance conditions](../hybrid-arithmetic-closure/REPORT.md).

## What is established toward an actual infinite arithmetic return?

### Takeaway

The inexpensive bulk and complete congruence reduction are established. Global boundary repair, a sufficiently long actual optimal head, and the combined accuracy-to-clearing estimate remain open here. No proof of Erdős168 or adequate arithmetic return is claimed. — [Exact certificate](farey_bulk_check.py).

### Cited Findings

- The previous skew/L construction had a complete degree-five rational denominator and a guaranteed roughly `2q` actual head; both must be improved together to obtain a return. — [Previous templates](../rational-coupling-construction/rational_templates.md).
- Strictness for any resulting positive-density bounded-offset coupling is available separately, so it need not be inferred from a few tested nonzero cells. — [Actual nonvanishing theorem](../rational-coupling-construction/coupling_strictness.md).

### Inferences

The two shapes are coordinate reflections. Their ordinary logarithmic arrival levels after normalization are `V log3+{0,e_u,e_w}` and `H log2-{0,e_u,e_w}`. Because the basis errors tend to zero, all first-family members arrive at physical scale `2^H` up to fixed constants; further geometric translations only increase that time. Hence the entire retained bulk lives at scales beginning near `2^H`, and its total reciprocal cost is of order `2^-H` (constants from the twelve six-period families). Most of the target mass remains in the boundary repair as H grows. Cheap bulk arithmetic alone cannot evaluate that mass. — [Normalized geometry and twelve-family formula](farey_bulk_check.py).

Boundary flux and the proposed full repair are being treated separately. Any final synthesis must combine their proved cost with(FB6), retain all low rows and finite exceptions, and verify actual completed-count equality only for that fully specified repaired coupling. A determinant, a small dispersion, a constant-index period or an integer bulk numerator does not establish the required matching window. — [Current goal and existing arithmetic frontier](../rational-coupling-construction/REPORT.md).

### Gaps

- No new full rational comparison family or actual approximation window is completed by this note alone. It supplies the bulk component and an exact checker for the boundary researcher. — [Bulk certificate](farey_bulk_check.py).
- Skipped: Lean, external review, installs, broad scans, density decimals and archived edits. Main risk: promoting the degree-two **bulk** denominator into an adequate full arithmetic return before evaluating the repair and its real error.
