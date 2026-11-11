# Exact phase guarded occupation transport

## What complete physical transport identity do the actual cone readouts satisfy?

### Takeaway

There is an exact two-axis discounted skew-product resolvent, and hence a fixed integer-coefficient identity for every translated high cone readout. It retains the actual phase guards, patch rule, low rows and finite sources. It does **not** close those guarded readouts in the rational span of the target. No exact occupation bridge has been constructed. — [Exact checker](exact_transport_check.py), [accepted occupation definitions](../numerator-and-residuals/response_arithmetic.md).

### Cited Findings

- The actual axes satisfy
  \[
  A_{a+1}-A_a=\omega^{-a-1}S(\lfloor(a+1)\alpha\rfloor),\qquad
  B_{b+1}-B_b=\omega^{-2b-2}P(\lfloor(b+1)\beta\rfloor),
  \]
  where \(\alpha=\log_3 2\), \(\beta=1/\alpha\), \(A_0=B_0=1\), and the three-periodic functions have values
  \(S=(1,-\omega,0)\), \(P=(1,-\omega^2,0)\). — [Actual axis formulas](../boundary-and-arithmetic/arithmetic.md), [accepted exact implementation](../response-closure-tests/response_relations_check.py).
- The complete target has high state \(\zeta_{a,b}=A_a+B_b-1+C_{a\bmod3,b\bmod3}-E_b\) for \(b\ge4\); low rows use their separate functions \(\Phi_b\), with no \(E_b\). The unexceptional full readout satisfies \(Z=2-3Q_{\rm full}(0)\), and \(Q_H=Q_{\rm full}-L\). — [Full normalization and low-row audit](../numerator-and-residuals/occupation_audit.md).
- The basic state Green stencil is already archived, and a previous bare discounted minimum-potential guess fails on an actual square. The following derivation does not reassert either as a new arithmetic bridge. — [H11–H13](../hybrid-arithmetic-closure/hybrid_compression.md).

### Inferences

**ET1. Exact horizontal lift.** Put
\[
x_n=\{n\alpha\},\quad Y_n=A_{3n},\quad
\Psi_i(x)=\sum_{s=1}^{i}\omega^{-s}S(\lfloor3x+s\alpha\rfloor),\quad
\Phi=\Psi_3.
\]
For \(0\le i\le3\), direct summation of the actual recurrence gives
\[
A_{3n+i}=Y_n+\Psi_i(x_n),\qquad
(Y_{n+1},x_{n+1})=T_A(Y_n,x_n),
\quad T_A(y,x)=(y+\Phi(x),\{x+\alpha\}).
\tag{ET1}
\]
The reason the floor formula is exact is that
\(\lfloor(3n+s)\alpha\rfloor=3\lfloor n\alpha\rfloor+\lfloor3x_n+s\alpha\rfloor\), and \(S\) is three-periodic. Define the positive finite lifted measure
\[
\Omega=\sum_{n\ge0}8^{-n}\delta_{(Y_n,x_n)}.
\]
It has the exact resolvent
\[
\boxed{\Omega=\delta_{(1,0)}+\tfrac18(T_A)_*\Omega.}
\tag{ET2}
\]
This is a measure on state **and phase**; omitting its phase coordinate loses information. For every bounded test \(f\), \(\Omega(f)=f(1,0)+\Omega(f\circ T_A)/8\). The exact finite-prefix version has terminal term \(-8^{-M}f(Y_M,x_M)\). — [Accepted recurrence above; exact finite terminal and axis checks](exact_transport_check.py).

**ET2. Exact vertical lift and high-row correction.** Set
\[
v_m=\{m\beta\},\quad V_m=B_{3m},\quad
\Xi_j(v)=\sum_{s=1}^{j}\omega^{-2s}P(\lfloor3v+s\beta\rfloor),
\]
\[
T_B(w,v)=(w+\Xi_3(v),\{v+\beta\}).
\]
Then \(B_{3m+j}=V_m+\Xi_j(v_m)\). Write \(M_k(v)=\lfloor3v+k\beta\rfloor\), including the negative \(k\) needed below. The complete high-row correction is the finite step function
\[
e_j(v)=
\begin{cases}
\omega^{M_j(v)-2j},&M_j(v)-M_{j-1}(v)=2,\\
\omega^{M_{j-1}(v)-1-2j},&M_{j-1}(v)-M_{j-3}(v)=4,\\
0,&\text{otherwise}.
\end{cases}
\tag{ET3}
\]
The two nonzero cases are disjoint in the accepted slope range. Substituting \(b=3m+j\) in the established correction proves \(E_b=e_j(v_m)\) whenever \(b\ge4\); all integer multiples of three cancel from the exponents and differences. Thus the isolate/patch term is not replaced by an independent arbitrary alphabet. — [Accepted exact high-row correction](../response-closure-tests/response_relations_check.py), [all vertical phase and correction checks](exact_transport_check.py).

For \(j=0,1,2\), put \(m_j=(2,1,1)_j\), so \(b_j=3m_j+j=(6,4,5)_j\), and define
\[
\Pi_j=\sum_{m\ge m_j}27^{-m}\delta_{(V_m,v_m)}.
\]
Its resolvent retains its actual starting state:
\[
\boxed{\Pi_j=27^{-m_j}\delta_{(V_{m_j},v_{m_j})}
+\tfrac1{27}(T_B)_*\Pi_j.}
\tag{ET4}
\]
The exceptional low indices are excluded by these three starts, rather than incorrectly periodizing \(b=0,1,2,3\) as high rows. — [Accepted low/high split](../numerator-and-residuals/occupation_audit.md), [ET4 finite terminal checks](exact_transport_check.py).

**ET3. Complete product kernel.** With \(F(x+y\omega)=\mathbf1_{x\le0,x\le y}\), define
\[
h_{ij,t}(y,w,x,v)=F\bigl(y+\Psi_i(x)+w+\Xi_j(v)-1
+C_{ij}-e_j(v)+t\bigr).
\]
Then
\[
Q_H(t)=\sum_{i,j=0}^2 2^{-i}3^{-j}
\langle h_{ij,t},\Omega\otimes\Pi_j\rangle.
\tag{ET5}
\]
This is the accepted occupation product with its complete phase controller made explicit. Its total mass is \(1/27\). Canonical response kernels are obtained by the published horizontal unit rotation and endpoint displacement, so the same resolvents apply to those bounded tests too. — [Accepted eight canonical endpoints and products](../numerator-and-residuals/response_arithmetic.md), [independent-style exact lift checks](exact_transport_check.py).

Let \(T_A,T_B\) act on their separate product coordinates. Multiplying ET2 and ET4 gives, for every bounded \(h\),
\[
\boxed{216\langle h\rangle-27\langle h\circ T_A\rangle
-8\langle h\circ T_B\rangle+\langle h\circ T_AT_B\rangle
=216\,27^{-m_j}h(1,V_{m_j},0,v_{m_j}).}
\tag{ET6}
\]
The brackets here use \(\Omega\otimes\Pi_j\). Finite rectangles have all three exact terminal edges/corner retained; the checker verifies that equality before passing to the infinite limit. Bounded kernels justify the limit. Linear-growth minimum potentials are also integrable because the discount measures have finite first moments. — [ET2–ET4; exact rectangular terminal certificate](exact_transport_check.py).

Write \(Q_H^{uv}(t)=\sum_{a\ge0,b\ge4}2^{-a}3^{-b}F(\zeta_{a+3u,b+3v}+t)\). Equation ET6 summed with ET5 becomes
\[
\boxed{216Q_H^{00}-27Q_H^{10}-8Q_H^{01}+Q_H^{11}
=216\sum_{i,j=0}^2 2^{-i}3^{-b_j}F(\zeta_{i,b_j}+t).}
\tag{ET7}
\]
The right side is a complete nine-cell corner and is rational; multiplying ET7 by 27 makes it integral. This general physical reindexing identity is consistent with the archived complete shift dictionary and is not advertised as a new way to obtain a nonzero target multiplier. Indeed its bulk evaluation is \(216-27\cdot8-8\cdot27+216=0\). — [Archived complete physical shifts](../weighted-response-identities/weighted_closure.md), [new explicit phase realization and checks](exact_transport_check.py).

**ET4. Low rows remain complete.** For \(b<4\), use
\[
\ell_{i,b,t}(y,x)=\Phi_b(y+\Psi_i(x)+B_b-1+C_{i,b\bmod3}+t).
\]
Their horizontal resolvents give
\[
8L(t)-L^{10}(t)=8\sum_{i=0}^2\sum_{b=0}^3
2^{-i}3^{-b}\Phi_b(\zeta_{i,b}+t).
\tag{ET8}
\]
No vertical physical-shift formula for the low rules is asserted: shifting \(b\) by three can change the readout itself from a low \(\Phi_b\) to a high \(F\). The target relation remains exactly \(Z=2-3Q_{\rm full}(0)\); the original \((0,1)\) override is the fixed \(1/3\) birth correction and is not repeatedly inserted into translated response tests. — [Exact low rules and origin audit](../numerator-and-residuals/occupation_audit.md), [all low-row terminal checks](exact_transport_check.py).

For completeness, \(m(\omega z)=m(z)-y\) and \(m(\omega^2z)=m(z)-x\) for \(z=x+y\omega\). These exact rotations can align minimum kernels, but their linear coordinate readouts and the phase guards still require their complete weighted sums. Neither rotation turns them into known rational constants. — [Direct coordinate identity; common minimum potential](../numerator-and-residuals/response_arithmetic.md).

### Gaps

- ET6–ET8 are exact integer-coefficient transport, but not \(T\nu^H(z)=uZ+v\). The other physical/state/guard readouts remain in the identity, and ET7 has zero bulk target coefficient. — [Explicit arithmetic limitation](../numerator-and-residuals/occupation_audit.md).
- Rationality of \(Z\) evaluates only \(Q_{\rm full}(0)\) arithmetically. It has not evaluated its high part, other state translations, or phase-conditioned cones.

## Can a finite phase controller or a fixed physical shift remove the guarded values?

### Takeaway

The obvious exact closures fail in precise scopes. A nonzero fixed physical index shift cannot act as one global affine translation of the actual horizontal axis; an exact finite interval phase partition cannot be invariant under the irrational rotation; and proper phase-guard masses themselves are irrational. None of these facts prohibits value-specific cancellation or proves any multiplier-height lower bound. — [Exact cut and actual counterexample checker](exact_transport_check.py).

### Cited Findings

- The actual horizontal orbit \(A_{3n}\) is unbounded; the preceding occupation audit reconstructs this on the precise phase-zero orbit from original row sums and the bounded-remainder theorem. — [Actual unboundedness proof](../numerator-and-residuals/occupation_audit.md).
- The checker finds the exact same-state ambiguity \(A_0=A_9=1\), but \(A_3-A_0=-\omega\) and \(A_{12}-A_9=\omega^2\). Thus even the actual state and its residue class do not specify the next three-step transition. — [Exact recurrence check](exact_transport_check.py), [independent original-board verification in companion height work](height_budget.md).

### Inferences

**ET5. Exactly \(9L\) genuine horizontal phase cuts.** For \(L\ge1\), repeated ET1 gives
\[
\Phi_L(x)=\sum_{s=1}^{3L}\omega^{-s}S(\lfloor3x+s\alpha\rfloor),\qquad
A_{3(n+L)}-A_{3n}=\Phi_L(x_n).
\tag{ET9}
\]
For each \(s\), the three cut points in \((0,1)\) are
\[
\frac{k-s\alpha}{3},\qquad
k=\lfloor s\alpha\rfloor+1,\ \lfloor s\alpha\rfloor+2,\ \lfloor s\alpha\rfloor+3.
\]
Two such cuts cannot coincide modulo one: otherwise an integer multiple of irrational \(\alpha\) would be an integer, unless the two \(s\)'s and then cuts were identical. At each cut, exactly one summand jumps, by the nonzero unit \(\omega^{-s+2k}\). Hence there are exactly \(9L\) genuine jumps, \(9L\) circle arcs, or \(9L+1\) ordinary \([0,1)\) intervals after adding the artificial cut zero. The latter interval counts equal 10 only when \(L=1\). — [ET9 direct floor derivation; exact affine-cut checks for \(L=1,\ldots,6\)](exact_transport_check.py).

**ET6. No global fixed affine index translation.** Suppose for a fixed integer \(h>0\) and fixed \(\gamma,t\) one had \(A_{a+h}=\gamma A_a+t\) for all \(a\ge0\). Bounded single-step axis increments give \(|A_{a+h}-A_a|\le h\). If \(\gamma\ne1\), this contradicts actual unboundedness. If \(\gamma=1\), three repetitions give \(A_{a+3h}-A_a=3t\). At \(a=3n\), ET9 says \(\Phi_h(x_n)=3t\). The phase orbit is dense, but \(\Phi_h\) has the genuine nonzero jumps just proved; it cannot be constant on that orbit. This excludes the asserted global affine recipe. It excludes neither a state/phase-conditioned relation, a finite-head approximation, nor a nontrivial weighted identity. — [ET9 and accepted actual unboundedness](../numerator-and-residuals/occupation_audit.md), [small actual witnesses](exact_transport_check.py).

**ET7. No finite invariant interval phase refinement.** A finite interval partition exactly resolving the guards of \(\Phi\) has a nonempty finite set of circle boundary points. If the phase rotation permuted that partition, its boundary set would be invariant under \(x\mapsto x+\alpha\). Every boundary point has an infinite irrational orbit, a contradiction. More generally an exact finite partition whose rotated atoms are unions of atoms must permute the atoms: the disjoint nonempty images of finitely many atoms partition the same finite atom set. Thus finite exact interval-Markov closure also fails. Refining for \(L\) successive physical steps really introduces the \(9L\) cuts in ET9. This is a partition theorem, not a prohibition on finite identities between numerical readouts. — [ET9 and elementary finite-boundary argument; exact cuts](exact_transport_check.py).

**ET8. Proper interval guard masses are irrational.** Let \(I\) be a finite union of intervals such that both \(I\) and its complement have nonempty interior; this includes every nondegenerate proper circle interval. The base-eight word \(d_n=\mathbf1_I(\{n\alpha\})\) is not eventually periodic. If it had eventual period \(p>0\), density of the tail orbit would imply equality of the two piecewise-constant indicators \(\mathbf1_I(x)\) and \(\mathbf1_I(x+p\alpha)\) away from their finite boundary set. Its nonempty finite essential boundary would be invariant under an irrational rotation, impossible. Finite boundary conventions change only finitely many orbit hits and do not affect the argument. Thus
\[
\boxed{G_I=\sum_{n\ge0}8^{-n}\mathbf1_I(\{n\alpha\})\notin\mathbb Q.}
\tag{ET10}
\]
A rational base-eight number has an eventually periodic digit expansion, by the finite remainder states of long division; digits 0 and 1 avoid the alternate terminating/all-seven ambiguity. The same proof gives irrational vertical proper guard masses with \(27^{-n}\) and \(\beta\). These are actual scalar phase observables, not occupation cone values. Nevertheless their partition sum is the rational total \(8/7\), or \(27/26\) vertically. Hence rational total occupation mass cannot rationalize the guards. — [ET1–ET4 and elementary density/base-expansion proof; accepted actual phases](../boundary-and-arithmetic/arithmetic.md).

### Gaps

- ET7 does not exclude finite-dimensional numerical relations, other measurable representations, state-dependent filters, or cancellations special to the target. Guard count does not bound an arithmetic multiplier: the coefficients \(u,v\) of the target may be arbitrarily large integers.
- The companion approximate work obtains simultaneous arithmetic approximants for pure guards; ET10 is not an obstruction to those approximants. Guarded **state/cone** readouts remain a different problem. — [Companion pure-guard analysis](approximate_bridge.md).
- No claim that \(G_I\in\mathbb Q+\mathbb Q Z\) follows. Irrationality of a separate guard value is not an irrationality proof for \(Z\).

## What has this actually established toward an occupation arithmetic bridge?

### Takeaway

The phase-conditioned physical transport is explicit and exact, and its most direct finite/state-only shortcuts are rigorously excluded. The required target-dependent arithmetic relation remains unproved. — [Complete transport checker](exact_transport_check.py), [accepted positive-return bridge criterion](../numerator-and-residuals/occupation_audit.md).

### Cited Findings

- The exact checker uses standard-library integers and fractions only, with no project imports. Rational atanh-series bounds certify every logarithmic floor and affine cut comparison; it reconstructs both actual axes, their residue lifts and the complete vertical correction. It runs in approximately 0.5 seconds. — [Checker](exact_transport_check.py).
- It checks all high kernels and complete low horizontal resolvents with exact finite terminal terms, the two-axis integer rectangle identity, all \(9L\) nonzero cut jumps for \(L=1,\ldots,6\), and the actual same-state transition ambiguity. Those finite tests verify the concrete constructions; ET1–ET10 above provide the infinite proofs. — [Exact assertions](exact_transport_check.py).

### Inferences

The positive occupation return is \(D_\omega D_{\omega^2}Q_H(-z)\). Applying the same state differences to ET6/ET7 is legitimate because state translations commute with the lifted skew maps, but it yields **guarded or physically shifted vertex readouts**, plus the finite translated corner. The other terms do not vanish or become integer constants. The old bulk coefficient remains zero. Consequently this application has not given \(T\nu^H(z)=uZ+v\), even though every term and source is now specified. — [ET6–ET8 and exact Green identity](../numerator-and-residuals/response_arithmetic.md).

The parent task's new positive family has its own proved infinitude and positivity. To finish it by exact transport, a next theorem must eliminate or control the guarded translated readouts in ET6 with a target coefficient that survives. State-radius sublinearity may make a genuinely proved multiplier \(\log T=O(\|z\|)\) affordable, but it does not supply the missing identity. — [Companion state-radius budget](height_budget.md), [unproved integer bridge](../numerator-and-residuals/occupation_audit.md).

### Gaps

- No exact integer-affine bridge, adequate infinite arithmetic return or proof of Erdős #168(ii) is obtained.
- Skipped: Lean, external review, priority claims, new external theorem searches and broader filter enumeration. Material risk: presenting the exact resolvent as a closed arithmetic system, a state step as a physical shift, or pure-guard irrationality as irrationality of the density target.
