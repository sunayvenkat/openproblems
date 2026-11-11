# exact check (aur/deep.py, CRT) of piece d=10023013 (K=5) of m=50115065, level s given on the command line
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'aur'))
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'aur'))
from deep import level
s = int(sys.argv[1]); t = time.time()
r = level(50115065, 10023013, s)
print('s=%d first nonzero (offset, coeff) = %s  [%.0fs]' % (s, r, time.time() - t), flush=True)
