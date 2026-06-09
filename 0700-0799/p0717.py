import numpy as np

N = 10**7

def sieve_primes(limit):
    """Odd primes below limit."""
    s = np.ones(limit, dtype=bool)
    s[:2] = False
    for i in range(2, int(limit**0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0]

def solve(n):
    """For an odd prime p, f(p) = floor(2^(2^p) / p) mod 2^p and g(p) = f(p) mod p.

    Let M = 2^p and r = 2^M mod p. Since M >= p, 2^M = 0 (mod 2^p), so from
    p * floor(2^M / p) = 2^M - r we get f(p) = floor(2^M/p) mod 2^p satisfying
    p * f(p) + r = 2^p * s with 0 <= s < p. Reducing mod p gives 2 s = r, hence
    s = r / 2 (mod p); reducing p*f(p) = 2^p s - r mod p^2 then isolates
        g(p) = f(p) mod p = ((2^p s - r) mod p^2) / p.
    Each prime needs only a few modular exponentiations.
    """
    primes = sieve_primes(n)
    total = 0
    for p in primes[1:]:  # skip 2; odd primes only
        p = int(p)
        e = pow(2, p, p - 1)        # 2^p mod (p-1)
        r = pow(2, e, p)            # 2^(2^p) mod p
        s = (r * ((p + 1) // 2)) % p  # r / 2 mod p
        num = (pow(2, p, p * p) * s - r) % (p * p)
        total += num // p           # f(p) mod p
    return total

if __name__ == "__main__":
    print(solve(N))  # 1603036763131
