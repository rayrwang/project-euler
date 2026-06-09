import numba
import numpy as np

# Largest empty convex polygon ("convex hole") among 500 pseudo-random
# points. Every convex hole is counted once via its lexicographically (y, x)
# smallest vertex b: all other vertices are lex-above b, so their angles
# around b span less than 180 degrees and the polygon is a fan of triangles
# (b, v_t, v_(t+1)) in angular order. The hole is empty iff every fan
# triangle has no given point strictly inside (interior points only; points
# on the boundary do not invalidate a hole), and convex iff each turn
# v_(t-1) -> v_t -> v_(t+1) is a strict left turn.
#
# Per b: sort candidates by angle (ties by distance), precompute the
# strictly-empty triangle pairs E[i, j], then DP
#     f[i, j] = area2(b, q_i, q_j) + max over k (E[k, i], left turn) f[k, i].
# The maximum f over all pairs and bases, halved, is the answer (verified
# against exhaustive subset search on the first 8, 10, 12 and 14 points).


@numba.njit(cache=True)
def _solve(xs: np.ndarray, ys: np.ndarray) -> int:
    n = len(xs)
    bests = np.zeros(n, dtype=np.int64)
    for bi in range(n):
        bx, by = xs[bi], ys[bi]
        # candidates lex-above b
        cx = np.empty(n, dtype=np.int64)
        cy = np.empty(n, dtype=np.int64)
        m = 0
        for i in range(n):
            if (ys[i] > by) or (ys[i] == by and xs[i] > bx):
                cx[m] = xs[i] - bx
                cy[m] = ys[i] - by
                m += 1
        if m < 2:
            continue
        ang = np.arctan2(cy[:m].astype(np.float64), cx[:m].astype(np.float64))
        order = np.argsort(ang)
        qx = cx[:m][order].copy()
        qy = cy[:m][order].copy()
        # fix collinear-with-b ties: order by distance
        for i in range(m - 1):
            j = i + 1
            while j < m and qx[i] * qy[j] - qy[i] * qx[j] == 0:
                j += 1
            if j - i > 1:
                for a in range(i, j):
                    for c in range(a + 1, j):
                        if (
                            qx[a] * qx[a] + qy[a] * qy[a]
                            > qx[c] * qx[c] + qy[c] * qy[c]
                        ):
                            qx[a], qx[c] = qx[c], qx[a]
                            qy[a], qy[c] = qy[c], qy[a]
        # strictly-empty fan triangles
        empty = np.zeros((m, m), dtype=np.bool_)
        for i in range(m):
            for j in range(i + 1, m):
                ok = True
                # chord q_i -> q_j; b (origin) side sign
                ax, ay = qx[i], qy[i]
                dx, dy = qx[j] - ax, qy[j] - ay
                sb = dx * (-ay) - dy * (-ax)  # cross(d, b - q_i)
                for k in range(i + 1, j):
                    # strict wedge: cross(q_i, q_k) > 0 and cross(q_j, q_k) < 0
                    if (
                        qx[i] * qy[k] - qy[i] * qx[k] > 0
                        and qx[j] * qy[k] - qy[j] * qx[k] < 0
                    ):
                        ck = dx * (qy[k] - ay) - dy * (qx[k] - ax)
                        if ck != 0 and (ck > 0) == (sb > 0):
                            ok = False
                            break
                empty[i, j] = ok
        f = np.zeros((m, m), dtype=np.int64)
        best = 0
        for j in range(m):
            for i in range(j):
                if not empty[i, j]:
                    continue
                tri = qx[i] * qy[j] - qy[i] * qx[j]  # 2x fan triangle area
                bv = tri
                for k in range(i):
                    if empty[k, i] and f[k, i] > 0:
                        turn = (qx[i] - qx[k]) * (qy[j] - qy[i]) - (qy[i] - qy[k]) * (
                            qx[j] - qx[i]
                        )
                        if turn > 0 and f[k, i] + tri > bv:
                            bv = f[k, i] + tri
                f[i, j] = bv
                if bv > best:
                    best = bv
        bests[bi] = best
    return bests.max()


def solve(n: int = 500) -> str:
    s = 290797
    vals = []
    for _ in range(2 * n):
        s = s * s % 50515093
        vals.append(s % 2000 - 1000)
    xs = np.array(vals[0::2], dtype=np.int64)
    ys = np.array(vals[1::2], dtype=np.int64)
    area2 = int(_solve(xs, ys))
    return f"{area2 / 2:.1f}"


if __name__ == "__main__":
    print(solve())  # 104924.0
