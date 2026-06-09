from math import isqrt

P = 10**9 + 7


def first_square_with_digit(p: int, k: int) -> int:
    """M(p, p - k): least m whose square, in base p, contains digit p - k.

    Requires prime p ≡ 3 (mod 4). Candidates in increasing order of size:

    * Last digit: m^2 ≡ -k (mod p). If -k is a quadratic residue the minimal
      square root (at most p/2) wins outright, since the alternatives below
      all exceed p - k/2. This also covers one-digit squares.
    * Leading digit of a two-digit square: m^2 in [(p-k)p, (p-k+1)p), an
      interval of length p that, with square gaps ~2p, only sometimes
      contains a square; when it does, m ≈ p - k/2.
    * Otherwise a three-digit square m = q p + r, whose middle base-p digit
      is (2 q r + floor(r^2 / p)) mod p; for each q = 1, 2, ... the equation
      2 q r + r^2/p = (p - k) + j p has a real root per branch j, and an
      integer solution sits within a few units of it when one exists. The
      top digit stays tiny and the bottom digit is a non-residue case, so
      the middle digit is the only option and small q always suffices.
    """
    target = p - k
    a = (-k) % p
    root = pow(a, (p + 1) // 4, p)
    if root * root % p == a:
        return min(root, p - root)
    low = target * p
    t = isqrt(low - 1) + 1
    if t * t < low + p:
        return t
    q = 1
    while True:
        best = -1
        for j in range(2 * q + 1):
            approx = isqrt(q * q * p * p + p * (target + j * p)) - q * p
            for r in range(max(0, approx - 4), min(p, approx + 5)):
                if (2 * q * r + r * r // p) % p == target:
                    if best == -1 or r < best:
                        best = r
                    break
        if best != -1:
            return q * p + best
        q += 1


if __name__ == "__main__":
    assert first_square_with_digit(11, 1) == 19  # M(11, 10), given example
    total = sum(first_square_with_digit(P, k) for k in range(1, 10**5 + 1))
    print(total)  # 93158936107011
