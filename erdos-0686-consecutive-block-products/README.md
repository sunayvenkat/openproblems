# Erdős #686, ratio-25 variant: products of consecutive blocks

**Target.** Can (m+1)(m+2)⋯(m+k) = 25·(n+1)(n+2)⋯(n+k) hold with disjoint blocks, for unbounded block length k? ([conjectures.io entry](https://conjectures.io/problems/erdos686-erdos-686-variants-twenty-five))

## Status: OPEN. Only k = 3 is treated here.

[notes/erdos686-length-three.tex](notes/erdos686-length-three.tex) treats k = 3. With x = m+2 and y = n+2 the equation becomes x³ − x = 25(y³ − y). This reduces to the 60 Thue equations a³ − 25b³ = −h, one for each h | 15600. The complete solutions come from Magma V2.29-10 (`code/erdos686-thue-check.m`, output in `results/erdos686-thue-results.json`). A postfilter (`code/erdos686-thue-verify.mjs`) then excludes k = 3. Completeness rests on Magma's Thue solver and has not been certified independently. `code/erdos686-elliptic-search.mjs` is an earlier direct search. No novelty claim is made.
