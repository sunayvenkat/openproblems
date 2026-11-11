# Fresh audit of the reflected and induced Erdős 168 returns

Audit completed: 7 November 2026. Scope: the new reflected-numerator, paired-model and continued-fraction arguments, and the final actual-carry and record-return notes. The completed global finite formula (C) is an accepted input. This auditor has edited only this file and the adjacent narrowly targeted certificate. **The adequate infinite weighted-return goal remains unproved.** The latest positive milestone is exact mixed corner support with a product-of-two-tail error. Its two hybrid comparison values have no proved arithmetic compression. Nonvanishing remains separate. The auxiliary results below pass with their stated scope and the identified low-event wording correction.

## Do the reflected and paired identities retain the complete model?

### Takeaway

**PASS with the stated limitations.** The opposite-side uncorrected reflection, its explicit ray error, the full scalar numerator, the paired binomial factor, and the vertical Laurent-coefficient obstruction all survive reconstruction. They yield neither a free replacement by the opposite original weighted value nor a new rational constant under the sole assumption that Z is rational. The formal obstruction is proved for two named models and the specified readout/coefficient architecture; it is not a general scalar cancellation impossibility theorem. [Reflection note](numerator_reflection.md), [paired note](two_sided_models.md).

### Cited Findings

- The primary model has positive-index one-sided floors, separately anchored A(0)=B(0)=1, opposite reciprocal convention, an isolated/patch correction at high rows, four distinct low-row tests, and one nonperiodic exception at (0,1). The admissible interval is 3/5<p/q<2/3. These are the definitions used in this audit. [Earlier independent model audit](../global-boundary-proof/independent_audit.md), [original checker](../../early-attacks/augmentation-and-return-attacks/returns_check.py).
- The reflection certificate's formulas and three exact model values can be checked without running its file-writing main section. The paired certificate ran successfully with Python -B and recovered the saved values, full graded numerator factor, and all stated rank witnesses. [Reflection certificate](numerator_reflection_check.py), [paired certificate](two_sided_models_check.py).
- This audit's separate certificate counts synthetic vertices in their actual one-sided grade order and applies the isolate/patch entry and exit events directly. It uses no optimum or formula (C) for a synthetic slope. It recovers the retained low rules and origin on the specified 5/8 test, and reconstructs the four named vertical minors directly from adjusted color counts. [Fresh certificate](final_reflected_audit_check.py).

### Inferences

**1. Reflection, including axes and rational ties, is exact for the uncorrected state.** Write P=3q, Q=3p and e_sigma=1_[sigma>0]. For 1<=k<P,

```
m_sigma(P-k)=3p-1-m_(-sigma)(k).
```

Opposite endpoint conventions are necessary here. The endpoint increments are f_sigma(P)=e_sigma and g_sigma(Q)=1-e_sigma. Since the full period sums vanish, backwards summation gives precisely

```
A_sigma(a)=conj A_(-sigma)(P-1-a)+S(a)-e_sigma,
B_sigma(b)=conj B_(-sigma)(Q-1-b)+T(b)-(1-e_sigma).
```

In particular A_sigma(P-1)=1-e_sigma and B_sigma(Q-1)=e_sigma; there is no unspecified axis error. Using C=(S-1)(T-1), the identity conj C(P-1-a,Q-1-b)=S(a)T(b) cancels all remaining terms. Thus the uncorrected state obeys z_sigma(a,b)=conj z_(-sigma)(P-1-a,Q-1-b). Conjugation exchanges the two closed-cone inequalities x<=0 and x-y<=0, including ties. The alternative P-a,Q-b reversal needs the displayed insertion term in (R4); dropping its wrap increments would be wrong. [Reflection note, (R1)-(R4)](numerator_reflection.md).

**2. The actual high-row reflection has the stated error, including its sign.** The reflected isolated condition becomes n_sigma(b+2)-n_sigma(b+1)=2, with color n_sigma(b+1)-2b-1. The reflected patch condition becomes n_sigma(b+4)-n_sigma(b+2)=4, with color n_sigma(b+2)-2b. This verifies (R5). The high correction is extended periodically, rather than by imposing an axis initial-state convention on it. The ray responses are

```
R0=-1_[x-1=min(y,0)],
R1= 1_[x=y<=0],
R2= 1_[x=0,y>=0].
```

Direct comparison of the two cone inequalities gives c(z-omega^j)-c(z)=3Rj(z). In particular the same-color response R0 is negative, not zero. This proves the full (R7) discrepancy. At (0,5), in each of the three actual-sided named models, z=0, E=0, E*=omega, and the two corrected coefficients are -2 and 1. Both rows are high. The discrepancy is not confined to a low or axis exception. [Reflection note, (R5)-(R7)](numerator_reflection.md).

**3. The full scalar numerator has no missing low or origin term.** If H is the periodic high extension and L is the low coefficient minus that extension, excluding the one origin exception, then

```
G=H/[(1-X^P)(1-Y^Q)]+L/(1-X^P)-3Y.
```

The low correction repeats horizontally only. Set U=2^P, V=3^Q, D=27(U-1)(V-1). Evaluating at (1/2,1/3) gives exactly

```
N=162W+2J(V-1)-D,
W=H_(-sigma)(2,3)+3K.
```

The factor 162 follows from 27 times the reversed tile's weight factor 6. The low term contributes 2J(V-1); the single exceptional coefficient contributes -D. Reversal evaluates the opposite polynomial at (2,3). It does not produce its original weighted numerator W_(-sigma). The ray term K and low term J have only exponential-height bounds here. Neither is a fixed bounded list of rational-coefficient S-units. [Reflection note, (N1)-(N3)](numerator_reflection.md).

**4. The synthetic adjusted-min proof of the paired binomial does not assume synthetic optimality.** Its model is defined to be M_r=min_j(K_j-I_j-P_j). For a vertex of normalized color 0, the indicator endpoint events are as follows.

- At b=0,a>=1, the new vertex and entered isolate have the same color, so the adjusted vector does not change. At the origin its minimum remains zero.
- At b=1,a>=2, the vertex and entered patch cancel in color 0, while removal of the isolate adds color 2. The after-state is K-e0, so the digit is 1 exactly when x>=1,y>=0. The actual initial finite states at a=0 and a=1 instead give digits 1 and 0, respectively.
- At b=2 no indicator changes at insertion; its active isolate has relative color 2. Applying the ordinary cone to z-omega^2 gives x<=-1 and x-y<=0.
- At b=3, insertion and patch removal add colors 0 and 2. The minimum difference is min(x,y,0)-min(x-1,y,-1), which equals 1_[min(x,0)<=y].

These are algebraic increments of the defined minimum. The sole off-vertex patch exit, at 27/lambda for root lambda, lies strictly between lambda^2*3 and lambda^4. Its color counts are (3,3,2); removing its patch changes the adjusted vector (3,2,2) to (3,3,2), so its minimum increment is zero. For p>3 it cannot coincide with a positive rational-grade vertex, since p(a+1)+qb=3q has no nonnegative solution. Thus every nonzero synthetic minimum increment is attached to the retained vertices. [Paired note, binomial proof](two_sided_models.md), [direct independent count certificate](final_reflected_audit_check.py).

For a fixed grade pa+qb=k, the two limits traverse the finite tie chain in opposite orders but start and end with the same adjusted count vector. Telescoping therefore proves equality of the total birth increments on that grade. There are equally many coefficient-1 terms on the two sides, so the grade sum of c^+-c^- vanishes. This proves (F^+-F^-)(t^p,t^q)=0. The full common-denominator numerator P is a polynomial, because its low-row defect is finite vertically. Dividing by the monic x^q-y^p leaves monomials with 0<=a<q, whose grades are all distinct by coprimality. Consequently P is divisible by x^q-y^p over Z[x,y]. This is a genuine full-model identity. [Paired note, (B1)-(B2)](two_sided_models.md).

After scalar evaluation, N_diff/(u-v) has only powers of 2 and 3 in its possible denominator. Since N_diff is integral and gcd(u-v,6)=1, u-v divides N_diff in Z. This is (B3). It does not show u-v divides the original denominator. Along ordinary convergent returns, |u-v|/u is only of order 1/q_next; it gives no fixed exponential gain. [Paired note, (B3)](two_sided_models.md).

**5. The vertical Laurent rank proof is valid, including the residue basis.** Work over Q(omega)(X), impose x^q=X and y^p=zeta, and use the quotient-ring basis x^a y^b with 0<=a<q and any complete p consecutive b residues. This basis is free even when y^p-zeta is reducible; no field irreducibility is being assumed. Thus cancellation of the whole vertical factor requires every residue equation (T8), rather than an average of them. A minor nonzero at X=2 is nonzero over Q(omega)(X). Independently reconstructed determinants, with the note's column order and listed rows, are

| model | zeta=1 | zeta=omega |
|---|---:|---:|
| 5/8 | -3969 | -19845-31752 omega |
| 53/84 | -3969 | 31752+11907 omega |

Full column rank forces each effective block coefficient to vanish at that root. Rational coefficients and conjugation add the omega^2 root. Therefore each effective coefficient must itself contain the canceled vertical factor, for arbitrary finite Laurent degree. Low-row additions have no vertical pole, and multiplying any finite head by block Laurent monomials still leaves no vertical pole. They cannot change this conclusion. Low rows can affect horizontal residues, so the note correctly refrains from asserting the same unrestricted full-model horizontal conclusion. [Paired note, (T7)-(T8)](two_sided_models.md), [fresh determinant certificate](final_reflected_audit_check.py).

This is a factor-accounting obstruction for the two named models and these four effective columns. Moving 1+Y+Y^2 into coefficients pays its v^2 scale either as coefficient height or minimum-unit cost. It is not a lower bound for every scalar denominator, arbitrary cone translation, or a special infinite subsequence of engineered evaluations. [Paired note, second question and gaps](two_sided_models.md).

**6. Normalization to the sole Z is correctly restricted.** Comparing the three common open cone regions and then the exceptional ray y=0,x>=1 proves that the universal six-readout identity (T5) holds exactly under a1=a2, b1=b2, kappa=a0+b0-a1-b1. Partition identities then leave only the two color-0 readouts. This does not prove that all other actual weighted color readouts are irrational; it means their rationality does not follow from this universal identity and Z in Q. A new special identity along the actual path would be an additional theorem. Likewise, a nonzero opposite-side scalar coefficient initially has only the q-by-p matching window. A finite correction can restore a longer rectangle but must be computed and charged, and does not change the vertical pole residues. [Paired note, (T4)-(T10)](two_sided_models.md).

### Gaps

- No estimate compresses K or J to fixed-term arithmetic data with adequate coefficient height.
- Neither the paired binomial nor the named rank minors prove a sufficient scalar denominator saving on an actual infinite sequence.
- No extra color, ray, or hybrid constant has been shown rational from the sole assumption Z in Q.

## Do the actual continued-fraction and record arguments control weighted arithmetic?

### Takeaway

**PASS for the induction, comparison-path hits, actual carry constraint and real mixed-corner estimate.** The induction reaches the origin-anchored actual endpoints and weighted profiles. The center/radius invariant requires an eventually nonresonant tail. The record theorem realizes its translates by the same quadratic comparison path's reciprocal rows, including E. The carry constraint applies to the target array. None supplies an adequate weighted arithmetic return for the actual logarithmic slope. [CF note](cf_induction.md), [record note](record_returns.md), [carry note](actual_carries.md).

### Cited Findings

- The actual axis recurrence and separated count state are proved independently of minimum-cover optimality. [Original arithmetic note](../boundary-and-arithmetic/arithmetic.md).
- The earlier center constants, including the opposite reciprocal side and bounded sum c_A+c_B, are available with every rational tie retained. [Skew-center derivation](../infinite-return-construction/skew_denominator.md).
- The CF certificate ran with Python -B and passed its direct mechanical-word, root-register, weighted concatenation, unipotent and three finite first-hit checks. This audit separately verified all admissible phase/digit/parity cases for the center and copied-prefix distances. [CF certificate](cf_induction_check.py), [fresh certificate](final_reflected_audit_check.py).

### Inferences

**1. Parity and the actual side convention pass.** For the lower mechanical words, n even gives C_n^a C_(n-1), while n odd gives C_(n-1) C_n^a. The concatenation root register Q_UV=Q_U+rho_U Q_V then gives exactly (I3). In particular the initial C_0=0,C_1=1 gives C_2=01 and C_3=011, consistent with this order. A lower convergent agrees with the actual floor at its endpoint q_n; an upper one lowers that endpoint by one. Its root-sum correction is (omega-1)rho_n, not its negative. Substitution into the summed original axis recurrence gives (I5) with A_0=1, and H_A=omega^2 Q_n^true gives (I6). The recentering register is consequently tied to the actual model rather than selected independently. [CF note, (I1)-(I6)](cf_induction.md).

**2. The center and prefix radius invariants pass with exactly the nonresonance hypothesis stated.** A nonresonant affine map has order three. When all three adjacent phases are nontrivial, a mod3=0 returns the preceding center; a mod3=1 requires equal preceding phases; a mod3=2 requires opposite phases. Direct substitution gives precisely the rotations of the old center difference listed in the table. Thus its length L is invariant. In either word order the copied prefix centers are at distance 0 or L from the new center, proving R_(n+1)<=max(R_n,R_(n-1))+L. These facts do not require bounded partial quotients. They fail as stated at a resonant phase, where the geometric sum is the full digit a. [CF note, (I7)-(I9)](cf_induction.md), [fresh all-case certificate](final_reflected_audit_check.py).

The resulting bound on every actual A prefix is O(CF depth). To obtain O(log(a+2)) for arbitrary a, choose the first denominator at least a; its preceding denominator is less than a, so the number of levels is O(log(a+2)) even when the next partial quotient is huge. The endpoint discrepancy between the actual word and an upper mechanical word is bounded. The reciprocal construction supplies the same statement for B. An O(log a) spatial bound does not bound the numerators of weighted sums whose exponents reach a. [CF note, radius argument and weighted cost](cf_induction.md).

**3. Weighted transfer is exact but still operator-valued.** The displacement formula (I11) follows by expanding S(m+u) and using 2u=-u modulo three. Splitting the prefixes of UV proves L_UV=L_U+t^|U| P_U L_V. P_U shifts both the actual incoming state and the residues. For a nonresonant word W, three copies have zero root sum, length and ones divisible by three, and zero axis displacement; hence P_W^3 is the identity on the complete extended state. Grouping repetitions in triples proves (I14) with its denominator 1-t^(3q). Its vertical analogue retains 1-3^(-3p). The small support of a growing profile does not give a bound on the height of its integer weighted coefficients or a fixed number of arithmetic coordinates. [CF note, (I10)-(I15)](cf_induction.md).

**4. The unipotent family and actual ray separation pass, with comparison-slope scope.** For alpha_*=[0;1,1,1,1,1,3,overline(2,1)], the four-digit register matrix has trace 2, determinant 1 and nonzero square-zero difference from the identity. Its stated initial vector gives Q_t=(t-1)omega and Q_t^prev=-t-omega, with c_A,t=(1-t)/3. The denominator matrix [[11,4],[8,3]] has eigenvalues 7+4sqrt(3) and its reciprocal. Its cube is the identity modulo three. Therefore the actual, correctly sided endpoint identity gives A_(q_(3ell))=1-ell+ell omega. The ray h_L(z)=H_02(z+L-1) then evaluates to 1_[ell=L]. These translates remain linearly independent after restriction to that single genuine path. [CF note, (I16)-(I20)](cf_induction.md).

The conclusion concerns functional profiles, not independence or irrationality of their weighted numerical values. It does not exclude controlled growing integer parameters. This explicit alpha_* is quadratic and differs from log_3 2. The argument therefore disproves a claim from generic no-resonance/recenter structure alone, not a special theorem for the actual target. The original 209,3083,43121 checks prove firstness only at those three levels and must not be presented as an all-level first-hit theorem. [CF note, final section](cf_induction.md).

**5. PASS for the reconstructed all-level record-hit identity.** The final note supplies a genuine all-level hit construction, which this audit independently reconstructs as follows. At four-digit block index t write W=W_t, V=V_t, q=|W|, v=|V|, and B=W^3V. The parity-correct induction gives

```
W_(t+1)=B^3 W^2 V,       V_(t+1)=B^2 W^2 V,
(q_(t+1),v_(t+1))=(11q+4v,8q+3v).
```

Put g_t=v_t/2-14 and f_t=q_t-v_t/2-14. The seed t=1 has (q,v)=(351,256), g_1=114, f_1=209, and its directly counted root prefix is G_1=-3-3omega. The size recurrence gives g_(t+1)=|B|+q+g_t and f_(t+1)=2|B|+q+g_t. Both are legitimate prefixes once 0<=g_t<q_t; these inequalities persist under the displayed positive recurrence.

Since Q(W)=(t-1)omega, Q(V)=-t-omega and the phases are omega,omega^2, one gets

```
Q(BW)=-1-omega,   rho(BW)=1,
Q(B^2W)=-t,       rho(B^2W)=omega^2.
```

Therefore G_t=Q(prefix(W_t,g_t))=-(t+2)(1+omega) follows by induction, and

```
Q(prefix(W_t,f_t))=(1-t)+(t+1)omega.
```

The length recurrence preserves q_t-v_t/2 modulo three and hence f_t=2 mod3. Substitution in the actual prefix-axis formula gives **A_(f_t)=1-t+omega for every t>=1**. All W_t are lower convergent prefixes of the same alpha_*; these states are therefore actual, origin-anchored states of that one path. This proves a hit, not firstness. The checker passes 25 induced levels; the recurrence above, rather than that finite count, proves all levels. [New record certificate](record_returns_check.py).

Since q_t=Theta((7+4sqrt(3))^t), f_L=Theta(q_L) while q_(3L)=Theta(q_L^3). The nonnegative ray profile sum_a h_L(A_a)2^(-a) is at least 2^(-f_L). Consequently large recentering alone cannot imply a uniform exp(-delta q_(3L)) upper bound on this profile. This is an obstruction on the comparison slope alpha_*, not a special no-go theorem for log_3 2, nor a lower bound on a signed total-density approximation error. [New record certificate](record_returns_check.py), [comparison path definitions](cf_induction.md).

**6. PASS for the exact four-array product-tail identity, without arithmetic closure.** Keep the true or model horizontal state in the first index and the true or model vertical state, including its matching correction and all low rules, in the second. Then the mixed array is c_TT-c_MT-c_TM+c_MM. It vanishes if a<R because the two horizontal states agree there; it vanishes if b<S because the entire vertical input agrees there. Every coefficient has magnitude at most 6. Absolute convergence proves

```
M=Z_TT-Z_MT-Z_TM+Z_MM,
|M|<=18*2^(-R)*3^(-S).
```

This statement is about actual arrays and their weighted sums, not just arbitrary lattice probes. The certificate recovers its support and bound in the stated small physical rectangle. The two hybrid sums remain genuine infinite unknowns. The better product tail is a bound for M, not automatically for Z_TT-Z_MM or for a rational approximation to Z_TT. [New record certificate](record_returns_check.py).

**7. PASS for the final reciprocal-row coupling, with alpha_* scope and the J=1 base.** Write d_t=p_t-(u_t+19)/2. The convergent bounds in the final note imply

```
53/66 < f_t alpha_*-d_t < 24/29+1/66 < 1.
```

They also put theta_t/alpha_* between 1 and 2, (theta_t+1)/alpha_* between 2 and 3, and (theta_t+2)/alpha_* between 4 and 5. Hence n_(d_t)=f_t-2, n_(d_t-1)=f_t-3, and n_(d_t-2)=f_t-5. The complementary Beatty sequences up to f_t+d_t have prefix lengths f_t,d_t. Their negative-character sums add to -1, and the B recurrence gives B_(d_t)=(t+1)+omega. Its last increment is 1, so B_(d_t-1)=t+omega. At b=d_t-1=2 mod3 the isolated test is active in color 1, giving E_b=omega. With C_(2,2)=1, the exact row offset is t. Thus (a,b)=(f_J,d_(J-1)-1) has full corrected state omega for every J>=1. [Final record note, (R12)-(R17)](record_returns.md).

The base J=1 uses f_0=11,d_0=6, B_5=omega, E_5=omega and zero row offset, together with A_(f_1)=omega. It does not use the negative auxiliary g_0. The separate t=0 seed gives A_(f_0)=1+omega. Both coupled physical indices are Theta(q_J); their positive weight is exp(-O(q_(3J)^(1/3))). This strengthens the obstruction to actual coupled states of the same fixed comparison cocycle. It remains a hit theorem for alpha_* only, with no firstness, target-logarithm, signed-error or comparison-board optimality claim. The updated record certificate passed all its 25 levels and its bounded independent reciprocal-row checks. [Final record note, (R10), (R16)-(R18), scope paragraph](record_returns.md), [updated certificate](record_returns_check.py).

**8. PASS for the actual no-1001 theorem and its limited arithmetic force.** For b>=4 the corrected state has curl r=omega^(-j) and horizontal edge u in {0,omega^(-j-1),-omega^(-j)}. For j=0 each permitted u weakly decreases the two cone forms. For j=1 the only possible exit has u+r=0. For j=2 either u+r=0 or u+r=(1,1), which cannot turn an outside point into an inside point. These cases exclude motif 1001 at d,2d,3d,6d for every actual high-row context, without bounding the cocycle. The mantissa formula retains both exceptions; its transformed color is k+h+1 and the five intervals give the listed necessary vertical alphabet. This argument imposes necessary local conditions, not independently selectable edge states. [Carry note, (AC1)-(AC3)](actual_carries.md).

The actual witness table contains the other fifteen motifs and both ends of each elementary arithmetic carry. The explicit 972,1458,2916 modification preserves weighted mass and survives every affected high-row no-1001 test; it need not satisfy the full actual recurrence. The row-pair countermodel has rational mass 3/4 for every sequence of choices, and exhausting pair boundaries proves its forbidden-pattern property. Nonperiodic choices and any finite actual head remain possible, with a zero buffer before the translated rational tail. Retaining all witnesses preserves the complete high-row language. This defeats deductions from that language and a finite head, not from the full actual floor/cocycle process. The carry certificate passed, including its independent count witnesses and tiny cover checks. [Carry note, second question](actual_carries.md), [carry certificate](actual_carries_check.py).

The low-event prose initially assigned the patch at 3*2^a already for a=1 and attributed the cutoff-3 exception to root 1. The correct facts are: the root 2^(a-1) is valid only for a>=2; at cutoff 6 its would-be value is 1; at cutoff 3 it is 1/2. The author has corrected those sentences; the table was already right. The dyadic isolate-cancellation explanation likewise requires a>=1, with the origin's zero digit checked directly. These wording corrections do not affect the b>=4 motif proof. [Carry note, low-event paragraph](actual_carries.md).

**9. PASS for the conditional product-tail arithmetic interface; its premise is unproved.** With J=Z_MT+Z_TM-Z_MM, the exact bound concerns |Z-J|. If DJ were integral at the old degree-six clearing cost, then

```
|DZ-DJ|<=486(1+o(1))*2^(4q-2q_next).
```

Under rationality, q_next-2q->+infinity would then force eventual equality. This exponent and the weaker integer-discreteness criterion are correct. But DJ in Z, fixed-term compression of J, and the actual infinite eligible supply have not been proved. Substituting J=Z-M adds no arithmetic information. The final note explicitly states all these limitations. [Final record note, (R19)-(R20) and arithmetic gaps](record_returns.md).

### Gaps

- The CF and carry work supplies neither an adequate target-slope physical weighted return nor bounded arithmetic coefficient data.
- No eventually nonresonant-tail hypothesis is proved for the actual logarithmic slope.
- Both final follow-ups have now been checked. Their comparison-path and local-language obstructions are not impossibility theorems for every controlled parameterized or signed return construction.

## Does the arithmetic criterion now accept an adequate infinite construction?

### Takeaway

**FAIL for completion of the requested goal.** The complete local product and projective height are correctly accounted for, but no new branch has supplied an adequate infinite upper construction. For an integer-cleared rational model, error tending to zero is sufficient under rationality; demanding a fixed exponential margin there would needlessly strengthen the target. Nonvanishing may remain a separate later task, but the adequate upper construction itself is still missing. [Reflection arithmetic section](numerator_reflection.md), [paired conclusion](two_sided_models.md), [CF conclusion](cf_induction.md).

### Cited Findings

- The primary one-form p-adic Subspace Theorem uses a distinguished nonzero coefficient, all other coordinate factors over S, and projective Weil height, and concludes containment in finitely many proper subspaces. [Luca-Ouaknine-Worrell, Theorem 1](https://arxiv.org/html/2412.07908v2#S2.Thmtheorem1), checked directly in this audit.
- The primary fixed-term nonzero lower bound requires 0<t<=min(1,u_1,...,u_m). Its proof handles exceptional hyperplanes by induction; its density application separately proves a nonzero choice. [Saved KK primary text, Proposition 7.4 and Corollary 6.5](../Erdos%20theorem%20transfer%20investigation/erdos1062-fork-free-density.pdf.txt), [upstream manuscript](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf).
- The accepted convergent supply and previous final audit give the sharp current budget and distinguish the stronger fixed exponential condition from the weaker integer-discreteness condition. [Supply note](../infinite-return-construction/diophantine_supply.md), [previous final audit](../infinite-return-construction/final_return_audit.md).

### Inferences

**1. The full three-place product is exactly the one claimed.** Under Z in Q, use x=(N,UV,U,V,1) and distinguish N at infinity. The four remaining coordinates are positive {2,3}-units and their entire S-products are one. Therefore

```
Phi(x)=|DZ-N| |N|_2 |N|_3,
H(x)<=162UV=exp((6+o(1))q log2).
```

The final coordinate 1 makes the integral vector primitive. Zero coordinates lie in fixed hyperplanes, and the primary covering theorem still supplies only a finite union of proper subspaces. It does not turn a newly claimed p-adic gain into a contradiction without controlling those relations. The existing real-smallness lower-bound induction is not a substitute for a new exceptional-relation argument using only extra p-adic smallness. [Reflection note, (A1)-(A2)](numerator_reflection.md), [primary Theorem 1](https://arxiv.org/html/2412.07908v2#S2.Thmtheorem1).

Scaling x by 1/(UV) preserves the height and the complete local product. The N-coordinate's 2-adic and 3-adic product gains precisely UV, canceling the real scaling. The smallest displayed unit becomes 1/(UV), so the real error E/(UV) must be compared with that scale, leaving the same ratio |E|. Moreover N/(UV) is an S-integer with variable numerator, not the integer term of the mixed lower bound. [Reflection arithmetic section](numerator_reflection.md).

**2. Reflection and real rationality do not identify a p-adic limit.** A quadrant positive-weight sum sum c(a,b)2^a3^b is not a 2-adic or 3-adic convergent series: one coordinate axis supplies terms of bounded valuation. A rectangular matching prefix cannot determine the entire opposite infinite strip needed for a local residue. Rational periodic resummation of that strip stores its full numerator; it does not identify it with the rational real target. The exact palindromic countermodel has real limit zero and cleared numerator -3(U+V+5), with both 2-adic and 3-adic valuations identically one. It satisfies bounded digits, exact reversal and arbitrarily long prefixes, so those properties alone cannot prove growing numerator divisibility. It is not an actual cocycle counterexample and is correctly scoped as a failure of that generic implication. [Reflection note, (N4)-(N5) and p-adic discussion](numerator_reflection.md).

**3. The sharper integer-cleared criterion is essential.** If Z=A/B, then E=DZ-N belongs to B^(-1)Z. Consequently E->0 already forces eventual equality, without any Subspace Theorem margin. The current exact rectangular bound is

```
|E|<=486(1+o(1))2^(5q-q_next).
```

Thus infinitely many actual eligible indices with q_next-5q->+infinity suffice for the upper approximation, with eventual equality then requiring a separate nonstabilization argument. In particular an infinite eligible next-digit-at-least-five supply would suffice. Such a supply has not been proved. The known smaller ratio supply, the reflected identities, and the paired factor do not supply it. [Previous final audit, scalar criterion](../infinite-return-construction/final_return_audit.md), [reflection conclusion](numerator_reflection.md).

For a genuinely nonintegral fixed-unit architecture, the acceptance condition remains the capped t<=min(1,u_i), controlled height, fixed dimension and rational coefficient data, and a real error small enough relative to t for the invoked theorem. Fixed term count with proved subexponential multiplicities can be allowed after paying the quantified coefficient loss; growing term count or merely small spatial support is not justified by that extension. [Coefficient extension](../../early-attacks/augmentation-and-return-attacks/coefficient_extension.md).

### Gaps

- No audited construction provides an actual unbounded sequence with an adequate weighted upper error and its complete arithmetic cost. The sharp latest frontier is the uncompressed hybrid value J in the proved mixed-corner construction. This is a failure to complete the requested research goal, not an impossibility theorem.
- Nonvanishing/nonstabilization is separate and also unproved; omitting it does not repair the missing upper construction.
- No Lean, installation, broad scan, density decimal, archived edit or external posting was performed. The only new executable file is the adjacent exact certificate; the supplied paired, CF, final record and actual-carry checks were run with imported bytecode disabled.
