# Exceptional patch deletion and a common-cover reduction

Research derivation and independent audit, 7 November 2026. The single-owner compatibility lemma and the independently checked high-prefix repair now close the aggregate cases of the finite-cover argument, using the preceding inputs explicitly cited below. The assembled finite theorem is ready for fresh-context adversarial review. This is not a proof of #168(ii) irrationality. No independent-component or arbitrary-boundary normalization is assumed.

## What can be proved when the exceptional owner is deleted?

### Takeaway

For any single forbidden owner, the unrestricted and restricted maximum deficiencies differ by either zero or one. In both cases there exists a single global optimum whose omitted owners, after the prescribed exclusion, maximize the restricted deficiency. This argument does not use the geometry of the patch and includes its small vertical-axis exception.

### Cited Findings

- The exact matching reduction is \(\tau=K_j-\max_{U\subset C_j}d(U)\), where \(d(U)=|U|-\nu(B(U))\). Its cover correspondence and canonical interpretation are proved in [canonical_phase.md](<../global-boundary-proof/canonical_phase.md>).
- The only possible axis-avoiding critical sets are the isolate and the patch. Excluding their unique exceptional horizontal root therefore removes all positive axis-avoiding sets. [Classification](<../../early-attacks/augmentation-and-return-attacks/multiroot.md>); [independent audit](<../global-boundary-proof/combinatorial_and_coefficient_audit.md>).
- An active patch has \(e=2^A\), \(A\ge1\), and \(6e\le t<27e/4\). The three omitted patch owners are \(e,9e/2,6e\). When \(A=1\), the middle owner is vertical; its actual critical interval extends to \(t<18\), beyond the sufficient construction-indicator window. [Exact incidence analysis](<../global-boundary-proof/vertical_critical.md>).

### Inferences

Fix a color \(p\) and a board owner \(e\in C_p\). Set
\[
D=\max_{U\subset C_p}d(U),\qquad
D^*=\max_{U\subset C_p\setminus\{e\}}d(U).
\]
The empty set is permitted. For every \(U\) containing \(e\), edge inclusion gives
\[
\nu(B(U))\ge\nu(B(U\setminus\{e\})),
\]
and hence
\[
d(U)\le d(U\setminus\{e\})+1\le D^*+1.
\tag{G1}
\]
If \(e\notin U\), directly \(d(U)\le D^*\). Together with the inclusion of allowed pools this proves
\[
\boxed{D^*\le D\le D^*+1.}
\tag{G2}
\]
No upper bound on the number of edges owned by \(e\) is used. Removing an owner can raise deficiency, but cannot lower it by more than one; (G1) has precisely the required direction.

There are exactly two cases.

1. **\(D=D^*+1\).** Every unrestricted maximizer contains \(e\), since a maximizer excluding it would have deficiency at most \(D^*\). For every such maximizer,
   \[
   D^*\ge d(U\setminus\{e\})\ge D-1=D^*,
   \]
   so deletion gives a restricted maximizer. In particular this works for the omitted owner set of every global minimum corner cover.
2. **\(D=D^*\).** Choose any restricted maximizer \(V\) and a minimum vertex cover \(W\) of \(B(V)\). Then
   \[
   F=(C_p\setminus V)\cup W
   \]
   is a corner cover of size \(K_p-D^*=K_p-D=\tau\). It contains \(e\), and its omitted color-\(p\) set is already the restricted maximizer \(V\).

Thus there is a common global minimum cover \(F\) such that
\[
V_p=(C_p\setminus F)\setminus\{e\}
\quad\text{attains }D^*.
\tag{G3}
\]
In the zero-drop case, \(e\in F\), so the displayed deletion does nothing. For every other color \(j\), the same \(F\) has omitted set \(C_j\setminus F\) attaining \(D_j=K_j-\tau\). To see this, its non-\(j\) part covers the corresponding graph; a smaller graph cover or larger deficiency would yield a smaller original cover. There is no need for \(F\) to be simultaneously canonical in several colors.

The equivalent optimization statement is
\[
\tau_{e\in F}=K_p-D^*\in\{\tau,\tau+1\}.
\]
This identifies exactly the two cases above. The argument works for one excluded owner; it does not assert the analogous compatibility after an arbitrary multiple-owner deletion.

One targeted exact check was made at \(t=96,e=16\), using the existing integer matcher: all 128 subsets of color 1 gave \(D=1,D^*=0\), with the empty set the smallest restricted maximizer. Every subset containing 16 was independently checked against (G1), and \(K=(7,7,6)\) was asserted. This is a bounded consistency check, not the proof of (G1)–(G3), and does not establish that the one-unit case always holds for patches. No broad board sweep was run.

### Gaps

No claim is made that deleting every active patch root always lowers maximum deficiency by exactly one. That stronger claim is unnecessary for the common-optimum argument and was not proved or refuted by the single finite check.

## What aggregate collision statement now includes active patches?

### Takeaway

For \(t\ge18\), the same common-cover collision reduction applies with an active patch. Any counterexample to the candidate formula must be exactly one below the candidate, and the adjusted top-vertical color must be a minimizing phase supporting an incomparable-root restricted critical set.

### Cited Findings

- The restricted-maximizer root balance, explicit prefix repairs, and mandatory small-owner table are (P1)–(P2) and the following table in [canonical_audit_and_collision.md](<../boundary-dominance/canonical_audit_and_collision.md>). That source labels the prefix statements as pending separate independent audit. The local uses relevant here were checked directly below; the present compatibility lemma does not strengthen any unproved high-family comparison.
- For an incomparable-root restricted maximizer, the vertical-strip dichotomy and the exclusion of the deep branch force its least vertical owner to exceed \(t/3\). [Deep-branch proof](<../boundary-dominance/deep_branch.md>); [independent vertical audit](<../boundary-dominance/vertical_audit_and_transfer.md>).

### Inferences

Write \(p=c(e)\) for the active patch color, \(P_p=1\), \(P_j=0\) otherwise, and
\[
M=\min_j(K_j-P_j),\qquad
q=c(3^{\lfloor\log_3t\rfloor}).
\]
No isolate coexists with an active patch: \(6e\le t<27e/4<8e\), so the largest pure power of two is \(4e\le2t/3\).

Suppose \(\tau<M\). Then \(D_j=K_j-\tau>P_j\) for every color. Set \(D_p^*\) as above and \(D_j^*=D_j\) for \(j\ne p\). By (G2), every \(D_j^*>0\). Choose the common optimum (G3), and put
\[
V_p=(C_p\setminus F)\setminus\{e\},\qquad
V_j=C_j\setminus F\quad(j\ne p).
\]
Each \(V_j\) is a maximizer in its allowed pool. Each contains an inclusion-minimal maximizing subset, and these subsets inherit the strict owner expansion and essential-cover properties because deleting owners stays within the pool. They are not initially being assumed critical or independent.

The preceding prefix arguments give the following fact for an allowed-pool minimal maximizer outside color \(q\):
\[
\begin{array}{c|ccc}
j&0&1&2\\\hline
\text{mandatory omitted owner}&6&12&18.
\end{array}
\tag{G4}
\]
The same owner is forced for the top color if its least roots are degenerate or include the origin. For clarity, the local checks behind this use are:

- In the origin case, \(R(1)\) forces at least one of 2 and 3 into the graph cover. Both cannot be selected, because each would then have at most one uniquely supported owner. The selected one forces owner 6.
- In color 1, the remaining configurations are \((A,B)=(1,2)\), whose first horizontal strip forces 12, and \((A,B)=(4,2)\), whose vertical chain contains 12.
- In color 2, \((A,B)=(2,4)\) has horizontal chain \(4,18,81\). The other configuration \((A,B)=(2,1)\) has vertical chain \(3,4\); when its rooted edge at 3 is available, essentiality forces owner 18. Its stronger edge-availability requirement can exclude additional small boards, but does not weaken the mandatory-owner conclusion for any configuration that exists.
- The explicit prefix additions are disjoint from the existing cones. In the \(a+2b\) case their owners are at most \(x/8\le t/12\); in the \(2a+b\) case they are at most \(y/27\le t/27\). Neither can insert the excluded patch root \(e>4t/27\). No hidden exception to the allowed pool is introduced.

Since every maximizing set contains such a minimal maximizing subset, (G4) concerns omitted owners of the **same** \(F\). None of 6, 12, 18 is a pure power of two, so none is the removed owner \(e\). If the top color also had a degenerate or origin-containing minimal maximizer, the whole corner \(\{6,12,18\}\) would be omitted from \(F\). This corner exists for \(t\ge18\), giving a contradiction.

The top color therefore has an incomparable-root minimal maximizer \(U\). Its vertical owner \(y>t/3\) is the only vertical owner it can contain: the next vertical owner of that color is \(27y>t\). Removing \(y\) leaves an allowed axis-avoiding set, whose deficiency is nonpositive. By the same monotonicity argument as (G1),
\[
0<D_q^*=d(U)\le d(U\setminus\{y\})+1\le1.
\]
Thus \(D_q^*=1\). Inclusion-minimality now really does make \(U\) critical: all proper subsets have deficiency strictly below the maximum 1, hence at most zero.

If \(p\ne q\), then \(D_q=D_q^*=1\) and \(\tau=K_q-1\). Since \(\tau<M\le K_q\), integrality gives \(M=K_q\). If \(p=q\), the counterexample hypothesis gives \(D_q\ge2\); (G2) and \(D_q^*=1\) force \(D_q=2\), so \(\tau=K_q-2\) and \(M=K_q-1\). Equivalently, in both cases,
\[
\boxed{M=K_q-P_q,\qquad \tau=M-1.}
\tag{G5}
\]
When the patch is in the top color its deficiency drop is forced to be exactly one **under this counterexample hypothesis**; no unconditional exact-drop theorem has been used.

#### The small active patch

The only active patch below 18 is \(e=2\), \(12\le t<27/2\). Throughout this interval the board is \(D_{12}\), with \(K=(3,3,2)\), \(P=(0,1,0)\), and \(M=2\). The disjoint corners \(\{1,2,3\}\) and \(\{4,8,12\}\) require two selected points. The cover \(\{3,4\}\) attains two. Thus \(\tau=M\), treating the vertical middle owner 9 exactly, without invoking the \(t\ge18\) collision.

### Gaps

(G5) by itself is a reduction, not a contradiction. Section 3 now closes it using the independently checked high-prefix repair and finite table. The argument does not presume that independent critical subsets contribute additive deficiency, that every optimum has a complete vertical phase, or that an arbitrary boundary word can be replaced by a phase.

## Does the high-prefix repair close every remaining aggregate case?

### Takeaway

**Independent audit: PASS.** The high-prefix repair excludes every remaining \(r=1,s\ge4\) restricted maximizer. The four smaller incomparable configurations have a strictly losing adjusted top phase. Together with the common-optimum lemma, the already audited reductions, and the explicit base cases below, this gives a complete proposed proof of the global finite formula for fresh-context review.

### Cited Findings

- The new high-prefix argument being independently checked is H1–H3 in [high_phase.md](<high_phase.md>). The reconstruction below checks all new-owner incidences and the missing frontier point explicitly.
- The preceding reduction leaves \(r=2,s=1\), \(r=1,s=1\), and \(r=1,s\ge2\) with \(64\cdot9^{s-1}\le t<8\cdot9^s\). Its edge cutoffs and exceptions were independently audited in [vertical_audit_and_transfer.md](<../boundary-dominance/vertical_audit_and_transfer.md>).
- The upper construction \(\tau\le\min_j(K_j-I_j-P_j)\) is established in [168_grid.md](<../../early-attacks/open-conjecture-transfer-search/168_grid.md>). The matching, root, and prefix inputs used for the lower bound are identified in Sections 1–2.

### Inferences

#### Independent reconstruction of the high-prefix repair

Let \(U\) be an inclusion-minimal maximizer in the allowed pool, with positive maximum deficiency \(D^*\), and let \(W\) be a minimum cover of \(B(U)\). Assume its least axis roots belong to the remaining high family
\[
r=1,\quad s\ge2,\quad A=s+2,\quad
x=2^A,\quad y=3^{2s+1},\quad z=4\cdot9^s.
\]
Thus \(y>t/3\), and the forced horizontal chain is
\(u_n=xq^n\), \(0\le n\le s\), where here \(q=9/2\). This use of \(q\) is a multiplier, not the top-color index of Section 2. Write \(g=4/3\) and introduce
\[
k=2a+b,\qquad k_0=2A=2s+4.
\]

In coordinates \(u=xg^m q^n\),
\[
a=A+2m-n,\quad b=2n-m,\quad k=k_0+3m.
\]
The horizontal cone has \(m,n\ge0\), while the vertical cone based at \(y=xg^{-1}q^s\) has \(m\ge-1,n\ge s\). Below \(k_0\), only \(m=-1\) is possible. Then \(a=s-n\ge0\) and \(n\ge s\) force \(n=s\), namely the single point \(y\). Consequently
\[
U\cap\{k<k_0\}=\{y\}.
\tag{H1}
\]
This is an exact intersection statement, not forward closure of either cone.

Let \(P_0\) consist of all preferred-color points on diagonals
\[
k_0-3,\ k_0-6,\ldots\ge0,
\]
and put \(P=P_0\setminus\{y\}\). Let \(L\) consist of all left-color points on diagonals
\[
k_0-4,\ k_0-7,\ldots\ge0.
\]
All of these points are on the board: the largest numerical point on \(2a+b=k\) is \(3^k\), and the top owner diagonal is \(k_0-3=2s+1\), with maximum \(y\le t\). The added cover points are at most \(y/3\). By (H1), \(P\cap U=\varnothing\).

The forced chain selects
\[
3u_n/2=2^{s+1-n}3^{2n+1}\in W,
\qquad 0\le n<s.
\tag{H2}
\]
These are exactly the points on frontier \(k=k_0-1=2s+3\) with \(a=2,3,\ldots,s+1\). The only other nonnegative points on that diagonal are \(2y\), at \(a=1\), and \(9y\), at \(a=0\). The latter is off-board since \(t<3y\). The former need not be selected; in fact the forced vertical chain excludes it from \(W\).

Every available new north or east edge has its left endpoint on diagonal \(k-1\), hence in \(L\). A rooted edge from any lower added owner likewise has left endpoint on an \(L\) diagonal. A rooted edge from the top new owner diagonal has left endpoint on frontier \(k_0-1\), where (H2) covers every possibility except \(2y\) and the off-board point \(9y\).

There is no missing new edge at \(2y\). Its complete possible owner list is
\[
y\quad(R),\qquad 4y/3=z\quad(E),\qquad 6y\quad(N).
\]
Only \(y\) lies below \(k_0\), and it was removed from \(P\) because it already lies in \(U\). The other two owners have diagonal \(k_0\) and are not new; moreover \(6y>t\). Also \(R(y)\) is unavailable because \(y>t/3\). Thus every newly owned edge is covered by \(W\cup L\). Existing edges remain covered because no point of \(W\) is removed. Doubly covered edges cause no difficulty.

The exceptional owner remains excluded. Any new pure power of two has even diagonal. The largest even preferred diagonal below \(k_0\) is \(k_0-6\), so its value is at most \(2^{A-3}=x/8\le t/8\). A possible exceptional patch root is greater than \(4t/27>t/8\), and an isolate is greater than \(2t/3\). Thus \(P\) contains neither possible forbidden owner.

The number of nonnegative points on diagonal \(2a+b=k\) is \(h(k)=\lfloor k/2\rfloor+1\), with \(h(-1)=0\). Pair each owner diagonal \(k_0-3n\) with left-cover diagonal \(k_0-3n-1\). Their count difference is one precisely when \(n\) is even. Therefore
\[
|P_0|-|L|=\lfloor A/3\rfloor,
\quad
|P|-|L|=\lfloor A/3\rfloor-1
=\left\lfloor\frac{s-1}{3}\right\rfloor.
\tag{H3}
\]
It follows that
\[
d(U\cup P)
\ge |U|+|P|-|W\cup L|
\ge D^*+\left\lfloor\frac{s-1}{3}\right\rfloor.
\]
Overlap between \(L\) and \(W\) only strengthens this inequality. For \(s\ge4\) the gain is positive, contradicting maximum deficiency in the allowed pool. The augmentation is an allowed set on the original board; it requires neither a smaller-board induction nor a replacement of an arbitrary boundary word.

#### Exact audit of every surviving incomparable interval

The following are all surviving incomparable cases. Each listed interval is left-closed and right-open. Write \(\delta=I+P\) and let \(q\) again denote the top vertical color.

| Case | Interval | \(K\) | \(I\) | \(P\) | \(q\) | \(K-I-P\) |
|---|---|---|---|---|---|---|
| \(r=s=1\) | \([54,64)\) | \((6,5,5)\) | \((0,0,0)\) | \((0,0,0)\) | 0 | \((6,5,5)\) |
| \(r=s=1\) | \([64,72)\) | \((7,5,5)\) | \((1,0,0)\) | \((0,0,0)\) | 0 | \((6,5,5)\) |
| \(r=2,s=1\) | \([216,243)\) | \((9,8,9)\) | \((0,0,0)\) | \((0,0,0)\) | 2 | \((9,8,9)\) |
| \(r=1,s=2\) | \([576,648)\) | \((12,12,11)\) | \((1,0,0)\) | \((0,0,0)\) | 1 | \((11,12,11)\) |
| \(r=1,s=3\) | \([5184,5832)\) | \((20,19,20)\) | \((1,0,0)\) | \((0,0,0)\) | 2 | \((19,19,20)\) |

Integer counting checked every entry, that no smooth vertex lies in the interior of any listed interval, and that no isolate or patch threshold lies there. The adjusted top phase is strictly larger than the minimum in every row. In particular, none of these intervals has an active patch. These are exact finite certificates, not MILP reports or a broad search for an optimum.

For reproducibility, the following complete assert-based calculation was run successfully without a solver or file mutation:

```python
from fractions import Fraction
cases = [(54,64,0),(64,72,0),(216,243,2),(576,648,1),(5184,5832,2)]
expected = [[6,5,5],[7,5,5],[9,8,9],[12,12,11],[20,19,20]]
points = []
p3, b = 1, 0
while p3 <= 5832:
    u, a = p3, 0
    while u <= 5832:
        points.append((u,a,b))
        u *= 2
        a += 1
    p3 *= 3
    b += 1
assert len({u for u,_,_ in points}) == len(points)
for (lo,hi,q), wanted in zip(cases,expected):
    current = [(u,a,b) for u,a,b in points if u <= lo]
    K = [sum((a-b)%3 == j for _,a,b in current) for j in range(3)]
    assert K == wanted
    assert not any(lo < u < hi for u,_,_ in points)
    I, P, transitions = [0,0,0], [0,0,0], []
    for u,a,b in points:
        if b == 0 and a >= 1:
            if u <= lo and 3*u > 2*lo:
                I[a%3] += 1
            if 6*u <= lo and 4*lo < 27*u:
                P[a%3] += 1
            transitions.extend([Fraction(3*u,2), Fraction(6*u), Fraction(27*u,4)])
    assert not any(lo < v < hi for v in transitions)
    assert P == [0,0,0]
    assert max(b for _,a,b in current if a == 0) % 3 == (-q)%3
    adjusted = [K[j]-I[j]-P[j] for j in range(3)]
    assert min(adjusted) < adjusted[q]
```

The finite table also follows from the row widths \(1+\lfloor\log_2(t/3^b)\rfloor\). For example at 5184 the eight row widths are \(13,11,10,8,7,5,3,2\), giving \(K=(20,19,20)\); the isolated point is 4096 of color zero. This provides a short independently reviewable arithmetic certificate for the largest row.

#### Unified aggregate assembly for \(t\ge18\)

At most one exceptional owner exists over all colors: an isolate and a patch cannot coexist, and each defining interval contains at most one power of two. Let \(\delta_j=I_j+P_j\). If there is an exception, use (G1)–(G3) for that owner; otherwise use any global minimum cover. Under a hypothetical strict failure \(\tau<M=\min_j(K_j-\delta_j)\), every restricted maximum is positive, because
\[
D_j^*\ge D_j-\delta_j
=K_j-\tau-\delta_j\ge1.
\]
All mandatory owners in (G4) are consequently omitted by a single common optimum. The origin and degenerate cases in the top color contradict the corner \(\{6,12,18\}\), so the top restricted maximizer is incomparable and has \(D_q^*=1\). Then
\[
1+\delta_q\le D_q\le D_q^*+\delta_q=1+\delta_q.
\]
Thus \(\tau=K_q-\delta_q-1\), and the inequalities \(\tau<M\le K_q-\delta_q\) force
\[
M=K_q-\delta_q.
\tag{H4}
\]
The high-prefix repair excludes \(s\ge4\). Every remaining incomparable interval in the exact table violates (H4). This closes the contradiction for \(t\ge18\), given the preceding matching, root-balance, degenerate-prefix, and high-branch inputs. No splitting of a high-deficiency set into positive components is used: its deficiency becomes one only after the unique vertical-root deletion argument.

#### All base cases \(3\le t<18\)

The following table includes the non-smooth correction threshold \(27/2\) for the small patch.

| Interval | \(K\) | \(I\) | \(P\) | \(M\) |
|---|---|---|---|---|
| \([3,4)\) | \((1,1,1)\) | \((0,0,0)\) | \((0,0,0)\) | 1 |
| \([4,6)\) | \((1,1,2)\) | \((0,0,1)\) | \((0,0,0)\) | 1 |
| \([6,8)\) | \((2,1,2)\) | \((0,0,0)\) | \((0,0,0)\) | 1 |
| \([8,9)\) | \((3,1,2)\) | \((1,0,0)\) | \((0,0,0)\) | 1 |
| \([9,12)\) | \((3,2,2)\) | \((1,0,0)\) | \((0,0,0)\) | 2 |
| \([12,27/2)\) | \((3,3,2)\) | \((0,0,0)\) | \((0,1,0)\) | 2 |
| \([27/2,16)\) | \((3,3,2)\) | \((0,0,0)\) | \((0,0,0)\) | 2 |
| \([16,18)\) | \((3,4,2)\) | \((0,1,0)\) | \((0,0,0)\) | 2 |

For \(3\le t<9\), the cover \(\{2\}\) meets every existing corner, and at least one point is necessary because the corner at 1 exists. For \(9\le t<18\), the cover \(\{3,4\}\) meets every corner, whose roots belong to \(\{1,2,3,4\}\). The already present corners rooted at 1, 2, and 3 have empty common intersection, so a one-point cover is impossible. Thus \(\tau=M\) on every base interval. There is no patch with root 1: its proposed middle owner \(9/2\) is not a board point.

#### Scope of the completed assembly

The upper construction and the lower argument above give the proposed finite theorem
\[
\tau(t)=\min_{j\in\{0,1,2\}}\{K_j(t)-I_j(t)-P_j(t)\}
\qquad(t\ge3).
\]
The new high-prefix repair and finite arithmetic have passed this independent audit. A fresh reviewer must still check the full chain of cited inputs and the assembly as a whole before the coordinator reports the finite theorem as verified. In particular, this note does not turn the separate irrationality transfer into a proved result.

The earlier first-failure exploration is not needed for this proof. Its valid bookkeeping facts were: a smooth point with positive 3-exponent creates exactly one new corner; pure powers of two create none; patch activation raises only the adjusted count in the old isolate color; patch deactivation raises two adjusted counts. Those facts alone did not supply a boundary-preserving induction, and no such induction is being imported into the completed argument.

### Gaps

No gap was found in the single-owner compatibility lemma, high-prefix augmentation, finite phase table, base cases, or their aggregate combination with the cited inputs. The full assembled proof is pending the requested fresh-context adversarial audit. The arithmetic obligations for #168(ii) are separate and remain outside this round. No Lean work, broad optimum sweep, new dependency, or alteration of earlier folders was used.
