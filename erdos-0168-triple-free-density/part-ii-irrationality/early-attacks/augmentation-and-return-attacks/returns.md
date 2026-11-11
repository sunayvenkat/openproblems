# Erdős 168: exact double returns and a four-unit periodic approximant

**The irrationality target remains unresolved.** This round proves an unconditional double-return identity with an integer corner term, and constructs a concrete rational periodic approximant conditional on (C). Its cleared error is a fixed four-unit form. The exact repetition length exposes two missing ingredients: sufficiently long suitable returns and nonvanishing. The calculation does not rule out a different sparse-return argument.

## What does a horizontal–vertical double return cancel exactly?

### Takeaway

The finite corner clears to an integer, but two infinite side-return series remain. The nonlinear mixed interior is an exact four-cone difference; it vanishes whenever either axis state returns. Thus the interior can have a product-size saving while the sides remain the dominant obligation.

### Cited Findings

- The unconditional coefficients are `c_(a,b)=1-3η_(a,b) in {1,-2}`, and `Z=sum c_(a,b)2^(-a)3^(-b)=9c-6`. The earlier one-shift identity does not resum its boundary atoms. — [Prior weighted identities](../open-proof-gap-attacks/weighted.md).
- The rotated color state separates as `A_a+B_b-1+C_(a mod3,b mod3)`, and its cone birth rule is conditional on (C). — [Reviewed arithmetic separation](../../investigations/boundary-and-arithmetic/arithmetic.md), [independent review](../../investigations/boundary-and-arithmetic/arithmetic_review.md).
- A solver-free exact check verifies the double-return algebra on a finite rational array. The other checks concern three specified rational models, not a new optimization sweep. — [Checker](returns_check.py), [saved results](returns_check.json).

### Inferences

**Unconditional identity.** Fix positive integer periods P,Q and write `u=2^P`, `v=3^Q`. Define

```
δ_H c(a,b)=c(a+P,b)-c(a,b),
δ_V c(a,b)=c(a,b+Q)-c(a,b),
N_(P,Q)=uv sum_(0≤a<P,0≤b<Q) c(a,b)/(2^a3^b).
```

The last quantity is an integer. Absolute convergence and reindexing give

```
(u-1)(v-1)Z - N_(P,Q)
 = u sum_(0≤a<P,b≥0) δ_V c(a,b)/(2^a3^b)
 + v sum_(a≥0,0≤b<Q) δ_H c(a,b)/(2^a3^b)
 +   sum_(a,b≥0) δ_Hδ_V c(a,b)/(2^a3^b).                 (1)
```

For verification, let R be the finite corner sum, H the full strip a<P, and V the full strip b<Q. The mixed series is

```
(u-1)(v-1)Z-u(v-1)H-v(u-1)V+uvR.
```

The first side-return series before its factor u is `(v-1)H-vR`; the second before its factor v is `(u-1)V-uR`. Adding them proves (1), including its signs and its single integer head `uvR`.

The first and second differences have coefficients respectively in `{0,±3}` and `{0,±3,±6}`. Equation (1) has four head units `uv,u,v,1` if Z is rational, but infinitely many side and interior terms unless a further return theorem is supplied.

**An exact nonlinear mixed-state formula.** For b≥4 put

```
E_b=ε_(b,0)+ε_(b,1)ω+ε_(b,2)ω²,
T_b=B_b-E_b,
F(x+yω)=1_[x≤0 and x-y≤0].
```

Conditional on (C), `η_(a,b)=F(A_a+T_b-1+C_(a mod3,b mod3))`. For P,Q divisible by three, let

```
z=A_a+T_b-1+C_(a mod3,b mod3),
r_a=A_(a+P)-A_a,  s_b=T_(b+Q)-T_b.
```

Then

```
δ_Hδ_V c(a,b)
 = -3[ F(z+r_a+s_b)-F(z+r_a)-F(z+s_b)+F(z) ].          (2)
```

Encoding ε in T includes its changes; no extra indicator-periodicity assumption is hidden in (2). The mixed term is zero if either r_a=0 or s_b=0. If these returns vanish for `0≤a<R` and `4≤b<S`, respectively, then the part of the mixed series with b≥4 is supported in `a≥R,b≥S`, and has absolute value at most

```
18·2^(-R)3^(-S).                                      (3)
```

The four low columns remain separate. The two side-return tails have only a single-axis decay: once their respective initial returns vanish, the bounds are at most `9u·3^(-S)` and `9v·2^(-R)`, apart from explicitly retained low-column terms. These factors u and v are the reason that good cancellation of the mixed interior alone is insufficient.

### Gaps

The side series in (1) have not been evaluated or compressed for the true cone process. Formula (2) is conditional on (C), whereas (1) is unconditional. A nonzero mixed difference or a long unweighted return does not imply a nonzero weighted remainder.

## Can an explicit periodic model produce a fixed-dimensional S-unit form?

### Takeaway

Yes. A one-sided rational floor model with periods 3q and 3p has a rational weighted sum whose denominator divides `27(2^(3q)-1)(3^(3p)-1)`. Its error is therefore a four-unit form with fixed coefficients under rationality. Consecutive convergents give an exact, proved matching window; they do not automatically make that window long enough.

### Cited Findings

- KK Proposition 7.4 fixes the number of units and coefficient vector. Corollary 6.5 separately provides nonzero error, sufficient exponential saving, and height control; the application in §7.3 uses all three. — [Primary manuscript](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf), [saved source, Proposition 7.4 and Corollary 6.5](../Erdos%20theorem%20transfer%20investigation/erdos1062-fork-free-density.pdf.txt).
- The current exact checker verifies axis periodicity, the denominator, and agreement with the same 120 previously certified optima for each of the three specified approximants. It also verifies the first floor disagreements by integer power comparisons. — [Checker](returns_check.py), [results](returns_check.json).

### Inferences

Write `α=log_3 2`, `β=1/α`, and choose coprime p,q with `1/2<p/q<2/3`. Put `σ=sign(α-p/q)`. For positive n define `floor_σ(np/q)` to be the usual floor, except that an exact integer is reduced by one when σ<0. This is the one-sided limiting floor toward α. The reciprocal slope uses the opposite sign.

Define the model axis states by

```
A~_0=B~_0=1,
A~_a-A~_(a-1)=ω^(-a) S(floor_σ(ap/q)),
B~_b-B~_(b-1)=ω^(-2b) P(floor_(-σ)(bq/p)),
```

where `S(m)=sum_(j=0)^m ω^(2j)` and `P(m)=sum_(i=0)^m ω^i`, both extended three-periodically.

**Why the state, not just its increments, becomes periodic.** Assume

```
p+q is not 0 modulo 3.                                 (4)
```

Set `P=3q`, `Q=3p`. The A increments have period P. Using

```
S(m)=(1-ω^(2m+2))/(1-ω²),
```

their sum over P splits into a vanishing sum of `ω^(-a)` and a second sum grouped by a=r+jq. Its three j terms have common ratio `ω^(2p-q)`, a nontrivial cube root by (4), so that sum vanishes as well. Thus `A~_(a+P)=A~_a`. The B proof is identical, with ratio `ω^(q-2p)`. The one-sided convention respects the required integer shift, including its exact ties. Therefore `B~_(b+Q)=B~_b`.

**A floor-only expression for the corrections.** For the true process, write `m_b=floor(bβ)`. For b≥4 the indicator conditions are equivalently

```
isolated iff m_b-m_(b-1)=2,
patch    iff m_(b-1)-m_(b-3)=4.                         (5)
```

The isolated color is `m_b-2b`; the patch color is `m_(b-1)-1-2b`, modulo three. For example, the patch's largest possible root has exponent `m_(b-1)-1`, and its strict upper-end condition is exactly `m_(b-1)-m_(b-3)≥4`. Since `3/2<β<5/3`, the relevant differences are only 1/2 and 3/4, respectively. Formula (5) also proves periodicity of the model corrections when `m_b` is replaced by its one-sided rational version: `m~_(b+Q)=m~_b+3q`.

Use the reviewed cone rule with A~, B~, C and these model corrections for b≥4. The four low columns have explicit fixed tests. If `Z~_(a,b)=x+yω`, the tests are

```
b=0: η~=0;
b=1: η~=1_[x≥1 and y≥0], except η~_(0,1)=1;
b=2: η~=1_[x≤-1 and x-y≤0];
b=3: η~=1_[min(x,0)≤y].                                (6)
```

These low-column rules follow from the actual indicator changes. At b=1 and a≥2, the isolated endpoint disappears and the patch starts, so only rotated adjusted count 2 increases. At a=1 the same test still gives the true digit 0; a=0 has digit 1. At b=3 the patch ends, so adjusted counts 0 and 2 both increase. The b=2 correction is always the isolated color 2. Thus (6) includes the finite-column edges rather than ignoring them.

Put `c~=1-3η~` and `Z~=sum c~_(a,b)2^(-a)3^(-b)`. Without the exception at (0,1), this array has period P in a everywhere and period Q in b for b≥4. The exception subtracts exactly 1 from its weighted sum. Summing the first four rows and the P-by-Q tail tile geometrically proves

```
D=27(2^P-1)(3^Q-1),
N=D Z~ is an integer.                                  (7)
```

This is an actual finite rational model; no eventual periodicity of a true infinite column is assumed.

**Exact repetition window from consecutive convergents.** Let p′/q′ be the next continued-fraction convergent after p/q. Then the one-sided floor model agrees with `floor(nα)` for

```
1≤n<q+q′,
```

and disagrees at n=q+q′. The reciprocal statement has p+p′ in place of q+q′.

Here is an elementary proof of the needed approximation fact. Consecutive convergents have determinant ±1, and α lies between their mediant and p′/q′: writing the remaining continued-fraction tail as t>1 gives `α=(p′t+p)/(q′t+q)`. Every rational strictly between the two convergents has, by inversion of their unimodular two-by-two matrix, numerator and denominator `kp+lp′`, `kq+lq′` with positive integers k,l. Its denominator is at least q+q′. The mediant has that denominator and lies strictly between p/q and α. A floor disagreement away from a rational tie occurs precisely when such a rational threshold has been crossed; at multiples of q the one-sided convention handles the tie correctly. This proves the assertion and its reciprocal without an assumption on the size of the next partial quotient.

Consequently A~=A for a<q+q′, B~=B for b<p+p′, and their corrections agree throughout the corresponding range. **Conditional on (C)**, all model birth digits agree with the true digits whenever

```
2^a3^b < X := min(2^(q+q′), 3^(p+p′)).                 (8)
```

The checker gives the exact examples

| p/q | next p′/q′ | first A floor disagreement | first B floor disagreement | periods P,Q |
|---|---|---:|---:|---:|
| 5/8 | 12/19 | 27 | 17 | 24,15 |
| 12/19 | 41/65 | 84 | 53 | 57,36 |
| 53/84 | 306/485 | 569 | 359 | 252,159 |

The first disagreements concern floor words; a cone digit could remain unchanged there. No converse assertion about the first changed birth digit is made.

**The four-unit form and its exact scale.** Under the temporary assumption Z rational, let u=2^P,v=3^Q. Equations (7)–(8) give

```
E=DZ-N =27Z·uv-27Z·u-27Z·v+27Z·1-N.                  (9)
```

Its four coefficients are fixed once Z is fixed. All units are at least 1. Since `|Z~|≤6`,

```
H(N:uv:u:v:1)≤162uv.                                 (10)
```

For any Y<X, agreement and the elementary geometric tail estimate give

```
|Z-Z~|≤3( (3/2) floor(log_2 Y)+9/2 )/Y,
|E|≤81(u-1)(v-1)( (3/2) floor(log_2 Y)+9/2 )/Y.        (11)
```

For completeness, the tail estimate follows by summing each row with a≤floor(log_2 Y), bounding it by `3/(2Y)`, and then summing the remaining dyadic rows. It works for the inclusive tail as well.

As q tends to infinity through convergents,

```
log(uv)=3q log2+3p log3=6q log2+o(1),
log X = min((q+q′)log2,(p+p′)log3).
```

Thus a sufficient condition for a fixed exponential saving in (11) is

```
q′/q > 5+δ                                            (12)
```

for a fixed δ>0 along infinitely many convergents also satisfying (4). Choosing Y with logarithm between `(6+δ/3)q log2` and `(6+2δ/3)q log2` then gives `|E|≤exp(-κq)` for some κ>0, after absorbing its polynomial factor. Apply KK Proposition 7.4 with smallest-unit parameter 1 and sufficiently small fixed ε. It follows that, **if (C), (4), (12), and Z rational all hold, then E=0 for every sufficiently large member of that sequence**.

Equivalently, rationality would force these explicit rational model values Z~ to stabilize exactly at Z. Proving that they do not stabilize would supply nonvanishing for this route. That has not been proved.

### Gaps

The present argument does not establish infinitely many convergents satisfying both (4) and (12), nor does it prove nonstabilization of their rational model values. An infinite supply of suitable long returns cannot be inferred from irrationality or transcendence of log_3 2. The threshold is a sufficient condition for this specific model, not a necessary condition for every KK-style proof.

## Do skew covariance or resonant approximants already remove these obligations?

### Takeaway

Not yet. The completed calculations reveal useful additional structure, but neither a smaller effective denominator nor a nonzero remainder has been proved. The infinite side terms remain a concrete place where a different argument could outperform the periodic model.

### Cited Findings

- For each of the three specified nonresonant models, the checker found that every tested cyclic skew triple in its fundamental blocks has birth-digit sum one. This is a finite exact observation about these models. — [Checker and ranges](returns_check.py), [results](returns_check.json).
- The earlier whole-column rationality criterion concerns an individual true column. It does not preclude a combined resummation of several columns or the finite artificial model above. — [Column criterion and its reviewed limitation](../../investigations/boundary-and-arithmetic/arithmetic_review.md).

### Inferences

**Skew observation, not a proved denominator reduction.** The exact checked relation is

```
sum_(i=0)^2 η~_(a+iq, b+((j-i) mod3)p)=1,
```

for `0≤a<q`, `4≤b<4+p`, and j=0,1,2 in the three displayed models. The rational A and B shift formulas rotate their nonperiodic parts by opposite cube roots. A combined shift such as `(q,2p)` can therefore rotate the two parts together after an affine recentering. A proof that the full cone digits, correction vector, and endpoint conventions yield a uniformly smaller denominator was not completed; the numerical skew identity is not being promoted to that proof.

**The resonant case was not silently treated as periodic.** If p+q=0 modulo three, the cancellation used in (4) fails. The increment words still have periods P=3q and Q=3p, so there are exact affine recurrences

```
A~_(a+P)=A~_a+d_A,  d_A=A~_P-1,
B~_(b+Q)=B~_b+d_B,  d_B=B~_Q-1.
```

Thus, on each residue class `a=r+iP,b=s+jQ` with b≥4, the model cone test has state `z_(r,s)+i d_A+j d_B`. Its two inequalities are integer linear inequalities in i,j. This is a specific lattice-cone summation problem, rather than a periodic array. No denominator formula or improved approximation threshold for these resonant cones was derived in this round. In particular, the four-unit conclusion (7)–(12) is asserted only under (4).

**Why the side/interior distinction matters.** The model's full-period agreement begins only after accounting for the period itself: if its axis word matches through index N, a guaranteed return `A_(a+P)=A_a` follows only for a<N-P. The analogous vertical statement subtracts Q. Treating N itself as the available return length would overstate the saving. In the exact double identity, the mixed interior benefits from the intersection of the two good-return ranges, but each side term pays one large multiplier and only one return length. An exact side-strip resummation could therefore change the threshold materially; the failure to establish it is not an impossibility theorem.

### Gaps

No proof of (C), no unconditional infinite long-return sequence satisfying (12), no nonstabilization/nonvanishing proof, and no completed resonant or skew denominator reduction were obtained. The target irrationality remains open in this work. All checks are terminal. No raw event-count sweep, new decimal expansion, external post, dependency installation, or Lean formalization was performed, and prior folders were not edited.
