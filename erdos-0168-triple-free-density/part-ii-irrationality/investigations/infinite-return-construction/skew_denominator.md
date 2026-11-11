# Exact skew covariance and the scalar-denominator obstruction

## Does the observed three-term skew identity hold in general?

### Takeaway

Yes, for every high-column digit of every admissible nonresonant rational model. The affine center is exactly one of two triangular-lattice barycenters. Both centers give an exact partition, including all lattice ties. The identity fails in low columns 0, 1, and 3; it is not a global identity for the full density array.

### Cited Findings

- The global finite formula (C) is now established in the workspace; older references to its conditional status are superseded by the [final report](<../prefix-and-phase-audit/REPORT.md>).
- The separated Eisenstein-coordinate state and its cone test come from [arithmetic.md](<../boundary-and-arithmetic/arithmetic.md>); the one-sided rational model, correction tests, and low-column rules are in [returns.md](<../../early-attacks/augmentation-and-return-attacks/returns.md>).
- The admissible range is **3/5 < p/q < 2/3**, not the broader range in the original checker. See the [independent audit](<../global-boundary-proof/independent_audit.md>).
- A new narrow [certificate](<skew_denominator_check.py>) checks the two affine partitions, all three saved models' centers, and the low-column counterexamples. It passes under Python 3.14; the proof below is general and does not depend on finite verification.

### Inferences

All statements in this subsection are exact derivations. Let omega^2+omega+1=0. Assume gcd(p,q)=1 and p+q is nonzero modulo 3. Let sigma=sign(log_3(2)-p/q). Put

```
m_k = floor_sigma(kp/q),       n_l = floor_(-sigma)(lq/p),
rho = omega^(2p-q) = omega^(-p-q),
H_A = sum_(k=1)^q omega^(2m_k+2-k),
H_B = sum_(l=1)^p omega^(n_l+1-2l),
c_A = -H_A / [(1-omega^2)(1-rho)],
c_B = -H_B / [(1-omega)(1-rho^(-1))].
```

The one-sided floors apply only at positive indices. In particular, A_0=B_0=1, rather than values obtained by applying a negative-side convention to index zero.

Summing the geometric part of each increment gives, for every a,b>=0,

```
A_a = 2/3 + omega^(-a)/3
      - sum_(k=1)^a omega^(2m_k+2-k)/(1-omega^2),
B_b = 2/3 + omega^(-2b)/3
      - sum_(l=1)^b omega^(n_l+1-2l)/(1-omega).
```

Consequently

```
R_a = A_a-2/3-omega^(-a)/3-c_A,    R_(a+q)=rho R_a,
S_b = B_b-2/3-omega^(-2b)/3-c_B,   S_(b+p)=rho^(-1) S_b.
```

The residue table has the particularly useful exact expression

```
C_(a mod3,b mod3)=(1-omega^(-a))(1-omega^(-2b))/3.
```

For b>=4 let E_b be the correction vector in Eisenstein coordinates. Its isolated color is m_b-2b, and its patch color is m_(b-1)-1-2b, where here m_b denotes the reciprocal floor n_b. Both indicator conditions are invariant under b->b+p and their colors advance by q-2p. Thus

```
E_(b+p)=rho^(-1) E_b.
```

Writing z_(a,b)=A_a+B_b-1+C_(a,b)-E_b, the full corrected state is

```
z_(a,b)=K+omega^(-a-2b)/3+R_a+S_b-E_b,
K=2/3+c_A+c_B.
```

Under (a,b)->(a+q,b+2p), every nonconstant term is multiplied by rho. Therefore

```
z_(a+q,b+2p)=K+rho(z_(a,b)-K).                       (S1)
```

**Exact center calculation.** Write s=p+q. The two finite sets

```
{ k+floor(kp/q) : 1<=k<q },
{ l+floor(lq/p) : 1<=l<p }
```

partition {1,...,s-2}. To verify disjointness, suppose k+floor(kp/q)=l+floor(lq/p), and put d=l-floor(kp/q)=k-floor(lq/p). If d<=0, then l<kp/q, so floor(lq/p)<=k-1 and d>=1, a contradiction. If d>=1, then l>kp/q, so floor(lq/p)>=k and d<=0, also a contradiction. There are exactly s-2 values in the required range, proving the partition.

Reflection l->p-l in H_B now gives

```
omega H_A + rho H_B
 = sum_(t=1)^(s-2) omega^(-t)
   + {rho+1, if sigma=+1; rho*omega+omega, if sigma=-1}.
```

There are no interior ties because p,q are coprime. The displayed endpoints are precisely where the one-sided convention matters. Also

```
c_A+c_B=(omega H_A+rho H_B)/[(1-omega)(1-rho)].
```

Evaluating by s modulo 3 gives the complete center table:

| s mod 3 | sigma | K |
|---|---:|---|
| 1 | +1 | (1-omega)/3 |
| 1 | -1 | (2+omega)/3 |
| 2 | +1 | (2+omega)/3 |
| 2 | -1 | (1-omega)/3 |

**All cone ties are resolved exactly.** Put F(x+y omega)=1_[x<=0 and x-y<=0]. For K=(1-omega)/3, the three orbit points, in either order, are

```
(x,y), (-y,x-y-1), (y-x+1,-x).
```

Their tests are respectively

```
x<=min(0,y);
y>=0 and x>=1;
y<=-1 and x>=y+1.
```

These partition the integer lattice. For K=(2+omega)/3, the orbit points are

```
(x,y), (1-y,x-y), (y-x+1,1-x),
```

and the tests are

```
x<=min(0,y);
y>=1 and x>=1;
y<=0 and x>=y+1.
```

Again this is a partition. In particular the superficially dangerous closed-cone ties create neither overlap nor a missing lattice point: the fractional center produces the necessary unit offsets.

Combining (S1), vertical period 3p, and these partitions proves

```
sum_(i=0)^2 eta~(a+iq,b+((j-i) mod3)p)=1             (S2)
```

for every a>=0, b>=4, and j=0,1,2. Equivalently, the corresponding three c~=1-3 eta~ values sum to zero. This proves, rather than extrapolates, the previously observed high-column identity.

**Low-column counterexamples.** For the valid model p/q=5/8, retain exactly the audited low-column rules, including the exception at (0,1). In (S2), the triples (a,b,j)=(3,0,1), (0,1,0), and (0,3,0) have sums 0, 2, and 2 respectively. Hence the full coefficient array does not obey the high-column recurrence. Column 2 happened to satisfy the tested finite instance; no general low-column extension is asserted.

### Gaps

This establishes a high-column identity, not an exact rational evaluation of any true infinite column. The true accumulated axis states remain unbounded and have not been replaced by a bounded phase state. No new conclusion about infinite successful returns follows from (S2) alone.

## Does root-of-unity projection actually lower the exact rational denominator?

### Takeaway

The skew partition does not force cancellation of a single scalar denominator factor. The saved 53/84 model provides a sharp finite warning: its reduced rational denominator is exactly D/6, where D=27(2^(3q)-1)(3^(3p)-1). Thus the proposed symmetry does not remove the cubic horizontal or vertical factors uniformly.

### Cited Findings

- The exact saved rational values and nominal denominators are in [returns_check.json](<../../early-attacks/augmentation-and-return-attacks/returns_check.json>); their original construction is in [returns_check.py](<../../early-attacks/augmentation-and-return-attacks/returns_check.py>).
- Exact Fraction reduction of those saved values yields nominal/reduced-denominator ratios 702, 3510, and 6 for 5/8, 12/19, and 53/84. The [new certificate](<skew_denominator_check.py>) checks these identities without recomputing density decimals.

### Inferences

Fix a fundamental q-by-p high block and write its 3-by-3 block coefficient polynomial as

```
T(x,y)=sum_(i,j=0)^2 c_ij x^i y^j.
```

Equation (S2) says that the sum of c_ij on each i+j modulo 3 is zero. Equivalently,

```
T(1,1)=T(omega,omega)=T(omega^2,omega^2)=0.             (S3)
```

These are three *joint* zeros. They do not say T(1,y) or T(omega,y) is identically zero, as would be needed to cancel horizontal factors, and they do not say the corresponding vertical evaluations vanish.

An explicit array with the same coefficient alphabet and partition proves the distinction. Put eta_ij=1 precisely at (0,0),(0,1),(1,1), and zero elsewhere. Each i+j residue contains exactly one selected cell. Its coefficient polynomial is

```
T=(1+x+x^2)(1+y+y^2)-3(1+y+xy).
```

Yet

```
T(1,y)=3y(y-1),          T(x,1)=3(x^2-1),
T(omega,y)=-3(1-omega^2 y),
T(x,omega)=-3(1+omega+x omega),
```

all nonzero polynomials. Conjugation gives the same conclusion at omega^2. Thus T/[(1-x^3)(1-y^3)] retains its entire bivariate denominator despite satisfying the exact skew partition. This is an algebraic counterexample to deducing a smaller scalar denominator from (S2).

The actual 53/84 model is stronger evidence against this specific proposed cancellation, rather than merely an arbitrary skew array: its scalar denominator is D/6 and has 507 bits, versus 509 bits for D. Therefore neither an entire horizontal cubic nor an entire vertical cubic, nor their full primitive cyclotomic factors, is cancelled in that model.

Another tempting rewrite is to exploit x approximately equal to y. Modulo x^3-1 and y^3-1, (S3) makes T divisible by x-y. At the positive integer scales u=2^q, v=3^p, however, |u-v|/u is only of convergent-size order O(1/q_next), not a fixed exponential saving in q. An exact rewrite introduces side terms; it is not legitimate to divide the scalar rational denominator by u-v. No such divisibility has been proved, and the explicit reduced denominator above rules out a uniform large algebraic-factor cancellation of the proposed type.

The same issue affects the sparse operator with positive shifts

```
c(a+2q,b)+c(a+q,b+p)+c(a,b+2p)=0,  b>=4.
```

Its formal weight polynomial u^2+uv+v^2 is small enough to be interesting, but summation on the quadrant retains infinite horizontal and vertical side strips. Treating their values as integers, or as bounded-coefficient rational functions without proof, would erase the very factors that survive in the exact 53/84 denominator.

**Why a large recentering does not localize all mixed blocks late.** We proved c_A+c_B=K-2/3, a bounded value. At fixed small a,b, therefore R_a=-c_A+O(1) and S_b=c_A+O(1). If the centers grow, these early components have comparable magnitude automatically. A proof based on one component dominating the other needs actual path/cancellation estimates; large cocycle size alone supplies none.

### Gaps

One finite model cannot exclude stronger cancellations along a special infinite subsequence. Nor does the abstract counterexample prove an impossibility theorem for another architecture, for the actual coupled axis paths, or for the retained side strips. What it excludes is the claimed automatic scalar denominator reduction from the skew partition. No improved denominator exponent has been established here.

## What exact error and height bounds remain, and do they give an unconditional return sequence?

### Takeaway

The full matching rectangle improves the elementary error bound by removing its unnecessary logarithmic factor. The fixed-ratio sufficient condition remains q_next/q>5+delta; ordinary rational discreteness also admits the weaker boundary condition q_next-5q tending to infinity. No adequate infinite suitable sequence or nonstabilization argument is supplied here.

### Cited Findings

- Consecutive-convergent matching, D=27(2^(3q)-1)(3^(3p)-1), integrality of N=D Z~, and the four-unit form are proved and audited in [returns.md](<../../early-attacks/augmentation-and-return-attacks/returns.md>) and the [independent audit](<../global-boundary-proof/independent_audit.md>).
- The relevant nonzero S-unit lower bound is KK Proposition 7.4; its primary manuscript is [available here](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf), with a [saved text](<../../../../meta/theorem-transfer-survey/erdos1062-fork-free-density.pdf.txt>). The earlier audit reconstructs this application and its separate nonvanishing obligation.

### Inferences

Let p'/q' be the next convergent, R=q+q', S=p+p'. The model and true digits agree throughout **the rectangle a<R, b<S**, not only below the smaller smooth cutoff. Each coefficient difference has absolute value at most 3. Summing the complementary geometric tails exactly gives

```
|Z-Z~| <= 9[2^(-R)+3^(-S)-2^(-R)3^(-S)].             (S4)
```

Indeed the total reciprocal weight is 3, and the rectangle's weight is 3(1-2^(-R))(1-3^(-S)). This proves (S4) directly, with no use of a log-counting estimate or an auxiliary Y.

Write U=2^(3q), V=3^(3p). Then

```
|DZ-N| <= 243(U-1)(V-1)
          [2^(-R)+3^(-S)-2^(-R)3^(-S)],              (S5)
H(N:UV:U:V:1) <= 162 UV.                            (S6)
```

Here |Z~|<=6, so |N|<=162 UV, and the final coordinate 1 makes the integer projective coordinates primitive. If Z is rational, the cleared form is

```
DZ-N = 27Z UV-27Z U-27Z V+27Z-N,
```

with four fixed rational coefficients. Along convergents,

```
log(UV)=6q log2+o(1),
min(R log2,S log3)=(q+q')log2+o(1).
```

Hence (S5) gives a fixed exponential saving whenever q'/q>5+delta for some fixed delta>0. Under rationality, the cited lower bound then forces Z~=Z for every sufficiently late member of such a sequence. This is eventual equality, not a contradiction without nonstabilization.

There is a simpler and slightly stronger arithmetic implication. If Z=A/B is rational, E=DZ-N lies in (1/B)Z. Thus E tending to zero already forces eventual equality, without a Subspace Theorem. Equation (S5) gives E tending to zero whenever q'-5q tends to positive infinity. In particular, infinitely many nonresonant convergents whose next partial quotient is at least five would suffice: q'=a_next*q+q_previous, so q'-5q>=q_previous tends to infinity. This boundary improvement uses the removal of the logarithmic factor in (S4). Such an infinite supply, and nonstabilization on it, remain unproved.

A concrete single sufficient jump is 53/84 -> 306/485, with 485=5*84+65; this is not an infinite sequence. No argument in this note guarantees infinitely many such jumps for log_3(2). Generic irrationality, and the extra fact that this log ratio is not quadratic, do not supply the missing partial-quotient threshold five. The exact skew theorem proved above does not lower the clearing exponent six.

### Gaps

The requested adequate unconditional infinite-return theorem remains unresolved in this branch. In particular there is no proved infinite sequence meeting the scalar model's error/height requirement and no proved nonstabilization of its rational values. No old file was edited, no dependency was installed, no broad sweep or new density decimal was computed, and no Lean work or external submission was performed.
