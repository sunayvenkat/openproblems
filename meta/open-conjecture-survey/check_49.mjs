// Exact totient-sieve and strict LIS screen for the open #49 finite claim.
const limit = Number(process.argv[2] || 2000000);
const phi = Uint32Array.from({length: limit + 1}, (_, i) => i);
phi[1] = 1;
for (let p = 2; p <= limit; ++p) if (phi[p] === p) {
  for (let j = p; j <= limit; j += p) phi[j] -= phi[j] / p;
}
if (phi[10] !== 4 || phi[12] !== 4 || phi[13] !== 12) throw Error('Totient self-check');
const tails = [];
let primes = 0, maxExcess = -Infinity, minExcess = Infinity;
for (let n = 1; n <= limit; ++n) {
  if (n >= 2 && phi[n] === n - 1) ++primes;
  let lo = 0, hi = tails.length;
  while (lo < hi) { const m = (lo + hi) >>> 1; if (tails[m] < phi[n]) lo = m + 1; else hi = m; }
  tails[lo] = phi[n];
  if (n < 2) continue;
  const excess = tails.length - primes;
  maxExcess = Math.max(maxExcess, excess); minExcess = Math.min(minExcess, excess);
  if (excess > 0) { console.log(JSON.stringify({counterexampleN:n,LIS:tails.length,primes})); process.exit(0); }
}
console.log(JSON.stringify({limit,LIS:tails.length,primes,minExcess,maxExcess,counterexample:null}));
