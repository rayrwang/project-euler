
from funcs import gcd

import numba

@numba.jit
def count_fractions(a, b):
    count = 0
    for d in range(2, 12_000+1):
        lower = int(a*d) + 1
        higher = int(b*d + 0.5) - 1
        for n in range(lower, higher+1):
            if gcd(n, d) == 1:
                count += 1
    return count

if __name__ == "__main__":
    print(count_fractions(1/3, 1/2))  # 7295372
