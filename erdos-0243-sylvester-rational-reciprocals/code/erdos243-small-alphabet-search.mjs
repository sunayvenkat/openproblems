// Finite exact exploration of primitive errors {-1,-3}; no infinite claim.
import assert from 'node:assert/strict';
import {writeFileSync} from 'node:fs';
function gcd(a,b){while(b)[a,b]=[b,a%b];return a;}
function orbit(u,v,maxSteps=24){
  assert.ok(u>0n&&v>0n&&gcd(u,v)===1n);
  const rows=[];
  for(let n=0;n<maxSteps;n++){
    if(v.toString(2).length>200000)return{rows,reason:'denominator bit cap'};
    const a=(2n*v+u)/(2n*u)+1n,e=v-(a-1n)*u;
    assert.ok(-u<=2n*e&&2n*e<u);
    if(e!==-1n&&e!==-3n)return{rows,reason:e===0n?'zero error':'left alphabet',next:{u,e}};
    const w=u-e,h=gcd(w,a*v);
    if(rows.length){
      const prev=rows.at(-1);
      if(prev.h===1n&&prev.e!==e){
        const root=prev.e===-1n?prev.a:3n*prev.a;
        assert.equal((root*root-3n)%u,0n);
        assert.equal(gcd(u,3n),1n);
        if(u%2n===0n){assert.equal(u%4n,2n);assert.equal(a%2n,0n);assert.equal(h%2n,1n);}
      }
      if(rows.length>=2){
        const preprev=rows.at(-2);
        if(preprev.h===1n&&preprev.e!==prev.e&&prev.u%2n===0n)assert.equal(h%2n,0n);
      }
    }
    rows.push({u,e,h,a});
    [u,v]=[w/h,a*v/h];
    assert.equal(gcd(u,v),1n);
  }
  return{rows,reason:'step cap'};
}
// Koizumi's modular replay continues past alphabet exit without huge D_n.
function continueRaw(C0,D0,maxSteps=256){
  const numerators=[C0],errors=[],rows=[];
  for(let n=0;n<maxSteps;n++){
    const C=numerators[n];
    if(C.toString(2).length>4096)return{rows,reason:'numerator bit cap'};
    let modulus=numerators.reduce((a,b)=>a*b,1n),x=D0%modulus;
    for(let j=0;j<n;j++){
      assert.equal((x-errors[j])%numerators[j],0n);
      const nextModulus=modulus/numerators[j],a=(x-errors[j])/numerators[j]+1n;
      x=x*a%nextModulus;modulus=nextModulus;
    }
    assert.equal(modulus,C);assert.ok(0n<=x&&x<C);
    const E=x-C*((2n*x+C)/(2n*C)),G=gcd(C,x);
    if(n){assert.equal(G%rows.at(-1).G,0n);rows.at(-1).h=G/rows.at(-1).G;}
    rows.push({C,G,u:C/G,e:E/G});
    if(E===0n)return{rows,reason:'zero error'};
    errors.push(E);numerators.push(C-E);
  }
  return{rows,reason:'step cap'};
}
const modularFixture=continueRaw(11n,29n);
assert.deepEqual(modularFixture.rows.map(r=>r.C),[11n,15n,19n,20n,16n]);
assert.deepEqual(modularFixture.rows.map(r=>r.u),[11n,15n,19n,5n,1n]);
assert.deepEqual(modularFixture.rows.map(r=>r.e),[-4n,-4n,-1n,1n,0n]);
const fixture=orbit(12n,407n);
assert.deepEqual(fixture.rows.map(r=>r.u),[12n,13n,16n]);
assert.deepEqual(fixture.rows.map(r=>r.e),[-1n,-3n,-3n]);
assert.equal(fixture.reason,'left alphabet');
assert.deepEqual(fixture.next,{u:19n,e:7n});
assert.equal(orbit(1n,7n).reason,'zero error');
assert.equal(orbit(11n,29n).rows.length,0);

// Separate original-rational arithmetic checks for small inputs.
for(let q=1n;q<=40n;q++)for(let p=1n;p<=q;p++)if(gcd(p,q)===1n){
 const actual=orbit(p,q,6);let C=p,D=q;const expected=[];
 for(let n=0;n<6;n++){
   const a=(2n*D+C)/(2n*C)+1n,E=D-(a-1n)*C,G=gcd(C,D),e=E/G;
   if(e!==-1n&&e!==-3n)break;
   const nextC=a*C-D,nextD=a*D,nextG=gcd(nextC,nextD);
   expected.push({u:C/G,e,h:nextG/G,a});
   [C,D]=[nextC,nextD];
 }
 assert.deepEqual(actual.rows,expected);
}

const primes=[11,13,23,37,47,61,73],perClass=5000,results=[],histogram={};
let tested=0,maxFullSteps=0,longestFull=null;const endings={},fullEndings={},unresolved=[];
for(const p of primes)for(const multiplier of [1,2]){
 const u=BigInt(multiplier*p-1),roots=[];
 for(let r=3;r<2*p+3;r++)if(r%2===1&&r*r%p===3)roots.push(BigInt(r));
 assert.equal(roots.length,2);
 for(const r of roots){let best=null;
  for(let t=0;t<perClass;t++){
    const a0=r+2n*BigInt(p)*BigInt(t),v=(a0-1n)*u-1n;
    const trace=orbit(u,v),length=trace.rows.length;
    const continuation=continueRaw(u,v);
    assert.ok(length>=2);
    assert.equal(trace.rows[0].e,-1n);assert.equal(trace.rows[1].e,-3n);
    tested++;histogram[length]=(histogram[length]??0)+1;
    endings[trace.reason]=(endings[trace.reason]??0)+1;
    fullEndings[continuation.reason]=(fullEndings[continuation.reason]??0)+1;
    if(continuation.reason!=='zero error')unresolved.push({u,v,reason:continuation.reason});
    if(continuation.rows.length>maxFullSteps){
      maxFullSteps=continuation.rows.length;longestFull={u,v,continuation};
    }
    if(!best||length>best.length)best={p,multiplier,root:r,t,u,v,length,...trace,continuation};
  }
  results.push({...best,rows:best.rows.map(({a,...r})=>({...r,aBits:a.toString(2).length}))});
 }
}
const bestLength=Math.max(...results.map(x=>x.length));
const continuationEndings={};
for(const result of results){
  const direct=orbit(result.u,result.v);
  assert.ok(result.continuation.rows.length>direct.rows.length);
  assert.deepEqual(result.continuation.rows.slice(0,direct.rows.length).map(({u,e,h})=>({u,e,h})),
    direct.rows.map(({u,e,h})=>({u,e,h})));
  const reason=result.continuation.reason;
  continuationEndings[reason]=(continuationEndings[reason]??0)+1;
}
const output={scope:'Finite trajectories only. Seeds enforce an immediate -1 to -3 switch. A zero proves a Sylvester tail for that start; leaving this alphabet does not rule out another asymptotic regime, and a cap proves neither nontermination nor vanishing relative errors.',
 tested,perClass,histogram,endings,bestLength,fullEndings,maxFullSteps,longestFull,unresolved,continuationEndings,results};
writeFileSync('erdos243-small-alphabet-results.json',JSON.stringify(output,(_,v)=>typeof v==='bigint'?String(v):v,2));
console.log(JSON.stringify({tested,histogram,endings,bestLength,fullEndings,maxFullSteps,unresolved,continuationEndings,
 best:results.filter(r=>r.length===bestLength)},(_,v)=>typeof v==='bigint'?String(v):v));
