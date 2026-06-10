from funcs import is_prime

# Admissible numbers below 10^9 are products of the first k primes
# (2 through at most 23, since the primorial of 29 exceeds 10^9) with all
# exponents at least one - 6656 of them, enumerated by DFS over exponents.
# For each, the pseudo-Fortunate number is the smallest M > 1 with N + M
# prime, found by direct Miller-Rabin scanning (the example
# pf(630) = 11 is asserted); distinct values are summed.

_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23]


def _admissible(limit: int) -> list[int]:
    out: list[int] = []
    for k in range(1, len(_PRIMES) + 1):

        def rec(i: int, v: int) -> None:
            if i == k:
                out.append(v)
                return
            v *= _PRIMES[i]
            while v < limit:
                rec(i + 1, v)
                v *= _PRIMES[i]

        rec(0, 1)
    return sorted(set(out))


def _pseudo_fortunate(n: int) -> int:
    m = 2
    while not is_prime(n + m):
        m += 1
    return m


def solve(limit: int = 10**9) -> int:
    assert _pseudo_fortunate(630) == 11
    return sum({_pseudo_fortunate(n) for n in _admissible(limit)})


if __name__ == "__main__":
    print(solve())  # 2209
