# Actual strictness of dispersed three-color couplings

**A genuine actual-target nonvanishing theorem is proved for a new class of coupling comparisons.** Any valid coupling with quadratically many completed triples having a fixed positive logarithmic dispersion is strictly below the actual rank optimum. This covers fixed-offset lattice/cone families and bounded-displacement bulk couplings, even with arbitrary remaining edge repairs. It applies to every canonical finite-head repair constructed in the companion note. These comparisons therefore have nonzero one-sided errors; no sufficiently cheap clearing denominator is established here, and the theorem says nothing by itself about the signed hierarchy residual R_m. — [Positive-token and rank inputs](../hybrid-arithmetic-closure/global_carries.md), [coupling input](../hybrid-arithmetic-closure/hierarchy_absorption.md), [exact supporting certificate](coupling_strictness_check.py).

## Does actual color balance force strictness for dispersed couplings?

### Takeaway

Yes. The actual corrected color imbalance is o(log t). A positive-density family of triples with a fixed positive logarithmic dispersion has integrated partial-token mass of order (log t)^2, which cannot be absorbed by that imbalance. This proves a positive total cost gap and deficits arbitrarily far out. — [Inputs](../hybrid-arithmetic-closure/global_carries.md), [finite identity certificate](coupling_strictness_check.py).

### Cited Findings

- The accepted finite theorem is tau(t)=min_j(K_j(t)-I_j(t)-P_j(t)); its positive token interpretation keeps original colors and delays dyadic 2^a to3*2^(a-1), a>=1, and row-one3*2^a to27*2^(a-3), a>=2. All arrivals are at least one. There is at most one active correction, and the sole nonsmooth arrival27/2 has zero minimum jump. — [Full retiming proof](../hybrid-arithmetic-closure/global_carries.md).
- If t_j(k) is the kth color-j arrival, then M=sum eta(d)/d=sum_k1/max_j t_j(k). A valid coupling is a bijective partition of all tokens into triples containing one token of each color. Its cost Q(C)=sum_gamma1/max_j t_gamma,j is at most M. — [Rank identity](../hybrid-arithmetic-closure/global_carries.md), [layer-cake coupling proof](../hybrid-arithmetic-closure/hierarchy_absorption.md).
- The current exact checker independently verifies the finite logarithmic-dispersion identity as an identity between the coefficients of log2 and log3. It also verifies the partial-token/imbalance relation and ordinary-row partial counts at six actual cutoffs, and certifies an explicit canonical cost gap at least5/1296. No floating-point logarithm or asymptotic conclusion is obtained from finite checking. — [Certificate](coupling_strictness_check.py).

### Inferences

Put lambda=log2, mu=log3. Their ratio is irrational: a rational relation would give2^q=3^p, contrary to unique factorization. Logarithmic cutoff is denoted T, so the physical cutoff is e^T. Let Q_j(T) count arrived color-j retimed tokens, N(T)=sum_jQ_j(T), and tau(e^T)=min_jQ_j(T). All statements below concern the actual slope and actual token universe.

**1. Uniform rotation averaging, proved directly.** If beta is irrational and I is an interval modulo one, then

```
sup_x | (1/n) sum_(k<n) 1_I(x+k beta) - |I| | ->0.       (CS1)
```

To see this, fix a coprime continued-fraction approximation p/q with |beta-p/q|<1/q^2. In any q consecutive iterates the displacement from the rational q-grid is at most1/q. Only grid points within1/q of the two interval endpoints can change membership. The grid itself has interval-count error at most two, so a fixed bound ten covers the complete q-block error, uniformly in its starting phase. Splitting n iterates into q-blocks and a remainder gives normalized error at most10/q+2q/n. Take n to infinity first and then choose q arbitrarily large. Finite linear combinations of interval indicators inherit uniform averaging. This proof handles moving starting phases and endpoint conventions; no unproved effective discrepancy rate is assumed.

**2. Actual color discrepancy is o(T).** Let omega^3=1, omega!=1, and form the raw complex discrepancy

```
W(T)=sum_(a,b>=0, lambda*a+mu*b<=T) omega^(a-b).
```

With B=floor(T/mu), X=T/lambda and beta=mu/lambda, summing each row gives

```
(1-omega)W(T)
 =sum_(b=0)^B omega^(-b)
  -sum_(b=0)^B omega^(floor(X-beta*b)+1-b).               (CS2)
```

The first sum is bounded. Write b=3k+r in the second. Its rth part is omega^(1-r) times the rotation sum of

```
g(u)=omega^(floor(3u)),        0<=u<1,
u=(X-beta*r)/3-k beta modulo one.
```

The mean of g is zero. Equation(CS1) therefore makes every residue part o(B), uniformly in X; hence W(T)=o(T). Root-of-unity filtering gives K_j(e^T)-|D_(e^T)|/3=o(T). Retiming changes each raw count by a bounded indicator, and its total by O(1), so

```
Q_j(T)-N(T)/3=o(T),
E(T):=N(T)-3tau(e^T)=o(T),       E(T)>=0.                (CS3)
```

The uniformity in(CS1) is essential because X moves with T. Simple row counting also gives N(T)=T^2/(2lambda*mu)+O(T). The bounded retiming correction does not change that leading term. These assertions are derived from the actual root coloring, not from the three rational marginal masses.

**3. Partial-token conservation.** For a valid coupling C, let G_C(T) be its number of completed triples at e^T. If a triple has k arrived tokens, it contributes k to N and contributes one to G_C exactly when k=3. Thus

```
U_C(T):=N(T)-3G_C(T)
 =sum_gamma [number of arrived tokens in gamma
              if that number is1 or2, otherwise0] >=0.

D_C(T):=tau(e^T)-G_C(T)=(U_C(T)-E(T))/3 >=0.             (CS4)
```

The last nonnegativity is the elementary count bound G_C<=min_jQ_j. Other triples or arbitrary edge repairs cannot cancel a subfamily's positive contribution to U_C. At every finite cutoff only finitely many tokens have arrived, so these counts and sums are well-defined.

**4. Exact integrated dispersion identity.** For a triple gamma put h_gamma,j=log t_gamma,j, h_gamma,max=max_j h_gamma,j and

```
g_gamma=sum_j(h_gamma,max-h_gamma,j) >=0.
```

All h are nonnegative. Integrating a single triple's contribution to U_C gives

```
integral_0^T U_gamma(s) ds
 =sum_j(T-h_gamma,j)_+ -3(T-h_gamma,max)_+
 =sum_j(min(T,h_gamma,max)-h_gamma,j)_+.                 (CS5)
```

It equals g_gamma whenever the triple is complete by e^T. Nonnegative summation/Tonelli therefore yields

```
integral_0^T U_C(s) ds
 >=sum_(gamma: h_gamma,max<=T) g_gamma.                 (CS6)
```

Simultaneous arrivals cause no problem: they are equal logarithmic endpoints and change no integral. The finite check uses exact prime-exponent pairs for both sides of(CS5), including the retimed27/2 token.

**Dispersion strictness theorem.** Suppose a subfamily F of a valid actual coupling satisfies, for some constants epsilon,kappa>0 and all sufficiently large T,

```
g_gamma>=epsilon          for gamma in F,
#{gamma in F: h_gamma,max<=T} >=kappa*T^2.               (CS7)
```

Then Q(C)<M. Moreover D_C(T) is positive on intervals arbitrarily far out.

Indeed, (CS3)-(CS7) give

```
integral_0^T D_C(s) ds
 >=(epsilon*kappa/3+o(1))*T^2.                          (CS8)
```

Here integral_0^T E(s)ds=o(T^2), obtained by splitting off a fixed initial interval and using E(s)<=delta*s afterwards. Thus D_C cannot vanish almost everywhere beyond any fixed cutoff. Since arrival events are locally finite, a positive integral entails an interval with positive integer D_C. Finally,

```
M-Q(C)=integral_0^infinity D_C(T)e^(-T)dT >0.            (CS9)
```

This follows separately for the two nonnegative sums from1/t=integral_(log t)^infinity e^(-T)dT; both costs are finite because the marginal reciprocal masses are finite.

For a sequence of couplings C_n, the constants in(CS7) may depend on n. If every member satisfies the hypotheses, every cost error is nonzero; a uniform lower bound in n is unnecessary for that nonvanishing conclusion. Since Z=3-3M, a rational cost Q(C_n) gives the strict rational comparison

```
Zhat_n=3-3Q(C_n) > Z.                                  (CS10)
```

This is an actual nonvanishing theorem for these **new genuine coupling comparisons**. It is not a nonvanishing theorem for the previously constructed signed residual R_m or for synthetic eta-model values.

### Gaps

- Strictness gives no clearing denominator, height bound or sufficiently small upper error. Those must be proved for the same constructed family. — [Current arithmetic gap](../hybrid-arithmetic-closure/REPORT.md).
- No effective T-threshold uniform in a coupling parameter is claimed. Equation(CS1) is qualitative, and epsilon,kappa may shrink with that parameter.
- A coupling without a sufficiently large dispersed subfamily need not satisfy(CS7); optimal comonotone couplings are not ruled out.

## Which periodic, polyhedral or bounded-displacement templates satisfy the criterion?

### Takeaway

A single fixed-offset family on a full-index lattice in an interior cone suffices. Consequently a finite piecewise-periodic bulk template is strictly suboptimal whenever it contains such a family. A broader bounded-displacement bulk coupling is also strictly suboptimal, without periodicity. — [Criterion(CS7)-(CS9) above](coupling_strictness.md), [actual token input](../hybrid-arithmetic-closure/global_carries.md).

### Cited Findings

- Ordinary tokens with original b>=2 are not retimed; their arrival is2^a3^b. Original labels remain distinct even where retimed boundary tokens share the same physical arrival. — [Retiming definitions](../hybrid-arithmetic-closure/global_carries.md).
- The companion canonical construction partitions the original labels into row triples (3n,b),(3n+1,b),(3n+2,b), hence provides an explicit fixed-offset ordinary bulk family. — [Canonical exact checker](rational_templates_check.py).
- The strictness theorem uses actual arrivals and valid bijective triples. A failed invariant canonical rank template does not exclude other optimal couplings, and no formal state translation is substituted for a physical translation. — [Earlier scope](../hybrid-arithmetic-closure/hierarchy_absorption.md).

### Inferences

**Fixed-offset lattice family.** Let Lambda be a full-index sublattice of Z^2 with covolume d, u+Lambda a coset, and delta_0,delta_1,delta_2 fixed integer offsets with all three colors modulo3. Suppose a valid coupling contains

```
gamma_z={original tokens z+delta_0,z+delta_1,z+delta_2}
```

for every coset point z sufficiently far into the positive quadrant. Choose that lower bound so each member is ordinary and all labels are nonnegative. The assumption that these triples belong to a coupling includes disjointness; overlapping translates cannot be silently counted as a matching.

Put h_j=lambda*delta_j,a+mu*delta_j,b and h_*=max_jh_j. The constant dispersion is

```
g=3h_*-sum_j h_j >0.                                   (CS11)
```

The strict inequality follows because distinct ordinary lattice labels have distinct physical times, by the irrationality of lambda/mu. The count of anchors with lambda*z_a+mu*z_b<=T-h_* is

```
T^2/(2d lambda mu)+O(T).                                (CS12)
```

One elementary proof tiles the plane by fixed fundamental parallelograms of Lambda: the discrepancy between lattice count and triangle area/d lies in a bounded-width boundary tube of area O(T). Fixed quadrant offsets and the constant h_* change only the O(T) term. Equations(CS11)-(CS12) prove(CS7), and even give integral_0^T D_C(s)ds>=(g/(6d lambda mu)+o(1))T^2.

The same conclusion holds when the family is required only for anchors inside any fixed open cone having a direction strictly inside the positive quadrant. A compact rectangle of positive area can be chosen inside the cone and below lambda*x+mu*y<1. Its dilates supply kappa*T^2 coset anchors whose three arrivals are complete by e^T. Thus only one positive-area periodic piece is needed; all remaining coupling triples may be arbitrary.

**Sharper periodic strip statement.** For fixed h>0, the same coset in a deep quadrant satisfies

```
#{z: T-h<lambda*z_a+mu*z_b<=T}
 = h*T/(d lambda mu)+o(T).                              (CS13)
```

Here is the needed narrow-strip argument, not an O(T) area error that would be too large. Since Lambda contains dZ^2, its coset splits into d rectangular-grid cosets of dZ^2. On one such grid, the row count away from the bounded last-row segment is

```
floor(x)-floor(x-h/(d lambda)),
x=(T-constant)/(d lambda)-n*mu/lambda.
```

The periodic function has mean h/(d lambda). Equation(CS1) applies uniformly in its starting phase over T/(d mu)+O(1) rows, and the bounded clipped segment contributes O(1). The one-grid answer is h*T/(d^2lambda mu)+o(T). Summing its d grid cosets proves(CS13). The same argument on a row interval of length proportional to T supplies a positive lower linear strip count within an interior cone.

For the full fixed-offset family, its exact partial-token mass is the sum of the three strips with widths h_*-h_j. Thus

```
U_family(T)=g*T/(d lambda mu)+o(T),
D_C(T)>=(g/(3d lambda mu)+o(1))*T.                       (CS14)
```

The other triples cannot reduce U_C, and actual E(T)=o(T). A cone-restricted family analogously gives D_C(T)>=cT+o(T) for some c>0, by taking a compact interval of directions inside the cone. Finite deletions of family triples do not alter these conclusions.

**Bounded-displacement bulk corollary.** Suppose every sufficiently deep original token belongs to an ordinary triple of coordinate diameter at most L, for a fixed finite L>=1. Then the coupling is strictly suboptimal, even if its assignment is not periodic. A deep token arriving by e^(T-L(lambda+mu)) has its entire triple complete by e^T. There are T^2/(2lambda mu)+O(T) such deep tokens, so they give at least T^2/(6lambda mu)+O(T) different completed triples. The finite collection of possible offsets gives a fixed positive dispersion lower bound. Explicitly any nontrivial ratio2^r3^s with |r|,|s|<=L differs from one by at least a unit fraction with denominator at most6^L, after inversion if needed. Hence a positive logarithmic span is at least log(1+6^(-L)), and g is at least that span. This verifies(CS7).

The conclusion also holds for any positive-quadratic-count subfamily of such bounded-offset triples; no condition is needed on arbitrary long-range repairs outside that subfamily.

### Gaps

- One-dimensional diagonal invariance alone does not establish a full-index lattice/cone family. The infinite root strips may have unbounded or nonperiodic offsets. A proposed model must verify its actual coupling class.
- No irrationality of M follows from the strictness of periodic rational comparisons alone: a rational number can be a strict limit of rational numbers.
- The theorem does not say a cheap rational bulk template exists with a long enough optimal prefix. It supplies nonvanishing only after a valid coupling and its class hypotheses have been established.

## What does strictness say quantitatively about canonical finite-head repairs?

### Takeaway

The canonical row coupling has completed-count deficit asymptotic to log t/(3log3). Finite equal-rank repairs have strictly positive cost error of exact order log X/X when the repaired head is cut at X. This establishes an infinite actual one-sided nonvanishing approximation family, and pinpoints the real tail left by this elementary repair. It does not provide a lower bound for the family's reduced denominators. — [Canonical construction/checker](rational_templates_check.py), [exact finite supporting identities](coupling_strictness_check.py).

### Cited Findings

- The canonical triples are the original labels (3n+r,b), r=0,1,2; actual retiming preserves their colors. Their exact reciprocal-max costs are1/(6*8^n) at b=0,2/(27*8^n) at b=1, and1/(4*8^n*3^b) at b>=2. Summing gives Q(C_0)=61/189. — [Companion exact checker](rational_templates_check.py).
- A repair takes the first K=min_jQ_j(log X) arrivals of each color, uncouples every canonical triple touching that balanced head, and equal-rank rematches their finite balanced union. Every touched token arrives by6X. The remainder of the canonical coupling stays fixed. — [Companion construction/checker](rational_templates_check.py).
- The independent strictness checker verifies canonical deficit two on the complete actual interval [81,96), giving M-Q(C_0)>=2(1/81-1/96)=5/1296. This finite exact bound is not used to prove an asymptotic rate. — [Strictness certificate](coupling_strictness_check.py).

### Inferences

**1. Actual canonical deficit asymptotic.** For any ordinary row b>=2, write the number of arrived original tokens as A_b+1. Its canonical completed triples number floor((A_b+1)/3), so its partial-token count is (A_b+1) modulo3. Equivalently it is

```
f({(T-b mu)/(3lambda)}),
f=1 on[0,1/3), 2 on[1/3,2/3), 0 on[2/3,1).             (CS15)
```

The mean is one. Uniform rotation averaging over b=2,...,floor(T/mu) gives

```
U_(C_0)(T)=T/mu+o(T).                                  (CS16)
```

The two exceptional original rows contribute O(1): their retimed triples occur in disjoint geometric groups, with at most one partial triple per row. Combining(CS16) with E(T)=o(T) proves

```
D_(C_0)(T)=tau(e^T)-G_(C_0)(T)=T/(3mu)+o(T).            (CS17)
```

This agrees with(CS14), where Lambda=3Z x Z, covolume three, and offsets(0,0),(1,0),(2,0) have dispersion3lambda.

**2. A finite balanced rematching leaves the tail counting process unchanged.** Let C_F replace finitely many whole canonical triples by another matching of exactly their balanced union. Once every touched token has arrived, the old and new finite parts have the same number of complete triples. Therefore G_(C_F)(T)=G_(C_0)(T) beyond the largest touched arrival. If the replacement is equal-rank, it also satisfies G_(C_F)(T)>=G_(C_0)(T) at every cutoff, by the same marginal-intersection count proof as the global coupling lemma.

For the companion head repair C_X, the first K tokens of each color are initial rank intervals of its finite union. Their matching therefore realizes every true rank layer completed by cutoff X. No untouched canonical triple can be complete by X, since at least one color has only K arrived tokens. Consequently

```
D_(C_X)(T)=0                 for e^T<=X,
0<=D_(C_X)(T)<=D_(C_0)(T)    at every cutoff,
D_(C_X)(T)=D_(C_0)(T)        for e^T>=6X.                (CS18)
```

The factor six includes every endpoint: labels in one row triple differ by at most two in a, giving original-time ratio at most four; every actual delay is at most3/2 and no delay is backwards. Thus one touched token arriving by X bounds all arrivals in its canonical triple by6X.

**3. Sharp real error order.** Put delta_X=M-Q(C_X). Equations(CS9),(CS17)-(CS18) imply

```
(1-o(1))*(log(6X)+1)/(18 mu X)
 <= delta_X
 <=(1+o(1))*(log X+1)/(3 mu X).                         (CS19)
```

For the upper bound integrate D_(C_0) only beyond log X. For the lower bound integrate the identical canonical tail beyond log(6X). The elementary integral is integral_L^infinity T e^(-T)dT=(L+1)e^(-L), and the o(T) term in(CS17) contributes o((L+1)e^(-L)) uniformly on that tail. Hence delta_X=Theta(log X/X)>0. The transformed rational upper comparisons Zhat_X=3-3Q(C_X) have error3delta_X and are nonzero for every X.

The companion construction bounds a clearing denominator by7*2^(A+2)*3^max(B,3), with A=floor(log_2 X), B=floor(log_3 X), hence O(X^2). Equation(CS19) shows that this simple head repair has no hidden extra real saving beyond its log X/X tail. An upper bound O(X^2) on denominators and a lower bound on delta_X do **not** constitute a lower bound on the reduced denominator, or a proof that every cleverly selected subsequence is arithmetically inadequate. No such overclaim is made.

### Gaps

- The constructed infinite family has a proven one-sided nonzero real error, but no adequate integer-cleared error estimate. The full infinite-return goal remains unproved. — [Arithmetic acceptance interface](../hybrid-arithmetic-closure/REPORT.md).
- The new strictness theorem is ready to apply to richer valid periodic/polyhedral comparisons. A full construction must still supply a sufficiently long optimal prefix and pay all infinite-strip and preperiod denominators.
- Nothing here establishes nonvanishing of the old signed R_m. A proved equality between that residual and a positive coupling gap would be an additional theorem.
- Skipped: Lean, external review, broad scans, density decimals, installations and archived edits. Main risk: treating nonvanishing of this new coupling family as denominator control, or transferring it to a signed residual without a genuine coupling identity.
