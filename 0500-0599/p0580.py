"""Project Euler problem 580: Squarefree Hilbert Numbers.

Hilbert numbers are the positive integers congruent to 1 mod 4; a Hilbert
number is squarefree (in the Hilbert sense) if no square of a Hilbert
number larger than 1 divides it.  Count them below 10^16.

Characterisation: for odd n write s = prod p^floor(a_p / 2), the square
root of the largest square dividing n.  A Hilbert square h^2 divides n
exactly when h divides s, so n is Hilbert-squarefree iff s has no divisor
congruent to 1 mod 4 other than 1.  Any prime p = 1 mod 4 in s is such a
divisor, and any two (not necessarily distinct) primes = 3 mod 4 in s
multiply to one, so the only admissible s are s = 1 and s = q for a
single prime q = 3 mod 4.  Hence n is Hilbert-squarefree iff n is
ordinarily squarefree, or n = q^e m with e in {2, 3}, q = 3 mod 4 prime,
and m squarefree and coprime to q.  (This matches the examples: 117 =
3^2 * 13 has s = 3, while 441 = 3^2 7^2 has s = 21 and 21^2 | 441.)

Counting: squarefree m <= x with m = r mod 4 is a Moebius sum over odd d,
G_r(x) = sum mu(d) #(t <= x / d^2, t = r mod 4), since d odd makes d^2 = 1
mod 4.  Coprimality to q peels off one factor of q at a time with the
residue twisting by q = 3 mod 4 each level.  Part A is G_1(N - 1); part B
sums over primes q = 3 mod 4 the counts for e = 2 (m = 1 mod 4) and e = 3
(m = 3 mod 4, since q^3 = 3 mod 4).  Total work is about
sum over q of sqrt(N) / q = O(sqrt(N) log log N) ~ 1.5 * 10^8 sieve
lookups; the cube bound q^3 <= x is tested as q <= x // q^2 to avoid
int64 overflow.

Verified: a direct sieve over Hilbert squares for N = 10^4..10^6, the
given count 2327192 below 10^7, and the solver-posted reference ladder
C(10^8) through C(10^15).
"""

import numpy as np
from numba import njit


@njit(cache=True)
def mobius_sieve(limit):
    mu = np.ones(limit + 1, np.int8)
    is_comp = np.zeros(limit + 1, np.uint8)
    primes = np.empty(6_000_000, np.int64)
    npr = 0
    for i in range(2, limit + 1):
        if not is_comp[i]:
            primes[npr] = i
            npr += 1
            mu[i] = -1
        for t in range(npr):
            p = primes[t]
            if i * p > limit:
                break
            is_comp[i * p] = 1
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu, primes[:npr]


@njit(cache=True, inline="always")
def cnt_r(y, r):
    """#{t in [1, y]: t = r mod 4} for r in {1, 3}."""
    return (y + 4 - r) // 4


@njit(cache=True)
def g_r(x, r, mu):
    """#{m <= x: m squarefree, m = r mod 4}."""
    tot = np.int64(0)
    d = 1
    while d * d <= x:
        if mu[d]:
            tot += mu[d] * cnt_r(x // (d * d), r)
        d += 2
    return tot


@njit(cache=True)
def sf_coprime(x, r, q, mu):
    """#{m <= x: squarefree, m = r mod 4, gcd(m, q) = 1} for q = 3 mod 4."""
    tot = np.int64(0)
    sign = np.int64(1)
    while x >= 1:
        tot += sign * g_r(x, r, mu)
        sign = -sign
        r = (3 * r) % 4
        x //= q
    return tot


@njit(cache=True)
def count(n_excl, mu, primes):
    """Number of squarefree Hilbert numbers below n_excl."""
    x = n_excl - 1
    total = g_r(x, 1, mu)
    for t in range(len(primes)):
        q = primes[t]
        if q * q > x:
            break
        if q % 4 != 3:
            continue
        total += sf_coprime(x // (q * q), 1, q, mu)
        if q <= x // (q * q):  # q^3 <= x, overflow-safe
            total += sf_coprime(x // (q * q) // q, 3, q, mu)
    return total


def brute(n_excl: int) -> int:
    sf = np.ones(n_excl, np.uint8)
    h = 5
    while h * h < n_excl:
        sf[h * h :: h * h] = 0
        h += 4
    idx = np.arange(n_excl)
    return int(sf[(idx % 4 == 1) & (idx > 0)].sum())


def main() -> None:
    mu, primes = mobius_sieve(100_000_001)
    for ne in (10**4, 10**5, 10**6):
        assert brute(ne) == count(ne, mu, primes), ne
    assert count(10**7, mu, primes) == 2327192  # given
    # solver-posted reference values
    assert count(10**10, mu, primes) == 2327212928
    assert count(10**13, mu, primes) == 2327213144648
    assert count(10**15, mu, primes) == 232721314792035

    print(count(10**16, mu, primes))  # 2327213148095366


if __name__ == "__main__":
    main()
