Your goal is to FULLY SOLVE Erdős #168: determine the limiting maximum density c of subsets of {1,…,N} containing no complete triple {n,2n,3n}, and prove c irrational. Part (i) is working-complete; part (ii) remains unproved. Choose any promising task, group or new approach. Resolve every gap for ONE complete proof; intermediate lemmas are milestones.

Workspace: the original workspace.
Read ERDOS168_PROGRESS.md, tasks/todo.md and tasks/plan.md. Crucially read research_notes/Erdos 168 tail gcd obstruction/codex_review_update.md and research_notes/Erdos 168 half-cleared vertical series/codex_review.md. These corrections govern source claims. Routes are alternatives. Final rigor/novelty review is deferred; check dependency errors.

WORKING RESULTS
The finite optimum and true birth rule η give
M=Σ_(a,b≥0)η_(a,b)2^(−a)3^(−b), c=1−M/3, Z=9c−6=3−3M.
Preserve every low row, isolate/patch correction and exceptional birth (0,1).

For suitable consecutive ACTUAL convergents p/q=p_n/q_n, P/Q=p_(n+1)/q_(n+1) of α=log(2)/log(3), nonresonant currents have p+q≢0 mod 3. Complete correct-side rational models satisfy
D_n=27(2^(3q)−1)(3^(3p)−1), D_nz_n∈ℤ,
D_n|Z−z_n|≤486(1+o(1))2^(5q−Q).
Nonvanishing is proved in six first-mediant classes. Unbounded denominators of convergent rational models are equivalent to infinitely-often nonvanishing.

Let K={n: current nonresonant, next digit a_(n+1)≥5}. Under rational Z=A/B, all sufficiently late n∈K satisfy z_n=Z and B|D_n. The accepted finite certificate gives B>2^56.

REPAIRED MODULAR TOOLS—CONDITIONAL
For each outside prime ell|B, define m_2=ord_ell(2)/gcd(ord_ell(2),3), m_3=ord_ell(3)/gcd(ord_ell(3),3). Put M_B=2·3·7·13·product(m_2 m_3), with product only over ell|B outside {2,3,7,13}.
M8: Prove arbitrarily late actual n∈K with gcd(p_n,M_B)=gcd(q_n,M_B)=1, for every relevant hypothetical B. The proved single-clearer implication then forces B≤4914. Infinite K alone does NOT establish these visits.
M9: Alternatively prove adequate triples beyond every cutoff, with pairwise coprime p coordinates and pairwise coprime q coordinates, plus the exceptional-prime witnesses specified in the review. The proved triple pigeonhole lemma then gives gcd of the three D_n≤4914. Finite observed triples do NOT prove this supply.
M2–M6 remain open: valuation identities do not prove infinite avoidance.

H1–H2 COMPLETED
For L=3q, horizontal periodization retaining the true vertical walk gives
G_n(b)=Σ_(a=0)^(L−1)(1−3η'_(a,b))2^(L−a),
W_n=Σ_(b≥0)G_n(b)3^(−b)−(2^L−1),
(2^L−1)Z=W_n+E_n, |E_n|≤9·2^(2q−Q).
H5 still needs actual infinite nonresonant next-digit-≥2 supply. H3/H6 need, for each fixed B>0, ||BW_n||≥ε_B>0 infinitely often on that same family. The decomposition W_n=2(2^L−1)−3𝒟_n+9ℛ_n leaves uncontrolled cancellation; irrationality of 𝒟_n alone is insufficient.

OTHER OPEN ROUTES
A: Infinite actual adequate supply in a known nonvanishing class, or a proved enlargement with adequate supply.
R: Full resonant clearing cost, effective error, nonvanishing and actual infinite supply together.
O: Affordable clearing of complete positive renewal residuals, or an occupation arithmetic bridge eliminating auxiliary readouts.

Avoid the rejected pair-gcd argument: cross factors invalidate it. Correct even valuations are v_2(D)=v_2(p)+2 and v_3(D)=v_3(q)+5. The single-clearer CF prefix loses accuracy at n=487. Finite scans and LLL searches prove no infinite theorem or universal barrier.

Aim for a complete proof. One sufficient endpoint is d_kz_k∈ℤ and 0<d_k|Z−z_k|→0 on an actual infinite family. Keep hypotheses on the same family, prove new lemmas, and disclose every unresolved step.

Rigorously try to break promising arguments. Leave Lean formalization for later.    Utilize clever and nontrivial techniques from other disciplines of math that wouldn't initially be intuitive. Do not worry about lean or claiming a full solution, i will verify everything. You should make a breakthrough
