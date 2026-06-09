from fractions import Fraction

# R(d) = phi(d) / (d - 1) and phi(d)/d = prod (1 - 1/p) over primes p | d, so
# the resilience is essentially minimised by using as many small distinct
# primes as possible: primorials. Once the primorial including prime p dips
# below the target, a smaller candidate may exist among multiples m * P0 of
# the previous primorial P0 (m composed of primes already in P0, so
# phi(m P0) = m phi(P0)); take the smallest multiple that works.


def solve() -> int:
    target = Fraction(15499, 94744)
    primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    primorial, phi = 1, 1
    for p in primes:
        primorial *= p
        phi *= p - 1
        if Fraction(phi, primorial - 1) < target:
            p0, phi0 = primorial // p, phi // (p - 1)
            for m in range(2, p + 1):
                mm = m
                for q in primes:
                    while mm % q == 0:
                        mm //= q
                if mm != 1:
                    continue  # phi(m * p0) = m * phi0 needs m's primes in p0
                if Fraction(m * phi0, m * p0 - 1) < target:
                    return min(m * p0, primorial)
            return primorial
    raise AssertionError("target not reached")


if __name__ == "__main__":
    print(solve())  # 892371480
