import numba
import numpy as np

MOD = 10**9 + 7
N = 10**12

@numba.njit(cache=True)
def lucy(n, r):
    """Lucy_Hedgehog prime counting: returns arrays (small, large) with
    small[v] = pi(v) for v <= r and large[i] = pi(n // i) for i = 1..r."""
    small = np.zeros(r + 1, np.int64)
    large = np.zeros(r + 1, np.int64)
    for v in range(1, r + 1):
        small[v] = v - 1
    for i in range(1, r + 1):
        large[i] = n // i - 1
    for p in range(2, r + 1):
        if small[p] == small[p - 1]:
            continue  # p not prime
        sp = small[p - 1]
        p2 = p * p
        imax = n // p2
        if imax > r:
            imax = r
        for i in range(1, imax + 1):
            ip = i * p
            if ip <= r:
                large[i] -= large[ip] - sp
            else:
                large[i] -= small[n // ip] - sp
        for v in range(r, p2 - 1, -1):
            small[v] -= small[v // p] - sp
    return small, large

def solve(n):
    r = int(n**0.5)
    while r * r > n:
        r -= 1
    while (r + 1) * (r + 1) <= n:
        r += 1
    small, large = lucy(n, r)

    def pi(x):
        if x <= 0:
            return 0
        if x <= r:
            return int(small[x])
        return int(large[n // x])

    # s = 1 term: A = sum over primes p<=n of q(n-q), q = floor(n/p),
    # grouped into blocks where floor(n/p) is constant.
    a = 0
    i = 1
    prev_pi = 0  # pi(i-1); the block boundaries are exactly key values
    while i <= n:
        q = n // i
        hi = n // q
        cnt = pi(hi) - prev_pi
        a = (a + (q % MOD) * ((n - q) % MOD) % MOD * (cnt % MOD)) % MOD
        prev_pi = pi(hi)
        i = hi + 1

    # s >= 2 term: only primes p <= sqrt(n) can satisfy p^s <= n.
    sieve = np.ones(r + 1, np.bool_)
    sieve[:2] = False
    for x in range(2, int(r**0.5) + 1):
        if sieve[x]:
            sieve[x * x::x] = False
    b = 0
    for p in range(2, r + 1):
        if not sieve[p]:
            continue
        ps = p * p
        while ps <= n:
            q = n // ps
            b = (b + (q % MOD) * ((n - q) % MOD)) % MOD
            ps *= p

    return 2 * (a + b) % MOD

if __name__ == "__main__":
    print(solve(N))  # 413876461
