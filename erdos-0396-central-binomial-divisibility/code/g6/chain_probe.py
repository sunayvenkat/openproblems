# Count Q-square solutions per position pattern and time the extension tests (k = 4).
import itertools, time, sys
from chain import solve4, square_roots
S = int(sys.argv[1]); t0 = time.time(); cnt = {}; ext = 0
for s in itertools.permutations(range(1, S + 1), 4):
    zs = [x * x for x in s]
    for P in [(0, 1, 2, 3), (0, 1, 2, 4), (0, 1, 3, 4), (0, 2, 3, 4)]:
        sol = solve4(zs, list(P))
        if not sol: continue
        cnt[P] = cnt.get(P, 0) + 1
        miss = [m for m in range(5) if m not in P] + [-1, 5]
        for m in miss:
            if square_roots(*sol, m): ext += 1; print("EXT", s, P, m, flush=True)
print(cnt, "extensions", ext, "time %.1f" % (time.time() - t0))
