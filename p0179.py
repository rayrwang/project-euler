import numpy as np

from funcs import divisor_count_sieve

if __name__ == "__main__":
    N = 10**7
    # d[k] = number of divisors of k, sieved in O(N log N).
    d = divisor_count_sieve(N + 1)
    # Count n with 1 < n < N where d(n) == d(n + 1); n ranges over 2..N-1.
    print(int(np.count_nonzero(d[2:N] == d[3:N + 1])))  # 986262
