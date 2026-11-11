# Workspace audit and permutation transfer obstruction

## What prior work already exists in the workspace?

### Takeaway
The workspace contains substantial partial work, but no prior full solution of the still-open targets inspected. The most developed arguments concern special cases of Marcus's block-permanent conjecture; other artifacts expressly retain gaps. This inspection checked the stated scope, not every proof or certificate.

### Cited Findings
- The selection report chose Marcus's block-permanent inequality and explicitly produced no solution at selection time. It also records that Erdős 156 was already closed on 4 November 2026. [Local report](../problem-selection/REPORT.md); [pool changes](https://conjectures.io/problems/changes).
- `marcus-three-pairs-proof.tex` states a sum-of-squares proof for three blocks of size two, including equality when no row vanishes. `marcus-further-cases-proof.tex` states exact certificate proofs for four blocks of size two and three blocks of size three. Both expressly leave arbitrary block sizes/counts unresolved. [Three-pairs artifact](../../marcus-block-permanent-conjecture/notes/marcus-three-pairs-proof.tex); [further cases](../../marcus-block-permanent-conjecture/notes/marcus-further-cases-proof.tex); [catalog target](https://conjectures.io/problems/fulloldproblemscatalog-marcusblockpermanent-conjecture).
- The Erdős 243 files state restricted results on recurrence increments, periodic errors, and quadratic profiles. The main barrier file explicitly says its asymptotic increment assumption has not been deduced from the full problem. [Barrier artifact](../../erdos-0243-sylvester-rational-reciprocals/notes/erdos243-loglog-barrier.tex); [quadratic rate](../../erdos-0243-sylvester-rational-reciprocals/notes/erdos243-quadratic-rate.tex); [periodic errors](../../erdos-0243-sylvester-rational-reciprocals/notes/erdos243-reduced-periodic-errors.tex).
- `erdos1192-finite-reduction.tex` gives an equivalence between the infinite basis question and bounded-energy covering sets in cyclic groups of order powers of two. It supplies no finite families satisfying that condition. [Artifact](../../erdos-1192-thin-additive-bases/notes/erdos1192-finite-reduction.tex).
- `erdos686-length-three.tex` treats only block length three in the ratio-25 variant, with the complete classification resting on a Magma Thue solver. Arbitrary block length remains unresolved. [Artifact](../../erdos-0686-consecutive-block-products/notes/erdos686-length-three.tex).
- `green15-spectral-reduction.tex` retires Green 15 after checking the accepted JenW1N result, with six-letter substitution and increments between 1 and 125. Its own spectral criterion supplies no substitution meeting its assumptions. [Artifact](../../green-15-additive-square-free-words/notes/green15-spectral-reduction.tex); [external solution](https://conjectures.io/results/66df312f-30b4-4331-b1fa-04be52f7f8ca/solution).

### Inferences
- None of these old artifacts should be described as new progress in the current transfer investigation.
- The prior proof files may be reusable, but their exact arithmetic and proof claims were not independently rerun in this audit.

### Gaps
- No direct connection from these existing partial arguments to Kohlmeyer–Kruer's new results was established.

## Can the four-term permutation result automatically solve Erdős 197?

### Takeaway
No. A natural bridge is false, even for a permutation of a complete interval of just 27 integers. The stronger general assertion fails arbitrarily badly: finite permutations can avoid every monotone four-term arithmetic progression while their monotone three-term progression hypergraphs have arbitrarily large chromatic number.

### Cited Findings
- Kohlmeyer and Kruer's result constructs a permutation of the natural numbers with no monotone four-term arithmetic progression. The source gives the exact bit-preference construction, saturation lemma, and closed-prefix invariant. [Published solution source](https://conjectures.io/results/e73b95f7-1d1b-42b5-a442-c07077741d73/solution).
- Erdős 197 asks whether the natural numbers can be divided into two sets, each admitting a permutation with no monotone three-term progression. The order of each set may be chosen freely. [Problem](https://www.erdosproblems.com/197); [related original research](https://arxiv.org/abs/2211.04451).
- A 2026 preprint studies why the canonical alternating dyadic-block partition fails, while leaving the full question unresolved. Its author's repository explicitly limits the claim to that partition. [Author repository](https://github.com/Wkasel/erdos197); [preprint](https://arxiv.org/abs/2609.02939).

### Inferences
**A false bridge.** One might hope that every four-term-free permutation could have its values colored red and blue so that neither induced subsequence contains a monotone three-term progression. Applied to the infinite permutation, compactness would prove Erdős 197. The finite statement underlying that argument is false.

**Exact 27-point counterexample.** Write every integer in `[0,27)` with three ternary digits, reverse the digits, and list the resulting values in the order of the original integers:

```
0,9,18,3,12,21,6,15,24,
1,10,19,4,13,22,7,16,25,
2,11,20,5,14,23,8,17,26.
```

This permutation has zero monotone four-term arithmetic progressions and 65 monotone three-term progressions. Its 65 triple constraints admit no red-blue coloring. The mathematical no-four proof below works at every dimension. The two-color failure at dimension three has been independently verified in two distinct finite procedures:

1. A DPLL-style constraint solver, using forced colors from a triple whose other two entries have the same color. Its entire search has 11 nodes. The saved JSON includes all branch choices, forced colors, and contradiction triples.
2. A separate exhaustive binary recursion with no unit propagation and an independent triple/quadruple enumeration. Fixing the color of 0 by complement symmetry, it visits 3,665 internal nodes; its 3,666 pruned branches each exhibit a monochromatic three-term progression. It finds zero complete colorings.

Both checks use exact integer operations. The discovery script checks the smaller ternary dimensions one and two, where a coloring does exist. The independent verifier also checks the earlier 30-value set described below.

Files in this notes directory:

- `test_196_197_ternary.mjs`: ternary-reversal construction and DPLL search.
- `196_197_ternary_obstruction.json`: exact permutation, 65 edges, 11-node forcing trace.
- `verify_196_197.mjs`: independent exhaustive verifier of both witnesses.
- `196_197_ternary_verification.json`: independently reproduced counts.

Run the verifier with `node "research_notes/Erdos theorem transfer investigation/verify_196_197.mjs"` from the workspace root.

**Theorem: unbounded obstruction.** For every positive integer `r`, there is a finite permutation avoiding monotone four-term arithmetic progressions whose monotone-three-term-progression hypergraph is not `r`-colorable.

**Proof.** For `m≥1`, let `R_m` reverse the `m` ternary digits, and order `[0,3^m)` by increasing `R_m(x)`. The reversal map is an involution, so this is the permutation displayed above when `m=3`.

Consider a nonconstant numerical progression `a,a+d,a+2d,a+3d` contained in that interval, with either sign of `d`. Let `k=v_3(d)`. Digits below position `k` are identical for all four numbers. At digit `k`, the residues have the form

`u, u+δ, u+2δ, u` modulo three, where `δ≠0` modulo three.

In the digit-reversal order, comparisons between different digits at position `k` are decided at that position. A strictly increasing or decreasing order of the four numbers would therefore require this digit sequence to be respectively nondecreasing or nonincreasing. Its first and last entries agree while both other residues occur, so neither is possible. Thus the permutation avoids all monotone four-term progressions.

Now take `m` large enough for the Hales–Jewett theorem with alphabet `{0,1,2}` and `r` colors. Every `r`-coloring of the ternary words contains a monochromatic combinatorial line. If `J` is its nonempty set of variable positions, its three numerical values are

`A, A+D, A+2D`, with `D=Σ_{j∈J}3^j>0`.

There are no carries because the variable positions have fixed digit zero in `A`. Their reversal ranks are similarly `R_m(A),R_m(A)+D',R_m(A)+2D'`, where `D'=Σ_{j∈J}3^{m-1-j}>0`. They therefore occur monotonically in the permutation, giving a monochromatic progression. This proves the theorem. The only external mathematical input is the classical Hales–Jewett theorem; the digit-reversal argument is elementary. [Hales and Jewett, Regularity and positional games](https://doi.org/10.1090/S0002-9947-1963-0143712-1).

This theorem was found collaboratively in this investigation; novelty has not been assessed. It is an obstruction to a proposed proof route, not a solution of Erdős 197.

**An additional independent witness.** Before the ternary construction was identified, a random greedy search found the following 4AP-free set whose ordinary three-term-progression hypergraph is not two-colorable:

`{1,3,7,12,14,15,17,18,19,25,26,29,35,37,38,42,53,58,59,60,63,73,75,77,84,85,88,93,94,95}`.

It has 51 three-term progressions and no four-term progressions. Independent exhaustive verification visits 2,976 internal nodes and rejects 2,977 branches, finding no coloring up to complement symmetry. The witness is in `196_197_obstruction.json`; the generator is `test_196_197.mjs`; the independent result is `196_197_verification.json`. The 27-point complete-interval permutation is the clearer result to present.

### Gaps
- These obstructions do not prove a negative answer to Erdős 197: its color classes may have entirely different orders.
- They also do not rule out coloring the particular infinite permutation constructed by Kohlmeyer and Kruer using additional special structure.
- No infinite two-set construction or impossibility theorem for the full problem was obtained.

## Which graph transfers are already present in the literature?

### Takeaway
The arc-graph route is very productive, but the most immediate strengthening is already explicitly present in the current literature. It should be credited rather than rediscovered as a new solution.

### Cited Findings
- Nguyen and Walczak explain Kohlmeyer–Kruer's construction and improve the bound on the chromatic number of four-cycle-free subgraphs from six to three. Their first version gives a high-fractional-chromatic base graph whose bounded-maximum-degree subgraphs are all two-degenerate, plus general `K_{s,t}` extraction and coloring lemmas. [Primary paper, version 1](https://arxiv.org/html/2609.40192v1).
- Their Theorem 2.1 already explicitly supplies arbitrarily large fractional chromatic number with no three-regular subgraph. The associated four-regular result was proved earlier by Janzer, Steiner, and Sudakov. [Nguyen–Walczak](https://arxiv.org/html/2609.40192v1); [Janzer–Steiner–Sudakov](https://people.math.ethz.ch/~sudakovb/chromatic-number-regular-subgraphs.pdf).
- Their first version also identifies the induced-shift-graph question of Adenwalla and collaborators as negatively answered by this construction. [Section 3](https://arxiv.org/html/2609.40192v1).

### Inferences
- From the version-1 lemmas one obtains, for fixed `s,t≥2`, arbitrarily high-chromatic triangle-free graphs whose `K_{s,t}`-free subgraphs are `(min(s,t)+1)`-colorable. Take `t=min(s,t)`, `r=t+1`, and use `binom(r,t)≥3` in Lemma 3.3. However, the other researcher checked that the current paper explicitly includes this as a theorem; it is not new here. See the current-version audit in `open_targets.md`.

### Gaps
- No currently open catalog problem was settled through these graph deductions in this round.
