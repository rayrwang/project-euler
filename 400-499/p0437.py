import numba
import numpy as np

@numba.njit(cache=True)
def mod_exp(a: int, e: int, m: int) -> int:
    r = 1
    a %= m
    while e > 0:
        if e & 1:
            r = r * a % m
        a = a * a % m
        e >>= 1
    return r

@numba.njit(cache=True)
def sqrt_mod(n: int, p: int) -> int:
    """A square root of n modulo prime p (n assumed a quadratic residue)."""
    n %= p
    if n == 0:
        return 0
    if p % 4 == 3:
        return mod_exp(n, (p + 1) // 4, p)
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while mod_exp(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c = s, mod_exp(z, q, p)
    t, r = mod_exp(n, q, p), mod_exp(n, (q + 1) // 2, p)
    while t != 1:
        t2, i = t, 0
        while t2 != 1:
            t2 = t2 * t2 % p
            i += 1
        b = mod_exp(c, 1 << (m - i - 1), p)
        m, c = i, b * b % p
        t = t * c % p
        r = r * b % p
    return r

@numba.njit(cache=True)
def is_primitive_root(g: int, p: int, facs: np.ndarray, nf: int) -> bool:
    if g == 0:
        return False
    for j in range(nf):
        if mod_exp(g, (p - 1) // facs[j], p) == 1:
            return False
    return True

@numba.njit(cache=True)
def run(is_composite: np.ndarray, small_primes: np.ndarray, n: int) -> int:
    """A Fibonacci primitive root of p is a primitive root that solves x^2=x+1,
    so it exists only when 5 is a quadratic residue mod p (p=5 or p == +-1 mod 5)
    and one of the two roots (1 +- sqrt5)/2 is a primitive root."""
    total = 0
    facs = np.empty(40, dtype=np.int64)
    for p in range(5, n):
        if is_composite[p]:
            continue
        if p == 5:
            total += 5
            continue
        if p % 5 != 1 and p % 5 != 4:
            continue
        m, nf = p - 1, 0
        for k in range(len(small_primes)):
            d = small_primes[k]
            if d * d > m:
                break
            if m % d == 0:
                facs[nf] = d
                nf += 1
                while m % d == 0:
                    m //= d
        if m > 1:
            facs[nf] = m
            nf += 1
        r = sqrt_mod(5, p)
        inv2 = (p + 1) // 2
        g1 = (1 + r) * inv2 % p
        g2 = (1 - r + p) * inv2 % p
        if is_primitive_root(g1, p, facs, nf) or is_primitive_root(g2, p, facs, nf):
            total += p
    return total

def sieve(n: int) -> np.ndarray:
    is_composite = np.zeros(n, dtype=np.uint8)
    is_composite[:2] = 1
    for i in range(2, int(n**0.5) + 1):
        if not is_composite[i]:
            is_composite[i * i :: i] = 1
    return is_composite

if __name__ == "__main__":
    small = np.array(
        [i for i in range(2, 10001) if all(i % j for j in range(2, int(i**0.5) + 1))],
        dtype=np.int64,
    )
    assert run(sieve(10000), small, 10000) == 1480491
    print(run(sieve(10**8), small, 10**8))  # 74204709657207
