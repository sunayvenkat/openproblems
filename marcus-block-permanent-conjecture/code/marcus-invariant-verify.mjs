// Standalone exact verifier: Node built-ins only; no optimization libraries.
// Usage: node marcus-invariant-verify.mjs marcus-invariant-exact-4-6.json
import {readFileSync} from 'node:fs';
import assert from 'node:assert/strict';

const data=JSON.parse(readFileSync(process.argv[2],'utf8'));
const m=data.m,k=data.degree??2,r=data.dimension,B=m*k-2;
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;}
function rat(a,b=1n){if(typeof a==='string'){const s=a.split('/');return rat(BigInt(s[0]),BigInt(s[1]??1));}if(!a)return [0n,1n];if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return [a/g,b/g];}
const zero=[0n,1n];
function add(x,y){if(!x[0])return y;if(!y[0])return x;const g=gcd(x[1],y[1]);return rat(x[0]*(y[1]/g)+y[0]*(x[1]/g),x[1]*(y[1]/g));}
function neg(x){return [-x[0],x[1]];}
function mul(x,y){if(!x[0]||!y[0])return zero;const a=gcd(x[0],y[1]),b=gcd(y[0],x[1]);return [(x[0]/a)*(y[0]/b),(x[1]/b)*(y[1]/a)];}
function div(x,y){assert(y[0]);return mul(x,rat(y[1],y[0]));}
function equal(x,y){return x[0]===y[0]&&x[1]===y[1];}
function permutations(a){if(!a.length)return [[]];return a.flatMap((x,i)=>permutations(a.filter((_,j)=>j!==i)).map(t=>[x,...t]));}
const perms=permutations(Array.from({length:m},(_,i)=>i));
function canonical(table){let best=null;for(const p of perms)for(let trans=0;trans<2;trans++){const v=[];for(let i=0;i<m;i++)for(let j=0;j<m;j++)v.push(table[(trans?p[j]:p[i])*m+(trans?p[i]:p[j])]);const key=v.join(',');if(best===null||key<best)best=key;}return best;}

// Enumerate individual Wick pairings independently of the factorial formula.
const wick=new Map(),table=new Array(m*m).fill(0);
function pairings(row,used){if(row===m*k){const key=table.join(',');wick.set(key,(wick.get(key)??0)+1);return;}
  for(let col=0;col<m*k;col++)if(!(used&(1<<col))){const at=Math.floor(row/k)*m+Math.floor(col/k);table[at]++;pairings(row+1,used|(1<<col));table[at]--;}}
assert(m*k<=20);pairings(0,0);
const orbitLookup=new Map(),targets=[],orbitKeys=[];
for(const [key,count] of wick){const t=key.split(',').map(Number),rep=canonical(t);let o=orbitKeys.indexOf(rep);if(o<0){o=targets.length;targets.push(0);orbitKeys.push(rep);}orbitLookup.set(key,o);if(t.some(x=>x!==0&&x!==k))targets[o]+=count;}
const reconstructed=targets.map(()=>zero);

function validate(net,cut){const L=k*cut-1,occ=new Map();assert.equal(net[0].length,m);
  for(let block=0;block<m;block++){assert.equal(net[0][block].length,k);for(const i of net[0][block]){assert(Number.isInteger(i)&&i>=0);if(!occ.has(i))occ.set(i,[]);occ.get(i).push(block<cut);}}
  for(const [i,j]of net[1]){assert(i>=0&&i<L&&j>=L&&j<B);for(const a of[i,j]){if(!occ.has(a))occ.set(a,[]);occ.get(a).push(null);}}
  for(let i=0;i<B;i++)assert.equal(occ.get(i)?.length,1);
  let internal=0;for(const [i,types]of occ)if(i>=B){assert.equal(types.length,2);assert.notEqual(types[0],types[1]);internal++;}
  assert(internal>=1);assert.equal(net[1].length,internal-1);
}
function diagram(a,b,cut){const shift=m*k,parents=Array.from({length:B+2*shift},(_,i)=>i),used=new Set();
  function root(i){while(parents[i]!==i){parents[i]=parents[parents[i]];i=parents[i];}return i;}
  function idx(i,side){return i<B?i:i+side*shift;}
  for(let side=0;side<2;side++){const net=side?b:a;for(const [i,j]of net[1]){const x=idx(i,side),y=idx(j,side);parents[root(x)]=root(y);used.add(x);used.add(y);}for(const legs of net[0])for(const i of legs)used.add(idx(i,side));}
  const comps=new Map();for(const i of used)comps.set(root(i),[]);
  for(let side=0;side<2;side++){const net=side?b:a;for(let block=0;block<m;block++)for(const i of net[0][block])comps.get(root(idx(i,side))).push([(block<cut)===(side===1),block]);}
  const t=new Array(m*m).fill(0);let loops=0;
  for(const legs of comps.values()){if(!legs.length){loops++;continue;}assert.equal(legs.length,2);assert.notEqual(legs[0][0],legs[1][0]);const hol=legs.find(x=>x[0])[1],anti=legs.find(x=>!x[0])[1];t[hol*m+anti]++;}
  const orbit=orbitLookup.get(t.join(','));assert(orbit!==undefined);return [orbit,r**loops];
}
function positiveDefinite(matrix){const n=matrix.length,L=Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>rat(BigInt(i===j)))),D=[];
  for(let j=0;j<n;j++){let pivot=matrix[j][j];for(let s=0;s<j;s++)pivot=add(pivot,neg(mul(mul(L[j][s],L[j][s]),D[s])));assert(pivot[0]>0n,`Nonpositive LDL pivot ${j}`);D.push(pivot);
    for(let i=j+1;i<n;i++){let x=matrix[i][j];for(let s=0;s<j;s++)x=add(x,neg(mul(mul(L[i][s],L[j][s]),D[s])));L[i][j]=div(x,pivot);}}
}

const allDiagrams=new Map();
for(const cut of data.cuts){const nets=data.networks[cut];nets.forEach(net=>validate(net,cut));const pairs=[];for(let i=0;i<nets.length;i++)for(let j=i;j<nets.length;j++)pairs.push([i,j,...diagram(nets[i],nets[j],cut)]);allDiagrams.set(cut,pairs);}
for(const block of data.blocks){const cut=Number(/^cut(\d+)\//.exec(block.name)[1]),nets=data.networks[cut],C=block.basis,d=block.gram.length;
  assert.equal(C.length,nets.length);assert(C.every(row=>row.length===d&&row.every(Number.isSafeInteger)));
  const maximum=Math.max(...C.flat().map(Math.abs));assert(Number.isSafeInteger(maximum**2*r**m*nets.length**2));
  const gram=block.gram.map(row=>row.map(x=>rat(x)));for(let i=0;i<d;i++)for(let j=0;j<d;j++)assert(equal(gram[i][j],gram[j][i]));positiveDefinite(gram);
  const sparse=C.map(row=>row.map((x,i)=>[i,x]).filter(x=>x[1]));const coefs=targets.map(()=>new Float64Array(d*d));
  for(const[i,j,o,value]of allDiagrams.get(cut))for(const[p,x]of sparse[i])for(const[q,y]of sparse[j]){coefs[o][p*d+q]+=value*x*y;if(i!==j)coefs[o][q*d+p]+=value*x*y;}
  for(let o=0;o<targets.length;o++)for(let p=0;p<d;p++)for(let q=0;q<d;q++){const c=coefs[o][p*d+q];assert(Number.isSafeInteger(c));if(c)reconstructed[o]=add(reconstructed[o],mul(rat(BigInt(c)),gram[p][q]));}
  console.log(JSON.stringify({positive_definite:block.name,order:d}));
}
targets.forEach((t,o)=>assert(equal(reconstructed[o],rat(BigInt(t))),`Coefficient mismatch at ${orbitKeys[o]}`));

// Equality check: the boundary-permutation orbit of the cut-one basis spans
// every raw covariant. Full rank over a prime field certifies full rank over Q.
function certifySpanning(cut){const nets=data.networks[cut],n=nets.length,L=k*cut-1,prime=1000003;
  const lookup=new Map(nets.map((net,i)=>[JSON.stringify(net),i])),actions=[];
  for(let a=0;a<B-1;a++){if(a===L-1)continue;const change=x=>x===a?a+1:x===a+1?a:x;actions.push(nets.map(([legs,deltas])=>{const moved=[legs.map(row=>row.map(change).sort((x,y)=>x-y)),deltas.map(pair=>pair.map(change)).sort((x,y)=>x[0]-y[0]||x[1]-y[1])];const idx=lookup.get(JSON.stringify(moved));assert(idx!==undefined);return idx;}));}
  const basis=new Map(),queue=[];
  function power(a,b){let v=1;while(b){if(b%2)v=v*a%prime;a=a*a%prime;b=Math.floor(b/2);}return v;}
  function insert(input){const v=Array.from(input,x=>(x%prime+prime)%prime);for(let p=0;p<n;p++){if(!v[p])continue;if(basis.has(p)){const row=basis.get(p),factor=v[p];for(let j=p;j<n;j++)v[j]=(v[j]-factor*row[j]%prime+prime)%prime;}else{const inverse=power(v[p],prime-2);for(let j=p;j<n;j++)v[j]=v[j]*inverse%prime;basis.set(p,v);queue.push(v);return;}}}
  for(const block of data.blocks)if(block.name.startsWith(`cut${cut}/`))for(let j=0;j<block.gram.length;j++)insert(block.basis.map(row=>row[j]));
  for(let at=0;at<queue.length&&basis.size<n;at++)for(const action of actions){const moved=new Array(n);queue[at].forEach((x,i)=>moved[action[i]]=x);insert(moved);}
  assert.equal(basis.size,n);return n;
}
const spanning=certifySpanning(1);
console.log(JSON.stringify({exact_verified:true,m,k,dimension:r,wick_tables:wick.size,coefficient_orbits:targets.length,positive_definite_blocks:data.blocks.length,equality_spanning_rank:spanning,dependencies:'Node built-ins only'}));
