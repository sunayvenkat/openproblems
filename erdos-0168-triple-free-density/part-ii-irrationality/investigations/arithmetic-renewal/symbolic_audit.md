# Independent audit of the complete symbolic source and prime arithmetic

## Does radius-zero closure give the claimed complete rational source?

### Takeaway

**PASS for actual-source closure, with one documentation correction.** All nine high source grids terminate under every interior A, B and AB branch, and all twelve low starts terminate. This proves the stated complete rational value at radius zero. It proves no full-phase termination theorem. The unsupported forward reference to such a theorem in the original `symbolic.md` was replaced by that explicit limitation. — [Corrected SY1 and scope](<symbolic.md>), [independent certificate](<symbolic_audit_check.py>), [finalized convex note](<convex.md>).

### Cited Findings

- The accepted pairing is
  \[
  S_H=216\sum_{i=0}^2\sum_{b\in\{6,4,5\}}2^{-i}3^{-b}p_H(i,b),\qquad
  S_L=8\sum_{i=0}^2\sum_{b=0}^3 2^{-i}3^{-b}p_L(i,b).
  \]
  It includes the entire horizontally infinite low rows before transport, including the zero-target row. For zero forcing, \(S_R=Q_{\rm full}(0)+\Psi_R\) and \(Z=2-3S_R+3\Psi_R\). The exceptional birth is already accounted for exactly once in this normalization. — [ET6–ET8](<../occupation-arithmetic-bridge/exact_transport.md>), [accepted exterior pairing](<../finite-volume-calibration/exterior_audit.md>).
- The supplied checker ran once successfully. The new checker uses exact integer comparisons for the logarithmic floors and constructs the axes from their increment recurrences; it then independently compares them with individual original board-cell enumeration through index 79. It checks original root windows through vertical index 127, the two actual state witnesses, and original corrected-minimum birth differences on a small triangle and selected larger cells. No project module, floating logarithm, solver or installation is used. — [Supplied checker](<symbolic_check.py>), [independent checker](<symbolic_audit_check.py>).
- The nonempty high graphs have `(interior vertices, maximum total increment)` equal to \((1,0),(3,2),(1,0),(1,0),(15,17)\) at starts \((0,6),(0,4),(0,5),(1,5),(2,6)\), respectively. The other four starts are exterior. Every low start exits within three horizontal steps. Backward substitution, independently of finite-depth Picard comparison, gives
  \[
  S_0=\frac{7949385124218080419452346025}{372885909329585286602293248},
  \qquad D_0=\operatorname{den}(S_0),\quad \operatorname{bitlength}(D_0)=89.
  \]
  The independent Picard computation agrees at depths 20 and 32. — [Independent graph, low-row and source assertions](<symbolic_audit_check.py>).
- The complete unexceptional head with \(a+b<100\), together with the full tail, certifies
  \[
  7851029231031622054440914924<D_0\Psi_0<7851029231031622054440914925.
  \]
  The independent assertions check strict inequalities for both rational bounding endpoints, rather than merely compare their floors. — [Exact head, tail and strict interval assertions](<symbolic_audit_check.py>).

### Inferences

- Emptying the exploration queue is a finite exhaustive certificate because every interior successor is either already included or explored, and each exterior successor has its prescribed value immediately. Each A/B/AB step strictly increases the sum of indices, so the graph is acyclic and backward substitution is exact. The maximum total increment 17 bounds the length of every interior path; depth 20 is therefore sufficient for all actual sources. This is stronger than observing stabilization at two depths, but its domain is precisely the actual source grids. — [SY1 graph construction and certificate](<symbolic_audit_check.py>).
- For a complete unexceptional head \(H_M\), Boolean births give
  \[
  0\le Q_{\rm full}(0)-H_M\le
  \sum_{a+b\ge M}2^{-a}3^{-b}=6\,2^{-M}-3\,3^{-M}.
  \]
  The equality follows by summing \(a\ge M-b\) for \(b<M\), then adding the entire geometric tail \(b\ge M\). Subtracting this interval from the exact \(S_0\) proves the displayed residual interval. Thus rationality here yields an enormous cleared residual, not a small return. — [Full-tail algebra and endpoint checks](<symbolic_audit_check.py>), [accepted source identity](<../finite-volume-calibration/exterior_audit.md>).

### Gaps

- **Corrected issue:** the original SY1 gaps paragraph claimed that a companion supplied a stronger full-phase radius-zero theorem. The finalized companion contains an ordered-axis construction, not that joint-termination theorem. The sentence was replaced in the current note; no archived file was changed. — [Corrected scope](<symbolic.md>), [finalized companion](<convex.md>).
- At radius one, the supplied exploration certifies termination for \((0,6)\) with 10,000 vertices and maximum total increment 425, and for \((1,4)\) with three vertices. The seven other starts reach the specified frontier. At radii two and three every start reaches it. Reaching a fixed frontier proves neither an infinite path nor eventual termination. These larger explorations were run in the supplied checker, not duplicated in the new checker. — [Supplied finite exploration](<symbolic_check.py>).

## Do the common numerator, prime recurrence and clearing-cost claims survive full-source cancellation?

### Takeaway

**PASS for SY2–SY4 with the stated large offsets.** The full common numerator includes all 21 sources. Its residue detects the exact three-adic reduced denominator, and the killed cellular recurrence is valid. The finite residue data supply no infinite nonvanishing theorem; the growing cleared majorant is not an actual-error lower bound. — [SY2–SY4](<symbolic.md>), [independent rational and modular comparisons](<symbolic_audit_check.py>).

### Cited Findings

- For Picard depth \(m\), with interior initial value zero and exterior values \(1+h/182\) high and \(1+h/7\) low, let \(q_m=182\,216^m p_{H,m}\), \(r_m=7\,8^m p_{L,m}\). The exact full numerator is
  \[
  \begin{aligned}
  N_m:=27\cdot182\cdot216^m S_m
  ={}&\sum_{i=0}^2\sum_{b\in\{6,4,5\}}2^{3-i}3^{6-b}q_m(i,b)\\
     &+26\,27^m\sum_{i=0}^2\sum_{b=0}^3 2^{3-i}3^{3-b}r_m(i,b).
  \end{aligned}
  \]
  The independent checker verifies integrality and this exact identity at depths \(0,1,2,4,8,12,20,32\), for each radius \(0,1,2,3\). — [Independent full-source formula assertions](<symbolic_audit_check.py>).
- Independent backward modular recursion agrees with exact rational Picard evaluation at every tested positive depth. At radius one it gives 71 nonzero residues among depths 1–100 and verifies \((v_2,v_3,\text{denominator bits})=(94,99,258)\) at depth 32. — [Independent arithmetic output](<symbolic_audit_check.py>).
- Actual killed B/AB commutator witnesses occur at \((R,a,b)=(0,0,26),(1,0,8),(2,1,10)\). Each has interior start and common terminal \((a+3,b+6)\), but unequal interior indicators at the intermediate B and AB cells. — [Actual-index witness assertions](<symbolic_audit_check.py>).

### Inferences

- **Integer scaling and cancellation proof.** Inside, the exact scaled recurrence is
  \[
  q_m=27q_{m-1,A}+8q_{m-1,B}-q_{m-1,AB}+182\,216^{m-1}h;
  \]
  outside it is \(q_m=216^m(182+h)\). The analogous low recurrence is \(r_m=r_{m-1,A}+7\,8^{m-1}h\), with exterior \(8^m(7+h)\). Starting from the specified integer seeds proves integrality for all depths. Substitution into the accepted corner pairings gives the displayed common numerator exactly: the high coefficient is \(27\cdot216\,2^{-i}3^{-b}\), and the low coefficient is \(26\cdot27^m\cdot8\cdot27\,2^{-i}3^{-b}\). — [Source pairings ET6–ET8](<../occupation-arithmetic-bridge/exact_transport.md>), [scaled source checks](<symbolic_audit_check.py>).
- **Exact three-adic conclusion.** For \(m\ge1\), the low summand and high rows \(b=4,5\) vanish modulo three. Thus \(F_m=N_m\bmod3=\sum_i2^{3-i}q_m(i,6)\bmod3\). If this is nonzero, the common numerator is a three-adic unit. The common denominator has valuation \(v_3(27\cdot182\cdot216^m)=3m+3\), so reduction leaves exactly \(v_3(\operatorname{den}S_m)=3m+3\), after all source cancellations. — [Exact numerator identity and SY3](<symbolic.md>), [independent valuation assertions](<symbolic_audit_check.py>).
- **Killed recurrence.** At depth one, inside, \(q_1\equiv2h-q_{0,B}-q_{0,AB}\pmod3\). From depth two onward, the forcing vanishes and \(q_m\equiv-q_{m-1,B}-q_{m-1,AB}\), with zero exterior values modulo three. This proves the recurrence at every interface. If \(P\) is the interior projection, the relevant killed branches are \(P U_B P\) and \(P U_AU_B P\); their two compositions contain different intermediate projections. The displayed actual witnesses make their commutator nonzero on a delta function at the common terminal. Commuting unrestricted physical shifts therefore do not justify Frobenius sparsification of the killed operator. — [Independent direct modular recursion and commutator witnesses](<symbolic_audit_check.py>).
- **Majorant proof and its limit.** The sums of positive source coefficients are \(182/27\) high and \(560/27\) low. Multiplying the respective global bounds \(183/182\), \(8/7\) by contraction factors \(6^{-m}\), \(8^{-m}\) yields
  \[
  |S_R-S_{R,m}|\le(61/9)6^{-m}+(640/27)8^{-m}.
  \]
  When \(F_m\ne0\), \(D_m\ge27^{m+1}\), so the product of \(D_m\) with the high part of this upper majorant is at least \(183(9/2)^m\). A growing upper bound gives no lower bound on the actual approximation error. — [Accepted contraction and source bounds](<../finite-volume-calibration/exterior_audit.md>), [exact coefficient and cost assertions](<symbolic_audit_check.py>).

### Gaps

- No infinite nonzero supply, useful vanishing subsequence, growing-radius source-denominator theorem or lower bound for the actual approximation error is proved by these finite computations. No conclusion about exact coupled-source rationality at general radii follows from rational finite approximants. — [Explicit SY2–SY4 limitations](<symbolic.md>).

## Does the smaller exterior offset prove all real interface inequalities?

### Takeaway

**PASS for SY5 as a separate real theorem.** The original small high prescription \((1+h)/182\) and matching low prescription \((1+h)/7\) give bounded real solutions, exact interior cancellation and strictly positive exterior residual at every interface. These statements do not inherit the numerical source or residue data for offset one. — [SY5](<symbolic.md>), [independent extremal constant checks](<symbolic_audit_check.py>).

### Cited Findings

- The high map has norm \(36/216=1/6\), independently of phase and radius. For exterior \(p=c+h/182\), its closed global ball \(|p|\le C=c+1/182\) is preserved whenever \((36C+1)/216\le C\), equivalently \(C\ge1/180\). At every exterior point,
  \[
  K=216c+(34/182)h-27p_A-8p_B+p_{AB}
    \ge180c-36/182.
  \]
  Therefore \(c>1/910\) suffices; that threshold also guarantees the ball condition. — [SY5 argument](<symbolic.md>), [threshold assertions](<symbolic_audit_check.py>).
- At \(c=1/182\), \(C=1/91\). Enumerating the Boolean current target and all endpoint signs of the three bounded successor values gives exactly the claimed universal bounds
  \[
  144/182\le K\le161/91.
  \]
  For the low problem, \(C_L=2/7\), \((C_L+1)/8\le C_L\), contraction is \(1/8\), and its exterior minimum is \(8/7-C_L=6/7\). — [Independent exact extrema](<symbolic_audit_check.py>).

### Inferences

- The ball-preserving contraction argument takes place on bounded functions over the complete interior lifted domain; it needs no finite phase partition. Its fixed point solves the exact interior equation. The exterior bound uses only the global successor bound and the retained current Boolean term, so it includes every interface. This validly strengthens the earlier small-offset assessment for zero forcing. — [SY5](<symbolic.md>), [accepted full-domain contraction framework](<../finite-volume-calibration/exterior_audit.md>).
- The small family changes the boundary seeds: high scaled exterior seed is \(1+h\), rather than \(182+h\), and low seed is \(1+h\), rather than \(7+h\). The formal corner coefficients remain the same, but the actual source, residue sequence and appropriate error constants must be recomputed. In particular the supplied `high_offset` argument changes only the high prescription; setting it alone does not select the matching small low prescription. All arithmetic assertions in this audit use the stated offset-one family. — [Supplied source implementation](<symbolic_check.py>), [independent large-offset source and separate small-offset constants](<symbolic_audit_check.py>).

### Gaps

- **Final disposition: PASS for SY1–SY5 in their corrected scopes.** The sole unsupported stronger-theorem reference has been corrected. The remaining arithmetic requirement is a proved infinite family whose complete source can be cleared affordably while its actual nonzero residual becomes small; neither finite prime data nor bounded-real existence supplies that theorem. No proof of Erdős #168(ii) follows. — [Corrected claims and explicit limitations](<symbolic.md>), [accepted arithmetic bridge criterion](<../finite-volume-calibration/exterior_audit.md>).
- Skipped Lean, installations, external theorem searches, posts, priority claims, archived-file edits and any reproof of the accepted global finite optimum, unboundedness or height theorem. Material risks are transferring offset-one arithmetic to the small family, treating frontier evidence as infinite survival, treating killed shifts as commuting, or mistaking failure of an upper majorant for failure of the actual error. — [Audited scopes](<symbolic.md>).
