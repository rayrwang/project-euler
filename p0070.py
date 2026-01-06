
from collections import Counter

import numba

@numba.jit
def find_prime_factors(n: int) -> list[int]:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return find_prime_factors(i) + find_prime_factors(n//i)
    return [n]

@numba.jit
def is_prime(n):
    if n == 2 or n == 5 or n == 11:
        return True
    if n % 2 == 0 or n % 5 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 10):
        if n % i == 0:      # 10k + 3
            return False
        if n % (i+4) == 0:  # 10k + 7
            return False
        if n % (i+6) == 0:  # 10k + 9
            return False
        if n % (i+8) == 0:  # 10k + 1
            return False
    return True

def totient(n):
    prime_factors = find_prime_factors(n)
    prod = 1
    for (p, k) in Counter(prime_factors).items():
        prod *= p**(k-1)*(p-1)
    return prod

if __name__ == "__main__":
    min_ratio = float("inf")
    min_ratio_n = None
    for n in range(1, int(1e7)):
        phi = totient(n)
        # If they are permutations of each other
        if sorted(str(phi)) == sorted(str(n)):
            ratio = n / phi
            if ratio < min_ratio:
                min_ratio = ratio
                min_ratio_n = n
    print(min_ratio_n)  # 8319823
