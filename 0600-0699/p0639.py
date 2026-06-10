"""Project Euler Problem 639: Summing a Multiplicative Function.

f_k is multiplicative with f_k(p^e) = p^k for every e >= 1; we need
sum_{k=1}^{50} S_k(10^12) mod 10^9 + 7 with S_k(n) = sum_{i<=n} f_k(i).

Write f_k = id_k * c_k (Dirichlet convolution).  Matching prime powers,
c_k(p) = 0 and generally c_k(p^e) = p^k - sum_{i=1}^{e} p^{ik} c_k(p^{e-i}),
so c_k is supported on powerful numbers -- only about 2.4 * 10^6 of them
lie below 10^12.  Then

    S_k(N) = sum_{m powerful, m <= N} c_k(m) * P_k(floor(N/m)),

with P_k(x) = sum_{i<=x} i^k.  For each k a DFS over primes p <= 10^6
generates every powerful m with its running c_k-product (the prime-power
values computed on the fly from the recurrence).  Quotients N/m below
10^6 hit a precomputed prefix-power table; the ~2400 powerful m < 10^6
have large quotients, evaluated by Lagrange interpolation of the degree
k+1 polynomial P_k from k+2 sample points.

Checks: S_1(10) = 41, S_1(100) = 3512, S_2(100) = 208090,
S_1(10^4) = 35252550 and sum_{k<=3} S_k(10^8) == 338787512 (given), plus
a brute-force multiplicative sieve for n <= 10^5, k <= 4.
"""

import numba
import numpy as np

P = 1_000_000_007


@numba.jit(cache=True)
def _pow(b: int, e: int) -> int:
    r = 1
    b %= P
    while e:
        if e & 1:
            r = r * b % P
        b = b * b % P
        e >>= 1
    return r


@numba.jit(cache=True)
def _faulhaber_large(x: int, k: int) -> int:
    """P_k(x) by Lagrange interpolation at points 0..k+1."""
    d = k + 2  # number of points
    ys = np.empty(d, dtype=np.int64)
    acc = 0
    for j in range(d):
        acc = (acc + _pow(j, k)) % P if j else 0
        ys[j] = acc
    xm = x % P
    pre = np.empty(d + 1, dtype=np.int64)
    suf = np.empty(d + 1, dtype=np.int64)
    pre[0] = 1
    for j in range(d):
        pre[j + 1] = pre[j] * ((xm - j) % P) % P
    suf[d] = 1
    for j in range(d - 1, -1, -1):
        suf[j] = suf[j + 1] * ((xm - j) % P) % P
    # factorials
    fact = np.empty(d, dtype=np.int64)
    fact[0] = 1
    for j in range(1, d):
        fact[j] = fact[j - 1] * j % P
    inv_full = _pow(fact[d - 1], P - 2)
    total = 0
    for j in range(d):
        num = pre[j] * suf[j + 1] % P
        denom = fact[j] * fact[d - 1 - j] % P
        term = ys[j] * num % P * _pow(denom, P - 2) % P
        if (d - 1 - j) % 2 == 1:
            term = P - term
        total = (total + term) % P
    _ = inv_full
    return total


@numba.jit(cache=True)
def S_k(N: int, k: int, primes: np.ndarray, q_small: int) -> int:
    # prefix powers for small quotients
    table = np.empty(q_small + 1, dtype=np.int64)
    table[0] = 0
    for i in range(1, q_small + 1):
        table[i] = (table[i - 1] + _pow(i, k)) % P
    np_ = len(primes)
    # explicit DFS over powerful numbers
    stack_idx = np.empty(3_000_000, dtype=np.int64)
    stack_val = np.empty(3_000_000, dtype=np.int64)
    stack_c = np.empty(3_000_000, dtype=np.int64)
    top = 0
    stack_idx[0] = 0
    stack_val[0] = 1
    stack_c[0] = 1
    q0 = N  # m = 1 contribution
    total = _faulhaber_large(q0, k) if q0 > q_small else table[q0]
    cpe = np.empty(64, dtype=np.int64)
    while top >= 0:
        idx = stack_idx[top]
        val = stack_val[top]
        cp = stack_c[top]
        top -= 1
        for j in range(idx, np_):
            p = primes[j]
            if val > N // (p * p):
                break
            # c_k(p^e) table for this prime
            pk = _pow(p, k)
            cpe[0] = 1
            cpe[1] = 0
            emax = 1
            m = val * p * p
            e = 2
            while True:
                # c(p^e) = p^k - sum_{i=1..e} p^{ik} c(p^{e-i})
                while emax < e:
                    emax += 1
                    s = pk
                    pik = 1
                    for i in range(1, emax + 1):
                        pik = pik * pk % P
                        s = (s - pik * cpe[emax - i]) % P
                    cpe[emax] = s % P
                c_new = cp * cpe[e] % P
                if c_new:
                    q = N // m
                    pv = table[q] if q <= q_small else _faulhaber_large(q, k)
                    total = (total + c_new * pv) % P
                    top += 1
                    stack_idx[top] = j + 1
                    stack_val[top] = m
                    stack_c[top] = c_new
                if m > N // p:
                    break
                m *= p
                e += 1
    return total % P


def primes_to(n: int) -> np.ndarray:
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if s[i]:
            s[i * i :: i] = False
    return np.flatnonzero(s).astype(np.int64)


def brute(n: int, k: int) -> int:
    f = np.ones(n + 1, dtype=np.int64)
    spf = np.zeros(n + 1, dtype=np.int64)
    for p in range(2, n + 1):
        if spf[p] == 0:
            spf[p::p] = p
    for i in range(2, n + 1):
        p = spf[i]
        j = i
        while j % p == 0:
            j //= p
        f[i] = f[j] * pow(int(p), k, P) % P
    return int(f[1:].sum() % P)


if __name__ == "__main__":
    primes = primes_to(10**6)
    small_primes = primes[primes <= 400]
    for k in range(1, 5):
        assert S_k(10**5, k, small_primes, 10**4) == brute(10**5, k), k
    assert S_k(10, 1, small_primes, 10) == 41
    assert S_k(100, 1, small_primes, 100) == 3512
    assert S_k(100, 2, small_primes, 100) == 208090
    assert S_k(10**4, 1, small_primes, 10**3) == 35252550
    p8 = primes[primes <= 10**4]
    assert sum(S_k(10**8, k, p8, 10**5) for k in range(1, 4)) % P == 338787512
    total = sum(S_k(10**12, k, primes, 10**6) for k in range(1, 51))
    print(total % P)  # 797866893
