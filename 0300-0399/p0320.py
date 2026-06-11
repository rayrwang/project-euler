import numba
import numpy as np

K = 1234567890
MOD = 10**18


@numba.jit(cache=True)
def legendre(n: int, p: int) -> int:
    """Exponent of prime p in n!."""
    s = 0
    while n > 0:
        n //= p
        s += n
    return s


@numba.jit(cache=True)
def smallest_n(p: int, t: int) -> int:
    """Smallest n with v_p(n!) >= t.

    v_p(n!) = (n - s_p(n)) / (p - 1), so n is near t (p - 1); the digit sum
    s_p(n) is at most about 64 (p - 1), bounding a short binary search.
    """
    lo = t * (p - 1)
    hi = lo + (p - 1) * 70
    while lo < hi:
        mid = (lo + hi) // 2
        if legendre(mid, p) >= t:
            hi = mid
        else:
            lo = mid + 1
    return lo


@numba.jit(cache=True)
def s(u: int) -> int:
    """sum of N(i) for 10 <= i <= u, mod 10^18.

    N(i) = max over primes p <= i of smallest_n(p, K * v_p(i!)).  Each
    v_p(i!) is nondecreasing in i, so the max never falls; stepping i to
    i + 1 only changes the primes dividing i + 1, so update those and fold
    them into a running maximum.
    """
    # Smallest-prime-factor sieve for fast factorisation of each i.
    spf = np.zeros(u + 1, dtype=np.int64)
    for p in range(2, u + 1):
        if spf[p] == 0:
            for m in range(p, u + 1, p):
                if spf[m] == 0:
                    spf[m] = p

    vp = np.zeros(u + 1, dtype=np.int64)  # v_p(i!) for current i
    cur_max = 0
    total = 0
    for i in range(2, u + 1):
        m = i
        while m > 1:
            p = spf[m]
            while m % p == 0:
                m //= p
                vp[p] += 1
            n_p = smallest_n(p, K * vp[p])
            if n_p > cur_max:
                cur_max = n_p
        if i >= 10:
            total = (total + cur_max) % MOD
    return total


if __name__ == "__main__":
    assert s(1000) == 614538266565663
    print(s(1_000_000))  # 278157919195482643
