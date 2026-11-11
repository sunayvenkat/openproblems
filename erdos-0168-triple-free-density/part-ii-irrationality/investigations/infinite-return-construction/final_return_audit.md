# Final independent audit of the infinite-return construction

Audit date: 7 November 2026. This audit independently reconstructs the new arguments in diophantine_supply.md, skew_denominator.md, and weighted_returns.md, using their established definitions. The completed global finite formula (C) is an input, as established in the current finite report; earlier conditional-C status is superseded. This is an ordinary mathematical audit, without Lean or external priority certification.

**Overall verdict: PASS for the principal auxiliary results, with the explicit corrections below; FAIL for completion of the requested adequate infinite weighted return.** The new results do not currently produce a fixed-term, arithmetically controlled, nonzero remainder with a fixed exponential improvement. In particular, the gap is larger than nonvanishing alone.

## Do the Diophantine supply and prefix obstructions survive independent review?

### Takeaway

**PASS.** The bounded-gap constant \(\varphi\), the improved sharp constant \(C_*=(15+\sqrt5)/10\), the transcendental sharpness construction, and the two prefix obstructions have valid proofs. They give genuine information for \(\alpha=\log_3 2\), but not an adequate sequence for the current scalar model. Its original \(5+\delta\) sufficient condition can be weakened by integer discreteness, as detailed in the final section.

### Cited Findings

- The audited statements, conventions, and elementary derivations are in [diophantine_supply.md](diophantine_supply.md). The original rational model and its corrected admissible interval \(3/5<p/q<2/3\) are in [returns.md](../../early-attacks/augmentation-and-return-attacks/returns.md) and its [independent audit](../global-boundary-proof/independent_audit.md).
- Elsner's Proposition 2.1, printed page 27, applies to every irrational and every odd prime: in six consecutive convergents there is a Hurwitz-quality approximant whose denominator avoids that prime. It is not a metric assertion. This attribution was checked directly in the [primary paper](https://www.fq.math.ca/Scanned/38-1/elsner.pdf).
- The Gelfond-Schneider theorem used to establish transcendence of the logarithmic ratio is stated as Theorem 10 in [Soundararajan's course notes](https://math.stanford.edu/~ksound/TransNotes.pdf). Irrationality itself follows from unique factorization: \(3^p=2^q\) is impossible for positive integers \(p,q\).
- Bounded partial quotients are compatible with transcendence, as discussed and exemplified in [Adamczewski, Bugeaud, and Davison](https://arxiv.org/pdf/math/0511682). The particular sharp constant here is the local note's own theorem, not a result attributed to that paper.

### Inferences

**1. PASS: one good ratio above \(\varphi\) in every four indices.** Set \(s_n=p_n+q_n\bmod3\), and call \(s_n\ne0\) good. Consecutive resonances are impossible by the determinant identity. If every good ratio \(r_i=q_{i+1}/q_i\) in a four-index block were at most \(\varphi\), each corresponding outgoing digit would be 1. Two consecutive good indices would then give
\[
r_{i+1}=1+1/r_i>\varphi,
\]
because the rational \(r_i\) cannot equal \(\varphi\). Consequently statuses would alternate. Each alternating four-index word has an interior good index preceded by a resonance; its outgoing digit 1 makes the following sum nonzero, contradicting alternation. The displayed three-index counterexample is exact: the two good ratios \(37/29\) and \(140/103\) are below \(\varphi\). Thus the block length four cannot be reduced to three.

The constant itself is sharp for arbitrary irrational slopes: an eventually all-1 continued fraction has \(r_n\to\varphi\), so no larger universal constant is possible.

**2. PASS: infinitely many good ratios above \(C_*\) if the digit tail is not all ones.** If a good outgoing digit is at least 2 infinitely often, the conclusion is immediate. Otherwise all sufficiently late good outgoing digits are 1. There must be resonances in this tail, and the sum recurrence forces the pattern \(0,c,c,2c,0\); resonances are exactly four apart. If \(R\) is a resonant ratio, the three intervening good ratios are
\[
1+1/R,\qquad 2-\frac1{R+1},\qquad \frac{3R+2}{2R+1}.
\]
The next resonant ratio is \(T_k(R)=k+(2R+1)/(3R+2)\). The map \(T_1\) is increasing and fixes \(\varphi\). Following a first digit \(k\ge2\), all resonant ratios exceed \(\varphi\); at each later such digit they exceed \(T_2(\varphi)=\varphi^2\). The middle good ratio therefore exceeds \(2-1/(\varphi^2+1)=C_*\) infinitely often.

An eventually all-1 tail gives a quadratic irrational. Gelfond-Schneider and the rational-power argument establish that the actual \(\alpha\) is transcendental. Therefore \(\alpha\) satisfies the improved supply theorem. Its implication is an infinite sequence above \(C_*\), not above 2, 3, or 5.

**3. PASS: sharpness even within transcendental slopes.** The initial six 1 digits put a resonance at \(8/13\). The blocks \((k,1,1,1)\), with \(k=2\) at factorial block indices and \(k=1\) otherwise, preserve the four-step resonance pattern. The derivative \(T_1'(R)=1/(3R+2)^2\) gives uniform contraction above \(\varphi\). The increasing spike gaps imply incoming ratios tend to \(\varphi\), spike ratios tend to \(\varphi^2\), and the good-index limsup is exactly \(C_*\).

The transcendence proof also passes, including the nonzero-resultant point. If \(m_j\) is the position of a spike, replace the subsequent tail by all 1s. The approximant \(\xi_j\) is quadratic and has an irreducible integer polynomial of height \(O(q_{m_j}^2)\le O(9^{m_j})\). The true number and this approximant agree through the next spike minus one, so their distance is \(O(2^{-m_{j+1}})\), while \(m_{j+1}/m_j\to\infty\). If the true number had fixed algebraic degree \(d\), the integer resultant and the mean value theorem would force a lower bound \(cH(P_j)^{-d}\), a contradiction. The other quadratic root comes from the negative conjugate of the all-1 complete quotient; the fractional linear map is injective and cannot put that root inside the same positive-tail cylinder. Thus the resultant is nonzero even if the hypothesized degree were 2.

This disproves a stronger universal conclusion from transcendence alone. It says nothing negative about a stronger property specific to \(\log_3 2\).

**4. PASS: semiconvergents and arbitrary intercepts do not enlarge this origin prefix.** A proper intermediate fraction \(u/v=(kp_n+p_{n-1})/(kq_n+q_{n-1})\) first meets the intervening Farey threshold at denominator \(v+q_n\). Its normalized window is \(1+q_n/v<2\), aside from initial indexing exceptions already excluded in the note.

For the intercept argument, \(N=q+q'\) and \(r=q_{n-1}\) satisfy \(N-r=(a_{n+1}+1)q\). Every real intercept gives the exact rational-model difference \((a_{n+1}+1)p\), whereas the true floor difference is this integer plus or minus 1. Both rational arguments are non-ties because \(q\ge2\) and consecutive denominators are coprime. The obstruction survives reducing floors modulo 3 because the three values of \(S\) are distinct. It rules out improving the full original prefix with an intercept; it does not rule out a genuinely shifted true-phase construction.

**5. PASS: Elsner's transformed application.** For \(\eta=1/(1+\alpha)\), the corresponding convergents are \(q_n/(p_n+q_n)\). Avoiding denominator divisibility by 3 is exactly nonresonance. The error transformation has prefactor \(u/(\eta v)\to1\), as stated. Hence every \(c>1/\sqrt5\) gives infinitely many nonresonant convergents with error \(<c/q_n^2\). No jump above 5 follows.

**6. PASS with an exact scale clarification: paired periods.** The guaranteed common horizontal period of the two prescribed models is the least common multiple \(3q_nq_{n+1}\). Its logarithmic cost is of order \(q_nq_{n+1}\), while their established matching length is of order \(q_n+q_{n+1}\). Describing this cost as quadratic in one current scale presupposes comparable denominators; the exact product statement is preferable. A special cancellation is not excluded.

**7. PASS: resonance itself has no transcendence-only infinite supply.** Here is a separate audit countermodel, following the same elementary quadratic-approximation method. Start with five 1 digits, whose last two convergent sums are \(2,1\bmod3\). Write \(t=s_{n-1}/s_n\) in \(\mathbb F_3\). From \(t=2\), digit 3 preserves \(t=2\), and the digit block \((2,1)\) takes \(2\to1\to2\), with no zero sum at either step. Append blocks consisting of a single 3, except at factorial block indices where the block is \((2,1)\). No subsequent convergent is resonant, and every outgoing ratio is below 4.

This number is transcendental: replace the tail after one sparse exceptional block by all 3s, using complete quotient \((3+\sqrt{13})/2\). The resulting quadratic polynomial has height \(O(16^{m_j})\), the next-disagreement distance is \(O(2^{-m_{j+1}})\), and \(m_{j+1}/m_j\to\infty\); the same nonzero-resultant argument applies. Its initial cylinder lies inside \((3/5,2/3)\). Therefore a scheme combining an arbitrary resonant-only improvement with the old nonresonant threshold 5 still needs an extra property of the actual logarithmic slope. This countermodel is not the actual slope.

### Gaps

- None of these results proves infinitely many actual nonresonant jumps above \(5+\delta\), or the weaker condition \(q'-5q\to+\infty\) sufficient for the discreteness argument below.
- The interface \(\gamma<1+C_*=(25+\sqrt5)/10\) is valid only after a replacement construction has independently supplied its fixed-term arithmetic form, height, minimum-unit scale, error, and nonvanishing. At equality, strict ratios tending to \(C_*\) give no fixed exponential margin.
- The actual slope's infinite resonant supply is not supplied by generic irrationality or transcendence.

## Do skew covariance, coupled swaps, and the interior operator give a global arithmetic reduction?

### Takeaway

**PASS for the exact identities and their stated limited scope. FAIL for an automatic scalar denominator reduction, a general finite-module closure, or a direct arithmetic interpretation of the retained side strips.** The same-color Hessian is essential. The independently reconstructed \(53/84\) model really has reduced denominator \(D/6\).

### Cited Findings

- The exact affine-center proof, lattice partitions, low-column failures, and denominator examples are in [skew_denominator.md](skew_denominator.md); the count-state and insertion conventions come from [arithmetic.md](../boundary-and-arithmetic/arithmetic.md) and [arithmetic_review.md](../boundary-and-arithmetic/arithmetic_review.md).
- The joint response, translation obstruction, periodic resolvents, and all retained terms in the interior identity are in [weighted_returns.md](weighted_returns.md).
- The final follow-ups are [ray_return_attack.md](ray_return_attack.md) and [resonant_models.md](resonant_models.md). Their mathematical claims were independently reconstructed for this audit; the two specifically requested resonant evaluations were also reproduced by the [targeted certificate](resonant_models_check.py).
- The saved model values used for comparison are in [returns_check.json](../../early-attacks/augmentation-and-return-attacks/returns_check.json). This audit additionally reconstructed the \(53/84\) value independently, rather than only reducing the saved fraction.
- The cited [Luca-Ouaknine-Worrell paper](https://people.mpi-sws.org/~joel/publications/hecke-mahler25.pdf) treats polynomial floor readouts and a separately stated recurrence/sparse-difference condition. Those hypotheses do not automatically cover a ray readout of an accumulated planar state.

### Inferences

**1. PASS: the two affine centers and every lattice tie.** The floor-sum expressions for \(A_a,B_b\) give the stated rotated remainders. The two Beatty-type finite sets partition \(\{1,\ldots,p+q-2\}\), with their one-sided endpoint contributions handled separately. Substitution yields exactly the two centers
\[
K=(1-\omega)/3\quad\hbox{or}\quad K=(2+\omega)/3
\]
in the four cases of the center table. The correction vector satisfies \(E_{b+p}=\rho^{-1}E_b\) for \(b\ge4\). Hence the full corrected state rotates about \(K\) under \((q,2p)\).

For the first center, the three integer cone tests are
\[
x\le\min(0,y),\quad y\ge0,\ x\ge1,\quad y\le-1,\ x\ge y+1.
\]
For the second, the last two tests become \(y\ge1,x\ge1\) and \(y\le0,x\ge y+1\). Each list partitions the whole integer lattice. Thus the high-column skew identity includes all closed-cone ties, and the corresponding three coefficients sum to zero. The low-column counterexamples at columns 0, 1, and 3 are legitimate failures of extending this theorem to the full array. No column-2 generalization is needed.

**2. PASS: joint Fourier zeros do not force scalar factor cancellation.** The skew relation gives \(T(1,1)=T(\omega,\omega)=T(\omega^2,\omega^2)=0\). These joint zeros do not imply a zero polynomial at any fixed horizontal or vertical root. The explicit alphabet-\(\{1,-2\}\) counterexample has nonzero evaluations at all relevant univariate roots, so the claimed automatic cancellation is false.

For the actual prescribed \(p/q=53/84\) rational model, this audit computed the axis states, the residue correction from its product formula, and all low/high coefficients afresh. It summed the finite tile using integer weights. With \(P=3q,Q=3p,U=2^P,V=3^Q\), it obtained
\[
D=27(U-1)(V-1),\qquad \gcd(N,D)=6.
\]
The reconstructed \(N/D\) equals the saved exact value. The nominal and reduced denominator bit lengths are 509 and 507. This is a narrow exact certificate, not a density decimal or an infinite-sequence argument. It rules out universal cancellation of the claimed large horizontal or vertical factors; it cannot exclude a special infinite subsequence.

**3. PASS: joint swap response, including the diagonal.** With \(m(Q)=\min Q_i\), assigning the changed increments to the same physical vertices gives
\[
\Delta\sum \eta/d=D_iD_jm(Q)(1/d_1-1/d_2).
\]
For \(i\ne j\), the Hessian is \(1_{Q_i=Q_j<Q_k}\). For \(i=j\), it is \(-1_{Q_i+1=\min(Q_j,Q_k)}\). Both formulas follow directly from the minimum. This audit independently checked all nine ordered pairs in the 27 states \(\{-1,0,1\}^3\), including their physical weight assignments. All 243 checks passed.

The diagonal term is substantive: for \(Q=(0,1,2)\), two color-0 insertions exchange the increments 1 and 0 between physical vertices. Therefore a same-color or resonant crossing is not invisible to reciprocal weights. The formulas require that the correction indicators remain unchanged; low-row swaps retain their actual events. For a finite reordering, the Hessian must be evaluated in the current adjacent-swap context. No argument is supplied for replacing those contexts by one original state or summing all infinite swaps without convergence control.

**4. PASS: minimum identities; PASS only as a general-state obstruction for finite closure.** The third mixed difference is the triple-tie indicator. Expanding \(T_0T_1T_2m=m+1\) yields the partition into one, two, or three tied minima. On \(Q=(0,0,t)\), translates of \(H_{01}\) are the distinct steps \(1_{t+n\ge1}\). Their jump differences prove linear independence. This excludes a finite-dimensional space of state functions stable under all integer translations. It does not exclude finite identities after restriction to the actual axis paths, one tailored set of shifts, or finite state spaces of a particular rational model.

The artificial separated state \(Q(a,b)=(0,0,x_a)\) also has the claimed rational \(D_0m\) readout and potentially irrational \(H_{01}\) readout. Positive-square binary digits give an explicit irrational latter sum. This is a valid nonimplication for those abstract hypotheses. It is not a counterexample to a theorem exploiting further special structure of the actual rotation cocycle.

**5. PASS with wording correction: periodic weighted resolvents.** The formula for the unique periodic solution of \(h_a=2G_a-G_{a+1}\) is correct and gives \(\sum h_a2^{-a}=2G_0\). It supplies the common denominator \(2^P-1\), and the two-variable resolvent supplies a common denominator \((2^P-1)(3^Q-1)\). Their numerators contain the weighted period data.

Do not read “retains the whole period denominator” as an assertion that every reduced denominator is exactly that common denominator. For example, \(h_a=1\) gives \(G_a=1\) and cancels it completely. The justified conclusion is that writing a resolvent does not itself prove any cancellation or small numerator. Exact full-scale denominator retention has separately been established for the \(53/84\) scalar model.

**6. PASS: finite-defect complexity does not itself compress the weighted response.** In a fixed interval \(1\le n\le Cq\), only boundedly many rational-grid residues can cross the relevant floor boundary, yielding the stated \(O_C(1)\) mismatch count. Exact ties are handled by the one-sided convention once \(q'>C\). Each defect can shift every subsequent accumulated state. Thus finitely many defects can still produce entire weighted ray local-time series.

The paired factor bound \(O(2^{-f}/q)\), or its \(q'\) version, gives no unconditional fixed exponential margin. This is an upper-bound statement, not a lower bound excluding exceptionally closer pairs. It must not be promoted into an impossibility theorem for a special sequence with unusually large next denominator or an additional exact cancellation. Variable exponential-height tile numerators likewise defeat the cited fixed-coefficient application as presently formulated; they do not establish that every more refined arithmetic treatment is impossible.

**7. PASS: the degree-two operator with every retained side.** For \(b\ge4\), the skew relation indeed gives
\[
\widetilde c(a+2q,b)+\widetilde c(a+q,b+p)+\widetilde c(a,b+2p)=0.
\]
For \(d(a,b)=c(a,b+4)\), \(u=2^q,v=3^p\), direct index shifts give exactly
\[
(u^2+uv+v^2)D
=u^2H_{2q}+uvH_q+uvV_p+v^2V_{2p}-uvR
+\sum_{a,b\ge0}\frac{Ld(a,b)}{2^a3^b}.
\]
Here \(uvR\) is integral, but all four displayed strip values are still semi-infinite real sums. The original total additionally retains the four low rows and \(D/81\). No low row or corner sign has disappeared.

The matching rectangle gives \(Ld=0\) for \(a<q'-q,\ b<p'-p-4\) when these bounds are positive. Since \(|Ld|\le6\), summing the complementary geometric strips proves the constant-18 bound (W12). It is a valid estimate for a real residual. Neither that estimate nor the small formal weight \(u^2+uv+v^2\) makes the right side an arithmetic linear form with controlled rational coefficients.

**8. PASS: actual-cocycle escape and bounded fixed-raw-winner persistence.** The follow-up [ray_return_attack.md](ray_return_attack.md) has a valid actual-rotation argument, including its discontinuity step. If one fixed raw color minimizes the adjusted counts at \(T,T+\log2,T+2\log2\), rotate that color to 0 and write \(W(T)=x+y\omega\). The adjusted cone inequalities are \(x\le1,\ x-y\le1\). Each strip error has both of these integer linear forms bounded in absolute value by 1. The next two rotated tests consequently give
\[
-2\le x\le1,\qquad -2\le y\le3,\qquad |W(T)|\le5.
\]
The indicators need not remain constant for this conclusion.

Direct iteration gives \(W(T+3n\log2)-W(T)=\sum_{k<n}\Phi(x_0+k\alpha)\), with \(x_0=T/(3\log3)\bmod1\). The established Kesten reduction is genuinely for \(W(2^{3m})\), not merely for a different sampling of cutoffs; therefore its unboundedness supplies phase-zero unboundedness of this precise cocycle.

If one phase had all prefixes bounded by \(M\), subtracting its prefixes would bound every forward orbit-start prefix by \(2M\). For each fixed length, phase 0 lies in a continuity cell of the prefix sum: \(k\alpha\) never meets any of the displayed rational-affine breakpoints, since that would make \(\alpha\) rational. Density would then bound every phase-zero prefix by \(2M\), a contradiction. Every phase therefore has unbounded prefixes.

The upgrade to uniform finite escape also passes. A sequence of phases with arbitrarily long bounded prefixes has a convergent subsequence approaching its limit consistently from one side, or equal to the limit. Each fixed prefix converges to that one-sided itinerary. Along one irrational orbit each of the finitely many breakpoints is met at most once. The one-sided itinerary thus differs from the specified endpoint code at at most nine times, with uniformly bounded total discrepancy for all prefix lengths. It would give an actual phase with bounded prefixes, contradicting the preceding paragraph. Endpoint limits do not invalidate compactness here.

It follows that for each \(M\) there is finite \(N(M)\) forcing escape above \(M\) from every phase. Applying this with \(M=10\) proves the stated fixed-raw-winner bound \(L<(3N(10)+2)\log2\). This is non-effective and depends on the fixed slope. It does not constrain a winner that rotates in a co-rotating frame or switches between the sample cutoffs.

**9. PASS: resonant drifts and a genuine single-diagonal rational generating function.** In [resonant_models.md](resonant_models.md), \(p+q=0\bmod3\) implies \(q\ne0\bmod3\). The permutation of \(rk\bmod q\), for \(p+q=3r\), evaluates the complete floor sum; retaining the one-sided endpoint gives exactly the four rows of the drift table. The Beatty partition supplies \(\omega H_A+H_B=\sigma(1-\omega)\), and the definitions indeed give
\[
h_A-h_B=\sigma,\qquad d_A-d_B=3\sigma.
\]
The sign is a difference, not a sum. The harmonic term in the \(q\)-by-\(p\) block formula is necessary and correctly retained.

The positive block shift \(T=(q,2p)\) for \(\sigma=+1\), or \(T=(2q,p)\) for \(\sigma=-1\), adds exactly \(\omega^q\) to the corrected state. It does not make that state periodic. Its cone increment is nonnegative and has precisely the line support stated in (R6).

The two rational cone formulas follow by summing \(j\ge\max(0,2i+x,\lceil(i+d)/2\rceil)\), or \(0\le j\le\min(2i-x,\lfloor(i-d)/2\rfloor)\), and then summing the geometric tails. The other two drift cases exchange the block coordinates. Both cutoff formulas are sufficient, including the floor/parity term in the upper-cone tail.

For the positive-shift difference, the cone-line conditions together bound both nonnegative block coordinates. In the first case, \(i=1-d+2j\) and \(j\le(2d-x-2)/3\); when \(|x|,|d|\le M\), this gives \(j\le M-1,\ i\le3M-1\). The remaining cases exchange coordinates or the two cone forms. Thus the high interior difference really has finite support. On the starting strips, all high and low digit tests become constant after finitely many blocks, uniformly over the finitely many residues. The coordinate differences kill their constant tails. Consequently
\[
f(U,V)=\frac{P_0(U,V)}
 {(1-U)(1-V)(1-U^{T_a}V^{T_b})}
\]
with integer polynomial \(P_0\) is valid. This is a genuine resonant reduction, distinct from the invalid nonresonant cancellation shortcut.

The conservative bounds \(A_*=3q(3M+4)+1,\ B_*=3p(3M+4)+4\) contain the finite differences and their starting-strip terms. Substitution at \(U=1/2,V=1/3\) gives the valid clearing factor \(D_*=S(W-1)\), where \(S=2^{A_*}3^{B_*}\) and \(W=2^{T_a}3^{T_b}\), and the height bound \(H(N_*:SW:S)\le6SW\). These are bounds with the full preperiod cost, not a cost-three denominator theorem.

The reproduced exact reduced denominators are
\[
\begin{array}{c|c}
7/11&2^{13}3^5(2^{22}3^7-1)\\
8/13&2^{29}3^{24}(2^{13}3^{16}-1)/7.
\end{array}
\]
The corresponding first floor-disagreement rectangles are \((19,12)\) and \((8,5)\); these two slopes are not consecutive-convergent models for the actual logarithm. Their finite evidence supports the exact evaluations and the need to include the S-costs, not an infinite construction.

Two terminology qualifications avoid overstatement. The non-S reduced denominator is a divisor of \(W-1\), not necessarily exactly \(W-1\), as the division by 7 shows. Also “primitive” refers to the \((1,2)\) or \((2,1)\) shift in the \(q\)-by-\(p\) block lattice; it need not be primitive in the full integer exponent lattice, and no irreducibility of the binomial is needed.

### Gaps

- There is no proved rationality transfer from the density to the actual ray, point, or side-strip constants.
- There is no fixed-term compression with sufficiently small coefficient heights and an adequate minimum-unit/error ratio.
- The obstruction results are architecture-specific logical limitations, not a proof that the requested weighted construction is impossible.

## Does the present work close the actual infinite-return goal?

### Takeaway

**FAIL: the required sufficient construction remains missing.** The arithmetic acceptance condition originally omitted the necessary cap \(t_L\le1\). That minimal correction and its linked erratum have now been applied to condition (15) in diophantine_supply.md. The existing model already uses \(t=1\), so the correction does not damage its conditional implication.

### Cited Findings

- The current finite input is the [completed prefix and phase report](../prefix-and-phase-audit/REPORT.md). This audit does not reopen that separate proof.
- KK Proposition 7.4 explicitly requires \(0<t\le\min(1,u_1,\ldots,u_m)\), fixed dimension and fixed rational coefficients. Its application separately uses nonvanishing and height/error estimates. These statements were checked directly in the [saved primary manuscript, sections 7.2-7.3](../Erdos%20theorem%20transfer%20investigation/erdos1062-fork-free-density.pdf.txt). The [upstream manuscript URL](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf) was unavailable to this audit's web fetch; the local saved primary text was readable.
- The fixed-term extension allowing subexponential integer multiplicities is proved in [coefficient_extension.md](../../early-attacks/augmentation-and-return-attacks/coefficient_extension.md), from the one-form Subspace Theorem in [Luca-Ouaknine-Worrell, Theorem 1](https://arxiv.org/html/2412.07908v2#S2.Thmtheorem1). The quoted covering theorem and its distinguished-index condition were checked against the primary source.
- For the new actual-rotation branch, [Kelly-Sadun, Theorem 1](https://arxiv.org/html/1404.0455) gives the cited interval bounded-remainder criterion. [Ralston, Theorem 1](https://arxiv.org/pdf/1106.0577) concerns one scalar half-interval discrepancy and its strictly heavy set. Both source attributions were checked; neither asserts the simultaneous two-inequality excursion required here.

### Inferences

**1. ORIGINAL DISPLAY FAIL; CORRECTION NOW APPLIED: condition (15)'s missing cap.** The sufficient target is
\[
0<t_L\le\min(1,u_{1,L},\ldots,u_{m,L}),\qquad
H(N_L:u_L)\le e^{CL},\qquad
0<|E_L|\le t_Le^{-\varepsilon_0L},
\]
with fixed term count, fixed rational coefficients (or the justified fixed-term multiplicity extension), positive fixed \(\varepsilon_0\), and unbounded \(L\). This correction supersedes the uncapped display (15).

The omission is material for a general interface. Take \(u_L=2^L,\ N_L=2^L-1,\ E_L=1,\ t_L=2^L\). For any \(0<\varepsilon_0<\log2\), the uncapped inequalities and an exponential height bound hold for every positive integer \(L\). They give no contradiction. The mandatory cap excludes this example. The scalar periodic model uses \(t=1\) and is unaffected.

**2. PASS WITH A SHARPER SUFFICIENT CONDITION: the scalar model.** Its clearing cost is \(6q\log2+O(1)\). The improved rectangle tail is
\[
|Z-\widetilde Z|
\le9\{2^{-(q+q')}+3^{-(p+p')}-2^{-(q+q')}3^{-(p+p')}\}.
\]
Removing the older logarithmic factor does not change the fixed exponential comparison. Nonresonance together with \(q'/q>5+\delta\) for fixed \(\delta>0\) remains sufficient, but is not necessary for this integer-cleared architecture. Indeed,
\[
(U-1)(V-1)=2^{6q}(1+o(1)),\qquad
3^{-(p+p')}=2^{-(q+q')}(1+o(1)),
\]
because the two convergent logarithmic errors tend to zero. The rectangle bound therefore gives
\[
|DZ-N|\le486(1+o(1))\,2^{5q-q'}.
\]
Thus any infinite nonresonant sequence with \(q'-5q\to+\infty\) has cleared error tending to zero. In particular, infinitely many nonresonant indices with next partial quotient \(a_{n+1}\ge5\) suffice, since
\[
q'-5q=(a_{n+1}-5)q+q_{n-1}\ge q_{n-1}\to\infty.
\]
This sharper sufficient condition follows from the existing exact rectangular estimate; a fixed ratio margin is unnecessary here.

The reason is rational discreteness: if \(Z=A/B\), then \(DZ-N\in B^{-1}\mathbb Z\), so an error tending to zero is eventually zero. Proposition 7.4 adds no strength at this step. Its more flexible scale is relevant to a genuinely different return with nonintegral S-unit coordinates. No infinite supply of these actual nonresonant indices is established. Even if it were, rationality would force eventual equality \(Z=\widetilde Z\), and proving that the associated model values do not eventually stabilize remains a separate obligation.

**3. PASS: coefficient growth needs a quantitative statement.** At fixed term count, the derived extension loses a power \(B^{m+\epsilon}\). Consequently \(B=e^{o(L)}\) can be absorbed into a genuine fixed exponential margin. An unbounded term count is not justified by that result. Exponential-height coefficients are not automatically admissible, but should be rejected by the actual loss calculation rather than by an assertion that variable coefficients are always forbidden.

**4. Exact consequence for the actual logarithm.** Formula (C) now makes the cone readout unconditional in its audited domain. There are infinitely many nonresonant convergents with ratio above \(C_*\), with the exact prefix-matching windows stated above. The high-column rational models satisfy the skew operator, and the actual model-comparison residual obeys (W12). What has not been obtained is an infinite sequence of fixed-term rational-coefficient weighted returns with the capped minimum-unit scale, controlled height, a fixed exponential improvement, and nonzero error. The open irrationality target has not been proved.

**5. PASS with a weaker discreteness alternative: finite-head excursion arithmetic.** In [ray_return_attack.md](ray_return_attack.md), the true head through \(e^{T_0}\) has denominator dividing \(\Lambda=2^{\lfloor T_0/\log2\rfloor}3^{\lfloor T_0/\log3\rfloor}\), with \(\log\Lambda=2T_0+O(1)\). Assuming a uniformly bounded model with fixed rational total denominator, a matching window of logarithmic length \(L\) gives a cleared error bounded by \(C(T_0+L+1)e^{T_0-L}\), as stated. The fixed exponential condition \(L-T_0\ge\eta L\) is sufficient for that bound.

As in the scalar model, integer discreteness permits the weaker sufficient condition
\[
(T_0+L+1)e^{T_0-L}\to0,
\quad\hbox{equivalently}\quad
L-T_0-\log(T_0+L+1)\to+\infty.
\]
Merely \(L-T_0\to\infty\) does not suffice for the displayed bound unless its logarithmic prefactor is also absorbed. For example, \(T_0=L-\tfrac12\log L\) makes that gap tend to infinity but does not make the bound tend to zero.

This arithmetic alternative does not construct the excursion or establish nonstabilization. Fixed raw winners are ruled out by the valid escape theorem. No suitable rotating winner, exact weighted switch description, or controlled starting-time relation has been supplied. The ray note correctly reports failure to produce an adequate return.

**6. PASS for the resonant criterion; FAIL for an adequate infinite supply.** The resonant construction correctly retains \(S\) in
\[
E=ZSW-ZS-N_*.
\]
Both units are integers at least 1, so \(t=1\) is admissible. Dividing by \(S\) makes the integer term nonintegral; expanding that term into small units must pay their minimum-unit scale. The exact sufficient comparison is \(D_*(2^{-R}+3^{-S_{\rm win}})\to0\), where \(S_{\rm win}\) denotes the vertical matching length, to distinguish it from the preperiod factor \(S\).

The bare diagonal factor has logarithmic cost \(3q\log2+o(q)\) along convergents. The actual clearing cost includes the additional powers of 2 and 3, currently controlled only in terms of the base-state intercept bound \(M\). Those costs cannot be omitted on the basis of the bounded drift table. The countermodel in the first section independently defeats any claimed generic infinite resonant supply. There is no actual-logarithm supply plus denominator/error plus nonstabilization package satisfying the return goal.

### Gaps

- Both final follow-ups have been checked. The ray result is a valid fixed-raw-winner obstruction; the resonant result is a valid rational architecture with uncontrolled full cost. Neither closes the infinite-return goal.
- A finite-state or period-matrix representation alone does not bound the number of scalar arithmetic coordinates independently of \(q\), prove fixed coefficients, remove axis/preperiod factors, or establish the needed minimum-unit scale.
- No Lean, installation, broad search, optimization sweep, external posting, or new density decimal was performed. This audit file and the specifically authorized scale-cap erratum in the current diophantine note are the only files edited by this auditor. The narrow checks reconstructed one specified nonresonant rational model, checked local swap formulas, and reproduced the two named resonant evaluations; none is enumeration promoted to an infinite theorem.
