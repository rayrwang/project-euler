"""Project Euler 916: Restricted Permutations.

By the RSK correspondence, permutations of {1, ..., 2n} biject with
pairs (P, Q) of standard Young tableaux of a common shape lambda |- 2n,
where the longest increasing subsequence equals the first row length
and the longest decreasing subsequence equals the first column length.
LDS <= 2 restricts to shapes with at most two rows
lambda = (lambda1, lambda2), lambda1 + lambda2 = 2n; combined with
LIS <= n + 1 and lambda1 >= lambda2 this leaves exactly
lambda1 in {n, n + 1}.  Hence

    P(n) = f(n, n)^2 + f(n+1, n-1)^2,

with the two-row ballot formula f(a, b) = (a - b + 1)/(a + 1) C(a+b, b),
so f(n, n) = Catalan(n) and f(n+1, n-1) = 3 C(2n, n-1)/(n + 2).
Checks: n = 2 gives 2^2 + 3^2 = 13; brute-force enumeration of all
permutations with literal LIS/LDS tests agrees for n <= 4; and the
given P(10) = 45265702 mod 10^9 + 7 is reproduced.  Only four
factorials up to (2n)! mod p are needed.
"""

import bisect
from itertools import permutations

import numba

P = 10**9 + 7


def _lis_len(seq) -> int:
    tails: list[int] = []
    for x in seq:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


def brute(n: int) -> int:
    cnt = 0
    for perm in permutations(range(1, 2 * n + 1)):
        if _lis_len(perm) <= n + 1 and _lis_len([-x for x in perm]) <= 2:
            cnt += 1
    return cnt % P


@numba.njit(cache=True)
def _facts_at(n):
    """(2n)!, n!, (n+1)!, (n-1)!  mod P."""
    f = 1
    f_nm1 = f_n = f_np1 = 1
    for i in range(1, 2 * n + 1):
        f = f * i % P
        if i == n - 1:
            f_nm1 = f
        elif i == n:
            f_n = f
        elif i == n + 1:
            f_np1 = f
    return f, f_n, f_np1, f_nm1


def solve(n: int) -> int:
    f2n, fn, fnp1, fnm1 = (int(x) for x in _facts_at(n))

    def inv(x: int) -> int:
        return pow(x, P - 2, P)

    catalan = f2n * inv(fn) % P * inv(fnp1) % P
    f_two = 3 * f2n % P * inv(fnm1) % P * inv(fnp1) % P * inv(n + 2) % P
    return (catalan * catalan + f_two * f_two) % P


if __name__ == "__main__":
    for n in (1, 2, 3, 4):
        assert solve(n) == brute(n), n
    assert solve(2) == 13
    assert solve(10) == 45265702
    print(solve(10**8))  # 877789135
