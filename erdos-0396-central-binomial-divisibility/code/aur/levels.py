# Print the level-s first coefficient (offset, value) for s = s0..s1 of piece d in x^m+1.
import sys, time
from deep import level
m, d, s0, s1 = map(int, sys.argv[1:5])
for s in range(s0, s1 + 1):
    t = time.time(); r = level(m, d, s)
    print(f's={s} {"None" if r is None else "offset %d coeff %.3e" % r} ({time.time() - t:.0f}s)', flush=True)
    if r and r[1] < 0: break
