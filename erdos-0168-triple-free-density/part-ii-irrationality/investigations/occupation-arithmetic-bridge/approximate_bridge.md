# Positivity aware approximate bridges and phase arithmetic

## What error budget would turn a positive occupation return into an arithmetic return?

### Takeaway

An approximate bridge is sufficient if its error is smaller than one known first-arrival weight and its multiplier is cheaper than the proved mass decay. A positive rational truncation without a target coefficient cannot satisfy that budget with a cheap reduced denominator. — [Accepted actual occupation family](../numerator-and-residuals/occupation_audit.md), [new exact checker](approximate_bridge_check.py).

### Cited Findings

- The actual high-state atom \(E_n=\nu^H(z_n)\) is positive and obeys \(E_n\le 6\,2^{-N_n}-3\,3^{-N_n}\), where \(N_n\) is its first total-index arrival. The origin relation is \(Z=2-3Q_{\rm full}(0)\), and \(Q_H=Q_{\rm full}-L\) retains all four low rows. — [Complete definitions and audited infinite support](../numerator-and-residuals/occupation_audit.md).
- State translation is not physical index translation; rationality of \(Z\) has not evaluated other cone values or their low-row terms. Universal finite-boundary filter classifications do not by themselves realize state Green differences. — [Occupation limitations](../numerator-and-residuals/response_arithmetic.md), [earlier full boundary obligations](../hybrid-arithmetic-closure/REPORT.md).

### Inferences

**AB1. A first-witness approximate-bridge criterion.** Choose an actual first-arrival cell \((a_n,b_n)\), \(b_n\ge4\), \(a_n+b_n=N_n\), with state \(z_n\), and put
\[
w_n=2^{-a_n}3^{-b_n}\le E_n,\qquad w_n\le2^{-N_n}.
\]
Suppose one constructs
\[
R_n=\frac{u_nZ+v_n}{T_n},\quad
T_n\in\mathbb Z_{>0},\quad u_n,v_n\in\mathbb Z,
\qquad |R_n-E_n|\le\vartheta w_n,\quad 0\le\vartheta<1,
\tag{AB1}
\]
with \(T_n2^{-N_n}\to0\). Then
\[
0<(1-\vartheta)w_n\le R_n
\le(6+\vartheta)2^{-N_n},
\qquad T_nR_n\longrightarrow0.
\tag{AB2}
\]
Under hypothetical \(Z=A/B\), \(BT_nR_n=u_nA+Bv_n\) is a positive integer tending to zero. This proves irrationality if AB1 is actually constructed. No height bound on \(u_n,v_n\) is required. The more conservative absolute error budget \(\vartheta3^{-N_n}\) is also sufficient because \(w_n\ge3^{-N_n}\). A bound merely tending to zero without comparison to \(w_n\) does not preserve positivity. These deductions use the full actual atom bound and its witness, not a truncated vertex.

**AB2. A target-free obstruction.** If \(u_n=0\) and \(R_n=r_n/s_n>0\) is reduced, AB2 forces
\[
s_n\ge1/R_n\ge2^{N_n}/(6+\vartheta).
\tag{AB3}
\]
Consequently finite occupation heads or rational model atoms, treated as rational numbers without a nonzero target-dependent identity, cannot furnish cheap multipliers: any integer clearing \(R_n\) is a multiple of \(s_n\), and \(T_nR_n\ge1\). This remains true after every genuine rational cancellation. It is a scoped obstruction to target-free rational replacements, not to \(u_nZ+v_n\) with \(u_n\ne0\), and not a lower bound on an actual signed model error.

### Gaps

- No AB1 relation for the actual occupation atoms has been constructed. The criterion is a sufficient interface, not an irrationality proof. — [Explicit existing arithmetic gap](../numerator-and-residuals/occupation_audit.md).
- The first witness controls the required positivity scale, but supplies neither integer coefficients nor cheap denominators for translated cone values.

## Can the actual phase guards themselves be approximated arithmetically at adequate cost?

### Takeaway

Yes. Pure phase guards admit simultaneous adequate rational approximants along a proved actual infinite sequence, including resonant current convergents. This positive arithmetic statement concerns phase words only; it does not price or evaluate their state-conditioned cone readouts. — [Exact physical guard coding](exact_transport.md), [independent exact phase/CF checks](approximate_bridge_check.py).

### Cited Findings

- The exact physical three-step lift has phase \(x_n=\{n\alpha\}\), \(\alpha=\log2/\log3\). A fixed finite physical context uses floor residues \(\lfloor3x+s\alpha\rfloor\bmod3\), with positive integer \(s\); at \(x_n\) these equal \(\lfloor(3n+s)\alpha\rfloor\bmod3\). — [Companion exact guarded transport](exact_transport.md).
- The actual \(\alpha\) is irrational by prime valuations and transcendental by Gelfond–Schneider: an algebraic irrational \(\alpha\) would make \(3^\alpha=2\) impossible. The external theorem is stated as Theorem 10 in the first-party course notes. — [Soundararajan, Theorem 10, PDF p. 9](https://math.stanford.edu/~ksound/TransNotes.pdf#page=9), [earlier checked specialization](../infinite-return-construction/final_return_audit.md).
- The new checker constructs the actual continued-fraction prefix from rigorous rational logarithm intervals and computes floor residues using integer powers only. It checks periods, common prefixes and complete tail intervals at \(12/19\), \(53/84\) and the resonant current \(665/1054\). — [Exact certificate](approximate_bridge_check.py).

### Inferences

**AB3. Common-denominator guard approximation.** Let \(S\subset\mathbb Z_{>0}\) be finite and nonempty, \(s_*=\max S\), and let \(f:\{0,1,2\}^{S}\to\{0,1\}\). Define
\[
g_n=f\bigl((\lfloor(3n+s)\alpha\rfloor\bmod3)_{s\in S}\bigr),
\qquad G_f=\sum_{n\ge0}8^{-n}g_n.
\]
For an actual convergent \(p/q\) with successor \(P/Q\), let \(\sigma=\operatorname{sign}(\alpha-p/q)\). At every positive integer \(k\), use the one-sided floor
\[
\lfloor kp/q\rfloor_\sigma
=\lfloor kp/q\rfloor-\mathbf1_{\{\sigma<0,\ q\mid k\}}.
\]
Replace the actual floors in \(g_n\) by these rational floors to get \(\widehat g_n\). Since increasing \(n\) by \(q\) adds \(3p\) to every floor, \(\widehat g\) is exactly \(q\)-periodic. Thus
\[
\widehat G_f=
\frac{\sum_{n=0}^{q-1}8^{-n}\widehat g_n}{1-8^{-q}},
\qquad (8^q-1)\widehat G_f\in\mathbb Z.
\tag{AB4}
\]
No nonresonance condition is used. Positive \(S\) avoids an unhandled index-zero floor override.

The parent Farey interval contains no interior rational with denominator below \(q+Q\). Therefore the one-sided and actual floors agree for \(0<k<q+Q\). If
\[
m=\left\lfloor\frac{q+Q-1-s_*}{3}\right\rfloor+1>0,
\]
the two Boolean words agree for \(0\le n<m\). Their difference after that point has magnitude at most one, so
\[
|G_f-\widehat G_f|\le\frac87\,8^{-m},
\qquad
\boxed{(8^q-1)|G_f-\widehat G_f|
\le\frac87\,2^{s_*+2q-Q}.}
\tag{AB5}
\]
This is simultaneous for every Boolean \(f\) on the context, with one denominator and a constant independent of the number of code labels. Neither equality of the complete state orbits nor periodicity of a rational state walk is asserted.

**AB4. Automatic unrestricted adequate supply.** Any irrational continued fraction not eventually all ones has infinitely many indices with
\[
Q-2q>q/3.
\tag{AB6}
\]
If digits \(a_{n+1}\ge3\) occur infinitely, their margin is at least \(q\). Otherwise the tail digits are at most two and infinitely many next digits equal two. At those late indices, the incoming digit is also at most two, so \(q<3q_{n-1}\), and
\[
Q-2q=q_{n-1}>q/3.
\]
An eventually all-one tail is quadratic; the actual transcendental \(\alpha\) is therefore covered. This proof requires neither unbounded partial quotients nor a favorable nonresonance state. In particular, the earlier countermodels against large jumps at nonresonant currents do not contradict AB6.

For fixed \(S\), AB5 tends to zero along this actual infinite subsequence. More generally it does so for contexts \(S_q\) with \(\max S_q=o(q)\), even with changing Boolean codes, because AB5 is uniform. This prices pure guards in sublinear physical contexts. It does not automatically make the denominator affordable relative to a chosen occupation first-arrival \(N(z)\), nor ensure an error smaller than its first weight.

**AB5. Which returns are nonzero?** The phase function
\[
x\longmapsto f\bigl((\lfloor3x+s\alpha\rfloor\bmod3)_{s\in S}\bigr)
\]
is piecewise constant with finitely many boundary points. If it is genuinely nonconstant on open intervals, its orbit word cannot be eventually periodic: such periodicity and orbit density would make the phase function invariant off its boundaries under an irrational rotation \(d\alpha\). Its finite nonempty boundary would then have to contain an infinite orbit, a contradiction. Its base-eight digits are zero or one, so rationality would force eventual periodicity. Therefore \(G_f\) is irrational, every rational \(\widehat G_f\) differs from it, and AB5 supplies genuine nonzero arithmetic returns for these pure guards. Constant or boundary-only codes are excluded from this nonzero assertion; AB5 itself applies to all Boolean codes. — [Exact guarded-word irrationality statement](exact_transport.md).

The checker verifies complete intervals for three actual cases:

| Current / successor | Current resonant? | Rational word period | Guaranteed matching length |
|---|---|---:|---:|
| \(12/19,\ 41/65\) | no | 19 | 27 |
| \(53/84,\ 306/485\) | no | 84 | 189 |
| \(665/1054,\ 15601/24727\) | yes | 1054 | 8593 |

It checks the nine realized three-floor Boolean cell guards simultaneously, proves the advertised cleared bound below one, and separately encloses a nonconstant guard return away from zero in each case. The infinite theorem rests on AB3–AB5, not these finite examples. — [Exact certificate](approximate_bridge_check.py).

### Gaps

- Guard arithmetic is not target arithmetic. These results prove no relation expressing \(G_f\), or a guarded cone value, as rational-affine in \(Z\).
- If the physical context grows on a different scale, its \(s_*\) factor must be paid. The bound requires \(Q-2q-s_*\to\infty\); the actual infinite subsequence above only guarantees a fixed positive fraction of \(q\) of slack.
- The Gelfond–Schneider theorem is a checked external input, not reproved here. No historical novelty is claimed for irrationality of rotation codes.

## Why does the guard construction not yet approximate the occupation arithmetic bridge?

### Takeaway

Periodic guard replacement has a rigorous small real error, but leaves unknown decimated actual-state readouts. An exact actual correlation certificate disproves the scalar-factorization shortcut. — [Complete skew transport](exact_transport.md), [new original-board certificate](approximate_bridge_check.py).

### Cited Findings

- The true occupation process retains both the state \(A_{3n}\) and phase \(\{n\alpha\}\). Its guarded readout is a joint observable of those two variables. — [Exact discounted lift](exact_transport.md), [accepted complete occupation products](../numerator-and-residuals/response_arithmetic.md).
- Original colored-board counts independently reconstruct \(A_a=\omega^{-a}\mathcal K(2^a)\). The new checker uses this identity directly, not a companion skew recurrence, in its correlation interval. — [Original-board input](../numerator-and-residuals/occupation_audit.md), [new checker](approximate_bridge_check.py).

### Inferences

**AB6. Exact remainder after periodic guard replacement.** For any bounded actual-state observable \(h_n\), retaining the actual states gives
\[
\left|\sum_{n\ge0}8^{-n}g_nh_n
-\sum_{n\ge0}8^{-n}\widehat g_nh_n\right|
\le\frac87\,\|h\|_\infty8^{-m}.
\tag{AB7}
\]
But the second sum is
\[
\sum_{r=0}^{q-1}8^{-r}\widehat g_r
\underbrace{\sum_{k\ge0}8^{-qk}h_{r+kq}}_{H_{q,r}}.
\tag{AB8}
\]
The \(H_{q,r}\) are decimated ACTUAL-state readouts. Pure guard periodicity does not make them rational, constant across residues, or affine in the sole target. Replacing the entire state orbit by a rational model is another operation whose state period, drift, low rows and denominator must be justified. In particular the resonant-current success in AB5 applies to state-free words; it grants no periodic rational state process at resonance.

**AB7. Actual correlation, not a hypothetical warning.** Put
\[
\Omega(h)=\sum_{n\ge0}8^{-n}h_n,\quad \Omega(1)=8/7,\qquad
g_n=\mathbf1_{\{\lfloor(3n+1)\alpha\rfloor\equiv0\pmod3\}}.
\]
For each of the two actual readouts
\[
h_n=\mathbf1_{\{A_{3n}=1\}},\qquad
h_n=F(A_{3n}-1),
\]
the complete sums satisfy
\[
\boxed{\frac1{10}<
\Omega(gh)-\frac{\Omega(g)\Omega(h)}{8/7}
<\frac16.}
\tag{AB9}
\]
The certificate uses 28 original-board samples and the complete positive tails \((8/7)8^{-28}\). For lower and upper product bounds it separately retains the unknown tails of both marginals and the joint. Thus it is a genuine actual infinite-sum inequality, not a numerical correlation from a finite sample. Both the vertex and cone observables fail the proposed independence factorization.

This does not rule out clever target-dependent cancellation. It specifically prevents replacing a joint guarded cone/state readout by the product of its phase mass and an unguarded readout. The finite-boundary filter route still needs a proved actual identity with nonzero target coefficient and all semi-infinite sides retained. No such filter or occupation bridge was obtained in this component. — [Earlier boundary identity restrictions](../hybrid-arithmetic-closure/REPORT.md).

### Gaps

- No actual \(R_n=(u_nZ+v_n)/T_n\) satisfying AB1 has been constructed.
- Adequate pure-guard approximants are compatible with irrational guards and strong state/guard correlation. They remove a possible overstatement that irrational guards are inherently unapproximable; they do not close the actual guarded-state module.
- Skipped: Lean, external review, larger finite filter searches and a reproof of the external transcendence theorem. Material risk: promoting pure phase arithmetic or a target-free rational truncation into a density arithmetic return.
