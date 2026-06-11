from collections import defaultdict
from functools import lru_cache

# Base beta = i - 1 digits: d = (a + b) mod 2, then z <- (z - d) / beta.
# Two digits per "bit level": d0 = (a + b) mod 2, d1 = b mod 2, and
#   (a, b) <- (-(b - d1)/2, (a - d0 + d1)/2),
# so each step consumes one low bit of each coordinate and SWAPS which
# original bit-stream feeds which coordinate, negating one of them.
# Since beta^2 = -2i, (beta^(2u)) = 2^u Z[i]: digit d_j depends only on
# (a mod 2^u, b mod 2^u) with u = ceil((j+1)/2).  Summing f over the box
# [-L, L]^2 therefore reduces, level by level, to a DP over the bits of the
# two residues, weighted by how often each residue occurs in [-L, L]:
#   n(r) = q + [r' < ell],  r' = (r - (-L)) mod 2^u,
# with q, ell = divmod(2L + 1, 2^u).  The DP state holds the two digit
# carries (in [-2, 2]), an addition carry per stream (adding alpha = -L mod
# 2^u to the free residue bits), and an LSB-first comparison bit per stream;
# the coordinate signs follow a fixed period-4 cycle.

SIGN_CYCLE = ((1, 1), (-1, 1), (-1, -1), (1, -1))


def b_total(limit: int) -> int:
    umax = 4
    while (1 << (umax // 2)) <= 4 * limit + 4:
        umax += 1
    total = 0
    for u in range(1, umax + 1):
        q, ell = divmod(2 * limit + 1, 1 << u)
        alpha = (-limit) % (1 << u)
        c = ell - 1  # weight bonus iff free residue bits r' satisfy r' <= c
        dp = {(0, 0, 0, 0, 1, 1): 1}  # (c_a, c_b, car_a, car_b, cmp_a, cmp_b)
        for t in range(u):
            s_a, s_b = SIGN_CYCLE[t % 4]
            ab = (alpha >> t) & 1
            cbit = (c >> t) & 1 if ell > 0 else 0
            last = t == u - 1
            ndp: dict = defaultdict(int)
            for (ca, cb, car_a, car_b, cmp_a, cmp_b), cnt in dp.items():
                for xb in (0, 1):
                    x = xb + ab + car_a
                    x0, ncar_x = x & 1, x >> 1
                    ncmp_x = 1 if (xb < cbit or (xb == cbit and cmp_a)) else 0
                    for yb in (0, 1):
                        y = yb + ab + car_b
                        y0, ncar_y = y & 1, y >> 1
                        ncmp_y = 1 if (yb < cbit or (yb == cbit and cmp_b)) else 0
                        d1 = (y0 + cb) & 1
                        d0 = (x0 + ca + y0 + cb) & 1
                        nca = -(s_b * y0 + cb - d1) // 2
                        ncb = (s_a * x0 + ca - d0 + d1) // 2
                        if last:  # digits d_{2u-2} = d0 and d_{2u-1} = d1
                            wx = q + (ncmp_x if ell > 0 else 0)
                            wy = q + (ncmp_y if ell > 0 else 0)
                            total += (d0 + d1) * cnt * wx * wy
                        else:  # streams swap coordinates
                            key = (nca, ncb, ncar_y, ncar_x, ncmp_y, ncmp_x)
                            ndp[key] += cnt
            dp = ndp
    return total


@lru_cache(maxsize=None)
def f(a: int, b: int) -> int:
    if a == 0 and b == 0:
        return 0
    d = (a + b) % 2
    return d + f((b - a + d) // 2, (d - a - b) // 2)


def b_brute(limit: int) -> int:
    return sum(
        f(a, b)
        for a in range(-limit, limit + 1)
        for b in range(-limit, limit + 1)
    )


if __name__ == "__main__":
    assert f(11, 24) == 9
    assert f(24, -11) == 7
    for limit in (1, 2, 5, 17, 37, 100):
        assert b_total(limit) == b_brute(limit)
    assert b_total(500) == 10795060
    print(b_total(10**15) % 1_000_000_007)  # 891874596
