"""Project Euler 949: Left vs Right II.

Each word is a partizan scoring game: Left trims the left side, Right the right
side, and the surviving single letter scores +1 for L, -1 for R. A turn in the
k-word game may trim any non-empty subset of the words (a selective compound),
and Right wins the whole position when the final score sum is negative.

The single-word game is summarised by two stops, u(w) (Left moves first) and
d(w) (Right moves first), built bottom-up over substrings: a left move turns w
into a proper suffix, a right move into a proper prefix, so

    u_raw(w) = max_{s proper suffix} d(s),   d_raw(w) = min_{p proper prefix} u(p).

If u_raw < d_raw the position is "cold": neither player wants to move, so it
behaves as the simplest dyadic number strictly between the two bounds, and we
set u(w) = d(w) = that number (flagging the word cold). Otherwise it is hot and
we keep u(w) = u_raw, d(w) = d_raw, scoring it by its Left stop u(w). Storing
the raw maxima/minima incrementally (M = running max of d over suffixes,
P = running min of u over prefixes) makes each word O(1); scaling every value by
2**n keeps the dyadics exact integers.

In the selective compound the surviving score of a tuple is Sigma u(w): Right
wins exactly when Sigma u(w) < 0, plus the boundary case Sigma u(w) = 0 in which
*every* component is cold (a hot component lets Left tip a zero sum upward).
Counting reduces to histograms of u over the 2**n words: with a = floor(k/2),
b = k - a, let D_a, D_b be the a- and b-fold convolutions of the full histogram
and C_a, C_b those of the cold-only histogram. Then

    G(n, k) = #{tuples : Sigma u < 0} + #{all-cold tuples : Sigma u = 0}
            = sum_{x + y < 0} D_a(x) D_b(y) + sum_x C_a(x) C_b(-x)  (mod p).

Verified against the given G(2, 3) = 14, G(4, 3) = 496 and
G(8, 5) = 26359197010.
"""
import bisect

import numpy as np

MOD = 1001001011


def _simplest_between(lo: np.ndarray, hi: np.ndarray, scale: int, n: int) -> np.ndarray:
    """Simplest dyadic (scaled by `scale`) strictly inside each open (lo, hi)."""
    res = np.zeros_like(lo)
    straddle = (lo < 0) & (hi > 0)  # an interval containing 0 -> 0 is simplest

    def fill_positive(low: np.ndarray, high: np.ndarray, mask: np.ndarray) -> np.ndarray:
        out = np.zeros(low.shape, dtype=np.int64)
        todo = mask.copy()
        m = 0
        while todo.any() and m <= n:
            step = scale >> m
            if step == 0:
                break
            cand = (low // step + 1) * step  # smallest multiple of step above low
            ok = todo & (cand < high)
            out[ok] = cand[ok]
            todo &= ~ok
            m += 1
        return out

    pos = (~straddle) & (lo >= 0)
    neg = (~straddle) & (hi <= 0)
    if pos.any():
        res[pos] = fill_positive(lo, hi, pos)[pos]
    if neg.any():  # mirror onto the positive side
        res[neg] = -fill_positive(-hi, -lo, neg)[neg]
    return res


def layer_histograms(n: int) -> tuple[dict[int, int], dict[int, int]]:
    """Histograms of the Left stop u(w) over all length-n words: (all, cold-only)."""
    scale = 1 << n
    u = np.array([scale, -scale], dtype=np.int64)  # length 1: L -> +1, R -> -1
    d = u.copy()
    max_d_suffix = d.copy()  # M: max of d over non-empty suffixes
    min_u_prefix = u.copy()  # P: min of u over non-empty prefixes
    cold = np.array([False, False])

    for length in range(2, n + 1):
        idx = np.arange(1 << length, dtype=np.int64)
        suffix = idx & ((1 << (length - 1)) - 1)  # drop leading letter
        prefix = idx >> 1  # drop trailing letter
        u_raw = max_d_suffix[suffix]
        d_raw = min_u_prefix[prefix]

        cold = u_raw < d_raw
        u = np.where(cold, 0, u_raw).astype(np.int64)
        d = np.where(cold, 0, d_raw).astype(np.int64)
        if cold.any():
            mid = _simplest_between(u_raw[cold], d_raw[cold], scale, n)
            u[cold] = mid
            d[cold] = mid

        max_d_suffix = np.maximum(d, u_raw)
        min_u_prefix = np.minimum(u, d_raw)

    all_hist: dict[int, int] = {}
    vals, counts = np.unique(u, return_counts=True)
    for v, c in zip(vals.tolist(), counts.tolist()):
        all_hist[v] = c % MOD
    cold_hist: dict[int, int] = {}
    if cold.any():
        vals, counts = np.unique(u[cold], return_counts=True)
        for v, c in zip(vals.tolist(), counts.tolist()):
            cold_hist[v] = c % MOD
    return all_hist, cold_hist


def _convolve(a: dict[int, int], b: dict[int, int]) -> dict[int, int]:
    out: dict[int, int] = {}
    for x, cx in a.items():
        for y, cy in b.items():
            s = x + y
            out[s] = (out.get(s, 0) + cx * cy) % MOD
    return out


def _convolve_power(hist: dict[int, int], e: int) -> dict[int, int]:
    result: dict[int, int] = {0: 1}
    base = dict(hist)
    while e:
        if e & 1:
            result = _convolve(result, base)
        e >>= 1
        if e:
            base = _convolve(base, base)
    return result


def count_right_wins(n: int, k: int) -> int:
    """G(n, k): ordered k-tuples of length-n words for which Right wins (mod p)."""
    all_hist, cold_hist = layer_histograms(n)
    a, b = k // 2, k - k // 2
    d_a, d_b = _convolve_power(all_hist, a), _convolve_power(all_hist, b)

    # Tuples with total Left stop strictly negative.
    ys = sorted(d_b)
    prefix = [0]
    for y in ys:
        prefix.append((prefix[-1] + d_b[y]) % MOD)
    negative = 0
    for x, cx in d_a.items():
        j = bisect.bisect_left(ys, -x)  # count y with x + y < 0
        negative = (negative + cx * prefix[j]) % MOD

    # All-cold tuples with total Left stop exactly zero.
    c_a, c_b = _convolve_power(cold_hist, a), _convolve_power(cold_hist, b)
    zero = 0
    for x, cx in c_a.items():
        cy = c_b.get(-x)
        if cy is not None:
            zero = (zero + cx * cy) % MOD

    return (negative + zero) % MOD


if __name__ == "__main__":
    assert count_right_wins(2, 3) == 14
    assert count_right_wins(4, 3) == 496
    assert count_right_wins(8, 5) == 26359197010 % MOD
    print(count_right_wins(20, 7))  # 726010935
