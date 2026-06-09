import numba
import numpy as np

@numba.jit(cache=True)
def floor_sum(n: int, m: int, a: int, b: int) -> int:
    """sum_{i=0}^{n-1} floor((a*i + b) / m) for nonnegative a, b."""
    res = 0
    while True:
        if a >= m:
            res += (a // m) * (n * (n - 1) // 2)
            a %= m
        if b >= m:
            res += (b // m) * n
            b %= m
        y = a * n + b
        if y < m:
            return res
        n = y // m
        b = y % m
        m, a = a, m

@numba.jit(cache=True)
def line_count(k: int, b: int, v: int) -> int:
    """#{p, q >= 1 : p*b + q*v <= k}."""
    p0 = (k - v) // b
    if p0 <= 0:
        return 0
    return floor_sum(p0, v, b, k - p0 * b)

@numba.jit(cache=True)
def x_count(m: int) -> int:
    """X(M) = #{u > v >= 1, c > b >= 1 : u*b + v*c <= M}.

    Substituting u = v + p, c = b + q reduces to counting (p, q >= 1)
    under the line p*b + q*v <= M - 2*v*b for every (v, b), each an
    O(log) floor_sum; (v, b) symmetry halves the work.
    """
    total = 0
    v = 1
    while 2 * v * v + 2 * v <= m:  # diagonal b = v exists
        total += line_count(m - 2 * v * v, v, v)
        v += 1
    v = 1
    while True:
        b = v + 1
        if 2 * v * b + b + v > m:
            break
        while 2 * v * b + b + v <= m:
            total += 2 * line_count(m - 2 * v * b, b, v)
            b += 1
        v += 1
    return total

@numba.jit(cache=True)
def w_count(m: int, d: np.ndarray, dpre: np.ndarray) -> int:
    """W(M) = #{u > v >= 1, b > c >= 1 : u*b + v*c <= M}.

    Inclusion-exclusion over the order relations: with
    W0 = #{all u,v,b,c >= 1} = sum_{x+y<=M} d(x) d(y) (x = ub, y = vc),
    the swap (u,v,b,c) -> (v,u,c,b) pairs the (>,>) region with (<,<) and
    (>,<) with (<,>), so W0 = 2W + 2X + B1 + B2 - Dh with B1 = #{u = v},
    B2 = #{b = c} (= B1 by symmetry) and Dh = #{u = v and b = c}.
    """
    w0 = 0
    for x in range(1, m):
        w0 += int(d[x]) * dpre[m - x]
    b1 = 0
    v = 1
    while v <= m:
        q = m // v
        v2 = m // q
        b1 += (v2 - v + 1) * (q * (q - 1) // 2)
        v = v2 + 1
    h = m // 2
    dh = 0
    v = 1
    while v <= h:
        q = h // v
        v2 = h // q
        dh += (v2 - v + 1) * q
        v = v2 + 1
    num = w0 - 2 * x_count(m) - 2 * b1 + dh
    return num // 2

@numba.jit(cache=True)
def euclid_step_sum(n: int) -> int:
    """S(N) = sum of Euclid step counts E(x, y) over 1 <= x, y <= N.

    Pairs scale by their gcd, leaving coprime pairs; for y > x the chain
    of E(y, x) climbs the reverse Euclid tree rooted at (1, 0), so the
    depth sum becomes a descendant count. Descendants of a node (b, c)
    have first coordinates u*b + v*c over continued-fraction prefixes,
    hitting (1,0) and (1,1) once and every coprime u > v >= 1 twice (the
    two CF representations). Summing and Mobius-inverting both
    coprimalities collapses (1 * mu * mu = mu) to the closed form
        S(N) = 2N^2 - N - floor(N/2) + 4 sum_m mu(m) W(floor(N/m)),
    with W the order-constrained quadruple count above.
    """
    # divisor counts and prefix sums
    d = np.zeros(n + 1, dtype=np.int32)
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            d[j] += 1
    dpre = np.zeros(n + 1, dtype=np.int64)
    s = 0
    for i in range(1, n + 1):
        s += d[i]
        dpre[i] = s
    # Mertens prefix of the Mobius function
    mu = np.ones(n + 1, dtype=np.int8)
    comp = np.zeros(n + 1, dtype=np.bool_)
    for p in range(2, n + 1):
        if not comp[p]:
            for j in range(p, n + 1, p):
                if j > p:
                    comp[j] = True
                mu[j] = -mu[j]
            pp = p * p
            for j in range(pp, n + 1, pp):
                mu[j] = 0
    mert = np.zeros(n + 1, dtype=np.int64)
    s = 0
    for i in range(1, n + 1):
        s += mu[i]
        mert[i] = s
    total = 2 * n * n - n - n // 2
    k = 1
    while k <= n:
        q = n // k
        k2 = n // q
        coeff = mert[k2] - mert[k - 1]
        if coeff != 0:
            total += 4 * coeff * w_count(q, d, dpre)
        k = k2 + 1
    return total

@numba.jit(cache=True)
def brute(n: int) -> int:
    total = 0
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            a, b = x, y
            while b:
                a, b = b, a % b
                total += 1
    return total

if __name__ == "__main__":
    assert euclid_step_sum(1) == 1  # S(1), given
    assert euclid_step_sum(10) == brute(10) == 221  # S(10), given
    assert euclid_step_sum(100) == brute(100) == 39826  # S(100), given
    assert euclid_step_sum(2000) == brute(2000)
    print(euclid_step_sum(5 * 10**6))  # 326624372659664
