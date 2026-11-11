# Opposite-side numerator reflection for Erdős 168(ii)

## Does a rational-model tile have an exact reflection, with all floor ties and corrections retained?

### Takeaway

There is an exact new **opposite-side reflection of the uncorrected state**, including its axes. Its cone readout is invariant under reflection. The actual corrected high-row coefficients do **not** obey that palindrome: all three prescribed models fail already at `(a,b)=(0,5)`. The exact replacement is a weighted cone-boundary local-time identity, derived below. It does not remove the active correction from the target density.

### Cited Findings

- The existing model, positive-index floor conventions, four exceptional low-row tests, and normalization `Z=9c−6` are the inputs. Their earlier conditional finite formula is now proved. — [Current return report](../infinite-return-construction/REPORT.md), [finite report](../prefix-and-phase-audit/REPORT.md), [audited model](../global-boundary-proof/independent_audit.md).
- Full skew covariance already supplies a different high-row three-term relation; it does not imply scalar factor cancellation. — [Skew-denominator proof](../infinite-return-construction/skew_denominator.md).
- The narrow new certificate independently checks the reflection identities for both signs on the three named tiles, the forward correction formula, the low-row numerator formula, and the saved exact model values. Its coordinate and ray identities have separate small assert checks. It imports the older model without writing bytecode. — [New checker](numerator_reflection_check.py), [exact results](numerator_reflection_check.json).

### Inferences

All identities in this subsection are proved here. Let `ω²+ω+1=0`, take coprime `3/5<p/q<2/3`, assume `p+q≠0 mod3`, and put `P=3q,Q=3p`. Both signs `σ∈{+1,−1}` below are model parameters; only one agrees with the true logarithmic slope at the first rational tie. Set

```
mσ(k)=floor_σ(kp/q),       nσ(l)=floor_(−σ)(lq/p),
S(r)=Σ_(j=0)^r ω^(2j),    T(r)=Σ_(i=0)^r ω^i,
eσ=1_[σ>0].
```

`S,T` are extended with period three. The two axis paths start at `Aσ(0)=Bσ(0)=1`; the negative-side floor convention is **not** applied to the index-zero initial state. Their increments are

```
fσ(k)=ω^(−k)S(mσ(k)),       gσ(l)=ω^(−2l)T(nσ(l)).
```

Both paths have their proved periods `P,Q`. For `1≤k<P`, the exact floor identity is

```
mσ(P−k)=3p−1−m_(−σ)(k).
```

It includes interior rational ties: the two opposite endpoint conventions add to one less than the integer complement. Also

```
S(−1−r)=1−conj S(r),       T(−1−r)=1−conj T(r).
```

Consequently `fσ(P−k)=ω^k−conj f_(−σ)(k)`. The endpoint must be separated: `fσ(P)=eσ`, while `gσ(Q)=1−eσ`. Summing backwards, and using the full-period sums zero, proves

```
Aσ(a)=conj A_(−σ)(P−1−a)+S(a)−eσ,        0≤a<P,
Bσ(b)=conj B_(−σ)(Q−1−b)+T(b)−(1−eσ),    0≤b<Q.       (R1)
```

For example, the axes force `Aσ(P−1)=1−eσ`, `Bσ(Q−1)=eσ`; they are not unspecified boundary errors.

Let

```
C(a,b)=(S(a)−1)(T(b)−1),
zσ(a,b)=Aσ(a)+Bσ(b)−1+C(a,b),
a*=P−1−a,    b*=Q−1−b.
```

Here `S(a)=Σ_(j=0)^a ω^(−j)` and `T(b)=Σ_(i=0)^b ω^(−2i)`, so this `C` is exactly the audited residue table. Since

```
conj C(a*,b*)=S(a)T(b),
S(a)+T(b)−1+C(a,b)=S(a)T(b),
```

the endpoint terms in (R1) cancel **exactly**:

```
                    zσ(a,b)=conj z_(−σ)(a*,b*).           (R2)
```

The closed cone is `F(x+yω)=1_[x≤0 and x−y≤0]`. Conjugation sends `(x,y)` to `(x−y,−y)` and exchanges its two inequalities. Thus `F(conj z)=F(z)`, including every lattice tie. If `fσ^0=1−3F(zσ)` denotes the artificial **uncorrected** readout, then

```
fσ^0(a,b)=f_(−σ)^0(a*,b*),
Tσ^0(X,Y)=X^(P−1)Y^(Q−1)T_(−σ)^0(X^(−1),Y^(−1)).     (R3)
```

Using `P−a,Q−b` instead of `P−1−a,Q−1−b` requires a local insertion term. With paths and residues extended periodically, the exact statement is

```
zσ(a,b)−conj z_(−σ)(P−a,Q−b)
 =fσ(a)+gσ(b)+C(a,b)−C(a−1,b−1).                    (R4)
```

At zero coordinates the increments in (R4) mean the periodic wrap increments `fσ(0)=fσ(P)`, `gσ(0)=gσ(Q)`, not an invented negative-side origin floor. Formula (R2), which has no such convention issue, is preferable for numerator reversal.

**The actual reflected correction.** Periodically extend the valid high-row indicator `Eσ(b)` to all integer `b`, using `nσ(b+Q)=nσ(b)+3q`. Equivalently evaluate its high-row formula at `b mod Q+Q`. In the formula below, the rational floor lift is allowed at all integers solely to define this periodic extension. Its positive-index values are the original ones. Set `Eσ*(b)=conj E_(−σ)(Q−1−b)`. Direct integer complementation gives

```
Eσ*(b)
 =1_[nσ(b+2)−nσ(b+1)=2] ω^(nσ(b+1)−2b−1)
  +1_[nσ(b+4)−nσ(b+2)=4] ω^(nσ(b+2)−2b).            (R5)
```

For example, `n_(−σ)(Q−1−b)=3q−1−nσ(b+1)`. The isolated condition consequently becomes a forward difference at `b+2`, and its conjugated color is `nσ(b+1)−2b−1`. The patch condition similarly becomes the forward two-step difference in (R5). The two tests do not overlap, because they are precisely the reflected original tests, in the audited admissible slope interval.

Write `Eσ(b)=Σ_j εσ_j(b)ω^j`, `Eσ*(b)=Σ_j εσ*_j(b)ω^j`, where each indicator vector has at most one nonzero entry. For `z=x+yω`, define the signed ray indicators

```
R0(z)=−1_[x−1=min(y,0)],
R1(z)= 1_[x=y≤0],
R2(z)= 1_[x=0 and y≥0].
```

Checking the two closed-cone inequalities directly gives

```
1−3F(z−ω^j)=1−3F(z)+3Rj(z).                          (R6)
```

This includes the same-color diagonal response `R0`; its minus sign cannot be dropped. In count notation `Qstate=(x,y,0)`, these indicators are `D0 Dj min(Qstate−e0−ej)`. Thus they agree with, and sharpen to explicit coordinates, the earlier Hessian response.

Let `hσ(a,b)=1−3F(zσ(a,b)−Eσ(b))` denote the periodic high-row extension. Equations (R2), (R5), and (R6) prove the **full corrected reflection identity**

```
hσ(a,b)−h_(−σ)(a*,b*)
 =3 Σ_(j=0)^2 [εσ_j(b)−εσ*_j(b)] Rj(zσ(a,b)).       (R7)
```

In all three prescribed models, using the sign toward the actual slope, the checker gives

| `p/q` | `σ` | `zσ(0,5)` | `Eσ(5)` | `Eσ*(5)` | `hσ(0,5)` | reflected `h_(−σ)` |
|---|---:|---:|---:|---:|---:|---:|
| `5/8` | `+1` | `0` | `0` | `ω` | `−2` | `1` |
| `12/19` | `−1` | `0` | `0` | `ω` | `−2` | `1` |
| `53/84` | `−1` | `0` | `0` | `ω` | `−2` | `1` |

Both the original row and its reflected row are high rows. The error is therefore not an axis artifact. Although the correction **changes** at events on a few low exponent rows, an active correction affects the winning phase at arbitrarily high-row insertions. Replacing `hσ` by `fσ^0` changes the density by the associated weighted ray occupations, whose rationality is unproved; there is no justification for declaring the difference a known rational constant.

### Gaps

- (R7) leaves an entire weighted ray-local-time polynomial. No bounded-term arithmetic evaluation of that polynomial is proved.
- The uncorrected model in (R3) approximates its own uncorrected target, not automatically `Z`. Rationality of the corrected target does not establish rationality of that new target.

## What exact scalar-numerator identity survives the low rows, and does it supply p-adic smallness?

### Takeaway

The reflected numerator is a positive-weight evaluation of the **opposite** polynomial, with explicit ray and low-row corrections. It is not the opposite model's original weighted numerator. Neither that algebraic reversal nor rationality of a real limit identifies the associated 2-adic or 3-adic limit. An explicit palindromic countermodel proves this failure even without the actual correction obstruction.

### Cited Findings

- The actual `53/84` reduced denominator is `D/6`; this was independently audited before the present work. — [Final return audit](../infinite-return-construction/final_return_audit.md).
- All three saved rational values are independently recovered by the numerator formula below; the certificate also gives their exact numerator valuations and the palindromic countermodel. — [New checker](numerator_reflection_check.py), [results](numerator_reflection_check.json), [saved original values](../../early-attacks/augmentation-and-return-attacks/returns_check.json).

### Inferences

Write `U=2^P,V=3^Q`. Let `lσ(a,b)` be the audited low-row coefficient **without** its single `(0,1)` exception, minus `hσ(a,b)`, for `0≤b≤3`. Retain every distinct low-row test. Define

```
Hσ(X,Y)=Σ_(0≤a<P,0≤b<Q) hσ(a,b)X^aY^b,
Lσ(X,Y)=Σ_(0≤a<P,0≤b≤3) lσ(a,b)X^aY^b.
```

The actual model generating function is exactly

```
Gσ(X,Y)=Hσ(X,Y)/[(1−X^P)(1−Y^Q)]
        +Lσ(X,Y)/(1−X^P)−3Y.                       (N1)
```

The last term is the single true origin exception; its evaluation is `−1`. In particular, the exceptional low rows repeat horizontally but **do not** repeat vertically. Treating the first full fundamental tile as the entire periodic array would repeat those exceptions incorrectly.

Put

```
Wσ=Σ hσ(a,b)2^(P−1−a)3^(Q−1−b),
Jσ=Σ_(a<P,b≤3) lσ(a,b)2^(P−1−a)3^(3−b),
D=27(U−1)(V−1).
```

Then (N1), evaluated at `(1/2,1/3)`, gives the integer numerator formula

```
Z~σ=Nσ/D,
Nσ=162 Wσ+2Jσ(V−1)−D.                              (N2)
```

This is independently equal to the older checker for all three named models. Summing (R7) with the reversed integer weights gives

```
Wσ=H_(−σ)(2,3)+3Kσ,
Kσ=Σ_(a<P,b<Q) Σ_j [εσ_j(b)−εσ*_j(b)]Rj(zσ(a,b))
                         ·2^(P−1−a)3^(Q−1−b),
Nσ=162H_(−σ)(2,3)+486Kσ+2Jσ(V−1)−D.                (N3)
```

Every axis, low-row and tie term is now present. The reversal sends `(1/2,1/3)` to `(2,3)`. The expression `H_(−σ)(2,3)` is not `W_(−σ)`, so it cannot simply be replaced by the opposite model's approximation to the real target.

The coefficients in (N3) are integers, but the new integer data need not be small: `|Wσ|≤(U−1)(V−1)`, `|Kσ|≤(U−1)(V−1)/2`, and `|Jσ|≤120(U−1)` follow from their alphabets and geometric sums. Their available bounds have exponential height on scale `q`, not subexponential coefficient cost. Placing these quantities into extra coordinates does not, by itself, supply a small fixed linear form.

The nominal valuations from (N2) are:

| `p/q` | `v2(Nσ)` | `v3(Nσ)` | `v2(D)` | `v3(D)` | `gcd(Nσ,D)` |
|---|---:|---:|---:|---:|---:|
| `5/8` | 1 | 3 | 1 | 5 | 702 |
| `12/19` | 1 | 5 | 4 | 3 | 3510 |
| `53/84` | 1 | 1 | 1 | 6 | 6 |

These finite cases do not disprove a special successful subsequence. They do disprove any proposed universal exponential-divisibility conclusion that already applies to these models at their full periods.

**Why a rectangular reflected prefix does not define a common p-adic sum.** A positive-weight polynomial `Σ c(a,b)2^a3^b` converges neither 2-adically nor 3-adically over the entire quadrant: the terms on `a=0` have 2-adic valuation at most one, and those on `b=0` are units at 3. A 2-adic residue modulo `2^r` requires every `b` on the strip `a<r`; agreement only on a rectangle `a<r,b<s` does not determine it. The 3-adic obstruction exchanges the two variables. Grouping the other variable through its rational periodic denominator stores its full strip numerator and therefore does not remove this issue.

**Exact countermodel to rationality transfer from palindromy.** For every `n≥0`, let `P=6n+3,Q=6n+6`, `U=2^P,V=3^Q`, and make a doubly periodic tile with alphabet `{1,−2}`. Set both opposite corners `(0,0),(P−1,Q−1)` equal to `−2` and every other entry equal to `1`. This tile is exactly palindromic. Its real weighted sum is

```
Z_n=−3(U+V+5)/[(U−1)(V−1)] → 0.                   (N4)
```

The limiting infinite coefficient array is also explicit: it is `1` everywhere except `c(0,0)=−2`; its real sum is `3−3=0`. Thus the limit is rational with arbitrarily long coefficient-prefix agreement.

Nevertheless its cleared numerator `M_n=−3(U+V+5)` has

```
v2(M_n)=v3(M_n)=1             for every n.          (N5)
```

Indeed `P` is odd, so `U+V+5≡1 mod3`; `Q` is even and `P≥3`, so `U+V+5≡6 mod8`. Multiplication by `−3` gives (N5). Formula (N4) follows by subtracting the two corner defects from the constant-array sum `3`; it is also checked independently by exact finite rational summation at three sizes. This is a general countermodel to an implication based only on bounded digits, reflection, real prefix convergence and rationality of the real limit. It does **not** model the actual cocycle, so it does not rule out an argument using new special properties of that cocycle.

### Gaps

- No identity makes `Kσ` or `Jσ` a fixed rational-coefficient combination of a bounded number of S-units.
- No theorem identifies a putative reflected p-adic limit with the rational number hypothesized to equal the real density.
- No growing numerator divisibility along an actual infinite eligible sequence has been proved or disproved.

## Does the reflection meet a primary arithmetic theorem on an actual infinite sequence?

### Takeaway

Not yet. For the existing five-coordinate form, the exact three-place product is `|DZ−N| |N|2 |N|3`. The reflection supplies no additional exponentially small factor. The existing matching window therefore still needs the unproved `q_next−5q→∞` supply, together with nonstabilization; the new identities are auxiliary progress rather than an adequate infinite return.

### Cited Findings

- The primary one-form p-adic Subspace Theorem permits one fixed algebraic linear form at a distinguished place and coordinate forms elsewhere; its conclusion is containment in finitely many proper subspaces. It uses projective Weil height. — [Luca–Ouaknine–Worrell, Theorem 1](https://arxiv.org/html/2412.07908v2#S2.Thmtheorem1), checked directly in this research turn.
- The fixed-unit nonzero lower bound has the essential restriction `0<t≤min(1,u_i)`, and the KK application separately proves a nonzero choice before using it. — [KK primary manuscript, Proposition 7.4 and Corollary 6.5](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf), [saved primary text](../Erdos%20theorem%20transfer%20investigation/erdos1062-fork-free-density.pdf.txt), text lines 777–790 and 841–865.
- Subexponential integer multiplicities are admissible only with fixed term count and their explicit coefficient loss charged. — [Derived coefficient extension](../../early-attacks/augmentation-and-return-attacks/coefficient_extension.md).
- The guaranteed nonresonant supply gives ratios above `(15+sqrt(5))/10` infinitely often for the actual slope, not the threshold five needed here. — [Supply proof and sharpness](../infinite-return-construction/diophantine_supply.md), [final audit](../infinite-return-construction/final_return_audit.md).

### Inferences

Assume `Z` rational. For an actual-side eligible convergent put

```
x=(N,UV,U,V,1),
L∞(x)=27Z·UV−27Z·U−27Z·V+27Z−N=E.
```

There are five coordinates and four fixed rational coefficients on positive `{2,3}`-units `UV,U,V,1`; the coefficient of `N` is `−1`. With `S={∞,2,3}`, distinguish `N` at infinity in the primary one-form theorem. Each unit has product of its absolute values over `S` equal to one. Therefore the **complete** local product is

```
Φ(x)=|L∞(x)| · ∏_((i,v)≠(N,∞)) |x_i|v
    =|E| |N|2 |N|3.                                (A1)
```

The integer vector is primitive because its last coordinate is `1`, and

```
H(x)≤162UV=exp((6+o(1))q log2).                     (A2)
```

Coordinate-zero cases lie in fixed hyperplanes and do not create an omitted local factor. The nominal numerators in the three certificates are nonzero. When the actual one-form product is below `H^(−ε)`, the primary conclusion is finite-subspace containment; it is **not** automatically a contradiction. To finish through this route one must also rule out the relevant exceptional relations. The mixed-unit lower-bound induction handles them for a nonzero form with a small **real** error; claiming a new gain merely from (A1) would require the corresponding new exceptional-relation argument.

For comparison with the fixed-unit lower bound, choose `t=1`: this is allowed and is the largest admissible choice. The established real estimate is

```
|E|≤486(1+o(1))2^(5q−q_next).                       (A3)
```

Thus the named numerator valuations do not improve its exponential scale. Even a general additional bound `2^(v2(N))3^(v3(N))≥2^(κq)` would require a new proof, an infinite actual sequence, and control of exceptional relations before extracting a multi-place contradiction.

Scaling the approximating equation by `UV` cannot erase the cost. The projective vector becomes

```
x/(UV)=(N/(UV),1,1/V,1/U,1/(UV)),
```

has the same height, and its one-form product remains (A1), because

```
|N/(UV)|2 |N/(UV)|3 = UV |N|2 |N|3.
```

The smallest displayed unit is `1/(UV)`, so a lower-bound application cannot use a common scale larger than that. The visible real approximation `|E|/(UV)` must be compared with this minimum unit; their ratio is again `|E|`. Moreover `N/(UV)` is an S-integer with variable numerator, not an integer term as in Proposition 7.4. Treating it as an integer would change that theorem's hypotheses.

If rationality `Z=A/B` is assumed, the original `E=DZ−N` lies in the fixed lattice `B^(−1)Z`. Hence `E→0` already implies eventual equality. The known sufficient supply is `q_next−5q→+∞` along infinitely many actual eligible indices; it remains unproved, and eventual equality must still be contradicted separately. Reflection (R2) and its exact corrections (R5)–(N3) have not supplied that sequence, a smaller arithmetic denominator, or the requisite nonvanishing.

### Gaps

- **The requested adequate infinite weighted-return construction remains open in this branch.** No true infinite sequence satisfies all of fixed dimension, controlled coefficients, height, minimum-unit scale, fixed exponential improvement and nonzero remainder on the basis of these results.
- The precise new obligation for this reflection approach is an arithmetic control of the weighted ray term in (N3), or a direct proof of appropriate numerator congruences plus an exceptional-subspace argument. An uncorrected symmetry alone does not meet it.
- Only the new note and its narrow exact certificates were written. No broad parameter sweep, density decimals, dependency installation, old-file edits, Lean work or external post was performed.
