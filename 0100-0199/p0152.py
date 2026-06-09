from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import gcd, isqrt


def _is_prime(n: int) -> bool:
    return n > 1 and all(n % i for i in range(2, isqrt(n) + 1))


def solve(top: int = 80) -> int:
    # Sum of distinct 1/k^2 (2<=k<=top) equal to 1/2. For each prime p>=11
    # (p^2 > top), the chosen multiples of p must form a p-integral group:
    # numerator of sum 1/(k/p)^2 divisible by p^2. Drop multiples in no group.
    cands = set(range(2, top + 1))
    for p in range(11, top + 1):
        if not _is_prime(p):
            continue
        mults = [k for k in range(2, top + 1) if k % p == 0]
        ms = [k // p for k in mults]
        usable: set[int] = set()
        for r in range(1, len(ms) + 1):
            for combo in combinations(range(len(ms)), r):
                ssum = sum(Fraction(1, ms[i] * ms[i]) for i in combo)
                if ssum.numerator % (p * p) == 0:
                    usable.update(mults[i] for i in combo)
        cands -= set(mults) - usable

    ks = sorted(cands)
    den = 1
    for k in ks:
        den = den * k * k // gcd(den, k * k)
    vals = [den // (k * k) for k in ks]
    target = den // 2

    # meet in the middle
    half = len(vals) // 2
    sums_a = [0]
    for v in vals[:half]:
        sums_a += [s + v for s in sums_a]
    sums_b = [0]
    for v in vals[half:]:
        sums_b += [s + v for s in sums_b]
    cnt_b = Counter(sums_b)
    return sum(cnt_b.get(target - s, 0) for s in sums_a)


if __name__ == "__main__":
    print(solve())  # 301
