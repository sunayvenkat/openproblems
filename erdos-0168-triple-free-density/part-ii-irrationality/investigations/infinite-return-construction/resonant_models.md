# Resonant rational models: universal drifts, exact cones, and hidden S-costs

## What are the exact resonant affine drifts and corrected positive shifts?

### Takeaway

For p+q divisible by 3, the harmonic-removed drifts are universally bounded and explicitly computable. They satisfy **h_A-h_B=sigma**, not h_A+h_B=sigma. A primitive positive diagonal shift adds omega or omega squared to the corrected state. It does not cancel the drift.

### Cited Findings

- The rational-floor model, low-column rules, and indicator tests are specified in [returns.md](<../../early-attacks/augmentation-and-return-attacks/returns.md>), with the necessary slope correction 3/5<p/q<2/3 in the [independent audit](<../global-boundary-proof/independent_audit.md>).
- The harmonic decomposition and exact fractional-lattice cone conventions are proved in [skew_denominator.md](<skew_denominator.md>). The global finite formula supplying the true birth interpretation is established in the [final prefix report](<../prefix-and-phase-audit/REPORT.md>).
- The new [resonant certificate](<resonant_models_check.py>) checks exactly the requested 7/11 and 8/13 models, their affine recurrences, correction transformations, positive-diagonal drifts, full rational sums, and reduced denominators. Its two cone formulas also pass independent finite-sum/tail checks. No broad model sweep was performed.

### Inferences

Assume gcd(p,q)=1, 3/5<p/q<2/3, and s=p+q is divisible by 3. Write sigma=sign(log_3(2)-p/q), and use the positive-index one-sided floor conventions of the earlier notes. Let

```
m_k=floor_sigma(kp/q),       n_l=floor_(-sigma)(lq/p),
H_A=sum_(k=1)^q omega^(2m_k+2-k),
H_B=sum_(l=1)^p omega^(n_l+1-2l),
h_A=-H_A/(1-omega^2),       h_B=-H_B/(1-omega).
```

The same geometric summation as before gives

```
R_a=A_a-2/3-omega^(-a)/3,       R_(a+q)=R_a+h_A,
S_b=B_b-2/3-omega^(-2b)/3,      S_(b+p)=S_b+h_B.       (R1)
```

These recurrences include index zero, where A_0=B_0=1 is specified separately. Put P=3q,Q=3p. Then the actual integral states satisfy

```
A_(a+P)=A_a+d_A,  d_A=3h_A,
B_(b+Q)=B_b+d_B,  d_B=3h_B.                          (R2)
```

**Universal drift table.** Write s=3r. Since gcd(r,q)=1, multiplication by r permutes residues modulo q. For 0<=k<q,

```
floor(ks/q) mod3 = floor(3(rk modq)/q).
```

Thus the sum of omega^(-floor(ks/q)) over k=0,...,q-1 equals 1 when q=1 modulo3, and -omega when q=2 modulo3. Remove k=0 and add the endpoint k=q; its weight is 1 for sigma positive and omega for sigma negative. Since omega H_A=sum_(k=1)^q omega^(-k-m_k), this determines H_A exactly.

For H_B, the finite Beatty partition proved in the skew note gives

```
omega H_A+H_B=sigma(1-omega).
```

The minus sign in h_B is essential: this identity implies h_A-h_B=sigma. Evaluating gives the complete table:

| q mod3 | sigma | 3h_A | 3h_B |
|---|---:|---|---|
| 1 | +1 | 2+omega | -1+omega |
| 1 | -1 | -1+omega | 2+omega |
| 2 | +1 | 1-omega | -2-omega |
| 2 | -1 | -2-omega | 1-omega |

In particular, d_A-d_B=3sigma. Both drifts have the same imaginary coordinate. Positive diagonal shifts add these imaginary components; they do not remove them.

For b>=4, the indicator conditions are invariant under b->b+p, and their colors advance by q-2p=0 modulo3. Therefore the entire correction vector satisfies

```
E_(b+p)=E_b.                                        (R3)
```

Using C=(1-omega^(-a))(1-omega^(-2b))/3, the corrected state is

```
z_(a,b)=2/3+omega^(-a-2b)/3+R_a+S_b-E_b.
```

For arbitrary nonnegative i,j, its q-by-p block formula is

```
z_(a+iq,b+jp)
 =z_(a,b)+i h_A+j h_B
   +omega^(-a-2b)[omega^(p(i+j))-1]/3.               (R4)
```

The harmonic is retained in (R4); dropping it would generally give nonintegral states. On the 3q-by-3p sublattice it disappears, giving exactly z+i d_A+j d_B.

Define the primitive positive shift

```
T=(q,2p) if sigma=+1; T=(2q,p) if sigma=-1.
```

The table, (R3), and the harmonic factor prove the particularly simple full identity

```
z_(a+T_a,b+T_b)=z_(a,b)+omega^q,  b>=4.              (R5)
```

For q=1 modulo3 this adds omega=(0,1); for q=2 modulo3 it adds omega^2=(-1,-1). In both cases the cone digit can only increase under T. Its increase conditions are respectively

```
q=1 mod3: x<=0 and x-y=1;
q=2 mod3: x=1 and x-y<=0.                           (R6)
```

These are exact integer conditions, with ties included. They are not zero-drift periodicity assertions.

For 7/11, sigma=-1 and (d_A,d_B)=((-2,-1),(1,-1)); T=(22,7), and its drift is omega^2. For 8/13, sigma=+1 and (d_A,d_B)=((2,1),(-1,1)); T=(13,16), and its drift is omega.

### Gaps

The bounded block drifts do not bound the base states A_a or B_b inside their respective periods. No uniform bound for those accumulated states, and no uniform bound for the resulting cone intercepts, is assumed here.

## What exact lattice-cone generating functions and scalar denominators result?

### Takeaway

Each high-column residue class has an explicit rational lattice-cone sum. Globally the only non-S denominator is a single primitive diagonal factor, of nominal cost 3q log2. Nevertheless the full scalar denominator also has powers of 2 and 3 from the cone intercepts and low-column preperiods. The requested models show that these additional costs can be substantial even when the base-state norm is only three.

### Cited Findings

- The exact coefficient alphabet, low columns, and isolated/patch corrections are those in the [audited model](<../global-boundary-proof/independent_audit.md>).
- The complete rational evaluations and independent truncation bounds are implemented in [resonant_models_check.py](<resonant_models_check.py>), which passes for both models. It does not print or compute new density decimals.

### Inferences

**One explicit cone formula.** Use P=3q,Q=3p and X=2^(-P),Y=3^(-Q). For a base corrected state z=x+y omega put d=x-y. When (d_A,d_B)=((2,1),(-1,1)), the cone condition at block (i,j) is

```
j>=L(i):=max(0,2i+x,ceil((i+d)/2)).
```

Put I=max(0,ceil(-x/2),ceil((d-2x)/3)). For i>=I, L(i)=2i+x, and therefore its complete generating function is

```
G_+(x,y;X,Y)
 = sum_(i=0)^(I-1) X^i Y^L(i)/(1-Y)
   +X^I Y^(2I+x)/[(1-Y)(1-XY^2)].                  (R7)
```

When (d_A,d_B)=((-2,-1),(1,-1)), the condition is

```
0<=j<=J(i):=min(2i-x,floor((i-d)/2)).
```

Put I=max(0,d,ceil(x/2),ceil((2x-d)/3)). For i>=I, J(i)=floor((i-d)/2)>=0. Consequently

```
G_-(x,y;X,Y)
 = sum_(0<=i<I,J(i)>=0) X^i(1-Y^(J(i)+1))/(1-Y)
   +X^I/[(1-X)(1-Y)]
   -[X^I Y^(floor((I-d)/2)+1)
      +X^(I+1)Y^(floor((I+1-d)/2)+1)]
     /[(1-Y)(1-X^2Y)].                             (R8)
```

The other two drift-table cases are obtained by swapping i,j and X,Y: q=1,sigma=-1 uses G_+(x,y;Y,X), and q=2,sigma=+1 uses G_-(x,y;Y,X). Thus (R7)-(R8) cover all resonant models, not only the two checked ones.

Sum the appropriate G with weights 2^(-a)3^(-b) over 0<=a<P and 4<=b<Q+4. This is a complete, finite, exact rational formula for all high digits. The columns b=0,1,2,3 are retained with their audited tests. On each residue a modulo P those tests are Boolean combinations of integer affine inequalities in the block index, so the digits eventually become constant. Their finite initial segment and geometric constant tail give their exact sum. The exception eta(0,1)=1 is retained separately. Finally Z~=3-3 sum eta~/(2^a3^b).

**Primitive diagonal denominator, with proof of what it does and does not mean.** Let f(U,V)=sum eta~(a,b)U^a V^b as a formal series. Equation (R6) changes a cone digit only on a finite set of high lattice cells. For example, in the first drift case, x+i*2-j<=0 and d+i-2j=1 force

```
i=1-d+2j,    0<=j<=floor((2d-x-2)/3).
```

This is finite. The other cases either exchange i,j or exchange x,d, and have the same finite bound. Therefore, outside the starting strips, multiplication by 1-U^(T_a)V^(T_b) leaves finitely many high coefficients. Each starting strip is eventually constant along its unbounded axis, including the four audited low columns. Multiplication by (1-U)(1-V) kills those constant tails. Hence

```
f(U,V)=P_0(U,V)/[(1-U)(1-V)(1-U^(T_a)V^(T_b))],      (R9)
```

where P_0 is an integer polynomial. In particular, the apparent cubic diagonal factor in (R7) or (R8) cancels after the complete residue sum; so do the large axis-period factors. This is a genuine resonant denominator reduction.

However the degree of P_0 is not uniformly bounded by T_a,T_b. Let M>=1 bound |x| and |x-y| for the corrected base states 0<=a<P,4<=b<Q+4, and also for the uncorrected low-column states 0<=a<P,0<=b<4. The finite exceptional families above have block coordinates at most 3M-1. High axis tails stabilize after at most M+1 blocks; all low tests stabilize after at most 2M+2 blocks, because |y|<=2M and their nonzero linear slopes have magnitude at least one. Including the starting shifts and the two unit differences, the safe degree bounds

```
A_* = P(3M+4)+1,    B_* = Q(3M+4)+4                 (R10)
```

contain the support of P_0. These bounds are deliberately conservative, but require no bounded-state assumption.

Set S=2^(A_*)3^(B_*), W=2^(T_a)3^(T_b). Substituting U=1/2,V=1/3 in (R9) proves

```
D_*=S(W-1),       N_*=D_* Z~ is an integer.           (R11)
```

Indeed (1-U)(1-V)=1/3, and S clears the polynomial P_0. Thus the reduced denominator has no prime factor outside {2,3} and the single diagonal W-1. But its powers of 2 and 3 are real denominator costs, not ignorable normalizations. The proved general bound is log D_*=O((q+p)M), rather than 3q log2+o(q). No sharp uniform constant gamma has been established.

The finite formula before collapsing its rational numerator has O(pq(M+1)) cone terms and low-column terms; the global polynomial bound has at most (A_*+1)(B_*+1)=O(pq(M+1)^2) monomials. Collapsing them to the one integer N_* gives a fixed two-unit expression, at the price of the S-factor in its height. With |Z~|<=6,

```
H(N_*:SW:S)<=6SW.                                  (R12)
```

**Exact requested models.** Full reduction gives

| p/q | M | Primitive W-1 | Exact reduced denominator | Bits |
|---|---:|---|---|---:|
| 7/11 | 3 | 2^22*3^7-1 = 9172942847 | 2^13*3^5*(2^22*3^7-1) | 55 |
| 8/13 | 3 | 2^13*3^16-1 = 352638738431 | 2^29*3^24*(2^13*3^16-1)/7 | 103 |

For 7/11 the cone formula's maximum finite block cutoff is three; for 8/13 it is one. Those are not the complete scalar preperiod costs: the reduced S-valuations in the table account for the full model, including all low columns. Safe low-column cutoffs used in the check are eight and nine blocks; they are bounds, not claims of minimal preperiods. The checker independently compares the complete infinite digit sum against a finite rectangle with its exact geometric-tail bound.

The exact first floor-disagreement rectangles are R=19,S=12 for 7/11, and R=8,S=5 for 8/13. These small rational slopes are not consecutive-convergent models with R=q+q'. Their matching windows are already much shorter than their full clearing scales.

### Gaps

Formula (R9) identifies the non-S denominator exactly, but it does not bound the powers of 2 and 3 in its reduced value by o(q), or by any small fixed multiple of q. The conservative bound (R10) can be far from sharp. No cancellation theorem removing these intercept/low-column S-costs has been proved. The exact examples are obstructions to ignoring the costs, not an impossibility theorem for every resonant subsequence.

## Do the error, height, minimum-unit scale, and resonant supply yield an adequate infinite sequence?

### Takeaway

No. Resonance supplies a genuinely different rational architecture, but neither its full clearing cost nor an adequate infinite supply is controlled. Even the idealized cost-three diagonal model would not combine with the old nonresonant threshold-five model to give a universal consequence of transcendence. Actual intercept costs make the gap larger.

### Cited Findings

- The full-rectangle error bound is proved in [skew_denominator.md](<skew_denominator.md>).
- Sharp nonresonant jump supply and the limitation of changing only a floor intercept are in [diophantine_supply.md](<diophantine_supply.md>).
- The final independent audit checks the no-resonance transcendental continued-fraction obstruction in [final_return_audit.md](<final_return_audit.md>).

### Inferences

If the one-sided rational floors match the true floors for a<R and b<S, all digit rules match on that rectangle, whether or not the model is resonant. Therefore

```
|Z-Z~|<=9(2^(-R)+3^(-S)-2^(-R)3^(-S)).              (R13)
```

For a convergent p/q with successor p'/q', the same Farey argument gives R=q+q',S=p+p'. Combining (R11) with (R13) gives the precise sufficient clearing condition

```
D_*(2^(-R)+3^(-S)) -> 0.                            (R14)
```

Under rationality Z=A/B, the cleared E=D_*Z-N_* belongs to (1/B)Z. Consequently (R14) already forces eventual exact equality Z~=Z by ordinary rational discreteness; a Subspace Theorem is unnecessary for this integer-cleared approximation. Nonstabilization would still be required for a contradiction.

If a sharp reduced denominator D has log D=gamma q log2+o(q), the scalar criterion requires the actual gap

```
(q+q')log2-log D -> +infinity,
```

with corresponding control of the small o(q) term. A fixed ratio margin q'/q>gamma-1+delta is sufficient. In the idealized case D=W-1 and gamma=3, next continued-fraction digits at least two would give q'-2q>=q_previous->infinity. The actual D has extra powers of 2 and 3, so this idealized conclusion cannot be applied without controlling them.

For the fixed-dimensional arithmetic formulation, keep the S-factor:

```
E=Z SW-Z S-N_*.
```

Both positive units SW and S are at least one, so the valid minimum-unit parameter is t=1. It satisfies **0<t<=min(1,SW,S)**. Dividing by S makes N_*/S nonintegral and does not preserve the hypotheses of the mixed-form statement. Equivalently, expanding its numerator into small S-units introduces a small minimum unit whose scale must be paid. Thus rescaling does not remove the preperiod cost.

There is also no universal infinite resonance supply. Let s_n=p_n+q_n modulo3 and t=s_(n-1)/s_n when both are nonzero. At t=2, digit 3 preserves t=2 and creates no zero. The two-digit block (2,1) maps t=2 to t=1 and back to t=2, again without a zero. After the five-1 prefix discussed in the independent audit, any tail built from these blocks avoids all later resonances. Such tails can be nonperiodic, and the independent audit constructs a sparse-block transcendental example. Every outgoing ratio is less than four, so the old nonresonant threshold-five scalar model does not cover it either. This is a limitation of inferring a return supply from generic transcendence; it is not a statement that log_3(2) has this continued fraction.

### Gaps

No adequate unconditional infinite-return sequence, controlled full resonant height, or nonstabilization theorem has been obtained. The resonant loophole does produce an exact and useful single-diagonal rational generating function, but it does not complete Erdős 168(ii). Only the two named models and the independent cone checks were computed; no old file was edited, no dependency installed, no broad sweep or new density decimal computed, and no Lean work performed.
