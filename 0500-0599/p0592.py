"""
https://projecteuler.net/problem=592

f(N) is the last twelve hexadecimal digits of N! before the trailing
zeroes. Find f(20!), where 20! ~ 2.4 * 10^18.

Write N! = 2^v * m with m odd and v = sum_(i>=1) floor(N / 2^i);
the trailing hex zeroes are floor(v/4), so
f(N) = m * 2^(v mod 4) mod 2^48. The odd part factors as
m = prod_(i>=0) OF(floor(N / 2^i)) with OF(R) the product of odd
j <= R, so everything reduces to OF(R) mod 2^56 for R up to
2.4 * 10^18.

OF is computed 2-adically: every odd j with j = 3 mod 4 is replaced
by -j (tracking the sign (-1)^floor((R+1)/4)), leaving units
u = 1 mod 4 where log u = sum_(m>=1) (-1)^(m+1) (u-1)^m / m
converges with v_2((u-1)^m / m) >= 2m - v_2(m), so truncating at
m = 34 is exact mod 2^56. The sum of (u-1)^m over each arithmetic
progression {a, a+4, ...} <= R expands binomially into the exact
power sums sum t^i, computed by the Pascal recursion in big
integers; divisions by m and by t! in the exponential are exact
2-adic operations (shift by the 2-valuation, multiply by the odd
part's inverse), and exp(L) = sum L^t / t! terminates at
t + s_2(t) >= 56 since L is a multiple of 4. The whole computation
is a few dozen polynomial sums.

OF is verified against the literal product mod 2^56 for various
R <= 1.3 * 10^5, and f against the actual factorial (zeroes
stripped) for N = 20 (the given 21C3677C82B4), 21, 25, 50, 100 and
1000.
"""

from math import comb, factorial

K = 56
MK = 1 << K


def _power_sums(t: int, imax: int) -> list[int]:
    """S_i = sum_(j=0..t-1) j^i exactly, for i = 0..imax."""
    sums = [t]
    for k in range(1, imax + 1):
        acc = sum(comb(k + 1, i) * sums[i] for i in range(k))
        sums.append((t ** (k + 1) - acc) // (k + 1))
    return sums


def _ap_log_sum(a: int, sigma: int, r: int, mterms: int = 34) -> int:
    """sum of log(sigma * j) mod 2^K over j in {a, a+4, ...} <= r,
    where sigma * j = 1 mod 4."""
    if r < a:
        return 0
    t = (r - a) // 4 + 1
    av, bv = sigma * a - 1, 4 * sigma
    sums = _power_sums(t, mterms)
    total = 0
    for m in range(1, mterms + 1):
        p = sum(comb(m, i) * av ** (m - i) * bv**i * sums[i] for i in range(m + 1))
        s2 = (m & -m).bit_length() - 1
        odd = m >> s2
        val = (p >> s2) % MK * pow(odd, -1, MK) % MK
        total = (total + (val if m % 2 == 1 else -val)) % MK
    return total


def odd_factorial(r: int) -> int:
    """product of all odd j <= r, mod 2^K."""
    if r < 1:
        return 1
    big = 1 << (K + 64)
    lval = (_ap_log_sum(1, 1, r) + _ap_log_sum(3, -1, r)) % MK
    res, lp = 0, 1
    for t in range(60):
        if t > 0:
            lp = lp * lval % big
            if t + bin(t).count("1") >= K:
                break
        ft = factorial(t)
        v2f = (ft & -ft).bit_length() - 1
        oddf = ft >> v2f
        res = (res + (lp >> v2f) % MK * pow(oddf, -1, MK)) % MK
    sign = -1 if ((r + 1) // 4) % 2 else 1
    return sign * res % MK


def f_of(n: int) -> str:
    odd, v2, m = 1, 0, n
    while m > 0:
        odd = odd * odd_factorial(m) % MK
        m //= 2
        v2 += m
    return f"{odd * pow(2, v2 % 4, MK) % (1 << 48):012X}"


def _f_direct(n: int) -> str:
    x = factorial(n)
    while x % 16 == 0:
        x //= 16
    return f"{x % (1 << 48):012X}"


if __name__ == "__main__":
    for r in (1, 2, 5, 10, 100, 1234, 99999, 123457):
        prod = 1
        for j in range(1, r + 1, 2):
            prod = prod * j % MK
        assert odd_factorial(r) == prod, r
    assert f_of(20) == "21C3677C82B4" == _f_direct(20)  # given
    for n in (21, 25, 50, 100, 1000):
        assert f_of(n) == _f_direct(n), n

    print(f_of(factorial(20)))  # 13415DF2BE9C
