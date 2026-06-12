"""
Project Euler Problem 792: Too Many Twos
https://projecteuler.net/problem=792

With S(n) = sum_{k=1}^{n} (-2)^k C(2k, k) and u(n) the 2-adic valuation
nu_2(3 S(n) + 4), find U(10^4) = sum_{n <= 10^4} u(n^3).

A 2-adic tail.  The term valuations nu_2((-2)^k C(2k, k)) = k + s_2(k)
(Kummer; s_2 is the binary digit sum) tend to infinity, so the full series
converges in Z_2, where the binomial expansion of (1 - 4x)^(-1/2) at
x = -2 is the square root of 1/9 congruent to 1 mod 4:

    sum_{k >= 0} (-2)^k C(2k, k) = -1/3   in Z_2.

Hence 3 S(n) + 4 = 3(-1/3 - 1 - T(n)) + 4 = -3 T(n) where T(n) is the
tail sum over k > n, and u(n) = nu_2(T(n)).

Computing the tail valuation.  Factor the first central binomial out of
the tail: with the ratio C(2m + 2, m + 1) = C(2m, m) * 2(2m + 1)/(m + 1),

    T(n) = (-2)^n C(2n, n) * sum_{j >= 1} (-4)^j
           prod_{i=1}^{j} (2n + 2i - 1) / (n + i),

and the j-th summand of C(2n, n) * (that sum) has valuation exactly
j + s_2(n + j) >= 2 (the factor (n+j)!/n! removes j + s_2(n) - s_2(n+j)
twos).  So working modulo 2^B only the first B terms matter, each an odd
running product times a power of two, with odd inverses taken mod 2^B.
u(n) = n + nu_2 of the accumulated sum; if the valuation lands too close
to the precision (possible cancellation), retry with 2B.  B = 96 already
suffices for every n^3 here, and the whole double-checked sum takes a few
seconds in plain Python.  Verified against the direct big-integer tail for
all n <= 3000 and the given u(4) = 7, u(20) = 24, U(5) = 241.
"""

N = 10**4


def u(n, bits=96):
    """nu_2(3 S(n) + 4) via the 2-adic tail, exact for this precision."""
    mod = 1 << bits
    total = 0
    num = 1  # running odd part of the j-th summand
    e = bin(n).count("1")  # exponent; reaches j + s_2(n + j) each step
    for j in range(1, bits + 8):
        m = n + j
        v = (m & -m).bit_length() - 1
        e += 2 - v
        num = num * ((2 * n + 2 * j - 1) % mod) % mod
        num = num * pow((m >> v) % mod, -1, mod) % mod
        if e < bits:
            term = (num << e) % mod
            total = (total - term) % mod if j % 2 else (total + term) % mod
    if total == 0:
        return u(n, bits * 2)
    v2 = (total & -total).bit_length() - 1
    if v2 > bits - 16:
        return u(n, bits * 2)  # too close to precision: redo
    return n + v2


def main():
    assert u(4) == 7
    assert u(20) == 24
    assert sum(u(n**3) for n in range(1, 6)) == 241
    return sum(u(n**3) for n in range(1, N + 1))


if __name__ == "__main__":
    print(main())  # 2500500025183626
