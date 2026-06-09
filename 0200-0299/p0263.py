import numba
import numpy as np

# An engineers' paradise n needs (n-9, n-3), (n-3, n+3), (n+3, n+9) to be
# three consecutive sexy prime pairs - so n-9, n-3, n+3, n+9 are primes with
# no prime strictly between them - and n-8, n-4, n, n+4, n+8 all practical.
#
# The four primes force n even (n-3 odd) and, mod 5, they are
# n+1, n+2, n+3, n+4, so n = 0 (mod 5); also n != 0 (mod 3). Hence n = 0
# (mod 10). Candidates m = n +/- 5 are divisible by 5, so "consecutive"
# reduces to n-7, n-1, n+1, n+7 being composite. A segmented sieve (blocks
# extended past the right edge so the +/-9 window never straddles) scans
# n = 10, 20, ... for the pattern; the rare survivors are then tested for
# practicality of the five even neighbours with Stewart's criterion:
# 2 | m and each successive prime p of m satisfies p <= sigma(so far) + 1.


@numba.njit(cache=True)
def _small_primes(n: int) -> np.ndarray:
    s = np.ones(n + 1, dtype=np.bool_)
    s[0] = s[1] = False
    for i in range(2, int(n**0.5) + 1):
        if s[i]:
            s[i * i :: i] = False
    return np.nonzero(s)[0].astype(np.int64)


@numba.njit(cache=True)
def _candidates(limit: int, primes: np.ndarray, out: np.ndarray) -> int:
    block = 10_000_000
    margin = 16
    flags = np.empty(block + margin, dtype=np.bool_)
    cnt = 0
    lo = 0
    while lo < limit:
        hi = min(lo + block, limit)
        size = hi - lo + margin
        flags[:size] = True
        if lo == 0:
            flags[0] = False
            flags[1] = False
        for p in primes:
            if p * p >= lo + size:
                break
            start = p * p if p * p >= lo else ((lo + p - 1) // p) * p
            for j in range(start - lo, size, p):
                flags[j] = False
        n = (lo // 10 + 1) * 10
        if n < 20:
            n = 20
        while n < hi:
            if n % 3 != 0:
                i = n - lo
                if (
                    flags[i - 9]
                    and flags[i - 3]
                    and flags[i + 3]
                    and flags[i + 9]
                    and not flags[i - 7]
                    and not flags[i - 1]
                    and not flags[i + 1]
                    and not flags[i + 7]
                ):
                    out[cnt] = n
                    cnt += 1
                    if cnt >= len(out):
                        return cnt
            n += 10
        lo = hi
    return cnt


def _is_practical(m: int) -> bool:
    if m % 2:
        return False
    sigma = 1
    x = m
    first = True
    p = 2
    while p * p <= x:
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            if not first and p > sigma + 1:
                return False
            sigma *= (p ** (e + 1) - 1) // (p - 1)
            first = False
        p += 1 if p == 2 else 2
    if x > 1:
        if first or x > sigma + 1:
            return False
        sigma *= x + 1
    return True


def solve(count: int = 4, limit: int = 1_500_000_000) -> int:
    primes = _small_primes(int((limit + 100) ** 0.5) + 10)
    out = np.zeros(200_000, dtype=np.int64)
    cnt = _candidates(limit, primes, out)
    paradises = []
    for n in out[:cnt]:
        n = int(n)
        if all(_is_practical(m) for m in (n - 8, n - 4, n, n + 4, n + 8)):
            paradises.append(n)
            if len(paradises) == count:
                break
    assert len(paradises) == count
    return sum(paradises)


if __name__ == "__main__":
    print(solve())  # 2039506520
