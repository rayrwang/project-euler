import numba
import numpy as np

@numba.njit(cache=True)
def solve(limit):
    """Sum of F(p) over primes p < limit, where F(p) counts solutions of
    a^3 + b^3 = c^3 (mod p) with 1 <= a, b, c < p.

    If p != 1 (mod 3), cubing permutes the nonzero residues, so F(p) is the
    number of pairs (a, b) with a + b nonzero: (p - 1)(p - 2).

    If p = 1 (mod 3), Gauss's count of projective points on the Fermat cubic
    x^3 + y^3 + z^3 = 0 over F_p gives N = p + 1 + a, where 4p = a^2 + 27 b^2
    with a = 1 (mod 3) (this determines a uniquely). Affine solutions number
    (p - 1) N + 1; removing those with a zero coordinate (9(p - 1) + 1 of
    them, since each of x^3 = y^3 and x^3 = -y^3 has 3(p - 1) nonzero
    solutions) leaves F(p) = (p - 1)(N - 9) = (p - 1)(p + a - 8).
    """
    sieve = np.ones(limit, dtype=np.bool_)
    sieve[0] = sieve[1] = False
    i = 2
    while i * i < limit:
        if sieve[i]:
            sieve[i * i :: i] = False
        i += 1

    total = 0
    for p in range(2, limit):
        if not sieve[p]:
            continue
        if p % 3 != 1:
            total += (p - 1) * (p - 2)
        else:
            # Find 4p = a^2 + 27 b^2 by scanning b.
            a = 0
            b = 1
            while True:
                rest = 4 * p - 27 * b * b
                if rest <= 0:
                    break
                r = int(np.sqrt(rest))
                while r * r > rest:
                    r -= 1
                while (r + 1) * (r + 1) <= rest:
                    r += 1
                if r * r == rest:
                    a = r if r % 3 == 1 else -r
                    break
                b += 1
            total += (p - 1) * (p + a - 8)
    return total

if __name__ == "__main__":
    assert solve(6) - solve(4) == 12  # F(5) = 12
    assert solve(8) - solve(6) == 0  # F(7) = 0
    print(solve(6_000_000))  # 4714126766770661630
