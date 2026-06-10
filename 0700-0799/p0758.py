MOD = 10**9 + 7

def mersenne_bezout_sum(u, v):
    """T = |x| + |y| (mod MOD) for the minimal Bezout pair of
    a = 2^u - 1, b = 2^v - 1 (u < v, gcd(u, v) = 1): a x + b y = 1 with
    |x| < b/2, |y| < a/2.

    Euclid on Mersenne numbers mirrors Euclid on exponents:
    M_e0 mod M_e1 = M_(e0 mod e1), with true quotient
        Q = sum_(j < t) 2^(e2 + j e1),  t = e0 // e1,  e2 = e0 mod e1,
    a geometric series evaluated mod MOD (with care when 2^e1 = 1 mod MOD).
    The Bezout coefficient signs alternate, so their magnitudes follow
    m_new = m_prev2 + Q * m_prev1 and can be tracked mod MOD directly.
    Stop at remainder exponent 1 (value M_1 = 1 = gcd)."""
    e0, e1 = v, u
    # remainder r_i = alpha_i * a + beta_i * b (magnitudes, mod MOD)
    a0, b0 = 0, 1  # r0 = b = M_v
    a1, b1 = 1, 0  # r1 = a = M_u
    while e1 != 1:
        t, e2 = divmod(e0, e1)
        r = pow(2, e1, MOD)
        if r == 1:
            q = t % MOD * pow(2, e2, MOD) % MOD
        else:
            q = (
                pow(2, e2, MOD)
                * (pow(r, t, MOD) - 1)
                % MOD
                * pow(r - 1, MOD - 2, MOD)
                % MOD
            )
        a0, b0, a1, b1 = a1, b1, (a0 + q * a1) % MOD, (b0 + q * b1) % MOD
        e0, e1 = e1, e2
    return (a1 + b1) % MOD

def solve(limit):
    """Sum of P(2^(p^5) - 1, 2^(q^5) - 1) over primes p < q < limit, mod MOD.

    The pouring puzzle with buckets a, b, a + b has exactly two productive
    cyclic strategies (verified optimal against BFS on thousands of pairs);
    counting their pours and simplifying the four +-1 stopping branches with
    the Bezout relation collapses everything to
        P(a, b) = 2 (|x| + |y|) - 2,
    the minimal Bezout magnitudes of a x + b y = 1 - also verified against
    BFS for every coprime pair with a in [3, 60), b < 140, and reproducing
    P(3,5) = 4, P(7,31) = 20, P(1234,4321) = 2780.
    """
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False
    primes = [i for i in range(limit) if sieve[i]]
    total = 0
    for i, p in enumerate(primes):
        for q in primes[i + 1 :]:
            t = mersenne_bezout_sum(p**5, q**5)
            total = (total + 2 * t - 2) % MOD
    return total

if __name__ == "__main__":
    # Cross-check the modular exponent-Euclid against exact arithmetic.
    for u, v in [(2, 3), (3, 5), (5, 7), (5, 13), (31, 64), (97, 125), (243, 3125)]:
        a, b = 2**u - 1, 2**v - 1
        x = pow(a, -1, b)
        if x > b - x:
            x -= b
        y = (1 - a * x) // b
        assert mersenne_bezout_sum(u, v) == (abs(x) + abs(y)) % MOD, (u, v)
    print(solve(1000))  # 331196954
