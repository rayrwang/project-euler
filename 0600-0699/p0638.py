"""Project Euler Problem 638: Weighted Lattice Paths.

Summing k^(area) over monotone lattice paths from (0, 0) to (a, b) is the
classic combinatorial definition of the Gaussian binomial coefficient:

    C(a, b, k) = qbinom(a + b, a) at q = k
               = prod_{i=1}^{a} (1 - q^(b + i)) / (1 - q^i)   for q != 1,

(which side of the path the area is measured on doesn't matter, since
transposing the grid swaps the two conventions without changing the sum).
Each factor uses the next power of q, so a running power and running
product give the whole product in O(a) modular multiplications; one Fermat
inversion finishes the job.  No factor vanishes mod p = 10^9 + 7 because
ord_p(q) divides p - 1 = 2 * 500000003 and is therefore far larger than
2 * 10^7 + 14 for q = 2..7.  The k = 1 term is the plain binomial.

Checks: brute force over all paths for small grids, and the given
C(10000, 10000, 4) = 395913804 mod 10^9 + 7.
"""

from itertools import combinations
from math import comb

MOD = 10**9 + 7


def C(a: int, b: int, k: int) -> int:
    if k % MOD == 1:
        return comb(a + b, a) % MOD
    num, den = 1, 1
    q_pow_b = pow(k, b, MOD)
    q_pow = 1  # q^i
    for _ in range(a):
        q_pow = q_pow * k % MOD
        num = num * (1 - q_pow_b * q_pow) % MOD
        den = den * (1 - q_pow) % MOD
    return num * pow(den, MOD - 2, MOD) % MOD


def C_brute(a: int, b: int, k: int) -> int:
    """Sum k^(area below path) over all monotone paths, by enumeration."""
    total = 0
    for ups in combinations(range(a + b), b):
        area = sum(pos - i for i, pos in enumerate(ups))  # cells below path
        total += k**area
    return total % MOD


if __name__ == "__main__":
    for a, b, k in [(2, 2, 1), (2, 2, 3), (3, 4, 2), (4, 3, 5), (5, 5, 7)]:
        assert C(a, b, k) == C_brute(a, b, k), (a, b, k)
    assert C(10000, 10000, 4) == 395913804
    print(sum(C(10**k + k, 10**k + k, k) for k in range(1, 8)) % MOD)  # 18423394
