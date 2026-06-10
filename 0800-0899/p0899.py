from functools import cache


def l_count(n: int) -> int:
    """Number of ordered losing pairs (a, b) with 1 <= a, b <= n.

    Moves from (a, b) with a <= b remove min = a stones in total without
    emptying a pile, so the successors are exactly the splits
    (a', b - a') of b with 1 <= a' <= a and b - a' >= 1.  Claim: (a, b)
    is losing precisely when a < 2^t, where t = v2(b + 1) (the low t bits
    of b are ones and bit t is zero, t exceeding a's bit length).

    Proof by induction on a + b.  The only terminal position is (1, 1),
    which satisfies the claim.  From a losing (a, b), a successor with
    parts c <= d and c + d = b being losing would need 2^len(c) | d + 1,
    so 2^min(t, len(c)) | (b + 1) - (d + 1) = c; but c <= a < 2^t and
    c < 2^len(c), so c = 0 -- impossible.  Conversely from a winning
    (a, b), i.e. a >= 2^t: split off c = 2^t <= a.  Then
    (b + 1) - c = 2^t (m - 1) with m = (b + 1) / 2^t odd, so
    v2(b - c + 1) >= t + 1 = len(c) and (c, b - c) is losing; c <= b - c
    holds because b < 2^(t + 1) would force b = 2^t - 1 < a, absurd.

    Counting with 2^k <= a < 2^(k + 1): b must be = -1 mod 2^(k + 1), so
    unordered-with-repetition counts multiply block sizes by
    floor((n + 1) / 2^(k + 1)); the diagonal pairs are a = b = 2^m - 1.
    """
    total = 0
    k = 0
    while (1 << k) <= n:
        block = min((1 << (k + 1)) - 1, n) - (1 << k) + 1
        total += block * ((n + 1) >> (k + 1))
        k += 1
    diag = 0
    m = 1
    while (1 << m) - 1 <= n:
        diag += 1
        m += 1
    return 2 * total - diag


@cache
def _win(a: int, b: int) -> bool:
    if a > b:
        a, b = b, a
    return any(
        not _win(min(ap, b - ap), max(ap, b - ap))
        for ap in range(1, a + 1)
        if b - ap >= 1
    )


if __name__ == "__main__":
    losing = [
        (a, b) for a in range(1, 130) for b in range(1, 130) if not _win(a, b)
    ]
    for n in (7, 17, 49, 100, 129):
        assert l_count(n) == sum(1 for a, b in losing if a <= n and b <= n), n
    assert l_count(7) == 21  # given
    assert l_count(7**2) == 221  # given
    print(l_count(7**17))  # 10784223938983273
