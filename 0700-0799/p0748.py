import numba

MOD = 10**9

@numba.njit(cache=True)
def gcd2(a, b):
    while b:
        a, b = b, a % b
    return a

@numba.njit(cache=True)
def S(n):
    """Last 9 digits of the sum of x + y + z over primitive solutions of
    1/x^2 + 1/y^2 = 13/z^2 with x <= y and x, y, z <= n.

    Writing x = g u, y = g v with gcd(u, v) = 1, the equation forces
    z = u v and u^2 + v^2 = 13 g^2 (the cofactor w satisfies w^2 | 13 so
    w = 1), with primitivity automatic. In Z[i], 13 = (3+2i)(3-2i) and
    gcd(u, v) = 1 forces u + v i = unit * (3 +- 2i)(s + t i)^2 with
    g = s^2 + t^2, gcd(s, t) = 1, s + t odd (both odd makes u, v even);
    the two conjugate families with s > t >= 0 enumerate each unordered
    primitive pair exactly once (they coincide at t = 0, and the rare
    13-imprimitive cases are caught by an explicit gcd(u, v) check).
    Verified: reproduces the full brute-force solution set for small
    bounds and S(10^2) = 124, S(10^3) = 1470, S(10^5) = 2340084.

    Bounds: max(u, v) >= sqrt(13/2) g, so y <= n forces
    g <= sqrt(n / 2.55), i.e. s <= ~7920 for n = 10^16.
    """
    total = 0
    smax = int(n**0.25) + 2  # need s^2 <= g <= (n / sqrt(6.5))^(1/2)
    for s in range(1, smax + 1):
        for t in range(s):
            if (s + t) % 2 == 0 or gcd2(s, t) != 1:
                continue
            g = s * s + t * t
            d1 = s * s - t * t
            d2 = s * t
            nfam = 1 if t == 0 else 2
            for fam in range(nfam):
                if fam == 0:
                    u = abs(3 * d1 - 4 * d2)
                    v = abs(2 * d1 + 6 * d2)
                else:
                    u = abs(3 * d1 + 4 * d2)
                    v = abs(2 * d1 - 6 * d2)
                if gcd2(u, v) != 1:
                    continue
                z = u * v
                if z > n:
                    continue
                x = g * u
                y = g * v
                if x > y:
                    x, y = y, x
                if y <= n:
                    total = (total + x + y + z) % MOD
    return total

if __name__ == "__main__":
    assert S(10**2) == 124
    assert S(10**3) == 1470
    assert S(10**5) == 2340084
    print(S(10**16))  # 276402862
