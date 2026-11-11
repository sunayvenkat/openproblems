# Review of the claimed tail-gcd solution

This reviews the earlier pair-gcd revision. For the rewritten single-clearer sources, read [the updated review](<codex_review_update.md>).

Reviewed 2026-11-10. Sources: notes.md, master_proof_synthesis.md and verify_tail_gcd.py in this folder. These files do not prove irrationality. Their claims closing M2–M7 are rejected; the canonical checklist restores those tasks. H1–H2 from the previous review remain working-complete.

## Decisive errors

1. Same-base gcd identities do not control cross factors. Coprimality of two p coordinates and two q coordinates bounds gcd(horizontal,horizontal) and gcd(vertical,vertical), but a prime may divide a horizontal factor of one clearer and a vertical factor of the other. For the actual consecutive convergents 5/8 and 12/19, both coordinate gcds are one, but the exact gcd of their nominal clearers is 24570=5*4914. Prime five divides 2^24-1 in the first clearer and 3^36-1 in the second. The exceptional-prime restrictions stated in the synthesis do not eliminate this example. It refutes the claimed general bound for coprime convergent pairs. These particular indices need not both be adequate to refute that general algebraic inference; restricting to K would require a new proof controlling cross factors there.

2. Two exceptional valuation formulas are wrong. For even p, v_2(D)=v_2(p)+2, not +3. For even q, v_3(D)=v_3(q)+5, not +4. Exact examples: (p,q)=(2,3) gives v_2(D)=3; (5,2) gives v_3(D)=5. Actual convergent examples also fail the claimed formulas: 12/19 has v_2(D)=4 rather than 5, and 5/8 has v_3(D)=5 rather than 4. The odd cases and the stated seven/thirteen formulas remain valid. Even the proof text contains inconsistent arithmetic. Correct valuation identities are not proofs that their small values occur infinitely often on the actual adequate family.

3. The argument for exceptional exponents one at seven and thirteen also needs its additional restrictions. Coordinate coprimality alone does not ensure that the same selected index simultaneously avoids both sources of a prime's contribution. No unconditional global gcd bound follows.

4. Seven tested cutoffs up to 500 do not prove a pair exists beyond every natural-number cutoff. Under hypothetical rationality the index after which B divides every adequate D_n depends on the unknown B. There is no proof that it lies within the tested prefix. Infinite K alone does not imply the asserted coprime/small-gcd pairs.

5. The script is not an exact gcd certificate. It uses reciprocal convergents via P=[1,0], Q=[0,1]; the correct append recurrence starts P=[0,1], Q=[1,0]. It checks outside primes only below 1000, not all primes, and constructs a product from four exceptional valuations rather than computing the full gcd. It also uses the incorrect even valuation formulas. Passing its assertions cannot certify its printed upper bound. The notes refer to primes below 2000, which also disagrees with the script. Its search does not enforce the pairwise coordinate-coprimality assumptions used in the purported theorem.

## What remains valid

The previously established rationality-implies-eventual-divisibility lemma and same-base gcd identity remain useful. The outside-prime multiplicative-order criterion is also correct. None supplies the missing actual infinite prime-avoidance statements. M2–M6 originally ask for infinitely many suitable actual indices, not just formulas evaluated conditionally at a single pair. M7 still needs a small gcd in every sufficiently late adequate tail.

The synthesis's residue recurrence gives a valid limited dichotomy: either nonresonant next digits at least two occur infinitely often, or, eventually, successive resonant indices are separated by three digit-one steps, giving blocks (A,1,1,1). The displayed block matrix lies in Gamma_0(3). This does not show which branch the actual logarithm ratio follows. Branch B supplies no unbounded or giant digits: A may remain bounded, and arbitrary nonperiodic bounded choices already give transcendental examples. Membership in this semigroup is not proved impossible for the actual alpha. Thus neither Route H supply nor a sufficient resonant error/cost budget follows from this classification.

## Verification scope and disposition

Direct Python integer-power/gcd calculations reproduced the counterexample and valuation failures above. The invalid verifier was inspected, not treated as evidence of its advertised universal theorem. Source manuscripts are preserved unchanged. The roadmap explicitly withdraws the claimed completion and links this review. Part (i) remains provisional; part (ii) remains unproved. Final comprehensive foundation/novelty review and Lean were not performed.
