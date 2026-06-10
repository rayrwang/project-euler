"""Project Euler Problem 658: Incomplete Words II.

S(k, n) = sum_{alpha <= k} I(alpha, n) where I counts words of length <= n
over an alpha-letter alphabet missing at least one letter.  By
inclusion-exclusion over the sub-alphabet actually used (as in 657),

    I(alpha, n) = sum_{i=0}^{alpha-1} (-1)^(alpha-1-i) C(alpha, i) G(i),

with G(i) = sum_{j<=n} i^j the geometric series.  Swapping the sums,

    S(k, n) = sum_{i=0}^{k-1} G(i) W(i),
    W(i) = sum_{alpha=i+1}^{k} (-1)^(alpha-1-i) C(alpha, i).

Applying Pascal's rule C(alpha, i) = C(alpha+1, i+1) - C(alpha, i+1) to
the column sum telescopes it into the next column, giving the recurrence

    W(i) = 2 W(i+1) + (-1)^(k-i-1) C(k+1, i+1) - 1,   W(k-1) = k,

verified directly for small k.  So a single downward sweep with
precomputed factorials yields all W(i) mod p, while G(i) =
(i^(n+1) - 1)/(i - 1) needs one modular power per i with the exponent
reduced by Fermat (i < k < p) and batch inverses of i - 1.

Checks: S(4, 4) = 406, S(8, 8) = 27902680, S(10, 100) = 983602076 mod p
(given), I(3, 0) = 1, I(3, 2) = 13, I(3, 4) = 79 via S(3, n) - S(2, n),
and a brute-force word count for alpha <= 4, n <= 6.
"""

from itertools import product

import numba
import numpy as np

P = 1_000_000_007


@numba.jit(cache=True)
def S(k: int, n: int) -> int:
    # factorials and inverse factorials up to k + 1
    fact = np.empty(k + 2, dtype=np.int64)
    fact[0] = 1
    for i in range(1, k + 2):
        fact[i] = fact[i - 1] * i % P
    inv_fact = np.empty(k + 2, dtype=np.int64)
    # Fermat inverse of fact[k + 1]
    b, e, r = fact[k + 1], P - 2, 1
    while e:
        if e & 1:
            r = r * b % P
        b = b * b % P
        e >>= 1
    inv_fact[k + 1] = r
    for i in range(k + 1, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % P

    inv = np.empty(k + 1, dtype=np.int64)  # inverses of 1..k
    inv[1] = 1
    for i in range(2, k + 1):
        inv[i] = (P - (P // i) * inv[P % i] % P) % P

    e_red = (n + 1) % (P - 1)  # Fermat exponent reduction
    total = 0
    # W sweep downward, fused with the G(i) evaluation
    w = k % P  # W(k - 1)
    for i in range(k - 1, -1, -1):
        # G(i)
        if i == 0:
            g = 1
        elif i == 1:
            g = (n + 1) % P
        else:
            b, e, r = i, e_red, 1
            while e:
                if e & 1:
                    r = r * b % P
                b = b * b % P
                e >>= 1
            g = (r - 1) * inv[i - 1] % P
        total = (total + g * w) % P
        if i > 0:  # W(i - 1) = 2 W(i) + (-1)^(k-i) C(k+1, i) - 1
            binom = fact[k + 1] * inv_fact[i] % P * inv_fact[k + 1 - i] % P
            sign = 1 if (k - i) % 2 == 0 else P - 1
            w = (2 * w + sign * binom + P - 1) % P
    return total


def S_brute(k: int, n: int) -> int:
    total = 0
    for alpha in range(1, k + 1):
        for length in range(n + 1):
            for word in product(range(alpha), repeat=length):
                total += len(set(word)) < alpha
    return total


if __name__ == "__main__":
    assert S(4, 4) == 406
    assert S(8, 8) == 27902680
    assert S(10, 100) == 983602076
    assert (S(3, 0) - S(2, 0)) % P == 1  # I(3, 0)
    assert (S(3, 2) - S(2, 2)) % P == 13  # I(3, 2)
    assert (S(3, 4) - S(2, 4)) % P == 79  # I(3, 4)
    for kk, nn in ((3, 5), (4, 6)):
        assert S(kk, nn) == S_brute(kk, nn) % P, (kk, nn)
    print(S(10**7, 10**12))  # 958280177
