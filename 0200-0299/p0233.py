import numpy as np

# The circle through (0,0), (N,0), (0,N), (N,N) has centre (N/2, N/2) and
# radius N/sqrt(2); substituting (u, v) = (2x - N, 2y - N) maps its lattice
# points bijectively onto solutions of u^2 + v^2 = 2 N^2 (the parity
# constraints hold automatically), so the count is r2(2 N^2) =
# 4 prod (2 b_i + 1) over the exponents b_i of the primes = 1 (mod 4) in N.
# 420 points means prod (2 b_i + 1) = 105, so the exponent multiset is one of
# (52), (17, 1), (10, 2), (7, 3), (3, 2, 1); the first two exceed 10^11 even
# with the smallest primes. N factors as a "core" with exactly that signature
# times a multiplier free of primes = 1 (mod 4).


def _primes(limit: int) -> np.ndarray:
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    return np.nonzero(sieve)[0]


def solve(limit: int = 10**11) -> int:
    # Prefix sums of admissible multipliers (no prime factor = 1 mod 4).
    k_max = limit // (5**3 * 13**2 * 17)  # smallest possible core
    allowed = np.ones(k_max + 1, dtype=np.int64)
    allowed[0] = 0
    small = _primes(k_max)
    for p in small[small % 4 == 1]:
        allowed[p::p] = 0
    prefix = np.cumsum(allowed * np.arange(k_max + 1, dtype=np.int64))

    p1 = [
        int(p) for p in (lambda pr: pr[pr % 4 == 1])(_primes(limit // (5**3 * 13**2)))
    ]

    total = 0

    def rec(
        pattern: tuple[int, ...], idx: int, core: int, used: frozenset[int]
    ) -> None:
        nonlocal total
        if idx == len(pattern):
            total += core * int(prefix[limit // core])
            return
        e = pattern[idx]
        for p in p1:
            if p in used:
                continue
            c = core * p**e
            if c > limit:
                break
            rec(pattern, idx + 1, c, used | {p})

    for pattern in ((10, 2), (7, 3), (3, 2, 1)):
        rec(pattern, 0, 1, frozenset())
    return total


if __name__ == "__main__":
    print(solve())  # 271204031455541309
