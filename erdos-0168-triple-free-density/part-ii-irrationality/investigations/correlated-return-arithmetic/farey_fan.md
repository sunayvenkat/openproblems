# Complete current side Farey fan resummation

## Can all current side fan jumps be retained with a smaller complete remainder?

### Takeaway

**Yes.** For every sufficiently late eligible parent pair, the entire infinite current-side fan can be resummed using three canonical actual response values. The complete remainder improves from (O(2^{-(2q+Q)})) to (O(2^{-(q+2Q)})), with an explicit bound below. This is a theorem about real approximation; its unknown response values are not thereby rationalized. — [Exact checker](farey_fan_check.py), [accepted full jump and variation identities](../signed-arithmetic-returns/signed_scalar.md).

### Cited Findings

- The complete scalar slope function has purely atomic bounded variation. Its jump at a reduced rational (r/s) is (J_{r,s}=(2^{-s}-3^{-r})\mathcal Q_{r,s}(1/2,1/3)), with quotient coefficients bounded by (3(1+b/r)). This factorization also applies to resonant rational jumps by complete grade conservation; it does not assign a cheap scalar denominator to resonant values. — [SS1–SS4](../signed-arithmetic-returns/signed_scalar.md), [resonant grade proof](../response-closure-tests/general_states.md).
- For a positive Farey pair (a/b,c/d), the complete open-interval variation is bounded by
  \[
  \mathcal V(a,b;c,d)=9\left[2^{1-A}\left(1+\frac{A+1}{bd}\right)+3^{-B}\left(\frac32+\frac{\frac32B+\frac34}{ac}\right)\right],
  \quad A=b+d,\quad B=a+c.
  \]
  — [Complete variation proof](../signed-arithmetic-returns/signed_scalar.md).
- Actual response arrays are defined from actual axes and the exact shifted endpoint, retaining low rows separately. On a common matching floor rectangle (A\le s,B\le r), the quotient-to-actual-response error is at most ((45/2)2^{-A}+(63/2)3^{-B}). The same construction and bound apply to the canonical resonant endpoint states, using grade conservation and the identical exterior estimate. — [RR1–RR4](../response-closure-tests/response_relations.md), [resonant endpoint extension](../response-closure-tests/general_states.md).

### Inferences

**FF1. Domain and the full fan.** Let (p/q,P/Q) be consecutive actual convergents of (\alpha=\log2/\log3), with (p/q) nonresonant and the first mediant balanced and nonresonant in one of the four accepted states. Put
\[
\sigma=\operatorname{sign}(\alpha-p/q),\qquad r=p+P,\quad s=q+Q,
\quad F_k=\frac{r_k}{s_k}=\frac{kp+P}{kq+Q}\quad(k\ge1).
\]
The convergent errors (\delta=q\alpha-p), (\delta'=Q\alpha-P) have opposite signs and (|\delta'|<|\delta|). Thus every (k\delta+\delta') has sign (\sigma): all (F_k) lie between the current endpoint and the actual slope, and all their jumps are crossed. Consecutive (F_k,F_{k+1}) are Farey neighbors. Their open intervals, together with the first-mediant/successor interval, contain every unretained breakpoint between the current model and the actual slope. The correct-side endpoint convention excludes the current endpoint jump. — [Accepted convergent and endpoint conventions](../signed-arithmetic-returns/signed_scalar.md).

For positive endpoint coordinates, the two rational factors in (\mathcal V) are at most (4) and (21/4), respectively. Consequently
\[
\mathcal V\le72\,2^{-A}+\frac{189}{4}3^{-B}.
\]
Define the explicit bound
\[
\begin{aligned}
B_{\rm off}={}&\mathcal V(r,s;P,Q)
 +\frac{72\,2^{-(3q+2Q)}}{1-2^{-2q}}
 +\frac{(189/4)3^{-(3p+2P)}}{1-3^{-2p}}.
\end{aligned}\tag{FF1}
\]
The last two terms bound the sum of all open fan gaps, since their denominator and numerator thresholds are ((2k+1)q+2Q) and ((2k+1)p+2P). Both geometric series are retained exactly. In particular no assertion that (k\delta+\delta') remains small for arbitrarily large (k) is used.

Absolute convergence of the jump sum follows from (|\mathcal Q|\le27/2) and geometric decay of (2^{-s_k}+3^{-r_k}). Alternatively, dominated convergence in the bounded coefficient series shows that the appropriate side limits at (F_k\to p/q) converge to the current correct-side model. Pure-jump variation therefore gives
\[
\left|Z-\widehat Z_{p,q}^{\sigma}-\sigma\sum_{k\ge1}J_{r_k,s_k}\right|\le B_{\rm off}.
\tag{FF2}
\]
This pays every unretained open interval; it does not assume the actual path traverses each whole interval. — [Complete variation and side-limit inputs](../signed-arithmetic-returns/signed_scalar.md), [exact finite full-target test](farey_fan_check.py).

**FF2. The fan has three canonical states, although its full quotients need not be periodic.** Let (U,V) be the lower and upper Christoffel parent words. Their transforms satisfy (H(UV)=H(U)+\rho(U)H(V)), and their commutator is (C=\omega^k(1-\omega)). The accepted balanced-mediant formula determines both parent transforms from their residues, the commutator phase, and the balanced transform. If the current word is the lower word, then
\[
H(U^kV)=\frac{1-x^k}{1-x}H(U)+x^kH(V),\quad x=\rho(U)\ne1.
\]
If it is the upper word, then
\[
H(UV^k)=H(U)+\rho(U)\frac{1-y^k}{1-y}H(V),\quad y=\rho(V)\ne1.
\]
Both formulas are three-periodic in (k); the residue pair is also three-periodic. The exact endpoint formula SS6 consequently defines three canonical actual response arrays (g_1,g_2,g_3\in\{-3,0,3\}), with (G_j=\sum g_j(a,b)2^{-a}3^{-b}), and (G_{k+3}=G_k). These are actual-axis arrays, not periodic rational quotients. Resonant phases are permitted analytically. — [Commutator and parent inversion GS1–GS4](../response-closure-tests/general_states.md), [canonical actual arrays](../response-closure-tests/response_relations.md), [independent direct fan-word checks](farey_fan_check.py).

**FF3. Common-floor repair.** For all (k\ge1), the rational (F_k) and the actual slope lie in the original parent Farey interval. There is no interior rational with denominator below (s), nor numerator below (r). Their direct floors therefore agree through (s-1) and reciprocal floors through (r-1). This permits the same rectangle (A=s,B=r) for every fan member, since (s\le s_k,r\le r_k). It does **not** permit (A=s_k,B=r_k) for (k\ge2): (F_1) already separates the later fan members from the actual slope.

With
\[
\varepsilon=\frac{45}{2}2^{-s}+\frac{63}{2}3^{-r},
\]
the complete comparison is uniformly
\[
|\mathcal Q_{r_k,s_k}(1/2,1/3)-G_k|\le\varepsilon.
\tag{FF3}
\]
This includes the model quotient exterior, the actual response exterior, every low row, and the resonant grade boundary. — [RR4 exterior proof](../response-closure-tests/response_relations.md), [resonant extension](../response-closure-tests/general_states.md).

**FF4. Infinite resummation and its complete remainder.** Set
\[
x=2^{-q},\quad y=3^{-p},\quad u=2^{-Q},\quad v=3^{-P},\qquad
C_j=\frac{ux^j}{1-x^3}-\frac{vy^j}{1-y^3}\quad(j=1,2,3).
\]
Since the physical gap at (F_k) is (ux^k-vy^k), the three-periodic actual responses give
\[
\boxed{Z-\widehat Z_{p,q}^{\sigma}=\sigma\sum_{j=1}^3C_jG_j+\mathcal R_{\rm fan},}
\tag{FF4}
\]
\[
\boxed{|\mathcal R_{\rm fan}|\le B_{\rm off}+
\varepsilon\left(\frac{ux}{1-x}+\frac{vy}{1-y}\right).}
\tag{FF5}
\]
All series are absolutely convergent. No floor comparison at an unjustified later scale is needed.

The right side is (O(2^{-(q+2Q)})), uniformly over the accepted classes. An explicit loose constant is **300** for sufficiently late actual parents. Indeed, take (q\ge4,Q\ge5,p\ge3). The first off-fan interval is at most ((855/4)2^{-(q+2Q)}), since its numerator/denominator offset is (\delta+2\delta'), of absolute value below (3/Q\le1). The geometric fan-gap sum is below (215\,2^{-(3q+2Q)}), using (|3\delta+2\delta'|<5/Q\le1). Also (3^{-r}\le3\,2^{-s}), so (\varepsilon\le117\,2^{-s}) and the gap-sum bound is at most (8\,2^{-s}). Their product is at most (936\,2^{-2s}). Thus the total is below
\[
\left(\frac{855}{4}+215\,2^{-2q}+936\,2^{-q}\right)2^{-(q+2Q)}
<300\,2^{-(q+2Q)}.
\tag{FF6}
\]
The exact checker certifies the whole FF5 enclosure at current (12/19), successor (41/65), using an independent accepted actual-target rectangle and complete exteriors. Its real-error bound improves by over (2^{40}), with binary ratio exponent46. State periodicity and the common-floor ranges are additionally checked at (53/84\to306/485) and (306/485\to665/1054). Finite direct rational-grade tests include the resonant fan member (65/103). — [Complete exact certificate](farey_fan_check.py).

### Gaps

- FF4 is not an arithmetic return: the (G_j) are fixed actual real series and have not been proved rational under target rationality. Their common definitions do not supply their arithmetic. — [Existing response arithmetic gap](../response-closure-tests/response_relations.md).
- The result assumes an eligible balanced first mediant. It proves no actual infinite supply of that class, and no adequacy after denominator clearing. — [Current conditional finish](../weighted-response-identities/REPORT.md).

## Do the three actual responses telescope around their period three cycle?

### Takeaway

**The simple sum-zero cycle fails in every compatible class, even at the weighted values.** Eight canonical actual response arrays suffice for all sixteen parent classes, arranged into five unordered triples. Every response is nonzero, and every triple has mixed signs. Exact pointwise rank additionally excludes a same-index affine target/constant closure in each class; this does not establish general weighted-value independence. — [Complete exact response and rank certificate](farey_fan_check.py).

### Cited Findings

- The twenty-four residue/commutator states and sixteen eligible parent classes form an exact closed finite graph descended from the actual (5/8<12/19) interval. — [GS2 graph proof and checker](../response-closure-tests/general_states.md).
- The canonical endpoint data determine the entire actual response array, with the actual axes, low rows, and patch vectors explicitly retained. — [RR1–RR3](../response-closure-tests/response_relations.md).

### Inferences

Use the labels in this table. The state notation is ((r\bmod3,s\bmod3,A_s^+)), not ((r,s,H)). The last column is a rigorous full-series enclosure, obtained from a (96\times96) integer-weighted rectangle and exterior (9(2^{-96}+3^{-96})). Endpoints are strict. — [Exact construction and certificate](farey_fan_check.py).

| Label | Canonical endpoint state | Complete response enclosure |
|---|---|---|
| (A) | ((0,1,-\omega)) | ((0.482747,0.482748)) |
| (B) | ((1,1,0)) | ((-0.058734,-0.058733)) |
| (C) | ((2,0,1)) | ((-1.071732,-1.071731)) |
| (D) | ((2,2,1)) | ((1.456689,1.456690)) |
| (E) | ((1,2,1)) | ((0.777374,0.777375)) |
| (F) | ((2,1,1)) | ((-0.547828,-0.547827)) |
| (G) | ((1,0,-\omega)) | ((-0.000169,-0.000168)) |
| (H) | ((0,2,1)) | ((-1.120067,-1.120066)) |

Here (A,B,C,D) are the previous four balanced responses, (E,F) are the canonical resonant responses, and the remaining two have Christoffel transforms0 and (3+2\omega), respectively. Applying the exact parent inversion and the three-periodic formulas FF2 to all sixteen cases gives precisely the following unordered cycles and complete sum enclosures:

| Fan triple | Complete sum enclosure |
|---|---|
| (A,B,F) | ((-0.124,-0.123)) |
| (A,E,C) | ((0.188,0.189)) |
| (H,E,D) | ((1.113,1.114)) |
| (G,B,E) | ((0.718,0.719)) |
| (C,F,D) | ((-0.163,-0.162)) |

All decimal endpoints here are exact terminating rational numbers, not floating-point estimates. In particular every (G_1+G_2+G_3\ne0). The hoped-for replacement of (C_j) by (C_j-C_3), based on a zero cycle sum, is therefore invalid for all these actual fan vectors. — [Exact rectangle, tail and cycle enumeration](farey_fan_check.py).

For each of the sixteen ordered classes, actual high-row cells give rank5 for the columns ((1,c_{a,b},g_1,g_2,g_3)). At current (12/19), whose ordered cycle is ((C,F,D)), a five-row witness is
\[
\begin{array}{c|rrrrr}
(a,b)&1&c&g_1&g_2&g_3\\\hline
(0,4)&1&-2&-3&3&0\\
(0,6)&1&-2&-3&0&-3\\
(0,8)&1&-2&-3&0&0\\
(0,9)&1&1&0&3&0\\
(0,28)&1&-2&0&3&-3
\end{array}
\]
with determinant (-81). The checker rebuilds original target entries from the finite optimum and the responses from the accepted actual-axis definitions. This disproves any everywhere coefficientwise affine cycle identity in the named class; all sixteen classes are checked with exact rational elimination. — [Exact matrix certificate](farey_fan_check.py).

### Gaps

- Neither full rank nor a nonzero cycle sum excludes a different weighted numerical identity involving (Z), infinite boundary profiles, shifted responses, or state-dependent coefficients. The witness rows include (a=0), so no eventual-identity exclusion is asserted.
- The eight-series finite analytic dictionary does not prove rationality or algebraic independence of its entries. Its definitions and complete nonzero bounds are the accepted conclusions.

## Does the real gain survive fully charged coefficient arithmetic?

### Takeaway

**Separate coefficient clearing does not convert this resummation into an adequate return.** The geometric prefactors carry the successor powers (2^Q3^P) in addition to the old period factors. The exact algebra makes that cost explicit; further cancellation of the complete model and actual weighted responses remains outside this conclusion. — [Exact coefficient certificate](farey_fan_check.py), [parallel arithmetic investigation](same_scale.md).

### Cited Findings

- The current rational scalar model clears by (D=27(2^{3q}-1)(3^{3p}-1)), while the response values themselves are actual real series. — [Accepted model arithmetic](../weighted-response-identities/REPORT.md).
- The accepted S-unit gcd input gives (\gcd(2^{3q}-1,3^{3p}-1)=\exp(o(q))) along these actual approaching pairs. Its fixed-group hypotheses and dependence exceptions were previously checked against Corvaja–Zannier's primary theorem. — [Primary paper, Corollary1 and Proposition2](https://arxiv.org/pdf/math/0311030v2), [accepted application audit](../response-closure-tests/cheaper_audit.md).

### Inferences

Set (a=2^q,b=3^p,c=2^Q,d=3^P). Direct substitution gives, for (j=1,2,3),
\[
C_j=\frac{a^{3-j}}{c(a^3-1)}-\frac{b^{3-j}}{d(b^3-1)}
=\frac{d(b^3-1)a^{3-j}-c(a^3-1)b^{3-j}}
{cd(a^3-1)(b^3-1)}.
\tag{FF7}
\]
Thus (cdD) clears the current model and all three rational coefficients. Its binary exponent is (2Q+6q+o(q)). Multiplying the proved remainder bound by this nominal clearer yields an upper bound of order (2^{5q}), not a decaying guarantee. This observation alone is not a reduced-denominator impossibility theorem.

There is also a genuine reduced-coefficient price. Let (N_3=d(b^3-1)-c(a^3-1)). Once (Q>v_2(b^3-1)) and (P>v_3(a^3-1)), the reduced denominator of (C_3) has exactly the factors (2^Q3^P): its numerator valuations at two and three are (v_2(b^3-1)) and (v_3(a^3-1)). These exceptional valuations are (O(\log q)). Off the primes2,3,
\[
\gcd(N_3,(a^3-1)(b^3-1))
\le\gcd(a^3-1,b^3-1)^2.
\]
The accepted gcd estimate consequently proves
\[
\log_2\operatorname{den}(C_3)=2Q+6q+o(q).
\tag{FF8}
\]
This is a theorem about the rational coefficient itself, independent of whether its associated response value is rational. It does not bound the reduced denominator after combining actual weighted values or adding the complete scalar model. — [Elementary valuation/gcd checks](farey_fan_check.py), [accepted off-S gcd theorem](../response-closure-tests/cheaper_audit.md).

At the named (12/19\to41/65) pair, the exact least common multiple of the old scalar clearer and the three reduced coefficient denominators has **241bits**. Multiplying FF5 by that separate-coefficient clearer exceeds1. This is a concrete failure of this way of certifying an adequate return, not a lower bound on the unknown true combined residual. — [Exact reduced coefficient and common-clearing calculation](farey_fan_check.py).

### Gaps

- No adequate infinite arithmetic return is proved. A cheap relation evaluating or cancelling the complete actual response vector, or additional complete numerator cancellation, is still needed.
- The parent-domain state/gap supply remains open. The stronger real approximation cannot be counted as solving it.
- Skipped: Lean, installations, external review, priority claims, arbitrary unbalanced-parent fans, and further research branches. Material risk: treating finite canonical state periodicity as periodicity of the full rational quotient, or promoting a separately cleared coefficient price into an impossibility theorem for combined actual returns.
