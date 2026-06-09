import numba

from funcs import prime_sieve_int

@numba.jit(cache=True)
def mod_pow_small(a: int, b: int, p: int) -> int:
    """(a^b) mod p for p < 2^31 (products stay inside int64)."""
    r = 1
    a %= p
    while b > 0:
        if b & 1:
            r = r * a % p
        a = a * a % p
        b >>= 1
    return r

@numba.jit(cache=True)
def prime_factor_sum(n_max: int, m: int) -> int:
    """sum_{n <= n_max} s(n, m), where s(n, m) adds the distinct primes
    p <= m dividing n^15 + 1.

    Swap the sums: each prime p contributes p once for every n <= n_max
    with n^15 = -1 (mod p). Since 15 is odd, x = -1 is always a root, and
    the full solution set is -w over the 15th roots of unity w, of which
    there are exactly g = gcd(15, p - 1). A root of unity of order g is
    found as z^((p-1)/g) for random-ish z (verified by checking its order),
    and its powers enumerate all g roots.
    """
    primes = prime_sieve_int(m + 1)
    total = 0
    for idx in range(len(primes)):
        p = primes[idx]
        if p == 2:  # n^15 = 1 (mod 2): all odd n
            total += 2 * ((n_max - 1) // 2 + 1)
            continue
        g = 1
        if (p - 1) % 3 == 0:
            g *= 3
        if (p - 1) % 5 == 0:
            g *= 5
        if g == 1:
            r = p - 1  # the single root n = -1
            cnt = (n_max - r) // p + 1
            if cnt > 0:
                total += p * cnt
            continue
        # find w of order exactly g, so its powers are all of mu_g
        e = (p - 1) // g
        w = 1
        z = 2
        while True:
            w = mod_pow_small(z, e, p)
            ok = w != 1
            if ok and g % 3 == 0 and mod_pow_small(w, g // 3, p) == 1:
                ok = False
            if ok and g % 5 == 0 and mod_pow_small(w, g // 5, p) == 1:
                ok = False
            if ok:
                break
            z += 1
        wk = 1
        cnt_all = 0
        for _ in range(g):
            r = p - wk  # root n = -w^k (mod p), in [1, p-1]
            c = (n_max - r) // p + 1
            if c > 0:
                cnt_all += c
            wk = wk * w % p
        total += p * cnt_all
    return total

def brute(n_max: int, m: int) -> int:
    total = 0
    for n in range(1, n_max + 1):
        v = n**15 + 1
        d = 2
        while d <= m and d * d <= v:
            if v % d == 0:
                total += d
                while v % d == 0:
                    v //= d
            d += 1
        if 1 < v <= m:
            total += v
    return total

if __name__ == "__main__":
    assert prime_factor_sum(100, 10**4) == brute(100, 10**4)
    assert prime_factor_sum(10, 1000) - prime_factor_sum(9, 1000) == 483  # s(10,1000)
    print(prime_factor_sum(10**11, 10**8))  # 2304215802083466198
