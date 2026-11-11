# Revised single-clearer and triple-clearer review

Reviewed 2026-11-10. The rewritten notes.md and master_proof_synthesis.md supersede the pair-gcd claims reviewed in codex_review.md. New scripts are verify_single_clearer_obstruction.py and verify_pigeonhole_gcd.py. The older verify_tail_gcd.py remains invalid in the ways already documented. No complete irrationality proof is supplied.

## Results that survive rigorous examination

The single-clearer theorem is correct conditional on its coprimality hypothesis. Assume Z=A/B, and let M_B=2*3*7*13 times the product of both reduced multiplicative-order moduli for every prime dividing B outside {2,3,7,13}. If an actual adequate nonresonant index beyond the rationality-dependent cutoff satisfies gcd(p_n,M_B)=gcd(q_n,M_B)=1, then p_n and q_n are odd, q_n is not divisible by seven, p_n is not divisible by thirteen, and none of B's outside primes divides D_n. Consequently gcd(B,D_n) divides 4914. Eventual divisibility B|D_n contradicts B>4914. The weaker previously accepted bound B>2^56 already suffices.

This is essentially the earlier ND conditional reduction with a sharper constant. It does not prove that the needed index exists. Infinite adequate supply alone does not imply visits to the coprime locus. The supplied ledger shifts both obligations into M1 and labels the other tasks conditionally proved; this does not establish the original M2–M6 infinite-visit targets. The canonical checklist keeps those targets open and adds the coprime-locus route explicitly as an alternative.

The corrected valuation STATEMENTS are valid: even p gives v_2(D)=v_2(p)+2; even q gives v_3(D)=v_3(q)+5. The synthesis still contains an erroneous intermediate equality v_2(27^p-1)=1+v_2(p) for even p; delete it and use the following correct even-exponent LTE argument. This local inconsistency does not invalidate the corrected final formula.

## A valid conditional triple lemma

For three indices with pairwise coprime q coordinates and pairwise coprime p coordinates, no outside prime can divide all three clearers. Otherwise assign each occurrence to its horizontal or vertical factor. Two of the three share an axis; its reduced order (at least two) would divide two coprime coordinates, impossible. This repairs the specific cross-factor problem for triples, not pairs.

To bound the FULL gcd by 4914, also require at least one odd p, at least one odd q, an index with seven not dividing q and odd p, and an index with thirteen not dividing p and four not dividing q. The exceptional valuation formulas then bound the four prime powers by (1,3,1,1). These witnesses need not be the same index. The script's check_triple implements these sufficient conditions. Without the exceptional conditions, only the outside-prime exclusion has been proved.

The needed infinite assertion is that such adequate triples exist beyond EVERY sufficiently large cutoff. Neither an infinite K nor a finite list of triples implies this. In particular, finite observed coprimality is not a recurrence theorem for the actual logarithm ratio.

## What the scripts actually verify

Both new scripts finish successfully as written. Their assertions are finite checks, not universal proof certificates.

- The single-clearer script correctly initializes its convergents, unlike the older verifier. Its order and selected integer valuation checks pass. However, 500 decimal digits are insufficient for its whole requested prefix: comparison with an independent exact logarithm-series interval gives the first mismatch at n=487 (reported next digit six, certified digit four), and mismatches at 12 reported indices. The claimed 500-prefix statistics are not adopted as certified data.
- Its candidate-denominator routine only factors outside primes below 100 and does not verify that a remaining factor is absent. It checks a convenient finite index, not that the rationality cutoff N_0(B) has been passed. Thus the printed candidate refutations are not complete rational-denominator exclusion certificates. These implementation limitations do not refute the written conditional theorem.
- The triple script reproduces the exact small-case gcd 24570 for the pair and 4914 after adding 41/65. It does not directly evaluate full clearers at the enormous later q values: there it tests the sufficient algebraic hypotheses and prints a theorem-based bound. That method is valid given the triple lemma, but its docstring overstates direct gcd computation.
- Independent integer logarithm-series intervals certify the first 600 triple-script convergents. Checking the actual adequacy and full triple hypotheses confirms finite examples beyond the seven cutoffs 10,50,100,200,300,400,500. This improves the finite evidence; it does not extend the quantifier to arbitrary cutoffs. No claim about all 650 generated digits is needed or certified here.

The synthesis also conflates two enclosures: cutoff 10^130 yielded the older 127-term CF certificate, not the later 71,933-term certificate. The larger certificate used the stored q=125743 scalar model and the full rectangle radius, as documented in the previous review. Its dependency and cached-value qualification remain unchanged.

## Disposition

Part (ii) is still unproved. H1–H2 remain working-complete. The single-clearer implication and conditional triple lemma are accepted working progress. Actual adequate supply, modulus-dependent coprime visits, arbitrarily late suitable triples, and half-cleared arithmetic separation remain open. Final comprehensive foundation and novelty review is not replaced by these targeted checks.
