# Erdős #893: divisors of Mersenne numbers under doubling

**Problem.** Let f(n) = Σ_{k≤n} τ(2^k − 1). Does f(2n)/f(n) tend to a limit, and is it +∞? Kovač and Luca proved lim sup = ∞. ([erdosproblems.com/893](https://www.erdosproblems.com/893))

**Sub-problem (β_K).** Let P_K = {p prime : τ(2^p+1) ≤ K}. Define β_K = lim sup over p ∈ P_K of log ω(2^p−1) · log log p / log p. Conjecture: β_K = 0 for every K ≥ 4.

## Status: OPEN (both)

Proved here (see the paper):
- f(2n) ≥ 3f(n) for every n, with equality exactly when n ∈ {1, 2, 4}.
- If the Fermat number F_a is composite, then f(2n) ≥ (4 − 16/(3·2^{a−2}+4)) f(n) on [2^a, 2^{a+1}). Hence f(2n) ≥ (24/7) f(n) for 32 ≤ n < 2^33. Also lim inf ≥ 4 if all large Fermat numbers are composite.
- For each C, the set {n : f(2n) > C f(n)} meets every doubling chain of length J(C) and has lower density ≥ 1/(2^{J(C)} − 1).
- An exact reduction of f(2n)/f(n) → ∞ to indices whose odd part has few divisors. This gives a conditional theorem under a much weaker hypothesis than Kovač–Luca's (H_δ).
- A negative answer by the natural route needs primes with τ(2^p+1) bounded and ω(2^p−1) = exp((log 2 + o(1)) log p / log log p). This is what motivates β_K.

β_K (see [beta-K-omega-of-mersenne/](beta-K-omega-of-mersenne/mersenne_omega_research_note.md)):
- A disproof would settle two open problems: infinitely many composite M_p, and many p with Ω(a_p) small.
- Finiteness of P_K would imply finitely many Wagstaff primes.
- Bounded-depth barrier models are consistent with both β_K = 0 and β_K = ∞.
- An "honest ideal" family shows that ideal-level divisibility is not enough.
- The function-field analogue is **proved**.
- Every method tried reduces to one pointwise counting estimate for q ≡ 1 (mod 2p) with 2^p ≡ 1 (mod q).
- Correction to the original prompt: ω(2^397 − 1) = 9, not ≤ 8.

## Layout

```
paper/                     mersenne_doubling_paper.tex (+ .html render, PDF of the barrier write-up),
                           paper_checks.py (all numerical claims), oeis_cache/ (b-files used by the checks)
notes/                     tau_mersenne_doubling.tex: earlier "what the method proves and needs" note
prompts/                   doubling_prompt.tex: the research prompt for the f(2n)/f(n) attack
beta-K-omega-of-mersenne/  research note on β_K, appendix (barrier models, p-adic, interpolation,
                           function field, second-order bound) with scripts/, and its prompts
```
