import numba
import numpy as np

@numba.jit(cache=True)
def max_stations(n: int) -> int:
    """S(n): most stations (2^i mod n, 3^i mod n), 0 <= i <= 2n, on a path
    with non-decreasing x and y.

    The pair sequence is eventually periodic: 2^i mod n has pre-period
    equal to the exponent of 2 in n (at most 20 for n = k^5, k <= 30) and
    likewise for 3, so from index 25 onward it is purely cyclic with period
    at most lambda(n) <= n. Generate pairs until the index-25 pair recurs;
    that window holds every distinct station. Encode (x, y) as x*n + y,
    sort, dedupe, and the answer is the longest non-decreasing subsequence
    of y over points sorted by (x, y) — patience sorting with upper-bound
    binary search.
    """
    if n == 1:
        return 1  # the single station (0, 0)
    pre = 25
    cap = 2 * n + 1 if 2 * n + 1 < n + 32 else n + 32  # count <= pre + period
    keys = np.empty(cap, dtype=np.int64)
    x, y = 1, 1
    x25, y25 = -1, -1
    count = 0
    i = 0
    while i <= 2 * n:
        if i == pre:
            x25, y25 = x, y
        elif i > pre and x == x25 and y == y25:
            break  # period closed; all later pairs repeat
        keys[count] = x * n + y
        count += 1
        x = x * 2 % n
        y = y * 3 % n
        i += 1
    pts = np.sort(keys[:count])
    tails = np.empty(count, dtype=np.int64)
    m = 0
    prev = -1
    for j in range(count):
        key = pts[j]
        if key == prev:
            continue  # duplicate station
        prev = key
        v = key % n  # y coordinate; pts already ordered by (x, y)
        # upper bound: first tail strictly greater than v
        lo, hi = 0, m
        while lo < hi:
            mid = (lo + hi) // 2
            if tails[mid] <= v:
                lo = mid + 1
            else:
                hi = mid
        tails[lo] = v
        if lo == m:
            m += 1
    return m

@numba.jit(cache=True)
def total() -> int:
    s = 0
    for k in range(1, 31):
        s += max_stations(k**5)
    return s

if __name__ == "__main__":
    assert max_stations(22) == 5
    assert max_stations(123) == 14
    assert max_stations(10000) == 48
    print(total())  # 9936352
