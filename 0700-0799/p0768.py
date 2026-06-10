from collections import defaultdict
from itertools import product
from math import comb

TR = 21  # truncation: we need coefficients up to t^20

def polymul(a, b):
    r = [0] * TR
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y and i + j < TR:
                    r[i + j] += x * y
    return r

def polypow(a, e):
    r = [0] * TR
    r[0] = 1
    while e:
        if e & 1:
            r = polymul(r, a)
        a = polymul(a, a)
        e >>= 1
    return r

def solve():
    """f(360, 20): balanced candle arrangements = 20-subsets of Z_360
    whose 360th roots of unity sum to zero.

    Write Z_360 = Z_8 x Z_9 x Z_5 and zeta_360 = zeta_8 zeta_9 zeta_5.
    Since zeta_8^(a+4) = -zeta_8^a, the sum vanishes iff for each
    a in {0..3} the difference function y_a(v, w) = x(a,v,w) -
    x(a+4,v,w) in {-1,0,1} has vanishing zeta_45-sum. Each cell pair
    contributes weight t (y = +-1, one candle) or 1 + t^2 (y = 0, zero
    or two candles), so f(360, m) = [t^m] W(t)^4 with W summing the
    weights over vanishing y on Z_45. In turn a Z_45 sum vanishes iff
    all five Z_9-columns of y have the same image in Z[zeta_9]
    (1 + zeta_5 + ... + zeta_5^4 = 0 is the only Z_5 relation), so
    W = sum over zeta_9-image classes of P_class(t)^5, where P groups
    the 3^9 column functions by their image with weight
    t^(#nonzero) (1+t^2)^(9-#nonzero). The same machinery at n = 36
    (two Z_4-pairs over one Z_9 column, f = [t^m] V^2 with V the
    zero-image class polynomial) reproduces the given f(36, 6) = 876.
    """
    classes = defaultdict(lambda: [0] * TR)
    for y in product((-1, 0, 1), repeat=9):
        # image in Z[zeta_9] on the basis 1..zeta^5 via
        # zeta^6 = -1 - zeta^3, zeta^7 = -zeta - zeta^4, zeta^8 = ...
        img = (y[0] - y[6], y[1] - y[7], y[2] - y[8],
               y[3] - y[6], y[4] - y[7], y[5] - y[8])
        n1 = sum(1 for v in y if v)
        cw = classes[img]
        for j in range(9 - n1 + 1):
            d = n1 + 2 * j
            if d < TR:
                cw[d] += comb(9 - n1, j)

    V = classes[(0,) * 6]
    assert polymul(V, V)[6] == 876  # f(36, 6)

    W = [0] * TR
    for poly in classes.values():
        W = [a + b for a, b in zip(W, polypow(poly, 5))]
    return polypow(W, 4)[20]

if __name__ == "__main__":
    print(solve())  # 14655308696436060
