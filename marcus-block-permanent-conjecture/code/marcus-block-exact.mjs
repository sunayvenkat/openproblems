import assert from 'node:assert/strict';
import { writeFileSync } from 'node:fs';
import { pathToFileURL } from 'node:url';

const add=(a,b)=>[a[0]+b[0],a[1]+b[1]];
const mul=(a,b)=>[a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]];
const conjugate=a=>[a[0],-a[1]];
export function exactPermanent(a) {
  const n=a.length,f=Array.from({length:1<<n},()=>[0n,0n]);f[0]=[1n,0n];
  for(let s=0;s<f.length-1;s++) {
    let row=0;for(let z=s;z;z&=z-1)row++;
    for(let j=0;j<n;j++)if(!(s&(1<<j))) {
      const t=s|(1<<j);f[t]=add(f[t],mul(f[s],a[row][j]));
    }
  }return f.at(-1);
}
export function exactGram(v) {
  return v.map(x=>v.map(y=>x.reduce((s,z,d)=>add(s,mul(conjugate(z),y[d])),[0n,0n])));
}
const submatrix=(a,rows,cols)=>rows.map(i=>cols.map(j=>a[i][j]));
export function exactCertificate(v,m,k) {
  const a=exactGram(v),groups=Array.from({length:m},(_,i)=>Array.from({length:k},(_,j)=>k*i+j));
  const g=groups.map(rows=>groups.map(cols=>exactPermanent(submatrix(a,rows,cols))));
  const p=exactPermanent(a),q=exactPermanent(g);
  assert.equal(p[1],0n);assert.equal(q[1],0n);
  const result={m,k,v,a,g,p:p[0],q:q[0],difference:p[0]-q[0]};
  if(m===3) {
    const complements=groups.map(group=>Array.from({length:m*k},(_,i)=>i).filter(i=>!group.includes(i)));
    let s=[0n,0n];for(let i=0;i<m;i++)for(let j=0;j<m;j++)s=add(s,mul(g[i][j],exactPermanent(submatrix(a,complements[i],complements[j]))));
    assert.equal(s[1],0n);
    result.S=s[0];result.D1=s[0]-3n*q[0];result.D2=p[0]-s[0]+2n*q[0];
    assert.equal(result.D1+result.D2,result.difference);
  }
  return result;
}
function directPermanent(a) {
  let sum=[0n,0n];
  function visit(i,used,p) {if(i===a.length){sum=add(sum,p);return;}for(let j=0;j<a.length;j++)if(!(used&(1<<j)))visit(i+1,used|(1<<j),mul(p,a[i][j]));}
  visit(0,0,[1n,0n]);return sum;
}
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href) {
  const sample=[[[2n,0n],[1n,1n],[0n,-1n]],[[1n,-1n],[3n,0n],[2n,2n]],[[0n,1n],[2n,-2n],[5n,0n]]];
  assert.deepEqual(exactPermanent(sample),directPermanent(sample));
  const identity=Array.from({length:6},(_,i)=>Array.from({length:6},(_,j)=>[BigInt(i===j),0n]));
  assert.equal(exactCertificate(identity,3,2).difference,0n);
  const triangle=[
    [[1n,0n],[0n,0n],[0n,0n]],[[0n,0n],[1n,0n],[1n,0n]],
    [[0n,0n],[1n,0n],[0n,0n]],[[-1n,0n],[0n,0n],[1n,0n]],
    [[0n,0n],[0n,0n],[1n,0n]],[[1n,0n],[0n,1n],[0n,0n]],
  ];
  const positive=exactCertificate(triangle,3,2);
  assert.equal(positive.p,88n);assert.equal(positive.q,14n);
  assert.deepEqual(exactPermanent(positive.a),directPermanent(positive.a));
  writeFileSync('marcus-collision-free-example.json',JSON.stringify(positive,(_,x)=>typeof x==='bigint'?x.toString():x,2)+'\n');
  let seed=19219;function random(){seed=Math.imul(seed,1664525)+1013904223|0;return(seed>>>0)/4294967296;}
  let witness;
  for(let trial=0;trial<10000;trial++) {
    const v=Array.from({length:6},()=>Array.from({length:3},()=>[BigInt(Math.floor(3*random())-1),0n]));
    if(v.some(row=>row.every(z=>z[0]===0n)))continue;
    const e=exactCertificate(v,3,2);
    if(e.D2<0n){witness={trial,...e};break;}
  }
  assert(witness,'Search did not find an obstruction to termwise positivity.');
  assert.deepEqual(exactPermanent(witness.a),directPermanent(witness.a));
  const file='marcus-negative-connected-term.json';
  writeFileSync(file,JSON.stringify(witness,(_,x)=>typeof x==='bigint'?x.toString():x,2)+'\n');
  console.log(JSON.stringify({file,trial:witness.trial,p:String(witness.p),q:String(witness.q),D1:String(witness.D1),D2:String(witness.D2),difference:String(witness.difference)}));
  console.log('Exact DP and independent permutation enumeration agree. This is not a counterexample to Marcus.');
}
