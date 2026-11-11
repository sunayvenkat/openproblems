# Independent algebra crosscheck of the Erdős 944 seed, §§3–6

**Verdict:** I found no counterexample or fatal gap in the specified CRT construction, short-ratio lemma, periodic character classification, or finite rounding argument. The derivations below establish their parameter choices and inequalities for every integer `r≥1`, not merely tested instances. This is a targeted proof audit, not a fresh Lean verification or a verification of the entire seed theorem.

I began with `seed-current-text.txt` and then inspected the supplied renderings of PDF pages 5–8 to resolve fractions and subscripts. I did not read the companion `seed.md` before reaching this verdict. Source: [pinned Kruer–Kohlmeyer manuscript](https://github.com/JENW1N/complete-math-solutions/blob/8b9db1d8c0ded5398d5e4e4bbdf8f2ec14ce5c23/papers/erdos-944.pdf), printed pp. 4–8, equations (9)–(40), Lemmas 3.1, 3.2, 5.1 and Proposition 6.1. The local supplied PDF is `seed-source.pdf`, SHA-256 `77e311d97357f98fc33db89ddd63ca6fc3fc5c610bf90075cd9dc1077922ecb8` as independently pinned in the companion source audit.

## 1. Recursive parameters, short ratios, and the five CRT blocks

### Choice of q and the recursive CRT

Set `t=r`, except that `t=r+1` when `5 | 3r+1`, and put `q=3t+1`. Then `t≥r`, `q≥4`, and `q≡1 (mod 3)`. If the exceptional branch occurs, the new q is 3 modulo 5; otherwise it was already nonzero modulo 5. Thus `gcd(q,15)=1`. Neither q nor any subsequent d is required to be prime.

Write `D=30q`, `M=5D`, `a₀=1`, and, for `j≥1`,

`dⱼ=D(κⱼ−1)+1`, `aⱼ=5dⱼ=M(κⱼ−1)+5`.

The recursive conditions are `κⱼ≡0 (mod 3)`, `κⱼ≡1 (mod 5(D−1))`, and `dⱼ≡κᵢ⁻¹ (mod dᵢ)` for every earlier i. The following induction is noncircular:

1. `dᵢ≡1 (mod D)` gives `gcd(dᵢ,D)=1`, in particular coprimality with 3, 5 and q.
2. Since `D≡1 (mod D−1)`, `dᵢ≡κᵢ≡1 (mod D−1)`. Together with `dᵢ≡1 (mod 5)`, this gives `gcd(dᵢ,5(D−1))=1`.
3. A divisor of both κᵢ and dᵢ divides `dᵢ−Dκᵢ=1−D`; κᵢ is 1 modulo D−1, so that divisor is 1. Also κᵢ is 1 modulo 5. Therefore `gcd(κᵢ,aᵢ)=1` and the inverse in the next step exists.
4. The desired new congruence is exactly

   `κⱼ ≡ D⁻¹(κᵢ⁻¹+D−1) (mod dᵢ)`.

5. The earlier dᵢ are pairwise coprime because each new d was prescribed to be a unit modulo every earlier one. The moduli `3`, `5(D−1)`, and all earlier dᵢ are therefore pairwise coprime; `5(D−1)≡1 (mod 3)`.

CRT supplies a full arithmetic progression for κⱼ. Its positive members are unbounded, so one can impose simultaneously `κⱼ≥6` and `aⱼ>10q aⱼ₋₁`. That growth constraint introduces no additional congruence. This completes the induction for the finite number `q−1` of indices.

The claimed residues follow: `dⱼ≡1 (mod 15)`, `κⱼ≡6 (mod 15)`, `aⱼ≡2 (mod 3)`, and `aⱼ≡5 (mod q)`. Useful uniform lower bounds are

`dⱼ≥5D+1=150q+1≥601`, `aⱼ≥3005`.

In particular all appearances of `dⱼ>8`, `aⱼ>100`, and nonempty coordinate intervals have ample margin. Also `0<κⱼ<aⱼ`, since

`aⱼ−κⱼ=(M−1)(κⱼ−1)+4>0`.

### Choice of n and exact inverse identities

Let `P=5∏dⱼ` and `L=3P=15∏dⱼ`. The system for n is equivalent to congruences modulo the pairwise coprime integers `3,q,5,d₁,…,d_q₋₁`:

- n is 1 modulo 3 and 0 modulo q;
- n is −1 modulo 5;
- n is `−κⱼ⁻¹` modulo dⱼ.

The common modulo-5 condition is consistent because every κⱼ is 1 modulo 5. The solutions form a progression of step `qL`. Choose any member with

`n>1000(r+1)qL²`.

All d, P and L have already been fixed before this choice; there is no circular large-n requirement. Every aⱼ is a unit modulo n. Moreover every `aᵢ≤P=L/3`, and the size bound implies `n>4qP`, `n>q`, `n>2L`, and `n>1`.

The quotient `(1+κⱼn)/aⱼ` is integral by the defining congruence. It is positive and less than n because κⱼ≤aⱼ−1 and n>1. It is consequently the least positive inverse of aⱼ modulo n, as claimed in (20).

For any integer `0<s<n`, let `eⱼ(s)=[κⱼs]_(aⱼ)`. Then

`R=(s+eⱼ(s)n)/aⱼ`

is integral, satisfies `aⱼR≡s (mod n)`, and lies strictly between 0 and n: its numerator is at most `(n−1)+(aⱼ−1)n<aⱼn`. This proves the exact normalized-coordinate identity (25), without a hidden floor or representative assumption.

### Lemma 3.2: every ordered pair of distinct indices

For denominator index `j=0`, the normalized ratio is just aᵢ. It is positive, below `n/q`, and 2 modulo 3.

For `j>0`, put `ℓ=[aᵢκⱼ]_(aⱼ)`. The candidate ratio is the integer

`Rᵢⱼ=(aᵢ+ℓn)/aⱼ`.

There are three genuinely different cases:

- **i=0.** Here `ℓ=κⱼ`. Since κⱼ≥6,

  `κⱼ/aⱼ < κⱼ/[5D(κⱼ−1)] ≤ 6/(25D)=1/(125q)<1/(4q)`.

- **i>j≥1.** The recursive condition gives `dᵢκⱼ≡1 (mod dⱼ)`, hence `aᵢκⱼ≡5 (mod aⱼ)`. Since aⱼ>5, `ℓ=5`; thus `ℓ/aⱼ=1/dⱼ<1/(4q)`.

- **0<i<j.** From `aⱼ=M(κⱼ−1)+5`, the exact identity is

  `aᵢκⱼ/aⱼ = (κᵢ−1)+5/M+(aᵢ/aⱼ)(1−5/M)`.

  The last two terms form a positive number less than

  `1/(30q)+1/(10q)=2/(15q)<1/(4q)<1`.

  Thus the integer part really is κᵢ−1, and `ℓ/aⱼ` is that positive fractional part. This also proves `ℓ≡aᵢκⱼ−aⱼ(κᵢ−1)≡2 (mod 3)`.

For i>0 both relevant cases have `ℓ≡2 (mod 3)`, while for i=0 it is 0. Substituting `aⱼ≡2` and `n≡1 (mod 3)` into the integer identity for R gives `Rᵢⱼ≡2 (mod 3)` in all cases. Also

`0<Rᵢⱼ/n=aᵢ/(aⱼn)+ℓ/aⱼ < 1/(4q)+1/(4q)=1/(2q)`.

The ratio is therefore the least positive residue, and satisfies the claimed stronger-than-needed size estimate. Equality of direction pairs would make a ratio 1 or n−1; their residues modulo 3 are 1 and 0, respectively, so neither can occur.

### Core membership and independent five-block coordinates

The above ratio bounds put every ±aᵢ into every `aⱼN_n`, and `aᵢ<n/2` excludes the involution. Multiplying an off-diagonal ratio by any `ℓ≤q` with `ℓ≡1 (mod 3)` causes no wrap and gives residue 2 modulo 3, proving the short compatibility needed for the chords.

Away from the exceptional ±aᵢ, membership in all normalized middle-residue classes is equivalent to

`s≡2 (mod 3)` and `eⱼ(s)≡2 (mod 3)` for every j.

Indeed `(s+eⱼn)/aⱼ≡2 (mod 3)` is equivalent to `s+eⱼ≡1`, and with s≡2 this says eⱼ≡2. These conditions have period L.

Because κⱼ≡1 modulo 5, eⱼ(s) and s have the same modulo-5 residue. For h=0,…,4 write

`eⱼ=2+3h+15yⱼ`, `mⱼ=(dⱼ−1)/3`.

Writing `dⱼ=15k+1` gives `aⱼ=75k+5` and `mⱼ=5k`. Listing eⱼ in `[0,aⱼ)` gives exactly `0≤yⱼ≤mⱼ` for h=0, and `0≤yⱼ≤mⱼ−1` for h>0. There is no lost endpoint: the h=0 final entry is aⱼ−3, whereas the h=1 candidate at y=mⱼ is aⱼ and is excluded.

Multiplication by κⱼ is invertible modulo dⱼ. CRT therefore makes all these coordinate choices independent after fixing s modulo 3 and 5. Each block is nonempty, and the five blocks are disjoint modulo 5. In particular the generic residue set R has at least five classes, enough to choose a class avoiding the possible involution.

## 2. Lemma 5.1: exact character rigidity

### Common real interval and character coordinates

The hypothesis requires the **whole** continuous path `αρ+βx (mod 1)`, `0≤x≤1`, to lie in the closed middle-third arc B. A continuous lift cannot cross the gaps between different integer translates of B. Hence `|β|≤1/3`. All initial phases have real representatives in the same interval

`I=B∩(B−β)`, of width `1/3−|β|`.

The character group of `Z/LZ` splits over `3,5,d₁,…,d_q₋₁`; replacing s modulo dⱼ by κⱼs modulo dⱼ is an invertible change of coordinates. Thus decomposition (31) is valid:

`αs ≡ u(s mod 3)/3+v(s mod 5)/5+Σ cⱼ eⱼ(s)/dⱼ (mod 1)`.

### Sparsity is forced by independence, not by cancellation

On the h=0 product, increasing yⱼ by one changes a phase by `15cⱼ/dⱼ (mod 1)`. Actual differences of the representatives in I lie in `[-1/3,1/3]`. This interval has length less than 1, so there is at most one representative of each modular difference. The actual increment δⱼ is therefore constant over the whole product and has the form `zⱼ/dⱼ` for integer zⱼ.

The real phase is affine on the independent rectangular grid. Its range has width exactly `Σmⱼ|δⱼ|`, by choosing each coordinate endpoint according to the sign of δⱼ. Thus

`Σ (dⱼ−1)|zⱼ|/(3dⱼ) ≤ 1/3`.

For a nonzero zⱼ, this gives `|zⱼ|≤dⱼ/(dⱼ−1)<2`, hence zⱼ=±1. Two nonzero coordinates would contribute

`2/3−1/(3dᵢ)−1/(3dⱼ)>1/3`,

because dᵢ,dⱼ>8. There is consequently at most one active coordinate. Opposite signs do not evade this estimate: the coordinates vary independently, so the width contains absolute values.

### No active coordinate

If δⱼ=0, then `15cⱼ≡0 (mod dⱼ)`, hence cⱼ=0 modulo dⱼ because `gcd(15,dⱼ)=1`. If v≠0 modulo 5, the five blocks give all five equally spaced fifths after a translation. They contain points of circular separation 2/5 and cannot fit into I of width at most 1/3. Therefore v=0.

The remaining phase is `2u/3 (mod 1)`, so u is 1 or 2. Thus α is 1/3 or 2/3 modulo 1. Since n≡1 modulo 3 and `K=αn+β` is integral, the bound `|β|≤1/3` forces respectively β=−1/3 or β=1/3. These give `K≡±(n−1)/3 (mod n)`, the desired conclusion with a₀=1.

### One active coordinate and the five-block frequency

Negating α and β preserves the hypothesis because `−B=B`. We may assume the active increment is `1/d`, where `a=5d`, `m=(d−1)/3`. Take `c=(1−d)/15`, an integer satisfying `15c≡1 (mod d)`.

The first phase in block h has the modular expression

`P_h ≡ 2u/3+(3v−1)(2+3h)/15+(2+3h)/(15d)`.

Within a block the actual increment is +1/d, by the same unique-difference argument. The h=0 block has width m/d, and the other blocks width `(m−1)/d`. All starting representatives must therefore lie in an interval of width at most

`1/3−(m−1)/d=4/(3d)`.

Consecutive starts differ modulo 1 by

`Δ=(3v−1)/5+1/(5d)`.

If v is not 2 modulo 5, its **distance to the nearest integer** is at least

`1/5−1/(5d)=(d−1)/(5d)>4/(3d)`.

The last strict inequality is equivalent to `3(d−1)>20` and follows from d>8. This contradicts the starting-interval width. Hence v=2. It would be incorrect to substitute an unqualified fractional-part bound here; the manuscript correctly uses distance from an integer.

When v=2 the actual consecutive start difference is `1/(5d)`, not this number minus 1, because all starts are confined to the short real interval. Thus `P_h=P₀+h/(5d)`. Every later block starts to the right of P₀ by at most `4/(5d)` but is shorter by 1/d. Its right endpoint is therefore below `P₀+m/d`. The entire real range is controlled by the h=0 block.

Its initial phase is `2u/3+2/3+2/(15d) (mod 1)`. For u=0 this is above 2/3; for u=2 it is below 1/3. Only u=1 works, producing exactly the range

`[1/3+2/(3a), 2/3−1/a]`.

### Exact β, including small-grid and integrality issues

For this range and its whole β-translate segment to stay in B one needs

`−2/(3a)≤β≤1/a`.

The character decomposition simplifies to `α≡1/3+κ/(3a) (mod 1)`: the difference in the other terms is `(6−κ)/15`, an integer. Now

`(1/3+κ/(3a))n+1/(3a)=((a+κ)n+1)/(3a)`

is integral. Its numerator is divisible by a because κn≡−1 modulo a, and by 3 because a≡2, κ≡0 and n≡1 modulo 3; `gcd(a,3)=1` allows the combined denominator.

Thus every admissible β differs from `1/(3a)` by an integer. The allowed interval has length `5/(3a)<1` and contains `1/(3a)`, so that is the unique β. This argument does not assume all β on the finer 1/L grid are separated by 1; it uses the already determined α modulo 1 and integer K to get the stronger integer difference.

Consequently `3aK≡1 (mod n)`. Since n≡1 modulo 3, its solution is

`aK≡(2n+1)/3≡−(n−1)/3 (mod n)`.

Negation supplies the other sign. This completes the character classification with no unproved uniformity step.

## 3. Proposition 6.1: finite sampling, exact rounding, and audit limits

### Every size estimate follows from the stated n bound

The required inequalities can be made explicit:

- `n>4r` makes `w=1/3+2r/(3n)<1/2`;
- `n>4r+6L` makes `w/(1−2L/n)<1/2`;
- `n>2L` makes the progression and its endpoint choices nondegenerate;
- `n>rL/3+L²/2` makes the endpoint rounding error strictly below 1/L.

All follow uniformly from `n>1000(r+1)qL²`, since r≥1, q≥4, L≥15. For example `(r+1)L≥r+L`, so `1000(r+1)qL²>4r+6L`. Also `rL/3+L²/2≤(r/3+1/2)L²<1000(r+1)qL²`. No asymptotic or eventual-in-r argument is being substituted for these finite inequalities.

### One uninterrupted progression gives a signed integer lift

Since `F(K)≤r` is a sum of nonnegative deficits and deficits are invariant under sign, every s in S has its phase in

`B_ε=[1/3−ε,2/3+ε]`, `ε=r/(3n)`.

Choose a generic residue class which does not contain the possible involution n/2; R has at least five classes. All its positive representatives below n lie in S. If the first representative is b with `1≤b≤L`, the number of representatives is `ceil((n−b)/L)≥n/L−1`. Thus there are at least `n/L−2` successive differences.

Their ordinary phase representatives all lie in the same real interval of width `w<1/2`. Every consecutive difference is congruent to `KL/n (mod 1)` and lies in `[-w,w]`, an interval of length less than 1. These differences must therefore all be one common δ. Write

`δ=KL/n−p`, with integer p, and set `α=p/L`, `β=nδ/L=K−pn/L`.

Telescoping gives `|δ|(n/L−2)≤w` and hence

`|β|≤w/(1−2L/n)<1/2`.

The integer p is chosen from the actual signed increment. It need not be `floor(KL/n)`; a negative increment may require the ceiling. The manuscript only asks for an integer lift, which is sufficient and correct.

### Endpoint rounding works even for the class containing the removed involution

For each generic class ρ, including the exceptional class just avoided, let s₀ and s₁ be its first and last positive representatives below n. Then `s₀≤L` and `n−s₁≤L`. Since n>2L, s₀<n/2<s₁; neither is the removed involution. Both therefore have the required phase estimate in B_ε.

Because `Ks/n≡αρ+βs/n (mod 1)`, these two estimates put αρ and αρ+β at circular distance from B at most

`ε+|β|L/n < (r/3+L/2)/n < 1/L`.

Both target phases lie on the exact grid `(1/L)Z/Z`, since α=p/L and β=K−pn/L. Both endpoints of B also lie on that grid, since 3 divides L. Any grid point outside this closed arc is at circular distance at least 1/L from it. Therefore both target phases are actually inside B. The strict error estimate, not a limiting argument, is essential here and is supplied by the stated n bound.

Take their real representatives x₀,x₁ in B. Then `x₁−x₀∈[-1/3,1/3]` and it is congruent to β modulo 1. Since `|β|<1/2`, their difference from β has absolute value less than 5/6 and is an integer; it must be zero. Hence the full interpolating segment is the real segment from x₀ to x₁ and stays in B. This proves Lemma 5.1's hypothesis simultaneously for every generic class, using the same α and β.

The resulting canonical relation `Kaᵢ≡±(n−1)/3 (mod n)` gives precisely deficit 1: the smaller circular residue is `(n−1)/3`, and `n−3(n−1)/3=1`. Thus Condition (iv) follows exactly as claimed.

### What this audit establishes and does not establish

The supplied arguments survive targeted attempts to exploit composite CRT moduli, the common factor 5, reversed index order in the ratios, cancellation of two active coefficients, the block-endpoint off-by-one, negative phase increments, the difference between floor and nearest-integer distance, the fine β grid, and the single removed involution. The proof addresses these points correctly, although several require the expansions above to become transparent.

I did not run Lean, trust a finite computation as a proof, optimize any constants, or inspect the height/winding and three-step-word arguments as part of this reassignment. Those are separate dependencies of the whole seed theorem. The conclusion here is limited to the mathematical validity of the stated §§3–6 under their explicit setup; it does not replace the full-seed audit or independently certify the formal source.
