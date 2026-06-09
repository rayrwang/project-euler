"""Project Euler Problem 512: Sums of Totients of Powers.

f(n) = (sum_{i=1}^n phi(n^i)) mod (n+1),  g(N) = sum_{n=1}^N f(n).  Find g(5e8).

Since phi(n^i) = n^{i-1} phi(n), the inner sum is phi(n) * (1 + n + ... + n^{n-1}).
Modulo n+1 we have n == -1, so n^{i-1} == (-1)^{i-1} and the geometric sum is
1 if n is odd and 0 if n is even.  As phi(n) <= n-1 < n+1, reduction is trivial:

    f(n) = phi(n)  for odd n,   f(n) = 0  for even n.

Hence g(N) = sum_{n odd, n<=N} phi(n).  Call this A(N).  Using sum_{d|m} phi(d)=m
restricted to odd m (all divisors of an odd number are odd):

    sum_{m odd <= N} m = sum_{k odd <= N} A(floor(N/k)),

and the left side is the sum of the first (N+1)//2 odd numbers = ((N+1)//2)^2.
Isolating k=1 gives the sublinear recurrence

    A(N) = ((N+1)//2)^2 - sum_{k odd, 3<=k<=N} A(floor(N/k)),

evaluated with memoisation over the O(sqrt N) distinct values of floor(N/k) and a
linear-sieve base case for small arguments.
"""

import sys

import numpy as np

from funcs import totient_sieve


def g(N: int) -> int:
    # Base case: prefix sums of phi over odd numbers up to L.
    L = max(1_000_000, int(N ** (2 / 3)) + 1)
    L = min(L, N)
    phi = totient_sieve(L + 1)
    odd_prefix = np.zeros(L + 1, dtype=np.int64)
    run = 0
    for i in range(1, L + 1):
        if i & 1:
            run += int(phi[i])
        odd_prefix[i] = run

    memo: dict[int, int] = {}

    def A(x: int) -> int:
        if x <= L:
            return int(odd_prefix[x])
        if x in memo:
            return memo[x]
        m = (x + 1) // 2
        res = m * m
        k = 3
        while k <= x:
            q = x // k
            kk = x // q
            # number of odd k in [k, kk]
            cnt_odd = (kk + 1) // 2 - k // 2
            res -= cnt_odd * A(q)
            k = kk + 1
        memo[x] = res
        return res

    return A(N)


if __name__ == "__main__":
    sys.setrecursionlimit(1_000_000)
    assert g(100) == 2007, g(100)
    print(g(5 * 10**8))  # 50660591862310323
