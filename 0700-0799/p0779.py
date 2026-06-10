import numba
import numpy as np

@numba.njit(cache=True)
def solve(limit):
    """sum_{K>=1} fbar_K where fbar_K is the mean of
    (alpha(n) - 1)/p(n)^K, p(n) the smallest prime factor of n and
    alpha(n) its exponent.

    The density of {p(n) = p, alpha(n) = a} is
    (1 - 1/p) p^(-a) prod_{q<p} (1 - 1/q), and
    sum_{a>=1} (a-1)(1-1/p) p^(-a) = 1/(p(p-1)), so
    fbar_K = sum_p prod_{q<p}(1 - 1/q) / (p^K p (p-1)). Summing the
    geometric series over K >= 1 gives
        answer = sum_p prod_{q<p}(1 - 1/q) / (p (p-1)^2),
    whose terms decay like 1/(p^3 ln p); primes to 1e8 leave a tail
    far below 1e-15. Both running sums are Kahan-compensated, and the
    same loop reproduces the given fbar_1 = 0.282419756159.
    """
    sieve = np.zeros(limit + 1, dtype=np.bool_)
    total = 0.0
    tc = 0.0
    f1 = 0.0
    f1c = 0.0
    prod = 1.0
    for p in range(2, limit + 1):
        if not sieve[p]:
            for m in range(p * p, limit + 1, p):
                sieve[m] = True
            pf = float(p)
            term = prod / (pf * (pf - 1.0) * (pf - 1.0))
            y = term - tc
            t = total + y
            tc = (t - total) - y
            total = t
            t1 = prod / (pf * pf * (pf - 1.0))
            y = t1 - f1c
            t = f1 + y
            f1c = (t - f1) - y
            f1 = t
            prod *= 1.0 - 1.0 / pf
    return total, f1

if __name__ == "__main__":
    total, f1 = solve(10**8)
    assert f"{f1:.12f}" == "0.282419756159"
    print(f"{total:.12f}")  # 0.547326103833
