from funcs import is_prime


def is_full_reptend(p: int) -> bool:
    """True if 10 is a primitive root modulo prime p (order p-1)."""
    n = p - 1
    factors = set()
    m, d = n, 2
    while d * d <= m:
        if m % d == 0:
            factors.add(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        factors.add(m)
    return all(pow(10, n // q, p) != 1 for q in factors)


def solve() -> int:
    """Digit sum of the cyclic number 00000000137...56789.

    A cyclic number is c = (10^(p-1) - 1)/p for a full-reptend prime p (10 a
    primitive root mod p), and equals the repeating block of 1/p, so it has
    p-1 digits. Its digit sum is 9(p-1)/2 (the digits pair up into nines).

    Leading 00000000137 means floor(10^11 / p) = 137, fixing the range
        10^11/138 < p <= 10^11/137.
    Trailing 56789 means c == 56789 (mod 10^5); since c*p = 10^(p-1) - 1 ==
    -1 (mod 10^5), this gives 56789*p == 99999 (mod 10^5), fixing p mod 10^5.
    Scan that arithmetic progression for the prime that is full-reptend.
    """
    mod = 10**5
    residue = (99999 * pow(56789, -1, mod)) % mod  # p mod 10^5
    lo, hi = 10**11 // 138 + 1, 10**11 // 137
    p = lo + (residue - lo) % mod
    while p <= hi:
        if is_prime(p) and is_full_reptend(p):
            return 9 * (p - 1) // 2
        p += mod
    raise AssertionError("no qualifying cyclic number found")


if __name__ == "__main__":
    print(solve())  # 3284144505
