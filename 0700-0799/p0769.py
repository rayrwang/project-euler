import numba
import numpy as np

@numba.njit(cache=True, inline='always')
def isqrt64(x):
    if x < 0:
        return -1
    r = int(np.sqrt(x))
    while r * r > x:
        r -= 1
    while (r + 1) * (r + 1) <= x:
        r += 1
    return r

@numba.njit(cache=True)
def W(m, cong):
    """#{(s,t): t >= 1, -5t/2 < s < -sqrt(3) t, s^2+5st+3t^2 >= -m},
    restricted to s == 4t (mod 13) when cong is set."""
    if m < 3:
        return 0
    total = 0
    tmax = isqrt64((4 * m) // 10) + 2
    for t in range(1, tmax + 1):
        smin = -(5 * t) // 2 + 1
        smax = -isqrt64(3 * t * t) - 1
        if smin > smax:
            continue
        d = 13 * t * t - 4 * m
        if d > 0:
            r = isqrt64(d)
            umin = r if r * r == d else r + 1
            if (umin & 1) != (t & 1):
                umin += 1
            s2 = (umin - 5 * t) // 2
            if s2 > smin:
                smin = s2
            if smin > smax:
                continue
        if not cong:
            total += smax - smin + 1
        else:
            a = (4 * t) % 13
            total += (smax - a) // 13 - (smin - 1 - a) // 13
    return total

@numba.njit(cache=True)
def C(n):
    """Primitive representations of squares z^2 (z <= n) by
    x^2 + 5xy + 3y^2 with x, y > 0 coprime.

    The conic x^2+5xy+3y^2 = z^2 is parametrised through (1, 0, 1):
    (x : y : z) = (3t^2 - s^2 : -t(2s+5t) : s^2+5st+3t^2). For coprime
    (s, t) the gcd of the three forms is 13 exactly when s == 4t
    (mod 13) (4 is the double root of c^2+5c+3 mod 13) and 1 otherwise,
    and distinct (s : t) give distinct solutions. Requiring x, y, z > 0
    means all three forms share a sign, which happens precisely for
    s/t in (-5/2, -sqrt(3)) (all negative), where the primitive
    solution is (-X, -Y, -Z)/d. This was verified by matching a direct
    brute-force count of representations at n = 100 and 1000.

    Hence C(n) counts coprime lattice points in a hyperbolic wedge:
    those with -Z <= n, plus those with s == 4t (mod 13) and
    n < -Z <= 13 n. Coprimality is removed by Moebius (when 13 | g the
    congruence becomes automatic); each W evaluation runs over
    t = O(sqrt(m)) with exact integer-sqrt interval endpoints, the
    quadratic constraint solved through u = 2s + 5t >= sqrt(13t^2-4m)
    with the parity of u fixed by t.
    """
    g = isqrt64(13 * n // 3) + 1
    mu = np.ones(g + 1, dtype=np.int8)
    isc = np.zeros(g + 1, dtype=np.bool_)
    primes = np.empty(g, dtype=np.int64)
    npp = 0
    for i in range(2, g + 1):
        if not isc[i]:
            primes[npp] = i
            npp += 1
            mu[i] = -1
        for j in range(npp):
            p = primes[j]
            if i * p > g:
                break
            isc[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    total = 0
    k = 1
    while k * k * 3 <= 13 * n:
        if mu[k] != 0:
            m1 = n // (k * k)
            total += mu[k] * W(m1, False)
            m2 = (13 * n) // (k * k)
            if k % 13 != 0:
                total += mu[k] * (W(m2, True) - W(m1, True))
            else:
                total += mu[k] * (W(m2, False) - W(m1, False))
        k += 1
    return total

if __name__ == "__main__":
    assert C(10**3) == 142
    assert C(10**6) == 142463
    print(C(10**14))  # 14246712611506
