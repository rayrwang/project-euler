import random

import numba
import numpy as np

# The XOR-product is multiplication in GF(2)[x] (with 2 = x), so the
# equation reads Q(a, b) = a^2 + x a b + b^2 = k over GF(2)[x].  Q is
# preserved by the swap S(a, b) = (b, a) and the involution
# V(a, b) = (a, b xor 2a), since (b + xa)^2 + xa(b + xa) = b^2 + xab in
# characteristic 2; these generate an infinite dihedral group, and the
# composite M = (a, b) -> (b, 2b xor a) walks each orbit as a bi-infinite
# line whose max-coordinate is U-shaped: it strictly decreases under the
# inverse step D(a, b) = (b xor 2a, a) until a valley pair and grows in
# both directions away from it.  Away from the valley the leading terms of
# b^2 and xab must cancel, so deg b grows by one per step while k is fixed;
# valley pairs with k <= 10^6 (19 bits) are therefore tiny and a scan of
# a <= b < 8192 finds every orbit (all valleys lie below 2048, asserted).
# G(N, m) is the total number of line elements with both coordinates at
# most N over all distinct orbits; for symmetric orbits (through a = 0 or
# a = b) the two rays fold onto each other, which collecting each orbit's
# normalised pairs into a set handles automatically.

N = 10**17
M = 10**6


@numba.njit(inline="always")
def clmul(a, b):
    r = np.int64(0)
    while b:
        if b & 1:
            r ^= a
        a <<= 1
        b >>= 1
    return r


@numba.njit(inline="always")
def quad(a, b):
    return clmul(a, a) ^ clmul(clmul(2, a), b) ^ clmul(b, b)


@numba.njit(cache=True)
def valley_pairs(box, m):
    out = []
    for b in range(box):
        for a in range(b + 1):
            if quad(a, b) <= m:
                x, y = a, b
                while True:
                    nx, ny = y ^ (x << 1), x
                    if nx > ny:
                        nx, ny = ny, nx
                    if max(nx, ny) < max(x, y):
                        x, y = nx, ny
                    else:
                        break
                out.append((x, y))
    return out


@numba.njit(cache=True)
def brute_count(n, m):
    c = 0
    for b in range(n + 1):
        for a in range(b + 1):
            if quad(a, b) <= m:
                c += 1
    return c


def orbit_solutions(seed: tuple, n: int) -> set:
    """Normalised pairs on the orbit line through seed with max <= n."""
    if seed == (0, 0):
        return {(0, 0)}
    sols = set()
    for direction in range(2):
        x, y = seed
        if direction:
            x, y = y ^ (x << 1), x  # start one D-step away to avoid repeats
        steps = 0
        while max(x, y) <= n or steps < 8:
            if max(x, y) <= n:
                sols.add((min(x, y), max(x, y)))
            if direction:
                x, y = y ^ (x << 1), x
            else:
                x, y = y, (y << 1) ^ x
            steps += 1
            if steps > 8 and max(x, y) > 4 * n + 16:
                break
    return sols


def canonical(seed: tuple) -> tuple:
    """Lexicographically least normalised pair near the valley (orbit id)."""
    if seed == (0, 0):
        return (0, 0)
    pool = set()
    for direction in range(2):
        x, y = seed
        for _ in range(12):
            pool.add((min(x, y), max(x, y)))
            if direction:
                x, y = y ^ (x << 1), x
            else:
                x, y = y, (y << 1) ^ x
    mm = min(mx for _, mx in pool)
    return min(p for p in pool if p[1] <= 2 * mm + 2)


def count(n: int, m: int, box: int) -> int:
    valleys = set(valley_pairs(box, m))
    assert all(b < box // 4 for _, b in valleys)  # scan window is large enough
    orbits = {canonical(p): p for p in valleys}
    return sum(len(orbit_solutions(p, n)) for p in orbits.values())


if __name__ == "__main__":
    assert clmul(7, 3) == 9  # given example of the XOR-product
    assert quad(3, 6) == 5  # given solution for k = 5
    assert count(1000, 100, 2048) == 398  # given
    rng = random.Random(3)
    for _ in range(20):
        n, m = rng.randint(10, 600), rng.randint(1, 500)
        assert count(n, m, 2048) == brute_count(n, m)
    print(count(N, M, 8192))  # 23707109
