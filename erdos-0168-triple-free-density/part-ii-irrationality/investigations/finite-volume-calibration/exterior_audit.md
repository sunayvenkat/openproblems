# Independent audit of positive exteriors and bounded real calibrations

## Are the complete box, shell and tail statements correct on actual support?

### Takeaway

**PASS; no substantive error in EX1–EX8.** The four-corner boxes, eight-corner shells, strict actual positivity and full tail bounds are valid. They yield positive small real quantities, without rationalizing any translated cone value. — [Audited note](<exterior.md>), [independent exact checker](<exterior_audit_check.py>).

### Cited Findings

- The accepted actual high occupation has atoms at \(\zeta_{a,b}=A_a+B_b-1+C_{a,b}-E_b\), weights \(2^{-a}3^{-b}\), domain \(a\ge0,b\ge4\), and total mass \(1/27\). Its actual fixed-row path \(\zeta_{3n,4}\) is unbounded. The complete normalization is \(Q_H=Q_{\rm full}-L\), \(Z=2-3Q_{\rm full}(0)\), where every low row is horizontally infinite and the exceptional birth at \((0,1)\) is already accounted for once. — [Independent occupation audit](<../numerator-and-residuals/occupation_audit.md>).
- The accepted height theorem is \(\max(|x|,|y|)\le C(a+b+1)^\kappa\), with fixed effective \(C>0\) and \(0<\kappa<1\). Its inverse is a **lower** bound on exterior arrival index. — [Independent height audit](<../occupation-arithmetic-bridge/height_audit.md>).
- Both the supplied checker and the new no-import checker pass. The new checker reconstructs the axes directly from original colored boards, the event corrections from original dyadic root windows, and selected Boolean births from original differences of minima. It uses integers and exact fractions only. — [Supplied checker](<exterior_check.py>), [independent checker](<exterior_audit_check.py>).

### Inferences

The coordinate conversion is exact:
\[
z=x+y\omega=s\omega+t\omega^2,
\qquad (s,t)=(y-x,-x),\qquad
\rho(z)=\max(|y-x|,|x|).
\]
Indeed \(s\omega+t\omega^2=-t+(s-t)\omega\). Both norm comparisons with factor two follow by the triangle inequality. The cone is \(F(z)=\mathbf1_{s,t\ge0}\); independently, \(F(z)=\min(0,x,y)-\min(0,x-1,y)\). — [Coefficientwise reconstruction and tests](<exterior_audit_check.py>).

Put \(q(s,t)=Q_H(-s\omega-t\omega^2)\). The actual atom at \(s\omega+t\omega^2\) is
\(q(s,t)-q(s+1,t)-q(s,t+1)+q(s+1,t+1)\). Summing over \([-R,R]^2\) gives exactly
\[
\mathcal B_R=Q_H(-R)-Q_H(-(R+1)\omega+R\omega^2)
-Q_H(R\omega-(R+1)\omega^2)+Q_H(R+1).
\]
The equivalent \((x,y)\) arguments are \((-R,0),(-R,-2R-1),(R+1,2R+1),(R+1,0)\). The checker also proves the stronger coefficientwise identity on every tested state before forming a finite positive occupation sum. No side term or normalization is missing. — [Independent exact checker](<exterior_audit_check.py>).

Since every lattice box is finite and actual support is infinite,
\[
\mathcal E_R^{\rm out}=1/27-\mathcal B_R=\nu^H\{\rho>R\}>0
\]
for **every** nonnegative integer radius. Set \(C_\rho=2C\), \(u=(R/C_\rho)^{1/\kappa}\) and \(m_R=\max(0,\lfloor u\rfloor)\). The strict exterior inequality forces \(a+b+1>u\), hence \(a+b\ge\lfloor u\rfloor\). This direction is correct even when \(u\) is an integer. The complete geometric tail, including every exterior cell, is
\[
0<\mathcal E_R^{\rm out}\le
\sum_{a+b\ge m_R}2^{-a}3^{-b}
=6\,2^{-m_R}-3\,3^{-m_R}\le6\,2^{-m_R}.
\]
The exact sum follows by summing all \(a\ge\max(m-b,0)\), then splitting \(b<m\) and \(b\ge m\). It overbounds the high domain safely; no upper escape-time assertion is needed. — [Accepted actual support](<../numerator-and-residuals/occupation_audit.md>), [height input](<../occupation-arithmetic-bridge/height_audit.md>), [full infinite-tail algebra](<exterior_audit_check.py>).

For \(a=3n,b=4\), the residue and event corrections are constant. Three root-unit horizontal increments give \(\rho\)-step at most three. Original-board reconstruction gives \(A_0=1,B_4=\omega,C_{0,4}=0,E_4=\omega\), so the path starts at zero. Its first crossing of any radius therefore lies in \(R<\rho\le R+3\). Consequently
\[
\mathcal E_R^{\rm sh}=\mathcal B_{R+3}-\mathcal B_R>0
\]
for every nonnegative integer radius, with the same upper tail and eight complete cone values. A crossing at index \(a=3n\) supplies weight \(8^{-n}3^{-4}>0\). The finite reconstruction reproduces first crossings \((R,a,z)=(0,3,(0,-1))\) and \((1,96,(1,-1))\); the infinite conclusion uses the accepted unboundedness theorem rather than extrapolation from these samples. — [Actual unboundedness proof](<../numerator-and-residuals/occupation_audit.md>), [independent original-board checker](<exterior_audit_check.py>).

The whole-kernel criterion is also sound. If \(\psi_R=0\) on \(\rho\le R\), \(0\le\psi_R\le C_R\), and it is positive either throughout a sufficiently far exterior or throughout the above shell, then
\[
0<\langle\psi_R,\nu^H\rangle\le C_R(6\,2^{-m_R}-3\,3^{-m_R}).
\]
A **proved** identity \(T_R\langle\psi_R,\nu^H\rangle=u_RZ+v_R\), with \(T_R>0,u_R,v_R\) integers and \(\log(T_RC_R)=o(R^{1/\kappa})\), would contradict rational \(Z=A/B\): its positive multiples \(BT_R\langle\psi_R,\nu^H\rangle=u_RA+Bv_R\) would be integers tending to zero. This counts both multiplier cost and kernel amplification; no separate height bound for \(u_R,v_R\) is required. — [Audited conditional criterion EX5–EX7](<exterior.md>).

### Gaps

- Neither box nor shell translation proves any cone value rational or integer-affine in the target. Replacing \(Q_H\) by \(Q_{\rm full}\) retains **all** translated infinite low-row corrections. — [Complete occupation arithmetic limitations](<../numerator-and-residuals/occupation_audit.md>).
- Global actual unboundedness, the finite optimum and the quantitative height theorem are accepted audited inputs here; they are not inferred from this finite checker. — [Occupation audit](<../numerator-and-residuals/occupation_audit.md>), [height audit](<../occupation-arithmetic-bridge/height_audit.md>).

## Do the outer inequalities hold, and can bounded real interior feasibility be proved?

### Takeaway

**PASS, with a valid strengthening.** The original small-offset ansatz has exactly the stated far-exterior margins. A larger offset proves a unique bounded real interior solution and positive residual at **every** exterior point, including interfaces. This is existence on the full lifted state/phase space; it supplies no finite rational-step representation or cheap rational source. — [Original EX9–EX11](<exterior.md>), [independent arithmetic checks](<exterior_audit_check.py>).

### Cited Findings

- The exact high adjoint is \(\mathcal L=216I-27U_A-8U_B+U_AU_B\), with \(\mathcal L1=182\). Its product pairing reduces to nine initial lifted values. The low adjoint is \(8I-U_A\), with constant eigenvalue seven and its own twelve initial values. — [ET5–ET8 and complete source normalization](<../occupation-arithmetic-bridge/exact_transport.md>), [independent transport audit](<../occupation-arithmetic-bridge/transport_audit.md>).
- Actual three-step state movements have \(\rho\)-bounds three horizontally, five vertically and eight jointly. The independent checker reconstructs actual axes from boards and also enumerates an overfamily of every three-step root-unit choice and every possible event-correction difference; its maxima are exactly \(3,5,8\). Thus the bound is uniform in phase, not a sampled typical-phase assertion. — [Exact checker](<exterior_audit_check.py>).

### Inferences

For the original \(p_\infty=(h+G+1)/182\), where \(h\) is Boolean and \(|g|\le G\), direct substitution gives
\[
\mathcal Lp_\infty-h-g=G+1-g+
\frac{34h-27h_A-8h_B+h_{AB}}{182}.
\]
The last integer numerator ranges from \(-35\) to \(35\) over all sixteen Boolean assignments. Therefore the bounds \(147/182\) and \(2G+217/182\) are correct. If the prescription holds outside radius \(R\), they apply automatically at current radius \(>R+8\). For the original low prescription the corresponding numerator \(h-h_A\) ranges from \(-1\) to one, giving bounds \(6/7\) and \(2G+8/7\) outside the width-three interface. These calculations require no invariant phase partition. — [Independent exact all-Boolean checks](<exterior_audit_check.py>).

Here is the stronger bounded-real statement. Fix one high residue block on the full lifted state/phase space \(X\), with actual commuting maps \(T_A,T_B\), Boolean target \(h\), and bounded forcing \(g\). Put
\[
D_R=\{\xi:\rho(\zeta(\xi))\le R\},\quad c=G+1,\quad
p(\xi)=c+h(\xi)/182\quad(\xi\notin D_R),\quad C_{\rm out}=c+1/182.
\]
On the Banach space of bounded real functions on \(D_R\), extend a candidate by these exterior values and define
\[
(\mathcal Tq)(\xi)=
\frac{27p(T_A\xi)+8p(T_B\xi)-p(T_AT_B\xi)+h(\xi)+g(\xi)}{216}.
\]
Two candidates differ by at most \(36\|q-q'\|_\infty/216=\|q-q'\|_\infty/6\). The contraction theorem gives one bounded fixed point and hence exact \(\mathcal Lp=h+g\) throughout \(D_R\). Its norm obeys
\[
\|p|_{D_R}\|_\infty\le\frac{36C_{\rm out}+c}{180}
=C_{\rm out}/5+c/180\le C_{\rm out}.
\]
This proof works on the actual physical-index domain too; the lifted formulation preserves the actual phase information. With Borel data, uniform iteration preserves Borel measurability. The domain contains all phase contexts above the finite state box and generally has infinitely many unknowns. It is not a finite-dimensional Dirichlet computation. — [Audited lifted maps and bounded pairing](<../occupation-arithmetic-bridge/exact_transport.md>), [exact contraction constants and extremal bounds](<exterior_audit_check.py>).

At **every** point outside \(D_R\), including the interface, current \(p\ge c\), every successor has absolute value at most \(C_{\rm out}\), and \(|h+g|\le c\). Consequently the whole residual \(K_R=\mathcal Lp-h-g\) satisfies
\[
K_R=0\quad(\rho\le R),\qquad
179c-18/91\le K_R\le252C_{\rm out}+c\quad(\rho>R).
\]
The lower bound follows from \(216c-36C_{\rm out}-c\); it is strictly positive because \(c\ge1\). This proves all real interface inequalities without using the displacement bound. The fixed-width bound remains useful for the smaller original ansatz. — [Independent extremal checker](<exterior_audit_check.py>).

For each low row use \(p=c+h/7\) outside \(D_R\). The interior fixed-point operator \(q\mapsto(p_A+h+g)/8\) has norm \(1/8\); with \(C_{\rm out}^{L}=c+1/7\), its solution has interior norm at most \((C_{\rm out}^{L}+c)/7\le C_{\rm out}^{L}\). Its residual satisfies
\[
K_R^L=0\quad(\rho\le R),\qquad
6c-1/7\le K_R^L\le9C_{\rm out}^{L}+c\quad(\rho>R).
\]
Thus high and low problems can all use target coefficient one, with nonnegative actual residuals. Taking \(g=0\) supplies uniform amplitudes independent of \(R\). The high component is strictly positive by actual infinite support, and its full exterior integral obeys the complete tail bound from the preceding section. The low-row state-height bound follows from the same actual-axis estimate and finitely many fixed low offsets after enlarging the constant, so the combined unexceptional residual has the same type of full-tail bound. — [Low/high state formulas and normalization](<../numerator-and-residuals/occupation_audit.md>), [actual-axis height proof](<../occupation-arithmetic-bridge/height_audit.md>), [independent exact constants](<exterior_audit_check.py>).

The arithmetic obstruction is explicit in the source. In the notation of ET4–ET8, put
\[
S_H=216\sum_{i,j=0}^2 2^{-i}3^{-b_j}
p_{ij}(1,V_{m_j},0,v_{m_j}),\quad (b_0,b_1,b_2)=(6,4,5),
\]
\[
S_L=8\sum_{i=0}^2\sum_{b=0}^3 2^{-i}3^{-b}p_{i,b}(1,0).
\]
These are finite linear combinations with rational coefficients, but their bounded-real Dirichlet values have **not** been proved rational. Boundedness legitimizes all exact infinite pairings and removal of terminal terms; it does not evaluate those initial values. If \(\Gamma\) denotes the full forcing readout, \(\Psi_R\) the full residual integral, and \(S_R=S_H+S_L\), transport gives precisely
\[
S_R=Q_{\rm full}(0)+\Gamma+\Psi_R,
\qquad Z=2-3S_R+3\Gamma+3\Psi_R.
\]
In particular \(g=0\) leaves a positive, uniformly bounded-amplitude, vanishing real residual and a potentially unknown source \(S_R\). The formal coefficient of the target is known, but proving rationality and cheap clearing of that source is the missing arithmetic theorem. This general bounded-real construction works for arbitrary bounded target data and therefore does not itself distinguish irrational targets. — [Exact finite-source product identity and low normalization ET6–ET8](<../occupation-arithmetic-bridge/exact_transport.md>), [complete target normalization](<../numerator-and-residuals/occupation_audit.md>).

### Gaps

- The smaller original outer prescription still lacks a proved useful finite rational-step interior/interface solution. The larger-offset argument **does** settle unrestricted bounded-real interior and interface existence; it does not settle existence in a finite rational phase ansatz or control the arithmetic of its initial values. — [Original ansatz scope](<exterior.md>), [explicit contraction proof above and exact constants](<exterior_audit_check.py>).
- A global pure-phase forcing requires a proved rational complete product-phase readout. Marginal irrationality or product-measure structure alone supplies no such rationality. A forcing multiplied by a state-region indicator is not pure phase and cannot use a scalar guard cancellation without additional proof. The contraction still handles it as bounded real data, which changes none of its arithmetic obligations. — [Transport and guard audit](<../occupation-arithmetic-bridge/transport_audit.md>), [EX6 forcing scope](<exterior.md>).

## Does compact mixed-Green clipping fail on actual occupied states?

### Takeaway

**PASS for the stated compact obstruction and the two actual signs.** It excludes a pure compact \(D_\omega D_{\omega^2}\) construction balancing a point source with a one-signed exterior. It does not exclude the full guarded discounted adjoint or the noncompact bounded-real construction above. — [Scoped obstruction EX7–EX8](<exterior.md>), [independent exact reconstruction](<exterior_audit_check.py>).

### Cited Findings

- For finite-support \(f\), each fixed row and column sum of its compact mixed Green difference vanishes by telescoping. The independent checker tests these marginals for arbitrary signed rational data and the natural clipped cones, as well as the explicit Green-rectangle stencil. — [Exact marginal checker](<exterior_audit_check.py>).
- For the coefficient-square cutoff \(\widetilde f_1=F\mathbf1_{\max(|x|,|y|)\le1}\), the independent checker reconstructs the specified physical cells from original boards and root windows, without importing accepted-axis code. — [Reconstruction and witness output](<exterior_audit_check.py>).

### Inferences

If \(D_sD_tf=\delta_0+e\), \(e(0)=0\), then \(e\ge0\) contradicts total sum zero. If \(e\le0\), write \(r=-e\ge0\). Zero row sums force \(r\) onto the zero row, and zero column sums force it onto the zero column; hence \(r\) is supported only at the forbidden origin. This also excludes the orientation \(\delta_0-r\) with nonnegative exterior \(r\). For \(f_R=\mathbf1_{0\le s,t\le R}\), direct telescoping yields
\[
D_\omega D_{\omega^2}f_R=
\delta_0-\delta_{(R+1)\omega}-\delta_{(R+1)\omega^2}+\delta_{-(R+1)}.
\]
This is an unweighted compact marginal argument, not a statement about signs after an occupation pairing. — [Independent coefficientwise stencil checks](<exterior_audit_check.py>).

For \(e_1=D_\omega D_{\omega^2}\widetilde f_1-\delta_0\), the reconstructed data are:

| Physical cell \((a,b)\) | \(A_a\) | \(B_b\) | \(C_{a,b}\) | \(E_b\) | Actual state \(\zeta\) | \(e_1(\zeta)\) |
|---|---|---|---|---|---|---:|
| \((12,8)\) | \(-\omega\) | \(-\omega\) | \(0\) | \(1\) | \(-2-2\omega\) | \(-1\) |
| \((22,35)\) | \(0\) | \(0\) | \(1+\omega\) | \(1\) | \(-1+\omega\) | \(+1\) |

These \((12,8),(22,35)\) are physical **index cells**, not state coordinates. Their states have occupation at least \(2^{-12}3^{-8}>0\) and \(2^{-22}3^{-35}>0\), respectively. Thus this specific square cutoff has both signs even on actual support. — [Exact original-board, root-window and minimum reconstruction](<exterior_audit_check.py>).

### Gaps

- The two witnesses do not determine the sign of \(\langle e_1,\nu^H\rangle\), prove actual mixed signs for every radius, or establish a no-go theorem for noncompact potentials, phase-dependent filters or the full discounted adjoint. — [Audited explicit scope](<exterior.md>).
- **Final disposition: PASS, with the bounded-real existence strengthening above.** No rational/cheap finite-source theorem, exact or approximate occupation arithmetic bridge, or proof of Erdős #168(ii) has been supplied. The independent checker passes original-board axes through index 159, actual triangle \(a+b<128\), coefficientwise boxes/shells, complete geometric tails, all-unit movement bounds, both occupied signs and both contraction estimates. — [Independent certificate](<exterior_audit_check.py>).
- Skipped Lean, installations, new branches, optimization, global finite-optimum reproofs and external theorem reproofs. Material risk: promoting a finite list of unknown bounded-real source values into rational constants, or describing unrestricted real contraction as a finite rational phase solution.
