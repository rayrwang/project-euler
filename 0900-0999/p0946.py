"""Project Euler 946: Continued Fraction Fraction.

Gosper's continued-fraction arithmetic computes the continued fraction of a
Mobius transform beta = (2 alpha + 3) / (3 alpha + 2) directly from the
continued fraction of alpha, never touching the real numbers themselves.
The state is the integer matrix of the transform applied to the not-yet-read
tail t of alpha's expansion, which always lies in (1, infinity):

    beta_tail = (p t + r) / (q t + s).

Ingesting the next term a of alpha replaces the matrix by its product with
[[a, 1], [1, 0]]; when the floor of the value is the same at both ends of
t's range (q >= 1, q + s >= 1 and floor(p/q) = floor((p+r)/(q+s))), that
floor is the next coefficient of beta, which is emitted by subtracting and
inverting: the matrix becomes [[q, s], [p - q0 q, r - q0 s]]. Both endpoint
floors use exact integer floor division, so the test is exact; since beta
is irrational the interval keeps shrinking and the process never stalls.
The determinant stays +-5 throughout and all entries remain tiny because
alpha's terms are 1 or 2, so 64-bit arithmetic suffices.

Alpha's terms are produced by a tiny state machine - a 2, then runs of 1's
whose lengths are the consecutive primes 2, 3, 5, ... - consuming roughly
one input term per output term, so primes up to a few hundred thousand
cover 10^8 coefficients. Verified against the given first ten coefficients
[0; 1, 5, 6, 16, 9, 1, 10, 16, 11] (sum 75) and against mpmath's continued
fraction expansion of beta computed at very high precision for the first
3000 coefficients.
"""

import numba
import numpy as np

N_TERMS = 10**8


def primes_upto(n):
    sieve = np.ones(n + 1, np.bool_)
    sieve[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    return np.flatnonzero(sieve).astype(np.int64)


@numba.njit(cache=True)
def sum_beta_terms(n_terms, primes):
    # state: beta_tail = (p t + r) / (q t + s), t = unread tail of alpha
    p, r = np.int64(2), np.int64(3)
    q, s = np.int64(3), np.int64(2)
    # alpha input state machine: first term 2, then runs of 1's of prime
    # lengths separated by single 2's
    prime_idx = 0
    ones_left = np.int64(0)  # 1's remaining in the current run
    first = True
    emitted = 0
    total = np.int64(0)
    while emitted < n_terms:
        # try to emit
        if q >= 1 and q + s >= 1:
            f1 = p // q
            f2 = (p + r) // (q + s)
            if f1 == f2:
                total += f1
                emitted += 1
                p, r, q, s = q, s, p - f1 * q, r - f1 * s
                continue
        # ingest the next term of alpha
        if first:
            a = np.int64(2)
            first = False
            ones_left = primes[0]
        elif ones_left > 0:
            a = np.int64(1)
            ones_left -= 1
        else:
            a = np.int64(2)
            prime_idx += 1
            if prime_idx >= len(primes):
                return np.int64(-1)  # prime supply exhausted
            ones_left = primes[prime_idx]
        # M <- M * [[a, 1], [1, 0]]
        p, r = p * a + r, p
        q, s = q * a + s, q
    return total


def solve() -> int:
    primes = primes_upto(3 * 10**6)
    return int(sum_beta_terms(N_TERMS, primes))


if __name__ == "__main__":
    print(solve())  # 585787007
