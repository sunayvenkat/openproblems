# Global minimum potentials, grade signs and retimed tokens

**Status: no adequate infinite weighted-return construction has been proved.** There are two positive exact results in this note. First, complete reversal of a balanced color block has a weighted sign, and a cyclic-color grade has that sign at every block length, with an explicit tie-ray formula. Second, the entire corrected count vector is a positive counting process after two explicit families of token delays. The low-event families genuinely defeat the naive grade-by-grade sign extension: two actual-context grades at the same rational slope have opposite weighted signs. The local carries do not yet eliminate hybrid arithmetic. — [Current finite theorem](../prefix-and-phase-audit/REPORT.md), [exact certificate](global_carries_check.py).

## Does reversing a complete grade have a definite weighted sign?

### Takeaway

Yes for every balanced color block, and also for every finite cyclic-color block, with a fixed initial adjusted state. The sign holds for complete reversal even though individual same-color adjacent swaps can have the opposite sign. It does not extend automatically to the attached exceptional events. — [Exact certificate](global_carries_check.py).

### Cited Findings

- The finite optimum is the minimum of the three corrected color counts. At an ordinary high-row vertex, exactly its color count increases by one. — [Finite formula and proof](../prefix-and-phase-audit/REPORT.md).
- An individual distinct-color swap has a nonnegative off-diagonal minimum Hessian, while the same-color Hessian is nonpositive. Reusing original contexts through a swap decomposition is invalid. — [Weighted swap identities](../infinite-return-construction/weighted_returns.md).
- At a nonresonant rational slope p/q, a finite grade pa+qb=k has colors cycling by q+p modulo3 along its lattice chain. The two one-sided models traverse each grade in reverse orders and have the same corrected vectors before and after it. — [Full graded potential proof](../reflected-return-models/two_sided_models.md).
- The new certificate independently checks the direct insertion orders, all cyclic residue formulas on 1,750 state/word cases, the weighted summation-by-parts identity, and 11,250 balanced-word cases. These finite checks supplement the proofs below. — [Certificate](global_carries_check.py).

### Inferences

**General exact reversal identity.** Let m(Q)=min(Q0,Q1,Q2) for any integer vector Q. Fix a finite ordered color word i0,...,i_(ell-1). Assign physical reciprocal weights w0>=...>=w_(ell-1)>0 to its positions. In the forward order let f_i be the minimum increment assigned to token i. In the reversed processing order let r_i be the increment assigned to the same physical token. Let N be the total color-count vector and n(k) the vector for the first k positions. Then

```
sum_(i<k) f_i = m(Q+n(k))-m(Q),
sum_(i<k) r_i = m(Q+N)-m(Q+N-n(k)).
```

Consequently the reverse-minus-forward prefix difference is exactly

```
D(k)=m(Q)+m(Q+N)-m(Q+n(k))-m(Q+N-n(k)).          (GC1)
```

The total difference D(ell) is zero. Summation by parts therefore gives

```
sum_i w_i(r_i-f_i)
 = sum_(k=1)^(ell-1) D(k)(w_(k-1)-w_k).         (GC2)
```

This compares the two complete orders with their correct intermediate contexts. It is not a sum of Hessians evaluated at one frozen state. — [Direct-order and weighted checks](global_carries_check.py).

**Balanced-block theorem.** If N=K(1,1,1), then

```
D(k)=2m(Q)-m(Q+n(k))-m(Q-n(k)) >= 0.            (GC3)
```

To prove the inequality choose j with Qj=m(Q). The two minima on the right are at most Qj+n_j(k) and Qj-n_j(k), whose sum is 2m(Q). Thus complete reversal never lowers the weighted min-birth cost. This holds for *any* color word with balanced totals, not just a cyclic word. If the physical weights strictly decrease, the sign is strict exactly when some D(k)>0. No matroid, generic submodularity or bounded-state hypothesis is used. — [Balanced-word certificate](global_carries_check.py).

**All-length cyclic-grade theorem.** Relabel colors in the order of their occurrence so that the word is 0,1,2,0,1,2,... . This covers either nonresonant color direction and any starting color. Write ell=3K+s, k=3L+r, and put

```
u0=0, u1=e0, u2=e0+e1.
```

Removing common translations in (GC1) gives

```
D(k)=m(Q)+m(Q+u_s)-m(Q+u_r)-m(Q+u_s-u_r).      (GC4)
```

It is zero for r=0 or r=s. All remaining cases are

|s|r|D(k)|
|---|---|---|
|0|1|1_[Q0=min(Q1,Q2)]|
|0|2|1_[Q2=min(Q0,Q1)]|
|1|2|1_[Q1=Q2<=Q0]|
|2|1|1_[Q0=Q1<Q2]|

Here is a direct verification rather than an empirical extrapolation. For s=0,r=1, the two possible increases D0 m(Q-e0) and D0 m(Q) differ precisely when Q0 equals min(Q1,Q2). The r=2 case follows by replacing u2 with the common translation 1-e2. For s=1,r=2, the expression is D1 m(Q-e1)-D1 m(Q+e0). The first term is 1 iff Q1<=min(Q0,Q2); the second is 1 iff Q1<=Q0 and Q1<Q2, leaving exactly Q1=Q2<=Q0. For s=2,r=1, the expression is the distinct-coordinate Hessian D0D1 m(Q)=1_[Q0=Q1<Q2]. These cases exhaust r,s. Thus D(k) is always0 or1. — [Independent direct-insertion table checks](global_carries_check.py).

For geometric weights w_i=w0*t^i, 0<t<1, the exact nonnegative response is

```
w0(1-t) sum_(k=1)^(ell-1) D(k)t^(k-1).          (GC5)
```

For a rational grade the physical values form a geometric progression. Taking the forward direction to be increasing physical value gives decreasing reciprocal weights, so (GC5) applies whenever the grade contains only ordinary color insertions. For the c=1-3eta coefficients the sign is reversed by the factor -3. This theorem gives a genuine nonvanishing criterion for one complete pure grade: a relevant tie-ray hit suffices. It does not prove nonvanishing after adding exceptional grades of possibly opposite signs. — [Grade structure](../reflected-return-models/two_sided_models.md), [certificate](global_carries_check.py).

### Gaps

- The adjusted process's low-row endpoint increments need not form a cyclic word. One cannot apply (GC4) using the original vertex colors when an attached indicator changes.
- A reversal of all grades between two different slopes is not a reversal of one balanced block. Balanced total counts alone do not prove a sign for that collection of partial reversals.
- No theorem controls the infinite sum of the tie-ray responses in (GC5) with the arithmetic required for the weighted-return goal.

## Can the full boundary correction be absorbed into a global positive process?

### Takeaway

Yes. The corrected vector K-I-P is exactly the counting process of explicitly delayed colored tokens. This removes negative indicator jumps from the global description and supplies a rational generating function for the marginal token weights. The nonlinear minimum and its rank coupling still carry the unresolved arithmetic. — [Finite indicator definitions](../prefix-and-phase-audit/REPORT.md), [retiming certificate](global_carries_check.py).

### Cited Findings

- An isolated dyadic root e>=2 is active on [e,3e/2); a patch root e>=2 is active on [6e,27e/4). At most one exception is active at a time. — [Complete finite formula](../prefix-and-phase-audit/REPORT.md).
- The actual low-row events cancel a dyadic insertion, replace a b=1 insertion by a different color, or add a second color at b=3. The origin and the small patch-root exceptions must be handled explicitly. — [Corrected low-event audit](../reflected-return-models/actual_carries.md).
- The new checker counts delayed tokens independently of the indicator formula and verifies vector equality at 23 exact cutoffs, including both sides of27/2 and both exceptional grade chains below. — [Certificate](global_carries_check.py).

### Inferences

Start with one token for every original vertex 2^a3^b, with fixed color a-b modulo3. Change its arrival time, keeping its color, as follows:

```
b=0,a>=1:  2^a       moves to 3*2^(a-1);
b=1,a>=2:  3*2^a     moves to 27*2^(a-3);
otherwise: arrival time remains 2^a3^b.             (GC6)
```

Let T_j(t) count arrived tokens of color j. Then, for every real t>=1,

```
T_j(t)=K_j(t)-I_j(t)-P_j(t).                       (GC7)
```

**Proof.** A dyadic token e=2^a,a>=1 is missing from the raw count exactly when e<=t<3e/2, exactly its isolated-root window. A row-one token at3*2^a,a>=2 is missing exactly when 3*2^a<=t<27*2^(a-3). Setting e=2^(a-1) turns this into6e<=t<27e/4; its color a-1 is exactly the patch root color. Every other token is unchanged. This proves the vector identity, including endpoints and all small admissibility restrictions, directly from the indicator definitions. — [Indicator source](../prefix-and-phase-audit/REPORT.md), [independent counting certificate](global_carries_check.py).

There is one nonsmooth arrival: the token originally at12 arrives at27/2. Its vector change is (3,2,2)->(3,3,2), so the minimum has zero increment. All other arrivals are smooth, with possible simultaneous tokens. At a common arrival time, processing the simultaneous tokens in any order gives the same weighted total min-increment because their reciprocal weights agree. Thus, using the proved finite formula,

```
tau(t)=min_j T_j(t)                               (GC8)
```

is a pure positive token-count process, with no deletion events. — [Nonvertex endpoint verification](../reflected-return-models/two_sided_models.md), [exact small vectors](global_carries_check.py).

The same identity extends to the synthetic parameter lambda=3^theta: delay lambda^a to3lambda^(a-1) and3lambda^a to27lambda^(a-3). It describes the artificial adjusted minimum used in the two-sided model, without assuming a global cover-optimum theorem for synthetic slopes. The delays remain forward because lambda<3 and lambda^3<9 in the prescribed slope interval. — [Synthetic model definition and interval](../reflected-return-models/two_sided_models.md).

**Exact rational marginal generating function.** Let x,y encode the retimed exponents, and let omega^3=1. The token color series is

```
T_omega(x,y)
 = 1/[(1-omega*x)(1-omega^2*y)]
   + omega*(y-x+x^(-1)*y^3-x^2*y)/(1-omega*x).      (GC9)
```

The first correction removes and delays the dyadic tokens; the second does the same for row-one tokens starting at a=2. The one negative x exponent is the single27/2 arrival, not an infinite negative-exponent tail. In particular the total uncolored reciprocal token mass is

```
T_1(1/2,1/3)=3-1/3-1/54=143/54.                  (GC10)
```

Root-of-unity filtering makes each of the three color marginal masses rational. This is a linear marginal statement; it does not evaluate the minimum's birth weights. — [Retiming proof above and exact arithmetic check](global_carries_check.py).

For an alternative precise global formulation, let t_j(k) be the kth arrival of color j, counting multiplicities. Equation(GC8) gives

```
sum_(a,b>=0) eta_(a,b)/(2^a3^b)
 = sum_(k>=1) 1/max(t_0(k),t_1(k),t_2(k)).          (GC11)
```

The zero increment at27/2 contributes nothing. Every term is nonnegative, so monotone convergence justifies the identity. Each marginal sum sum_k1/t_j(k) is rational by(GC9), whereas the rank-coupled maximum in(GC11) is not evaluated. This isolates one global nonlinear obstruction without postulating finite state. — [Finite minimum formula](../prefix-and-phase-audit/REPORT.md), [retiming certificate](global_carries_check.py).

### Gaps

- No finite or discounted carry identity evaluates the rank-coupled maximum in(GC11) from its three rational marginals.
- The token retiming does not turn all rational grades into balanced or cyclic color words. It identifies exactly where that property fails.
- A bounded or controlled carry potential satisfying a discounted identity for the true min-readout has not been constructed. Writing an ordinary potential difference would still leave its discounted weighted series.

## Do the exceptional grades preserve a usable global sign or close the return?

### Takeaway

The straightforward sign extension fails in exact actual contexts, not just arbitrary translated states. A possible strict bracketing statement restricted to actual continued-fraction convergents remains a sharply defined candidate for proving nonstabilization; it is unproved. The adequate upper-return family and its arithmetic costs remain unresolved. — [Exact grade counterexamples](global_carries_check.py), [current arithmetic frontier](../reflected-return-models/REPORT.md).

### Cited Findings

- The correct5/8 side agrees with the actual target on a<27,b<17. Its full plus/minus values and all low rules are explicitly reconstructed by the existing exact model. — [Matching and model conventions](../reflected-return-models/record_returns.md), [paired model source](../reflected-return-models/two_sided_models_check.py).
- The sole high-row forbidden motif does not control global carries; the earlier rational aperiodic countermodel can preserve any finite actual head and the full fifteen-pattern language. The present results use the minimum potential and full correction process instead. — [Earlier carry theorem and limitations](../reflected-return-models/actual_carries.md).
- The current arithmetic construction still needs adequate actual infinite supply and nonvanishing. The product-tail hybrid comparison has no proved denominator compression. — [Latest audit](../reflected-return-models/final_reflected_audit.md).

### Inferences

**Two exact actual-context opposite signs.** Use the rational grade5a+8b=k and increasing actual physical values. Both chains below consist of consecutive actual smooth points; the checker verifies the complete chain and counts its actual adjusted vectors independently.

|Grade|Points(a,b)|Initial actual Q|Effective token colors|eta_plus|eta_minus|Weighted eta_plus-minus|
|---|---|---|---|---|---|---|
|48|(0,6),(8,1)|(11,12,12)|0,0|1,0|0,1|13/186624|
|88|(0,11),(8,6),(16,1)|(37,36,36)|1,2,2|0,1,0|1,0,0|-13/45349632|

At grade48 the physical values are729,768; at grade88 they are177147,186624,196608. The b=1 attached event changes the effective final color by+2. The first chain becomes a same-color word and has the opposite sign to the pure-grade theorem. The second has its displayed positive/negative arrangement. The plus digits equal the actual finite-optimum births at all five points, verified directly and also covered by the matching rectangle. Thus these are genuine actual-context failures of the proposed grade-by-grade monotonic extension. — [Exact actual counts, order checks and rational signs](global_carries_check.py).

The complete5/8 paired weighted eta difference is also exactly

```
sum (eta_plus-eta_minus)/(2^a3^b)
 =25199209663/249993707168205 >0.                  (GC12)
```

Therefore the c-weighted scalar value has a strictly negative jump from the minus model to the plus model as the synthetic slope crosses5/8 upward. A globally nondecreasing synthetic scalar functional is false. This statement follows from the complete rational model evaluation, not merely from one grade. No assertion that every possible grouped/corrected functional fails is made. — [Independent assertion of the full rational value](global_carries_check.py), [full model evaluation](../reflected-return-models/two_sided_models_check.py).

**Precisely delimited followup candidate.** On selected *actual* nonresonant continued-fraction convergents p_n/q_n, prove a strict paired bracket

```
min(Z_plus(n),Z_minus(n)) < Z < max(Z_plus(n),Z_minus(n))
```

infinitely often, or any equivalent strict matched-side inequality. This would show that the corresponding scalar error is nonzero at those scales. It would not establish the upper approximation threshold q_next-5q->infinity, and an intersection with any adequate-supply subsequence must still be justified. Restricting to actual convergents is substantive; this note gives no bracketing theorem for arbitrary rational slopes. No new sweep or assumed numerical trend supports this candidate. — [Actual supply and nonstabilization interface](../infinite-return-construction/REPORT.md).

The two exact positive lemmas suggest a narrower next calculation: in the retimed-token representation, group the exceptional endpoint words using their actual delays and derive the resulting discounted residual, retaining all tie-ray contexts. A successful grouping would need complete coverage, convergence and a denominator or fixed-coefficient proof. Neither a local binary carry nor the rationality of the token marginals supplies these facts. — [Retimed representation(GC6)-(GC11)](global_carries_check.py), [weighted arithmetic obstruction](../infinite-return-construction/weighted_returns.md).

### Gaps

- No adequate infinite weighted upper return, hybrid elimination or target-slope bracketing theorem was obtained.
- The positive grade sign is a complete-block theorem, not a proof that the signed sum over all actual/model differences is nonzero.
- The retimed-token formula is exact global structure but leaves nonlinear rank coupling. It should not be presented as S-unit compression.
- Skipped: Lean, installs, broad scans, density decimals, old-file edits and external posting. Main risk: applying a pure cyclic or balanced-block sign to exceptional endpoint words, or replacing the rank-coupled minimum by its rational marginals.
