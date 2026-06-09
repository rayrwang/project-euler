"""
https://projecteuler.net/problem=561

S(n) counts pairs (a, b) of distinct divisors of n with a | b. E(m, n)
is the 2-adic valuation of S((p_m#)^n), and Q(n) sums E(904961, i)
for i = 1..n. Find Q(10^12).

Chains a | b | n choose exponents 0 <= x_i <= y_i <= e_i independently
per prime, so with d(n) = prod (e_i + 1) counting the a = b cases,

    S(n) = prod (e_i + 1)(e_i + 2) / 2  -  prod (e_i + 1).

For (p_m#)^i all exponents equal i, giving S = A^m - B^m with
B = i + 1 and A = (i + 1)(i + 2) / 2. Writing k = i + 1 and m odd, the
2-adic valuation splits cleanly by k mod 4:

  k = 1 (mod 4): A^m - B^m = k^m (u^m - 1) 2^(m) / 2^m with
                 u = (k+1)/2 odd; since m is odd the cofactor of u - 1
                 in u^m - 1 is odd, so E = v2(k - 1) - 1.
  k = 3 (mod 4): v2(k + 1) >= 2 makes the bracket odd: E = 0.
  k = 2 (mod 4): A is odd while B is even: E = 0.
  k = 0 (mod 4): v2(A) = v2(k) - 1 < v2(B), so E = m (v2(k) - 1).

E is verified below against direct big-integer valuations,
exhaustively for several small odd m and selectively for m = 904961
itself. Summing the two nonzero cases over k = 2..n+1 (substituting
l = k - 1 in the first) telescopes into floor sums:

    Q(n) = m * sum_(j>=2) floor((n+1) / 2^j) + sum_(j>=2) floor(n / 2^j),

verified against term-by-term summation and the given Q(8) = 2714886.
"""

M = 904961


def v2(x: int) -> int:
    return (x & -x).bit_length() - 1


def s_brute(n: int) -> int:
    divs = [d for d in range(1, n + 1) if n % d == 0]
    return sum(1 for a in divs for b in divs if a != b and b % a == 0)


def s_formula(exps: list[int]) -> int:
    pairs = dcount = 1
    for e in exps:
        pairs *= (e + 1) * (e + 2) // 2
        dcount *= e + 1
    return pairs - dcount


def factor_exps(n: int) -> list[int]:
    exps = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            exps.append(e)
        d += 1
    if n > 1:
        exps.append(1)
    return exps


def e_direct(m: int, i: int) -> int:
    a, b = (i + 1) * (i + 2) // 2, i + 1
    return v2(a**m - b**m)


def e_formula(m: int, i: int) -> int:
    k = i + 1
    r = k % 4
    if r == 1:
        return v2(k - 1) - 1
    if r == 0:
        return m * (v2(k) - 1)
    return 0


def q_of(n: int) -> int:
    a = b = 0
    j = 4
    while j <= n + 1:
        a += (n + 1) // j
        j *= 2
    j = 4
    while j <= n:
        b += n // j
        j *= 2
    return M * a + b


if __name__ == "__main__":
    for nn in range(2, 400):
        assert s_brute(nn) == s_formula(factor_exps(nn)), nn
    assert s_formula([1, 1]) == 5  # S(6) = 5
    for m in (1, 3, 5, 7, 999):
        for i in range(1, 200):
            assert e_direct(m, i) == e_formula(m, i), (m, i)
    for i in range(1, 13):  # the actual m, against ~10^6-digit powers
        assert e_direct(M, i) == e_formula(M, i), i
    assert e_formula(M, 1) == 0  # E(2,1) analogue: v2(S(6)) = 0
    for nn in (1, 2, 8, 17, 100, 12345):
        assert q_of(nn) == sum(e_formula(M, i) for i in range(1, nn + 1)), nn
    assert q_of(8) == 2714886

    print(q_of(10**12))  # 452480999988235494
