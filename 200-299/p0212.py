import numpy as np
from numba import njit


def _gen_boxes(n: int) -> np.ndarray:
    # Lagged Fibonacci generator; box n is [x0,x1] x [y0,y1] x [z0,z1].
    size = max(56, 6 * n + 1)
    s = np.empty(size, dtype=np.int64)
    for k in range(1, 56):
        s[k] = (100003 - 200003 * k + 300007 * k * k * k) % 1000000
    for k in range(56, 6 * n + 1):
        s[k] = (s[k - 24] + s[k - 55]) % 1000000
    boxes = np.empty((n, 6), dtype=np.int64)
    for i in range(1, n + 1):
        x0, y0, z0 = s[6 * i - 5] % 10000, s[6 * i - 4] % 10000, s[6 * i - 3] % 10000
        dx, dy, dz = 1 + s[6 * i - 2] % 399, 1 + s[6 * i - 1] % 399, 1 + s[6 * i] % 399
        boxes[i - 1] = (x0, x0 + dx, y0, y0 + dy, z0, z0 + dz)
    return boxes


@njit(cache=True)
def _seg_update(cnt, cov, ys, node, lo, hi, ql, qr, val):
    # Klee segment tree over compressed y-intervals: range add, cov[1] = covered length.
    if qr < lo or hi < ql:
        return
    if ql <= lo and hi <= qr:
        cnt[node] += val
    else:
        mid = (lo + hi) // 2
        _seg_update(cnt, cov, ys, 2 * node, lo, mid, ql, qr, val)
        _seg_update(cnt, cov, ys, 2 * node + 1, mid + 1, hi, ql, qr, val)
    if cnt[node] > 0:
        cov[node] = ys[hi + 1] - ys[lo]
    elif lo == hi:
        cov[node] = 0
    else:
        cov[node] = cov[2 * node] + cov[2 * node + 1]


@njit(cache=True)
def _volume(boxes: np.ndarray, ys: np.ndarray, yindex: np.ndarray) -> int:
    # Sweep z over distinct boundaries; per slab take the 2D union area of the
    # active boxes (an x-sweep with the y segment tree, which self-clears since
    # every +1 at x0 is matched by a -1 at x1) and multiply by the slab height.
    n = boxes.shape[0]
    zvals = np.empty(2 * n, dtype=np.int64)
    for i in range(n):
        zvals[2 * i] = boxes[i, 4]
        zvals[2 * i + 1] = boxes[i, 5]
    zs = np.unique(zvals)
    m = len(ys)
    cnt = np.zeros(4 * m, dtype=np.int64)
    cov = np.zeros(4 * m, dtype=np.int64)
    active = np.empty(n, dtype=np.int64)
    pos = np.full(n, -1, dtype=np.int64)
    asize = 0
    enter_order = np.argsort(boxes[:, 4])
    exit_order = np.argsort(boxes[:, 5])
    ep = xp = 0
    nleaf = m - 1
    ev_x = np.empty(2 * n, dtype=np.int64)
    ev_lb = np.empty(2 * n, dtype=np.int64)
    ev_ub = np.empty(2 * n, dtype=np.int64)
    ev_v = np.empty(2 * n, dtype=np.int64)
    total = 0
    for si in range(len(zs) - 1):
        zlo, zhi = zs[si], zs[si + 1]
        while ep < n and boxes[enter_order[ep], 4] == zlo:
            b = enter_order[ep]
            active[asize] = b
            pos[b] = asize
            asize += 1
            ep += 1
        while xp < n and boxes[exit_order[xp], 5] == zlo:
            b = exit_order[xp]
            p = pos[b]
            if p != -1:
                last = active[asize - 1]
                active[p] = last
                pos[last] = p
                asize -= 1
                pos[b] = -1
            xp += 1
        if asize == 0:
            continue
        ne = 0
        for i in range(asize):
            b = active[i]
            lb, ub = yindex[b * 2], yindex[b * 2 + 1] - 1
            ev_x[ne] = boxes[b, 0]
            ev_lb[ne] = lb
            ev_ub[ne] = ub
            ev_v[ne] = 1
            ne += 1
            ev_x[ne] = boxes[b, 1]
            ev_lb[ne] = lb
            ev_ub[ne] = ub
            ev_v[ne] = -1
            ne += 1
        order = np.argsort(ev_x[:ne])
        area = 0
        prevx = 0
        for j in range(ne):
            e = order[j]
            x = ev_x[e]
            if j > 0:
                area += cov[1] * (x - prevx)
            _seg_update(cnt, cov, ys, 1, 0, nleaf - 1, ev_lb[e], ev_ub[e], ev_v[e])
            prevx = x
        total += area * (zhi - zlo)
    return total


def solve(n: int = 50000) -> int:
    boxes = _gen_boxes(n)
    ys = np.unique(np.concatenate((boxes[:, 2], boxes[:, 3]))).astype(np.int64)
    yindex = np.empty(2 * n, dtype=np.int64)
    yindex[0::2] = np.searchsorted(ys, boxes[:, 2])
    yindex[1::2] = np.searchsorted(ys, boxes[:, 3])
    return int(_volume(boxes, ys, yindex))


if __name__ == "__main__":
    print(solve())  # 328968937309
