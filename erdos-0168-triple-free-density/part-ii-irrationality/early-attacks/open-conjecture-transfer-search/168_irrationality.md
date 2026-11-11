# Checkpoint: #168 exact-formula candidate and irrationality obstruction

Status: **neither #168(ii) nor the candidate exact finite formula has been proved**. The two outstanding obligations are (1) a combinatorial lower bound on cover size matching the candidate and (2) an irrationality argument for the resulting density. This note preserves the research; it does not mark the goal complete.

The live target is [Conjectures.io #168(ii)](https://conjectures.io/problems/erdos168-erdos-168-parts-ii). Let F(N) be the largest size of a subset of [1,N] avoiding {n,2n,3n}. The target is irrationality of c=lim F(N)/N. Existence is known. The exact formal definition agrees with this statement: [source](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/168.lean).

## Finite reduction and candidate formula

Let

\[
D_t=\{(a,b)\in\mathbb Z_{\ge0}^2:2^a3^b\le t\},\qquad
K_j(t)=\#\{(a,b)\in D_t:a+2b\equiv j\pmod3\}.
\]

Every forbidden corner \(\{(a,b),(a+1,b),(a,b+1)\}\) has all three colors. Write τ(D_t) for the minimum vertex-cover size of these corners. If d_k are the increasing positive3-smooth numbers and f(k)=k−τ(D_{d_k}), then

\[
c=\frac13\sum_{k\ge1}\frac{f(k)-f(k-1)}{d_k}.
\]

This decomposition is classical; see [Veselinov's primary account](https://arxiv.org/html/2604.15515v1), which also gives f(k)=2k/3+O(√k), the increment-one property at pure2-powers, and the fact that each other insertion introduces only one new triangle. It does not resolve irrationality.

For t≥3 define e_j(t) to be1 in either of the following cases, and0 otherwise:

1. There is a power s=2^a with 2t/3<s≤t and j≡a(mod3).
2. There is a power x=2^a with 6x≤t<27x/4 and j≡a(mod3).

Each condition admits at most one power, and their ranges cannot overlap. The candidate is

\[
\boxed{\tau(D_t)=\min_{j=0,1,2}\bigl(K_j(t)-e_j(t)\bigr).}
\tag{C}
\]

For t<3, all available vertices can be retained. Formula(C) is established only as an upper bound on τ, because explicit covers realize its right side.

The first correction removes the only possible isolated vertex. For the second, put x=2s, s=2^a. In color j≡a+1(mod3), replace the cover vertices

\[
\{2s,9s,12s\}\quad\text{by}\quad\{3s,4s\}
\]

when12s≤t<27s/2. The incident-triangle check is exact. The triangle at9s/2, when that anchor is integral, is absent because its third vertex27s/2 exceeds t. Other potentially problematic descendants also exceed t. The remaining incident triangles contain3s or4s. This saves one cover vertex.

A reflected patch at the3-power axis does not work: removing4s for s=3^b, b≥1, leaves \(\{4s/3,8s/3,4s\}\) uncovered. All its vertices are already below the removed point.

For optional counting, let Ψ_{8,27}(y)=#{(u,v)≥0:8^u27^v≤y}. Then

\[
\begin{aligned}
K_0(t)&=\Psi_{8,27}(t)+\Psi_{8,27}(t/6)+\Psi_{8,27}(t/36),\\
K_1(t)&=\Psi_{8,27}(t/2)+\Psi_{8,27}(t/9)+\Psi_{8,27}(t/12),\\
K_2(t)&=\Psi_{8,27}(t/3)+\Psi_{8,27}(t/4)+\Psi_{8,27}(t/18).
\end{aligned}
\]

The offset products are all216, which cancels their principal asymptotic differences. Their discrepancies nevertheless are unbounded, as proved below.

## Exact arithmetic calculation, conditional on(C)

Ordering all positive3-smooth numbers≤10^100 by exact integer comparison gives35,084 prefixes. Formula(C)'s candidate increments are always0 or1 throughout this scan. Summing their reciprocal contributions as exact rational numbers gives

\[
\begin{split}
c_{\rm candidate}={}&0.80096575500655898909042032638808241322472498911028458781919045603644708044249630021895087751711466454827914033\ldots
\end{split}
\]

The established35-digit value from [OEIS A386439](https://oeis.org/A386439) is

\[
0.80096575500655898909042032638808241\ldots,
\]

and agrees. The extra digits are **conditional predictions**, not a proved extension of the known value.

The rigorous reciprocal-tail formula, valid independently of(C), is: if A=⌊log₂X⌋ and b_a=1+⌊log₃(X/2^a)⌋,

\[
\sum_{2^u3^v>X}2^{-u}3^{-v}
=\frac32\sum_{a=0}^{A}\frac1{2^a3^{b_a}}+\frac3{2^{A+1}}.
\]

At X=10^100, one third of this is

\[
1.0146360493534903669943679691865420514753276221870817123885957787126442156589998402141965174440977131970646094\times10^{-98}.
\]

Thus, *if(C) holds*, the displayed truncated rational sum differs from c by less than this amount. Code: [check_168_color_discrepancy.py](./check_168_color_discrepancy.py).

## What was tested and broken

- Descending greedy selects16 vertices at t=162, versus17 from the exact cover \(\{2,9,12,16,54,72,96\}\). [Check](./check_168_arithmetic.py), [output](./check_168_arithmetic.json).
- Uncorrected color classes fail there because they include isolated128.
- Correcting only isolated vertices fails at t=1536: all three classes have15 active vertices, but the set \(\{3,4,18,24,32,81,108,144,192,384,486,512,648,864\}\) covers all corners and has14 vertices. This is the second correction above.
- Sampled finite MILPs for k=3,10,20,30,40,50,70,100,150,200,300,500 give f(k)=2,7,14,21,27,34,48,67,101,134,201,334. Integer witnesses are checked exactly; floating-point solver bounds are not formal optimality certificates. [Samples](./check_168_arithmetic_samples.json).
- The graph agent reports all1,449 fetched published OEIS first-hit records agree with(C), spanning through k=5000/f=3335; its own notes contain the replay details.
- Local-exchange searches fix one color outside a strip along the sloped boundary and optimize the inside. At height40 and dyadic width parameter5, all42 cutoff ratios and all3 colors gave no extra improvement. At height120 and dyadic width parameter10, all122 cutoff ratios and all3 colors again gave no extra improvement. The latter366 solves all reported optimal status; no time limit or unknown status occurred. Exact rational cutoff ratios are normalized3-powers in[1,2); all candidate witnesses are checked by exact incidence. Width parameter H allows H+1 consecutive exponents per row. These are numerical MILP bounds, not an infinite proof. [Boundary-exchange search](./check_168_boundary_exchange.py), [status audit](./168_boundary_exchange_summary.json).

## Rigorous obstruction: the color spread is unbounded

Numerically, the first spreads1,2,3,4 appear respectively at t=1,8,34992,2^199·3^7. At the last value k=14096 and (K_0,K_1,K_2)=(4701,4697,4698). The maximum spread up to10^100 is4. [Exact record](./check_168_color_discrepancy.json).

The following argument proves unboundedness. It is a derived observation, with no claim to literature novelty.

Let β=log₂3, ω=e^{2πi/3}, t=2^{3m}, and B=⌊3m/β⌋. Summing along horizontal rows gives

\[
(1-\omega)\sum_{j=0}^2K_j(t)\omega^j
=\sum_{b=0}^B\omega^{-b}
-\omega\sum_{b=0}^B\omega^{-\lceil(\beta+1)b\rceil}.
\tag{1}
\]

This uses the exact last exponent a=3m−⌈βb⌉ on row b, including b=0. The first sum on the right is bounded.

Put θ=(β+1)/3. For b≥1, the summand in the second sum is ω²,ω,1 as {bθ} lies respectively in (0,1/3],(1/3,2/3],(2/3,1). No positive iterate is an endpoint because θ is irrational. If those complex sums were bounded, the discrepancy of the last third would be bounded: for the sum over b=1,…,B,

\[
\#\{1\le b\le B:\{b\theta\}\in(2/3,1)\}-B/3
=\frac23\operatorname{Re}\sum_{b=1}^B\omega^{-\lceil(\beta+1)b\rceil}.
\]

Kesten's theorem excludes this, since an interval for irrational rotation θ has bounded discrepancy only if its length belongs to Zθ+Z, whereas1/3∉Zθ+Z. The primary modern proof states the fixed-start formulation explicitly: [Kelly–Sadun, Theorem1](https://arxiv.org/html/1404.0455); [original Kesten article](https://geodesic.mathdoc.fr/articles/10.4064/aa-12-2-193-212/).

There is no hidden fixed-point-versus-almost-everywhere gap. If an interval discrepancy were bounded by C for all prefixes starting at0, its value for every orbit starting point {mθ} would be bounded by2C, by subtracting two prefixes. For each fixed length N, orbit points are dense and the discrepancy is piecewise constant with finitely many endpoint discontinuities. Consequently the same2C bound holds away from endpoints for every starting point, and an extra bounded endpoint allowance gives a uniform bound everywhere. Thus even an almost-everywhere bounded-remainder version of Kesten would apply.

Finally, B(m) has gaps at most2 because1<3/β<2. Boundedness on these sampled indices would imply boundedness at all indices. Equation(1) therefore forces the left side to be unbounded. Hence max K_j−min K_j is unbounded.

Since the three deviations K_j−|D_t|/3 sum to0, |D_t|/3−min K_j is also unbounded. The color construction gives

\[
f(|D_t|)-2|D_t|/3\ge |D_t|/3-\min_jK_j(t),
\]

so f(k)−2k/3 is unbounded. This does **not** contradict(C); it rules out a finite state consisting only of uniformly bounded color-count differences.

## Exact interface needed for the #1062 S-unit method

The reusable primary result is Kohlmeyer–Kruer Proposition7.4: for fixed m, d∈Q^m, and ε>0, there exists C>0 such that for every N∈Z, positive{2,3}-units u_i, and0<t≤min(1,u_i),

\[
0\ne E=\sum_{i=1}^m d_i u_i-N
\quad\Longrightarrow\quad
|E|\ge Ct\,H(N:u_1:\cdots:u_m)^{-\varepsilon}.
\]

It follows from the p-adic Subspace Theorem. Their #1062 proof constructs, under rationality, an infinite sequence of **fixed-dimension, fixed-coefficient** forms with units≥e^{−T}, height≤e^{27L}, and nonzero error≤e^{−T−L/200}. Their two finite-step rotation codings yield boundedly many return-event families; a 2-adic argument proves at least one of two truncations is nonzero. [Primary manuscript, §§6–7](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf).

For #168, a sufficient replacement would produce constants m,M,C,η>0, a finite set of coefficient vectors, and arbitrarily large L with

\[
u_i\ge e^{-T},\quad H(N:u)\le e^{CL},\quad
0<\left|\sum d_i u_i-N\right|\le e^{-T-\eta L},\quad m\le M.
\]

Pigeonhole fixes m and d, then choose ε<η/C. Neither the required return identity nor noncancellation is presently proved.

A useful elementary zero-cocycle lemma is available. If q≡0(mod3), gcd(p,q)=1, and |θ−p/q|<1/q², then the q points {bθ},1≤b≤q, put exactly q/3 points in each right-closed third. Nonboundary rational-grid points move less than1/q and cannot cross a third boundary. For positive displacement the three boundary points move cyclically, preserving all counts; for negative displacement they remain in their respective right-closed cells. Thus the complex three-color cocycle sums to0 over that block.

Ordinary continued-fraction convergence alone does not establish the denominator congruence and approximation quality in that sufficient lemma. However, the adjustable-phase replacement below does supply infinitely many balanced blocks. Denjoy–Koksma bounds alone are not being used to claim a zero offset or a finite-event identity.

Even proving the zero-block lemma for an infinite return sequence would still require transporting it through the minimum of the three color counts in(C), controlling boundary corrections, and proving a nonzero truncation. These are explicit unresolved steps, not routine omissions.

## Balanced return blocks at adjustable phases: the congruence gap is removed

An additional idea from the coordinator becomes a proved auxiliary lemma using a published restricted-approximation theorem.

**Elsner, Proposition2.1:** for an irrational η and an odd prime ℓ, among every six consecutive convergents there is u/v satisfying \(|\eta-u/v|<1/(\sqrt5 v^2)\) with ℓ∤v. [Carsten Elsner, *On Diophantine Approximations with Rationals Restricted by Arithmetical Conditions*, Fibonacci Quarterly38(1),2000, printed p27](https://www.fq.math.ca/Scanned/38-1/elsner.pdf).

Apply this with η=1/(3θ)>0 and ℓ=3. Invert the resulting positive approximants and put p=v,n=u. Then p≢0(mod3), and

\[
n^2\left|3\theta-\frac pn\right|
=\frac{u}{\eta v}\,v^2\left|\eta-\frac uv\right|.
\]

Since u/(ηv)→1, infinitely many such fractions satisfy \(|3\theta-p/n|<c/n^2\) for the fixed choice c=.46<1/2. Put δ=nθ−p/3; then |δ|<c/(3n).

Group a length3n orbit block into triples indexed by1≤k≤n:

\[
x+k\theta,\quad x+k\theta+p/3+\delta,\quad
x+k\theta+2p/3+2\delta\pmod1.
\]

The ideal offsets0,p/3,2p/3 visit all thirds because3∤p. Work modulo1/3. For δ>0 it is sufficient that x+kθ avoid the interval within2δ to the left of the third-boundary; for δ<0 use the interval within2|δ| to its right. Thus each k excludes a phase interval of length2|δ| on a circle of length1/3. The union excludes length at most2n|δ|<2c/3. Its complement has measure at least(1−2c)/3>0 and, because there are at most n excluded intervals, contains an interval of length at least(1−2c)/(3n). Its midpoint has a margin at least(1−2c)/(6n). At every phase in this complement, each triple has exactly one point in each third, so the complete3n-block has exactly n points in every third and zero complex color cocycle.

This establishes infinitely many balanced blocks at adjustable phases with a quantitative O(1/n) margin. The next section transports them to exact color-count returns and a long orbit segment. Bounding the number of S-unit event families and proving the necessary noncancellation remain unresolved, in addition to proving(C).

## Exact horizontal cocycle and a proved long orbit segment

This paragraph uses \(\alpha=\log2/\log3\) and \(\theta_h=(1+\alpha)/3\); this is different from the reciprocal slope θ in the Kesten calculation above. The preceding balanced-block theorem holds for every positive irrational θ, so it applies to θ_h.

Define

\[
W(T)=\sum_{j=0}^2\omega^jK_j(e^T),\qquad
S(B)=\sum_{b=0}^B\omega^{2b}.
\]

For T≥0, separating a=0 from a≥1 proves

\[
W(T+\log2)=\omega W(T)+S\!\left(\left\lfloor\frac{T+\log2}{\log3}\right\rfloor\right).
\]

Iterating and using Q≡0(mod3) yields the coordinator's exact identity

\[
R_Q(T):=W(T+Q\log2)-W(T)
=-\frac{\omega^2}{1-\omega^2}
\sum_{s=1}^{Q}\omega^{-\lfloor T/\log3+s(1+\alpha)\rfloor}.
\tag{2}
\]

To check the constant, the geometric-series expression for S gives a first sum Σ_{s=1}^Qω^{−s}=0; the other exponent2⌊T/log3+sα⌋−s is congruent modulo3 to−⌊T/log3+s(1+α)⌋.

Put h(x)=ω^{−⌊3x⌋}, periodically on R/Z, and B_Q(x)=Σ_{s=1}^Qh(x+sθ_h). Equation(2) is R_Q(T)=−ω²B_Q(T/(3log3))/(1−ω²). The key finite-jump derivative is

\[
B_Q(x+\theta_h)-B_Q(x)
=h(x+(Q+1)\theta_h)-h(x+\theta_h).
\tag{3}
\]

The phase shift x→x+θ_h corresponds exactly to T→T+log6.

Choose an Elsner approximant p/n from the preceding section for3θ_h, with c=.46 and Q=3n. The initial good-phase set on R/Z has measure at least1−2c=.08, and satisfies B_Q(x)=0. Set ε=Qθ_h−p, so |ε|<c/n. The right side of(3) is nonzero only when x+θ_h lies within a one-sided ε-neighborhood of one of the three discontinuities of h. Its exceptional set has measure at most3|ε|<3c/n.

For any M, a union bound shows that the phases where one of the first M derivatives is nonzero have measure at most3Mc/n. Taking

\[
M=\left\lfloor\frac{1-2c}{6c}n\right\rfloor
\]

leaves a set of measure at least(1−2c)/2>0 on which

\[
B_Q(x+k\theta_h)=0\quad(0\le k\le M).
\]

Consequently there is a continuous cutoff phase T_0, which can be increased by a multiple of3log3 to ensure T_0≥log6, such that

\[
W(T_0+k\log6+Q\log2)=W(T_0+k\log6)
\quad(0\le k\le M).
\tag{4}
\]

The phase sets involved are finite unions of intervals, so a phase away from all endpoints can be chosen. Here M is a fixed positive multiple of n asymptotically (approximately.02898n).

Equality of W forces all three integer color-count increments to be the same. Moreover e_j(2^Qt)=e_j(t) for t≥6 and Q≡0(mod3). Thus, *conditional on(C)*, the centered extremal function

\[
g(t)=f(|D_t|)-\tfrac23|D_t|
\]

satisfies

\[
g(2^Q6^ke^{T_0})=g(6^ke^{T_0})\quad(0\le k\le M).
\tag{5}
\]

This is an actual long orbit segment. It is still not the needed S-unit tail identity: (5) is an identity at discrete cutoffs, not throughout the intervening intervals, and alone does not control the reciprocal-weighted density tail. In particular, equal endpoint counts do not equate the sums of Δf(d)/d over intervals between consecutive6-power cutoffs: those intervals contain many mixed smooth jumps with different reciprocal weights. Growing event counts and noncancellation remain unresolved.

Finally, the coordinator's arbitrary-cutoff observation is valid after clearing one extra factor3. Put L(t)=2^{⌊log₂t⌋}3^{⌊log₃t⌋}. Every smooth d≤t divides L(t), so the density partial sum P(t)=(1/3)Σ_{d_k≤t}Δf(k)/d_k has denominator dividing3L(t). If qc∈Z, then3qL(t)(c−P(t)) is an integer for every real t≥1. Thus a cutoff need not be an integer or smooth number. This integrality alone gives no contradiction: its multiplier is of order t² while the uncancelled tail is of order at most(logt)/t. Return cancellation is still necessary.

Source-audit caution: Veselinov Proposition4.3 claims a sharp reciprocal-tail error O((logX)^{r−2}/X), but the displayed proof substitutes a counting estimate with error O((logX)^{r−1}) and retains an error O((logX)^{r−1}/X). Canceling the leading terms does not improve that error. This note relies on the exact two-prime geometric tail identity, not that unjustified sharper remainder.
