"""
https://projecteuler.net/problem=581

Find the sum of all n such that T(n) = n(n+1)/2 is 47-smooth.

Since n and n+1 are coprime, T(n) is 47-smooth iff both n and n+1 are
47-smooth (the division by 2 cannot introduce or remove prime factors
above 47). Stormer's theorem guarantees that for any finite set of
primes there are only finitely many pairs of consecutive integers that
are both smooth over that set, so the answer is a finite sum.

Search: every pair (n, n+1) contains exactly one odd number, and odd
47-smooth numbers are much sparser than all 47-smooth numbers. So we
enumerate every odd 47-smooth v up to the search bound by depth-first
search over exponent vectors of the primes 3, 5, ..., 47, and test
v - 1 and v + 1 for 47-smoothness by trial division; each qualifying
pair is found exactly once via its odd member.

With the bound 9 * 10^18 (near the int64 limit) the largest pair found
starts at n = 1109496723125 ~ 1.1 * 10^12, i.e. the search continues
more than 8 * 10^6 times past the last solution without finding
another one. This agrees with Lehmer's computation of all consecutive
47-smooth pairs via Stormer's method (OEIS A117581 lists
1109496723126 = n + 1 as the largest p-smooth triangular-pair member
for p = 47).
"""

import numba
import numpy as np

BOUND = 9 * 10**18

ODD_PRIMES = np.array(
    [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47], dtype=np.int64
)


@numba.njit(cache=True)
def _is_smooth(m: int) -> bool:
    while m % 2 == 0:
        m //= 2
    for j in range(14):
        p = ODD_PRIMES[j]
        while m % p == 0:
            m //= p
        if m == 1:
            return True
    return m == 1


@numba.njit(cache=True)
def sum_pairs(bound: int) -> tuple[int, int, int]:
    """Sum of n, number of pairs, and largest n over all pairs of
    consecutive 47-smooth integers (n, n+1) with odd member <= bound."""
    stack_v = np.empty(4096, dtype=np.int64)
    stack_i = np.empty(4096, dtype=np.int64)
    top = 0
    stack_v[0] = 1
    stack_i[0] = 0
    total = 0
    npairs = 0
    largest = 0
    while top >= 0:
        v = stack_v[top]
        i = stack_i[top]
        top -= 1
        if _is_smooth(v + 1):  # pair (v, v + 1)
            total += v
            npairs += 1
            largest = max(largest, v)
        if v > 2 and _is_smooth(v - 1):  # pair (v - 1, v)
            total += v - 1
            npairs += 1
            largest = max(largest, v - 1)
        for j in range(i, 14):
            p = ODD_PRIMES[j]
            if v <= bound // p:
                top += 1
                stack_v[top] = v * p
                stack_i[top] = j
    return total, npairs, largest


@numba.njit(cache=True)
def brute_force(n_max: int) -> tuple[int, int]:
    """Sum and count of n <= n_max with n and n+1 both 47-smooth, by
    direct trial division of every integer."""
    total = 0
    cnt = 0
    prev_smooth = True  # n = 1 is smooth
    for n in range(1, n_max + 1):
        cur_smooth = _is_smooth(n + 1)
        if prev_smooth and cur_smooth:
            total += n
            cnt += 1
        prev_smooth = cur_smooth
    return total, cnt


if __name__ == "__main__":
    # cross-check the pair enumeration against direct trial division;
    # with an odd bound B, "odd member <= B" and "n <= B" coincide
    assert sum_pairs(10**7 + 1)[:2] == brute_force(10**7 + 1)

    total, npairs, largest = sum_pairs(BOUND)
    # the search bound exceeds the largest pair found by a huge margin
    assert largest < BOUND // 10**6

    print(total)  # 2227616372734
