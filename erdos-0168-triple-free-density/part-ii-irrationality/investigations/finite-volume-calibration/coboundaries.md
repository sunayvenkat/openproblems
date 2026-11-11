# Scalar guard cohomology and retained state flux

## When is a discounted finite rational step guard rational?

### Takeaway

For a right-continuous finite rational step function under an irrational circle rotation, rationality of its discounted value at **one** starting phase is equivalent to an exact finite rational discounted coboundary. A finite weighted jump test gives a constructive complete criterion. Arbitrary endpoint overrides require a separate finite rational correction; ignoring that qualification makes the functional converse false. — [Exact algebra and actual-orbit checker](coboundaries_check.py).

### Cited Findings

- The accepted actual guards are finite step functions of the floors \(\lfloor3x+s\alpha\rfloor\bmod3\), with \(\alpha=\log2/\log3\), horizontal discount \(1/8\), and vertical analogues at \(\beta=1/\alpha\), discount \(1/27\). Their individual irrationality did not establish independence of linear combinations. — [ET1–ET10](../occupation-arithmetic-bridge/exact_transport.md), [guard audit](../occupation-arithmetic-bridge/guard_audit.md).
- Ordinary discounted telescoping has appeared in the archived work; this note does not call that elementary identity a discovery. The additions below are the converse, complete orbit-charge criterion, fixed numerical guard module and explicit state-flux limitation. No historical priority is checked. — [Earlier weighted cancellation](../infinite-return-construction/weighted_returns.md), [exact transport scope](../occupation-arithmetic-bridge/transport_audit.md).

### Inferences

**CG1. Complete scalar converse.** Let \(R(x)=x+\theta\pmod1\), with irrational \(\theta\), and let \(b\ge2\) be an integer. For a right-continuous finite rational step function \(h\), define
\[
U_h(x)=\sum_{n\ge0}b^{-n}h(R^nx).
\]
The following are equivalent:

1. \(U_h(x_0)\in\mathbb Q\) at one phase \(x_0\).
2. There is a finite right-continuous rational step function \(f\) with
   \[
   h=f-b^{-1}f\circ R.
   \tag{CG1}
   \]
3. \(U_h(x)\in\mathbb Q\) for every phase; in fact \(U_h=f\).

Here finite step means finitely many circle cuts and constant rational values on the half-open arcs. No endpoint is left unspecified. The proof is self-contained. — [Finite reconstruction and carry tests](coboundaries_check.py).

Multiply \(h\) by a common integer denominator, so its values are integers. Uniform convergence gives a bounded right-continuous \(U=U_h\), and
\[
U(Rx)=bU(x)-bh(x).
\tag{CG2}
\]
If \(U(x_0)=r/s\), this recurrence puts every value on the dense forward orbit of \(x_0\) in \(s^{-1}\mathbb Z\). Right continuity lets that orbit approach each phase from the right, so **every** value of \(U\) lies in the same bounded finite rational lattice. Choose a partial sum \(U_M\) with uniform tail smaller than \(1/(3s)\). On each arc of its finite step partition, any two values of \(U\) differ by less than \(2/(3s)\), and hence coincide. Thus \(U\) itself is a finite rational step function. Equation CG2 supplies CG1. Conversely CG1 telescopes, with terminal term \(b^{-M}f(R^Mx)\to0\). Undoing the initial denominator does not change the conclusion. This argument uses uniform convergence and right continuity, rather than assuming that irrationality of individual guards implies independence. — [Exact telescoping/reconstruction checker](coboundaries_check.py).

**CG2. Finite orbit-charge test.** Write \(J_h(c)=h(c+)-h(c-)\). Group the finitely many nonzero jumps into their rotation orbits. On one orbit choose \(c_j=c_0+j\theta\), \(j\in\mathbb Z\), and let
\[
\mathcal C_{[c_0]}(h)=\sum_j b^{-j}J_h(c_j).
\tag{CG3}
\]
The sum is finite. Changing the base representative only multiplies the charge by a nonzero power of \(b\). Then
\[
\boxed{U_h(x_0)\in\mathbb Q\iff
\mathcal C_{\mathcal O}(h)=0\quad\hbox{for every cut orbit }\mathcal O.}
\tag{CG4}
\]
To prove this, the jumps \(v_j=J_f(c_j)\) of a transfer must satisfy
\[
J_h(c_j)=v_j-b^{-1}v_{j+1}.
\]
If the guard jumps have support in \([m,M]\), start with \(v_{M+1}=0\) and solve backwards:
\[
v_j=\sum_{k=j}^{M}b^{j-k}J_h(c_k).
\tag{CG5}
\]
This has finite support on the left exactly when CG3 vanishes. For a genuine circle step function, \(\sum_cJ_h(c)=0\). Summing the recurrence therefore gives \((1-b^{-1})\sum_cv(c)=0\), so the reconstructed finite jumps integrate to a circle step function \(f_0\) with rational values. The remaining difference \(h-f_0+b^{-1}f_0\circ R\) is a rational constant \(C\). Adding \(C/(1-b^{-1})\) to \(f_0\) proves CG1 exactly. This is an effective finite linear test once the cut-orbit equivalences are known. — [Finite orbit recurrence certificate](coboundaries_check.py).

**CG3. Endpoints and carries.** If a finite step rule uses arbitrary rational values at its finitely many endpoints, replace it by the canonical right-continuous version \(h^+\). Each exceptional point can be met at most once on an irrational forward orbit. Thus \(U_h(x_0)-U_{h^+}(x_0)\) is a finite rational sum of powers of \(b^{-1}\). The rationality criterion CG4 is unchanged, but the functional identity CG1 applies to the canonical function. A singleton spike has rational readout at every start but generally requires infinitely many point spikes in its transfer; it is a counterexample to claiming the original arbitrary endpoint rule itself has a finite step transfer. — [Endpoint argument above; exact finite telescoping tests](coboundaries_check.py).

There are nonconstant integer-valued guards with rational readout. For any proper interval indicator \(p\),
\[
h=bp-p\circ R\quad\Longrightarrow\quad U_h(x)=bp(x).
\tag{CG6}
\]
Its values can include \(-1,b-1,b\), so the no-carry proof for Boolean digits cannot be used. In the actual horizontal drift notation, \(\Phi_2-9\Phi_1=\Phi_1\circ R-8\Phi_1\) likewise has rational \(\mathbb Q[\omega]\)-valued readout. — [Actual pointwise/carry certificate](coboundaries_check.py).

### Gaps

- CG1–CG4 classify scalar finite-step phase readouts. They do not classify functions of the accumulated unbounded state, nor do they evaluate the density or any translated occupation cone.
- No historical novelty claim is made. No external classification theorem is needed for the proof given here.

## What finite numerical module do the actual guards occupy?

### Takeaway

All finite horizontal floor-residue guard values lie in a fixed **ten-dimensional rational vector space**: rational constants plus nine fixed guard values. Their rational-linear relations are exactly the nine orbit-charge equations. This is a numerical readout reduction, not a finite invariant phase partition. — [Actual nine-basis and charge checker](coboundaries_check.py).

### Cited Findings

- Actual positive-offset horizontal cuts have the form
  \[
  c_{s,k}=(k-s\alpha)/3\pmod1,\qquad s\in\mathbb Z_{>0},\ k=0,1,2.
  \]
  The accepted exact transport proves their distinctness and their nonzero drift jumps. — [ET9](../occupation-arithmetic-bridge/exact_transport.md), [independent transport audit](../occupation-arithmetic-bridge/transport_audit.md).
- For the actual drift \(\Phi\), the jump at \(c_{r,k}\), \(r=1,2,3\), is \(\omega^{-r+2k}\). The checker independently reconstructs these jumps by exact logarithmic interval isolation and values on both adjacent phase cells. — [Exact certificate](coboundaries_check.py).

### Inferences

**CG4. Exactly nine cut orbits.** Irrationality of \(\alpha\) gives
\[
c_{s,k}-c_{s',k'}\in\mathbb Z\alpha+\mathbb Z
\iff s\equiv s'\pmod3,\quad k\equiv k'\pmod3.
\tag{CG7}
\]
Indeed comparing rational coefficients in
\((k-k')/3-(s-s')\alpha/3=j\alpha+\ell\)
forces both displayed divisibilities. Use representatives \(c_{r,k}\), \(r=1,2,3\). If \(s=r+3m\), then \(c_{s,k}=R^{-m}c_{r,k}\). A finite actual guard \(h\) is therefore rational-discounted exactly when its nine charges
\[
C_{r,k}(h)=\sum_{m\ge0}8^mJ_h(c_{r+3m,k})
\tag{CG8}
\]
vanish. Zero jumps may be omitted. The same equations classify every rational-linear combination of finitely many such guards. — [CG1–CG5; exact actual orbit charges](coboundaries_check.py).

**CG5. A fixed basis.** Designate the orbit \(0=(3,0)\), put \(c_0=c_{3,0}=-\alpha\), and let \([u,v)\) mean the positively oriented half-open circle arc. Take the eight guards
\[
B_i=\mathbf1_{[c_0,c_i)},\qquad i=(r,k)\ne(3,0),
\]
and the ninth
\[
B_0=\mathbf1_{[c_0,c_{6,0})}.
\]
All these are Boolean functions of the floor residues with offsets \(1,\ldots,6\). One floor residue first distinguishes three arcs of length \(1/3\); the remaining floor residues each change at most once inside each such arc. Hence their complete code distinguishes the refined phase atoms, and every displayed arc is a union of those atoms. This is checked explicitly on all eighteen circle cells. — [Exact Boolean-cell/basis certificate](coboundaries_check.py).

Their charge columns are
\[
C(B_i)=e_0-e_i\quad(i\ne0),\qquad
C(B_0)=(1-8)e_0=-7e_0.
\tag{CG9}
\]
The matrix has determinant \(-7\). If \(C(h)=(C_i)_i\), define
\[
a_i=-C_i\ (i\ne0),\qquad
a_0=-\frac{\sum_iC_i}{7}.
\]
The remainder \(h-\sum_i a_iB_i\) has all charges zero. Reconstructing its rational transfer \(f\) gives the exact numerical reduction
\[
\boxed{G_h= f(0)+\sum_{i=0}^{8}a_iG_{B_i}.}
\tag{CG10}
\]
Moreover \(1,G_{B_0},\ldots,G_{B_8}\) are rationally independent: a rational relation would, by CG4, put a nonzero vector in the kernel of CG9. Thus this is exactly a ten-dimensional rational numerical space, not merely an upper bound. — [Charge inverse and actual cell tests](coboundaries_check.py).

If offsets are bounded by \(M\), guard values have common denominator \(D\) and magnitude at most \(H\), the charges, basis coefficients and a reconstructed transfer have rational bit heights
\[
O\bigl(M+\log(2+D)+\log(2+H)\bigr).
\tag{CG11}
\]
For the charges this follows by a geometric sum of \(8^m\) up to \(m\le(M-1)/3\). Reconstruction CG5 adds only the opposite powers up to the same order; integration and the constant adjustment add fixed factors and at most a logarithmic number-of-cuts loss. This is a scalar coefficient budget, not an occupation-bridge multiplier bound. — [Constructive formulas CG5, CG8–CG10; finite exact reconstruction](coboundaries_check.py).

The identical proof at \(\theta=\beta\), \(b=27\), gives nine vertical pure-phase generators modulo rationals, with \(-26e_0\) in place of \(-7e_0\). Consequently a finite **rational-valued** two-phase step function constant on a finite rectangle refinement has a pure product-measure readout in an **at-most one-hundred-dimensional** rational span of the ten horizontal and ten vertical generators. Functions valued in \(\mathbb Q[\omega]\) are handled coordinatewise. The product-measure factorization is legitimate here because these tests have no state dependence. No independence of the one hundred products, or of horizontal and vertical generators together, is asserted. — [Scalar proof CG1–CG10 and accepted product measure](../occupation-arithmetic-bridge/exact_transport.md).

**CG6. Actual affine moment application.** Let \(Y_n=A_{3n}\), \(M_A=\sum_{n\ge0}8^{-n}Y_n\). Bounded increments ensure convergence. The actual recurrence gives
\[
G_\Phi=7M_A-8.
\tag{CG12}
\]
Each of its nine charge vectors is the nonzero unit \(\omega^{-r+2k}\). They include \(1\) and \(\omega\), so any nonzero rational coordinate functional \(\ell:\mathbb Q[\omega]\to\mathbb Q\) has a nonzero charge. CG4 proves \(G_{\ell\Phi}\) irrational. Therefore
\[
1,\quad \operatorname{coord}_1(M_A),\quad
\operatorname{coord}_\omega(M_A)
\quad\hbox{are rationally independent.}
\tag{CG13}
\]
Here coordinates are lattice coefficients, not the usual complex real and imaginary parts. The same statement holds for the complete horizontal moment \(M_A^{\rm all}=\sum_{a\ge0}2^{-a}A_a\), because
\[
M_A^{\rm all}=2+\frac14G_{\Phi+2\Psi_1+\Psi_2}.
\]
Its jumps are the same unit directions multiplied, at offsets \(1,2,3\), by \(4,2,1\), respectively. The checker verifies both identities against direct original colored-board axes with exact finite terminal terms. — [Actual moment certificates](coboundaries_check.py), [accepted exact lift](../occupation-arithmetic-bridge/exact_transport.md).

For the minimum potential \(m(x,y)=\min(0,x,y)\), the exact rotation formulas are \(m(\omega z)=m(z)-y\) and \(m(\omega^2z)=m(z)-x\). Thus the discounted horizontal minimum potentials at these rotations have irrational differences given by the two coordinate moments. This is a value-level reason that a rotation's linear correction cannot simply be replaced by a rational constant. It neither proves irrationality of the density nor rules out cancellation with the vertical or low-row terms. — [Rotation formulas](../occupation-arithmetic-bridge/exact_transport.md), [CG12–CG13 and exact moment checks](coboundaries_check.py).

### Gaps

- The fixed ten-dimensional closure concerns pure phase numerical readouts. It is not an invariant phase partition and does not make accumulated state periodic.
- The ten horizontal and ten vertical bases need not be jointly independent. No algebraic independence is proved.
- Irrational affine state moments are not the target cone value \(Z\); no relation rationalizing them under rational \(Z\) is supplied.

## What happens when the phase reduction is used inside the actual cone process?

### Takeaway

Scalar phase coboundaries acquire an explicit state-flux term in the actual skew product. An exact actual counterexample shows that dropping this term can turn a nonzero cone readout into a falsely asserted zero. The finite pure-guard module is useful cancellation data, but no occupation arithmetic bridge has been constructed. — [Complete retained-flux checker](coboundaries_check.py).

### Cited Findings

- The actual skew map is \(T(y,x)=(y+\Phi(x),Rx)\), with \(Y_0=1\), and its discounted occupation satisfies \(\Omega(f)=f(1,0)+\Omega(f\circ T)/8\). State-only update already has an exact counterexample. — [Complete transport and audit](../occupation-arithmetic-bridge/transport_audit.md).
- Accepted positive occupation returns require a target-affine identity with nonzero density coefficient. Rationality of \(Z\) controls only \(Q_{\rm full}(0)=(2-Z)/3\), not arbitrary guarded or translated cone values. — [Exact occupation normalization and bridge gap](../numerator-and-residuals/occupation_audit.md).

### Inferences

**CG7. Retained state flux.** For bounded \(f(y,x)\), put
\[
C_Rf(y,x)=f(y,x)-\tfrac18f(y,Rx),\qquad
C_Tf(y,x)=f(y,x)-\tfrac18f(y+\Phi(x),Rx).
\]
Exactly,
\[
C_Rf=C_Tf+\tfrac18\bigl[f(y+\Phi(x),Rx)-f(y,Rx)\bigr],
\]
and hence
\[
\boxed{\Omega(C_Rf)=f(1,0)+\tfrac18\Omega\bigl(f(y+\Phi(x),Rx)-f(y,Rx)\bigr).}
\tag{CG14}
\]
A finite prefix has the additional terminal term \(-8^{-M}f(Y_M,x_M)\). This proof needs only absolute convergence. When the state-dependent transfer is locally constant in the state variable, its extra flux vanishes there; if it varies only near a state boundary, the flux localizes there. **Its sign and arithmetic are not automatic.** — [Exact finite-terminal state-flux certificate](coboundaries_check.py).

Thus applying CG10 separately at each formal state \(y\) can reduce pure phase coefficients, but the associated transfers must use CG14 under the actual occupation. The residual flux is a joint state-and-phase readout. Setting it to zero would be the same unproved decoupling that the accepted scalar-correlation example already refutes. — [Previous actual correlations](../occupation-arithmetic-bridge/guard_audit.md), [CG14 exact checker](coboundaries_check.py).

**CG8. Actual nonzero flux despite zero fixed-state phase values.** Take
\[
g(x)=\mathbf1_{\{\lfloor3x+\alpha\rfloor\equiv2\ (3)\}},
\qquad f(y,x)=F(y-1)g(x).
\]
For every fixed \(y\), the scalar phase readout of \(C_Rf(y,\cdot)\) telescopes to \(f(y,0)=0\), since \(\lfloor\alpha\rfloor=0\). Nevertheless its actual skew readout is negative. Direct original-board values give \(Y_0=1,Y_1=1-\omega\), so \(F(Y_0-1)=1,F(Y_1-1)=0\). Also \(g(\alpha)=1\) and \(g(2\alpha)=0\), because \(\lfloor4\alpha\rfloor=2\) and \(\lfloor7\alpha\rfloor=4\). The first state-flux term in CG14 is \(-1/8\), the next is zero, and the entire remainder has absolute value at most
\[
\frac18\sum_{n\ge2}8^{-n}=\frac1{448}.
\]
Consequently
\[
\boxed{-\frac{57}{448}\le\Omega(C_Rf)\le-\frac{55}{448}<0.}
\tag{CG15}
\]
The exact checker independently encloses the full value strictly inside this range from sixteen original-board steps and the complete remaining flux tail. This is an actual cone/phase counterexample, not a hypothetical correlation or extrapolation. — [Original-board, complete-tail and flux checks](coboundaries_check.py).

**CG9. What is supplied to finite-volume calibration.** The nine charge equations and explicit fixed basis provide finite rational cancellation constraints for any pure guard terms that truly separate from the accumulated state. Products give a sufficient finite spanning family for pure two-phase terms without asserting independence. CG14 identifies the extra state flux when coefficients depend on state. A successful calibration must cancel or control that flux, the remaining basis-coefficient readouts and every complete low row, while retaining a nonzero coefficient of \(Z\). No such calibration or cheap integer multiplier is proved here. — [CG4–CG15; accepted target normalization](../numerator-and-residuals/occupation_audit.md).

### Gaps

- No exact or approximate identity \(T_n\nu^H(z_n)=u_nZ+v_n\) satisfying the needed multiplier/error budget is obtained. No adequate infinite density arithmetic return or proof of Erdős #168(ii) follows.
- The scalar classification imposes no lower bound on all bridge multipliers and no prohibition on more elaborate joint-state cancellations.
- Skipped Lean, external review, historical-priority verification, broad literature searches and larger filter enumeration. Material risk: confusing a finite numerical pure-guard basis with finite closure of the state-and-phase occupation process.
