"""Project Euler Problem 664: An Infinite Game.

Conway-soldiers potential argument.  Weight each square sigma^t where t
is its taxicab distance to the target square and sigma = 1/phi, so that
sigma^2 + sigma = 1.  A move advancing a token from distance k to k - 1
gains sigma^(k-1) - sigma^k = sigma^(k+1) and discards a token of
weight at most sigma^(k+1), so the total potential never increases, and
reaching the target needs initial potential strictly above 1 (a finite
play leaves leftover weight).  Column d of the half-plane, with d^n
tokens per square, contributes d^n sigma^(t+d-1) sum_y sigma^|y| where
the row sum is 1 + 2 sigma / (1 - sigma) = phi^3.  Hence the target at
distance t is reachable iff sigma^(t-4) A_n > 1 with
A_n = sum_{d>=1} d^n sigma^d, giving

    F(n) = 3 + ceil(log_phi A_n).

This matches all six given values, computed EXACTLY: with
sum_d d^n x^d = sum_k S(n,k) k! x^k / (1-x)^(k+1) and 1 - sigma =
sigma^2, A_n = sum_k S(n,k) k! phi^(k+2) lies in Z[phi]; writing
phi^m = F_{m-1} + F_m phi, the ceiling is the least k with
phi^k >= A_n, decided by the exact sign of x + y phi via comparing
(2x + y)^2 with 5 y^2.

For n = 1234567 the EGF sigma e^x / (1 - sigma e^x) has its dominant
simple pole at x = ln(phi), so A_n = n! / (ln phi)^(n+1) up to a factor
1 + O((ln phi / |ln phi + 2 pi i|)^n), utterly negligible.  Then
log_phi A_n = (ln n! - (n+1) ln ln phi) / ln phi in floating point with
about 1e-8 absolute error (cross-checked by Kahan-summing ln k), while
the fractional part sits 0.189 from the nearest integer.

Verified: F(0, 1, 2, 3, 11, 123) = 4, 6, 9, 13, 58, 1173 exactly, and
exact == asymptotic for every n in 3..400.
"""

import math

N = 1234567
LNPHI = math.log((1 + math.sqrt(5)) / 2)


def sign_zphi(x: int, y: int) -> int:
    """Exact sign of x + y * phi with phi = (1 + sqrt 5) / 2."""
    u = 2 * x + y  # sign of u + y * sqrt(5)
    if u >= 0 and y >= 0:
        return 1 if (u or y) else 0
    if u <= 0 and y <= 0:
        return -1
    if y > 0:
        return 1 if 5 * y * y > u * u else -1
    return 1 if u * u > 5 * y * y else -1


def exact_f(n: int) -> int:
    if n == 0:
        a, b = 0, 1  # A_0 = phi
    else:
        stir = [0] * (n + 1)
        stir[0] = 1
        for i in range(1, n + 1):
            new = [0] * (n + 1)
            for k in range(1, i + 1):
                new[k] = stir[k - 1] + k * stir[k]
            stir = new
        fib = [0, 1]
        while len(fib) < n + 3:
            fib.append(fib[-1] + fib[-2])
        a = b = 0
        fact = 1
        for k in range(1, n + 1):
            fact *= k
            c = stir[k] * fact
            a += c * fib[k + 1]
            b += c * fib[k + 2]
    fib = [0, 1]
    k = 1
    while True:
        while len(fib) <= k + 1:
            fib.append(fib[-1] + fib[-2])
        if sign_zphi(fib[k - 1] - a, fib[k] - b) >= 0:
            return 3 + k
        k += 1


def asym_f(n: int) -> int:
    ln_fact = math.lgamma(n + 1)
    log_a = (ln_fact - (n + 1) * math.log(LNPHI)) / LNPHI
    dist = abs(log_a - round(log_a))
    assert dist > 1e-6, "too close to an integer for float precision"
    return 3 + math.ceil(log_a)


def kahan_ln_factorial(n: int) -> float:
    total = comp = 0.0
    for k in range(2, n + 1):
        y = math.log(k) - comp
        t = total + y
        comp = (t - total) - y
        total = t
    return total


if __name__ == "__main__":
    for n, want in ((0, 4), (1, 6), (2, 9), (3, 13), (11, 58),
                    (123, 1173)):
        assert exact_f(n) == want, n
    for n in range(3, 401):
        assert exact_f(n) == asym_f(n), n
    assert abs(kahan_ln_factorial(N) - math.lgamma(N + 1)) < 1e-6
    print(asym_f(N))  # 35295862
