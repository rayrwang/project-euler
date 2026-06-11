import numba
import numpy as np

P = 1_000_000_007
INV2 = pow(2, P - 2, P)

# A castle is uniquely determined by its column heights a_1..a_w in [1, h]
# (occupancy is downward closed, and blocks are the maximal runs per row).
# Its block count is B = a_1 + sum_c max(0, a_c - a_{c-1}).
# Let S(m, w) = sum over [1,m]^w of (-1)^B.  Then
#   #(B even, max <= m) = (m^w + S(m, w)) / 2,
#   F(w, h) = (h^w - (h-1)^w + S(h, w) - S(h-1, w)) / 2.


@numba.jit(cache=True)
def s_dp(m: int, w: int) -> int:
    """S(m, w) mod P in O(w m) via suffix sums and alternating prefix sums."""
    v = np.empty(m, dtype=np.int64)
    for a in range(1, m + 1):
        v[a - 1] = P - 1 if a % 2 == 1 else 1
    suf = np.empty(m + 1, dtype=np.int64)
    nv = np.empty(m, dtype=np.int64)
    for _ in range(w - 1):
        suf[m] = 0
        for i in range(m - 1, -1, -1):
            suf[i] = (suf[i + 1] + v[i]) % P
        altpre = 0  # sum_{a < b} (-1)^a v[a]
        for b in range(1, m + 1):
            sgn = P - 1 if b % 2 == 1 else 1
            nv[b - 1] = (suf[b - 1] + sgn * altpre) % P
            altpre = (altpre + sgn * v[b - 1]) % P
        v, nv = nv, v
    total = 0
    for i in range(m):
        total = (total + v[i]) % P
    return total


@numba.jit(cache=True)
def mat_mul(a, b):
    n = a.shape[0]
    c = np.zeros((n, n), dtype=np.int64)
    for i in range(n):
        for k in range(n):
            if a[i, k]:
                aik = a[i, k]
                for j in range(n):
                    c[i, j] = (c[i, j] + aik * b[k, j]) % P
    return c


@numba.jit(cache=True)
def s_matpow(m: int, w: int) -> int:
    """S(m, w) mod P for huge w via the m x m signed transfer matrix."""
    t = np.empty((m, m), dtype=np.int64)
    for b in range(1, m + 1):
        for a in range(1, m + 1):
            if a >= b:
                t[b - 1, a - 1] = 1
            else:
                t[b - 1, a - 1] = P - 1 if (b - a) % 2 == 1 else 1
    v = np.empty(m, dtype=np.int64)
    for a in range(1, m + 1):
        v[a - 1] = P - 1 if a % 2 == 1 else 1
    e = w - 1
    res = np.eye(m, dtype=np.int64)
    while e > 0:
        if e & 1:
            res = mat_mul(res, t)
        t = mat_mul(t, t)
        e >>= 1
    total = 0
    for b in range(m):
        row = 0
        for a in range(m):
            row = (row + res[b, a] * v[a]) % P
        total = (total + row) % P
    return total


def lagrange_eval(xs: list[int], ys: list[int], x: int) -> int:
    n = len(xs)
    pre = [1] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] * ((x - xs[i]) % P) % P
    suf = [1] * (n + 1)
    for i in range(n - 1, -1, -1):
        suf[i] = suf[i + 1] * ((x - xs[i]) % P) % P
    total = 0
    for i in range(n):
        den = 1
        for j in range(n):
            if j != i:
                den = den * ((xs[i] - xs[j]) % P) % P
        total = (total + ys[i] * pre[i] % P * suf[i + 1] % P * pow(den, P - 2, P)) % P
    return total


def f_castle(w: int, h: int, s_func) -> int:
    val = (pow(h, w, P) - pow(h - 1, w, P) + s_func(h, w) - s_func(h - 1, w)) % P
    return val * INV2 % P


def f_tall(w: int, h: int) -> int:
    """F(w, h) for small w and huge h: S(m, w) is quasi-polynomial in m
    with period 2, degree about w, so interpolate even/odd samples."""
    n_samples = w + 20
    samples = {m: s_dp(m, w) for m in range(1, 2 * n_samples + 1)}
    even_xs = list(range(2, 2 * n_samples + 1, 2))
    odd_xs = list(range(1, 2 * n_samples, 2))
    # Held-out verification of the quasi-polynomial degree bound.
    for xs in (even_xs, odd_xs):
        fit, held = xs[:-3], xs[-3:]
        ys = [samples[m] for m in fit]
        assert all(lagrange_eval(fit, ys, m) == samples[m] for m in held)

    def s_interp(m: int, _w: int) -> int:
        xs = even_xs if m % 2 == 0 else odd_xs
        return lagrange_eval(xs, [samples[x] for x in xs], m)

    return f_castle(w, h, s_interp)


if __name__ == "__main__":
    s_py = lambda h, w: s_dp(h, w)  # noqa: E731
    assert f_castle(4, 2, s_py) == 10
    assert f_castle(13, 10, s_py) == 3729050610636 % P
    assert f_castle(10, 13, s_py) == 37959702514 % P
    assert f_castle(100, 100, s_py) == 841913936
    assert s_matpow(50, 37) == s_dp(50, 37)
    assert f_tall(9, 23) == f_castle(9, 23, s_py)

    a = f_castle(10**12, 100, lambda h, w: s_matpow(h, w))
    b = f_castle(10000, 10000, s_py)
    c = f_tall(100, 10**12)
    print((a + b + c) % P)  # 749485217
