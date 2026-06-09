import numba
import numpy as np


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


@numba.njit(cache=True)
def _collect(limit: int, primes: np.ndarray, out: np.ndarray) -> int:
    # n must be even and (since n^2 mod 5 forces it) a multiple of 5, hence of
    # 10. Reject any n where a small prime divides one of n^2 + offset.
    cnt = 0
    n = 10
    while n < limit:
        n2 = n * n
        ok = True
        for pi in range(primes.shape[0]):
            p = primes[pi]
            r = n2 % p
            if ((r + 1) % p == 0 or (r + 3) % p == 0 or (r + 7) % p == 0
                    or (r + 9) % p == 0 or (r + 13) % p == 0 or (r + 27) % p == 0):
                ok = False
                break
        if ok:
            out[cnt] = n
            cnt += 1
        n += 10
    return cnt


def solve(limit: int = 150_000_000) -> int:
    primes = np.array(
        [3, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
         71, 73, 79, 83, 89, 97], dtype=np.int64)
    out = np.zeros(limit // 10 + 1, dtype=np.int64)
    cnt = _collect(limit, primes, out)

    good = (1, 3, 7, 9, 13, 27)
    bad = (5, 11, 15, 17, 19, 21, 23, 25)  # must be composite for consecutiveness
    total = 0
    for i in range(cnt):
        n = int(out[i])
        n2 = n * n
        if all(_is_prime(n2 + k) for k in good) and not any(_is_prime(n2 + k) for k in bad):
            total += n
    return total


if __name__ == "__main__":
    print(solve())  # 676333270
