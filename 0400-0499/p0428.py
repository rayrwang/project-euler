"""Problem 428: Necklace of Circles.

C_in (diameter b) sits inside C_out (diameter a+b+c) with centre
offset (a-c)/2, and a closed ring of k >= 3 pairwise non-overlapping
circles tangent to both is a Steiner chain. By Steiner's porism the
existence depends only on the inversive distance
    I = ((2a+b)(2c+b) + b^2) / (2 b (a+b+c)),
and a single-wrap k-chain needs I = (1 + sin^2(pi/k))/(1 - sin^2(pi/k)).
I is rational, so by Niven's theorem k in {3, 4, 6}, i.e. I in
{7, 3, 5/3} (the given examples (5,5,5) -> 5/3, (4,3,21) -> 3 and the
non-example (2,2,5) -> 19/9 all check). Clearing denominators:
    k=4: (a -  b)(c -  b) =  2 b^2          -> tau(2 b^2) solutions
    k=3: (a - 3b)(c - 3b) = 12 b^2          -> tau(12 b^2)
    k=6: (3a - b)(3c - b) =  4 b^2, both factors = -b (mod 3):
         3 | b: (2 gamma - 1) tau(4 b^2 / 9^...) over the non-3 part;
         else (tau(4 b^2) - chi(b) F(4 b^2)) / 2 with chi the mod-3
         character and F(n) = sum chi(d) over d | n, which collapses to
         the divisor count of the (p = 1 mod 3)-part of b squared.
(The negative branches are impossible by a size comparison.) All
three counts are multiplicative in b's exponents, so a segmented
sieve factoring every b <= 10^9 accumulates T(N) directly.
"""

import numba
import numpy as np

@numba.jit(cache=True)
def necklace_count(n: int, primes: np.ndarray, block: int) -> int:
    total = 0
    rem = np.empty(block, dtype=np.int64)
    a2 = np.empty(block, dtype=np.int64)
    g3 = np.empty(block, dtype=np.int64)
    trest = np.empty(block, dtype=np.int64)
    f1 = np.empty(block, dtype=np.int64)
    chi = np.empty(block, dtype=np.int64)
    start = 1
    while start <= n:
        end = min(start + block - 1, n)
        size = end - start + 1
        for i in range(size):
            rem[i] = start + i
            a2[i] = 0
            g3[i] = 0
            trest[i] = 1
            f1[i] = 1
            chi[i] = 1
        # powers of 2
        first = start + ((-start) % 2)
        for v in range(first, end + 1, 2):
            i = v - start
            e = 0
            while rem[i] % 2 == 0:
                rem[i] //= 2
                e += 1
            a2[i] = e
            if e & 1:
                chi[i] = -chi[i]
        # powers of 3
        first = start + ((-start) % 3)
        for v in range(first, end + 1, 3):
            i = v - start
            e = 0
            while rem[i] % 3 == 0:
                rem[i] //= 3
                e += 1
            g3[i] = e
        # odd primes > 3
        for pi in range(len(primes)):
            p = primes[pi]
            first = start + ((-start) % p)
            if first > end:
                continue
            for v in range(first, end + 1, p):
                i = v - start
                e = 0
                while rem[i] % p == 0:
                    rem[i] //= p
                    e += 1
                trest[i] *= 2 * e + 1
                if p % 3 == 1:
                    f1[i] *= 2 * e + 1
                elif e & 1:
                    chi[i] = -chi[i]
        for i in range(size):
            if rem[i] > 1:  # leftover prime > sqrt(n)
                trest[i] *= 3
                if rem[i] % 3 == 1:
                    f1[i] *= 3
                else:
                    chi[i] = -chi[i]
            al = a2[i]
            ga = g3[i]
            tr = trest[i]
            total += (2 * al + 2) * (2 * ga + 1) * tr  # k = 4
            total += (2 * al + 3) * (2 * ga + 2) * tr  # k = 3
            if ga >= 1:
                total += (2 * ga - 1) * (2 * al + 3) * tr  # k = 6
            else:
                total += ((2 * al + 3) * tr - chi[i] * f1[i]) // 2
        start = end + 1
    return total

def t_of(n: int) -> int:
    lim = int(n**0.5) + 2
    sieve = np.ones(lim + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(lim**0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    primes = np.nonzero(sieve)[0]
    primes = primes[primes > 3].astype(np.int64)
    return int(necklace_count(n, primes, 1 << 20))

def t_brute(n: int) -> int:
    """Independent: count c >= 1 by solving each equation for c over a."""
    total = 0
    for b in range(1, n + 1):
        for m in (1, 3):
            # c = m b (a + b) / (a - m b), a > m b
            for a in range(m * b + 1, m * b + m * (m + 1) * b * b + 1):
                num = m * b * (a + b)
                den = a - m * b
                if num % den == 0:
                    total += 1
        # 3 a c = b (a + b + c): c (3a - b) = b (a + b)
        for a in range(b // 3 + 1, (b + 4 * b * b) // 3 + 1):
            den = 3 * a - b
            if den > 0 and (b * (a + b)) % den == 0:
                total += 1
    return total

if __name__ == "__main__":
    assert t_of(1) == t_brute(1) == 9  # given
    assert t_of(20) == t_brute(20) == 732  # given
    assert t_of(3000) == 438106  # given
    print(t_of(10**9))  # 747215561862
