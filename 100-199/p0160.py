from math import factorial

_M = 3125  # 5^5


def _p_mod(n: int) -> int:
    # n! with all factors of 5 removed, mod 5^5. Multiples of 5 peel off as
    # 5^floor(n/5) * (n//5)!, recursing; the coprime residues over each full
    # period of 5^5 multiply to -1 (Wilson for odd prime powers).
    if n == 0:
        return 1
    res = _M - 1 if (n // _M) % 2 == 1 else 1
    part = 1
    for k in range(1, n % _M + 1):
        if k % 5:
            part = part * k % _M
    return res * part % _M * _p_mod(n // 5) % _M


def _valuation(n: int, p: int) -> int:
    s, pk = 0, p
    while pk <= n:
        s += n // pk
        pk *= p
    return s


def solve(n: int = 10**12) -> int:
    z = _valuation(n, 5)                       # matched 2-5 pairs (trailing zeros)
    excess = _valuation(n, 2) - z
    r5 = _p_mod(n) * pow(pow(2, -1, _M), z, _M) % _M   # (n!/10^z) mod 5^5
    if excess >= 5:
        r2 = 0
    else:                                      # tiny-n fallback only
        f = factorial(n)
        while f % 10 == 0:
            f //= 10
        r2 = f % 32
    # CRT: X = r2 (mod 32), X = r5 (mod 3125)
    t = (r5 - r2) * pow(32, -1, _M) % _M
    return (r2 + 32 * t) % 100000


if __name__ == "__main__":
    print(solve())  # 16576
