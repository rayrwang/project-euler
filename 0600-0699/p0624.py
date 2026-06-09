"""Project Euler Problem 624: Two Heads Are Better Than One.

The first HH ends at toss m with probability F(m-1) / 2^m (Fibonacci,
F(1) = F(2) = 1): sequences of length m - 2 with no HH followed by THH are
counted by the Fibonacci-shaped no-two-consecutive-heads count.  Hence

    P(n) = sum_{k >= 1} F(kn - 1) / 2^{kn}.

Using Binet, F(m) = (phi^m - psi^m) / sqrt(5), the sum splits into two
geometric series.  With u = (phi / 2)^n and v = (psi / 2)^n,

    P(n) = ( u / (phi (1 - u)) - v / (psi (1 - v)) ) / sqrt(5).

P(n) is rational, and Q(P(n), p) is just its residue mod p taken in
1..p-1, so evaluate the closed form in GF(p).  This works because 5 is a
quadratic residue mod p = 10^9 + 9 (and mod 109 for the given checks), so
sqrt(5), phi and psi all exist in the field.  The square root is found with
Tonelli-Shanks.

Checks: P(2) = 3/5, P(3) = 9/31 (so Q(P(2), 109) = 66, Q(P(3), 109) = 46).
"""


def sqrt_mod(a: int, p: int) -> int:
    """Tonelli-Shanks square root of a modulo prime p."""
    assert pow(a, (p - 1) // 2, p) == 1
    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c, t, r = s, pow(z, q, p), pow(a, q, p), pow(a, (q + 1) // 2, p)
    while t != 1:
        t2, i = t, 0
        while t2 != 1:
            t2 = t2 * t2 % p
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        m, c = i, b * b % p
        t, r = t * c % p, r * b % p
    return r


def Q(n: int, p: int) -> int:
    """P(n) reduced modulo p, as the smallest positive representative."""
    r5 = sqrt_mod(5, p)
    inv2 = pow(2, p - 2, p)
    phi = (1 + r5) * inv2 % p
    psi = (1 - r5) * inv2 % p
    u = pow(phi * inv2 % p, n, p)
    v = pow(psi * inv2 % p, n, p)
    term_u = u * pow(phi * (1 - u) % p, p - 2, p) % p
    term_v = v * pow(psi * (1 - v) % p, p - 2, p) % p
    return (term_u - term_v) * pow(r5, p - 2, p) % p


if __name__ == "__main__":
    assert Q(2, 109) == 66, Q(2, 109)
    assert Q(3, 109) == 46, Q(3, 109)
    # P(2) = 3/5 and P(3) = 9/31 against a big prime:
    big = 10**9 + 9
    assert Q(2, big) == 3 * pow(5, big - 2, big) % big
    assert Q(3, big) == 9 * pow(31, big - 2, big) % big
    print(Q(10**18, big))  # 984524441
