# Same scale fan arithmetic and complete scalar normalization

## Does the correlated fan gain survive clearing its rational coefficients?

### Takeaway

The complete three-response fan has a precisely calculable arithmetic price. Its third coefficient alone has reduced-denominator exponent \(2Q+6q+o(q)\); clearing the vector separately therefore consumes the improved real-error scale. A general fixed-rational-vector classification accounts for both monomial cancellation at zero and cyclotomic axis cancellation. This is a price theorem for the fan correction, not an impossibility theorem for the complete corrected scalar approximation. — [Fan derivation](farey_fan.md), [exact arithmetic checker](same_scale_check.py).

### Cited Findings

- The new correlated fan uses consecutive actual convergents \(p/q,P/Q\), a nonresonant current model, and a balanced nonresonant first mediant. Put \(x=2^{-q},y=3^{-p},u=2^{-Q},v=3^{-P}\). Its three canonical actual response values \(G_1,G_2,G_3\) have coefficients
  \[
  C_j=\frac{ux^j}{1-x^3}-\frac{vy^j}{1-y^3},\qquad j=1,2,3,
  \]
  and the charged real remainder is \(O(2^{-q-2Q})\). No rationality of the actual \(G_j\) is proved. — [Complete fan construction and limitations](farey_fan.md).
- The accepted primary S-unit gcd input gives
  \[
  \log\gcd(2^{3q}-1,3^{3p}-1)=o(q)
  \tag{SS1}
  \]
  along these actual convergents. This is ineffective asymptotic information, not a finite bound at a named model. — [Earlier full application and exceptional-set check](../response-closure-tests/cheaper_audit.md), [Corvaja–Zannier, Corollary1 and Proposition2](https://arxiv.org/pdf/math/0311030v2).
- All eight response values occurring in the sixteen fan classes are nonzero. Each of the five unordered response triples has mixed signs and a rigorously nonzero complete sum. Their sums lie in \((-.124,-.123),(.188,.189),(1.113,1.114),(.718,.719),(-.163,-.162)\), respectively. Thus no triple is all equal and none sums to zero. — [Complete response enclosures, with both exterior strips](farey_fan.md), [exact fan checker](farey_fan_check.py).

### Inferences

Write
\[
a=2^q,\quad b=3^p,\quad U=2^Q,\quad V=3^P,
\quad A=a^3-1,\quad B=b^3-1.
\]
Then
\[
C_j=\frac{a^{3-j}}{UA}-\frac{b^{3-j}}{VB},
\qquad
C_3=\frac{VB-UA}{UVAB}.
\tag{SS2}
\]
These are exact identities, retaining the successor powers that a real-size estimate could conceal. The checker verifies them by independent `Fraction` construction. — [Exact SS2 certificate](same_scale_check.py).

**SS3. Exact eventual smooth part of the third denominator.** Let \(v_\ell\) denote prime valuation. Since \(A\) is odd and \(3\nmid B\), LTE gives \(v_2(B)=O(\log p)\) and \(v_3(A)=O(\log q)\). Eventually \(Q>v_2(B)\) and \(P>v_3(A)\). The two terms of \(VB-UA\) have different valuations at both primes, hence
\[
v_2(VB-UA)=v_2(B),\qquad
v_3(VB-UA)=v_3(A).
\]
Consequently the reduced denominator of \(C_3\) has **exactly** smooth part \(2^Q3^P\). Define \(A_0=A/3^{v_3(A)}\), \(B_0=B/2^{v_2(B)}\), and \(g=\gcd(A_0,B_0)\). Then
\[
UV\frac{A_0B_0}{g^2}\ \mid\ \operatorname{den}(C_3)\ \mid\ UV A_0B_0.
\tag{SS3}
\]
Indeed, at an off-\(\{2,3\}\) prime with unequal valuations in \(A_0,B_0\), the numerator has the smaller valuation; with equal valuations, the displayed lower divisor has exponent zero. This proves the left divisibility even if the equal-valuation terms cancel unusually strongly. Combining SS1–SS3 with \(p\log3=q\log2+o(1)\) and \(P\log3=Q\log2+o(1)\) gives
\[
\boxed{\log_2\operatorname{den}(C_3)=2Q+6q+o(q).}
\tag{SS4}
\]
The least integer clearing all three \(C_j\) has the same exponent: it is at least this denominator and divides \(UVAB\). — Proof above using [SS1](../response-closure-tests/cheaper_audit.md); [exact smooth-part and divisor checks](same_scale_check.py).

For named current/successor pairs \(12/19,41/65\), \(53/84,306/485\), and \(306/485,665/1054\), the third-coefficient denominator and the common vector denominator have respectively **238,1465,5013 bits**; they are equal in each example. The exact normalized independent majorant \(L_C2^{-q-2Q}\) exceeds \(2^{4q}\) in all three examples. This is not a lower bound on the true fan residual. — [Reproducible exact calculation](same_scale_check.py).

**SS5. Complete fixed-rational-vector classification.** Fix a nonzero rational vector \(g=(g_1,g_2,g_3)\), independently of \(q\), and set
\[
P_g(t)=g_1t^2+g_2t+g_3,\quad
\ell=\operatorname{ord}_{t=0}P_g,\quad
d=\deg\gcd(P_g,t^3-1).
\]
The rational fan correction is
\[
T_g=\sum_{j=1}^3 C_jg_j
=\frac{P_g(a)}{UA}-\frac{P_g(b)}{VB}.
\]
Its actual reduced denominator satisfies
\[
\boxed{\log_2\operatorname{den}(T_g)
=2\max(Q-\ell q,0)+2(3-d)q+o(q).}
\tag{SS5}
\]
Here the little-o constants may depend on the fixed rational vector; no coefficient is permitted to vary with \(q\) in this theorem.

To prove SS5, clear the fixed rational content and write
\(P_g(t)=t^\ell F(t)R(t)\), where \(F=\gcd(P_g,t^3-1)\) is monic and \(H=(t^3-1)/F\). Then \(R(0)\ne0\) and \(R,H\) are coprime. Each summand reduces to \(a^\ell R(a)/(UH(a))\) or \(b^\ell R(b)/(VH(b))\). A fixed nonzero resultant bounds \(\gcd(R(a),H(a))\) and \(\gcd(R(b),H(b))\), apart from the already cleared fixed content. The first summand's smooth denominator has logarithm
\([Q-\ell q]_+\log2+O(\log q)\); the second has
\([P-\ell p]_+\log3+O(\log q)\). The extra smooth valuations in \(H(a),H(b)\), being divisors of \(A,B\), are at most logarithmic by LTE. The off-S denominator sizes are \((3-d)q\log2+o(q)\) each. — Algebra from SS2; the fixed-resultant step follows by evaluating a polynomial Bézout identity.

The gcd of the two reduced summand denominators has logarithm \(o(q)\): its smooth part is at most the smaller, logarithmic smooth part on the opposite axis, and its remaining part divides \(\gcd(A,B)\) up to fixed factors, so SS1 applies. For reduced fractions with denominators \(d_1,d_2\), the denominator of their difference lies between \(d_1d_2/\gcd(d_1,d_2)^2\) and \(d_1d_2\). This follows prime by prime, including the equal-valuation cancellation case. Adding the two denominator logarithms therefore proves SS5. The conversions of positive parts use \((P-\ell p)\log3=(Q-\ell q)\log2+o(1)\), so the proof also covers \(Q<2q\). — [Accepted SS1 input](../response-closure-tests/cheaper_audit.md); [finite monomial/cyclotomic identity checks](same_scale_check.py).

Since \(\ell+d\le2\), SS5 implies
\[
\log_2\operatorname{den}(T_g)\ge2Q+2q-o(q).
\tag{SS6}
\]
The minimum types are \(P_g=c(t^2+t+1)\), \(ct(t-1)\), or \(ct^2\), the last reaching the minimum when \(Q\ge2q\). The other fixed polynomial types have the costs given by SS5, rather than a silently retained \(2^Q3^P\) factor. In particular, \(P_g=ct^2\) has cost \(6q+2[Q-2q]_+\), which is essential when \(Q<2q\). — Direct case split in SS5.

If an **actual** fan response vector were rational, the certified nonzero components force \(\ell=0\); its nonzero sum rules out the factor \(t-1\), and its mixed signs rule out a rational multiple of \(t^2+t+1\). Thus \(d=0\), and that actual rational correction would retain the **full** price \(2Q+6q+o(q)\). This inference is conditional on rationality of the response vector and says nothing about rationality following from \(Z\). — [Complete actual triple enclosures](farey_fan.md).

### Gaps

- A larger denominator for \(T_g\) is not a lower bound for \(\operatorname{den}(z+\sigma T_g)\). The complete scalar model can cancel additional axis factors. SS5 is not an adequate-return impossibility theorem. — [Exact scalar formula below](same_scale_check.py).
- A divergent separately cleared remainder bound is not a lower bound on the true correlated residual. Stronger cancellations may remain. The S-unit asymptotics are ineffective; the bit counts above are separate exact finite facts.

## What exact arithmetic saving would the complete corrected scalar need?

### Takeaway

There is a complete, reviewable interface for any proposed saving: it is a gcd of the **whole** corrected numerator. Even granting rational response values, the fan's improved analytic remainder does not automatically meet the arithmetic budget. Corrected-residual nonvanishing is also a new, separate obligation. — [Exact coefficient and affine checks](same_scale_check.py), [accepted scalar clearing](../weighted-response-identities/REPORT.md).

### Cited Findings

- The complete current scalar model has \(z=N/(27AB)\) for an integer \(N\), with all original low rows and exceptional corrections retained. This is a known clearer, not necessarily the reduced denominator of \(z\). — [Accepted full model](../reflected-return-models/two_sided_models.md).
- Rationality of \(Z\) has not been proved to imply rationality of the actual fan response values. The stronger scalar nonvanishing theorem concerns \(Z-z\); it is not a nonvanishing theorem for the residual after subtracting a fan correction. — [Uniform scalar theorem and scope](../weighted-response-identities/REPORT.md), [fan construction](farey_fan.md).

### Inferences

Suppose, as an additional hypothesis, a fixed actual response vector satisfies \(G_j=h_j/T\), with fixed integers \(h_j\), \(T>0\), and put \(P_h(t)=h_1t^2+h_2t+h_3\). Its fan-corrected approximation is
\[
z_*=z+\frac{\sigma}{T}\left(\frac{P_h(a)}{UA}-\frac{P_h(b)}{VB}\right)
=\frac{J}{L},
\]
where
\[
L=27TUVAB,\qquad
J=TUVN+27\sigma\bigl(VB P_h(a)-UA P_h(b)\bigr).
\tag{SS7}
\]
Therefore the **actual** reduced denominator is exactly
\[
b_* =\frac L{\gcd(|J|,L)}.
\tag{SS8}
\]
This retains every scalar numerator, successor prime power and response coefficient. It does not replace an actual gcd by a pole count. — [Exact named-model and trial-vector verification of SS7–SS8](same_scale_check.py).

For the unit normalized fan majorant,
\[
b_*2^{-q-2Q}
=27T(1+o(1))\frac{2^{5q}}{\gcd(|J|,L)}.
\tag{SS9}
\]
Thus the currently available fan-error estimate tends to zero after clearing precisely if \(\gcd(|J|,L)/2^{5q}\to\infty\) along the candidate sequence. This is an equivalence for this displayed **majorant**, not a necessary condition for a truly smaller correlated error. A successful full-model cancellation could in principle provide the required gcd, but none has been proved. — SS7–SS8 and \(UVAB=2^{2Q+6q}(1+o(1))\) along actual convergents.

An irrationality argument using \(z_*\) additionally needs \(Z-z_*\ne0\) infinitely often. It cannot inherit this from \(Z-z\ne0\): subtracting a nonzero leading fan correction changes the residual. The full needed interface is therefore actual value arithmetic, sufficient whole-numerator gcd saving or a stronger correlated error, an infinite applicable family, and corrected-residual nonvanishing. None is silently supplied by the real resummation. — [Scalar nonvanishing's exact scope](../weighted-response-identities/fixed_logs_audit.md), [complete fan residual](farey_fan.md).

### Gaps

- No theorem proves the response vector rational under rational \(Z\), the gcd saving in SS9, or corrected-residual nonvanishing infinitely often.
- The trial integer vectors in the checker verify arithmetic identities only; they are not asserted to be the actual response values. No actual adequate infinite arithmetic return is obtained.

## Do the new resonant response states provide a direct same-scale closure?

### Takeaway

The two new resonant profiles have simple exact color-dependent displacement formulas, but they do not produce a direct same-index affine identity with the target and the four old responses. An explicit eight-row determinant is \(-2187\). This is only a narrow pointwise certificate; weighted numerical identities remain possible. — [Resonant displacement proof SD4](state_supply.md), [exact rank and displacement checker](same_scale_check.py).

### Cited Findings

- The newly classified resonant states are \((p\bmod3,q\bmod3,H)=(1,2,1+\omega)\) and \((2,1,1)\), with canonical endpoint pair \(A_q^+=1,A_q^-=0\). Their complete high and low row response arrays are given by
  \[
  g_\pm(a,b)=-3\bigl[\Phi_b(z+D_j^\pm)-\Phi_b(z+D_j^\pm-1)\bigr],\qquad j=a-b\pmod3,
  \]
  \[
  D^+=(0,1,-\omega),\qquad D^-=(0,1+\omega,1).
  \]
  Here \(z\) is the original actual unexceptional state, \(\Phi_b\) uses the four separate low-row rules and the high cone rule, and the target's sole exceptional \((0,1)\) birth is handled separately. — [Written resonant algebra SD4](state_supply.md), [canonical response definitions](../response-closure-tests/response_relations.md).
- The new checker confirms these formulas against the canonical shifted-axis response construction on a \(96\times96\) actual rectangle, including rows0–3, using exact integer powers and the accepted actual axes. — [Independent displacement cross-check](same_scale_check.py).

### Inferences

For the constant, original target coefficients, four old balanced response arrays and these two resonant arrays, take the actual high-row cells
\[
(0,4),(0,5),(0,6),(0,8),(0,9),(0,11),(0,28),(2,4).
\]
The \(8\times8\) evaluation determinant is exactly
\[
\boxed{-2187=-3^7.}
\tag{SS10}
\]
The target entries are reconstructed independently from the global finite-cover formula, and the response entries use their complete canonical axis construction. Hence no nontrivial rational constant-coefficient same-index affine identity holds everywhere among these eight arrays. This extends the older six-array certificate to the two newly supplied resonant profiles. — [Actual row selection and exact determinant](same_scale_check.py), [accepted finite theorem](../prefix-and-phase-audit/REPORT.md).

The displayed cells include the horizontal boundary, so this says nothing about an identity valid only sufficiently far from every boundary. Applying a weighted sum can also annihilate a nonzero array. SS10 therefore does not establish rational independence of the eight weighted values, does not rationalize any resonant response from rational \(Z\), and does not prohibit an identity with complete boundary terms. — Linear-algebra scope of SS10; [previous analogous scope audit](../weighted-response-identities/weighted_audit.md).

### Gaps

- The exact checker passes with the installed Python3.14 interpreter using only the standard library and read-only imports from accepted helpers. No archived source was changed. Finite checks support the named algebra and determinant; SS3–SS6 are written asymptotic proofs.
- Skipped Lean, external review, new priority research, installations, larger searches and arithmetic evaluation of the actual response constants. Material risk: interpreting the fan-correction denominator price or the finite pointwise determinant as a prohibition on full scalar gcd cancellation or weighted special-value identities. No such global claim is made.
