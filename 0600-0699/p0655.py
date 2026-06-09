"""Project Euler Problem 655: Divisible Palindromes.

Count palindromes below 10^32 divisible by P = 10000019.

An L-digit palindrome is determined by its outer ceil(L/2) digits; digit i
(0 = most significant) contributes with weight w_i = 10^i + 10^(L-1-i)
mod P (or 10^((L-1)/2) for the middle digit of an odd length).  For each
length, run a DP over the full residue ring Z_P: keep the count vector of
palindrome-prefixes by remainder and, for each digit position, fold in the
ten possible digits as cyclic shifts of the vector by d * w_i (two
contiguous numpy slice-adds per shift; the leading digit only ranges over
1..9).  The number of L-digit palindromes divisible by P is the final count
at remainder 0, and the answer sums L = 1..32.  In total about
sum_L ceil(L/2) = 272 positions, each ten 10^7-length vector folds.

Checks: a direct brute force for the modulus 109 over palindromes up to
10^7 digit-length by digit-length, including the given nine palindromes
below 10^5.
"""

import numpy as np

P = 10000019


def count_for_length(length: int, p: int) -> int:
    """Number of `length`-digit palindromes divisible by p."""
    half = (length + 1) // 2
    weights = []
    for i in range(half):
        j = length - 1 - i
        weights.append((pow(10, i, p) + pow(10, j, p)) % p if i != j
                       else pow(10, i, p))
    dist = np.zeros(p, dtype=np.int64)
    dist[0] = 1
    for i, w in enumerate(weights):
        out = np.zeros(p, dtype=np.int64)
        for d in range(1 if i == 0 else 0, 10):
            s = d * w % p
            out[s:] += dist[: p - s]
            out[:s] += dist[p - s:]
        dist = out
    return int(dist[0])


def brute(limit: int, p: int) -> int:
    count = 0
    for n in range(p, limit, p):
        s = str(n)
        count += s == s[::-1]
    return count


if __name__ == "__main__":
    assert sum(count_for_length(ln, 109) for ln in range(1, 6)) == 9  # < 10^5
    assert sum(count_for_length(ln, 109) for ln in range(1, 8)) == brute(10**7, 109)
    print(sum(count_for_length(ln, P) for ln in range(1, 33)))  # 2000008332
