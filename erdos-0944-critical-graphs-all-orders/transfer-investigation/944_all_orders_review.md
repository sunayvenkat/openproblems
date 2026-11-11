# Adversarial review of the all-orders transfer for Erdős 944

## Verdict and exact input

I found no mathematical gap in the proposed transfer. The following conclusion follows from the stated source theorem by an elementary finite graph construction:

> If a vertex-critical four-chromatic graph `G` on `g` vertices remains four-chromatic after deleting any set of at most `r` edges, then for every integer `N≥45g²` there is such a graph on exactly `N` vertices.

Consequently, the source existence theorem for every `r` implies the stronger assertion that, for each fixed `r`, **every sufficiently large order** admits such a graph. Equivalently, the maximum critical-edge-set size over four-vertex-critical graphs of order `N` tends to infinity with `N`.

The external input is Theorem 1.1 of Kruer–Kohlmeyer, *Vertex-critical four-chromatic graphs with no small critical edge set*, in `erdos-944.pdf.txt` in this directory. The source explicitly disclaims the every-sufficiently-large-order conclusion. I reviewed the transfer independently; I have not re-proved the source's cyclic/CRT existence theorem or established literature priority for the transfer.

Attribution update from the coordinator: the split-vertex terminal gadget is already Lemma 2.1 of Skottova–Steiner, [arXiv:2508.08703](https://arxiv.org/abs/2508.08703). The self-contained proof below should be cited to that source rather than described as a new gadget. The all-orders implication remains mathematically valid; whether it was previously recorded is a separate literature question.

## The terminal gadget and substitution

Put `q=3`. The robustness property of `G` is exactly:

> Every map `V(G)→{1,2,3}` makes at least `r+1` edges monochromatic.

Indeed, deleting all monochromatic edges of a coloring gives a three-colorable graph. Conversely, a proper three-coloring after deleting at most `r` edges has at most that many monochromatic edges in the original graph.

Choose `v∈V(G)` and a proper three-coloring `φ` of `G−v`. Split `v` into two nonadjacent terminals `a,b`. Attach to `a` precisely the neighbors of `v` with `φ`-color 1, and to `b` all other neighbors of `v`. Keep every edge of `G−v`. Call the resulting graph `S`.

The gadget has `g−1` internal vertices, and these four properties hold:

1. **Distinct terminal colors are feasible.** Extend `φ` with `a=2,b=1`. A permutation of the three colors realizes any specified distinct colors at `a,b`.
2. **Equal terminal colors cost at least `r+1` bad edges.** Identifying `a,b` recovers `G`, edge for edge, with no parallel edges or deleted edges. Thus a three-color assignment with equal terminal colors corresponds to a coloring of `G` with exactly the same number of monochromatic edges.
3. **Deleting an internal vertex permits equal terminal colors.** If `x` is internal, take a proper three-coloring of `G−x` and give both `a,b` the color of `v`. A color permutation realizes any prescribed common terminal color.
4. **Deleting either terminal leaves a three-colorable graph.** The coloring in item 1 restricted to that graph works. A color permutation realizes any prescribed color at the surviving terminal.

These properties remain valid if some terminal neighbor class is empty. In fact the source's four-chromaticity ensures that every color appears among the neighbors of `v` under `φ`, but the proof does not need this separately.

Now let `H` be a graph which is four-chromatic and becomes three-colorable on deleting **any edge or any vertex**. Replace every edge `xy` of `H` by a fresh copy of `S`, identifying its terminals with `x,y`; delete the original edge `xy`. Distinct gadget interiors are disjoint. Call the result `T(H)`.

**Four-colorability.** Properly four-color `H`. Every edge has distinct terminal colors, so item 1 extends the coloring to its gadget using those two colors and one other of the four colors. All extensions agree because gadgets overlap only in terminals.

**Robust non-three-colorability.** For an arbitrary three-color assignment to `T(H)`, its restriction to `V(H)` has a monochromatic edge `xy`, since `χ(H)=4`. The gadget on `xy` then contributes at least `r+1` monochromatic edges by item 2. All these are distinct edges of `T(H)`. Therefore deleting at most `r` edges cannot make `T(H)` three-colorable. Combined with four-colorability, the edge-deleted graph still has chromatic number four.

**Internal-vertex criticality.** Suppose `x` is internal to the gadget replacing edge `uv`. Color `H−uv` properly with three colors. Necessarily `u,v` have the same color, since otherwise this would color `H`. Use item 3 on the punctured gadget and item 1 on every other gadget. This gives a proper three-coloring of `T(H)−x`.

**Skeleton-vertex criticality.** Suppose a skeleton vertex `u` is deleted. Color `H−u` properly with three colors. For gadgets not incident with `u`, use item 1. Every incident gadget has lost exactly one terminal, so item 4 extends its surviving terminal color. This gives a proper three-coloring of `T(H)−u`.

In either deletion case the chromatic number is exactly three: if it were at most two, adding the removed vertex in a new color would three-color `T(H)`, contradicting four-chromaticity.

Finally,

`|V(T(H))| = |V(H)| + (g−1)|E(H)|`.

No edge-criticality of the source `G` is needed. Edge-criticality is needed only for the skeleton `H`, and this is why a mere vertex-critical skeleton would be insufficient.

## Critical skeletons, their orders, and the numerical threshold

Three suitable full four-critical skeletons are:

| Skeleton | Vertices | Edges |
|---|---:|---:|
| `K4` | 4 | 6 |
| Wheel on a five-cycle, with its hub | 6 | 10 |
| Mycielski graph of the five-cycle | 11 | 20 |

The first two are elementary. For the odd wheel, removing a rim edge leaves a path whose two-coloring extends by a third hub color. Removing a spoke permits the spoke's rim endpoint and hub to share a color, while the remaining rim path is two-colored. Edge-criticality implies vertex-criticality here since there are no isolated vertices.

For completeness, the Mycielski graph has vertices `v0,...,v4,u0,...,u4,w`, subscripts modulo five, and edges

- `vi v(i+1)`;
- `ui v(i−1)` and `ui v(i+1)`;
- `w ui`.

It is not three-colorable. If `w` has color 3, then every `ui` has color 1 or 2. Recolor any `vi` of color 3 with the color of `ui`. This would produce a proper two-coloring of the five-cycle, a contradiction. A proper four-coloring is obtained by three-coloring the cycle, giving each shadow its original's color, and giving `w` the fourth color.

There are three edge orbits under the graph's dihedral symmetries. The following proper three-colorings after deleting a representative edge prove edge-criticality. The tuple order is `v0,v1,v2,v3,v4,u0,u1,u2,u3,u4,w`; colors are `0,1,2`.

| Deleted edge | Coloring tuple |
|---|---|
| `v0 v1` | `(1,1,0,1,0,2,2,2,1,2,0)` |
| `u0 v1` | `(0,1,0,1,2,1,1,2,1,2,0)` |
| `w u0` | `(0,1,0,1,2,0,1,2,1,2,0)` |

I additionally enumerated all twenty edge deletions and found a proper three-coloring for each, and found none for the original graph. These computations only check this small skeleton; the displayed certificates and preceding argument make no reliance on a solver necessary.

**Hajós sums preserve the required criticality.** Take two disjoint four-critical graphs `H1,H2`, remove an edge `a1b1` from the first and `a2b2` from the second, identify `a1,a2` to `a`, and add `b1b2`. The result `J` has

`v(J)=v(H1)+v(H2)−1`, `e(J)=e(H1)+e(H2)−1`.

It is not three-colorable: in any three-coloring of each `Hi−aibi`, its two distinguished endpoints must agree. Their identification would force `b1,b2` to agree, violating the new edge. It is four-colorable by matching the colors at `a` and choosing distinct colors at `b1,b2` using color permutations.

For edge deletion, if the new edge is removed, combine three-colorings of the two edge-deleted summands. If an old edge `f≠aibi` in `Hi` is removed, use a three-coloring of `Hi−f`, where `ai,bi` necessarily differ because their original edge is present in that coloring; use a three-coloring of the other edge-deleted summand, whose distinguished endpoints agree. Align the colors at `a`. The new edge is then proper.

For vertex deletion, deleting `a` leaves `H1−a1` and `H2−a2` joined by the single new edge, handled by color permutations. Deleting `bi` removes the new edge and permits independent compatible three-colorings. Deleting any other vertex uses the punctured summand's three-coloring, in which `ai,bi` differ, and the edge-deleted other summand with equal distinguished endpoints. Thus every edge and every vertex is critical in `J`.

Start with `K4` and take any nonnegative numbers `a,b,d` of Hajós sums with the three skeletons. Put `c=g−1`. The resulting replacement graph has order

`4+6c + a(3+5c) + b(5+9c) + d(10+19c)`.

Set

`base=6g−2`, `A=5g−2`, `B=9g−4`, `C=19g−9`.

Then `9A−5B=2`. If `g` is odd, `A,B` are odd and hence coprime. All integers at least `(A−1)(B−1)` are nonnegative combinations of `A,B`. Therefore all orders

`N≥base+(A−1)(B−1)=45g²−46g+13`

occur.

If `g` is even, `A,B` are even, `gcd(A/2,B/2)=1`, and `C` is odd. Every sufficiently large even remainder is a combination of `A,B`; for odd remainders first subtract `C`. It is sufficient that

`N≥base+C+2(A/2−1)(B/2−1)=(45/2)g²−8g+1`.

Both displayed bounds are at most `45g²`. Thus **every integer `N≥45g²` is realized**, with the exact vertex-critical and edge-robust properties required.

The only coin theorem used is the elementary two-generator conductor bound. One can prove it directly: for coprime positive integers `u,v`, choose `b∈{0,...,u−1}` so that `bv≡n (mod u)`; if `n≥(u−1)(v−1)`, then `n−bv>−u`, so its being a multiple of `u` forces `n−bv≥0`.

### Checks against likely failure modes

- Gadgets contribute `g−1`, not `g` or `g+1`, new vertices per skeleton edge.
- The original skeleton edges must be removed, rather than retained alongside their gadgets.
- The two split terminals are nonadjacent, so equal colors can be used after deleting an internal vertex.
- A monochromatic skeleton edge is only a certificate selecting one gadget; it is not itself counted as a retained edge.
- Only one such gadget is needed for the robustness lower bound, so no averaging or independence assumption occurs.
- The Grötzsch graph's edge-criticality is necessary and has explicit finite certificates above.
- The parity case distinction is correct: `g` odd corresponds to `c` even.
- The result proves all sufficiently large orders for each fixed `r`, not a claimed explicit growth rate in `N` without a bound on the source size `g(r)`.
