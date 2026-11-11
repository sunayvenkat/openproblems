import assert from 'node:assert/strict';
import { writeFileSync } from 'node:fs';
import { pathToFileURL } from 'node:url';

// Interleaved complex arrays; Gram matrices use <v_i,v_j> = conjugate(v_i) v_j.
const counts = new Map();
function population(n) {
  if (!counts.has(n)) {
    const c = new Uint8Array(1 << n);
    for (let s = 1; s < c.length; s++) c[s] = c[s >> 1] + (s & 1);
    counts.set(n, c);
  }
  return counts.get(n);
}

export function permanent(a, n, derivative = false) {
  const size = 1 << n, pop = population(n), f = new Float64Array(2 * size);
  f[0] = 1;
  for (let s = 0; s < size - 1; s++) {
    const row = pop[s], x = f[2*s], y = f[2*s+1];
    for (let j = 0; j < n; j++) if (!(s & (1 << j))) {
      const z = 2*(row*n+j), t = 2*(s | (1 << j));
      f[t] += x*a[z] - y*a[z+1];
      f[t+1] += x*a[z+1] + y*a[z];
    }
  }
  const value = [f[2*size-2], f[2*size-1]];
  if (!derivative) return { value };
  const b = new Float64Array(2*size), grad = new Float64Array(2*n*n);
  b[2*size-2] = 1;
  for (let s = size-2; s >= 0; s--) {
    const row = pop[s];
    for (let j = 0; j < n; j++) if (!(s & (1 << j))) {
      const z = 2*(row*n+j), t = 2*(s | (1 << j));
      b[2*s] += a[z]*b[t] - a[z+1]*b[t+1];
      b[2*s+1] += a[z]*b[t+1] + a[z+1]*b[t];
      grad[z] += f[2*s]*b[t] - f[2*s+1]*b[t+1];
      grad[z+1] += f[2*s]*b[t+1] + f[2*s+1]*b[t];
    }
  }
  return { value, grad };
}

export function gram(v, n, rank) {
  const a = new Float64Array(2*n*n);
  for (let i = 0; i < n; i++) for (let j = 0; j < n; j++) {
    const z = 2*(i*n+j);
    for (let d = 0; d < rank; d++) {
      const x = 2*(i*rank+d), y = 2*(j*rank+d);
      a[z] += v[x]*v[y] + v[x+1]*v[y+1];
      a[z+1] += v[x]*v[y+1] - v[x+1]*v[y];
    }
  }
  return a;
}

export function evaluate(v, m, k, rank, derivative = true) {
  const n = m*k, a = gram(v,n,rank), g = new Float64Array(2*m*m), blocks = [];
  for (let i = 0; i < m; i++) for (let j = 0; j < m; j++) {
    const block = new Float64Array(2*k*k);
    for (let u = 0; u < k; u++) for (let w = 0; w < k; w++) {
      const z = 2*((i*k+u)*n+j*k+w), t = 2*(u*k+w);
      block[t] = a[z]; block[t+1] = a[z+1];
    }
    const p = permanent(block,k,derivative);
    g[2*(i*m+j)] = p.value[0]; g[2*(i*m+j)+1] = p.value[1];
    blocks.push(p);
  }
  const p = permanent(a,n,derivative), q = permanent(g,m,derivative);
  assert(p.value[0] > 0 && q.value[0] > 0);
  assert(Math.abs(p.value[1]) < 1e-8*p.value[0]);
  assert(Math.abs(q.value[1]) < 1e-8*q.value[0]);
  const value = Math.log(p.value[0]/q.value[0]);
  if (!derivative) return {value,p:p.value[0],q:q.value[0]};
  const grad = new Float64Array(v.length);
  for (let i = 0; i < n; i++) for (let j = 0; j < n; j++) {
    const z = 2*(i*n+j), b = Math.floor(i/k)*m+Math.floor(j/k), t = 2*((i%k)*k+j%k);
    const c = blocks[b].grad, qr = q.grad[2*b], qi = q.grad[2*b+1];
    const dr = p.grad[z]/p.value[0] - (qr*c[t]-qi*c[t+1])/q.value[0];
    const di = p.grad[z+1]/p.value[0] - (qr*c[t+1]+qi*c[t])/q.value[0];
    for (let d = 0; d < rank; d++) {
      const x = 2*(i*rank+d), y = 2*(j*rank+d);
      grad[x] += 2*(dr*v[y]-di*v[y+1]);
      grad[x+1] += 2*(dr*v[y+1]+di*v[y]);
    }
  }
  return {value,p:p.value[0],q:q.value[0],grad};
}

function normalize(v, rank) {
  for (let i = 0; i < v.length; i += 2*rank) {
    let norm = 0;
    for (let d = 0; d < 2*rank; d++) norm += v[i+d]**2;
    norm = Math.sqrt(norm);
    for (let d = 0; d < 2*rank; d++) v[i+d] /= norm;
  }
  return v;
}
function rng(seed) {
  return () => { seed |= 0; seed = seed + 0x6D2B79F5 | 0; let t = Math.imul(seed ^ seed >>> 15, 1 | seed); t ^= t + Math.imul(t ^ t >>> 7, 61 | t); return ((t ^ t >>> 14) >>> 0)/4294967296; };
}

function selfCheck() {
  const random = rng(7231);
  for (let n = 1; n <= 6; n++) {
    const a = Float64Array.from({length:2*n*n},()=>2*random()-1);
    let re = 0, im = 0;
    function visit(row,used,x,y) {
      if (row === n) {re+=x; im+=y; return;}
      for (let j=0;j<n;j++) if (!(used&(1<<j))) {
        const z=2*(row*n+j);
        visit(row+1,used|(1<<j),x*a[z]-y*a[z+1],x*a[z+1]+y*a[z]);
      }
    }
    visit(0,0,1,0);
    const p=permanent(a,n,true);
    assert(Math.abs(re-p.value[0])+Math.abs(im-p.value[1])<1e-9);
  }
  for (const [m,k,rank] of [[3,2,4],[2,3,3],[4,2,5]]) {
    const v=normalize(Float64Array.from({length:2*m*k*rank},()=>2*random()-1),rank);
    const e=evaluate(v,m,k,rank), h=1e-5;
    for(let z=0;z<v.length;z++) {
      v[z]+=h; const plus=evaluate(v,m,k,rank,false).value;
      v[z]-=2*h; const minus=evaluate(v,m,k,rank,false).value; v[z]+=h;
      assert(Math.abs(e.grad[z]-(plus-minus)/(2*h))<2e-7,`gradient ${m},${k},${z}`);
    }
  }
  const identity=new Float64Array(72);
  for(let i=0;i<6;i++)identity[2*(6*i+i)]=1;
  assert.equal(evaluate(identity,3,2,6).value,0);
  const ones=new Float64Array(12); for(let i=0;i<6;i++)ones[2*i]=1;
  const e=evaluate(ones,3,2,1); assert.equal(e.p,720); assert.equal(e.q,48);
  console.log('Self-check: direct permutation sums, finite-difference gradients, identity and rank-one formulas passed.');
}

export function search(m,k,rank,restarts=100,steps=500,seed=1) {
  const random=rng(seed), n=m*k; let best=Infinity, witness, bestP, bestQ;
  const minima=[];
  for(let trial=0;trial<restarts;trial++) {
    let v=normalize(Float64Array.from({length:2*n*rank},()=>2*random()-1),rank);
    let e=evaluate(v,m,k,rank), alpha=.2;
    for(let iter=0;iter<steps;iter++) {
      let norm=0; for(const x of e.grad)norm+=x*x;
      if(norm<1e-20)break;
      let next,ne;
      for(let ls=0;ls<25;ls++) {
        next=normalize(Float64Array.from(v,(x,z)=>x-alpha*e.grad[z]),rank);
        ne=evaluate(next,m,k,rank,false);
        if(ne.value<=e.value-1e-4*alpha*norm)break;
        alpha*=.5;
      }
      if(ne.value>e.value || alpha<1e-12)break;
      v=next; e=evaluate(v,m,k,rank); alpha=Math.min(alpha*1.3,2);
      if(e.value < -1e-7)break;
    }
    minima.push(Math.exp(e.value));
    if(e.value<best) {
      best=e.value; witness=Array.from(v); bestP=e.p; bestQ=e.q;
      console.log(JSON.stringify({m,k,rank,trial,ratio:Math.exp(best)}));
    }
    if(best < -1e-7)break;
  }
  return {m,k,rank,restarts: minima.length,steps,seed,bestRatio:Math.exp(best),p:bestP,q:bestQ,v:witness,minima};
}

if (process.argv[1] && import.meta.url===pathToFileURL(process.argv[1]).href) {
  selfCheck();
  if(process.argv[2]!=='check') {
    const [m=3,k=2,rank=4,restarts=100,steps=500,seed=1]=process.argv.slice(2).map(Number);
    const result=search(m,k,rank,restarts,steps,seed);
    const filename=`marcus-block-results-${m}-${k}-${rank}-${seed}.json`;
    writeFileSync(filename,JSON.stringify(result,null,2)+'\n');
    console.log(JSON.stringify({file:filename,bestRatio:result.bestRatio}));
  }
}
