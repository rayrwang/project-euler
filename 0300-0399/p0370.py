import math

import numba


@numba.njit
def _a_all(p: int) -> int:
    """sum over integer pairs m <= n with n < phi*m (the triangle inequality) and
    base = m^2 + m n + n^2 <= p of floor(p / base).

    For a fixed m, base is increasing in n, so floor(p / base) is a step function;
    each step is jumped in one go by solving base(n) <= p // q for the block end,
    making the per-m work O(number of distinct quotients) rather than O(range).
    """
    total = 0
    m = 1
    while 3 * m * m <= p:
        # Largest n with n^2 - m n - m^2 < 0, i.e. n < phi*m (triangle inequality).
        n_tri = (m + int(math.sqrt(5.0 * m * m))) // 2
        while n_tri * n_tri - m * n_tri - m * m >= 0:
            n_tri -= 1
        while (n_tri + 1) * (n_tri + 1) - m * (n_tri + 1) - m * m < 0:
            n_tri += 1
        n = m
        while n <= n_tri:
            base = m * m + m * n + n * n
            if base > p:
                break
            q = p // base
            lim = p // q  # block: all n2 with base(n2) <= lim share quotient q
            dd = 4 * lim - 3 * m * m
            if dd < 0:
                n2 = n
            else:
                n2 = (-m + int(math.sqrt(dd))) // 2
                while n2 * n2 + m * n2 + m * m > lim:
                    n2 -= 1
                while (n2 + 1) * (n2 + 1) + m * (n2 + 1) + m * m <= lim:
                    n2 += 1
            if n2 > n_tri:
                n2 = n_tri
            if n2 < n:
                n2 = n
            total += (n2 - n + 1) * q
            n = n2 + 1
        m += 1
    return total


def count_geometric_triangles(p: int) -> int:
    """Number of integer triangles a <= b <= c with b^2 = a c (sides in geometric
    progression) and perimeter <= p.

    Such a triangle is a scaling s * (m^2, m n, n^2) of a primitive shape with
    gcd(m, n) = 1, m <= n, and the triangle inequality m^2 + m n > n^2 (n < phi*m);
    its perimeter is s * (m^2 + m n + n^2). The count is therefore
        sum over primitive (m, n) of floor(p / (m^2 + m n + n^2)).
    Dropping coprimality, A(p) = sum over all (m, n) of floor(p / base) satisfies
    A(p) = sum_g f(floor(p / g^2)) with f the primitive-only sum, because a pair
    (g m', g n') contributes floor(p / (g^2 base')). Mobius inversion then gives
        f(p) = sum_g mu(g) * A(floor(p / g^2)).
    """
    r = int(math.isqrt(p // 3)) + 2
    mu = [1] * (r + 1)
    primes: list[int] = []
    is_comp = bytearray(r + 1)
    for i in range(2, r + 1):
        if not is_comp[i]:
            primes.append(i)
            mu[i] = -1
        for q in primes:
            if i * q > r:
                break
            is_comp[i * q] = 1
            if i % q == 0:
                mu[i * q] = 0
                break
            mu[i * q] = -mu[i]
    total = 0
    g = 1
    while 3 * g * g <= p:
        if mu[g]:
            total += mu[g] * _a_all(p // (g * g))
        g += 1
    return total


if __name__ == "__main__":
    # Given: 861805 geometric triangles with perimeter <= 10^6.
    assert count_geometric_triangles(10**6) == 861805
    print(count_geometric_triangles(25 * 10**12))  # 41791929448408
