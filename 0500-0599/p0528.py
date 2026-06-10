"""
https://projecteuler.net/problem=528

S(n, k, b) counts solutions of x_1 + ... + x_k <= n with
0 <= x_m <= b^m. Find sum_(k=10..15) S(10^k, k, k) mod 10^9 + 7.

Adding a slack variable turns the inequality into an equation with
k + 1 nonnegative variables, counted by stars and bars as
C(n + k, k); the upper bounds are removed by inclusion-exclusion
over which variables overflow, each overflow at position m shifting
n by b^m + 1:

  S(n,k,b) = sum_(T subset [k]) (-1)^|T| C(n - sum_(m in T)(b^m+1) + k, k),

with C(N, k) = 0 for N < k. There are at most 2^15 subsets per
evaluation, and each binomial is a k-term falling-factorial product
mod p.

Verified against literal enumeration for S(14,3,2) = 135 and
S(200,5,3) = 12949440 (both given), plus the given
S(1000,10,5) = 624839075 mod p.
"""

MOD = 10**9 + 7


def _binom_mod(n: int, k: int, p: int) -> int:
    if n < k:
        return 0
    num = 1
    for i in range(k):
        num = num * ((n - i) % p) % p
    den = 1
    for i in range(1, k + 1):
        den = den * i % p
    return num * pow(den, p - 2, p) % p


def s_count(n: int, k: int, b: int, p: int = MOD) -> int:
    bounds = [b**m + 1 for m in range(1, k + 1)]
    total = 0
    for mask in range(1 << k):
        d = sum(bounds[m] for m in range(k) if mask >> m & 1)
        if n < d:
            continue
        sgn = -1 if bin(mask).count("1") % 2 else 1
        total = (total + sgn * _binom_mod(n - d + k, k, p)) % p
    return total % p


def _s_brute(n: int, k: int, b: int) -> int:
    bounds = [b**m for m in range(1, k + 1)]
    cnt = 0

    def rec(i: int, rem: int) -> None:
        nonlocal cnt
        if i == k:
            cnt += 1
            return
        for x in range(min(bounds[i], rem) + 1):
            rec(i + 1, rem - x)

    rec(0, n)
    return cnt


if __name__ == "__main__":
    assert s_count(14, 3, 2) == 135 == _s_brute(14, 3, 2)  # given
    assert s_count(200, 5, 3) == 12949440 == _s_brute(200, 5, 3)  # given
    assert s_count(1000, 10, 5) == 624839075  # given

    print(sum(s_count(10**k, k, k) for k in range(10, 16)) % MOD)  # 779027989
