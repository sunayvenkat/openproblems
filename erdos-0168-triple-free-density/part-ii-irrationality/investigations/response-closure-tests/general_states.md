# Compatible child states and two-node Farey returns

## Can a balanced mediant control a nonbalanced or resonant child?

### Takeaway

**Yes: a Christoffel commutator restricts the neighboring transforms to a finite list.** In the actual prefix cylinder, there are sixteen compatible current-side child cases. Their complete toric quotient responses are all nonzero; five have the same sign as the balanced mediant, including four cases with resonant children. This is a classification of these compatible children, not of arbitrary unbounded Eisenstein states. — [Exact finite-state and response certificate](general_states_check.py).

### Cited Findings

- The accepted lower Christoffel transform satisfies \(H(UV)=H(U)+\rho(U)H(V)\), where \(\rho(U)=\omega^{|U|}\), and the word of a Farey mediant is the lower word followed by the upper word. — [CR3, complete floor/word proof](../boundary-return-mechanisms/cf_return_state.md).
- A paired scalar jump has the complete toric factorization \(J_{r,s}=(2^{-s}-3^{-r})\mathcal Q_{r,s}(1/2,1/3)\). Its quotient coefficients obey \(|Q_{a,b}|\le3(1+b/r)\), and for \(r\ge24\) the exterior of a \(24\times24\) rectangle is at most \(T_{24}=\frac{27}{2}2^{-24}+\frac{45}{2}3^{-24}\). — [SS1–SS2](../signed-arithmetic-returns/signed_scalar.md).
- The four balanced nonresonant rational states and the fixed short direct/reciprocal floor word are explicitly specified. An actual Farey parent interval containing the logarithmic slope supplies that word to all its sufficiently late interior rationals. — [SS2 and SS4](../signed-arithmetic-returns/signed_scalar.md).

### Inferences

**GS1. The neighboring-word commutator is a root of unity times \(1-\omega\).** Let \(U,V\) be the lower and upper Christoffel words of a Farey pair and write \(x=\rho(U),y=\rho(V)\). Define
\[
C(U,V)=(1-y)H(U)-(1-x)H(V).
\tag{GS1}
\]
For the initial words \(E,N\), this is \(1-\omega\). The two Stern–Brocot replacements give
\[
C(U,UV)=xC(U,V),\qquad C(UV,V)=C(U,V).
\]
These identities follow by substituting the concatenation formula. Thus every neighboring pair has
\[
C(U,V)=\omega^k(1-\omega),\qquad k\in\{0,1,2\}.
\tag{GS2}
\]
No claim that two long words differ by one adjacent swap is needed.

Let the mediant word be \(W=UV\), with \(h=H(W)\), \(\rho(W)=xy\ne1\). Then
\[
H(V)=\frac{(1-y)h-C(U,V)}{1-xy},\qquad
H(U)=h-xH(V).
\tag{GS3}
\]
Consequently a balanced mediant, whose \(h\) belongs to the four-row table, determines both parent transforms once the residue pair and commutator phase are known. This does not determine the values of any weighted actual ray profiles.

The current-side child is \(UW\) if the current parent is lower, and \(WV\) if it is upper. Its transform is respectively
\[
H(UW)=H(U)+x h,\qquad H(WV)=h+xyH(V).
\tag{GS4}
\]
The child can be resonant even when the current parent and mediant are not.

**GS2. Exact finite compatibility reduction.** Start at the actual neighboring interval \(5/8<12/19\). Its residue/commutator state is
\[
((2,2),(0,1),k=0).
\]
Here residue pairs mean \((p\bmod3,q\bmod3)\), with lower before upper. Replacing the lower endpoint by the mediant updates \((u,v,k)\) to \((u+v,v,k)\); replacing the upper endpoint updates it to \((u,u+v,k+u_p+u_q)\), all modulo three. The exhaustive finite closure has exactly twenty-four states, one phase for each determinant-minus-one residue pair. This is an exact finite graph check: the checker constructs the closure, verifies its size and unique phase per pair, and solves (GS3) in the Eisenstein ring. Every sufficiently late actual interval descends from this initial interval, so induction puts it in this closed graph.

Requiring a balanced nonresonant mediant and a nonresonant current parent leaves sixteen cases. The complete quotient intervals certify all sixteen child responses away from zero, with absolute value greater than \(1/10000\). Five have the same sign as the mediant. They all have the current parent as the upper endpoint:

| Lower/successor residue \(u\) | Upper/current residue \(v\) | Phase \(k\) | Mediant \((p,q,H)\bmod3\) | Current-side child \((p,q,H)\) |
|---|---|---:|---|---|
| \((0,1)\) | \((1,0)\) | 0 | \((1,1,1)\) | \((2,1,1)\) |
| \((0,2)\) | \((2,0)\) | 1 | \((2,2,2)\) | \((1,2,1+\omega)\) |
| \((1,2)\) | \((0,2)\) | 1 | \((1,1,1)\) | \((1,0,0)\) |
| \((2,0)\) | \((1,1)\) | 1 | \((0,1,1)\) | \((1,2,1+\omega)\) |
| \((2,2)\) | \((0,1)\) | 0 | \((2,0,2+\omega)\) | \((2,1,1)\) |

The three distinct child responses needed in these rows obey the tail-inclusive bounds
\[
\begin{array}{c|c}
(p\bmod3,q\bmod3,H)&\mathcal Q(1/2,1/3)\\\hline
(2,1,1)&(-11/20,-27/50)\\
(1,2,1+\omega)&(77/100,79/100)\\
(1,0,0)&(-1/5000,-1/10000).
\end{array}
\tag{GS5}
\]
The first two rows are resonant. They are not assigned a nonresonant scalar clearing denominator.

**Why the resonant response calculation is legitimate.** The complete grade-birth total is unchanged when a finite grade is read in either tie order, regardless of resonance. Thus the grade-conservation proof of the toric factorization and coefficient bound still applies. The fixed small-coordinate response uses only the exact endpoint formula for \(A_q^\pm\), the transform \(H\), and the short floor word; none of those steps assumes nonresonance. The sole negative-effective-exponent token has zero birth in the stated slope interval. The certificate independently enumerates the retimed original tokens by rational grade at the resonant child \(65/103\), using both tie orientations and simultaneous duplicate arrivals, and checks the low quotient against the algebraic response formula. The infinite remainder is then controlled by the same absolute coefficient bound. This proves the jump bound without proving rationality of either resonant scalar value.

### Gaps

- Eleven compatible children have response sign opposite to the mediant. Nonzero individual responses do not prevent their sum from cancelling. — [Exact sign classification](general_states_check.py).
- This finite compatibility theorem does not classify arbitrary unbounded \(H\), evaluate the limiting actual ray series, or provide an infinite supply of any parent class.

## Does a two-node cluster cover an additional asymptotic regime?

### Takeaway

**Yes, on the five same-sign classes.** If \(Q\ge3q\), the current-side child supplies a subexponentially small leading gap on the original \(q\) scale. The criterion needs neither bounded \(Q/q\) nor a following digit at least two. It therefore covers a part of the previously exceptional \(a_{n+2}=1\), unbounded-ratio regime. Actual infinite adequate-gap supply remains unproved. — [Two complete exact cluster checks](general_states_check.py).

### Cited Findings

- The scalar slope function has purely atomic bounded variation, with the full open-Farey upper bound \(\mathcal V\) from SS3. Correct-side limits exclude the current endpoint jump and include each interior rational jump exactly. — [SS3–SS4](../signed-arithmetic-returns/signed_scalar.md).
- The actual convergent errors have opposite signs and decreasing magnitudes, with \(|q\alpha-p|>1/(q+Q)\). The checked fixed one-unit seed consequence is \(\log Q=o(q)\). — [SS5](../signed-arithmetic-returns/signed_scalar.md), [seed normalization](../signed-arithmetic-returns/seed_arithmetic_audit.md).

### Inferences

**GS3. Complete two-node decomposition.** Let \(p/q,P/Q\) be consecutive actual convergents, with current \(p/q\) nonresonant. Set
\[
m=\frac rs=\frac{p+P}{q+Q},\qquad
\ell=\frac tu=\frac{2p+P}{2q+Q},\qquad
\sigma=\operatorname{sign}(\alpha-p/q).
\]
The actual slope lies beyond \(m\) as viewed from the current parent, while \(\ell\) lies between the current parent and \(m\). Put
\[
R_2=\mathcal V(p,q;t,u)+\mathcal V(t,u;r,s)+\mathcal V(r,s;P,Q).
\tag{GS6}
\]
Pure-jump variation gives the exact error estimate
\[
\left|(Z-\widetilde Z^\sigma_{p,q})-
\sigma(J_{r,s}+J_{t,u})\right|\le R_2.
\tag{GS7}
\]
All three remaining open intervals are included. No claim is made that the actual path traverses their full length; their full variation is a safe overestimate.

For a finite certificate, multiply the two complete quotient intervals by their exact rational gaps \(2^{-s}-3^{-r}\) and \(2^{-u}-3^{-t}\), add them, and enlarge by \([-R_2,R_2]\). If the result excludes zero, the correct error is nonzero. This also works in opposite-sign cases when their actual magnitudes allow it; no general conclusion for those cases is asserted.

**GS4. Eventual dominance on the five classes.** Both \(m\) and \(\ell\) lie on the same side of \(\alpha\), hence their gap factors have the same sign. In a row of the five-class table, their complete quotient responses have the same sign too. Therefore
\[
|J_{r,s}+J_{t,u}|=|J_{r,s}|+|J_{t,u}|\ge |J_{t,u}|.
\]
Write \(\delta=q\alpha-p\), \(\delta'=Q\alpha-P\). Then \(\delta\) and \(\delta'\) have opposite signs and \(|\delta'|<|\delta|\), so
\[
|u\alpha-t|=|2\delta+\delta'|>|\delta|>
\frac1{q+Q}.
\]
The relevant logarithmic form is \(u\log2-t\log3\). Since these errors tend to zero, (GS5) gives, for a fixed positive constant \(c_0\),
\[
|J_{t,u}|\ge c_0\frac{2^{-u}}{q+Q}
=c_0\frac{2^{-(s+q)}}{q+Q}.
\tag{GS8}
\]
If \(Q\ge3q\), all three Farey remainders in (GS6) are
\[
R_2=O(2^{-(s+2q)}).
\tag{GS9}
\]
Indeed their denominator-sum thresholds are \(s+2q\), \(2s+q\), and \(s+Q\); the last is at least \(s+3q\). Numerator thresholds have the same logarithmic size because \(p\log3-q\log2\) and \(P\log3-Q\log2\) tend to zero. The rational prefactors in \(\mathcal V\) remain uniformly bounded.

Finally, \(\log(q+Q)=o(q)\) yields \(2^q/(q+Q)\to\infty\). Thus (GS8) dominates (GS9), proving eventual correct-side nonvanishing on any actual sequence in the five classes with \(Q\ge3q\). No condition on \(a_{n+2}\) or upper bound on \(Q/q\) is needed. In particular \(Q-5q\to\infty\) already implies the required \(Q\ge3q\) eventually.

The checker verifies the complete two-node intervals for \(12/19\) with successor \(41/65\), and \(53/84\) with successor \(306/485\). Their certified leading-to-remainder ratios exceed respectively \(18318776\) and \(18168129295004104279455783313574041127430456078\). These finite examples test the formula but do not provide unbounded-ratio actual supply.

### Gaps

- A true infinite sequence with an adequate scalar gap and one of the five state classes has not been proved for \(\log_3 2\). The new criterion removes a dominance restriction on such a sequence; it does not supply the sequence.
- No cheaper scalar clearing factor is claimed. Current nonresonant \(p/q\) still uses the fully charged \(27(2^{3q}-1)(3^{3p}-1)\). Resonant child jumps are analytic contributions to the cluster, not arithmetic approximants whose denominator is borrowed from that formula.
- General unbalanced response states and the eleven opposite-sign compatible classes remain outside the same-sign asymptotic theorem. The finite interval criterion still applies if independently checked.
- Skipped: Lean, installations, new external theorems, archived edits, larger numerical cases and historical priority. Material risk: mistaking a broader correct-side nonvanishing criterion for actual infinite adequate-gap supply or a reduced arithmetic denominator.
