import numba

from funcs import is_prime, mul_mod_bounded

MOD = 1234567891011


@numba.jit(cache=True)
def collect_primes(start: int, count: int):
    """The first `count` primes strictly greater than `start`."""
    primes = [0] * count
    found = 0
    n = start + 1
    if n % 2 == 0:
        n += 1
    while found < count:
        if is_prime(n):
            primes[found] = n
            found += 1
        n += 2
    return primes


@numba.jit(cache=True)
def fib_mod(n: int, mod: int) -> int:
    """Fibonacci F(n) mod `mod` by fast doubling (mod < 2**62)."""
    # Process the bits of n from most significant to least, maintaining
    # (F(k), F(k+1)); doubling identities:
    #   F(2k)   = F(k) * (2*F(k+1) - F(k))
    #   F(2k+1) = F(k)^2 + F(k+1)^2
    a, b = 0, 1  # F(0), F(1)
    high = 0
    while (1 << (high + 1)) <= n:
        high += 1
    for i in range(high, -1, -1):
        two_b = (2 * b) % mod
        t = (two_b - a) % mod
        c = mul_mod_bounded(a, t, mod)            # F(2k)
        d = (mul_mod_bounded(a, a, mod)
             + mul_mod_bounded(b, b, mod)) % mod  # F(2k+1)
        if (n >> i) & 1:
            a, b = d, (c + d) % mod
        else:
            a, b = c, d
    return a


@numba.jit(cache=True)
def solve(count: int) -> int:
    primes = collect_primes(10**14, count)
    total = 0
    for p in primes:
        total = (total + fib_mod(p, MOD)) % MOD
    return total


if __name__ == "__main__":
    # F(11) = 89, and small sanity checks of the doubling routine.
    assert fib_mod(11, MOD) == 89
    assert fib_mod(100, MOD) == 354224848179261915075 % MOD
    print(solve(100_000))  # 283988410192
