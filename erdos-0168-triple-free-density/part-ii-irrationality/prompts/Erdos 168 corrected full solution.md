Your goal is to FULLY SOLVE Erdős #168: determine the limiting maximum density c of subsets of {1,…,N} containing no complete triple {n,2n,3n}, and prove c irrational. Part (i) is working-complete; irrationality remains unproved. Choose the most promising task, group, or new approach. Resolve every gap needed for ONE complete proof; intermediate lemmas are milestones, not the final objective.

Workspace: the original workspace.
Read ERDOS168_PROGRESS.md, tasks/todo.md and tasks/plan.md. Read research_notes/Erdos 168 tail gcd obstruction/codex_review.md and research_notes/Erdos 168 half-cleared vertical series/codex_review.md before using their source claims. Follow relevant references. Final comprehensive rigor/novelty review is deferred; investigate dependency errors.

WORKING RESULTS
The finite optimum and true birth rule η give
M=Σ_(a,b≥0)η_(a,b)2^(−a)3^(−b),
c=1−M/3, Z=9c−6=3−3M.
Preserve all low rows, isolate/patch corrections and the exceptional birth (0,1).

For suitable consecutive ACTUAL convergents p/q=p_n/q_n, P/Q=p_(n+1)/q_(n+1) of α=log(2)/log(3), nonresonant currents have p+q≢0 mod 3. Complete correct-side rational models satisfy
D_n=27(2^(3q)−1)(3^(3p)−1), D_nz_n∈ℤ,
D_n|Z−z_n|≤486(1+o(1))2^(5q−Q).
Nonvanishing is proved in six first-mediant classes. For convergent rational models, unbounded denominators are equivalent to infinitely-often nonvanishing. Under rational Z=A/B, sufficiently late nonresonant next-digit-≥5 models equal Z, hence B divides D_n. A finite certificate gives B>2^56.

H1–H2 are working-complete. Periodizing only the horizontal walk while retaining the true vertical walk gives L=3q,
G_n(b)=Σ_(a=0)^(L−1)(1−3η'_(a,b))2^(L−a),
W_n=Σ_(b≥0)G_n(b)3^(−b)−(2^L−1),
(2^L−1)Z=W_n+E_n, |E_n|≤9·2^(2q−Q).
The error tends to zero on any infinite applicable nonresonant next-digit-≥2 family; that family's existence is NOT implied by transcendence. The identity W_n=2(2^L−1)−3𝒟_n+9ℛ_n leaves an uncontrolled infinite remainder. Irrationality of 𝒟_n alone does not prevent cancellation.

REJECTED CLAIMS—DO NOT REUSE
M2–M7 remain OPEN. Coordinate coprimality does not bound the full clearer gcd: cross factors were omitted. Actual consecutive convergents 5/8 and 12/19 have gcd(D(5,8),D(12,19))=24570>4914.
Correct even-case valuations are v_2(D)=v_2(p)+2 and v_3(D)=v_3(q)+5; the manuscript's +3 and +4 are wrong.
The verifier swaps p and q, scans only bounded primes/cutoffs, and does not compute the full gcd. Finite checks cannot certify every late tail. Residue-tail classification does not guarantee large resonant digits or determine α's actual branch.

OPEN CHOICES
A: Prove infinite actual adequate supply in a known nonvanishing class, or enlarge the class and establish supply there.
M: Prove adequate supply plus a small gcd in EVERY sufficiently late adequate tail, or the checklist's primewise nonpersistence conditions.
H: Establish actual infinite supply and, for each fixed B>0, ||BW_n||≥ε_B>0 infinitely often on that same family.
R: Fit complete resonant clearing cost, effective error, nonvanishing and actual infinite supply together.
O: Clear complete positive renewal residuals affordably, or construct an occupation arithmetic bridge eliminating auxiliary readouts.

A sufficient finish is d_kz_k∈ℤ and 0<d_k|Z−z_k|→0 on an actual infinite family; rational Z would give nonzero integers tending to zero. Other rigorous contradictions are welcome. Pursue the chosen path to a complete proof. Keep hypotheses on the same actual family, prove new lemmas, and expose any remaining unproved step. Never label conditional or numerical evidence an unconditional solution.

Rigorously try to break promising arguments. Leave Lean formalization for later.    Utilize clever and nontrivial techniques from other disciplines of math that wouldn't initially be intuitive. Do not worry about lean or claiming a full solution, i will verify everything. You should make a breakthrough
