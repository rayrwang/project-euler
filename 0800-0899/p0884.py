_memo: dict[int, int] = {}
_t: list[int] = [0]  # _t[K] = sum of s(3k^2 + 3k + 1) for k = 1..K


def _icbrt(n: int) -> int:
    x = round(n ** (1 / 3))
    while x**3 > n:
        x -= 1
    while (x + 1) ** 3 <= n:
        x += 1
    return x


def s(n: int) -> int:
    """Sum of D(m) for 0 < m < n, where D greedily strips largest cubes.

    For m in the block [k^3, (k+1)^3) we have D(m) = 1 + D(m - k^3).  The
    blocks below n therefore contribute n - 1 (one first step per m) plus
    S of each block's length.  Every full block has length 3k^2 + 3k + 1,
    shared by all callers, so their S values are accumulated once into
    the prefix sums _t; only the topmost, partial block recurses on a
    bespoke value, and that chain shrinks like n -> O(n^(2/3)).
    """
    if n <= 1:
        return 0
    if n in _memo:
        return _memo[n]
    k = _icbrt(n - 1)
    while len(_t) <= k - 1:
        j = len(_t)
        _t.append(_t[-1] + s(3 * j * j + 3 * j + 1))
    res = n - 1 + s(n - k**3) + _t[k - 1]
    _memo[n] = res
    return res


def _d(n: int) -> int:
    steps = 0
    while n:
        n -= _icbrt(n) ** 3
        steps += 1
    return steps


if __name__ == "__main__":
    assert _d(100) == 4
    assert s(100) == 512
    assert all(s(n) == sum(_d(m) for m in range(1, n)) for n in range(1, 300))
    print(s(10**17))  # 1105985795684653500
