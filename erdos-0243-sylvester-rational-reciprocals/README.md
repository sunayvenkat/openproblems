# Erdős #243: rational reciprocal sums with Sylvester-like growth

**Problem.** Let a₁ < a₂ < … be positive integers with a_{n+1}/a_n² → 1 and Σ 1/a_n ∈ ℚ. Must a_{n+1} = a_n² − a_n + 1 for all large n? ([erdosproblems.com/243](https://www.erdosproblems.com/243), [conjectures.io](https://conjectures.io/problems/erdos243-erdos-243))

## Status: OPEN

Write S = p/s, D_n = s∏_{j<n} a_j, and C_n = D_n Σ_{j≥n} 1/a_j. These give the integer state recurrences D_{n+1} = a_n D_n and C_{n+1} = a_n C_n − D_n. The notes prove only restricted results:

| Note | Result |
|---|---|
| `notes/erdos243-loglog-barrier.tex` | **COND.** If the numerator increments are eventually ≤ α log log C_n + O(1) with α ≤ 1/log 2, the tail is eventually Sylvester. Also sieve and CRT constraints on the denominator prime support. |
| `notes/erdos243-polynomial-obstruction.tex` | Excludes some exact numerator patterns, including jumps much larger than log log. Finite-state modular exclusions, verified computationally. |
| `notes/erdos243-quadratic-exclusion.tex` | Restricted exclusion of quadratic numerator profiles, using gcd stabilisation and a square obstruction. |
| `notes/erdos243-quadratic-rate.tex` | Irrationality under the much stronger rate a_n²/a_{n+1} = 1 + 2/n + o(n⁻²). Uses two Magma integral-point computations (`results/erdos243-elliptic-magma-certified.xml`). |
| `notes/erdos243-reduced-periodic-errors.tex` | Rules out eventually periodic signed errors and two bounded error alphabets. |
| `notes/erdos243-small-alphabet.tex` | Necessary switching conditions for the alphabet {−1, −3}. Exact search of 140,000 rational starts: all reach zero error. |
| `notes/erdos243-counterexample-search.tex` | No infinite counterexample. Six computed rational starts all enter a Sylvester tail. |

The rational-tail framework is from Koizumi (2026). No novelty claim has been checked.

## Layout

`notes/` holds the write-ups and adversarial reviews (`*-review.txt`). The prompts given to reviewers are in `notes/review-prompts/`. `code/` holds Node/Magma verifiers. `results/` holds their outputs.
