from collections import defaultdict


def _base5(n: int) -> list[int]:
    digits = []
    while n:
        digits.append(n % 5)
        n //= 5
    return digits or [0]


def _count_low_carries(m: int, t: int) -> int:
    """Count j in [1, m] with 5 not dividing j and C(j) <= t, where C(j) is the
    number of carries produced when doubling j in base 5.

    Digit DP over the base-5 digits of m (least significant first). The doubling
    carry flows from low to high, so the recursion fixes the high digits and lets
    the lower part report, for each carry it pushes up, the distribution of the
    carry count so far; the least-significant digit is forced nonzero to enforce
    5 does not divide j.
    """
    if m < 1 or t < 0:
        return 0
    digits = _base5(m)
    length = len(digits)
    cache: dict[tuple[int, bool], dict[int, dict[int, int]]] = {}

    def rec(pos: int, tight: bool) -> dict[int, dict[int, int]]:
        if pos < 0:
            return {0: {0: 1}}
        key = (pos, tight)
        if key in cache:
            return cache[key]
        res: dict[int, dict[int, int]] = defaultdict(lambda: defaultdict(int))
        hi = digits[pos] if tight else 4
        lo = 1 if pos == 0 else 0  # least-significant digit nonzero => 5 does not divide j
        for d in range(lo, hi + 1):
            next_tight = tight and d == hi
            for carry_in, count_map in rec(pos - 1, next_tight).items():
                carry_out = (2 * d + carry_in) // 5
                for carries, cnt in count_map.items():
                    res[carry_out][carries + carry_out] += cnt
        cache[key] = res
        return res

    total = 0
    for count_map in rec(length - 1, True).values():
        for carries, cnt in count_map.items():
            if carries <= t:
                total += cnt
    return total


def solve(n: int = 10**18) -> int:
    """T_5(n): the number of i in [1, n] with f5((2i-1)!) < 2 f5(i!), where f5 is
    the exponent of 5.

    By Legendre f5(m!) = (m - s5(m)) / 4 with s5 the base-5 digit sum, and
    s5(2i-1) = s5(2i) - 1 + 4 v5(i) where v5(i) is the number of trailing base-5
    zeros. Working through the algebra, s5(2i) - 2 s5(i) = -4 C(i) where C(i) is
    the number of carries when doubling i in base 5, so the condition collapses to
        v5(i) > C(i).
    Writing i = 5^v * j with 5 not dividing j, the trailing zeros do not create
    carries, so C(i) = C(j) and we need v > C(j). Hence
        T_5(n) = sum_{v >= 1} #{ j : 5 not dividing j, j <= n / 5^v, C(j) <= v - 1 },
    and each inner count is a base-5 digit DP. The given T_5(10^3) = 68 and
    T_5(10^9) = 2408210 confirm it.
    """
    total = 0
    v = 1
    while 5**v <= n:
        total += _count_low_carries(n // 5**v, v - 1)
        v += 1
    return total


if __name__ == "__main__":
    assert solve(10**3) == 68
    assert solve(10**9) == 2408210
    print(solve(10**18))  # 22173624649806
