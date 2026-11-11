# Erdős 168(ii): finite-cover proof-gap attacks

The sharp candidate `tau(t)=min_j(K_j-I_j-P_j)` remains unproved. None of the results below resolves #168(ii), which additionally asks for irrationality. This bounded round decisively eliminates the unrestricted-LP ceiling route, strengthens finite evidence for the restricted boundary words, and proves local reductions for the remaining matching problem.

A subsequent analytical round proves global filling of bounded complement holes and reduces maximum deficiency to simply connected components touching the horizontal axis. See [the complete hole-filling proof and remaining boundary inequality](<hole_filling.md>).

## Does rounding the unrestricted fractional optimum give the integer optimum?

### Takeaway

No. The first failure is the actual 2–3 weighted triangle at `t=486`, with 33 vertices: its integer optimum is 11, while its fractional optimum is exactly `2468/249`, whose ceiling is 10.

### Cited Findings

- The previously established exact diagonal recurrence is reused without modification. [Original recurrence and implementation](<../open-conjecture-transfer-search/exact_168_diagonal.py>)
- Rational primal and dual certificates, and all earlier fractional/integer values, are saved in [the counterexample artifact](<cover_lp_counterexample.json>). The search reconstructs every rational certificate and checks all inequalities with `Fraction`, rather than accepting floating-point solver tolerances. [Search and certificate reconstruction](<cover_lp.py>)
- A solver-free exact verifier checks the decisive rational certificates and integer DP value. [Verifier](<verify_cover_certificates.py>)

### Inferences

The six row lengths at `t=486` are `(9,8,6,5,3,2)`. An independent application of the existing row-mask DP gives final costs `[11,11,11,12]` for its four possible top-row masks; the diagonal DP also gives 11. Thus the lower bound is exhaustive exact integer computation, not a numerical MILP claim.

A particularly simple fractional cover has weight 1 at 128, weight 1/2 at

```
2,3,4,9,12,16,18,24,32,54,72,81,96,108,144,162,288,324,
```

and weight zero elsewhere. Each corner has weight at least one and the total weight is 10. This alone disproves a ceiling lower bound of 11. The exact primal-dual certificates sharpen the fractional optimum to `2468/249`. [Simple half-integral certificate](<cover_lp_simple_primal.json>)

The search verifies rational optimality and integer optimality at every earlier nontrivial smooth prefix, `k=3,...,32`, and finds `tau-1 < fractional_tau <= tau` throughout. Prefixes 1 and 2 have no corners. Since the domain changes only at smooth numbers, 486 is the first threshold where the ceiling claim fails.

### Gaps

This disproves only the proposed LP route. It does not refute the patched candidate for the integer optimum. A successful lower bound needs additional integer information or a combinatorial argument; the unrestricted linear relaxation alone cannot supply it.

## Do row drops avoiding 11 and 222 force a two-color optimum?

### Takeaway

No counterexample was found in the bounded exact search. This remains a conjectural normalization; no infinite theorem has been proved.

### Cited Findings

- The exact search checks all 3,787 complete shapes with initial width 21 through 34, terminal row length 1 or 2, drops in `{1,2}`, and neither `11` nor `222` in the drop word. Each unrestricted optimum equals the smallest of the three two-color optima. [Final search record](<cover_words_exact_results.json>)
- The new checker applies the existing diagonal recurrence to strict Ferrers shapes and uses the existing bipartite matching implementation for the restricted optima. It self-checks against the independent row-mask DP on all admissible width-10 shapes, reproduces the old 155-vertex counterexample, and reproduces `tau(486)=11`. [Exact checker](<cover_words_exact.cjs>)
- The older 155-vertex counterexample has both forbidden patterns, so it does not answer this narrower question. [Earlier adversarial review](<../open-conjecture-transfer-search/168_cover_review.md>)

### Inferences

For the true weighted triangle, put `beta=log_2(3)`. Its row length is `w_b=floor(log_2(t)-b*beta)+1`. Since `3/2<beta<5/3`, two successive row drops cannot both be 1: their sum is a difference of floors at spacing `2*beta>3`, hence at least 3. Three successive drops cannot all be 2: their sum is a difference of floors at spacing `3*beta<5`, hence at most 5. Thus the tested subshift is a genuine necessary consequence of the actual geometry.

Eight structured substitutions of the old bad word were also tested numerically, replacing its symbols by `12/122`, `21/221`, `122/12`, or `221/21`, with last row 1 or 2. Seven proposed improvements were solver-infeasible; one 860-vertex instance timed out. This experiment supplied no positive result and no exact theorem. [Substitution checker](<cover_word_substitutions.py>)

### Gaps

The finite test does not prove normalization even for this subshift. No further sweep is running. The earlier MILP enumeration was interrupted after width 26 once the faster exact recurrence replaced it; its partial results are not the final evidence.

## What can be proved about matching deficiency and its missing augmentations?

### Takeaway

The N/E-edge subgraph has an exact path formula; root edges are indispensable even in a ten-point domain. A local honeycomb filling rule preserves or increases deficiency, but a global uncrossing or augmentation theorem is still missing.

### Cited Findings

- For `U subset C_j`, let `B(U)` join the two other colors in every corner whose color-j label is in U. The existing reduction is `tau=K_j-max_U(|U|-nu(B(U)))`. The north-parent edges give the initial matching. [Matching reduction](<../open-conjecture-transfer-search/168_grid.md>)
- The elementary finite obstruction below is checked alongside the LP certificate. [Exact verifier](<verify_cover_certificates.py>)

### Inferences

**Notation.** The three possible edges owned by label u are

```
N(u) = {u/3,2u/3},     present iff 3 divides u;
E(u) = {u/2,3u/2},     present iff 2 divides u and 3u<=2t;
R(u) = {2u,3u},        present iff 3u<=t.
```

These statements refer to divisibility within the smooth lattice. In the bipartition with left color `j+1`, the N edge goes from `u/3` to `2u/3`; the E edge goes from `3u/2` to `u/2`.

**Exact N/E path formula.** Retain only N and E edges. Each physical vertex has degree at most two, with at most one edge of each type. Following an N edge from left to right multiplies its physical value by 2; following an E edge from right to left multiplies it by 3. A two-edge continuation therefore multiplies by 6, so no component is a cycle. All components containing edges are finite paths.

Let

```
r = #{u in U: N(u) is absent},
q = #{u in U: E(u) is absent},
o = number of N/E path components having an odd number of edges.
```

There are exactly `2|U|-r-q` N/E edges. A path with m edges has matching number `ceil(m/2)`, hence

```
nu_NE = |U| - (r+q-o)/2.
```

Consequently, for a selected class j with allowed correction `delta_j=I_j+P_j`, the remaining sharp Hall statement is exactly the demand that adding the R edges increase maximum matching size by at least

```
(r+q-o)/2 - delta_j,
```

whenever the right-hand side is positive. For U avoiding the vertical axis, `r` counts horizontal-axis labels and `q` counts labels exceeding `2t/3`. This formula does not prove the demanded augmentation count.

**Why one matching edge per removed label is invalid.** At `t=18`, choose color 2 and `U={4,18}`. Then

```
B(U): 2 -- 6 -- 12 -- 8
       E(4) N(18) R(4)
```

Its maximum matching has size 2, realized by both edges owned by label 4. The sole edge owned by label 18 meets both of them, so no matching of size 2 can use one edge of each label. Omitting root edges leaves matching number 1. Thus a proof may count edges globally, but cannot demand a rainbow matching indexed by U.

**Pendant-edge structure.** If u is the smallest numerical label in U and `3|u`, then `u/3` is a leaf: its other potential incident labels are `u/6` and `2u/9`, both smaller. Matching N(u) removes only one edge of a larger label, namely E(4u/3). If u is a horizontal-axis label with u>=2 and E(u) exists, then `u/2` is a leaf; its other possible labels are smaller or nonsmooth. Matching E(u) can remove only N(9u/2) from larger labels. This creates a single future blocked edge, but the `U={4,18}` example shows why unused root edges of already processed labels must remain available as credits.

**Proved local filling rule.** Write `d(U)=|U|-nu(B(U))`. Suppose u is not in U and the three labels

```
u/6, 4u/3, 9u/2
```

belong to U. They are precisely the owners of the three complementary edges of the honeycomb hexagon around u: `R(u/6), E(4u/3), N(9u/2)`. The three newly added edges `N(u),E(u),R(u)` alternate with them. Smoothness and membership of the three neighbors ensure that all six corners/vertices in this configuration are present.

Take a maximum matching after adding u. If it uses zero new edges, leave it unchanged. If it uses one, delete that edge. If it uses two, replace those two by the complementary edge joining two of their four endpoints; this loses just one edge and creates no conflict with untouched matching edges. If it uses all three, replace them by the three complementary edges. In every case one obtains a matching before addition losing at most one edge. Therefore

```
nu(B(U union {u})) <= nu(B(U))+1,
d(U union {u}) >= d(U).
```

This also has boundary versions. Adding any label with at most one available edge never decreases d. For a degree-two label, it suffices that an old edge joins one endpoint from each of its two owned edges. In particular:

- A horizontal-axis label with E and R edges can be filled if `9u/2` is in U.
- An interior label in `(t/3,2t/3]`, with N and E edges, can be filled if `u/6` is in U.
- A vertical-axis label `u=3^b`, b>=1, with `u<=t/3`, has N and R edges; it can be filled if `4u/3` is in U, whose E edge is the complementary bridge. This case is usable for unrestricted maximizers, but not when U is required to avoid the vertical axis.

Thus a maximizing set can be taken closed under these valid fills, and to contain every allowed degree-zero or degree-one label. If maximizing only over U avoiding the vertical axis, apply the fill rules only when the new label also avoids that axis.

### Gaps

The filling rules do not show that a maximizing U has a single monotone boundary or no interior holes. Nor do they prove that different horizontal-axis deficits acquire distinct augmentations. The exact remaining obligation is the root-edge augmentation bound displayed above, or another sharp lower bound including all three-color covers. Exact-cover rigidity still applies only to covers hitting every corner exactly once and cannot supply this missing normalization.

All processes from this bounded round are terminal: the original word MILP session 30936 was interrupted; substitution session 14469 finished with exit code 0; exact word session 55089 finished with exit code 0. No older research folder was modified. The finite candidate, its irrationality transfer, and the parent goal remain unresolved.
