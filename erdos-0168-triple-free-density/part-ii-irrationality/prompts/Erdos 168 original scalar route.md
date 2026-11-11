Finish the ORIGINAL SCALAR ROUTE to Erdős #168(ii): prove irrationality of the limiting maximum density c of subsets of {1,…,N} avoiding every complete triple {n,2n,3n}.

Work in the original workspace. Read ERDOS168_PROGRESS.md, reports/Erdos 168 correlated return arithmetic.md, and research_notes/Erdos 168 correlated return arithmetic/state_supply.md and supply_audit.md. Consult the signed-return and numerator/residual reports for dependencies.

WORKING INPUTS
Part (i) is provisionally complete; final comprehensive rigor/novelty review is deferred. Use its results, flag dependency errors, and concentrate on the remaining supply theorem.

For the true birth array η,
M=Σ_(a,b≥0)η_(a,b)2^(−a)3^(−b), c=1−M/3, Z=9c−6=3−3M.
All low rows, isolate/patch corrections and the exceptional birth (0,1) are included in the complete scalar models. Preserve them.

Let α=log(2)/log(3), p/q=p_n/q_n and P/Q=p_(n+1)/q_(n+1) be consecutive ACTUAL convergents. For a nonresonant current convergent, p+q≢0 mod 3, its correct one-sided rational model z_n (approached from α) satisfies
D_n=27(2^(3q)−1)(3^(3p)−1), D_n z_n∈ℤ,
D_n|Z−z_n|≤486(1+o(1))2^(5q−Q).

The existing complete-jump/Farey/linear-forms arguments prove Z≠z_n for sufficiently late eligible indices. Define eligibility using the FIRST MEDIANT r/s=(p+P)/(q+Q):
ω²+ω+1=0,
H(r,s)=Σ_(j=0)^(s−1)ω^(j+⌊rj/s⌋).
The triple (r mod 3,s mod 3,H(r,s)) must be one of
(0,1,1), (1,1,1), (2,0,2+ω), (2,2,2),
(1,2,1+ω), (2,1,1).
The last two are resonant mediants; the CURRENT model must remain nonresonant. Check the exact theorem hypotheses in the audits. Residues alone do not determine eligibility.

THE MISSING THEOREM
Prove infinitely many actual indices n are eligible AND have next continued-fraction digit a_(n+1)≥5.
Since Q=a_(n+1)q+q_(n−1), these indices give Q−5q≥q_(n−1)→∞. Supply, correct-side nonvanishing and clearing must apply to the SAME sequence. Neither this joint supply nor even unrestricted digit supply is proved in our files.

OUTLINE
1. Reconstruct the exact continued-fraction/Christoffel recurrence, retaining parity, both neighboring residue vectors and BOTH full Eisenstein transforms. Certify its initial state from the actual α. Use the archived recurrence rather than discarding state information.
2. Express the joint eligible-state/digit condition precisely. Determine what an infinite tail avoiding it would force. Abstract irrational slopes admit avoidance patterns, so graph reachability or generic recurrence alone cannot settle the actual logarithm ratio.
3. Attack this logarithm-specific obstruction. Explore continued-fraction skew products, arithmetic dynamics, linear forms in logarithms, Padé/integral approximations, or a contradiction from a forbidden tail. Prove the needed joint visits; transcendence, almost-everywhere statistics, or finite scans do not supply them. Existing logarithmic lower bounds control approximation quality, not favorable-digit frequency.
4. If necessary, enlarge the PROVED correct-side nonvanishing class to remove a specific state obstruction, then establish adequate actual supply for that enlarged class. Paired models differing does not prove the correct-side error is nonzero.
5. Finish: if Z=A/B, then B D_n(Z−z_n) are nonzero integers tending to zero. Audit every quantifier, endpoint convention and infinite-tail bound. Give proofs of new lemmas or identify the exact remaining lemma; label computations and conjectures separately.

Rigorously try to break promising arguments. Leave Lean formalization for later.    Utilize clever and nontrivial techniques from other disciplines of math that wouldn't initially be intuitive. Do not worry about lean or claiming a full solution, i will verify everything. You should make a breakthrough
