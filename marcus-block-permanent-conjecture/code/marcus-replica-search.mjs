import assert from 'node:assert/strict';
import { writeFileSync } from 'node:fs';
import { gram, permanent } from './marcus-block-search.mjs';

// A necessary test for a stronger Gaussian-chaos comparison, not a certificate
// for Marcus: sums of independent copies need not split into linear factors.
const [rank=3,restarts=100,steps=300,m=3]=process.argv.slice(2).map(Number);
const mode=process.argv[6]??'first';
assert(mode==='first'||(mode==='connected'&&m===3));
function basis(d) {
  const a=[];
  function add(left,prefix) {
    if(prefix.length===rank-1){a.push([...prefix,left]);return;}
    for(let j=0;j<=left;j++)add(left-j,[...prefix,j]);
  }add(d,[]);return a;
}
const b2=basis(2),b4=basis(4),dim=b2.length,lookup=new Map(b4.map((x,i)=>[x.join(','),i])),fac=[1,1,2,6,24],table=[];
for(let i=0;i<dim;i++)for(let j=0;j<dim;j++) {
  const c=b2[i].map((x,s)=>x+b2[j][s]);
  table.push([2*i,2*j,2*lookup.get(c.join(',')),Math.sqrt(c.reduce((z,x,s)=>z*fac[x]/fac[b2[i][s]]/fac[b2[j][s]],1))]);
}
const choices=[];for(let i=0;i<m;i++)for(let j=i+1;j<m;j++)choices.push([i,j]);
const complements=choices.map(pair=>Array.from({length:m},(_,i)=>i).filter(i=>!pair.includes(i)));
const b6=basis(6),lookup6=new Map(b6.map((x,i)=>[x.join(','),i])),fact6=[1,1,2,6,24,120,720],last=[];
if(mode==='connected')for(let i=0;i<b4.length;i++)for(let j=0;j<dim;j++) {
  const c=b4[i].map((x,s)=>x+b2[j][s]);
  last.push([2*i,2*j,2*lookup6.get(c.join(',')),Math.sqrt(c.reduce((z,x,s)=>z*fact6[x]/fact6[b4[i][s]]/fact6[b2[j][s]],1))]);
}
function evaluate(u) {
  const g=gram(u,m,dim),pairs=[];
  for(const indices of choices) {
    const off=indices.map(i=>2*dim*i),p=new Float64Array(2*b4.length);
    for(const [i,j,t,w]of table) {
      const x=i+off[0],y=j+off[1];
      p[t]+=w*(u[x]*u[y]-u[x+1]*u[y+1]);p[t+1]+=w*(u[x]*u[y+1]+u[x+1]*u[y]);
    }pairs.push(p);
  }
  let s=0;
  for(let a=0;a<choices.length;a++)for(let b=0;b<choices.length;b++) {
    let re=0,im=0;const x=pairs[a],y=pairs[b];
    for(let j=0;j<x.length;j+=2){re+=x[j]*y[j]+x[j+1]*y[j+1];im+=x[j]*y[j+1]-x[j+1]*y[j];}
    for(const cols of [choices[b],[choices[b][1],choices[b][0]]]) {
      const x=2*(m*choices[a][0]+cols[0]),y=2*(m*choices[a][1]+cols[1]);
      re-=g[x]*g[y]-g[x+1]*g[y+1];im-=g[x]*g[y+1]+g[x+1]*g[y];
    }
    const small=new Float64Array(2*(m-2)**2);
    for(let i=0;i<m-2;i++)for(let j=0;j<m-2;j++) {
      const x=2*(m*complements[a][i]+complements[b][j]),y=2*((m-2)*i+j);
      small[y]=g[x];small[y+1]=g[x+1];
    }
    const p=permanent(small,m-2).value;s+=p[0]*re-p[1]*im;
  }
  const q=permanent(g,m).value[0];
  if(mode==='first')return s/q;
  if(s/q<1e-6)return 2;
  const triple=new Float64Array(2*b6.length),pair=pairs[0],offset=4*dim;
  for(const [i,j,t,w]of last) {
    const x=offset+j;triple[t]+=w*(pair[i]*u[x]-pair[i+1]*u[x+1]);triple[t+1]+=w*(pair[i]*u[x+1]+pair[i+1]*u[x]);
  }
  const p=triple.reduce((s,x)=>s+x*x,0);return (p-q-s)/s;
}
function normalize(u){for(let i=0;i<m;i++){let s=0;for(let j=0;j<2*dim;j++)s+=u[2*dim*i+j]**2;for(let j=0;j<2*dim;j++)u[2*dim*i+j]/=Math.sqrt(s);}return u;}
function gradient(u){const h=1e-5,g=new Float64Array(u.length);for(let i=0;i<u.length;i++){u[i]+=h;const p=evaluate(u);u[i]-=2*h;const q=evaluate(u);u[i]+=h;g[i]=(p-q)/(2*h);}return g;}
const diagonal=new Float64Array(2*m*dim);
if(rank>=m){for(let i=0;i<m;i++)diagonal[2*(i*dim+b2.findIndex(a=>a[i]===2))]=1;assert(Math.abs(evaluate(diagonal)-(mode==='first'?0:2))<1e-12);}
const same=new Float64Array(2*m*dim);for(let i=0;i<m;i++)same[2*i*dim]=1;assert(Math.abs(evaluate(same)-(mode==='first'?m*(m-1):4/3))<1e-10);
let seed=5131;function random(){seed=Math.imul(1664525,seed)+1013904223|0;return(seed>>>0)/4294967296;}
let best=Infinity,witness;const minima=[];
for(let trial=0;trial<restarts;trial++) {
  let u=normalize(Float64Array.from({length:2*m*dim},()=>2*random()-1)),e=evaluate(u),alpha=.15;
  for(let step=0;step<steps;step++) {
    const g=gradient(u),norm=g.reduce((s,x)=>s+x*x,0);if(norm<1e-15)break;
    let v,f;
    for(let j=0;j<20;j++){v=normalize(Float64Array.from(u,(x,i)=>x-alpha*g[i]));f=evaluate(v);if(f<=e-1e-4*alpha*norm)break;alpha*=.5;}
    if(f>e||alpha<1e-10)break;u=v;e=f;alpha=Math.min(alpha*1.3,1);
  }
  minima.push(e);if(e<best){best=e;witness=Array.from(u);console.log(JSON.stringify({trial,firstCorrection:best}));}
}
const file=`marcus-replica-results-${m}-${rank}-${mode}.json`;
writeFileSync(file,JSON.stringify({m,rank,restarts,steps,mode,basis:b2,bestCorrection:best,u:witness,minima},null,2)+'\n');
console.log(JSON.stringify({file,bestCorrection:best}));
