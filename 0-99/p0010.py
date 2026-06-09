
import numpy as np

from funcs import prime_sieve_int

if __name__ == "__main__":
    print(np.sum(prime_sieve_int(2_000_000)))  # 142913828922
