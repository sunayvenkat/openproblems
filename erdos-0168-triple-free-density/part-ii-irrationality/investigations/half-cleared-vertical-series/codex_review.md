# Antigravity half-cleared series integration review

Reviewed 2026-11-09. New sources are notes.md and verify.py in this folder, identified in SOURCE_MANIFEST.json and preserved unchanged. The previous 37 manifested source files are unchanged. Antigravity also edited the roadmap and marked H1–H2 complete in the checklist.

## Accepted working progress

H1's complete horizontal hybrid is correctly normalized. Use the correct-side nonresonant rational horizontal walk A', of period L=3q, while retaining the actual vertical walk, event corrections and every low row. Remove the exceptional birth before periodization and restore its scalar contribution once. With the unexceptional indicators eta', define

\[
G_n(b)=\sum_{a=0}^{L-1}(1-3\eta'_{a,b})2^{L-a},\qquad
W_n=\sum_{b\ge0}G_n(b)3^{-b}-(2^L-1).
\]

These definitions retain the background and minus-three coefficient previously missing from the proposed reformulation. Absolute convergence holds for each fixed n. Periodicity uses the accepted rational-axis theorem; a zero sum over one block alone would not establish periodicity without the periodic increment rule, which is also available here.

H2's written proof is sound within the accepted state/model framework for the sufficiently late applicable convergents. Correct-side Farey floor agreement gives A_a=A'_a for a<q+Q, hence agreement of the complete hybrid and true unexceptional births for every vertical index in those columns. The difference is supported in a>=q+Q. Its coefficient bound and complete geometric tail give

\[
(2^{3q}-1)Z=W_n+E_n,\qquad
|E_n|\le9\,2^{2q-Q}.
\]

No vertical truncation is used in that universal estimate. The small initial convergents outside the established model's slope domain should not be included in an unqualified all-convergents statement. For any infinite applicable nonresonant family with next digit at least two, Q>=2q+q_previous implies E_n->0. Under rational Z=A/B, ||B W_n||<=B|E_n|. This is conditional on that family, not a proof that it is infinite.

The supplied verify.py passes its two cases, including finite modulo-three/nine checks. Its axes use mpmath and its error sum is truncated without a certified exterior interval; it is a numerical consistency check, not an exact infinite-series certificate. Independent integer-power floor calculations reproduce horizontal agreement in both windows. The written full-tail proof, not the numerical script, supports adoption of H1–H2. The source mentions verify_multiple.py, which is not supplied.

## Modulo-nine law: correct identity, arithmetic gap retained

Writing C_0=2^(L+1)-2, the elementary congruences G_n(b)=C_0 modulo three and G_n(b)=C_0-3*Delta_n(b) modulo nine are correct. Choose Delta_n(b) in {0,1,2} from the parity-weighted indicator sum, and R_n(b)=(G_n(b)-C_0+3*Delta_n(b))/9. Then

\[
W_n=2(2^L-1)-3\mathcal D_n+9\mathcal R_n
\]

is an exact absolutely convergent identity for fixed n. It does not remove carries or prove H3. The remainder mathcal R_n is another infinite real series. Its integer coefficients do not make its real value an integer or a rational with known denominator. It may cancel the fractional contribution of mathcal D_n.

Neither a finite frequency observation nor density of the underlying rotation proves that this accumulated-state readout is nonperiodic or Sturmian. Even a proof of irrationality of mathcal D_n alone would not establish uniform separation of the COMPLETE B*W_n along an infinite family. Those claimed consequences are not incorporated as theorems.

## Corrections to the appended roadmap claim

The parenthetical statement that infinitely many nonresonant next digits at least two follow from transcendence is false as an inference. The existing actual-supply note's Lemma C constructs infinite abstract transcendental tails with block (A,1,1,1): large digits occur at resonant currents and all intermediate nonresonant currents carry next digit one. Transcendence therefore does not establish the family Route H needs for this particular logarithm ratio.

H1 and H2 are working-complete. H3 still requires BOTH actual infinite eligible supply and arithmetic separation of the full vertical series. The checklist now isolates H5 (supply) and H6 (remainder/cancellation control) as subtargets toward H3. H4 is the already identified final assembly step. Other routes remain alternatives; no irrationality proof or new unconditional infinite-supply theorem has been obtained.

Final comprehensive rigor and novelty review remains deferred. This review does not establish historical priority or Lean formalization.
