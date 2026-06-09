import sys

import numpy as np

from funcs import totient_sieve

sys.setrecursionlimit(1000000)
MOD = 999999017  # prime

def solve(n: int, k: int) -> int:
    """S(n) mod MOD.

    lcm(n,i) = n*i/gcd(n,i), so A(n) = sum_i i/gcd(n,i) = sum_{e|n} T(e) with
    T(e) = e*phi(e)/2 (and T(1)=1). Hence
        S(n) = sum_{e<=n} T(e)*floor(n/e) = (n + sum_{e<=n} e*phi(e)*floor(n/e))/2.
    Writing f(e)=e*phi(e) and F(x)=sum_{e<=x} f(e), the identity
    (Id*phi) * Id = Id^2 gives sum_{m<=x} m*F(floor(x/m)) = sum_{m<=x} m^2, so
        F(x) = sq2(x) - sum_{m>=2} m*F(floor(x/m)),
    evaluated sublinearly with a sieve cutoff at k.
    """
    phi = totient_sieve(k + 1)
    idx = np.arange(k + 1, dtype=np.int64)
    f = (idx % MOD) * (phi.astype(np.int64) % MOD) % MOD
    f_small = (np.cumsum(f) % MOD).astype(np.int64)
    memo: dict[int, int] = {}

    def sq2(x: int) -> int:
        return x * (x + 1) * (2 * x + 1) // 6 % MOD

    def tri(x: int) -> int:
        return x * (x + 1) // 2 % MOD

    def big_f(x: int) -> int:
        if x <= k:
            return int(f_small[x])
        cached = memo.get(x)
        if cached is not None:
            return cached
        res = sq2(x)
        m = 2
        while m <= x:
            q = x // m
            hi = x // q
            res = (res - (tri(hi) - tri(m - 1)) * big_f(q)) % MOD
            m = hi + 1
        memo[x] = res % MOD
        return memo[x]

    total = 0
    e = 1
    while e <= n:
        q = n // e
        hi = n // q
        total = (total + (q % MOD) * ((big_f(hi) - big_f(e - 1)) % MOD)) % MOD
        e = hi + 1
    return ((n % MOD) + total) % MOD * pow(2, MOD - 2, MOD) % MOD

if __name__ == "__main__":
    assert solve(100, 100) == 122726
    print(solve(99999999019, 22000000))  # 106467648
