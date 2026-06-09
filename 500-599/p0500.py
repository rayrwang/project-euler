import heapq

from funcs import prime_sieve_int

def smallest_2_pow_divisors(n: int, mod: int) -> int:
    """Smallest number with 2**n divisors, modulo `mod`.

    The divisor count is the product of (exponent + 1) over the prime
    factorisation. To reach exactly 2**n divisors every (exponent + 1) must
    itself be a power of two, so each exponent has the form 2**k - 1. Doubling
    the divisor count means either introducing a fresh prime (exponent 0 -> 1)
    or promoting a prime sitting at exponent 2**k - 1 up to 2**(k+1) - 1, which
    multiplies the value by the "atom" p**(2**k). We perform n such doublings,
    always spending the cheapest atom, via a min-heap.
    """
    primes = prime_sieve_int(7_500_000)  # > 500500 primes available
    result = 1
    # Heap entries: (atom_value, prime, exponent). atom_value = prime**exponent
    # is kept as an exact int so comparisons never touch floats.
    heap = [(int(primes[0]), int(primes[0]), 1)]
    next_idx = 1
    for _ in range(n):
        value, p, e = heapq.heappop(heap)
        result = (result * pow(p, e, mod)) % mod
        # Next promotion of this prime costs p**(2e) = value**2.
        heapq.heappush(heap, (value * value, p, e * 2))
        if e == 1:
            # A brand-new prime was just used; expose the next one as a candidate.
            nxt = int(primes[next_idx])
            heapq.heappush(heap, (nxt, nxt, 1))
            next_idx += 1
    return result

if __name__ == "__main__":
    print(smallest_2_pow_divisors(500500, 500500507))  # 35407281
