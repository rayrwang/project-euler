from math import sqrt

import numba
import numpy as np

# With the circumcentre at the origin, the orthocentre is H = A + B + C, so
# the vertices are lattice points on a common circle x^2 + y^2 = N with
# A + B + C = (5, 0). Fix the vertex A = (a, b): then B + C = S = (5-a, -b)
# and B - C is perpendicular to S (equal radii), so B - C = j (-s2, s1) / g
# with g = gcd(|5-a|, |b|) and sigma = S / g primitive. Writing
# q = |sigma|^2, the circle condition |S|^2 + |B-C|^2 = 4N gives
#     j^2 = (4N - g^2 q) / q,
# and since N = 25 - 10 g s1 + g^2 q, divisibility q | (4N - g^2 q) is
# exactly q | (40 g s1 - 100). In particular q <= 20 |5 - 2 g s1|, so
# |sigma| <= 40 g + 3: enumerating pairs (g, sigma) with that cap (plus
# g |sigma| <= R_max + 5) costs only ~10^8 cheap steps even though the disk
# holds ~10^9 lattice points. Every side has length sqrt(3N + 10 a' - 25)
# (a' the opposite vertex's x), so triangles are near-equilateral and
# perimeter <= 10^5 bounds R <= 10^5 / (3 sqrt 3) + 2. Each valid (g, sigma)
# yields B, C = (S +/- D)/2 (parity permitting); each triangle appears once
# per vertex, deduplicated by its sorted vertex key. Verified against direct
# triple search for perimeter <= 50 (9 triangles, sum 291.0089) and <= 500
# (27 triangles).


@numba.njit(cache=True)
def _gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


@numba.njit(cache=True)
def _enumerate(p_limit: float, r_max: int, out: np.ndarray) -> int:
    cnt = 0
    for g in range(1, r_max + 6):
        cap = (r_max + 5) // g + 1
        sig_max = 40 * g + 12
        if cap < sig_max:
            sig_max = cap
        if sig_max < 1:
            break
        for s1 in range(-sig_max, sig_max + 1):
            for s2 in range(-sig_max, sig_max + 1):
                q = s1 * s1 + s2 * s2
                if q == 0 or q > sig_max * sig_max:
                    continue
                if _gcd(abs(s1), abs(s2)) != 1:
                    continue
                if (40 * g * s1 - 100) % q != 0:
                    continue
                a = 5 - g * s1
                b = -g * s2
                n = a * a + b * b
                t = 4 * n - g * g * q
                if t <= 0:
                    continue
                j2 = t // q
                j = int(np.sqrt(j2))
                while j * j > j2:
                    j -= 1
                while (j + 1) * (j + 1) <= j2:
                    j += 1
                if j * j != j2 or j == 0:
                    continue
                sx, sy = g * s1, g * s2
                dx, dy = -j * s2, j * s1
                if (sx + dx) % 2 or (sy + dy) % 2:
                    continue
                bx, by = (sx + dx) // 2, (sy + dy) // 2
                cx, cy = (sx - dx) // 2, (sy - dy) // 2
                if (bx == a and by == b) or (cx == a and cy == b):
                    continue
                per = (
                    np.sqrt((a - bx) ** 2 + (b - by) ** 2)
                    + np.sqrt((a - cx) ** 2 + (b - cy) ** 2)
                    + np.sqrt((bx - cx) ** 2 + (by - cy) ** 2)
                )
                if per <= p_limit:
                    out[cnt, 0] = a
                    out[cnt, 1] = b
                    out[cnt, 2] = bx
                    out[cnt, 3] = by
                    out[cnt, 4] = cx
                    out[cnt, 5] = cy
                    cnt += 1
    return cnt


def solve(p_limit: float = 100_000.0) -> str:
    r_max = int(p_limit / (3 * sqrt(3))) + 10
    out = np.zeros((200_000, 6), dtype=np.int64)
    cnt = _enumerate(p_limit, r_max, out)
    seen = set()
    total = 0.0
    for row in out[:cnt]:
        a = (int(row[0]), int(row[1]))
        b = (int(row[2]), int(row[3]))
        c = (int(row[4]), int(row[5]))
        key = tuple(sorted([a, b, c]))
        if key in seen:
            continue
        seen.add(key)
        total += (
            sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
            + sqrt((a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2)
            + sqrt((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2)
        )
    return f"{total:.4f}"


if __name__ == "__main__":
    print(solve())  # 2816417.1055
