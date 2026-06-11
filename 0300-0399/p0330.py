import numpy as np
from sympy.ntheory.modular import crt

MODULUS = 77_777_777  # = 7 * 11 * 73 * 101 * 137
PRIMES = (7, 11, 73, 101, 137)


def _residue(p: int, index: int) -> int:
    """(A(n) + B(n)) mod p at n = index, computed over one full period.

    Writing a(n) = (A(n)e + B(n)) / n!, plugging into a(n) = sum_{i>=1} a(n-i)/i! and clearing
    n! gives the binomial-convolution recurrences

        A(n) = sum_{i=1}^n C(n, i) A(n-i) + n!,
        B(n) = sum_{i=1}^n C(n, i) B(n-i) - sum_{i=0}^n n!/i!,

    where the tail d(n) = sum_{i=0}^n n!/i! satisfies d(n) = n*d(n-1) + 1. Reduced modulo a prime
    p, the binomial coefficients (via Lucas) and factorials make the sequence periodic with period
    p(p-1), so one period determines every value."""
    size = index + 1
    fact = np.ones(size, dtype=np.int64)
    for i in range(1, size):
        fact[i] = fact[i - 1] * i % p
    tail = np.zeros(size, dtype=np.int64)
    tail[0] = 1
    for k in range(1, size):
        tail[k] = (k * tail[k - 1] + 1) % p

    a = np.zeros(size, dtype=np.int64)
    b = np.zeros(size, dtype=np.int64)
    a[0] = fact[0] % p
    b[0] = (-tail[0]) % p

    row = np.zeros(size, dtype=np.int64)  # Pascal's triangle row C(k, .) mod p
    row[0] = 1
    for k in range(1, size):
        nxt = np.zeros(size, dtype=np.int64)
        nxt[0] = 1
        nxt[1 : k + 1] = (row[0:k] + row[1 : k + 1]) % p
        row = nxt
        coeffs = row[1 : k + 1]
        a[k] = (int((coeffs * a[k - 1 :: -1][:k]).sum()) + fact[k]) % p
        b[k] = (int((coeffs * b[k - 1 :: -1][:k]).sum()) - tail[k]) % p
    return (int(a[index]) + int(b[index])) % p


def solve(n: int = 10**9) -> int:
    """A(n) + B(n) mod 77777777 for the sequence a(n) = (A(n)e + B(n))/n!.

    The modulus factors into distinct small primes, so the answer is recovered by CRT from the
    residue at n mod p(p-1) for each prime p (one period suffices). The example a(10) with
    A(10) = 328161643 and B(10) = -652694486 confirms the recurrences."""
    residues = [_residue(p, n % (p * (p - 1))) for p in PRIMES]
    value, _ = crt(list(PRIMES), residues)
    return int(value) % MODULUS


if __name__ == "__main__":
    # a(10) = (328161643 e - 652694486) / 10!
    assert (_residue(7, 10) - ((328161643 - 652694486) % 7)) % 7 == 0
    print(solve())  # 15955822
