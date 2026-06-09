from math import gcd


def solve(p: int = 1009, q: int = 3643) -> int:
    # RSA exponents e with gcd(e, phi)=1; the number of unconcealed messages is
    # (1+gcd(e-1, p-1))(1+gcd(e-1, q-1)). Sum every e attaining the minimum.
    phi = (p - 1) * (q - 1)
    best = None
    total = 0
    for ex in range(2, phi):
        if gcd(ex, phi) != 1:
            continue
        unconcealed = (1 + gcd(ex - 1, p - 1)) * (1 + gcd(ex - 1, q - 1))
        if best is None or unconcealed < best:
            best, total = unconcealed, ex
        elif unconcealed == best:
            total += ex
    return total


if __name__ == "__main__":
    print(solve())  # 399788195976
