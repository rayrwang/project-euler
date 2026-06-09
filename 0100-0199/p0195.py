from math import gcd, sqrt


def solve(limit: int = 1053779) -> int:
    # Integer-sided triangles with exactly one 60-degree angle (Eisenstein
    # triples) fall into two primitive families; the inradius of a primitive
    # triangle scales linearly, so each (p, q) contributes floor(bound/(p q))
    # multiples whose inradius stays within the limit.
    bound1 = int(limit * 2 / sqrt(3))
    bound2 = int(limit * 6 / sqrt(3))
    total = 0
    q = 1
    while q * q <= bound1:
        p = q + 1
        while p * q <= bound1:
            if (p - q) % 3 != 0 and gcd(p, q) == 1:
                total += bound1 // (p * q)
            p += 1
        q += 1
    q = 1
    while q * q <= bound2:
        p = q + 3
        while p * q <= bound2:
            if gcd(p, q) == 1:
                total += bound2 // (p * q)
            p += 3
        q += 1
    return total


if __name__ == "__main__":
    print(solve())  # 75085391
