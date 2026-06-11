import numba
import numpy as np

M = 50515093

@numba.njit
def _update(cnt, lazy, length, node, lo, hi, left, right, shift):
    """Rotate (add `shift` hours to) the coverage of y-leaves [left, right)
    in the subtree `node` spanning leaves [lo, hi)."""
    if right <= lo or hi <= left:
        return
    if left <= lo and hi <= right:
        tmp = np.empty(12, dtype=np.int64)
        for h in range(12):
            tmp[(h + shift) % 12] = cnt[node, h]
        for h in range(12):
            cnt[node, h] = tmp[h]
        lazy[node] = (lazy[node] + shift) % 12
        return
    mid = (lo + hi) // 2
    s = lazy[node]
    if s:
        _update(cnt, lazy, length, 2 * node, lo, mid, lo, mid, s)
        _update(cnt, lazy, length, 2 * node + 1, mid, hi, mid, hi, s)
        lazy[node] = 0
    _update(cnt, lazy, length, 2 * node, lo, mid, left, right, shift)
    _update(cnt, lazy, length, 2 * node + 1, mid, hi, left, right, shift)
    for h in range(12):
        cnt[node, h] = cnt[2 * node, h] + cnt[2 * node + 1, h]

@numba.njit
def C(steps):
    """Sum of the hours shown after `steps` rectangle updates.

    The hour of a clock depends only on its update count mod 12 (count 0
    and count 12 both show 12), so a sweep over compressed x-intervals
    drives a segment tree over compressed y-intervals whose nodes hold,
    per residue class mod 12, the total y-length in that class; a
    rectangle becomes +1 on its y-range at its left edge and -1 just past
    its right edge, and each x-strip contributes
    (strip width) * sum_h length[h] * hour(h).
    """
    s = np.empty(4 * steps, dtype=np.int64)
    v = 290797
    for i in range(4 * steps):
        s[i] = v
        v = v * v % M
    x1 = np.minimum(s[0::4], s[1::4])
    x2 = np.maximum(s[0::4], s[1::4])
    y1 = np.minimum(s[2::4], s[3::4])
    y2 = np.maximum(s[2::4], s[3::4])

    ys = np.unique(np.concatenate((y1, y2 + 1, np.array([0, M], dtype=np.int64))))
    nleaves = len(ys) - 1
    size = 1
    while size < nleaves:
        size *= 2
    cnt = np.zeros((2 * size, 12), dtype=np.int64)
    lazy = np.zeros(2 * size, dtype=np.int64)
    length = ys[1:] - ys[:-1]
    for i in range(nleaves):
        cnt[size + i, 0] = length[i]
    for node in range(size - 1, 0, -1):
        for h in range(12):
            cnt[node, h] = cnt[2 * node, h] + cnt[2 * node + 1, h]

    # x-sweep events: (x, y_left_leaf, y_right_leaf, shift)
    ev_x = np.concatenate((x1, x2 + 1))
    ev_l = np.concatenate((np.searchsorted(ys, y1), np.searchsorted(ys, y1)))
    ev_r = np.concatenate((np.searchsorted(ys, y2 + 1), np.searchsorted(ys, y2 + 1)))
    ev_s = np.concatenate(
        (np.full(steps, 1, dtype=np.int64), np.full(steps, 11, dtype=np.int64))
    )
    order = np.argsort(ev_x, kind="mergesort")

    total = 0
    prev_x = 0
    i = 0
    n_ev = 2 * steps
    while i <= n_ev:
        cur_x = ev_x[order[i]] if i < n_ev else M
        if cur_x > prev_x:
            strip = cur_x - prev_x
            row = 0
            for h in range(12):
                row += cnt[1, h] * (12 if h == 0 else h)
            total += strip * row
            prev_x = cur_x
        if i == n_ev:
            break
        e = order[i]
        _update(cnt, lazy, length, 1, 0, size, ev_l[e], ev_r[e], ev_s[e])
        i += 1
    return total

if __name__ == "__main__":
    assert C(0) == 30621295449583788
    assert C(1) == 30613048345941659
    assert C(10) == 21808930308198471
    assert C(100) == 16190667393984172
    print(C(10**5))  # 16585056588495119
