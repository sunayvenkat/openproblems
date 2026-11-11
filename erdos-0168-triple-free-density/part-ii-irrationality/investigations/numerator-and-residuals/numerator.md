# Whole numerator residues and the two axis savings

## What are the complete scalar numerator's actual period residues?

### Takeaway

The complete numerator reduces to four explicit congruences on the genuine linear and order-three period factors. These formulas retain all four low rows and the exceptional origin correction. They concern the evaluated integer numerator, rather than a formal pole or the fan correction by itself. — [Accepted full scalar definition](../reflected-return-models/two_sided_models.md), [new exact checker](numerator_check.py).

### Cited Findings

- For a reduced nonresonant rational slope \(3/5<p/q<2/3\), the complete correct-side model is periodic horizontally with period \(3q\); its high rows are periodic vertically with period \(3p\). The low rows are separate and the original exceptional birth at \((0,1)\) is removed before horizontal periodization and then contributes the scalar correction \(-1\). — [Accepted model and proof](../reflected-return-models/two_sided_models.md), [accepted exact evaluator](../reflected-return-models/two_sided_models_check.py).
- The already audited integer Horner formula gives \(z=N/(27AB)\), where \(a=2^q,b=3^p,A=a^3-1,B=b^3-1\). This is a full integer numerator with a known clearer, not necessarily a reduced numerator. — [Independent prior evaluator](../correlated-return-arithmetic/arithmetic_audit_check.py), [prior complete-normalization audit](../correlated-return-arithmetic/arithmetic_audit.md).
- The new checker reconstructs the full period blocks from the accepted coefficient definition, compares their numerator exactly with the independently written integer Horner evaluator, and checks each of the four residue identities below. — [Exact certificate](numerator_check.py).

### Inferences

Write \(\bar c_{u,v}=1-3\bar\eta_{u,v}\) for the periodic coefficient rule before the single exceptional origin birth is restored. In particular \(\bar\eta_{0,1}=0\). For \(i,j\in\{0,1,2\}\), define the integer low-row and high-tile sums
\[
H_i=\sum_{r=0}^{q-1}\sum_{v=0}^3
\bar c_{r+iq,v}\,2^{q-1-r}3^{3-v},
\]
\[
T_{ij}=\sum_{r=0}^{q-1}\sum_{t=0}^{p-1}
c_{r+iq,t+jp+4}\,2^{q-1-r}3^{p-1-t}.
\tag{NN1}
\]
Every index and weight is finite and nonnegative. Set
\[
W_i=BH_i+\sum_{j=0}^2b^{2-j}T_{ij},\qquad
Y_j=\sum_{i=0}^2a^{2-i}T_{ij}.
\]
Factoring each Horner block gives the exact complete numerator
\[
\boxed{N=2\sum_{i=0}^2a^{2-i}W_i-27AB
=2B\sum_{i=0}^2a^{2-i}H_i
+2\sum_{j=0}^2b^{2-j}Y_j-27AB.}
\tag{NN2}
\]
To check the normalization directly, the four-row head has value \(2\sum_i a^{2-i}H_i/(27A)\); the periodically repeated high tile contributes \(2\sum_{i,j}a^{2-i}b^{2-j}T_{ij}/(27AB)\). Restoring the origin correction subtracts one, giving NN2. This derivation retains the entire low-row contribution; there is no uncomputed infinite strip inside an integer symbol. — [Accepted geometric summation](../reflected-return-models/two_sided_models_check.py), [independent equality check](numerator_check.py).

Define \(\Phi_3(t)=t^2+t+1\). Evaluation at the **integer** period factors gives
\[
\begin{array}{c|l}
\text{modulus}&N\text{ has the following residue}\\\hline
a-1&2(W_0+W_1+W_2)\\
\Phi_3(a)&2\bigl((W_1-W_0)a+W_2-W_0\bigr)\\
b-1&2(Y_0+Y_1+Y_2)\\
\Phi_3(b)&2\bigl((Y_1-Y_0)b+Y_2-Y_0\bigr).
\end{array}
\tag{NN3}
\]
For example, \(a^2\equiv-a-1\pmod{\Phi_3(a)}\) gives the second row. The vertical head and origin terms are multiples of \(B\), hence disappear from both vertical residues. Horizontally the head is retained in \(W_i\). These statements hold before stripping any small prime factors, so they also hold for all divisors used below. — NN2 and the elementary polynomial remainders; [exact four-residue tests](numerator_check.py).

These are scalar congruences. Neither coefficient of the displayed linear expression may be set to zero merely because the expression is divisible by \(\Phi_3(a)\). The coefficients contain complete model words and are large. Indeed \(|T_{ij}|\le(a-1)(b-1)\), \(|H_i|\le80(a-1)\), so their natural heights already grow exponentially with \(q\). No fixed-coefficient S-unit theorem is licensed by writing the nine-block formula. — Bounds from NN1 and \(|c|\le2\); [prior coefficient-scope audit](../signed-arithmetic-returns/seed_arithmetic_audit.md).

### Gaps

- NN3 has not been shown to match the actual response differences required by a cheap return. It exposes that comparison rather than assuming it. — [Actual response arithmetic remains open](../correlated-return-arithmetic/arithmetic_audit.md).
- No lower bound for the complete corrected denominator follows from the old formal pole matrices alone. Large evaluated integer gcd cancellation remains possible. — [Formal-versus-scalar scope](../reflected-return-models/two_sided_models.md).

## Which factors can the whole corrected numerator cancel?

### Takeaway

For a fixed rational response triple with nonzero third component, the whole corrected numerator has exact eventual valuations at two and three independently of \(N\). All remaining exponential saving is a simultaneous question about the two real period axes, with four explicit cyclotomic congruences. — [Full fan normalization](../correlated-return-arithmetic/same_scale.md), [new complete-normalization checker](numerator_check.py).

### Cited Findings

- For an actual fan class the full real correction is \(\sigma\sum C_j\Gamma_j\), with \(C_j=a^{3-j}/(UA)-b^{3-j}/(VB)\), \(U=2^Q,V=3^P\), and corrected residual bounded by \(300\,2^{-q-2Q}\). All actual third components are nonzero, but rationality of the triple under rationality of \(Z\) has not been proved. — [Complete fan audit](../correlated-return-arithmetic/fan_audit.md), [arithmetic scope](../correlated-return-arithmetic/arithmetic_audit.md).
- Under the **additional** fixed rational representation \(\Gamma_j=h_j/T\), the whole scalar numerator is
  \[
  J=TUVN+27\sigma\bigl(VB P_h(a)-UA P_h(b)\bigr),\quad
  L=27TUVAB,\quad P_h(t)=h_1t^2+h_2t+h_3.
  \]
  The corrected reduced denominator is exactly \(L/\gcd(|J|,L)\). — [Accepted full normalization and factor-300 audit](../correlated-return-arithmetic/arithmetic_audit.md).

### Inferences

**NN4. Exact eventual smooth valuations.** Fix integers \(h_1,h_2,h_3,T\), with \(T>0,h_3\ne0\). Put
\[
s_2=v_2(B),\quad s_3=v_3(A),\quad
h_S=2^{v_2(h_3)}3^{v_3(h_3)},\quad
T_S=2^{v_2(T)}3^{v_3(T)},\quad T_0=T/T_S.
\]
For sufficiently large \(q,p\), \(v_2(P_h(a))=v_2(h_3)\) and \(v_3(P_h(b))=v_3(h_3)\). If
\[
Q>s_2+v_2(h_3),\qquad P>3+s_3+v_3(h_3),
\]
the three terms in \(J\) have a unique lowest valuation at each smooth prime. Thus, for **every integer \(N\)**,
\[
\boxed{v_2(J)=s_2+v_2(h_3),\qquad
v_3(J)=3+s_3+v_3(h_3).}
\tag{NN4}
\]
LTE gives \(s_2,s_3=O(\log q)\), so these inequalities are automatic eventually along the actual convergents. The third component being nonzero is essential; vectors with \(h_3=0\) can have growing extra smooth cancellation and are outside NN4. All actual fan components are nonzero, so the condition is valid if their hypothetical fixed rational representation exists. — Direct valuation proof above; [exact complete-J checks with several fixed vectors and denominators](numerator_check.py).

Strip the small primes:
\[
A_0=A/3^{s_3},\qquad B_0=B/2^{s_2},\qquad
g=\gcd(|J|,A_0B_0),\qquad
e=\frac{\gcd(|J|,T_0A_0B_0)}g.
\]
Primewise, \(e\) is a positive divisor of the fixed integer \(T_0\), including when \(T_0\) shares primes with the period factors. NN4 gives the exact factorization
\[
\gcd(|J|,L)=27\,2^{s_2}3^{s_3}h_S\,e\,g,
\]
\[
\boxed{\operatorname{den}(z_*)=
\frac{UVT_S}{h_S}\,
\frac{T_0A_0B_0}{eg}.}
\tag{NN5}
\]
The first factor is an integer supported only at two and three for sufficiently late indices. The second is an integer coprime to six. In particular the exact smooth part of the full corrected denominator is \(UVT_S/h_S\), irrespective of \(N\). The model can cancel axis factors but cannot silently remove its successor smooth powers. — NN4 and the prime factorization of \(L\); [exact NN5 certificate](numerator_check.py).

**NN6. Exact two-axis residue gcds.** Since \(V\) is a unit modulo \(A_0\), and \(U\) a unit modulo \(B_0\),
\[
g_A:=\gcd(|J|,A_0)
=\gcd\bigl(TUN+27\sigma B P_h(a),A_0\bigr),
\]
\[
g_B:=\gcd(|J|,B_0)
=\gcd\bigl(TVN-27\sigma A P_h(b),B_0\bigr).
\tag{NN6}
\]
No inverse of \(T\), no coprimality of \(A_0,B_0\), and no assumption about a reduced original numerator is needed. Prime by prime,
\[
\frac{g_Ag_B}{g}\text{ is an integer divisor of }\gcd(A_0,B_0).
\tag{NN7}
\]
For period valuations \(\alpha,\beta\) and numerator valuation \(n\), the exponent of this ratio is \(\min(n,\alpha)+\min(n,\beta)-\min(n,\alpha+\beta)\), which lies between zero and \(\min(\alpha,\beta)\). This also checks equal-valuation cancellation, where informal multiplication of gcds could overcount. — Primewise proof above; [exact NN6–NN7 checks](numerator_check.py).

Now split the genuine period factors into coprime off-S pieces:
\[
A_1=\frac{a-1}{3^{v_3(a-1)}},\quad
A_2=\frac{\Phi_3(a)}{3^{v_3(\Phi_3(a))}},\quad
B_1=\frac{b-1}{2^{v_2(b-1)}},\quad B_2=\Phi_3(b).
\]
Then \(A_0=A_1A_2\), \(B_0=B_1B_2\), with \(\gcd(A_1,A_2)=\gcd(B_1,B_2)=1\). This uses \(\gcd(t-1,\Phi_3(t))\mid3\) and \(3\nmid b-1\); \(\Phi_3(b)\) is odd. Write \(s_h=h_1+h_2+h_3\) and \(R_h(t)=(h_2-h_1)t+h_3-h_1\). Combining NN3–NN6 gives the four explicit residues controlling \(g_A,g_B\):
\[
\begin{array}{c|l}
A_1&2TU\sum_iW_i+27\sigma B s_h\\
A_2&2TU((W_1-W_0)a+W_2-W_0)+27\sigma B R_h(a)\\
B_1&2TV\sum_jY_j-27\sigma A s_h\\
B_2&2TV((Y_1-Y_0)b+Y_2-Y_0)-27\sigma A R_h(b).
\end{array}
\tag{NN8}
\]
The gcd of each row with its modulus is exact; multiplying the two rows on each axis gives \(g_A\) or \(g_B\). These congruences are the complete model arithmetic interface, with the low-row asymmetry retained. — NN3 and NN6; [all four corrected residues checked independently of direct-J gcd reduction](numerator_check.py).

### Gaps

- No actual \(h/T\) representation has been established. All such uses are explicitly conditional. — [Open actual-response arithmetic](../correlated-return-arithmetic/arithmetic_audit.md).
- NN8 permits arithmetic cancellation; it does not prove it cannot occur. Its model-dependent coefficients vary with the actual period and cannot be treated as fixed rational coefficients or independent formal variables. — NN1–NN3 and [formal pole scope](../reflected-return-models/two_sided_models.md).

## Does the exact reduction produce a complete infinite arithmetic return?

### Takeaway

No adequate return is produced. The new reduction makes the required savings more precise: the current majorant needs simultaneous large **whole-model** gcds on both period axes, including large divisors of both order-three factors. Rational actual responses alone would not supply this. — [Current complete majorant](../correlated-return-arithmetic/arithmetic_audit.md), [new whole-model certificate](numerator_check.py).

### Cited Findings

- The accepted primary Corvaja–Zannier input gives \(\log\gcd(A,B)=o(q)\) along the actual convergents. The relevant integer S-unit pairs avoid the dependence exceptions by their valuations at two and three. This is ineffective asymptotic information; no finite numerical threshold is extracted here. — [Primary Corollary 1](https://arxiv.org/pdf/math/0311030v2#page=2), [accepted independent application](../correlated-return-arithmetic/arithmetic_audit.md).
- The guaranteed real fan bound is \(300\,2^{-q-2Q}\); its corrected residual needs a separate nonvanishing theorem. — [Complete fan audit](../correlated-return-arithmetic/fan_audit.md).

### Inferences

NN5–NN7 and the accepted cross-gcd bound give the new full-model asymptotic
\[
\boxed{\log_2\operatorname{den}(z_*)
=2Q+6q-\log_2g_A-\log_2g_B+o(q).}
\tag{NN9}
\]
This holds for the **whole corrected model**, not its correction alone, and allows arbitrary integer model numerators \(N\). The nontrivial terms are the actual residue gcds from NN6–NN8. It therefore does not become a denominator lower bound until these gcds are controlled. — NN5–NN7; [full-model exact tests](numerator_check.py).

Exactly, the unit majorant is
\[
M_*:=\operatorname{den}(z_*)2^{-q-2Q}
=\frac{UV}{2^{2Q}}\,
\frac{T_ST_0}{h_Se}\,
\frac{A_0B_0}{2^qg}.
\tag{NN10}
\]
The actual guaranteed error is strictly below \(300M_*\). Under its hypotheses this is identical to the earlier whole-J formula, now separated into explicitly retained smooth powers and genuine period savings. It is not an asymptotic for the actual residual. — NN5 and [accepted factor-300 normalization](../correlated-return-arithmetic/arithmetic_audit.md).

Since the two axis capacities have logarithms \(3q+o(q)\), if this **majorant** tends to zero then necessarily
\[
\log_2g_A\ge2q-o(q),\qquad
\log_2g_B\ge2q-o(q).
\tag{NN11}
\]
Indeed NN9 requires \(\log_2g_A+\log_2g_B\ge5q-o(q)\), while either summand is at most \(3q+o(q)\). Likewise the four coprime-within-axis factor capacities are \(q,2q,q,2q\), up to \(o(q)\). Consequently both quadratic-factor gcds in NN8 must satisfy
\[
\log_2\gcd(J,A_2)\ge q-o(q),\qquad
\log_2\gcd(J,B_2)\ge q-o(q).
\tag{NN12}
\]
These are necessary conditions for certification by the present majorant, not necessary conditions for all possible smaller actual errors. A stronger correlated residual could escape them. — NN7–NN10 and the exact period-factor degrees.

Conversely, the residue mechanism is algebraically capable of full cancellation. If \(T\) is coprime to \(A_0B_0\), then \(TUV\) is invertible there, and choosing an artificial integer \(N\) in the residue class
\[
N\equiv-27\sigma(VB P_h(a)-UA P_h(b))(TUV)^{-1}
\pmod{A_0B_0}
\]
makes \(g=A_0B_0\). This is not the actual scalar numerator and does not establish the analytic fan identity for that artificial model. It proves that an argument using only the abstract denominator shape and fixed \(h\) cannot prohibit the whole-model cancellation. The real task is to establish what the **actual** \(N\) from NN1–NN2 does. — Elementary modular inversion applied to NN5; no actual-return conclusion is drawn.

The checker passes the full block decomposition and all four residues at \(5/8,12/19,53/84\), compares complete numerators with the prior independent evaluator, and verifies NN4–NN8 for several fixed rational vectors at those models and \(306/485\). Their original correct-side reduced denominators have respectively 44,108,507,2908 bits. The vectors are algebra checks, not asserted actual responses. Runtime is approximately 1.2 seconds using the installed Python 3.14 and standard library, with read-only imports from accepted helpers. — [Reproducible certificate](numerator_check.py).

### Gaps

- No proof identifies rational values of the actual response triple under hypothetical rational \(Z\), forces the large whole-model gcds in NN11–NN12, or supplies an infinite applicable family. — [Explicit current arithmetic requirements](../correlated-return-arithmetic/arithmetic_audit.md).
- Corrected fan residual nonvanishing is being studied separately; it cannot be inherited from scalar nonvanishing. None of the modular calculations presumes its outcome. — [Accepted scope](../correlated-return-arithmetic/fan_audit.md).
- Skipped Lean, external review, fresh priority research, installations and reproof of accepted external theorems. Material risk: promoting exact four-factor formulas or necessary majorant savings into either actual arithmetic closure or a universal no-go theorem. Neither is established here.
