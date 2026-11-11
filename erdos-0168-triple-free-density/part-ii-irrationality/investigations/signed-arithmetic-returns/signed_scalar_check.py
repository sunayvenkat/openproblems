"""Exact local-response certificates for complete paired scalar jumps."""
from fractions import Fraction as F
from pathlib import Path
import importlib.util


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def neg(z):
    return -z[0], -z[1]


def rot(z, k):
    for _ in range(k % 3):
        z = -z[1], z[0] - z[1]
    return z


def conj(z):
    return z[0] - z[1], -z[1]


def div_one_minus_omega2(z):
    # 1-omega^2=2+omega, whose norm is three.
    a, b = z[0] + z[1], 2 * z[1] - z[0]
    assert a % 3 == b % 3 == 0
    return a // 3, b // 3


def floor_alpha(n):
    power, result = 1, 0
    while 3 * power <= 2 ** n:
        power *= 3
        result += 1
    return result


def floor_beta(n):
    return (3 ** n).bit_length() - 1


def rootsum(k):
    return ((0, 0), (1, 0), (1, 1))[k % 3]


def limiting_response(pr, qr, transform, width):
    """Low quotient rectangle; valid at any matching CF state p,q>width."""
    s = lambda m: ((1, 0), (0, -1), (0, 0))[m % 3]
    t = lambda m: ((1, 0), (1, 1), (0, 0))[m % 3]
    b_axis = [(1, 0)]
    for n in range(1, width):
        b_axis.append(add(b_axis[-1], rot(t(floor_beta(n)), -2 * n)))
    endpoint_word = add(add(transform, (-1, 0)), rot((1, 0), pr + qr))
    first = rot(rootsum(qr), -qr)
    numerator = add(first, neg(rot(conj(endpoint_word), 2)))
    aq_plus = add((1, 0), div_one_minus_omega2(numerator))
    gamma = rot((1, 0), 2 * pr - qr)
    aq_minus = add(aq_plus, neg(gamma))
    plus, minus = [aq_plus], [aq_minus]
    for r in range(1, width):
        increment = rot(s(pr + floor_alpha(r)), -qr - r)
        plus.append(add(plus[-1], increment))
        minus.append(add(minus[-1], increment))
    correction = (((0, 0), (0, 0), (0, 0)),
                  ((0, 0), (1, 0), (1, 1)),
                  ((0, 0), (0, -1), (1, 0)))

    def eta(axis, r, b):
        x, y = add(add(axis[r], b_axis[b]), correction[(qr + r) % 3][b % 3])
        x -= 1
        if b < 4:
            return (0 if b == 0 else int(x >= 1 and y >= 0) if b == 1
                    else int(x <= -1 and x - y <= 0) if b == 2
                    else int(min(x, 0) <= y))
        isolated = floor_beta(b) - floor_beta(b - 1) == 2
        patch = floor_beta(b - 1) - floor_beta(b - 3) == 4
        assert not (isolated and patch)
        event = (rot((1, 0), floor_beta(b) - 2 * b) if isolated else
                 rot((1, 0), floor_beta(b - 1) - 1 - 2 * b) if patch else (0, 0))
        x, y = x - event[0], y - event[1]
        return int(x <= 0 and x - y <= 0)

    value = sum((F(-3 * (eta(plus, r, b) - eta(minus, r, b)), 2 ** r * 3 ** b)
                 for r in range(width) for b in range(width)), F(0))
    # For p>=width, |quotient coefficient(a,b)|<=3(1+b/p).
    tail = F(27, 2 * 2 ** width) + F(45, 2 * 3 ** width)
    return aq_plus, value, tail


def farey_variation(p, q, r, s):
    """Total variation on the OPEN Farey interval, using floor break counts."""
    assert abs(p*s-r*q) == 1 and min(p,q,r,s) > 0
    a, b = q+s, p+r
    horizontal_width = F(1,q*s)
    vertical_width = F(1,p*r)
    return 9 * (F(2,2**a)*(1+horizontal_width*(a+1))
                +F(1,3**b)*(F(3,2)+vertical_width*(F(3*b,2)+F(3,4))))


def actual_enclosure(a_count=160, b_count=110):
    """A separate exact rectangle enclosure of the true coefficient series."""
    s = lambda m: ((1,0),(0,-1),(0,0))[m%3]
    t = lambda m: ((1,0),(1,1),(0,0))[m%3]
    aa,bb=[(1,0)],[(1,0)]
    for a in range(1,a_count):
        aa.append(add(aa[-1],rot(s(floor_alpha(a)),-a)))
    for b in range(1,b_count):
        bb.append(add(bb[-1],rot(t(floor_beta(b)),-2*b)))
    correction=(((0,0),(0,0),(0,0)),((0,0),(1,0),(1,1)),((0,0),(0,-1),(1,0)))
    total=0
    for b in range(b_count):
        isolated=b>=4 and floor_beta(b)-floor_beta(b-1)==2
        patch=b>=4 and floor_beta(b-1)-floor_beta(b-3)==4
        assert not(isolated and patch)
        event=rot((1,0),floor_beta(b)-2*b) if isolated else rot((1,0),floor_beta(b-1)-1-2*b) if patch else (0,0)
        row=0
        for a in range(a_count):
            x,y=add(add(aa[a],bb[b]),correction[a%3][b%3]);x-=1
            eta=(0 if b==0 else 1 if b==1 and a==0 else int(x>=1 and y>=0) if b==1
                 else int(x<=-1 and x-y<=0) if b==2 else int(min(x,0)<=y) if b==3
                 else int(x-event[0]<=0 and x-event[0]-(y-event[1])<=0))
            row=2*row+1-3*eta
        total=3*total+row
    partial=F(total,2**(a_count-1)*3**(b_count-1))
    exterior=F(1,2**a_count)+F(1,3**b_count)-F(1,2**a_count*3**b_count)
    return partial-6*exterior,partial+3*exterior


if __name__ == '__main__':
    path = Path(__file__).resolve().parents[1] / 'Erdos 168 reflected return models/two_sided_models_check.py'
    spec = importlib.util.spec_from_file_location('scalar_models', path)
    model = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(model)
    assert div_one_minus_omega2((2, 1)) == (1, 0)
    assert div_one_minus_omega2((1, -1)) == (0, -1)
    states = [(0, 1, (1, 0)), (1, 1, (1, 0)), (2, 0, (2, 1)), (2, 2, (2, 0))]
    bounds=[(F(9,20),F(1,2)),(-F(3,50),-F(1,20)),(-F(11,10),-F(1)),(F(7,5),F(3,2))]
    for state,(lo,hi) in zip(states,bounds):
        endpoint, response, tail = limiting_response(*state, 24)
        print('balanced state', state, 'Aq+', endpoint,
              'response numerator/denominator', response.numerator, response.denominator,
              'tail', tail, 'sign', 1 if response > tail else -1 if response < -tail else 0)
        assert abs(response)-tail > F(1,20)
        assert lo < response-tail < response+tail < hi
    # The endpoint and low-response implementation is checked against the full
    # archived model, separately from the new uniform tail argument.
    for p, q, transform in [(5, 8, (2, 0)), (12, 19, (1, 0)), (41, 65, (2, 0)), (53, 84, (2, 1))]:
        plus, minus = model.model(p, q, 1), model.model(p, q, -1)
        width = min(p, q, 12)
        endpoint, local, tail = limiting_response(p % 3, q % 3, transform, width)
        assert endpoint == plus[0][q]
        direct = sum((F(-3 * (plus[3](q+r,b)-minus[3](q+r,b)),2**r*3**b)
                      for r in range(width) for b in range(width)),F(0))
        assert local == direct
        u, v = 2 ** q, 3 ** p
        quotient = (plus[4] - minus[4]) / (F(1,u)-F(1,v))
        assert abs(quotient-local) <= tail
    # A complete Farey-cluster bound, not a numerical first-jump guess.
    p,q,r,s = 12,19,41,65
    medp,medq = p+r,q+s
    _,local,tail = limiting_response(2,0,(2,1),24)
    lower = abs(F(1,2**medq)-F(1,3**medp))*(abs(local)-tail)
    remainder = farey_variation(p,q,medp,medq)+farey_variation(medp,medq,r,s)
    assert lower > remainder
    jump = model.model(medp,medq,1)[4]-model.model(medp,medq,-1)[4]
    difference = model.model(p,q,-1)[4]-model.model(r,s,1)[4]
    assert abs(difference-jump) <= remainder and difference != 0
    assert 2**q < 3**p and 2**s > 3**r
    assert 2**medq < 3**medp  # The actual slope lies past the first mediant.
    actual_low,actual_high=actual_enclosure()
    current=model.model(p,q,-1)[4]
    upper=abs(F(1,2**medq)-F(1,3**medp))*(abs(local)+tail)
    assert actual_low-current > lower-remainder > 0
    assert actual_high-current < upper+remainder
    print('Farey cluster PASS: |leading jump| lower / remainder upper >', lower//remainder)
    print('Correct actual12/19 scalar error is strictly positive by the cluster bound')
    for p,q,r,s in [(53,84,306,485),(306,485,665,1054)]:
        mp,mq=p+r,q+s
        transform=(0,0)
        for n in range(mq):
            transform=add(transform,rot((1,0),n+(mp*n)//mq))
        required={(0,1):(1,0),(1,1):(1,0),(2,0):(2,1),(2,2):(2,0)}
        assert required[(mp%3,mq%3)]==transform
        _,local,tail=limiting_response(mp%3,mq%3,transform,24)
        factor=abs(F(1,2**mq)-F(1,3**mp))
        leading=factor*(abs(local)-tail)
        rest=farey_variation(p,q,mp,mq)+farey_variation(mp,mq,r,s)
        assert leading>rest
        assert abs(p*s-r*q)==1 and (2**q>3**p)!=(2**s>3**r)
        # The current endpoint and its mediant are on the same side of alpha.
        assert (2**q>3**p)==(2**mq>3**mp)
        print('Actual model',p,q,'nonzero cluster certificate, mediant',mp,mq,
              'leading/remainder >',leading//rest)
        if (p,q)==(53,84):
            denominator=27*(2**(3*q)-1)*(3**(3*p)-1)
            exterior=F(1,2**mq)+F(1,3**mp)-F(1,2**mq*3**mp)
            assert 0 < denominator*(leading-rest) < denominator*9*exterior < 1
            cleared_upper=denominator*9*exterior
            k=0
            while cleared_upper*2**(k+1)<1:
                k+=1
            assert cleared_upper < F(1,2**k)
            print('53/84: 0 < absolute scalar cleared error < 2^(-%s)' % k)
    print('PASS: endpoint states, complete paired-jump quotient enclosures')
