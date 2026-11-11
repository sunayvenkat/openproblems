# Erdos 168 remaining proof checklist

Updated 2026-11-09. Part (ii) remains unproved. Complete ONE route below, then the shared final checks. The routes are alternatives, not a list of cumulative requirements. A direct proof of a route's endpoint may replace its suggested sublemmas.

Use [the roadmap](<PROGRESS.md>) for definitions and accepted dependencies, and [the research plan](<plan.md>) for the route map. For an LLM handoff, assign one task ID and request its precise lemma, proof and dependencies. An exact counterexample to that lemma is useful progress; a finite supporting scan does not complete an infinite task.

## Available inputs — do not re-prove during ordinary gap work

- The finite optimum, true birth rule and density reduction are working-complete: c=1-M/3 and Z=9c-6=3-3M.
- Complete nonresonant scalar models, their integer clearers and full error estimates are available. Low rows, isolated/patch corrections and the exceptional birth must be retained.
- Correct-side nonvanishing is proved for sufficiently late indices in the six known first-mediant classes.
- For convergent rational models, unbounded denominators are equivalent to infinitely-often nonvanishing.
- The resonant-mediant eligibility test is a pure residue condition; the balanced test also uses full Eisenstein transforms.
- Under rational Z=A/B, every sufficiently late adequate nonresonant model equals Z, so B divides its nominal clearer. The new modular obstruction theorem is proved conditional on its supply assumptions.
- Ordered renewal gives a rational complete source and a positive residual tending to zero. An infinite positive occupation family with a real tail estimate is also available.

These remain inputs for the final comprehensive audit, not claims of external certification or novelty. The numerical denominator exclusions and giant partial quotient are finite evidence, not an irrationality proof.

## Notation and common finish condition

Let alpha=log(2)/log(3), p/q=p_n/q_n and P/Q=p_(n+1)/q_(n+1) be actual consecutive convergents, with next digit a_(n+1). Put sigma_n=p_n+q_n modulo three and
\[
D_n=27(2^{3q_n}-1)(3^{3p_n}-1).
\]
For suitable nonresonant currents, sigma_n!=0,
\[
D_nz_n\in\mathbb Z,\qquad
D_n|Z-z_n|\le486(1+o(1))2^{5q_n-q_{n+1}}.
\]
The correct-side model is the one-sided limit toward alpha. All numerical and analytic conditions must refer to that same value.

One sufficient general endpoint is an actual infinite sequence with d_kz_k integral and 0<d_k|Z-z_k|->0. Under rational Z=A/B, B*d_k*(Z-z_k) would be a nonzero integer tending to zero. Routes M and H give equivalent rationality contradictions without separately proving each model error nonzero.

Tasks marked **research** isolate unproved mathematics, sometimes a major open infinite-visit problem. Splitting them does not make them routine. Tasks marked **technical** or **assembly** still require a proof, but use already identified objects and estimates.

## Route A — adequate supply in a known nonvanishing class

Source: [scalar supply note](<investigations/scalar-supply-barrier/supply_barrier.md>) and the roadmap's exact L_E, L_* and L_B statements.

- [ ] **A1 — Prove actual adequate nonresonant supply. [research]** Show that K={n:sigma_n!=0, a_(n+1)>=5} is infinite. Done when a theorem specific to the actual alpha supplies arbitrarily large such n. Transcendence, generic Gauss-map statistics and the finite 125-index prefix do not complete this task. Dependencies: working continued-fraction identities only. A direct proof of A2 already includes A1.

- [ ] **A2 — Synchronize that supply with known nonvanishing. [research]** Prove infinitely many n in K satisfy sigma_n+sigma_(n+1)=0 modulo three (L_*), OR have their first-mediant state in the four balanced classes (L_B). Done when the actual joint visits are proved, retaining the full transform in the balanced branch. Dependencies: A1 if proved separately; the existing eligibility classification. A proof of either sufficient branch closes the research gap for this route.

- [ ] **A3 — Assemble the existing scalar contradiction. [assembly]** Extract an increasing sequence from A2, discard its finite initial exceptions, and apply the already proved nonvanishing and clearing/error estimates. Verify q_(n+1)-5q_n>=q_(n-1)->infinity on that sequence and explicitly obtain nonzero integer-cleared errors tending to zero. Dependencies: A2. No new primitive-prime or denominator-growth theorem is required.

### Optional replacement for A2 — enlarge the analytic domain

Use this branch only if it makes actual supply easier. Do not redo the six already covered states.

- [ ] **A4 — Specify one additional state family exactly. [technical/research]** Define its residues, full transforms, orientation and matching-prefix hypotheses, including any unbounded parameter. Done when membership is a precise mathematical predicate and the complete paired-jump quotient is defined on it. Dependencies: accepted state and jump formulas.

- [ ] **A5 — Prove a full jump lower bound for that family. [research]** Bound the complete quotient away from zero, with its entire exterior and parameter dependence controlled. A finite table suffices only for a genuinely finite state family with a proved uniform tail bound. Dependencies: A4. Paired-model inequality alone does not finish nonvanishing of the correct-side error.

- [ ] **A6 — Prove correct-side nonvanishing in the enlarged family. [research]** Show the A5 jump dominates the sum of every remaining crossed jump in the relevant Farey intervals, on the required old-q scale. Done when Z!=z_n follows uniformly for sufficiently late applicable indices. Dependencies: A5 and the complete variation estimate.

- [ ] **A7 — Prove infinite actual adequate supply in the enlarged family. [research]** Supply infinitely many n in K satisfying A4–A6. Dependencies: A4–A6, and A1 if obtained separately. Then use A3 with this new class.

## Route M — modular obstruction to a rational target denominator

Source: [cheap-clearer note, Section 8](<investigations/cheap-clearer-search/notes.md>), [Single-Clearer Obstruction note](<investigations/tail-gcd-obstruction/notes.md>), and `verify_single_clearer_obstruction.py`. Use the correct convergent initialization ($p_0=0, q_0=1, p_1=1, q_1=1$).

Under hypothetical rationality $Z=A/B$, Lemma 8.1 proves that $B \mid D_n$ for every sufficiently late adequate nonresonant convergent $n \in K = \{n : \sigma_n \ne 0, a_{n+1} \ge 5\}$. The Single-Clearer Divisibility Obstruction (Theorem 1, 2026-11-10) proves that for the fixed integer modulus $M_B = 2 \cdot 3 \cdot 7 \cdot 13 \prod_{\ell \mid B,\ \ell\notin\{2,3,7,13\}} m_2(\ell) m_3(\ell)$, any convergent $n \in K$ beyond $N_0(B)$ with $\gcd(p_n, M_B) = \gcd(q_n, M_B) = 1$ forces $\gcd(B, D_n) \le 4914$, contradicting $B \ge 2^{150990}$. This eliminates cross-factors by evaluating divisibility at a single clearer.

- [ ] **M1 — Establish infinite actual K. [research]** Prove infinitely many actual nonresonant indices have next digit at least five. Coprime-locus recurrence is a separate stronger obligation in M8; infinitude alone does not supply it.

- [ ] **M2 — Bound the persistent power of two. [research]** Prove v_2(D_n)<=1 infinitely often on K. The corrected conditional valuation formula is proved; infinitely many odd p_n on K remain unproved.

- [ ] **M3 — Bound the persistent power of three. [research]** Prove v_3(D_n)<=3 infinitely often on K. The corrected formula is available; actual infinitely many odd q_n remain unproved.

- [ ] **M4 — Bound the persistent power of seven. [research]** Prove v_7(D_n)<=2 infinitely often on K. A conditional valuation identity is not a proof of these visits.

- [ ] **M5 — Bound the persistent power of thirteen. [research]** Prove v_13(D_n)<=2 infinitely often on K. Actual infinite visits remain missing.

- [ ] **M6 — Exclude every other persistent prime. [research]** For each fixed outside prime ell, prove ell does not divide D_n infinitely often on K. The order criterion is established but its actual avoidance is not.

- [ ] **M7 — Assemble the modular contradiction. [assembly]** Apply M2–M6, or the alternative M8 or M9 theorem, beyond the rationality-dependent cutoff. The conditional integer/divisibility deduction is ready; its actual infinite hypotheses are not.

### Alternative modular supply targets

- [ ] **M8 — Prove arbitrarily late coprime-locus visits. [research]** For every relevant fixed modulus M (it suffices to handle every hypothetical M_B), prove arbitrarily late actual n in K with gcd(p_n,M)=gcd(q_n,M)=1. The accepted single-clearer theorem then bypasses separate M2–M6 proofs. This is stronger than M1 and is not established by finite statistics.

- [ ] **M9 — Prove arbitrarily late adequate triples. [research]** Beyond every cutoff, construct three actual indices in K with pairwise coprime p coordinates and pairwise coprime q coordinates, plus the exceptional-prime witnesses in the updated review. The proved conditional triple lemma bounds their gcd by 4914. Seven tested cutoffs do not finish this task. Completing M9 supplies M1 and an alternative to M2–M6.

## Route R — use resonant CURRENT models

These are different from Route A's resonant MEDIANTS. Complete rational cone models already exist; another derivation of their bare diagonal denominator does not close this route.

- [ ] **R1 — Bound the full reduced clearing cost. [research]** On an explicitly specified actual resonant family, prove a usable upper bound for log_2 den(z_n), including every power of two and three caused by finite heads/intercepts and low rows. Done when the cost is quantitative enough to compare with an error exponent. Dependencies: accepted complete cone formula and its denominator classification.

- [ ] **R2 — Prove the effective error bound. [research]** Give a rigorous upper bound |Z-z_n|<=2^(-E_n) for the same complete models. If using deep states, show actual birth agreement, not just floor agreement, and charge both infinite exteriors. The observed R-EW behavior is not an input theorem. Dependencies: exact model and state rules; R1 need not be solved first.

- [ ] **R3 — Prove nonvanishing on that family. [research]** Establish Z!=z_n for infinitely many selected actual resonant currents. A certificate at 665/1054 alone does not finish this task. Dependencies: complete model identity, a full sign/jump comparison or another argument.

- [ ] **R4 — Prove an adequate infinite intersection. [research]** Show the same actual indices satisfy E_n-log_2 den(z_n)->infinity and R3. This needs explicit control of the full cost/error difference, not only separate O(q) and effective-window statements. Dependencies: R1–R3 and actual supply.

- [ ] **R5 — Apply the integer contradiction. [assembly]** Use the reduced denominators on R4's sequence. Dependencies: R4.

## Route H — make the proposed half-cleared identity usable

H1–H2 are now working-complete from Antigravity's written definitions and full-tail proof; see the half-cleared series integration review. The supplied numerical script is a consistency check, not an exact infinite-tail certificate. H3 remains the research gap.

- [x] **H1 — Define the complete horizontal hybrid. [technical]** (Completed 2026-11-09, see [notes.md](<investigations/half-cleared-vertical-series/notes.md>)). Complete definition of W_n = sum_{b>=0} G_n(b) 3^{-b} - (2^L - 1) with L = 3q_n, where G_n(b) = sum_{a=0}^{L-1} (1 - 3 eta'_{a,b}) 2^{L-a} in Z, retaining all low rows b=0,1,2,3, true vertical walk B_b and events E_b, L-periodic horizontal model A'_a, and the exact Z = 3 - 3M = 2 - 3Q_full(0) normalization with the exceptional birth (0,1) shifted into -(2^L-1).

- [x] **H2 — Prove a uniform half-cleared error bound. [technical]** (Completed 2026-11-09, see [notes.md](<investigations/half-cleared-vertical-series/notes.md>)). Proved (2^(3q_n)-1)Z = W_n + E_n with the explicit uniform bound |E_n| <= 9 * 2^{2q_n - q_{n+1}}, using exact agreement A_a = A'_a below the Farey window W = q_n + q_{n+1} and geometric tail summation. Numerically checked, with an uncertified truncated exterior, in verify.py with ratio |E_n|/bound ~ 0.119. On any nonresonant convergent with a_{n+1} >= 2, 2q_n - q_{n+1} <= -q_{n-1} -> -infinity, giving E_n -> 0 exponentially fast. Under rationality Z = A/B, ||B W_n|| <= 9B * 2^{2q_n - q_{n+1}} -> 0.

- [ ] **H3 — Prove arithmetic separation on actual returns. [research]** For every fixed positive integer B, prove there is epsilon_B>0 and an infinite actual nonresonant family with next digit at least two and ||B W_n||>=epsilon_B while E_n->0. Dependencies: H1–H2 and a proof of the actual joint supply. Carries or individual irrational readouts do not establish separation of the complete series.

- [ ] **H4 — Contradict rationality. [assembly]** If Z=A/B, H2 gives ||B W_n||<=B|E_n|->0, contradicting H3. Dependencies: H3.

### Subtargets toward H3

- [ ] **H5 — Prove actual infinite supply for the half-cleared route. [research]** Prove infinitely many actual nonresonant indices have next digit at least two, or directly construct the infinite family required in H3. Transcendence alone does not supply these indices. Dependencies: the actual continued-fraction orbit; H1–H2 give decay once supply is established.

- [ ] **H6 — Control cancellation in the complete vertical series. [research]** Starting from W_n=2(2^L-1)-3*mathcal D_n+9*mathcal R_n, either obtain useful arithmetic control of mathcal R_n or analyze the combined series directly. Done when, for each fixed B, a positive separation bound for the full ||B W_n|| holds infinitely often on H5's actual family. Digit congruences, finite frequencies or irrationality of mathcal D_n alone do not suffice. Dependencies: H1, H5 for the joint infinite conclusion. A proof of H6 with this quantification completes H3; then apply H4.

## Route O — exploit an already positive residual

Source: the complete ordered renewal and occupation reports linked in the roadmap.

- [ ] **O1 — Control the denominator of the COMPLETE renewal source. [research]** For z_R=2-3S_R^ord, identify its reduced denominator d_R after aggregation, retaining all nine high and twelve low sources or consistently removing the zero term. Prove a usable bound; clearing internal representations separately is not required. Dependencies: accepted exact renewal construction.

- [ ] **O2 — Make clearing affordable along unbounded radii. [research]** Prove d_R*Psi_R->0 along an actual infinite radius sequence. Use the proved positive tail estimate together with O1's full arithmetic cost. Dependencies: O1. Positivity and unscaled decay alone do not finish it.

- [ ] **O3 — Apply positivity and integrality. [assembly]** Use Z=z_R+3Psi_R and a hypothetical rational denominator of Z to obtain positive integers tending to zero. Dependencies: O2. A separate nonvanishing theorem is already supplied by positivity.

An alternative occupation bridge can replace O1–O2:

- [ ] **O4 — Eliminate auxiliary readouts in an exact arithmetic identity. [research]** Prove T_n*nu^H(z_n)=u_nZ+v_n with positive integers T_n and integers u_n,v_n for the known positive actual atoms. All translated, phase-conditioned and low-row terms must be accounted for; rational Z does not make them rational automatically. Dependencies: accepted positive occupation construction.

- [ ] **O5 — Prove the occupation multiplier fits the tail. [research]** Show T_n*nu^H(z_n)->0 on the same infinite occupied family. For the available bound nu^H(z_n)<=6*2^(-N_n), log_2 T_n<=(1-epsilon)N_n for fixed epsilon>0 suffices. Dependencies: O4. Then a hypothetical denominator of Z gives the positive-integer contradiction directly.

## Route P — potential and slice hypotheses still to establish

The new claims were reviewed in [codex_review.md](<investigations/potential-theoretic-obstruction/codex_review.md>). No slice transcendence or natural-boundary theorem for the actual array is accepted as proved.

- [x] **P1 — Establish the kernel stencil and decaying-function flux lemma. [technical]** The archived stencils and mixed-difference rectangle telescoping give these identities under the stated decay/summability hypotheses. This does not establish the target application; see P5.

- [ ] **P2 — Establish actual slice complexity and justify the transcendence application. [research]** Prove a universal usable complexity bound for the actual accumulated-state row/column digit words, not floor(n*alpha) modulo three. Combine with P6 and the precise canonical-digit hypotheses of Adamczewski–Bugeaud. Increment phase-cut counts alone do not suffice.

- [ ] **P3 — Prove any generating-function property being used. [research, optional]** Establish actual nonrationality or a precisely stated boundary property with applicable hypotheses. Neither follows from irrational driving dynamics. This task can be bypassed by another arithmetic proof; a function property alone does not establish a special-value theorem.

- [ ] **P4 — Prove a target-specific arithmetic bridge. [research]** Show the COMPLETE weighted sum at (1/2,1/3) is irrational using actual structure. Even if P2 succeeds, transcendental slices may cancel. No carry, remainder, low-row or normalization term may be omitted. This may replace the CF routes only after a complete proof.

- [ ] **P5 — Repair the potential representation. [research]** Retain the reflected-stencil shift and derive an identity with all non-decaying boundary terms accounted for. Q_H(-z) tends to mass 1/27 in one direction, so the decaying-function flux lemma cannot be applied directly. Done when an exact target identity with valid boundary estimates is proved.

- [ ] **P6 — Prove actual non-eventual-periodicity for each proposed slice. [research]** Specify the exact row/column and demonstrate infinitely many failures of every candidate eventual period. Irrational rotation and finite frequency observations alone are insufficient. Pair with P2 before invoking a digit-complexity transcendence theorem.

## Shared final checks — after ONE route closes

- [ ] **F1 — Assemble one complete proof with one dependency ledger.** Every new lemma must state its quantifiers, domain, constants and actual family. Check that clearing, error, nonvanishing or modular obstruction apply together. Remove conjectural links and circular uses of irrationality.

- [ ] **F2 — Perform the deferred comprehensive rigor review.** Recheck the universal finite covering proof, density passage, low-row and exceptional-birth normalization, the chosen model/bridge, all infinite tails and external-theorem hypotheses. Challenge the most fragile step independently; finite tests do not replace its proof.

- [ ] **F3 — Perform the deferred novelty check and write the final conclusion.** Check relevant primary literature and explain whether the complete proof is new, while stating exactly which part of Erdős 168 it resolves. Lean remains deferred and is not a mathematical prerequisite.

No autonomous proof-search goal is active. This checklist is a handoff for selecting small proof targets; no open item is marked complete merely because its numerical instances were tested.
