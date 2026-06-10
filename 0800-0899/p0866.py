from itertools import permutations
from math import comb, factorial

MOD = 987654319


def expected_product(n: int) -> int:
    """Expected product of hexagonal numbers h(k) = k(2k-1) over a tidy-up.

    Let f(m) be the sum of the products over all m! pick-up orders of a
    length-m caterpillar.  The last piece placed sits at some position j;
    it always completes the whole segment, contributing h(m), while the
    j - 1 pieces to its left and m - j to its right form independent
    sub-caterpillars whose placements interleave arbitrarily:
        f(m) = h(m) * sum_j C(m-1, j-1) f(j-1) f(m-j),  f(0) = 1.
    The expectation f(n) / n! is an integer (as stated), computed exactly.
    """
    f = [1] * (n + 1)
    for m in range(1, n + 1):
        f[m] = (m * (2 * m - 1)) * sum(
            comb(m - 1, j - 1) * f[j - 1] * f[m - j] for j in range(1, m + 1)
        )
    q, r = divmod(f[n], factorial(n))
    assert r == 0
    return q


def _expected_brute(n: int) -> int:
    total = 0
    for order in permutations(range(n)):
        placed = [False] * n
        prod = 1
        for i in order:
            placed[i] = True
            k = 1
            j = i - 1
            while j >= 0 and placed[j]:
                k += 1
                j -= 1
            j = i + 1
            while j < n and placed[j]:
                k += 1
                j += 1
            prod *= k * (2 * k - 1)
        total += prod
    q, r = divmod(total, factorial(n))
    assert r == 0
    return q


if __name__ == "__main__":
    for n in range(1, 8):
        assert expected_product(n) == _expected_brute(n), n
    assert expected_product(4) == 994  # given
    print(expected_product(100) % MOD)  # 492401720
