import heapq

from funcs import prime_sieve_int

MOD = 500500507

if __name__ == "__main__":
    n = 500500  # need 2^500500 divisors, i.e. 500500 doublings

    # The smallest number with 2^n divisors is the product of the n smallest
    # entries of the table {p^(2^k)} (p prime, k>=0): each such factor doubles
    # the divisor count, since it lifts an exponent e -> 2e+1. Greedily take the
    # n smallest with a min-heap, pushing the square p^(2^(k+1)) after each pop.
    # The answer never needs a prime beyond the 500500th (7376507).
    primes = prime_sieve_int(7_400_001)[:n]
    heap = [(int(p), int(p) % MOD) for p in primes]
    heapq.heapify(heap)

    result = 1
    for _ in range(n):
        value, value_mod = heapq.heappop(heap)
        result = result * value_mod % MOD
        heapq.heappush(heap, (value * value, value_mod * value_mod % MOD))

    print(result)  # 35407281
