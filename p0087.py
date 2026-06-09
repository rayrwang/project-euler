import numba
import numpy as np

from funcs import prime_sieve_int

@numba.jit(cache=True)
def count_triples(primes, limit):
    reachable = np.zeros(limit, dtype=np.bool_)
    for c in primes:
        c4 = c**4
        if c4 >= limit:
            break
        for b in primes:
            b3 = b**3
            if c4 + b3 >= limit:
                break
            base = c4 + b3
            for a in primes:
                n = base + a * a
                if n >= limit:
                    break
                reachable[n] = True
    return int(reachable.sum())

if __name__ == "__main__":
    LIMIT = 50_000_000
    primes = prime_sieve_int(7072)  # square roots go up to 7071
    print(count_triples(primes, LIMIT))  # 1097343
