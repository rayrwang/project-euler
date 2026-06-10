import numpy as np
from numba import njit


@njit
def _smallest_prime_factor(n: int) -> np.ndarray:
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, n + 1):
        if spf[i] == 0:
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf


@njit
def _gen_divisors(
    k: int,
    spf: np.ndarray,
    primes_buf: np.ndarray,
    exps_buf: np.ndarray,
    divs_buf: np.ndarray,
) -> int:
    """Write the positive divisors of 2*k^2 into divs_buf; return their count."""
    n_primes = 0
    x = k
    while x > 1:
        p = spf[x]
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        primes_buf[n_primes] = p
        exps_buf[n_primes] = e
        n_primes += 1
    has_two = False
    for i in range(n_primes):
        exps_buf[i] *= 2  # k^2 doubles every exponent
        if primes_buf[i] == 2:
            exps_buf[i] += 1  # the extra factor of 2
            has_two = True
    if not has_two:
        primes_buf[n_primes] = 2
        exps_buf[n_primes] = 1
        n_primes += 1
    divs_buf[0] = 1
    n_div = 1
    for i in range(n_primes):
        p = primes_buf[i]
        e = exps_buf[i]
        cur = n_div
        pe = 1
        for _ in range(e):
            pe *= p
            for j in range(cur):
                divs_buf[n_div] = divs_buf[j] * pe
                n_div += 1
    return n_div


@njit
def _count(big_k: int, big_x: int, spf: np.ndarray) -> int:
    """F(K, X): integer quadruplets (k, a, b, c), 1 <= k <= K, -X <= a < b < c <= X,
    whose parabola triangle has at least one 45-degree angle.

    A chord between the points at x = u and x = v has slope (u + v)/k, so a
    45-degree interior angle at a vertex factors cleanly into a product equal to
    -2k^2:
        C1 (at a): (a + b - k)(a + c + k) = -2k^2
        C2 (at c): (a + c - k)(b + c + k) = -2k^2
        C3 (at b): (a + b + k)(b + c - k) = -2k^2
    The answer is |C1 union C2 union C3| by inclusion-exclusion. For a single
    condition one pairwise vertex-sum is a signed divisor d of 2k^2 and the third
    vertex is free, giving a clamped interval of valid values. Two conditions at
    once force a right-isoceles triangle (two 45-degree angles, hence a right
    angle) and are counted by requiring a second quantity to divide 2k^2; all
    three at once is impossible. By the reflection x -> -x, |C2| = |C1| and
    |C2 ∩ C3| = |C1 ∩ C3|, so
        F = 2|C1| + |C3| - |C1 ∩ C2| - 2|C1 ∩ C3|.
    """
    primes_buf = np.empty(64, dtype=np.int64)
    exps_buf = np.empty(64, dtype=np.int64)
    divs_buf = np.empty(300000, dtype=np.int64)
    c1 = c3 = c13 = c12 = 0
    for k in range(1, big_k + 1):
        n_div = _gen_divisors(k, spf, primes_buf, exps_buf, divs_buf)
        total = 2 * k * k
        neg = -total
        for di in range(n_div):
            d_pos = divs_buf[di]
            for sign in range(2):
                d1 = d_pos if sign == 0 else -d_pos
                d2 = neg // d1

                # C1: d1 = a+b-k, d2 = a+c+k, a free; need c > b.
                if d2 - d1 - 2 * k > 0:
                    lo, hi = -big_x, big_x
                    a_max = (d1 + k - 1) // 2  # a < (d1+k)/2
                    if a_max < hi:
                        hi = a_max
                    if d1 + k - big_x > lo:
                        lo = d1 + k - big_x
                    if d1 + k + big_x < hi:
                        hi = d1 + k + big_x
                    if d2 - k - big_x > lo:
                        lo = d2 - k - big_x
                    if d2 - k + big_x < hi:
                        hi = d2 - k + big_x
                    if hi >= lo:
                        c1 += hi - lo + 1

                # C3: d1 = a+b+k, d2 = b+c-k, b free.
                lo, hi = -big_x, big_x
                b_min = (d1 - k) // 2 + 1  # b > (d1-k)/2
                if b_min > lo:
                    lo = b_min
                b_max = (d2 + k - 1) // 2  # b < (d2+k)/2
                if b_max < hi:
                    hi = b_max
                if d1 - k - big_x > lo:
                    lo = d1 - k - big_x
                if d1 - k + big_x < hi:
                    hi = d1 - k + big_x
                if d2 + k - big_x > lo:
                    lo = d2 + k - big_x
                if d2 + k + big_x < hi:
                    hi = d2 + k + big_x
                if hi >= lo:
                    c3 += hi - lo + 1

                # C1 ∩ C3: also need (d1 + 2k) | 2k^2.
                dd = d1 + 2 * k
                if dd != 0 and total % dd == 0:
                    a_plus_c = -total // d1 - k
                    b_plus_c = -total // dd + k
                    a_plus_b = d1 + k
                    num_a = a_plus_b + a_plus_c - b_plus_c
                    if num_a % 2 == 0:
                        a = num_a // 2
                        b = a_plus_b - a
                        c = a_plus_c - a
                        if a < b and b < c and -big_x <= a and c <= big_x:
                            c13 += 1

                # C1 ∩ C2: a+c = -2k^2/d1 - k, also need (a+c-k) | 2k^2.
                a_plus_c = -total // d1 - k
                ac_minus_k = a_plus_c - k
                a_plus_b = d1 + k
                if ac_minus_k != 0 and total % ac_minus_k == 0:
                    b_plus_c = -total // ac_minus_k - k
                    num_a = a_plus_b + a_plus_c - b_plus_c
                    if num_a % 2 == 0:
                        a = num_a // 2
                        b = a_plus_b - a
                        c = a_plus_c - a
                        if a < b and b < c and -big_x <= a and c <= big_x:
                            c12 += 1

    return 2 * c1 + c3 - c12 - 2 * c13


def solve(big_k: int = 1_000_000, big_x: int = 1_000_000_000) -> int:
    spf = _smallest_prime_factor(big_k + 10)
    return _count(big_k, big_x, spf)


if __name__ == "__main__":
    spf_small = _smallest_prime_factor(20)
    assert _count(1, 10, spf_small) == 41
    assert _count(10, 100, spf_small) == 12492
    print(solve())  # 141630459461893728
