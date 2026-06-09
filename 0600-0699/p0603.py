import numba
import numpy as np

from funcs import prime_sieve_int

P = 10**9 + 7

@numba.jit(cache=True)
def digit_sums(primes: np.ndarray, inv10: int, mod: int):
    """Walk the digits of the concatenation P of the given primes, returning
    D and the four position-weighted digit sums (mod `mod`):
      s1 = sum p_r 10^-r,  s2 = sum p_r r 10^-r,  s3 = sum p_r,  s4 = sum p_r r.
    """
    s1 = s2 = s3 = s4 = 0
    r = 0
    pw = 1  # 10^-r
    for idx in range(len(primes)):
        n = int(primes[idx])
        nd = 0
        m = n
        while m > 0:
            nd += 1
            m //= 10
        for j in range(nd):
            d = (n // 10 ** (nd - 1 - j)) % 10
            dpw = d * pw % mod
            s1 = (s1 + dpw) % mod
            s2 = (s2 + dpw * (r % mod)) % mod
            s3 = (s3 + d) % mod
            s4 = (s4 + d * (r % mod)) % mod
            r += 1
            pw = pw * inv10 % mod
    return r, s1, s2, s3, s4

def solve(n_primes: int, k: int) -> int:
    """S(C(n_primes, k)) mod P.

    S(x) = sum_i d_i (i+1) (10^(L-i) - 1)/9 over the digits of x. Since C is the
    period-D repetition of P = P(n_primes), splitting the global index i = bD + r
    factors the block sum (over b = 0..k-1) into geometric series in g = 10^D.
    """
    primes = prime_sieve_int(15_485_900)[:n_primes]
    inv10 = pow(10, P - 2, P)
    D, s1, s2, s3, s4 = digit_sums(primes, inv10, P)

    g = pow(10, D, P)
    gk = pow(10, k * D, P)  # g^k
    # A = sum_{c=1}^k g^c,  B = sum_{c=1}^k c g^c
    if g != 1:
        inv_g1 = pow(g - 1, P - 2, P)
        A = g * (gk - 1) % P * inv_g1 % P
        num = (1 - (k + 1) * gk + k * (gk * g % P)) % P
        B = g * num % P * pow((1 - g) ** 2 % P, P - 2, P) % P
    else:
        A = k % P
        B = (k * (k + 1) // 2) % P

    kD = (k % P) * (D % P) % P
    alpha = ((kD + 1) * A - D * B) % P
    beta = (D * (((k - 1) * k // 2) % P) + k) % P
    res = (alpha * s1 + A * s2 - beta * s3 - (k % P) * s4) % P
    return res * pow(9, P - 2, P) % P

if __name__ == "__main__":
    print(solve(10**6, 10**12))  # 879476477
