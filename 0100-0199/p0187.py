import numpy as np

from funcs import prime_sieve_int

def count_semiprimes(N):
    """Count n < N that are a product of exactly two primes p <= q."""
    # The larger factor q satisfies q <= (N-1)//2 (when p = 2), so sieving to
    # N//2 captures every prime that can appear as a factor.
    primes = prime_sieve_int(N // 2 + 1)
    count = 0
    i = 0
    while primes[i] * primes[i] < N:
        p = primes[i]
        # Count primes q with p <= q <= (N-1)//p. searchsorted gives the number
        # of primes <= that bound; subtract the i primes that are below p.
        hi = (N - 1) // p
        count += int(np.searchsorted(primes, hi, side="right")) - i
        i += 1
    return count

if __name__ == "__main__":
    print(count_semiprimes(10**8))  # 17427258
