# Erdős 168(ii): exact weighted returns and the obstruction to the KK transfer

Status: **the irrationality conjecture is not solved**. The results below do not assume the proposed cover formula (C), except where a statement is explicitly labeled conditional. They give an exact arithmetic return identity with controlled height, an exact counterexample to the endpoint-to-weighted implication, and a count of the unavoidable events in the direct return expansion. They do not prove that every possible resummation fails.

## What exact weighted return identity is available?

### Takeaway

The density has an unconditional return identity with an integer head and coefficients in a fixed finite set. Its height bound has precisely the exponential scale needed by Kohlmeyer–Kruer; the missing parts are a bounded number of retained terms, an additional exponential saving in the remainder, and nonvanishing.

### Cited Findings

- The local smooth-component reduction expresses the density as a reciprocal sum of the increments of the finite extremal function. The local extremal increment is either zero or one. — [Veselinov, §§3–6](https://arxiv.org/html/2604.15515v1)
- Kohlmeyer–Kruer Proposition 7.4 applies to a fixed-dimensional linear form with fixed rational coefficients in positive S-units. Their application obtains at most 404 terms, height at most exp(27L), and a nonzero error at most exp(−T−L/200). — [Primary manuscript, §§6–7](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf), [saved source](../Erdos%20theorem%20transfer%20investigation/erdos1062-fork-free-density.pdf.txt)

### Inferences

**The following identities and bounds are proved here.** Let S={2^a3^b:a,b≥0}. Put K(t)=#(S∩[1,t]), let F(t) be the largest subset of the corresponding exponent triangle containing no forbidden corner, and let τ(t)=K(t)−F(t). All three functions are zero for t<1. Define

\[
g(t)=F(t)-\tfrac23K(t),\qquad h(t)=3g(t)=K(t)-3\tau(t).
\]

At d∈S put

\[
a_d=\Delta h(d)=3\Delta F(d)-2\in\{1,-2\},
\]

and put a_x=0 when x∉S. Adding one vertex cannot decrease F and can increase it by at most one. In particular h has a **nonzero** jump at every smooth number. Absolute convergence gives

\[
Z:=\sum_{d\in S}\frac{a_d}{d}
=\int_1^\infty\frac{h(t)}{t^2}\,dt
=9c-6,
\tag{1}
\]

because Σ_{d∈S}1/d=3 and c=(1/3)ΣΔF(d)/d.

Fix Q≥1, q=2^Q, B=⌊log₃q⌋, and define, for r>1,

\[
b_Q(r)=a_{qr}-a_r.
\]

Its support is contained in q⁻¹S. If r∈S then b_Q(r)∈{−3,0,3}; otherwise b_Q(r)∈{1,−2}. Directly reindexing (1) proves

\[
\boxed{3^B(q-1)Z-N_Q
=\sum_{r>1}\frac{3^B b_Q(r)}r,}
\tag{2}
\]

where

\[
N_Q=3^B\left(q\sum_{d\in S,\ d\le q}\frac{a_d}{d}-1\right)\in\mathbb Z.
\tag{3}
\]

To check integrality, if d=2^a3^b≤q then a≤Q and b≤B, so 3^Bq/d is integral. The −1 is a₁. Thus the direct arithmetic analogue of KK's return identity exists without (C).

For a real T≥0 define

\[
S_Q(T)=\sum_{1<r\le e^T}\frac{3^B b_Q(r)}r,
\qquad E_Q(T)=3^BqZ-3^BZ-N_Q-S_Q(T).
\tag{4}
\]

Under the temporary assumption c∈Q, this is a rational-coefficient S-unit linear form minus an integer. Its coefficients lie in the fixed finite set {±Z,±1,±2,±3}.

Every retained unit is 3^B/r≥3^B exp(−T). Write r=2^(a−Q)3^b, with a,b≥0. Since r≤exp(T),

\[
a\log2+b\log3\le T+Q\log2.
\]

Consequently a common denominator of all coordinates divides a number at most 6exp(2T). Indeed the needed power of two is at most exp(T), and the needed power of three, after the factor 3^B, is at most 3exp(T). The head units are at most q²; all retained units are at most q; and |N_Q|≤7q². Therefore

\[
H\bigl(N_Q:3^Bq:3^B:(3^B/r)_r\bigr)
\le42\exp(2T+2Q\log2).
\tag{5}
\]

This bound does not depend on the number of terms. If T≥Qlog2, the quantity t₀=3^B exp(−T) is an admissible smallest-unit parameter in Proposition 7.4.

An explicit elementary tail bound follows from

\[
\sum_{d\in S,d>X}\frac1d
\le\frac{\tfrac32\lfloor\log_2X\rfloor+\tfrac92}{X}
\quad(X\ge1).
\]

Using |a_d|≤2 on the two reindexed tails gives

\[
\boxed{|E_Q(T)|\le
\left(3Q+\frac6{\log2}T+18\right)3^B e^{-T}.}
\tag{6}
\]

This is only a polynomial multiple of the smallest retained unit; the required additional factor exp(−ηQ) has not been obtained.

For comparison, the exact integral renewal identity for any multiplier q>1 is

\[
\int_1^\infty\frac{g(qt)-g(t)}{t^2}\,dt
=(q-1)\int_1^\infty\frac{g(t)}{t^2}\,dt
-q\int_1^q\frac{g(u)}{u^2}\,du.
\tag{7}
\]

No equality at a finite collection of cutoffs changes the last identity into equality of the weighted integrals between those cutoffs.

### Gaps

- The exact identity (2) does not yet give a sequence of forms of fixed dimension. Summing many events into one rational coefficient is not a remedy unless that coefficient is shown to belong to a fixed finite set, or a different applicable arithmetic theorem is proved.
- Neither a remainder smaller than t₀ by an exponential factor nor nonvanishing of the remainder has been established.
- Proving (C) remains a separate combinatorial problem. None of (1)–(7) requires it.

## Do balanced endpoint returns cancel the weighted intervals?

### Takeaway

No. A certified example has exact color and extremal returns at both endpoints, but a nonzero weighted defect. More generally, a single horizontal return necessarily has densely recurring boundary jumps and cannot agree pointwise on a long logarithmic interval.

### Cited Findings

- Existing work proves balanced returns at cutoffs T₀+klog6 for infinitely many Q, but explicitly leaves the weighted interval implication unproved. — [Earlier return proof](../open-conjecture-transfer-search/168_irrationality.md)
- The finite extremal values used below were recomputed by the exhaustive integer diagonal-mask dynamic program. All 120 prefixes through 294912 were replayed, without numerical optimization. — [Exact check](weighted_check.mjs), [result](weighted_check.json), [proof of the recurrence](../open-conjecture-transfer-search/168_grid.md)

### Inferences

**Exact finite counterexample, independent of (C).** Take q=512=2⁹ and t=10. The color-count triples and g-values are

| cutoff | (K₀,K₁,K₂) | g |
|---:|---:|---:|
| 10 | (3,2,2) | 1/3 |
| 5120 | (20,19,19) | 1/3 |
| 60 | (6,5,5) | 1/3 |
| 30720 | (28,27,27) | 1/3 |

Thus W(512·10)=W(10) and W(512·60)=W(60), where W(t)=Σω^jK_j(t); both actual g-values return as well. Nevertheless exact rational summation gives

\[
\sum_{10<d\le60}\frac{\Delta g(d)}d=\frac{13}{864},\qquad
\sum_{5120<d\le30720}\frac{\Delta g(d)}d=\frac{45511}{967458816},
\]

and therefore

\[
\boxed{512\sum_{5120<d\le30720}\frac{\Delta g(d)}d
-\sum_{10<d\le60}\frac{\Delta g(d)}d
=\frac{2135}{236196}\ne0.}
\tag{8}
\]

By Stieltjes integration by parts, the same number is

\[
\int_{10}^{60}\frac{g(512s)-g(s)}{s^2}\,ds,
\]

since the difference vanishes at both endpoints. All four cutoffs avoid smooth jumps, so no endpoint convention is involved. This refutes the proposed general implication from endpoint returns to weighted cancellation; it does not refute the proved existence of long discrete return segments.

**Mandatory boundary events.** For every Q≥1, at

\[
r=2^{a-Q}3^b\ge1,\qquad 0\le a<Q,
\tag{9}
\]

the function h(qt) jumps by a_(qr)∈{1,−2}, while h(t) does not jump because r has a negative two-exponent. Consequently b_Q(r)≠0 at every such point, independently of (C) or any return approximation.

For T≥0 and L>0, the exact number of these points in log r∈(T,T+L] is

\[
\sum_{a=0}^{Q-1}\left[
\left\lfloor\frac{T+L+(Q-a)\log2}{\log3}\right\rfloor
-\left\lfloor\frac{T+(Q-a)\log2}{\log3}\right\rfloor
\right]
=\frac{QL}{\log3}+O(Q),
\tag{10}
\]

with absolute error less than Q. Distinct exponent pairs give distinct points. Hence a logarithmic window of length proportional to Q contains order Q² mandatory nonzero atoms in the direct expansion (2).

The a=0 family alone has one atom every log3. Therefore h(qt)−h(t), and likewise g(qt)−g(t), cannot vanish identically throughout any logarithmic interval of length greater than log3. In particular no choice of a balanced phase can promote the known discrete endpoint return to pointwise equality throughout an interval of length proportional to Q.

This also prevents applying KK's event-free-window argument to the raw one-shift return: its event set has no gaps longer than log3. It does **not** prevent an as-yet-unknown algebraic resummation from canceling many events.

### Gaps

- The example (8) does not show that every specially selected long return block has nonzero weighted defect; it shows that endpoint equality alone is insufficient.
- The event lower bound counts the literal expansion. It is not a lower bound on the number of S-unit terms in every possible exact algebraic representation.

## Can a second difference or a known irrationality theorem close the gap?

### Takeaway

A second difference removes the mandatory fractional boundary obstruction, but an actual interior change of minimizing color survives. Existing polynomial Hecke–Mahler transcendence theorems require a sparsity property that has not been proved for this extremum process, and exact cancellation among the raw return atoms blocks a naive nonvanishing argument.

### Cited Findings

- KK starts with two geometric series having fixed step-function rotation coefficients. Its return identity has sixteen event families; a rotation spacing lemma creates long event-free windows, and its specific coefficient valuations prove that two truncations differ. — [Primary manuscript, §§5–6](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf)
- Luca–Ouaknine–Worrell's transcendence condition assumes fixed linear differences with nonzero positions separated by a positive multiple of the return length, together with polynomial variation. Their application concerns polynomials in ⌊nθ+α⌋. This is not an unconditional theorem for maxima of unbounded rotation cocycles. — [Definition 4 and Theorems 5, 7](https://arxiv.org/html/2412.07908v2)
- The three color discrepancies are unbounded, so a bounded collection of discrepancy states cannot be assumed. — [Earlier proof using Kesten's theorem](../open-conjecture-transfer-search/168_irrationality.md)

### Inferences

**The linear color renewal is valid.** With W(t)=Σ_{2^a3^b≤t}ω^(a+2b), inclusion-exclusion leaves only a 3×3 corner:

\[
W(t)-W(t/8)-W(t/27)+W(t/216)
=\sum_{0\le a,b<3}\omega^{a+2b}1_{2^a3^b\le t}=0
\quad(t\ge36).
\tag{11}
\]

The maximum element in that 3×3 corner is 2²3²=36; its total weight is zero. This proves the stated threshold directly.

Conditional on (C), g is a maximum of three affine functions of W, with explicit patch indicators. Applying a mixed difference to that maximum cannot commute the maximum with the difference. Its remaining jumps depend on which color is minimizing.

**A certified interior kink.** Define

\[
J(t)=g(t)-g(t/8)-g(t/27)+g(t/216).
\]

At d=157464=2³3⁹, the exact four jumps are

\[
\left(\Delta g(d),\Delta g(d/8),\Delta g(d/27),\Delta g(d/216)\right)
=\left(\tfrac13,\tfrac13,\tfrac13,-\tfrac23\right),
\]

so ΔJ(d)=−1. The four underlying smooth points are 157464, 19683, 5832, and729. Division by8 or27 preserves color, so the jumps of both color strips W(t)−W(t/8) and W(t)−W(t/27) cancel at d. All four points have three-exponent6 or9, whereas the isolated/patch indicator boundaries have three-exponents0,1, or3. Thus none of those indicators changes there either. The surviving kink is a real change of the extremal choice; it cannot be dismissed as an omitted axis correction. This finite claim is unconditional because its optima were checked exactly.

**Noncancellation needs a new argument.** For Q=6, the mandatory strip atoms coming from d=432=2⁴3³ and d=864=2⁵3³ lie at r=27/4 and r=27/2. Their exact h-jump coefficients are1 and−2, so their weighted contributions cancel:

\[
\frac{64}{432}-\frac{128}{864}=0.
\tag{12}
\]

Thus nonzero jumps, distinct event locations, and positivity of the underlying units do not establish a nonzero weighted truncation difference. The coefficients have both signs; adjacent dyadic indices can have precisely the valuations allowing cancellation. KK's largest-index valuation argument depends on a separation and coefficient pattern not supplied here.

The exact available route is now explicit: starting from (2), or a proved further difference, obtain a representation with a uniformly bounded number of S-unit terms, coefficients in a fixed finite set, error at most 3^B exp(−T−ηQ), and a proof that at least one such error is nonzero. Bound (5) would then supply the arithmetic height input. The present discrete returns, count identities, and mixed color renewal do not establish those three requirements.

### Gaps

- No applicable general irrationality theorem for this weighted minimum of unbounded color cocycles was found.
- No sparse-return theorem for J, or another nonlinear difference that replaces it, has been proved. The interior witness does not prove such a theorem impossible.
- No claim of novelty or solution to #168(ii) is made. No Lean formalization, new dependency, external submission, or extra decimal computation was attempted.

