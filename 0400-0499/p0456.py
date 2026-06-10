import numba
import numpy as np

@numba.jit(cache=True)
def gen_points(n: int):
    xs = np.empty(n, dtype=np.int64)
    ys = np.empty(n, dtype=np.int64)
    xv = 1
    yv = 1
    for k in range(n):
        xv = xv * 1248 % 32323
        yv = yv * 8421 % 30103
        xs[k] = xv - 16161
        ys[k] = yv - 15051
    return xs, ys

@numba.jit(cache=True)
def gcd64(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

@numba.jit(cache=True)
def c3(x: int) -> int:
    return x * (x - 1) * (x - 2) // 6 if x >= 3 else 0

@numba.jit(cache=True)
def count_from_blocks(dx: np.ndarray, dy: np.ndarray, sz: np.ndarray,
                      n: int) -> int:
    """B + correction over the circular list of direction blocks.

    Every triple not strictly containing the origin spans a minimal closed
    arc of length <= pi; its leader is the minimal-index point at the arc
    start. From a leader in block b, the companions lie in the open arc
    (theta_b, theta_b + pi) — the cross > 0 blocks, W_strict points — or
    at the antipodal direction, or share b's direction with larger index.
    Hockey-sticking over the leader's rank inside its own block gives
    sum_i C(c_i, 2) = C(W + s, 3) - C(W, 3) per block. Triples on a full
    line through the origin that use both rays are counted once per ray,
    so C(r1 + r2, 3) - C(r1, 3) - C(r2, 3) is subtracted once per line.
    """
    m = len(sz)
    total = 0
    e = 0  # window end pointer over the doubled circular list
    run = 0  # points in blocks (b, e) with cross > 0
    for b in range(m):
        if e < b + 1:
            e = b + 1
            run = 0
        while e < b + m:
            i = e % m
            cr = dx[b] * dy[i] - dy[b] * dx[i]
            if cr > 0:
                run += sz[i]
                e += 1
            else:
                break
        w = run
        # antipodal block immediately after the cross>0 run, if present
        if e < b + m:
            i = e % m
            cr = dx[b] * dy[i] - dy[b] * dx[i]
            dt = dx[b] * dx[i] + dy[b] * dy[i]
            if cr == 0 and dt < 0:
                w += sz[i]
                # subtract the both-rays line triples once per line:
                # do it when b is the canonical (upper-half) block
                if dy[b] > 0 or (dy[b] == 0 and dx[b] > 0):
                    r1 = sz[b]
                    r2 = sz[i]
                    total -= c3(r1 + r2) - c3(r1) - c3(r2)
        total += c3(w + sz[b]) - c3(w)
        run -= sz[(b + 1) % m] if e > b + 1 else 0
        # (when the window was empty the pointer reset handles run)
    return total

def origin_triangles(n: int) -> int:
    """C(n): triangles on the first n points with the origin strictly
    inside, as C(n, 3) minus the closed-half-plane triples."""
    xs, ys = gen_points(n)
    g = np.gcd(np.abs(xs), np.abs(ys))
    px = xs // g
    py = ys // g
    ang = np.arctan2(py.astype(np.float64), px.astype(np.float64))
    order = np.lexsort((py, px, ang))
    px_s = px[order]
    py_s = py[order]
    # blocks of identical primitive direction (exact integer comparison)
    new_block = np.empty(n, dtype=bool)
    new_block[0] = True
    new_block[1:] = (px_s[1:] != px_s[:-1]) | (py_s[1:] != py_s[:-1])
    starts = np.flatnonzero(new_block)
    sz = np.diff(np.append(starts, n)).astype(np.int64)
    dx = px_s[starts].astype(np.int64)
    dy = py_s[starts].astype(np.int64)
    bad = count_from_blocks(dx, dy, sz, n)
    return c3_py(n) - bad

def c3_py(x: int) -> int:
    return x * (x - 1) * (x - 2) // 6 if x >= 3 else 0

def brute(n: int) -> int:
    xs, ys = gen_points(n)
    pts = list(zip(xs.tolist(), ys.tolist()))
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                (x1, y1), (x2, y2), (x3, y3) = pts[i], pts[j], pts[k]
                c1 = x1 * y2 - y1 * x2
                c2 = x2 * y3 - y2 * x3
                c3v = x3 * y1 - y3 * x1
                if (c1 > 0 and c2 > 0 and c3v > 0) or (
                        c1 < 0 and c2 < 0 and c3v < 0):
                    cnt += 1
    return cnt

if __name__ == "__main__":
    assert origin_triangles(8) == brute(8) == 20
    for m in (30, 80, 150):
        assert origin_triangles(m) == brute(m), m
    assert origin_triangles(600) == 8950634  # given
    assert origin_triangles(40_000) == 2666610948988  # given
    print(origin_triangles(2_000_000))  # 333333208685971546
