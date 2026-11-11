// Reproduce in Magma V2.29-10 or later. The default class-group setting
// is unconditional; no GRH bound is requested.
SetSeed(2399912018);
R<t>:=PolynomialRing(Integers());
T:=Thue(t^3-25);
for h in Divisors(15600) do
 S:=Solutions(T,-h);
 print h,S;
 for v in S do
  a:=v[1]; b:=v[2];
  if a gt 0 and b gt 0 and GCD(a,b) eq 1 then
   r:=25*b-a;
   if r gt 0 and r mod h eq 0 then
    ok,g:=IsSquare(r div h);
    if ok and g*b ge 2 and g*a ge g*b+3 then
     print "WITNESS",g*a-2,g*b-2;
    end if;
   end if;
  end if;
 end for;
end for;
