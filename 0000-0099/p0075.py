import numba
import numpy as np

@numba.jit(cache=True)
def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a

@numba.jit(cache=True)
def solve(limit):
    """Count wire lengths <= limit that fold into exactly one integer right triangle."""
    count = np.zeros(limit + 1, dtype=np.int32)
    # Euclid: every primitive triple comes from m > n > 0, coprime, opposite parity,
    # with perimeter 2m(m+n). Non-primitive triples are its integer multiples.
    m = 2
    while 2 * m * (m + 1) <= limit:
        for n in range(1, m):
            if (m - n) % 2 == 1 and _gcd(m, n) == 1:
                p = 2 * m * (m + n)
                if p > limit:
                    break
                for perimeter in range(p, limit + 1, p):
                    count[perimeter] += 1
        m += 1
    total = 0
    for v in count:
        if v == 1:
            total += 1
    return total

if __name__ == "__main__":
    print(solve(1_500_000))  # 161667
