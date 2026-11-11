# Independent audit of guarded occupation transport

## Does the complete transport retain every source, high correction and low row?

### Takeaway

**PASS; no substantive erratum.** ET1–ET8 are exact discounted state-and-phase identities. The integer216 product relation has a complete finite corner and zero bulk target coefficient; it is not an integer-affine occupation bridge. — [Audited note](exact_transport.md), [independent checker](transport_audit_check.py).

### Cited Findings

- The accepted actual axes and unexceptional state are the ones used in the earlier occupation theorem. Its normalization is \(Z=2-3Q_{\rm full}(0)\), with \(Q_H=Q_{\rm full}-L\); the original \((0,1)\) birth override is separate and occurs once. — [Accepted occupation audit](../numerator-and-residuals/occupation_audit.md).
- Both the supplied checker and the new independent checker pass. The independent checker imports no project module. It computes axes from original colored-board counts, the isolate/patch correction from the original numerical root windows, and row readouts from differences of minima. — [Supplied certificate](exact_transport_check.py), [independent certificate](transport_audit_check.py).

### Inferences

For \(x_n=\{n\alpha\}\), the identity
\[
\lfloor(3n+s)\alpha\rfloor
=3\lfloor n\alpha\rfloor+\lfloor3x_n+s\alpha\rfloor
\]
and the three-periodicity of \(S\) reconstruct ET1 directly. The factors \(\omega^{-3n}\) disappear. Thus \(Y_n=A_{3n}\) and the phase evolve by the stated skew map, and
\[
\Omega-\frac18(T_A)_*\Omega=\delta_{(1,0)}.
\]
For a prefix ending before \(M\), the right side has the additional terminal atom \(-8^{-M}\delta_{(Y_M,x_M)}\). This fixes the sign and index of the terminal term independently. — [ET1–ET2](exact_transport.md), [original-board lift checks](transport_audit_check.py).

The same floor calculation with \(\beta=1/\alpha\), coefficients \(\omega^{-2s}\), and the periodic partial sum \(P\) proves the vertical lift. At \(b=3m+j\), all multiples of three drop out of the high correction exponents. The two stated tests in ET3 reproduce the original correction, including the negative offsets in \(M_{j-1},M_{j-3}\). Their disjointness is inherited from the accepted slope range. The high starts are exactly \(b_j=(6,4,5)\), or \(m_j=(2,1,1)\); the vertical source retains its original factor \(27^{-m_j}\). — [ET3–ET4](exact_transport.md), [accepted high correction](../response-closure-tests/response_relations.md), [independent guard checks](transport_audit_check.py).

The independent vertical test uses an alternative derivation. If \(f_j=\lfloor3v+j\beta\rfloor\), isolation means
\(\{3v+j\beta\}<\beta-1\); a patch means
\(\{3v+(j-1)\beta\}<2\beta-3\).
These follow from the original windows \(3e>2t\) and \(4t<27e\), respectively. Exact rational logarithm intervals verify both descriptions on every interval of the full vertical phase partition, not only on sampled orbit phases. Direct integer powers also check the original root windows at the actual sampled rows. — [Independent implementation](transport_audit_check.py), [original root definitions](../prefix-and-phase-audit/prefix_audit.md).

Taking the product of the two measure resolvents gives
\[
216\langle h\rangle-27\langle h\circ T_A\rangle
-8\langle h\circ T_B\rangle+\langle h\circ T_AT_B\rangle
=216\,27^{-m_j}h(1,V_{m_j},0,v_{m_j}).
\]
The maps act on separate product coordinates and commute. A finite rectangle additionally has its two terminal edges and terminal corner, with signs minus, minus, plus. Bounded cone kernels allow the infinite limit; linear-growth minimum potentials are integrable against the finite discounted first moments. — [ET5–ET6](exact_transport.md), [independent finite rectangle equality](transport_audit_check.py).

After summing the residue factors, the complete physical identity is
\[
216Q_H^{00}-27Q_H^{10}-8Q_H^{01}+Q_H^{11}
=216\sum_{i,j=0}^2 2^{-i}3^{-b_j}F(\zeta_{i,b_j}+t).
\]
This is precisely the nine-cell corner of the original high domain \(a\ge0,b\ge4\). Multiplying its right side by27 gives an integer. The independent checker evaluates that corner from original-board states and confirms the terminal identities before taking any infinite limit. The complete low rows separately satisfy their horizontal8-coefficient relation; no inappropriate vertical replacement of a low \(\Phi_b\) by the high \(F\) is made. — [ET7–ET8](exact_transport.md), [independent high and low checks](transport_audit_check.py).

The original birth override is not included in these unexceptional translated kernels. Independent differences of the accepted finite optimum verify the target coefficients at seven cells, including \((0,1)\), where the unexceptional readout is zero and the true birth is one. Its weight \(1/3\) gives the known scalar correction once. — [Accepted finite theorem](../prefix-and-phase-audit/REPORT.md), [independent origin check](transport_audit_check.py).

Finally, complete physical reindexing evaluates the high combination's bulk multiplier as
\[
216-27\cdot8-8\cdot27+8\cdot27=0.
\]
The relation contains shifted or guarded readouts and finite sources, but no surviving nonzero multiplier of the one target value. Applying state Green differences leaves physically shifted or guarded vertex values; it does not turn them into integer constants. — [ET6–ET8 and their scope](exact_transport.md), [complete shift dictionary](../weighted-response-identities/weighted_audit.md).

### Gaps

- The earlier finite optimum, canonical endpoint formulas and actual-axis definitions are explicit accepted inputs. This audit reconstructs their use in the new transport, not their complete global proofs. — [Accepted framework](../numerator-and-residuals/REPORT.md).
- No identity \(T\nu^H(z)=uZ+v\) follows from the zero-bulk transport. The additional guarded cone values and full low rows remain unevaluated arithmetically. — [Accepted bridge gap](../numerator-and-residuals/occupation_audit.md).

## Do the finite-controller and proper-guard obstructions have exactly their claimed scope?

### Takeaway

**PASS.** There are exactly \(9L\) genuine horizontal phase jumps, no global fixed affine physical-index shift, and no nontrivial finite invariant interval-phase partition. Proper finite-interval guard masses are irrational. None of these conclusions is a multiplier-height lower bound or an exclusion of arbitrary weighted numerical identities. — [ET5–ET10](exact_transport.md), [independent cut reconstruction](transport_audit_check.py).

### Cited Findings

- The actual horizontal axis is unbounded, as independently established in the accepted occupation audit. Its individual increments have modulus at most one. — [Actual support proof](../numerator-and-residuals/occupation_audit.md), [actual increment formulas](exact_transport.md).
- The independent checker reproduces \(A_0=A_9=1\), \(A_3-A_0=-\omega\) and \(A_{12}-A_9=\omega^2\) from original board counts. — [Independent actual witness](transport_audit_check.py).

### Inferences

For \(1\le s\le3L\), the summand
\(\omega^{-s}S(\lfloor3x+s\alpha\rfloor)\) has three cuts
\((k-s\alpha)/3\) in \((0,1)\). Equality of two cuts modulo one would make an integer multiple of irrational \(\alpha\) an integer, unless the indices and cuts coincide. At each cut only that summand changes, by the nonzero unit \(\omega^{-s+2k}\). Consequently \(\Phi_L\) has exactly \(9L\) jumps, \(9L\) circle arcs, and \(9L+1\) ordinary intervals after the artificial cut zero. The checker independently sorts exact affine cuts and verifies the adjacent values for \(L=1,\ldots,5\); the argument proves the count for every \(L\). — [ET9 derivation](exact_transport.md), [independent exact cut checks](transport_audit_check.py).

If a fixed \(h>0,\gamma,t\) satisfied \(A_{a+h}=\gamma A_a+t\) for all \(a\), bounded increments would bound \((\gamma-1)A_a+t\). Actual unboundedness therefore excludes \(\gamma\ne1\). For \(\gamma=1\), three repetitions would make \(\Phi_h(\{n\alpha\})=3t\) on a dense orbit. The genuine jumps just proved make this impossible. This rules out a single global affine recipe, including its stated cube-root special cases. It does not rule out phase-conditioned transport or finite-head approximations. — [ET6 and ET9](exact_transport.md), [accepted actual unboundedness](../numerator-and-residuals/occupation_audit.md).

A finite interval partition resolving a nonconstant guard has a nonempty finite essential boundary set. Rotation invariance would give each such point an infinite orbit inside that finite set. If rotated atoms are only assumed to be unions of atoms, their finitely many disjoint nonempty images still partition the same finite atom set, so each image is exactly one atom. The same contradiction applies. This is an exact interval-partition statement; it does not exclude other measurable representations or finite-dimensional relations between numerical readouts. — [ET7 proof](exact_transport.md).

For a finite union of intervals whose set and complement both have nonempty interior, the binary word
\(d_n=\mathbf1_I(\{n\alpha\})\) cannot be eventually periodic. An eventual period \(p\) and density of the tail orbit would imply that \(\mathbf1_I(x)=\mathbf1_I(x+p\alpha)\) at every joint continuity point. Its finite nonempty essential boundary would then be invariant under an irrational rotation. Endpoints themselves can change only finitely many digits and do not affect the conclusion. A rational base-eight number has an eventually periodic digit expansion; the digits0 and1 cannot be an alternate all-seven representation. Hence \(\sum_{n\ge0}8^{-n}d_n\) is irrational. The identical proof applies to vertical base27 with irrational \(\beta\) and any fixed phase start. — [ET8–ET10](exact_transport.md).

Constant or boundary-only codes are excluded from that assertion. Rational total mass is fully compatible with these irrational proper guard values, since complementary guards sum to \(8/7\), or \(27/26\) vertically. Rational independence of guards, or nonexistence of a target-dependent relation, is not implied. — [ET10 and explicit limitations](exact_transport.md).

### Gaps

- The actual same-state witness refutes state-only deterministic three-step transport in that specified representation. It does not refute every possible finite augmented model. — [Actual witness and scope](exact_transport.md).
- Neither the growing cut count nor irrational marginal guards bounds \(T\) in a prospective occupation bridge. A weighted-value cancellation can survive without a finite invariant interval partition. — [ET7–ET10 limitations](exact_transport.md).

## What was checked independently, and does this establish the requested arithmetic bridge?

### Takeaway

**PASS for the stated transport and obstructions; the arithmetic bridge remains unproved.** Both supplied and independent checkers pass. There is no substantive audit erratum and no proof of Erdős #168(ii) from this component. — [Audited scope](exact_transport.md), [independent checker](transport_audit_check.py).

### Cited Findings

- The independent checker uses original colored-board counts, original root-window inequalities, minimum-difference row tests and rational interval arithmetic. It imports no project helper, uses no floating arithmetic or solver, and runs in about0.15seconds with the installed Python3.14 interpreter. — [Independent certificate](transport_audit_check.py).
- It reconstructs both actual axes, all residue lifts, every vertical phase cell, actual original birth spot checks and origin, all complete high216 and low8 finite-terminal identities at five state translations, finite-corner integrality, the \(9L\) cut counts, and the actual state ambiguity. The supplied checker separately passes its larger prefix and cut ranges. — [Independent certificate](transport_audit_check.py), [supplied certificate](exact_transport_check.py).

### Inferences

The finite checks certify the concrete formulas and witnesses. The infinite conclusions rest on the written floor-periodicity, absolute-convergence, discounted telescoping, irrational-density and finite-boundary arguments above. No finite test is promoted to an infinite bridge or general impossibility theorem. — [ET1–ET10, independently reviewed](exact_transport.md).

The next successful exact-transport step would need to eliminate or control the guarded translated cone values while retaining a nonzero integer coefficient of the density target. The currently verified identity has zero such coefficient and therefore does not accomplish that step. — [ET6–ET8](exact_transport.md), [positive-return bridge criterion](../numerator-and-residuals/occupation_audit.md).

### Gaps

- Skipped Lean, external review, priority verification and full reconstruction of the archived finite foundation. Material risk: treating a correct resolvent as a closed arithmetic system, or treating the scoped finite-controller obstructions as a theorem against every occupation bridge. — [Explicit remaining gap](exact_transport.md).
