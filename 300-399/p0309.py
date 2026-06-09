import numba
import numpy as np

from funcs import gcd


@numba.jit(cache=True)
def square_divisors_into(m: int, spf: np.ndarray, buf: np.ndarray) -> int:
    """Fill buf with all divisors of m^2 (m >= 1); return how many there are."""
    buf[0] = 1
    count = 1
    n = m
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        base = count
        pe = 1
        for _ in range(2 * e):  # exponent of p in m^2 is 2e
            pe *= p
            for i in range(base):
                buf[count] = buf[i] * pe
                count += 1
    return count


@numba.jit(cache=True)
def count_for_incidence(w: int, x1_height: int, limit: int,
                        spf: np.ndarray, buf: np.ndarray) -> int:
    """Count valid larger heights X2 for a width w and smaller height X1.

    The crossing height h = X1*X2/(X1+X2) is an integer exactly when
    (X1 + X2) divides X1^2, so X2 = D - X1 for a divisor D of X1^2 with
    D > 2*X1. Each candidate X2 is kept when w^2 + X2^2 is a perfect square
    (a ladder of integer length) below the limit.
    """
    w2 = w * w
    found = 0
    n = square_divisors_into(x1_height, spf, buf)
    for i in range(n):
        d = buf[i]
        if d <= 2 * x1_height:
            continue
        x2_height = d - x1_height
        if x2_height >= limit:  # x2 >= sqrt(w^2 + X2^2) > X2, so X2 must be < limit
            continue
        hyp2 = w2 + x2_height * x2_height
        r = int(hyp2**0.5)
        while r * r > hyp2:
            r -= 1
        while (r + 1) * (r + 1) <= hyp2:
            r += 1
        if r * r == hyp2 and r < limit:
            found += 1
    return found


@numba.jit(cache=True)
def build_spf(n: int) -> np.ndarray:
    spf = np.arange(n, dtype=np.int64)
    i = 2
    while i * i < n:
        if spf[i] == i:
            for j in range(i * i, n, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    return spf


@numba.jit(cache=True)
def solve(limit: int) -> int:
    """Triples (x, y, h) with 0 < x < y < limit and an integer street width.

    Generate every Pythagorean triple with hypotenuse < limit. Each triple
    {p, q, c} supplies two ladder/width incidences: width p with wall height q,
    and width q with wall height p. For each incidence the partner height that
    makes the crossing integral is found from the divisors of the height's
    square.
    """
    spf = build_spf(limit)
    buf = np.empty(1 << 14, dtype=np.int64)
    count = 0
    m = 2
    while m * m + 1 < limit:
        for n in range(1, m):
            if (m - n) % 2 == 1 and gcd(m, n) == 1:
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                if c >= limit:
                    continue
                k = 1
                while k * c < limit:
                    leg1 = k * a
                    leg2 = k * b
                    # incidence: width leg1, wall height leg2 (and vice versa)
                    count += count_for_incidence(leg1, leg2, limit, spf, buf)
                    count += count_for_incidence(leg2, leg1, limit, spf, buf)
                    k += 1
        m += 1
    return count


if __name__ == "__main__":
    assert solve(200) == 5
    assert solve(1600) == 146
    print(solve(1_000_000))  # 210139
