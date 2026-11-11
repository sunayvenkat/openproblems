# Complete fractional Farey arithmetic

## Can a fractional periodic bulk be repaired with full degree two arithmetic?

### Takeaway

**Yes, under explicit finite linear balance conditions.** Rational nonnegative torus weights give a genuine fractional coupling after clipping and componentwise equal-mass rank repair. The complete cost clears with only one common weight-denominator factor. This is a construction theorem, not a long-head feasibility theorem. — [Exact construction certificate](fractional_arithmetic_check.py), [integer predecessor](../farey-transport-corrections/boundary_repairs.md).

### Cited Findings

- The accepted actual token has original identity `(a,b)`, color `a-b mod3`, and arrival `2^a3^b`, except `b=0,a>=1` has factor `3/2` and `b=1,a>=2` factor `9/8`. Thus `(2,1)` arrives at `27/2`. The optimum is `M=3(1-c)`, and every valid fractional coupling has cost at most `M` by marginal counting. — [Token and rank inputs](../hybrid-arithmetic-closure/global_carries.md), [rank optimum](../hybrid-arithmetic-closure/hierarchy_absorption.md), [actual-time certificate](fractional_arithmetic_check.py).
- The 72 types consist of both orientations of `{0,u,v}` at all36 anchor residues modulo6, for `u=(q,-p),v=(s,-r)`, determinant magnitude1 and opposite nonzero colors. Integer exact covers are only one special case of the following fractional construction. — [Type specification](../farey-transport-corrections/torus_bulk.md).
- The new certificate independently builds nonintegral mixtures from translated plane tilings, converts them into weighted torus types, checks every residue marginal, constructs the actual weighted rank repairs, sums complete geometric tails, and verifies the full clearing factor. It imports no earlier checker. — [Certificate](fractional_arithmetic_check.py).

### Inferences

**FA1. Variables and the whole-plane marginal.** Let `x_k>=0`, `k=1,...,72`. For each original residue node `z` impose

```
sum_(k whose mask contains z) x_k = 1.                 (FA1)
```

Give every plane triple of type `k` mass `x_k`. Distinct offsets have distinct residues, so a point belongs to at most one triple of a given type. Equation(FA1) gives every original point total marginal mass1. In particular `0<=x_k<=1` and `sum x_k=12`. A fractional coupling means a countable nonnegative weighted triple family with these unit marginals; disjointness of the supports is unnecessary. — [Type and coverage assertions](fractional_arithmetic_check.py).

Keep only wholly quadrant-contained triples. At a quadrant point `z`, set

```
w_x(z)=1-sum_(kept type-k owner of z) x_k.              (FA2)
```

This is nonnegative because it is the mass of the omitted crossing owners. With `H=max(q,s), V=max(p,r)`, every residual point lies in `a<H or b<V`. Put `A=6ceil(H/6), B=6ceil(V/6)` and assume `A,B>=6`. Partition residuals into the corner
`C=[0,A)x[0,B)`, bottom blocks `R_n=[A+6n,A+6n+6)x[0,B)`, and left blocks `L_n=[0,A)x[B+6n,B+6n+6)`. These regions are disjoint and exhaustive. In `R_n` no owner's horizontal coordinate can cross zero, and in `L_n` no owner's vertical coordinate can cross zero. Consequently residual masses repeat exactly under the corresponding six-coordinate shift. — [Geometry reconstructed in the certificate](fractional_arithmetic_check.py), [integer geometry predecessor](../farey-transport-corrections/boundary_repairs.md).

For `E=C,R_0,L_0`, define `m_E,j(x)=sum_(z in E, color j) w_x(z)`. Impose the six linear balance equations

```
m_E,0=m_E,1=m_E,2,       E=C,R_0,L_0.                 (FA3)
```

No unproved zero-flux property is assumed for arbitrary torus weights. These are actual constraints. No lower bound on edge capacity is needed: a zero-mass balanced block has the empty repair. Balanced corner mass eliminates donors and their preperiod entirely. This restricted repair theorem does not address an unbalanced corner. — [Balanced examples and zero-mass handling](fractional_arithmetic_check.py).

**FA2. The rank construction and its single denominator factor.** Suppose `Sx_k` are integers. Then every `w_x(z)` lies in `(1/S)Z`. In each finite balanced component order the points of each color by their actual arrivals, keeping ties in any fixed order. Assign to each point a consecutive mass interval of length `w_x(z)`; overlay the three color interval partitions. Every nonempty common interval gives a triple with its length as mass. Cumulative endpoints and their differences all lie in `(1/S)Z`, so every triple mass has denominator dividing **S**, not `S^2` or `S^3`. Each point receives exactly its residual mass. — [Greedy interval-overlay routine and marginal reconstruction](fractional_arithmetic_check.py).

Perform this construction in `C,R_0,L_0` and repeat the edge repairs by six-coordinate shifts. Bottom points have `a>=A>=6`, so the dyadic and row-one timing exceptions are already in their scaling regime; horizontal shifting multiplies **actual** arrivals by64, even in those two low rows. Left points have `b>=B>=6`, so they are ordinary and vertical shifting multiplies actual arrivals by729. If `q_C,q_R,q_L` are the three finite root costs, the full residual cost is

```
q_C+(64/63)q_R+(729/728)q_L.                         (FA4)
```

The clipped bulk and these repairs give every token total mass1. Overlapping fractional triples are accounted for by mass, not discarded. — [Exact rank marginals, scale tests and cost construction](fractional_arithmetic_check.py).

**FA3. Every bulk stream and all low exceptions.** Normalize each type's coordinate minima. Its least contained anchor in its residue class has coordinates at most5; each vertex then has exponents at most `H+5,V+5`. Let `M_act,M_asym,M_raw` be the first triple's actual, asymptotically retimed, and ordinary maxima. Its entire stream has cost

```
x_k[1/M_act+1/(63M_asym)+64/(63*728M_raw)].           (FA5)
```

The first term retains the exceptions at `(0,0),(0,1),(1,1)`. Later horizontal translates are in the asymptotic timing regime; positive vertical translates are ordinary. Thus the proof used for twelve integer streams applies to all72 independently weighted streams, with no extra least common multiple beyond `S`. — [Independent stream implementation](fractional_arithmetic_check.py), [earlier complete geometric identity](../farey-transport-corrections/farey_bulk.md).

All finite root coordinates are bounded by `A+5,B+5`; the possible retiming factors introduce only bounded additional powers of2 and3. Equations(FA4)-(FA5) therefore prove the safe complete clearance

```
D=S*(63*728*2^6*3^6)*2^A*3^B,       DQ(x) in Z.      (FA6)
```

This includes every root, fractional rank piece, and both infinite edges. It is a clearing upper bound, not a statement about the reduced denominator. For actual near-isotime Farey bases and polynomial `S`,

```
log D=H log2+V log3+O(log H)=(2+o(1))H log2.          (FA7)
```

**FA4. Explicit genuinely fractional repaired examples.** Equal mixing of phases `(0,0),(2,0),(4,0)` for basis `(8,-5),(3,-2)` gives36 active types of weight1/3. Half mixing phases `(0,0),(1,0)` for basis `(19,-12),(27,-17)` gives24 active types of weight1/2. Their complete repaired data are:

|Basis|S|Corner mass/color|Bottom root mass/color|Left root mass/color|Complete Q|
|---|---:|---:|---:|---:|---|
|8/3|3|17|5|8|60728105/101896704|
|19/27|2|317/2|18|53/2|22603355036644932679/37855052008758706176|

The checker verifies complete clearance, every finite rank marginal, all componentwise event minima, and actual global optimal heads through64 and33554432 respectively. These small heads demonstrate non-vacuity of the rational repair theorem, **not an improvement beyond the known head barrier**. — [Exact output and all assertions](fractional_arithmetic_check.py).

### Gaps

- No infinite sequence of these balanced weights with an adequate long head is supplied. The companion feasibility certificates show the two named bases are already impossible for the weaker ideal-capacity problem at6561 and3057647616. Additional repair constraints cannot fix that failure. — [Companion capacity findings](fractional_capacity.md).
- Arbitrary balanced edge flux does not imply corner balance;(FA3) explicitly requires both. An unbalanced repair with donors would need its own arithmetic and head calculation. — [Actual corner examples](fractional_arithmetic_check.py), [integer donor construction](../farey-transport-corrections/boundary_repairs.md).

## Can the actual long head be imposed without expensive auxiliary denominators?

### Takeaway

**Yes: an exact projected polytope in the original72 variables suffices.** Its coefficients have polynomial height in the Farey span at any fixed exponential head. A nonempty such polytope has a rational vertex with a common denominator polynomial in the span. This proves the proposed arithmetic-height reduction, conditional only on actual feasibility. — [Construction above](fractional_arithmetic_check.py), [earlier necessary-capacity distinction](../farey-transport-corrections/torus_bulk.md).

### Cited Findings

- Equal-mass rank matching in a finite balanced component completes exactly the minimum arrived color mass at every actual cutoff, including simultaneous arrivals. The exact certificate tests this identity independently for every component event in the two fractional examples. — [Component minima assertions](fractional_arithmetic_check.py).
- The prior torus inequalities concern an ideal global repair of residual tokens. They are weaker than optimality of the specified corner and individually periodic edge repairs. — [Prior necessary-only scope](../farey-transport-corrections/torus_bulk.md).

### Inferences

**FA5. The actual completed-mass functional.** At cutoff `t`, let `g_k(t)` count completed retained type-k triples, and let `c_E,j(t;x)` be the arrived residual color mass in component `E`. Then the coupling constructed above has exact completed mass

```
G_x(t)=sum_k g_k(t)x_k+sum_E min_j c_E,j(t;x).         (FA8)
```

Here `E` runs over `C` and all edge blocks with an arrived token; there are only `O(log t+1)` such components. Each `c_E,j` is an affine integer-coefficient function of `x`, by(FA2). The rank identity follows because the mass arrived in color j is exactly the initial interval `[0,c_E,j]`; their common intersection has length the minimum. Validity of the coupling gives `G_x(t)<=tau(t)`. Hence its head is optimal through `X` exactly when `G_x(t)>=tau(t)` at every actual arrival event `t<=X`. No arbitrary residual-global-rank replacement has entered the proof. — [Finite interval overlay checked in the certificate](fractional_arithmetic_check.py).

For each event the latter inequality is equivalent to the finite family

```
sum_k g_k(t)x_k+sum_E c_E,sigma(E)(t;x)>=tau(t)
for EVERY choice sigma(E) in {0,1,2}.                (FA9)
```

Indeed minimizing over independent choices gives precisely the sum of minima. This is a polyhedral projection directly into `x`; it introduces no auxiliary variables whose denominators must be cleared. A separation oracle just chooses an actually minimizing color in each component. The possibly exponential number of inequalities affects computational effort but not ambient dimension or the following denominator bound. — [Derivation from(FA8), supported by exact component-minimum identities](fractional_arithmetic_check.py).

**FA6. Coefficient heights across all components.** Fix `K>=1` and `1<=X<=2^(KH)`. Put `R=H+V+12`. Because actual retiming is forward, the total head-token count satisfies

```
N_X<=(floor(log_2 X)+1)(floor(log_3 X)+1)
   <=(KH+1)^2 <=(K+1)^2 R^2.                         (FA10)
```

The components are disjoint. In any selected sum in(FA9), each arrived token can occur at most once. Therefore the magnitude of a combined residual coefficient, summed over **all** chosen components, is at most `N_X`; the bulk coefficient is also at most `N_X`. This is not a per-block bound multiplied once more by `O(H)`. Right sides after moving constants have magnitude at most `2N_X`. The finite corner contains at most `R^2` points and each edge root at most `R^2`; their balance-equation coefficients have magnitude at most `2R^2`. Thus every coefficient and right side in coverage, nonnegativity, balance and head inequalities has magnitude at most

```
L=4(K+1)^2 R^2.                                     (FA11)
```

All events are actual arrivals, independent of x; between them every count is constant. Consequently there are finitely many inequalities despite the original all-real-cutoff wording. — [Token timing and finite component definitions](fractional_arithmetic_check.py), [explicit projection(FA9)].

**FA7. A single determinant clears every weight.** Let `P_X` be the polytope just specified. It is bounded since coverage implies `0<=x_k<=1`. If nonempty it has a vertex. At that vertex select72 linearly independent active normals, including equality rows as necessary; boundedness guarantees that the active normals span the ambient space. This gives an invertible72-by72 integer system `Ax=b` with entries bounded by L. Cramer's rule gives one common clearing factor

```
S=|det A|,       Sx in Z^72,
1<=S<=(sqrt(72)*L)^72.                              (FA12)
```

The determinant bound follows by bounding each row's Euclidean norm by `sqrt(72)L` and applying the elementary volume bound. It does not multiply72 separate reduced denominators. In the bounded-slope regime `log S=O(log H)`. Combining(FA6) and(FA12) proves complete degree-two arithmetic for **any nonempty actual-head polytope**. No numerical LP result is used. — [Single-denominator rank construction verified in the certificate](fractional_arithmetic_check.py); determinant and projection arguments are the new derivation(FA9)-(FA12).

**FA8. Growing original-coordinate periods.** The same proof holds for any period `m` divisible by6, with `d=2m^2` anchored types, `A=mceil(H/m),B=mceil(V/m)`, and balanced corner plus two m-wide edge roots. Replace63,728 by `2^m-1,3^m-1`; a safe fixed-period constant is

```
C_m=(2^m-1)(3^m-1)2^m3^m,
D=S C_m2^A3^B.                                     (FA13)
```

The stream identity is `x[1/M_act+1/((2^m-1)M_asym)+2^m/((2^m-1)(3^m-1)M_raw)]`. Actual low-row exceptions are still isolated in the first term. The component and coefficient bounds are polynomial in `H+V+m`; applying the same d-dimensional determinant estimate gives

```
log S=O(m^2 log(H+V+m)),
log D=Hlog2+Vlog3+O(m+m^2 log(H+V+m)).               (FA14)
```

Thus `m^2 log(H+m)=o(H)` preserves clearing exponent two when `V=O(H)`. This is a proved parameterized arithmetic implication, not evidence that any larger-period polytope is feasible. The checker exercises m=6 only; the displayed general identities and coefficient proof supply the extension. — [m=6 exact construction](fractional_arithmetic_check.py), [periodic bulk resummation input](../farey-transport-corrections/farey_bulk.md).

### Gaps

- The determinant bound proves cheap weights **if** the actual-head polytope is nonempty. It gives no feasibility theorem, no efficient algorithm for the projected inequality family, and no favorable actual infinite subsequence. — [Companion finite obstructions](fractional_capacity.md).
- The super-two-span head cannot be inferred from coverage, balanced components, or nearly equal bulk times alone. All of(FA9) must hold for the actual logarithmic rotation. — [Earlier failed inference and capacity examples](../farey-transport-corrections/boundary_repairs.md).

## Does this fractional framework supply nonzero errors and an exact route to irrationality?

### Takeaway

**Strict nonvanishing extends to every constructed fractional candidate.** What remains is an actual infinite feasibility theorem at a head longer than the degree-two clearing scale. Proving that theorem would complete this coupling route; it has not been proved here. — [Strictness input](../rational-coupling-construction/coupling_strictness.md), [complete fractional construction](fractional_arithmetic_check.py).

### Cited Findings

- For actual retimed tokens the color imbalance `E(T)=N(exp T)-3tau(exp T)` is `o(T)`. The existing dispersion proof uses positivity of partial-token mass and lattice area counts. — [Strictness theorem and its actual-rotation input](../rational-coupling-construction/coupling_strictness.md).
- The complete ordinary finite optimum and density identities are accepted inputs; this note neither reproves nor weakens their scope. — [Finite proof and audits](../prefix-and-phase-audit/REPORT.md).

### Inferences

**FA9. Weighted dispersion is still strict.** In a fractional coupling define completed mass `G(T)` and partial-token mass `U(T)=N(exp T)-3G(T)>=0`. Then

```
3(tau(exp T)-G(T))=U(T)-E(T)>=0.                    (FA15)
```

At least one type has weight `x_k>0`, since `sum x_k=12`. Deep ordinary retained triples of that type have anchors in a full-index lattice coset. Their number completed by logarithmic cutoff T is `aT^2+O(T)`, `a>0`. Each has fixed positive logarithmic dispersion `g=3max h_j-sum h_j>0`; distinct ordinary times cannot coincide because `2^a3^b=2^c3^d` forces `(a,b)=(c,d)`. Integrating U from0 toT counts at least `x_k g(aT^2+O(T))`, while integrating E gives `o(T^2)`. Equation(FA15) therefore cannot vanish identically. Its nonnegative cost integral is strictly positive:

```
0<M-Q(x).                                          (FA16)
```

This is exactly the positive dispersion argument with masses retained throughout; overlapping supports do not subtract partial mass. The basis, x and g are fixed for each candidate. No positive lower bound uniform in H is claimed or needed. — [Original lattice and integrated-partial-mass proof](../rational-coupling-construction/coupling_strictness.md), [unit marginals of the new construction](fractional_arithmetic_check.py).

**FA10. The precise sufficient remaining theorem.** Fix `epsilon>0`. If actual Farey levels with `H->infinity` have nonempty polytopes above for

```
X_H>=2^((2+epsilon)H),                              (FA17)
```

then first restrict each head to exactly `2^((2+epsilon)H)` and choose the rational vertices from(FA12) at the fixed value `K=2+epsilon`. This restriction preserves nonemptiness and is necessary to invoke the stated fixed-exponential coefficient bound. Their full couplings have no completed-count deficit through that head; their positive tail cost gap is bounded by the smooth reciprocal tail `O(log X_H/X_H)`, with `X_H` now denoting the restricted head. Equations(FA7),(FA12),(FA16) give

```
DQ in Z,       0<D(M-Q)<=H^O(1)*2^(-epsilon H)->0.    (FA18)
```

If `M=A/B` were rational, the positive quantities `BD(M-Q)` would be integers tending to zero, an impossibility. Thus(FA17) plus the already proved construction would imply irrationality of M and c. This implication also holds with growing m satisfying(FA14)'s sublinear overhead. It is an explicit conditional reduction, not a proof that(FA17) occurs. The older signed hierarchy still needs its own boundary arithmetic and nonvanishing; no residual identification is supplied here. — [Accepted arithmetic interface](../farey-transport-corrections/REPORT.md), [construction and small-head scope](fractional_arithmetic_check.py).

### Gaps

- **The actual infinite long-head feasibility assertion(FA17) remains open.** The two named period-six cases fail even before this restricted repair is considered. None of the conditional results prove Erdős #168(ii). — [Companion capacity certificates](fractional_capacity.md).
- Skipped: Lean, package installations, density decimals, broad model searches, external review, priority verification and edits to archived notes. Main risk: treating the proved fixed-dimensional arithmetic implication as an actual feasibility or infinite-return theorem. — [Certificate scope](fractional_arithmetic_check.py).
