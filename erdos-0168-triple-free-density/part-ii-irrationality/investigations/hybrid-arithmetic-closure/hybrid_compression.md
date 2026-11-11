# Hybrid arithmetic and reciprocal-axis compression

**Status: no adequate infinite weighted-return family has been constructed.** This first-round investigation proves an exact one-axis integer-alphabet normal form for the two hybrids, rigorously disproves their unconditional D-integrality for two actual logarithmic models, certifies opposite scalar approximation signs at those models, and derives an origin-anchored reciprocal-axis identity. A targeted discounted minimum-potential identity fails on an actual high-row square. A surviving exact state-translation identity localizes cone curvature to a weighted point local time. These results constrain a replacement construction; they do not prove hybrid rationality, conditional rationality transfer from Z, or infinite nonstabilization. — [Exact certificate](hybrid_compression_check.py), [previous frontier](../reflected-return-models/REPORT.md).

## What arithmetic remains after each periodic axis is summed exactly?

### Takeaway

Each hybrid is a single integer-alphabet series in base 3 or base 2, with an explicit rational prefactor. The alphabets have exponentially growing size and height as q grows. The specific premise D J in Z is false unconditionally for both actual 5/8 and 53/84 hybrids; at 53/84, even an additional integer factor at most 2^60 cannot repair it. — [Certificate](hybrid_compression_check.py).

### Cited Findings

- The complete finite formula C and exact corrected birth rules are established inputs. For b>=4, the coefficient is 1-3F(A_a+B_b-1+C_ab-E_b), where F(x+y omega)=1_[x<=0,x-y<=0]. The four low rows have distinct rules, including the unique origin exception at (0,1). — [Finite proof](../prefix-and-phase-audit/REPORT.md), [audited full model](../global-boundary-proof/independent_audit.md).
- For a nonresonant p/q, P=3q and Q=3p are the model-axis periods. Put U=2^P, V=3^Q and D=27(U-1)(V-1). The full model Z_MM satisfies N=D Z_MM in Z. The hybrid comparison is J=Z_MT+Z_TM-Z_MM, and its exact real residual obeys |Z-J|<=18*2^-R*3^-S when the corresponding axis inputs match for a<R and b<S. — [Full product-tail proof](../reflected-return-models/record_returns.md).
- The new executable uses only the standard library and the existing audited model helper in two_sided_models_check.py; it edits neither helper nor older data. It independently performs both periodic-axis evaluations and both agree exactly with the complete saved model value. Actual logarithmic floors are computed by integer comparisons of powers of 2 and 3, not floating point. — [Certificate source](hybrid_compression_check.py), [reused model helper](../reflected-return-models/two_sided_models_check.py).

### Inferences

**1. An exact integer-alphabet normal form.** Remove only the exceptional override eta(0,1)=1, and denote the resulting generic coefficients by c^0. In each hybrid and the full model this removal changes that coefficient from -2 to 1, adding exactly one to the full weighted value. All other low rules and every E term remain. The periodic horizontal data of MT therefore give

```
S_b = sum_(r=0)^(P-1) c^0_MT(r,b) 2^(P-1-r),
Z_MT = 2/(U-1) sum_(b>=0) S_b 3^(-b) - 1.             (H1)
```

Here S_b is an integer satisfying

```
-2(U-1) <= S_b <= U-1,
S_b = (U-1)-3 W_b,      0<=W_b<=U-1.                  (H2)
```

The last assertion follows by encoding the P binary birth digits in ordinary binary order. The finite horizontal sum is exactly 2 S_b/(U-1); no tail in the actual vertical axis has been discarded. — [Certificate, row function](hybrid_compression_check.py).

For TM, keep the four low rows and then sum the Q-periodic high vertical tail. Define

```
T_a = (V-1) sum_(b=0)^3 c^0_TM(a,b) 3^(3-b)
    + sum_(r=0)^(Q-1) c^0_TM(a,4+r) 3^(Q-1-r).
```

Then

```
Z_TM = 1/[27(V-1)] sum_(a>=0) T_a 2^(-a) - 1,         (H3)
-81(V-1) <= T_a <= (81/2)(V-1),       T_a in Z.
```

The factor 27 is essential: multiplying the high tail's geometric denominator by 27 changes its lowest power to 3^0, while every low-row denominator also clears. The bounds follow from -2<=c<=1 and total vertical weight 3/2. Since V is odd the upper bound is integral. — [Certificate, column function](hybrid_compression_check.py).

Combining (H1) and (H3) gives the exact arithmetic identity

```
D J = 54(V-1) sum_(b>=0) S_b 3^(-b)
    + (U-1) sum_(a>=0) T_a 2^(-a) - 2D - N.           (H4)
```

Thus the missing arithmetic is a relation between two very specific integer-alphabet series. Treating their alphabets as finitely many S-unit terms is invalid: the series are still infinite, and their alphabet bounds grow like U and V. Rationality of a noncanonical integer-alphabet expansion does not imply eventual periodicity of the original coefficients. Normalizing by U or V charges those factors in denominators or minimum-unit scale; it does not make the height free. These conclusions follow directly from (H1)-(H4) and the fixed-term arithmetic interface. — [Current arithmetic audit](../reflected-return-models/final_reflected_audit.md).

**2. Rigorous actual-logarithm interval certificates.** The certificate sums MT exactly over every horizontal index and b<B, and sums TM exactly over every vertical index and a<A. Let the resulting finite value, after subtracting the exact Z_MM, be j_0. Every omitted coefficient lies in {-2,1}; therefore, with w=2^-A+3^-B,

```
j_0-6w <= J <= j_0+3w.                               (H5)
```

Indeed the omitted MT geometric weight is 3*3^-B and the omitted TM weight is 3*2^-A. Their lower coefficient bound -2 gives -6w and their upper bound 1 gives 3w. The unique origin correction is already included in the finite sums. This is a full infinite enclosure, not a finite numerical approximation without tail control. — [Certificate, lower/upper construction](hybrid_compression_check.py).

For p/q=5/8, sigma=+, choose (A,B)=(78,60). Exact arithmetic yields

```
D = 6499836386373330,
floor(DJ) = 7856298909435584,
788789/1048576 < {DJ} < 788790/1048576.                (H6)
```

The enclosed interval has width less than 1/5166442. In particular, DJ is not an integer. The full model integer is N=7856298907408926, so floor(DJ)-N=2026658. The certificate also directly verifies all true/model floor equalities for a<27,b<17 and the first disagreements at 27 and 17. Combining (H5) with the full product-tail bound proves

```
Z > Z_MM(5/8,+).                                     (H7)
```

For p/q=53/84, sigma=-, choose (A,B)=(744,558), and write N=D Z_MM as the exactly reconstructed integer. The enclosure proves

```
N-1 < DJ < N,
-2^-60 < DJ-N < -2^-100.                              (H8)
```

Its width is less than

```
1/7225569665555532000918685837847066833710752183515298391111426953082513.
```

Here all true/model floors agree for a<569,b<359, checked directly, and the first disagreements are exactly those endpoints. The product-tail correction is smaller than the negative gap, giving

```
Z < Z_MM(53/84,-).                                   (H9)
```

Both signs concern the complete actual infinite density series through its proved finite formula. They establish named nonvanishing and show that the actual-slope value is neither a minimum nor a maximum against these two scalar model values. The two fractions lie on opposite sides of the actual slope, so these signs do not disprove an increasing-in-slope principle. — [Complete asserted certificate](hybrid_compression_check.py).

**3. A bounded-factor repair is already expensive in a named case.** If DJ=m/k in lowest terms at 53/84, (H8) implies

```
1/k <= N-m/k < 2^-60,
```

so k>2^60. Consequently no positive integer multiplier at most 2^60, including any such smooth multiplier 2^u3^v, makes DJ integral there. This is an unconditional implication if J is rational; rationality of J itself is not proved. It does not exclude one fixed larger multiplier for that one case or a specially chosen infinite subsequence. — [Certificate, final 53/84 assertions](hybrid_compression_check.py).

### Gaps

- Actual DJ nonintegrality disproves an unconditional universal D-integrality assertion. It does not refute a theorem conditional on Z rational, or a specially selected infinite family; proving such a conditional implication would itself be powerful.
- The exact two named nonvanishing results do not establish infinitely many adequate returns or nonstabilization.
- Neither (H4) nor a finite alphabet establishes a fixed rational span generated by Z. No replacement arithmetic closure is proved.

## Can exact reciprocal-axis coupling turn the hybrids into one discounted potential?

### Takeaway

The true axes are not independent: along the merged Beatty boundary their states are conjugates up to a nine-entry residue table. This supplies one origin-anchored master walk for both hybrid profiles. The natural minimum potential fails the proposed discounted harmonic test even on an actual high-row square; its translated cone curvature nevertheless has an exact point-source identity. — [Certificate](hybrid_compression_check.py).

### Cited Findings

- The actual axes satisfy 3A_a=2+omega^(-a)+(1-omega^2)Q_A(a), where Q_A(a)=sum_(k=1)^a omega^(-k-floor(k alpha)); the reciprocal formula conjugates the corresponding root sum. The earlier record theorem used Beatty complementation at particular comparison-slope indices. — [Exact induction](../reflected-return-models/cf_induction.md), [earlier specialized coupling](../reflected-return-models/record_returns.md).
- The actual cone state is z_ab=A_a+B_b-1+C_ab-E_b, with a unit mixed curl; its horizontal/vertical increments are not arbitrary independent translations. — [Actual carry and increment identities](../reflected-return-models/actual_carries.md).
- The new certificate checks the reciprocal identity on both types of merged boundary points, computes the actual discounted counterexample, and verifies the point-source stencil on a bounded grid. The proofs below establish their full stated scopes. — [Certificate](hybrid_compression_check.py).

### Inferences

**1. General actual reciprocal identity.** Let alpha=log_3 2. At any merged boundary pair with b=floor(a alpha) or a=floor(b/alpha), put n=a+b. The complementary positive-integer sequences

```
k+floor(k alpha),             ell+floor(ell/alpha)
```

partition the positive integers. Up to n, their respective prefix lengths are a and b. This follows directly from the two opposite strict floor inequalities; alpha is irrational, so there are no shared endpoints. Hence

```
Q_A(a)+Q_B(b)=T_n,      T_n=sum_(j=1)^n omega^(-j).
```

Conjugate the A formula and add the reciprocal B formula:

```
3(B_b+conj(A_a))
 =4+omega^a+omega^b+(1-omega)conj(T_(a+b)).
```

The three possible T_n values are 0, omega^2 and -1. Substitution gives the exact nine-entry table

```
B_b+conj(A_a)=Lambda_(a mod3,b mod3),
Lambda = [[2,       2+omega, 1],
          [2+omega, 1+omega, 1],
          [1,       1,       1]].                      (H10)
```

The root-sum formulas follow by telescoping the exact axis increments, so this is a theorem about the actual logarithmic axes from their fixed origin. It is not an assignment of an arbitrary lattice state. — [Axis root-sum formulas](../reflected-return-models/cf_induction.md), [new exact checks](hybrid_compression_check.py).

An equivalent single-walk description orders the axis births 2^a and 3^b. The horizontal birth k has merged index k+floor(k alpha); the vertical birth ell has merged index ell+floor(ell/alpha). Let S_n be the sum of omega^(-j) over horizontal events j<=n. At a horizontal event S increments by omega^(-n); at a vertical event it stays fixed. The counts a,b and their residues give A and B from S_n and T_n through the formulas above. Thus the two integer-alphabet profiles in (H4) can be evaluated on one master walk with a finite residue controller. Their discounts remain 2^-a at horizontal events and 3^-b at vertical events; the walk state is accumulated and unbounded. — [Proof of (H10)](hybrid_compression_check.py).

**2. The direct discounted harmonic guess fails on an actual square.** Take mu(x,y)=min(x,y,0). At the actual high-row points d=81,2d=162,3d=243,6d=486, the corrected states are respectively

```
(0,0), (0,-1), (0,0), (0,0).
```

Therefore

```
(1/2)mu(z_162)+(1/3)mu(z_243)+(1/6)mu(z_486)-mu(z_81)
 = -1/2.                                             (H11)
```

The weights sum to one and are precisely the reciprocal carry weights, but the minimum potential is not harmonic for these actual transitions. This excludes the bare candidate, not an augmented q-dependent discounted potential or an identity with a retained residual. — [Actual-state certificate](hybrid_compression_check.py).

**3. Exact localization of state-space curvature.** Write F(x,y)=1_[x<=0,x<=y]. On integer states,

```
F(x,y)-F(x,y-1)=1_[x=y<=0].
```

Subtract this relation at (x-1,y-1). The diagonal ray is unchanged except at its endpoint, proving for every integer x,y

```
F(x,y)-F(x,y-1)-F(x-1,y-1)+F(x-1,y-2)
 = -1_[(x,y)=(1,1)].                                 (H12)
```

Equivalently, if T_v acts by translating the state argument by v,

```
(1-T_(0,-1))(1-T_(-1,-1))F = -delta_(1,1).
```

For the high-row weighted translated cone sum

```
Q(s)=sum_(a>=0,b>=4) F(z_ab+s)/(2^a3^b),
```

absolute convergence allows the same two differences, giving

```
Q(s)-Q(s-(0,1))-Q(s-(1,1))+Q(s-(1,2))
 = -sum_(a>=0,b>=4) 1_[z_ab+s=(1,1)]/(2^a3^b).        (H13)
```

This is a precise positive point-local-time residual, with the minus sign displayed. The translations in (H12)-(H13) are state translations, not physical shifts of a or b. Replacing one by the other without a phase-dependent transition proof would be invalid. In particular, rationality of the original Z supplies no rationality of the other three translated sums. — [Exact stencil check](hybrid_compression_check.py), [earlier translation limitations](../infinite-return-construction/weighted_returns.md).

### Gaps

- Master-walk coupling reduces the number of independent state paths; it does not bound the accumulated register or establish a discounted coboundary for the profiles in (H4).
- No q-dependent potential has been found whose entire discounted residual has adequate arithmetic or exponentially late actual support.
- The point-local-time identity is exact but contains translated values with no proved rationality transfer and no actual infinite weighted-return theorem.

## What would make this a valid arithmetic return rather than a real identity?

### Takeaway

The old universal D-integrality shortcut is now explicitly false on actual inputs. A replacement must control the coupled series (H4), or construct a different discounted potential with all residual arithmetic charged. The current results still do not establish the objective's infinite family. — [Exact arithmetic counterexamples](hybrid_compression_check.py).

### Cited Findings

- For the scalar model, ordinary rational discreteness is sufficient if q_next-5q tends to infinity along eligible indices, followed by a separate nonstabilization argument. For a hypothetical D-integral hybrid J, the product tail would improve that threshold to q_next-2q tending to infinity; D-integrality is an additional premise, not a consequence of the real bound. — [Previous final audit](../reflected-return-models/final_reflected_audit.md).
- A nonintegral S-unit alternative must keep fixed term count, controlled coefficients and height, a nonzero error, and the capped scale 0<t<=min(1,u_i). Growing integer-alphabet profiles do not meet that theorem simply because their entries are bounded at a fixed q. — [Audited arithmetic interface](../reflected-return-models/final_reflected_audit.md).

### Inferences

The concrete next candidate is a discounted potential on the merged walk (H10), with q-dependent finite source data, whose residual can be written using controlled point local times as in (H13). A proof would need to identify the actual transitions, retain the indicator and low-row terms, prove the complete arithmetic form and height, and obtain sufficient late support or signed cancellation on an unbounded actual sequence. Merely replacing ray occupations by point occupations, or merely identifying a closed finite state loop without discounts, does not complete any of those obligations. — [Exact normal form and potential test](hybrid_compression_check.py).

The named nonvanishing certificates are genuine progress against false global min/max or exact-equality guesses, but they do not create the required infinite supply. The goal remains open; no unconditional irrationality conclusion follows from the present note. — [Certified scope of (H7)-(H9)](hybrid_compression_check.py).

### Gaps

- No arithmetic closure of J, no replacement adequate infinite approximation, and no infinite nonstabilization theorem were obtained.
- No Lean, installs, broad scans, density decimal evaluation, edits to older folders, external posting, or priority claim were undertaken. The only new executable is the adjacent exact certificate; its reused local model helper is an explicit dependency.
- The main risk is confusing (H10)'s exact coupling or (H13)'s compact state-space source with the missing arithmetic and physical-index return estimates.
