// Two necessary integral-point problems, not the unrestricted Erdos243 problem.
SetSeed(1);
Q := Rationals();
// Explicitly retain unconditional class-group proof bounds.
minkowski := map< PowerStructure(RngOrd) -> Integers() |
                   order :-> MinkowskiBound(order) >;
SetClassGroupBoundMaps(minkowski, minkowski);
R<z> := PolynomialRing(Q);
for s in [1,-1] do
    assert (2*z^2+4+32*s*z)^2-(2*z+16*s)^2*(z^2+4)
           eq 16*(4*s*z^3+48*z^2-63);
    assert (2*z^2-4-16*s*z)^2-(32*s-2*z)^2*(z^2-4)
           eq 16*(4*s*z^3-48*z^2-24*s*z+257);
end for;
print "Both symbolic norm identities verified";
models := [[Q|0,12,1,0,-16],[Q|0,-12,1,-6,64]];
expected := [ {-8,4}, {-2,2,16,44,52} ];
for i in [1..2] do
    coeffs := models[i];
    E := EllipticCurve(coeffs);
    print E;
    print "discriminant", Factorization(Integers()!Discriminant(E));
    lo, hi := RankBounds(E);
    print "rank bounds", <lo,hi>;
    G, mw, rankProved, groupProved := MordellWeilGroup(E);
    print "MW proof flags", rankProved, groupProved;
    assert rankProved and groupProved;
    print "full Mordell-Weil group", G;
    basis := ReducedBasis([ mw(G.i) : i in [1..Ngens(G)] ]);
    assert #basis eq 1;
    print "full free basis modulo torsion", basis;
    pts := IntegralPoints(E : FBasis := basis, SafetyFactor := 2);
    print "integral points up to sign", pts;
    xs := { Integers()!P[1] : P in pts };
    print "integral x coordinates", xs;
    assert xs eq expected[i];
end for;
