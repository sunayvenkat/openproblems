# Review of Route P and the breakthrough synthesis

Reviewed 2026-11-10. Sources are this folder's notes.md, verify_potential_theory.py and adversarial_audit_p.py, together with master_proof.md and adversarial_audit.md in the breakthrough synthesis folder. No complete solution is established. The earlier part-i snapshot and the 28+9+2 previously manifested source files are unchanged.

## Accepted identities and their limits

The high Green stencil and low-row stencils are correct, but already present in the archived occupation/kernel work. They do not themselves supply an arithmetic relation with the single target value Z. The decaying-function flux theorem also has a valid proof: set u=-x, v=y-x and g(u,v)=f(-u,v-u). The operator becomes the mixed backward difference in u,v. On a rectangle 0<=u,v<=N its sum is g(N,N)-g(-1,N)-g(N,-1)+g(-1,-1). The first three terms vanish by uniform decay, leaving f(1,0). Absolute summability allows passage to the full cone. This avoids the manuscript's unjustified claim that an increasing number of outer boundary terms vanish individually.

The subsequent application to f(z)=Q_H(-z) is invalid. For z=(m,0) tending to positive infinity, F(w-z) tends to one for every fixed occupied state w. Dominated convergence gives Q_H(-z)->||nu^H||=1/27, not zero. Thus the required decay fails. Reflection also changes the stencil: from LQ_H(t)=nu^H(-t), direct shift algebra gives L_z[Q_H(-z)]=nu^H(z+1), not nu^H(z). The stated potential representation does not follow. As a generic check, nu=delta_(1,1) gives sum_C nu=0 but Q_H(-1)=F(0,1)=1.

## Slice transcendence is not proved

The claimed identification of the actual birth word as a finite-interval coding of phase alone is unsupported. A_a is an accumulated cocycle; the exact transport already retains BOTH unbounded state and phase. Counting the phase cuts in one increment does not count the partitions needed for the accumulated-state cone test. No proof that the actual row/column factor complexity is O(n) is supplied.

The verifier's sequence is floor(n*alpha) modulo three. It is not eta_(n,b) for any demonstrated b. Its finite p(n)=3n tests prove neither a universal complexity bound nor the needed property of the actual birth word. The printed 2n+1 bound is even exceeded by its own data; the script tests the different 3n+1 bound. The geometric-series test likewise does not independently reconstruct the complete state/phase resolvent; use the archived exact transport proof for that input.

The [Adamczewski–Bugeaud theorem](https://annals.math.princeton.edu/2007/165-2/p04) concerns low complexity of the digit expansion of an irrational algebraic number. To infer transcendence of a proposed slice, one must establish both low complexity and non-eventual-periodicity for its actual canonical digit sequence. Irrationality/ergodicity of a driving rotation alone proves neither: a constant readout remains periodic under any rotation. Finite frequencies do not repair this. Applying the theorem to W_n's large, signed coefficients additionally requires justified canonical base-three digits and carry control. Slice transcendence and transcendence of W_n remain unproved here.

## Generating-function claims and value arithmetic

The manuscript has not established non-semilinearity of the actual support: its asserted nonperiodicity of every nontrivial row uses the same missing accumulated-state argument. It supplies no applicable proof of its cited multivariate natural-boundary assertion. Nonrationality of a multivariate integer-coefficient generating function does not by itself force the entire polydisc boundary to be natural. For example g(x)/(1-y), with g(x)=sum_(k>=1)x^(2^k), has zero-one bivariate coefficients and both coordinate radii one, yet extends across y=-1 when |x|<1.

Even valid slice transcendence or a natural boundary would not imply irrationality at (1/2,1/3). The sum of transcendental terms can be rational; analytic functions with natural boundaries may have rational special values. The source correctly acknowledges the latter gap in Section 6.2. However its status ledger incorrectly treats the preceding unproved hypotheses as certified. P2 and P3 have been reopened. P4 remains open, and P5/P6 isolate the invalid potential application and missing nonperiodicity proof.

## Corrections to the new adversarial audit

Its rejection of a completed proof is justified, but some of its own stronger statements are unsupported. The constants 17.25 and 2.48 come from finite observations/conjectures; a negative proposed upper-bound margin does not prove actual cleared errors diverge. Route R remains open, not disproved in general. Likewise an independently proved lower bound on ||B W_n|| would be a valid rationality contradiction; it is not circular merely because it conflicts with the consequence of hypothetical rationality. The missing proof is the inference from aperiodic driving dynamics to that bound. Routes H and R remain legitimate open alternatives.

## Checks and disposition

verify_potential_theory.py runs successfully: finite stencils, a numerical flux test, elementary geometric sums and finite driver-word complexity. Those assertions do not verify its advertised actual-slice transcendence, natural boundary or target arithmetic. The written mixed-difference argument above establishes the flux lemma under its stated decay and summability assumptions; those assumptions fail for the proposed target application.

Part (i) remains working-complete with final audit deferred, not freshly certified by these files. Part (ii) remains unproved. No old open supply or arithmetic task is closed by the new architecture. Source files are preserved; corrected task statuses govern the roadmap. Historical novelty, the full foundational proof audit and Lean were not checked.
