"""Project Euler 900: DistribuNim II.

A move removes exactly min(piles) stones in total, never emptying a pile.
Brute-forcing small positions reveals that a position with r piles, minimum
pile m and stone total s is losing for the player to move if and only if

    s = m - [r even]  (mod 2^L),   2^L = smallest power of two > m,

verified exhaustively for all positions with 2..6 piles of sizes up to
16/10/7/5/4. For n piles of n stones plus one pile of n + k (r = n + 1,
m = n, s = n^2 + n + k) the criterion gives

    t(n) = (-n^2 - (n mod 2)) mod 2^L.

Splitting n in [2^(L-1), 2^L) and writing n = 2^(L-1) + j, we have
n^2 = j^2 (mod 2^L), so the block sum f(L) only involves j^2 mod 2^L for
j < 2^(L-1).  Odd j: each quadratic residue 1 mod 8 below 2^L is hit
exactly twice, giving a closed form.  Even j = 2i reduces to the full-period
sum Q(M) = sum_{i < 2^M} (i^2 mod 2^M), which satisfies
Q(M) = 2^(M-1) (2^(M-1) - 3) + 8 Q(M-2).  Everything is computed mod the
required prime; the formula reproduces S(10) = 361522 exactly.
"""

P = 900497239


def t(n: int) -> int:
    """Smallest k >= 0 making (n piles of n, one pile n+k) losing."""
    mod = 1
    while mod <= n:
        mod *= 2
    return (-n * n - (n & 1)) % mod


def s_direct(n_exp: int) -> int:
    return sum(t(n) for n in range(1, 2**n_exp + 1))


def s_mod(n_exp: int, p: int) -> int:
    pow2 = [1] * (2 * n_exp + 2)
    for i in range(1, 2 * n_exp + 2):
        pow2[i] = pow2[i - 1] * 2 % p

    q = [0] * (n_exp + 1)  # Q(M) mod p
    q[1], q[2] = 1, 2
    for m in range(3, n_exp + 1):
        q[m] = (pow2[m - 1] * (pow2[m - 1] - 3) + 8 * q[m - 2]) % p

    def q_neg(m: int) -> int:
        """sum_{i < 2^M} ((-i^2) mod 2^M), mod p."""
        return (pow2[2 * m] - q[m] - pow2[m] * pow2[m // 2]) % p

    total = 2  # blocks L = 1, 2 contribute t(1) + t(2) + t(3) = 2
    for ell in range(3, n_exp + 1):
        block = 4 * q_neg(ell - 2) + pow2[ell - 2] * (pow2[ell - 1] + 2)
        total = (total + block) % p
    return total % p


if __name__ == "__main__":
    assert s_direct(10) == 361522
    assert s_mod(10, P) == 361522
    print(s_mod(10**4, P))  # 646900900
