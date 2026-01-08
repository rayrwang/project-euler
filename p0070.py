
from collections import Counter

import numba

@numba.jit
def find_prime_factors(n: int) -> list[int]:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return find_prime_factors(i) + find_prime_factors(n//i)
    return [n]

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
