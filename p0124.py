
import math

from funcs import find_prime_factors_set

def rad(n):
    return math.prod(find_prime_factors_set(n))

if __name__ == "__main__":
    rads = {}
    for n in range(1, 100_000+1):
        rads[n] = rad(n)
    rads = sorted(rads.items(), key=lambda item: item[1])
    print(rads[10_000-1][0])  # 21417
