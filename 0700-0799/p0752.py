import numba
import numpy as np

@numba.njit(cache=True)
def unit_pow(n, mod):
    """(1 + sqrt(7))^n in Z[sqrt(7)] / (mod), returned as (alpha, beta)."""
    u, v = 1, 0
    bu, bv = 1 % mod, 1 % mod
    e = n
    while e > 0:
        if e & 1:
            u, v = (u * bu + 7 * v * bv) % mod, (u * bv + v * bu) % mod
        bu, bv = (bu * bu + 7 * bv * bv) % mod, 2 * bu * bv % mod
        e >>= 1
    return u, v

@numba.njit(cache=True)
def is_one(n, mod):
    u, v = unit_pow(n, mod)
    return u == 1 % mod and v == 0

@numba.njit(cache=True)
def order_mod_prime(p, spf):
    """g(p) for a prime p >= 5, p != 7: the order of 1 + sqrt(7) in the unit
    group of Z[sqrt(7)] / (p). The group exponent is p - 1 when 7 is a
    quadratic residue (ring splits as F_p x F_p) and p^2 - 1 otherwise
    (ring is F_{p^2}); start from it and strip prime factors."""
    # Euler's criterion for 7 mod p.
    sym = 1
    b = 7 % p
    e = (p - 1) // 2
    r = 1
    while e > 0:
        if e & 1:
            r = r * b % p
        b = b * b % p
        e >>= 1
    sym = 1 if r == 1 else -1
    order = p - 1 if sym == 1 else p * p - 1
    # Strip: for each prime q | order, divide while still the identity.
    for part in (p - 1, p + 1):
        if part == p + 1 and sym == 1:
            continue
        x = part
        while x > 1:
            q = spf[x]
            while x % q == 0:
                x //= q
            while order % q == 0 and is_one(order // q, p):
                order //= q
    return order

@numba.njit(cache=True)
def G(n_max):
    """g(x) is the order of the unit 1 + sqrt(7) modulo x; it is 0 iff
    gcd(x, 6) > 1, since (1 + sqrt(7))(1 - sqrt(7)) = -6 makes the element a
    unit exactly when 6 is invertible. By CRT, g is the lcm of g(p^e) over
    the prime powers of x. g(p^e) lifts from g(p) by multiplying by p while
    the power fails to be 1 modulo p^e (and g(7) = 7 is found the same way
    starting from 1)."""
    spf = np.zeros(n_max + 2, dtype=np.int64)
    for i in range(2, n_max + 2):
        if spf[i] == 0:
            for j in range(i, n_max + 2, i):
                if spf[j] == 0:
                    spf[j] = i

    # g over prime powers, stored at the prime-power index.
    gpp = np.zeros(n_max + 1, dtype=np.int64)
    for p in range(5, n_max + 1):
        if spf[p] != p:
            continue
        if p == 7:
            base = 1
        else:
            base = order_mod_prime(p, spf)
        o = base
        pe = p
        while True:
            while not is_one(o, pe):
                o *= p
            gpp[pe] = o
            if pe > n_max // p:
                break
            pe *= p

    total = 0
    for x in range(2, n_max + 1):
        if x % 2 == 0 or x % 3 == 0:
            continue
        g = 1
        rest = x
        while rest > 1:
            p = spf[rest]
            pe = 1
            while rest % p == 0:
                rest //= p
                pe *= p
            o = gpp[pe]
            # lcm(g, o)
            a, b = g, o
            while b:
                a, b = b, a % b
            g = g // a * o
        total += g
    return total

if __name__ == "__main__":
    assert G(10**2) == 28891
    assert G(10**3) == 13131583
    print(G(10**6))  # 5610899769745488
