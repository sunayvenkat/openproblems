# Corrected fan residual nonvanishing

## Can the corrected full fan residual be proved nonzero?

### Takeaway

**Yes on a precise new subfamily.** For every sufficiently late applicable balanced-parent pair whose following continued-fraction digit is at least two, the corrected full-fan residual is nonzero, with a uniform relative expansion governed by the successor-side child. This concerns the corrected residual itself, not an inference from scalar nonvanishing. No actual infinite supply or arithmetic closure is obtained. — [Exact new checker](corrected_residual_check.py), [accepted complete fan](../correlated-return-arithmetic/farey_fan.md).

### Cited Findings

- For consecutive actual convergents \(p/q,P/Q\) of \(\alpha=\log2/\log3\), the current model is assumed nonresonant and its first mediant balanced and nonresonant in one of the four accepted states. Put \(\sigma=\operatorname{sign}(\alpha-p/q)\), \(r=p+P,s=q+Q\), and \(F_k=(kp+P)/(kq+Q)\). The accepted complete expansion is
  \[
  Z-z=\sigma\sum_{j=1}^3C_j\Gamma_j+\mathcal R_{\rm fan},\qquad
  C_j=\frac{2^{-Q-jq}}{1-2^{-3q}}-\frac{3^{-P-jp}}{1-3^{-3p}}.
  \]
  Its quotient-to-actual-response error is uniformly bounded by
  \(\varepsilon=(45/2)2^{-s}+(63/2)3^{-r}\). — [FF1–FF6 and independent audit](../correlated-return-arithmetic/fan_audit.md).
- The rational paired jump is \(J_{u,v}=(2^{-v}-3^{-u})\mathcal Q_{u,v}\), including resonant grades. Complete open-Farey variation is bounded by the established \(\mathcal V\); all low rows and quotient exteriors are retained. — [SS1–SS4](../signed-arithmetic-returns/signed_scalar.md), [resonant grade extension](../response-closure-tests/general_states.md).
- Primary Matveev specialization gives fixed effective \(c>0,K\ge1\) with \(|m\log2-n\log3|>c\max(m,n)^{-K}\), and consequently \(Q\le Cq^K\). — [Primary Theorem 2.1, journal p. 1219](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng#page=3), [accepted primary-source and scale audit](../weighted-response-identities/fixed_logs_audit.md).

### Inferences

**CR1. Exact crossing condition.** Let \(\delta=q\alpha-p\), \(\delta'=Q\alpha-P\), and let \(a=a_{n+2}\) be the digit following the successor, where \(p/q=p_n/q_n\). If \(\delta''\) is the next convergent error, then
\[
\delta''=\delta+a\delta',\qquad
\frac{|\delta|}{|\delta'|}=a+\frac{|\delta''|}{|\delta'|}\in(a,a+1).
\]
Therefore the successor-side child
\[
W=\frac{w}{t}=\frac{p+2P}{q+2Q}
\]
is on the current side of the actual slope, and crossed in the current-to-actual path, **if and only if \(a_{n+2}\ge2\)**. In that case \(\delta+2\delta'\) has sign \(\sigma\). At digit one it has the opposite sign, so the same jump cannot be inserted into the path. — [Accepted CF endpoint conventions](../signed-arithmetic-returns/signed_scalar.md), [exact actual crossing checks](corrected_residual_check.py).

**CR2. A complete residual decomposition.** Retain every current-side fan jump and the crossed jump at \(W\). The open interval from \(F_1\) to the successor splits at \(W\). The other open fan gaps are unchanged. If \(\mathcal Q_k\) denotes the complete quotient at \(F_k\), then the exact fan correction defect remains
\[
\sigma\sum_{k\ge1}(2^{-Q-kq}-3^{-P-kp})(\mathcal Q_k-\Gamma_k).
\]
It is bounded by \(\varepsilon\) times the sum of absolute physical gaps; it is not discarded or assigned a favorable sign. The accepted pure-jump representation and absolute convergence give
\[
\boxed{|\mathcal R_{\rm fan}-\sigma J_{w,t}|\le B_*},
\tag{CR2}
\]
where, writing \(x=2^{-q},y=3^{-p},u=2^{-Q},v=3^{-P}\),
\[
\begin{aligned}
B_*={}&\mathcal V(r,s;w,t)+\mathcal V(w,t;P,Q)\\
&+\frac{72\,2^{-(3q+2Q)}}{1-2^{-2q}}
 +\frac{(189/4)3^{-(3p+2P)}}{1-3^{-2p}}\\
&+\varepsilon\left(\frac{ux}{1-x}+\frac{vy}{1-y}\right).
\end{aligned}
\tag{CR3}
\]
Every interval is an open Farey interval. The first two terms pay both \(W\)-children in full even though the actual path may traverse only part of them. The next two terms pay every open gap between adjacent fan members. The last line pays the complete fan quotient comparison, including low rows and infinite exteriors. — [Full fan coverage, geometric sums and common rectangle](../correlated-return-arithmetic/fan_audit.md), [new exact implementation](corrected_residual_check.py).

**CR3. Uniform remainder on the smaller scale.** For sufficiently late parents, use \(q\ge4,Q\ge5,p\ge3\). The two new child thresholds are
\[
(2q+3Q,2p+3P),\qquad(q+3Q,p+3P).
\]
Their log offsets have absolute value below \(5/Q\) and \(4/Q\), so the previously audited variation estimate gives each at most \((855/4)2^{-A}\). Each threshold \(A\) is at least \(2q+2Q\), since \(Q>q\). The retained fan-gap geometric sum is below \(215\,2^{-(3q+2Q)}\); the full comparison product is at most \(936\,2^{-2s}\), exactly as in the accepted fan proof. Thus
\[
B_*<\left(\frac{855}{2}+\frac{215}{16}+936\right)2^{-2s}
=\frac{22031}{16}2^{-2s}<1400\,2^{-(2q+2Q)}.
\tag{CR4}
\]
The fan geometric sums are evaluated separately in bases two and three. No smallness assertion about \(k\delta\) for unbounded \(k\) enters this bound. — [Accepted constants reconstructed in fan audit](../correlated-return-arithmetic/fan_audit.md), [exact checks of CR3–CR4](corrected_residual_check.py).

**CR4. Uniform nonvanishing theorem.** Section two proves that all sixteen compatible parent classes have complete \(W\)-quotient magnitude above \(1/20000\) once the fixed low-floor rectangle matches. Put \(\Delta_W=2^{-t}-3^{-w}\). Since \(t=q+2Q\le(1+2C)q^K\), a second use of the same fixed-log theorem gives
\[
|t\log2-w\log3|\ge c_1q^{-K^2},\qquad
|\Delta_W|\ge\eta\,2^{-t}q^{-K^2}
\]
for a fixed effective \(\eta>0\). The exponential conversion is legitimate because \(|t\log2-w\log3|<3\log3/Q<1\) eventually. Hence
\[
|J_{w,t}|>\frac{\eta}{20000}2^{-t}q^{-K^2},\qquad
\frac{B_*}{|J_{w,t}|}<\frac{28000000}{\eta}q^{K^2}2^{-q}\longrightarrow0.
\]
It follows that **every sufficiently late applicable balanced-parent index with \(a_{n+2}\ge2\) has \(\mathcal R_{\rm fan}\ne0\)**. Eventually its sign is the sign of \(\sigma J_{w,t}\), and
\[
|\mathcal R_{\rm fan}|>\frac{\eta}{40000}2^{-t}q^{-K^2}.
\tag{CR5}
\]
This is a uniform theorem over the finite sixteen-class family, not an assertion that this family occurs infinitely often. The effective threshold is not optimized. — [Matveev input and scale conversion](../weighted-response-identities/fixed_logs_audit.md), [finite child certificate](corrected_residual_check.py).

The same proof gives a relative expansion in the ten actual child responses \(\Lambda_S\). The interval \((F_1,P/Q)\) is Farey, with first interior threshold \((t,w)\); both \(W\) and the actual slope lie in this interval. Consequently its direct/reciprocal floors match through \(t-1,w-1\), and the accepted comparison gives \(\mathcal Q_{w,t}-\Lambda_S=O(2^{-t}+3^{-w})=O(2^{-t})\). Dividing CR2 by \(|\Delta_W\Lambda_S|\) yields
\[
\boxed{\mathcal R_{\rm fan}=\sigma\Delta_W\Lambda_S
\left(1+O(q^{K^2}2^{-q})\right).}
\tag{CR6}
\]
Since \(\sigma\Delta_W<0\) in the crossing case, the eventual corrected-residual sign is \(-\operatorname{sign}\Lambda_S\). This uses no arithmetic assumption about \(\Lambda_S\) or the earlier fan responses. — [Accepted complete actual-response comparison](../response-closure-tests/response_relations.md), [CR2–CR5 and exact sign checks](corrected_residual_check.py).

### Gaps

- This closes corrected-fan nonvanishing only on the stated following-digit subfamily. Infinitely many actual applicable indices in that subfamily are not proved. — [Current supply gap](../correlated-return-arithmetic/REPORT.md).
- It neither rationalizes the fan correction nor proves enough cancellation in the whole corrected numerator. A corrected rational return needs those arithmetic inputs separately. — [Complete arithmetic interface](../correlated-return-arithmetic/arithmetic_audit.md).
- The new theorem does not apply to arbitrary unbalanced parents or to the separate hierarchy residual. — [Explicit domain of the accepted fan](../correlated-return-arithmetic/farey_fan.md).

## Are every successor child and the actual examples rigorously controlled?

### Takeaway

**All sixteen compatible classes are controlled.** They use ten canonical successor-child states, including two responses absent from the original eight-response fan dictionary. Exact 48-by-48 response rectangles and complete exteriors put every quotient away from zero; two actual following-digit examples pass the full corrected-residual inequality. — [New exact checker](corrected_residual_check.py).

### Cited Findings

- The accepted 24-state residue/commutator graph and balanced-parent inversion give sixteen oriented compatible parent classes. — [GS1–GS4 and independent audit](../response-closure-tests/general_states.md), [finite graph audit](../correlated-return-arithmetic/fan_audit.md).
- If \(U,V\) are lower/upper parent words with multipliers \(x,y\), then \(H(UV)=H_U+xH_V\). The successor-side child is \(UV^2\) when the current parent is lower, and \(U^2V\) when the current parent is upper. — [Accepted Christoffel transform recurrence](../response-closure-tests/general_states.md), [explicit new state enumeration](corrected_residual_check.py).

### Inferences

The child transforms are exactly
\[
H(UV^2)=H_U+x(1+y)H_V,\qquad
H(U^2V)=(1+x)H_U+x^2H_V.
\]
Substituting every accepted compatible parent gives the following complete quotient/actual-response enclosures. A pair \((a,b)\) denotes \(a+b\omega\). Every endpoint is an exact terminating rational, not a floating approximation. The quotient exterior used is \((27/2)2^{-48}+(45/2)3^{-48}\); the actual bounded-response exterior is smaller. — [Exact state, minimum-difference and full-tail checks](corrected_residual_check.py).

| \((w\bmod3,t\bmod3,H_W)\) | Canonical plus endpoint | Complete enclosure |
|---|---|---|
| \((0,1,1)\) | \(-\omega\) | \((.482747,.482748)\) |
| \((0,2,-\omega)\) | \(\omega\) | \((-.000056,-.000055)\) |
| \((0,2,3+2\omega)\) | \(1\) | \((-1.120067,-1.120066)\) |
| \((1,0,0)\) | \(-\omega\) | \((-.000169,-.000168)\) |
| \((1,0,3)\) | \(2\) | \((.425183,.425184)\) |
| \((1,1,1)\) | \(0\) | \((-.058734,-.058733)\) |
| \((1,2,1+\omega)\) | \(1\) | \((.777374,.777375)\) |
| \((2,0,2+\omega)\) | \(1\) | \((-1.071732,-1.071731)\) |
| \((2,1,1)\) | \(1\) | \((-.547828,-.547827)\) |
| \((2,2,2)\) | \(1\) | \((1.456689,1.456690)\) |

All magnitudes exceed \(1/20000\); the new small state is why the stronger guessed lower bound \(1/10000\) must not be used. The checker independently compares each endpoint-defined actual rectangle with the accepted limiting-response rectangle. The new states are \((0,2,-\omega)\) and \((1,0,3)\); their existence here asserts nothing about their actual infinite occurrence. — [New full-tail state certificate](corrected_residual_check.py).

The complete CR3 criterion passes at the following actual current/successor pairs:

| Current, successor | Crossed successor child \(W\) | \(|J_W|_{\rm lower}/B_*\) | Corrected residual sign |
|---|---|---|---|
| \(53/84,306/485\) | \(665/1054\), resonant | \(>4.288\times10^{18}\) | positive |
| \(306/485,665/1054\) | \(1636/2593\) | \(>2^{400}\) | positive |

The input pairs are the previously accepted actual convergents. Their side and the \(W\)-crossing inequalities are additionally checked by exact comparisons of integer powers. The criterion encloses the complete rational \(W\)-jump from its fixed response rectangle and full quotient exterior, then pays both new Farey children, every other fan gap and the complete fan quotient defect. It therefore proves a statement about the actual corrected residual, without assuming the real fan correction rational. — [Exact criterion and sign checks](corrected_residual_check.py), [accepted actual CF prefix and scalar input checks](../signed-arithmetic-returns/signed_scalar_check.py).

### Gaps

- The finite rectangle checks support the ten numerical enclosures and actual examples. The infinite theorem is proved by the written pure-jump decomposition, complete tails and fixed-log comparison above, not extrapolated from those examples. — [CR1–CR6 and checker](corrected_residual_check.py).
- Resonant \(W\) is used analytically only; no resonant scalar denominator is asserted. — [Accepted resonance-independent grade proof](../response-closure-tests/general_states.md).

## What happens at following digit one, and what remains for the arithmetic goal?

### Takeaway

**The digit condition is genuinely necessary for this proof.** At actual current \(12/19\), successor \(41/65\), the successor child \(94/149\) is not crossed. A complete actual-series enclosure proves that the true corrected fan residual is negative and lies in magnitude between \(2^{-176}\) and \(2^{-175}\), whereas the wrongly inserted successor jump is positive and exceeds the proposed small remainder bound. This is a concrete failure of an unconditional extension of CR2. — [Exact digit-one enclosure and false-extension check](corrected_residual_check.py).

### Cited Findings

- Integer powers give \(12/19>\alpha\), but \(94/149<\alpha\). The accepted current-side fan correction for \(12/19\) uses its ordered three actual states. — [Accepted actual fan example](../correlated-return-arithmetic/fan_audit.md), [new exact inequalities](corrected_residual_check.py).
- The new certificate encloses the true target with a \(260\times180\) rectangle and both full exteriors; each fan response is enclosed with a \(192\times192\) rectangle and exterior \(9(2^{-192}+3^{-192})\). Each response uncertainty is multiplied by its exact rational coefficient before the subtraction from the target. The complete periodic rational current model, including its origin exception, is retained. — [Complete enclosure implementation](corrected_residual_check.py).

### Inferences

The exact interval arithmetic proves
\[
-2^{-175}<\mathcal R_{\rm fan}<-2^{-176}.
\]
The complete un-crossed \(94/149\) jump has \(\sigma J_W>0\) and \(\sigma J_W>B_*\), using the same complete quotient lower bound. Consequently
\[
|\mathcal R_{\rm fan}-\sigma J_W|>B_*.
\]
The proposed all-digit version of CR2 is false on this actual input; it is not merely unsupported by an asymptotic argument. The digit-one residual itself is nonzero in this finite example, but this supplies no universal digit-one theorem. Identifying its leading quotient-comparison defect, including possible state Green/occupation terms, remains a separate unproved task. — [Exact counterexample and interval certificate](corrected_residual_check.py).

For the arithmetic goal, CR5 removes the corrected-residual nonvanishing obligation on an explicitly stated following-digit subfamily. The full response arithmetic, enough whole-model numerator gcd saving or stronger actual correlated cancellation, and an actual infinite applicable subsequence still have to be proved. No complete irrationality proof or adequate infinite arithmetic return follows. — [Full scalar/fan arithmetic requirements](../correlated-return-arithmetic/arithmetic_audit.md).

### Gaps

- No actual infinite supply of balanced-parent indices with \(a_{n+2}\ge2\), no rationality of actual responses under rational \(Z\), and no sufficient whole-model gcd saving is established here.
- The digit-one finite enclosure does not settle other digit-one indices, arbitrary unbalanced fans or the separate hierarchy residual.
- Skipped: Lean, external review, priority verification, optimized constants and reconstruction of the already accepted finite optimum/Matveev proof. Material risk: promoting the new corrected-residual theorem beyond its crossing and arithmetic hypotheses.
