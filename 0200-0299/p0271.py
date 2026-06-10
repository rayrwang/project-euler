from itertools import product
from math import prod

# n = 13082761331670030 is the product of the primes from 2 through 43, so
# by CRT the cube roots of unity mod n are the combinations of cube roots
# mod each prime: one root for p != 1 (mod 3), three for the six primes
# 7, 13, 19, 31, 37, 43 - hence 3^6 = 729 solutions. Each combination maps
# back through the CRT idempotents e_p = (n/p) ((n/p)^-1 mod p); the answer
# sums them all and removes x = 1. S(91) = 363 verifies the construction.


def s_of(n: int, factors: list[int]) -> int:
    roots_per = [[x for x in range(p) if pow(x, 3, p) == 1] for p in factors]
    idem = [(n // p) * pow(n // p, -1, p) for p in factors]
    total = 0
    for combo in product(*roots_per):
        total += sum(c * e for c, e in zip(combo, idem)) % n
    return total - 1


def solve() -> int:
    factors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    return s_of(prod(factors), factors)


if __name__ == "__main__":
    print(solve())  # 4617456485273129588
