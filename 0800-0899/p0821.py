def _loss_thresholds(limit: int) -> list[int]:
    """3-smooth values at which the per-grid loss increments, up to `limit`.

    Two interleaved families (found by solving the per-grid optimum exactly for
    small grids and reading off where the loss steps up):
      A: 2^a * 3 for a in {1, 3, 7, 10, 13, 16, ...} (a = 1, 3 then 7 + 3k),
      B: 2 * 3^3 = 54, then 3^b for b in {5, 8, 11, 14, ...} (b = 5 + 3k).
    """
    thresholds = []
    for a in (1, 3):
        if 2**a * 3 <= limit:
            thresholds.append(2**a * 3)
    a = 7
    while 2**a * 3 <= limit:
        thresholds.append(2**a * 3)
        a += 3
    if 54 <= limit:
        thresholds.append(54)
    b = 5
    while 3**b <= limit:
        thresholds.append(3**b)
        b += 3
    return thresholds


def _coprime6_upto(m: int) -> int:
    """Count of integers in [1, m] coprime to 6."""
    return m - m // 2 - m // 3 + m // 6


def max_separable(n: int) -> int:
    """F(n): max |(S u 2S u 3S) n [1, n]| over 123-separable sets S.

    Every positive integer factors uniquely as m * 2^a * 3^b with gcd(m, 6) = 1,
    and the maps x -> 2x, x -> 3x preserve m, so the problem splits independently
    over each residue class m coprime to 6. Within a class, the reachable
    integers form a staircase grid of cells (a, b) with m * 2^a * 3^b <= n. The
    three disjointness conditions forbid choosing, for S, any two cells differing
    by (1, 0) (from S n 2S), (0, 1) (from S n 3S), or (1, -1) (from 2S n 3S); the
    objective counts cells covered by S or its (+1, 0)/(0, +1) shifts.

    Maximizing coverage leaves a "loss" (uncovered cells) that depends only on
    the grid shape, i.e. on t = n / m through which 3-smooth numbers are <= t.
    The loss is a step function whose jumps occur exactly at the thresholds
    above, so loss(t) = #{theta : theta <= t}. Since each grid has exactly its
    own cells and every integer in [1, n] is one cell, the cells total n and
        F(n) = n - sum_{m coprime 6} loss(n / m)
             = n - sum_{theta} #{m coprime 6 : m <= n / theta},
    swapping the order of summation. Verified against the exact per-grid optimum
    for all n <= 5000 (F(6) = 5, F(20) = 19).
    """
    total_loss = sum(_coprime6_upto(n // theta) for theta in _loss_thresholds(n))
    return n - total_loss


if __name__ == "__main__":
    assert max_separable(6) == 5
    assert max_separable(20) == 19
    assert max_separable(100) == 93
    print(max_separable(10**16))  # 9219661511328178
