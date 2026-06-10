"""Project Euler 956: Super Duper Sum.

n* = prod_{i<=n} i$ = prod_{j<=n} (j!)^(n+1-j), so the exponent of a prime p
in 1000* is sum_{j=1}^{1000} (1001 - j) v_p(j!) with Legendre's formula; only
the 168 primes below 1000 occur.

Selecting divisors d with Omega(d) divisible by m is a roots-of-unity filter:

    D(n, m) = (1/m) sum_{j=0}^{m-1} prod_{p^e || n} sum_{i=0}^{e} (w^j p)^i,

since each divisor d contributes d w^{j Omega(d)}. The modulus 999999001 is
prime and 999999000 is divisible by 1000, so F_MOD contains an element w of
exact order 1000 (a power of a primitive root) and the filter identity
sum_j w^{jk} = m [m | k] holds in F_MOD. Each inner sum is a geometric series
evaluated with one modular exponentiation (or e + 1 when w^j p == 1 mod MOD).

Verified: D(24, 3) = 21 and D(6*, 6) = 6368195719791280 computed exactly by a
DP over Omega residues, both matching the filter. Total work is 1000 x 168
geometric sums, under a second.
"""

MOD = 999999001
MOD_FACTORS = (2, 3, 5, 7, 11, 13, 37)  # prime factors of MOD - 1


def primes_below(n: int) -> list[int]:
    sieve = bytearray([1]) * n
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = bytearray(len(sieve[i * i :: i]))
    return [i for i in range(n) if sieve[i]]


def primitive_root() -> int:
    g = 2
    while any(pow(g, (MOD - 1) // q, MOD) == 1 for q in MOD_FACTORS):
        g += 1
    return g


def vp_factorial(p: int, j: int) -> int:
    v, q = 0, p
    while q <= j:
        v += j // q
        q *= p
    return v


def solve(n: int, m: int) -> int:
    exps = {
        p: sum((n + 1 - j) * vp_factorial(p, j) for j in range(1, n + 1))
        for p in primes_below(n + 1)
    }
    w = pow(primitive_root(), (MOD - 1) // m, MOD)
    total = 0
    for j in range(m):
        wj = pow(w, j, MOD)
        prod = 1
        for p, e in exps.items():
            x = wj * p % MOD
            if x == 1:
                s = (e + 1) % MOD
            else:
                s = (pow(x, e + 1, MOD) - 1) * pow(x - 1, MOD - 2, MOD) % MOD
            prod = prod * s % MOD
        total = (total + prod) % MOD
    return total * pow(m, MOD - 2, MOD) % MOD


print(solve(1000, 1000))  # 882086212
