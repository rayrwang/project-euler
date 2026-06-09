import numba

from funcs import prime_sieve_int

@numba.jit(cache=True)
def S(N, primes):
    """Sum over prime pairs p < q (with p*q <= N) of the largest p^a * q^b <= N."""
    total = 0
    n = len(primes)
    for i in range(n):
        p = primes[i]
        if p * p > N:          # then p*q > p^2 > N for every q > p
            break
        for j in range(i + 1, n):
            q = primes[j]
            if p * q > N:       # primes increase, so no further q works
                break
            # Largest p^a * q^b <= N with a, b >= 1.
            best = 0
            pa = p
            while pa * q <= N:
                rem = N // pa
                qb = q
                while qb * q <= rem:
                    qb *= q
                prod = pa * qb
                if prod > best:
                    best = prod
                pa *= p
            total += best
    return total

if __name__ == "__main__":
    N = 10_000_000
    primes = prime_sieve_int(N // 2 + 1)
    print(S(N, primes))  # 11109800204052
