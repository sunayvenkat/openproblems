Prove Erdős #168(ii): the limiting maximum density c of subsets of {1,…,N} avoiding every complete triple {n,2n,3n} is irrational.

First read ../PROGRESS.md All paths below are relative to that workspace.

WORKING FOUNDATION
Part (i) is provisionally complete; final rigor/novelty review is deferred. Use its results without unnecessarily repeating that work, but flag suspected dependency errors.

For D_t={2^a3^b≤t}, let τ(t) be the minimum corner-cover size. Color (a,b) by a−b mod 3, with counts K_j. Let I_j indicate a root e=2^A, A≥1, A≡j mod 3, with 2t/3<e≤t; let P_j indicate A≥2 with 6e≤t<27e/4.
τ(t)=min_j(K_j−I_j−P_j) for t≥3; τ(t)=0 below 3.

Write Q_j=K_j−I_j−P_j. At d=2^a3^b≥3, the colors increased by one are, modulo 3:
b=0: none;
b=1,a≤2: a+1,a+2;
b=1,a≥3: a+1;
b=3: a,a+2;
otherwise: a−b.
The true jump η_(a,b)=1 iff every minimizing color of Q(d−) increases. Initially η_(0,0)=η_(1,0)=0, η_(0,1)=1.

M=Ση_(a,b)2^(−a)3^(−b), c=1−M/3, Z=9c−6=3−3M.
In transport notation M=Q_full(0)+1/3 and Z=2−3Q_full(0). Preserve this exceptional-birth correction and all infinite low rows.

Another exact working form is
c=757/972+(2/9)∫₃^∞H(Ŝ(t))t^(−2)dt,
Ŝ=Σ_jQ_jω^j, H(z)=max_j Re(−ω^(−j)z), ω²+ω+1=0.

MAIN GAP
It suffices to construct an actual infinite rational family z_n with positive integer clearers d_n such that
d_n z_n∈ℤ and 0<|d_n(Z−z_n)|→0.
Under rational Z=A/B, multiplying by B gives nonzero integers tending to zero. Other complete contradictions are welcome. Supply, arithmetic cost, error bounds and nonvanishing must hold for the SAME family.

AVAILABLE ROUTES
• Ordered renewal already gives Z=2−3S_R+3Ψ_R for every radius, with rational S_R, Ψ_R>0 and Ψ_R→0. Affordable reduced clearing remains open. This does not rationalize the unrestricted coupled source.
• For suitable consecutive convergents p/q,P/Q of α=log(2)/log(3), nonresonant scalar models have
D=27(2^(3q)−1)(3^(3p)−1), Dz∈ℤ,
D|Z−z|≤486(1+o(1))2^(5q−Q).
Nonvanishing has specific state hypotheses. Infinite actual eligible visits with Q−5q→∞ remain unproved.
• Gauge integrals, carries, source congruences or other architectures may work. A genuine bridge with log(multiplier×amplitude)=o(R^(1/κ)) fits the known exterior decay exp(−γR^(1/κ)), 0<κ<1, γ>0.

AVOID KNOWN FALSE SHORTCUTS
Nonperiodic two-base coefficients need not give an irrational sum. Rational totals do not rationalize boundary readouts. Pure-phase closure does not close joint state/phase observables; retain flux. Killed shifts need not commute. Finite patterns do not prove infinite supply; failed upper bounds are not actual-error lower bounds. Generic shrinking-interval optimization merely gives a condition equivalent to irrationality. Justify any partial-quotient, response-rationality or uniform S-unit hypothesis.

Consult the part-i snapshot; reports/Erdos 168 arithmetic renewal.md and its audits; research_notes/Erdos 168 occupation arithmetic bridge/exact_transport.md; and the numerator/residual and signed-return reports.

Deliver a proof or precise remaining gap, separating working inputs, proved results and conjectural steps. Account for every auxiliary readout and arithmetic cost; additional decimal precision is not the goal.

Rigorously try to break promising arguments. Leave Lean formalization for later.    Utilize clever and nontrivial techniques from other disciplines of math that wouldn't initially be intuitive. Do not worry about lean or claiming a full solution, i will verify everything. You should make a breakthrough
