import numba

@numba.jit(cache=True)
def sum_sq_mod(m: int, mod: int) -> int:
    """sum_{k=1}^m k^2 mod, via m(m+1)(2m+1)/6 with the /6 done exactly."""
    a = m
    b = m + 1
    c = 2 * m + 1
    if a % 2 == 0:        # one of m, m+1 is even
        a //= 2
    else:
        b //= 2
    if a % 3 == 0:        # one of m, m+1, 2m+1 is divisible by 3
        a //= 3
    elif b % 3 == 0:
        b //= 3
    else:
        c //= 3
    a %= mod
    b %= mod
    c %= mod
    return (a * b % mod) * c % mod

@numba.jit(cache=True)
def sigma2_summatory(n: int, mod: int) -> int:
    total = 0
    k = 1
    s_prev = 0  # S(k-1), starting at S(0) = 0
    while k <= n:
        q = n // k
        hi = n // q        # largest k' with n//k' == q
        s_hi = sum_sq_mod(hi, mod)
        block = (s_hi - s_prev) % mod
        total = (total + (q % mod) * block) % mod
        s_prev = s_hi
        k = hi + 1
    return total % mod

if __name__ == "__main__":
    MOD = 10**9
    assert sigma2_summatory(6, MOD) == 113
    print(sigma2_summatory(10**15, MOD))  # 281632621
