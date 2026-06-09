import numba
import numpy as np

from funcs import mod_exp_bounded

@numba.jit(cache=True)
def winning_positions(n: int, p: int) -> int:
    """W(n) mod p for Nim Extreme.

    Ordered distinct n-tuples from {1,..,2^n-1}; losers are XOR-zero positions.
    W(n) = P(M,n) - 2^-n [P(M,n) + M*n!*c_n], where c_n is the x^n coefficient
    of (1+x)^(2^(n-1)-1) (1-x)^(2^(n-1)).
    """
    pow2_nm1 = mod_exp_bounded(2, n - 1, p)
    pow2_n = mod_exp_bounded(2, n, p)
    a = (pow2_nm1 - 1) % p          # exponent on (1+x)
    b = pow2_nm1 % p                # exponent on (1-x)
    big_m = (pow2_n - 1) % p        # M = 2^n - 1

    # Modular inverses 1..n via the standard linear recurrence.
    inv = np.empty(n + 1, dtype=np.int64)
    inv[1] = 1
    for i in range(2, n + 1):
        inv[i] = (p - (p // i) * inv[p % i] % p) % p

    # Cb[m] = binomial(b, m) mod p, built forward.
    cb = np.empty(n + 1, dtype=np.int64)
    cb[0] = 1
    for m in range(1, n + 1):
        cb[m] = cb[m - 1] * ((b - m + 1) % p) % p * inv[m] % p

    # c_n = sum_j binomial(a, j) binomial(b, n-j) (-1)^(n-j)
    ca = 1                          # binomial(a, 0)
    cn = 0
    for j in range(n + 1):
        if j > 0:
            ca = ca * ((a - j + 1) % p) % p * inv[j] % p
        term = ca * cb[n - j] % p
        if (n - j) & 1:
            cn = (cn - term) % p
        else:
            cn = (cn + term) % p
    cn %= p

    fact = 1
    for i in range(2, n + 1):
        fact = fact * i % p

    perm = 1                        # P(M, n) = M (M-1) ... (M-n+1)
    for i in range(n):
        perm = perm * ((big_m - i) % p) % p

    inv2n = mod_exp_bounded(pow2_n, p - 2, p)        # (2^n)^-1 mod p
    inner = (perm + big_m * fact % p * cn) % p
    return (perm - inv2n * inner) % p

if __name__ == "__main__":
    P = 10**9 + 7
    assert winning_positions(1, P) == 1
    assert winning_positions(2, P) == 6
    assert winning_positions(3, P) == 168
    assert winning_positions(5, P) == 19764360
    assert winning_positions(100, P) == 384777056
    print(winning_positions(10**7, P))  # 253223948
