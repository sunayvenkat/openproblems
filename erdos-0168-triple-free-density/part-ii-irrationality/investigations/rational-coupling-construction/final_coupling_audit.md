# Final independent audit of rational couplings and signed boundary certificates

**Local mathematical verdict: PASS, with the scope qualifications below. Overall completion verdict: OPEN.** The finalized notes construct genuine rational comparisons with strict actual one-sided errors and prove barriers for explicitly defined polynomial/window architectures. They do not construct an adequate infinite arithmetic return, prove nonvanishing of the old signed `R_m`, absorb the full target's low rows, or prove irrationality. The new phase and signed followups do not close those gaps. — [Strictness](coupling_strictness.md), [rational templates](rational_templates.md), [phases](coupling_phases.md), [signed boundaries](signed_boundaries.md), [window certificates](window_certificates.md).

The audit accepts the previously proved finite minimum, full positive-token retiming and layer-cake optimum as background. It reconstructs the new arguments from those inputs. All five supplied checkers and the new independent narrow checker ran successfully with `python -B`. The phase/window checkers explicitly reuse their first-round dependencies; these are not five independent implementations. The new checker imports none of them. — [Accepted token representation](../hybrid-arithmetic-closure/global_carries.md), [accepted matching theorem](../hybrid-arithmetic-closure/hierarchy_absorption.md), [independent checker](final_coupling_audit_check.py).

## Does actual color balance prove strictness and the sharp canonical repair error?

### Takeaway

Yes. The uniform moving-phase rotation argument gives actual color imbalance `o(T)`, and the integrated partial-token identity converts a positive quadratic supply of dispersed triples into a strictly positive cost gap. For the canonical finite-head repairs, the stated `Theta(log X/X)` estimate and both constants reconstruct correctly. — [Proof CS1-CS19](coupling_strictness.md).

### Cited Findings

- The actual arrival map is `2^a3^b`, except `b=0,a>=1` has multiplier `3/2`, and `b=1,a>=2` has multiplier `9/8`. Original colors `(a-b) mod3` remain attached to tokens. The exceptional arrival `12 ->27/2` has zero minimum jump. These facts are retained in both the proof and independent checker. — [Accepted GC6-GC11](../hybrid-arithmetic-closure/global_carries.md), [independent time2/records routines](final_coupling_audit_check.py).
- With `lambda=log2`, `mu=log3`, logarithmic cutoff `T`, total arrived-token count `N(T)`, and actual minimum `tau(e^T)`, the claimed discrepancy is `E(T)=N(T)-3tau(e^T)=o(T)`, with `E>=0`. It is a statement about the actual corrected counts. — [CS1-CS3](coupling_strictness.md).
- For any genuine three-color coupling, the partial-token count and deficit satisfy `U=N-3G` and `D=tau-G=(U-E)/3>=0`. For a triple with logarithmic arrivals `h_j>=0` and `h_*=max h_j`, its exact integrated contribution is `sum_j(min(T,h_*)-h_j)_+`, equaling `g=3h_*-sum h_j` when complete. — [CS4-CS6](coupling_strictness.md), [finite exact certificate](coupling_strictness_check.py).
- A dispersed subfamily with `g>=epsilon>0` and at least `kappa*T^2` complete triples gives `integral_0^T D(s)ds >=(epsilon*kappa/3+o(1))*T^2`. Consequently deficits occur on intervals arbitrarily far out, and `M-Q=integral_0^infinity D(T)e^-T dT>0`. Thus a rational coupling cost yields `Zhat=3-3Q>Z`. — [CS7-CS10](coupling_strictness.md).
- Fixed-offset families on a full-index lattice coset in a deep quadrant, or inside a positive-area interior cone, meet the criterion if they really are disjoint triples of the coupling. A fixed bounded coordinate diameter also supplies a positive dispersion lower bound and quadratically many completed triples. — [CS11-CS14 and bounded-displacement corollary](coupling_strictness.md).

### Inferences

The rotation proof handles its essential uniformity correctly. A continued-fraction denominator `q` divides any long orbit into `q`-blocks. Displacement from the rational grid is below `1/q`; only a fixed number of grid points near interval endpoints can change membership. Thus the error is bounded by `10/q+2q/n`, uniformly in starting phase. Taking `n` to infinity before taking `q` large proves the needed qualitative result. In the root-of-unity row sum, writing `b=3k+r` produces the zero-mean step function `g(u)=omega^floor(3u)`, with rotation step `-mu/lambda`. The initial phase moves with `T`, so this uniform statement is exactly what is needed. Forward retiming alters the raw counts by only a bounded amount. — [CS1-CS3](coupling_strictness.md).

The dispersion proof correctly uses nonnegativity. For a partially arrived triple, its arrived tokens contribute one or two to `U`; other triples cannot subtract that mass. Also `integral_0^T E=o(T^2)` follows by bounding `E(s)<=delta*s` beyond a fixed threshold. Local finiteness then changes a positive integral into an actual interval with positive integer deficit. The cost identity follows by Tonelli from `1/t=integral_(log t)^infinity e^-s ds`; finite marginal reciprocal masses ensure finite costs. — [CS4-CS9](coupling_strictness.md).

The sharper lattice strip statement has the necessary `o(T)` error. If the lattice has index `d`, it contains `dZ^2` and is the union of `d` rectangular-grid cosets. Uniform rotation averaging on each such coset yields a strip count `hT/(d lambda mu)+o(T)`. An `O(T)` triangle-area error alone would not suffice here. For bounded displacement, the possible nontrivial ratios `2^r3^s`, `|r|,|s|<=L`, have logarithmic span at least `log(1+6^-L)>0`; this supplies the claimed parameter-dependent dispersion constant. — [CS13-CS14 and bounded-displacement proof](coupling_strictness.md).

For the canonical row coupling, each ordinary row's partial count is the residue of its token count modulo three, with average one. The two retimed low rows contribute only `O(1)`. Therefore `D_0(T)=T/(3mu)+o(T)`. For the repair at physical cutoff `X`, set `K=min_j T_j(X)`, take the first `K` actual tokens of each color, and rematch the finite union of all whole canonical triples meeting that head. Every touched original label differs horizontally from a head label by at most two; the forward actual multiplier is at most `3/2`. Thus every touched arrival is at most `6X`, including the low exceptions. The repaired deficit is zero up to `X`, at most `D_0` everywhere, and exactly `D_0` after `6X`. Integrating gives precisely

```
(1-o(1))*(log(6X)+1)/(18*mu*X)
  <= M-Q_X <= (1+o(1))*(log X+1)/(3*mu*X).
```

This proves the sharp real order and strictness for every finite repair, while the transformed `Zhat_X` error is three times as large. The supporting finite certificate also independently gives the canonical gap `M-61/189>=5/1296` from deficit two on `[81,96)`. — [CS15-CS19](coupling_strictness.md), [supporting finite certificate](coupling_strictness_check.py).

### Gaps

- No effective discrepancy threshold uniform in a coupling parameter is proved; none is needed for per-member strictness. A family parameter may change both `epsilon` and `kappa`. The theorem requires the stated actual coupling/dispersed-subfamily hypotheses. — [Strictness scope](coupling_strictness.md).
- The sharp canonical real error and an upper clearing bound do not give a lower bound on its reduced denominator or exclude every selected arithmetic subsequence. They also say nothing about nonvanishing of an older signed residual without an identity identifying that residual with a genuine positive coupling gap. — [CS19 and final gaps](coupling_strictness.md).

## Are the rational templates, phases and their complete denominator costs valid?

### Takeaway

Yes. Both original constructions are exhaustive bijective couplings, the finite head correction is exactly `1/27`, and the complete skew cost clears by `27*3^(2p)*(2^(3q)-1)`. The phase and fold formulas retain every endpoint repair. Their period removal has the stated dyadic price; the fold worsens the approximation. — [RT1-RT11](rational_templates.md), [CP1-CP15](coupling_phases.md).

### Cited Findings

- The canonical triples `(3n,b),(3n+1,b),(3n+2,b)` have actual maxima `6*8^n`, `(27/2)*8^n`, and `4*8^n*3^b` in rows zero, one and `b>=2`. Their complete sum is `4/21+16/189+1/21=61/189`. Every original token is used once, with one of each color per triple. — [RT1](rational_templates.md), [exact checker](rational_templates_check.py).
- The balanced finite repair has `Q_K=61/189-Q_row(U)+M(U)`. Nested heads give nested unions of whole row triples. The old finite matching plus added untouched row triples is a candidate on the larger union, proving monotonicity; inclusion of the first `K` true optimal ranks proves convergence to `M`. — [RT2](rational_templates.md).
- With integer `X>=1`, `A=floor(log_2 X)`, `B=floor(log_3 X)`, all repaired actual arrivals have dyadic exponent at most `A+2` and ternary exponent at most `max(B,3)`. Hence `D_X=7*2^(A+2)*3^max(B,3)` clears `Q_X`; the negative dyadic exponent at `27/2` produces a numerator. For `X>=27`, `D_X<=28X^2`. The displayed tail bound is `(3/2)(A+3)/X`. — [RT3-RT4](rational_templates.md).
- For `p>=2,q>=3,p+q!=0 mod3`, bulk triples at `(r+3qn,b+2p),(r+q+3qn,b+p),(r+2q+3qn,b)` leave exactly one translated finite L-block per horizontal block. That L-block has `3pq` tokens and `pq` of each color. — [RT5-RT6](rational_templates.md), [direct ownership checker](final_coupling_audit_check.py).
- Writing `u=2^q`, `v=3^p`, `O=O_inf`, `delta=1/27`, and `S=1/M0+1/(3M1)+1/(6M2)`, the full skew cost is `Q0=delta+u^3 O/(u^3-1)+2u^2 S/(u^2+u+1)`. Its stated complete clearance is `27v^2(u^3-1)` and has nominal actual-convergent exponent five. — [RT7-RT10](rational_templates.md), [independent direct bulk sum](final_coupling_audit_check.py).

The exact prescribed values and first deficits were independently reproduced from direct token ownership and complete event counts, rather than the supplied maximum-enumeration helper. — [Supplied certificate](rational_templates_check.py), [independent certificate](final_coupling_audit_check.py).

|Slope|Complete rational cost|First actual deficit|`tau,G`|
|---|---|---|---|
|`5/8`|`7302767222/12230589735`|`59049=3^10`|`31,30`|
|`12/19`|`72910517586918632358010200787/122107157304408335741677589853`|`293534171136=2^27*3^7`|`163,162`|

### Inferences

The partition can be inverted without any infinite remainder. Write `a=3qn+iq+r`, with `i=0,1,2`, `0<=r<q`. A token is in the L-block exactly when `i<2` and `b<(2-i)p`; otherwise its bulk base row is `b-(2-i)p`. This gives unique ownership. The color increment along each bulk triple is `p+q mod3`, so nonresonance gives all colors. For the L-block, the character is `A_q B_p(1+omega^-p+omega^q)`: either a geometric sum vanishes, or nonresonance forces the last factor to vanish. Hence its exact color multiplicities really are `pq`. — [RT5-RT6](rational_templates.md), [independent inverse ownership](final_coupling_audit_check.py).

The head correction checks every changed rank. Only `(0,0),(0,1),(1,1)` change between actual and asymptotic retiming. The first two color lists are respectively `(1,6)` versus `(3/2,27/4)`, `(3,9)` unchanged, and `(3,6)` versus `(27/8,6)`. Thus the first maximum changes from `3` to `27/8`, the second remains `9`, and all later ranks agree. All necessary labels belong to L under the stated lower bounds. Therefore `O_0-O=1/3-8/27=1/27`, with no discarded early term. Reciprocals in `O` clear by `2^(2q-1)*3^(2p-1)`; multiplication by `u^3` removes that dyadic part. The complete bulk resummation cancels `u-1` only after summing all `r<q`; each selected maximum's dyadic part is canceled or cleared as stated. These facts prove the full denominator, including the unchanged infinite bulk. — [RT7-RT10](rational_templates.md).

The first outside-L arrival is `min(v^2,uv,(3/2)u^2)`. Before it, the actual finite L optimum attains the global minimum count. This gives an agreement scale `2^((2+o(1))q)` and an upper tail bound of order `q*2^(-(2+o(1))q)` along actual convergents. The two first deficits above are finite all-event theorems, not an all-level first-defect result or a transferred Farey window. A fixed ordinary bulk coset has dispersion `3*|log u-log v|>0`, proving strictness separately for every member. — [RT11 and its scope](rational_templates.md), [actual strictness criterion](coupling_strictness.md).

For the two completed rightshift phases, vertical triples in every column have maximum `9*27^m*2^a`, so the whole vertical cost is `V=3/13`. A strip of width `h` costs `V(1-2^-h)`. The translated right part has exact asymptotic retiming because `a>=q>=3`. Therefore `Q_r=V+(Qinf-V)/u^r`, `r=1,2`, while `Q0=Qinf+delta`. Their equal average is

```
Qbar=V*(1-(u^2+u+1)/(3u^2)) + u*O/(3*(u-1)) +(2/3)*S+1/81,
D_bar=1053*u^2*v^2*(u-1).
```

The average has deficit `2/3` on the entire actual interval `[3,9)`, giving `M-Qbar>=4/27`. Thus the unmodified equal average cannot converge to `M`. The fixed six-token vertical head has cost `1/6` before and `7/18` after optimal rematching; a mixture of weight `1/6` therefore adds exactly `delta`, as charged in CP10. — [CP1-CP5 and CP10](coupling_phases.md), [phase checks](coupling_phases_check.py).

The deterministic one-block fold is a genuine coupling because the first `3q` columns and remaining vertical columns are disjoint exhaustive regions. Its exact value and comparison sign are

```
Q_fold=O+delta+2*(u-1)*S/u+V/u^3,
Q_fold-Q0=u^-3*(V-Qinf)<0,
D_fold=351*u^3*v^2.
```

The strict sign uses `Qinf>=8/27>3/13`. Its extra positive error is `u^-3*(Qinf-V)=O(u^-3)`; it preserves the earlier upper bound, not an unproved generic sharp skew-error order. The folded and original couplings have the same completed counts below `(3/2)u^3`, so both prescribed first-deficit events persist. The convex identity with `epsilon=1/[u^2(u-1)]` reproduces the same value; no second denominator cost is imposed after the deterministic realization has already established its actual clearance. — [CP6-CP10](coupling_phases.md), [independent arithmetic](final_coupling_audit_check.py).

The exact dyadic statements have the correct eventual scope: `q>=4` and `v^2<=(9/8)u^2`, which hold eventually along actual convergents. In this regime `M0=(3/2)u^2`, `M1=(9/8)u^2`, and `M2=max(u^2,v^2)`. The finite-block estimate `v_2(O)>=1-2q` makes the displayed `u^-2` or `u^-3` term uniquely least in valuation. Thus

|Actual side|`v_2(Qbar)`|`v_2(Q_fold)`|
|---|---|---|
|`u>v`|`3-2q`|`3-3q`|
|`u<v`|`-2q`|`-3q`|

These are reduced dyadic-denominator theorems, not merely clearing upper bounds. They charge the smooth factor that replaces the removed odd period; they do not determine all odd reduced factors. — [CP11-CP15](coupling_phases.md), [phase checker](coupling_phases_check.py), [independent valuations](final_coupling_audit_check.py).

### Gaps

- The canonical repair's clearing estimate and the original/phase/fold nominal exponents are not universal reduced-denominator lower bounds. Neither the two observed early defects nor an inadequate upper error estimate proves that all selected families fail. — [RT scope](rational_templates.md), [CP scope](coupling_phases.md).
- Convex combinations of one-sided coupling errors cannot cancel those positive errors. Different actual matchings or head repairs can change the errors and require new coverage, window and arithmetic proofs. No such adequate family is established here. — [Coupling inequality](coupling_strictness.md), [phase gaps](coupling_phases.md).

## Do the signed finite-boundary, valuation, Laurent and window claims survive full arithmetic accounting?

### Takeaway

Yes. The finite-boundary characterization, integer corner, two-adjacent prime divisor, balanced Laurent identities and strengthened window barrier reconstruct correctly. The fixed Laurent operator and explicit ordinary beyond-window repair have rigorously nonzero actual residuals, with their complete tails retained. Those results concern the defined architectures and examples. — [SB1-SB8](signed_boundaries.md), [WC1-WC7](window_certificates.md).

### Cited Findings

- For an ordinary finite signed polynomial `P`, formal finite support of its weighted boundary kernel is equivalent to `P(X,3)=P(2,Y)=lambda=P(2,3)`, or `P=lambda+(X-2)(Y-3)Q` with integer `Q` for integer `P`. Its exact boundary is `B_P(d)=-6(Qd)(0,0)`, an integer for integer `d`. — [SB1-SB3](signed_boundaries.md), [exact signed checker](signed_boundaries_check.py).
- A multiple of a single nonconstant annihilator `L_(p,q)=X^(2q)+X^qY^p+Y^(2p)` cannot have a nonzero constant restriction at `Y=3`. This allows arbitrary signed polynomial multipliers; it does not assume positive coefficients. — [Common-factor theorem](signed_boundaries.md).
- If `p/q<r/s`, `qr-ps=1`, `q>=3,r>=3`, and an ordinary integer combination of the two annihilators has formally finite boundary, then `2^(2 max(q,s))*3^(2 max(p,r))` divides its target coefficient `lambda`. A rational-coefficient representation must charge an actual common coefficient denominator before applying this theorem. — [SB4-SB5](signed_boundaries.md).
- The Laurent operator `P0=-X^3Y^3+27X^3+8Y^3-34` has target coefficient `182`, finite boundary `216*sum_(a,b<3)d(a,b)2^-a3^-b`, and actual corner `-552`. Its full actual residual satisfies `139875/1024<W(P0d)<139876/1024`. — [SB6-SB8](signed_boundaries.md), [independent actual-token enclosure](final_coupling_audit_check.py).
- The window followup proves its theorem for arbitrary finite depth and rational signed coefficients, using the original immediate successor `q_i^+`, not the next retained scale. It also supplies one complete ordinary integer finite-boundary construction beyond those windows. — [WC1-WC7](window_certificates.md), [followup checker](window_certificates_check.py).

### Inferences

For the finite-boundary necessity, take `b` beyond the maximum Y exponent. The kernel becomes `2^-a3^-b * sum_(A>a)2^A sum_B c_AB3^B`. Finite support forces every such tail sum to vanish; successive differences give the constant X restriction. The other restriction follows symmetrically. Monic division over the integers gives the product factorization. Direct reindexing yields `W((S_a-2)(S_b-3)e)=6e(0,0)`, and the identity `lambda W(d)=B_P(d)+W(Pd)` gives the minus sign in `B_P=-6(Qd)(0,0)`. This also shows why independently dropping corner terms would be wrong. — [SB1-SB3](signed_boundaries.md).

The two prime bounds retain both algebraic roots and the integral ceilings. At a 3-adic root of the lower annihilator, `v_3(x)=p/q`; the upper annihilator has unique least term of valuation `2sp/q=2r-2/q`, whose ceiling is `2r` for `q>=3`. At a root of the upper annihilator, the lower one's unique minimum is `2p`. Hence `v_3(lambda)>=2 max(p,r)`. For 2-adic roots of the corresponding Y polynomials, the unique minima are `2s` and `2ps/r=2q-2/r`; the latter ceiling is `2q` for `r>=3`. Thus `v_2(lambda)>=2 max(q,s)`. Integer polynomial coefficients evaluated at these positive-valuation roots have nonnegative valuation, so no multiplier was assumed to be a unit. For actual late adjacent convergents the resulting nonzero target cost is at least `(4+o(1))*Q*log2`, with `Q=max(q,s)`. This is a lower bound within the universally coefficient-cleared finite-boundary two-generator architecture. — [SB4-SB5 and proof](signed_boundaries.md).

The Laurent identities are exact coefficient identities. For `U=X^qY^-p`, `V=X^sY^-r`, determinant one gives `X=U^r V^-p`, `Y=U^s V^-q`. Balanced words of `U^3` and `V^-3` produce `X^3-1` and `Y^3-1`; combining them gives `P0`. Their coordinate support widths are `O(q+s)` horizontally and `O(p+r)` vertically. The general monomial count is `O(p+r+q+s)`, specializing to `O(q+s)` for the bounded actual slopes. Both wording corrections are present in the finalized note. — [Balanced Laurent construction](signed_boundaries.md).

Negative extension and smooth arithmetic are not free. In the three named certificates the required shifts are `X^78`, `X^249`, `X^1704`, with the listed complete support ranges. Evaluating Laurent monomials at `(2,3)` can introduce the corresponding dyadic denominators even when their real size is modest. A bounded extension across negative indices also adds the missing infinite boundary profiles when the weighted sums are reindexed. Clearing the first orientation by `X^M` yields `X^M P0`, whose Y=3 restriction is `182X^M`; it therefore has infinite vertical sides. Its evaluation need not satisfy the finite-boundary divisor theorem, which resolves the apparent bit-count comparison in the second example. An actual vanishing relation cannot be inferred from the toric quotient: the complete positive interval for `W(P0d)` already disproves that promotion for this operator. — [SB6-SB8 and support table](signed_boundaries.md).

The full-tail enclosure of `P0` is correct independently of the digit implementation. For `a<A,b<B`, the omitted reciprocal region has weight `3v`, where `v=2^-A+3^-B-2^-A3^-B`. Since `d` lies in `{-2,1}`, its contribution lies between `-6v` and `3v`. With `A=28,B=20`, multiply by `182` and subtract the exact corner `-552`. The independent checker obtains the same interval from the retimed positive-token minimum instead of the supplied raw-correction counter. — [SB8](signed_boundaries.md), [independent minimum tables and enclosure](final_coupling_audit_check.py).

For the many-scale window test, let `w_i=q_i^+-q_i`, `g_i=A_i(X,3)`, and choose the largest active retained index `k`. The newest contribution is monic at degree `deg g_k+2q_k>=2q_k`. If every `deg g_i<2w_i`, each older contribution has degree `<2q_i^+<=2q_k`, so cancellation is impossible. This proves the stronger algebraic range while the actual zero window remains only `a<w_i`. The raw weak endpoint `deg_X A_i<=w_i` still lies within the excluded range. At the weak doubled endpoint `deg g_i<=2w_i`, cancellation requires `deg g_k=0`, an active immediate original predecessor `j`, and `deg g_j=2w_j`; these are necessary, not sufficient. No adjacent active indices means the barrier still applies at that endpoint. — [WC1-WC2 and endpoint qualifications](window_certificates.md).

Without a degree assumption, a nonzero constant restriction still forces some older contribution to reach the newest leading coefficient. Therefore

```
deg g_j >= deg g_k+2*(q_k-q_j)
        = deg g_k+2*w_j+2*(q_k-q_j^+).
```

That actual older multiplier has horizontal support outside its known origin window. The existing individual support argument cannot supply a positive surviving origin width for that term. This is a failure of that particular proof route, not a lower bound on every signed actual residual. — [WC3-WC4](window_certificates.md).

Finally the explicit beyond-window ordinary example is arithmetically complete. The two opposite Laurent orientations give shifts `M=78,N=48`. Put `T=X^M Y^N-3^N X^M-2^M Y^N`; then `P=P0*T` is represented by ordinary integer multiples of the two annihilators, both axis restrictions are `lambda=-182*2^78*3^48`, and the boundary is a finite integer head. The effective X degrees are `62,40`, with `62=40+2*(19-8)`, while the original windows are `11,46`. The 162-bit target factor is retained. The full actual certificate is

```
-699753*2^64 < W(Pd) < -699752*2^64.
```

Its tail estimate uses `|Pd|<=2*sum|p_AB|`, hence total omitted magnitude at most `6v*sum|p_AB|`. The independent checker constructs this explicit `P0*T`, computes every shifted digit from delayed-token arrivals, and reproduces the enclosure with its entire tail. This is a valid finite-boundary identity with a large actual residual, not an adequate return. — [WC5-WC7](window_certificates.md), [supplied exact certificate](window_certificates_check.py), [independent certificate](final_coupling_audit_check.py).

### Gaps

- Formal finite support is a universal kernel property; a nonfinite kernel could still have a rational or canceling value on the actual array. The single-factor, adjacent-factor, and window barriers do not cover all actual-specific relations, all many-generator ideals, negative extensions with new estimates, or nonlinear matching constructions. — [Signed scope](signed_boundaries.md), [window scope](window_certificates.md).
- A finite integer boundary for the high array alone does not evaluate the full target. The accepted identity still contains `81*lambda*L_0`, accounting for all four low rows. The old hierarchy's actual residual nonvanishing and full numerator lattice remain unproved. — [Full target HA10](../hybrid-arithmetic-closure/hierarchy_absorption.md).
- **Final completion verdict remains OPEN:** no adequately small, nonzero infinite integer-cleared error family for the actual full target has been proved. The exact positive coupling comparisons and the new architecture-specific barriers are valid progress, not completion. — [Current arithmetic frontier](../hybrid-arithmetic-closure/REPORT.md), [all finalized results and scopes above](rational_templates.md).
- Skipped: Lean, external validation, installations, broad scans, archived-file edits and external posts. Material risk: promoting one of these scoped comparisons or barriers to a universal no-go, or dropping a coefficient, negative-extension, minimum-unit, boundary, or low-row arithmetic cost.
