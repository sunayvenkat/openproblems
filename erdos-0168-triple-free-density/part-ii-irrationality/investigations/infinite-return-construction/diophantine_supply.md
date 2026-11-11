# Unconditional Diophantine supply for the Erdős 168 return construction

Research note, 7 November 2026. The finite formula (C) is taken from the completed prefix and phase audit. This note proves a sharp unconditional supply lemma for its rational models, then tests several ways of enlarging that supply. It does **not** supply the exponentially improved, nonzero weighted return needed to prove #168(ii). No earlier note was edited.

## What denominator jumps are actually guaranteed at nonresonant convergents?

### Takeaway

For every irrational slope, one of every four consecutive convergents is nonresonant and has successor denominator ratio greater than \(\varphi=(1+\sqrt5)/2\). For every slope whose continued fraction is not eventually all ones, there are infinitely many nonresonant convergents with ratio greater than

\[
\boxed{C_*:=\frac{15+\sqrt5}{10}.}
\tag{1}
\]

Both constants are sharp in their respective classes; the second is sharp even among transcendental slopes in \((3/5,2/3)\). In particular, the log-ratio slope qualifies for (1), but irrationality and transcendence alone do not give ratios above 2, 3, or 5 infinitely often.

### Cited Findings

- The existing one-sided rational model has periods \(3q,3p\) under \(p+q\not\equiv0\pmod3\). For a convergent with successor \(p'/q'\), its proved first floor disagreements are \(q+q'\) and \(p+p'\). Its current clearing factor has logarithm \(6q\log2+o(1)\). — [Return construction](../../early-attacks/augmentation-and-return-attacks/returns.md), [independent audit, corrected slope and scale](../global-boundary-proof/independent_audit.md).
- Gelfond–Schneider rules out an irrational algebraic value of \(\log_3 2\); a rational value would give an impossible equality between positive powers of 2 and 3. Thus this slope is transcendental, in particular not quadratic. — [Soundararajan's first-party lecture notes, Theorem 10](https://math.stanford.edu/~ksound/TransNotes.pdf).
- The sharp constants and proofs below are deductions in this note, not claims that an external paper states this particular congruence-restricted theorem. The usual convergent recurrences also appear in [Elsner's primary paper, §2](https://www.fq.math.ca/Scanned/38-1/elsner.pdf).

### Inferences

**Notation and resonance.** Write the continued fraction convergents of an irrational \(\alpha\in(0,1)\) as \(p_n/q_n\), with

\[
p_{-1}=1,\ p_0=0,\quad q_{-1}=0,\ q_0=1,
\]
\[
p_{n+1}=a_{n+1}p_n+p_{n-1},\qquad
q_{n+1}=a_{n+1}q_n+q_{n-1}.
\]

Put

\[
s_n=p_n+q_n\pmod3,\qquad r_n=q_{n+1}/q_n.
\]

An index is good when \(s_n\ne0\), and resonant when \(s_n=0\). The determinant identity implies that consecutive indices cannot both be resonant: two vectors with \(p+q=0\) in \(\mathbb F_3^2\) would be dependent. The exact recurrences are

\[
s_{n+1}=a_{n+1}s_n+s_{n-1}\pmod3,
\qquad r_{n+1}=a_{n+2}+1/r_n.
\tag{2}
\]

**Bounded-gap theorem.** Among any four consecutive indices \(n,n+1,n+2,n+3\), with \(n\ge1\), some good index has \(r_i>\varphi\).

To prove it, suppose all good ratios in that block are at most \(\varphi\). Every outgoing digit at such a good index is 1, because an outgoing digit at least 2 would give \(r_i>2\). If two consecutive indices \(i,i+1\) are good, then

\[
r_{i+1}=1+1/r_i>\varphi,
\]

since the rational number \(r_i\le\varphi\) is strictly less than \(\varphi\). Thus the four indices contain neither consecutive good indices nor consecutive resonant indices, so must alternate. At a good index preceded by a resonant one, its outgoing digit 1 gives \(s_{i+1}=s_i\ne0\), contradicting the supposed alternation. This proves the assertion. It uses no asymptotic estimate or property of logarithms.

The block length four cannot be replaced by three. The exact consecutive fractions

\[
\frac{18}{29},\quad\frac{23}{37},\quad\frac{64}{103},\quad\frac{87}{140}
\tag{3}
\]

come from the word \([0;1,1,1,1,1,3,1,2,1]\). The first three have statuses good, resonant, good. Their two good ratios are \(37/29\) and \(140/103\), both below \(\varphi\). Indeed their values of \(r^2-r-1\) are negative by the integer numerators \(-545\) and \(-5429\), respectively.

**Improvement when the tail is not all ones.** If outgoing digits at least 2 occur at good indices infinitely often, then \(r_i>2>C_*\) infinitely often, so there is nothing to prove. Otherwise discard a finite prefix; every good outgoing digit is 1.

There must then be a resonant index in the tail. If there were none, all later digits would be 1; the Fibonacci recurrence modulo 3 forces a zero among every four successive sums. After any resonant index \(n\), write its previous nonzero sum as \(c\). Regardless of the outgoing digit at \(n\), the next sums are exactly

\[
s_n=0,\quad s_{n+1}=c,\quad s_{n+2}=c,\quad
s_{n+3}=2c,\quad s_{n+4}=0.
\tag{4}
\]

Thus resonant indices are now exactly four apart. Let \(R_j\) be \(r_n\) at the \(j\)-th resonant index, and \(k_j\ge1\) its outgoing digit. The next three, good, ratios are

\[
\frac{R_j+1}{R_j},\qquad
\frac{2R_j+1}{R_j+1},\qquad
\frac{3R_j+2}{2R_j+1}.
\tag{5}
\]

The four-step map is

\[
R_{j+1}=T_{k_{j+1}}(R_j),\qquad
T_k(R)=k+\frac{2R+1}{3R+2}.
\tag{6}
\]

If the digit tail is not eventually all ones, infinitely many \(k_j\) are at least 2. After the first such occurrence, \(R_j>\varphi\) forever: \(T_1\) is increasing and fixes \(\varphi\), while \(T_k\ge T_1\). At every subsequent occurrence of \(k_j\ge2\),

\[
R_j>T_2(\varphi)=\varphi^2.
\]

The middle good ratio in (5) is therefore strictly greater than

\[
2-\frac1{\varphi^2+1}
=\frac{15+\sqrt5}{10}=C_*.
\]

This proves (1), including infinitely many strict inequalities. Any number with an eventually all-1 continued fraction is a fractional linear transform of \(\varphi\), hence quadratic. Consequently every nonquadratic irrational, including \(\log_3 2\), satisfies the hypothesis.

**Useful interface for denominator work.** Suppose a replacement construction, on these models, gives a fixed number of terms and a clearing cost

\[
\log D_q\le(\gamma+o(1))q\log2,
\qquad H\le e^{O(q)},
\tag{7}
\]

with minimum unit bounded below by 1 after clearing. Keep the already proved matching threshold

\[
\log X_q=(1+r_n)q\log2+o(1).
\]

Then the supply above gives a fixed exponential saving whenever

\[
\boxed{\gamma<1+C_*=\frac{25+\sqrt5}{10}.}
\tag{8}
\]

For example \(\gamma=2\) would suffice. Costs \(\gamma=3,4,6\) are not covered by this unconditional interface. At equality in (8), infinitely many strict ratios do **not** give a fixed positive margin: their excess can tend to zero in the sharpness construction below.

If a proposed form has a smaller minimum unit \(t_q\), (8) must be recomputed for \(|E_q|/t_q\); ignoring this scale can turn an apparent saving into none. Nonvanishing is a separate obligation even if (8) holds.

### Gaps

The present model has \(\gamma=6\), requiring \(r_n>5+\delta\), rather than (8). No unconditional infinite supply satisfying that condition was proved. The sharp supply theorem is an interface for a better weighted construction, not a replacement for such a construction.

## Are these constants sharp, and do semiconvergents or phases enlarge the prefix window?

### Takeaway

There are exact transcendental counterexamples to every universal improvement of \(C_*\). Proper semiconvergents have a smaller prefix-length/denominator ratio, below 2. Changing the rational intercept cannot extend the existing convergent model's origin-prefix floor window at all.

### Cited Findings

- The starting point for the following window obstructions is the audited first-disagreement theorem, including its one-sided convention at rational ties. — [Independent return audit, Farey matching](../global-boundary-proof/independent_audit.md).
- Bounded partial quotients are compatible with transcendence; the literature develops many such examples. The construction below has its own elementary proof, so no particular symbolic-transcendence criterion is assumed. — [Adamczewski–Bugeaud–Davison, introduction](https://arxiv.org/pdf/math/0511682).
- All sharpness and obstruction assertions in the following paragraphs are proved here; they are not extrapolations from a computed convergent of the logarithm.

### Inferences

**Sharpness of \(\varphi\).** An eventually all-1 continued fraction has \(r_n\to\varphi\), while good indices occur infinitely often. A finite prefix can place the resulting number inside \((3/5,2/3)\). Thus a universal limsup lower bound greater than \(\varphi\) is false for arbitrary irrationals.

**Sharpness of \(C_*\), even for transcendental slopes.** Begin with six digits 1. The sixth convergent is \(8/13\), with \(8+13\equiv0\pmod3\). Append blocks

\[
(k_0,1,1,1),(k_1,1,1,1),\ldots,
\]

where \(k_j=2\) when \(j\in\{m!:m\ge3\}\), and \(k_j=1\) otherwise. Formula (4) shows that resonance is exactly at the beginnings of these blocks, irrespective of the choices \(k_j\). The resulting irrational \(\xi\) lies in \((3/5,2/3)\), because its initial convergents bracket it there.

After the first spike, all resonant ratios exceed \(\varphi\). Between spikes, \(T_1\) decreases them toward \(\varphi\); its derivative is \(1/(3R+2)^2\), uniformly less than 1 for \(R\ge\varphi\). Spike gaps tend to infinity, so the incoming ratios at successive spikes tend to \(\varphi\), and their outgoing ratios tend to

\[
T_2(\varphi)=\varphi^2.
\]

All intermediate values lie between these endpoints. Therefore

\[
\limsup_jR_j=\varphi^2.
\]

For \(R\ge\varphi\), the first and third good ratios in (5) are at most \(\varphi\); the middle one increases with \(R\). Consequently

\[
\boxed{\limsup_{s_n\ne0}r_n=C_*.}
\tag{9}
\]

Here is an elementary transcendence check. Let \(m_j\) be the digit position of the \(j\)-th spike, and let \(\xi_j\) retain all digits through that spike and replace the remaining tail by all ones. It is a quadratic irrational of the form

\[
\xi_j=\frac{p_{m_j}\varphi+p_{m_j-1}}
              {q_{m_j}\varphi+q_{m_j-1}}.
\]

Eliminating \(\varphi^2-\varphi-1=0\) gives a nonzero integer quadratic \(P_j\) with

\[
H(P_j)=O(q_{m_j}^2)=O(9^{m_j}),
\]

because all digits are at most 2 and \(q_n\le3^n\). The true \(\xi\) and \(\xi_j\) share their digits through \(m_{j+1}-1\), so

\[
0<|\xi-\xi_j|\le q_{m_{j+1}-1}^{-2}
\le2^{-m_{j+1}+O(1)}.
\tag{10}
\]

The factorial gaps give \(m_{j+1}/m_j\to\infty\). If \(\xi\) were algebraic of fixed degree \(d\), its resultant with \(P_j\), a nonzero integer, would give

\[
|P_j(\xi)|\ge c_\xi H(P_j)^{-(d-1)}.
\]

Indeed the other \(d-1\) conjugate factors are each \(O_\xi(H(P_j))\). The mean value theorem on \((0,1)\) also gives

\[
|P_j(\xi)|\le3H(P_j)|\xi-\xi_j|.
\]

Thus \(|\xi-\xi_j|\ge c'_\xi H(P_j)^{-d}\), contradicting (10). The resultant is nonzero: \(P_j\) is the irreducible quadratic of \(\xi_j\); its other root is obtained from the tail \((1-\sqrt5)/2<0\), so is outside the continued-fraction cylinder whose tails are greater than 1. The number \(\xi\) is inside that cylinder and differs from \(\xi_j\) by its next spike. Hence \(\xi\) is transcendental, and (9) disproves any stronger conclusion based only on transcendence.

**Proper semiconvergents.** Fix consecutive convergents \(p_{n-1}/q_{n-1}\), \(p_n/q_n\), and take

\[
\frac{u}{v}=\frac{k p_n+p_{n-1}}{k q_n+q_{n-1}},
\qquad1\le k<a_{n+1}.
\]

The next intermediate fraction is

\[
\frac{u+p_n}{v+q_n}.
\]

It lies strictly between \(u/v\) and \(\alpha\), since the complete quotient toward \(\alpha\) exceeds \(a_{n+1}\ge k+1\). The unimodular Farey argument proves that it is the first rational threshold that can change a one-sided floor word. Thus the first mismatch index is exactly

\[
W=v+q_n,
\qquad \frac Wv=1+\frac{q_n}{kq_n+q_{n-1}}<2
\tag{11}
\]

away from the irrelevant initial convergents. This remains true when the original convergent is resonant and the intermediate fraction becomes nonresonant. A proper intermediate fraction can repair the congruence, but loses the long prefix.

**An arbitrary rational intercept cannot improve the origin-prefix window.** Let \(p/q=p_n/q_n\) and \(p'/q'=p_{n+1}/q_{n+1}\), with \(q\ge2\). Write

\[
q'=a q+q_{n-1},\qquad N=q+q'=(a+1)q+q_{n-1},\qquad r=q_{n-1}.
\]

For every real intercept \(\rho\), the mechanical floor model obeys

\[
\left\lfloor Np/q+\rho\right\rfloor
-\left\lfloor rp/q+\rho\right\rfloor=(a+1)p.
\tag{12}
\]

The audited one-sided model agrees with the true word at \(r\) and first disagrees at \(N\). That disagreement is exactly one: \(N|\alpha-p/q|<1/q+1/q'<1\). The rational arguments at \(r\) and \(N\) are nonintegral and have the same fractional part, so the one-sided convention does not alter their difference. Therefore

\[
\lfloor N\alpha\rfloor-\lfloor r\alpha\rfloor=(a+1)p\pm1.
\tag{13}
\]

No intercept can match the true floors at both \(r\) and \(N\). The three values of \(S(m)\) are distinct for the three residue classes of \(m\pmod3\), so (12)–(13) also obstruct simultaneous matching of the \(S\)-coded axis increments. Adjusting only the rational phase cannot extend this model's prefix window beyond \(N-1\).

For an exact small instance, \(5/8\) has predecessor \(2/3\) and successor \(12/19\). Here \(r=3\), \(N=27\), \((a+1)p=15\), while

\[
\lfloor3\log_3 2\rfloor=1,\qquad
\lfloor27\log_3 2\rfloor=17.
\]

The latter are certified by \(3<2^3<3^2\) and \(3^{17}<2^{27}<3^{18}\), so their difference is 16.

**Nonconsecutive windows and paired periods.** A large ratio \(q_{n+k}/q_n\) is automatic for fixed sufficiently large \(k\), but the model at \(p_n/q_n\) already crosses a genuine threshold at \(q_n+q_{n+1}\). Replacing that threshold by \(q_n+q_{n+k}\) is false unless every intervening defect is explicitly corrected or resummed. A common period of the two ordinary models is also not free: consecutive denominators are coprime, so their common horizontal period is \(3q_nq_{n+1}\). Its logarithmic denominator cost is quadratic in the current convergent scale, while the proved matching range is only linear. These observations do not exclude a specially canceled combination of models; they exclude the corresponding unsupported shortcuts.

### Gaps

Shifted blocks at genuinely adjustable *true* phases are not ruled out by (12), which fixes the original prefix. Such a replacement must still account for the weighted head, tail, minimum unit, and height. No such replacement was completed here. The counterexamples concern what follows from broad Diophantine assumptions; they do not prove that the particular slope \(\log_3 2\) fails a stronger property.

## What do restricted approximation and the arithmetic lower bound still permit?

### Takeaway

Elsner supplies nonresonant convergents with Hurwitz-quality error, and balanced returns at adjustable phases remain valid. Neither statement gives the missing weighted exponential saving. A successful construction must lower its effective clearing cost below (8), or prove a different fixed-term return identity; growing coefficients alone need not be the obstruction.

### Cited Findings

- Elsner Proposition 2.1 states that among any six successive convergents of any irrational, some fraction has error less than \(1/(\sqrt5 v^2)\) and denominator not divisible by a prescribed odd prime. Its scope is every irrational, not a metric statement. — [Primary paper, printed p. 27](https://www.fq.math.ca/Scanned/38-1/elsner.pdf).
- The earlier adjustable-phase argument gives infinitely many balanced blocks and a positive-length orbit segment, with a quantitative phase margin. Its own final paragraph explicitly distinguishes equality at discrete cutoffs from equality of reciprocal-weighted tails. — [Balanced-return note](../../early-attacks/open-conjecture-transfer-search/168_irrationality.md).
- KK Proposition 7.4 requires fixed dimension, fixed coefficients, height control, a minimum-unit scale, and a nonzero remainder. Its application supplies the extra exponential saving and nonvanishing independently. — [Primary manuscript, §§7.2–7.3](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf), [saved primary text](../Erdos%20theorem%20transfer%20investigation/erdos1062-fork-free-density.pdf.txt).
- A proved extension in the existing notes absorbs subexponential integer multiplicities at fixed term count. It does not allow an unbounded number of terms. — [Coefficient extension](../../early-attacks/augmentation-and-return-attacks/coefficient_extension.md).

### Inferences

**Elsner applies directly to the desired resonance condition.** Put

\[
\eta=\frac1{1+\alpha}.
\]

If \(\alpha=[0;a_1,a_2,\ldots]\), then \(\eta=[0;1,a_1,a_2,\ldots]\). Its corresponding convergents are exactly

\[
u/v=q_n/(p_n+q_n).
\]

Apply Elsner with prime 3. For infinitely many of these fractions, \(3\nmid v\), equivalently \(s_n\ne0\). Transforming back gives

\[
q_n^2\left|\alpha-\frac{p_n}{q_n}\right|
=\frac{u}{\eta v}\,v^2\left|\eta-\frac uv\right|.
\tag{14}
\]

The prefactor tends to 1. Therefore, for every fixed \(c>1/\sqrt5\), there are infinitely many **nonresonant convergents of \(\alpha\)** with error \(<c/q_n^2\). This verifies an exact route to the congruence and good approximation together; it does not yield a jump ratio above 5. The sharp examples above satisfy ordinary good approximation while violating that stronger jump condition.

**What phase adjustment has already proved.** In the earlier notation, Elsner applied after inversion yields infinitely many \(p/n\) with \(3\nmid p\) and \(|3\theta-p/n|<c/n^2\), for fixed \(1/\sqrt5<c<1/2\). Grouping the length-\(3n\) orbit into triples leaves a good phase set of measure at least \(1-2c\), and a union bound for subsequent derivative events gives a zero-cocycle orbit segment of length proportional to \(n\). Choosing \(c\) arbitrarily close to \(1/\sqrt5\) improves its numerical constant but leaves the same qualitative scale. Every good phase can be represented by a bounded real cutoff phase; no integer cutoff is intrinsically required.

What is missing is equality or controlled compression of the integrals of the extremal step function between those cutoffs. Equal color counts at their endpoints do not equate sums of jumps with different reciprocal weights. A proof must construct those weighted event families and demonstrate that their number stays bounded, or use a different mechanism altogether.

**Arithmetic acceptance condition.** The useful target is still a fixed \(m\), fixed rational coefficients \(d_i\) (or the already justified fixed-term version with subexponential integer multiplicities), and unbounded scales \(L\) for which

\[
0<t_L\le\min(1,u_1,\ldots,u_m),\quad H(N:u)\le e^{CL},\quad
0<\left|\sum_{i=1}^m d_i u_i-N\right|
\le t_L e^{-\varepsilon_0L}.
\tag{15}
\]

**Erratum from the [final independent audit](final_return_audit.md):** the cap \(t_L\le1\) is necessary for the mixed form with an integer term. The uncapped condition would admit \(u_L=2^L,\ N_L=2^L-1,\ E_L=1,\ t_L=2^L\), which has no arithmetic contradiction. The scalar periodic model already uses \(t=1\) and is unaffected.

The present supply theorem can support such a construction under (8). It cannot turn an error that remains exponentially large after clearing into (15). Polynomial coefficient losses do not repair a missing positive linear exponent, and the coefficient extension does not justify a term count growing with \(q\).

**Narrow exact certificate.** The following standard-library check was run using the prescribed Python executable. It checks one specified three-index obstruction, independently compares the convergent recurrence with continuant matrix multiplication, checks the four-step maps, and checks the resonance pattern on one fixed sparse-spike sample. It is evidence for the algebra, not a substitute for the infinite proofs above.

```python
from fractions import Fraction as F

def convergents(word):
    pm2, pm1, qm2, qm1 = 1, 0, 0, 1
    out = []
    for a in word:
        p, q = a*pm1+pm2, a*qm1+qm2
        out.append((p, q))
        pm2, pm1, qm2, qm1 = pm1, p, qm1, q
    return out

def mul(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))

word = [1]*5 + [3,1,2,1]
cs = convergents(word)
assert cs == [(1,1),(1,2),(2,3),(3,5),(5,8),
              (18,29),(23,37),(64,103),(87,140)]
M = ((0,1),(1,0))
for a, (p,q) in zip(word, cs):
    M = mul(M, ((a,1),(1,0)))
    assert (M[0][0], M[1][0]) == (p,q)
for (p,q),(r,s) in zip(cs,cs[1:]):
    assert abs(p*s-q*r) == 1
assert [(p+q)%3 for p,q in cs[5:8]] == [2,0,2]
assert 37*37-37*29-29*29 < 0
assert 140*140-140*103-103*103 < 0

for R in [F(3,2),F(2),F(3),F(10)]:
    r1 = 1+1/R
    r2 = 1+1/r1
    r3 = 1+1/r2
    assert r2 == (2*R+1)/(R+1)
    assert 1/r3 == (2*R+1)/(3*R+2)
    for k in [1,2,3]:
        assert k+1/r3 == k+(2*R+1)/(3*R+2)

ks = [2 if j in {2,5,11,23} else 1 for j in range(24)]
word2 = [1]*6 + [a for k in ks for a in [k,1,1,1]]
for index,(p,q) in enumerate(convergents(word2),1):
    if index >= 6:
        assert ((p+q)%3 == 0) == ((index-6)%4 == 0)
```

Result: all assertions passed; 9 exact fractions with independent matrices and determinants, the two small-ratio inequalities, four-step maps at four specified rational inputs, and 97 resonance positions.

### Gaps

No unconditional sequence meeting the current \(5+\delta\) requirement, no weighted replacement satisfying (15), and no nonvanishing theorem were obtained. No broad sweep, new density decimal, dependency installation, external posting, further delegation, or Lean work was performed. The sharp supply and obstructions identify the quantitative target for the other return constructions; they do not settle the irrationality problem.
