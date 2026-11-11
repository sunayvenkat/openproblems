# Two floor sides, centered color readouts, and polynomial pole cancellation

Status, 7 November 2026: **no adequate infinite weighted return is constructed.** There are new exact relations between the two prescribed models, including a general binomial factor in their full difference, and a stronger, specifically tested obstruction to formal pole cancellation. For the two named models, that obstruction covers Laurent-polynomial coefficients in the block scales, not merely constant averages. It does not exclude special scalar arithmetic cancellation on an infinite exceptional subsequence. The finite formula (C) is taken as proved; no Lean, installation, broad sweep, archived edit, decimal density calculation, or external post was used.

## How are the two one-sided models actually related?

### Takeaway

The two axis states differ by explicit three-periodic block shifts. They are not globally related by reflecting one state about the opposite barycenter. The indicator correction has three additional defect rows per vertical block; dropping these rows would change the proposed model.

### Cited Findings

- The model uses positive-index one-sided floors, opposite reciprocal convention, initial states A0=B0=1, and the four separate low-column rules. The admissible interval is 3/5<p/q<2/3. — [Audited definitions](../global-boundary-proof/independent_audit.md), [scalar construction](../../early-attacks/augmentation-and-return-attacks/returns.md).
- The two centers are K_L=(1−omega)/3 and K_R=(2+omega)/3. Their assignment to sigma depends on p+q modulo three. — [Exact center calculation](../infinite-return-construction/skew_denominator.md).
- A new narrowly targeted certificate checks both floor sides, their axis differences and all indicated correction differences for p/q=5/8. It independently reconstructs the saved correct-side rational values for both 5/8 and 53/84 and verifies the full numerator's binomial divisibility. — [Exact certificate](two_sided_models_check.py).

### Inferences

Write rho=omega^(2p−q), which is a nontrivial cube root. Superscripts + and − below mean the two choices of the **horizontal** tie convention, whether or not that convention is the correct side of the actual logarithm. Put

```
L_i = sum_(k=1)^i rho^k,
M_j = sum_(k=1)^j rho^(−k).
```

Then, at every nonnegative index,

```
A^+_a − A^-_a = L_floor(a/q),
B^+_b − B^-_b = −M_floor(b/p).                         (T1)
```

Indeed the horizontal increment differs only at a=kq. There S(kp)−S(kp−1)=omega^(2kp), giving the increment rho^k after rotating by omega^(−kq). The reciprocal increment changes with the opposite sign and gives −rho^(−k). Index zero contributes no endpoint term. Thus the horizontal block shifts are (0,rho,−1) and the vertical shifts are (0,−rho^(−1),1), cyclically repeated. This directly derives the relation rather than inferring it from K_L+K_R=1.

For p>3, let E^sigma_b be the high-column isolated/patch correction. At b=jp+r, with 0<=r<p and b>=4, the only possible nonzero correction differences are

```
E^+_b − E^-_b = rho^(−j) *
    { −1,             r=0;
      omega^2−1,      r=1;
      omega^2,        r=3;
      0,              otherwise. }                    (T2)
```

The formula applies only where the displayed positive-index events exist; for example r=3,j=0 is outside b>=4. To verify it, use 3/2<q/p<5/3. At b=jp, the ordinary reciprocal floor makes an isolated event that the lowered endpoint removes. At b=jp+1, lowering the preceding floor replaces the ordinary patch by an isolated event. At b=jp+3, lowering the floor three steps earlier creates a patch. Their colors give (T2). The events do not overlap.

Consequently the corrected high states satisfy

```
z^+_(a,b) − z^-_(a,b)
  = L_floor(a/q) − M_floor(b/p) − (E^+_b−E^-_b).        (T3)
```

The correction term is essential. Even in the first block above a rational crossing, replacing (T3) by a constant translation or by 1−z gives wrong cone digits.

The exact first digit disagreements, ordered by the actual weight 2^a3^b, are

| p/q | (a,b) | eta^+ | eta^- |
|---|---|---:|---:|
| 5/8 | (0,6) | 1 | 0 |
| 53/84 | (85,1) | 1 | 0 |

The certificate checks these by a small complete candidate set around the first two axis crossings. The models agree for a<q,b<p, and the displayed candidate weights are below both 16*2^q and 16*3^p. Every omitted potentially changed point is heavier. The 53/84 disagreement lies in a low column, so a high-cone-only correction would miss it. These are actual paired-model facts, not consequences of the old single-model denominator obstruction.

**A positive general identity: the full paired numerator has a binomial factor.** Define the full formal series, retaining every low rule,

```
F^sigma(x,y)=sum_(a,b>=0)c^sigma_(a,b)*x^a*y^b,
P(x,y)=(1−x^(3q))*(1−y^(3p))*(F^+(x,y)−F^−(x,y)).
```

Then

```
P(x,y) is in (x^q−y^p)*Z[x,y].                        (B1)
```

Here is a proof accounting for the indicator events rather than dropping them. For an irrational r near p/q, put lambda=3^r and order vertices by lambda^a*3^b. Let K_r be the three color counts in this synthetic order. Define the same monomial indicators: isolated root lambda^A when lambda*t/3<lambda^A<=t, and patch root lambda^A when3*lambda*lambda^A<=t<27*lambda^A/lambda^2, always A>=1. Let

```
M_r(t)=min_j(K_(r,j)(t)−I_(r,j)(t)−P_(r,j)(t)).
```

This minimum is an **artificial model definition**; no extension of (C)'s global optimality to synthetic slopes is assumed or needed. Directly taking this minimum's increment gives exactly the audited rational-model rules in the one-sided limit r→p/q:

- At b>=4 no indicator changes at the vertex, giving the corrected cone test.
- At b=0,a>=1, the inserted vertex and new isolated indicator cancel; the increment is zero. At(0,0) the minimum likewise stays zero.
- At b=1,a>=2, the inserted color0 and entered patch cancel; removing the isolated indicator adds color2. After insertion the adjusted state is K−e0. Thus the increment is1 exactly when x>=1,y>=0. The two finite exceptions are a=0, where the increment is1, and a=1, where it is0, as in the retained rules.
- At b=2 the surviving indicator has relative color2. The ordinary cone becomes x<=−1,x−y<=0.
- At b=3 the removed patch and the vertex add colors2 and0. Therefore the increment is min(x,y,0)−min(x−1,y,−1), equal to1_[min(x,0)<=y].

The only indicator endpoint not attached to a nonnegative-exponent vertex is the patch endpoint27/lambda for root lambda. It lies strictly between lambda^2*3 and lambda^4 when3/5<r<2/3. The color counts there are(3,3,2): removing the patch changes(3,2,2) to(3,3,2), so the minimum has zero increment. Moreover, at rational slope p/q with p>3 that endpoint cannot coincide with any positive vertex: pa+qb=3q−p would force a+1=kq,b=3−kp, impossible for a,b>=0.

Fix a rational grade k=pa+qb. Its positive vertices form a finite tie chain. The two r-limits traverse this chain in opposite orders, including their attached indicator events, but have identical adjusted count vectors before and after the complete grade. Telescoping M_r therefore proves

```
sum_(pa+qb=k)(c^+_(a,b)−c^−_(a,b))=0                 (B2)
```

for every k. Hence(F^+−F^−)(t^p,t^q)=0. Multiplying by the common polynomial denominator gives P(t^p,t^q)=0. The kernel of Z[x,y]→Z[t], x→t^p,y→t^q, is precisely(x^q−y^p): divide by the monic polynomial x^q−y^p; remaining monomials with0<=a<q have distinct grades because gcd(p,q)=1. This proves(B1).

Writing u=2^q,v=3^p and D=27(u^3−1)(v^3−1), (B1) also yields

```
u−v divides the integer D*(Z^+−Z^−).                 (B3)
```

Indeed the quotient after dividing by u−v is a rational number whose denominator has only primes2,3; the full numerator is integral and gcd(u−v,6)=1. The new certificate independently verifies(B1) by grouping the **finite full numerator polynomial** by grade for both5/8 and53/84; this is stronger than checking(B3) numerically. Their absolute u−v values are13 and40432553845953101497907, respectively. — [Formal and scalar checks](two_sided_models_check.py).

This factor does not remove an axis pole. Its relative size |u−v|/u is of order |q*log2−p*log3|, hence only of order1/q' on convergent returns with bounded q'/q. Dividing by u−v instead creates a new non-S-unit denominator unless further structure is proved. Thus(B1) is genuine paired structure, but not yet the required exponential improvement.

### Gaps

No theorem here says that the first changed digit causes a lower bound of comparable size for the entire scalar difference: subsequent weighted differences could cancel. Likewise, (T1)–(T3) do not establish an infinite supply of adequate returns.

## Can centered color readouts and polynomial coefficients cancel the poles?

### Takeaway

The six centered readouts have only four independent high-column components. For each of 5/8 and53/84, explicit full-rank residue matrices prove that a formal Laurent-polynomial combination can cancel a complete vertical factor only if **each effective coefficient already contains that factor**. This includes degree one, degree two, and arbitrary finite degrees. Finite exact corrections and the low columns do not change this vertical conclusion.

### Cited Findings

- Each centered high-column cone partition sums to one, equivalently its three c=1−3eta readouts sum to zero; the low columns do not share that identity. — [Partitions and low-column counterexamples](../infinite-return-construction/skew_denominator.md).
- The new certificate checks full rank over the exact field Q(omega), including explicit four-row witnesses, at X=1,omega with Y=2 and at Y=1,omega with X=2 for both named slopes. It also checks all four constant-coefficient axis-cancellation matrices for5/8. — [Certificate and emitted matrices](two_sided_models_check.py).
- The target clearing budget from the proved convergent supply is gamma<(25+sqrt(5))/10, whereas the current complete scalar denominator has exponent six. — [Supply interface](../infinite-return-construction/diophantine_supply.md), [final audit](../infinite-return-construction/final_return_audit.md).

### Inferences

For a lattice point z=x+y*omega, the centered partitions are

```
K_L: F(z), 1_[x>=1,y>=0], 1_[y<=−1,x>=y+1];
K_R: F(z), 1_[x>=1,y>=1], 1_[y<=0,x>=y+1].            (T4)
```

Only the assignment of the ray H={y=0,x>=1} differs. Thus, on a common state z, a universal identity

```
sum_(r=0)^2 a_r*c_(L,r)(z)
+sum_(r=0)^2 b_r*c_(R,r)(z) = kappa*c_0(z)             (T5)
```

holds if and only if

```
a_1=a_2,  b_1=b_2,
kappa=a_0+b_0−a_1−b_1.                               (T6)
```

To prove this, compare the three common open cone regions and then H. The comparison on H forces b1=b2, the common cone comparison then forces a1=a2; the remaining coefficient is as displayed. Partition identities reduce (T5) exactly to A*c_(L,0)+B*c_(R,0), A+B=kappa. Therefore centered readouts do not create extra rational constants from the sole hypothesis Z in Q. An approach using any further color constant must prove a new identity for the actual weighted path; rationality of Z does not supply it.

Here is the stronger formal cancellation test. Use formal weights x,y, and block weights X=x^q,Y=y^p. For each a in[0,q), b in[4,4+p), define a block numerator

```
T_(sigma,r;a,b)(X,Y)
  = sum_(i,j=0)^2 c_(sigma,r)(a+iq,b+jp)*X^i*Y^j.      (T7)
```

Its denominator is (1−X^3)(1−Y^3). The four independent columns are (sigma,r)=(+,0),(+,1),(−,0),(−,1), since color2 is minus colors0 and1. Multiplying the rational generating functions by Laurent polynomials A_(sigma,r)(X,Y) corresponds to a fixed finite set of block-scale S-unit coefficients.

At a vertical root Y=zeta in{1,omega}, cancellation of the corresponding entire factor requires

```
sum_(sigma,r) A_(sigma,r)(X,zeta)
                     T_(sigma,r;a,b)(X,zeta)=0        (T8)
```

for every a,b. Lower residue monomials x^a*y^b form the independent basis after imposing x^q=X and y^p=zeta; there is no averaging over a,b in (T8). The tested four-by-four minors are nonzero already at X=2, so the column matrix has full rank over Q(omega)(X). It follows that every A_(sigma,r)(X,zeta) is zero. For rational Laurent coefficients, conjugation adds the omega^2 root. Therefore cancellation of1−Y forces each coefficient divisible by1−Y; cancellation of1+Y+Y^2 forces each coefficient divisible by1+Y+Y^2. This argument is independent of the degree bound on A.

For reproducibility, the 53/84 witnesses at Y=1,X=2, with columns in the displayed order, are

```
(a,b)=(0,4):   ( 0, 0, 12,−15)
      (0,8):   ( 0, 0,  9, −6)
      (1,4):   (−6,−3,  3, −9)
      (2,4):   (−9, 6,  0,  0).
```

At Y=omega,X=2, the four row labels are(0,4),(0,8),(0,11),(1,4); their exact Eisenstein entries are printed by the certificate. Gaussian elimination uses rational arithmetic in Q(omega), with independently asserted multiplication and division checks.

Every low-column addition has no vertical pole. A finite exact head/defect correction is a polynomial in x,y and likewise has no vertical pole. Consequently they contribute zero after multiplying by1−Y^3 and evaluating at a vertical root. They cannot defeat (T8). By contrast, low-column additions **can** change horizontal residues; the high-only horizontal matrix result is not asserted as an unrestricted horizontal statement for the full model.

The conclusion is not that writing a canceling coefficient is impossible: taking A divisible by the factor trivially cancels it. It is that this transfers the factor into the arithmetic coefficients. For example

```
1+Y+Y^2 = (v^2+v+1)/v^2,  v=3^p,
```

so canceling this factor in weight variables pays either the integer coefficient v^2+v+1 or the denominator/minimum-unit scale v^2. The usual complete clearing budget does not save its2p*log3 cost. The remaining vertical1−Y costs p*log3, retaining nominal total3p*log3. Along convergents this is3q*log2+o(1), already above the supplied budget even before paying horizontal factors. This is a factor-accounting obstruction to the proposed formal architecture; it is not a lower bound for every scalar approximation with specially engineered coefficients.

### Gaps

- This is proved for two specified models, including53/84, not uniformly for all admissible slopes or an infinite subsequence.
- It concerns formal cancellation of entire axis factors. A reduced scalar denominator at x=1/2,y=1/3 can have arithmetic gcd cancellation invisible to this test.
- Arbitrary affine translations of cone readouts need not lie in these four columns. No universal no-go theorem for such additional readouts is claimed. Their normalization to the sole Z and their exact early defects would need separate proofs.

## Does a paired scalar combination preserve the long true prefix and an adequate arithmetic scale?

### Takeaway

The naive mean and difference do not provide a denominator reduction of the required scale, and the opposite side has early defects well before the long Farey window. Correcting a finite prefix does not remove the pole obstruction above. An adequate infinite supply, a sufficiently cheap scalar cancellation, and nonvanishing remain unproved.

### Cited Findings

- The correct side matches a<q+q',b<p+p'. Its full denominator is D=27(2^(3q)−1)(3^(3p)−1), and its cleared error is at most486(1+o(1))*2^(5q−q'). — [Rectangular bound and integer discreteness](../infinite-return-construction/skew_denominator.md).
- Exact full-model reductions, including all low-column rules and the origin exception, give the following nominal/reduced ratios. The main side is plus for5/8 and minus for53/84. — [New two-side certificate](two_sided_models_check.py), independently matched to [saved correct-side values](../../early-attacks/augmentation-and-return-attacks/returns_check.json).

| p/q | D/den(Z+) | D/den(Z−) | D/den((Z++Z−)/2) | D/den(Z+−Z−) |
|---|---:|---:|---:|---:|
|5/8|702|2730|39|78|
|53/84|1554|6|18|6|

- Paired order changes have exact response −3*H_ij(Q)*(1/d1−1/d2), with off-diagonal and same-color diagonal Hessians; low indicator changes require their own treatment. — [Weighted swap identities](../infinite-return-construction/weighted_returns.md).

### Inferences

Let M be the correctly sided model and M_opp the other. A normalized two-side approximation is

```
W=A*M+B*M_opp,   Q=A+B,
W−Q*Z=A*(M−Z)+B*(M_opp−Z).                            (T9)
```

Only the first error automatically enjoys the q+q',p+p' matching window. The other agrees automatically merely in a<q,b<p. Its safe geometric bound is

```
|M_opp−Z| <=9*(2^(−q)+3^(−p)−2^(−q)*3^(−p)).          (T10)
```

Thus a nonzero opposite-side coefficient cannot inherit the long window by declaration. Degree-one or degree-two block-scale coefficients can amplify (T10); their growth must be included before comparing with the clearing factor. Exact early corrections are possible in principle, but must be actually evaluated and charged.

If C is the exact difference between the correct and opposite models on the entire Farey rectangle, replacing M_opp by M_opp+C restores that rectangle. A direct rectangular correction has denominator dividing2^(R−1)*3^(S−1), R=q+q', S=p+p'. This is an upper bound on a possibly expensive correction, not a lower bound or an impossibility theorem: a clever sparse evaluation could reduce it. Nevertheless such a finite correction does not affect (T8), so it cannot create formal free cancellation of the vertical factors.

For any attempt to sum the opposite-side defects via ordering changes, both weights in the Hessian response must remain attached to their physical vertices. In particular

```
H_ij(Q)=1_[Q_i=Q_j<Q_k]                 (i!=j),
H_ii(Q)=−1_[Q_i+1=min(Q_j,Q_k)].                       (T11)
```

Same-color ties are not invisible. Formula(T2) and the first discrepancy(85,1) also show why a high-row swap calculation alone does not account for the actual paired model. A finite formal color or minimum identity is not a proof that the resulting weighted Hessian sums are rational under Z in Q.

The arithmetic test stays the corrected one: t<=min(1,all units), controlled height and coefficients, and an adequate error relative to t. For integer-cleared rational models, an error tending to zero suffices by rational discreteness. None of the new paired calculations supplies such an infinite sequence at the sharp available ratio C_*=(15+sqrt(5))/10.

### Gaps

The requested full infinite construction remains open in this branch. What survives as a useful next target is a **scalar**, rather than merely formal, cancellation using extra actual-path identities, or a genuinely new readout family whose rationality follows from the sole density. Either must include the opposite side's early low-column and indicator defects and prove its effective arithmetic cost. No general failure theorem for that broader target has been established.
