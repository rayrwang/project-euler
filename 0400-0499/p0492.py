import numba
import numpy as np

@numba.jit(cache=True)
def isqrt(n: int) -> int:
    if n < 2:
        return n
    r = int(n**0.5)
    while r * r > n:
        r -= 1
    while (r + 1) * (r + 1) <= n:
        r += 1
    return r

@numba.jit(cache=True)
def pow_mod(a: int, e: int, m: int) -> int:
    a %= m
    r = 1
    while e > 0:
        if e & 1:
            r = r * a % m
        a = a * a % m
        e >>= 1
    return r

@numba.jit(cache=True)
def lucas_v(k: int, p_param: int, p: int) -> int:
    """V_k mod p for the Lucas sequence V_0=2, V_1=P, with Q=1
    (so V_k = lambda^k + lambda^-k for lambda + lambda^-1 = P)."""
    if k == 0:
        return 2 % p
    vm = 2 % p
    vm1 = p_param % p
    nbits = 0
    kk = k
    while kk > 0:
        nbits += 1
        kk >>= 1
    for bit in range(nbits - 1, -1, -1):
        if (k >> bit) & 1:
            vm = (vm * vm1 - p_param) % p
            vm1 = (vm1 * vm1 - 2) % p
        else:
            vm1 = (vm * vm1 - p_param) % p
            vm = (vm * vm - 2) % p
    return vm

@numba.jit(cache=True)
def b(x: int, y: int, n: int) -> int:
    """sum over primes p in [x, x+y] of (a_n mod p), where a_1=1 and
    a_{k+1} = 6 a_k^2 + 10 a_k + 3.

    Substituting w = 6a + 5 turns the recurrence into w_{k+1} = w_k^2 - 2 with
    w_1 = 11, so w_n = lambda^(2^(n-1)) + lambda^(-2^(n-1)) where lambda solves
    X^2 - 11X + 1 = 0 (discriminant 117 = 9*13). That is the Lucas V-sequence
    with P=11, Q=1. Since lambda^(p-1)=1 when 13 is a quadratic residue mod p
    and lambda^(p+1)=1 otherwise, the huge exponent 2^(n-1) only matters modulo
    p-1 or p+1; reduce it, evaluate V by Lucas doubling, and recover a_n.
    """
    lim = isqrt(x + y) + 1
    is_base = np.ones(lim + 1, dtype=np.bool_)
    is_base[0] = False
    is_base[1] = False
    for i in range(2, isqrt(lim) + 1):
        if is_base[i]:
            is_base[i * i::i] = False

    segment = np.ones(y + 1, dtype=np.bool_)
    for q in range(2, lim + 1):
        if is_base[q]:
            start = ((x + q - 1) // q) * q
            if start < q * q:
                start = q * q
            for multiple in range(start, x + y + 1, q):
                segment[multiple - x] = False

    total = 0
    exponent = n - 1
    for i in range(y + 1):
        if segment[i]:
            p = x + i
            legendre = pow_mod(13, (p - 1) // 2, p)
            order = p - 1 if legendre == 1 else p + 1
            e = pow_mod(2, exponent, order)
            w = lucas_v(e, 11, p)
            total += (w - 5) * pow_mod(6, p - 2, p) % p
    return total

if __name__ == "__main__":
    assert b(10**9, 10**3, 10**3) == 23674718882
    assert b(10**9, 10**3, 10**15) == 20731563854
    print(b(10**9, 10**7, 10**15))  # 242586962923928
