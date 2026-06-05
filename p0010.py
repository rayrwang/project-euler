
import numpy as np

if __name__ == "__main__":
    is_prime_array = np.full(2_000_000, True)
    is_prime_array[0] = False
    is_prime_array[1] = False
    for n in range(2, int(2_000_000**0.5)+1):
        if is_prime_array[n]:  # Not already done by lower numbers
            is_prime_array[n**2::n] = False

    # Sum primes
    print(np.sum(np.arange(2_000_000, dtype=np.int64)[is_prime_array]))  # 142913828922
