// Exact integer searches over partitions of real reflection roots.
import assert from 'node:assert/strict';
import {writeFileSync} from 'node:fs';
import {exactCertificate} from './marcus-block-exact.mjs';

function factorial(n){let x=1;for(let j=2;j<=n;j++)x*=j;return x;}
function permanent(a){
  const n=a.length,f=new Float64Array(1<<n);f[0]=1;
  for(let mask=1;mask<f.length;mask++){
    let row=-1;for(let x=mask;x;x&=x-1)row++;
    for(let j=0;j<n;j++)if(mask&(1<<j)){
      const term=a[row][j]*f[mask^(1<<j)];
      assert.ok(Number.isSafeInteger(term),'integer product range exceeded');
      f[mask]+=term;
      assert.ok(Number.isSafeInteger(f[mask]),'integer sum range exceeded');
    }
  }
  return f.at(-1);
}
function roots(type,r){
  const vectors=[];
  if(type==='B')for(let i=0;i<r;i++){const v=Array(r).fill(0);v[i]=1;vectors.push(v);}
  for(let i=0;i<r;i++)for(let j=i+1;j<r;j++)for(const sign of type==='A'?[-1]:[-1,1]){
    const v=Array(r).fill(0);v[i]=1;v[j]=sign;vectors.push(v);
  }
  const degrees=Array.from({length:r},(_,j)=>type==='A'?j:type==='D'?2*j:2*j+1);
  const p=factorial(r)*degrees.reduce((s,j)=>s*factorial(j),1);
  assert.ok(Number.isSafeInteger(p));
  return{vectors,p,degrees};
}
function run(type,r,k,exhaustive,samples=0){
  const started=Date.now(),{vectors,p,degrees}=roots(type,r),n=vectors.length,m=n/k;
  assert.ok(Number.isInteger(m)&&n<=21);
  const a=vectors.map(v=>vectors.map(w=>v.reduce((s,x,i)=>s+x*w[i],0)));
  const blockLists=new Map(),cache=new Map(),base=2**n;
  function list(mask){
    if(!blockLists.has(mask)){const ids=[];for(let i=0;i<n;i++)if(mask&(1<<i))ids.push(i);blockLists.set(mask,ids);}
    return blockLists.get(mask);
  }
  function entry(left,right){
    if(left>right)[left,right]=[right,left];
    const key=left*base+right;
    if(!cache.has(key))cache.set(key,permanent(list(left).map(i=>list(right).map(j=>a[i][j]))));
    return cache.get(key);
  }
  let count=0,maxQ=-Infinity,best=null;
  function evaluate(blocks){
    const g=blocks.map(left=>blocks.map(right=>entry(left,right))),q=permanent(g);count++;
    if(q>maxQ){maxQ=q;best={blocks:blocks.map(x=>list(x)),g};}
  }
  function enumerate(remaining,blocks){
    if(!remaining){evaluate(blocks);return;}
    const first=remaining&-remaining,ids=[];
    for(let j=0;j<n;j++)if((remaining^first)&(1<<j))ids.push(j);
    function choose(start,left,mask){
      if(!left){enumerate(remaining^mask,[...blocks,mask]);return;}
      for(let i=start;i<=ids.length-left;i++)choose(i+1,left-1,mask|(1<<ids[i]));
    }
    choose(0,k-1,first);
  }
  if(exhaustive)enumerate((1<<n)-1,[]);
  else{
    let state=117361;function random(){state=Math.imul(state,1664525)+1013904223|0;return(state>>>0)/4294967296;}
    for(let trial=0;trial<samples;trial++){
      const order=Array.from({length:n},(_,i)=>i);
      for(let j=n-1;j>0;j--){const h=Math.floor(random()*(j+1));[order[j],order[h]]=[order[h],order[j]];}
      evaluate(Array.from({length:m},(_,i)=>order.slice(i*k,(i+1)*k).reduce((mask,j)=>mask|(1<<j),0)));
    }
  }
  if(exhaustive){
    let expected=1n;for(let j=2;j<=n;j++)expected*=BigInt(j);
    let divisor=1n;for(let j=2;j<=k;j++)divisor*=BigInt(j);
    expected/=divisor**BigInt(m);for(let j=2;j<=m;j++)expected/=BigInt(j);
    assert.equal(BigInt(count),expected);
  }
  // A second implementation verifies the maximizing partition using original Gram vectors.
  if(n<=16){
    const v=best.blocks.flatMap(block=>block.map(i=>vectors[i].map(x=>[BigInt(x),0n])));
    const exact=exactCertificate(v,m,k);
    assert.equal(exact.p,BigInt(p));assert.equal(exact.q,BigInt(maxQ));
  }
  const result={scope:exhaustive?'All equal-size partitions of this fixed root set only.':'Finite random partitions only.',type,r,k,m,exhaustive,samples,seed:exhaustive?null:117361,count,p,maxQ,minRatio:p/maxQ,degrees,vectors,best,seconds:(Date.now()-started)/1000};
  const file=`marcus-reflection-${type}-${r}-${k}.json`;
  writeFileSync(file,JSON.stringify(result,null,2)+'\n');
  console.log(JSON.stringify({file,count,p,maxQ,minRatio:p/maxQ,seconds:result.seconds}));
}
assert.equal(permanent([[1,2],[3,4]]),10);
assert.equal(permanent([[1,0,0],[0,1,0],[0,0,1]]),1);
const [type,r,k,mode,samples]=process.argv.slice(2);
assert.ok(['A','B','D'].includes(type));assert.ok(['all','random'].includes(mode));
run(type,Number(r),Number(k),mode==='all',Number(samples??0));
