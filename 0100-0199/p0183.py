from math import e as _E
from math import floor, gcd, log


def solve(lo: int = 5, hi: int = 10000) -> int:
    # M(N) = max over k of (N/k)^k, maximised near k = N/e. (N/k)^k terminates
    # iff the reduced denominator k/gcd(N,k) has only the prime factors 2 and 5.
    total = 0
    for n in range(lo, hi + 1):
        base = floor(n / _E)
        best_val, best_k = None, base
        for k in (base, base + 1):
            if k < 1:
                continue
            val = k * log(n / k)
            if best_val is None or val > best_val:
                best_val, best_k = val, k
        d = best_k // gcd(n, best_k)
        while d % 2 == 0:
            d //= 2
        while d % 5 == 0:
            d //= 5
        total += -n if d == 1 else n
    return total


if __name__ == "__main__":
    print(solve())  # 48861552
