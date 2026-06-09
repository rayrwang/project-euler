import numba

from funcs import prime_sieve_int, reverse_bounded, is_prime

@numba.jit(cache=True)
def _isqrt_exact(n):
    r = int(n**0.5)
    for c in (r - 1, r, r + 1):
        if c >= 0 and c * c == n:
            return c
    return -1

@numba.jit(cache=True)
def sum_first_50(primes):
    total = 0
    count = 0
    for i in range(len(primes)):
        sq = primes[i] * primes[i]
        rev = reverse_bounded(sq)
        if rev != sq:                 # not a palindrome
            root = _isqrt_exact(rev)  # reverse must be a perfect square...
            if root > 0 and is_prime(root):  # ...of a prime
                total += sq
                count += 1
                if count == 50:
                    return total
    return -1

if __name__ == "__main__":
    primes = prime_sieve_int(32_000_000)  # the 50th has prime root ~3.11e7
    print(sum_first_50(primes))  # 3807504276997394
