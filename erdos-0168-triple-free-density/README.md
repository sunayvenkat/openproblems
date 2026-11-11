# Erdős #168: sets with no triple {n, 2n, 3n}

**Problem.** Let F(N) be the largest size of A ⊆ {1,…,N} that contains no complete triple {n, 2n, 3n}, and let c = lim F(N)/N.
(i) Determine c. (ii) Is c irrational? ([erdosproblems.com/168](https://www.erdosproblems.com/168), [OEIS A386439](https://oeis.org/A386439))

## Status

| Part | Status | Where |
|---|---|---|
| (i) finite formula τ(t) = min_j (K_j − I_j − P_j) for every t ≥ 3 | **PROVED**, self-contained; independent referee audit passed. No external human review, no Lean. | [part-i-density-formula/PROOF.md](part-i-density-formula/PROOF.md), [audit/AUDIT.md](part-i-density-formula/audit/AUDIT.md) |
| (i) explicit increment rule η_{a,b}, c = 1 − (1/3) Σ η_{a,b} 2^{−a}3^{−b} | **PROVED** given the formula | [part-i-density-formula/REPORT.md](part-i-density-formula/REPORT.md) §4–5 |
| (i) c = 0.80096575500655898909042032638808241322472498911028458781919045603644708044249630021895087751711467131844149435653902330834474… | **certified interval**, width 1.3·10⁻¹²⁸; agrees with A386439 | REPORT.md §6, `c_digits.py` |
| (ii) irrationality of c | **OPEN** | [part-ii-irrationality/PROGRESS.md](part-ii-irrationality/PROGRESS.md) |

Part (ii) is reduced to six alternative routes (A, M, R, H, O, P). Each one lacks one theorem, usually "actual infinite adequate supply" of good indices. Only one route has to be closed. [plan.md](part-ii-irrationality/plan.md) has the dependency map. [todo.md](part-ii-irrationality/todo.md) lists each missing lemma with its finish condition.

**Retracted claims.** Several drafts claimed a full solution of (ii). Each one was refuted on audit. See [breakthrough-synthesis/adversarial_audit.md](part-ii-irrationality/investigations/breakthrough-synthesis/adversarial_audit.md) and [tail-gcd-obstruction/codex_review.md](part-ii-irrationality/investigations/tail-gcd-obstruction/codex_review.md). PROGRESS.md is the authoritative record.

## Layout

```
part-i-density-formula/     PROOF.md, REPORT.md, verification scripts, audit/ (independent re-derivation + code)
part-ii-irrationality/
  PROGRESS.md               authoritative current state of (ii); read first
  plan.md, todo.md          route map and granular lemma checklist
  prompts/                  research prompts used for each attack round
  investigations/<topic>/   one folder per attack round: notes, checks (*.py), outputs (*.json),
                            REPORT.md (round summary, where one exists), *audit*/codex_review.md (reviews)
  early-attacks/            first rounds: cover/hole-filling lemmas, return attacks, transfer search
```

For a quick read, use [PROGRESS.md](part-ii-irrationality/PROGRESS.md) and then the review file of the route you care about.
