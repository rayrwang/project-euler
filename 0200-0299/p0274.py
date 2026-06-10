import numpy as np

# Writing n = 10q + r, the map f(n) = q + m r preserves divisibility by p
# exactly when f(n) = k n (mod p) for an invertible k: comparing
# coefficients, 10 k = 1 and m = k, so the divisibility multiplier is
# m = 10^(-1) mod p (m = 34 for p = 113 as stated). For p coprime to 10,
# m = (k p + 1)/10 with the single digit k satisfying k p = -1 (mod 10):
# k = 9, 3, 7, 1 for p = 1, 3, 7, 9 (mod 10). Sieve the primes below 10^7
# and sum the closed form (verified by checking 10 m = 1 (mod p) for all).


def solve(limit: int = 10**7) -> int:
    s = np.ones(limit, dtype=bool)
    s[:2] = False
    for i in range(2, int(limit**0.5) + 1):
        if s[i]:
            s[i * i :: i] = False
    primes = np.nonzero(s)[0].astype(np.int64)
    primes = primes[(primes != 2) & (primes != 5)]
    r = primes % 10
    k = np.zeros_like(primes)
    k[r == 1] = 9
    k[r == 3] = 3
    k[r == 7] = 7
    k[r == 9] = 1
    m = (k * primes + 1) // 10
    assert ((m * 10) % primes == 1).all()
    return int(m.sum())


if __name__ == "__main__":
    print(solve())  # 1601912348822
