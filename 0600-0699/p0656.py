"""Project Euler Problem 656: Palindromic Sequences.

S_alpha(n) = floor(alpha n) - floor(alpha (n-1)) is, up to relabeling
the two letters, the mechanical (Sturmian) word of slope
theta = frac(alpha) with intercept 0.  The palindromic prefixes of such
a word are classical: with theta = [0; a_1, a_2, ...] and convergent
denominators q_{-1} = 0, q_0 = 1, q_k = a_k q_{k-1} + q_{k-2}, the
palindromic prefix lengths are exactly

    n = q_{k-2} + t * q_{k-1},   k odd,  1 <= t <= a_k,

in increasing order.  The statement's data for sqrt(31) confirms this
term by term (1; then 3, 5, 7 from k = 3; then 44, 81, 118 from k = 5;
273; 3158, ...), and an independent brute force below re-derives every
palindromic prefix up to length 20000 for several beta by exact integer
arithmetic (floor(n sqrt(b)) = isqrt(n^2 b)) and rolling hashes.

For each non-square beta <= 1000 the continued fraction of sqrt(beta)
is periodic and computed by the standard quadratic-surd recurrence; the
period is repeated as long as needed to harvest the first 100 lengths.
Everything runs in exact big integers, reduced mod 10^15 at the end.

Verified: the 20 listed values for sqrt(31), H_20(sqrt(31)) = 150243655,
and brute-force palindrome scans for beta in {2, 3, 5, 7, 10, 31, 999}.
"""

import math

MOD = 10**15
G = 100
LIMIT = 1000


def cf_sqrt(n: int) -> tuple[int, list[int]]:
    """a0 and the repeating period of the continued fraction of sqrt(n)."""
    a0 = math.isqrt(n)
    m, d, a = 0, 1, a0
    period = []
    while True:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        period.append(a)
        if a == 2 * a0:
            return a0, period


def palindromic_lengths(beta: int, count: int) -> list[int]:
    """First `count` palindromic prefix lengths for alpha = sqrt(beta)."""
    _, period = cf_sqrt(beta)
    out: list[int] = []
    q_prev, q_cur = 0, 1  # q_{k-2}, q_{k-1}
    k = 1
    while len(out) < count:
        a_k = period[(k - 1) % len(period)]
        if k % 2 == 1:
            for t in range(1, a_k + 1):
                out.append(q_prev + t * q_cur)
                if len(out) == count:
                    break
        q_prev, q_cur = q_cur, a_k * q_cur + q_prev
        k += 1
    return out


def brute_palindromic_lengths(beta: int, max_n: int) -> list[int]:
    word = []
    prev = 0
    for n in range(1, max_n + 1):
        cur = math.isqrt(n * n * beta)
        word.append(cur - prev)
        prev = cur
    base, hmod = 1_000_003, (1 << 61) - 1
    fwd = bwd = 0
    pw = 1
    out = []
    for n, c in enumerate(word, start=1):
        fwd = (fwd * base + c) % hmod
        bwd = (bwd + c * pw) % hmod
        pw = pw * base % hmod
        if fwd == bwd and word[: n] == word[: n][::-1]:
            out.append(n)
    return out


if __name__ == "__main__":
    first20 = palindromic_lengths(31, 20)
    assert first20 == [
        1, 3, 5, 7, 44, 81, 118, 273, 3158, 9201, 15244, 21287, 133765,
        246243, 358721, 829920, 9600319, 27971037, 46341755, 64712473,
    ]
    assert sum(first20) == 150243655
    for beta in (2, 3, 5, 7, 10, 31, 999):
        brute = brute_palindromic_lengths(beta, 20000)
        pred = palindromic_lengths(beta, len(brute) + 5)
        assert [n for n in pred if n <= 20000] == brute, beta

    total = 0
    for beta in range(2, LIMIT + 1):
        if math.isqrt(beta) ** 2 == beta:
            continue
        total += sum(palindromic_lengths(beta, G))
    print(total % MOD)  # 888873503555187
