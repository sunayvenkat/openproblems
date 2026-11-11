# Marcus's block-permanent conjecture

**Problem.** Let A ∈ ℂ^{mk×mk} be Hermitian PSD, split into m×m blocks A_ij of size k×k, and let G_ij = per(A_ij). Conjecture: per(A) ≥ per(G). For k ≥ 2 with positive definite diagonal blocks, equality should hold iff every off-diagonal block is zero. ([conjectures.io](https://conjectures.io/problems/fulloldproblemscatalog-marcusblockpermanent-conjecture), [problem list](https://yair-lavi.com/mincs-list/conjecture-9/index.html))

## Status: OPEN in general. Three cases proved here.

| (m,k) | Result | Where |
|---|---|---|
| (3,2) | **PROVED**, with the equality case: explicit positive-integer SOS for three quadratic forms in ≤ 5 variables, plus a projection argument | `notes/marcus-three-pairs-proof.tex` |
| (4,2), (3,3) | **PROVED**, with the equality case: exact rational SOS certificates, verified by two independent implementations | `notes/marcus-further-cases-proof.tex`, `results/marcus-invariant-exact-4-6.json`, `results/marcus-invariant-exact-3-9-k3.json` |
| general | OPEN. A natural stronger inductive inequality **fails** (exact counterexample). | `notes/marcus-induction-obstruction.tex` |

Re-verify a certificate (Node built-ins and BigInt only):

```bash
node code/marcus-invariant-verify.mjs results/marcus-invariant-exact-4-6.json
```

Other material:
- `notes/marcus-goal-state.txt`: running state and how to read the certificates.
- `notes/marcus-block-working.tex`, `notes/marcus-amplification-interpolation.tex`, `notes/marcus-reflection-experiments.tex`: working notes.
- `code/`: counterexample searches (block, chaos, replica, spectral, Gaussian interpolation, vector SDP) and the SDP certificate pipeline. Their outputs are in `results/`.

No novelty check has been done.
