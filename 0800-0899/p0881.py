TARGET = 10**4
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]


def _extend(poly: list[int], e: int) -> list[int]:
    """Multiply poly by 1 + x + ... + x^e (sliding-window prefix sums)."""
    out = [0] * (len(poly) + e)
    run = 0
    for i in range(len(out)):
        if i < len(poly):
            run += poly[i]
        if i - e - 1 >= 0:
            run -= poly[i - e - 1]
        out[i] = run
    return out


def g_of_exponents(exps: list[int]) -> int:
    """g(n) for n with these prime exponents.

    The divisor graph links divisors differing by one prime factor, so the
    distance from n to a divisor d is Omega(n / d) and level k collects the
    divisors with Omega = Omega(n) - k.  Their counts are the coefficients
    of prod_i (1 + x + ... + x^(e_i)), and g(n) is the largest one.
    """
    poly = [1]
    for e in exps:
        poly = _extend(poly, e)
    return max(poly)


def smallest_with_width(target: int) -> int:
    """Smallest n whose divisor graph has a level of at least target vertices.

    Only the exponent multiset matters for g, and putting the larger
    exponents on the smaller primes minimises n for a given multiset, so a
    DFS over non-increasing exponent sequences suffices, pruned by the
    best n found so far (g only grows when exponents are raised or primes
    appended, so the first success along a branch is its cheapest).
    """
    k = 1
    while g_of_exponents([1] * k) < target:
        k += 1
    best = 1
    for p in PRIMES[:k]:
        best *= p  # primorial upper bound: k distinct primes suffice

    def dfs(i: int, cap: int, n: int, poly: list[int]) -> None:
        nonlocal best
        p = PRIMES[i]
        val = n
        for e in range(1, cap + 1):
            val *= p
            if val >= best:
                break
            npoly = _extend(poly, e)
            if max(npoly) >= target:
                best = val
                break
            if i + 1 < len(PRIMES):
                dfs(i + 1, e, val, npoly)

    dfs(0, 60, 1, [1])
    return best


def _g_brute(n: int) -> int:
    from collections import Counter

    levels: Counter[int] = Counter()
    for d in range(1, n + 1):
        if n % d == 0:
            m, omega = d, 0
            f = 2
            while f * f <= m:
                while m % f == 0:
                    omega += 1
                    m //= f
                f += 1
            if m > 1:
                omega += 1
            levels[omega] += 1
    return max(levels.values())


if __name__ == "__main__":
    assert _g_brute(45) == 2  # given
    assert _g_brute(5040) == 12  # given
    assert g_of_exponents([4, 2, 1, 1]) == 12  # 5040 via the polynomial
    # cross-check the search against a brute-force scan for small targets
    for t in range(2, 7):
        n = 1
        while _g_brute(n) < t:
            n += 1
        assert smallest_with_width(t) == n, t
    print(smallest_with_width(TARGET))  # 205702861096933200
