"""Project Euler Problem 691: Long Substring with Many Repetitions.

The string: a_n is the Thue-Morse sequence (parity of popcount), b_n is
the Fibonacci/Beatty word floor((n+1)/phi) - floor(n/phi), and c_n is
their XOR.  floor(n/phi) = floor((sqrt(5) n - n)/2) is computed exactly
with integer square roots (floats are not trusted that close to 5 * 10^6).

A substring occurs at least k times exactly when k suffixes share a prefix,
i.e. when some window of k - 1 consecutive entries of the LCP array (in
suffix-array order) has min at least its length, so

    L(k) = max over windows of width k - 1 of (min LCP),   L(1) = n.

Pipeline, all O(n log n) / O(n):
 1. suffix array by prefix doubling, one stable numpy argsort per round on
    the packed key rank * (n + 2) + next_rank;
 2. LCP array by Kasai's algorithm (numba);
 3. M(w) = max over width-w windows of min, for all w at once: a monotonic
    stack finds for each LCP value the maximal window in which it is the
    minimum, then a suffix maximum fills in narrower widths;
 4. answer = n + sum of the non-zero M(w).

Verified: the eight given L(k, S_n) values for n = 10, 100, 1000, the
given sum 2460 for S_1000, and L against brute-force substring counting
for S_10 and S_100.
"""

import numba
import numpy as np

N = 5_000_000


def build_string(n: int) -> np.ndarray:
    idx = np.arange(n + 1, dtype=np.int64)
    # Thue-Morse: parity of the number of set bits.
    a = idx.copy()
    for shift in (32, 16, 8, 4, 2, 1):
        a ^= a >> shift
    a &= 1
    # floor(m / phi) = (isqrt(5 m^2) - m) // 2, exactly.
    v = 5 * idx * idx
    r = np.sqrt(v.astype(np.float64)).astype(np.int64)
    r = np.where(r * r > v, r - 1, r)
    r = np.where((r + 1) * (r + 1) <= v, r + 1, r)
    fl = (r - idx) >> 1
    b = fl[1:] - fl[:-1]
    return (a[:-1] ^ b).astype(np.int8)


def suffix_array(s: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    n = len(s)
    rank = s.astype(np.int64)
    k = 1
    while True:
        key = rank * (n + 2)
        key[: n - k] += rank[k:] + 1
        sa = np.argsort(key, kind="stable")
        sorted_key = key[sa]
        new = np.empty(n, dtype=np.int64)
        new[sa[0]] = 0
        new[sa[1:]] = np.cumsum(sorted_key[1:] != sorted_key[:-1])
        rank = new
        if rank[sa[-1]] == n - 1:
            return sa, rank
        k *= 2


@numba.jit(cache=True)
def kasai(s: np.ndarray, sa: np.ndarray, rank: np.ndarray) -> np.ndarray:
    n = len(s)
    lcp = np.zeros(n - 1, dtype=np.int64)
    h = 0
    for i in range(n):
        r = rank[i]
        if r > 0:
            j = sa[r - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[r - 1] = h
            if h > 0:
                h -= 1
        else:
            h = 0
    return lcp


@numba.jit(cache=True)
def max_min_per_width(lcp: np.ndarray) -> np.ndarray:
    """best[w] = max over windows of exactly w entries of the window min."""
    m = len(lcp)
    stack = np.empty(m, dtype=np.int64)
    left = np.empty(m, dtype=np.int64)
    right = np.empty(m, dtype=np.int64)
    top = -1
    for i in range(m):
        while top >= 0 and lcp[stack[top]] >= lcp[i]:
            top -= 1
        left[i] = stack[top] if top >= 0 else -1
        top += 1
        stack[top] = i
    top = -1
    for i in range(m - 1, -1, -1):
        while top >= 0 and lcp[stack[top]] > lcp[i]:
            top -= 1
        right[i] = stack[top] if top >= 0 else m
        top += 1
        stack[top] = i
    best = np.zeros(m + 1, dtype=np.int64)
    for i in range(m):
        w = right[i] - left[i] - 1
        if lcp[i] > best[w]:
            best[w] = lcp[i]
    for w in range(m - 1, 0, -1):
        if best[w + 1] > best[w]:
            best[w] = best[w + 1]
    return best


def big_l_all(s: np.ndarray) -> np.ndarray:
    """best[w] = L(w + 1) for w >= 1; L(1) = len(s) handled by caller."""
    sa, rank = suffix_array(s)
    lcp = kasai(s, sa, rank)
    return max_min_per_width(lcp)


def answer(n: int) -> int:
    best = big_l_all(build_string(n))
    return n + int(best.sum())


def big_l_brute(s: str, k: int) -> int:
    for length in range(len(s), 0, -1):
        counts: dict[str, int] = {}
        for i in range(len(s) - length + 1):
            t = s[i : i + length]
            counts[t] = counts.get(t, 0) + 1
        if max(counts.values()) >= k:
            return length
    return 0


if __name__ == "__main__":
    for n, given in ((10, {2: 5, 3: 2}), (100, {2: 14, 4: 6}),
                     (1000, {2: 86, 3: 45, 5: 31})):
        s = build_string(n)
        best = big_l_all(s)
        for k, val in given.items():
            assert best[k - 1] == val, (n, k)
        if n <= 100:
            text = "".join(str(c) for c in s)
            for k in range(2, 12):
                mine = int(best[k - 1]) if k - 1 < len(best) else 0
                assert mine == big_l_brute(text, k)
    assert answer(1000) == 2460
    print(answer(N))  # 11570761
