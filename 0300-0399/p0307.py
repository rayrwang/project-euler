from decimal import Decimal, getcontext

getcontext().prec = 60


def prob_at_least_three(k: int, n: int) -> Decimal:
    """Probability that some chip carries >= 3 of k defects spread over n chips.

    Work with the complement: every chip has 0, 1 or 2 defects. If exactly j
    chips hold two defects (using 2j of the k labelled defects) and the other
    k - 2j defects sit alone, the number of placements is
        C(n, j) * C(n - j, k - 2j) * k! / 2^j,
    and dividing by n^k turns it into a probability t_j. The ratio of
    consecutive terms collapses to
        t_j / t_(j-1) = (k - 2j + 2)(k - 2j + 1) / (2 j (n + j - k)),
    starting from t_0 = prod_(i=0)^(k-1) (n - i) / n (all defects distinct).
    """
    N = Decimal(n)
    t0 = Decimal(1)
    for i in range(k):
        t0 *= Decimal(n - i) / N
    cur = t0
    total = t0
    for j in range(1, k // 2 + 1):
        cur *= Decimal((k - 2 * j + 2) * (k - 2 * j + 1)) / (
            Decimal(2 * j) * Decimal(n + j - k)
        )
        total += cur
    return Decimal(1) - total


def solve(k: int, n: int) -> Decimal:
    return prob_at_least_three(k, n).quantize(Decimal("1.0000000000"))


if __name__ == "__main__":
    assert solve(3, 7) == Decimal("0.0204081633")
    print(solve(20_000, 1_000_000))  # 0.7311720251
