"""Project Euler 955: Finding Triangles.

Between triangle numbers the recurrence a_{n+1} = 2 a_n - a_{n-1} + 1 has
second difference 1, and the step out of a triangle number is +1, so k steps
after reaching the triangle number T_m the value is T_m + T_k. The next
triangle number in the sequence is therefore the smallest k >= 1 with
T_m + T_k = T_M for some M, i.e.

    (M - k)(M + k + 1) = m(m + 1).

Writing D1 = M - k, D2 = M + k + 1 this is a factorisation of N = m(m+1)
into a pair with odd difference D2 - D1 = 2k + 1 >= 3. So each hop is: factor
N, take the divisor pair of opposite parity with the smallest difference >= 3,
advance the index by k = (D2 - D1 - 1)/2 and set m = (D1 + D2 - 1)/2.

Starting from a_0 = 3 = T_2 we hop 69 times. The values stay below ~5 * 10^24
(m below ~3 * 10^12), so Pollard rho factors every N instantly. The method
reproduces the given 10th triangle number a_2964 = 1439056 (and brute force
agrees on the first ten triangle indices).
"""

import math
import random


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def pollard_rho(n: int) -> int:
    if n % 2 == 0:
        return 2
    while True:
        x = random.randrange(2, n)
        y, c, d = x, random.randrange(1, n), 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = math.gcd(abs(x - y), n)
        if d != n:
            return d


def factorize(n: int, out: dict[int, int]) -> None:
    if n == 1:
        return
    if is_prime(n):
        out[n] = out.get(n, 0) + 1
        return
    d = pollard_rho(n)
    factorize(d, out)
    factorize(n // d, out)


def divisors(fac: dict[int, int]) -> list[int]:
    divs = [1]
    for p, e in fac.items():
        divs = [d * p**i for d in divs for i in range(e + 1)]
    return divs


def solve(target: int) -> int:
    m, idx = 2, 0  # a_0 = 3 = T_2 is the 1st triangle number
    for _ in range(target - 1):
        n_val = m * (m + 1)
        fac: dict[int, int] = {}
        factorize(m, fac)
        factorize(m + 1, fac)
        best_d1, best_diff = 0, 0
        for d in divisors(fac):
            d2 = n_val // d
            diff = d2 - d
            if diff % 2 == 1 and diff >= 3 and (best_d1 == 0 or diff < best_diff):
                best_d1, best_diff = d, diff
        idx += (best_diff - 1) // 2
        m = (best_d1 + n_val // best_d1 - 1) // 2
    return idx


if __name__ == "__main__":
    print(solve(70))  # 6795261671274
