import assert from 'node:assert/strict';
import { writeFileSync } from 'node:fs';
import { gram, permanent, evaluate as gramEvaluate } from './marcus-block-search.mjs';

// Tests the stronger statement for arbitrary homogeneous polynomials.
// These polynomials need not split into linear factors, so a failure here alone
// would not disprove Marcus's conjecture.
const [m=3,k=2,r=3,restarts=100,steps=600]=process.argv.slice(2).map(Number);
const fact=[1]; for(let j=1;j<=m*k;j++)fact[j]=j*fact[j-1];
const bases=new Map(), maps=new Map();
function basis(d) {
  if(bases.has(d))return bases.get(d);
  const a=[];
  function add(left,prefix) {
    if(prefix.length===r-1) {a.push([...prefix,left]);return;}
    for(let j=0;j<=left;j++)add(left-j,[...prefix,j]);
  }
  add(d,[]); bases.set(d,a); return a;
}
function table(d,e) {
  const key=`${d},${e}`; if(maps.has(key))return maps.get(key);
  const a=basis(d),b=basis(e),c=basis(d+e),lookup=new Map(c.map((x,j)=>[x.join(','),j]));
  const rows=[];
  for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++) {
    const sum=a[i].map((v,s)=>v+b[j][s]);
    const w=Math.sqrt(sum.reduce((z,v,s)=>z*fact[v]/(fact[a[i][s]]*fact[b[j][s]]),1));
    rows.push([2*i,2*j,2*lookup.get(sum.join(',')),w]);
  }
  maps.set(key,rows);return rows;
}
const dim=basis(k).length;
function evaluate(u,derivative=true) {
  const f=[new Float64Array([1,0])];
  for(let i=0;i<m;i++) {
    const next=new Float64Array(2*basis((i+1)*k).length), offset=2*i*dim;
    for(const [a,b,c,w] of table(i*k,k)) {
      next[c]+=w*(f[i][a]*u[offset+b]-f[i][a+1]*u[offset+b+1]);
      next[c+1]+=w*(f[i][a]*u[offset+b+1]+f[i][a+1]*u[offset+b]);
    }
    f.push(next);
  }
  const p=f[m].reduce((s,x)=>s+x*x,0), q=permanent(gram(u,m,dim),m,derivative);
  const value=Math.log(p/q.value[0]);
  if(!derivative)return {value,p,q:q.value[0]};
  const grad=new Float64Array(u.length);let back=f[m];
  for(let i=m-1;i>=0;i--) {
    const prev=new Float64Array(f[i].length),offset=2*i*dim;
    for(const [a,b,c,w] of table(i*k,k)) {
      grad[offset+b]+=2*w*(f[i][a]*back[c]+f[i][a+1]*back[c+1])/p;
      grad[offset+b+1]+=2*w*(f[i][a]*back[c+1]-f[i][a+1]*back[c])/p;
      prev[a]+=w*(u[offset+b]*back[c]+u[offset+b+1]*back[c+1]);
      prev[a+1]+=w*(u[offset+b]*back[c+1]-u[offset+b+1]*back[c]);
    }
    back=prev;
  }
  for(let i=0;i<m;i++)for(let j=0;j<m;j++)for(let s=0;s<dim;s++) {
    const z=2*(i*m+j),a=2*(i*dim+s),b=2*(j*dim+s);
    grad[a]-=2*(q.grad[z]*u[b]-q.grad[z+1]*u[b+1])/q.value[0];
    grad[a+1]-=2*(q.grad[z]*u[b+1]+q.grad[z+1]*u[b])/q.value[0];
  }
  return {value,p,q:q.value[0],grad};
}
function normalize(u) {
  for(let i=0;i<m;i++) {
    let norm=0;for(let s=0;s<2*dim;s++)norm+=u[2*i*dim+s]**2;
    for(let s=0;s<2*dim;s++)u[2*i*dim+s]/=Math.sqrt(norm);
  }return u;
}
let seed=23217;
function random(){seed=(Math.imul(seed,1664525)+1013904223)|0;return (seed>>>0)/4294967296;}
const check=normalize(Float64Array.from({length:2*m*dim},()=>2*random()-1)),ce=evaluate(check),h=1e-5;
for(let z=0;z<check.length;z++) {
  check[z]+=h;const plus=evaluate(check,false).value;check[z]-=2*h;const minus=evaluate(check,false).value;check[z]+=h;
  assert(Math.abs(ce.grad[z]-(plus-minus)/(2*h))<1e-7);
}
// Split-polynomial check against the independent Gram permanent calculation.
const v=Float64Array.from({length:2*m*k*r},()=>2*random()-1),split=new Float64Array(2*m*dim);
for(let i=0;i<m;i++) {
  let f=new Float64Array([1,0]);
  for(let j=0;j<k;j++) {
    const next=new Float64Array(2*basis(j+1).length);
    for(const [a,b,c,w]of table(j,1)) {
      const coord=basis(1)[b/2].indexOf(1),z=2*((i*k+j)*r+coord);
      next[c]+=w*(f[a]*v[z]-f[a+1]*v[z+1]);next[c+1]+=w*(f[a]*v[z+1]+f[a+1]*v[z]);
    }f=next;
  }split.set(f,2*i*dim);
}
assert(Math.abs(evaluate(split,false).value-gramEvaluate(v,m,k,r,false).value)<1e-9);
console.log('Self-check: gradients and split-polynomial Gram identity passed.');
let best=Infinity,witness,minima=[];
for(let trial=0;trial<restarts;trial++) {
  let u=normalize(Float64Array.from({length:2*m*dim},()=>2*random()-1)),e=evaluate(u),alpha=.2;
  for(let step=0;step<steps;step++) {
    const norm=e.grad.reduce((s,x)=>s+x*x,0);if(norm<1e-20)break;
    let next,ne;
    for(let ls=0;ls<25;ls++) {
      next=normalize(Float64Array.from(u,(x,z)=>x-alpha*e.grad[z]));ne=evaluate(next,false);
      if(ne.value<=e.value-1e-4*alpha*norm)break;alpha*=.5;
    }
    if(ne.value>e.value||alpha<1e-12)break;
    u=next;e=evaluate(u);alpha=Math.min(2,alpha*1.3);
  }
  minima.push(Math.exp(e.value));
  if(e.value<best){best=e.value;witness=Array.from(u);console.log(JSON.stringify({trial,ratio:Math.exp(best)}));}
}
const file=`marcus-chaos-results-${m}-${k}-${r}.json`;
writeFileSync(file,JSON.stringify({m,k,r,restarts,steps,bestRatio:Math.exp(best),basis:basis(k),u:witness,minima},null,2)+'\n');
console.log(JSON.stringify({file,bestRatio:Math.exp(best)}));
