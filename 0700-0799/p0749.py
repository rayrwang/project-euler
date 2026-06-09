import numba
import numpy as np

LIMIT = 10**16
MAX_K = 60

@numba.njit(cache=True)
def digit_counts_match(n, counts):
    seen = np.zeros(10, dtype=np.int64)
    while n > 0:
        seen[n % 10] += 1
        n //= 10
    for v in range(10):
        if seen[v] != counts[v]:
            return False
    return True

@numba.njit(cache=True)
def check_multiset(counts, lo, hi, pw, found, idx):
    """Scan exponents k and record any n in [lo, hi] whose digit multiset is
    `counts` and whose k-th digit power sum is n + 1 or n - 1."""
    for k in range(1, MAX_K + 1):
        s = 0
        for v in range(1, 10):
            if counts[v]:
                s += counts[v] * pw[v, k]
        if s > LIMIT + 1:
            break
        for n in (s - 1, s + 1):
            if lo <= n <= hi and digit_counts_match(n, counts):
                found[idx] = n
                idx += 1
        if s == counts[1]:  # digits are all 0/1, so s never grows: stop
            break
    return idx

@numba.njit(cache=True)
def S(max_digits):
    """Sum of near power sum numbers with at most max_digits digits.

    The digit power sum depends only on the multiset of digits, so enumerate
    multisets (about 5.3 million for 16 digits) instead of numbers. For each
    multiset and each exponent k, the only candidates are n = s -+ 1 where s
    is the power sum; accept n when it has this exact multiset. Powers are
    clamped at LIMIT + 2 so sums cannot overflow before the break test.
    """
    cap = LIMIT + 2
    pw = np.zeros((10, MAX_K + 1), dtype=np.int64)
    for v in range(10):
        pw[v, 0] = 1
        for k in range(1, MAX_K + 1):
            prev = pw[v, k - 1]
            pw[v, k] = prev * v if v == 0 or prev <= cap // v else cap
    found = np.zeros(100000, dtype=np.int64)
    idx = 0
    lo = 1
    for d in range(1, max_digits + 1):
        hi = lo * 10 - 1
        # Odometer over counts of digits 1..9 with total <= d; digit 0 takes
        # the remainder.
        counts = np.zeros(10, dtype=np.int64)
        used = 0
        while True:
            counts[0] = d - used
            idx = check_multiset(counts, lo, hi, pw, found, idx)
            counts[0] = 0
            v = 1
            while v <= 9:
                if used < d:
                    counts[v] += 1
                    used += 1
                    break
                used -= counts[v]
                counts[v] = 0
                v += 1
            if v > 9:
                break
        lo *= 10
    # The same n can qualify for several exponents k; count each n once.
    hits = np.unique(found[:idx])
    return hits.sum()

if __name__ == "__main__":
    assert S(2) == 110
    assert S(6) == 2562701
    print(S(16))  # 13459471903176422
