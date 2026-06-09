import numpy as np
from numba import njit


def _primes_1mod4(limit: int) -> np.ndarray:
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    pr = np.nonzero(sieve)[0]
    return pr[pr % 4 == 1].astype(np.int64)


@njit(cache=True)
def _generate(p_max: int, primes: np.ndarray, bound: int, out: np.ndarray) -> int:
    # Each Alexandrian integer is A = p (p + d)(p + (p^2+1)/d) for d | p^2 + 1.
    # Only prime factors 2 and primes = 1 (mod 4) divide p^2 + 1. Store A <= bound,
    # guarding the product against int64 overflow.
    cnt = 0
    for p in range(1, p_max + 1):
        n = p * p + 1
        m = n
        pf = np.empty(40, np.int64)
        pe = np.empty(40, np.int64)
        k = 0
        if m % 2 == 0:
            c = 0
            while m % 2 == 0:
                m //= 2
                c += 1
            pf[k] = 2
            pe[k] = c
            k += 1
        for idx in range(len(primes)):
            pr = primes[idx]
            if pr * pr > m:
                break
            if m % pr == 0:
                c = 0
                while m % pr == 0:
                    m //= pr
                    c += 1
                pf[k] = pr
                pe[k] = c
                k += 1
        if m > 1:
            pf[k] = m
            pe[k] = 1
            k += 1
        divs = np.empty(4096, np.int64)
        divs[0] = 1
        nd = 1
        for t in range(k):
            base = nd
            pw = 1
            for _ in range(pe[t]):
                pw *= pf[t]
                for j in range(base):
                    divs[nd] = divs[j] * pw
                    nd += 1
        for j in range(nd):
            d = divs[j]
            e = n // d
            if d <= e:
                f1, f2, f3 = p, p + d, p + e
                if f2 > bound // f1:
                    continue
                prod = f1 * f2
                if f3 > bound // prod:
                    continue
                a = prod * f3
                if a <= bound:
                    out[cnt] = a
                    cnt += 1
    return cnt


def solve(rank: int = 150000) -> int:
    # Min A for a given p exceeds 4 p^3, so p <= 95000 covers everything up to the
    # bound (3e15), which comfortably exceeds the 150000th value.
    p_max = 95000
    bound = 3_000_000_000_000_000
    primes = _primes_1mod4(120000)
    out = np.empty(20_000_000, dtype=np.int64)
    cnt = _generate(p_max, primes, bound, out)
    vals = np.unique(out[:cnt])
    return int(vals[rank - 1])


if __name__ == "__main__":
    print(solve())  # 1884161251122450
