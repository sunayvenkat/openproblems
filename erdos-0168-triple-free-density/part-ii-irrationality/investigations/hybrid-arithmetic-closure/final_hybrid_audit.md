# Fresh audit of hybrid arithmetic closure

## Do the one-axis normal forms and the named actual arithmetic certificates hold?

### Takeaway

**PASS for the exact normal forms, complete-tail nonintegrality certificates, named scalar signs, actual reciprocal-axis table, and the 12/19 followup.** The unconditional premise `D J in Z` fails at the two named actual models. These facts neither refute a conditional theorem under `Z in Q` nor produce an infinite family. [Hybrid note](hybrid_compression.md), [hybrid certificate](hybrid_compression_check.py), [bracketing followup](hybrid_bracketing.md), [bracketing certificate](hybrid_bracketing_check.py).

### Cited Findings

- Accepted inputs are the internally proved finite formula `tau=min_j(K_j-I_j-P_j)`, the origin-anchored axis dynamics and all four low-row rules, and the prior return/arithmetic frontier. This audit does not reprove the finite combinatorial theorem. [Finite theorem](../prefix-and-phase-audit/REPORT.md), [model definitions and frontier](../reflected-return-models/REPORT.md), [preceding fresh audit](../reflected-return-models/final_reflected_audit.md).
- All five scripts ran successfully with `python -B`, from the workspace root, including both finalized focused followups and the hardened first hybrid script. Source inspection confirmed exact integers/Fractions; logarithmic floors use integer power comparisons, and golden floors use integer square roots. There is no floating-point logarithm, density decimal, or omitted indicator/low-row branch in the named actual enclosures. [Hybrid certificate](hybrid_compression_check.py), [global-carry certificate](global_carries_check.py), [adaptive certificate](adaptive_induction_check.py), [bracketing certificate](hybrid_bracketing_check.py), [absorption certificate](hierarchy_absorption_check.py).
- The hybrid script reuses the already audited complete model helper; the new row and column evaluations agree separately with its exact full model value. Thus the two evaluations are separate summations, not independent reproofs of the shared model definitions. [Model helper](../reflected-return-models/two_sided_models_check.py), [hybrid certificate](hybrid_compression_check.py).

### Inferences

**1. PASS: H1-H4, including every correction and denominator.** Set `P=3q`, `Q=3p`, `U=2^P`, `V=3^Q`, and `D=27(U-1)(V-1)`. Removing just the exceptional `(0,1)` birth changes its coefficient from `-2` to `1` and hence adds exactly `3/3=1` to any complete sum. The resulting generic horizontal coefficients are P-periodic in the horizontal model, even in the four low rows. Their binary numerator is

```
S_b=sum_(r<P)c^0_MT(r,b) 2^(P-1-r)
   =(U-1)-3W_b,        0<=W_b<=U-1.
```

Consequently `Z_MT=2/(U-1) sum_b S_b 3^-b-1` exactly. The true vertical tail and its actual E terms have not been replaced or truncated. [Hybrid note, H1-H2](hybrid_compression.md), [row implementation](hybrid_compression_check.py).

For TM, only the high vertical part is Q-periodic: positive-index side conventions give `m(b+Q)=m(b)+3q` for every argument used when `b>=4`, so both exception tests and the E color repeat. The four low rows must stay separate. Multiplying their sum and the high periodic tail by `27(V-1)` gives exactly the stated integer `T_a`; the high term's last exponent is zero. The total vertical weight is `3/2`, so the bounds are `-81(V-1)<=T_a<=(81/2)(V-1)`. Restoring the origin override subtracts one. Multiplying the two formulas by D and subtracting `N=D Z_MM` proves H4 with constant term **`-2D-N`**. No finite-term or rationality closure follows from an integer alphabet whose size and heights grow with U,V. [Hybrid note, H3-H4](hybrid_compression.md), [column implementation](hybrid_compression_check.py), [arithmetic scope](../reflected-return-models/final_reflected_audit.md).

**2. PASS: H5-H9 are full infinite enclosures.** The omitted MT weight is `3*3^-B`; the omitted TM weight is `3*2^-A`. Coefficients lie in `[-2,1]`, giving `j_0-6w<=J<=j_0+3w` with `w=2^-A+3^-B`. The finite TM sum includes the actual origin exception directly, while the MT summation subtracts the entire exceptional weight once; the tails therefore do not lose an origin term. The sign comparison then adds the *separate* exact mixed-corner allowance `18D*2^-R*3^-S`. [Hybrid note, H5](hybrid_compression.md), [hybrid certificate](hybrid_compression_check.py), [accepted mixed-corner proof](../reflected-return-models/record_returns.md).

At 5/8 the reproduced output is `D=6499836386373330`, `floor(DJ)=7856298909435584`, and `788789/1048576<{DJ}<788790/1048576`, with cutoffs `(78,60)`, floor window `(R,S)=(27,17)`, and a strictly positive full `Z-Z_MM`. At 53/84 the cutoffs are `(744,558)` and the floor window is `(569,359)`; the enclosed gap satisfies `-2^-60<DJ-N<-2^-100`, and remains negative after the full mixed-tail allowance. The model-side conventions are the actual matched ones, respectively plus and minus. [Exact assertions](hybrid_compression_check.py).

The positive 5/8 sign was initially printed without a dedicated assertion. At this auditor's request, its author added `assert gap_lower-mixed>0`; this is a narrow certificate hardening, not a change to the mathematical bound. The 53/84 sign already had an assertion. [Hardened hybrid certificate](hybrid_compression_check.py).

If `DJ=m/k` in lowest terms at 53/84, then `0<N-m/k<2^-60`, and the nonzero integer `Nk-m` yields `1/k<=N-m/k`. Hence `k>2^60`. This is conditional only on DJ being rational; nonintegrality itself is unconditional. A single named failure does not exclude a conditional rationality implication, a larger repair factor, or a selected infinite family. [Hybrid note, H8 and bounded-factor conclusion](hybrid_compression.md).

**3. PASS: actual Beatty reciprocity and point curvature.** At either merged boundary pair, the positive Beatty event indices `k+floor(k alpha)` and `ell+floor(ell/alpha)` partition `{1,...,a+b}` with respective prefix lengths a,b. Thus `Q_A(a)+Q_B(b)=T_(a+b)`. Conjugating the horizontal root-sum formula and adding the reciprocal formula gives

```
3(B_b+conj(A_a))
 =4+omega^a+omega^b+(1-omega)conj(T_(a+b)).
```

Substituting `T_n=0,omega^2,-1` for residues `0,1,2` gives precisely the stated nine-entry Lambda table. The common initial states remain `A_0=B_0=1`. This is genuine coupling, but the root-sum register still accumulates and its two discounts differ. [Hybrid note, H10](hybrid_compression.md), [root-sum formulas](../reflected-return-models/cf_induction.md), [exact table check](hybrid_compression_check.py).

For `F(x,y)=1_[x<=0,x<=y]`, the first difference is the diagonal ray `1_[x=y<=0]`; subtracting its translate at `(x-1,y-1)` leaves **`-1_[(x,y)=(1,1)]`**. Absolute convergence proves H13 with the same minus sign. These are state translations; they cannot be replaced by physical index shifts. The actual square at 81,162,243,486 independently gives the minimum-potential residual `-1/2`, so the bare harmonic guess really fails on the actual path. Neither identity transfers rationality to translated cone sums. [Hybrid note, H11-H13](hybrid_compression.md), [exact actual-state and stencil checks](hybrid_compression_check.py).

**4. PASS: one actual-convergent strict reverse ordering at 12/19.** The CF prefix `[0;1,1,1,2,2]` has terminal convergents 5/8,12/19; its cylinder endpoints are 17/27 and 12/19. The strict power comparisons `2^27>3^17` and `2^19<3^12` place the actual logarithmic slope in that cylinder. Thus 12/19 is an actual upper nonresonant convergent. [Bracketing note](hybrid_bracketing.md), [exact CF and power assertions](hybrid_bracketing_check.py).

For the actual rectangle `a<160,b<110`, its exterior weight is exactly `3v`, where `v=2^-160+3^-110-2^-160*3^-110`; therefore `S-6v<=Z<=S+3v`. Reproduced exact model numerators and integer enclosures are

```
D=584034748065108629302925842213505040,
D Z_plus =705918015253698271783679476310697738,
D Z_minus=705918008015665023891011916838310910,

-7238033247892667559404885391 < D(Z-Z_plus)
                                  < -7238033247892667559404885390,
67501437 < D(Z-Z_minus) < 67501438.
```

This proves `Z_minus<Z<Z_plus`. It refutes a fixed ordered convention `Z_plus<=Z<=Z_minus`; it supports this one unordered bracket instance and leaves any infinite unordered bracketing theorem open. The two upper-convergent minus models 12/19 and 53/84 also have opposite matched-side errors, so the side label alone does not supply a uniform error sign. [Bracketing certificate](hybrid_bracketing_check.py), [53/84 certificate](hybrid_compression_check.py).

### Gaps

- No H1-H4 arithmetic closure under `Z in Q` is established. The actual nonintegrality examples do not logically disprove such a conditional closure. [Hybrid conclusion](hybrid_compression.md).
- No named strict sign or finite bracket proves infinitely many nonzero errors on an adequate return family. [Bracketing limitations](hybrid_bracketing.md).

## Do the reversal, positive-token, and complementary-resonance theorems survive independent reconstruction?

### Takeaway

**PASS, with the scopes stated in the notes.** The pure reversal sign has the correct physical-weight orientation; token retiming is a global vector identity; the complementary induction handles both parities; and the golden example supplies all-level corrected defects and an individual-row denominator bound. These results give no target-logarithm impossibility theorem or signed-error lower bound. [Global-carry note](global_carries.md), [adaptive note](adaptive_induction.md).

### Cited Findings

- The global-carry checker passed 1,750 cyclic cases, 11,250 balanced cases, 23 exact retiming cutoffs, two actual-context exceptional-grade comparisons, and the full 5/8 paired scalar comparison. The finite cases supplement algebraic proofs; they do not establish an infinite statement by exhaustion. [Carry certificate](global_carries_check.py).
- The adaptive checker passed both parity transfers and both nontrivial phases, the narrow direct band checks, and its three direct checks of the all-level golden formulas. Its golden floors use integer square roots; adjacent rational brackets separately cross-check the relevant formula on a fixed initial range. [Adaptive certificate](adaptive_induction_check.py).

### Inferences

**5. PASS: complete reversal, with weights attached to physical tokens.** Let `n(k)` be the first k tokens' color count and N the full count. In the reverse processing order those same physical first k tokens are processed last. Their total increment is `m(Q+N)-m(Q+N-n(k))`. Subtracting the forward prefix gives exactly GC1. Since the full prefix difference is zero, summation by parts gives GC2 with `w_(k-1)-w_k>=0`. This proves the stated **reverse-minus-forward min-birth** sign, and multiplying by `-3` reverses the c sign. [Global-carry note, GC1-GC2](global_carries.md).

For a balanced block, common translations give `D(k)=2m(Q)-m(Q+n(k))-m(Q-n(k))`. A coordinate minimizing Q bounds the sum of the last two minima by `2m(Q)`. For a cyclic word, writing total and prefix residues as s,r gives GC4 after canceling the common `(1,1,1)` translations. Its four nontrivial cases are exactly the four tie indicators stated in the note, all in `{0,1}`. Consequently the sign holds for every finite pure cyclic grade. The increasing-physical-value direction has decreasing reciprocal weights; reversing that direction without also reversing the sign would be an error. [Global-carry note, GC3-GC5](global_carries.md), [direct-order certificate](global_carries_check.py).

The exceptions genuinely break the naive extension: the grade-48 effective word is `(0,0)` at initial `(11,12,12)`, giving forward-minus-reverse `13/186624`; the grade-88 word is `(1,2,2)` at `(37,36,36)`, giving `-13/45349632`. The checker independently confirms actual adjusted counts and that the displayed points are consecutive actual smooth values. The complete paired eta difference is `25199209663/249993707168205>0`; hence the fixed-weight scalar c-functional has a downward jump from minus to plus at 5/8. None of this refutes every possible corrected grouping. [Global-carry note, exceptional-grade table and GC12](global_carries.md), [exact comparisons](global_carries_check.py).

**6. PASS: full positive token process, rational marginals, and nonlinear rank sum.** Delaying the dyadic token e from e to `3e/2` removes exactly `I_j`. Delaying the row-one token `3*2^a`, `a>=2`, to `27*2^(a-3)` removes exactly the patch root `e=2^(a-1)>=2` on `[6e,27e/4)`. Its color is `a-1`, the root color. Therefore GC7 holds vectorwise, at every endpoint, with no invalid root 1 and no missing small patch. The only nonsmooth arrival is `27/2`; its before/after vectors have the same minimum. Simultaneous smooth arrivals have equal reciprocal weights, so their internal processing order does not change weighted total minimum increments. [Global-carry note, GC6-GC8](global_carries.md), [retiming certificate](global_carries_check.py).

The generating function follows by subtracting and adding the two geometric token families:

```
dyadic correction = omega*(y-x)/(1-omega*x),
row-one correction = omega*(x^-1*y^3-x^2*y)/(1-omega*x).
```

Thus GC9 is exact and its sole negative x exponent is the one token at `27/2`. At `(x,y)=(1/2,1/3)` the uncolored corrections are `-1/3` and `-1/54`, giving `143/54`. Filtering colors yields rational marginal reciprocal masses. If `t_j(k)` is the kth color-j arrival, then `min_j T_j(t)=sum_k 1_[max_j t_j(k)<=t]`. Summing its nonnegative atomic increments proves GC11 by monotone convergence. It leaves the **rank-coupled maximum**, which cannot be evaluated from the three separate marginal masses. [Global-carry note, GC9-GC11](global_carries.md).

**7. PASS: both-parity four-step transfer and genuine unipotent drift.** The accepted parity-sensitive word concatenation is essential. In even parity its successive root registers through the first three steps are `kQ+P`, `(k+1)Q+P`, and `(1-k r^2)Q-r^2 P`; the fourth is `-r^2 Q`. In odd parity they are `P+krQ`, `P+(k+1)rQ`, and `(r^2-k)Q-r^2 P`; the fourth is `-rQ`. In both cases the new preceding phase is `r^2`. Substituting a second block with digit l restores Q,r and gives respectively `P+(k+l+1)Q` and `P+(k+l+1)rQ`. This proves A1 for all positive k,l, rather than only the sampled digits. Multiplying the ordinary denominator-step matrices separately gives `[[3k+2,3],[2k+1,2]]`; it is not the root transfer. [Adaptive note, A1](adaptive_induction.md), [accepted concatenation](../reflected-return-models/cf_induction.md), [transfer certificate](adaptive_induction_check.py).

At golden indices `n=6+8j`, the exact seed is `(p,q,u,v)=(8,13,5,8)` and `(Q_res,Q_prev)=(1,-omega)`. Two k=1 blocks give the stated `[[34,21],[21,13]]` size matrix and `Q_prev=3j-omega`; residues and eigenvalue `phi^8` follow. These are one fixed comparison path's origin-anchored registers. [Adaptive note, A2](adaptive_induction.md).

**8. PASS: all-level golden states, denominator scope, and fully corrected defects.** The upper endpoint correction is `(omega-1)omega^2=2+omega`, so `Q_A(v)=3j+2` and `A_v=(j+1)(2+omega)`. The floor values at `v-2,v-1,v` are `u-2,u-1,u-1`, giving increments `1,-1,-omega^2` and hence `A_(v-1)=A_(v-3)=(2j+1)+j omega`. The preceding lower word satisfies `Q_(n-2)=1-omega(3j-omega)=-(3j+1)omega`, proving A4. In the resonant model, the `3q` shift is `(2,1)`; with `B_1=0` and `C_(2,1)=-omega`, A5 follows. Each low-row residue eventually enters the low-row cone. If L is the whole row's last zero, then `2-sum_(zero a)2^-a` has denominator exactly `2^L` because its last-zero numerator is odd. The selected residue gives only the lower bound `L>=q-v+3jq`. No argument here prevents cancellation after other rows are added. [Adaptive note, A3-A5](adaptive_induction.md), [exact checks](adaptive_induction_check.py).

For an explicit all-level floor justification, put `beta=phi`, `delta=q-p beta>0`, and `n=2q+v`. Fibonacci convergents give `v-u beta=-phi*delta`; thus `S beta=n-epsilon`, where `S=2p+u` and `epsilon=(2-phi)delta`. The positive epsilon decreases from its 8/13 value and is less than `phi-1`. The true floors at `S-2,S,S+1` are therefore `n-4,n-1,n+1`. For the upper-sided rational reciprocal model they are `n-4,n,n+1`; these also follow directly from `qu=pv+1` and `p>=8`. Hence the model patch has `E_M=omega`, while the true isolated correction has `E_T=1`. The accumulated B difference is `-omega`, so the **fully corrected state difference is -1**. [Adaptive note, A6-A8](adaptive_induction.md), [correction rules](adaptive_induction_check.py).

The vertical base is also anchored: Beatty complementation at `(v+1,u+1)` gives `Q_B(u+1)=-(3j+2+omega)` and hence `B_(u+1)=(1-j)+(j+1)omega`. The reciprocal resonant period root is `-1` (the sided rational Beatty blocks sum with `Q_A(q)=1` to zero); shifting by `2p` adds `omega-1` after retaining the harmonic term. This proves both B values in A6. Combining them with A3, the actual C residue and `a=v_h-1` or `v_h-3` proves the exact states in A8 for every j, including the `j=0,a=7,b=22` base. The direct three-level checks corroborate, rather than replace, this induction. [Adaptive note, A6-A8](adaptive_induction.md), [actual reciprocity](hybrid_compression.md), [exact golden certificate](adaptive_induction_check.py).

Since `q_j=Theta((phi^8)^j)` and `h=ceil(j/2)`, the witness has `a_j=Theta(sqrt(q_j))`, `b_j=S_j+1`, and absolute c-discrepancy weight exactly `3^-S_j*2^-a_j`. This rules out the proposed generic extra exponential **absolute-support** gain on this comparison pattern. It says nothing about a signed scalar error after coherent cancellation, actual target-logarithm trajectories, or firstness of the witnesses. [Adaptive note, A7-A9 and scope](adaptive_induction.md).

### Gaps

- Pure cyclic/balanced signs do not cover exceptional token words; rational marginals do not remove nonlinear rank coupling. [Global-carry gaps](global_carries.md).
- The golden example is a comparison cocycle. Its row denominator and absolute defect witness are not lower bounds for the complete target scalar denominator or signed approximation error. [Adaptive scope and gaps](adaptive_induction.md).

## Does the hierarchy supply an adequate actual infinite return and complete the objective?

### Takeaway

**PASS for the conditional 5/2 arithmetic budget and the actual multiscale real-residual identity; FAIL for completion of the arithmetic-return objective.** The final followup does construct an actual infinite sequence of exponentially small real residuals, a stronger conclusion than the first-round bookkeeping alone. Its complete boundary has not been put in a fixed rational lattice, and nonvanishing remains unproved. [Adaptive note, A10-A13](adaptive_induction.md), [final absorption followup](hierarchy_absorption.md).

### Cited Findings

- The accepted actual eligible supply gives original successor ratios greater than `C_*=(15+sqrt(5))/10`; the degree-two interior identity retains four infinite sides. [Supply proof](../infinite-return-construction/diophantine_supply.md), [retained-side identity W11](../infinite-return-construction/weighted_returns.md).
- The finalized absorption checker passed its operator composition, boundary kernel, twelve actual column-head denominator checks, the named unchanged-model repair, and the finite rank-coupling comparison. Its independent inputs for the last two arithmetic checks are the proved finite count formula and the saved audited 53/84 rational value. [Absorption certificate](hierarchy_absorption_check.py).

### Inferences

**9. PASS: thinning and the sum of little-o costs.** Retain eligible indices `n_j` with gaps at least four, and write `d_j=q_(n_j)`. The CF recurrence gives `d_(j+1)>=5d_j`, so `sum_(i<=j)d_i<=(5/4)d_j`. The matching window must still use the **original immediate successor** `q_(n_j+1)`, never the next retained denominator. [Adaptive note, A10](adaptive_induction.md), [supply note, nonconsecutive-window warning](../infinite-return-construction/diophantine_supply.md).

If `log F_i=2d_i log2+epsilon_i d_i` with `epsilon_i->0`, split the sum at a fixed I. The early error is constant; the rest has absolute value at most `sup_(i>=I)|epsilon_i|*(5/4)d_j`. Dividing by d_j and then taking I large proves `sum_i o(d_i)=o(d_j)`. Thus the **hypothesized** positive clearing integer in A11 has logarithm at most `(5/2+o(1))d_j log2`, after charging the fixed C and every extra `S_j` factor. This step does not require fixed term count. [Adaptive note, A11-A12](adaptive_induction.md).

A rational comparison represented by uniformly bounded coefficients and genuinely matching the last actual rectangle has error `exp(-(1+r_j+o(1))d_j log2)`, where `r_j=q_(n_j+1)/d_j>C_*`. Therefore its cleared error tends to zero with fixed margin `C_*-3/2=sqrt(5)/10>0`. If `Z=A/B`, the errors lie in `B^-1 Z` because `D_j L_j` is integral, and eventually vanish. A separate theorem must show nonvanishing for these **same** comparisons. This is elementary rational discreteness, not a growing-dimension Subspace Theorem application. [Adaptive note, A13](adaptive_induction.md), [accepted arithmetic criterion](../reflected-return-models/final_reflected_audit.md).

**10. PASS: the finalized exact multiscale real hierarchy.** For any bounded d and positive shift `(A,B)`, reindexing the absolutely convergent series removes the union `a<A OR b<B`. This gives HA1-HA3, with corner subtraction once and exact kernel

```
K_P(a,b)=2^-a 3^-b sum_(A,B: a<A OR b<B)c_AB 2^A3^B.
```

The corner term is integral after multiplying by `2^A3^B`; the semi-infinite sides remain real unknowns. Applying the identity first to d and then to `L_1 d` gives `F_2F_1W(d)=F_2B_1(d)+B_2(L_1d)+W(L_2L_1d)`, including the essential current-array argument `L_1d`. Products of the commuting positive shifts prove HA5 at every depth. [Absorption note, HA1-HA5](hierarchy_absorption.md), [independent finite-array checks](hierarchy_absorption_check.py).

For the actual high array `d(a,b)=c(a,b+4)`, the newest annihilator vanishes in its proved actual/model rectangle. The earlier product can shift by at most `2Q_-,2P_-`. Thus the retained zero rectangle really is

```
A_m=q_next-q_m-2Q_-,
B_m=p_next-p_m-4-2P_-.
```

Since `|L_m d|<=6` and the older coefficient sum is `3^(m-1)`, its remaining exterior has bound `18*3^(m-1)(2^-A_m+3^-B_m-2^-A_m*3^-B_m)`. The same thinned actual supply gives `Q_-<=q_m/4`, `m=O(log q_m)`, and `P_-=alpha Q_-+O(1)`: indeed the sum of retained convergent errors `p_i-alpha q_i` is absolutely bounded. Hence `A_m>=(r_m-3/2)q_m` and `B_m log3=A_m log2+O(1)`. The factors from both older shifts and coefficient growth have been paid, proving the **actual infinite-sequence real bound** `|W(P_m d)|<=exp(-(C_*-3/2+o(1))q_m log2)`. This is no longer only a conditional decay estimate. [Absorption note, HA6-HA9](hierarchy_absorption.md), [accepted latest-annihilator rectangle](../infinite-return-construction/weighted_returns.md).

The low rows cannot be dropped: `W(d)=81(Z-L_0)` gives exactly

```
81 Pi_m Z=N_m^*+W(P_m d),
N_m^*=81 Pi_m L_0+B_(P_m)(d).
```

HA10 includes all four low rows and every remaining side. No theorem makes `N_m^*` integral or places it in a fixed rational lattice. Calling it rational from this identity under `Z in Q` would still require rationality of the residual and would not establish a uniform denominator. Thus HA8 is a genuine real smallness theorem, but not yet an adequate **arithmetic** return. [Absorption note, HA10 and gaps](hierarchy_absorption.md).

**11. PASS: narrowly scoped side and head obstructions.** The unique all-horizontal monomial of `P_m` has `(A,B)=(A_max,0)` and coefficient one; all other monomials have smaller A. At `a=A_max-1,b>=B_max`, only that monomial enters the boundary kernel, giving `K=2*3^-b`. This nonzero formal infinite-column functional proves that multiplication of these positive operators alone does not formally absorb all sides. It does not exclude special relations among the actual column profiles. [Absorption note, HA11](hierarchy_absorption.md).

At `a=0`, write `K(0,b)=3^-b M_b`. For every b, the same unique B=0 monomial contributes `2^A_max`, while every other included monomial is divisible by three. Thus `M_b` is a 3-adic unit. Each actual d is also a unit modulo three, since `1` and `-2` both equal one modulo three. The last term of the head through `b=T-1` has strictly smallest 3-adic valuation, proving reduced denominator **exactly `3^(T-1)`** for every `T>=1`. This is a separate-column head result; it gives no reduced-denominator bound for the combined infinite boundary or scalar Z. Its elementary tail upper bound loses the decay after separately multiplying by `3^(T-1)`; that is a limitation of this repair estimate, not a lower bound on every signed tail. [Absorption note, individual-column argument](hierarchy_absorption.md), [actual twelve-digit check](hierarchy_absorption_check.py).

The specified unchanged-model repair `27 F_(5,8)F_(53,84)` has 192 bits, while the saved 53/84 model's reduced denominator has 507 bits; exact multiplication remains nonintegral. This defeats that particular two-factor repair of that unchanged value. It neither proves a denominator theorem for all new comparisons nor assumes a nonexistent four-index spacing of that named pair. [Absorption note, concrete repair and scope](hierarchy_absorption.md), [exact bit and rational checks](hierarchy_absorption_check.py).

**12. PASS: comonotone matching, without rational closure.** For the decreasing reciprocal arrival lists, the layer-cake count of triples with every coordinate at least s is at most the smallest of the three marginal superlevel counts. Equal-rank matching attains the minimum at every threshold, because every superlevel set is an initial rank interval. Tonelli therefore proves that rank matching maximizes the total reciprocal minimum, also for the infinite summable token lists. A strict lower coupling needs a strict deficit on an interval of thresholds; nonunique optimal matchings are possible. No failure of a canonical diagonal template can rule out all optimal couplings from this lemma. [Absorption note, matching lemma](hierarchy_absorption.md), [positive token inputs](global_carries.md).

The two finite abstract color-0 lists `(2,12)` and `(3,4)` have the same reciprocal mass `7/12`, with the other two lists both `(6,9)`, but the rank costs are `1/4` and `5/18`. This proves that the three rational marginal masses alone do not determine the rank-coupled value. It is explicitly an abstract positive-process example, not a counterexample to the prescribed actual token coloring. No cheap actual rational coupling is constructed. [Absorption note, finite marginal example and gaps](hierarchy_absorption.md), [exact finite rational check](hierarchy_absorption_check.py).

### Gaps

- **FAIL for completion:** no rational/fixed-lattice boundary theorem for `N_m^*`, adequate integer-cleared comparison family, or nonvanishing/nonstabilization theorem on that family is established. The ordinary scalar route still lacks the stronger adequate actual supply. The hybrid and real hierarchy results do not fill those arithmetic gaps. [Final absorption gaps](hierarchy_absorption.md), [previous accepted scalar criterion](../reflected-return-models/final_reflected_audit.md).
- Both required focused followups are finalized and checked. The named counterexamples refute their stated templates only; none is a general impossibility theorem for actual-specific signed identities, selected infinite subsequences, or nonlinear hierarchies. No additional exploratory research round is warranted by this audit. [Bracketing scope](hybrid_bracketing.md), [absorption scope](hierarchy_absorption.md).
- No broad scans, external research or posting, installations, Lean work, archived-file edits, or additional exploratory model family were performed. Only this new audit file was written by this auditor; the single requested checker assertion was applied by its author. [Audited file scope](hybrid_compression_check.py).
