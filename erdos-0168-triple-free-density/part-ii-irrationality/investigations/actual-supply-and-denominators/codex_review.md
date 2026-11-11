# Integration review of the new scalar-supply work

Reviewed 2026-11-08. This incorporates [the scalar supply note](<../scalar-supply-barrier/supply_barrier.md>) and [the actual-model theory and computations](<theory.md>). The [manifest](<SOURCE_MANIFEST.json>) identifies all 28 source files. Their contents are preserved. Claude's additions to the consolidated progress document have been folded into its main roadmap with the qualifications below.

Part (ii) remains unproved. This is a bounded dependency and certificate review; part (i), complete scalar-model identities, the rectangle bound and prior uniform nonvanishing theorems remain working inputs for the deferred final audit.

## Mathematical results incorporated

**Convergence makes denominator growth equivalent to infinitely-often nonvanishing.** For any infinite indexed family of rational z_n converging to Z, the following are equivalent: unbounded reduced denominators, failure of eventual constancy, and z_n!=Z infinitely often. A bounded-denominator convergent family lies in a fixed discrete lattice and must eventually equal its limit. This elementary lemma is correct and needs convergence, not G1 itself.

Consequently, if an infinite family lies in the previously proved six-state nonvanishing domain, its denominators are automatically unbounded. This is a conditional result about any such infinite family, not an independent proof that the actual favorable family is infinite. Outside that domain, infinitely-often nonvanishing or equivalent denominator growth remains unproved. Primitive-prime survival is still one possible sufficient method, not a necessary additional obligation on a known nonvanishing class.

**The resonant-mediant branch has a residue-only supply criterion.** Put sigma_n=p_n+q_n modulo three and t_n=sigma_(n-1)/sigma_n in the projective line over F_3. The recurrence is

\[
\sigma_{n+1}=a_{n+1}\sigma_n+\sigma_{n-1},\qquad
t_{n+1}=1/(a_{n+1}+t_n).
\]

A resonant first mediant is equivalent to sigma_n+sigma_(n+1)=0. The determinant condition implies both parent residues are nonzero. The archived commutator formula then forces one of the two already proved nonzero response states, regardless of the sizes of the parent transforms. Thus the following single missing statement suffices for the existing scalar route:

\[
\mathrm{L_*}:\quad \#\{n:a_{n+1}\ge5,\ \sigma_n+\sigma_{n+1}=0\pmod3\}=\infty.
\]

Equivalently require sigma_n!=0 and a_(n+1)=-1-t_n modulo three. The nonzero qualification cannot be omitted when dividing by sigma_n. L_* is a sufficient subfamily of the full six-state criterion; it is not equivalent to all possible balanced-or-resonant supply.

The lower-first Christoffel identity H(lower+upper)=H(lower)+omega^(p_lower+q_lower)H(upper) is correctly derived in the supply note. It agrees with the archived recurrence and supplies an exact algorithm. It does not supply a frequency theorem for the actual logarithm ratio.

**Conditional transcendence upgrade.** The five-coordinate argument in Lemma B fits the primitive-integer form of Schlickewei's theorem, checked against [Evertse, Theorem 1.1](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf). After division by a gcd at most 27, the product of local forms is at most 2^(5q-Q+O(1)), while height is of order 2^(6q). Infinitely many applicable nonresonant next digits at least six give a fixed negative height exponent. A resulting rational linear relation either forces Z rational or contradicts the pure S-unit coordinates. In the latter case the omitted divergence justification is elementary: |2^(3q)-3^(3p)|>=2^(2q), by factoring a difference of cubes with nonzero integer factor 2^q-3^p.

Therefore the stated hypothesis excludes algebraic irrational Z. Combining it with infinite known nonvanishing supply gives transcendence. Unbounded applicable digits on such a nonvanishing family also give arbitrarily high rational-approximation exponents. None of these implications proves its supply hypothesis.

**The resonant four-step block is a valid abstract countermodel.** From sigma_n=0, a next-digit block (A,1,1,1) returns to sigma=0 after four steps, with all intermediate nonresonant currents carrying next digit one. Arbitrary infinite A choices give genuine infinite tails; a bounded two-choice subfamily already contains transcendental slopes. This shows that generic transcendence and finite irrationality measure alone do not force the actual nonresonant digit visits. It says nothing affirmative about the actual infinite tail of log_3(2), and does not rule out unrelated proof architectures.

The separate finite greedy-avoidance experiment in B5 is weaker: it does not establish an infinite avoiding tail, and cannot prove that an all-large-digit infinite tail avoids eligibility. The earlier B2 claim about the full balanced branch is explicitly repaired in the source; only its resonant-branch avoidance survives without extra analysis.

## Selected exact certificate checks

The [review checker](<codex_review_check.py>) passed. It uses explicit integer bounds on the logarithm series, integer/Fraction arithmetic and data-only loading of the stored integer caches.

- An interval for alpha certifies 600 continued-fraction digits. On indices 3 through 591 it reproduces 159 eligible indices, 168 next digits at least five, and 39 joint visits: 38 resonant-mediant and one balanced. The source's two-precision observations are thereby upgraded to interval-certified finite observations for this range.
- The grouped evaluator matches the archived complete evaluator on both sides at 5/8, 12/19, 41/65 and 53/84. The complete values at 15601/24727 and resonant 665/1054 were regenerated and match their caches.
- Eight cached actual nonresonant models through q=125743 retain both tested full cyclotomic factors, with numerator coprime to each. The ninth reported case at q=176251 was not regenerated or independently checked from a full cached value.
- For n=4,...,11, the later-model enclosure excludes equality to Z. At n=12, the resonant-mediant jump exceeds the complete variation in both Farey children, giving an additional finite nonvanishing certificate without regenerating the q=176251 model.
- Starting with the stored q=125743 model and the full rectangle-error radius, both enclosure endpoints have 71,933 common CF terms. The partial quotient at index 10,707 has 27,607 bits. The preceding convergent is exactly the complete resonant 665/1054 model. These calculations were reproduced; the largest model value used as the center was not recomputed from its entire tile.
- The last common convergent denominator has 150,991 bits. Conditional on the working model/rectangle theorem and stored value, any rational Z therefore has denominator at least 2^150990. Since den(9c-6) divides den(c) for rational c, the same bound applies to c. This strengthens the source's weaker 2^150986 assertion. The resonant-model comparison also verifies its separate error bound below 2^(-63973).

These are finite certificates, not irrationality or a Liouville classification of Z.

## Corrections governing the consolidated roadmap

1. **The printed radius loses a factor near two.** The actual radius at the best stored model is epsilon=9(2^(-301994)+3^(-190537)-2^(-301994)3^(-190537)). Exact comparisons give 2^(-301990)<epsilon<2^(-301989), not epsilon<2^(-301990). The scripts use the full correct radius for the CF enclosure, so this correction does not invalidate its reproduced common prefix.
2. **The original nonvanishing test cannot pass.** certify.py tests |z_n-z_m|>epsilon_n+epsilon_m. Valid intervals imply the opposite weak inequality. To exclude Z=z_n using the later interval, the sufficient test is |z_n-z_m|>epsilon_m. nonvanish_out.txt and this review use the latter test. The impossible earlier test explains the False entries in certify_out.txt.
3. **kappa_min.py gives a necessary lower bound, not an attained minimum.** Its Legendre/CF comparisons exclude denominator <=2^(3q) at the finite input q=84 for the checked slack budgets. They do not refute the true conditional threshold lemma B3 or an eventual asymptotic construction, whose cutoff and little-o terms are unspecified. The floating-point reported exponents are illustrative; the exclusion was rechecked with integer inequalities.
4. **An effective-window conjecture alone does not finish the resonant route.** It still needs full denominator control including powers of 2 and 3, nonvanishing, and an infinite actual supply on which the gain exceeds that full cost. A single exceptional resonant return supplies none of those infinite assertions.
5. **No universal cost barrier has been established.** Periods, a finite lower-bound example, and a failed construction do not exclude target-specific cancellation, another scalar family, or a different proof route.

The exact missing scalar statements and alternative arithmetic bridges are now listed in [ERDOS168_PROGRESS.md](<../../PROGRESS.md>). Final comprehensive rigor, novelty and Lean work remain deferred. No autonomous proof-search goal was started.
