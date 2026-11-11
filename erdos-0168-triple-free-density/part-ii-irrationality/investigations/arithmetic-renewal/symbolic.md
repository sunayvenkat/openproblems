# Prime arithmetic of the coupled source

## Can actual coupled paths terminate and give a rational source?

### Takeaway

Yes at radius zero: every actual high source grid terminates under all interior horizontal, vertical and diagonal branches. The resulting full 21-source value is rational, but its cleared positive residual is enormous. At radius one most tested grids reach the search frontier; no infinite survival or uniform termination conclusion follows. — [Exact certificate](symbolic_check.py), [accepted source identity](../finite-volume-calibration/exterior_audit.md).

### Cited Findings

- The accepted high operator is \(\mathcal L=216I-27U_A-8U_B+U_AU_B\). For \(g=0\), exterior values \(p=1+h/182\), and its unique bounded real Dirichlet solution, the complete source satisfies \(S_R=Q_{\rm full}(0)+\Psi_R\), \(\Psi_R>0\), and \(Z=2-3S_R+3\Psi_R\). The source contains nine high and twelve low initial values; low rows remain infinite before transport. — [Complete exterior/source audit](../finite-volume-calibration/exterior_audit.md), [exact transport ET6–ET8](../occupation-arithmetic-bridge/exact_transport.md).
- The present checker reconstructs the actual axes directly from original colored boards, and corrections from original root windows. It reproduces the accepted actual states \(\zeta_{12,8}=(-2,-2)\), \(\zeta_{22,35}=(-1,1)\), and \(A_0=A_9=1\), without importing project code or using floating logarithms. — [Checker](symbolic_check.py), [independent earlier reconstruction](../finite-volume-calibration/exterior_audit_check.py).

### Inferences

**SY1: actual finite source closure at \(R=0\).** At each high start \((i,b_j)\), \(i=0,1,2\), \((b_0,b_1,b_2)=(6,4,5)\), explore all reachable interior cells \((a,b)\) using the successors \((a+3,b),(a,b+3),(a+3,b+3)\). A successor outside the state box is terminal, since its value is prescribed independently of subsequent dynamics. A queue that empties therefore proves complete termination on that actual starting grid, rather than merely surviving a fixed number of tests. Both indices increase monotonically, so a finite explored graph is acyclic. Backward substitution proves that its source value is rational. — [Exact exhaustive algorithm](symbolic_check.py).

At \(R=0\), the nonempty high graphs have respectively:

| Start \((i,b)\) | Interior vertices | Maximum \((a-i+b-b_j)/3\) |
|---|---:|---:|
| \((0,6)\) | 1 | 0 |
| \((0,4)\) | 3 | 2 |
| \((0,5)\) | 1 | 0 |
| \((1,5)\) | 1 | 0 |
| \((2,6)\) | 15 | 17 |

The other four high starts are already exterior. All twelve low starts exit in at most three horizontal steps. Thus depth 20 Picard evaluation is exact at every source, regardless of behavior at other phase contexts. This is a certificate on the actual initial values; it does not by itself establish a finite-step representation over the full lifted phase domain. — [Full branch and low-exit assertions](symbolic_check.py).

For the accepted large-offset prescription, the exact complete source is
\[
S_0=\frac{7949385124218080419452346025}
{372885909329585286602293248}.
\]
Put \(D_0=\operatorname{den}(S_0)\). The checker evaluates the complete unexceptional birth head for \(a+b<100\). Since every omitted birth is between zero and one, the exact omitted mass is bounded by
\[
6\,2^{-100}-3\,3^{-100}.
\]
Consequently it proves
\[
7851029231031622054440914924
<D_0\Psi_0<
7851029231031622054440914925.
\]
This finite rational source does not supply a small cleared return. The bound retains every low row and the accepted exceptional-birth normalization. — [Exact rational head, complete tail and interval assertion](symbolic_check.py), [normalization](../numerator-and-residuals/occupation_audit.md).

At \(R=1\), the \((0,6)\) source grid also terminates: its graph has 10,000 vertices and maximum total increment 425; \((1,4)\) terminates with three vertices. The other seven source grids reach \(n=300\) or \(m=300\). At radii two and three every high start reaches that frontier. These are finite search outcomes only. — [Exact branch exploration](symbolic_check.py).

### Gaps

- Neither infinite joint survival nor joint termination at every radius is proved. Pure-axis uniform exit cannot establish termination under arbitrary alternating branches. Only the actual-source radius-zero closure is proved here; full-phase joint termination remains unproved.
- Rationality of one finite source is insufficient: the reduced denominator and the entire positive residual must be controlled along a growing family.

## Can prime-specific arithmetic detect the actual source cancellation?

### Takeaway

There is an exact modulo-three cellular recurrence for the **full aggregate source**, including its low-row normalization. A nonzero residue proves that its reduced denominator contains the entire factor \(3^{3m+3}\). This is sharper than an assumed \(216^m\) cost and explicitly includes cancellation across all 21 sources; it does not prove an infinite nonzero residue supply or a lower bound on the actual real approximation error. — [Certificate and independent recurrence](symbolic_check.py).

### Cited Findings

- The source coefficients are
\[
S_{R,m}^{H}=216\sum_{i=0}^{2}\sum_{b\in\{6,4,5\}}
2^{-i}3^{-b}p_{R,m}^{H}(i,b),\qquad
S_{R,m}^{L}=8\sum_{i=0}^{2}\sum_{b=0}^{3}
2^{-i}3^{-b}p_{R,m}^{L}(i,b).
\]
These are the accepted exact corner pairings, now applied to finite Picard approximants. — [ET6–ET8](../occupation-arithmetic-bridge/exact_transport.md).
- In this section the offset is specifically the accepted **large offset one**, not the improved small offset in the final section. Start \(p_{R,0}=0\) inside and with the prescribed \(1+h/182\) high, \(1+h/7\) low exterior values. Iteration is the actual Dirichlet fixed-point map, with exterior values held fixed. — [Accepted fixed point](../finite-volume-calibration/exterior_audit.md), [implementation](symbolic_check.py).

### Inferences

**SY2: exact common numerator and three-adic test.** Define
\[
q_m(a,b)=182\,216^m p_{R,m}^{H}(a,b),\qquad
r_m(a,b)=7\,8^m p_{R,m}^{L}(a,b).
\]
They are integers, by induction. Put
\[
N_{R,m}=27\cdot182\cdot216^m S_{R,m}.
\]
The full, unreduced numerator is exactly
\[
\begin{aligned}
N_{R,m}={}&
\sum_{i=0}^{2}\sum_{b\in\{6,4,5\}}
2^{3-i}3^{6-b}q_m(i,b)\\
&+26\,27^m
\sum_{i=0}^{2}\sum_{b=0}^{3}
2^{3-i}3^{3-b}r_m(i,b).
\end{aligned}
\tag{SY2}
\]
For \(m\ge1\), all low terms vanish modulo three, as do high starts at \(b=4,5\). Therefore
\[
F_{R,m}:=N_{R,m}\pmod3
=\sum_{i=0}^{2}2^{3-i}q_m(i,6)\pmod3.
\]
If \(F_{R,m}\ne0\), then exactly
\[
\boxed{v_3\bigl(\operatorname{den}(S_{R,m})\bigr)=3m+3.}
\tag{SY3}
\]
The denominator's possible factors 2, 7 and 13 do not alter this conclusion. All low sources were retained and shown to vanish at this prime; they were not assumed rational constants or omitted. — [Exact source scaling and assertions](symbolic_check.py).

Here is a cheap recurrence for \(F_{R,m}\). Let \(I_R(a,b)\) indicate that the actual corrected high state is inside, and write
\[
q_0(a,b)=
\begin{cases}0,&I_R(a,b)=1,\\182+h(a,b),&I_R(a,b)=0.\end{cases}
\]
On an interior cell,
\[
q_1(a,b)\equiv2h(a,b)-q_0(a,b+3)-q_0(a+3,b+3)\pmod3.
\]
For \(m\ge2\), the recurrence modulo three is
\[
q_m(a,b)\equiv
-q_{m-1}(a,b+3)-q_{m-1}(a+3,b+3)\pmod3
\]
inside, and zero outside. Thus initialize weights \(2^{3-i}\) at the interior starts \((i,6)\). At each step push a weight negatively to its \(B\) and \(AB\) successors, discarding exterior successors. Pair the layer \(m-1\) weights with \(q_1\). This is a finite-field, killed Pascal-type cellular evolution on actual corrected states. The source residues from this recurrence agree with separate exact rational Picard evaluation at depths \(1,2,4,8,12,20,32\), for each \(R=0,1,2,3\). — [Independent recurrence in checker](symbolic_check.py).

At radius one, \(F_{1,m}\ne0\) at 71 of the first 100 depths, including \(m=1,4,12,20,32\). In particular the depth-32 full source has \(v_2(\operatorname{den})=94\), \(v_3(\operatorname{den})=99\), and a 258-bit reduced denominator. The finite observation is not an infinite-density or nonvanishing theorem. — [Exact residue and rational outputs](symbolic_check.py).

The complete certified real error obeys
\[
|S_R-S_{R,m}|
\le\frac{61}{9}6^{-m}+\frac{640}{27}8^{-m}.
\tag{SY4}
\]
Indeed the sums of high and low source coefficients are \(182/27\) and \(560/27\), the corresponding global potential bounds are \(183/182\) and \(8/7\), and the contractions are \(1/6\) and \(1/8\). Along a depth where \(F_{R,m}\ne0\), the reduced clearing factor \(D_{R,m}\) is at least \(27^{m+1}\). Its product with the high term of this particular error majorant is at least
\[
183(9/2)^m.
\]
Thus the standard contraction estimate cannot certify a small cleared error at those depths. This is a **failure of the certified majorant**, not a lower bound on \(D_{R,m}|S_R-S_{R,m}|\). A real cancellation stronger than the contraction estimate remains possible. — [Accepted contraction/source bounds](../finite-volume-calibration/exterior_audit.md), [new numerator proof above](symbolic_check.py).

The unrestricted commuting symbol satisfies \(\Delta=27A+8B-AB\), with \(\Delta\bmod3=-B(1+A)\). After killing at the state boundary, the interior projections break that commutation. Frobenius sparsification cannot be applied to the killed operator as if it were the unrestricted polynomial. The path recurrence above remains valid at every interface. — [Actual killed recurrence](symbolic_check.py).

### Gaps

- No infinite nonzero supply for \(F_{R,m}\), useful vanishing subsequence, growing-radius cancellation theorem or actual error lower bound is proved.
- No rationality statement for the exact coupled source follows from finite approximants. Its rational approximation must preserve positivity relative to \(\Psi_R\), not merely have an absolute error tending to zero.

## Does the original small exterior offset already control every interface?

### Takeaway

For \(g=0\), yes. Retaining the current Boolean target term proves that the original \(p=(1+h)/182\) high prescription already has a bounded real interior solution with strictly positive residual across every interface. This improves the amplitude and corrects the earlier narrower assessment of that prescription, without giving rational sources. — [Original ansatz](../finite-volume-calibration/exterior.md), [exact constant checks](symbolic_check.py).

### Cited Findings

- The previous audit proved unrestricted real existence using the larger exterior \(1+h/182\), and left only far-exterior positivity established for \((1+h)/182\). — [Earlier audit and its scope](../finite-volume-calibration/exterior_audit.md).

### Inferences

**SY5: smaller-offset full real theorem.** Prescribe \(p=c+h/182\) outside, with \(g=0\), and put \(C=c+1/182\). If \(C\ge1/180\), the interior fixed-point map preserves the closed ball \(\|p\|_\infty\le C\), since
\[
\frac{36C+1}{216}\le C.
\]
Its contraction factor remains \(1/6\). At every exterior point, including interfaces,
\[
\begin{aligned}
\mathcal Lp-h
&=216c+\frac{34}{182}h-27p_A-8p_B+p_{AB}\\
&\ge180c-\frac{36}{182}.
\end{aligned}
\]
Consequently every \(c>1/910\) suffices. In particular the original \(c=1/182\), \(C=1/91\), gives
\[
144/182\le\mathcal Lp-h\le161/91
\]
on the entire exterior. The upper bound retains the current target term and uses \(216c+34/182+36C=161/91\). This uses the same full lifted domain and retained event data as the accepted theorem. — [Exact fixed-point operator](../occupation-arithmetic-bridge/exact_transport.md), [constant self-check](symbolic_check.py).

The matching low prescription \(p=(1+h)/7\) has \(C_L=2/7\), maps its closed ball into itself under contraction \(1/8\), and satisfies
\[
(8I-U_A)p-h\ge6/7
\]
everywhere outside. It is the earlier binary one-axis Dirichlet construction. Combining high and low preserves a strictly positive full residual with amplitudes independent of radius. — [Binary low construction](../finite-volume-calibration/calibration_audit.md).

### Gaps

- The smaller offset changes the exact source and its prime recurrences. The large-offset constants in SY1–SY4 must not be silently transferred to the small-offset family.
- Rational source arithmetic remains open for growing radii. This real improvement neither proves an adequate infinite return nor settles Erdős #168(ii).
- Skipped Lean, external theorem searches, external review and historical priority checks. Main risk: promoting finite prime data into an infinite supply theorem, or promoting failure of an upper majorant into failure of the actual error.
