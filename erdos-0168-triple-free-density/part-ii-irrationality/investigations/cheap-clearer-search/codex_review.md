# Integration review of the cheap-clearer investigation

Reviewed 2026-11-09. Source: [notes.md](<notes.md>) and its eight scripts. The [manifest](<SOURCE_MANIFEST.json>) identifies all nine new source files, preserved unchanged. The 28 files in the previous integration manifest are also unchanged.

Part (ii) remains unproved. The useful new theorem is a conditional modular obstruction to rationality. The negative searches do not establish a universal denominator-cost lower bound. The complete mathematical roadmap is [ERDOS168_PROGRESS.md](<../../PROGRESS.md>); remaining proof tasks with finish conditions are in [tasks/todo.md](<../../todo.md>).

## Conditional divisibility route: accepted within the working framework

Let K be an infinite actual nonresonant family with a_(n+1)>=5, and let D_n=27(2^(3q_n)-1)(3^(3p_n)-1). If Z=A/B is rational in lowest terms, the existing scalar error and integrality theorems imply z_n=Z and B divides D_n for all sufficiently late n in K. This is Lemma 8.1; no first-mediant state is needed.

The elementary prime/order classification in Lemma 8.2 is correct. Outside {2,3,7,13}, put m_2=ord_ell(2)/gcd(ord_ell(2),3) and m_3=ord_ell(3)/gcd(ord_ell(3),3). Both are at least two, and ell divides D_n exactly when m_2 divides q_n or m_3 divides p_n. The exceptional valuations are

\[
v_2(D_n)=1\ (p_n\text{ odd}),\qquad v_3(D_n)=3\ (q_n\text{ odd}),
\]
\[
v_7(D_n)=1+v_7(q_n)+[p_n\text{ even}](1+v_7(p_n)),
\]
\[
v_{13}(D_n)=1+v_{13}(p_n)+[4\mid q_n](1+v_{13}(q_n)).
\]

These follow by multiplicative orders and lifting exponents. If a divisor B of D_n exceeds 447174=2*27*49*169, either it has an outside prime imposing the order condition, or one of its exceptional prime powers exceeds the stated caps.

Theorem 8.3 therefore correctly proves irrationality under the additional ND hypothesis: for every fixed M>=2, infinitely many n in the same K have both p_n and q_n coprime to M. Under rationality, choose M from the finitely many order moduli attached to B, together with 2,4,7,13. ND rules out every case of Lemma 8.2, whereas the established finite certificate gives B>2^56>447174. The actual infinite K and its ND property are unproved. This is an alternative sufficient arithmetic condition, not a proof that response-state restrictions disappear for free.

## A weaker modular target for the checklist

An immediate useful corollary is that it suffices to prove, for every sufficiently large cutoff N,

\[
g_N=\gcd\{D_n:n\in K,\ n\ge N\}\le447174.
\]

The infinite gcd is well-defined and equals a finite subset's gcd: start with one D_n and keep taking gcds; the resulting descending positive divisors stabilize. Thus one can instead construct arbitrarily late finite adequate blocks whose clearers have a small gcd.

It is enough to establish the following prime-by-prime claims on the same K:

- v_2(D_n)<=1 infinitely often;
- v_3(D_n)<=3 infinitely often;
- v_7(D_n)<=2 and v_13(D_n)<=2 each infinitely often;
- for every fixed outside prime ell, ell does not divide D_n infinitely often.

Different primes can use different subsequences. Each bound applies to every tail gcd, which then has no outside primes and has exceptional exponents at most (1,3,2,2). Under rationality B divides every late D_n, hence divides g_N, contradicting its size. This corollary is a logical reduction of the accepted conditional argument; none of its actual infinite-visit hypotheses has been proved. It is weaker than simultaneous ND for every composite modulus. A small gcd in an initial finite prefix does not establish a bound on all later tails.

## Selected checks and a finite-data correction

The supplied audit8.py ran successfully:

- 8,771 coprime pairs through 120: zero failures in the valuation/order tests;
- 102,147 large divisors from the selected small pairs: zero exceptions to the classification;
- all eight stored nonresonant model denominators divide their nominal D_n.

The written derivation, rather than these finite tests, supports the universal arithmetic identities. The supplied raw-colour isotypic_check.py also passed all 6,893 samples, agreeing with the elementary geometric-sum recurrence.

**The finite divisibility script uses reciprocal convergents.** divisibility_check.py initializes its append recurrence with P=[1,0], Q=[0,1]. Since it includes a_0=0, this produces 1/0 first and 8/5 where the actual convergent is 5/8. The correct initialization is P=[0,1], Q=[1,0]. The set K is unchanged by swapping p and q because its selection uses their sum, but D_n, the parity labels and some prime frequencies change.

Using explicit logarithm intervals to certify 600 digits and the correct recurrence, the probe range n=3,...,590 gives:

| Quantity | Corrected result |
|---|---:|
| Adequate nonresonant indices | 125 |
| p_n odd | 77, rather than 83 |
| q_n odd | 83, rather than 77 |
| Primes 5<=ell<20000 dividing every tested D_n | 7 and 13 |
| Additional primes dividing every tested second-half D_n | None |
| Most persistent outside prime below 2000 | 73, dividing 61 of 125 rather than 57 |
| Both p_n,q_n coprime to 2, 182, 6, 30030, 9699690 | 35, 26, 10, 5, 5 respectively |

The last row is invariant under swapping the two coordinates. These remain finite observations, not proofs of ND or primewise nonpersistence.

## Claims retained only in limited scope

1. **Raw character decomposition.** The stated recurrences for T and X are correct for the uncorrected colour sum. They do not prove a minimal period for the complete nonlinear birth readout or prohibit cancellation in its evaluated scalar value. Isolated/patch corrections and low rows are explicitly omitted from that derivation. Claims excluding all Eisenstein clearers, subproducts or alternative architectures are not incorporated as theorems.
2. **Finite candidate searches.** The subproduct search probes a specified bounded list, using a fixed-precision center. The LLL searches return reduced bases, not an exhaustive proof excluding every small-coefficient relation in a span. The larger searches were read but not rerun. Their absence of a new candidate is evidence, not a no-go theorem.
3. **Half-cleared reformulation.** It is a potentially useful technical target, but the proposed G_n sums birth indicators whereas the complete Z readout uses 1-3eta. Its background, minus-three factor, exceptional birth and all low/correction terms need an explicit complete formula. A uniform error constant and actual infinite arithmetic separation must then be proved. This is why H1–H3 are open tasks rather than accepted inputs.
4. **Orbit and wing decompositions.** Finite {2^A3^B Z modulo one} is equivalent to rational Z by an elementary repeated-orbit argument. That reformulation supplies no arithmetic closure of the two wings and corner. Finite walk depth and fixed-offset scans do not bound every possible return or clearer.
5. **Earlier numerator/denominator labels.** The new note correctly notices a mislabeled convergent recurrence in the older CF scripts. The previous integration's independent checker tracked both numerators and denominators correctly and verified the 150,991-bit final denominator. Its finite denominator exclusion is unaffected; no new precision claim is added here.

The main open alternatives are therefore unchanged in kind: actual adequate supply in a known nonvanishing class, adequate supply with a proved modular obstruction, or a complete cheaper/resonant/renewal bridge with its own budget and nonvanishing. The checklist decomposes those alternatives and marks the hard infinitude tasks explicitly. Comprehensive proof/novelty review and Lean remain deferred; no autonomous proof-search goal was started.
