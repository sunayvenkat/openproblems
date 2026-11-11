# Arithmetic height of the complete boundary-response map

## Can a boundary with few geometric points guarantee a cheap exact network reduction?

### Takeaway

**No for the full boundary-response map.** One genuine low-row boundary parameter already has an exact response coefficient whose reduced denominator grows at least as `exp(c R^(1/kappa))`. In particular, a universal exact reduction to an `O(R)`-variable integer system with polynomial-sized coefficients cannot represent this response. This is a scoped obstruction to a concrete compression strategy, not a proof about the denominator of the particular optimized target source. — [Exact certificate](boundary_check.py), [accepted complete transport](../occupation-arithmetic-bridge/exact_transport.md), [accepted height and renewal audit](../arithmetic-renewal/renewal_audit.md).

### Cited Findings

- The complete ordered source includes the low term `8·3^(-1) q_(0,1)(1,0)`. The target in row `b=1` is the genuine Boolean kernel `Phi_1(x+y omega)=1_{x>=1,y>=0}`, rather than the identically zero row `b=0`. Low rows retain their separate horizontal resolvents and are not vertically shifted. — [ET8 and low definitions](../occupation-arithmetic-bridge/exact_transport.md), [exact implementation](../occupation-arithmetic-bridge/exact_transport_check.py).
- At horizontal residue `i=0`, the actual low-row state at `(a,b)=(3n,1)` is `A_(3n)-1`: `B_1=0` and `C_(0,1)=0`. The high row `b=4` has exactly the same state because `B_4=E_4=omega` and `C_(0,1)=0`. Its first-exit times from the Green box are already recorded as `tau_0=1`, `tau_1=32`, `tau_2=1065`. — [Actual lift and correction](../occupation-arithmetic-bridge/exact_transport.md), [independent renewal data](../arithmetic-renewal/renewal_audit.md).
- The accepted actual state-height estimate, enlarged for the finitely many low offsets, has fixed `C_rho>0`, `0<kappa<1` with `rho(zeta_(a,b)) <= C_rho(a+b+1)^kappa`. It is a lower bound on the physical index of an exterior arrival, not an upper bound on exit time. — [Height budget](../occupation-arithmetic-bridge/height_audit.md), [complete-tail application](../arithmetic-renewal/renewal_audit.md).
- The standalone checker uses no project imports or floating logarithms. It independently reconstructs the axes from integer powers, compares them with original colored boards, verifies the two row identifications, and reproduces the three exits and response denominators below. — [Checker](boundary_check.py).

### Inferences

**B1. Exact response of a single nonzero target row.** Keep every high block and every other low block fixed at its accepted ordered solution. Only in low block `(i,b)=(0,1)` prescribe the boundary value

\[
q_c=c+h/7\quad\text{outside }D_R,
\qquad (8I-U_A)q_c=h\quad\text{inside }D_R,
\qquad c\in[1/7,2/7].
\]

The domain and its first-exit time do not depend on `c`. The exact first-exit formula therefore gives, at the actual initial point,

\[
q_c(1,0)=\sum_{n<\tau_R}8^{-n-1}h_n
       +8^{-\tau_R}(c+h_{\tau_R}/7),
\quad \frac{\partial q_c(1,0)}{\partial c}=8^{-\tau_R}.
\]

Because only this low block varies, the coefficient of `c` in the **complete assembled source** is exactly

\[
\boxed{\beta_R:=\frac{\partial S_R}{\partial c}
  =\frac83\,8^{-\tau_R}
  =\frac1{3\,8^{\tau_R-1}}.}
\tag{B1}
\]

There is no cancellation from the other source terms: they are independent of this parameter. This parameter lies inside the same positive family as the accepted construction. Indeed `0<=q_c<=c+1/7`, and its exterior residual is `8c+h/7-q_c o T_A >=7c-1/7 >=6/7`. All other residuals remain unchanged, so the complete density identity and paired positivity are retained. This argument does not treat a single omitted local term as the whole target. — [First-exit formula and complete source weights](../arithmetic-renewal/renewal.md), [independent source audit](../arithmetic-renewal/renewal_audit.md).

For the three actual radii the reduced response denominator has:

| Radius | First exit `tau_R` | Reduced denominator of `beta_R` | Bit length |
|---|---:|---|---:|
| 0 | 1 | `3` | 2 |
| 1 | 32 | `3·2^93` | 95 |
| 2 | 1065 | `3·2^3192` | 3194 |

The target row is not a dummy: its actual reward is zero at `n=0` and one at `n=2`. The checker verifies the source response using two exact boundary values, rather than only verifying a copied fraction. — [Independent exact certificate](boundary_check.py).

**B2. Critical arithmetic height is intrinsic to the full response map.** At this first exit, `rho(zeta_(3 tau_R,1))>R`. The accepted height estimate gives

\[
\tau_R>\frac13\left((R/C_\rho)^{1/\kappa}-2\right).
\]

Consequently

\[
\log_2\operatorname{den}(\beta_R)
=3\tau_R-3+\log_2 3
>(R/C_\rho)^{1/\kappa}-5+\log_2 3.
\tag{B2}
\]

Since `1/kappa>1`, this exceeds every fixed multiple of `R log R` eventually. A rank-one boundary response can therefore have the same critical arithmetic scale as the full tail, despite its tiny rank. A Schur complement may reduce dimension while moving these large denominators into its entries; geometric boundary size alone does not control arithmetic height. — [Actual coefficient B1 and accepted height theorem](../occupation-arithmetic-bridge/height_audit.md).

**B3. Consequence for exact small integer networks, with scaling retained.** Suppose a proposed universal reduction represents this input-to-output coefficient as

\[
\beta_R=u_R^T K_R^{-1}v_R+w_R,
\]

where `K_R` is an invertible `m_R` by `m_R` integer matrix and `u_R,v_R,w_R` are integer input/output data. Its reduced denominator divides `|det K_R|`, regardless of cancellation in its numerator. If every matrix entry has magnitude at most `B_R`, the determinant expansion directly gives `|det K_R|<=m_R! B_R^(m_R)`. Thus

\[
\log\operatorname{den}(\beta_R)
\le m_R\log B_R+\log(m_R!).
\tag{B3}
\]

For `m_R=O(R)` and `B_R=R^O(1)`, this is `O(R log R)`, contradicting B2. Polynomial-sized rational input/output scalings with a common polynomial-sized denominator add only `O(log R)` and cannot repair the contradiction. The same observation applies to a rational matrix after a **common polynomial-sized clearing**. Arbitrary independent rational matrix denominators are not covered by that last condition. — [Elementary determinant expansion and coefficient B1](boundary_check.py).

### Gaps

- This excludes a universal exact `O(R)`-size, polynomial-height **integer** network for the full boundary-response map under the stated input/output scaling. It does not exclude an exact representation with many more variables, large-height entries, irrational phase readouts, or a different architecture. No claim is made about a general infinite-dimensional boundary operator's rank. — [Precise B1–B3 argument above](boundary.md).
- Most importantly, the result does **not** exclude cheap representation of one carefully chosen aggregate source `S_R(c_R)`. A large-denominator response coefficient can cancel against the fixed part after a rational parameter is chosen; internal parameter denominators need not be cleared in the final integer-affine identity. That is exactly why the previous convex interval construction is not contradicted by B2. Its optimized infinite denominator condition remains equivalent to irrationality, not independently proved. — [Aggregate-source distinction and Farey equivalence](../arithmetic-renewal/convex_audit.md).
- No adequate infinite family, proof of `d_R Psi_R ->0`, or solution of Erdős #168(ii) has been obtained. The remaining boundary obligation is **target-specific cancellation or another complete integer-affine identity**, including all low rows, with affordable clearing and the same nonzero residual. — [Full target acceptance criterion](../arithmetic-renewal/REPORT.md).
- Work stopped after this investigation round at the user's direction. Skipped Lean, external review, novelty checks, broad enumeration and new research directions. Material risk: promoting an obstruction for the full response map into an impossibility theorem for the particular target source. — [Scope and proof recorded here](boundary.md).
