# Erdős 168: boundary components and the single-root theorem

The patched finite-cover formula and #168(ii) remain unproved. This round proves the sharp deficiency bound for every removed-label component avoiding the vertical axis and containing at most one horizontal-axis label. It also gives an explicit charge controlling which boundary pockets can be filled. The remaining axis-avoiding obstruction is a component containing multiple horizontal-axis roots; components meeting the vertical axis require a further global argument.

## What does inclusion-minimal positive deficiency force?

### Takeaway

An inclusion-minimal positive-deficiency set avoiding the vertical axis has deficiency one. Its smallest numerical label is a horizontal-axis point. Apart from a singleton isolate, it necessarily contains the three labels of the known patch.

### Cited Findings

- The matching objective is `d(U)=|U|-nu(B(U))`, where U is contained in one color `j=a-b mod3`. Its north-parent baseline matches every label with b>=1. [Established matching reduction](<../../early-attacks/open-conjecture-transfer-search/168_grid.md>)
- A maximum-deficiency set can be normalized into disjoint simply connected positive components, each meeting b=0. [Proved hole normalization](<../../early-attacks/open-proof-gap-attacks/hole_filling.md>)

### Inferences

Throughout this section U avoids a=0. Call U critical if `d(U)>0` and every proper subset has nonpositive deficiency. Put m=|U|. For every u in U,

```
nu(B(U)) >= nu(B(U\{u})) >= m-1.
```

Thus `d(U)=1`. A minimum vertex cover W of `B(U)` has size m-1.

**Essential-cover property.** Every w in W uniquely covers edges belonging to at least two distinct labels of U. Here an edge is uniquely covered by w if its other endpoint is not in W. Otherwise all edges uniquely covered by w have a single owner u, and `W\{w}` covers `B(U\{u})`, giving a proper positive-deficiency subset. If w uniquely covers no edge, it is already redundant. In particular a leaf cannot belong to W.

The owned edges of label u are

```
N(u)={u/3,2u/3},   if b>=1;
E(u)={u/2,3u/2},   if a>=1 and 3u<=2t;
R(u)={2u,3u},      if 3u<=t.
```

**The smallest label cannot have b>=1.** Suppose u is smallest in U and a,b>=1. The vertex u/3 is a leaf of N(u): its other possible owners are u/6 and 2u/9, both smaller. Hence `2u/3` belongs to W. Essentiality forces its other unique edge to be E(4u/3), since its remaining possible owner 2u/9 is absent. Consequently `4u/3` belongs to U, `2u` does not belong to W, and `2u<=t`.

Thus E(u) is present. Its endpoint u/2 is also a leaf: the other possible owners are u/6 and 3u/4, both smaller. Hence `3u/2` belongs to W. Essentiality now forces N(9u/2), with `3u` not in W. In particular `9u/2<=t`, so R(u) is present. Both endpoints 2u and 3u of R(u) are outside W, a contradiction.

Therefore the smallest label is `x=2^a`, with a>=1.

**The initial patch is forced.** If `x>2t/3`, x is isolated; its singleton already has positive deficiency, so criticality forces `U={x}`. Otherwise E(x) is present. The same leaf argument at x/2 forces `3x/2` into W and forces N(9x/2), with `3x` outside W. Thus `9x/2` belongs to U and `x<=2t/9`.

R(x) is therefore present and forces `2x` into W. Its only additional possible unique support is N(6x): the possible owner 4x/3 is nonsmooth because x is a pure power of two. Thus `6x` belongs to U and `4x` is outside W. In particular

```
{x,9x/2,6x} subset U,
x<=t/6,
{3x/2,2x} subset W,
{x/2,3x,4x} disjoint W.
```

Since U avoids the vertical axis, the forced label 9x/2 also shows that a>=2. If `6x<=t<27x/4`, these three labels themselves form a positive-deficiency set, so criticality forces U to be exactly this patch. Any genuinely different critical axis-avoiding obstruction must therefore start with `x<=4t/27` and continue beyond the patch.

### Gaps

These arguments do not by themselves exclude a continuation with several horizontal-axis labels. Inclusion-minimal positive deficiency and the maximal-cardinality hole normalization are different choices of representative; their additional properties must not be silently combined.

## Why are all single-horizontal-root obstructions now classified?

### Takeaway

For U avoiding the vertical axis, the north-parent baseline is maximum if and only if every available E/R edge has its left endpoint already matched by that baseline. The previously proved closure classification then shows that any positive-deficiency set with one horizontal-axis root contains the isolated-point or three-face patch obstruction.

### Cited Findings

- The bipartition has left color j+1 and right color j+2. The N baseline and its residual arcs are established in [the earlier matching analysis](<../../early-attacks/open-conjecture-transfer-search/168_grid.md>).
- The finite examples at t=18 and t=486 rule out, respectively, requiring one matching edge per label and rounding the unrestricted fractional optimum. Their exact certificates remain valid and are not used as replacements for the argument below. [Counterexamples and exact verifier](<../../early-attacks/open-proof-gap-attacks/cover.md>)

### Inferences

**Residual notation.** Put `Q={u in U:b(u)>=1}`. The baseline matches `u/3` on the left with `2u/3` on the right for every u in Q. Give a left physical vertex l the index 3l, and a right physical vertex r the index 3r/2. Some right indices may be nonsmooth; they are then automatically outside Q. A vertex is externally unmatched exactly when its index is not in Q.

After contracting baseline edges, the nonmatching arcs are

```
R(w): 6w -> 9w/2,
E(w): 9w/2 -> 3w/4.
```

Whenever a target index is in Q, its matched edge carries the path back to the left vertex of the same index. A target outside Q is an unmatched right endpoint. A residual path from an external left vertex to an external right vertex is an augmenting path. Both arc types decrease the a coordinate, so no directed cycle can occur.

**Rotation lemma.** Suppose `w in U`, `w<=4t/9`, and the left vertex with index `9w/2` is reachable from an external left vertex. Then an augmenting path exists.

Indeed E(w) is present because w avoids the vertical axis and `w<=4t/9<2t/3`. Put `q=3w/4`. If q is not in Q, E(w) exits at an external right endpoint. If q is in Q, then q is in U, avoids the vertical axis, and

```
3q=9w/4<=t.
```

Therefore R(q) is present and begins at the same left index `6q=9w/2`. Follow it to index `9q/2`. If that index is outside Q, this already exits at an external right endpoint. Otherwise follow its baseline edge and repeat with w replaced by q. Each replacement decreases a by two and preserves the required upper bound on w. Since U avoids a=0, iteration cannot continue indefinitely. An external right endpoint is reached. This proof explicitly permits an early R-edge exit; it does not assume all exits use E edges.

**Zero-augmentation theorem.** Assume the baseline has no augmenting path.

First, no R edge can have an external left source. If R(w) did, then `w<=t/3`. Its right target either is external immediately or leads to the reachable left index `9w/2`; the rotation lemma applies because `w<=t/3<4t/9`.

Second, no E edge can have an external left source. Suppose otherwise and choose its smallest numerical owner w. If `w<=4t/9`, the rotation lemma applies directly at its external source. If `w>4t/9`, E(w) being present implies `w<=2t/3`. Absence of augmentation forces its target `q=3w/4` into Q. Thus

```
t/3 < q <= t/2.
```

E(q) is present, and its left index `9q/2>t` is external. This is a smaller external E owner, contradicting the choice of w.

Consequently every E/R left endpoint is baseline-matched. Conversely, if all those endpoints are matched, the N baseline saturates every left vertex incident to B(U); it is maximum. Equivalently, no augmentation occurs exactly when

```
6u in U whenever R(u) is present,
9u/2 in U whenever E(u) is present.
```

The generated labels have positive b, so membership in U here is the same as membership in Q.

**Classification of the closed sets.** For completeness, the earlier elementary classification is reproduced. Such a set cannot contain a point in `(t/6,t/3]`, since R generates `6u>t`; nor can it contain a point in `(t/3,2t/3]`, since E generates `9u/2>t`. Thus every label is low, at most t/6, or high, exceeding 2t/3.

Starting at a low label u, repeatedly multiply by 6, and let p be the last low label in this sequence. Both `6p` and `9p/2` must be high, forcing

```
4t/27 < p <= t/6.
```

If an earlier step occurred, its predecessor `q=p/6` generates `r=9q/2=3p/4`, which lies in `(t/9,t/8]`. Since r belongs to U and avoids the vertical axis, its E edge generates `9r/2`, lying in `(t/2,9t/16]`, the forbidden middle interval. Hence no earlier step occurred. Therefore

```
U subset (4t/27,t/6] union (2t/3,t].
```

There is at most one horizontal-axis root in the low interval and at most one in the high interval. They cannot both occur: if the low root is x, then `6x<=t<27x/4<8x`, so the largest pure power of two at most t is 4x, which is at most 2t/3. Thus the high interval has no horizontal-axis root.

**Single-root conclusion.** Suppose U avoids the vertical axis and has exactly one horizontal-axis root. Its N baseline has size `|U|-1`. If d(U)>0, this baseline must already be maximum; apply the zero-augmentation theorem and the classification.

- A high root is an isolated point and is itself a positive-deficiency subset.
- A low root x satisfies `6x<=t<27x/4`, and closure forces `{x,9x/2,6x}` into U. This is the known positive-deficiency patch.

In particular

```
d(U) <= I_j(t)+P_j(t)
```

for every axis-avoiding U with at most one horizontal-axis root, for any baseline color j. The no-root case follows directly from the N matching. If U is critical and has one root, it is exactly the isolate or the three-face patch.

By additivity across the face components in the hole normalization, the same sharp bound holds whenever every positive axis-avoiding component has at most one horizontal-axis root: disjoint components cannot both contain the sole possible exceptional root.

### Gaps

For two or more roots, positive deficiency does not imply that the N baseline is maximum: it may have some augmentations but fewer than the number required. The theorem proves existence of an augmentation, not enough mutually disjoint augmentations.

For bookkeeping set `k=a+2b` and `n=(k-j)/3`. An owner `(n,b)` activates

```
R: (n+1,b+1) -> (n+1,b+2),
E: (n+1,b+2) -> (n,b+1).
```

R arcs stay on a k-row and E arcs drop k by three. Internal matched vertices of rotation paths on distinct rows are disjoint, but the full paths need not be: an early R exit can coincide with another row's E exit. Source ownership can also merge, as `6*(6x)=(9/2)*(8x)`. An earlier suggestion that distinct k alone proves disjoint complete paths was incorrect and is explicitly withdrawn here.

## What does the boundary-pocket charge prove, and what remains open?

### Takeaway

The hole-filling argument extends to truncated boundary regions with an explicit signed charge. A maximal-cardinality deficiency maximizer can leave a complementary pocket only if its charge is positive enough. This provides a precise boundary condition, but does not yet control multi-root components.

### Cited Findings

- The full-region proof establishes `I+B/2=2m+1-h` and the abstract perfect matching of complementary boundary edges. [Global hole-filling proof](<../../early-attacks/open-proof-gap-attacks/hole_filling.md>)
- Three narrowly targeted MILP checks sought an improvement over a winning color while retaining at least one vertex of its known patch and fixing the vertical-axis vertices of that color in the cover. At t=1536,3072,24576, the solver reported infeasibility. These are numerical reports, not exact infeasibility certificates. [Targeted checker](<test_alternative_patch.py>), [Results](<alternative_patch_results.json>)

### Inferences

**General boundary extension.** Let V be a finite connected set of m omitted-color faces disjoint from U, all with centers in the finite board. Its full geometric polyhex has h holes, I interior vertices, and B boundary vertices. Let P be the abstract perfect matching of boundary edges whose owners lie outside V. Partition its edges as follows:

```
p2: both endpoints in D_t and the edge already in B(U);
q2: both endpoints in D_t but the edge absent from B(U);
p1: exactly one endpoint in D_t;
p0: neither endpoint in D_t.
```

Thus `B/2=p2+q2+p1+p0`. There are `A=2p2+2q2+p1` available boundary vertices, and put

```
z=A-p2=B/2+q2-p0.
```

Take a maximum matching after adding V and fix all its edges outside the polyhex one-skeleton, including edges in holes. If b available boundary vertices remain unoccupied, the matching inside uses at most `floor((I+b)/2)` edges. The p2 old matching edges leave at least `max(0,p2-(A-b))=max(0,b-z)` compatible edges. Here `0<=z<=A`, so maximizing the possible replacement loss over `0<=b<=A` gives

```
nu(B(U union V))-nu(B(U))
   <= floor((I+z)/2)
    = m+floor((1-h+q2-p0)/2).
```

The same inequality remains valid if any interior vertex were unavailable, because I is only an upper bound on usable interior vertices. In the present convex weighted triangle all interior vertices are in fact available: each is the average of its three incident V face centers.

Consequently filling V does not decrease deficiency whenever `q2-p0<=h`.

**Explicit charge for a complementary component.** Suppose V is a component of `C_j(t)\U`. A complementary owner inside the board is then in U; otherwise it would belong to the same component V. Hence a q2 edge must have its owner outside the board. For a label `v=2^a3^b` in V, its three complementary-owner edges are

```
owner v/6:   edge {v/3,v/2};
owner 4v/3:  edge {2v/3,2v};
owner 9v/2:  edge {3v/2,3v}.
```

Only the last can contribute q2: exactly when `a>=1` and `2t/9<v<=t/3`. The p0 cases are respectively:

```
v=1;
b=0 and v>t/2;
v>2t/3, or a=0 and v>t/3.
```

Each counted edge has its owner outside the board and therefore outside V, so no extra boundary indicator is needed. The signed charge is the additive quantity

```
q2-p0 = sum_{v in V} sigma_t(v),

sigma_t(2^a3^b)
 = 1_[a>=1, 2t/9<v<=t/3]
   -1_[v=1]
   -1_[b=0, v>t/2]
   -1_[v>2t/3 OR (a=0, v>t/3)].
```

For a maximizer of d chosen with maximal cardinality, every nonempty remaining complementary component V must therefore satisfy

```
sum_{v in V} sigma_t(v) >= h(V)+1.
```

Otherwise filling it would preserve or increase d and increase cardinality. This states a necessary condition on boundary-attached pockets; it is not yet a bound on d(U).

**Additional boundary contacts.** The N, E, and R edges each form a matching when all edges of that type are present. Hence a positive-deficiency component must contain a missing edge of every type. It must touch b=0; it must also have either a vertical-axis label or a label exceeding 2t/3; and it must contain a label exceeding t/3. Thus a positive component avoiding the vertical axis connects the horizontal axis to the outer band above 2t/3.

### Gaps

The outstanding case is a simply connected positive component avoiding the vertical axis but meeting the horizontal axis at least twice. Several roots may share sources, sinks, or internal matching bottlenecks. The explicit charge and zero-augmentation theorem do not yet supply the required number of disjoint augmentations. Components meeting the vertical axis additionally require a comparison between global color phases. No currently open conjecture has been solved here.

All three targeted numerical checks finished. No search sweep or process remains running, and no earlier-round folder was changed.
