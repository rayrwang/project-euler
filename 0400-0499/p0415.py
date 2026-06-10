import numba
import numpy as np

MOD = 10**8  # = 2^8 * 5^8
INV256 = pow(256, -1, 5**8)

@numba.jit(cache=True)
def pow2_mod(e: int) -> int:
    """2^e mod 10^8 for any e >= 0, via CRT on 2^8 and 5^8."""
    if e < 27:
        return (1 << e) % MOD
    # 2^e = 0 (mod 256); 2^e mod 5^8 with exponent mod lambda(5^8)
    r = 1
    b = 2
    x = e % 312500  # phi(5^8) = 4 * 5^7
    m5 = 390625
    while x > 0:
        if x & 1:
            r = r * b % m5
        b = b * b % m5
        x >>= 1
    return 256 * (r * INV256 % m5) % MOD

@numba.jit(cache=True)
def half_prod(a: int, b: int, mod: int) -> int:
    """a*b/2 mod `mod` where a*b is even, halving exactly first."""
    if a % 2 == 0:
        a //= 2
    else:
        b //= 2
    return (a % mod) * (b % mod) % mod

@numba.jit(cache=True)
def square_pyramid(x: int, mod: int) -> int:
    """1^2 + ... + x^2 mod `mod` via exact cancellation of the 6."""
    a, b, c = x, x + 1, 2 * x + 1
    if a % 2 == 0:
        a //= 2
    else:
        b //= 2
    if a % 3 == 0:
        a //= 3
    elif b % 3 == 0:
        b //= 3
    else:
        c //= 3
    return (a % mod) * (b % mod) % mod * (c % mod) % mod

@numba.jit(cache=True)
def titanic_count(n: int) -> int:
    """T(n) mod 10^8: subsets of the (n+1)^2 grid admitting a line through
    exactly two of their points.

    By Sylvester-Gallai the non-titanic sets are exactly: empty, single
    points, and collinear sets of size >= 3. So with g(k) = 2^k - 1 - k
    - k(k-1)/2, T = 2^P - 1 - P - sum over lines of g(k_L).

    Axis-parallel lines contribute 2(n+1) g(n+1). For a primitive slanted
    direction (a, b), the window count A_m = (n+1-(m-1)a)(n+1-(m-1)b)
    counts every line with k points (k-m+1) times, so lines with >= m
    points are A_m - A_{m+1} and double Abel summation leaves
    sum_L g = sum_m A_m (2^(m-2) - 1). Substituting s = m-1, Mobius over
    gcd(a, b), and grouping by t = s*d gives
        Slant = 2 sum_t F(t)^2 h(t),   h = mu * w,  w(s) = 2^(s-1) - 1,
    with F(t) = K(n+1) - t K(K+1)/2, K = floor(n/t), constant-K blocks.
    The weighted prefix sums H_j(x) = sum_{t<=x} t^j h(t) unfold as
    sum_d mu(d) d^j G_j(x/d) with closed-form G_j, weighted Mertens sums
    M_j computed sublinearly, and every argument a quotient of n.
    """
    r = int(n**0.5)
    while (r + 1) * (r + 1) <= n:
        r += 1
    while r * r > n:
        r -= 1
    # ---- weighted Mertens M_j on a sieved base ----
    d0 = int(n ** (2.0 / 3.0)) + 1
    if d0 < 2 * r + 2:
        d0 = 2 * r + 2
    mu = np.ones(d0 + 1, dtype=np.int8)
    comp = np.zeros(d0 + 1, dtype=np.bool_)
    for p in range(2, d0 + 1):
        if not comp[p]:
            for j in range(p, d0 + 1, p):
                if j > p:
                    comp[j] = True
                mu[j] = -mu[j]
            pp = p * p
            for j in range(pp, d0 + 1, pp):
                mu[j] = 0
    m0s = np.zeros(d0 + 1, dtype=np.int32)
    m1s = np.zeros(d0 + 1, dtype=np.int32)
    m2s = np.zeros(d0 + 1, dtype=np.int32)
    a0 = a1 = a2 = 0
    for i in range(1, d0 + 1):
        if mu[i] != 0:
            im = i % MOD
            v = int(mu[i])
            a0 = (a0 + v) % MOD
            a1 = (a1 + v * im) % MOD
            a2 = (a2 + v * im % MOD * im) % MOD
        m0s[i] = a0
        m1s[i] = a1
        m2s[i] = a2
    # big quotients y = n // i for i <= n // d0, filled in increasing y
    nbig = n // d0
    m0b = np.zeros(nbig + 1, dtype=np.int64)
    m1b = np.zeros(nbig + 1, dtype=np.int64)
    m2b = np.zeros(nbig + 1, dtype=np.int64)
    for i in range(nbig, 0, -1):
        y = n // i
        s0, s1, s2 = 1, 1, 1
        k = 2
        while k <= y:
            q = y // k
            k2 = y // q
            if q <= d0:
                v0, v1, v2 = m0s[q], m1s[q], m2s[q]
            else:
                idx = n // q
                v0, v1, v2 = m0b[idx], m1b[idx], m2b[idx]
            cnt = (k2 - k + 1) % MOD
            ksum = half_prod(k + k2, k2 - k + 1, MOD)
            k2sum = (square_pyramid(k2, MOD) - square_pyramid(k - 1, MOD)) % MOD
            s0 = (s0 - cnt * v0) % MOD
            s1 = (s1 - ksum * v1) % MOD
            s2 = (s2 - k2sum * v2) % MOD
            k = k2 + 1
        m0b[i] = s0
        m1b[i] = s1
        m2b[i] = s2

    # ---- closed-form G_j at every quotient of n ----
    gs = np.zeros((3, r + 1), dtype=np.int64)       # arguments y <= r
    gb = np.zeros((3, r + 1), dtype=np.int64)       # arguments y = n // i
    for half in range(2):
        for i in range(1, r + 1):
            y = i if half == 0 else n // i
            p2 = pow2_mod(y)
            ym = y % MOD
            g0 = (p2 - 1 - ym) % MOD
            g1 = (((ym - 1) * p2 + 1) % MOD - half_prod(y, y + 1, MOD)) % MOD
            t2 = ((ym * ym - 2 * ym + 3) % MOD * p2 - 3) % MOD
            g2 = (t2 - square_pyramid(y, MOD)) % MOD
            if half == 0:
                gs[0, i], gs[1, i], gs[2, i] = g0, g1, g2
            else:
                gb[0, i], gb[1, i], gb[2, i] = g0, g1, g2

    # ---- outer sum over constant-K blocks, H_j at each boundary ----
    slant = 0
    h0p = h1p = h2p = 0  # H_j at previous boundary
    t = 1
    while t <= n:
        kq = n // t
        t2 = n // kq
        # H_j(t2) = sum_d mu(d) d^j G_j(t2 // d)
        h0 = h1 = h2 = 0
        d = 1
        while d <= t2:
            q = t2 // d
            d2 = t2 // q
            if q <= r:
                g0, g1, g2 = gs[0, q], gs[1, q], gs[2, q]
            else:
                idx = n // q
                g0, g1, g2 = gb[0, idx], gb[1, idx], gb[2, idx]
            if d2 <= d0:
                w0 = (m0s[d2] - m0s[d - 1]) % MOD
                w1 = (m1s[d2] - m1s[d - 1]) % MOD
                w2 = (m2s[d2] - m2s[d - 1]) % MOD
            else:
                lo0, lo1, lo2 = (m0s[d - 1], m1s[d - 1], m2s[d - 1]) \
                    if d - 1 <= d0 else (m0b[n // (d - 1)],
                                         m1b[n // (d - 1)], m2b[n // (d - 1)])
                w0 = (m0b[n // d2] - lo0) % MOD
                w1 = (m1b[n // d2] - lo1) % MOD
                w2 = (m2b[n // d2] - lo2) % MOD
            h0 = (h0 + w0 * g0) % MOD
            h1 = (h1 + w1 * g1) % MOD
            h2 = (h2 + w2 * g2) % MOD
            d = d2 + 1
        # block contribution with F(t) = A - B t
        a = (kq % MOD) * ((n + 1) % MOD) % MOD
        b = half_prod(kq, kq + 1, MOD)
        term = (a * a % MOD * ((h0 - h0p) % MOD)
                - 2 * a * b % MOD * ((h1 - h1p) % MOD)
                + b * b % MOD * ((h2 - h2p) % MOD)) % MOD
        slant = (slant + term) % MOD
        h0p, h1p, h2p = h0, h1, h2
        t = t2 + 1

    # ---- assemble ----
    p_pts = (n + 1) * (n + 1) if n < 3 * 10**9 else -1
    if p_pts >= 0:
        two_p = pow2_mod(p_pts)
        p_mod = p_pts % MOD
    else:  # (n+1)^2 overflows nothing here (n <= 1e11 -> 1e22 > int64)
        np1 = n + 1
        # exponent mod 312500 and value mod 1e8 via modular squares
        e5 = (np1 % 312500) * (np1 % 312500) % 312500
        # e >= 27 certainly; emulate pow2_mod on the reduced exponent
        r5 = 1
        bb = 2
        x = e5 % 312500
        m5 = 390625
        while x > 0:
            if x & 1:
                r5 = r5 * bb % m5
            bb = bb * bb % m5
            x >>= 1
        two_p = 256 * (r5 * INV256 % m5) % MOD
        p_mod = (np1 % MOD) * (np1 % MOD) % MOD
    # g(n+1) for the 2(n+1) axis-parallel lines
    k1 = n + 1
    g_axis = (pow2_mod(k1) - 1 - k1 % MOD - half_prod(k1, k1 - 1, MOD)) % MOD
    total = (two_p - 1 - p_mod
             - 2 * (k1 % MOD) % MOD * g_axis
             - 2 * slant) % MOD
    return total % MOD

if __name__ == "__main__":
    assert titanic_count(1) == 11
    assert titanic_count(2) == 494
    assert titanic_count(4) == 33554178 % MOD
    assert titanic_count(111) == 13500401  # given
    assert titanic_count(10**5) == 63259062  # given
    print(titanic_count(10**11))  # 55859742
