# Arithmetic and obstruction audit before the global boundary proof

Audit date: 7 November 2026. This is an audit-only round. I independently checked the LCM translation argument and the coefficient-extension argument, including its cited arithmetic theorem. I also reproduced the exact spanning counterexample without rerunning its search or changing earlier artifacts. I authored the preceding multi-root argument, so this note does **not** independently certify that argument.

Verdict: no substantive gap was found in the audited arithmetic proofs. The integer-coefficient statements should explicitly retain the hypothesis \(B\ge1\). The weak three-color spanning obstruction is false, even with positive-exponent contacts on both axes and with the exceptional isolate excluded. Its witnesses have negative deficiency, so positive criticality remains an essential missing hypothesis. No global optimum or irrationality theorem follows from this audit.

## Does the LCM boundary recursion and translate-independence proof survive independent review?

### Takeaway

Yes. The absolute-convergence argument, finite-quotient recurrence lemma, separation of jump fibers, and transfer from the kernel to the summed functions are valid as stated for a finite prime set of size at least two. The conclusion excludes a particular exact linear translation mechanism; it does not imply irrationality of a value at one phase.

### Cited Findings

- The definitions and proofs audited are Section 2, items 1–5 of [lcm.md](<../../early-attacks/augmentation-and-return-attacks/lcm.md>), including its equations (1)–(7).
- The return-scale application in that note invokes [coefficient_extension.md](<../../early-attacks/augmentation-and-return-attacks/coefficient_extension.md>), audited separately below.

### Inferences

**1. The ambient denominator kernel is correct.** For a fixed finite prime set \(P\), put \(k=|P|\ge2\),

\[
H_P(x)=\prod_{p\in P}p^{\lfloor\log_p x\rfloor},\qquad
w_P(t)=H_P(e^t)^{-1}.
\]

The running LCM of the \(P\)-smooth prefix through \(x\) equals \(H_P(x)\): every prefix member divides this product, and the prefix contains the largest allowed power of each prime. Summing once per smooth integer therefore preserves repeated denominators. There is no accidental replacement by the distinct-denominator series.

**2. Absolute convergence justifies the boundary identity.** For \(A\subseteq P\), let

\[
F_{P,A}(t)=\sum_{s\in\mathcal S_A}w_P(t+\log s),\qquad t\ge0.
\]

The bound

\[
0<w_P(t+\log s)\le C_Pe^{-kt}s^{-k},
\qquad C_P=\prod_{p\in P}p,
\]

has summable majorant \(C_P\prod_{q\in A}(1-q^{-k})^{-1}\), independent of \(t\ge0\). Thus the series converges absolutely and uniformly there. Splitting the exponent of \(q\in A\) into zero and positive values gives exactly

\[
(I-T_{\log q})F_{P,A}=F_{P,A\setminus\{q\}},
\qquad
\prod_{q\in A}(I-T_{\log q})F_{P,A}=w_P.
\]

The denominator prime set remains \(P\). No exchange of a conditionally convergent sum, limit, or infinite family of operators occurs: the final operator is a finite product. The stated decay comparison with the smaller ambient prime set is also correct; a lower bound follows already from the summand \(s=1\).

**3. The finite-ratio recurrence lemma is valid over real coefficients.** If \(a_n>0\), its ratios \(r_n=a_{n+1}/a_n\) take finitely many values, and

\[
\sum_{j=0}^M c_j a_{n+j}=0,\qquad c_0c_M\ne0,
\]

eventually, division by \(a_{n+M-1}\) makes the next ratio a unique function of the preceding \(M-1\) ratios. Positivity makes every denominator nonzero. The actual sequence of finite states is deterministic, hence eventually periodic. The cases \(M=0\) and \(M=1\) are handled explicitly in the source note. No arithmetic restriction on the real \(c_j\) is needed.

For \(\kappa_n=w_P(n\log p)\), the ratio is

\[
\frac{\kappa_{n+1}}{\kappa_n}
=p^{-1}\prod_{q\ne p}q^{-\delta_q(n)},\qquad
\delta_q(n)=\lfloor(n+1)\log_qp\rfloor-\lfloor n\log_qp\rfloor.
\]

Each exponent has two possible integer values. Periodicity of the rational ratio would, by unique prime factorization, make each \(\delta_q\) eventually periodic. Its mean would then be rational, whereas telescoping gives mean \(\log_qp\), irrational for distinct primes. This proves the required absence of any eventual constant-coefficient recurrence for \(\kappa_n\).

**4. Jump fibers are correctly separated.** At a positive jump time \(n\log p\), only the \(p\)-factor changes, and the right-minus-left jump is \(-(p-1)\kappa_n\). For shifts \(s_v=\sum_qv_q\log q\), equality of a \(p\)-jump of one translate and a \(q\)-jump of another gives

\[
ne_p-v=me_q-u.
\]

For \(p\ne q\) and fixed \(u,v\), the exponent coordinates determine at most one pair \((n,m)\). Hence only finitely many cross-prime coincidences occur in a finite proposed translate relation. Distinct fibers that agree away from \(p\) are exactly the translates sharing infinitely many \(p\)-jump times. After excluding the finitely many coincidences and domain endpoints, the jumps in any one fiber yield an eventual recurrence for \(\kappa_n\). The preceding step forces every coefficient in that fiber to vanish.

Only irrationality of individual logarithmic ratios and unique prime factorization are used. The proof does not assume rational independence of reciprocal logarithmic ratios or full torus equidistribution.

**5. Independence transfers to every summed boundary family.** An eventual relation among finitely many translates of \(F_{P,A}\) can be acted on by the finite commuting boundary operator above. It produces the identical coefficient relation among translates of \(w_P\), already excluded. Every additional shift is positive, so the assumed late half-line remains inside the identity's domain. Potentially negative original shifts cause no difficulty after increasing its starting point.

Consequently the constant-coefficient translate-independence statement and the exclusion of a finite-dimensional invariant space containing \(F_{P,A}\) are justified. The displayed nonlinear branch-switching identity for \(w_P\) is compatible with this conclusion: linear independence of discontinuous translates does not give algebraic independence.

### Gaps

- No gap was found in these elementary proofs. This is not an audit of the separate historical-priority, live problem-status, Cook-manuscript, or value-theorem applicability claims in Section 1 of the original note.
- The argument concerns identities valid for every sufficiently large real phase. It says nothing decisive about a nonlinear identity or rational value at a single phase, and does not exclude sparse approximate return identities.
- It does not construct the bounded-term compression, exponentially small nonzero error, or arithmetic nonvanishing required for an irrationality proof.

## Is the coefficient extension actually uniform in its variable parameters?

### Takeaway

Yes, under \(B\ge1\) and the stated fixed-data hypotheses. The actual cited one-form Subspace Theorem supports the induction, and each exceptional-hyperplane step preserves the required coordinate bounds. The constants can be chosen independently of \(B\), the integer coefficients, the S-units, the integer term, and the lower scale.

### Cited Findings

- I fetched the primary statement of [Luca–Ouaknine–Worrell, *Transcendence of Hecke–Mahler Series*, Theorem 1 and its preceding height definition](https://arxiv.org/html/2412.07908v2#S2.Thmtheorem1) on 7 November 2026. Its dimension, S-integer, distinguished-coordinate, projective-height, and finite-union-of-subspaces hypotheses match the application.
- The derived statements audited are (P), (M), the integer-coefficient corollary (3), and the external-height formulation in [coefficient_extension.md](<../../early-attacks/augmentation-and-return-attacks/coefficient_extension.md>). These extensions are deductions in the note, not assertions that the primary source states those exact corollaries.

### Inferences

#### Actual arithmetic input and fixed data

Specialize the cited theorem to \(K=\mathbb Q\), the place set \(S^*=S\cup\{\infty\}\), distinguished place \(\infty\), a fixed rational linear form \(L\), and a coordinate \(k\) whose coefficient is nonzero. In dimension at least two, its conclusion covers all S-integer vectors satisfying

\[
|L(\mathbf z)|\prod_{(i,v)\ne(k,\infty)}|z_i|_v
\le H(\mathbf z)^{-\epsilon}
\]

by finitely many proper rational subspaces. These may be enlarged to rational hyperplanes. The family depends only on the fixed form, dimension, places, and \(\epsilon\), not on later bounds imposed on the coordinates. This is precisely the uniformity needed in the note. One-dimensional base cases are proved directly and do not invoke the theorem outside its stated dimension range.

The extension fixes \(S,m,d_1,\ldots,d_m,\epsilon\). It then quantifies over all \(B\ge1\), all admissible nonzero S-integers \(x_i\), all integers \(N\), and every \(0<t\le\min(1,|x_i|)\). Constants may depend on the fixed data but not on these latter variables. Neither their effectiveness nor uniformity as \(m\) grows is asserted.

#### Pure form: product and exceptional branches

Define \(A_S(x)=|x|\prod_{p\in S}|x|_p\). For a nonzero S-integer this is a positive integer, so \(1\le A_S(x)\le B\) is meaningful. For \(E=\sum d_ix_i\) and a nonzero coefficient \(d_k\), the exact theorem product is

\[
\Phi_P=\frac{|E|}{|x_k|}\prod_i A_S(x_i)
\le |E|B^m/t.
\]

Outside the fixed exceptional union, this yields the claimed lower bound with constant one. On each exceptional hyperplane, solving for one coordinate changes only the fixed rational coefficients of \(E\); the remaining coordinates themselves are not changed. Thus their S-integer property, bounds \(A_S(x_i)\le B\), and lower bound \(|x_i|\ge t\) survive unchanged.

Deleting coordinates from a nonzero rational vector cannot increase its projective height: every local maximum decreases weakly, and only finitely many factors differ from one. The retained vector is nonzero here because all its coordinates are nonzero. The lower-dimensional bound has B-loss \(B^{-(m-1)}\), which is at least \(B^{-m}\). Zero new coefficient vectors create only vacuous branches because \(E\ne0\) is required. Taking the minimum over finitely many positive branch constants proves (P), uniformly in \(B\).

#### Mixed form: why no bound on the size of \(N\) is required

For \(E=\sum d_ix_i-N\), \(N\ne0\), distinguish the \(N\)-coordinate, whose coefficient is \(-1\). The exact product becomes

\[
\Phi_M=|E|\prod_{p\in S}|N|_p\prod_i A_S(x_i)
\le |E|B^m.
\]

Here \(|N|_p\le1\) uses integrality, so no separate absolute-value bound on \(N\) is needed. Outside exceptional hyperplanes the bound is stronger than required because \(t\le1\).

On a hyperplane with nonzero \(N\)-coefficient, eliminating \(N\) gives a pure form in the original \(m\) coordinates; this is why the proof establishes all pure dimensions first. On a hyperplane whose \(N\)-coefficient is zero, eliminating an \(x_i\) leaves the integer \(N\) unchanged and invokes the smaller mixed dimension. Heights decrease under both deletions. The cases \(N=0\), zero fixed coefficients, negative coordinates, and impossible hyperplanes are handled correctly. A finite minimum of constants again retains the required uniformity.

#### Variable integer coefficients and height

Put \(x_i=c_iu_i\), where \(u_i>0\) are rational S-units and \(0<|c_i|\le B\). Then

\[
A_S(x_i)=A_S(c_i)\le B,\qquad |x_i|\ge u_i\ge t.
\]

At every nonarchimedean place, multiplication of coordinates by integers weakly decreases the local maximum. At the real place, \(B\ge1\) gives

\[
\max(|N|,|c_1u_1|,\ldots,|c_mu_m|)
\le B\max(|N|,u_1,\ldots,u_m).
\]

Therefore

\[
H(N:c_1u_1:\cdots:c_mu_m)
\le B H(N:u_1:\cdots:u_m),
\]

and (M) gives exactly

\[
\left|\sum_i d_ic_iu_i-N\right|
\ge CtB^{-m-\epsilon}H(N:u_1:\cdots:u_m)^{-\epsilon},
\quad\sum_i d_ic_iu_i-N\ne0.
\]

If some \(c_i=0\), deleting those coordinates is valid; there are only finitely many possible supports. Their constants can be minimized, their smaller B-loss is stronger, and their heights do not exceed the original height. Empty support gives a nonzero integer and is immediate.

**Minor statement clarification.** The integer-coefficient corollary and its restatement in `lcm.md` should explicitly say \(B\ge1\), as the preceding theorem does. Without that convention, the all-zero coefficient choice could allow \(B=0\), making the displayed power undefined. The proof already uses \(B\ge1\), including in the real-place estimate for the unchanged \(N\)-coordinate. This is a missing restatement of a parameter condition, not a failure of the theorem under its intended hypotheses. Earlier files were left unchanged.

#### Return scale and external height

For fixed \(m,S,d_i\), height at most \(e^{C_0L}\), coefficient bound \(B_L=e^{o(L)}\), and fixed \(\eta>0\), choose \(\epsilon>0\) with \(C_0\epsilon<\eta\). The lower bound is then \(Ct_L\exp(-C_0\epsilon L-o(L))\), contradicting \(0<|E_L|\le t_Le^{-\eta L}\) along unbounded \(L\). The factor \(t_L>0\) cancels; it need not have its own exponential lower bound. The number of terms must remain fixed.

The external-height version is also valid: apply (P) or (M) with \(\epsilon/2\), use \(B=\mathscr H^\delta\), and impose \(m\delta\le\epsilon/2\). Combined with \(H(\mathbf z)\le\mathscr H\), this yields \(Ct\mathscr H^{-\epsilon}\). If \(\delta<0\), the stated S-integer bound has no admissible coordinates because \(A_S(x_i)\ge1\) and \(\mathscr H\ge2\); the nonvacuous case has \(\delta\ge0\).

### Gaps

- No material arithmetic failure was found after checking the cited theorem directly. The constants are qualitative and may be ineffective.
- The result does not allow the number of terms, prime set, or rational coefficient vector to vary arbitrarily with the return scale.
- Fixed-term compression and nonzero exponential saving remain hypotheses. Neither the coefficient extension nor the LCM translation obstruction supplies them.

## What exactly does the \(t=729\) spanning counterexample disprove?

### Takeaway

Connectivity, both axis contacts, and an outer contact do not prohibit three color-specific sets from lying together in an independent set. An exact witness avoids the origin entirely; adding the origin also works. Its deficiencies are negative, so it does not refute any claim requiring positive-deficiency critical sets, the global finite optimum, or an existential complete vertical phase for a minimum cover.

### Cited Findings

- The original single-board search is preserved in [phase_spanning_check.py](<../../early-attacks/augmentation-and-return-attacks/phase_spanning_check.py>) and [its numerical search record](<../../early-attacks/augmentation-and-return-attacks/phase_spanning_check.json>). Its optimization status is not needed as a mathematical certificate.
- The stronger exact witness, with 27 added and 1 optionally removed, is verified by the dependency-free [verify_phase_witness.py](<../../early-attacks/augmentation-and-return-attacks/verify_phase_witness.py>), with explicit data in [verify_phase_witness.json](<../../early-attacks/augmentation-and-return-attacks/verify_phase_witness.json>).
- In this audit I loaded that verifier with a non-main module name, called its certificate function on both stored cases, and compared the results exactly with the saved JSON. Every assertion passed. This did not rerun the MILP or write to the earlier folder.

### Inferences

#### A counterexample without origin contacts

Let \(t=729\), color \(2^a3^b\) by \(a-b\pmod3\), and take

\[
V_0=\{6,8,27,48,288\},\quad
V_1=\{16,72,243,324\},\quad
V_2=\{4,18,81,486\}.
\]

Each set lies in its indicated color. The same-color face steps are multiplication by \(6,4/3,9/2\) and their inverses. The following simple paths establish connectivity:

\[
27-6-8-48-288,\qquad
16-72-324-243,\qquad
4-18-81-486.
\]

Each set has positive-exponent contacts on both axes and a label above \(t/3=243\):

| Color | Horizontal contact | Vertical contact | Outer contact |
|---|---:|---:|---:|
| 0 | 8 | 27 | 288 |
| 1 | 16 | 243 | 324 |
| 2 | 4 | 81 | 486 |

Thus the counterexample does not exploit the origin meeting two boundary sides. It also excludes 512, the unique isolated horizontal label of this board.

Write \(I=V_0\cup V_1\cup V_2\). The only selected possible roots of an upward corner at most \(t/3\) are

\[
4,6,8,16,18,27,48,72,81,243.
\]

For these roots, respectively, one missing endpoint is

\[
12,12,24,32,36,54,96,144,162,729.
\]

Therefore no triple \(\{u,2u,3u\}\) lies in \(I\). Roots above \(t/3\) have their triple endpoint outside the board; roots outside \(I\) cannot produce a fully selected corner. This gives a direct integer certificate of independence.

#### Exact deficiencies, not solver estimates

Use the left/right convention

\[
N(u)=(u/3,2u/3),\quad E(u)=(3u/2,u/2),\quad R(u)=(2u,3u)
\]

with their usual divisibility and board-cutoff conditions. The following are valid matchings:

- For \(V_0\): \((2,4),(9,3),(12,18),(16,32),(72,24),(54,81),(96,192),(432,144)\).
- For \(V_1\): \((24,8),(32,48),(108,36),(144,216),(81,162),(486,729)\).
- For \(V_2\): \((6,2),(8,12),(27,9),(36,54),(162,324),(729,243)\).

Each list uses distinct left endpoints and distinct right endpoints. The full graphs have exactly the following numbers of incident vertices on each side, so these matchings meet the immediate bipartite upper bound and certify the exact matching numbers:

| Set | Labels | Left vertices | Right vertices | \(\nu\) | \(d=|V|-\nu\) |
|---|---:|---:|---:|---:|---:|
| \(V_0\) | 5 | 8 | 8 | 8 | \(-3\) |
| \(V_1\) | 4 | 6 | 6 | 6 | \(-2\) |
| \(V_2\) | 4 | 6 | 6 | 6 | \(-2\) |

Adding 1 to \(V_0\) preserves independence because the only new rooted corner would require both 2 and 3, neither selected. It preserves connectivity since 1 and 6 are face adjacent. Its new edge \(R(1)=(2,3)\) introduces no new graph vertex, so the same matching and upper bound give \(\nu=8\), while the label count rises to six. The deficiencies for this version are therefore exactly \((-2,-2,-2)\).

The initial numerical witness used \(\{1,6,8,48,288\}\) in color zero. Adding 27 gives the latter six-label version; removing 1 gives the stronger origin-free version tabulated above. These variants are distinguished so the certificate is not silently attributed to the original solver output.

#### Consequence for the next proof stage

The rejected statement is the purely geometric implication

> Three connected color sets, each meeting both axes and \(u>t/3\), force an upward corner in their union.

It is false even for paths and distinct non-origin axis contacts. Consequently a Sperner/Hex argument using only those properties cannot establish the desired global optimum. The exact counterexample does **not** contain three positive-deficiency sets: every displayed deficiency is negative. It therefore leaves open the stronger obstruction involving inclusion-minimal positive-deficiency sets and their essential-cover constraints.

### Gaps

- No minimum-size claim is made for the counterexample, and the numerical optimizer's optimality status is not used as a proof.
- The relation between three simultaneous positive critical sets and the global finite optimum remains unresolved here. This audit neither proves nor disproves a criticality-dependent topological statement.
- No new vertical-axis proof, broad search, Lean check, historical-priority claim, or external posting was undertaken. Earlier research folders were not edited.
