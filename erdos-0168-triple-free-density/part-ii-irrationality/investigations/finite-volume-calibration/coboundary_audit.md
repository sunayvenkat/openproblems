# Audit of scalar guard coboundaries and actual state flux

**PASS, with two scope clarifications.** The scalar converse, jump criterion, nine-guard horizontal module, affine-moment application and nonzero actual flux survive this independent audit. Charges classify rationality, or relations modulo rational constants; exact zero relations also require the reconstructed rational constant to vanish. The at-most-100 product span concerns the actual horizontal/vertical cut-orbit modules, not arbitrary new phase cuts. No source theorem otherwise requires correction. Audited 7 November 2026.

## Does rationality at one phase really force a finite step transfer?

### Takeaway

Yes, for an irrational rotation, integer discount base and a finite **rational-valued, right-continuous** step guard. A bounded-lattice argument followed by a uniform finite-partition approximation proves the converse without assuming continuity at a dense set of possible jumps. Arbitrary endpoint overrides preserve the rationality test but do not preserve the asserted functional class of the transfer. — [Audited source](coboundaries.md), [standalone exact checker](coboundary_audit_check.py).

### Cited Findings

- The supplied checker exits successfully with `PASS: jump reconstruction, nine-guard basis, carry coboundary, actual moments and nonzero state flux`. — [Supplied checker](coboundaries_check.py).
- The separate checker imports only `fractions` and `functools`. It independently reconstructs a mixed non-Boolean guard, checks the transfer at all refined cells and endpoints, tests both discount bases, and tests a singleton endpoint spike. It exits with PASS. These finite computations check the formulas; the infinite converse is justified below. — [Standalone checker](coboundary_audit_check.py).

### Inferences

Let \(R(x)=x+\theta\pmod1\), \(\theta\notin\mathbb Q\), \(b\in\mathbb Z_{\ge2}\), and \(h\) be a finite rational right-continuous circle step function. Set
\[
 U(x)=\sum_{n\ge0}b^{-n}h(R^nx).
\]
The series converges uniformly. Therefore \(U\) is bounded and right-continuous, and
\[
 U(Rx)=bU(x)-bh(x).                                      \tag{A1}
\]
After multiplying \(h\) by a common positive denominator, assume its values are integers. If \(U(x_0)=r/s\), A1 puts every forward-orbit value in \(s^{-1}\mathbb Z\). Boundedness makes this a finite set. Every point is a limit of forward-orbit points approaching from the right; right continuity implies that **every** value of \(U\) belongs to the same finite lattice.

Choose a finite partial sum \(U_M\) with uniform error below \(1/(3s)\). On each half-open atom of its finite step partition, \(U_M\) is constant. Any two \(U\)-values on that atom differ by less than \(2/(3s)\), hence are equal. This includes the left endpoint by the specified half-open convention. Thus \(U\) is itself a finite rational right-continuous step function. Equation A1 gives \(h=U-b^{-1}U\circ R\). Undoing the denominator establishes the claimed converse. Conversely, for bounded \(f\),
\[
 \sum_{n=0}^{N-1}b^{-n}(f-b^{-1}f\circ R)(R^nx)
 =f(x)-b^{-N}f(R^Nx),
\]
so a finite rational step transfer implies rational readout at every start. The proof never assumes that \(U\) is continuous at its potential dense jump set.

The jump orientation is correct. On an orbit \(c_j=c_0+j\theta\), write \(d_j=\Delta h(c_j)\), \(v_j=\Delta f(c_j)\). A jump of \(f\circ R\) at \(c_j\) is the jump of \(f\) at \(c_{j+1}\), so
\[
 d_j=v_j-b^{-1}v_{j+1},\qquad
 \mathcal C(h)=\sum_j b^{-j}d_j.                         \tag{A2}
\]
For guard support in \([m,M]\), terminal condition \(v_{M+1}=0\) yields
\[
 v_j=\sum_{k=j}^{M}b^{j-k}d_k.
\]
For \(j<m\), this equals \(b^j\mathcal C(h)\). Consequently the transfer jumps have finite support exactly when the charge is zero. This is both necessary and sufficient on each orbit. A transfer cannot hide an additional orbit of nonzero jumps: the homogeneous recurrence on such an orbit has no nonzero finitely supported solution.

The circle compatibility and constant term are essential. Summing A2 over all orbits gives
\[
 0=\sum_c\Delta h(c)=(1-b^{-1})\sum_c v(c).
\]
Thus the reconstructed jumps integrate to a rational circle step \(f_0\). The finite step function \(h-f_0+b^{-1}f_0\circ R\) has no jumps and is therefore a rational constant \(C\). Adding \(C/(1-b^{-1})\) to \(f_0\) completes the transfer. The criterion is effective once cut-orbit equivalences have been established; it does not provide an algorithm for deciding arbitrary real orbit membership.

For finitely many arbitrary rational endpoint overrides, write \(h=h^++e\), where \(h^+\) is the canonical right-continuous rule and \(e\) has finite point support. An irrational forward orbit visits each exceptional point at most once, so \(U_h(x)-U_{h^+}(x)\) is a finite rational sum. Therefore the same charge test decides rationality. But the original \(h\) need not have a finite step transfer, even if isolated endpoint values are allowed in that transfer. For the singleton \(h=\mathbf1_{\{c\}}\),
\[
 U_h(R^{-k}c)=b^{-k}\quad(k\ge0),
\]
and \(U_h\) is zero elsewhere. All readouts are rational, but the bounded transfer is uniquely \(U_h\), with infinitely many distinct values and point spikes. A finite step transfer is impossible. The separate checker tests this at \(c=-\alpha\pmod1\).

Carries are a real obstruction to a naive digit argument. If \(p\) is an interval indicator, then \(h=bp-p\circ R\) is integer-valued with possible values \(-1,0,b-1,b\), and \(U_h=bp\) is rational. The standalone checker verifies finite terminal identities for \(b=8,27\). Nonperiodicity of a Boolean word cannot justify irrationality for arbitrary rational or integer linear combinations of guards.

### Gaps

The result is a scalar phase theorem. It does not establish closure of accumulated-state observables, the arithmetic bridge to the density, or historical priority. Endpoint conventions and integer \(b\ge2\) are used in the proof, rather than disposable technical assumptions.

## Is the ten-dimensional module complete, and does its moment application follow?

### Takeaway

Yes. The actual horizontal cuts occupy exactly nine rotation orbits, and a fixed Boolean basis has nonsingular charge matrix of determinant \(-7\). This captures every rational relation, including carries. It also proves rational independence of 1 and the two lattice coordinates of both actual horizontal affine moments. These are moment results, not density irrationality results. — [Source claims CG4–CG6](coboundaries.md), [independent certificates](coboundary_audit_check.py).

### Cited Findings

- The accepted actual-axis and transport definitions are the inputs to this audit. No density bridge is assumed. — [Occupation arithmetic bridge](../occupation-arithmetic-bridge/REPORT.md), [exact transport](../occupation-arithmetic-bridge/exact_transport.md), [transport audit](../occupation-arithmetic-bridge/transport_audit.md).
- The standalone checker isolates logarithms with rational positive-series bounds, orders all actual cuts without floats, checks the eighteen-cell six-offset Boolean code, constructs the charge matrix from adjacent cell values, computes its determinant by rational elimination, and reconstructs a twelve-offset mixed guard. For the actual moments it computes original-board row color counts independently of the drift recurrence, then checks 24 blocks and their exact terminal terms. — [Standalone checker](coboundary_audit_check.py).

### Inferences

Write \(\alpha=\log2/\log3\); it is irrational because a rational relation would give a positive-power equality between 2 and 3. The cuts are \(c_{s,k}=(k-s\alpha)/3\pmod1\), \(s>0\), \(k\in\{0,1,2\}\). Comparing rational and \(\alpha\) coefficients proves
\[
 c_{s,k}-c_{s',k'}\in\mathbb Z\alpha+\mathbb Z
 \iff s\equiv s'\pmod3,quad k\equiv k'\pmod3.
\]
Choose representatives \(c_{r,k}\), \(r=1,2,3\). Since \(c_{r+3m,k}=R^{-m}c_{r,k}\), the correct horizontal charges are
\[
 C_{r,k}(h)=\sum_{m\ge0}8^m\Delta h(c_{r+3m,k}).         \tag{A3}
\]
The positive power \(8^m\) is essential and agrees with A2.

Let the distinguished representative be \(c_0=c_{3,0}=-\alpha\pmod1\). For the other eight representatives use \(B_i=\mathbf1_{[c_0,c_i)}\), with positive circle orientation, and use \(B_0=\mathbf1_{[c_0,c_{6,0})}\). They are Boolean functions of offsets 1 through 6. To see that the complete code distinguishes phase atoms, first fix one of the three arcs identified by the first residue. Each other residue changes at most once inside that arc; between any two different refined atoms some component has changed and cannot have returned to its old value. The first component separates the three original arcs. The checker independently verifies all eighteen refined atoms.

The charge columns, ordering the distinguished orbit first, are
\[
 C(B_0)=-7e_0,\qquad C(B_i)=e_0-e_i\quad(i\ne0).
\]
Their determinant is \(-7\). For any actual finite guard \(h\), let
\[
 a_i=-C_i(h)\ (i\ne0),\qquad a_0=-\frac{\sum_i C_i(h)}7.
\]
Then \(h-\sum_i a_iB_i\) has zero charges, so its reconstructed transfer \(f\) gives
\[
 G_h=f(0)+\sum_i a_iG_{B_i}.                            \tag{A4}
\]
If a rational combination of \(G_{B_i}\) were rational, A2 would force its nonzero coefficient vector into the kernel of this matrix. Hence \(1,G_{B_0},\ldots,G_{B_8}\) are rationally independent: the space is **exactly ten-dimensional**. More generally, to test a zero relation between arbitrary finitely many guards, reduce them by A4, test the nine basis coefficients, and then test the remaining rational constant. Charges alone classify relations **modulo rationals**, not exact vanishing without that last check. This distinction is already supported by the source's constant reconstruction.

The constructive height bound is sound. With offsets at most \(M\), common denominator \(D\), and absolute guard height at most \(H\), A3 is a sum of at most \(3M\) rational jumps with powers up to \(8^{O(M)}\). The fixed inverse adds only the factor 7. A2 reconstructs transfers with denominators dividing a fixed multiple of \(D8^{O(M)}\); integrating at most \(O(M)\) jumps and correcting the constant adds only a fixed factor and \(\log M\) bits. Thus the rational numerator/denominator bit heights are
\[
 O\bigl(M+\log(2+D)+\log(2+H)\bigr).
\]
The basis needs at most offset 6, which changes only an absolute constant. This bound is for scalar guard coefficients, not for arithmetic bridge multipliers.

For the vertical phase \(\beta=1/\alpha\), base 27, the same proof gives nine nonconstant generators and charge column \(-26e_0\). A finite rational rectangle refinement whose horizontal and vertical cuts belong to these **actual cut-orbit modules** therefore has a product-measure readout in the span of at most \(10\cdot10=100\) products. Cuts certified to lie in the same orbits are also allowed. Arbitrary new cuts require extra orbit classes: for example, the endpoints of \([1/7,2/7)\) lie outside the nine actual horizontal classes, as follows by the same rational-coefficient comparison. Its nonzero new charges cannot be canceled by the existing basis. The source's unrestricted-sounding phrase “finite rectangle refinement” must be read with this actual-module restriction. No product independence or joint state-and-phase closure follows.

For the actual drift, put \(S(m)=\sum_{j=0}^m\omega^{2j}\) and
\[
 \Phi(x)=\sum_{s=1}^3\omega^{-s}S(\lfloor3x+s\alpha\rfloor).
\]
At \(c_{r,k}\), its jump is \(\omega^{-r+2k}\). Each class has exactly one jump, so its charges are these units. They include both 1 and \(\omega\), spanning the two rational lattice coordinates. Every nonzero rational functional \(\ell:\mathbb Q[\omega]\to\mathbb Q\) therefore leaves at least one nonzero charge. A2 proves \(G_{\ell\Phi}\notin\mathbb Q\). The checked actual carry identity \(\Phi_2-9\Phi_1=\Phi_1\circ R-8\Phi_1\) is consistent with this conclusion and is captured by the same charges.

Let \(Y_n=A_{3n}\), with \(Y_0=1\), and \(M_A=\sum_{n\ge0}8^{-n}Y_n\). The actual recurrence is \(Y_{n+1}-Y_n=\Phi(\{n\alpha\})\). Bounded increments give \(Y_n=O(n+1)\), hence absolute convergence. Summing the recurrence gives
\[
 G_\Phi=7M_A-8.
\]
A rational relation between 1 and the two coordinates of \(M_A\) would make \(G_{\ell\Phi}\) rational for a nonzero rational functional \(\ell\), a contradiction. These are the coefficients of 1 and \(\omega\), not ordinary real and imaginary coordinates.

With \(\Psi_i\) the partial drift through offsets 1 to \(i\), the complete horizontal moment is
\[
 M_A^{\rm all}=\sum_{a\ge0}2^{-a}A_a
 =2+\tfrac14G_{\Phi+2\Psi_1+\Psi_2}.
\]
Its jumps retain the unit directions with factors 4, 2, 1 at offsets 1, 2, 3. The same independence argument applies. The checker obtains the axes directly from the board \(2^i3^j\le2^a\): row \(j\) has maximal column \(L=\lfloor\log_2(\lfloor2^a/3^j\rfloor)\rfloor\), with color \(t\) at columns \(i\equiv t+j\pmod3\); it counts these progressions, forms the two color differences, then rotates by \(\omega^{-a}\). It checks both moment identities with their finite terminal corrections. It also verifies
\[
 m(\omega z)=m(z)-y,\qquad m(\omega^2z)=m(z)-x,\qquad m(x,y)=\min(0,x,y).
\]
Thus the corresponding horizontal rotated-minimum readouts have irrational differences given by the coordinate moments. This proves no assertion about the target density or cancellation against vertical and low-row contributions.

### Gaps

No independence of the 100 products, horizontal/vertical joint independence, algebraic independence, or finite invariant state partition is established. The affine-moment theorem supplies no target-affine relation to the density. Actual-module cut scope and the rational constant in zero relations must remain explicit.

## Does fixed-state scalar cancellation survive the actual occupation?

### Takeaway

It survives only with the state-flux correction. The displayed actual example has zero scalar coboundary readout at every fixed state but a strictly negative joint readout. This refutes omitting flux; it does not refute all state-dependent calibrations. — [Source claims CG7–CG9](coboundaries.md), [actual-board flux certificate](coboundary_audit_check.py).

### Cited Findings

- The accepted joint map is \(T(y,x)=(y+\Phi(x),Rx)\), with actual start \((1,0)\). The target normalization controls a specific full occupation value; it does not grant rationality of arbitrary guarded translated readouts. — [Accepted transport audit](../occupation-arithmetic-bridge/transport_audit.md), [occupation audit](../numerator-and-residuals/occupation_audit.md).
- The standalone checker derives \(Y_0,Y_1,Y_2\) from board counts, uses the actual minimum-cone test, checks the finite terminal flux identity for 24 blocks, and encloses the entire remaining flux tail. Its exact enclosure is
  \[
  \left[-\frac{4131944571720433692673}{33056565380087516495872},
        -\frac{4131944571720433692671}{33056565380087516495872}\right]
  \subset\left(-\frac{57}{448},-\frac{55}{448}\right).
  \]
  — [Standalone checker](coboundary_audit_check.py).

### Inferences

For bounded \(f\), define \(C_Rf=f(y,x)-f(y,Rx)/8\) and \(C_Tf=f(y,x)-f(y+\Phi(x),Rx)/8\). Pointwise subtraction and absolutely convergent telescoping yield
\[
 \Omega(C_Rf)=f(1,0)+\frac18\Omega\bigl(f(y+\Phi(x),Rx)-f(y,Rx)\bigr). \tag{A5}
\]
For a prefix through \(n=N-1\), the right-hand side also has terminal term \(-8^{-N}f(Y_N,x_N)\). Its sign and placement agree with the checker. A fixed-state phase reduction uses \(R\), whereas actual telescoping uses \(T\); A5 is the exact difference.

Take \(F(u,v)=\mathbf1_{\{u\le0, u\le v\}}\),
\[
 g(x)=\mathbf1_{\{\lfloor3x+\alpha\rfloor\equiv2\ (3)\}},\qquad
 f(y,x)=F(y-1)g(x).
\]
For any fixed state \(y\), the scalar discounted readout of \(C_Rf(y,\cdot)\) equals \(f(y,0)=0\), because \(g(0)=0\). But the actual board gives \(Y_0=1\), \(Y_1=1-\omega\), \(Y_2=2\). Consequently \(F(Y_0-1)=1\), \(F(Y_1-1)=0\). Certified logarithmic bounds give \(\lfloor4\alpha\rfloor=2\), \(\lfloor7\alpha\rfloor=4\), so \(g(x_1)=1\), \(g(x_2)=0\). The first flux term in A5 is \(-1/8\), and the next is zero. Every later undiscounted flux summand has absolute value at most \(1/8\); therefore
\[
 \left|\text{tail from }n=2\right|
 \le\frac18\sum_{n\ge2}8^{-n}=\frac1{448}.
\]
This proves the complete infinite enclosure
\[
 -\frac{57}{448}\le\Omega(C_Rf)\le-\frac{55}{448}<0.
\]
The sharper 24-block interval above uses the same complete tail argument, with tail \(8^{-24}/7\); no eventual pattern or uncomputed return is assumed.

The valid conclusion is that scalar closure cannot be applied independently at formal states while discarding its changing-state transfer flux. A calibration may still cancel that flux with other joint observables. The finite phase basis provides exact cancellation constraints for genuinely separated terms; it does not decide the required joint occupation arithmetic.

### Gaps

No target-affine calibration with a nonzero density coefficient, adequate integer-multiplier budget, complete low-row cancellation, or proof of Erdős #168 follows. Skipped Lean, historical-priority searches and external review. The remaining material risk is treating a finite numerical pure-phase module as closure of the unbounded joint state process.
