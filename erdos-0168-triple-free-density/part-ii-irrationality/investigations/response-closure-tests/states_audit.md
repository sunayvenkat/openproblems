# Independent audit of compatible child returns

## Does the Christoffel commutator justify the finite classification?

### Takeaway

**PASS.** The commutator and its two exact updates justify the necessary finite compatibility reduction. The twenty-four residue/phase states produce sixteen compatible current-side children, but this does not assert that every compatible case occurs infinitely often for the actual logarithm. — [Audited proof](general_states.md), [independent certificate](states_audit_check.py).

### Cited Findings

- The supplied checker passes, returning 24 reachable residue/phase states, 16 compatible cases, five same-sign cases, and no unresolved child-response sign. — [Supplied exact certificate](general_states_check.py).
- The independent checker imports only `fractions`. It constructs literal lower Christoffel words, evaluates transforms by the positions of their east steps, and reconstructs the finite graph without companion helpers. — [Independent certificate](states_audit_check.py).
- The balanced nonresonant mediant transforms are the four values already proved in the scalar construction. Their use here retains the actual short direct/reciprocal floor-word hypothesis. — [Accepted four-state theorem, SS2](../signed-arithmetic-returns/signed_scalar.md).

### Inferences

Write \(x=\rho(U)\), \(y=\rho(V)\) and
\[
C=(1-y)H(U)-(1-x)H(V).
\]
The lower-word concatenation rule gives
\[
C(U,UV)=xC(U,V),\qquad C(UV,V)=C(U,V).
\]
Both are exact substitutions, including when a parent is resonant. Starting from \(E,N\), for which \(C=1-\omega\), induction gives \(C=\omega^k(1-\omega)\). The independent literal-word check verifies the convention at the initial pair and at the actual pairs used in the certificates. — [GS1 and GS2](general_states.md), [literal-word replay](states_audit_check.py).

For \(h=H(UV)\) and \(xy\ne1\), the two equations
\[
h=H(U)+xH(V),\qquad
C=(1-y)H(U)-(1-x)H(V)
\]
have a unique complex solution, with
\[
H(V)=\frac{(1-y)h-C}{1-xy},\qquad H(U)=h-xH(V).
\]
Thus specifying a balanced **nonresonant** mediant, parent residues and phase legitimately determines both parent transforms. The independent implementation does not copy the source's division routine: it finds the unique Eisenstein solution by a bounded exact search, then verifies both equations. Uniqueness follows analytically from \(1-xy\ne0\), rather than from the search bound. — [GS3](general_states.md), [independent parent reconstruction](states_audit_check.py).

From the actual interval \(5/8<12/19\), the two residue updates have exactly 24 reachable states, one phase per determinant-minus-one residue pair. The certificate also enumerates every such residue pair directly and verifies equality of those sets. Every sufficiently late actual neighboring interval is a descendant along this Stern–Brocot path; the graph is therefore a necessary compatibility test for those intervals. Applying the balanced-mediant table and current-parent nonresonance leaves exactly the stated sixteen cases. — [Finite closure, GS2](general_states.md), [graph and residue replay](states_audit_check.py).

### Gaps

- Finite residue reachability does not prove that the full specified transforms, or any favorable class, recur infinitely along \(\log_3 2\). It is used only as a necessary finite list under the mediant-state assumption. — [Source scope](general_states.md).
- Sufficiently late actual intervals share the fixed short floor word. The entire initial interval need not already share every floor of index at most 23, so that additional domain condition must remain visible for individual early rational examples. — [SS2 and SS4](../signed-arithmetic-returns/signed_scalar.md).

## Are the child response signs valid even at resonant children?

### Takeaway

**PASS.** Every listed child has a complete quotient interval excluding zero; five have the mediant's sign, including four resonant cases. This is a statement about complete real jump values, not a borrowed nonresonant clearing denominator. — [GS5 and resonance argument](general_states.md), [independent response replay](states_audit_check.py).

### Cited Findings

- The toric factorization uses equal total minimum-count births on a complete rational grade. That conservation does not require \(p+q\not\equiv0\pmod3\). The universal coefficient bound remains \(3(1+b/p)\). — [SS1](../signed-arithmetic-returns/signed_scalar.md).
- The independent response calculation reconstructs the endpoint through its exact Eisenstein equation, computes short axis increments from integer powers of two and three, uses the explicit rectangle correction and all four low-row rules, and retains the full \(24\times24\) exterior bound. — [Independent certificate](states_audit_check.py).
- A separate original-token enumeration checks the entire \(24\times24\) quotient rectangle at the resonant rational \(65/103\). It starts with original \((a,b)\) labels and their actual retiming rules, grouping coincident effective points before computing minimum-count increments. — [Independent resonant certificate](states_audit_check.py).

### Inferences

Every omitted quotient coefficient is covered by the established absolute bound. For numerator \(p\ge24\), the tail after a \(24\times24\) rectangle is at most
\[
T_{24}=\frac{27}{2}2^{-24}+\frac{45}{2}3^{-24}.
\]
The short endpoint and coefficient formulas do not divide by \(1-\rho\); they therefore remain valid at the finite compatible resonant states. The negative-effective-exponent token remains included and has zero birth in the required slope interval. — [GS resonance proof](general_states.md), [SS1–SS2](../signed-arithmetic-returns/signed_scalar.md).

The original-token certificate has a proved finite grade cutoff. In \(3/5<p/q<2/3\), both retimings raise the original rational grade: the increases are \(q-p>0\) and \(2q-3p>0\). Thus every token of effective grade at most the cutoff is found by enumerating original nonnegative labels of raw grade at most that cutoff. No hidden model predecessor is omitted. Two opposite tie orders then give the quotient coefficients in the low rectangle, where \(b<p\). — [Independent cutoff and enumeration](states_audit_check.py).

All sixteen complete child responses have absolute value greater than \(1/10000\). The five same-sign classes reproduce the table in GS2 exactly; all have the current parent as the upper endpoint. Their three distinct child response enclosures are
\[
\begin{array}{c|c}
(p\bmod3,q\bmod3,H)&\mathcal Q(1/2,1/3)\\\hline
(2,1,1)&(-11/20,-27/50)\\
(1,2,1+\omega)&(77/100,79/100)\\
(1,0,0)&(-1/5000,-1/10000).
\end{array}
\]
The first two states are resonant. The five cases have four resonant children because those two states recur in four rows of the compatibility table. — [Exact source table](general_states.md), [independent sixteen-case certificate](states_audit_check.py).

### Gaps

- No rationality or cheap arithmetic clearing factor for a resonant scalar value is needed or proved here. Only its complete analytic jump is enclosed. — [Source scope](general_states.md).
- Eleven compatible cases have opposite response signs. Nonvanishing of their separate jumps does not rule out cancellation in the combined jump. This audit makes no new conclusion for them. — [Sign certificate](general_states_check.py).

## Does the full two-node cluster give the claimed asymptotic nonvanishing?

### Takeaway

**PASS, with the stated state hypotheses.** On the five same-sign classes, \(Q\ge3q\) gives eventual correct-side nonvanishing without either a bounded ratio \(Q/q\) or a condition on the following continued-fraction digit. Actual infinite adequate-gap supply remains unproved. — [GS3–GS4](general_states.md), [independent complete cluster certificate](states_audit_check.py).

### Cited Findings

- The prior scalar theorem gives an entire open-Farey variation bound \(\mathcal V\), including all later direct and reciprocal floor breaks, and has no resonance restriction for this variation estimate. — [SS3](../signed-arithmetic-returns/signed_scalar.md).
- The supplied and independent checkers reproduce the two-node leading-to-remainder ratio floors \(18318776\) at \(12/19\) and \(18168129295004104279455783313574041127430456078\) at \(53/84\). Their gaps and variation bounds use exact rational arithmetic. — [Supplied checker](general_states_check.py), [independent checker](states_audit_check.py).
- The required seed input is \(\log Q=o(q)\) at consecutive actual convergents. It supplies a growth scale, not the occurrence of favorable states. — [Seed normalization audit](../signed-arithmetic-returns/seed_arithmetic_audit.md).

### Inferences

Let the current and successor be \(p/q,P/Q\), put \((r,s)=(p+P,q+Q)\), \((t,u)=(2p+P,2q+Q)\), and use the current-side convention \(\sigma\). The actual slope lies beyond the mediant \(r/s\), while \(t/u\) lies between the current parent and that mediant. Both jumps are therefore crossed. All other jumps lie in the three open Farey pieces, giving
\[
\left|(Z-\widetilde Z^\sigma_{p,q})
-\sigma(J_{r,s}+J_{t,u})\right|
\le \mathcal V(p,q;t,u)+\mathcal V(t,u;r,s)+\mathcal V(r,s;P,Q).
\]
The current endpoint is excluded by its correct-side limit, and no successor endpoint jump is crossed. — [GS6–GS7](general_states.md).

Both nodes are on the same side of the actual slope. Their physical gap factors consequently have the same sign. On a favorable row their complete quotient responses also have the same sign, so
\[
|J_{r,s}+J_{t,u}|\ge |J_{t,u}|.
\]
Opposite consecutive errors \(\delta=q\alpha-p\), \(\delta'=Q\alpha-P\) satisfy \(|\delta'|<|\delta|\). Therefore
\[
|u\alpha-t|=|2\delta+\delta'|>|\delta|>\frac1{q+Q}.
\]
The uniform child-response lower bound and the small logarithmic-gap comparison give
\[
|J_{t,u}|\ge c_0\frac{2^{-(s+q)}}{q+Q}
\]
for one positive constant \(c_0\) eventually. This lower bound is on the **old \(q\) scale**, not an unjustified replacement of \(o(s)\) by \(o(q)\). — [GS8](general_states.md).

The three direct-index thresholds of the remaining intervals are \(s+2q\), \(2s+q\), and \(s+Q\). If \(Q\ge3q\), every term is \(O(2^{-(s+2q)})\). The vertical thresholds have the same physical logarithmic size because the two actual convergent errors tend to zero; all rational prefactors in \(\mathcal V\) are uniformly bounded. The ratio of the child lower bound to the remainder is thus at least a positive constant times
\[
\frac{2^q}{q+Q}\longrightarrow\infty,
\]
using \(\log Q=o(q)\). This proves the stated eventual correct-side nonvanishing. — [GS8–GS9](general_states.md).

### Gaps

- An actual infinite sequence in one of the five classes with \(Q-5q\to\infty\) remains missing. The new theorem would remove the earlier dominance-regime condition on that sequence; it does not supply the sequence or lower the nonresonant scalar denominator. — [Source final scope](general_states.md).
- The original cheap scalar clearing factor applies to the current nonresonant model. The resonant child is a jump contribution, not a new approximant with that denominator. — [Source scope](general_states.md).
- No substantive erratum was found. Both supplied and independent checkers pass. Skipped: Lean, external review, broader state searches, opposite-sign extensions and any claim of actual infinite supply. Material risk: treating this enlarged nonvanishing domain as the still-unproved adequate infinite return.
