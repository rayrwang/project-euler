"""Project Euler 942: Mersenne's Square Root.

We need the minimal x with x^2 = q (mod p) for p = 2^q - 1 and
q = 74207281, a 74-million-bit Mersenne prime. Generic square-root
algorithms (Tonelli-Shanks, or q^((p+1)/4) since p = 7 mod 8) would
need ~q squarings of q-bit numbers - hopeless. The structure of p
solves it instantly: 2^q = 1 (mod p), so zeta = 2 is a primitive q-th
root of unity in F_p, and the quadratic Gauss sum over the prime q,

    g = sum_{t=1}^{q-1} legendre(t, q) * 2^t  (mod p),

satisfies g^2 = legendre(-1, q) * q = q because q = 1 (mod 4). So the
two square roots are +-g, and R(q) = min(g mod p, p - g mod p), each a
single q-bit big integer assembled from the quadratic-residue pattern
mod q. Marking residues costs (q-1)/2 modular squarings; the two bit
masks become integers via packbits, and no big division is needed
since |A - B| < p.

Verified against the given values R(5) = 6 and R(17) = 47569, and
against brute force for all Mersenne primes 2^q - 1 with q = 1 mod 4
up to q = 13.
"""

import numba
import numpy as np

MOD = 10**9 + 7


@numba.njit(cache=True)
def qr_bits(q: int) -> np.ndarray:
    """bits[t] = 1 if t is a nonzero quadratic residue mod q, else 0."""
    bits = np.zeros(q, np.uint8)
    for s in range(1, (q - 1) // 2 + 1):
        bits[s * s % q] = 1
    return bits


def gauss_sum_root(q: int) -> int:
    """Minimal square root of q modulo 2^q - 1 (q prime, q = 1 mod 4)."""
    p = (1 << q) - 1
    bits = qr_bits(q)
    bits[0] = 0
    a = int.from_bytes(np.packbits(bits, bitorder="little").tobytes(), "little")
    nbits = 1 - bits
    nbits[0] = 0
    b = int.from_bytes(np.packbits(nbits, bitorder="little").tobytes(), "little")
    g = a - b
    if g < 0:
        g += p
    return min(g, p - g)


def solve() -> int:
    q = 74207281
    assert q % 4 == 1
    return gauss_sum_root(q) % MOD


if __name__ == "__main__":
    assert gauss_sum_root(5) == 6
    assert gauss_sum_root(17) == 47569
    print(solve())  # 557539756
