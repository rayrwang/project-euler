import numba

from funcs import mul_mod_bounded, prime_sieve_int

@numba.jit(cache=True)
def mod_pow32(a: int, b: int, p: int) -> int:
    r = 1
    a %= p
    while b > 0:
        if b & 1:
            r = r * a % p
        a = a * a % p
        b >>= 1
    return r

@numba.jit(cache=True)
def tonelli_shanks(a: int, p: int) -> int:
    """A square root of a mod an odd prime p, assuming (a|p) = 1."""
    if p % 4 == 3:
        return mod_pow32(a, (p + 1) // 4, p)
    # write p - 1 = q * 2^s with q odd
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2  # find a non-residue
    while mod_pow32(z, (p - 1) // 2, p) != p - 1:
        z += 1
    c = mod_pow32(z, q, p)
    x = mod_pow32(a, (q + 1) // 2, p)
    t = mod_pow32(a, q, p)
    m = s
    while t != 1:
        i = 0
        t2 = t
        while t2 != 1:
            t2 = t2 * t2 % p
            i += 1
        b = mod_pow32(c, 1 << (m - i - 1), p)
        x = x * b % p
        t = t * b % p * b % p
        c = b * b % p
        m = i
    return x

@numba.jit(cache=True)
def mod_inverse64(a: int, m: int) -> int:
    old_r, r = a % m, m
    old_s, s = 1, 0
    while r != 0:
        quo = old_r // r
        old_r, r = r, old_r - quo * r
        old_s, s = s, old_s - quo * s
    return old_s % m

@numba.jit(cache=True)
def smallest_root_sum(limit: int) -> int:
    """SR(L): sum over primes p <= L of the smallest positive n with
    n^2 - 3n - 1 = 0 (mod p^2), or 0 if none exists.

    The roots are n = (3 +- sqrt(13)) / 2, so a solution mod p^2 exists iff
    13 is a quadratic residue mod p. Take a square root of 13 mod p
    (Tonelli-Shanks) and Hensel-lift it to mod p^2; the two roots follow,
    and R(p) is the smaller representative in [1, p^2].

    p = 2 fails (n^2 - 3n - 1 is always odd), and p = 13 fails too: mod 13
    the double root is n = 8 with f(8) = 39 not divisible by 169, and the
    derivative vanishes so the root cannot lift.
    """
    total = 0
    for p in prime_sieve_int(limit + 1):
        if p == 2 or p == 13 or mod_pow32(13, (p - 1) // 2, p) != 1:
            continue
        p2 = p * p
        s = tonelli_shanks(13, p)
        # Hensel: s <- s - (s^2 - 13) / (2s) mod p^2
        corr = mul_mod_bounded((s * s - 13) % p2, mod_inverse64(2 * s, p2), p2)
        s2 = (s - corr) % p2
        inv2 = (p2 + 1) // 2
        r1 = mul_mod_bounded((3 + s2) % p2, inv2, p2)
        r2 = mul_mod_bounded((3 - s2) % p2, inv2, p2)
        total += r1 if r1 < r2 else r2
    return total

if __name__ == "__main__":
    # R(3) = 5 since f(5) = 9; brute-force cross-check over small primes
    assert smallest_root_sum(3) == 5
    assert smallest_root_sum(200) == sum(
        next((n for n in range(1, p * p + 1)
              if (n * n - 3 * n - 1) % (p * p) == 0), 0)
        for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                  59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
                  127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
                  191, 193, 197, 199]
    )
    print(smallest_root_sum(10**7))  # 2647787126797397063
