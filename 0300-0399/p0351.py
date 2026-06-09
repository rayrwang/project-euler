import sys

import numpy as np

from funcs import totient_sieve


def solve(n: int) -> int:
    """Hidden points in a hexagonal orchard of order n.

    By six-fold symmetry the hidden points are 6 * sum_(i=1)^n (i - phi(i)),
    because in each of the six triangular sectors the lattice points at radial
    index i that are *visible* from the centre are exactly the phi(i) points
    whose coordinates are coprime, leaving i - phi(i) hidden. Hence
        H(n) = 6 ( n(n+1)/2 - Phi(n) ),    Phi(n) = sum_(i=1)^n phi(i).

    Phi is the totient summatory function. Using
        sum_(d=1)^n Phi( floor(n/d) ) = n(n+1)/2
    gives the recurrence Phi(n) = n(n+1)/2 - sum_(d=2)^n Phi(floor(n/d)),
    evaluated sublinearly by grouping equal values of floor(n/d) and sieving
    phi (hence Phi) for all small arguments up to about n^(2/3).
    """
    threshold = max(2_000_000, int(n ** (2 / 3)) + 64)
    if threshold > n:
        threshold = n
    phi = totient_sieve(threshold + 1)
    phi_prefix = np.cumsum(phi.astype(np.int64))  # phi_prefix[x] = Phi(x)

    memo: dict[int, int] = {}
    sys.setrecursionlimit(1 << 16)

    def big_phi(x: int) -> int:
        if x <= threshold:
            return int(phi_prefix[x])
        if x in memo:
            return memo[x]
        result = x * (x + 1) // 2
        d = 2
        while d <= x:
            v = x // d
            d_hi = x // v
            result -= (d_hi - d + 1) * big_phi(v)
            d = d_hi + 1
        memo[x] = result
        return result

    return 6 * (n * (n + 1) // 2 - big_phi(n))


if __name__ == "__main__":
    assert solve(5) == 30
    assert solve(10) == 138
    assert solve(1000) == 1177848
    print(solve(100_000_000))  # 11762187201804552
