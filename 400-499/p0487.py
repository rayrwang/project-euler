import numba
import numpy as np

from funcs import is_prime

@numba.jit(cache=True)
def pow_mod(a: int, e: int, p: int) -> int:
    # p < 2^31, so a*a stays below 2^62 and int64 mulmod is exact.
    a %= p
    r = 1
    while e > 0:
        if e & 1:
            r = r * a % p
        a = a * a % p
        e >>= 1
    return r

@numba.jit(cache=True)
def s_k_mod(p: int, k: int, n: int) -> int:
    """S_k(n) mod p, where S_k(n)=sum_{i<=n} f_k(i), f_k(i)=sum_{j<=i} j^k.

    S_k is a polynomial in n of degree k+2, so sample it at 0..k+2 and
    Lagrange-interpolate at n mod p over those consecutive integer nodes.
    """
    d = k + 2
    x = n % p
    y = np.empty(d + 1, dtype=np.int64)
    f = 0
    s = 0
    for i in range(d + 1):
        ik = pow_mod(i, k, p) if i > 0 else 0
        f = (f + ik) % p
        s = (s + f) % p
        y[i] = s
    if x <= d:  # node hit exactly; also avoids a zero factor below
        return y[x]

    # prefix/suffix products of (x - j) so prod_{j!=i}(x-j) = pre[i]*suf[i+1]
    pre = np.empty(d + 2, dtype=np.int64)
    pre[0] = 1
    for i in range(d + 1):
        pre[i + 1] = pre[i] * ((x - i) % p) % p
    suf = np.empty(d + 2, dtype=np.int64)
    suf[d + 1] = 1
    for i in range(d, -1, -1):
        suf[i] = suf[i + 1] * ((x - i) % p) % p

    fact = np.empty(d + 1, dtype=np.int64)
    fact[0] = 1
    for i in range(1, d + 1):
        fact[i] = fact[i - 1] * i % p
    invf = np.empty(d + 1, dtype=np.int64)
    invf[d] = pow_mod(fact[d], p - 2, p)
    for i in range(d, 0, -1):
        invf[i - 1] = invf[i] * i % p

    # denominator prod_{j!=i}(i-j) = (-1)^(d-i) * i! * (d-i)!
    res = 0
    for i in range(d + 1):
        num = pre[i] * suf[i + 1] % p
        den = invf[i] * invf[d - i] % p
        term = y[i] * num % p * den % p
        if (d - i) & 1:
            term = (p - term) % p
        res = (res + term) % p
    return res

if __name__ == "__main__":
    k = 10000
    n = 10**12
    lo = 2 * 10**9
    assert s_k_mod(1000003, 4, 100) == 35375333830 % 1000003  # S_4(100)=35375333830
    total = 0
    for cand in range(lo + 1, lo + 2001):
        if is_prime(cand):
            total += int(s_k_mod(cand, k, n))
    print(total)  # 106650212746
