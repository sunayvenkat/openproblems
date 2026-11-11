# One actual-convergent bracketing counterexample

**Final followup status: the ordered candidate Z_plus<=Z<=Z_minus is false at the actual convergent 12/19.** The exact result is Z_minus(12/19)<Z<Z_plus(12/19). The unordered min/max bracket survives this one test and remains an unproved candidate; no infinite bracketing or return theorem follows. Per the assigned stopping rule, no additional model tests or potential search were undertaken after this counterexample. — [Exact certificate](hybrid_bracketing_check.py).

## Does the ordered bracket survive the one prescribed actual-convergent test?

### Takeaway

No. A complete actual-target rectangle enclosure, with all indicator and low-row corrections and an exact infinite-tail allowance, reverses the proposed plus/minus orientation at 12/19. Both strict inequalities are certified by integer interval bounds. — [Certificate](hybrid_bracketing_check.py).

### Cited Findings

- The existing model's signs + and - designate the horizontal one-sided floor convention, with the opposite convention for the reciprocal floor. They are not definitions of the smaller and larger scalar value. The complete model retains all E terms, four low-row rules and the exceptional origin digit. — [Audited model definition](../global-boundary-proof/independent_audit.md), [complete paired-model implementation](../reflected-return-models/two_sided_models_check.py).
- The actual coefficient array is c_ab=1-3 eta_ab in {-2,1}, and Z=sum c_ab 2^-a 3^-b. The proved finite formula supplies its exact birth-digit rule. — [Finite theorem](../prefix-and-phase-audit/REPORT.md), [current normalization and dynamics](../reflected-return-models/REPORT.md).
- The direct actual series is independently enclosed on a<160,b<110. The script computes every logarithmic floor by exact integer power comparisons, then evaluates the full corrected state and its correct low-row rule. No density decimal is computed. — [New direct-rectangle certificate](hybrid_bracketing_check.py), [reused exact coefficient routine](hybrid_compression_check.py).

### Inferences

**12/19 really is an actual convergent.** The rational continued-fraction prefix [0;1,1,1,2,2] has consecutive terminal convergents 5/8 and 12/19. Its open final cylinder has endpoints 17/27 and 12/19. The certificate verifies

```
2^27 > 3^17,       2^19 < 3^12,
```

so 17/27<alpha=log_3 2<12/19 lies in that cylinder. Thus the check is about an actual nonresonant convergent, not an arbitrary rational slope. Since alpha<12/19, its matched-side model is minus. — [Exact cylinder and continued-fraction assertions](hybrid_bracketing_check.py).

**Complete tail control.** Put A=160, B=110 and let S be the finite actual sum over 0<=a<A,0<=b<B. The omitted geometric weight is exactly

```
3v,      v=2^-A+3^-B-2^-A 3^-B.
```

Since every omitted coefficient is between -2 and 1,

```
S-6v <= Z <= S+3v.                                   (B1)
```

There is no missing infinite side in this enclosure: it includes both exterior strips and subtracts their intersection. The cylinder verification and tail estimate are separate from the arithmetic comparison model. — [Exact enclosure construction](hybrid_bracketing_check.py).

**Complete model values and strict gap bounds.** At p/q=12/19, set

```
D=27(2^57-1)(3^36-1)
 =584034748065108629302925842213505040.
```

The independently evaluated full periodic models give

```
D Z_plus  =705918015253698271783679476310697738,
D Z_minus =705918008015665023891011916838310910.
```

Combining each exact rational value with (B1), the certificate proves

```
-7238033247892667559404885391
 < D(Z-Z_plus)
 < -7238033247892667559404885390,

67501437 < D(Z-Z_minus) < 67501438.                    (B2)
```

The actual Z interval has width less than 1/(D*2^20); both displayed integer enclosures are asserted strict in the code. Hence

```
Z_minus(12/19) < Z < Z_plus(12/19).                    (B3)
```

The prescribed ordered bracket is disproved. The script now asserts this counterexample, rather than leaving an expected failing conjecture assertion. — [Passing exact assertions and model reconstruction](hybrid_bracketing_check.py).

### Gaps

- No additional rational slopes were tested in this followup.
- This falsifies the fixed ordered plus/minus convention, not an unordered bracket or a more refined phase-dependent inequality.
- The model and actual coefficient rule are accepted from the existing complete finite proof; this certificate does not independently reprove global finite optimality.

## What does this change about matched-side nonvanishing and the unordered candidate?

### Takeaway

There is now a third named actual nonvanishing certificate. A fixed sign based on the matched minus-side convention alone fails: 12/19 has Z-Z_minus>0, while 53/84 has Z-Z_minus<0. The unordered bracket remains open and has no infinite proof. — [New 12/19 certificate](hybrid_bracketing_check.py), [previous actual 53/84 certificate](hybrid_compression_check.py).

### Cited Findings

- Earlier actual-target interval certificates proved Z>Z_MM(5/8,+) and Z<Z_MM(53/84,-), with full tail control. — [First-round note](hybrid_compression.md), [first-round checker](hybrid_compression_check.py).
- The global-carry note deliberately formulates the potential followup as min(Z_plus,Z_minus)<Z<max(Z_plus,Z_minus); it does not assert a fixed ordering of the labels. It also gives exact failures of naive global slope monotonicity and exceptional-grade signs. — [Candidate and its limitations](global_carries.md).
- The final auditor requested a narrow hardening in the first-round checker: assert the positive 5/8 sign rather than merely print it. That single assertion has been added, and the complete first-round checker still passes. The first-round mathematical note was left unchanged. — [Explicit positive-sign assertion](hybrid_compression_check.py).

### Inferences

The literal ordered candidate and the unordered candidate must remain distinct. Equation (B3) is a counterexample to the former and a supporting named instance for the latter. Supporting instances at a finite set of convergents do not prove an infinite family, and any eventual bracket theorem would still have to intersect the subsequence used for the adequate upper approximation. — [Exact scope of (B2)-(B3)](hybrid_bracketing_check.py), [supply interface](../infinite-return-construction/REPORT.md).

The changed matched-minus sign also prevents using that convention alone as a universal nonvanishing sign argument. A theorem restricted to actual convergents might still use additional phase, state, or retimed-token information; no such theorem is proved here. — [Actual signs](hybrid_compression_check.py), [new strict sign](hybrid_bracketing_check.py).

### Gaps

- The unordered actual-convergent bracket is unresolved.
- No strict matched-side inequality covering an infinite actual family was proved.
- The retimed positive-token and master-walk identities remain valid inputs, but the instructed branch stopped when the ordered candidate failed; they were not used to manufacture a replacement assertion.

## Does this provide the adequate infinite upper approximation required by the goal?

### Takeaway

No. The new result removes an incorrect sign shortcut and proves one more actual nonvanishing instance. It supplies neither the adequate infinite weighted upper family nor hybrid arithmetic closure. — [Current frontier](../reflected-return-models/REPORT.md).

### Cited Findings

- The scalar route still needs actual eligible supply with q_next-5q tending to infinity, followed by nonvanishing on the same family. The hybrid product-tail route has unproved comparison-value arithmetic and actual supply. — [Audited arithmetic requirements](../reflected-return-models/final_reflected_audit.md).
- Both followup and hardened first-round checkers passed using Python -B. No Lean, external posting or archived-folder edits were performed. — [Followup checker](hybrid_bracketing_check.py), [hardened first checker](hybrid_compression_check.py).

### Inferences

This is a rigorous adversarial correction to the proposed route. It should be reported as a named counterexample and nonvanishing certificate, with the unordered and infinite questions left open. No completion claim for the infinite-return objective is justified. — [Passing counterexample certificate](hybrid_bracketing_check.py).

### Gaps

- No new discounted potential or arithmetic compression was obtained after the failed candidate.
- Skipped: further model tests, broad scans, density decimals, Lean and external review. The remaining risk is treating a named strict bracket as an infinite nonstabilization theorem or conflating model-side labels with numerical order.
