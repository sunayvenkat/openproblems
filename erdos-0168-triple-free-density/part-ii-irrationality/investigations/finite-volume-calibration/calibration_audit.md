# Independent audit of the finite-volume calibrations

## Do all phases exit uniformly, and does the killed source have the claimed cost?

### Takeaway

**PASS; no substantive erratum.** The actual phase-zero unboundedness implies unboundedness at every phase, including every one-sided limiting itinerary. Compactness therefore gives a uniform finite exit time for each finite state box. This justifies finite rational step Poisson solutions without an invariant phase partition. The positive-odd killed source has exactly the stated reduced denominator and cannot produce an adequate cleared return. These conclusions are restricted to the stated source class. — [Audited FC1–FC3](calibration.md), [standalone exact checker](calibration_audit_check.py).

### Cited Findings

- The accepted actual process is \(Y_n=A_{3n}\), \(x_n=\{n\alpha\}\), \(\alpha=\log2/\log3\), with \(Y_0=1\) and \(T(y,x)=(y+\Phi(x),x+\alpha)\). The bounded-test identity is \(\Omega((8I-T)p)=8p(1,0)\), for \(\Omega=\sum_{n\ge0}8^{-n}\delta_{(Y_n,x_n)}\). The complete finite version retains the terminal atom. — [Accepted transport and independent audit](../occupation-arithmetic-bridge/transport_audit.md).
- The precise actual orbit \(A_{3n}\) is unbounded by the accepted original-board reduction and fixed-start bounded-remainder theorem. This is the phase-zero input, not a generic-phase assertion. The quantitative actual state-height bound is a separate accepted input. — [Actual-orbit audit](../numerator-and-residuals/occupation_audit.md), [height audit](../occupation-arithmetic-bridge/height_audit.md).
- Both the supplied checker and the new standalone checker pass. The standalone checker imports no project module, reconstructs actual axes from the original colored boards, and orders all common-refinement cuts using proved rational logarithm intervals. It checks actual cut values as well as cell words. — [Supplied certificate](calibration_check.py), [independent certificate](calibration_audit_check.py).

### Inferences

Write \(S_n(x)=\sum_{k<n}\Phi(x+k\alpha)\). If \(\|S_n(x)\|\le C\) for every \(n\) at one phase, the cocycle identity gives
\[
\|S_n(x+m\alpha)\|=\|S_{n+m}(x)-S_m(x)\|\le2C
\]
for every \(m,n\). For each fixed \(n\), the function \(S_n\) is continuous at zero. Indeed, a forward iterate \(k\alpha\), \(k\ge0\), could equal a cut \((j-s\alpha)/3\) modulo one only if \((3k+s)\alpha\) were an integer; here \(s\in\{1,2,3\}\). Irrationality rules this out. Density of the forward phase orbit now gives \(\|S_n(0)\|\le2C\) for all \(n\), contradicting the actual unboundedness. Adding a fixed initial state does not affect this conclusion. — [FC1 and its exact cut conventions](calibration.md).

The discontinuity issue in compactness is real, and the note handles it correctly. If two cut hits occurred along one phase orbit, subtracting their cut equations would force \(3m=s-s'\) for an integer \(m\). Since \(|s-s'|\le2\), this implies \(m=0\), \(s=s'\), and the same cut. Thus there is at most one hit. The left and right limiting infinite itineraries differ at at most one increment. Each differs from the actual right-continuous itinerary by a bounded eventual displacement, so both are unbounded. — [FC2](calibration.md).

If no uniform exit bound existed for a fixed finite box, choose arbitrarily long surviving orbits, pass to one fixed initial state, and then to phases converging from one side (or a constant subsequence). Every fixed finite itinerary stabilizes exactly on that side because it has finitely many cuts. Its limiting state sequence remains in the box at every time, contradicting the preceding one-sided unboundedness. Consequently \(M_R=\sup_{y\in K_R,x}\tau_R(y,x)<\infty\). This argument uses one-sided itineraries; ordinary continuity of the exit map is neither assumed nor available. — [FC2](calibration.md).

For a bounded positive odd integer reward, the killed solution
\[
p_R=\sum_{n<\tau_R}8^{-n-1}h\circ T^n
\]
inside the box, extended by zero outside, is therefore a finite rational phase-step function. A common refinement includes the finite-horizon cocycle cuts **and any pulled-back reward cuts**. The pure depth-\(M_R\) cocycle refinement suffices for the concrete state-only reward \(h=1+6F(y-1)\). No invariant partition is needed. Its residual \(e=h-(8I-T)p_R\) vanishes inside and equals \(h+p_R\circ T\ge1\) outside. Boundedness of \(p_R\) justifies the full infinite telescoping identity. — [FC3](calibration.md).

At the actual first exit \(\tau\ge1\),
\[
p_R(1,0)=\frac{\sum_{n<\tau}8^{\tau-1-n}h_n}{8^\tau}.
\]
The numerator is odd because its final digit is odd. Hence
\[
\operatorname{den}(p_R(1,0))=8^\tau,\quad
\operatorname{den}(8p_R(1,0))=D_R=8^{\tau-1},\quad
D_R\Omega(e)\ge D_R8^{-\tau}=\frac18.
\]
The accepted state-height estimate additionally forces the stated critical first-exit source cost, \(\log D_R\ge cR^{1/\kappa}-O(1)\), for this construction. It supplies no lower bound for a different source or general multiplier. — [FC3](calibration.md), [accepted height estimate](../occupation-arithmetic-bridge/height_audit.md).

The independent exact certificate covers **2,305 phase cells and all nine starting states of \(K_1\)** on the depth-256 common refinement: the maximum first exit is **232**. Actual cut values agree with the adjacent right-cell word through every relevant exit; the separate circle boundary is also checked. Direct original-board states give **\(\tau_1=2\), \(\tau_2=67\)**, killed-potential denominators \(8^2,8^{67}\), and head denominators \(8,8^{66}\). This finite certificate is not the proof of unboundedness or a bound for all radii. — [Independent certificate](calibration_audit_check.py).

### Gaps

- Uniform exit has no general quantitative upper bound here. Its existence relies on the accepted phase-zero theorem, rather than on finite observations. — [FC1–FC2](calibration.md).
- The exact denominator barrier requires the stated positive odd reward. Zero digits, signed corrections, or noncompact boundary values can change the source arithmetic. The height result does not restore a universal barrier. — [FC3 and its scope](calibration.md).
- This is a one-axis target readout. The vertical occupation, translated readouts, and complete low rows remain separate arithmetic obligations. — [Accepted complete bridge status](../occupation-arithmetic-bridge/REPORT.md).

## Are the binary Dirichlet normalizations and carry criterion correct?

### Takeaway

**PASS, including the uncancelled factor seven.** The noncompact binary construction has a globally positive exterior, even for outside-to-inside transitions. Its source cancellations are completely classified. Adequacy would require unbounded terminal-one runs ending in an exit zero along selected actual exits; no such supply is proved. The construction still targets a one-axis observable. — [FC4–FC7](calibration.md), [independent source/carry checks](calibration_audit_check.py).

### Cited Findings

- The actual reward is \(h(y)=F(y-1)\in\{0,1\}\). Outside the box the prescribed value is \(p_\infty=(1+h)/7\); inside it is the finite exit sum plus the discounted terminal boundary value. — [FC4](calibration.md).
- Independent actual source values agree with the supplied checker: at \(R=1\), \(\operatorname{den}(8p_0)=56\), \(\operatorname{den}(56p_0)=8\); at \(R=2\), these are \(7\cdot8^{66}\) and \(8^{66}\). Every binary word through \(\tau=10\), **4,092 words**, independently satisfies the valuation and reduced-denominator formulas. — [Independent checker](calibration_audit_check.py).

### Inferences

The finite formula gives \((8I-T)p=h\) inside and \(0\le p\le2/7\) globally. Outside,
\[
e=(8I-T)p-h=\frac{8+h}7-p\circ T,\qquad \frac67\le e\le\frac97.
\]
This bound uses the actual potential after the transition, so it covers re-entry into the box. Consequently \(8p_0-\Omega(h)=\Omega(e)>0\). — [FC4–FC5](calibration.md).

For \(N=N_\tau=1+h_\tau+7\sum_{n<\tau}8^{\tau-1-n}h_n\), direct multiplication gives
\[
p_0=\frac{N}{7\,8^\tau},\qquad
8p_0=\frac{N}{7\,8^{\tau-1}},\qquad
56p_0=\frac{N}{8^{\tau-1}}.
\]
Since \(N\equiv1+h_\tau\in\{1,2\}\pmod7\), **seven never cancels**. With
\(T=2^{\max(3(\tau-1)-v_2(N),0)}\), the exact denominators are
\[
\operatorname{den}(56p_0)=T,\qquad
\operatorname{den}(8p_0)=7T,\qquad
\operatorname{den}(p_0)=7\,2^{\max(3\tau-v_2(N),0)}.
\]
The source denoted \(T\) is the denominator of the **scaled** head \(56p_0\). It is not the denominator of \(8p_0\). — [FC6–FC7](calibration.md), [independent exact fractions](calibration_audit_check.py).

The valuation classification follows directly from the integer numerator. If \(h_\tau=0\) and the preceding prefix ends in \(\ell\ge1\) ones, their contribution is \(8^\ell-1\). Adding the terminal one leaves \(8^\ell\). If \(\ell<\tau\), the next previous bit is zero, so \(N/8^\ell\equiv1\pmod8\), giving \(v_2(N)=3\ell\). If the entire prefix is ones, \(N=8^\tau\). When the exit bit is one and the previous bit zero, \(N\equiv2\pmod8\), giving valuation one. Equal final bits give an odd numerator and valuation zero. These cases exhaust all words. — [FC5 carry classification](calibration.md), [exhaustive independent finite word check](calibration_audit_check.py).

Set \(C_R=7\Omega(e)=56p_0-7\Omega(h)\). The complete positive exterior gives
\[
6\,8^{-\tau}\le C_R\le\frac{72}7\,8^{-\tau}.
\]
Along exit times tending to infinity, \(T C_R\to0\) is therefore equivalent to \(T8^{-\tau}\to0\). For a terminal-one run ending in zero, the latter lies between \(8^{-\ell-1}\) and \(8^{-\ell}\), including the all-one-prefix exception. In every other case it stays bounded away from zero. Thus this ansatz gives adequate returns along a selected sequence exactly when the corresponding terminal-one runs tend to infinity. Merely observing some long runs, or merely proving the cocycle unbounded, does not supply this arithmetic condition. — [FC6 and stated conditional criterion](calibration.md).

### Gaps

- No theorem supplies those long runs at actual state-box first exits. The tested radii give no denominator saving. — [Actual tests and explicit supply gap](calibration.md).
- No proved integer-affine relation converts \(\Omega(h)\) to \(Z\) while paying the vertical and low-row readouts. Even a successful one-axis run supply would not alone settle the density problem. — [Complete occupation normalization and limitations](../numerator-and-residuals/occupation_audit.md).

## Is the complete density rectangle correctly normalized, and what does its failure imply?

### Takeaway

**PASS.** The unexceptional full reward has total **\(7-2Z\)**, its odd-by-odd physical heads have exact reduced denominator \(2^{A-1}3^{B-1}\), and their positive cleared exterior diverges. This is a proved failure of this concrete family with a nonzero target coefficient. It is not an impossibility theorem for all calibrations. — [FC8–FC10](calibration.md), [independent original-board rectangle check](calibration_audit_check.py).

### Cited Findings

- The true birth series is \(M=Q_{\rm full}(0)+1/3\), owing to the sole birth override at \((a,b)=(0,1)\). The accepted normalization is \(Z=3-3M=2-3Q_{\rm full}(0)\). Complete high rows retain isolate/patch corrections; every low row is separate. — [Accepted complete normalization](../numerator-and-residuals/occupation_audit.md).
- The standalone checker evaluates births by differences of the accepted finite-cover formula on original integer colored boards, without importing the axis/row helper. Sixteen odd-by-odd rectangle heads pass, including the origin correction and all low/high cells in those rectangles. — [Independent checker](calibration_audit_check.py), [accepted finite-cover foundation](../prefix-and-phase-audit/REPORT.md).

### Inferences

For the **unexceptional** birth \(\bar\eta\), put \(r_{ab}=1+6\bar\eta_{ab}\). The full baseline mass is \(\sum2^{-a}3^{-b}=3\), so
\[
\sum r_{ab}2^{-a}3^{-b}=3+6Q_{\rm full}(0)=7-2Z.
\]
Using true births instead adds exactly \(6/3=2\), yielding \(9-2Z\). The audited reward uses unexceptional births, so \(7-2Z\) is correct. Direct finite differences verify the true birth at \((0,1)\) is one and its unexceptional value zero. For any checked head containing that cell, the two reward heads differ by exactly two. — [Independent origin and head checks](calibration_audit_check.py), [FC8 normalization](calibration.md).

For odd positive \(A,B\), let \(q=\sum_{a<A,b<B}r_{ab}2^{-a}3^{-b}\) and \(D=2^{A-1}3^{B-1}\). Then \(Dq\) is integral. Modulo two only the final horizontal index remains, giving \(B\equiv1\pmod2\). Modulo three only the final vertical index remains; since \(r_{ab}\equiv1\pmod3\), it gives \(\sum_{j=0}^{A-1}2^j=2^A-1\not\equiv0\pmod3\). Thus the exact reduced denominator is \(D\), independently of the interior birth pattern. — [FC8](calibration.md).

The whole positive complement is \(E=7-2Z-q\). Its geometric mass, including both infinite strips and subtracting their intersection, is
\[
W=3(2^{-A}+3^{-B}-2^{-A}3^{-B}).
\]
Because \(1\le r_{ab}\le7\), \(W\le E\le7W\). In particular
\[
DE=-2DZ+7D-Dq,\qquad
DE\ge\frac{3^B}{2},\qquad DE\ge2^{A-1}.
\]
The rational head has a nonzero density-target coefficient after clearing, but its positive cleared exterior diverges as the odd sides grow. It cannot give the small nonzero integer-affine returns required for irrationality. This proof applies to these physical rectangle heads; it does not exclude signed interior corrections, different sources, or a different complete exterior. — [FC9–FC10](calibration.md).

### Gaps

- No adequate infinite arithmetic return for \(Z\) is constructed by this audit. All vertical, translated and low-row arithmetic remains unresolved wherever the accepted bridge leaves it unresolved. — [Current complete progress report](../occupation-arithmetic-bridge/REPORT.md).
- The certificate is exact standard-library Python. Its phase test covers whole finite-horizon cells and actual cut values; it contains no floating phase sampling or finite-to-infinite inference. The original finite-cover theorem, actual unboundedness theorem and quantitative height theorem remain explicitly accepted inputs, not fresh global proofs supplied by the checker. — [Independent checker](calibration_audit_check.py).
- Skipped Lean, external review, historical priority and a new global finite-cover proof. Main residual risk is enlarging these scoped results into an unproved long-run supply, an identification of the one-axis observable with \(Z\), or a universal multiplier obstruction.
