// Koizumi's exact modular recomputation, for finite orbit exploration only.
import assert from 'node:assert/strict';
import { writeFileSync } from 'node:fs';

const sample = modularOrbit(11n, 29n, 20);
assert.deepEqual(sample.rows.map(r => r.C), [11n,15n,19n,20n,16n]);
assert.deepEqual(sample.rows.map(r => r.E), [-4n,-4n,-1n,4n,0n]);
assert.equal(sample.reason, 'zero gap');

function gcd(a, b) { while (b) [a,b]=[b,a%b]; return a; }
function modularOrbit(C0, D0, maxSteps, forcedPrefix = 0) {
  assert.ok(C0 > 0n && D0 > 0n && Number.isInteger(maxSteps) && maxSteps > 0);
  assert.ok(Number.isInteger(forcedPrefix) && 0 <= forcedPrefix && forcedPrefix <= maxSteps);
  const numerators = [C0], errors = [], rows = [];
  if (forcedPrefix) {
    assert.ok(C0 >= 3n);
    let product = 1n;
    for (let i=0;i<forcedPrefix;i++) product *= C0 + BigInt(i);
    assert.equal((D0 + 1n) % product, 0n);
    // (D'+1)=(D+1)(D+C)/C consumes one factor of the prescribed product.
    for (let i=0;i<forcedPrefix;i++) {
      const C = C0 + BigInt(i);
      rows.push({ C, E: -1n, G: 1n, A: C });
      errors.push(-1n); numerators.push(C+1n);
    }
  }
  for (let n=forcedPrefix;n<maxSteps;n++) {
    const C = numerators[n];
    if (C.toString(2).length > 4096) return { rows, reason: 'numerator size cap' };
    let modulus = numerators.reduce((a,b) => a*b, 1n), residue = D0 % modulus;
    for (let j=0;j<n;j++) {
      assert.equal((residue-errors[j]) % numerators[j], 0n);
      const nextModulus = modulus / numerators[j];
      const multiplier = (residue-errors[j]) / numerators[j] + 1n;
      residue = residue * multiplier % nextModulus;
      modulus = nextModulus;
    }
    assert.equal(modulus,C);
    assert.ok(0n <= residue && residue < C);
    const rounded = (2n*residue+C)/(2n*C), E = residue-rounded*C, G = gcd(C,residue);
    assert.ok(-C <= 2n*E && 2n*E < C);
    rows.push({ C, E, G, A: C/G });
    if (E === 0n) return { rows, reason: 'zero gap' };
    errors.push(E); numerators.push(C-E);
  }
  return { rows, reason: 'step cap' };
}
function direct(C,D,maxSteps) {
  const rows=[];
  for(let n=0;n<maxSteps;n++) {
    const a=(2n*D+C)/(2n*C)+1n, E=D-(a-1n)*C, G=gcd(C,D);
    rows.push({C,E,G,A:C/G});
    if(E===0n)break;
    assert.ok(D.toString(2).length<100000);
    [C,D]=[a*C-D,a*D];
  }
  return rows;
}
for(let q=1n;q<=30n;q++)for(let p=1n;p<=q;p++)if(gcd(p,q)===1n)
  assert.deepEqual(modularOrbit(p,q,16).rows,direct(p,q,16));
for(const M of [3n,5n,17n])for(const N of [1,2,3,7]) {
  let product=1n; for(let j=0;j<N;j++)product*=M+BigInt(j);
  const D0=17n*product-1n, plain=modularOrbit(M,D0,16);
  const directRows=direct(M,D0,10);
  assert.deepEqual(plain.rows.slice(0,directRows.length),directRows);
  assert.deepEqual(modularOrbit(M,D0,16,N),plain);
  for(let j=0;j<N;j++)assert.deepEqual(plain.rows[j],{C:M+BigInt(j),E:-1n,G:1n,A:M+BigInt(j)});
}

const results=[];
const cases=[[17n,32,1n],[101n,128,1n],[1009n,512,1n],[1009n,512,17n],
  [10007n,1024,1n],[10007n,1024,17n]];
for(const [M,N,multiple]of cases) {
  let product=1n;for(let j=0;j<N;j++)product*=M+BigInt(j);
  const D0=multiple*product-1n, orbit=modularOrbit(M,D0,N+2048,N);
  let maxC=0n, maxA=0n, largestTailError={E:0n,C:1n};
  for(const [i,r]of orbit.rows.entries()) {
    maxC=maxC>r.C?maxC:r.C; maxA=maxA>r.A?maxA:r.A;
    const abs=r.E<0n?-r.E:r.E;
    if(i>=N&&abs*largestTailError.C>largestTailError.E*r.C) largestTailError={E:abs,C:r.C};
  }
  const result={M,N,multiple,D0,initialDenominatorBits:D0.toString(2).length,
    reason:orbit.reason,steps:orbit.rows.length,maxC,maxA,
    largestPostForcedError:Number(largestTailError.E*1000000000000n/largestTailError.C)/1e12,
    rows:orbit.rows};
  results.push(result);
  console.log(JSON.stringify({...result,D0:undefined,rows:undefined},(_,v)=>typeof v==='bigint'?v.toString():v));
  writeFileSync('erdos243-modular-results.json',JSON.stringify({
    source:'Koizumi2026 modular recomputation; initial rows also use the proved finite linear-prefix construction.',
    scope:'Finite trajectories of specified rational starts only. Reaching zero proves an eventual Sylvester tail for that start. A cap is not evidence of an infinite orbit or of gaps tending to zero.',
    completed:results.length===cases.length,results},(_,v)=>typeof v==='bigint'?v.toString():v,2));
}
