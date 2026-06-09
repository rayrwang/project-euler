import numba
import numpy as np

# F and G are the bisector feet on CA and AB, so AF = bc/(a + c),
# AG = bc/(a + b) and area(ABC)/area(AFG) = (a + b)(a + c)/(b c) =: R.
# With a <= b <= c each factor (1 + a/b), (1 + a/c) lies in (1, 2], so an
# integral R is 2, 3 or 4. R = 4 forces a = b = c (equilateral,
# floor(N/3) triangles). For k = R in {2, 3}, substituting
# X = (k - 1) b - a, Y = (k - 1) c - a turns the condition into X Y = k a^2,
# and the triangle inequality a + b > c is exactly X > a, while b <= c gives
# X <= Y i.e. X < sqrt(k) a. For k = 3, b and c integral additionally
# require X = Y = a (mod 2).
#
# Enumerate by the divisor X (named d below): d | k a^2 holds iff a is a
# multiple of m(d) = prod p^ceil((e_p - v_p(k)) / 2) over p^e_p || d, read
# off a smallest-prime-factor sieve. For each d, walk a over multiples of
# m(d) in (d / sqrt(k), d), with the perimeter increasing in a so the scan
# breaks early. Verified against full brute force for perimeters up to 3000.


@numba.njit(cache=True)
def _spf_sieve(n: int) -> np.ndarray:
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, n + 1):
        if spf[i] == 0:
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf


@numba.njit(cache=True)
def _count_k(n: int, k: int, spf: np.ndarray) -> int:
    # Minimal perimeter for divisor d is at a = d/sqrt(k), where k a^2/d = d:
    # k = 2: P_min = d (3/sqrt(2) + 2) = 4.1213 d
    # k = 3: P_min = d (2/sqrt(3) + 1) = 2.1547 d
    count = 0
    for d in range(2, n):
        if k == 2:
            if 103 * d > 25 * n:  # 4.12 d > n implies P_min > n
                break
        elif 15 * d > 7 * n:  # 2.1429 d > n implies P_min > n
            break
        m = 1  # minimal a-step so that d | k a^2
        x = d
        while x > 1:
            p = spf[x]
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            if p == k:
                e -= 1
            if e > 0:
                m *= p ** ((e + 1) // 2)
        a_min = int(np.sqrt(d * d / k)) - 2
        if a_min < 1:
            a_min = 1
        while k * a_min * a_min < d * d:
            a_min += 1
        a = ((a_min + m - 1) // m) * m
        while a < d:
            d2 = k * a * a // d
            if k == 2:
                p_sum = 3 * a + d + d2
                if p_sum > n:
                    break
                count += 1
            else:
                p_sum = 2 * a + (d + d2) // 2
                if p_sum > n:
                    break
                if (d - a) % 2 == 0 and (d2 - a) % 2 == 0:
                    count += 1
            a += m
    return count


def solve(n: int = 100_000_000) -> int:
    spf = _spf_sieve(n // 2)
    return n // 3 + int(_count_k(n, 2, spf)) + int(_count_k(n, 3, spf))


if __name__ == "__main__":
    print(solve())  # 139012411
