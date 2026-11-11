# Independent seed crosscheck: graph criterion, height, winding, and word assembly

## Do the graph criterion and height/winding lemmas prove edge robustness?

### Takeaway

No counterexample or fatal gap was found in Theorem 2.1, Lemma 2.2, Lemma 2.3, or their interfaces to distinct undirected edges. The arguments below were checked directly from the current source before reading any other seed audit. References are line numbers in [seed-current-text.txt](<./seed-current-text.txt>), extracted from the pinned [seed-source.pdf](<./seed-source.pdf>).

### Cited Findings

- The criterion explicitly assumes `n = 1 mod 3`, `q=3t+1`, `t>=r>=1`, `q|n`, `q<n`, `q` units with distinct direction pairs, and an inverse-closed connection set without zero or an involution. Its four conditions specify punctured compatibility, cross-type chord compatibility, disjoint three-step words, and a positive unit deficit whenever total deficit is at most `r`. [Source, Theorem 2.1, lines 51–71](<./seed-current-text.txt:51>)
- Lemma 2.2 constructs the height character from a properly colored Cayley graph. Lemma 2.3 bounds arbitrary allowed path increments when at most `t` distinct edges of the Andrásfai gap graph are bad. [Source, lines 85–117 and 143–164](<./seed-current-text.txt:85>)

### Inferences

All verdicts below concern the displayed general assertions, not numerical instances.

| Target and source lines | Independent check | Verdict |
|---|---|---|
| Bad graph edge to bad core direction pair, 118–121 | If two undirected core edges `{v,v+s}` and `{w,w+t}` coincide, then `t=s` or `t=-s`. Thus edge sets of distinct direction pairs are disjoint. Choosing one bad edge per bad pair injects bad pairs into bad core edges, so there are at most `r` bad pairs even when the augmented graph has repeated chord descriptions. Chord deduplication cannot change this injection among the distinct core edges actually present. | Pass. |
| A remaining clean unit generator, 119–121 | The chosen `q` unit directions have distinct pairs and `q=3t+1>r`. At least one has no bad edge anywhere in its entire translated core edge set. Its cyclic subgroup is all of `Z/nZ`, so the remaining proper directions generate the group. This supplies the hypothesis of Lemma 2.2. | Pass; no assumption that chord sets are disjoint is needed. |
| Square integrability, 97–103 | Each pulled-back grid edge has increment `+1` or `-1`. The sum around a square is divisible by 3 because it is a sum of color differences, and is even because there are four odd increments. Its absolute value is at most 4, so it is zero. Backtracking also sums to zero. Swapping neighboring coordinate steps and cancelling inverse steps reduces every closed grid walk. Hence an integer height exists. | Pass. |
| Period functional and exact character, 104–112 | For a lattice period `lambda`, height difference `h(x+lambda)-h(x)` is divisible by 3. Moving `x` by a grid step changes this difference by an element of `{-2,0,2}` that remains divisible by 3, so the difference is constant. Period differences are additive. The period lattice has finite index, hence full rank, giving a unique real linear extension `theta`. Height parity gives `phi(lambda)=sum lambda_j mod 2`, while color agreement gives `phi(lambda)=0 mod 3`; therefore `(theta-3*1)/6` is integer-valued on the period lattice. Modulo integers it factors through the cyclic quotient and equals the character `K/n`. This is exactly `theta_u=3+6Ku/n mod 6`. | Pass. |
| Bounds and translation means, 107 and 113–117 | Summing the `n` increments in direction `u` gives the period value `n theta_u`; each term is between -1 and 1, proving `abs(theta_u)<=1`. Even if `u` is not a unit, each orbit has a shorter period and the same argument gives average `theta_u` on each orbit. Changing a lift of the starting group vertex adds the same period constant at both ends of a word. Translation permutes starting vertices, so the average word increment is the signed sum of the generator means. An odd word contributes `3 mod 6` to the constant term. | Pass; no unit assumption on every proper generator is hidden here. |
| Clean word for a bad target, 122–124 | The bad target's own pair consumes at least one of the at most `r` bad pairs. Its `r` alternative words avoid that pair and use pair sets disjoint **between words**. Each of the at most `r-1` other bad pairs can spoil at most one word, so some word uses only globally proper directions. Repeated directions within one word do not invalidate this argument. If the target pair is proper, the word `(s,s,-s)` is entirely proper. | Pass; `r` words really suffice, rather than `r+1`. |
| Values of a translated word increment, 124–130 | A sum of three proper increments belongs to `{-3,-1,1,3}` and is congruent to the endpoint color difference. Hence it is `+1` or `-1` on a proper target edge, and `+3` or `-3` on a bad target edge. The chosen word is fixed while its starting point is translated; its clean directions are proper at every translate. | Pass. |
| Exact unordered count `beta_s`, 128–138 | The map `v -> {v,v+s}` is injective unless `s=0` or `2s=0`. Both are explicitly excluded. Therefore it parametrizes exactly `n` distinct undirected edges of this direction pair, and exactly `beta_s` starting vertices have bad target edges. Averaging the previous row gives `abs(mu_s)<=1+2 beta_s/n` without a factor-of-two error. Summing `beta_s` over the one-per-pair set `J` counts each bad core edge exactly once and is at most the number of bad augmented edges. | Pass; excluding the involution is essential and is actually done. |
| Character deficit, 130–140 | Put `x=[Ks]_n/n`. The smallest absolute value of a real number congruent to `3+6x mod 6` is `3-6 min(x,1-x)`. Combining this with the previous bound gives `beta_s >= n-3 min([Ks]_n,n-[Ks]_n)`, and `beta_s>=0` supplies its positive part. Thus `F(K)<=r`, and positive deficit forces `abs(mu_s)>1`. | Pass. |
| Rotational symmetry of `B_t`, 143–158 | It has cyclic length `m=3t+2`; an allowed positive difference is `1 mod 3`, and its complementary difference `m-d` is also `1 mod 3`. Rotations preserve the graph. Removing three consecutive interior vertices of a four-edge cyclic window changes differences across the removed block by exactly 3, so the retained induced graph, cyclically relabeled, is exactly `B_(t-1)`. | Pass. |
| Induction base and clean-cycle case, 150–154 | For `t=0`, `B_0` is a proper edge traversed in both directions, so its cycle sum is zero. If no cycle edge is bad, the maximal cycle sum is at most `3t+2`, divisible by 3, and has the parity of `3t+2`; these conditions imply it is at most `3t`. | Pass, including the doubled traversal in the two-vertex base case. |
| Finding and deleting the four-edge window, 154–161 | For `1<=b<=t` bad cycle edges, the number of proper cycle edges is `3t+2-b>2b`, so one bad edge is followed by at least three proper edges before the next bad edge. Remove the three interior vertices of that four-edge window. The initial bad edge disappears, so the retained induced graph has at most `t-1` bad edges. The new cycle bridge was already an edge of the original `B_t` (distance 4), so no extra bad edge is introduced into the induced graph. | Pass; the bridge is not an uncounted newly inserted edge. |
| Local change in maximal cycle sum, 159–161 | The three proper increments sum to `s=-3,-1,1,3`. The removed four-edge sum is `3+s`; the bridge's maximal increment is respectively `3,-1,1,3`. Thus old sum minus new sum is respectively `-3,3,3,3`, always at most 3. Induction gives the claimed `3t` cycle bound. | Pass. |
| Arbitrary assigned path increments, 162–164 | On a bad edge the assigned sign may be either `+3` or `-3`; the maximal increment `+3` dominates both. The closing maximal increment is at least -1, so a path sum greater than `3t+1` would force cycle sum greater than `3t`. Reverse the path and negate its assigned increments for the lower bound; reversal preserves `B_t`. | Pass. |
| Filled gaps and contradiction, 165–171 | The deficit unit need not be the clean unit used earlier for generation. Its selected proper word has mean `mu` with absolute value greater than 1; it supplies valid `+/-1` or `+/-3` increments along the possibly bad unit cycle. A unit visits all `n` vertices, so total increment is `n mu`. The vertices with residue `i mod q` occur every `q` steps because the unit remains invertible mod `q`; `q|n` partitions the cycle into `n/q` designated length-`q` gaps. Reversing orientation negates the mean and reverses the same gap graphs. Some gap then has sum greater than `q`, contradicting the winding bound. | Pass; the proof does not incorrectly require its positive-deficit unit to be clean. |
| Chord deduplication inside a gap, 69–71 and 169–171 | A length-`q` unit segment has `q+1` distinct vertices because `q<n`. Its unit edges give differences 1, and the inserted chords give every remaining difference `4,7,...,q`; these are precisely the edges of `B_t`. Different edges of this copy map to different undirected graph edges because the vertex map is injective. Extra edges from other chord types are harmless, as the proof needs a copy of `B_t`, not an induced copy. Thus its number of bad edges is at most the global number `r<=t`, despite deduplication elsewhere. | Pass; `q<n` is the necessary injectivity assumption and is present. |

Two notation details deserve explicit explanation but do not create counterexamples. First, for a bad direction the quantity denoted `theta_s` in (7) is the **mean of the selected three-step word**, not the mean of a single proper generator. The proof uses only its displayed congruence and magnitude bound; it never assumes all these selected means form one additive functional on bad directions. Second, if a chosen unit `a_i` is the negative of the representative in `J`, reverse that representative's word and reverse all its steps. Its increment at `v` is the negative of the original word increment at `v-a_i`; the mean changes sign and its absolute value is unchanged. Inverse closure guarantees all reversed steps remain proper. This supplies the harmless orientation extension used in the last paragraph. [Source, lines 56–61 and 124–171](<./seed-current-text.txt:56>)

### Gaps

- This section verifies the criterion conditional on its four hypotheses; it does not independently establish the character-rigidity hypothesis (iv).
- No finite enumeration or Lean execution was used as evidence for these general claims. The reasoning above covers every allowed parameter value.

## Do the punctured colorings and three-step word construction work for every required vertex and direction?

### Takeaway

Yes, under the integer-parameter facts invoked by the source. The punctured coloring works separately at every vertex, and the §7 coordinate construction produces enough choices to avoid previously used direction pairs. No missing factor of two, within-word distinctness assumption, or endpoint exception was found.

### Cited Findings

- The explicit coloring at a removed vertex `v` is `c_v(u)=[[a_i^(-1)(u-v)]_n]_3`, where `i=[v]_q`. Core edges and the two chord cases are treated separately. [Source, §2.1, lines 72–84](<./seed-current-text.txt:72>)
- The generic direction conditions and normalized-coordinate identity are (25)–(26). Section 7 specifies exact coordinate sums, splits them into three generic coordinates, and chooses actual representatives in short intervals before applying finite-set avoidance. [Source, lines 264–290 and 407–467](<./seed-current-text.txt:264>)

### Inferences

**Punctured coloring, lines 72–84.** Condition (i) says every normalized core direction is either `+1`, `-1`, or has least representative `2 mod 3`. In the last case, the color difference is 2 without wrapping and `2-n=1 mod 3` after wrapping. For a `+/-1` edge, the only wrapping edges touch normalized coordinate zero, which has been deleted. Thus every remaining core edge is proper.

For a chord of type `i`, the normalized forward length is `ell=1 mod 3`. A wrap would be bad, so this is the delicate case. The chord lies in a designated length-`q` unit segment from a vertex `x=i mod q`. Its strict interior contains no vertex of residue `i mod q`: if `0<k<q`, then `k a_i` is nonzero modulo `q` because `a_i` is a unit modulo `q`. The deleted vertex `v` has precisely that residue, and therefore cannot lie in the chord's strict forward arc. If it is an endpoint, the chord is removed. Otherwise the normalized chord does not wrap past coordinate zero and its color difference is 1. For a chord of type `j!=i`, Condition (ii) gives normalized length `2 mod 3`, so the earlier wrap-safe argument applies. This proves a proper coloring for **each** `v`, including all chord endpoints and all residue classes. [Source, §2.1](<./seed-current-text.txt:72>)

**Target cases and coordinate sums, lines 407–431.** A target `z` in `J` is either 1 or `2 mod 3`. If nongeneric it is a positive chosen unit: all negative chosen units exceed `n/2`. With `W=z+cn`, choosing `c=2` at `z=1` and `c=1` otherwise gives `W=0 mod 3` and `n<W<=2n+1`. For every `j>=1` the three cases for `M_j` satisfy all four assertions in (43):

| Target case | Exact checks |
|---|---|
| `z=1` | `M_j=a_j+kappa_j-2`. Since `a_j=2 mod 3`, `kappa_j=0 mod 3`, this is divisible by 3. The facts `6<=kappa_j<a_j` imply `a_j<M_j<2a_j`. Modulo 5 it is -1, equal to `z-c`. Modulo `a_j` it is `kappa_j-2=kappa_j(1+2n)` because `kappa_j n=-1`. |
| `z=a_j` | `M_j=2a_j-1` is divisible by 3, strictly between `a_j` and `2a_j`, and is -1 modulo both 5 and `a_j`; these equal `z-c mod 5` and `kappa_j(a_j+n) mod a_j`. |
| Other targets | `M_j=a_j+e_j(z)-1`. Here `e_j(z)=2 mod 3`, so its least representative lies between 2 and `a_j-3`. Hence the strict bounds and divisibility by 3 hold. Since `kappa_j=1 mod 5`, `e_j(z)=z mod 5`, giving the required common residue. Modulo `a_j`, `M_j=e_j(z)-1=kappa_j(z+n)`. For a different chosen unit, the asserted residue of `e_j(z)` follows from the short compatibility and formula (25); for a generic target it is the definition. |

These checks use the parameter facts `a_j=0 mod 5`, `a_j=2 mod 3`, `kappa_j=6 mod 15`, `kappa_j n=-1 mod a_j`, and `kappa_j` invertible modulo `a_j`, all explicitly supplied earlier. [Source, (14), (18), (25), and (42)–(43)](<./seed-current-text.txt:186>)

**Coordinate split and CRT compatibility, lines 432–445.** Write `m=M_j/3` and choose the greatest integer `E_j<=m` that is 2 modulo 15. Then `b_j=m-E_j` is an integer from 0 to 14. The three coordinates are `E_j,E_j,m+2b_j`; their sum is `M_j`. Each is `2 mod 3`. The inequalities `a_j<M_j<2a_j` and `a_j>100` give

`E_j > a_j/3-14 > 0`, and `0 < m+2b_j < 2a_j/3+28 < a_j`.

Their residues modulo 5 are `2,2,z-c-4`, independently of `j`. Because all `a_j=5d_j` share only their factor 5, these common residues are exactly the compatibility needed for the CRT. Inverting `kappa_j` modulo `a_j`, and prescribing residue 2 modulo 3, therefore gives the three generic classes modulo `L=lcm(3,a_1,...,a_(q-1))`. Their sum agrees with `W` modulo each `a_j` by (43), and modulo 3 because both sums are zero; hence it agrees modulo `L`. [Source, (16), (43)–(45)](<./seed-current-text.txt:432>)

**Actual representatives and forbidden directions, lines 446–467.** Each of `s_1,s_2` is chosen in an interval of length `n/12`; a residue class modulo `L` has at least `n/(12L)-1` representatives there. The interval is strictly within `(0,n)`, since `n<W<=2n+1` and the parameters give `n>2`. Setting `s_3=W-s_1-s_2` puts it in the required third class and within `n/12` of `W/3`, also strictly within `(0,n)`. Consequently each such integer represents a distinct residue modulo `n`.

After adjoining the possible involution, the forbidden set has size at most `6r+3`. There are more than `2(6r+3)` choices for either of the first two representatives because the displayed size hypothesis `n>1000(r+1)qL^2` is much stronger than that inequality. Choose an allowed `s_1`. For fixed `s_1`, forbidding `s_2` excludes at most `6r+3` choices; forbidding `s_3=W-s_1-s_2` excludes at most another `6r+3`, since this map is injective on the candidate interval. Thus a valid `s_2` remains. All three summands are generic and avoid the only excluded involution, so they belong to `S` and sum to `z mod n`.

Initially forbidding `z,-z` excludes the target pair. After each word, forbidding both signs of its three directions increases the forbidden-set size by at most 6. Before word number `r`, its size is at most `2+6(r-1)`, within the lemma's bound `6r+2`. Repeated directions inside a word only reduce this count; they are not prohibited or needed to be distinct. The resulting words have disjoint direction-pair sets **between words**, precisely the property used in the bad-pair argument. [Source, Lemma 7.1 and its application](<./seed-current-text.txt:455>)

### Gaps

- The recursive construction and short-compatible-ratio theorem in §3 were used through their explicit stated conclusions; they were not independently re-proved in this targeted pass.
- The precise identification of the generic classes used above is (25)–(26), which was checked for this interface. The later exact character classification of those classes is outside this pass.
- No short-word counting error or missing numerical lower bound was found.

## Does the final assembly satisfy the exact graph property claimed?

### Takeaway

The verified graph criterion converts its inputs into the exact `(4,r)` property, including equality after every vertex deletion and resistance to deleting any set of at most `r` distinct undirected edges. The final seed conclusion remains conditional in this crosscheck on the separately audited parameter and rigidity results; no Lean-build claim is made here.

### Cited Findings

- Section 4 defines `S` as the intersection of the normalized safe direction sets, removing the involution when present. Section 7's final proof assigns the four criterion hypotheses to the parameter, compatibility, word, and rigidity results. [Source, lines 254–290 and 470–473](<./seed-current-text.txt:254>)
- The criterion's last paragraph proves the four-color upper bound, the bad-edge obstruction, deletion tolerance, and exact vertex-criticality. [Source, lines 165–175](<./seed-current-text.txt:165>)

### Inferences

The assembly interfaces match as follows:

1. The earlier parameters give positive finite `n`, `n=1 mod 3`, `q=3t+1|n`, `t>=r`, `q<n`, and chosen distinct unit direction pairs. The size inequality is stronger than all small positivity, interval, and avoidance bounds used in §7.
2. The set `N_n` is inverse-closed because `n=1 mod 3`; multiplication by a unit preserves inverse closure and excludes zero. Their intersection and removal of the self-inverse element therefore give exactly the nonzero, non-involution, inverse-closed set required by the criterion. Compatibility places all chosen unit pairs in it.
3. Condition (i) follows directly from the intersection. For Condition (ii), the short ratio is positive and less than `n/q`; multiplying it by `ell<=q` gives a representative strictly below `n`, so no unnoticed wrap changes its residue. Since `ell=1 mod 3` and the ratio is `2 mod 3`, the required chord residue is 2.
4. Section 7 supplies exactly Condition (iii), as proved above. Proposition 6.1 is invoked to supply Condition (iv); this pass has not independently checked that proposition.
5. The punctured coloring gives `chi(G-v)<=3` for every vertex. Since `n>q>=4`, a vertex exists; coloring that vertex with a fresh fourth color gives `chi(G)<=4`. There is no need for the punctured colorings at different vertices to agree.
6. If a coloring proper on `G-F` existed for `|F|<=r`, every monochromatic edge of the same assignment on `G` would lie in `F`. It would therefore have at most `r` bad undirected edges, contradicting the criterion's winding argument. This proves `chi(G-F)>=4`; the original four-coloring restricts to `G-F`, proving equality. Taking `F` empty gives `chi(G)=4`.
7. If some `G-v` were two-colorable, adding a fresh color at `v` would three-color `G`. Therefore every already established three-colorable puncture has chromatic number exactly 3. This is the exact vertex-criticality convention in equation (1), not merely an upper bound on deletion colorings.

These are deductions from the [source definition and criterion](<./seed-current-text.txt:14>). They cover arbitrary distributed edge deletion sets and all vertices. No extra property of connected chord copies, absence of repeated chord descriptions, or monotonicity of a chromatic extremal function is used.

### Gaps

- The unresolved scope of this crosscheck is §3's full parameter proof and §§5–6's exact rigidity/rounding proof; those are assigned to the main seed auditor. Passing this targeted crosscheck is not by itself a certification of the complete seed theorem.
- No Lean build, dependency replay, broad literature search, or exhaustive finite graph search was performed. The source and original transfer manuscript were left unchanged.
- Within the assigned targets, no actual bug or counterexample was found. The few implicit extensions identified above (negative orientations, word means on bad directions, non-induced gap copies) are justified directly and do not require an additional hypothesis.
