# Record prefixes, actual early ties, and the product-tail interface

**Final-round status: the adequate infinite weighted-return theorem remains unproved.** There is now an all-level proof of the previously observed *hit* formula on a genuine comparison-slope cocycle. More strongly, its translates are realized by that same comparison cocycle's reciprocal-axis rows, giving coupled tie contexts with its prescribed correction E included. This rigorously defeats a universal large-recenter/late-support inference. It is not a theorem about the target logarithmic slope or finite D_t optimality. A universal mixed-hybrid identity also produces a product-of-two-tail error at the real level, but its two hybrid weighted sums have no established arithmetic compression. [Previous exact induction](cf_induction.md), [previous arithmetic audit](../infinite-return-construction/final_return_audit.md).

The only new executable is [record_returns_check.py](record_returns_check.py), run with Python `-B`. Its narrow checks cover the all-level induced prefix formulas, exact lower/upper floor brackets, three direct reciprocal-axis contexts, and one actual-logarithm mixed-corner rectangle. No old folder was edited and no density decimal was computed.

## What universal record and weighted-prefix transfer is actually available?

### Takeaway

First-hit positions and their weighted integer numerators induce exactly at the actual incoming state. A finite modular endpoint controller does not determine these quantities: physical word lengths enter every numerator shift, and a ray with early support has an exponentially large numerator in the natural period representation. This is a precise arithmetic accounting identity, not an adequate return by itself.

### Cited Findings

- The parity-sensitive lower Christoffel recurrence, the actual-axis endpoint formula, the invariant adjacent center distance and the nonresonant triple endpoint identity are proved in the first-round [CF note](cf_induction.md). Its [certificate](cf_induction_check.py) independently checks direct floor words and weighted concatenation.
- The paired-order response is a weighted local time of a genuine minimum Hessian, including the same-color term. The old degree-two interior relation retains four infinite sides. [Weighted-response proof](../infinite-return-construction/weighted_returns.md), [final audit](../infinite-return-construction/final_return_audit.md).
- A nonresonant rational model's actual scalar denominator can retain the full degree-six cost: the prescribed 53/84 model has reduced denominator exactly `27(2^(3q)-1)(3^(3p)-1)/6`. [Exact denominator obstruction](../infinite-return-construction/skew_denominator.md).

### Inferences

Use the extended axis state `s=(A,a mod3,floor(a alpha) mod3)` from the first round. Let `F_W(s)` be its endpoint after a finite word W. For a zero/one cone or tie-ray readout h, define

```
e_W(s)=min {1<=k<=|W|: h(F_(W[1:k])(s))=1},
        with min(empty)=infinity,
N_W(s)=sum_(k=1)^|W| 2^(|W|-k) h(F_(W[1:k])(s)).
```

Splitting an actual concatenated orbit segment at its boundary gives the universal exact transfers

```
F_UV=F_V composed with F_U,
e_UV(s)=min(e_U(s), |U|+e_V(F_U(s))),
N_UV(s)=2^|V| N_U(s)+N_V(F_U(s)).                 (R1)
```

The readout inside the right term is evaluated after the actual U prefix. Keeping the same initial state on both terms is incorrect. For a finite first hit `e=e_W(s)`, positivity gives the useful bit bounds

```
2^(|W|-e)<=N_W(s)<=2^(|W|-e+1)-1.                (R2)
```

Equivalently, the weighted finite profile lies between `2^(-e)` and `2^(1-e)`. The vertical version replaces 2 by 3, with the corresponding ternary geometric bound. For signed Hessian combinations one can use (R1) directly; the positive lower bound (R2) applies only to a positive readout and must not be used to rule out signed cancellation.

On a no-resonance tail, the first-round center-distance argument controls the spatial support by O(n^2) lattice states through CF depth n. One can therefore memoize (R1) on the exact induced word DAG and the actual states reached by its prefixes. This is a legitimate growing-register method. However, its integer numerators can have `|W|-e+1` bits. Small spatial support does not make their height subexponential in physical word length.

If a nonresonant block W of length q is repeated forever, its endpoint map satisfies `F_W^3=identity`. The readout has period P=3q. Starting at prefix index 1, its infinite weighted value is exactly

```
sum_(k>=1) h(F_(W^infinity[1:k])(s))/2^k
   = N_(W^3)(s)/(2^(3q)-1).                      (R3)
```

Thus order-three endpoint closure retains the cubic period denominator and a weighted numerator. The numerator may reduce with that denominator, but no reduction follows merely from the endpoint map. A fixed word does not acquire unipotent drift on repetition; the drift exhibited below comes from changing CF words. A `q times register` preperiod cost must therefore be proved for a particular architecture, rather than inferred from that drift.

### Gaps

- Formula (R1) is an exact record algorithm, not a lower bound placing the first hit after the arithmetic clearing scale.
- A reduced scalar denominator can cancel; (R2) measures the natural binary numerator and does not assert a universal reduced-height lower bound.
- There is no established fixed-dimensional arithmetic closure of these profiles, no adequate infinite sequence, and no nonvanishing argument for an arithmetic return.

## Can record-sized recentering force the relevant actual tie rays exponentially late?

### Takeaway

No such general support claim holds. On the explicit no-resonance comparison slope below, a recenter of size L at current denominator q_(3L) has a genuine corrected tie context already at two physical indices of order q_L, hence of order q_(3L)^(1/3). The corresponding positive tie weight is subexponential in the current denominator. The all-level existence proof is new; firstness is not required and is not claimed.

### Cited Findings

- The comparison slope, endpoint-register formula, and its actual sampled states were established in [cf_induction.md](cf_induction.md). The first round only certified three first crossings; it explicitly left the all-level formula unproved.
- The exact relation between A, B, the residue table and E is `z_(a,b)=A_a+B_b-1+C_(a mod3,b mod3)-E_b`; `H_02(x+y omega)=1_[x=0,y>=1]`. [Arithmetic state derivation](../boundary-and-arithmetic/arithmetic.md), [minimum Hessian derivation](../infinite-return-construction/weighted_returns.md).
- The new [certificate](record_returns_check.py) checks 25 induced levels without expanding their huge words, validates actual floor values by adjacent-convergent brackets, and independently computes the first three reciprocal contexts through b=1914.

### Inferences

**Scope of this section.** Every statement (R4)-(R18) is about the comparison-slope cocycle at alpha_* only. Its A, B and E are defined by the same exact floor recurrences and correction tests. These statements do not concern `alpha=log_3 2`, the actual finite boards D_t, or their optimal covering numbers. Here "actual state" means the state reached from the fixed origin of this comparison cocycle, rather than a freely selected lattice state.

**1. Fix one genuine comparison cocycle.** Let

```
alpha_*=[0;1,1,1,1,1,3,overline(2,1)].
```

This slope belongs to `(18/29,41/66)`, hence to `(3/5,2/3)`. It is not the actual logarithmic slope. For t>=0 let W_t be its lower-convergent word at index n=6+4t and V_t its preceding upper-convergent word. Write their lengths and numbers of ones as

```
|W_t|=q_t,  p(W_t)=p_t,
|V_t|=v_t,  p(V_t)=u_t.
```

The initial data are `(p_0,q_0)=(18,29)` and `(u_0,v_0)=(5,8)`. Both words are nonresonant, with phases `rho_W=omega,rho_V=omega^2` at every t. The exact four-digit word recurrence is

```
W_(t+1)=(W_t^3 V_t)^3 W_t^2 V_t,
V_(t+1)=(W_t^3 V_t)^2 W_t^2 V_t.                 (R4)
```

Indeed the four successive words are `W^2V`, `W^3V`, `(W^3V)^2W^2V`, and `(W^3V)^3W^2V`, using the alternating concatenation order. Consequently

```
[q_(t+1),v_(t+1)]^T=[[11,4],[8,3]][q_t,v_t]^T,
[p_(t+1),u_(t+1)]^T=[[11,4],[8,3]][p_t,u_t]^T.    (R5)
```

The exact endpoint root sums and rational recenter are

```
Q_(W_t)=(t-1)omega,   Q_(V_t)=-t-omega,
c_A,t=(1-t)/3.                                   (R6)
```

All q_t are odd, v_t even, p_t even and u_t odd, as follows from (R5) modulo2.

**2. An exact all-level EARLY HIT.** Define

```
g_t=v_t/2-14                 (t>=1),
f_t=q_t-v_t/2-14             (t>=0).
```

For t>=1, `0<g_t<q_t`; in particular, g_1=114. Let `Q_W(k)` be the root sum of the prefix of W of length k. Recall the affine root map `T_W(z)=Q_W+rho_W z`. Since `T_W^3=identity`, the prefix of W_(t+1) of length `4q_t+v_t` has map `T_V T_W`. From (R6),

```
T_V T_W(z)=z+omega^2.                            (R7)
```

Also `g_(t+1)=4q_t+v_t+g_t`. The remaining prefix is a prefix of a W_t copy, so

```
Q_(W_(t+1))(g_(t+1))=omega^2+Q_(W_t)(g_t).
```

The independent direct-floor seed is `Q_(W_1)(114)=3omega^2`. Hence

```
Q_(W_t)(g_t)=(t+2)omega^2                         (t>=1).    (R8)
```

Next, the prefix of W_(t+1) of length `7q_t+2v_t` has map `T_V^2 T_W`, and (R6) gives

```
T_V^2 T_W(z)=-t+omega^2 z.
```

Because `f_(t+1)=7q_t+2v_t+g_t`, equation (R8) yields

```
Q_(W_t)(f_t)=1-t+(t+1)omega                       (t>=2).    (R9)
```

The two initial seeds are `f_0=11,Q(f_0)=1+omega` and `f_1=209,Q(f_1)=2omega`, so (R9) holds for all t>=0. Furthermore, `f_(t+1)-f_t=6q_t+3v_t`, so `f_t=2 mod3` for every t.

The origin-anchored actual-axis identity is

```
3A_a=2+omega^(-a)+(1-omega^2)Q_A(a).
```

Each W_t is a lower-convergent word, so its f_t prefix agrees with the true alpha_* floor word. Substituting (R9), with `omega^(-f_t)=omega`, proves

```
ACTUAL A_(f_t)=1-t+omega                          (t>=0).    (R10)
```

This proves the all-level *hit* formula suggested by the three first-round crossings. It does not prove that f_t is the first such hit.

The Perron eigenvalue in (R5) is `lambda=7+4sqrt(3)`, and `v_t/q_t -> sqrt(3)-1`. Thus

```
q_t=Theta(lambda^t),
f_t~[(3-sqrt(3))/2]q_t,
f_L=Theta(q_(3L)^(1/3)).                          (R11)
```

**3. The translates are realized by ACTUAL B rows and E.** This step removes the objection that the h_L translates might not occur in the actual two-axis state.

Put

```
d_t=p_t-(u_t+19)/2.
```

Then `d_0=6`, `d_t=0 mod3`, and `d_(t+1)-d_t=6p_t+3u_t`. We claim

```
floor(f_t alpha_*)=d_t.                          (R12)
```

Let `epsilon_t=q_t alpha_*-p_t>0` and `epsilon'_t=u_t-v_t alpha_*>0`. Direct substitution gives

```
theta_t=f_t alpha_*-d_t
       =19/2-14alpha_*+epsilon_t+epsilon'_t/2.
```

Convergent inequalities and the initial denominators give `epsilon_t<1/66`, `epsilon'_t<1/29` for all t. With `18/29<alpha_*<41/66`, this implies

```
53/66<theta_t<24/29+1/66<1.                       (R13)
```

Thus (R12) holds. The same bounds imply

```
alpha_*<theta_t<2alpha_*,
2alpha_*<theta_t+1<3alpha_*,
4alpha_*<theta_t+2<5alpha_*.
```

Writing `n_b=floor(b/alpha_*)`, we obtain the exact reciprocal floors

```
n_(d_t)=f_t-2,
n_(d_t-1)=f_t-3,
n_(d_t-2)=f_t-5.                                (R14)
```

There are no rational ties, because alpha_* is irrational.

To compute B, use the elementary Beatty complement of the two sets

```
{k+floor(k alpha_*):k>=1},
{ell+floor(ell/alpha_*):ell>=1}.
```

They partition the positive integers: disjointness follows from the two opposite strict floor inequalities; their counting functions sum to M up to every integer M, since `1/(1+alpha_*)+1/(1+1/alpha_*)=1`. Up to `M=f_t+d_t`, the respective prefix sizes are f_t and d_t. Therefore, if Q_B is the reciprocal root sum with the same negative character,

```
Q_A(f_t)+Q_B(d_t)=sum_(j=1)^(f_t+d_t) omega^(-j)=-1.
```

The final equality uses `f_t=2 mod3,d_t=0 mod3`. Conjugating for the B recurrence and substituting (R9) gives

```
B_(d_t)=(t+1)+omega.                             (R15)
```

At d_t the B increment is exactly 1, by (R14), so

```
B_(d_t-1)=t+omega.
```

At `b=d_t-1=2 mod3`, equation (R14) activates the comparison cocycle's isolated correction test because `n_b-n_(b-1)=2`. Its color is `n_b-2b=1 mod3`, hence `E_b=omega`. The patch test cannot coexist with that test in the admissible slope range. Since `C_(2,2)=1`, for every `a=2 mod3` the comparison cocycle's corrected vertical row offset is

```
B_b-1+C_(2,2)-E_b=t.                            (R16)
```

Now take any L>=1 and set

```
a_L=f_L,             b_L=d_(L-1)-1.
```

Equations (R10) and (R16) prove the full ACTUAL state

```
z_(a_L,b_L)=A_(f_L)+(L-1)=omega,
H_02(z_(a_L,b_L))=1.                             (R17)
```

Both a_L and b_L are positive physical indices of order q_L. There is no freely chosen lattice state, phase or vertical translation. These are tie contexts on the same fixed comparison-slope cocycle, with its E included and b_L>=5. The lowest case is explicit: `f_0=11,d_0=6`, `B_5=omega`, `E_5=omega`, `C_(2,2)=1`, so the row offset is zero; `f_1=209` has `A_(f_1)=omega`. Thus the J=1 extension does not require a negative auxiliary prefix g_0.

**4. The weighted support obstruction is quantitative.** At current induced scale t=3L, the rational recenter is `c_A=1/3-L`, and q_(3L) is of order q_L cubed. The ray in (R16) has translation L-1, within the fixed offset -2/3 of `-c_A`. Its nonnegative horizontal local time is at least `2^(-f_L)`. Likewise, the nonnegative full weighted tie local time restricted to these actual contexts includes the term

```
1/(2^(a_L)3^(b_L))=exp(-O(q_L))
                  =exp(-O(q_(3L)^(1/3))).         (R18)
```

Consequently this relevant positive tie support cannot be bounded by `exp(-delta q_(3L))` for any fixed delta>0 at all large L. In particular, a large record recenter alone cannot force all these genuine tie events beyond a linear current-prefix scale. This refutes that proposed support mechanism exactly. It does not refute cancellation of several signed responses or a special result for the actual logarithm.

### Gaps

- The comparison slope is quadratic. The statement does not assert that `log_3 2` has these record trajectories. It establishes failure of a universal inference from the actual cocycle's order-three blocks and large recentering.
- The proof establishes hits, not firstness. The first-round finite first-hit values remain valid, but are not needed for (R18).
- A tie at an actual count state is not automatically the coefficient of every particular adjacent-swap decomposition. A proposed signed weighted return must retain and audit its actual contexts. The positive local-time lower bound cannot rule out coherent signed cancellation.

## Does a product-of-two-tail construction reach the arithmetic return threshold?

### Takeaway

The corner support and its product error are unconditional once the established finite formula is used. The arithmetic requirement is concentrated in two hybrid sums. Those sums are exactly where the weighted ray profiles remain, so this does not complete the return. If they could be cleared at the existing degree-six cost, the sufficient jump threshold would improve from q'-5q to q'-2q.

### Cited Findings

- True and one-sided rational-model axis words agree for `a<R=q+q'`, `b<S=p+p'`, including the correction data; the four low-column rules are distinct and must be retained. [Audited rational model](../global-boundary-proof/independent_audit.md), [current return report](../infinite-return-construction/REPORT.md).
- The clearing integer `D=27(2^(3q)-1)(3^(3p)-1)` has logarithmic cost `6q log2+o(1)`. Ordinary rational discreteness applies once the cleared real error tends to zero, provided the comparison value really is D-integral. [Previous denominator/error proof](../infinite-return-construction/skew_denominator.md).
- Generic transcendence does not guarantee infinitely many nonresonant outgoing digits >=2; all nonunit digits can be confined to the resonant pattern. The available universal supply is the smaller sharp ratio C_*. [Diophantine supply and sharpness](../infinite-return-construction/diophantine_supply.md), [final supply audit](../infinite-return-construction/final_return_audit.md).

### Inferences

**1. The exact hybrid construction.** Let `X_a` be all true horizontal data used by a birth readout, and `X~_a` its rational-model counterpart. Let `Y_b,Y~_b` contain the vertical axis state, correction E and the low-column convention. The residue-dependent readout is fixed. Define four bounded coefficient arrays

```
c_TT(a,b)=G_(a mod3,b)(X_a,Y_b),
c_MT(a,b)=G_(a mod3,b)(X~_a,Y_b),
c_TM(a,b)=G_(a mod3,b)(X_a,Y~_b),
c_MM(a,b)=G_(a mod3,b)(X~_a,Y~_b),
```

where `G=1-3 eta` uses the exact cone and actual four low-column rules. All four coefficients lie in `{1,-2}`. Their weighted sums Z_TT,Z_MT,Z_TM,Z_MM converge absolutely. The true target is Z_TT; Z_MM is the established rational model.

Set

```
Delta(a,b)=c_TT-c_MT-c_TM+c_MM,
M=Z_TT-Z_MT-Z_TM+Z_MM.
```

If `a<R`, the two horizontal data agree, so the first two and last two terms cancel. If `b<S`, the vertical data agree, so the other pairing cancels. Thus

```
Delta(a,b)=0 whenever a<R OR b<S,
|Delta(a,b)|<=6.
```

Summing the remaining corner gives the exact product bound

```
|M|<=6 [sum_(a>=R)2^(-a)] [sum_(b>=S)3^(-b)]
    =18*2^(-R)*3^(-S).                           (R19)
```

The shifts implicit in E's local floor tests do not shorten S: whenever b<S, the required earlier reciprocal floors also agree. Low columns are included in the readout, so they cancel exactly rather than being discarded.

**2. This corner residual is nontrivial on the ACTUAL logarithmic array.** The narrow certificate uses `p/q=5/8`, with successor `12/19` for `alpha=log_3 2`, so `(R,S)=(27,17)`. It computes true floors by exact integer comparisons of powers of2 and3, and the model floors with the audited one-sided endpoint rule. Including all E and low-column rules, it verifies corner support through `0<=a<=36,0<=b<=26`. There are 38 nonzero mixed corners in that targeted rectangle; the first in the certificate's order is

```
Delta(27,19)=3.
```

This is evidence for the exact support and nontriviality of this construction, not a proof of the full infinite weighted residual's nonvanishing. Terms outside the rectangle may cancel its finite partial sum.

**3. The exact missing arithmetic statement.** Define the hybrid comparison value

```
J=Z_MT+Z_TM-Z_MM.
```

Then (R19) gives `|Z-J|` with a product of two tails. Suppose, as an ADDITIONAL unproved input, that along an infinite nonresonant sequence

```
D_n J_n is an integer,
D_n=27(2^(3q_n)-1)(3^(3p_n)-1).
```

Under rationality `Z=A/B`, the cleared error `D_nZ-D_nJ_n` lies in `B^(-1) Z`. From (R19),

```
|D_nZ-D_nJ_n|
 <=486(1+o(1))*2^(4q_n-2q_(n+1)).                (R20)
```

Thus `q_(n+1)-2q_n -> +infinity` forces eventual equality. In particular, infinitely many nonresonant outgoing digits at least2 suffice, because

```
q_(n+1)-2q_n=(a_(n+1)-2)q_n+q_(n-1)>=q_(n-1).
```

A nonzero-error argument would then be necessary for contradiction. This is precisely the conditional advantage of a product-tail architecture.

**4. Why the arithmetic input has not been supplied.** In Z_MT, the horizontal state is periodic but the actual vertical state is accumulated and unbounded; Z_TM has the reciprocal problem. Their finite horizontal or vertical period evaluations leave the true weighted cone/ray profiles as coefficients. Applying `P_W^3=identity` evaluates the model direction but does not evaluate the other direction. The sum of three model-rotated horizontal components does not rotate the fixed true vertical component about the same barycenter, so the full skew cone partition cannot simply be inserted into a hybrid.

Consequently neither `D_nJ_n in Z` nor a fixed-coefficient S-unit expression for J_n has been proved. Substituting `J_n=Z-M_n` would restate the real identity and add no denominator information. Ordinary discreteness cannot be applied to M_n merely because it is small. The additional product error is established; the arithmetic comparison point needed to use it is not.

### Gaps

- No arithmetic compression of J_n was obtained. This is the central unresolved step in this product-tail route.
- Infinitely many actual eligible next digits >=2 are unproved, and the universal case with nonunit digits concentrated at resonances still needs another branch.
- No nonvanishing theorem for M_n or another adequate weighted return was proved. The requested infinite-return objective remains unresolved.
- Skipped: Lean, installs, broad scans, density decimals, archived edits and external submission. Main risk: confusing exact corner support or an induced record formula with rationality/controlled height of the hybrid weighted values.
