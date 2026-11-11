# Independent audit of whole numerator residues

## Do the complete blocks give the claimed evaluated period residues?

### Takeaway

**PASS; no substantive erratum.** NN1–NN3 retain the four low rows and the single exceptional origin correction. The congruences concern the evaluated integer numerator. — [Audited notes](numerator.md), [independent checker](numerator_audit_check.py).

### Cited Findings

- The accepted rational model has horizontal period \(3q\), vertical high-row period \(3p\), four separate low rows and the admissible range \(3/5<p/q<2/3\). The exceptional \((0,1)\) birth is removed before horizontal periodization, then restored once. — [Accepted definition](../reflected-return-models/two_sided_models.md), [accepted evaluator](../reflected-return-models/two_sided_models_check.py).
- The standalone audit checker imports no project module. It reconstructs rational axes from root-of-unity partial sums, derives the color correction algebraically, and uses minimum differences for the high cone and third low row. Separate original retimed-token enumeration checks low, high and tie-sensitive births and the zero nonsmooth arrival. — [Independent implementation](numerator_audit_check.py).
- Both checkers pass. A separate read-only comparison confirms exact equality of all four full integer numerators with the accepted independent Horner evaluator, beyond equality of denominator bit lengths. — [Supplied checker](numerator_check.py), [independent checker](numerator_audit_check.py), [comparison evaluator](../correlated-return-arithmetic/arithmetic_audit_check.py).

### Inferences

Put \(a=2^q,b=3^p,A=a^3-1,B=b^3-1\). The definitions
\[
H_i=\sum_{r<q}\sum_{v=0}^3\bar c_{r+iq,v}2^{q-1-r}3^{3-v},
\qquad
T_{ij}=\sum_{r<q}\sum_{t<p}c_{r+iq,t+jp+4}2^{q-1-r}3^{p-1-t}
\]
give the complete periodic head value \(2\sum_i a^{2-i}H_i/(27A)\) and high-row value \(2\sum_{i,j}a^{2-i}b^{2-j}T_{ij}/(27AB)\). Restoring the original birth subtracts \(3/3=1\). Therefore, with
\[
W_i=BH_i+\sum_jb^{2-j}T_{ij},\qquad
Y_j=\sum_i a^{2-i}T_{ij},
\]
the full model is \(z=N/(27AB)\), where
\[
N=2\sum_i a^{2-i}W_i-27AB
=2B\sum_i a^{2-i}H_i+2\sum_jb^{2-j}Y_j-27AB.
\tag{A1}
\]
This verifies the factor two, high-row offset four and origin term. The independent implementation computes the full head/high rectangle separately from its nine-block decomposition and checks the geometric normalization with exact fractions. — [NN1–NN2](numerator.md), [independent complete periods](numerator_audit_check.py).

Reducing A1 gives the four true integer congruences:
\[
\begin{array}{c|l}
\text{modulus}&N\text{ residue}\\\hline
a-1&2\sum_iW_i\\
a^2+a+1&2((W_1-W_0)a+W_2-W_0)\\
b-1&2\sum_jY_j\\
b^2+b+1&2((Y_1-Y_0)b+Y_2-Y_0).
\end{array}
\tag{A2}
\]
The checker verifies the original moduli before stripping small primes. Vertically, the head and origin terms disappear because they are multiples of \(B\); horizontally the head remains in \(W_i\). The order-three reductions use \(a^2\equiv-a-1\) and its \(b\) analogue. They do not permit setting the two coefficients of a displayed linear expression to zero. — [NN3](numerator.md), [independent residue checks](numerator_audit_check.py).

The bounds \(\lvert T_{ij}\rvert\le(a-1)(b-1)\) and \(\lvert H_i\rvert\le80(a-1)\) follow from \(\lvert c\rvert\le2\). These varying coefficients already have exponential natural heights; writing nine blocks does not license a fixed-coefficient seed theorem. — [NN1 and scope](numerator.md).

### Gaps

- The accepted finite optimum, rational-model construction and period theorem are inputs, not globally reproved here. — [Accepted model source](../reflected-return-models/two_sided_models.md).
- A2 neither evaluates the actual response constants nor forces the required gcd saving. — [Explicit arithmetic gaps](numerator.md).

## Are the whole corrected valuations and axis gcds exact?

### Takeaway

**PASS.** NN4–NN8 isolate the successor smooth powers and reduce all remaining cancellation to two whole-model gcds and four coprime-within-axis factors. The fixed rational response hypothesis and \(h_3\ne0\) are essential. — [NN4–NN8](numerator.md), [independent checker](numerator_audit_check.py).

### Cited Findings

- Under the extra hypothesis \(\Gamma_j=h_j/T\), with fixed integer \(h_j\), \(T>0\),
  \[
  J=TUVN+27\sigma(VBP_h(a)-UAP_h(b)),\quad
  L=27TUVAB,\quad P_h(t)=h_1t^2+h_2t+h_3,
  \]
  where \(U=2^Q,V=3^P\). The corrected reduced denominator is exactly \(L/\gcd(|J|,L)\). — [Accepted normalization](../correlated-return-arithmetic/arithmetic_audit.md).
- The independent checker tests five fixed vectors/denominators against actual \(N\), \(N=0,1,-1\), and admissible synthetic modular numerators. — [Independent tests](numerator_audit_check.py).

### Inferences

Write \(s_2=v_2(B),s_3=v_3(A)\). Eventually
\[
v_2(P_h(a))=v_2(h_3),\qquad v_3(P_h(b))=v_3(h_3).
\]
If \(Q>s_2+v_2(h_3)\) and \(P>3+s_3+v_3(h_3)\), the \(VBP_h(a)\) term has uniquely least valuation at two and the \(UAP_h(b)\) term at three. Hence for **every integer \(N\)**,
\[
v_2(J)=s_2+v_2(h_3),\qquad
v_3(J)=3+s_3+v_3(h_3).
\tag{A3}
\]
LTE makes these thresholds eventual. They also put each valuation strictly below the corresponding valuation of \(L\), so no minimum with \(v_\ell(L)\) is omitted. — [NN4](numerator.md), [independent valuations](numerator_audit_check.py).

Define
\[
h_S=2^{v_2(h_3)}3^{v_3(h_3)},\quad
T_S=2^{v_2(T)}3^{v_3(T)},\quad T_0=T/T_S,
\]
\[
A_0=A/3^{s_3},\quad B_0=B/2^{s_2},\quad
g=\gcd(|J|,A_0B_0),\quad
e=\gcd(|J|,T_0A_0B_0)/g.
\]
Primewise comparison gives \(e\mid T_0\), even if \(T_0\) shares period primes. Consequently
\[
\gcd(|J|,L)=27\,2^{s_2}3^{s_3}h_Seg,\qquad
\operatorname{den}(z_*)=\frac{UVT_S}{h_S}\frac{T_0A_0B_0}{eg}.
\tag{A4}
\]
Both factors are integers eventually; the second is coprime to six. Thus the whole model cannot remove the successor smooth powers beyond fixed vector-dependent factors. Vectors with \(h_3=0\) are outside this claim. — [NN5](numerator.md), [independent exact reductions](numerator_audit_check.py).

Because \(V\) is a unit modulo \(A_0\) and \(U\) a unit modulo \(B_0\),
\[
g_A=\gcd(TUN+27\sigma BP_h(a),A_0)=\gcd(J,A_0),
\]
\[
g_B=\gcd(TVN-27\sigma AP_h(b),B_0)=\gcd(J,B_0).
\tag{A5}
\]
No inverse of \(T\), no coprimality between axes, and no reduced-original-numerator assumption is needed. At a prime with axis valuations \(\alpha,\beta\) and numerator valuation \(n\), the exponent of \(g_Ag_B/g\) is
\[
\min(n,\alpha)+\min(n,\beta)-\min(n,\alpha+\beta)
\in[0,\min(\alpha,\beta)].
\]
Thus \(g_Ag_B/g\) is an integer divisor of \(\gcd(A_0,B_0)\). — [NN6–NN7](numerator.md), [independent gcd assertions](numerator_audit_check.py).

The off-S pieces
\[
A_1=(a-1)/3^{v_3(a-1)},\quad
A_2=\Phi_3(a)/3^{v_3(\Phi_3(a))},\quad
B_1=(b-1)/2^{v_2(b-1)},\quad B_2=\Phi_3(b)
\]
are coprime within each axis and multiply to \(A_0,B_0\). This uses \(\gcd(t-1,\Phi_3(t))\mid3\), \(3\nmid b-1\), and oddness of \(\Phi_3(b)\). Substitution of A2 into A5 gives exactly all four corrected residues in NN8. At order-three factors the response polynomial becomes \((h_2-h_1)t+h_3-h_1\); at the linear factors it becomes \(h_1+h_2+h_3\). Within-axis gcds multiply exactly. — [NN8](numerator.md), [independent four-factor checks](numerator_audit_check.py).

### Gaps

- No implication \(Z\in\mathbb Q\Rightarrow\Gamma_j\in\mathbb Q\) is established. Nonzero actual third components justify \(h_3\ne0\) only if that fixed rational representation exists. — [Actual response arithmetic gap](../correlated-return-arithmetic/arithmetic_audit.md).
- The congruences allow cancellation. They do not bound the actual corrected denominator from below without controlling the actual \(g_A,g_B\). — [NN8–NN9 scope](numerator.md).

## What do the asymptotics and finite certificates actually establish?

### Takeaway

**PASS for NN9–NN12 and the synthetic example; no adequate infinite return is established.** The large axis and order-three savings are necessary for the present majorant to tend to zero, not lower bounds for the true residual or sufficient closure conditions. — [Audited deductions](numerator.md), [independent checker](numerator_audit_check.py).

### Cited Findings

- I independently read Corvaja–Zannier's original Corollary 1 and its integer gcd formulation. It supplies the subexponential gcd consequence for multiplicatively independent pairs in a fixed finitely generated group, with finitely many exceptions depending on the exponent and group. — [Primary Corollary 1, printed p. 2](https://arxiv.org/pdf/math/0311030v2#page=2).
- Both checkers pass. The standalone reconstruction gives reduced current-model denominator lengths \(44,108,507,2908\) bits at \(5/8,12/19,53/84,306/485\), respectively. — [Supplied checker](numerator_check.py), [independent checker](numerator_audit_check.py).

### Inferences

The pairs \((2^{3q},3^{3p})\) lie in the fixed group generated by \((2,1),(1,3)\); prime valuations exclude multiplicative dependence. Their decremented gcd is coprime to six. The primary theorem therefore gives \(\log\gcd(A,B)=o(q)\), with ineffective threshold. Combining it with A4–A5 and the convergent logarithm relations proves
\[
\log_2\operatorname{den}(z_*)
=2Q+6q-\log_2g_A-\log_2g_B+o(q).
\tag{A6}
\]
This identity concerns the **whole** corrected denominator, permits arbitrary integer \(N\), and is not a denominator lower bound. — [Primary theorem](https://arxiv.org/pdf/math/0311030v2#page=2), [NN9](numerator.md).

The unit majorant is exactly
\[
M_*=\operatorname{den}(z_*)2^{-q-2Q}
=\frac{UV}{2^{2Q}}\frac{T}{h_Se}\frac{A_0B_0}{2^qg}.
\tag{A7}
\]
The guaranteed actual error is less than \(300M_*\); A7 is not an asymptotic for that error. If this majorant tends to zero, A6 forces \(\log_2g_A+\log_2g_B\ge5q-o(q)\). Each axis has capacity at most \(3q+o(q)\), so each gcd is at least \(2^{2q-o(q)}\). Since each linear-factor capacity is \(q+o(q)\), both order-three gcds must be at least \(2^{q-o(q)}\). A smaller true correlated residual can escape these necessary majorant conditions. — [NN10–NN12](numerator.md), [factor-300 error input](../correlated-return-arithmetic/fan_audit.md).

When \(T\) is coprime to \(A_0B_0\), modular inversion chooses an artificial \(N\) making \(J\) divisible by the entire \(A_0B_0\). The checker confirms this. It demonstrates algebraic permission for full cancellation, not the actual birth-word numerator or an analytic fan identity for that artificial model. — [Synthetic example and caveat](numerator.md), [independent modular checks](numerator_audit_check.py).

The independent checker reconstructs all four full block decompositions, including \(306/485\); tests original moduli before stripping small primes; checks original-token births and the nonsmooth zero arrival; tests actual/artificial numerator valuations and exact reductions; verifies all four corrected residues and within/cross-axis gcd relations; and checks the complete affine value and exact unit majorant. It takes about \(2.9\) seconds using Python 3.14 and standard library only. A separate read-only comparison establishes equality of all four complete integer numerators with the accepted independent evaluator. No floating logarithm, solver, nominal-denominator substitution or finite-to-infinite extrapolation is used. — [Independent certificate](numerator_audit_check.py), [comparison evaluator](../correlated-return-arithmetic/arithmetic_audit_check.py).

### Gaps

- Actual response arithmetic, sufficient evaluated gcd savings, an infinite applicable family and any required corrected-residual nonvanishing remain separate obligations. This audit draws no conclusion about the parallel residual theorem. — [NN12 limitations](numerator.md).
- **Final disposition: PASS; no substantive erratum.** Skipped independent reconstruction of the entire accepted finite-cover foundation and Subspace Theorem, Lean, external review and priority verification. Material risk: treating fixed-vector conditional arithmetic or necessary majorant savings as an unconditional infinite return, or treating an artificial numerator as an actual model. — [Audited scope](numerator.md).
