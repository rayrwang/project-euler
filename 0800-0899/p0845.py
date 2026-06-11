"""Project Euler 845: Prime Digit Sum.

D(n) is the n-th positive integer whose digit sum is prime; we need
D(10^16).

Counting integers up to x with prime digit sum is a textbook digit
dynamic program: with T[d][s] denoting the number of d-digit strings
(digits 0-9) summing to s, walk the decimal digits of x left to right
and, at each position, for every smaller digit choice add the number
of free completions whose total lands on a prime (digit sums never
exceed 9 * 18 = 162, so only a few dozen primes matter), finally
including x itself when its own digit sum is prime.

The counting function is non-decreasing, so D(n) is the smallest x
with count(x) >= n, found by binary search; that minimal x necessarily
has a prime digit sum itself, since otherwise x - 1 would have the
same count.  The whole computation is a few thousand table lookups and
reproduces the given D(61) = 157 and D(10^8) = 403539364.
"""

from __future__ import annotations

MAX_DIGITS = 20


def primes_upto(n: int) -> list[int]:
    flags = bytearray([1]) * (n + 1)
    flags[0:2] = b"\x00\x00"
    for i in range(2, int(n**0.5) + 1):
        if flags[i]:
            flags[i * i :: i] = b"\x00" * len(flags[i * i :: i])
    return [i for i in range(2, n + 1) if flags[i]]


PRIMES = set(primes_upto(9 * MAX_DIGITS))

TABLE = [[0] * (9 * MAX_DIGITS + 1) for _ in range(MAX_DIGITS + 1)]
TABLE[0][0] = 1
for _d in range(1, MAX_DIGITS + 1):
    for _s in range(9 * _d + 1):
        TABLE[_d][_s] = sum(TABLE[_d - 1][_s - v] for v in range(10) if _s >= v)


def count_prime_digit_sum(x: int) -> int:
    """Number of integers in [1, x] whose digit sum is prime."""
    if x <= 0:
        return 0
    digits = list(map(int, str(x)))
    n = len(digits)
    total = 0
    prefix = 0
    for i, d in enumerate(digits):
        rem = n - i - 1
        for v in range(d):
            s0 = prefix + v
            for q in PRIMES:
                if 0 <= q - s0 <= 9 * rem:
                    total += TABLE[rem][q - s0]
        prefix += d
    if prefix in PRIMES:
        total += 1
    return total


def nth_prime_digit_sum(n: int) -> int:
    lo, hi = 1, 10**18
    while lo < hi:
        mid = (lo + hi) // 2
        if count_prime_digit_sum(mid) >= n:
            hi = mid
        else:
            lo = mid + 1
    return lo


def main() -> None:
    assert nth_prime_digit_sum(61) == 157
    assert nth_prime_digit_sum(10**8) == 403539364
    print(nth_prime_digit_sum(10**16))  # 45009328011709400


if __name__ == "__main__":
    main()
