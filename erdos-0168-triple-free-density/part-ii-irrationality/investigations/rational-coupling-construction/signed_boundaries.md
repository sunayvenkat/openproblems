# Signed boundary cancellation and its arithmetic cost

**Status: no adequate arithmetic infinite return is constructed.** There are three new exact results. A signed polynomial has a formally finite weighted boundary precisely when its restrictions to the two evaluation axes are the same constant. No nonzero-evaluation multiple of a single annihilator can have this property, even with arbitrary signed coefficients. More strongly, an integer combination of two adjacent annihilators with finite boundary must pay an explicit smooth divisor of asymptotic degree four. Adjacent toric Laurent identities do allow a fixed finite-boundary operator, but negative shifts and their arithmetic cost cannot be discarded. A complete actual-tail certificate shows that this fixed operator's target residual is nonzero. — [Exact certificate](signed_boundaries_check.py), [previous boundary identity](../hybrid-arithmetic-closure/hierarchy_absorption.md).

The only new executable is [signed_boundaries_check.py](signed_boundaries_check.py). It uses integer/Fraction arithmetic and the proved finite formula to count actual digits. It edits no earlier file, makes no density-decimal calculation, and tests only three prescribed adjacent pairs plus one fixed actual residual. The polynomial and valuation proofs below establish the general statements; finite checks supplement them. — [Certificate source](signed_boundaries_check.py).

## Which signed shift polynomials really remove every infinite boundary profile?

### Takeaway

For finite nonnegative-index shifts, formal removal of all infinite sides is completely characterized by a two-axis restriction. When the coefficients are integers, the surviving boundary is automatically an explicit integer finite head. A signed multiplier of any one nonconstant annihilator cannot retain a nonzero target coefficient and satisfy this characterization. — [General boundary kernel](../hybrid-arithmetic-closure/hierarchy_absorption.md), [certificate](signed_boundaries_check.py).

### Cited Findings

- For bounded arrays d on the nonnegative quadrant, with W(d)=sum d(a,b)2^(-a)3^(-b), the previous exact identity is P(2,3)W(d)=B_P(d)+W(Pd). Its boundary kernel is 2^(-a)3^(-b) times sum c_AB2^A3^B over a<A OR b<B. This holds for signed coefficients as well as positive ones. — [HA1-HA3](../hybrid-arithmetic-closure/hierarchy_absorption.md).
- The actual high array is d(a,b)=c(a,b+4), where c lies in {1,-2}; its four omitted low rows remain a separate contribution to Z. A finite-head theorem for d alone does not evaluate those low rows. — [HA10 and low-row scope](../hybrid-arithmetic-closure/hierarchy_absorption.md).
- The new certificate checks the kernel, the finite-head formula for an independently chosen signed Q, and the special fixed operator used below. — [Certificate](signed_boundaries_check.py).

### Inferences

**Signed finite-boundary theorem.** Let P in Z[X,Y] be finite, and lambda=P(2,3). Its boundary kernel has finite support on the nonnegative quadrant if and only if

```
P(X,3)=lambda,             P(2,Y)=lambda.             (SB1)
```

Equivalently there exists Q in Z[X,Y] with

```
P=lambda+(X-2)(Y-3)Q.                                (SB2)
```

Here finite support is a statement about the kernel itself, hence valid for every bounded d, not just the actual array. — [Kernel source](../hybrid-arithmetic-closure/hierarchy_absorption.md), [finite checks](signed_boundaries_check.py).

**Proof.** Choose a maximal Y exponent B_max. For b>=B_max the kernel is 2^(-a)3^(-b) times

```
sum_(A>a) 2^A sum_B c_AB3^B.
```

If this functional has finite support, the displayed cumulative sum must vanish for every a>=0. Successive differences imply sum_B c_AB3^B=0 for every A>=1. Thus P(X,3) is constant. Its value at X=2 is lambda. Interchanging the axes proves the other restriction. Conversely the two restrictions make the vertical tail vanish for b>=B_max and the horizontal tail vanish for a>=A_max. The remaining support is finite. Finally P-lambda is divisible by both monic factors X-2 and Y-3. Successive monic division proves (SB2) over Z, not merely over Q. — [Kernel identity and coefficient certificate](signed_boundaries_check.py).

There is also an exact integer evaluation of that finite head:

```
B_P(d)=-6 (Qd)(0,0)=-6 sum_(A,B) q_AB d(A,B).        (SB3)
```

Indeed direct reindexing gives W((S_a-2)(S_b-3)e)=6e(0,0), for any bounded e; apply it to e=Qd in (SB2). This proves integrality for every integer d. It also identifies all signs and all corner terms without independently truncating an infinite side. — [Exact check](signed_boundaries_check.py).

**Common-factor obstruction.** Put

```
L_(p,q)(X,Y)=X^(2q)+X^qY^p+Y^(2p),  p,q>0.
```

If P=A L_(p,q), with A in Z[X,Y], satisfies (SB1), then lambda=0. To see this, specialize Y=3. The nonconstant polynomial L_(p,q)(X,3) would divide the constant lambda. The same conclusion holds for any polynomial multiple of a product containing one such factor. Thus arbitrary signed multiplication does not repair the old positive-product boundary problem while preserving a nonzero coefficient of W(d). This does not concern actual-specific identities that cancel a nonzero kernel only after it is paired with the actual array. — [Annihilator source](../infinite-return-construction/weighted_returns.md), [proof above](signed_boundaries_check.py).

### Gaps

- Formal finite support is sufficient for arithmetic control, but is not necessary for the actual boundary to have a rational value. The theorem does not rule out a relation using the actual coupled states. — [Actual boundary gap](../hybrid-arithmetic-closure/hierarchy_absorption.md).
- The full target boundary also contains all four low rows. They have not been absorbed by (SB1)-(SB3). — [HA10](../hybrid-arithmetic-closure/hierarchy_absorption.md).
- Several different annihilators can be combined without sharing a common factor. The next theorem treats two adjacent slopes; it is not a theorem for every deeper hierarchy. — [Two-scale setup below](signed_boundaries_check.py).

## What must a two-adjacent-annihilator signed elimination pay?

### Takeaway

For adjacent slopes, every integer polynomial combination with nonzero evaluation and formally finite boundary pays at least 2^(2Q)3^(2P), where Q and P are the larger denominator and numerator. This includes signed sums, not just products. For actual large adjacent convergents its logarithmic cost is at least (4+o(1))Q log2, which exceeds the presently proved clearing-cost interface. It is a scoped cost theorem, not a general impossibility result. — [Proof and exact ceiling checks](signed_boundaries_check.py), [current budget](../hybrid-arithmetic-closure/adaptive_induction.md).

### Cited Findings

- An additive prime valuation extends to an algebraic extension of its complete valued field. We use the extension normalized by v_ell(ell)=1; it may take rational values on algebraic elements. — [Sharifi, Algebraic Number Theory, Theorem 5.4.7](https://math.ucla.edu/~sharifi/notes/algnum-ch05.html).
- With a unique least-valuation term, a sum has that least valuation. This follows from the nonarchimedean triangle inequality by dividing by that term; all other terms lie in the maximal ideal. — [Valuation framework and extension theorem](https://math.ucla.edu/~sharifi/notes/algnum-ch05.html).
- The currently proved last-rectangle clearing interface requires an effective exponent below 1+C_*=(25+sqrt5)/10. The actual hierarchy has cost at most5/2, but has no integer boundary numerator. — [Supply and acceptance](../infinite-return-construction/diophantine_supply.md), [actual hierarchy](../hybrid-arithmetic-closure/hierarchy_absorption.md).

### Inferences

**Adjacent signed-elimination cost theorem.** Label the two slopes increasingly and assume

```
p/q<r/s,       qr-ps=1,       q>=3, r>=3.
```

Suppose A,B,P are integer polynomials, with

```
P=A L_(p,q)+B L_(r,s),
P(X,3)=P(2,Y)=lambda.
```

Then

```
2^(2 max(q,s))*3^(2 max(p,r)) divides lambda.        (SB4)
```

The statement permits lambda=0; its cost conclusion concerns lambda!=0. If a pair is supplied in determinant-minus-one orientation, interchange the two pairs first. The maximums are unchanged. A symmetric sufficient condition is p,q,r,s>=3, which covers every sufficiently late actual adjacent pair. Resonance modulo three is not needed for this algebraic theorem; it matters separately when using the Li as actual local annihilators. — [Certificate for both input order patterns](signed_boundaries_check.py).

**The 3-adic bound.** In an algebraic extension of Q_3 choose a root x of x^q=3^p omega, where omega is a primitive cube root of unity. It has v_3(x)=p/q>0 and is a root of L_(p,q)(X,3). Every integer polynomial in x has nonnegative valuation. Since sp/q<r, the three terms of L_(r,s)(x,3) have valuations

```
2sp/q,       sp/q+r,       2r,
```

with the first uniquely smallest. Evaluating the polynomial combination at x proves

```
v_3(lambda)>=2sp/q=2r-2/q.
```

The valuation of the integer lambda is integral, so q>=3 gives v_3(lambda)>=2r. Conversely choose x with x^s=3^r omega, a root of the upper-slope polynomial. The lower polynomial's three valuations have unique minimum 2p, proving v_3(lambda)>=2p. Together they give v_3(lambda)>=2max(p,r). Zero evaluations of A or B only strengthen the inequalities. — [Extension theorem](https://math.ucla.edu/~sharifi/notes/algnum-ch05.html), [exact ceiling assertions](signed_boundaries_check.py).

**The 2-adic bound.** In an algebraic extension of Q_2 choose y with y^p=2^q omega. It is a root of L_(p,q)(2,Y) and has v_2(y)=q/p. Since rq/p>s, the upper polynomial has unique least valuation 2s, so v_2(lambda)>=2s. At a root y^r=2^s omega of the upper polynomial, the lower polynomial has unique least valuation

```
2ps/r=2q-2/r.
```

The ceiling is 2q when r>=3. Hence v_2(lambda)>=2max(q,s). The two prime bounds prove (SB4). No estimate for the size of A or B was needed. — [Valuation extension](https://math.ucla.edu/~sharifi/notes/algnum-ch05.html), [certificate](signed_boundaries_check.py).

**Coefficient clearing and scope of the cost.** If rational coefficients are used instead, let D be an actual positive integer clearing every coefficient of the representation. Apply (SB4) to DP. The combined target coefficient Dlambda, not an uncharged scaled-down lambda, pays the stated divisor. From (SB3), the corresponding universally cleared boundary is an integer. An actual cancellation that clears only the final evaluated head with a smaller denominator is a different, state-dependent assertion and is not ruled out. — [Finite-head formula and exact arithmetic](signed_boundaries_check.py).

For actual adjacent convergents, write Q=max(q,s), P=max(p,r). Their numerators increase with their denominators, and P log3=Q log2+o(1). Thus every nonzero lambda in this architecture has

```
log|lambda| >=2Q log2+2P log3=(4+o(1))Q log2.       (SB5)
```

This does not fit the already established error interface using only the guaranteed ratio r>C_*, whose budget is1+C_*<4. It does not preclude a stronger actual error theorem or unusually large actual successor ratios. Nor does it cover an ideal generated by many differently sized annihilators, nonlinear profiles, different matching constructions, or a boundary functional proved rational only on the actual array. — [Budget being compared](../infinite-return-construction/diophantine_supply.md).

### Gaps

- No near-optimal coefficient construction attaining the lower bound is asserted. A large resultant is unnecessary for the lower bound, but the theorem does not compute the minimum possible height of every identity. — [Exact theorem scope](signed_boundaries_check.py).
- A stronger real estimate could change the relevant arithmetic budget. The theorem does not establish absence of an actual adequate infinite family. — [Open actual arithmetic requirement](../hybrid-arithmetic-closure/hierarchy_absorption.md).
- Common coefficient clearing cannot be omitted. Conversely, a proof using special actual-state divisibility rather than universal coefficient clearing requires its own argument. — [Full arithmetic interface](../hybrid-arithmetic-closure/final_hybrid_audit.md).

## Do adjacent Laurent relations provide a cheaper valid escape?

### Takeaway

There is an explicit boundary-free operator of evaluation182 in the adjacent Laurent ideal, with balanced representations having only linear exponent support. Its coefficients use negative horizontal shifts. Clearing those shifts reintroduces infinite sides; their small real evaluations do not make arithmetic height free. The fixed actual residual is rigorously nonzero. — [Exact balanced certificates and actual-tail enclosure](signed_boundaries_check.py).

### Cited Findings

- With qr-ps=1, the monomials U=X^qY^(-p), V=X^sY^(-r) satisfy X=U^rV^(-p), Y=U^sV^(-q). Each U^3-1 is a Laurent multiple of L_(p,q), and each V^3-1 is a Laurent multiple of L_(r,s). — [Exact polynomial certificate](signed_boundaries_check.py).
- Negative shifts are not positive-shift operators on the original quadrant. Multiplying a Laurent identity by a monomial makes its coefficients polynomial, but changes the weighted boundary kernel. — [Boundary kernel](../hybrid-arithmetic-closure/hierarchy_absorption.md), [explicit translated-kernel check](signed_boundaries_check.py).
- The new actual enclosure computes d by the proved finite minimum and keeps the entire omitted geometric tail; it is not a finite numerical approximation without tail control. — [Actual digit and tail code](signed_boundaries_check.py).

### Inferences

**A fixed Laurent elimination.** The two identities U^3=1,V^3=1 in the quotient imply X^3=Y^3=1 there. Define

```
P0=-X^3Y^3+27X^3+8Y^3-34
  =(27-Y^3)(X^3-1)+7(Y^3-1).                        (SB6)
```

It is in the adjacent Laurent ideal and satisfies

```
P0(2,3)=182,        P0(X,3)=P0(2,Y)=182,
B_P0(d)=216 sum_(a,b<3)d(a,b)2^(-a)3^(-b) in Z.     (SB7)
```

Equivalently P0=182-(X-2)(Y-3)(X^2+2X+4)(Y^2+3Y+9), so (SB7) follows also from (SB2)-(SB3). The constant term -34 shows P0 is not in the ordinary polynomial ideal (L_(p,q),L_(r,s)): both generators vanish at(0,0). Thus some negative exponent is unavoidable in every Laurent representation of this particular fixed P0. — [Exact P0 and kernel checks](signed_boundaries_check.py).

**Balanced, rather than quadratic-support, inverse powers.** To telescope X^3-1, use r steps U^3 and p steps V^(-3). At prefix t of N=r+p steps, take floor(tr/N) U^3 steps. To telescope Y^3-1, use s U^3 steps and q V^(-3) steps, with floor(ts/(s+q)) U^3 steps. The partial exponent vectors stay in a rectangle of side O(q+s) by O(p+r). A U^3 step from exponent(a,b) contributes

```
X^aY^b(U^3-1)
 =[X^(a+q)Y^(b-3p)-X^aY^(b-2p)] L_(p,q),
```

and a V^(-3) step contributes

```
X^aY^b(V^(-3)-1)
 =[-X^(a-2s)Y^b+X^(a-3s)Y^(b+r)] L_(r,s).
```

Their telescoping sum has O(p+r+q+s) terms in general and O(q+s) for the bounded slopes of the actual convergent application, after combining the X and Y paths in (SB6). These are exact integer Laurent identities. The certificate reconstructs both endpoint identities and P0 coefficientwise; it does not merely compare values at(2,3). — [Balanced path implementation](signed_boundaries_check.py).

For the prescribed oriented pairs the complete P0 coefficient supports and the shifts required by this construction are:

|Lower and upper slopes|Total coefficient monomials|X support|Y support|Shift to nonnegative exponents|Translated evaluation bits|
|---|---:|---|---|---|---:|
|5/8,12/19|90|[-78,-13]|[0,41]|X^78|86|
|41/65,12/19|276|[-249,-38]|[0,135]|X^249|257|
|306/485,53/84|1858|[-1704,-168]|[0,971]|X^1704|1712|

After the shift X^M, the target operator is X^M P0, whose restriction at Y=3 is182X^M. It has infinite vertical boundary profiles by (SB1). Its evaluation182*2^M is therefore **not** a successful finite-boundary clearing coefficient and need not satisfy (SB4). For example the second translated evaluation has257 bits whereas the mandatory divisor for a truly finite-boundary ordinary combination has260 bits; there is no contradiction. — [Exact supports, evaluations and mandatory divisors](signed_boundaries_check.py).

The real value of a monomial X^aY^b at(2,3) may be modest because a log2+b log3 is small. The numerator and denominator exponents are still linear in q+s, and extending the actual array across negative indices introduces the missing boundary profiles. Neither an uncharged common denominator nor the assumption of a common large origin rectangle is justified. The older adjacent annihilator has only its own q_next-q and p_next-p-4 window. — [Actual annihilator windows](../hybrid-arithmetic-closure/hierarchy_absorption.md), [signed support certificate](signed_boundaries_check.py).

**A fixed actual nonzero residual.** For the actual high array, the finite corner in (SB7) is exactly -552. Summing W(d) for a<28,b<20 and retaining its full tail gives

```
139875/1024 < W(P0d) < 139876/1024.                  (SB8)
```

To verify the enclosure, put v=2^(-28)+3^(-20)-2^(-28)3^(-20). Since d is in{-2,1}, the complete W(d) lies between its rectangle sum minus6v and that sum plus3v. Multiply these bounds by182 and add552, using (SB7). This proves (SB8) without assuming irrationality of any series. In particular the formal toric quotient cannot be promoted to P0d=0 on the actual process. — [Full-tail assertion](signed_boundaries_check.py).

### Gaps

- The Laurent representations do not establish small weighted residuals after all negative-index and boundary corrections are retained. The fixed actual residual is nonzero, not exponentially small. — [SB8 certificate](signed_boundaries_check.py).
- No signed actual-state corrector, cheap rational coupling phase combination, fixed-lattice boundary theorem, or adequate infinite arithmetic return has been obtained. The full goal remains open. — [Current actual hierarchy gap](../hybrid-arithmetic-closure/hierarchy_absorption.md).
- These theorems leave actual-specific cancellation, richer readout families, many-scale nonprincipal ideals and nonlinear matching constructions available; they should not be cited as a general impossibility theorem. — [Precisely scoped classification and cost proof above](signed_boundaries_check.py).
- Skipped: Lean, broad scans, installs, density decimals, old-file edits, external submission and priority assessment. Main risk: treating a Laurent quotient identity, a small real monomial value, or a formal finite-head condition as a budget-compatible actual arithmetic return.
