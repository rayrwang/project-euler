import numpy as np


def _row_start(n: int) -> int:
    return n * (n - 1) // 2 + 1


def _seg_sieve(lo: int, hi: int) -> np.ndarray:
    size = hi - lo + 1
    sieve = np.ones(size, dtype=bool)
    limit = int(hi**0.5) + 1
    base = np.ones(limit + 1, dtype=bool)
    base[:2] = False
    for i in range(2, int(limit**0.5) + 1):
        if base[i]:
            base[i * i :: i] = False
    for p in np.nonzero(base)[0]:
        start = max(p * p, ((lo + p - 1) // p) * p)
        if start <= hi:
            sieve[start - lo :: p] = False
    return sieve


def _shift(a: np.ndarray, d: int) -> np.ndarray:
    r = np.zeros_like(a)
    if d > 0:
        r[:-d] = a[d:]
    elif d < 0:
        r[-d:] = a[:d]
    else:
        r[:] = a
    return r


def _row_sum(n: int) -> int:
    # Sum of primes in row n that belong to a prime triplet. In the 8-neighbour
    # triangle a prime is in a triplet iff it is a "centre" (>=2 prime
    # neighbours) or it neighbours a centre. Work over rows n-2..n+2.
    lo, hi = _row_start(n - 2), _row_start(n + 2) + (n + 2) - 1
    sieve = _seg_sieve(lo, hi)
    width = n + 3
    prime = np.zeros((5, width), dtype=np.int32)
    for k, r in enumerate(range(n - 2, n + 3)):
        st = _row_start(r) - lo
        prime[k, :r] = sieve[st : st + r]
    blur = np.array([_shift(prime[m], -1) + prime[m] + _shift(prime[m], 1) for m in range(5)])
    centre = np.zeros((5, width), dtype=np.int32)
    for k in (1, 2, 3):
        nb = blur[k - 1] + blur[k] + blur[k + 1] - prime[k]
        centre[k] = (nb >= 2) & (prime[k] == 1)
    cblur = np.array([_shift(centre[k], -1) + centre[k] + _shift(centre[k], 1) for k in range(5)])
    near_centre = cblur[1] + cblur[2] + cblur[3]
    cols = np.nonzero((prime[2, :n] == 1) & (near_centre[:n] > 0))[0]
    return _row_start(n) * len(cols) + int(cols.sum())


def solve(rows: tuple[int, int] = (5678027, 7208785)) -> int:
    return sum(_row_sum(n) for n in rows)


if __name__ == "__main__":
    print(solve())  # 322303240771079935
