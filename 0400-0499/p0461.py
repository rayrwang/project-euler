from decimal import Decimal, getcontext

import numba
import numpy as np

PI_STR = "3.14159265358979323846264338327950288419716939937510582097"

@numba.jit(cache=True)
def pair_sums(f: np.ndarray, limit: float) -> np.ndarray:
    k = len(f)
    cnt = 0
    for i in range(k):
        if 2 * f[i] > limit:
            break
        j = i
        while j < k and f[i] + f[j] <= limit:
            cnt += 1
            j += 1
    out = np.empty(cnt, dtype=np.float64)
    pos = 0
    for i in range(k):
        if 2 * f[i] > limit:
            break
        j = i
        while j < k and f[i] + f[j] <= limit:
            out[pos] = f[i] + f[j]
            pos += 1
            j += 1
    return out

@numba.jit(cache=True)
def find_pairs(f: np.ndarray, wanted: np.ndarray, limit: float) -> np.ndarray:
    """One sweep recovering some (i, j) with f[i] + f[j] == s bit-exactly
    for every s in `wanted` (sorted)."""
    k = len(f)
    out = np.full((len(wanted), 2), -1, dtype=np.int64)
    for i in range(k):
        if 2 * f[i] > limit:
            break
        j = i
        while j < k and f[i] + f[j] <= limit:
            s = f[i] + f[j]
            pos = np.searchsorted(wanted, s)
            if pos < len(wanted) and wanted[pos] == s and out[pos, 0] < 0:
                out[pos, 0] = i
                out[pos, 1] = j
            j += 1
    return out

@numba.jit(cache=True)
def near_best(p: np.ndarray, target: float, band: float) -> np.ndarray:
    """Two-pointer over sorted pair sums; return candidate (lo, hi) sum
    pairs whose total is within `band` of the best found."""
    lo = 0
    hi = len(p) - 1
    best = 1e18
    cand = np.empty((4096, 2), dtype=np.float64)
    cnt = 0
    while lo <= hi:
        s = p[lo] + p[hi]
        err = abs(s - target)
        if err < best:
            best = err
        if err <= best + band and cnt < 4096:
            cand[cnt, 0] = p[lo]
            cand[cnt, 1] = p[hi]
            cnt += 1
        if s > target:
            hi -= 1
        else:
            lo += 1
    # second pass keeping only those within band of the final best
    out = np.empty((cnt, 2), dtype=np.float64)
    m = 0
    for t in range(cnt):
        if abs(cand[t, 0] + cand[t, 1] - target) <= best + band:
            out[m] = cand[t]
            m += 1
    return out[:m]

def almost_pi(n: int) -> int:
    """g(n) = a^2+b^2+c^2+d^2 minimizing |f_n(a)+f_n(b)+f_n(c)+f_n(d) - pi|
    with f_n(k) = e^{k/n} - 1.

    Meet in the middle on pair sums: all f_a + f_b <= pi (+margin) are
    sorted in place, and a two-pointer finds the closest two-pair total
    to pi. Because the best error at n = 10^4 is ~1e-15, within float64
    noise, every candidate within a small band of the float optimum is
    re-evaluated in 50-digit decimals against a high-precision pi before
    the winner is declared. The (a, b) behind each chosen pair sum is
    recovered by re-scanning for the bit-exact float value.
    """
    getcontext().prec = 60
    pi_d = Decimal(PI_STR)
    kmax = int(n * np.log(1 + np.pi)) + 2
    f = np.expm1(np.arange(kmax + 1, dtype=np.float64) / n)
    limit = float(np.pi) + 1e-9
    p = pair_sums(f, limit)
    p.sort()
    cands = near_best(p, float(np.pi), 3e-13)
    wanted = np.unique(cands.ravel())
    rec = find_pairs(f, wanted, limit)
    lookup = {float(wanted[t]): (int(rec[t, 0]), int(rec[t, 1]))
              for t in range(len(wanted))}
    best_err = Decimal(10)
    best_g = 0
    for s1, s2 in cands:
        a, b = lookup[float(s1)]
        c, d = lookup[float(s2)]
        val = sum((Decimal(int(t)) / n).exp() - 1 for t in (a, b, c, d))
        err = abs(val - pi_d)
        if err < best_err:
            best_err = err
            best_g = a * a + b * b + c * c + d * d
    return best_g

if __name__ == "__main__":
    assert almost_pi(200) == 64658  # given g(200)
    print(almost_pi(10**4))  # 159820276
