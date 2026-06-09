"""Project Euler Problem 700: Eulercoin.

Consider x_n = A*n mod M with A = 1504170715041707, M = 4503599627370517.  An
Eulercoin is a term strictly smaller than all earlier terms.  Find their sum.

The record minima of A*n mod M are the best one-sided rational approximations of
A/M: as we descend the Stern-Brocot tree toward A/M, each mediant denominator b3
gives a candidate index n = b3, and A*b3 mod M produces the successive minima.  We
walk the tree (taking mediants of the bounding fractions), record every new minimum,
and stop at the unavoidable final minimum 1 (gcd(A, M) = 1).
"""

A = 1504170715041707
M = 4503599627370517


def eulercoins() -> list[int]:
    coins = [A]  # n = 1 gives the first Eulercoin
    mn = A
    a1, b1 = 0, 1
    a2, b2 = 1, 1
    while True:
        a3, b3 = a1 + a2, b1 + b2
        if M * a3 < A * b3:          # mediant a3/b3 < A/M
            a1, b1 = a3, b3
        else:
            a2, b2 = a3, b3
        t = (A * b3) % M
        if t < mn:
            coins.append(t)
            mn = t
            if t == 1:
                break
    return coins


def _brute(limit_n: int) -> list[int]:
    out = []
    mn = M + 1
    x = 0
    for _ in range(1, limit_n + 1):
        x += A
        if x >= M:
            x -= M
        if x < mn:
            mn = x
            out.append(x)
    return out


if __name__ == "__main__":
    coins = eulercoins()
    assert coins[0] == 1504170715041707
    assert coins[1] == 8912517754604
    # cross-check the prefix against a direct scan
    b = _brute(10**6)
    assert coins[: len(b)] == b, (coins[: len(b)], b)
    print(sum(coins))  # 1517926517777556
