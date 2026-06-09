"""Project Euler Problem 516: 5-smooth Totients.

S(L) = sum of n <= L with phi(n) a Hamming number (5-smooth).  Find S(1e12) mod 2^32.

phi is multiplicative and phi(p^e) = p^{e-1}(p-1).  For phi(n) to be 5-smooth every
prime-power factor must contribute a 5-smooth value:
  * p in {2,3,5}: p^{e-1}(p-1) is 5-smooth for any e (since 2-1=1, 3-1=2, 5-1=4),
  * p > 5: p^{e-1} carries the factor p > 5 unless e = 1, and then we still need
    p - 1 to be 5-smooth.

So the admissible n are exactly  n = (2^a 3^b 5^c) * Q,  where Q is a squarefree
product of distinct "special" primes p > 5 with p-1 a Hamming number.  Each n
factors uniquely this way (the 2,3,5 part is a Hamming number H, the rest is Q), so

    S(L) = sum over squarefree special-prime products Q <= L  of  Q * H(floor(L/Q)),

where H(x) is the sum of Hamming numbers <= x.  Answer taken mod 2^32.
"""

from bisect import bisect_right

from funcs import is_prime

LIMIT = 10**12
MOD = 2**32


def hamming_upto(limit: int) -> list[int]:
    out = []
    p2 = 1
    while p2 <= limit:
        p23 = p2
        while p23 <= limit:
            p235 = p23
            while p235 <= limit:
                out.append(p235)
                p235 *= 5
            p23 *= 3
        p2 *= 2
    out.sort()
    return out


def S(limit: int) -> int:
    ham = hamming_upto(limit)
    # prefix sums for fast "sum of Hamming numbers <= x"
    prefix = [0] * (len(ham) + 1)
    for i, h in enumerate(ham):
        prefix[i + 1] = prefix[i] + h

    def ham_sum(x: int) -> int:
        return prefix[bisect_right(ham, x)]

    # special primes p > 5 with p-1 a Hamming number, p <= limit
    specials = []
    for h in ham:
        p = h + 1
        if p > 5 and p <= limit and is_prime(p):
            specials.append(p)
    specials.sort()
    m = len(specials)

    total = 0

    def dfs(idx: int, q: int) -> None:
        nonlocal total
        total += q * ham_sum(limit // q)
        for j in range(idx, m):
            nq = q * specials[j]
            if nq > limit:
                break
            dfs(j + 1, nq)

    dfs(0, 1)
    return total % MOD


if __name__ == "__main__":
    assert S(100) == 3728, S(100)
    print(S(LIMIT))  # 939087315
