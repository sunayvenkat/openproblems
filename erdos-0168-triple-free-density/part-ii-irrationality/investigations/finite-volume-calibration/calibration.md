# Finite volume calibrations with fully paid sources

## Can a finite state volume be calibrated without an invariant phase partition?

### Takeaway

**Yes: an absorbing finite state box has a finite rational step Poisson solution on a sufficiently large common phase refinement.** This does not require an invariant finite phase partition. For the simplest positive-reward solution, however, its source denominator is at the actual first-exit scale and its positive cleared return cannot tend to zero. This is a scoped failure of a concrete calibration, not a theorem against all occupation bridges. — [Exact checker](calibration_check.py), [accepted actual skew product](../occupation-arithmetic-bridge/exact_transport.md).

### Cited Findings

- The actual horizontal process is \(Y_n=A_{3n}\), \(x_n=\{n\alpha\}\), \(\alpha=\log2/\log3\), with \(T(y,x)=(y+\Phi(x),\{x+\alpha\})\). The lifted positive measure \(\Omega=\sum_{n\ge0}8^{-n}\delta_{(Y_n,x_n)}\) obeys \(\Omega(8p-p\circ T)=8p(1,0)\) for every bounded test. — [ET1–ET2 and complete terminal terms](../occupation-arithmetic-bridge/exact_transport.md), [independent preceding audit](../occupation-arithmetic-bridge/transport_audit.md).
- The precise actual phase-zero process \(Y_n\) is unbounded. The preceding audit derives this from original colored-board sums and the fixed-start Kesten criterion. — [Actual support audit](../numerator-and-residuals/occupation_audit.md).
- The nine cuts of \(\Phi\) have the form \((k-s\alpha)/3\), \(s=1,2,3\), with three consecutive \(k\)'s for each \(s\). Refining for \(L\) steps gives exactly \(9L\) genuine cuts. — [ET9 and exact phase convention](../occupation-arithmetic-bridge/exact_transport.md).
- The new checker imports only the explicitly identified accepted exact transport helper. It adds the absorbing-volume tests, binary-source carry tests and the complete density-rectangle reductions below; it does not claim to be an independent reconstruction of that helper. — [Implementation](calibration_check.py).

### Inferences

**FC1. Every starting phase has an unbounded cocycle.** Write \(S_n(x)=\sum_{k<n}\Phi(x+k\alpha)\). If one \(S_n(x)\) were bounded by a fixed \(C\), then
\[
|S_n(x+m\alpha)|=|S_{n+m}(x)-S_m(x)|\le2C
\]
for all \(m,n\). For each fixed \(n\), \(S_n\) is continuous at phase zero: an equality \(k\alpha=(r-s\alpha)/3\pmod1\), with \(k\ge0,s\ge1\), would make \((3k+s)\alpha\) an integer. Density of the tail orbit therefore gives \(|S_n(0)|\le2C\) for every \(n\), contradicting the accepted actual unboundedness. Adding any fixed starting state does not change this conclusion. — [Accepted phase-zero input](../numerator-and-residuals/occupation_audit.md), [cut formula](../occupation-arithmetic-bridge/exact_transport.md).

**FC2. Uniform finite exit exists for each finite box.** Let \(K_R=\{x+y\omega:\max(|x|,|y|)\le R\}\), and let \(\tau_R(y,x)\) be the first time the state leaves \(K_R\). Each phase orbit hits at most one of the nine cuts of \(\Phi\): equality of two cuts along an orbit would force \(3m=s-s'\), hence \(s=s',m=0\), and then equality of the cuts themselves. Thus the left- and right-limit itineraries at any phase differ at at most one increment, and both are unbounded by FC1.

If no uniform exit horizon existed, choose arbitrarily long surviving orbits, pass to one fixed initial state in the finite \(K_R\), and take a subsequence of phases tending to a limit from one side. Every fixed prefix then stabilizes to the corresponding one-sided itinerary. It remains in \(K_R\) at every time, contradicting its unboundedness. Hence
\[
M_R:=\sup_{y\in K_R,x}\tau_R(y,x)<\infty.
\tag{FC1}
\]
This is not a quantitative escape-time estimate. The proof uses compactness of one-sided itineraries, not a nonexistent invariant finite partition. A depth-\(M_R\) common refinement suffices because all exit decisions are then determined. — [Exact finite refinement checker](calibration_check.py), [prior finite-partition limitation](../occupation-arithmetic-bridge/transport_audit.md).

**FC3. A complete killed Poisson calibration.** Take a bounded positive odd integer reward \(h(y,x)\), a finite step function in phase for each state; the concrete example is \(h=1+6F(y-1)\in\{1,7\}\). Define
\[
p_R(y,x)=\sum_{n<\tau_R(y,x)}8^{-n-1}h(T^n(y,x))
\quad(y\in K_R),\qquad p_R=0\quad(y\notin K_R).
\]
FC2 makes this a finite rational step function of phase on each state. Its coefficients have a common denominator dividing \(8^{M_R}\), and
\[
8p_R-p_R\circ T=h\quad\hbox{inside }K_R.
\]
The complete residual \(e_R=h-(8p_R-p_R\circ T)\) is zero inside and equals \(h+p_R\circ T>0\) outside. In particular \(0\le e_R\le8H/7\) if \(1\le h\le H\). The exact infinite identity is
\[
\boxed{\Omega(h)=8p_R(1,0)+\Omega(e_R).}
\tag{FC2}
\]
No phase guard or terminal term was dropped. This has a nonzero coefficient of the one-axis target readout, in contrast to the zero-bulk product resolvent. It does not by itself express that one-axis target as the density \(Z\). — [Accepted discounted identity](../occupation-arithmetic-bridge/exact_transport.md), [new exact finite-terminal tests](calibration_check.py).

Let \(\tau=\tau_R(1,0)\ge1\). The source is the actual finite head
\[
8p_R(1,0)=\sum_{n<\tau}8^{-n}h_n,
\qquad h_n=h(Y_n,x_n).
\]
Because the last \(h_{\tau-1}\) is odd, the reduced denominator of \(8p_R(1,0)\) is **exactly** \(D_R=8^{\tau-1}\); the reduced denominator of \(p_R(1,0)\) itself is \(8^\tau\). The positive residual contains its first exit contribution, so
\[
\Omega(e_R)\ge8^{-\tau},\qquad
\boxed{D_R\Omega(e_R)\ge1/8.}
\tag{FC3}
\]
Thus this calibration is not adequate even after full fraction reduction. Its source multiplier has \(\log_2D_R=3(\tau-1)\). The accepted quantitative bound \(R(Y_n)\le C(3n+1)^\kappa\), \(\kappa=K/(K+1)\), also forces \(\log D_R\ge cR^{1/\kappa}-O(1)\) at exit; this particular method reaches the critical first-arrival scale rather than the affordable subcritical budget. This is a multiplier statement only for the specified killed, positive odd reward source. — [Accepted quantitative state bound](../occupation-arithmetic-bridge/height_audit.md), [exact denominator tests](calibration_check.py).

The checker covers every initial state in \(K_1\) and every phase on a depth-256 common refinement, proving a finite exit bound of 232 there. Right-continuity means each cut has the same finite itinerary as its adjacent cell on the right, so endpoints are covered too. Actual source exits are \(\tau_1=2\), \(\tau_2=67\), giving denominators \(8\), \(8^{66}\) for \(8p_R(1,0)\), and \(8^2\), \(8^{67}\) for \(p_R(1,0)\). These examples check FC2–FC3; FC1 is proved for every finite box by the argument above, not extrapolated from them. — [Exact certificate](calibration_check.py).

### Gaps

- This calibration targets a one-axis discounted reward. Recovering the full density requires the vertical occupation and all low-row equations, which have not been eliminated. — [Complete product/readout distinction](../occupation-arithmetic-bridge/transport_audit.md).
- FC3 does not apply to arbitrary zero-one rewards, signed potentials, noncompact outer potentials or specially cancelled sources. The next section gives an explicit zero-one escape from its arithmetic premise. — [Exact carry tests](calibration_check.py).
- No global lower bound on an occupation-bridge multiplier is proved. Scalar phase cancellation criteria cannot be applied to state-conditioned coefficients without retaining the state flux. — [Accepted guard/state correlation audit](../occupation-arithmetic-bridge/guard_audit.md).

## Can the actual zero-one cone reward avoid the positive-odd cost obstruction?

### Takeaway

**Yes in principle: a rational noncompact boundary value permits exact base-eight source cancellations.** The resulting one-axis calibration is globally positive outside the state box. Adequacy reduces to a precise terminal-one-run condition that is not proved for the actual first-exit sequence, and the readout is still not the full density. — [Exact source/word checker](calibration_check.py).

### Cited Findings

- The actual cone reward used below is \(h(y)=F(y-1)\in\{0,1\}\); it is one of the actual readouts used in the independently certified guard/state correlation. No scalar factorization of that readout and its guard is valid. — [Actual cone correlation](../occupation-arithmetic-bridge/guard_audit.md).
- A finite absorbing volume can be solved on a larger common refinement by FC1. No invariant phase partition or rationality of an infinite guarded readout is used to define the finite source. — [FC1–FC2 and checker](calibration_check.py).

### Inferences

**FC4. A positive noncompact Dirichlet calibration.** Prescribe
\[
p_\infty(y,x)=\frac{1+h(y)}7\quad(y\notin K_R),
\]
and inside use the exact finite exit formula
\[
p_R(y,x)=\sum_{n<\tau_R}8^{-n-1}h(T^n(y,x))
+8^{-\tau_R}p_\infty(T^{\tau_R}(y,x)).
\tag{FC4}
\]
It is a finite rational step function inside and a bounded rational state function outside; \(0\le p_R\le2/7\). Inside, \((8I-T)p_R=h\). Outside, the complete residual in the opposite orientation is
\[
e_R=(8I-T)p_R-h=\frac{8+h(y)}7-p_R\circ T,
\qquad \frac67\le e_R\le\frac97.
\]
Consequently \(e_R\) is zero inside, positive on every outside point, and
\[
\boxed{8p_R(1,0)-\Omega(h)=\Omega(e_R)>0.}
\tag{FC5}
\]
This retains incoming boundary transitions as well as exits; it is not just a prescribed far-exterior sign. — [New exact Dirichlet/resolvent tests](calibration_check.py).

Let \(h_0,\ldots,h_\tau\) be the actual binary word through first exit. Define
\[
N_\tau=1+h_\tau+7\sum_{n<\tau}8^{\tau-1-n}h_n.
\]
The scaled calibration is
\[
\mathcal C_R:=7\Omega(e_R)
=\frac{N_\tau}{8^{\tau-1}}-7\Omega(h),
\qquad
6\,8^{-\tau}\le\mathcal C_R\le\frac{72}7\,8^{-\tau}.
\tag{FC6}
\]
Its exact source denominator is
\[
T_R=2^{[3(\tau-1)-v_2(N_\tau)]_+}.
\tag{FC7}
\]
Here the source is \(7\cdot8p_R(1,0)=56p_R(1,0)\), and its denominator is \(T_R\). The unscaled quantities are
\[
p_R(1,0)=\frac{N_\tau}{7\,8^\tau},\qquad
8p_R(1,0)=\frac{N_\tau}{7\,8^{\tau-1}}.
\]
Because \(N_\tau\equiv1+h_\tau\in\{1,2\}\pmod7\), the factor seven does not cancel: their exact reduced denominators are respectively
\[
7\,2^{[3\tau-v_2(N_\tau)]_+},\qquad 7T_R.
\]
This exposes genuine source cancellation instead of assuming the odd-reward conclusion; it also keeps the fixed denominator seven in every unscaled finite claim. — [Exact source arithmetic and all binary words through length nine](calibration_check.py).

**FC5. Exact carry classification.** Modulo eight,
\(N_\tau\equiv1+h_\tau-h_{\tau-1}\). If \(h_\tau=0\) and the preceding word ends in \(\ell\ge1\) consecutive ones, each such one carries through one entire base-eight digit. If \(\ell<\tau\), the next previous bit is zero, leaving a unit, so \(v_2(N_\tau)=3\ell\). If the whole prefix is ones, \(N_\tau=8^\tau\). In the other cases, \(v_2(N_\tau)=1\) for the transition \(0\to1\), and zero if the last two bits agree. These are exhaustive cases. — [Direct integer formula and exhaustive exact check](calibration_check.py).

It follows from the two-sided bound in FC6 that, along an unbounded sequence of exit times, adequate cleared calibrations in this ansatz occur exactly when a selected subsequence has unbounded terminal-one runs ending with \(h_\tau=0\). In that case \(T_R8^{-\tau}\) is between \(8^{-\ell-1}\) and \(8^{-\ell}\). Without such runs it stays bounded below. This is a conditional new route, not a proof that the actual exit words have the required runs. At the actual \(R=1,2\) exits, the denominators of \(56p_R(1,0)\) remain \(8\), \(8^{66}\); the denominators of \(8p_R(1,0)\) are \(56\), \(7\cdot8^{66}\). Thus these tested volumes do not provide the saving. — [Actual cone and carry certificates](calibration_check.py).

### Gaps

- No unbounded terminal-run theorem is proved for these actual state-box exits. A nonconstant orbit word need not have unbounded runs; neither transcendence nor the old guard supply proves this condition. — [Actual versus guard supply distinction](../occupation-arithmetic-bridge/guard_audit.md).
- Even an adequate one-axis calibration would need a proved target-dependent relation to \(Z\); the vertical and low-row readouts remain separate. — [Complete occupation representation](../numerator-and-residuals/occupation_audit.md).
- The finite-phase scalar guard quotient can simplify pure-phase source terms, but applying it separately at each state introduces a state-flux correction. No claim that it removes that correction is made here. — [Accepted guard/state correlation audit](../occupation-arithmetic-bridge/guard_audit.md).

## What does a completely priced nonzero-density calibration establish?

### Takeaway

There is an exact positive finite-volume calibration with a nonzero coefficient of the ACTUAL density target. Its full reduced denominator and positive exterior can both be proved, and that natural rectangular family is decisively inadequate. This isolates a real arithmetic failure without extrapolating it to all guarded calibrations. — [Complete actual head and denominator checker](calibration_check.py).

### Cited Findings

- The unexceptional all-row birth readout satisfies \(Q_{\rm full}(0)=M-1/3\), with \(Z=2-3Q_{\rm full}(0)\). The single origin override is retained by this normalization. — [Accepted full normalization](../numerator-and-residuals/occupation_audit.md).
- Define \(r_{a,b}=1+6\Phi_b(\zeta_{a,b})\in\{1,7\}\), using the full high patch rule and every separate low row. Then
\[
\sum_{a,b\ge0}r_{a,b}2^{-a}3^{-b}
=3+6Q_{\rm full}(0)=7-2Z.
\]
This is an actual target relation, not an artificial numerator or unproved rational response assumption. — [Accepted complete rules](../numerator-and-residuals/occupation_audit.md), [new actual rectangle checks](calibration_check.py).

### Inferences

For odd positive integers \(A,B\), let
\[
q_{A,B}=\sum_{a<A,b<B}r_{a,b}2^{-a}3^{-b},
\qquad D_{A,B}=2^{A-1}3^{B-1}.
\]
Its numerator after multiplication by \(D_{A,B}\) is an integer coprime to both two and three. Modulo two only \(a=A-1\) remains, giving \(B\equiv1\). Modulo three only \(b=B-1\) remains, giving \(\sum_{j=0}^{A-1}2^j=2^A-1\not\equiv0\). Thus
\[
\boxed{\operatorname{den}(q_{A,B})=D_{A,B}.}
\tag{FC8}
\]
The conclusion uses the actual reduced denominator, not just a common clearer, and holds independently of the interior birth word because every reward is one modulo six. — [Exact parity/valuation certificate](calibration_check.py).

The whole complement is a positive exterior:
\[
\mathcal E_{A,B}=7-2Z-q_{A,B}>0,
\]
\[
3(2^{-A}+3^{-B}-2^{-A}3^{-B})
\le\mathcal E_{A,B}
\le21(2^{-A}+3^{-B}-2^{-A}3^{-B}).
\tag{FC9}
\]
Both infinite strips and their intersection are included. Multiplying yields an exact integer-affine relation
\[
D_{A,B}\mathcal E_{A,B}
=-2D_{A,B}Z+7D_{A,B}-D_{A,B}q_{A,B},
\]
but its positive cleared size satisfies
\[
\boxed{D_{A,B}\mathcal E_{A,B}\ge3^B/2,
\qquad D_{A,B}\mathcal E_{A,B}\ge2^{A-1}.}
\tag{FC10}
\]
Hence it diverges as both odd sides grow, even though the real exterior tends to zero. This is a fully priced failure with a nonzero target coefficient, rather than another zero-bulk identity. — [Exact full-quadrant tail and actual rectangle checks](calibration_check.py).

The finite-volume state construction above and FC8–FC10 show complementary limitations: existence of a finite common phase refinement does not guarantee a cheap source, while a positive full-density exterior can have prohibitive actual denominator. They do not exclude a signed interior correction with a noncompact reference potential, state-dependent phase cancellation, different source arithmetic, or a genuinely smaller actual exterior. The companion shell analysis supplies an analytic criterion for such a different complete calibration; feasibility and the integer-affine source are not established here. — [Prior full boundary requirements](../occupation-arithmetic-bridge/transport_audit.md), [parent task's remaining bridge](../occupation-arithmetic-bridge/REPORT.md).

### Gaps

- No adequate infinite arithmetic return for \(Z\) is constructed. The original scalar actual eligible digit-five supply, the fan response/gcd requirements and the occupation arithmetic bridge remain open. — [Current accepted status](../occupation-arithmetic-bridge/REPORT.md).
- The checker uses the explicitly identified accepted transport helper for exact logarithmic floors, axis recurrence and row tests. It adds exhaustive short-source carry checks, all-phase finite-volume tests and exact actual rectangle fractions. Its dependency is part of the certificate, not hidden independent verification. — [Checker](calibration_check.py).
- Skipped Lean, external review, historical priority and a global reproof of the accepted finite-cover theorem. Material risk: extending the positive-odd cost barrier to zero-one or signed calibrations, treating the one-axis cone target as the density, or treating a finite positive calibration as an adequate arithmetic return.
