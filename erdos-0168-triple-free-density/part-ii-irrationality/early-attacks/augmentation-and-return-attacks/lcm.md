# Erdős #269: exact boundary recursion and the arithmetic return interface

Research round of 7 November 2026 UTC (6 November local time). The repeated running-LCM series is retained throughout. The results below do not solve the universal irrationality target. New derivations are presented with proofs, without a priority claim; previously known two-prime results and Cook's existing obstructions are identified as such.

## What is the current target, and do existing value theorems already apply?

### Takeaway

The universal finite-prime irrationality target is still marked open in the current primary formal source, and Cook's current manuscript explicitly leaves the repeated series unresolved for three or more primes. Neither a quadratic-slope Hecke–Mahler theorem nor a general multivariate Mahler theorem applies to the present representation without substantial additional work.

### Cited Findings

* The target quantifies over every finite prime set of cardinality at least two. Its formal series includes the empty-prefix term; subtracting that rational term gives the series studied here. The source marks the irrationality variant `research open`. [Current primary formal statement, lines 42–73](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/269.lean).
* Cook distinguishes the repeated sum from the distinct-denominator sum, records the already settled two-prime case, and explicitly leaves the repeated sum open for at least three primes. His Theorem 16 proves arbitrary-order nonzero minors of the three-prime kernel, ruling out finite separation of one exponent from the others. It does not concern identities after summation. [Current primary manuscript](https://github.com/wcook04/plectis-erdos/blob/main/docs/papers/full-text/erdos-269-three-prime-running-lcm.md).
* Cook's reasoning surface already explains why moving boundary terms defeat a scalar finite-difference shortcut even when there are no floor crossings. Its weighted count is not simply a polynomial evaluated at one floor. This note does not repeat the old cubic counterexample as a new result. [Primary reasoning surface, weighted-difference and unresolved-question sections](https://github.com/wcook04/plectis-erdos/blob/main/docs/papers/full-text/erdos269-running-lcm-reasoning-surface.md).
* Pellarin's Theorem 1.1 concerns a quadratic irrational slope, algebraic evaluation points in the convergence domain, and a rank-one condition on their quadratic-order monomial orbits up to torsion. Under those conditions, its algebraic-independence criterion uses specified auxiliary formal series. This is not a theorem about arbitrary higher-dimensional floor kernels. [Pellarin, published primary paper, pp. 330–332](https://www.numdam.org/item/ASNSP_2006_5_5_3_329_0.pdf).
* Adamczewski–Faverjon's multivariate lifting theorem starts with convergent algebraic-coefficient power series \(\mathbf f(Tz)=A(z)\mathbf f(z)\), with \(T\) a nonnegative integer matrix and \(A\) invertible over the algebraic rational-function field. An algebraic point \(\alpha\) must be regular along its orbit. Admissibility requires exponential growth control for \(T^j\), matching exponential decay of \(T^j\alpha\), and nonvanishing infinitely often along that orbit for every nonzero convergent analytic germ. Under these hypotheses, Corollary 3.5 equates the transcendence degrees of the functions and their values. [Primary author manuscript, Definitions 3.1–3.2 and 5.1, Theorem 3.3, Corollary 3.5; printed pp. 8–10, 18](https://faverjon.perso.math.cnrs.fr/AdamczewskiFaverjon_MahlerFiniteAutomata.pdf).

Source record: the two Cook files were fetched directly through the GitHub connector in this round. Their file-blob SHAs were respectively `00be5ed7dc29e5edfe38c54c16de6e6c7abc47a5` and `5e3e59d85cd2a5a9544d08797def000137a24c22`. These identify file contents, not repository commits. The formal source and the two original value-theorem papers were fetched directly in this round. No Lean checks were run.

### Inferences

Fix a finite prime set \(P\), let \(k=|P|\ge2\), and let \(\mathcal S_A\) denote the positive integers supported on a subset \(A\subseteq P\), including one. Define

\[
H_P(x)=\prod_{p\in P}p^{\lfloor\log_p x\rfloor}\quad(x\ge1),
\qquad R_P=\sum_{s\in\mathcal S_P}\frac1{H_P(s)}.
\]

This is the repeated running-LCM sum. Indeed, every P-smooth integer at most \(x\) divides \(H_P(x)\), while the prefix contains the largest power of each prime at most \(x\). Each smooth integer contributes a summand even when its denominator equals that of a preceding integer. This also verifies directly the interpretation recorded by Cook.

The phase variable introduced below is a real logarithmic translation, not an algebraic variable of an already constructed Mahler system. Neither a multivariate sum nor a finite set of denominator primes supplies the analytic system and admissible algebraic evaluation point required above. No such representation is constructed here.

The independence of \(1,\log_q p_1,\ldots,\log_q p_r\), for distinct primes \(q,p_i\), follows by multiplying a rational relation by \(\log q\) and using prime factorization. This does **not** establish independence of \(1,\log_{p_1}q,\ldots,\log_{p_r}q\). No assertion of full torus equidistribution for those reciprocal ratios is used below. The proofs need only the irrationality of each individual ratio of logarithms of distinct primes.

### Gaps

The [live conjectures.io page](https://conjectures.io/problems/erdos269-erdos-269-variants-irrational) could not be fetched in this round. Its prior saved status is not presented as a fresh live verification; the fresh status evidence is the formal source and Cook's explicit statement. No general repeated-series irrationality proof, counterexample, or applicable higher-dimensional value-theorem representation was found. Nonlinear identities of the scalar value remain possible and unconstructed.

## Can exact exponent translations recursively cancel every boundary face?

### Takeaway

There is an exact recursion that removes one summation direction at a time, but it retains the full denominator kernel. That kernel, and even the already summed repeated phase function, has linearly independent finite families of distinct P-unit logarithmic translates. Hence no nonzero constant-coefficient translation polynomial annihilates either function on a late half-line.

### Cited Findings

Cook's established infinite-rank theorem concerns separation of the pointwise exponent kernel. The result proved below instead concerns real logarithmic translations, and its corollary applies after summation. This distinguishes the mechanism being excluded without claiming priority or claiming that all scalar identities are excluded. [Cook, Theorem 16 and the paragraph following its approximation discussion](https://github.com/wcook04/plectis-erdos/blob/main/docs/papers/full-text/erdos-269-three-prime-running-lcm.md).

### Inferences

All statements in this subsection are derived here from the displayed definitions and elementary prime factorization.

**1. The exact boundary recursion.** For \(t\ge0\), set

\[
w_P(t)=H_P(e^t)^{-1},\qquad
F_{P,A}(t)=\sum_{s\in\mathcal S_A}w_P(t+\log s),\qquad
\mathcal R_P(t)=F_{P,P}(t).
\]

Then \(F_{P,\varnothing}=w_P\) and \(\mathcal R_P(0)=R_P\). If \(C_P=\prod_{p\in P}p\), the floor bounds give

\[
e^{-kt}\le w_P(t)\le C_Pe^{-kt},
\qquad
F_{P,A}(t)\le C_Pe^{-kt}
       \prod_{q\in A}(1-q^{-k})^{-1}.\tag{1}
\]

Thus the series converge absolutely, uniformly on \(t\ge0\). Let \(T_hf(t)=f(t+h)\). Splitting the q-exponent into zero and positive values, then reindexing the positive part, gives for every \(q\in A\)

\[
\boxed{(I-T_{\log q})F_{P,A}=F_{P,A\setminus\{q\}}.}\tag{2}
\]

All translations commute. Consequently

\[
\boxed{\prod_{q\in A}(I-T_{\log q})F_{P,A}=w_P.}\tag{3}
\]

This cancellation is exact and preserves multiplicities. Its endpoint is the ambient kernel \(w_P\), not a constant or a smaller-prime repeated sum.

**Why deleting a direction is not deleting a denominator prime.** For \(P=\{2,3,5\}\), \(A=\{2,3\}\), the A-smooth integer \(s=6\) contributes \(1/H_P(6)=1/60\) to the boundary family, whereas \(1/H_A(6)=1/12\). At \(s=1\) both kernels equal one, so no constant multiple identifies these two kernels on all A-smooth integers. More generally, (1) gives \(F_{P,A}(t)\asymp e^{-|P|t}\), while \(F_{A,A}(t)\asymp e^{-|A|t}\) for nonempty proper \(A\). Their ratio tends to zero; they cannot be nonzero constant multiples as phase functions. This does not exclude a more complicated relation at \(t=0\).

**2. A finite quotient alphabet forces periodicity under a recurrence.** Let \(a_n>0\) and suppose the quotients \(r_n=a_{n+1}/a_n\) lie in a fixed finite set. If \(a_n\) satisfies any nontrivial eventual constant-coefficient linear recurrence with real coefficients, then \(r_n\) is eventually periodic.

Proof: delete leading and trailing zero coefficients and shift the starting index to write

\[
\sum_{j=0}^{M}c_ja_{n+j}=0\quad(n\ge N),\qquad c_0c_M\ne0.
\]

The case \(M=0\) is impossible because \(a_n>0\). For \(M=1\), the quotient is constant. For \(M\ge2\), divide by \(a_{n+M-1}\) to obtain

\[
c_M r_{n+M-1}+c_{M-1}
 +\sum_{j=0}^{M-2}\frac{c_j}{r_{n+j}\cdots r_{n+M-2}}=0.\tag{4}
\]

The next quotient is uniquely determined by the preceding \(M-1\) quotients. There are finitely many such states, so the actual eventual state sequence is deterministic on a finite set and must eventually cycle. No rationality of the \(c_j\) is needed. \(\square\)

**3. Prime-power kernel samples admit no such recurrence.** Fix \(p\in P\), and put \(\kappa_n=w_P(n\log p)=H_P(p^n)^{-1}\) for \(n\ge0\). With \(\alpha_q=\log_q p\),

\[
\frac{\kappa_{n+1}}{\kappa_n}
=p^{-1}\prod_{q\in P\setminus\{p\}}
q^{-\delta_q(n)},\qquad
\delta_q(n)=\lfloor(n+1)\alpha_q\rfloor-\lfloor n\alpha_q\rfloor.
\tag{5}
\]

Each \(\delta_q(n)\) belongs to \(\{\lfloor\alpha_q\rfloor,\lceil\alpha_q\rceil\}\), so the quotient alphabet is finite. If \(\kappa_n\) satisfied a nonzero eventual recurrence, Step 2 would make these quotients eventually periodic. Unique prime factorization then makes every integer word \(\delta_q(n)\) eventually periodic. Its mean would be rational: the sum over one period divided by the period length. On the other hand, telescoping (5) gives

\[
\lim_{N\to\infty}\frac1N\sum_{n=0}^{N-1}\delta_q(n)=\alpha_q,
\]

which is irrational for any \(q\ne p\). Since \(|P|\ge2\), such a prime exists. This contradiction proves that \(\kappa_n\) has no nontrivial eventual constant-coefficient recurrence, including recurrences with real coefficients. \(\square\)

**4. Independence of the kernel translates.** For an integer exponent vector \(v=(v_q)_{q\in P}\), write \(s_v=\sum_qv_q\log q\). Distinct vectors give distinct real shifts. For any finite set of distinct vectors \(V\subset\mathbb Z^P\),

\[
\sum_{v\in V}c_vw_P(t+s_v)=0
\quad\hbox{for every sufficiently large }t
\quad\Longrightarrow\quad c_v=0\text{ for every }v,
\tag{6}
\]

where the coefficients \(c_v\) may be arbitrary real numbers. All shifted arguments are nonnegative once \(t\) is sufficiently large.

Proof: fix one prime \(p\in P\). At \(t=n\log p>0\), no other prime jumps, and the right-continuous function \(w_P\) has jump

\[
w_P(n\log p)-w_P(n\log p-)=-(p-1)\kappa_n.\tag{7}
\]

Partition \(V\) into p-fibers: two exponent vectors lie in the same fiber if they agree away from the p-coordinate. In a fiber choose a representative \(v_0\); its vectors have the form \(v_0+me_p\) for finitely many integers \(m\). At the common p-jump time \(t=n\log p-s_{v_0}\), their jumps are \(-(p-1)\kappa_{n+m}\).

Different p-fibers never share a p-jump. A p-jump of one translate can coincide with a q-jump of another, for \(q\ne p\), only if

\[
n e_p-v=m e_q-u.
\]

For each fixed pair \((v,u)\) and distinct primes \((p,q)\), this determines at most one pair of integers \((n,m)\), by comparing exponent coordinates. Since only finitely many translates occur, all cross-prime coincidences are absent at sufficiently late times. Possible jumps where a shifted argument is zero are likewise finite and irrelevant.

Taking the jump of (6) at the remaining p-jump times gives, for every sufficiently large integer \(n\),

\[
\sum_{m:\,v_0+me_p\in V}c_{v_0+me_p}\kappa_{n+m}=0.
\]

After shifting the index and deleting zero end coefficients, any nonzero fiber would give the recurrence excluded in Step 3. Every coefficient in every fiber therefore vanishes. \(\square\)

**5. Independence survives the full repeated summation.** The same conclusion (6) holds with \(w_P\) replaced by \(\mathcal R_P\), and indeed by any \(F_{P,A}\). To prove it, apply the commuting operator \(\prod_{q\in A}(I-T_{\log q})\) to an assumed eventual translate relation. Equation (3) yields exactly the same relation for \(w_P\), contradicting Step 4. Only positive additional shifts are applied, so an identity on a late half-line remains valid there.

Equivalently, no nonzero Laurent polynomial with real coefficients in the translations \(T_{\log p}\), \(p\in P\), annihilates any \(F_{P,A}\) eventually. In particular, these functions cannot belong to a finite-dimensional space of eventual functions invariant under even one of the prime translations: the consecutive translates in such a space would be linearly dependent.

Thus the finite family of all boundary sums indexed by \(A\subseteq P\) does not close under all translations. Formula (2) controls a translation by \(q\) when \(q\in A\); the missing cases \(q\notin A\) cannot all be repaired by adjoining finitely many functions in a constant-coefficient translation-invariant system.

### Gaps

This is an obstruction to an exact, homogeneous, constant-coefficient linear translation mechanism, not an irrationality proof for \(R_P=\mathcal R_P(0)\). It does not exclude nonlinear scalar identities, phase-dependent coefficients, a different analytic representation, or sparse approximate return relations.

The nonlinear loophole is concrete even for the kernel. For fixed \(p\), the quotient \(w_P(t+\log p)/w_P(t)\) belongs to a finite rational set \(\mathcal A_p\), by the same floor-increment calculation as (5). Consequently

\[
\prod_{r\in\mathcal A_p}\bigl(w_P(t+\log p)-r w_P(t)\bigr)=0
\]

identically. This branch-switching relation between discontinuous functions does not survive summation automatically and supplies no admissible Mahler value theorem. No useful nonlinear relation for the scalar repeated sum is established.

## What arithmetic compression would now suffice?

### Takeaway

Fixed coefficients are unnecessarily restrictive: a fixed number of S-unit terms with subexponential integer coefficients is enough for the KK-style lower-bound contradiction. The unsolved task is to produce those finitely many grouped terms with an exponentially smaller nonzero error, not to force their coefficients into a finite alphabet.

### Cited Findings

The one-form Subspace Theorem holds for any fixed finite set of places, not just the two denominator primes in a particular application. [Luca–Ouaknine–Worrell, Theorem 1](https://arxiv.org/html/2412.07908v2#S2.Thmtheorem1). The full derived extension, with constants and exceptional-hyperplane induction checked explicitly, is in [coefficient_extension.md](<coefficient_extension.md>).

### Inferences

For fixed \(m,S,d_i\in\mathbb Q\) and any \(\epsilon>0\), the companion proof gives a constant \(C>0\) independent of \(B\), the integer coefficients \(c_i\), the positive S-units \(u_i\), and \(N\in\mathbb Z\), such that

\[
0<t\le\min(1,u_1,\ldots,u_m),\quad |c_i|\le B,\quad
E=\sum_{i=1}^m d_ic_iu_i-N\ne0
\]

imply

\[
\boxed{|E|\ge CtB^{-m-\epsilon}
 H(N:u_1:\cdots:u_m)^{-\epsilon}.}\tag{8}
\]

Zeros and signs among the integer coefficients are allowed. The proof first handles S-integers \(x_i\) with \(|x_i|\prod_{p\in S}|x_i|_p\le B\), with loss \(B^{-m}\), and then substitutes \(x_i=c_iu_i\). The projective height increases by at most a factor \(B\), since integer coordinate multipliers contract every nonarchimedean local maximum.

Therefore a valid irrationality argument could still use polynomial multiplicities produced by a boundary-face summation. It would suffice, after assuming rationality, to derive along unbounded scales \(L\) a relation with:

* a fixed number \(m\) of grouped S-unit terms;
* coefficient sizes \(B_L=e^{o(L)}\) and height at most \(e^{C_0L}\);
* a common lower scale \(0<t_L\le\min(1,u_{i,L})\);
* a nonzero remainder \(0<|E_L|\le t_Le^{-\eta L}\), with fixed \(\eta>0\).

Choosing \(\epsilon\) with \(C_0\epsilon<\eta\) contradicts (8). This is a proved conditional interface, not evidence that the displayed hypotheses hold for #269. The exact boundary recursion (2) alone gives no such error estimate; the independence theorem only rules out replacing it by a finite exact homogeneous translation closure.

### Gaps

No bounded-term compression with the stated saving and nonvanishing has been proved for the repeated series with three or more primes. Neither a dense set of weighted boundary terms nor polynomial bounds on their individual sizes establish it. No decimal calculations, broad numerical sweeps, new dependencies, external posts, or new formalization were used in this round. The full open target remains unresolved.
